#!/usr/bin/env python3
"""Publish drafts whose held date has arrived, and report what is still waiting.

Runs on the web server from cron each morning. The owner reads a draft, decides
it is good, and says "put it out on Sunday" — this is what makes Sunday happen.
The approval already took place; only the effective date is deferred, so nothing
here publishes anything a human has not already read and agreed to.

    ./venv/bin/python deploy/publish_due.py            # publish what is due
    ./venv/bin/python deploy/publish_due.py --report   # say what is pending, publish nothing

Dates are IST. The server runs UTC, and an article held for Sunday must appear on
Sunday in Delhi, not at half past five on Saturday evening.
"""
import os
import sqlite3
import sys
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import stage_draft  # noqa: E402  (reuses its .env loading, signing and notify)

IST = timezone(timedelta(hours=5, minutes=30))
DB_PATH = os.getenv('DATABASE_PATH', os.path.expanduser('~/lawminded-data/lawminded.db'))


def _conn():
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c


def pending(conn):
    return conn.execute(
        'SELECT slug, title, publish_on FROM articles '
        'WHERE published=0 ORDER BY publish_on IS NULL, publish_on, created_at'
    ).fetchall()


def publish_due(conn, today):
    """Anything held for today or earlier. Earlier matters: if the box was down
    on Sunday, Monday's run should still put out Sunday's article rather than
    leave it stranded forever."""
    due = conn.execute(
        'SELECT id, slug, title FROM articles '
        'WHERE published=0 AND publish_on IS NOT NULL AND publish_on <= ?',
        (today,)).fetchall()

    stamp = datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S')
    out = []
    for row in due:
        conn.execute(
            'UPDATE articles SET published=1, publish_on=NULL, created_at=?, updated_at=? '
            'WHERE id=?', (stamp, stamp, row['id']))
        out.append(row)
    if out:
        conn.commit()
    return out


def main():
    report_only = '--report' in sys.argv
    today = datetime.now(IST).strftime('%Y-%m-%d')
    conn = _conn()

    published = [] if report_only else publish_due(conn, today)

    lines = []
    for row in published:
        url = f'{stage_draft.SITE_URL}/article/{row["slug"]}'
        lines.append(f'Published today: {row["title"]}\n{url}')

    waiting = pending(conn)
    if waiting:
        held = [r for r in waiting if r['publish_on']]
        loose = [r for r in waiting if not r['publish_on']]
        if held:
            lines.append('Scheduled:\n' + '\n'.join(
                f'  {r["publish_on"]} — {r["title"]}' for r in held))
        if loose:
            lines.append(f'Waiting for your decision ({len(loose)}):\n' + '\n'.join(
                f'  {r["title"]}\n  {stage_draft.SITE_URL}/draft/{r["slug"]}'
                f'?t={stage_draft.sign(r["slug"])}' for r in loose[:5]))
    conn.close()

    msg = '\n\n'.join(lines) if lines else 'Nothing published, nothing pending.'
    print(msg)
    # Only interrupt the owner's day when something actually went live, or when
    # they asked for a report. A daily "nothing happened" message trains people
    # to ignore the channel that also carries the real ones.
    if published or report_only:
        stage_draft.notify_text(msg)


if __name__ == '__main__':
    main()
