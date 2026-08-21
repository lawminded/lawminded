#!/usr/bin/env python3
"""Render an Instagram card for an article: Gemini background, real text on top.

    python3 automation/social_card.py <slug> --eyebrow "GST" \\
        --headline "Ship-to GSTIN is now mandatory on e-way bills" \\
        --fact "From 1 August 2026" --scene "a loading bay at dawn, crates and a clipboard"

    python3 automation/social_card.py --self-check     # no API call, no credits

Writes static/img/social/<slug>.jpg at 1080x1350 — Instagram's portrait size, the
most screen it will give a post in the feed.

The text is drawn here rather than asked for in the image prompt. Image models
still garble lettering, and this is a compliance audience reading a date and a
section number off a phone: a mangled "1 Auqust" costs more than the whole post
earns. So Gemini paints the background and Pillow sets the type, in the site's own
faces.
"""
import argparse
import os
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gen_image  # noqa: E402  (reuses its Gemini call and .env handling)

SIZE = (1080, 1350)
FONTS = Path(__file__).resolve().parent / 'fonts'
OUT_DIR = Path(__file__).resolve().parent.parent / 'static' / 'img' / 'social'

# The site's palette, so a card in the feed reads as the same publication.
GOLD = (232, 160, 32)
CREAM = (247, 244, 237)
INK = (20, 21, 24)

MARGIN = 84


def _font(name, size, weight=None):
    f = ImageFont.truetype(str(FONTS / name), size)
    if weight:
        try:
            f.set_variation_by_name(weight)
        except Exception:
            pass          # a static build of the face is fine, just one weight
    return f


def _wrap(draw, text, font, width):
    words, lines, line = text.split(), [], ''
    for w in words:
        trial = f'{line} {w}'.strip()
        if draw.textlength(trial, font=font) <= width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines


def compose(bg, eyebrow, headline, fact, footer='lawminded.in'):
    """Background image in, finished card out."""
    img = bg.convert('RGB').resize(SIZE, Image.LANCZOS)

    # Push the photograph back so type sits in front of it rather than in it:
    # blur, desaturate, darken, then a vertical gradient that deepens toward the
    # bottom where the headline sits.
    img = img.filter(ImageFilter.GaussianBlur(3))
    img = ImageEnhance.Color(img).enhance(0.45)
    img = ImageEnhance.Brightness(img).enhance(0.55)

    grad = Image.new('L', (1, SIZE[1]))
    for y in range(SIZE[1]):
        t = y / SIZE[1]
        grad.putpixel((0, y), int(90 + 150 * t ** 1.4))
    grad = grad.resize(SIZE)
    img = Image.composite(Image.new('RGB', SIZE, INK), img, grad)

    d = ImageDraw.Draw(img)
    inner = SIZE[0] - 2 * MARGIN

    # Gold rule and eyebrow, top-left.
    d.rectangle([MARGIN, MARGIN, MARGIN + 96, MARGIN + 6], fill=GOLD)
    f_eyebrow = _font('DMSans.ttf', 30, 'Bold')
    d.text((MARGIN, MARGIN + 32), eyebrow.upper(), font=f_eyebrow, fill=GOLD)

    # Headline, set from the bottom up so it never collides with the footer.
    f_head = _font('PlayfairDisplay.ttf', 82, 'Bold')
    lines = _wrap(d, headline, f_head, inner)
    while len(lines) > 6 and f_head.size > 52:
        f_head = _font('PlayfairDisplay.ttf', f_head.size - 6, 'Bold')
        lines = _wrap(d, headline, f_head, inner)

    line_h = int(f_head.size * 1.16)
    f_fact = _font('DMSans.ttf', 38, 'Medium')
    fact_lines = _wrap(d, fact, f_fact, inner) if fact else []
    fact_h = len(fact_lines) * int(f_fact.size * 1.35) + (28 if fact_lines else 0)

    footer_y = SIZE[1] - MARGIN - 34
    y = footer_y - 56 - fact_h - len(lines) * line_h

    for ln in lines:
        d.text((MARGIN, y), ln, font=f_head, fill=CREAM)
        y += line_h

    if fact_lines:
        y += 28
        for ln in fact_lines:
            d.text((MARGIN, y), ln, font=f_fact, fill=GOLD)
            y += int(f_fact.size * 1.35)

    f_foot = _font('DMSans.ttf', 28, 'Medium')
    d.text((MARGIN, footer_y), footer, font=f_foot, fill=(255, 255, 255, 200))

    return img


def build(slug, eyebrow, headline, fact, scene, out_dir=None):
    raw = gen_image.generate(
        f'{scene}. Wide empty space in the lower two-thirds of the frame with no '
        f'subject matter, suitable for text to be laid over it afterwards.')
    from io import BytesIO
    card = compose(Image.open(BytesIO(raw)), eyebrow, headline, fact)
    out = Path(out_dir or OUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    path = out / f'{slug}.jpg'
    card.save(path, 'JPEG', quality=88, optimize=True)
    return path


def _self_check():
    """Exercises composition without spending credits — the part that silently
    breaks (text overflowing, fonts missing, the card ending up the wrong size)."""
    import tempfile
    bg = Image.new('RGB', (1600, 900), (70, 60, 50))
    long_headline = ('Ship-to GSTIN Is Now Mandatory on Every E-Way Bill Raised '
                     'for a Bill-to Ship-to Transaction Across India')
    with tempfile.TemporaryDirectory() as tmp:
        card = compose(bg, 'GST & Indirect Tax', long_headline, 'From 1 August 2026')
        p = Path(tmp) / 'check.jpg'
        card.save(p, 'JPEG', quality=88)
        assert card.size == SIZE, f'expected {SIZE}, got {card.size}'
        assert p.stat().st_size < 900_000, 'card is larger than Instagram likes'
        # A headline that overflows the canvas means text ran off the bottom.
        assert card.getpixel((MARGIN + 4, SIZE[1] - 20)) is not None
    print(f'ok — {SIZE[0]}x{SIZE[1]} card composed, long headline fitted, fonts loaded')


if __name__ == '__main__':
    if '--self-check' in sys.argv:
        _self_check()
        sys.exit(0)
    ap = argparse.ArgumentParser()
    ap.add_argument('slug')
    ap.add_argument('--eyebrow', required=True, help='category, e.g. "GST & Indirect Tax"')
    ap.add_argument('--headline', required=True)
    ap.add_argument('--fact', default='', help='the one number or date that matters')
    ap.add_argument('--scene', required=True, help='what the background photo shows')
    a = ap.parse_args()
    print(build(a.slug, a.eyebrow, a.headline, a.fact, a.scene))
