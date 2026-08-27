"""Guards the SEO markup that search engines read but no human ever notices
breaking. Run with `python3 test_seo.py` — no pytest, no fixtures.

Covers the three things that silently rot: descriptions drifting past the
snippet width, JSON-LD becoming unparseable after a template edit (one stray
quote kills the whole block), and the Article schema going missing from a
page type.
"""
import collections
import html
import json
import re

from app import (app, JUDGMENTS_PUBLISHED, autolink, seotitle, SITE_URL,
                 TITLE_MAX)
from seo_meta import (SEO_DESCRIPTIONS, SEO_TITLES, SEARCH_META_CHANGED,
                      RETIRED_ARTICLES)
import content as C

DESC_RE = re.compile(r'<meta name="description" content="(.*?)">', re.S)
LD_RE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
TITLE_RE = re.compile(r'<title>(.*?)</title>', re.S)


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


def test_title_length(client, paths):
    """Google shows roughly 60 characters of a <title>. Anything longer it cuts
    off itself, mid-word, and the result reads as a broken page.

    Article titles go through the `seotitle` filter, which already respects the
    limit. Every other page type builds its title by string concatenation in the
    template, where nothing enforces it — which is how 54 of 55 format pages
    ended up averaging 79 characters."""
    too_long = []
    for path in paths:
        r = client.get(path, base_url=SITE_URL)
        if r.status_code != 200:
            continue
        m = TITLE_RE.search(r.get_data(as_text=True))
        assert m, f'{path} renders no <title>'
        title = html.unescape(m.group(1).strip())
        if len(title) > TITLE_MAX:
            too_long.append((len(title), path, title))
    assert not too_long, (
        f'{len(too_long)} pages render a <title> over {TITLE_MAX} chars, which '
        'Google truncates mid-word:\n' + '\n'.join(
            f'  {n} chars  {p}\n    {t}'
            for n, p, t in sorted(too_long, reverse=True)[:10]))


def test_seotitle_cases():
    """The automatic shortener must not leave a title ending mid-phrase.

    Each headline below is real. The last case is kept deliberately: nothing in
    the string distinguishes a dangling 'Raise' from a perfectly fine 'Removal',
    so the shortener cannot fix every headline and the pages that matter carry a
    hand-written SEO_TITLES entry instead."""
    cases = [
        # Trims at the last clause boundary instead of stranding a phrase's
        # first word ('... ADT-1, Sections', '... e-Jagriti - Step'). Trimming
        # can free enough room for the brand, as it does here.
        ('Auditor Appointment, Rotation & Removal: ADT-1, Sections 139-140',
         'Auditor Appointment, Rotation & Removal: ADT-1 - Law Minded'),
        # 51 chars after the trim, so the 13-char brand no longer fits.
        ('How to File a Consumer Complaint Online on e-Jagriti - Step by Step',
         'How to File a Consumer Complaint Online on e-Jagriti'),
        # Inside the budget already: untouched, and the brand fits.
        ('Reduction of Share Capital',
         'Reduction of Share Capital - Law Minded'),
        # Inside the budget without the brand, which does not fit.
        ('Appointment of KMP: Section 203 Thresholds for MD, CFO & CS',
         'Appointment of KMP: Section 203 Thresholds for MD, CFO & CS'),
        # No clause boundary in range: falls back to the word-boundary trim,
        # which cannot know that 'Raise' opens a phrase.
        ('FPO (Further Public Offer): How Listed Companies Raise Capital Again',
         'FPO (Further Public Offer): How Listed Companies Raise'),
    ]
    for headline, expected in cases:
        got = seotitle({'title': headline, 'seo_title': None, 'slug': ''})
        assert got == expected, (
            f'seotitle({headline!r})\n  got      {got!r}\n  expected {expected!r}')
        assert len(got) <= TITLE_MAX, f'{got!r} is {len(got)} chars'


def test_seo_titles_valid(slugs):
    """Every hand-written title must fit the budget and point at a live page.

    The slug check is the guard INTERNAL_LINKS already has: when an article is
    renamed, a stale entry fails the build instead of silently going dead and
    handing the page back to the automatic shortener."""
    for slug, title in SEO_TITLES.items():
        assert slug in slugs, (
            f'SEO_TITLES has an entry for {slug!r}, which is not a published '
            'article. Rename it or remove it.')
        assert title == title.strip(), f'{slug}: title has stray whitespace'
        assert len(title) <= TITLE_MAX, (
            f'{slug}: hand-written title is {len(title)} chars, over {TITLE_MAX}\n'
            f'  {title}')


def test_seo_title_wins(client):
    """A hand-written title beats both the database column and the shortener."""
    if not SEO_TITLES:
        return
    slug, expected = next(iter(SEO_TITLES.items()))
    page = client.get(f'/article/{slug}', base_url=SITE_URL).get_data(as_text=True)
    got = html.unescape(TITLE_RE.search(page).group(1).strip())
    assert got.startswith(expected), (
        f'/article/{slug} rendered {got!r}, expected it to start with {expected!r}')


