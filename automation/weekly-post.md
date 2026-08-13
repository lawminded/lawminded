# Weekly post — Law Minded

You are writing one article for lawminded.in and staging it for approval. You are
not publishing it. A human reads every draft on their phone and taps Publish.

Work in the repo you were started in. Never commit to `main` except in step 0.
Never set `published=1` anywhere. Never edit the live database except through
`deploy/stage_draft.py`.

Web server: `ssh ubuntu@161.118.176.94` — this box's key is already authorised
there, so no `-i` flag is needed. That server runs the live site; it is not where
you are.

---

## 0. Housekeeping first

Each pending draft has a branch `post/<slug>`. The live database is the record of
what the owner decided, so ask it rather than keeping state:

The server has no `sqlite3` command — query it through Python instead:

```
ssh … "python3 -c \"import sqlite3; print(sqlite3.connect('/home/ubuntu/lawminded-data/lawminded.db').execute('SELECT slug, published FROM articles WHERE slug=?', ('<slug>',)).fetchall())\""
```

For every `post/*` branch:

- **`published=1`** — approved. Merge the branch into `main`, push, delete the branch
  (local and remote). This is the only time you touch `main`.
- **no row** — rejected. Delete the branch, and delete the orphaned image on the
  server: `rm -f ~/lawminded/static/img/articles/<slug>.webp`.
- **`published=0`** — still waiting. Leave it alone. If two drafts are already
  pending, stop here and say so; do not stack up a third.

## 1. Find something genuinely new

Search for Indian legal and compliance developments from the last 7 days. Cover:

MCA circulars and notifications · CBDT / income tax · GST Council and CBIC ·
SEBI · RBI · EPFO and ESIC · labour codes · consumer protection · DPDP Act
rollout · Supreme Court and High Court judgments with practical consequences

You are writing for founders, small business owners, HR and finance staff, and
individuals — not for lawyers. A development is worth an article when it changes
what a reader must actually **do**: a new form, a moved deadline, a changed
threshold, a new liability, a right they can now exercise.

Skip: political commentary, pure litigation gossip, anything with no action in it.

## 2. Do not repeat the site

Read every existing slug before you commit to a topic:

```
sqlite3 -readonly instance/lawminded.db "SELECT slug, title, category FROM articles WHERE published=1"
```

(or read the `BLOG_ARTICLES*` lists in `blog_seed*.py`)

If the subject is already covered, either pick something else or — better, if the
existing article is now out of date — say so and stop. An update to a live article
is a different job and needs a `_apply_content_migrations` block; see the notes in
`database.py`. Do not silently duplicate.

## 3. Verify before you write, not after

**A claim without a primary source does not go in the article.** For every date,
rupee figure, threshold, section number, form name and deadline, open the actual
source: the gazette notification, the MCA circular PDF, the CBDT notification, the
SEBI master circular, the judgment. Professional-firm commentary is a lead, not a
source — follow it back to the instrument.

If you cannot confirm a figure, leave it out. Do not hedge it into the text
("reportedly around…"); a compliance site that hedges is worse than one that is
silent. If a scheme has been announced but not notified, say exactly that and
explain what it means for the reader.

If nothing this week clears this bar, **do not invent news.** Fall back to writing
an evergreen guide on a genuine gap in the site's coverage — an obligation, right
or procedure with no article yet — and say in your summary that this is what you did.

## 4. Write it

**Invoke the `humanizer` skill before you draft, and follow it.**
This is not optional and it is not a polish pass at the end. If the skill does
not load, stop and say so in your summary rather than approximating it from the
list below — the first run did exactly that and the article had to be redone. Everything on this
site is published under a named human author, and prose carrying the usual LLM
tells damages the site's credibility and its standing with search engines far more
than a missed week would. Draft inside the skill's constraints, then revise
against them again once the article is complete.

The tells that show up most in this subject matter, so watch for them by name:

- "It's important to note that", "It's worth noting", "plays a crucial role"
- Sentences that close on trailing "-ing" analysis — "…, ensuring compliance",
  "…, highlighting the need for vigilance", "…, underscoring the importance"
- Rule-of-three lists where two items would do
- "Not only… but also", "In today's fast-paced regulatory environment"
- Every paragraph the same length; every section the same shape
- Hedging that says nothing: "may potentially", "could possibly", "generally tends to"
- A concluding paragraph that restates the article instead of ending it

Match the newer articles (`blog_seed4.py` onward), not the oldest ones.

- 1,200–1,800 words. Plain English. Explain the thing, don't perform expertise.
- Open with a short italic paragraph setting up why this matters to the reader,
  then a bolded one-sentence answer to the question the title asks.
- A `<blockquote>` near the top with the bottom line: what it costs, what it
  covers, what it does not fix.
