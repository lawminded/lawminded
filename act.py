"""The section-wise Companies Act, 2013 reference.

Reads the parsed Act (content/companies-act-2013.json, built by
automation/parse_act.py) and serves it as chapter pages, with each section
opening in place.

Three levels, the way a legal reference is actually used and the way
ca2013.com lays it out: the Act lists its chapters, a chapter lists the names
of its sections, and a section has its own page. Nobody reads a chapter
end to end; they arrive knowing they want section 135 and want to get there.

On a section page the Law Minded summary comes first, in plain English, and
the exact words of the Act sit behind a tap underneath it.

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


def get_section(number):
    """One section by its number, only if it is publishable — a section with no
    summary must not render the statute on its own. See the module docstring."""
    want = str(number).lower()
    for s in load()['sections']:
        if str(s['number']).lower() == want:
            return s if act_summaries.get(s['number']) else None
    return None


def neighbours(section):
    """The previous and next publishable sections, for the prev/next links a
    reference page needs."""
    pub = [s for s in load()['sections'] if act_summaries.get(s['number'])]
    for i, s in enumerate(pub):
        if s['number'] == section['number']:
            return (pub[i - 1] if i else None,
                    pub[i + 1] if i + 1 < len(pub) else None)
    return (None, None)


# Section 2 is a list of ~95 defined terms, and a reader looking for one wants
# to see the term, not a wall of prose. ca2013.com lists them individually under
# the section, which is the right call, so this pulls them out: (1) "abridged
# prospectus" means... -> ('1', 'abridged prospectus').
_Q = '\u201c\u201d\u2018\u2019"\''
# A defined term can be a pair — the Act says "alter" or "alteration" — and
# showing only the first half reads as a typo next to the printed reckoner.
_DEFN_RE = re.compile(
    r'\((?P<num>\d{1,3})\)\s*'
    r'[' + _Q + r'](?P<term>[^' + _Q + r']{2,70})[' + _Q + r']'
    r'(?P<more>(?:\s+(?:or|and)\s+[' + _Q + r'][^' + _Q + r']{2,70}[' + _Q + r'])*)')


def definitions(section, with_text=False):
    """The defined terms in a definitions section, in order. Empty for any
    section that is not built as a list of definitions.

    Numbering follows the Act, so gaps are real: (49) "interested director" was
    omitted by the Companies (Amendment) Act, 2017, which is why section 2 has
    93 definitions running up to number 94.
    """
    out, seen = [], set()
    for m in _DEFN_RE.finditer(section.get('text', '')):
        term = re.sub(r'\s+', ' ', m.group('term')).strip()
        # Fold "alter" or "alteration" into one readable label.
        extra = [re.sub(r'\s+', ' ', t).strip()
                 for t in re.findall(r'[' + _Q + r']([^' + _Q + r']{2,70})[' + _Q + r']',
                                     m.group('more') or '')]
        if extra:
            term = ' or '.join([term] + extra)
        key = term.lower()
        if key in seen or len(term) < 2:
            continue
        seen.add(key)
        entry = {'num': m.group('num'), 'term': term,
                 'slug': f"{m.group('num')}-{_slugify(term)}"}
        if with_text:
            entry['text'] = _defn_text(section['text'], m.end())
        out.append(entry)
    return out


def _slugify(term):
    return re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', term.lower())).strip('-')


def _defn_text(text, start):
    """One definition's own words: from where its term ends to the start of the
    next numbered definition."""
    nxt = re.search(r'\s\(\d{1,3}\)\s*[\u201c\u2018"\']', text[start:])
    body = text[start:start + nxt.start()] if nxt else text[start:]
    return re.sub(r'\s+', ' ', body).strip(' ;,')


def get_definition(section_number, slug):
    """One definition of one section, by its slug."""
    sec = get_section(section_number)
    if not sec:
        return None, None
    for d in definitions(sec, with_text=True):
        if d['slug'] == slug:
            return sec, d
    return sec, None


def chapter_neighbours(slug):
    """Previous and next published chapter, for the 'Chapter 3 of 28' strip."""
    pub = published_chapters()
    for i, c in enumerate(pub):
        if c['slug'] == slug:
            return (pub[i - 1] if i else None,
                    pub[i + 1] if i + 1 < len(pub) else None,
                    i + 1, len(pub))
    return (None, None, 0, len(pub))


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
        'definitions': definitions(section),
        'words': section['words'],
    }


# Sub-sections open with "(1)", clauses with "(a)". Breaking on those turns one
# unreadable slab into something a person can follow, without changing a word.
# Not every "(10)" starts a sub-section: "referred to in sub-section (10) of
# section 143" is mid-sentence, and splitting there left "(10) of section 143;"
# stranded as its own paragraph.
_SPLIT_RE = re.compile(
    r'(?<!sub-section )(?<!sub -section )(?<!subsection )(?<!section )'
    r'(?<!clause )(?<!clauses )(?<!and )(?<!or )(?<!to )'
    r'(?=\((?:\d{1,2}|[a-z]{1,2}|[ivx]{1,4})\)\s)')


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
