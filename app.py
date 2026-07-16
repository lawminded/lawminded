import os
import re
import sqlite3
import base64
import hmac
from io import BytesIO
from datetime import date
from functools import wraps, lru_cache
from flask import (Flask, render_template, request, redirect, url_for,
                   session, flash, jsonify, send_from_directory, send_file, abort)
from flask_mail import Mail, Message
from itsdangerous import URLSafeSerializer, BadSignature
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_wtf import CSRFProtect
from flask_wtf.csrf import CSRFError
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
import bleach
from dotenv import load_dotenv

# Load .env BEFORE importing database, which reads DATABASE_PATH at import time.
# (If load_dotenv runs after that import, the custom DB path is silently ignored.)
load_dotenv()

from database import get_db, init_db, seed_articles, seed_documents, seed_formats
import content as C
import formats as F

# Production flag: enables HTTPS enforcement, HSTS, and Secure cookies on the live
# server. Stays off locally so http://localhost development still works.
IS_PROD = os.getenv('PRODUCTION', 'false').lower() in ('1', 'true', 'yes')

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-change-in-production')

# Behind a reverse proxy (nginx on the Oracle VM, or Render's edge), trust the
# X-Forwarded-* headers so request.scheme is 'https'. Without this, Talisman's
# force_https would redirect-loop forever when the app sits behind nginx.
if IS_PROD:
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)

# ── Hardened session / request config ──
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_COOKIE_SECURE'] = IS_PROD
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB — room for admin Word (.docx) uploads
app.config['WTF_CSRF_TIME_LIMIT'] = None            # token valid for the session

# Mail configuration — provider-agnostic via env (defaults to Gmail SMTP).
# Set MAIL_SERVER/PORT for a custom-domain mailbox (e.g. Zoho, Titan, Workspace).
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', '587'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'true').lower() in ('1', 'true', 'yes')
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL', 'false').lower() in ('1', 'true', 'yes')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
# Sender can differ from the login user (defaults to the login user).
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER', os.getenv('MAIL_USERNAME'))

mail = Mail(app)

# ── CSRF protection on every POST form ──
csrf = CSRFProtect(app)

# ── Rate limiting (brute-force + spam protection) ──
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=['300 per hour'],
    storage_uri='memory://',
)

# ── Security headers + Content-Security-Policy ──
# script-src is intentionally permissive (https:) so Google AdSense and the
# Three.js CDN load reliably; the high-value protections (clickjacking, object/base
# lockdown, MIME-sniffing, referrer, HSTS, secure cookies) are all enforced.
CSP = {
    'default-src': "'self'",
    'script-src': ["'self'", "'unsafe-inline'", 'https:'],
    'style-src': ["'self'", "'unsafe-inline'", 'https://fonts.googleapis.com'],
    'font-src': ["'self'", 'https://fonts.gstatic.com', 'data:'],
    'img-src': ["'self'", 'data:', 'https:'],
    'frame-src': ['https://*.googlesyndication.com', 'https://*.google.com',
                  'https://*.doubleclick.net'],
    'connect-src': ["'self'", 'https:'],
    'object-src': "'none'",
    'base-uri': "'self'",
    'frame-ancestors': "'self'",
    'form-action': "'self'",
}
Talisman(
    app,
    content_security_policy=CSP,
    force_https=IS_PROD,
    strict_transport_security=IS_PROD,
    session_cookie_secure=IS_PROD,
    referrer_policy='strict-origin-when-cross-origin',
)


@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('error.html', code=400,
                           message='Your session expired. Please go back and try again.'), 400


# ── HTML sanitisation for admin-entered article content ──
ALLOWED_TAGS = ['h2', 'h3', 'h4', 'p', 'ul', 'ol', 'li', 'strong', 'em', 'b', 'i',
                'u', 'a', 'br', 'blockquote', 'code', 'pre', 'span', 'hr', 'table',
                'thead', 'tbody', 'tr', 'th', 'td']
ALLOWED_ATTRS = {'a': ['href', 'title', 'rel', 'target'], 'span': ['class'],
                 'td': ['colspan', 'rowspan'], 'th': ['colspan', 'rowspan']}


def sanitize_html(raw):
    return bleach.clean(raw or '', tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRS, strip=True)

CONTACT_RECEIVER = os.getenv('CONTACT_RECEIVER', os.getenv('MAIL_USERNAME'))
# Admin credentials live in .env (ADMIN_USERNAME + ADMIN_PW_HASH_B64), never in
# the database — so a database reset can NEVER revert access to a default password.
# There is intentionally NO hardcoded default: if credentials are unset, the admin
# login fails closed (no access until credentials are configured on the server).
ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')

# Google AdSense — set ADSENSE_CLIENT in .env to your publisher id (ca-pub-XXXX).
# Ad slot ids are configured per-placement in ADSENSE_SLOTS below.
ADSENSE_CLIENT = os.getenv('ADSENSE_CLIENT', '')
ADSENSE_SLOTS = {
    'top': os.getenv('ADSENSE_SLOT_TOP', ''),
    'mid': os.getenv('ADSENSE_SLOT_MID', ''),
    'bottom': os.getenv('ADSENSE_SLOT_BOTTOM', ''),
    'article_top': os.getenv('ADSENSE_SLOT_ARTICLE_TOP', ''),
    'article_bottom': os.getenv('ADSENSE_SLOT_ARTICLE_BOTTOM', ''),
}

# Google Search Console — paste the "content" value from the HTML-tag
# verification method into GOOGLE_SITE_VERIFICATION in .env. When set, base.html
# renders <meta name="google-site-verification" ...> so Google can verify the site.
GOOGLE_SITE_VERIFICATION = os.getenv('GOOGLE_SITE_VERIFICATION', '')

VALID_EMAIL_RE = re.compile(r'^[^\s@]+@[^\s@]+\.[^\s@]+$')

# Public base URL of the live site (used for canonical tags, sitemap, OG, JSON-LD).
SITE_URL = os.getenv('SITE_URL', 'https://lawminded.in').rstrip('/')

# ── Named author (E-E-A-T) ──────────────────────────────────────────────────
# Legal content is YMYL, where Google weights demonstrable, *named* authorship
# most heavily. This single block drives the article byline, the Person schema,
# and the /author bio page. Fill CREDENTIAL and SAME_AS with real facts (a held
# qualification such as 'Company Secretary'; the author's own LinkedIn/X) so the
# expertise signal is genuine — never invent a credential.
AUTHOR = {
    'name': 'Piyush Kundnani',
    'slug': 'piyush-kundnani',
    'role': 'Founder & Editor',
    'credential': '',   # e.g. 'Company Secretary' — shown in byline + schema jobTitle
    'bio': ('Piyush Kundnani is the founder and editor of Law Minded, where he '
            'leads its plain-English coverage of Indian corporate compliance, '
            'labour law and consumer rights.'),
    'same_as': [],      # the author\'s OWN professional profiles (personal LinkedIn/X)
}
AUTHOR['url'] = SITE_URL + '/author/' + AUTHOR['slug']

CATEGORY_MAP = C.CATEGORY_MAP

# Signed, tamper-proof tokens for one-click newsletter unsubscribe links.
# itsdangerous ships with Flask, so no new dependency is needed.
_unsub_serializer = URLSafeSerializer(app.secret_key, salt='lm-unsubscribe')


