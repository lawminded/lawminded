"""Guards the subscriber poll. Run with `python3 test_poll.py`.

The result of this poll decides whether the templates library gets put behind a
login, so the count has to mean something. Two ways it could quietly stop meaning
something: a link scanner casting votes by fetching URLs, and one person being
able to vote more than once.
"""
import os
import sys
import tempfile
from pathlib import Path

os.environ.setdefault('SECRET_KEY', 'test-key-not-a-real-one')
os.environ['DATABASE_PATH'] = str(Path(tempfile.mkdtemp()) / 'poll-test.db')
sys.path.insert(0, str(Path(__file__).resolve().parent))

import database  # noqa: E402
import app as A  # noqa: E402

SLUG = 'templates-login'
VOTER = 'reader@example.com'


def setup():
    database.init_db()
    with A.app.app_context():
        db = A.get_db()
        db.execute('DELETE FROM poll_votes')
        db.execute('INSERT OR IGNORE INTO subscribers (name, email) VALUES (?,?)',
                   ('Test Reader', VOTER))
        db.commit()
        db.close()


def _token():
    return A._poll_serializer.dumps([SLUG, VOTER])


def _counts():
    with A.app.app_context():
        db = A.get_db()
        c = A.poll_counts(db, SLUG)
        db.close()
    return c


def test_opening_the_link_does_not_cast_a_vote():
    """Gmail, Outlook and every corporate link scanner fetch the URLs in a
    message to build previews. If GET voted, a chunk of the ballot would be cast
    by machines before a human read the email — the same reason the draft
    approval page uses POST."""
    setup()
    c = A.app.test_client()
    r = c.get(f'/poll/{SLUG}?token={_token()}')
    assert r.status_code == 200, r.status_code
    assert _counts()['total'] == 0, 'merely opening the link recorded a vote'


def test_a_vote_is_recorded_on_post():
    setup()
    c = A.app.test_client()
    r = c.post(f'/poll/{SLUG}', data={'token': _token(), 'choice': 'yes'})
    assert r.status_code == 200, r.status_code
    assert _counts() == {'yes': 1, 'no': 0, 'total': 1}, _counts()


def test_voting_twice_changes_the_answer_rather_than_adding_one():
    setup()
    c = A.app.test_client()
    c.post(f'/poll/{SLUG}', data={'token': _token(), 'choice': 'yes'})
    c.post(f'/poll/{SLUG}', data={'token': _token(), 'choice': 'no'})
    assert _counts() == {'yes': 0, 'no': 1, 'total': 1}, \
        f'one person voted twice: {_counts()}'


def test_an_unsigned_or_forwarded_link_cannot_vote():
    """The link is personal. A forwarded copy with the token stripped, or a
    guessed one, must not count."""
    setup()
    c = A.app.test_client()
    c.post(f'/poll/{SLUG}', data={'choice': 'yes'})
    c.post(f'/poll/{SLUG}', data={'token': 'not-a-real-token', 'choice': 'yes'})
    assert _counts()['total'] == 0, f'an unsigned link voted: {_counts()}'


def test_a_token_for_another_poll_does_not_work_here():
    setup()
    other = A._poll_serializer.dumps(['some-other-poll', VOTER])
    c = A.app.test_client()
    c.post(f'/poll/{SLUG}', data={'token': other, 'choice': 'yes'})
    assert _counts()['total'] == 0, 'a token signed for a different poll voted'


def test_results_are_hidden_while_voting_is_open():
    """An early landslide showing on the page would steer whoever votes next."""
    setup()
    c = A.app.test_client()
    c.post(f'/poll/{SLUG}', data={'token': _token(), 'choice': 'yes'})
    body = c.get(f'/poll/{SLUG}?token={_token()}').get_data(as_text=True)
    assert 'Yes: 1' not in body, 'live counts are visible while voting is open'


def test_the_page_is_not_indexable():
    setup()
    c = A.app.test_client()
    body = c.get(f'/poll/{SLUG}?token={_token()}').get_data(as_text=True)
    assert 'noindex' in body, 'the poll page should not be in search results'


def test_results_are_admin_only():
    setup()
    c = A.app.test_client()
    r = c.get(f'/admin/poll/{SLUG}', follow_redirects=False)
    assert r.status_code in (301, 302, 401, 403), \
        f'poll results reachable without logging in: {r.status_code}'


def test_personalisation_reaches_each_subscriber():
    """mail_subscribers must be able to greet people by name and hand each one a
    link signed for their own address."""
    setup()
    seen = []
    real = A.send_branded_email
    A.send_branded_email = lambda subject, to, heading, html, text, unsub=None: \
        seen.append((to[0], heading, html))
    try:
        with A.app.app_context():
            A.mail_subscribers(
                'Subject',
                heading=lambda p: f"Hello {p['name'] or 'there'}",
                body_html=lambda p: f"<p>{A.poll_url(SLUG, p['email'])}</p>",
                body_text=lambda p: 'text',
                kind='poll')
    finally:
        A.send_branded_email = real

    assert seen, 'nothing was sent'
    addr, heading, html = seen[0]
    assert heading == 'Hello Test Reader', f'not personalised: {heading!r}'
    with A.app.app_context():
        assert A.poll_url(SLUG, addr) in html, \
            'the link in the email is not the one signed for the person receiving it'


def test_the_emailed_link_has_no_query_string():
    """A long ?token=... is the shape of a click-tracking link, and filters read
    it that way. The token goes in the path instead."""
    with A.app.app_context():
        url = A.poll_url(SLUG, VOTER)
    assert '?' not in url, f'the emailed link looks like a tracking URL: {url}'
    assert url.startswith(f'https://lawminded.in/poll/{SLUG}/') or '/poll/' in url, url


def test_the_path_form_of_the_link_opens_without_voting():
    setup()
    with A.app.app_context():
        url = A.poll_url(SLUG, VOTER)
    path = url.split('lawminded.in', 1)[-1] if 'lawminded.in' in url else url
    c = A.app.test_client()
    r = c.get(path)
    assert r.status_code == 200, r.status_code
    assert 'Yes' in r.get_data(as_text=True), 'the voting buttons did not render'
    assert _counts()['total'] == 0, 'opening the path link cast a vote'


if __name__ == '__main__':
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            fn()
            print(f'  ok  {name}')
    print('\nPoll holds.')
