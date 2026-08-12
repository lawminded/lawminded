#!/usr/bin/env python3
"""Stage a weekly draft on the live server and send it to Telegram for approval.

Runs ON the server, not on the Mac, for one reason: the preview link is signed
with SECRET_KEY, which lives only in the server's .env. Reads one article as
JSON on stdin, inserts it as published=0 (already invisible to /article), and
messages a signed link. Nothing is public until someone taps Publish.

    ssh ubuntu@server 'cd ~/lawminded && ./venv/bin/python deploy/stage_draft.py' < article.json

The JSON needs: title, slug, category, act, read_time, summary, content.
Optional: sources — a list of URLs, shown in the message but not stored.
"""
import json
import os
import sqlite3
import sys
import urllib.parse
import urllib.request

from dotenv import load_dotenv
from itsdangerous import URLSafeSerializer

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env'))

DB_PATH = os.getenv('DATABASE_PATH', os.path.expanduser('~/lawminded-data/lawminded.db'))
SITE_URL = os.getenv('SITE_URL', 'https://lawminded.in')

REQUIRED = ('title', 'slug', 'category', 'act', 'read_time', 'summary', 'content')


def sign(slug):
    """The signed preview token. Must stay identical to _draft_serializer in
    app.py — same key, same salt. test_draft.py asserts the two agree."""
    secret = os.getenv('SECRET_KEY')
    if not secret:
        sys.exit('SECRET_KEY is not set — cannot sign a preview link.')
    return URLSafeSerializer(secret, salt='lm-draft').dumps(slug)


def stage(article):
    missing = [k for k in REQUIRED if not article.get(k)]
    if missing:
        sys.exit(f'Article is missing required fields: {", ".join(missing)}')

    conn = sqlite3.connect(DB_PATH)
    live = conn.execute('SELECT published FROM articles WHERE slug=?',
                        (article['slug'],)).fetchone()
    if live and live[0] == 1:
        conn.close()
        sys.exit(f'{article["slug"]} is already published — refusing to overwrite it.')

    # Re-staging the same slug replaces the pending draft rather than erroring,
    # so a re-run after a failed send is safe.
    conn.execute('DELETE FROM articles WHERE slug=? AND published=0', (article['slug'],))
    conn.execute(
        'INSERT INTO articles (title, slug, category, act, read_time, summary, '
        'content, published) VALUES (?,?,?,?,?,?,?,0)',
        tuple(article[k] for k in REQUIRED))
    conn.commit()
    conn.close()
    return f'{SITE_URL}/draft/{article["slug"]}?t={sign(article["slug"])}'


def notify(article, url):
    """Send the draft to Telegram. Absence of credentials is not fatal — the
    draft is staged either way, and the link is printed to stdout."""
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    if not (token and chat_id):
        print('TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID not set — skipping the message.',
              file=sys.stderr)
        return False

    def esc(s):
        return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    lines = [f'<b>{esc(article["title"])}</b>',
             '',
             esc(article['summary']),
             '',
             f'{esc(article["category"])} · {esc(article["act"])} · {esc(article["read_time"])}']
    sources = article.get('sources') or []
    if sources:
        lines += ['', '<b>Sources</b>'] + [esc(s) for s in sources]
    lines += ['', f'<a href="{esc(url)}">Read the draft and publish</a>']

    body = urllib.parse.urlencode({
        'chat_id': chat_id,
        'text': '\n'.join(lines),
        'parse_mode': 'HTML',
        'disable_web_page_preview': 'true',
    }).encode()
    req = urllib.request.Request(
        f'https://api.telegram.org/bot{token}/sendMessage', data=body)
    with urllib.request.urlopen(req, timeout=20) as r:
        if not json.load(r).get('ok'):
            sys.exit('Telegram rejected the message.')
    return True


if __name__ == '__main__':
    art = json.load(sys.stdin)
    link = stage(art)
    sent = notify(art, link)
    print(link)
    print('Staged as a draft.' + (' Sent to Telegram.' if sent else ''))