def unsubscribe_url(email):
    """Absolute, signed unsubscribe link for inclusion in outgoing emails."""
    token = _unsub_serializer.dumps(email)
    return f'{SITE_URL}{url_for("unsubscribe")}?token={token}'


# ─── Branded transactional email ─────────────────────────────────────────────
# A single shell keeps every outgoing email on-brand (logo, palette) and
# improves deliverability: real plain-text part, List-Unsubscribe header, and
# an inline (cid:) logo so it shows even when remote images are blocked.
EMAIL_LOGO = 'static/img/logo-horizontal.png'


def _email_html(heading, body_html, unsub=None):
    foot_unsub = (
        '<p style="margin:14px 0 0;font:400 12px/1.6 Arial,sans-serif;color:#A99B78;">'
        'You are receiving this because you subscribed at Law Minded. '
        f'<a href="{unsub}" style="color:#8A5E07;">Unsubscribe</a>.</p>'
    ) if unsub else ''
    return (
        '<!doctype html><html lang="en"><body style="margin:0;padding:0;background:#F4F0E6;">'
        '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" '
        'style="background:#F4F0E6;padding:28px 12px;font-family:Arial,Helvetica,sans-serif;">'
        '<tr><td align="center">'
        '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" '
        'style="max-width:540px;background:#ffffff;border:1px solid #ECE6D8;border-radius:14px;overflow:hidden;">'
        '<tr><td style="height:4px;background:#E8A020;font-size:0;line-height:0;">&nbsp;</td></tr>'
        '<tr><td style="padding:26px 34px 0;">'
        '<img src="cid:logo" alt="LAW MiNDED" width="168" style="display:block;height:auto;border:0;outline:none;text-decoration:none;">'
        '<p style="margin:10px 0 0;font:600 10px/1 Arial,sans-serif;letter-spacing:.16em;'
        'text-transform:uppercase;color:#B7AC8E;">Where complexity meets clarity</p>'
        '</td></tr>'
        '<tr><td style="padding:20px 34px 28px;color:#33302A;">'
        f'<h1 style="margin:0 0 14px;font:700 20px/1.3 Georgia,\'Times New Roman\',serif;color:#1C1B16;">{heading}</h1>'
        f'{body_html}'
        '<hr style="border:0;border-top:1px solid #ECE6D8;margin:22px 0 12px;">'
        '<p style="margin:0;font:400 12px/1.6 Arial,sans-serif;color:#A99B78;">'
        'Law&nbsp;Minded — India\'s free legal-awareness platform.</p>'
        f'{foot_unsub}'
        '</td></tr></table></td></tr></table></body></html>'
    )


def send_branded_email(subject, recipients, heading, body_html, body_text, unsub=None):
    """Build + send a branded HTML email (with plain-text alt + inline logo)."""
    msg = Message(subject=subject, recipients=recipients)
    msg.body = body_text
    msg.html = _email_html(heading, body_html, unsub)
    if CONTACT_RECEIVER:
        msg.reply_to = CONTACT_RECEIVER
    if unsub:
        # RFC 2369 + RFC 8058 one-click unsubscribe — a strong inbox-placement signal.
        msg.extra_headers = {
            'List-Unsubscribe': f'<{unsub}>',
            'List-Unsubscribe-Post': 'List-Unsubscribe=One-Click',
        }
    with app.open_resource(EMAIL_LOGO) as f:
        msg.attach('logo.png', 'image/png', f.read(), 'inline',
                   headers={'Content-ID': '<logo>', 'X-Attachment-Id': 'logo'})
    mail.send(msg)


# ─── Context Processor (globals available in every template) ─────────────────

def asset_version(rel_path):
    """Cache-busting token (file mtime) so browsers always fetch the latest CSS/JS."""
    try:
        return int(os.path.getmtime(os.path.join(app.static_folder, rel_path)))
    except OSError:
        return 1


@app.template_filter('humandate')
def humandate(value):
    """Render a stored timestamp as day-first, e.g. '21 Jun 2026'."""
    if not value:
        return ''
    s = str(value)[:10]
    try:
        from datetime import datetime as _dt
        return _dt.strptime(s, '%Y-%m-%d').strftime('%d %b %Y')
    except ValueError:
        return s


@app.template_filter('iso8601')
def iso8601(value, offset='+05:30'):
    """Render a stored timestamp as valid ISO-8601 for structured data,
    e.g. '2026-06-27T15:26:32+05:30'. Google requires the 'T' separator and a
    timezone designator; the raw SQLite 'YYYY-MM-DD HH:MM:SS' form is invalid.
    The wall-clock value is kept as-is and tagged with the site offset (IST),
    consistent with how humandate renders the same value."""
    if not value:
        return ''
    from datetime import datetime as _dt
    s = str(value).strip().replace('T', ' ')[:19]
    for fmt in ('%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d'):
        try:
            return _dt.strptime(s, fmt).strftime('%Y-%m-%dT%H:%M:%S') + offset
        except ValueError:
            continue
    return str(value)


@app.template_filter('seotitle')
def seotitle(article, brand=' - Law Minded', maxlen=60):
    """Build a search-friendly <title>. Uses the article's explicit seo_title
    when set; otherwise shortens the long editorial headline (preferring the
    lead before a colon, else trimming on a word boundary). The ' - Law Minded'
    suffix is only appended when the whole thing still fits Google's ~60-char
    display width, so titles stop truncating mid-phrase in search results."""
    def _get(row, key):
        try:
            v = row[key]
        except (KeyError, IndexError, TypeError):
            v = None
        return v.strip() if isinstance(v, str) else ''

    title = _get(article, 'seo_title')
    if not title:
        raw = ' '.join(_get(article, 'title').split())
        title = raw
        if ':' in raw:
            lead = raw.split(':', 1)[0].strip()
            if 12 <= len(lead) <= maxlen:
                title = lead
        if len(title) > maxlen:
            cut = title[:maxlen]
            if ' ' in cut:
                cut = cut[:cut.rindex(' ')]
            title = cut.rstrip(' ,;:-–—')
    if brand and len(title) + len(brand) <= maxlen:
        return title + brand
    return title


@app.template_filter('faqs')
def faqs(content, limit=10):
    """Pull (question, answer) pairs from an article's 'Frequently asked
    questions' section for FAQPage schema. Matches the seeded structure:
    an <h2>FAQ</h2> heading followed by <p><strong>Q?</strong> A</p> pairs.
    ponytail: naive regex parse of known-good seeded HTML; re-check if the
    editor ever emits a different FAQ structure."""
    if not content:
        return []
    import re
    m = re.search(
        r'<h2[^>]*>\s*(?:frequently asked questions|common questions|faqs?)\s*</h2>(.*?)(?:<h2|$)',
        content, re.I | re.S)
    if not m:
        return []
    out = []
    for q, a in re.findall(r'<p>\s*<strong>(.*?)</strong>\s*(.*?)</p>', m.group(1), re.S):
        q = re.sub(r'<[^>]+>', '', q).strip()
        a = re.sub(r'<[^>]+>', '', a).strip()
        if q.endswith('?') and a:
            out.append({'q': q, 'a': a})
    return out[:limit]


