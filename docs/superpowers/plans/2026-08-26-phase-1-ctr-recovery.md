# Phase 1 CTR Recovery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Stop Law Minded rendering broken and over-long `<title>` tags in Google, and hand-write titles for the 47 live pages that carry 80% of the site's search impressions.

**Architecture:** Titles are built in two places — the `seotitle` filter in `app.py` (articles only) and free-form `{% block title %}` strings in the other page templates. Both produce titles that Google cuts off. This plan adds a hand-written `SEO_TITLES` dict to `seo_meta.py` mirroring the `SEO_DESCRIPTIONS` dict already there, makes `seotitle` prefer it, improves the automatic fallback for the ~90 pages nobody hand-writes, and shortens the format and compare title patterns so a single template edit fixes 54 format pages at once.

**Tech Stack:** Flask 3.0.3, Jinja2 templates, SQLite. Tests are plain asserts run with `python3 test_seo.py` — no pytest, no fixtures.

## Global Constraints

- **Python interpreter:** `/usr/bin/python3`. It is the only interpreter on this machine with Flask and the app's other dependencies installed. `python3` on PATH resolves to Homebrew Python 3.14, which has none of them.
- **Run tests with:** `/usr/bin/python3 test_seo.py` from the repo root. There is no pytest. Tests are functions called from `main()` and assert directly.
- **Title budget:** 60 characters for the entire rendered `<title>`, brand suffix included. This is Google's approximate display width and the number the existing `seotitle` filter already uses.
- **Brand suffix:** `' - Law Minded'` (13 characters, leading space-hyphen-space). Appended only when the result still fits in 60. Never truncate to make it fit.
- **No database migration.** Every change ships with `git push` plus `./deploy/update.sh`. `seo_meta.py` exists specifically so search metadata deploys this way — its module docstring records that decision. Do not add a column.
- **The `seo_title` database column stays.** It is admin-editable and used by the article editor at `templates/admin/article_edit.html:40`. It keeps working; `SEO_TITLES` simply takes precedence over it.
- **Deployment is gated on owner approval.** Build locally, run tests, produce the before/after report in Task 8, and stop. Do not `git push` or run `deploy/update.sh`.
- **Indian English, sentence-accurate statute references.** Section numbers are proven search terms — Search Console shows `section 203 of companies act 2013`, `62(1)(a)`, `kmp section`, `what is upsi` — so keep them in the title wherever they fit.

---

### Task 1: Guard title length sitewide, and fix the format page pattern

54 of 55 format pages render titles over 60 characters (average 79, longest 105), because `format.html` appends 41 characters of boilerplate to the document name. Format pages convert at 6.38% CTR — nine times the article average — so this is the highest-value single edit in the plan.

**Files:**
- Modify: `templates/format.html:4`
- Modify: `test_seo.py` (add `test_title_length` and call it from `main()`)

**Interfaces:**
- Consumes: nothing from earlier tasks.
- Produces: `test_title_length()` in `test_seo.py`, which every later task re-runs. It crawls the same page list `main()` already builds and asserts `len(title) <= 60`.

- [ ] **Step 1: Write the failing test**

Add to `test_seo.py`, above `main()`:

```python
TITLE_RE = re.compile(r'<title>(.*?)</title>', re.S)
TITLE_MAX = 60


def test_title_length(client, paths):
    """Google shows roughly 60 characters of a <title>. Anything longer is cut
    off by the search engine itself, mid-word, and reads as a broken page.

    Article titles go through the `seotitle` filter, which already respects the
    limit. Every other page type builds its title by string concatenation in the
    template, where nothing enforces it."""
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
        f'Google truncates mid-word:\n' + '\n'.join(
            f'  {n} chars  {p}\n    {t}' for n, p, t in sorted(too_long, reverse=True)[:10]))
```

Add `import html` to the imports at the top of `test_seo.py` (it currently imports `collections`, `json`, `re`).

Call it from `main()`, alongside the existing checks, passing the same client and path list `main()` already assembles for the description check.

- [ ] **Step 2: Run the test to verify it fails**

Run: `/usr/bin/python3 test_seo.py`

