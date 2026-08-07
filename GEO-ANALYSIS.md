# GEO / AI Search Analysis — lawminded.in

**Target:** https://lawminded.in/ (homepage, with site-wide sampling)
**Date:** 2026-08-07
**Framing:** Per [Google's AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), optimizing for generative AI search *is* SEO. Findings below are SEO fundamentals applied to AI-search surfaces, not a separate discipline.

---

## 0. Fix log — 2026-08-07

Scores below describe the site **as audited**, before these changes. Shipped since:

| # | Fix | Status |
|---|---|---|
| 1 | `/compare` server-rendered; one URL per comparison (`/compare/<slug>`), in sitemap | done |
| 2 | Homepage stat counters server-rendered with live counts (was `0+` pre-JS, and understated) | done |
| 3 | Hero chips linked to topic hubs (were plain text; 11 hubs were unlinked from `/`) | done |
| 4 | Homepage: author byline, ~130-word citable intro, dates on article cards, `ItemList` schema | done |
| 5 | Homepage `<title>` swapped off the zero-volume tagline | done |
| 6 | `dateModified` now moves on real content edits (`_touch` in database.py) | mechanism fixed, no backfill |
| — | **Bug found while verifying:** content migrations ran *before* the seeders, so on any fresh database every fix silently no-opped and stamped itself applied | fixed |
| 7 | One URL per document format (`/format/<slug>`), full document text rendered into the page, `DigitalDocument` + `BreadcrumbList` schema, all 55 in sitemap | done |
| 8 | Author bio page removed at owner's request — `/author/<slug>` 301s to `/about`, byline no longer links | done |

Sitemap went from 146 to **219 URLs**: +55 formats, +5 comparisons, −1 author page (the article count also drops 128→126 now that the dedup migration actually applies).

Not done, and why: no `Person` `sameAs` and no author page (owner declined, §5); no og:image card (needs a designed 1200×630 asset); no video, Reddit or YouTube presence — off-code work.

**Watch item:** the 55 format pages share a lot of boilerplate — many board resolutions differ by only a few lines. If Google dampens them as near-duplicates, the fix is to thicken the unique part of each page (when you'd use it, what to fill in, which section of the Companies Act it serves) rather than to remove the pages.

---

## 1. GEO Readiness Score: 58/100

| Dimension | Weight | Score | Verdict |
|---|---|---|---|
| Citability | 25% | 16/25 | Articles strong, homepage near-zero |
| Structural Readability | 20% | 15/20 | Excellent heading + paragraph discipline; no tables |
| Multi-Modal Content | 15% | 6/15 | Images only — no video, no charts, tables absent |
| Authority & Brand Signals | 20% | 7/20 | **Weakest.** Synthetic dates, orphaned entity, zero off-site presence |
| Technical Accessibility | 20% | 14/20 | SSR solid, crawlers allowed — one severe JS blind spot |

The site is **better built than most** on the things that are hard to retrofit (server-side rendering, schema, paragraph structure, author attribution in `Article` schema). It loses points almost entirely on signals that are cheap to fix.

---

## 2. Platform Breakdown

| Platform | Est. Score | Binding Constraint |
|---|---|---|
| **Google AI Overviews** | ~45/100 | Strongly ranking-correlated. Eligibility floor is "indexed + snippet-eligible". Per the SXO audit, the site does not appear to rank for its own brand or its article topics — so AIO is gated upstream by indexation, not by GEO quality. **Verify in GSC.** |
| **Google AI Mode** (Gemini 3.5 Flash) | ~52/100 | Weakly ranking-correlated, broader pool (~9 domains/query). Best near-term prospect. Held back by synthetic `dateModified` and zero entity corroboration. |
| **ChatGPT** | ~35/100 | Cites Wikipedia (47.9%) + Reddit (11.3%). Law Minded has neither. |
| **Perplexity** | ~30/100 | Cites Reddit (46.7%). Zero Reddit footprint found. |
| **Bing Copilot** | unverified | Bing indexation not checked in this audit. IndexNow status unknown. |

> AI Mode and AI Overviews agree ~86% of the time but cite the same URLs only **13.7%** of the time. Treat them as two surfaces. AI Mode is where freshness and entity authority pay off independently of rank — which is exactly where this site's cheapest wins are.

---

## 3. AI Crawler Access Status — PASS

`robots.txt` is `User-agent: * / Allow: / / Disallow: /admin`. No AI crawler is blocked.

Live UA verification against `/` — all returned **200**:

| Crawler | Status | Crawler | Status |
|---|---|---|---|
| GPTBot | 200 ✅ | PerplexityBot | 200 ✅ |
| OAI-SearchBot | 200 ✅ | CCBot | 200 ✅ |
| ChatGPT-User | 200 ✅ | Bytespider | 200 ✅ |
| ClaudeBot | 200 ✅ | Google-Extended | 200 ✅ |

No action needed. If you later want to withhold training data while keeping search visibility, block `CCBot` and `anthropic-ai` only — never `OAI-SearchBot`, `ChatGPT-User`, `ClaudeBot` or `PerplexityBot`, which serve live citations.

---

## 4. llms.txt Status — PRESENT, and unusually well-built

`/llms.txt` returns 200. 159 lines, 36KB, 132 article links across 12 topic sections, each with a description. This is a genuinely good file — better than most sites that ship one.

**It is worth approximately nothing for citations, and you should not invest another hour in it.**

| Source | Finding |
|---|---|
| John Mueller (Google), 2025 | "No AI system currently uses llms.txt." Compared it to meta keywords. |
| Gary Illyes (Google), Jul 2025 | Google has no plans to support it. |
| SE Ranking, 300k domains, Nov 2025 | Of the 50 most AI-cited domains, **one** had an llms.txt. |
| OtterlyAI server logs, 2025 | **0.1%** of AI-bot traffic requested it (84 of 62,100). |

Google's own AI optimization guide lists creating `llms.txt` under **myths**. Keep the file — it costs nothing and it does help AI coding agents quote you accurately — but treat it as shipped and done. `/llms-full.txt` (404) and RSL 1.0 (`/.well-known/rsl.xml`, 404) are not worth adding.

---

## 5. Brand Mention Analysis — the largest structural gap

Brand mentions correlate **3× more strongly** with AI visibility than backlinks (Ahrefs, 75k brands, Dec 2025).

| Platform | Correlation w/ AI citations | Law Minded presence |
|---|---|---|
| YouTube | ~0.737 (strongest known signal) | **None found** |
| Reddit | High | **None found** |
| Wikipedia | High | **None** |
| Wikidata | High | **None** |
| LinkedIn | Moderate | Brand URL in schema is `linkedin.com/in/lawminded/` — the `/in/` personal format, not `/company/` |
| X / Instagram | Low | Both resolve (200) |

**Author entity — closed by owner decision (2026-08-07).**

The `Person` schema at `/author/piyush-kundnani` carries `name`, `hasCredential` (B.Com) and `worksFor`, and deliberately carries **no `sameAs`, no `jobTitle`, no bio and no photo**. An earlier draft of this report recommended linking the author's personal profiles to strengthen entity resolution. The owner has declined, and the author page has been trimmed to name and qualification only.

Treat this as settled. Do not re-propose personal profile links, a bio paragraph, or an author photo — `app.py` and `test_seo.py` now both enforce the minimal shape.

The measurable consequence stands and is worth stating plainly: with no external corroboration, AI systems cannot resolve the author to a verified real-world identity, so author-level authority will not be a contributor to this site's AI visibility. That is an acceptable trade — it simply means the remaining levers (§8 items 1, 2, 4, and organisation-level presence) carry all the weight.

> **Caveat, and it matters:** WebSearch here is US-geo. Absence of Indian-audience Reddit/YouTube mentions in these results is suggestive, not conclusive. Verify against Indian SERPs before treating "zero presence" as fact.

---

## 6. Passage-Level Citability

**Optimal citation block: 134–167 words. ~44% of AI citations come from the first 30% of a page.**

### Articles — strong (20/25)

Sampled `/article/what-is-upsi-regulation-2-1-n` (1,819 words, 9 H2s):

- **30 paragraphs, average 34.8 words, only one over 100 words.** Textbook structure.
- A definitional block appears at roughly **5% page depth** — deep inside the high-citation zone:
  > "UPSI = information relating to a company or its securities that is not generally available and, once available, is likely to materially affect the price. The 2025 amendment expanded the illustrative list from 5 items to 16."

  This follows the `X = ...` pattern AI extractors favour, is fully self-contained, and carries a specific number. It is the best-constructed citable passage on the site.
- Section headings are extraction-friendly: `Worked example`, `Common mistakes`, `Checklist`, `FAQ`, and one question-form H2 (`When does UPSI stop being UPSI?`).
- FAQ answers are short, factual and quotable: *"At least 8 years, with time-stamped and non-tamperable audit trails."* / *"10 June 2025 — 90 days from the 11/12 March 2025 notification."*
- 3 `<ul>`, 3 `<ol>`, 40 `<li>`, 3 blockquotes.

**Only real weakness: zero tables.** An article whose subject is "the list expanded from 5 items to 16" is asking for a table, and table-format extraction is a distinct citation path you're forfeiting.

### Homepage — near-zero (6/25)

462 words total. Eleven paragraphs, of which the **longest piece of substantive prose is the legal disclaimer (50 words)**. Card blurbs run 10–13 words. There is no definitional passage, no statistic with a source, and nothing remotely near the 134–167 word band.

The homepage is currently uncitable by construction. That is defensible for a hub page — but it means every AI citation the domain earns has to come from an article, and the homepage contributes nothing to entity understanding.

---

## 7. Server-Side Rendering Check

**AI crawlers do not execute JavaScript.** Verified by diffing raw HTML against Playwright-rendered HTML.

| URL | Raw HTML | After JS | Verdict |
|---|---|---|---|
| `/` | Full content, `is_spa=False` | same | ✅ PASS |
| `/article/*` | Full content, 1,819 words | same | ✅ PASS |
| `/compare` | **0 tables** | **1 table, 10 rows** | ❌ FAIL → **fixed**, see §0 |
| `/` stat counters | `0+` / `0+` / `0+` / `0%` | `50+` / `10+` / `100+` / `100%` | ❌ FAIL → **fixed**, see §0 |

Post-fix, verified against the running app: `/compare/private-limited-vs-llp` serves a 10-row `<table>` in raw HTML with no JavaScript, and `/` serves `126+ / 55+ / 11 / 100%` pre-JS.

### The `/compare` blind spot — most severe finding

`/compare` ships five comparison titles in HTML and **no comparison data**. The table is injected client-side after a dropdown selection. Every AI crawler sees five headings and nothing else:

- Private Limited Company vs LLP
- Lease Agreement vs Leave & License
- Partnership Firm vs LLP
- Consumer Forum vs Civil Court
- RTI vs PIL

These are high-intent comparison queries — precisely the query class where AI answers dominate and where table-structured data is the preferred citation format. The content exists, is well-chosen, and is 100% invisible to GPTBot, ClaudeBot, PerplexityBot and Google's AI extraction. There are also no `/compare/*` deep-link URLs, so there is no per-comparison page to cite even if the data were rendered.

### Stat counters

`data-target` attributes animate from zero. Google executes JS and will resolve them; AI crawlers will not. They currently read: *"0+ Compliance Topics Covered, 0+ Document Templates, 0+ Rights & Procedures Explained, 0% Free, Forever."*

Worse, the true values understate reality — the sitemap carries **128 articles** and the library holds **55 templates** against claims of "50+" and "10+".

---

## 8. Top 5 Highest-Impact Changes

**1. Server-render `/compare`, and give each comparison its own URL.**
Emit the comparison table in HTML on page load; add `/compare/pvt-ltd-vs-llp` etc. Five high-intent comparisons go from invisible to citable, in the table format AI surfaces extract most readily. Highest impact-to-effort ratio on the site.

**2. Make `dateModified` mean something.**
Every sampled article has `dateModified` identical to `datePublished`, in **batch timestamps** — `2026-06-27T15:26:32` appears on `companies-act-2013-guide`, `dpdp-act-compliance-guide` and `fundamental-rights` alike; `2026-07-24T18:42:33` on two more. These are migration timestamps, not editorial dates. Two consequences: content under 3 months old is ~3× more likely to be cited and pages stale 6+ months lose eligibility, so the field needs to move on real edits — and Google's helpful-content guidance explicitly names *faking publication-date freshness* as a warning sign. Set `dateModified` on actual edit, and run a quarterly refresh pass on the top 20 articles.

**3. ~~Add `sameAs` to the `Person` schema.~~ — withdrawn, owner declined (see §5).**
The author page is intentionally name + B.Com only. The one piece of this item still worth doing is at the *organisation* level, which carries no personal detail: fix the Organization `sameAs`, where `linkedin.com/in/lawminded/` uses the `/in/` personal-profile format and should be a `/company/` URL.

Replacement third priority — **strengthen the brand entity instead of the personal one.** A Wikidata item for Law Minded (the publication, not the person), consistent `Organization` `sameAs` across X/Instagram/LinkedIn, and the brand named consistently in article copy. This buys entity resolution at the publisher level, which is where a masthead-style site should hold its authority anyway.

**4. Add comparison tables to articles.**
Four of five sampled articles have zero tables. Start where the content is already tabular: the UPSI 5→16 expansion, DPDP compliance deadlines, entity-type comparisons. Table snippets are a citation path currently closed to you.

**5. Build authentic YouTube and Reddit presence.**
YouTube mentions carry the strongest known correlation with AI citations (~0.737); Perplexity draws 46.7% of citations from Reddit. Both are currently zero.

> **Do this the legitimate way.** Google's guide explicitly rejects *"chasing inauthentic mentions across blogs, forums, videos"* as a tactic. The play is real participation — answering compliance questions in r/IndiaInvestments, r/legaladviceindia, r/india where you genuinely help, and short explainer videos of your existing articles. Mention-farming is both against Google's stated position and detectable.

---

## 9. Schema Recommendations

**Already correct — leave alone:** `Article` with named `Person` author, `BreadcrumbList`, `FAQPage` (5 Q&As on the article, 6 on `/faq`), `ImageObject`, `Organization`, `WebSite` + `SearchAction`.

**Add:**

| Schema | Where | Why |
|---|---|---|
| `ItemList` | homepage "Latest articles" | Makes the featured set machine-readable |
| `Table` / server-rendered `<table>` | `/compare/*` | The citation format for comparison queries |
| `about` + `mentions` with Wikidata `@id`s | articles | Link statutes to Wikidata entities (e.g. Companies Act 2013, SEBI) so AI systems can resolve topics to known entities |
| `speakable` | articles | Low cost, marks the definitional block explicitly |

**Do not add:** more `FAQPage` for its own sake. Google's guide warns against over-investing in structured data specifically for AI features. Your schema coverage is already above par; the gap is content and entity signals, not markup.

---

## 10. Content Reformatting Suggestions

**Homepage — add one citable block.** Directly under the hero, a 140-word plain-prose paragraph answering "What is Law Minded?" with specifics: what it covers, how many guides, who writes it, that it is free. This is the passage AI systems will quote when asked about the brand, and right now there is nothing to quote. Include the real numbers (128 guides, 55 templates, 11 practice areas).

**Homepage — server-render the counters.** Print real values in HTML; let JS animate *from* them rather than *to* them.

**Homepage — surface the author.** An "Edited by Piyush Kundnani, B.Com — Founder & Editor" line linking to the author page. Currently the homepage carries no human signal at all.

**Articles — convert prose lists to tables** where the content is comparative or enumerable. The UPSI 5→16 expansion is the clearest candidate.

**Articles — keep doing what you're doing.** The 34.8-word average paragraph, the definitional opener, the `Checklist` / `Worked example` / `Common mistakes` section pattern, and the short factual FAQ answers are all correctly built for AI extraction. Do not restructure them.

> Note: Google explicitly rejects *"chunking content for AI"* and *"rewriting content with AI-specific phrasings"* as myths. Nothing above asks for either — these are ordinary structure and clarity improvements that happen to help extraction.

---

## 11. Limitations

- **WebSearch is US-geo.** Brand-mention absence (Reddit, YouTube, Wikipedia) is suggestive but not conclusive for an India-focused site. Verify against Indian SERPs.
- **No GSC data.** AI Overviews eligibility depends on being indexed and snippet-eligible; that could not be confirmed here. The AIO score assumes the SXO audit's indexation concern is real — check Search Console before acting on it.
- **DataForSEO MCP unavailable**, so no live ChatGPT/Perplexity citation checks. Platform scores are inferred from measurable presence/absence of the sources each platform is known to cite, not from observed citations.
- **Bing indexation and IndexNow status not audited.**
- Five articles sampled, not all 128. The `dateModified` and table findings were consistent across the sample but are not a census.
- Sampled article `/article/what-is-upsi-regulation-2-1-n` published 2026-07-24 — genuinely recent, which flatters the freshness read. Older cohorts will score worse.
