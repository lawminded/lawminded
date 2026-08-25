#!/usr/bin/env python3
"""Generate an article hero image with Gemini, sized to match the existing ones.

    python3 automation/gen_image.py <slug> "<image prompt>" ["stock search terms"]
    python3 automation/gen_image.py --self-check     # no API call, no credits

Writes static/img/articles/<slug>.webp at 1200x630 — the size app.py's
_article_image_url helper expects, and the size og:image wants.

Runs on the Mac only. GEMINI_API_KEY lives in the local .env and never goes near
the server; images are committed as static WebP and deployed with the code.
Billing must be enabled on the Google project — the free tier returns limit: 0
for image generation. When it is not, this falls back to a licensed photograph
from Pexels (set PEXELS_API_KEY), whose licence allows commercial use and
modification without attribution. It does not fall back to a general web image:
those are somebody's copyright, and this site is monetised.
"""
import base64
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from io import BytesIO

from PIL import Image, ImageOps

# Google retires gemini-2.5-flash-image on 2 October 2026. Overridable so the
# successor can be dropped in from .env without a code change and without anyone
# having to remember where the name was written down.
MODEL = os.getenv('GEMINI_IMAGE_MODEL', 'gemini-2.5-flash-image')
ENDPOINT = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent'
SIZE = (1200, 630)

# What the existing article images look like, so a new one does not stand out.
STYLE = ('Editorial photograph for a legal-awareness article. Warm natural light, '
         'muted cream and charcoal palette with soft gold accents, shallow depth of '
         'field, calm and professional. Indian context. No text, no words, no '
         'lettering, no logos, no government seals or emblems, no watermarks, no '
         'recognisable branding. Photographic, not an illustration or 3D render.')


def _api_key():
    key = os.getenv('GEMINI_API_KEY')
    if not key:
        from dotenv import load_dotenv
        load_dotenv()
        key = os.getenv('GEMINI_API_KEY')
    if not key:
        sys.exit('GEMINI_API_KEY is not set (expected in .env of the main checkout).')
    return key


def generate(subject):
    """Ask Gemini for one image and return the raw bytes."""
    body = json.dumps({
        'contents': [{'parts': [{'text': f'{subject.strip()}\n\n{STYLE}'}]}],
        'generationConfig': {
            'responseModalities': ['IMAGE'],
            'imageConfig': {'aspectRatio': '16:9'},
        },
    }).encode()
    req = urllib.request.Request(
        ENDPOINT, data=body,
        headers={'Content-Type': 'application/json', 'x-goog-api-key': _api_key()})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            payload = json.load(r)
    except urllib.error.HTTPError as e:
        detail = e.read().decode('utf-8', 'replace')[:400]
        sys.exit(f'Gemini returned HTTP {e.code}: {detail}')

    for part in payload.get('candidates', [{}])[0].get('content', {}).get('parts', []):
        blob = part.get('inlineData') or part.get('inline_data')
        if blob and blob.get('data'):
            return base64.b64decode(blob['data'])
    # A safety block comes back as a well-formed response with no image in it.
    sys.exit(f'No image in the response: {json.dumps(payload)[:400]}')


# Pexels: free API, and its licence permits commercial use and modification with
# no attribution required. That last part matters — a general web image is almost
# certainly someone's copyright, and putting one on a monetised legal-compliance
# site is exactly the risk this site exists to warn people about.
PEXELS_SEARCH = 'https://api.pexels.com/v1/search'

# Pexels answers 403 to urllib's default "Python-urllib/3.x" while the identical
# request from curl succeeds. Identify the caller properly — this is a real site
# making real requests, and saying so is also just good manners to an API being
# given away for free.
UA = {'User-Agent': 'LawMindedBot/1.0 (+https://lawminded.in)'}


def _pexels_key():
    key = os.getenv('PEXELS_API_KEY')
    if not key:
        from dotenv import load_dotenv
        load_dotenv()
        key = os.getenv('PEXELS_API_KEY')
    return key


def fetch_stock(query, orientation='landscape'):
    """A licensed photograph matching the query, as raw bytes. Returns None rather
    than raising when there is no key or no match, so callers can fall through to
    the next option."""
    key = _pexels_key()
    if not key:
        return None
    url = f'{PEXELS_SEARCH}?{urllib.parse.urlencode({"query": query, "orientation": orientation, "per_page": 15})}'
    try:
        req = urllib.request.Request(url, headers={'Authorization': key, **UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            photos = json.load(r).get('photos') or []
        if not photos:
            return None
        # Take the widest available rendition; save() crops it down anyway, and
        # starting large keeps the 1200x630 crop sharp.
        src = photos[0]['src']
        best = src.get('original') or src.get('large2x') or src.get('large')
        with urllib.request.urlopen(
                urllib.request.Request(best, headers=UA), timeout=60) as r:
            return r.read()
    except (urllib.error.URLError, urllib.error.HTTPError, KeyError, ValueError) as e:
        print(f'  Pexels lookup failed: {e}', file=sys.stderr)
        return None


def best_effort(subject, stock_query=None):
    """Try the sources in order of how well they fit the article, and say which
    one answered. Gemini renders exactly the scene asked for; Pexels gives a real
    photograph that is merely close; neither is guaranteed to be available."""
    try:
        return generate(subject), 'gemini'
    except SystemExit as e:
        print(f'  Gemini unavailable: {e}', file=sys.stderr)
    raw = fetch_stock(stock_query or subject)
    if raw:
        return raw, 'pexels'
    return None, 'none'


def save(raw, slug, root='.'):
    """Crop to 1200x630 and write the WebP. ImageOps.fit centre-crops rather than
    squashing, so a 16:9 render loses a sliver of sky instead of distorting."""
    img = ImageOps.fit(Image.open(BytesIO(raw)).convert('RGB'), SIZE, Image.LANCZOS)
    out = os.path.join(root, 'static', 'img', 'articles', f'{slug}.webp')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    img.save(out, 'WEBP', quality=82, method=6)
    return out


def _self_check():
    """Exercises the resize/encode half without spending API credits — that is
    the part that silently drifts (wrong size, wrong format, squashed aspect)."""
    import tempfile
    buf = BytesIO()
    Image.new('RGB', (1920, 1080), (200, 170, 110)).save(buf, 'PNG')
    with tempfile.TemporaryDirectory() as tmp:
        path = save(buf.getvalue(), 'self-check', root=tmp)
        with Image.open(path) as im:
            assert im.size == SIZE, f'expected {SIZE}, got {im.size}'
            assert im.format == 'WEBP', f'expected WEBP, got {im.format}'
        assert os.path.getsize(path) < 300_000, 'file larger than any existing hero'
    print('ok — 1200x630 WebP written and within size budget')


if __name__ == '__main__':
    if '--self-check' in sys.argv:
        _self_check()
    elif len(sys.argv) < 3:
        sys.exit(__doc__)
    else:
        # argv[3], when given, is the plain-language search used if Gemini cannot
        # be reached — "warehouse loading bay" finds a photo where the full scene
        # description would not.
        raw, source = best_effort(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
        if not raw:
            sys.exit('No image source available (Gemini unavailable, no Pexels key '
                     'or no match). The article will fall back to the site logo.')
        print(f'  source: {source}', file=sys.stderr)
        print(save(raw, sys.argv[1]))
