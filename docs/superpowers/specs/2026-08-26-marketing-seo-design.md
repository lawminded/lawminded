# Marketing SEO programme — design

**Date:** 26 August 2026
**Source data:** `docs/gsc-performance-2026-08-26.xlsx` — Search Console, last 28 days, web search.

## The problem

The site is indexed and ranking. It is not being clicked.

| | Pages | Impressions | Clicks | CTR | Avg position |
|---|---:|---:|---:|---:|---:|
| Formats | 19 | 235 | 15 | **6.38%** | 21.0 |
| Articles | 121 | 3,576 | 26 | **0.73%** | 22.9 |
| Compare | 3 | 156 | 2 | 1.28% | 18.2 |
| Judgments | 7 | 44 | 0 | 0.00% | 76.2 |
| **Site total** | 167 | **4,136** | **59** | **1.43%** | — |

India alone is 2,544 impressions and 55 clicks (2.16%). The United States
contributes 788 impressions and zero clicks at an average position of 9.2 —
noise, not a market.

A page ranking eighth should earn roughly 3–4% of its impressions.
`/article/consumer-complaint-guide` ranks 8.7 and earns nothing from 55
impressions. `/article/fpo-further-public-offer-explained` ranks 7.6 and earns
nothing from 48. `/article/rights-issue-procedure-section-62` alone carries 554
impressions — 13.4% of the whole site — at position 11.1, and converts two of
them.

### One proven cause

The `seotitle` filter in `app.py` trims a long headline to 60 characters on a
word boundary, then drops a dangling connector (`and`, `of`, `the`, `&`).
Nothing catches a dangling noun or verb, so these are live in Google right now:

- `Auditor Appointment, Rotation & Removal: ADT-1, Sections`
- `How to File a Consumer Complaint Online on e-Jagriti - Step`
- `FPO (Further Public Offer): How Listed Companies Raise`

A title that stops mid-phrase reads as a broken page and costs the click. All
three sit on pages with real impressions and zero or near-zero clicks.

### One cause we cannot fix

`difference between rti and pil` ranks **4.6** with 15 impressions and zero
clicks. Top-five rank earning nothing is the signature of an AI Overview
answering the question above us. Some share of the CTR gap is structural and no
rewrite recovers it. This is stated here so that a partial recovery in Phase 1
is not read as a failure.

## What Google thinks this site is

The fifteen highest-impression pages are almost entirely Companies Act and SEBI:
rights issue, auditor rotation, KMP s.203, board committees, private placement,
secretarial standards, UPSI, minutes s.118, IPO/ICDR, SAST, bonus issue.

The owner's decision is to serve both audiences rather than abandon the
citizen-facing mission. The data supports this more than it first appears: the
citizen and tax guides *do* draw impressions — HUF (125), Income-tax Act 2025
(66), contract termination (63), labour codes (47) — they are simply buried at
positions 39 to 73. They need different treatment from the corporate pages, not
less attention.

## Scope

Forty-nine pages carry 80% of all impressions. They are the programme's target
set, split by what each actually needs.

**Bucket A — ranks 15 or better, CTR failing (23 pages).**
The rank is already there. A title and description rewrite is the entire fix.
Includes rights issue (554 impressions), influencer disclosure (146), KMP
(130), board committees (128), private placement (124), RTI vs PIL (105),
secretarial standards (103), UPSI (102).

**Bucket B — ranks 15–32, striking distance (13 pages).**
Title and description rewrite, plus enough content depth to close the gap to
page one. Includes auditor appointment (136), SEBI PIT (107), SAST (72),
perquisite valuation (63), AGM/EGM (58).

**Bucket C — ranks below 35 despite real impressions (13 pages).**
Google finds these relevant but ranks them poorly. Needs genuine content work or
consolidation, not metadata. This bucket is where most citizen-facing content
sits: HUF (125 impressions at 68.8), Income-tax Act 2025 (66 at 65.3), contract
termination (63 at 39.5), labour codes (47 at 73.2), Limitation Act (23 at 50).

Out of scope: off-page work of every kind — backlink outreach, social posting,
directory submission, Reddit and Quora. The owner has not committed to it and it
cannot be done from the codebase. This caps what Phases 2–4 can achieve and the
cap is accepted deliberately.

## Design

Phase 1 is the only phase specified to implementation detail here, and the
implementation plan that follows this spec covers Phase 1 alone. Phases 2 to 4
are sketched so the sequence is visible and so Phase 1's choices do not box them
out; each gets its own spec when the phase before it has reported.

### Phase 1 — CTR recovery

Add `SEO_TITLES` to `seo_meta.py`, keyed by slug, mirroring the existing
`SEO_DESCRIPTIONS` dict directly above it. That file's own docstring records why
this shape was chosen: it is a plain module rather than a database column so it
ships with an ordinary `git push` — no migration, no script run against the
production database. The same reasoning applies unchanged to titles.

