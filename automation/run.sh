#!/usr/bin/env bash
# ============================================================================
# Law Minded — write one article and stage it for approval.
#
# Runs on the OCI writer box (Ubuntu ARM) from cron, Fri/Sat/Sun; also runnable
# by hand any time:   ./automation/run.sh
#
# Works on the Mac too — the repo path comes from wherever this script lives,
# so nothing is hardcoded to one machine.
# ============================================================================
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOGS="$REPO/automation/logs"
PROMPT="$REPO/automation/weekly-post.md"

mkdir -p "$LOGS"
LOG="$LOGS/$(date +%Y-%m-%d-%H%M).log"

cd "$REPO"

# cron and launchd both hand over a near-empty PATH, so npm's global bin and
# Homebrew are missing unless named explicitly. cron does set HOME, but this runs
# under `set -u`, so an empty environment would abort on the reference alone.
HOME="${HOME:-$(getent passwd "$(id -un)" | cut -d: -f6)}"
export HOME
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin:${HOME}/.local/bin"

# --check validates everything the run depends on and exits without spending a
# Claude run. Use it after touching the schedule or moving the repo.
if [ "${1:-}" = "--check" ]; then
  fail=0
  for f in "$PROMPT" "$REPO/deploy/stage_draft.py" "$REPO/automation/gen_image.py"; do
    [ -r "$f" ] && echo "ok   $f" || { echo "MISSING  $f"; fail=1; }
  done
  command -v claude >/dev/null && echo "ok   claude $(claude --version)" || { echo "MISSING  claude on PATH"; fail=1; }
  command -v git >/dev/null && echo "ok   git" || { echo "MISSING  git"; fail=1; }
  claude auth status 2>/dev/null | grep -q '"loggedIn": true' \
    && echo "ok   claude authenticated" || { echo "NOT LOGGED IN  run: claude auth login"; fail=1; }
  ssh -o BatchMode=yes -o ConnectTimeout=8 ubuntu@161.118.176.94 true 2>/dev/null \
    && echo "ok   web server reachable" || { echo "UNREACHABLE  web server over ssh"; fail=1; }
  git -C "$REPO" push --dry-run -q origin HEAD:refs/heads/_check 2>/dev/null \
    && echo "ok   git push access" || { echo "NO PUSH ACCESS  check the deploy key"; fail=1; }
  [ "$fail" = 0 ] && echo "--- ready ---" || echo "--- NOT ready ---"
  exit "$fail"
fi

# The Claude auth token lives outside the repo so it never risks being commited.
# Written by hand once with `claude setup-token`; absent on the Mac, which uses
# its own interactive login instead.
if [ -f "$HOME/.claude-writer.env" ]; then
  set -a; . "$HOME/.claude-writer.env"; set +a
fi

{
  echo "=== $(date '+%Y-%m-%d %H:%M:%S') — weekly post run on $(hostname) ==="

  # Start from current main. A leftover checkout on last week's branch would
  # otherwise have the run branching off a branch.
  git checkout main
  git pull --ff-only

  # Skill must be in the list or the humanizer / seo-content / seo-schema steps
  # in the prompt silently do nothing.
  claude -p "$(cat "$PROMPT")" \
    --permission-mode acceptEdits \
    --allowedTools 'Read,Write,Edit,Glob,Grep,WebSearch,WebFetch,Bash,Skill'

  echo "=== exit $? at $(date '+%H:%M:%S') ==="
} >>"$LOG" 2>&1

# Keep the last 30 runs; the logs hold full article drafts and get large.
ls -1t "$LOGS"/*.log 2>/dev/null | tail -n +31 | xargs -r rm --
