#!/usr/bin/env bash
# ============================================================================
# Every connection this automation depends on, checked in one place.
#
#     ./automation/healthcheck.sh
#
# Written because almost every failure here has been silent: a dead weekly run,
# a mail password that stopped working, a status reporter whose errors went to
# /dev/null. Each was invisible until someone happened to look. This is the
# looking, in one command.
#
# Exits non-zero if anything is down, so it can be wired to an alert later.
# ============================================================================
set -uo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WEB=ubuntu@161.118.176.94
FAIL=0

ok()   { printf '  \033[32m✓\033[0m %-34s %s\n' "$1" "${2:-}"; }
bad()  { printf '  \033[31m✗\033[0m %-34s %s\n' "$1" "${2:-}"; FAIL=1; }
warn() { printf '  \033[33m!\033[0m %-34s %s\n' "$1" "${2:-}"; }

echo "── Writer box ──────────────────────────────────────────────"
[ "$(systemctl is-active lm-bot)" = active ] \
  && ok "telegram bot" "$(systemctl show lm-bot -p NRestarts --value) restarts" \
  || bad "telegram bot" "NOT RUNNING"

# Anchored to the start of the command line. `pgrep -f "claude -p"` also matches
# any shell or ssh wrapper that merely mentions the string — including the command
# doing the checking, which reported a job running when the box was idle.
if ps -eo args | grep -q "^claude -p"; then
  warn "claude job" "one running ($(ps -eo etime,args | grep "^ *[0-9:]* claude -p" | head -1 | awk '{print $1}'))"
else
  ok "claude job" "idle"
fi

claude auth status 2>/dev/null | grep -q '"loggedIn": true' \
  && ok "claude auth" "logged in" || bad "claude auth" "NOT LOGGED IN"

command -v claude >/dev/null && ok "claude cli" "$(claude --version 2>/dev/null)" \
  || bad "claude cli" "missing"

for s in humanizer seo-content seo-schema; do
  [ -f "$HOME/.claude/skills/$s/SKILL.md" ] && ok "skill: $s" "installed" \
    || bad "skill: $s" "MISSING — runs will silently approximate it"
done

echo
echo "── Connections out ─────────────────────────────────────────"
git -C "$REPO" push --dry-run -q origin HEAD:refs/heads/_health 2>/dev/null \
  && ok "github push" "deploy key works" || bad "github push" "DENIED"

ssh -o BatchMode=yes -o ConnectTimeout=8 "$WEB" true 2>/dev/null \
  && ok "ssh → web server" "reachable" || bad "ssh → web server" "UNREACHABLE"

TG=$(grep '^TELEGRAM_BOT_TOKEN=' "$REPO/.env" 2>/dev/null | cut -d= -f2-)
if [ -n "$TG" ] && curl -s -m 12 "https://api.telegram.org/bot$TG/getMe" | grep -q '"ok":true'; then
  ok "telegram api" "bot reachable"
else
  bad "telegram api" "getMe failed"
fi

if [ -n "${PEXELS_API_KEY:-$(grep '^PEXELS_API_KEY=' "$REPO/.env" 2>/dev/null | cut -d= -f2-)}" ]; then
  python3 -c "
import sys; sys.path.insert(0, '$REPO/automation')
import gen_image
sys.exit(0 if gen_image.fetch_stock('office desk') else 1)
" 2>/dev/null && ok "pexels images" "fetching" || bad "pexels images" "key set but fetch failed"
else
  bad "pexels images" "no key"
fi

python3 -c "
import sys; sys.path.insert(0, '$REPO/automation')
import gen_image
try:
    gen_image.generate('a plain grey square')
    print('ok')
except SystemExit as e:
    print('fail', e)
" 2>/dev/null | grep -q '^ok' \
  && ok "gemini images" "credits available" \
  || warn "gemini images" "unavailable (credits) — falls back to Pexels"

