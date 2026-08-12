"""Guards the draft-approval flow the weekly writer depends on. Run with
`python3 test_draft.py` — no pytest, no fixtures, same as test_seo.py.

The thing that must never break: an unpublished draft is invisible to the
public and to search engines, and the only way to publish it is a POST carrying
a valid signature. If the signature check ever goes soft, anyone who guesses a
slug can publish unreviewed legal content on a live compliance site.
"""
import os
import tempfile

# Point at a throwaway DB before importing app — database.py reads DATABASE_PATH
# at import time, and load_dotenv() won't override an env var already set.
_tmp = tempfile.mkdtemp()
os.environ['DATABASE_PATH'] = os.path.join(_tmp, 'test.db')

from app import app, _draft_serializer  # noqa: E402
from database import get_db  # noqa: E402

SLUG = 'zzz-draft-flow-test'
app.config['WTF_CSRF_ENABLED'] = False


def _insert_draft():
    db = get_db()
    db.execute(
        'INSERT OR REPLACE INTO articles (title, slug, category, act, read_time, '
        'summary, content, published) VALUES (?,?,?,?,?,?,?,0)',
        ('Draft Flow Test', SLUG, 'corp', 'Companies Act 2013', '2 min',
         'Summary.', '<p>Body of the draft.</p>'))
    db.commit()
    db.close()


def _row():
    db = get_db()
    row = db.execute('SELECT * FROM articles WHERE slug=?', (SLUG,)).fetchone()
    db.close()
    return row


def test_draft_is_invisible_without_a_valid_signature():
    _insert_draft()
    c = app.test_client()
    assert c.get(f'/article/{SLUG}').status_code == 404, 'unpublished draft served publicly'
    assert c.get(f'/draft/{SLUG}').status_code == 404, 'no token accepted'
    assert c.get(f'/draft/{SLUG}?t=nonsense').status_code == 404, 'garbage token accepted'
    # A signature is bound to its own slug: one draft's token must not open another's.
    other = _draft_serializer.dumps('some-other-slug')
    assert c.get(f'/draft/{SLUG}?t={other}').status_code == 404, 'token reused across slugs'


def test_valid_token_previews_but_does_not_index():
    _insert_draft()
    c = app.test_client()
    r = c.get(f'/draft/{SLUG}?t={_draft_serializer.dumps(SLUG)}')
    assert r.status_code == 200, f'valid token -> {r.status_code}'
    html = r.get_data(as_text=True)
    assert 'Body of the draft.' in html, 'draft body missing from preview'
    assert 'Draft — not published' in html, 'approval bar missing'
    assert 'noindex, nofollow' in html, 'draft preview is indexable'


def test_publish_needs_the_signature_and_then_goes_live():
    _insert_draft()
    c = app.test_client()
    token = _draft_serializer.dumps(SLUG)

    assert c.post(f'/draft/{SLUG}/publish', data={'t': 'nonsense'}).status_code == 404
    assert _row()['published'] == 0, 'bad signature published the draft'

    r = c.post(f'/draft/{SLUG}/publish', data={'t': token})
    assert r.status_code == 302, f'publish -> {r.status_code}'
    assert _row()['published'] == 1, 'publish did not flip the row'
    assert c.get(f'/article/{SLUG}').status_code == 200, 'published article still 404s'

    # Publishing is one-way: the draft routes stop matching once it is live, so a
    # leaked link cannot later be used to delete a published article.
    assert c.post(f'/draft/{SLUG}/reject', data={'t': token}).status_code == 404
    assert _row() is not None, 'reject deleted a published article'


def test_staging_script_signs_the_same_way_as_the_app():
    """deploy/stage_draft.py builds the token itself so it need not import the
    whole Flask app on a 1 GB server. If the key or salt ever drifts apart, the
    weekly Telegram link 404s and nobody finds out until a Friday morning."""
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deploy'))
    import stage_draft as stage
    os.environ['SECRET_KEY'] = app.secret_key
    assert stage.sign(SLUG) == _draft_serializer.dumps(SLUG), \
        'stage_draft.py and app.py disagree on the draft signature'


def test_reject_removes_the_draft():
    _insert_draft()
    c = app.test_client()
    r = c.post(f'/draft/{SLUG}/reject', data={'t': _draft_serializer.dumps(SLUG)})
    assert r.status_code == 302, f'reject -> {r.status_code}'
    assert _row() is None, 'rejected draft still in the database'


if __name__ == '__main__':
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            fn()
            print(f'  ok  {name}')
    print('\nDraft approval flow: all checks passed.')
