#!/usr/bin/env python3
"""Turn the bare Companies Act 2013 PDF into structured JSON.

    python3 automation/parse_act.py <act.pdf> --out content/companies-act-2013.json
    python3 automation/parse_act.py <act.pdf> --check      # parse and report only

Why this exists, and why the text is safe to publish: Section 52(1)(q)(ii) of the
Copyright Act, 1957 makes reproducing an Act of a Legislature no infringement
*provided it is published together with commentary or other original matter*. So
the statute goes on the site alongside our own explanation, never on its own.

Source: the India Code copy of the Act, which carries amendment footnotes and
runs later than MCA's own downloadable PDF (that one is stamped 1-4-2021; this
one has amendments through 2023). MCA's live e-book is more current than either
and is the authority — automation/watch_mca.py is what keeps us honest about the
gap, and every rendered page carries the source and its date.

The parse is deliberately strict. A silent mis-parse on a compliance site is
worse than a crash, so anything that does not look like the Act is reported
rather than guessed at, and --check exists to be run before publishing.
"""
import argparse
import json
import re
import sys
from pathlib import Path

# "135. Corporate Social Responsibility.—(1) Every company..." — number, an
# optional letter suffix (3A, 10A), the heading, then an em or en dash.
#
# The optional "3[" prefix is an amendment footnote marker: where a whole
# section was substituted, the replacement opens with one. Section 42 was
# substituted in full and went missing from the parse until this allowed for it.
# The heading may wrap onto a second line (section 24, 118 and 459 all do), and
# the dash that ends it is an em dash, an en dash, or occasionally a plain
# hyphen (section 3A).
SECTION_RE = re.compile(
    r'^\s*(?:\d{1,2}\s*\[\s*)?(?P<num>\d{1,3}[A-Z]{0,2})\.\s+'
    r'(?P<head>[^\n]{3,160}?(?:\n[ \t]*[^\n]{1,90}?)?)'
    r'\s*\.?\s*\n?\s*[—–-]',
    re.M)
CHAPTER_RE = re.compile(
    r'^\s*CHAPTER\s+(?P<num>[IVXLC]+[A-Z]?)\s*\n\s*(?P<title>[^\n]{3,90})',
    re.M)
# Omitted and repealed sections appear as "11. [Omitted.]." with no dash.
OMITTED_RE = re.compile(
    r'^\s*(?:\d{1,2}\s*\[\s*)?(?P<num>\d{1,3}[A-Z]{0,2})\.\s*'
    r'\[\s*(?P<head>[^\]]{3,120}?)\s*\]\s*(?P<what>Omitted|Repealed)\b',
    re.M)


def read_pdf(path):
    try:
        import pypdf
    except ImportError:
        sys.exit('pypdf is not installed. Run: python3 -m pip install --user pypdf')
    reader = pypdf.PdfReader(str(path))
    return '\n'.join((p.extract_text() or '') for p in reader.pages)


def split_body(text):
    """Drop the ARRANGEMENT OF SECTIONS table of contents at the front.

    Both copies repeat 'CHAPTER I / PRELIMINARY' — once in the contents and once
    where the Act actually begins. The real body is the second occurrence, and it
    is followed by the text of section 1 rather than by a list of headings."""
    marks = [m.start() for m in re.finditer(r'^\s*CHAPTER\s+I\s*$', text, re.M)]
    if len(marks) < 2:
        # Some renderings put the chapter number and title on one line.
        marks = [m.start() for m in re.finditer(r'CHAPTER\s+I\s*\n\s*PRELIMINARY', text)]
    if len(marks) < 2:
        sys.exit('Could not find where the contents end and the Act begins.')
    body = text[marks[1]:]
    # The Act ends where the Schedules begin. Table F inside Schedule I has
    # numbered articles that look exactly like sections — that is where a
    # phantom "42. All general meetings..." came from, overwriting the real
    # section 42 — and the last real section swallowed everything after it.
    sched = re.search(r'\n\s*SCHEDULE\s+I\b', body)
    if sched:
        body = body[:sched.start()]
    return body, text[:marks[1]]


def clean(s):
    """Join the PDF's hard-wrapped lines back into sentences and drop the page
    furniture, without touching the words themselves."""
    s = re.sub(r'\n?\s*\d{1,3}\s*\n', '\n', s)          # bare page numbers
    s = re.sub(r'[ \t]+', ' ', s)
    s = re.sub(r'\s*\n\s*', ' ', s)
    return s.strip()


FRONT_SECTION_RE = re.compile(r'^\s*(\d{1,3}[A-Z]{0,2})\.\s+\S', re.M)


def expected_numbers(front):
    """The section numbers the Act's own ARRANGEMENT OF SECTIONS lists.

    This is the authority on what exists. The body parse is a best effort over
    PDF text; anything it finds that the contents do not list is a phantom —
    usually a numbered clause inside a section — and anything the contents list
    that the body parse missed is a genuine gap worth failing over."""
    return [m.group(1) for m in FRONT_SECTION_RE.finditer(front)]