@app.context_processor
def inject_globals():
    return {
        'adsense_client': ADSENSE_CLIENT,
        'adsense_slots': ADSENSE_SLOTS,
        'google_site_verification': GOOGLE_SITE_VERIFICATION,
        'category_map': CATEGORY_MAP,
        'current_year': date.today().year,
        'site_url': SITE_URL,
        'canonical_url': SITE_URL + request.path,
        'asset_v': asset_version,
        'author': AUTHOR,
    }


# Canonical host: in production, funnel every alternate hostname (www, the
# lawminded.co.in domain, etc.) to the single primary domain from SITE_URL — one
# site for SEO + AdSense. ACME challenges are always let through for cert renewal.
CANONICAL_HOST = SITE_URL.split('://', 1)[-1].split('/', 1)[0].lower()


@app.before_request
def _force_canonical_host():
    if not IS_PROD or request.path.startswith('/.well-known/'):
        return
    host = (request.host or '').split(':')[0].lower()
    if host and host != CANONICAL_HOST and host.endswith(('lawminded.in', 'lawminded.co.in')):
        target = f'https://{CANONICAL_HOST}{request.path}'
        if request.query_string:
            target += '?' + request.query_string.decode()
        return redirect(target, code=301)


# ─── Helpers ────────────────────────────────────────────────────────────────

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    return re.sub(r'[\s_-]+', '-', text)


def get_articles_by_cat():
    db = get_db()
    by_cat = {}
    for cat in CATEGORY_MAP:
        by_cat[cat] = db.execute(
            'SELECT * FROM articles WHERE category=? AND published=1 ORDER BY created_at DESC',
            (cat,)
        ).fetchall()
    db.close()
    return by_cat


def get_all_articles():
    db = get_db()
    rows = db.execute(
        'SELECT * FROM articles WHERE published=1 ORDER BY created_at DESC'
    ).fetchall()
    db.close()
    return rows


def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated


# ─── Documents (DB-managed templates & resolutions) ──────────────────────────
DOC_TYPES = {'template': 'Template', 'board': 'Board Resolution'}
DOC_LIST_TITLE = {'board': 'Board Resolutions'}


def get_documents(doc_type):
    db = get_db()
    rows = db.execute(
        'SELECT * FROM documents WHERE doc_type=? ORDER BY sort_order, id', (doc_type,)
    ).fetchall()
    db.close()
    return rows


def get_document(doc_type, slug):
    db = get_db()
    row = db.execute(
        'SELECT * FROM documents WHERE doc_type=? AND slug=?', (doc_type, slug)
    ).fetchone()
    db.close()
    return row


# ─── Document Formats (uploaded Word files, DB-managed) ──────────────────────
FORMATS_DIR = os.path.join(app.static_folder, 'formats')


def get_formats_grouped():
    """Shape DB format rows into the {name, icon, docs:[{slug,file,title,desc}]}
    structure the Templates page expects, preserving the known category order."""
    db = get_db()
    rows = db.execute('SELECT * FROM formats ORDER BY sort_order, id').fetchall()
    db.close()
    by_cat = {}
    for r in rows:
        by_cat.setdefault(r['category'], []).append(
            {'slug': r['slug'], 'file': r['filename'], 'title': r['title'],
             'desc': r['description'] or ''}
        )
    cats, seen = [], set()
    for name in F.CATEGORY_NAMES:
        if name in by_cat:
            cats.append({'name': name, 'icon': F.CATEGORY_ICONS.get(name, F.DEFAULT_CATEGORY_ICON),
                         'docs': by_cat[name]})
            seen.add(name)
    for name, docs in by_cat.items():
        if name not in seen:
            cats.append({'name': name, 'icon': F.CATEGORY_ICONS.get(name, F.DEFAULT_CATEGORY_ICON),
                         'docs': docs})
    return cats


def get_format(slug):
    db = get_db()
    row = db.execute('SELECT * FROM formats WHERE slug=?', (slug,)).fetchone()
    db.close()
    return row


def formats_count():
    db = get_db()
    n = db.execute('SELECT COUNT(*) FROM formats').fetchone()[0]
    db.close()
    return n


def doc_to_view(d):
    """Shape a DB document row for the public templates/resolutions pages."""
    return dict(
        d,
        desc=d['description'],
        tags=(d['tags'].split(',') if d['tags'] else []),
        html=C.render_resolution_html(C.parse_doc_body(d['body'])),
    )


def get_setting(key):
    db = get_db()
    row = db.execute('SELECT value FROM settings WHERE key=?', (key,)).fetchone()
    db.close()
    return row['value'] if row else None


def set_setting(key, value):
    db = get_db()
    db.execute(
        'INSERT INTO settings (key, value) VALUES (?,?) '
        'ON CONFLICT(key) DO UPDATE SET value=excluded.value',
        (key, value)
    )
    db.commit()
    db.close()


def _set_env_vars(updates):
    """Persist key=value pairs to .env (atomic) and the live process env."""
    lines = []
    if os.path.exists(ENV_PATH):
        with open(ENV_PATH, 'r') as f:
            lines = f.read().splitlines()
    seen, out = set(), []
    for ln in lines:
        key = ln.split('=', 1)[0] if ('=' in ln and not ln.lstrip().startswith('#')) else None
        if key in updates:
            out.append(f'{key}={updates[key]}'); seen.add(key)
        else:
            out.append(ln)
    for k, v in updates.items():
        if k not in seen:
            out.append(f'{k}={v}')
    tmp = ENV_PATH + '.tmp'
    with open(tmp, 'w') as f:
        f.write('\n'.join(out) + '\n')
    os.replace(tmp, ENV_PATH)
    for k, v in updates.items():
        os.environ[k] = v


def _env_value(key):
    """Read a key straight from .env each time, so every gunicorn worker sees a
    credential change immediately (no restart). Falls back to the process env."""
    try:
        with open(ENV_PATH, 'r') as f:
            for ln in f:
                ln = ln.rstrip('\n')
                if ln.startswith(key + '='):
                    return ln.split('=', 1)[1]
    except OSError:
        pass
    return os.getenv(key, '')


def get_admin_username():
    return (_env_value('ADMIN_USERNAME') or '').strip()


def _admin_hash():
    """Admin password hash, stored base64-encoded in .env (keeps the '$'-laden
    hash safe from dotenv variable interpolation)."""
    b64 = _env_value('ADMIN_PW_HASH_B64') or ''
    try:
        return base64.b64decode(b64).decode('utf-8') if b64 else ''
    except Exception:
        return ''


def admin_configured():
    return bool(get_admin_username() and _admin_hash())


def check_admin(username, password):
    """Verify admin username + password. Fails closed — there is no default."""
    u, h = get_admin_username(), _admin_hash()
    if not u or not h:
        return False
    if not hmac.compare_digest((username or '').strip().lower(), u.lower()):
        return False
    return check_password_hash(h, password or '')


def set_admin_credentials(username=None, password=None):
    """Write new admin credentials to .env (password stored only as a hash)."""
    updates = {}
    if username is not None:
        updates['ADMIN_USERNAME'] = username.strip()
    if password is not None:
        h = generate_password_hash(password, method='pbkdf2:sha256')
        updates['ADMIN_PW_HASH_B64'] = base64.b64encode(h.encode('utf-8')).decode('ascii')
    if updates:
        _set_env_vars(updates)


