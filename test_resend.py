"""Guards the Resend delivery path. Run with `python3 test_resend.py`.

Every email the site sends — the contact acknowledgement, the internal enquiry
notification, the newsletter — goes through `_deliver`. It has two ways out, and
the one that is live depends on whether RESEND_API_KEY is set on the server. So
both need a test: a translation bug would be invisible until someone noticed
mail had quietly stopped, or that the logo had become a broken image.
"""
import os
import sys
from pathlib import Path

os.environ.setdefault('SECRET_KEY', 'test-key-not-a-real-one')
sys.path.insert(0, str(Path(__file__).resolve().parent))

import app as A  # noqa: E402
from flask_mail import Message  # noqa: E402


def _msg():
    """A message shaped like the ones the site actually sends: HTML plus a real
    plain-text part, a reply-to, one-click unsubscribe headers, and the inline
    logo."""
    m = Message(subject='Test subject', recipients=['reader@example.com'])
    m.body = 'plain text part'
    m.html = '<p>html part <img src="cid:logo"></p>'
    m.reply_to = 'hello@lawminded.in'
    m.extra_headers = {'List-Unsubscribe': '<https://lawminded.in/u/abc>',
                       'List-Unsubscribe-Post': 'List-Unsubscribe=One-Click'}
    m.attach('logo.png', 'image/png', b'\x89PNG-not-really', 'inline',
             headers={'Content-ID': '<logo>', 'X-Attachment-Id': 'logo'})
    return m


def test_payload_carries_everything_resend_needs():
    with A.app.app_context():
        p = A._resend_payload(_msg())
    assert p['to'] == ['reader@example.com']
    assert p['subject'] == 'Test subject'
    assert p['text'] == 'plain text part'
    assert '<p>html part' in p['html']
    assert p['from'], 'no From address — Resend rejects the send'
    assert p['reply_to'] == 'hello@lawminded.in'
    assert p['headers']['List-Unsubscribe-Post'] == 'List-Unsubscribe=One-Click', \
        'one-click unsubscribe header lost — an inbox-placement signal'


def test_the_inline_logo_survives_the_translation():
    """The branded template references the logo as cid:logo. Resend carries that
    through `content_id`; drop it and every email goes out with a broken image
    where the masthead should be."""
    with A.app.app_context():
        p = A._resend_payload(_msg())
    att = p['attachments'][0]
    assert att['content_id'] == 'logo', f'cid lost: {att}'
    assert att['filename'] == 'logo.png'
    assert att['content_type'] == 'image/png'
    import base64
    assert base64.b64decode(att['content']) == b'\x89PNG-not-really', \
        'attachment must be base64 of the raw bytes'


def test_no_key_means_smtp_and_nothing_reaches_resend():
    """The fallback has to stay working: if the key is ever unset or removed,
    mail must go out over SMTP rather than vanishing."""
    sent, posted = [], []
    real_key, real_send, real_open = A.RESEND_API_KEY, A.mail.send, A.urllib.request.urlopen
    A.RESEND_API_KEY = None
    A.mail.send = sent.append
    A.urllib.request.urlopen = lambda *a, **k: posted.append(a) or (_ for _ in ()).throw(
        AssertionError('called Resend with no API key set'))
    try:
        with A.app.app_context():
            A._deliver(_msg())
    finally:
        A.RESEND_API_KEY, A.mail.send, A.urllib.request.urlopen = real_key, real_send, real_open
    assert len(sent) == 1, 'with no API key the message must go out over SMTP'
    assert posted == []


def test_a_resend_error_says_what_resend_said():
    """"HTTP 403" on its own sends whoever debugs this to the wrong place. The
    usual cause is an unverified domain, and Resend says so in the body."""
    import io
    import urllib.error
    real_key, real_open = A.RESEND_API_KEY, A.urllib.request.urlopen

    def boom(*a, **k):
        raise urllib.error.HTTPError(
            A.RESEND_ENDPOINT, 403, 'Forbidden', {},
            io.BytesIO(b'{"message":"The lawminded.in domain is not verified"}'))

    A.RESEND_API_KEY = 're_test_key'
    A.urllib.request.urlopen = boom
    try:
        with A.app.app_context():
            A._deliver(_msg())
        raise AssertionError('a rejected send must raise, not pass silently')
    except RuntimeError as e:
        assert 'not verified' in str(e), f'lost the reason: {e}'
        assert '403' in str(e)
    finally:
        A.RESEND_API_KEY, A.urllib.request.urlopen = real_key, real_open


def test_a_message_can_override_the_from_address():
    """The poll letter goes out as a named person rather than the brand, which is
    part of why Gmail files it under Primary instead of Promotions. If msg.sender
    stopped being honoured, it would silently revert to the site-wide From."""
    with A.app.app_context():
        m = _msg()
        m.sender = 'Piyush Kundnani <hello@lawminded.in>'
        assert A._resend_payload(m)['from'] == 'Piyush Kundnani <hello@lawminded.in>'

        plain = _msg()
        plain.sender = None
        assert A._resend_payload(plain)['from'] == A.RESEND_FROM, \
            'a message with no sender must still fall back to the site default'


def test_the_request_identifies_itself():
    """Resend is behind Cloudflare, which answers urllib's default
    "Python-urllib/3.x" with 403 and Cloudflare error 1010 — a body that
    mentions neither the key nor the domain, so it reads like an auth failure.
    The first live send hit exactly this."""
    captured = {}
    real_key, real_open = A.RESEND_API_KEY, A.urllib.request.urlopen

    def capture(req, *a, **k):
        captured['headers'] = {k.lower(): v for k, v in req.header_items()}
        class R:
            def read(self): return b'{"id":"test"}'
            def __enter__(self): return self
            def __exit__(self, *a): return False
        return R()

    A.RESEND_API_KEY = 're_test_key'
    A.urllib.request.urlopen = capture
    try:
        with A.app.app_context():
            A._deliver(_msg())
    finally:
        A.RESEND_API_KEY, A.urllib.request.urlopen = real_key, real_open

    ua = captured['headers'].get('User-agent'.lower(), '')
    assert ua and 'python-urllib' not in ua.lower(), \
        f'request would be blocked by Cloudflare with this User-Agent: {ua!r}'
    assert 'lawminded' in ua.lower(), f'the caller should say who it is: {ua!r}'


def test_the_key_is_never_hardcoded():
    """A key in the repo is a key in every clone and on GitHub."""
    import re
    src = (Path(__file__).resolve().parent / 'app.py').read_text()
    assert "os.getenv('RESEND_API_KEY')" in src, 'the key must come from the environment'
    # A real key is re_ followed by a long opaque string. Matching a bare "re_"
    # would fire on ordinary words like "are_" and "more_".
    leaked = re.findall(r'\bre_[A-Za-z0-9_]{16,}', src)
    assert not leaked, f'something shaped like a Resend key is in app.py: {leaked}'


if __name__ == '__main__':
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            fn()
            print(f'  ok  {name}')
    print('\nResend delivery path holds.')
