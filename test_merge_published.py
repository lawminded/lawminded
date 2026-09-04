"""Guards the hourly branch-merge job. Run with `python3 test_merge_published.py`.

This thing pushes to main and deletes branches without a human watching, and it
builds both a database query and a git ref out of a branch name. Two failures
matter more than the rest: merging something that is not actually live, and
deleting a branch whose article was never published.
"""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / 'automation'))
import merge_published as M  # noqa: E402


def test_odd_branch_names_are_refused():
    """The slug goes into a git ref and a SQL parameter list. It comes from a
    branch name, which is attacker-controlled if push access ever leaks."""
    for bad in ('../../etc/passwd', 'a; rm -rf /', 'has space', 'UPPER',
                'semi;colon', '-leading-dash', '', 'x' * 90, 'quote\'s'):
        assert not M.SLUG_RE.match(bad), f'accepted a bad slug: {bad!r}'
    for good in ('rti-vs-pil-difference', 'ccfs-2026-extended-15-september-2026',
                 'pas-3-vs-pas-4'):
        assert M.SLUG_RE.match(good), f'rejected a real slug: {good!r}'


def test_shell_quote_survives_a_quote():
    got = M.shell_quote("it's")
    assert got.startswith("'") and got.endswith("'")
    # Round-trip it through a real shell rather than trusting the string.
    out = subprocess.run(['sh', '-c', f'printf %s {got}'],
                         capture_output=True, text=True).stdout
    assert out == "it's", repr(out)


def test_a_dry_run_changes_nothing():
    """--dry-run must not merge, push or delete."""
    calls = []
    real_git, real_run = M.git, subprocess.run

    def fake_git(*args, **kw):
        calls.append(args)
        if args[:2] == ('branch', '-r'):
            return 'origin/post/alpha-slug\norigin/post/beta-slug'
        return ''

    M.git = fake_git
    M.published_slugs = lambda slugs: {'alpha-slug'}
    subprocess.run = lambda *a, **k: type('R', (), {'returncode': 1, 'stdout': '', 'stderr': ''})()
    try:
        sys.argv = ['merge_published.py', '--dry-run']
        M.main()
    finally:
        M.git, subprocess.run = real_git, real_run

    forbidden = [c for c in calls if c[0] in ('push', 'merge', 'worktree')]
    assert not forbidden, f'a dry run tried to change things: {forbidden}'


def test_an_unpublished_branch_is_never_deleted():
    """A branch pushed a minute before its draft is staged looks exactly like a
    rejected one. Deleting on absence would throw away work in progress."""
    calls = []
    real_git, real_run = M.git, subprocess.run

    def fake_git(*args, **kw):
        calls.append(args)
        if args[:2] == ('branch', '-r'):
            return 'origin/post/not-yet-staged'
        return ''

    M.git = fake_git
    M.published_slugs = lambda slugs: set()          # nothing is live
    subprocess.run = lambda *a, **k: type('R', (), {'returncode': 1, 'stdout': '', 'stderr': ''})()
    try:
        sys.argv = ['merge_published.py']
        M.main()
    finally:
        M.git, subprocess.run = real_git, real_run

    deletes = [c for c in calls if 'push' in c and '--delete' in c]
    assert not deletes, f'deleted a branch that was never published: {deletes}'


def test_it_stands_down_while_a_weekly_run_is_going():
    """Two processes moving the checkout between branches is how a run commits to
    the wrong one."""
    calls = []
    real_git, real_run = M.git, subprocess.run
    M.git = lambda *a, **k: calls.append(a) or ''
    # pgrep returning 0 means a run.sh is alive.
    subprocess.run = lambda *a, **k: type('R', (), {'returncode': 0, 'stdout': '', 'stderr': ''})()
    try:
        sys.argv = ['merge_published.py']
        M.main()
    finally:
        M.git, subprocess.run = real_git, real_run
    assert calls == [], f'ran git while a weekly run was in progress: {calls}'


if __name__ == '__main__':
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            fn()
            print(f'  ok  {name}')
    print('\nHourly merge job holds.')
