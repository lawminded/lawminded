#!/usr/bin/env python3
"""Check the parsed Act for the defects that are invisible on the page.

    python3 automation/check_act.py content/companies-act-2013.json
    python3 automation/check_act.py content/companies-act-2013.json --against <other.pdf>

Two checks, because the bug that got through was caught by a human comparing
our section 1 against another site's. Section 1 read 2,095 words against a real
244: the Act's entire commencement history had been swallowed from a page
footnote. Nothing in the parse looked wrong — the section had a heading, a
chapter and plausible text.

1. CONTAMINATION. Statutory text does not talk about its own amendment history.
   A section whose body carries "vide notification No. S.O. 582(E)" or "see
   Gazette of India, Extraordinary" has footnote debris in it.

2. SECOND SOURCE. Parse a different PDF of the same Act and compare each
   section's length. Two independent renderings disagreeing by a wide margin
   means one of them is wrong, and it says which sections to look at.

The second source is deliberately a local file rather than another website:
checking 523 sections against someone else's server would be 523 requests we
have no right to make, and their page structure is theirs to change.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

# Wording that belongs in a footnote and never in the body of a section.
CONTAMINATION = re.compile(
    r'vide notification|Gazette of India|Extraordinary, Part II'
    r'|see Gazette|dated \d{1,2}(?:st|nd|rd|th)? \w+, \d{4}, see', re.I)

# How far apart two parses of one section may be before it is worth a look.
# Different printings genuinely differ a little — one carries an amendment the
# other predates — so the threshold is generous and the report is a list to
# read, not a failure.
RATIO = 1.6
FLOOR = 40          # ignore short sections, where a few words swing the ratio


def contamination(sections):
    out = []
    for s in sections:
        m = CONTAMINATION.search(s['text'])
        if m:
            out.append((s['number'], s['heading'], s['words'],
                        s['text'][max(0, m.start() - 60):m.start() + 70]))
    return out


def compare(ours, theirs):
    other = {s['number']: s for s in theirs}
    out = []
    for s in ours:
        t = other.get(s['number'])
        if not t or s['omitted'] or t['omitted']:
            continue
        a, b = s['words'], t['words']
        if max(a, b) < FLOOR:
            continue
        ratio = max(a, b) / max(1, min(a, b))
        if ratio >= RATIO:
            out.append((s['number'], s['heading'], a, b, round(ratio, 1)))
    missing = [s['number'] for s in ours if s['number'] not in other]
    extra = [n for n in other if n not in {s['number'] for s in ours}]
    return out, missing, extra


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('parsed', help='content/companies-act-2013.json')
    ap.add_argument('--against', help='a second PDF of the same Act')
    a = ap.parse_args()

    data = json.loads(Path(a.parsed).read_text())
    secs = data['sections']
    print(f'{len(secs)} sections parsed from {data.get("source", "?")}\n')

    bad = contamination(secs)
    print(f'== footnote contamination: {len(bad)} section(s)')
    for num, head, words, ctx in bad[:15]:
        print(f'   s.{num:<6} {head[:40]:<42} {words:>5}w')
        print(f'      ...{re.sub(chr(10), " ", ctx)}...')
    if len(bad) > 15:
        print(f'   ... and {len(bad) - 15} more')

    if a.against:
        import parse_act
        print(f'\n== second source: {Path(a.against).name}')
        theirs = parse_act.parse(parse_act.read_pdf(Path(a.against)))['sections']
        print(f'   {len(theirs)} sections parsed there')
        diffs, missing, extra = compare(secs, theirs)
        print(f'\n== length disagreements over {RATIO}x: {len(diffs)}')
        for num, head, a_w, b_w, r in sorted(diffs, key=lambda d: -d[4])[:20]:
            print(f'   s.{num:<6} {head[:38]:<40} ours {a_w:>5}w  theirs {b_w:>5}w  ({r}x)')
        if missing:
            print(f'\n   only in ours ({len(missing)}): {missing[:12]}')
        if extra:
            print(f'   only in theirs ({len(extra)}): {extra[:12]}')

    print()
    if bad:
        print('FAIL — footnote text is inside at least one section.')
        return 1
    print('OK — no footnote debris found in any section.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
