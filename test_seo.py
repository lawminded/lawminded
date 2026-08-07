"""Guards the SEO markup that search engines read but no human ever notices
breaking. Run with `python3 test_seo.py` — no pytest, no fixtures.

Covers the three things that silently rot: descriptions drifting past the
snippet width, JSON-LD becoming unparseable after a template edit (one stray
quote kills the whole block), and the Article schema going missing from a
page type.
"""
import collections
import json
import re

from app import app, JUDGMENTS_PUBLISHED, autolink
from seo_meta import SEO_DESCRIPTIONS, RETIRED_ARTICLES, RETIRED_ARTICLES
import content as C

DESC_RE = re.compile(r'<meta name="description" content="(.*?)">', re.S)
LD_RE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)


def _page(client, path):
    r = client.get(path)
    assert r.status_code == 200, f'{path} -> {r.status_code}'
    return r.get_data(as_text=True)


def _blocks(html, path):
    """Every JSON-LD block on the page, parsed. Unescapes the HTML entities
    Jinja's autoescaping adds inside the <script>."""
    out = []
    for raw in LD_RE.findall(html):
        txt = (raw.replace('&#34;', '"').replace('&quot;', '"')
                  .replace('&#39;', "'").replace('&amp;', '&'))
        try:
            out.append(json.loads(txt))
        except json.JSONDecodeError as e:
            raise AssertionError(f'{path}: invalid JSON-LD ({e}): {txt[:200]}')
    return out


def _types(blocks):
    types = set()
    for b in blocks:
        for node in b.get('@graph', [b]):
            types.add(node.get('@type'))
    return types


