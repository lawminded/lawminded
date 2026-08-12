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
BEFORE="$(git rev-parse HEAD)"
git pull --ff-only

# Safe to run on a schedule: with nothing new pulled there is nothing to restart.
# An hourly cron entry means approved posts reach the server without anyone
# SSHing in (the article itself is already live — this brings the seed file and
# image that keep it alive across a database reset).
if [ "$BEFORE" = "$(git rev-parse HEAD)" ] && [ "${1:-}" != "--force" ]; then
  echo "✅ Already up to date — nothing to restart."
  exit 0
fi

echo "==> Updating dependencies…"
./venv/bin/pip install -r requirements.txt

echo "==> Restarting app…"
sudo systemctl restart lawminded

echo "✅ Deployed."
sudo systemctl --no-pager --lines=0 status lawminded | head -4
