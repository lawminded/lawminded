#!/usr/bin/env python3
"""Merge any post/<slug> branch whose article is already live, then delete it.

    ./automation/merge_published.py --dry-run
    ./automation/merge_published.py

Runs hourly on the writer box. The weekly run does this too, in step 0 of
automation/weekly-post.md, but only on Friday, Saturday and Sunday. Twice now an
article has been published and its branch left unmerged for days — the CCFS
extension and the SARFAESI judgment — which means the seed file and the hero
image existed only on a branch while the article was live. A database reset in
that window loses the article, and the hand-written search title and description
never reach the site at all, because seo_meta.py ships with the code.

What it does NOT do, deliberately:

  * It never deletes a branch whose article has no row. That is the weekly run's
    "rejected" case, and telling the two apart needs judgement this script does
    not have — a branch pushed a minute before the draft is staged looks
    identical to a rejected one.
  * It never force-pushes and never resolves a conflict. On a conflict it stops,
    leaves the branch alone and says so on Telegram.

Deliberately not a Claude run: this is a lookup and a merge, it should cost
nothing, and it should keep working when the quota is gone.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
WEB = 'ubuntu@161.118.176.94'
DB = '/home/ubuntu/lawminded-data/lawminded.db'
SLUG_RE = re.compile(r'^[a-z0-9][a-z0-9-]{0,80}$')


def git(*args, cwd=REPO, check=True):
    r = subprocess.run(['git', *args], cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f'git {" ".join(args)} failed:\n{r.stderr.strip()}')
    return r.stdout.strip()


def telegram(text):
    """Only used when something needs a human. An hourly job that reports success
    is an hourly job people learn to ignore."""
    env = {}
    try:
        for line in (REPO / '.env').read_text().splitlines():
            if '=' in line:
                k, v = line.split('=', 1)
                env[k.strip()] = v.strip()
    except OSError:
        return
    token, chat = env.get('TELEGRAM_BOT_TOKEN'), env.get('TELEGRAM_CHAT_ID')
    if not (token and chat):
        return
    try:
        urllib.request.urlopen(urllib.request.Request(
            f'https://api.telegram.org/bot{token}/sendMessage',
            data=urllib.parse.urlencode(
                {'chat_id': chat, 'text': text,
                 'disable_web_page_preview': 'true'}).encode()), timeout=20)
    except Exception as e:                                    # noqa: BLE001
        print(f'could not reach Telegram: {e!r}', file=sys.stderr)


def published_slugs(slugs):
    """Ask the live database which of these slugs are published. One SSH round
    trip for all of them rather than one each."""
    if not slugs:
        return set()
    script = (
        'import sqlite3, json, sys\n'
        f'c = sqlite3.connect({DB!r})\n'
        'want = json.load(sys.stdin)\n'
        'q = ",".join("?" * len(want))\n'
        'rows = c.execute("SELECT slug FROM articles WHERE published=1 AND slug IN (%s)" % q, want)\n'
        'print(json.dumps([r[0] for r in rows]))\n')
    r = subprocess.run(
        ['ssh', '-o', 'BatchMode=yes', '-o', 'ConnectTimeout=20', WEB,
         f'/home/ubuntu/lawminded/venv/bin/python -c {shell_quote(script)}'],
        input=json.dumps(sorted(slugs)), capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        raise RuntimeError(f'could not reach the live database:\n{r.stderr.strip()}')
    return set(json.loads(r.stdout))


def shell_quote(s):
    return "'" + s.replace("'", "'\\''") + "'"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true',
                    help='say what would be merged, change nothing')
    a = ap.parse_args()

    # A weekly run does its own housekeeping and moves the checkout between
    # branches. Two of us doing that at once is how a run ends up committing to
    # the wrong branch, so stand down and try again next hour.
    if subprocess.run(['pgrep', '-f', 'automation/run.sh'],
                      capture_output=True).returncode == 0:
        print('a weekly run is in progress — skipping this hour')
        return

    git('fetch', '-q', '--prune', 'origin')
    branches = [b.strip().replace('origin/', '', 1)
                for b in git('branch', '-r', '--list', 'origin/post/*').splitlines()
                if b.strip() and '->' not in b]
    if not branches:
        print('no post/ branches')
        return

    slugs = {}
    for b in branches:
        slug = b.split('post/', 1)[1]
        # The slug is interpolated into a database query and a git ref. It comes
        # from a branch name, which anyone with push access controls.
        if SLUG_RE.match(slug):
            slugs[slug] = b
        else:
            print(f'skipping branch with an odd name: {b}')

    live = published_slugs(set(slugs))
    if not live:
        print(f'{len(slugs)} post branch(es), none published yet — nothing to do')
        return

    for slug in sorted(live):
        branch = slugs[slug]
        print(f'{slug}: published, merging {branch}')
        if a.dry_run:
            continue

        # A throwaway worktree, so a weekly run's checkout is never touched.
        with tempfile.TemporaryDirectory() as tmp:
            wt = os.path.join(tmp, 'merge')
            git('worktree', 'add', '-q', '--detach', wt, 'origin/main')
            try:
                r = subprocess.run(
                    ['git', 'merge', '--no-ff', '-m',
                     f'Merge {branch} (published)\n\n'
                     f'Merged automatically once {slug} went live, so the seed '
                     f'file, the hero image and the search title reach main '
                     f'rather than sitting on a branch behind a live article.',
                     f'origin/{branch}'],
                    cwd=wt, capture_output=True, text=True)
                if r.returncode != 0:
                    msg = (f'Could not merge {branch} automatically — it conflicts '
                           f'with main. The article is live; the branch is '
                           f'untouched and needs merging by hand.\n\n'
                           f'{(r.stdout + r.stderr).strip()[:600]}')
                    print(msg, file=sys.stderr)
                    telegram(msg)
                    continue
                git('push', '-q', 'origin', 'HEAD:main', cwd=wt)
            finally:
                git('worktree', 'remove', '--force', wt, check=False)
                git('worktree', 'prune', check=False)

        git('push', '-q', 'origin', '--delete', branch)
        print(f'{slug}: merged into main, branch deleted')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:                                    # noqa: BLE001
        print(f'merge_published failed: {e!r}', file=sys.stderr)
        telegram(f'The hourly branch-merge job failed: {e!r}')
        sys.exit(1)
