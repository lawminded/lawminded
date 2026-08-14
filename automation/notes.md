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
- When the owner asks to preview a document (resolution, deed, etc.) as a real
  file rather than pasted text, generate an actual .docx with python-docx and
  send it straight to Telegram via the Bot API's sendDocument (token/chat id
  from .env) — the `send()` helper in telegram_bot.py only does text, so this
  needs a direct API call, not the wrapper. This only applies to documents the
  owner asks for directly (resolutions, deeds) — it is not something to bring
  into blog articles or topic scheduling.
- Owner can pin the topic for a specific upcoming weekly-post run ahead of
  time without having it drafted immediately. Handled via
  `automation/next-topic.md` — see the override step added to
  `weekly-post.md` step 1. Set for Sunday 2026-08-16: HUF (Hindu Undivided
  Family).
