"""Guards the rewritten article bodies in content/humanized/.

Run with `python3 test_humanized.py` — no pytest, no fixtures.

These files are what the site actually serves (migration 7 in database.py
replaces the seeded body with them), so a broken one is a broken live page.
The checks are the things that fail silently rather than loudly:

  * FAQ markup drifting out of the exact shape faqs() parses, which empties the
    FAQPage schema without changing anything a human would notice.
  * An internal link pointing at a slug that does not exist, i.e. a 404 planted
    in the body of an article.
  * The dropped section patterns creeping back in.

It deliberately does NOT check prose quality or compare against the pre-rewrite
text. See content/humanized/README.md for what the rewrite was allowed to change.
"""
import os
import re
import sys

from app import faqs
from seo_meta import RETIRED_ARTICLES
import content as C

HUMANIZED = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'content', 'humanized')

# Sections the rewrite removed everywhere. base.html already carries a site-wide
# legal disclaimer, "Related Articles" was a list of unlinked italics, and the
# Key takeaways / Conclusion closers are the pattern the house style dropped.
BANNED_HEADINGS = ('key takeaways', 'conclusion', 'disclaimer', 'related articles',
                   "what you'll learn")


def _known_slugs():
    """Every slug the site can serve, from the seeders rather than a live DB —
    this has to pass on a machine that has never built one."""
    slugs = set(RETIRED_ARTICLES)          # these 301, so a link to them resolves
    import database
    for mod, var in (('blog_seed', 'BLOG_ARTICLES'), ('blog_seed2', 'BLOG_ARTICLES_2'),
                     ('blog_seed3', 'BLOG_ARTICLES_3'), ('blog_seed4', 'BLOG_ARTICLES_4'),
                     ('blog_seed5', 'BLOG_ARTICLES_5'), ('blog_seed6', 'BLOG_ARTICLES_6'),
                     ('blog_seed7', 'BLOG_ARTICLES_7'), ('blog_seed8', 'BLOG_ARTICLES_8')):
        slugs |= {a[1] for a in getattr(__import__(mod), var)}
    slugs |= set(database.PUBLISH_SCHEDULE)
    import article_rewrites
    slugs.add(article_rewrites.DPT3_SLUG)
    return slugs


def main():
    if not os.path.isdir(HUMANIZED):
        print('no content/humanized/ — nothing to check')
        return 0

    files = sorted(f for f in os.listdir(HUMANIZED) if f.endswith('.html'))
    known = _known_slugs()
    topics = set(C.TOPIC_BY_SLUG)
    failures = []

    for name in files:
        slug = name[:-5]
        body = open(os.path.join(HUMANIZED, name), encoding='utf-8').read()

        def bad(msg):
            failures.append(f'{slug}: {msg}')

        if slug not in known:
            bad('no article has this slug — the file would never be applied')

        # The FAQPage schema depends on this exact shape; see faqs() in app.py.
        if not faqs(body):
            bad('FAQ does not parse — FAQPage schema would come out empty')

        for h in re.findall(r'<h2[^>]*>(.*?)</h2>', body, re.S | re.I):
            plain = re.sub(r'<[^>]+>', '', h).strip().lower().rstrip(':')
            if plain in BANNED_HEADINGS:
                bad(f'reintroduced dropped section "{plain}"')

        for href in re.findall(r'href="/article/([^"#?]+)"', body):
            if href not in known:
                bad(f'links to /article/{href}, which does not exist')
        for href in re.findall(r'href="/topic/([^"#?]+)"', body):
            if href not in topics:
                bad(f'links to /topic/{href}, which does not exist')
        if f'href="/article/{slug}"' in body:
            bad('links to itself')

        if body.count('<p>') != body.count('</p>'):
            bad('unbalanced <p> tags')
        if body.count('<ul>') != body.count('</ul>'):
            bad('unbalanced <ul> tags')
        if '<h2' not in body:
            bad('no <h2> sections')
        if not body.strip():
            bad('empty file')

    for f in failures:
        print('FAIL ' + f)
    print(f'\n{len(files)} rewritten articles checked, {len(failures)} problems')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