Expected: FAIL, an assertion naming ~56 pages over 60 characters — 54 `/format/...` pages plus `/compare/consumer-forum-vs-civil-court` and `/compare/lease-vs-leave-and-license`.

- [ ] **Step 3: Shorten the format title pattern**

`templates/format.html:4` currently reads:

```jinja
{% block title %}{{ fmt['title'] }} — Free Word Format Download | Law Minded{% endblock %}
```

Replace with a pattern that keeps the searched words (`free`, `word`, `format`) but drops 22 characters of boilerplate, appending the brand only when it fits:

```jinja
{% block title %}{% set t = fmt['title'] ~ ' — Free Word Format' %}{{ t ~ ' | Law Minded' if t|length <= 47 else t }}{% endblock %}
```

Worked examples:
- `Deed of Cancellation — Free Word Format` is 39 → brand fits → 52 chars
- `Minutes – Audit Committee Meeting — Free Word Format` is 52 → brand omitted → 52 chars
- `Board Resolution – General Template — Free Word Format` is 54 → brand omitted → 54 chars

- [ ] **Step 4: Shorten the compare title pattern**

`templates/compare.html:3` currently reads:

```jinja
{% block title %}{% if current %}{{ current.title }} — Compared Side by Side | Law Minded{% else %}Compare Indian Laws Side by Side — 5 Comparisons | Law Minded{% endif %}{% endblock %}
```

Search Console shows the real query shape is `difference between rti and pil`, not `rti vs pil compared side by side`. Lead with the word people type:

```jinja
{% block title %}{% if current %}{% set t = current.title ~ ': Key Differences Compared' %}{{ t ~ ' | Law Minded' if t|length <= 47 else t }}{% else %}Compare Indian Laws Side by Side | Law Minded{% endif %}{% endblock %}
```

Worked examples:
- `RTI vs PIL: Key Differences Compared` is 36 → brand fits → 49 chars
- `Consumer Forum vs Civil Court: Key Differences Compared` is 54 → brand omitted → 54 chars
- `Lease vs Leave and License: Key Differences Compared` is 51 → brand omitted → 51 chars

- [ ] **Step 5: Run the test to verify it passes**

Run: `/usr/bin/python3 test_seo.py`

Expected: PASS. If any format document has a name long enough to breach 60 on its own, the assertion names it — shorten that document's `title` in the database seed rather than weakening the limit.

- [ ] **Step 6: Commit**

```bash
git add templates/format.html templates/compare.html test_seo.py
git commit -m "Stop Google cutting off the titles it shows for formats

54 of 55 format pages rendered a title past the width Google displays,
averaging 79 characters, because the template appended 41 characters of
boilerplate to every document name. Format pages convert nine times better
than articles, so they were the worst place to lose the end of the title.

Compare pages now lead on 'Key Differences' — Search Console shows people
type 'difference between rti and pil', not 'compared side by side'."
```

---

### Task 2: Stop the automatic shortener cutting titles mid-phrase

120 of 133 published articles render a title that stops mid-phrase: `…ADT-1, Sections`, `…e-Jagriti - Step`, `…How Listed Companies Raise`. The `seotitle` filter trims on a word boundary and strips a trailing connector (`and`, `of`, `the`, `&`) but nothing catches a dangling noun or verb.

Preferring the last clause boundary fixes two of the three observed cases and leaves already-good titles untouched. It cannot fix all of them — no rule can tell that `Raise` dangles while `Removal` does not — which is why the 47 highest-traffic pages get hand-written titles in Task 5.

**Files:**
- Modify: `app.py:570-583` (the `if len(title) > maxlen:` branch of `seotitle`)
- Modify: `test_seo.py` (add `test_seotitle_cases` and call it from `main()`)

**Interfaces:**
- Consumes: `test_title_length()` from Task 1 must still pass.
- Produces: `seotitle(article, brand=' - Law Minded', maxlen=60)` keeps its exact signature. Task 3 modifies the same function's lookup order and relies on the truncation branch remaining the last resort.

- [ ] **Step 1: Write the failing test**

Add to `test_seo.py`:

```python
def test_seotitle_cases():
    """The automatic shortener must not leave a title ending mid-phrase.

    Each case is a real headline from the site. `expected` is the whole rendered
    title including the ' - Law Minded' suffix where it fits in 60 characters."""
    cases = [
        # Trims at the last clause boundary instead of mid-phrase.
        ('Auditor Appointment, Rotation & Removal: ADT-1, Sections 139-140',
         'Auditor Appointment, Rotation & Removal: ADT-1'),
        ('How to File a Consumer Complaint Online on e-Jagriti - Step by Step',
         'How to File a Consumer Complaint Online on e-Jagriti'),
        # Already inside the budget: untouched, and the brand fits.
        ('Reduction of Share Capital',
         'Reduction of Share Capital - Law Minded'),
        # Inside the budget without the brand, which does not fit.
        ('Appointment of KMP: Section 203 Thresholds for MD, CFO & CS',
         'Appointment of KMP: Section 203 Thresholds for MD, CFO & CS'),
        # No clause boundary in range: falls back to the word-boundary trim.
        ('FPO (Further Public Offer): How Listed Companies Raise Capital Again',
         'FPO (Further Public Offer): How Listed Companies Raise'),
    ]
    for headline, expected in cases:
        got = seotitle({'title': headline, 'seo_title': None, 'slug': ''})
        assert got == expected, (
            f'seotitle({headline!r})\n  got      {got!r}\n  expected {expected!r}')
        assert len(got) <= TITLE_MAX, f'{got!r} is {len(got)} chars'
```

Import `seotitle` from `app` — change line 13 of `test_seo.py` to:

```python
from app import app, JUDGMENTS_PUBLISHED, autolink, seotitle, SITE_URL
```

While editing that import block, drop the duplicated `RETIRED_ARTICLES` on line 14; it is imported twice.

Call `test_seotitle_cases()` from `main()`.

- [ ] **Step 2: Run the test to verify it fails**

Run: `/usr/bin/python3 test_seo.py`

Expected: FAIL on the first case — got `'Auditor Appointment, Rotation & Removal: ADT-1, Sections'`, expected `'Auditor Appointment, Rotation & Removal: ADT-1'`.

- [ ] **Step 3: Prefer the last clause boundary**

In `app.py`, inside `seotitle`, replace the `if len(title) > maxlen:` block (currently lines 570-583) with:

```python
        if len(title) > maxlen:
            # Prefer the last clause boundary that leaves a substantial title.
            # Cutting at a comma, colon or dash ends on a complete phrase;
            # cutting on a word boundary can strand the first word of one
            # ("... ADT-1, Sections", "... on e-Jagriti - Step").
            boundary = None
            for m in _CLAUSE_RE.finditer(title):
                if _CLAUSE_FLOOR <= m.start() <= maxlen:
                    boundary = m.start()
            if boundary is not None:
                title = title[:boundary].rstrip(' ,;:-–—&')
            else:
                cut = title[:maxlen]
                if ' ' in cut:
                    cut = cut[:cut.rindex(' ')]
                title = cut.rstrip(' ,;:-–—&')
                # Drop a dangling connector so the title doesn't read as cut off
                # mid-phrase ("… Section 63 Sources, Conditions &").
                while True:
                    head, _, last = title.rpartition(' ')
                    if head and last.lower() in ('and', 'the', 'a', 'an', 'of', 'for',
                                                 'in', 'on', 'to', 'with', '&'):
                        title = head.rstrip(' ,;:-–—&')
                        continue
                    break
```

Define the two constants just above the `seotitle` filter, next to the other module-level regexes:

```python
# A clause boundary is where a title can be cut and still read as a finished
# phrase. Below _CLAUSE_FLOOR characters the remainder is too short to describe
# the page, so a word-boundary trim of the full headline beats it.
_CLAUSE_RE = re.compile(r'[,:;]|\s[-–—]\s')
_CLAUSE_FLOOR = 30
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `/usr/bin/python3 test_seo.py`

Expected: PASS, including `test_title_length` from Task 1.

- [ ] **Step 5: Commit**

```bash
git add app.py test_seo.py
git commit -m "Cut a long headline at a clause, not mid-phrase

The shortener trimmed on a word boundary, which left 120 of 133 articles
ending on the first word of a phrase — 'ADT-1, Sections', 'e-Jagriti - Step'.
Cutting at the last comma, colon or dash instead ends on a complete thought.