echo
echo "── Live site ───────────────────────────────────────────────"
for path in / /blogs /sitemap.xml; do
  code=$(curl -s -o /dev/null -m 15 -w '%{http_code}' "https://lawminded.in$path")
  [ "$code" = 200 ] && ok "site $path" "$code" || bad "site $path" "$code"
done
code=$(curl -s -o /dev/null -m 15 -w '%{http_code}' https://lawminded.in/admin/automation)
[ "$code" = 302 ] && ok "dashboard" "302 → login (protected)" \
  || bad "dashboard" "$code — expected a redirect to login"

echo
echo "── Web server ──────────────────────────────────────────────"
ssh -o BatchMode=yes -o ConnectTimeout=10 "$WEB" '
  [ "$(systemctl is-active lawminded)" = active ] && echo "OK app" || echo "BAD app"
  [ "$(systemctl is-active nginx)" = active ] && echo "OK nginx" || echo "BAD nginx"
  cd ~/lawminded 2>/dev/null || exit
  ./venv/bin/python - <<PY
import os, smtplib, sqlite3, json, sys
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
load_dotenv("/home/ubuntu/lawminded/.env")
try:
    s = smtplib.SMTP(os.getenv("MAIL_SERVER"), int(os.getenv("MAIL_PORT", 587)), timeout=20)
    s.ehlo(); s.starttls(); s.ehlo()
    s.login(os.getenv("MAIL_USERNAME"), os.getenv("MAIL_PASSWORD")); s.quit()
    print("OK smtp")
except Exception as e:
    print("BAD smtp", repr(e)[:60])
c = sqlite3.connect("/home/ubuntu/lawminded-data/lawminded.db")
print("OK db", c.execute("SELECT COUNT(*) FROM articles WHERE published=1").fetchone()[0],
      "published,", c.execute("SELECT COUNT(*) FROM subscribers").fetchone()[0], "subscribers")
try:
    d = json.load(open("/home/ubuntu/lawminded-data/writer-status.json"))
    age = datetime.now(timezone(timedelta(hours=5, minutes=30))) - datetime.fromisoformat(d["generated_at"])
    mins = int(age.total_seconds() // 60)
    print(("OK" if mins < 12 else "BAD"), "snapshot", f"{mins} min old")
except Exception as e:
    print("BAD snapshot", repr(e)[:50])
PY' 2>/dev/null | while read -r status name rest; do
  case "$status" in
    OK)  ok  "$name" "$rest" ;;
    BAD) bad "$name" "$rest" ;;
  esac
done

echo
echo "── Schedules ───────────────────────────────────────────────"
n=$(crontab -l 2>/dev/null | grep -c 'run.sh')
[ "$n" -eq 3 ] && ok "weekly runs" "Fri 08:00, Sat/Sun 12:00 IST" \
  || bad "weekly runs" "$n cron entries, expected 3"
crontab -l 2>/dev/null | grep -q report_status \
  && ok "status reporter" "every 5 min" || bad "status reporter" "no cron entry"
ssh -o BatchMode=yes -o ConnectTimeout=10 "$WEB" 'crontab -l 2>/dev/null | grep -c publish_due' 2>/dev/null \
  | grep -q '^1$' && ok "scheduled publisher" "daily 07:00 IST" \
  || bad "scheduled publisher" "missing on the web server"

q=$(sed -n '/## Pending/,/## Written/p' "$REPO/automation/queue.md" 2>/dev/null | grep -c '^- \[ \]')
ok "queued topics" "$q pending"
[ -s "$REPO/automation/.bot_retry.json" ] \
  && warn "held requests" "$(python3 -c "import json;print(len(json.load(open('$REPO/automation/.bot_retry.json'))))" 2>/dev/null || echo '?') waiting on quota" \
  || ok "held requests" "none"

echo
[ "$FAIL" = 0 ] && echo "  ALL GREEN" || echo "  SOMETHING IS DOWN — see the ✗ lines above"
exit "$FAIL"