def parse(text):
    body, front = split_body(text)
    expected = expected_numbers(front)

    # Where each chapter starts, so a section can be told which one it is in.
    chapters = []
    for m in CHAPTER_RE.finditer(body):
        title = m.group('title').strip().rstrip('.')
        if title.isupper() and len(title) > 3:
            chapters.append({'roman': m.group('num'), 'title': title.title(),
                             'at': m.start()})

    starts = []
    for m in SECTION_RE.finditer(body):
        head = re.sub(r'\s+', ' ', m.group('head')).strip()
        # A heading is Title Case prose, not a fragment of a sentence. Without
        # this, mid-sentence numbers like "...under 135. of the Act" become
        # phantom sections.
        if head.endswith('.'):
            head = head[:-1]
        if len(head.split()) > 24 or head[:1].islower():
            continue
        starts.append({'num': m.group('num'), 'head': head, 'at': m.start(),
                       'body_at': m.end()})
    for m in OMITTED_RE.finditer(body):
        starts.append({'num': m.group('num'),
                       'head': f'{m.group("head")} [{m.group("what").lower()}]',
                       'at': m.start(), 'body_at': m.end(), 'omitted': True})
    starts.sort(key=lambda s: s['at'])

    # Keep the first appearance of each number: a later "135." inside a
    # cross-reference is not a second section 135.
    seen, ordered = set(), []
    for s in starts:
        if s['num'] not in seen:
            seen.add(s['num'])
            ordered.append(s)

    sections = []
    for i, s in enumerate(ordered):
        end = ordered[i + 1]['at'] if i + 1 < len(ordered) else len(body)
        chap = None
        for c in chapters:
            if c['at'] <= s['at']:
                chap = c
            else:
                break
        text_body = clean(body[s['body_at']:end])
        sections.append({
            'number': s['num'],
            'heading': s['head'],
            'chapter_roman': chap['roman'] if chap else None,
            'chapter_title': chap['title'] if chap else None,
            'omitted': bool(s.get('omitted')),
            'text': text_body,
            'words': len(text_body.split()),
        })

    # Keep only what the Act's own contents list, in the order it lists them.
    want = []
    for n in expected:
        if n not in want:
            want.append(n)
    found = {s['number']: s for s in sections}
    kept = [found[n] for n in want if n in found]
    phantom = sorted(set(found) - set(want))
    missing = [n for n in want if n not in found]

    for c in chapters:
        c.pop('at', None)
    return {'chapters': chapters, 'sections': kept,
            'phantom_dropped': phantom, 'missing': missing,
            'expected_count': len(want)}


def report(data):
    secs, chaps = data['sections'], data['chapters']
    print(f'chapters: {len(chaps)}')
    print(f'sections: {len(secs)} of {data["expected_count"]} listed in the Act\'s '
          f'own contents  (omitted/repealed: {sum(s["omitted"] for s in secs)})')
    if data['missing']:
        print(f'  MISSING from the parse: {data["missing"]}')
    if data['phantom_dropped']:
        print(f'  phantoms dropped: {len(data["phantom_dropped"])} '
              f'-> {data["phantom_dropped"][:10]}')
    thin = [s['number'] for s in secs if not s['omitted'] and s['words'] < 12]
    print(f'suspiciously short: {len(thin)}' + (f' -> {thin[:12]}' if thin else ''))
    nochap = [s['number'] for s in secs if not s['chapter_roman']]
    print(f'without a chapter: {len(nochap)}' + (f' -> {nochap[:8]}' if nochap else ''))
    print('\nspot checks:')
    want = {'1': 'Short title', '2': 'Definitions', '135': 'Corporate Social',
            '42': 'private placement', '62': 'further issue', '203': 'key managerial',
            '447': 'fraud', '470': 'difficult'}
    by = {s['number']: s for s in secs}
    for n, expect in want.items():
        s = by.get(n)
        if not s:
            print(f'  {n:>4}  MISSING')
            continue
        ok = expect.lower() in (s['heading'] + ' ' + s['text'][:400]).lower()
        print(f'  {n:>4}  {"ok " if ok else "?? "} {s["heading"][:52]:<54} '
              f'{s["words"]:>5}w  ch.{s["chapter_roman"]}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pdf')
    ap.add_argument('--out')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()

    data = parse(read_pdf(Path(a.pdf)))
    data['source'] = Path(a.pdf).name
    report(data)

    if a.out and not a.check:
        out = Path(a.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(data, indent=1, ensure_ascii=False))
        print(f'\nwrote {out} ({out.stat().st_size // 1024} KB)')


if __name__ == '__main__':
    main()
