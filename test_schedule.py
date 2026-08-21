"""Guards held-until-a-date publishing. Run with `python3 test_schedule.py`.

Two things here decide whether an article appears on the right day.

The date must be IST. The server runs UTC, so anything published after 18:30 UTC
is already tomorrow in Delhi, and a naive CURRENT_TIMESTAMP dates it yesterday —
a five and a half hour window every night where the article carries the wrong day.
The owner asked specifically for the publication date to be the day it goes live.

And a held article must still go out if the box was down on its day. A scheduler
that only matches "== today" strands an article forever the first time cron misses
a morning.
"""
import os
import sqlite3
import sys
import tempfile
from datetime import datetime, timedelta, timezone

_tmp = tempfile.mkdtemp()
os.environ['DATABASE_PATH'] = os.path.join(_tmp, 'sched.db')

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(REPO, 'deploy'))

from app import app, ist_now, ist_today  # noqa: E402
from database import get_db  # noqa: E402
import publish_due  # noqa: E402

publish_due.DB_PATH = os.environ['DATABASE_PATH']
IST = timezone(timedelta(hours=5, minutes=30))


def _draft(slug, publish_on=None):
    db = get_db()
    db.execute('DELETE FROM articles WHERE slug=?', (slug,))
    db.execute(
        'INSERT INTO articles (title, slug, category, act, read_time, summary, '
        'content, published, publish_on, created_at) '
        'VALUES (?,?,?,?,?,?,?,0,?,?)',
        (f'Draft {slug}', slug, 'corp', 'Companies Act 2013', '3 min',
         'Summary.', '<p>Body.</p>', publish_on, '2026-01-01 09:00:00'))
    db.commit()
    db.close()


def _row(slug):
    db = get_db()
    r = db.execute('SELECT published, publish_on, created_at FROM articles WHERE slug=?',
                   (slug,)).fetchone()
    db.close()
    return r


def test_ist_clock_is_not_utc():
    ist = datetime.now(IST)
    assert ist_today() == ist.strftime('%Y-%m-%d'), 'ist_today() is not IST'
    assert ist_now().startswith(ist.strftime('%Y-%m-%d %H:')), 'ist_now() is not IST'
    # The whole point: during the 18:30–24:00 UTC window these differ by a day.
    utc_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    if datetime.now(timezone.utc).hour >= 19:
        assert ist_today() != utc_date, 'IST and UTC should differ by a day right now'


def test_a_draft_held_for_tomorrow_stays_put():
    tomorrow = (datetime.now(IST) + timedelta(days=1)).strftime('%Y-%m-%d')
    _draft('zzz-tomorrow', tomorrow)
    conn = publish_due._conn()
    done = publish_due.publish_due(conn, ist_today())
    conn.close()
    assert done == [], 'published something held for tomorrow'
    assert _row('zzz-tomorrow')['published'] == 0


def test_a_draft_held_for_today_goes_live_dated_today():
    _draft('zzz-today', ist_today())
    conn = publish_due._conn()
    done = publish_due.publish_due(conn, ist_today())
    conn.close()
    assert len(done) == 1, 'did not publish a draft due today'
    r = _row('zzz-today')
    assert r['published'] == 1
    assert r['publish_on'] is None, 'publish_on should be cleared once published'
    assert r['created_at'].startswith(ist_today()), \
        f'dated {r["created_at"]}, expected today in IST ({ist_today()})'


def test_a_missed_day_still_goes_out():
    """If cron did not run on Sunday, Monday must still publish Sunday's article
    rather than leaving it held forever."""
    past = (datetime.now(IST) - timedelta(days=3)).strftime('%Y-%m-%d')
    _draft('zzz-overdue', past)
    conn = publish_due._conn()
    done = publish_due.publish_due(conn, ist_today())
    conn.close()
    assert len(done) == 1, 'an overdue draft was stranded'
    assert _row('zzz-overdue')['created_at'].startswith(ist_today()), \
        'an overdue article should carry the day it actually went out'


def test_an_unscheduled_draft_is_never_auto_published():
    """A draft with no date is one the owner has not ruled on. Nothing may put it
    live except their own tap."""
    _draft('zzz-undecided', None)
    conn = publish_due._conn()
    publish_due.publish_due(conn, ist_today())
    conn.close()
    assert _row('zzz-undecided')['published'] == 0, \
        'auto-published a draft the owner never scheduled'


if __name__ == '__main__':
    with app.app_context():
        for name, fn in sorted(globals().items()):
            if name.startswith('test_'):
                fn()
                print(f'  ok  {name}')
    print('\nScheduled publishing holds.')
