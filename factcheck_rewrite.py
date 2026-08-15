"""Diff a humanized article against its pre-rewrite body and report fact drift.

    python3 factcheck_rewrite.py                 # every file in content/humanized/
    python3 factcheck_rewrite.py <slug> [<slug>] # just these

The humanizer pass is meant to change prose and nothing else. On a compliance
site the dangerous failure is silent: a rewritten sentence that drops a section
number or rounds a rupee figure reads fine and is wrong. So this extracts the
tokens that must survive verbatim — figures, section and rule numbers, form
names, dates, percentages — and diffs the sets.

Reports, does not assert. A genuinely redundant third repeat of the same figure
may legitimately go, and singular/plural citation forms ("Section 101" vs
"Sections 101") flag harmlessly. Every flag gets read by a human.

The "before" body is reconstructed here rather than read from a saved export:
the script rebuilds a throwaway database from the seeders and migrations 1-6,
with migration 7 neutralised, which is exactly the text the rewrite started
from. So this needs no setup and works in any fresh checkout.
"""
import html as _html
import os
import re
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
HUMANIZED = os.path.join(HERE, 'content', 'humanized')


def _pre_rewrite_bodies():
    """{slug: body} as the articles read *before* the humanizer pass."""
    tmp = tempfile.mkdtemp()
    os.environ['DATABASE_PATH'] = os.path.join(tmp, 'before.db')
    sys.path.insert(0, HERE)
    import database
    # Migration 7 is what applies content/humanized/. Neutralise it so the
    # database stops at the state the rewrite started from.
    database._humanized_articles = lambda: []
    database.init_db()
    database.seed_articles()
    database.apply_content_migrations()
    conn = database.get_db()
    rows = conn.execute('SELECT slug, content FROM articles').fetchall()
    return {r[0]: r[1] for r in rows}


def text(body):
    """Visible text: tags out, entities decoded, whitespace flattened."""
    return re.sub(r'\s+', ' ', _html.unescape(re.sub(r'<[^>]+>', ' ', body)))


# Things that must survive a prose-only rewrite.
PATTERNS = [
    # Rupee amounts. The \b and leading \d are load-bearing: without them,
    # case-insensitive "Rs" plus a bare comma matches the tail of "matters,".
    r'(?:₹|\bRs\.?\s?)\s?\d[\d,]*(?:\.\d+)?(?:\s?(?:crore|lakh|lakhs|cr))?',
    r'\b\d[\d,]*(?:\.\d+)?\s?(?:crore|lakh|lakhs)\b',
    r'\bSections?\s+\d+[A-Z]*(?:\(\d+\))?(?:\([a-z]+\))?',
    r'\bRegulations?\s+\d+(?:\(\d+\))?(?:\([a-z]\))?',
    r'\bRules?\s+\d+[A-Z]*(?:\(\d+\))?',
    r'\bArticles?\s+\d+[A-Z]*',
    r'\bClause\s+\d+',
    r'\b(?:AOC|MGT|ADT|DIR|DPT|CHG|SH|INC|MR|BEN|FC|GSTR|ITR|MSME|STK|URC|PAS|NDH|FLA'
    r'|MBP|MSC|CAA|RSC|CSR|CMP|TM|RD|CAA)-\s?\d+[A-Z]*\b',
    r'\bForm\s+\d+[A-Z]*\b',
    r'\b\d+\s?(?:days?|months?|years?|weeks?)\b',
    r'\b\d{1,2}(?:st|nd|rd|th)?\s+(?:January|February|March|April|May|June|July|August|'
    r'September|October|November|December)(?:,?\s+\d{4})?',
    r'\b(?:January|February|March|April|May|June|July|August|September|October|'
    r'November|December)\s+\d{4}\b',
    r'\b(?:19|20)\d{2}\b',
    r'\b\d+(?:\.\d+)?\s?%',
]
FACT_RE = re.compile('|'.join(PATTERNS), re.I)


def facts(body):
    """Set of load-bearing tokens, normalised for harmless spelling drift.

    A set, not a multiset: how often an article repeats "18%" is a prose
    decision, and counting it would flag every ordinary edit.
    """
    out = set()
    for m in FACT_RE.findall(text(body)):
        # [\d,]+ happily eats the comma ending a clause ("₹1,800, but…"),
        # inventing a token that can never match on the other side.
        k = re.sub(r'\s+', ' ', m.strip().lower().rstrip('.,;:')).strip()
        k = k.replace('rs. ', 'rs ').replace('₹', 'rs ').replace('lakhs', 'lakh')
        out.add(re.sub(r'^rs\s*', 'rs ', k))
    return out


def faq_count(body):
    """Mirrors faqs() in app.py — FAQPage schema silently empties if this drifts."""
    m = re.search(r'<h2[^>]*>\s*(?:frequently asked questions|common questions|faqs?)'
                  r'\s*</h2>(.*?)(?:<h2|$)', body, re.I | re.S)
    if not m:
        return 0
    return sum(1 for q, a in re.findall(r'<p>\s*<strong>(.*?)</strong>\s*(.*?)</p>',
                                        m.group(1), re.S)
               if re.sub(r'<[^>]+>', '', q).strip().endswith('?')
               and re.sub(r'<[^>]+>', '', a).strip())


def check(slug, before, after):
    issues = []
    fb, fa = facts(before), facts(after)
    if fb - fa:
        issues.append('DROPPED FACTS: ' + ', '.join(sorted(fb - fa)))
    # Anything the original never contained is either invented or restated in a
    # different unit. Both need eyes on them.
    if fa - fb:
        issues.append('NEW FACTS (verify): ' + ', '.join(sorted(fa - fb)))

    lb = set(re.findall(r'href="(/article/[^"]+|/topic/[^"]+)"', before))
    la = set(re.findall(r'href="(/article/[^"]+|/topic/[^"]+)"', after))
    if lb - la:
        issues.append('DROPPED LINKS: ' + ', '.join(sorted(lb - la)))

    qb, qa = faq_count(before), faq_count(after)
    if qb and not qa:
        issues.append(f'FAQ SCHEMA BROKEN: parsed {qb} -> 0')
    elif qa < qb:
        issues.append(f'FAQ shrank: {qb} -> {qa} questions')

    wb, wa = len(text(before).split()), len(text(after).split())
    if wa < wb * 0.75:
        issues.append(f'LENGTH: {wb} -> {wa} words ({100 * wa // wb}%)')

    if re.search(r'<h2[^>]*>\s*Key takeaways', after, re.I):
        issues.append('reintroduced "Key takeaways" (pattern was dropped)')
    if after.count('<p>') != after.count('</p>'):
        issues.append('unbalanced <p> tags')
    return issues


def main():
    before = _pre_rewrite_bodies()
    slugs = sys.argv[1:] or sorted(f[:-5] for f in os.listdir(HUMANIZED)
                                   if f.endswith('.html'))
    bad = 0
    for slug in slugs:
        path = os.path.join(HUMANIZED, slug + '.html')
        if not os.path.exists(path):
            print(f'\n── {slug}\n   NO REWRITE FILE at {path}')
            bad += 1
            continue
        if slug not in before:
            print(f'\n── {slug}\n   no article has this slug — file would never apply')
            bad += 1
            continue
        issues = check(slug, before[slug], open(path, encoding='utf-8').read())
        if issues:
            bad += 1
            print(f'\n── {slug}')
            for i in issues:
                print('   ' + i)
    print(f'\n{len(slugs)} checked, {bad} with flags, {len(slugs) - bad} clean')
    return 0


if __name__ == '__main__':
    sys.exit(main())
