#!/usr/bin/env bash
# ============================================================================
# Law Minded — one-time server setup for an Oracle Cloud (Ubuntu) VM.
# Run it from inside the cloned repo:   ./deploy/setup.sh
# Safe to re-run; it won't overwrite your existing .env.
# ============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_DIR="$(dirname "$SCRIPT_DIR")"
APP_USER="$(whoami)"
DATA_DIR="$HOME/lawminded-data"
SERVICE_NAME="lawminded"

echo "==> App dir:  $APP_DIR"
echo "==> User:     $APP_USER"
echo "==> Data dir: $DATA_DIR"
echo

# ── 1. System packages ──────────────────────────────────────────────────────
echo "==> Installing system packages (python, nginx, certbot, git)…"
sudo apt-get update -y
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y \
  python3-venv python3-pip nginx git curl \
  certbot python3-certbot-nginx

# ── 2. Swap file (1 GB VM runs smoother with a little swap) ─────────────────
if [ ! -f /swapfile ]; then
  echo "==> Creating a 1 GB swap file…"
  sudo fallocate -l 1G /swapfile 2>/dev/null || sudo dd if=/dev/zero of=/swapfile bs=1M count=1024
  sudo chmod 600 /swapfile
  sudo mkswap /swapfile
  sudo swapon /swapfile
  grep -q '/swapfile' /etc/fstab || echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab >/dev/null
fi

# ── 3. Python virtualenv + dependencies ─────────────────────────────────────
echo "==> Setting up Python virtualenv…"
cd "$APP_DIR"
[ -d venv ] || python3 -m venv venv
./venv/bin/pip install --upgrade pip
./venv/bin/pip install -r requirements.txt

# ── 4. Persistent data directory (DB survives updates & reboots) ────────────
mkdir -p "$DATA_DIR"

# ── 5. .env (created once; preserved on re-runs) ────────────────────────────
if [ ! -f "$APP_DIR/.env" ]; then
  echo
  echo "==> First-time setup: creating .env"
  read -rsp "    Choose an ADMIN password (for the admin panel login): " ADMIN_PW; echo
  SECRET=$(python3 -c "import secrets; print(secrets.token_hex(32))")
  cat > "$APP_DIR/.env" <<EOF
PRODUCTION=true
SECRET_KEY=$SECRET
ADMIN_PASSWORD=$ADMIN_PW
DATABASE_PATH=$DATA_DIR/lawminded.db
# ── Optional Gmail (fill later to enable contact form + newsletter emails) ──
MAIL_USERNAME=
MAIL_PASSWORD=
CONTACT_RECEIVER=
# ── Google AdSense ──
ADSENSE_CLIENT=ca-pub-5076002954680667
ADSENSE_SLOT_TOP=8385529112
ADSENSE_SLOT_MID=8385529112
ADSENSE_SLOT_BOTTOM=8776369792
ADSENSE_SLOT_ARTICLE_TOP=2869436994
ADSENSE_SLOT_ARTICLE_BOTTOM=2869436994
EOF
  chmod 600 "$APP_DIR/.env"
  echo "==> .env created (kept private, never committed)."
else
  echo "==> .env already exists — keeping your settings."
fi

# ── 6. systemd service (always-on, auto-restart, survives reboot) ───────────
echo "==> Installing systemd service…"
sed -e "s|__APP_DIR__|$APP_DIR|g" -e "s|__APP_USER__|$APP_USER|g" \
  "$APP_DIR/deploy/gunicorn.service" | sudo tee /etc/systemd/system/$SERVICE_NAME.service >/dev/null
sudo systemctl daemon-reload
sudo systemctl enable "$SERVICE_NAME"
sudo systemctl restart "$SERVICE_NAME"

# ── 7. nginx reverse proxy ──────────────────────────────────────────────────
echo "==> Configuring nginx…"
sed -e "s|__APP_DIR__|$APP_DIR|g" \
  "$APP_DIR/deploy/nginx.conf" | sudo tee /etc/nginx/sites-available/$SERVICE_NAME >/dev/null
sudo ln -sf /etc/nginx/sites-available/$SERVICE_NAME /etc/nginx/sites-enabled/$SERVICE_NAME
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx

# ── 8. Firewall — open 80/443 (Oracle Ubuntu blocks them by default) ────────
echo "==> Opening ports 80 and 443 in the OS firewall…"
for PORT in 80 443; do
  sudo iptables -C INPUT -p tcp --dport "$PORT" -j ACCEPT 2>/dev/null \
    || sudo iptables -I INPUT -p tcp --dport "$PORT" -j ACCEPT
done
echo "iptables-persistent iptables-persistent/autosave_v4 boolean true" | sudo debconf-set-selections
echo "iptables-persistent iptables-persistent/autosave_v6 boolean true" | sudo debconf-set-selections
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y iptables-persistent
sudo netfilter-persistent save

# ── Done ────────────────────────────────────────────────────────────────────
PUBLIC_IP="$(curl -s --max-time 5 ifconfig.me || echo 'YOUR_PUBLIC_IP')"
echo
echo "============================================================"
echo " ✅ Server setup complete — app is running."
echo
echo "   Quick local check (should print HTTP/1.1 200):"
echo "     curl -I http://127.0.0.1"
echo
echo " NEXT STEPS:"
echo "   1) In your domain registrar, point DNS at this server:"
echo "        A     @     ->  $PUBLIC_IP"
echo "        A     www   ->  $PUBLIC_IP"
echo "   2) Once the domain resolves to that IP, enable free HTTPS:"
echo "        sudo certbot --nginx -d lawminded.in -d www.lawminded.in"
echo "============================================================"