def main():
    app.config['SERVER_NAME'] = None
    client = app.test_client()

    with app.app_context():
        db = __import__('database').get_db()
        rows = db.execute(
            'SELECT slug, summary, category, content FROM articles WHERE published=1'
        ).fetchall()
        db.close()
    slugs = [r['slug'] for r in rows]
    summaries = {r['slug']: r['summary'] or '' for r in rows}
    bodies = {r['slug']: r['content'] or '' for r in rows}
    article_cat = {r['slug']: r['category'] for r in rows}

    paths = (['/', '/blogs', '/judgments', '/about', '/faq', '/author/piyush-kundnani']
             + [f'/topic/{t["slug"]}' for t in C.TOPICS.values()]
             + [f'/judgment/{j["slug"]}' for j in C.JUDGMENTS]
             + [f'/article/{s}' for s in slugs])

    long_descs, checked = [], 0
    for p in paths:
        html = _page(client, p)

        m = DESC_RE.search(html)
        assert m, f'{p}: no meta description'
        desc = m.group(1)
        assert desc.strip(), f'{p}: empty meta description'
        if len(desc) > 155:
            long_descs.append((len(desc), p))

        _blocks(html, p)   # raises if any block is malformed
        checked += 1

    assert not long_descs, f'meta descriptions over 155 chars: {long_descs[:5]}'

    # Every hand-written description points at a real article and already fits,
    # so the metadesc filter stays a safety net rather than the thing shaping
    # what searchers read. A renamed slug shows up here, not in the SERP.
    stale = set(SEO_DESCRIPTIONS) - set(slugs)
    assert not stale, f'seo_meta.py keys with no published article: {sorted(stale)}'
    too_long = {k: len(v) for k, v in SEO_DESCRIPTIONS.items() if len(v) > 155}
    assert not too_long, f'hand-written descriptions over 155 chars: {too_long}'
    clipped = [s for s in slugs if s not in SEO_DESCRIPTIONS
               and len(' '.join(summaries[s].split())) > 155]
    assert not clipped, f'articles still falling back to a clipped summary: {clipped}'

    # Every judgment brief carries Article schema with a real publication date.
    for j in C.JUDGMENTS:
        p = f'/judgment/{j["slug"]}'
        blocks = _blocks(_page(client, p), p)
        art = next((b for b in blocks if b.get('@type') == 'Article'), None)
        assert art, f'{p}: missing Article schema'
        assert art['datePublished'].startswith(JUDGMENTS_PUBLISHED), p
        assert art['author']['name'], p
        assert 'BreadcrumbList' in _types(blocks), p

    # Articles kept their Article schema; the author page states the credential
    # as a degree, not as a job title.
    p = f'/article/{slugs[0]}'
    assert 'Article' in _types(_blocks(_page(client, p), p)), p

    p = '/author/piyush-kundnani'
    person = next(b for b in _blocks(_page(client, p), p) if b.get('@type') == 'Person')
    assert person['jobTitle'] == 'Founder & Editor', person['jobTitle']
    assert person['hasCredential']['name'] == 'B.Com', person.get('hasCredential')

    # An article hero photo must never leak into the Organization logo.
    blocks = _blocks(_page(client, f'/article/{slugs[0]}'), 'org-logo')
    org = next(n for b in blocks for n in b.get('@graph', [b])
               if n.get('@type') == 'Organization')
    assert org['logo'].endswith('/static/img/logo-full.png'), org['logo']

    # Retired duplicates must 301 to their survivor, never 404 and never sit in
    # a listing. A retired slug that still resolves means two near-identical
    # pages are competing again, which is the thing retiring them fixed.
    for old, new in RETIRED_ARTICLES.items():
        r = client.get(f'/article/{old}')
        assert r.status_code == 301, f'/article/{old} -> {r.status_code}, expected 301'
        assert r.headers['Location'].endswith(f'/article/{new}'), r.headers['Location']
        assert new in slugs, f'{old} redirects to {new}, which is not published'
        assert old not in slugs, f'{old} is retired but still published'
    sitemap = client.get('/sitemap.xml').get_data(as_text=True)
    for old in RETIRED_ARTICLES:
        assert f'/article/{old}<' not in sitemap, f'{old} is still in the sitemap'

    # Internal linking. The site shipped 123 articles with 7 links between them
    # (all external), so every guide was an island. These assertions are what
    # stops it silently regressing to that.
    inbound, outbound, problems = collections.Counter(), [], []
    with app.test_request_context('/'):
        for slug in slugs:
            body = autolink(bodies[slug], slug)
            targets = re.findall(r'href="/article/([a-z0-9\-]+)"', body)
            outbound.append(len(targets))
            if slug in targets:
                problems.append(f'{slug}: links to itself')
            if len(targets) != len(set(targets)):
                problems.append(f'{slug}: same target linked twice')
            for t in targets:
                if t not in slugs:
                    problems.append(f'{slug}: dead link -> {t}')
                inbound[t] += 1
            # An <a> inside an <a> is invalid and browsers silently drop it;
            # a linked heading hijacks the page's own outline.
            if re.search(r'<a\b[^>]*>(?:(?!</a>).)*?<a\b', body, re.S):
                problems.append(f'{slug}: nested anchor')
            if any('<a ' in h for h in
                   re.findall(r'<h[1-6][^>]*>.*?</h[1-6]>', body, re.S)):
                problems.append(f'{slug}: link inside a heading')
    assert not problems, f'autolink problems: {problems[:5]}'
    assert max(outbound) <= 8, f'article exceeds the 8-link cap: {max(outbound)}'

    # Every article must be reachable from somewhere: an in-body link, or
    # failing that its topic hub. An article no page links to is invisible.
    hubbed = {s for s in slugs
              if C.TOPICS.get(article_cat[s], {}).get('slug')}
    unreachable = [s for s in slugs if inbound[s] == 0 and s not in hubbed]
    assert not unreachable, f'articles with no inbound link at all: {unreachable}'

    # Each hub links to every article it covers, and is itself linked from /blogs.
    hub_html = _page(client, '/blogs')
    for cat, t in C.TOPICS.items():
        assert f'/topic/{t["slug"]}' in hub_html, f'/blogs does not link {t["slug"]}'
        page = _page(client, f'/topic/{t["slug"]}')
        for s in (s for s in slugs if article_cat[s] == cat):
            assert f'/article/{s}' in page, f'{t["slug"]} hub missing {s}'

    print(f'OK — {checked} pages: descriptions <=155, JSON-LD valid, '
          f'{len(C.JUDGMENTS)} judgments have Article schema, '
          f'{len(C.TOPICS)} topic hubs, {sum(outbound)} in-body internal links, '
          f'{len([s for s in slugs if inbound[s] == 0])} articles rely on their hub alone')


if __name__ == '__main__':
    main()
