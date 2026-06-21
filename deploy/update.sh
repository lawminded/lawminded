#!/usr/bin/env bash
# ============================================================================
# Law Minded — deploy the latest code to the server.
# After you push changes to GitHub, SSH in and run:   ./deploy/update.sh
# (Adding articles via the admin panel does NOT need this — that's instant.)
# ============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_DIR="$(dirname "$SCRIPT_DIR")"
cd "$APP_DIR"

echo "==> Pulling latest code…"
git pull --ff-only

echo "==> Updating dependencies…"
./venv/bin/pip install -r requirements.txt

echo "==> Restarting app…"
sudo systemctl restart lawminded

echo "✅ Deployed."
sudo systemctl --no-pager --lines=0 status lawminded | head -4