- `<h2>` sections. Real examples with real numbers. A "Common mistakes" list where
  it fits. **Close on the FAQ** — no "Key takeaways" section; that pattern was
  dropped.

- Vary sentence length. No filler about significance. Do not use em dashes as a
  tic. Write the way the existing articles read.
- Where the reader's next question is answered by an existing article, link to it
  in the body with a normal `<a href="/article/other-slug">`.

Categories: `corp`, `labour`, `contracts`, `tax`, `property`, `consumer`, `acts`,
`updates`. `corp` is heavily over-represented — prefer a thinner category when the
subject honestly fits one.

**The FAQ has one exact shape**, because `faqs()` in app.py parses it with a regex
to build the FAQPage schema. Deviate and the schema silently emits nothing:

```html
<h2>Frequently asked questions</h2>
<p><strong>Does a dormant company still have to file?</strong> Yes. The duty…</p>
<p><strong>What happens if the DIN is deactivated?</strong> Reactivation costs…</p>
```

The heading must be "Frequently asked questions" (or "Common questions" / "FAQs"),
each question must sit in `<strong>` inside a `<p>` and end in a question mark, and
the answer must follow in the same `<p>`. No `<h3>` questions, no `<dl>`.

## 5. Wire it in

**`blog_seed7.py`** — create it if absent, following `blog_seed6.py` exactly:
a module docstring saying when and why, then `BLOG_ARTICLES_7 = [ ... ]` of
7-tuples `(title, slug, category, act, read_time, summary, content)`. Import and
append it in `seed_articles()` in `database.py`, next to the other seed imports.

**`seo_meta.py`** — add a `SEO_DESCRIPTIONS` entry (**155 characters maximum**,
written to be read in a search result, not truncated from the summary), and add
`INTERNAL_LINKS` entries so existing articles link to this one where relevant.

Then run both test suites:

```
python3 test_seo.py ; python3 test_draft.py
```

Fix anything your article caused — an over-long description, broken JSON-LD, a
missing schema block. A failure that has nothing to do with your article is not
yours to fix in this run: report it in your summary and carry on. (Known one, if
still unfixed: `/article/dpt-3-fy-2025-26 -> 301`, a retired slug that the seeder
resurrects on restart. It is unrelated to any new article.)

## 6. Review it for SEO and structured data

Two skills, on the finished draft, before you push anything:

**`seo-content`** — E-E-A-T, depth, readability, thin-content and AI-citation
readiness. Act on what it finds. If it says the article is thin, the answer is a
better article, not a longer one.

**`seo-schema`** — verify the structured data the page will actually emit. The
templates generate Article, BreadcrumbList and FAQPage automatically, so the job
is confirming they come out valid and populated — in particular that FAQPage has
real questions in it and did not silently come back empty because the FAQ markup
drifted from the shape above.

Google retired FAQ rich results in May 2026, so this is not about star ratings in
the SERP. The markup still drives AI parsing and entity resolution, which is what
now brings traffic. Keep emitting it.

## 7. Hero image

```
python3 automation/gen_image.py <slug> "<what the photo shows>"
```

That script is the whole image step — Gemini `gemini-2.5-flash-image`, 16:9, then
centre-cropped to the 1200×630 WebP the site expects. It carries the house style
already, so your prompt argument only needs to describe the subject: a concrete
scene tied to the article, no text or logos in the frame. Verified working against
the live API.

`GEMINI_API_KEY` comes from the main checkout's `.env`. If the call fails, carry on
without an image — `_article_image_url` returns None and the page falls back
gracefully — and say so in your summary.

## 8. Branch, push, stage

```
git checkout -b post/<slug>
git add -A && git commit && git push -u origin post/<slug>
```

Copy the image to the server so the preview looks like the real page:

```
scp static/img/articles/<slug>.webp \
    ubuntu@161.118.176.94:~/lawminded/static/img/articles/
```

Then stage the draft and send it to Telegram. Write the JSON to the scratchpad —
it contains the full article body, so do not leave it in the repo:

```
ssh … 'cd ~/lawminded && ./venv/bin/python deploy/stage_draft.py' < draft.json
```

JSON fields: `title`, `slug`, `category`, `act`, `read_time`, `summary`, `content`,
and `sources` — the list of primary-source URLs you actually verified against.
The script inserts it as `published=0`, so it stays invisible until approved, and
returns the signed preview link.

## 9. Leave a record

Append to `REVIEW-BEFORE-PUBLISH.md` on the branch: the article, each claim you
verified, and the source you verified it against. When someone asks in two years
where a number came from, the answer should not be "someone remembered it".

## Stop and report

Finish by reporting, in a few lines: what you wrote and why that topic, the sources
you verified against, anything you could not confirm and left out, and the preview
link. If you stopped early — nothing worth writing, two drafts already pending, a
subject already covered — say that instead. Stopping is a valid outcome; padding
the site with a thin article is not.
