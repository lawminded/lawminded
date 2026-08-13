"""Guards the one invariant that seeding has to satisfy: restarting the app must
not change what is published. Run with `python3 test_seed.py` — no pytest.

This exists because of a bug that reached production. Content migration 6 renamed
`dpt-3-fy-2025-26` to `dpt-3-return-filing`, but the old slug was still in
blog_seed3 and not in RETIRED_SLUGS. Migrations are guarded by PRAGMA
user_version so the rename ran once; seed_articles() runs on every boot. The gap
the rename left got refilled on the next restart, and the site ended up serving a
duplicate that only 301s — in the sitemap and the article listings.

The site ran for six weeks without restarting, so nobody saw it until a
maintenance reboot. That is the shape of the problem: a boot-order bug is
invisible until something reboots, which is exactly when you are not looking.

Rather than assert anything about DPT-3 specifically, this boots a database twice
and requires the second boot to be a no-op. Any future migration that renames a
seeded slug fails here instead of in production.
"""
import os
import subprocess
import sqlite3
import sys
import tempfile

REPO = os.path.dirname(os.path.abspath(__file__))


def _boot(db_path):
    """One application start, in a fresh process — the only faithful way to
    simulate a restart, since the bootstrap runs at import time."""
    env = {**os.environ, 'DATABASE_PATH': db_path, 'PYTHONPATH': REPO}
    r = subprocess.run([sys.executable, '-c', 'import app'],
                       cwd=REPO, env=env, capture_output=True, text=True)
    assert r.returncode == 0, f'app failed to start:\n{r.stderr[-2000:]}'


def _articles(db_path):
    conn = sqlite3.connect(db_path)
    rows = conn.execute('SELECT slug, published FROM articles ORDER BY slug').fetchall()
    conn.close()
    return rows


def test_a_restart_changes_nothing():
    with tempfile.TemporaryDirectory() as tmp:
        db = os.path.join(tmp, 'boot.db')

        _boot(db)
        first = _articles(db)
        assert first, 'first boot seeded nothing'

        _boot(db)
        second = _articles(db)

        added = set(second) - set(first)
        removed = set(first) - set(second)
        assert not added, f'restart added rows: {sorted(added)}'
        assert not removed, f'restart removed rows: {sorted(removed)}'

        # A third boot too — a bug that alternates would slip past two.
        _boot(db)
        assert _articles(db) == first, 'third boot diverged'
        print(f'  ({len(first)} articles, stable across three boots)')


def test_retired_slugs_never_come_back():
    """RETIRED_SLUGS is the list of URLs that must stay dead. seed_articles both
    skips and deletes them, so no boot should ever leave one in the table."""
    sys.path.insert(0, REPO)
    from database import RETIRED_SLUGS

    with tempfile.TemporaryDirectory() as tmp:
        db = os.path.join(tmp, 'retired.db')
        _boot(db)
        _boot(db)
        live = {slug for slug, _ in _articles(db)}
        back = live & RETIRED_SLUGS
        assert not back, f'retired slugs present after boot: {sorted(back)}'
        print(f'  ({len(RETIRED_SLUGS)} retired slugs, none resurrected)')


if __name__ == '__main__':
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            print(f'  ok  {name}')
            fn()
    print('\nSeeding is idempotent across restarts.')
