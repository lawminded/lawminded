"""The section-wise Companies Act, 2013 reference.

Reads the parsed Act (content/companies-act-2013.json, built by
automation/parse_act.py) and serves it as chapter pages, with each section
opening in place.

Chapter pages rather than 523 section pages, deliberately. Five hundred thin
pages carrying little but statutory text is what search engines treat as
mass-produced filler, and it would put the rankings the site already has at
risk. A chapter page carries the full text of its sections in the HTML, so it
is indexed and deep-linkable at #section-135, while being one substantial page
instead of thirty slight ones.

A chapter is published only when every section in it has a Law Minded summary.
That is both an editorial rule and a legal one: s.52(1)(q)(ii) of the Copyright
Act, 1957 allows reproducing an Act only together with commentary.
"""
import json
import re
from functools import lru_cache
from pathlib import Path

import act_summaries

DATA = Path(__file__).resolve().parent / 'content' / 'companies-act-2013.json'

ACT_TITLE = 'Companies Act, 2013'
ACT_SLUG = 'companies-act-2013'
# What the reader is told about currency, on every page. The site does not
# pretend to be the gazette: MCA's e-book is the authority and says so here.
SOURCE_NOTE = ('Text from the India Code copy of the Act published by the '
               'Legislative Department, including amendments notified up to 2023.')
AUTHORITY_NOTE = ('The Ministry of Corporate Affairs is the authority on the '
                  'current text. Where this page and MCA differ, MCA is right.')

ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}


def _roman_value(s):
    """Sort chapters in numeric order. 'XXIA' sorts just after 'XXI'."""
    core = ''.join(c for c in s if c in ROMAN)
    total, prev = 0, 0
    for ch in reversed(core):
        v = ROMAN[ch]
        total = total - v if v < prev else total + v
        prev = max(prev, v)
    suffix = s[len(core):]
    return (total, suffix)


@lru_cache(maxsize=1)
def load():
    """The parsed Act. Cached: it is a megabyte of JSON and never changes
    between deploys."""
    try:
        return json.loads(DATA.read_text())
    except (OSError, ValueError):
        return {'chapters': [], 'sections': []}


def _section_slug(number):
    return f'section-{str(number).lower()}'


@lru_cache(maxsize=1)
def chapters():
    """Every chapter, in order, each with its sections and whether it is ready
    to publish."""
    data = load()
    out = []
    for c in data['chapters']:
        secs = [s for s in data['sections'] if s['chapter_roman'] == c['roman']]
        if not secs:
            continue
        ready = all(act_summaries.get(s['number']) for s in secs)
        out.append({
            'roman': c['roman'],
            'title': c['title'],
            'slug': f'chapter-{c["roman"].lower()}',
            'sections': secs,
            'count': len(secs),
            'range': _range_label(secs),
            'ready': ready,
            'written': sum(1 for s in secs if act_summaries.get(s['number'])),
        })
    out.sort(key=lambda c: _roman_value(c['roman']))
    return out


def _range_label(secs):
    if not secs:
        return ''
    first, last = secs[0]['number'], secs[-1]['number']
    return first if first == last else f'{first} to {last}'


def published_chapters():
    return [c for c in chapters() if c['ready']]


def get_chapter(slug):
    for c in chapters():
        if c['slug'] == slug:
            return c
    return None


def section_view(section):
    """One section, ready to render: its text broken into paragraphs and its
    summary split into the paragraphs the writer intended."""
    summary = act_summaries.get(section['number'])
    return {
        'number': section['number'],
        'heading': section['heading'],
        'omitted': section['omitted'],
        'anchor': _section_slug(section['number']),
        'summary': [p.strip() for p in (summary or '').split('\n\n') if p.strip()],
        'paragraphs': split_text(section['text']),
        'words': section['words'],
    }


# Sub-sections open with "(1)", clauses with "(a)". Breaking on those turns one
# unreadable slab into something a person can follow, without changing a word.
_SPLIT_RE = re.compile(r'(?=\((?:\d{1,2}|[a-z]{1,2}|[ivx]{1,4})\)\s)')


def split_text(text, limit=60):
    """Break statutory text into paragraphs at sub-section markers."""
    if not text:
        return []
    parts = [p.strip() for p in _SPLIT_RE.split(text) if p.strip()]
    # A section with no numbered sub-sections comes back as one long block;
    # leave it whole rather than inventing breaks that are not in the Act.
    merged, buf = [], ''
    for p in parts:
        if len(buf) + len(p) < 160:          # keep tiny fragments together
            buf = f'{buf} {p}'.strip()
        else:
            if buf:
                merged.append(buf)
            buf = p
    if buf:
        merged.append(buf)
    return merged[:limit]
