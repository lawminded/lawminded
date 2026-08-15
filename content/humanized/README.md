# Rewritten article bodies

One file per article, named `<slug>.html`, holding the full `content` field.
Migration 7 in `database.py` reads this directory and replaces the body of any
article whose slug matches. **This is what the site serves** — the prose in
`blog_seed*.py` is the older, pre-humanizer text, kept only because migrations
1a, 4b and 4c do exact-string surgery on it.

## Why the rewrite happened

Everything here was written before the `humanizer` skill was wired into the
weekly writer, and it showed: a fixed Introduction / What You'll Learn / Why It
Matters / Conclusion / Disclaimer scaffold on the oldest articles, "Key
takeaways" closers, Title Case headings, bold scattered decoratively, and
paragraphs that all ran the same length. The site publishes under a named human
author, so that costs credibility with readers and with search engines.

## The rules the rewrite followed

Prose only. Titles, slugs, categories, summaries, read times and **dates** are
untouched — migration 7 deliberately does not call `_touch()`.

Every figure, section number, date, form name and case citation was carried
across verbatim. Nothing was added that the original did not assert: no invented
examples with invented numbers. Where the original was wrong on the law, that is
a separate migration, not a rewrite.

Two sections were dropped everywhere they appeared:

- **`<h2>Disclaimer</h2>`** — `base.html` already renders a site-wide legal
  disclaimer on every page. Substantive content inside these blocks (helplines,
  One-Stop Centres, legal aid routes) was moved into the body instead of lost.
- **`<h2>Related Articles</h2>`** — plain italic titles that were never links.
  Genuine cross-references are now inline `<a href="/article/...">` in the prose,
  which is what the internal-linking work in `seo_meta.py` expects.

## House style

Match `eway-bill-ship-to-gstin-mandatory-2026.html` and the newer seeds, not the
oldest ones:

1. Opening `<p><em>…</em></p>` — a concrete situation the reader recognises.
2. `<p><strong>…</strong></p>` — one sentence answering the question in the title.
3. `<blockquote>` with **The bottom line**: what it costs, what it covers, what
   it does not fix.
4. Sentence-case `<h2>` sections. Prose by default; a list only where the content
   is genuinely enumerable.
5. A **Common mistakes** list where it fits.
6. **Close on the FAQ.** No Key takeaways, no Conclusion.

The FAQ has one exact shape, because `faqs()` in `app.py` parses it with a regex
to build the FAQPage schema — deviate and the schema silently emits nothing:

```html
<h2>Frequently asked questions</h2>
<p><strong>Does a dormant company still have to file?</strong> Yes. The duty…</p>
```

## Checking a rewrite

Two tools, both runnable from a clean checkout with no setup:

```
python3 factcheck_rewrite.py <slug>   # fact drift vs the pre-rewrite body
python3 test_humanized.py             # structural rules on every file here
```

`factcheck_rewrite.py` reconstructs the "before" text itself — it rebuilds a
throwaway database from the seeders and migrations 1-6 with migration 7
neutralised — then diffs every figure, section number, form name and date. Read
every flag: singular/plural citation forms and years from deleted "Related
Articles" lists are harmless, but a dropped rule number or an invented rupee
figure is not. It has caught both.

Two flag shapes recur and are benign once you have checked them. The first is a
citation the original wrote in shorthand — "(Reg 7(2))", "an 11B direction",
"194I" bare — which reads as a NEW FACT once it is written out in full, because
the differ only recognises a provision when the word Section, Rule or Regulation
precedes it. Spell them out; the flag is the differ noticing an improvement. The
second is a figure the original only ever wrote inside a dropped section, so it
disappears with that section: check it is the same figure you carry elsewhere in
another form, and if it is, put it back in the form people search for.

One quirk of the fact regex is worth knowing before it wastes an hour. On a
rupee figure with no unit, `[\d,]*` eats the trailing comma and then matches the
"cr" of the next word, so "about ₹18,000, credited within 45 days" invents a
token. Reword rather than chasing it.

## The state of the pass

Complete. Every slug in `PUBLISH_SCHEDULE` has a file here, plus
`dpt-3-return-filing`, which reaches the database through
`article_rewrites.DPT3_SLUG` rather than the schedule.

`ls content/humanized/` stays the progress record if the set ever grows: a slug
in `PUBLISH_SCHEDULE` with no file here has not been rewritten, except the two
humanizer-era articles named above and the four unpublished slugs that only 301.
