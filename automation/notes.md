# Notes from the owner

Standing preferences and corrections. Read before writing; append when told something worth remembering.

## 2026-08-14

- Keep the language easier for general readers, not just lawyers. The MSME
  Amendment Bill draft came back "in a little tough English" — too much
  legal-clause-stacking and jargon (e.g. "adjudicating officer" used without
  a plain explanation, dense single sentences carrying two or three clauses).
  Stay professional, but write shorter sentences and explain terms in plain
  words the first time they appear. Facts, figures, section numbers and dates
  stay exactly as verified either way — only the phrasing gets simpler.

## 2026-08-26

- The plain-English note of 2026-08-14 was given again, on the corporate veil
  case study: "some complex law terms and language is in law format like a
  laymen would not be able to understand or absorb it". Twice now, which means
  it is not being applied at drafting time — it is being applied after the
  owner complains. Write the first draft in short sentences with every legal
  term explained on first use. A useful check before staging: average sentence
  length under about 17 words, nothing over 40 words unless it is a verbatim
  quote from a statute or judgment.

- Do not put personal guarantees next to veil-lifting in the same article. The
  owner asked for the guarantee point to be cut from the case study because it
  was "causing confusion". A guarantee is protection the director signs away
  by contract; veil-lifting is protection the law takes back. Sitting side by
  side they read as two versions of the same thing. Keep them in separate
  articles.

- Any article built on an invented story ends with a fiction disclaimer, in the
  first draft, not after the owner asks. The wording the owner wanted on the
  corporate veil case study: the story is fiction, the company and the people
  in it are invented, and any resemblance to a real company or to any person
  living or dead is purely coincidental. Say in the same breath that the law
  around the story is real and was checked against the bare Act or the
  judgment. Put it after the FAQ — a trailing <p> does not disturb the FAQPage
  regex in app.py, which only reads <p><strong>question?</strong> answer</p>.
  Invented names matter here: "Meridian Weaves" or "Mehta Fabrics" are ordinary
  enough that a real business could be carrying one.

## 2026-08-28

- "Detailed" and "for laymen" are one instruction, not two competing ones. The
  SEBI request came in as "make a detailed brief blog for laymen remember its
  for laymen but make it full detailed". Plain English is not a licence to
  write short. Cover the subject fully, in short sentences, with every term
  explained on first use. Where the two pull against each other, add sections
  rather than compress sentences: the SEBI guide ran 2,672 words against the
  1,200-1,800 house band, deliberately, and stayed at a 15.7-word average
  sentence. The word band in automation/weekly-post.md is a default for the
  weekly run, not a cap on what the owner asks for by name.

- The owner asked for "a hot tag line super seo" on the Subhash Chandra NCLT
  request. Read as a headline preference: lead the title with the concrete
  number or the named thing a person would actually type into Google, not with
  a category label. The headline that went out was "Subhash Chandra's Rs 22,006
  Crore, Settled for Rs 6.5 Crore: What the NCLT Order Actually Says". Where an
  editorial headline like that runs past Google's display width, add a shorter
  SEO_TITLES entry in seo_meta.py rather than blunting the headline on the page.
