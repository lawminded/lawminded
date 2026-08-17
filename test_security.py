"""Security regressions worth catching. Run: python3 test_security.py

Each of these guards a fix from the Aug 2026 hardening pass. They are cheap and
assert-only — no framework, no fixtures.
"""
import os
import sys

os.environ.setdefault('PRODUCTION', 'false')
os.environ.setdefault('DATABASE_PATH', '/tmp/lm-sectest.db')

import app as A


def test_csp_has_no_blanket_https():
    """script-src / connect-src must name origins, never a bare `https:`.

    A blanket https: lets any injected markup pull its payload from any host on
    the internet, which is most of what a CSP is supposed to prevent.
    """
    for ads_on in (False, True):
        csp = A._build_csp(ads_on)
        for directive in ('script-src', 'connect-src'):
            assert 'https:' not in csp[directive], \
                f'{directive} contains blanket https: (ads_on={ads_on})'


def test_csp_is_same_origin_while_ads_are_off():
    csp = A._build_csp(False)
    assert csp['script-src'] == ["'self'", "'unsafe-inline'"], csp['script-src']
    assert csp['connect-src'] == ["'self'"], csp['connect-src']
    assert csp['frame-src'] == ["'none'"], csp['frame-src']


def test_csp_admits_adsense_when_ads_are_on():
    csp = A._build_csp(True)
    assert any('googlesyndication' in s for s in csp['script-src']), \
        'AdSense would be blocked when ads are switched back on'


def test_locked_down_directives_never_loosen():
    for ads_on in (False, True):
        csp = A._build_csp(ads_on)
        assert csp['object-src'] == "'none'"
        assert csp['base-uri'] == "'self'"
        assert csp['frame-ancestors'] == "'self'"
        assert csp['form-action'] == "'self'"


def test_admin_pages_require_login():
    """Every /admin route must bounce an anonymous visitor to the login page."""
    A.app.config['WTF_CSRF_ENABLED'] = False
    client = A.app.test_client()
    admin_routes = [
        r.rule for r in A.app.url_map.iter_rules()
        if r.rule.startswith('/admin') and 'GET' in r.methods and '<' not in r.rule
    ]
    assert len(admin_routes) > 5, f'expected a real admin surface, found {admin_routes}'
    for rule in admin_routes:
        if rule in ('/admin/login', '/admin/logout'):
            continue
        resp = client.get(rule)
        assert resp.status_code in (302, 308), f'{rule} returned {resp.status_code}, not a redirect'
        assert '/admin/login' in resp.headers.get('Location', ''), \
            f'{rule} did not redirect to the login page'


def test_dead_upload_route_is_gone():
    """/uploads/templates/<f> served a directory that does not exist. Removed."""
    rules = [r.rule for r in A.app.url_map.iter_rules()]
    assert not any(r.startswith('/uploads/') for r in rules), \
        f'dead upload route is back: {[r for r in rules if r.startswith("/uploads/")]}'


def test_session_cookie_is_hardened():
    assert A.app.config['SESSION_COOKIE_HTTPONLY'] is True
    assert A.app.config['SESSION_COOKIE_SAMESITE'] == 'Lax'
    assert A.app.config['PERMANENT_SESSION_LIFETIME'].total_seconds() <= 8 * 3600


def test_admin_login_fails_closed_without_credentials():
    """With no ADMIN_* configured, no username/password combination may work."""
    saved = (os.environ.pop('ADMIN_USERNAME', None), os.environ.pop('ADMIN_PW_HASH_B64', None))
    try:
        assert A.check_admin('admin', 'admin') is False
        assert A.check_admin('', '') is False
        assert A.check_admin('admin', 'Wine123') is False
    finally:
        if saved[0] is not None:
            os.environ['ADMIN_USERNAME'] = saved[0]
        if saved[1] is not None:
            os.environ['ADMIN_PW_HASH_B64'] = saved[1]


def test_html_sanitiser_strips_script_and_handlers():
    dirty = '<p onclick="steal()">hi</p><script>alert(1)</script><a href="javascript:x()">z</a>'
    clean = A.sanitize_html(dirty)
    assert '<script' not in clean.lower()
    assert 'onclick' not in clean.lower()
    assert 'javascript:' not in clean.lower()


if __name__ == '__main__':
    tests = [v for k, v in sorted(globals().items()) if k.startswith('test_')]
    failed = 0
    for t in tests:
        try:
            t()
            print(f'  ok   {t.__name__}')
        except AssertionError as e:
            failed += 1
            print(f'  FAIL {t.__name__}: {e}')
    print(f'\n{len(tests) - failed}/{len(tests)} passed')
    sys.exit(1 if failed else 0)