This does not fix every case: nothing can tell that 'Raise' dangles while
'Removal' does not. The pages that matter get written by hand."
```

---

### Task 3: Add the SEO_TITLES lookup

`seo_meta.py` already holds 102 hand-written search descriptions keyed by slug, as a plain module so they deploy with `git push` and no migration. Titles get the same treatment.

**Files:**
- Modify: `seo_meta.py` (add the `SEO_TITLES` dict, empty for now, above `SEO_DESCRIPTIONS`)
- Modify: `app.py:36` (import), `app.py:557` (lookup order)
- Modify: `test_seo.py` (add `test_seo_titles_valid`, call it from `main()`)

**Interfaces:**
- Consumes: `seotitle` from Task 2, whose truncation branch becomes the third and last fallback.
- Produces: `SEO_TITLES: dict[str, str]` — slug to bare title, no brand suffix. `seotitle` appends the brand when it fits, exactly as it does for the other two sources. Task 5 fills this dict.

- [ ] **Step 1: Write the failing test**

Add to `test_seo.py`:

```python
def test_seo_titles_valid(slugs):
    """Every hand-written title must fit the budget and point at a live page.

    The slug check is the same guard INTERNAL_LINKS already has: when an article
    is renamed, the stale entry fails the build instead of silently going dead."""
    for slug, title in SEO_TITLES.items():
        assert slug in slugs, (
            f'SEO_TITLES has an entry for {slug!r}, which is not a published '
            f'article. Rename it or remove it.')
        assert title == title.strip(), f'{slug}: title has stray whitespace'
        assert len(title) <= TITLE_MAX, (
            f'{slug}: hand-written title is {len(title)} chars, over {TITLE_MAX}\n'
            f'  {title}')


def test_seo_title_wins(client):
    """A hand-written title beats both the database column and the shortener."""
    if not SEO_TITLES:
        return
    slug, expected = next(iter(SEO_TITLES.items()))
    html_out = client.get(f'/article/{slug}', base_url=SITE_URL).get_data(as_text=True)
    got = html.unescape(TITLE_RE.search(html_out).group(1).strip())
    assert got.startswith(expected), (
        f'/article/{slug} rendered {got!r}, expected it to start with {expected!r}')