def build_resolution_docx(title, blocks):
    """Build a Word (.docx) document from resolution blocks, returned as BytesIO."""
    from docx import Document
    from docx.shared import Pt

    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Calibri'
    style.font.size = Pt(11)

    for kind, text in blocks:
        if kind == 'spacer':
            doc.add_paragraph('')
        elif kind in ('heading', 'subheading'):
            p = doc.add_paragraph()
            run = p.add_run(text)
            run.bold = True
            if kind == 'heading':
                run.font.size = Pt(12)
        elif kind == 'bullet':
            doc.add_paragraph(text, style='List Bullet')
        else:
            doc.add_paragraph(text)

    bio = BytesIO()
    doc.save(bio)
    bio.seek(0)
    return bio


# ─── Public Pages ─────────────────────────────────────────────────────────────

@app.route('/')
def index():
    articles = get_all_articles()
    featured = articles[:6]
    return render_template('index.html', featured=featured)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/author/<slug>')
def author_page(slug):
    if slug != AUTHOR['slug']:
        abort(404)
    return render_template('author.html', profile=AUTHOR)


@app.route('/blogs')
def blogs():
    return render_template('blogs.html', articles_by_cat=get_articles_by_cat())


@app.route('/article/<slug>')
def article(slug):
    db = get_db()
    row = db.execute(
        'SELECT * FROM articles WHERE slug=? AND published=1', (slug,)
    ).fetchone()
    if not row:
        db.close()
        abort(404)
    related = db.execute(
        'SELECT * FROM articles WHERE category=? AND id!=? AND published=1 ORDER BY created_at DESC LIMIT 4',
        (row['category'], row['id'])
    ).fetchall()
    # Top up to 4 with recent articles from other categories so the row is always full.
    if len(related) < 4:
        seen = {r['id'] for r in related} | {row['id']}
        extra = db.execute(
            'SELECT * FROM articles WHERE published=1 ORDER BY created_at DESC LIMIT 12'
        ).fetchall()
        related = list(related) + [r for r in extra if r['id'] not in seen][:4 - len(related)]
    db.close()
    return render_template('article.html', article=row, related=related)


@app.route('/templates')
def templates_page():
    rendered = [doc_to_view(d) for d in get_documents('template')]
    return render_template('templates_page.html', templates=rendered,
                           format_categories=get_formats_grouped(),
                           formats_count=formats_count())


@app.route('/template/<slug>/download')
def template_download(slug):
    item = get_document('template', slug)
    if not item:
        abort(404)
    bio = build_resolution_docx(item['title'], C.parse_doc_body(item['body']))
    return send_file(
        bio, as_attachment=True, download_name=f'{slug}.docx',
        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )


@app.route('/format/<slug>/download')
def format_download(slug):
    """Serve one of the real .docx document formats from static/formats.

    The slug is looked up in FORMATS_BY_SLUG, so only known filenames are ever
    served (no path-traversal from user input)."""
    item = get_format(slug)
    if not item:
        abort(404)
    folder = os.path.join(app.static_folder, 'formats')
    return send_from_directory(
        folder, item['filename'], as_attachment=True, download_name=item['filename'],
        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )


@lru_cache(maxsize=128)
def _render_format_preview(slug):
    """Render a stored .docx format to safe HTML for the in-page preview modal.

    Returns an HTML fragment (headings, paragraphs, tables) built from our own
    trusted files, with all text escaped. Cached per slug so repeat previews
    don't re-parse the document."""
    item = get_format(slug)
    if not item:
        return None
    from markupsafe import escape
    from docx import Document
    from docx.oxml.ns import qn
    from docx.table import Table as _Tbl
    from docx.text.paragraph import Paragraph as _Para

    doc = Document(os.path.join(app.static_folder, 'formats', item['filename']))

    def runs_html(p):
        parts = []
        for r in p.runs:
            t = str(escape(r.text or ''))
            if not t:
                continue
            if r.bold:
                t = f'<strong>{t}</strong>'
            if r.italic:
                t = f'<em>{t}</em>'
            parts.append(t)
        return ''.join(parts) if parts else str(escape(p.text or ''))

    def cell_html(cell):
        bits = [runs_html(p) for p in cell.paragraphs if p.text.strip()]
        return '<br>'.join(bits)

    out = []
    for child in doc.element.body.iterchildren():
        if child.tag == qn('w:p'):
            p = _Para(child, doc)
            txt = runs_html(p)
            if not txt.strip():
                continue
            style = (p.style.name if p.style else '') or ''
            tag = 'h4' if (style.startswith('Heading') or style.startswith('Title')) else 'p'
            out.append(f'<{tag}>{txt}</{tag}>')
        elif child.tag == qn('w:tbl'):
            tbl = _Tbl(child, doc)
            rows = ''.join(
                '<tr>' + ''.join(f'<td>{cell_html(c)}</td>' for c in row.cells) + '</tr>'
                for row in tbl.rows
            )
            if rows:
                out.append(f'<table class="preview-table"><tbody>{rows}</tbody></table>')
    return '\n'.join(out)


@app.route('/format/<slug>/preview')
def format_preview(slug):
    html_out = _render_format_preview(slug)
    if html_out is None:
        abort(404)
    return html_out


@app.route('/compare')
def compare():
    return render_template('compare.html')


@app.route('/judgments')
def judgments():
    return render_template('judgments.html', judgments=C.JUDGMENTS)


@app.route('/judgment/<slug>')
def judgment(slug):
    j = next((x for x in C.JUDGMENTS if x['slug'] == slug), None)
    if not j:
        abort(404)
    return render_template('judgment.html', j=j)


@app.route('/resolutions/<rtype>')
def resolutions(rtype):
    if rtype not in DOC_LIST_TITLE:
        abort(404)
    rendered = [doc_to_view(d) for d in get_documents(rtype)]
    return render_template('resolutions.html', rtype=rtype,
                           list_title=DOC_LIST_TITLE[rtype], items=rendered)


@app.route('/resolution/<rtype>/<slug>/download')
def resolution_download(rtype, slug):
    if rtype not in DOC_LIST_TITLE:
        abort(404)
    item = get_document(rtype, slug)
    if not item:
        abort(404)
    bio = build_resolution_docx(item['title'], C.parse_doc_body(item['body']))
    return send_file(
        bio, as_attachment=True, download_name=f'{slug}.docx',
        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )


@app.route('/resources')
def resources():
    return render_template('resources.html', resources=C.RESOURCES)


