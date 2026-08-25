#!/usr/bin/env python3
"""Send subscribers a round-up of a month's articles.

    ./venv/bin/python deploy/send_roundup.py --month 2026-08 --dry-run
    ./venv/bin/python deploy/send_roundup.py --month 2026-08

Always read it with --dry-run first. This is the one thing here that reaches
other people's inboxes, and it cannot be recalled.

The per-article announcements handle the day-to-day; this exists for the first
send to a list that has never heard from us, and for a monthly summary if that
ever becomes wanted.
"""
import argparse
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Articles are grouped by what a reader would consider the same subject, rather
# than by publication order, which is meaningless to them.
GROUPS = [
    ('Tax, GST and personal finance', ('tax',)),
    ('Companies and LLPs', ('corp',)),
    ('Employment, MSME and contracts', ('labour', 'contracts', 'consumer',
                                        'property', 'acts', 'updates')),
]


def build(site, month):
    db = site.get_db()
    rows = db.execute(
        'SELECT title, slug, summary, category, created_at FROM articles '
        'WHERE published=1 AND created_at >= ? AND created_at < ? '
        'ORDER BY created_at',
        (f'{month}-01', f'{month}-32')).fetchall()
    subscriber_count = db.execute('SELECT COUNT(*) FROM subscribers').fetchone()[0]
    db.close()

    if not rows:
        sys.exit(f'No articles published in {month}. Nothing to send.')

    pretty_month = datetime.strptime(month, '%Y-%m').strftime('%B')
    html, text = [], []

    html.append(
        f'<p style="margin:0 0 16px;">You signed up to hear when something new '
        f'goes up on Law Minded. {pretty_month} turned out to be a heavy month for '
        f'it — {len(rows)} guides, most of them prompted by something that '
        f'actually changed in the law rather than by a content calendar.</p>'
        f'<p style="margin:0 0 22px;">Here they are, grouped so you can skip '
        f'straight to the part that concerns you.</p>')
    text.append(
        f'You signed up to hear when something new goes up on Law Minded.\n'
        f'{pretty_month} was a heavy month: {len(rows)} guides, most prompted by '
        f'something that actually changed in the law.\n')

    for group_name, cats in GROUPS:
        items = [r for r in rows if r['category'] in cats]
        if not items:
            continue
        html.append(
            f'<p style="margin:26px 0 12px;font-size:13px;letter-spacing:.07em;'
            f'text-transform:uppercase;color:#8a6412;font-weight:600;">'
            f'{group_name}</p>')
        text.append(f'\n{group_name.upper()}\n')
        for r in items:
            url = f'{site.SITE_URL}/article/{r["slug"]}'
            summary = (r['summary'] or '').strip()
            if len(summary) > 165:
                summary = summary[:163].rsplit(' ', 1)[0] + '…'
            # One link per article, on the title. A second "Read →" pointing at
            # the same place doubled the link count to 24 in a single message,
            # which is the shape mail filters treat as promotional — and this
            # domain has almost no sending history to argue otherwise.
            html.append(
                f'<p style="margin:0 0 16px;line-height:1.5;">'
                f'<a href="{url}" style="color:#8a6412;font-weight:600;'
                f'text-decoration:none;font-size:16px;">{r["title"]}</a><br>'
                f'<span style="color:#5f5f5f;font-size:14px;">{summary}</span>'
                f'</p>')
            text.append(f'* {r["title"]}\n  {summary}\n  {url}\n')

    html.append(
        '<p style="margin:30px 0 0;color:#5f5f5f;font-size:14px;">'
        'Everything on the site is free and needs no account. If a subject you '
        'deal with is missing, reply to this email and say so — it is a short '
        'list of people and we read all of it.</p>')
    text.append('\nEverything on the site is free and needs no account. If a '
                'subject you deal with is missing, reply and say so.\n')

    subject = f'{len(rows)} new guides on Law Minded this {pretty_month}'
    return subject, ''.join(html), '\n'.join(text), len(rows), subscriber_count


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--month', required=True, help='YYYY-MM')
    ap.add_argument('--dry-run', action='store_true',
                    help='print what would be sent, mail nobody')
    a = ap.parse_args()

    import app as site
    with site.app.app_context():
        subject, html, text, n_articles, n_subs = build(site, a.month)

        print(f'Subject: {subject}')
        print(f'Articles: {n_articles}   Subscribers: {n_subs}')
        print('-' * 70)
        print(text)
        print('-' * 70)

        if a.dry_run:
            print('DRY RUN — nothing sent.')
            return

        sent, failed = site.mail_subscribers(
            subject, f'{n_articles} new guides this month', html, text,
            kind='roundup')
        print(f'sent: {sent}   failed: {failed}')
        if failed:
            sys.exit(1)


if __name__ == '__main__':
    main()