```

Import `SEO_TITLES` on line 14 of `test_seo.py`:

```python
from seo_meta import SEO_DESCRIPTIONS, SEO_TITLES, RETIRED_ARTICLES
```

Call both from `main()`, passing the published-slug set `main()` already builds.

- [ ] **Step 2: Run the test to verify it fails**

Run: `/usr/bin/python3 test_seo.py`

Expected: FAIL with `ImportError: cannot import name 'SEO_TITLES' from 'seo_meta'`.

- [ ] **Step 3: Add the dict**

In `seo_meta.py`, directly above `SEO_DESCRIPTIONS = {`, add:

```python
# Hand-written <title> tags, keyed by article slug, for the pages that carry the
# traffic. Same reasoning as SEO_DESCRIPTIONS below and the same deployment
# story: a plain module ships with `git push`, no migration.
#
# The automatic shortener in app.py trims a long editorial headline to fit
# Google's ~60-character display width. It cannot always end on a complete
# phrase, so the pages Search Console shows people actually reaching get a title
# written for the query rather than derived from the headline.
#
# Values carry no brand suffix. `seotitle` appends ' - Law Minded' when the
# result still fits in 60 characters.
SEO_TITLES = {}

```

- [ ] **Step 4: Wire the lookup into seotitle**

In `app.py`, change the import on line 36 to:

```python
from seo_meta import SEO_DESCRIPTIONS, SEO_TITLES, INTERNAL_LINKS, RETIRED_ARTICLES
```

In `seotitle`, replace line 557 (`title = _get(article, 'seo_title')`) with:

```python
    # Three sources, most deliberate first: a title written for the query, the
    # admin-editable column, then the shortened headline.
    title = SEO_TITLES.get(_get(article, 'slug'), '') or _get(article, 'seo_title')
```

Update the docstring's first sentence to name the new source:

```python
    """Build a search-friendly <title>. Prefers a hand-written SEO_TITLES entry,
    then the article's explicit seo_title column, and otherwise shortens the long
    editorial headline (trimming at a clause boundary where one fits, else on a
    word boundary). The ' - Law Minded' suffix is only appended when the whole
    thing still fits Google's ~60-char display width, so titles stop truncating
    mid-phrase in search results."""
```

- [ ] **Step 5: Run the tests to verify they pass**

Run: `/usr/bin/python3 test_seo.py`

Expected: PASS. `test_seo_title_wins` returns early while the dict is empty; Task 5 fills it.

- [ ] **Step 6: Commit**

```bash
git add app.py seo_meta.py test_seo.py
git commit -m "Let a page carry a title written for the query it answers

Descriptions have been hand-written per slug for a while; titles could only
be the headline, shortened. Adds the matching dict and prefers it, so the
pages people actually reach can say what they searched for.

Empty for now — the entries land next."
```

---

### Task 4: Fill in the four missing search descriptions

35 of the 41 target articles already have a hand-written description. Four fall back to the article `summary`, which opens on a narrative hook — right on the page, wrong in a search result. The other two are 301 redirects and need nothing.

**Files:**
- Modify: `seo_meta.py` (four entries in `SEO_DESCRIPTIONS`, in existing alphabetical position)

**Interfaces:**
- Consumes: nothing.
- Produces: nothing consumed later.

- [ ] **Step 1: Confirm they are missing**

Run:

```bash
/usr/bin/python3 -c "
import sys; sys.path.insert(0, '.')
from seo_meta import SEO_DESCRIPTIONS
for s in ['influencer-disclosure-misleading-ads', 'new-labour-codes-explained',
          'epf-esi-social-security-code', 'limitation-act-1963-guide']:
    print(('HAS ' if s in SEO_DESCRIPTIONS else 'MISSING '), s)"
```

Expected: all four print `MISSING`.

- [ ] **Step 2: Add the entries**

Insert each into `SEO_DESCRIPTIONS` at its alphabetical position, matching the file's existing two-line style:

```python
    'epf-esi-social-security-code':
        "EPF and ESI in 2026: the wage ceilings that trigger each deduction, "
        "the contribution rates, and what employers must file.",
    'influencer-disclosure-misleading-ads':
        "India's disclosure rules for paid posts: what counts as a material "
        "connection, the labels that satisfy the law, and the penalties.",
    'limitation-act-1963-guide':
        "How long you have to file: the Limitation Act's periods for contracts, "
        "recovery and appeals, when the clock starts, and when it can be paused.",
    'new-labour-codes-explained':
        "India's four labour codes took effect on 21 November 2025, replacing 29 "
        "laws. What changed for wages, hours, social security and termination.",
```

- [ ] **Step 3: Run the tests to verify they pass**

Run: `/usr/bin/python3 test_seo.py`

Expected: PASS. The existing description-length check confirms each renders at 155 characters or fewer.

- [ ] **Step 4: Commit**

```bash
git add seo_meta.py
git commit -m "Give four more pages a description written for search

They were falling back to the article summary, which opens on a narrative
hook — the right voice on the page and the wrong one in a result list."
```

---

### Task 5: Hand-write titles for the 39 target articles

These are the article pages inside the 80%-of-impressions set. Each title leads with the phrase people search, keeps its statute reference where one fits, and is a complete phrase within the budget.

**Files:**
- Modify: `seo_meta.py` (fill `SEO_TITLES`)

**Interfaces:**
- Consumes: `SEO_TITLES` from Task 3 and its two guard tests.
- Produces: nothing consumed later.

- [ ] **Step 1: Fill the dict**

Replace `SEO_TITLES = {}` in `seo_meta.py` with the entries below, keeping the comment block above it. Impressions and position are from the 26 August 2026 export and are noted so a later reader knows why these slugs and not others.

```python
SEO_TITLES = {
    # Ordered by impressions in the 2026-08-26 Search Console export. The
    # comment on each line is impressions · average position at that time.
    # Sits at the 60-char ceiling if 'Under' is kept. Google's real limit is
    # pixel width, not characters, so the site's biggest page does not run to
    # the edge of the heuristic.
    'rights-issue-procedure-section-62':
        'Rights Issue Section 62(1)(a): Procedure, Renunciation',  # 554 · 11.1
    'influencer-disclosure-misleading-ads':
        "Influencer Disclosure & Misleading Ad Rules in India 2026",  # 146 · 7.1
    'auditor-appointment-rotation-removal':
        'Auditor Appointment & Rotation: ADT-1, Sections 139-140',  # 136 · 17.8
    'appointment-of-kmp-section-203':
        'Appointment of KMP Under Section 203: MD, CFO & CS Rules',  # 130 · 11.4
    'board-committees-audit-nrc-stakeholders':
        'Board Committees Under Sections 177 & 178: Audit, NRC, SRC',  # 128 · 12.1
    'hindu-undivided-family-huf-tax-guide':
        'HUF Explained: How to Create One and What It Saves in Tax',  # 125 · 68.8
    'private-placement-section-42':
        'Private Placement Under Section 42: PAS-4, PAS-3 & Limits',  # 124 · 13.2
    'sebi-pit-insider-trading-explained':
        'SEBI Insider Trading Rules (PIT): UPSI, Trading Window',  # 267 consolidated · 23.2
    'secretarial-standards-ss-1-ss-2':
        'Secretarial Standards SS-1 & SS-2: Are They Mandatory?',  # 103 · 13.0
    'drafting-maintaining-minutes-section-118':
        'Minutes of Meetings Under Section 118: Rules & Time Limits',  # 80 · 12.4
    'ipo-sebi-icdr-eligibility-process':
        'IPO Under SEBI ICDR 2018: Eligibility & Listing Process',  # 79 · 9.7
    'sebi-sast-takeover-code-open-offer':
        'SEBI Takeover Code (SAST) 2011: Open Offer Triggers',  # 72 · 22.3
    'income-tax-act-2025-what-changed':
        'Income-tax Act 2025: What Changed on 1 April 2026',  # 66 · 65.3
    'perquisite-valuation-rules-2026-salaried':
        'Perquisite Valuation Rules 2026: Car, HRA & Meal Limits',  # 63 · 20.7
    'how-to-terminate-a-contract':
        'How to Terminate a Contract Legally in India',  # 63 · 39.5
    'conducting-agm-egm-companies-act':
        'AGM & EGM Rules: Notice, Quorum, Proxies & E-Voting',  # 58 · 28.2
    'consumer-complaint-guide':
        'How to File a Consumer Complaint Online on e-Jagriti',  # 55 · 8.7
    'fpo-further-public-offer-explained':
        'FPO Explained: How Listed Companies Raise Capital Again',  # 48 · 7.6
    'new-labour-codes-explained':
        "India's New Labour Codes 2025: What Changed for Employers",  # 47 · 73.2
    'bonus-issue-of-shares-section-63':
        'Bonus Issue Under Section 63: Sources, Conditions, Process',  # 44 · 22.0
    'dematerialization-of-shares':
        'Dematerialization of Shares: Rules for Private Companies',  # 41 · 43.4
    'posh-internal-committee-small-company':
        'POSH Internal Committee Rules for Small Companies',  # 39 · 8.0
    'llp-capital-contribution-increase-reduction':
        "LLP Capital Contribution: How to Increase or Reduce It",  # 38 · 7.1
    'alteration-of-moa-aoa-section-13-14':
        'Alteration of MOA & AOA: Sections 13, 14 and MGT-14',  # 38 · 22.8
    'eway-bill-ship-to-gstin-mandatory-2026':
        'Ship-to GSTIN Now Mandatory on E-Way Bills (Aug 2026)',  # 38 · 26.2
    'secretarial-audit-mr-3-section-204':
        'Secretarial Audit Under Section 204: MR-3 Applicability',  # 37 · 12.2
    'dpdp-rules-2025-compliance-timeline':
        'DPDP Rules 2025: The Full Compliance Deadline Calendar',  # 34 · 8.2
    'ccfs-2026-companies-compliance-facilitation-scheme':
        'CCFS-2026: Cut ROC Late Fees by 90% Before 31 August',  # 33 · 14.2
    'statutory-registers-and-records':
        'Statutory Registers Every Indian Company Must Keep',  # 33 · 48.1
    'share-transfer-private-company-sh4':
        'Share Transfer in a Private Company: Form SH-4 Procedure',  # 33 · 40.2
    'director-duties':
        'Director Duties Under the Companies Act 2013',  # 32 · 57.3
    'reduction-of-share-capital-section-66':
        'Reduction of Share Capital Under Section 66: NCLT Route',  # 29 · 26.6
    'cci-merger-control-sun-pharma-ranbaxy':
        'CCI Merger Control: Thresholds & the Deal Value Test',  # 28 · 10.4
    'epf-esi-social-security-code':
        'EPF & ESI Rules 2026: Wage Ceilings and Employer Duties',  # 28 · 15.8
    'msme-development-amendment-bill-2026':
        'MSME Amendment Bill 2026: Delayed Payment Rules Explained',  # 26 · 7.0
    'gig-platform-workers-rights-labour-codes':
        "Gig Worker Rights Under India's Labour Codes",  # 26 · 28.8
    'sebi-pit-compliance-solutions-founders-kmp':
        'SEBI PIT Compliance for Founders and KMPs',  # 26 · 38.0
    'mergers-amalgamations-companies-act':
        'Mergers & Amalgamations Under the Companies Act 2013',  # 24 · 30.7
    'limitation-act-1963-guide':
        'Limitation Act 1963: Time Limits to File a Case in India',  # 23 · 50.0
}
```

- [ ] **Step 2: Run the tests to verify they pass**

Run: `/usr/bin/python3 test_seo.py`

Expected: PASS. `test_seo_titles_valid` confirms every slug is live and every title fits 60 characters; `test_seo_title_wins` confirms the first entry actually renders.

If a slug fails the live check, it has been renamed or retired — look it up in `RETIRED_ARTICLES` in the same file and use the surviving slug.

- [ ] **Step 3: Commit**

```bash
git add seo_meta.py
git commit -m "Write titles for the 39 pages people actually reach

Taken from the pages carrying 80% of impressions. Each leads with the phrase
people type and keeps its section number — Search Console shows the numbers
get searched directly, 'kmp section' and '62(1)(a)' among them.

Impressions and position are noted per line so a later reader can tell why
these slugs were chosen and re-check them against a fresh export."
```

---

### Task 6: Retitle the templates landing page

`/templates` draws 30 impressions at average position 47.7 and no clicks, with a title that omits the two things that make the page worth clicking: how many formats there are and that they are Word files.

**Files:**
- Modify: `templates/templates_page.html:3`

**Interfaces:**
- Consumes: `test_title_length()` from Task 1.
- Produces: nothing consumed later.

- [ ] **Step 1: Change the title**

`templates/templates_page.html:3` currently reads:

```jinja
{% block title %}Free Legal Document Templates - Law Minded{% endblock %}
```

Replace with:

```jinja
{% block title %}55 Free Indian Legal Document Formats (Word){% endblock %}
```

That is 44 characters. The brand is deliberately dropped: the count and the file type earn the click, and the page already ranks for brand queries.

- [ ] **Step 2: Run the tests to verify they pass**

Run: `/usr/bin/python3 test_seo.py`

Expected: PASS.

- [ ] **Step 3: Commit**

```bash
git add templates/templates_page.html
git commit -m "Say how many formats there are, and that they are Word files

The page drew 30 impressions and no clicks at position 48 with a title that
mentioned neither."
```

---

### Task 7: Verify the whole site and produce the before/after report

The owner approves before anything deploys. This task produces what they read.

**Files:**
- Create: `docs/phase-1-title-changes.md`

**Interfaces:**
- Consumes: every earlier task.
- Produces: the report the owner approves. Nothing consumes it in code.

- [ ] **Step 1: Re-measure the site**

Run:

```bash
/usr/bin/python3 - <<'PY'
import html, re, sys
sys.path.insert(0, '.')
from app import app, SITE_URL
import database

T = re.compile(r'<title>(.*?)</title>', re.S)
conn = database.get_db()
arts = [(r['slug'], r['title']) for r in conn.execute(
    'SELECT slug, title FROM articles WHERE published=1')]
conn.close()

trunc = over = ok = 0
with app.test_client() as c:
    for slug, raw in arts:
        r = c.get(f'/article/{slug}', base_url=SITE_URL)
        if r.status_code != 200:
            continue
        t = html.unescape(T.search(r.get_data(as_text=True)).group(1).strip())
        bare = t[:-len(' - Law Minded')] if t.endswith(' - Law Minded') else t
        if bare != raw and raw.startswith(bare[:max(len(bare)-2, 1)]):
            trunc += 1
        elif len(t) > 60:
            over += 1
        else:
            ok += 1
print(f'articles: {trunc} truncated, {over} over 60, {ok} clean (of {len(arts)})')
PY
```

Expected: truncated count well below the 120 measured before the plan, and `over` at 0. The remainder are low-traffic pages the shortener handles acceptably.

- [ ] **Step 2: Generate the before/after table**

`git stash` is shared across worktrees on this machine and unsafe here, so the
"before" column comes from a second checkout rather than from stashing. Run:

```bash
BASE=$(git rev-parse HEAD~6)
WT=$(mktemp -d)/before
git worktree add -q "$WT" "$BASE"
cp lawminded.db "$WT/lawminded.db" 2>/dev/null || true

/usr/bin/python3 - "$WT" <<'PY' > /tmp/titles-before.tsv
import html, re, subprocess, sys
code = r'''
import html, re, sys
sys.path.insert(0, ".")
from app import app, SITE_URL
import database
T = re.compile(r"<title>(.*?)</title>", re.S)
conn = database.get_db()
slugs = [r["slug"] for r in conn.execute("SELECT slug FROM articles WHERE published=1")]
conn.close()
paths = [f"/article/{s}" for s in slugs] + [
    "/templates", "/compare/rti-vs-pil", "/compare/consumer-forum-vs-civil-court",
    "/format/deed-of-cancellation", "/format/minutes-audit-committee-meeting",
    "/format/board-resolution-general-template"]
with app.test_client() as c:
    for p in paths:
        r = c.get(p, base_url=SITE_URL)
        if r.status_code != 200:
            continue
        m = T.search(r.get_data(as_text=True))
        if m:
            print(p + "\t" + html.unescape(m.group(1).strip()))
'''
subprocess.run(['/usr/bin/python3', '-c', code], cwd=sys.argv[1], check=True)
PY

git worktree remove --force "$WT"
wc -l /tmp/titles-before.tsv
```

Then render the same paths at `HEAD` into `/tmp/titles-after.tsv` by running the
identical inner script from the repo root, and join the two files on the path
column to build the table.

If `HEAD~6` does not predate Task 1 — because commits were combined or split —
use `git log --oneline` to find the commit before the first Task 1 commit and set
`BASE` to it.

- [ ] **Step 3: Write the report**

Create `docs/phase-1-title-changes.md` with:

- A one-paragraph plain-English summary: what was broken, what changed, what the owner should expect.
- The counts before and after, from Step 1 and from the figures in the spec (120 of 133 truncated; 54 of 55 formats over-length).
- The before/after table from Step 2, sorted by impressions descending, covering the 39 hand-written articles plus the three format and two compare samples and `/templates`.
- The explicit caveat, restated from the spec: a page ranking 4.6 with zero clicks is probably losing them to an AI Overview, and no title rewrite recovers that.

- [ ] **Step 4: Run the full suite one final time**

Run: `/usr/bin/python3 test_seo.py`

Expected: PASS, with the summary line reporting the page count.

- [ ] **Step 5: Commit**

```bash
git add docs/phase-1-title-changes.md
git commit -m "Record what every changed title used to say

So the owner can approve the change by reading it, and so a later reader can
tell what moved when the next Search Console export comes in."
```

- [ ] **Step 6: Stop. Do not deploy.**

Report to the owner: the counts before and after, the report path, and that the branch is ready to push on their approval. Deployment is `git push` then `./deploy/update.sh` on the Oracle box — the owner's call, not the implementer's.

---

## Follow-up, not in this plan

- **Re-export Search Console 28 days after deploy** and re-run the striking-distance analysis. Phase 1 succeeds or fails on that number before Phase 2 starts.
- **The remaining ~80 truncated article titles.** They carry 20% of impressions between them. Worth doing once Phase 1 proves the effect is real.
- **Judgment pages** average position 76.2 with zero clicks across seven pages. They need diagnosis, not a title.
