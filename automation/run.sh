#!/usr/bin/env bash
# ============================================================================
# Law Minded — write one article and stage it for approval.
#
# Fired by launchd on Friday, Saturday and Sunday morning; also runnable by
# hand any time:   ./automation/run.sh
#
# Runs from the main checkout, not a worktree, because that is where .env with
# GEMINI_API_KEY lives. Output goes to automation/logs/ so a failed
# Friday can be read on Saturday.
# ============================================================================
set -euo pipefail

REPO="/Users/piyush_kundnani/LAW Minded-Claude/lawminded-v3"
LOGS="$REPO/automation/logs"
PROMPT="$REPO/automation/weekly-post.md"

mkdir -p "$LOGS"
LOG="$LOGS/$(date +%Y-%m-%d-%H%M).log"

cd "$REPO"

# launchd hands over a near-empty PATH, so /usr/local/bin is not on it.
export PATH="/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"

{
  echo "=== $(date '+%Y-%m-%d %H:%M:%S') — weekly post run ==="

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