`seotitle` gains one lookup at the top of its fallback chain:

1. `SEO_TITLES[slug]` — hand-written, always preferred
2. the `seo_title` database column — kept, admin-editable, unchanged
3. the truncating fallback — kept for the ~90 pages nobody will hand-write

Hand-write titles and descriptions for all 49 target pages. Each title
front-loads the phrase people actually search, keeps its statute reference
(Search Console confirms section numbers are searched directly — `section 203 of
companies act 2013`, `62(1)(a)`, `section 68`), and is a complete phrase within
60 characters.

Harden the fallback for the ~90 pages nobody hand-writes. When the headline is
too long, prefer the last clause boundary — comma, colon, semicolon, or spaced
dash — that falls between 30 and 60 characters, and only trim on a word boundary
when no such boundary exists.

Checked against the observed breakages, this rule fixes two of three:

| Headline | Today | With the rule |
|---|---|---|
| `Auditor Appointment, Rotation & Removal: ADT-1, Sections 139-140` | `…ADT-1, Sections` | `…Removal: ADT-1` |
| `How to File a Consumer Complaint Online on e-Jagriti - Step-by-Step Guide` | `…e-Jagriti - Step` | `…on e-Jagriti` |
| `FPO (Further Public Offer): How Listed Companies Raise Capital Again` | `…Companies Raise` | unchanged — no boundary in range |
| `Appointment of KMP: Section 203 Thresholds for MD, CFO & CS` | already fits | untouched |

It is a safety net that measurably reduces breakage, not a cure. FPO shows the
limit: no heuristic can tell that `Raise` dangles while `Removal` does not. Every
one of the 49 target pages therefore gets a hand-written entry, and after the
rule lands, all remaining rendered titles are reviewed and any that still read
broken are hand-written too.

**Tests.** `test_seo.py` gains: no rendered title on any page type exceeds 60
characters; the shortener produces the expected output for a fixed table of real
headlines, including the two it now fixes and the one it cannot; every
`SEO_TITLES` key matches a live article slug (the same guard `INTERNAL_LINKS`
already has, so a slug rename fails the build rather than silently going stale).

A test asserting "no title ends on a dangling word" is deliberately *not*
written. As the table above shows, that property is not decidable — `Removal` is
a fine ending and `Raise` is not, and nothing in the string distinguishes them.
The table of known cases is the honest guard.

**Deployment.** Staged locally, tests run, before/after title list shown to the
owner for approval, then `git push` and `./deploy/update.sh`.

### Phase 2 — depth on Buckets B and C

Bucket B pages get an answer-first opening block (the question restated and
answered in about 40 words before any preamble), a fact table carrying the
deadlines, forms, thresholds and penalties, and `HowTo` schema where the guide
is genuinely procedural. Tables are already supported — `.prose-table` CSS
exists and 43 tables live in the seed files — the high-traffic guides simply do
not use them.

Bucket C pages are diagnosed individually before anything is written. A page at
position 68 with 125 impressions is not failing on metadata, and the honest
answers may include merging it into a stronger page or accepting that it needs
links the programme cannot supply.

### Phase 3 — the format library

Format pages convert at 6.38%, nearly nine times the articles, and only 19 of 55
draw impressions at all. The other 36 get the same title and description
treatment plus unique lead-in content — when to use this document, what to fill
in, which provision it serves. `/templates` itself ranks 47.7 and needs to work
as a real landing page.

The near-duplicate risk flagged in `GEO-ANALYSIS.md` applies: many board
resolutions differ by a few lines. Thicken the unique part of each page rather
than removing pages.

### Phase 4 — demand-capture assets

Calculators and tools that earn links without outreach. Scoped after Phases 1–3
report, because their design should be informed by what the earlier phases
reveal about which queries convert.

## Success criteria

Measured against a fresh Search Console export 28 days after Phase 1 deploys.

- Article CTR rises from 0.73% toward 2.5%. On current impressions that is
  roughly 26 clicks a month becoming roughly 90.
- `/article/rights-issue-procedure-section-62` improves on 2 clicks from 554
  impressions.
- No page regresses in average position.

Phase 1 succeeds or fails on its own numbers before Phase 2 begins. If rewritten
titles do not move CTR, the AI Overview explanation is the dominant one and
Phases 2–4 need rethinking rather than executing.

## Risks

**Average position is an average.** A page showing 11.1 may rank third for a
rare query and thirtieth for a common one. The per-page CTR argument is drawn
from a consistent pattern across many pages, not from any single figure.

**The query sheet is thin.** Search Console anonymises rare queries: the export
attributes only 390 of 4,136 impressions to a named query. Page-level data is
sound; query-level targeting is directional.

**Twenty-eight days is a short window.** 59 clicks is a small number and normal
variation is wide. The follow-up export is a signal, not proof.
