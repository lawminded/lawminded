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

- Pick the topic from the news, then answer it from the official document. The
  owner's words, on the Subhash Chandra article: "we wanted to pick the topic
  from the hot news and hot headlines... in this case it only took from
  government website, no headline or anything was introduced, so it was not
  spicy at all to get read by the people... take headlines, numbers, names,
  each and everything from current news, but verify it from official source and
  give the verdict of official source, and not just make the blog on the
  listen-hear-and-say news."

  One instruction with two halves, both compulsory. What it corrects is not
  inaccuracy — the PMEGP and Subhash drafts were both sourced properly. It is
  that the run started from a scheme page or a gazette instead of from what
  people were reading that week, so nothing in the headline matched what anyone
  would type into a search box. A correctly sourced article nobody searches for
  is still a wasted week.

  Written into automation/weekly-post.md section 1 and 3, and into the Telegram
  preamble in automation/telegram_bot.py, so it applies to the weekly run and to
  anything asked for over Telegram.

## 2026-08-31

- When the owner reports a government announcement that cannot be found, ask
  him for the link in the same reply as the refusal. On 31 August he said MCA
  had extended CCFS-2026 to 15 September. Nothing existed on mca.gov.in,
  TaxGuru, Taxscan, CAclubindia or ICSI at 8pm IST, so the run declined to
  write it and queued it instead. That was the right call on the facts, but the
  reply stopped at "I could not verify it" and left the next move to him. He
  sent the circular, and it was real: General Circular No. 04/2026 dated
  31 August 2026. Refusing to write an unverified claim is correct and does not
  change. Ending the message without asking for the source costs an hour.

- **mca.gov.in returns HTTP 403 to every direct fetch**, from this box and from
  the web server, with any user agent. It is not down and it is not the key.
  Route MCA PDFs through the reader proxy instead:

      https://r.jina.ai/<the fully percent-encoded MCA URL>

  Encode the whole target URL, including the `%` signs inside the `mds=`
  parameter, or the proxy normalises the double encoding and MCA hands back an
  empty file. This worked on all three CCFS circulars and is how the article of
  31 August was sourced. Same trick reaches icsi.edu representations. A
  `share.google/...` link resolves by fetching it and reading the redirect
  chain: it goes to google.com first, then to the real mca.gov.in document.
