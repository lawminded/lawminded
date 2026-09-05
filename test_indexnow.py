"""Guards the IndexNow and Bing wiring. Run with `python3 test_indexnow.py`.

IndexNow publishes a key at a URL to prove the domain is ours, and pings an
endpoint on every publish. Two things must hold: the key route must not become a
catch-all on every .txt at the site root, and a search engine being unreachable
must never break publishing an article.
"""
import os
import sys
from pathlib import Path

os.environ.setdefault('SECRET_KEY', 'test-key-not-a-real-one')
sys.path.insert(0, str(Path(__file__).resolve().parent))
import app as A  # noqa: E402


def test_only_the_configured_key_is_served():
    """A catch-all on /<anything>.txt would hand out a 200 for any probe and
    make the site look like it hosts files it does not."""
    real = A.INDEXNOW_KEY
    A.INDEXNOW_KEY = 'abc123realkey'
    c = A.app.test_client()
    try:
        good = c.get('/abc123realkey.txt')
        assert good.status_code == 200, good.status_code
        assert good.get_data(as_text=True) == 'abc123realkey'
        for probe in ('/secrets.txt', '/robots-backup.txt', '/wrongkey.txt'):
            assert c.get(probe).status_code == 404, f'{probe} should 404'
    finally:
        A.INDEXNOW_KEY = real


def test_no_key_means_no_key_file():
    real = A.INDEXNOW_KEY
    A.INDEXNOW_KEY = ''
    try:
        assert A.app.test_client().get('/anything.txt').status_code == 404
    finally:
        A.INDEXNOW_KEY = real


def test_a_dead_endpoint_does_not_break_publishing():
    """Publishing must survive IndexNow being down, refusing us, or DNS failing."""
    real_key, real_prod, real_open = A.INDEXNOW_KEY, A.IS_PROD, A.urllib.request.urlopen
    A.INDEXNOW_KEY, A.IS_PROD = 'k', True

    def boom(*a, **k):
        raise OSError('network is on fire')

    A.urllib.request.urlopen = boom
    try:
        with A.app.app_context():
            assert A.ping_indexnow('https://lawminded.in/article/x') is False
    finally:
        A.INDEXNOW_KEY, A.IS_PROD, A.urllib.request.urlopen = real_key, real_prod, real_open


def test_nothing_is_pinged_off_production():
    """A dev machine must not tell Bing that localhost changed."""
    real_key, real_prod = A.INDEXNOW_KEY, A.IS_PROD
    A.INDEXNOW_KEY, A.IS_PROD = 'k', False
    called = []
    real_open = A.urllib.request.urlopen
    A.urllib.request.urlopen = lambda *a, **k: called.append(a)
    try:
        with A.app.app_context():
            assert A.ping_indexnow('https://lawminded.in/article/x') is False
        assert called == [], 'pinged IndexNow from a non-production run'
    finally:
        A.INDEXNOW_KEY, A.IS_PROD, A.urllib.request.urlopen = real_key, real_prod, real_open


def test_the_payload_is_what_indexnow_expects():
    import json
    real_key, real_prod, real_open = A.INDEXNOW_KEY, A.IS_PROD, A.urllib.request.urlopen
    A.INDEXNOW_KEY, A.IS_PROD = 'thekey', True
    seen = {}

    def capture(req, *a, **k):
        seen['body'] = json.loads(req.data)
        seen['url'] = req.full_url
        class R:
            status = 200
            def __enter__(self): return self
            def __exit__(self, *a): return False
        return R()

    A.urllib.request.urlopen = capture
    try:
        with A.app.app_context():
            A.ping_indexnow('https://lawminded.in/article/a', 'https://lawminded.in/article/b')
    finally:
        A.INDEXNOW_KEY, A.IS_PROD, A.urllib.request.urlopen = real_key, real_prod, real_open

    b = seen['body']
    assert b['key'] == 'thekey'
    assert b['host'] == 'lawminded.in', b['host']
    assert b['keyLocation'].endswith('/thekey.txt'), b['keyLocation']
    assert len(b['urlList']) == 2


def test_bing_verification_renders_only_when_set():
    real = A.BING_SITE_VERIFICATION
    c = A.app.test_client()
    try:
        A.BING_SITE_VERIFICATION = ''
        assert 'msvalidate.01' not in c.get('/').get_data(as_text=True)
        A.BING_SITE_VERIFICATION = 'ABC123'
        # The context processor reads the module global at request time.
        A.app.jinja_env.cache.clear()
        html = c.get('/').get_data(as_text=True)
        assert 'msvalidate.01' in html and 'ABC123' in html, 'Bing meta tag missing'
    finally:
        A.BING_SITE_VERIFICATION = real


if __name__ == '__main__':
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            fn()
            print(f'  ok  {name}')
    print('\nIndexNow and Bing wiring holds.')