@app.route('/faq')
def faq():
    return render_template('faq.html', faqs=C.FAQS)


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/terms')
def terms():
    return render_template('terms.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


@app.route('/search')
def search():
    query = request.args.get('q', '').strip()
    results = C.search_all(query, get_all_articles()) if query else []
    if query:
        q = query.lower()
        db = get_db()
        docs = db.execute('SELECT * FROM documents').fetchall()
        db.close()
        for d in docs:
            hay = ' '.join(str(d[k] or '') for k in ('title', 'description', 'tags', 'body')).lower()
            if q in hay:
                if d['doc_type'] == 'template':
                    results.append({'type': 'Template', 'title': f"{d['icon']} {d['title']}",
                                    'snippet': d['description'], 'url_kind': 'page', 'url_arg': 'templates_page'})
                elif d['doc_type'] in DOC_LIST_TITLE:
                    results.append({'type': DOC_TYPES.get(d['doc_type'], 'Document'), 'title': d['title'],
                                    'snippet': d['description'], 'url_kind': 'resolutions', 'url_arg': d['doc_type']})
    return render_template('search.html', query=query, results=results)


# ─── Form / API Endpoints ─────────────────────────────────────────────────────

@app.route('/contact', methods=['POST'])
@limiter.limit('6 per minute')
def contact():
    # Honeypot: real users never fill the hidden "website" field; bots do.
    if request.form.get('website', '').strip():
        return jsonify({'success': True, 'message': 'Your query has been submitted successfully!'})

    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    query = request.form.get('query', '').strip()

    errors = {}
    if not name:
        errors['name'] = 'Name is required.'
    if not email or not VALID_EMAIL_RE.match(email):
        errors['email'] = 'Valid email is required.'
    if not query or len(query) < 20:
        errors['query'] = 'Please describe your query (at least 20 characters).'

    if errors:
        return jsonify({'success': False, 'errors': errors}), 400

    db = get_db()
    db.execute(
        'INSERT INTO contact_messages (name, email, query) VALUES (?,?,?)',
        (name, email, query)
    )
    db.commit()
    db.close()

    try:
        # Internal notification to the team (reply goes straight to the sender).
        notify = Message(
            subject=f'New enquiry from {name} — Law Minded',
            recipients=[CONTACT_RECEIVER],
            body=f'Name: {name}\nEmail: {email}\n\nMessage:\n{query}'
        )
        notify.reply_to = email
        mail.send(notify)
        # Branded acknowledgement to the person who wrote in.
        send_branded_email(
            subject='We received your message — Law Minded',
            recipients=[email],
            heading=f'Thanks, {name} — we have your message',
            body_html=(
                '<p style="margin:0 0 12px;font:400 15px/1.65 Arial,sans-serif;">'
                'Thanks for reaching out to Law Minded. We have received your message '
                'and will get back to you as soon as we can.</p>'
                '<p style="margin:0;font:400 15px/1.65 Arial,sans-serif;color:#6F6857;">'
                'You can simply reply to this email if you have anything to add.</p>'
            ),
            body_text=(
                f'Hi {name},\n\n'
                'Thanks for reaching out to Law Minded. We have received your message '
                'and will get back to you as soon as we can.\n\n'
                '— Law Minded'
            ),
        )
    except Exception:
        pass

    return jsonify({'success': True, 'message': 'Your query has been submitted successfully!'})


@app.route('/newsletter', methods=['POST'])
@limiter.limit('6 per minute')
def newsletter():
    if request.form.get('website', '').strip():
        return jsonify({'success': True, 'message': "Thank you! You've been subscribed."})

    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()

    if not email or not VALID_EMAIL_RE.match(email):
        return jsonify({'success': False, 'message': 'Please enter a valid email address.'}), 400

    db = get_db()
    try:
        db.execute('INSERT INTO subscribers (name, email) VALUES (?,?)', (name, email))
        db.commit()
    except sqlite3.IntegrityError:
        db.close()
        return jsonify({'success': True, 'message': "You're already subscribed!"})
    db.close()

    try:
        unsub = unsubscribe_url(email)
        hi = name or 'there'
        hub = f'{SITE_URL}{url_for("blogs")}'
        send_branded_email(
            subject='Welcome to Law Minded',
            recipients=[email],
            heading=f'Welcome, {hi}',
            body_html=(
                '<p style="margin:0 0 12px;font:400 15px/1.65 Arial,sans-serif;">'
                'You are now subscribed — thank you for joining.</p>'
                '<p style="margin:0 0 12px;font:400 15px/1.65 Arial,sans-serif;">'
                'From time to time we will send plain-English updates on compliance changes, '
                'new guides, and important court judgments. Nothing more, and nothing you did not sign up for.</p>'
                '<p style="margin:0;font:400 15px/1.65 Arial,sans-serif;">'
                f'In the meantime, browse our free <a href="{hub}" style="color:#8A5E07;">Knowledge Hub</a> '
                'for guides written for founders, professionals, and everyday citizens.</p>'
            ),
            body_text=(
                f'Hi {hi},\n\n'
                'You are now subscribed to Law Minded — thank you for joining.\n\n'
                'From time to time we will send plain-English updates on compliance changes, '
                'new guides, and important court judgments.\n\n'
                f'Browse our free Knowledge Hub: {hub}\n\n'
                '— Law Minded\n\n'
                f'Unsubscribe anytime: {unsub}'
            ),
            unsub=unsub,
        )
    except Exception:
        pass

    return jsonify({'success': True, 'message': f'Thank you{", " + name if name else ""}! You\'ve been subscribed.'})


@app.route('/unsubscribe', methods=['GET', 'POST'])
@csrf.exempt
def unsubscribe():
    """Unsubscribe via a signed token.

    GET only shows a confirmation page with an "Unsubscribe" button — visiting the
    link never removes anyone. The removal happens on POST: either the in-page
    button, or the RFC 8058 one-click path that Gmail/Outlook fire automatically
    from the List-Unsubscribe header (identified by the List-Unsubscribe=One-Click
    body field, which the button submit does not send)."""
    token = request.values.get('token', '')
    try:
        email = _unsub_serializer.loads(token)
    except BadSignature:
        email = None

    # A plain visit changes nothing — just ask the person to confirm.
    if request.method == 'GET':
        return render_template('unsubscribe.html', email=email, token=token,
                               removed=False, confirm=bool(email), valid=bool(email))

    # POST: actually remove them.
    removed = False
    if email:
        db = get_db()
        cur = db.execute('DELETE FROM subscribers WHERE email=?', (email,))
        db.commit()
        removed = cur.rowcount > 0
        db.close()

    # Mail-client one-click (RFC 8058) expects a bare 2xx with no page body.
    if request.form.get('List-Unsubscribe') == 'One-Click':
        return ('', 204)

    return render_template('unsubscribe.html', email=email, token=token,
                           removed=removed, confirm=False, valid=bool(email))


@app.route('/download-request', methods=['POST'])
@limiter.limit('20 per minute')
def download_request():
    email = request.form.get('email', '').strip()
    template_name = request.form.get('template', '').strip()

    if email and VALID_EMAIL_RE.match(email):
        db = get_db()
        db.execute(
            'INSERT INTO download_requests (email, template_name) VALUES (?,?)',
            (email, template_name)
        )
        try:
            db.execute('INSERT INTO subscribers (name, email) VALUES (?,?)', ('', email))
        except sqlite3.IntegrityError:
            pass
        db.commit()
        db.close()

    return jsonify({'success': True, 'message': 'Download ready!'})


@app.route('/uploads/templates/<filename>')
def serve_template(filename):
    return send_from_directory(
        os.path.join(app.root_path, 'static', 'uploads', 'templates'),
        filename
    )


@app.route('/ads.txt')
def ads_txt():
    # Required by Google AdSense to authorise this site to show your ads.
    if not ADSENSE_CLIENT:
        abort(404)
    pub = ADSENSE_CLIENT.replace('ca-', '')
    line = f'google.com, {pub}, DIRECT, f08c47fec0942fa0\n'
    return app.response_class(line, mimetype='text/plain')


@app.route('/robots.txt')
def robots_txt():
    lines = [
        'User-agent: *',
        'Allow: /',
        'Disallow: /admin',
        'Disallow: /admin/',
        f'Sitemap: {SITE_URL}/sitemap.xml',
        '',
    ]
    return app.response_class('\n'.join(lines), mimetype='text/plain')


@app.route('/sitemap')
def sitemap_page():
    # Human-readable HTML site map (this is what the footer "Sitemap" link opens).
    # Distinct from the machine-readable /sitemap.xml below, which is for search engines.
    return render_template('sitemap.html', judgments=C.JUDGMENTS)


@app.route('/sitemap.xml')
def sitemap_xml():
    # Static pages
    pages = [
        ('index', 'weekly', '1.0'),
        ('about', 'monthly', '0.7'),
        ('blogs', 'daily', '0.9'),
        ('templates_page', 'weekly', '0.8'),
        ('compare', 'monthly', '0.7'),
        ('judgments', 'monthly', '0.7'),
        ('resources', 'monthly', '0.6'),
        ('faq', 'monthly', '0.7'),
        ('contact_page', 'yearly', '0.5'),
        ('terms', 'yearly', '0.3'),
        ('privacy', 'yearly', '0.3'),
        ('sitemap_page', 'yearly', '0.3'),
    ]
    urls = []
    for endpoint, freq, prio in pages:
        urls.append((SITE_URL + url_for(endpoint), freq, prio, None))

    # Author bio page (E-E-A-T)
    urls.append((AUTHOR['url'], 'yearly', '0.4', None))

    # Resolution library pages
    for rtype in DOC_LIST_TITLE:
        urls.append((SITE_URL + url_for('resolutions', rtype=rtype), 'monthly', '0.6', None))

    # Landmark judgment briefs
    for jd in C.JUDGMENTS:
        urls.append((SITE_URL + url_for('judgment', slug=jd['slug']), 'monthly', '0.6', None))

    # Published articles (with last-modified)
    db = get_db()
    rows = db.execute(
        'SELECT slug, updated_at FROM articles WHERE published=1 ORDER BY updated_at DESC'
    ).fetchall()
    db.close()
    for r in rows:
        lastmod = (r['updated_at'] or '')[:10] or None
        urls.append((SITE_URL + url_for('article', slug=r['slug']), 'monthly', '0.8', lastmod))

    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, freq, prio, lastmod in urls:
        xml.append('  <url>')
        xml.append(f'    <loc>{loc}</loc>')
        if lastmod:
            xml.append(f'    <lastmod>{lastmod}</lastmod>')
        xml.append(f'    <changefreq>{freq}</changefreq>')
        xml.append(f'    <priority>{prio}</priority>')
        xml.append('  </url>')
    xml.append('</urlset>')
    return app.response_class('\n'.join(xml), mimetype='application/xml')


@app.route('/llms.txt')
def llms_txt():
    """AI-search discovery file (llmstxt.org): a clean, linked index of the
    site's guides so ChatGPT/Perplexity/AI Overviews can find and cite them."""
    from itertools import groupby
    db = get_db()
    rows = db.execute(
        'SELECT slug,title,summary,category FROM articles WHERE published=1 '
        'ORDER BY category,title'
    ).fetchall()
    db.close()
    out = [
        '# Law Minded',
        '',
        "> India's plain-English legal and compliance platform — corporate "
        'compliance, labour law, consumer rights and constitutional law, '
        'explained simply for founders, professionals and citizens.',
        '',
        '## Key pages',
        f'- [Knowledge Hub]({SITE_URL}/blogs): every guide, by topic',
        f'- [Free templates]({SITE_URL}/templates): ready-to-use legal document formats',
        f'- [Landmark judgments]({SITE_URL}/judgments): plain-English case summaries',
        f'- [FAQ]({SITE_URL}/faq)',
        '',
    ]
    for cat, items in groupby(rows, key=lambda r: r['category']):
        out.append(f'## {CATEGORY_MAP.get(cat, (cat or "Guides").title())}')
        for r in items:
            summ = ' '.join((r['summary'] or '').split())[:140]
            out.append(f'- [{r["title"]}]({SITE_URL}/article/{r["slug"]})'
                       + (f': {summ}' if summ else ''))
        out.append('')
    return app.response_class('\n'.join(out), mimetype='text/plain; charset=utf-8')


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


# ─── Admin Routes ────────────────────────────────────────────────────────────

@app.route('/admin/login', methods=['GET', 'POST'])
@limiter.limit('10 per minute; 40 per hour', methods=['POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        if check_admin(username, password):
            session.clear()                      # rotate session on login (anti-fixation)
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        flash('Incorrect username or password.', 'error')
    return render_template('admin/login.html')


@app.route('/admin/password', methods=['GET', 'POST'])
@admin_required
def admin_password():
    if request.method == 'POST':
        current = request.form.get('current', '')
        new_username = request.form.get('username', '').strip()
        new = request.form.get('new', '')
        confirm = request.form.get('confirm', '')
        cur_hash = _admin_hash()
        if not cur_hash or not check_password_hash(cur_hash, current):
            flash('Your current password is incorrect.', 'error')
        elif new_username and not re.fullmatch(r'[A-Za-z0-9._-]{3,40}', new_username):
            flash('Username must be 3–40 characters (letters, numbers, . _ - only).', 'error')
        elif len(new) < 8:
            flash('New password must be at least 8 characters.', 'error')
        elif new != confirm:
            flash('New password and confirmation do not match.', 'error')
        else:
            set_admin_credentials(username=new_username or get_admin_username(), password=new)
            flash('Admin credentials updated successfully.', 'success')
            return redirect(url_for('admin_dashboard'))
    return render_template('admin/password.html', admin_username=get_admin_username())


@app.route('/admin/logout')
def admin_logout():
    session.clear()
    return redirect(url_for('admin_login'))


@app.route('/admin')
@admin_required
def admin_dashboard():
    db = get_db()
    stats = {
        'articles': db.execute('SELECT COUNT(*) FROM articles').fetchone()[0],
        'published': db.execute('SELECT COUNT(*) FROM articles WHERE published=1').fetchone()[0],
        'subscribers': db.execute('SELECT COUNT(*) FROM subscribers').fetchone()[0],
        'messages': db.execute('SELECT COUNT(*) FROM contact_messages').fetchone()[0],
    }
    recent_messages = db.execute(
        'SELECT * FROM contact_messages ORDER BY created_at DESC LIMIT 5'
    ).fetchall()
    db.close()
    return render_template('admin/dashboard.html', stats=stats, recent_messages=recent_messages)


@app.route('/admin/articles')
@admin_required
def admin_articles():
    db = get_db()
    articles = db.execute('SELECT * FROM articles ORDER BY created_at DESC').fetchall()
    db.close()
    return render_template('admin/articles.html', articles=articles)


@app.route('/admin/articles/new', methods=['GET', 'POST'])
@admin_required
def admin_article_new():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        category = request.form.get('category', '').strip()
        act = request.form.get('act', '').strip()
        read_time = request.form.get('read_time', '').strip()
        summary = request.form.get('summary', '').strip()
        seo_title = request.form.get('seo_title', '').strip()
        content_html = sanitize_html(request.form.get('content', '').strip())
        published = 1 if request.form.get('published') else 0
        slug = slugify(title)

        db = get_db()
        base_slug = slug
        i = 1
        while db.execute('SELECT id FROM articles WHERE slug=?', (slug,)).fetchone():
            slug = f'{base_slug}-{i}'
            i += 1
        db.execute(
            'INSERT INTO articles (title, slug, category, act, read_time, summary, seo_title, content, published) VALUES (?,?,?,?,?,?,?,?,?)',
            (title, slug, category, act, read_time, summary, seo_title, content_html, published)
        )
        db.commit()
        db.close()
        flash('Article created successfully.', 'success')
        return redirect(url_for('admin_articles'))

    return render_template('admin/article_edit.html', article=None)


@app.route('/admin/articles/<int:article_id>/edit', methods=['GET', 'POST'])
@admin_required
def admin_article_edit(article_id):
    db = get_db()
    art = db.execute('SELECT * FROM articles WHERE id=?', (article_id,)).fetchone()
    if not art:
        db.close()
        abort(404)

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        category = request.form.get('category', '').strip()
        act = request.form.get('act', '').strip()
        read_time = request.form.get('read_time', '').strip()
        summary = request.form.get('summary', '').strip()
        seo_title = request.form.get('seo_title', '').strip()
        content_html = sanitize_html(request.form.get('content', '').strip())
        published = 1 if request.form.get('published') else 0
        db.execute(
            '''UPDATE articles SET title=?, category=?, act=?, read_time=?, summary=?,
               seo_title=?, content=?, published=?, updated_at=CURRENT_TIMESTAMP WHERE id=?''',
            (title, category, act, read_time, summary, seo_title, content_html, published, article_id)
        )
        db.commit()
        db.close()
        flash('Article updated successfully.', 'success')
        return redirect(url_for('admin_articles'))

    db.close()
    return render_template('admin/article_edit.html', article=art)


@app.route('/admin/articles/<int:article_id>/delete', methods=['POST'])
@admin_required
def admin_article_delete(article_id):
    db = get_db()
    db.execute('DELETE FROM articles WHERE id=?', (article_id,))
    db.commit()
    db.close()
    flash('Article deleted.', 'success')
    return redirect(url_for('admin_articles'))


@app.route('/admin/subscribers')
@admin_required
def admin_subscribers():
    db = get_db()
    subscribers = db.execute('SELECT * FROM subscribers ORDER BY created_at DESC').fetchall()
    db.close()
    return render_template('admin/subscribers.html', subscribers=subscribers)


@app.route('/admin/subscribers/add', methods=['POST'])
@admin_required
def admin_subscriber_add():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    if not email or not VALID_EMAIL_RE.match(email):
        flash('Please enter a valid email address.', 'error')
        return redirect(url_for('admin_subscribers'))
    db = get_db()
    try:
        db.execute('INSERT INTO subscribers (name, email) VALUES (?,?)', (name, email))
        db.commit()
        flash(f'Subscriber {email} added.', 'success')
    except sqlite3.IntegrityError:
        flash(f'{email} is already subscribed.', 'error')
    db.close()
    return redirect(url_for('admin_subscribers'))


@app.route('/admin/subscribers/<int:sub_id>/delete', methods=['POST'])
@admin_required
def admin_subscriber_delete(sub_id):
    db = get_db()
    db.execute('DELETE FROM subscribers WHERE id=?', (sub_id,))
    db.commit()
    db.close()
    flash('Subscriber removed.', 'success')
    return redirect(url_for('admin_subscribers'))


@app.route('/admin/subscribers/export')
@admin_required
def admin_subscribers_export():
    """Download all subscribers as a real .xlsx (opens directly in Excel)."""
    db = get_db()
    rows = db.execute(
        'SELECT name, email, created_at FROM subscribers ORDER BY created_at DESC'
    ).fetchall()
    db.close()

    from openpyxl import Workbook
    from openpyxl.styles import Font
    wb = Workbook()
    ws = wb.active
    ws.title = 'Subscribers'
    ws.append(['Name', 'Email', 'Subscribed On'])
    for col in ('A1', 'B1', 'C1'):
        ws[col].font = Font(bold=True)
    for r in rows:
        ws.append([r['name'] or '', r['email'], (str(r['created_at'])[:19] if r['created_at'] else '')])
    ws.column_dimensions['A'].width = 24
    ws.column_dimensions['B'].width = 36
    ws.column_dimensions['C'].width = 22
    ws.freeze_panes = 'A2'

    bio = BytesIO()
    wb.save(bio)
    bio.seek(0)
    fname = f'lawminded-subscribers-{date.today().isoformat()}.xlsx'
    return send_file(
        bio, as_attachment=True, download_name=fname,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )


@app.route('/admin/messages')
@admin_required
def admin_messages():
    db = get_db()
    messages = db.execute('SELECT * FROM contact_messages ORDER BY created_at DESC').fetchall()
    db.close()
    return render_template('admin/messages.html', messages=messages)


# ─── Admin: Documents (templates & resolutions) ──────────────────────────────

RESOLUTION_TYPES = ('board',)


def _doc_home(doc_type):
    """Which admin listing a document belongs to, based on its type."""
    return 'admin_resolutions' if doc_type in RESOLUTION_TYPES else 'admin_documents'


@app.route('/admin/documents')
@admin_required
def admin_documents():
    db = get_db()
    docs = db.execute(
        "SELECT * FROM documents WHERE doc_type='template' ORDER BY sort_order, id"
    ).fetchall()
    db.close()
    return render_template(
        'admin/documents.html',
        grouped={'template': list(docs)},
        doc_types={'template': DOC_TYPES['template']},
        admin_section='templates',
        page_title='Templates',
        page_intro='Manage your downloadable document templates. Changes appear on the site instantly.',
        new_label='+ New Template',
        new_default_type='template',
    )


@app.route('/admin/resolutions')
@admin_required
def admin_resolutions():
    db = get_db()
    placeholders = ','.join('?' * len(RESOLUTION_TYPES))
    docs = db.execute(
        f"SELECT * FROM documents WHERE doc_type IN ({placeholders}) "
        "ORDER BY doc_type, sort_order, id", RESOLUTION_TYPES
    ).fetchall()
    db.close()
    grouped = {k: [] for k in RESOLUTION_TYPES}
    for d in docs:
        grouped.setdefault(d['doc_type'], []).append(d)
    return render_template(
        'admin/documents.html',
        grouped=grouped,
        doc_types={k: DOC_TYPES[k] for k in RESOLUTION_TYPES},
        admin_section='resolutions',
        page_title='Resolutions',
        page_intro='Manage your Board resolutions. Changes appear on the site instantly.',
        new_label='+ New Resolution',
        new_default_type='board',
    )


def _save_document(form, doc_id=None):
    doc_type = form.get('doc_type', '').strip()
    title = form.get('title', '').strip()
    icon = form.get('icon', '').strip() or '📄'
    description = form.get('description', '').strip()
    tags = ','.join([t.strip() for t in form.get('tags', '').split(',') if t.strip()])
    body = form.get('body', '').strip()
    if doc_type not in DOC_TYPES or not title or not body:
        return None, 'Type, title and body are required.'
    db = get_db()
    base = slugify(title) or 'document'
    slug = base
    i = 1
    while True:
        clash = db.execute(
            'SELECT id FROM documents WHERE doc_type=? AND slug=? AND id IS NOT ?',
            (doc_type, slug, doc_id)
        ).fetchone()
        if not clash:
            break
        slug = f'{base}-{i}'; i += 1
    if doc_id:
        db.execute(
            'UPDATE documents SET doc_type=?, slug=?, icon=?, title=?, description=?, tags=?, body=?, '
            'updated_at=CURRENT_TIMESTAMP WHERE id=?',
            (doc_type, slug, icon, title, description, tags, body, doc_id)
        )
    else:
        order = db.execute('SELECT COALESCE(MAX(sort_order),0)+1 FROM documents WHERE doc_type=?',
                           (doc_type,)).fetchone()[0]
        db.execute(
            'INSERT INTO documents (doc_type, slug, icon, title, description, tags, body, sort_order) '
            'VALUES (?,?,?,?,?,?,?,?)',
            (doc_type, slug, icon, title, description, tags, body, order)
        )
    db.commit()
    db.close()
    return True, None


@app.route('/admin/documents/new', methods=['GET', 'POST'])
@admin_required
def admin_document_new():
    if request.method == 'POST':
        ok, err = _save_document(request.form)
        if ok:
            flash('Document created.', 'success')
            return redirect(url_for(_doc_home(request.form.get('doc_type', ''))))
        flash(err, 'error')
    default_type = request.form.get('doc_type') or request.args.get('type') or 'template'
    return render_template('admin/document_edit.html', doc=None, doc_types=DOC_TYPES,
                           default_type=default_type,
                           admin_section=('resolutions' if default_type in RESOLUTION_TYPES else 'templates'))


@app.route('/admin/documents/<int:doc_id>/edit', methods=['GET', 'POST'])
@admin_required
def admin_document_edit(doc_id):
    db = get_db()
    doc = db.execute('SELECT * FROM documents WHERE id=?', (doc_id,)).fetchone()
    db.close()
    if not doc:
        abort(404)
    if request.method == 'POST':
        ok, err = _save_document(request.form, doc_id=doc_id)
        if ok:
            flash('Document updated.', 'success')
            return redirect(url_for(_doc_home(request.form.get('doc_type', doc['doc_type']))))
        flash(err, 'error')
    return render_template('admin/document_edit.html', doc=doc, doc_types=DOC_TYPES,
                           default_type=doc['doc_type'],
                           admin_section=('resolutions' if doc['doc_type'] in RESOLUTION_TYPES else 'templates'))


@app.route('/admin/documents/<int:doc_id>/delete', methods=['POST'])
@admin_required
def admin_document_delete(doc_id):
    db = get_db()
    row = db.execute('SELECT doc_type FROM documents WHERE id=?', (doc_id,)).fetchone()
    db.execute('DELETE FROM documents WHERE id=?', (doc_id,))
    db.commit()
    db.close()
    flash('Document deleted.', 'success')
    return redirect(url_for(_doc_home(row['doc_type']) if row else 'admin_documents'))


# ─── Admin: Document Formats (uploaded Word files) ───────────────────────────
ALLOWED_FORMAT_EXTS = {'.docx'}


@app.route('/admin/formats')
@admin_required
def admin_formats():
    db = get_db()
    rows = db.execute('SELECT * FROM formats ORDER BY sort_order, id').fetchall()
    db.close()
    by_cat = {}
    for r in rows:
        by_cat.setdefault(r['category'], []).append(r)
    grouped = {}
    for name in F.CATEGORY_NAMES:
        if name in by_cat:
            grouped[name] = by_cat[name]
    for name, items in by_cat.items():
        grouped.setdefault(name, items)
    return render_template('admin/formats.html', grouped=grouped, categories=F.CATEGORY_NAMES)


def _save_format(form, files, fmt_id=None, existing=None):
    category = form.get('category', '').strip()
    title = form.get('title', '').strip()
    description = form.get('description', '').strip()
    if not category or not title:
        return None, 'Category and title are required.'
    filename = existing['filename'] if existing else None
    upload = files.get('docfile')
    if upload and upload.filename:
        if os.path.splitext(upload.filename)[1].lower() not in ALLOWED_FORMAT_EXTS:
            return None, 'Only Word (.docx) files can be uploaded.'
        base = secure_filename(os.path.splitext(upload.filename)[0]) or 'document'
        fname = f'{base}.docx'
        os.makedirs(FORMATS_DIR, exist_ok=True)
        i = 1
        while os.path.exists(os.path.join(FORMATS_DIR, fname)):
            fname = f'{base}-{i}.docx'
            i += 1
        upload.save(os.path.join(FORMATS_DIR, fname))
        filename = fname
    if not filename:
        return None, 'Please choose a Word (.docx) file to upload.'
    db = get_db()
    base_slug = slugify(title) or 'document'
    slug = base_slug
    i = 1
    while db.execute('SELECT id FROM formats WHERE slug=? AND id IS NOT ?', (slug, fmt_id)).fetchone():
        slug = f'{base_slug}-{i}'
        i += 1
    if fmt_id:
        db.execute(
            'UPDATE formats SET category=?, slug=?, title=?, description=?, filename=?, '
            'updated_at=CURRENT_TIMESTAMP WHERE id=?',
            (category, slug, title, description, filename, fmt_id)
        )
    else:
        order = db.execute('SELECT COALESCE(MAX(sort_order),0)+1 FROM formats').fetchone()[0]
        db.execute(
            'INSERT INTO formats (category, slug, title, description, filename, sort_order) '
            'VALUES (?,?,?,?,?,?)',
            (category, slug, title, description, filename, order)
        )
    db.commit()
    db.close()
    _render_format_preview.cache_clear()
    return True, None


@app.route('/admin/formats/new', methods=['GET', 'POST'])
@admin_required
def admin_format_new():
    if request.method == 'POST':
        ok, err = _save_format(request.form, request.files)
        if ok:
            flash('Document uploaded.', 'success')
            return redirect(url_for('admin_formats'))
        flash(err, 'error')
    return render_template('admin/format_edit.html', fmt=None, categories=F.CATEGORY_NAMES)


@app.route('/admin/formats/<int:fmt_id>/edit', methods=['GET', 'POST'])
@admin_required
def admin_format_edit(fmt_id):
    db = get_db()
    fmt = db.execute('SELECT * FROM formats WHERE id=?', (fmt_id,)).fetchone()
    db.close()
    if not fmt:
        abort(404)
    if request.method == 'POST':
        ok, err = _save_format(request.form, request.files, fmt_id=fmt_id, existing=fmt)
        if ok:
            flash('Document updated.', 'success')
            return redirect(url_for('admin_formats'))
        flash(err, 'error')
    return render_template('admin/format_edit.html', fmt=fmt, categories=F.CATEGORY_NAMES)


@app.route('/admin/formats/<int:fmt_id>/delete', methods=['POST'])
@admin_required
def admin_format_delete(fmt_id):
    db = get_db()
    db.execute('DELETE FROM formats WHERE id=?', (fmt_id,))
    db.commit()
    db.close()
    _render_format_preview.cache_clear()
    flash('Document deleted.', 'success')
    return redirect(url_for('admin_formats'))


# ─── App Init ────────────────────────────────────────────────────────────────

with app.app_context():
    init_db()
    seed_articles()
    seed_documents()
    seed_formats()

if __name__ == '__main__':
    # PORT lets the dev preview pick a free port; defaults to 8000 locally.
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', '8000')), debug=not IS_PROD)