def test_sitemap_lastmod(client, slugs):
    """Every URL whose freshness we can honestly establish carries a lastmod.

    A sitemap that omits lastmod, or reports one that never moves when the page
    does, tells Google there is nothing to re-crawl. Before this guard, all 55
    format pages, the comparisons and the topic hubs carried none at all, and the
    articles reported a date drawn from the article body — which does not move
    when the title Google displays is rewritten."""
    xml = client.get('/sitemap.xml', base_url=SITE_URL).get_data(as_text=True)
    urls = re.findall(r'<url>(.*?)</url>', xml, re.S)
    entries = {}
    for block in urls:
        loc = re.search(r'<loc>([^<]+)</loc>', block).group(1)
        lm = re.search(r'<lastmod>([^<]+)</lastmod>', block)
        entries[loc.replace(SITE_URL, '')] = lm.group(1) if lm else None

    for kind in ('/article/', '/format/', '/compare/', '/topic/', '/judgment/'):
        missing = [p for p, lm in entries.items() if p.startswith(kind) and not lm]
        assert not missing, (
            f'{len(missing)} {kind} URLs have no <lastmod>, so Google has no '
            f'signal to re-crawl them: {missing[:5]}')

    for path, lm in entries.items():
        if lm:
            assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', lm), \
                f'{path}: lastmod {lm!r} is not a plain ISO date'

    # The metadata revision is a real change to what these pages serve, so no
    # page may report a date earlier than it.
    stale = [(p, lm) for p, lm in entries.items()
             if lm and p.startswith(('/article/', '/format/')) and lm < SEARCH_META_CHANGED]
    assert not stale, (
        f'{len(stale)} pages report a lastmod older than the metadata revision '
        f'({SEARCH_META_CHANGED}): {stale[:5]}')


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

    with app.app_context():
        db = __import__('database').get_db()
        format_slugs = [r['slug'] for r in
                        db.execute('SELECT slug FROM formats ORDER BY sort_order, id')]
        db.close()

    paths = (['/', '/blogs', '/judgments', '/about', '/faq', '/templates', '/compare']
             + [f'/compare/{c["slug"]}' for c in C.COMPARISON_TABLES]
             + [f'/format/{s}' for s in format_slugs]
             + [f'/topic/{t["slug"]}' for t in C.TOPICS.values()]
             + [f'/judgment/{j["slug"]}' for j in C.JUDGMENTS]
             + [f'/article/{s}' for s in slugs])

    test_title_length(client, paths)
    test_seotitle_cases()
    test_seo_titles_valid(slugs)
    test_seo_title_wins(client)
    test_sitemap_lastmod(client, slugs)

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

    # Articles carry Article schema whose author is the name + the held
    # qualification and nothing else. The owner removed the author bio page and
    # wants no bio, photo, job title or personal profile links anywhere, so
    # assert the absence as well as the presence.
    p = f'/article/{slugs[0]}'
    blocks = _blocks(_page(client, p), p)
    assert 'Article' in _types(blocks), p
    art = next(b for b in blocks if b.get('@type') == 'Article')
    person = art['author']
    assert person['name'] == 'Piyush Kundnani', person['name']
    assert person['hasCredential']['name'] == 'B.Com', person.get('hasCredential')
    for field in ('jobTitle', 'description', 'sameAs', 'image', 'url'):
        assert field not in person, f'{field} must stay off the author schema'

    # The author bio page is gone and must stay gone (301 to /about, not 200).
    assert client.get('/author/piyush-kundnani').status_code == 301
    assert '/author/' not in _page(client, f'/article/{slugs[0]}'), 'byline must not link'

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

    # Both domains answer directly. The owner wants lawminded.in and
    # lawminded.co.in each reachable rather than one funnelling into the other,
    # so no hostname may 301 to another. This has to force production mode on,
    # because that is the only mode the old host redirect ever fired in — left
    # off, the check would happily pass against a reinstated redirect.
    import app as _app
    was_prod = _app.IS_PROD
    _app.IS_PROD = True
    try:
        for host in ('lawminded.in', 'www.lawminded.in',
                     'lawminded.co.in', 'www.lawminded.co.in'):
            for path in ('/', '/blogs'):
                r = client.get(path, base_url=f'https://{host}')
                assert r.status_code == 200, (
                    f'https://{host}{path} -> {r.status_code}, expected 200. '
                    'Both domains must serve directly; no hostname may redirect '
                    'to another.')
            # Whichever host served it, the page still nominates one URL for
            # indexing. That canonical tag is the only thing keeping two live
            # domains from reading as duplicate content.
            html = client.get('/', base_url=f'https://{host}').get_data(as_text=True)
            m = re.search(r'<link rel="canonical" href="([^"]+)"', html)
            assert m, f'no canonical tag served on {host}'
            assert m.group(1).rstrip('/') == SITE_URL.rstrip('/'), (
                f'{host} declares canonical {m.group(1)}, expected {SITE_URL}')
    finally:
        _app.IS_PROD = was_prod

    print(f'OK — {checked} pages: descriptions <=155, JSON-LD valid, '
          f'{len(C.JUDGMENTS)} judgments have Article schema, '
          f'{len(C.TOPICS)} topic hubs, {sum(outbound)} in-body internal links, '
          f'{len([s for s in slugs if inbound[s] == 0])} articles rely on their hub alone')


if __name__ == '__main__':
    main()
