# Fact-check record — the eight articles added July/August 2026

Kept as provenance. On a compliance site the question "where did this number come
from?" gets asked eventually, and the answer should not be "someone remembered it".

Verified 7 August 2026 against live sources. Everything below checked out; where a
draft had hedged ("roughly eighteen months"), the hedge was replaced with the
confirmed date.

## blog_seed5.py — five gap articles

| Article | Claim verified | Result |
|---|---|---|
| Gig and platform workers | Labour Codes in force **21 November 2025** | Confirmed, two independent sources |
| | Aggregator levy 1–2% of turnover, capped at 5% of amounts payable to workers | Confirmed — Social Security Code s.114(4), quoted verbatim in the source |
| | Turnover excludes tax, levy and cess paid to the Centre | Confirmed, and added to the article |
| Non-compete | s.27 Indian Contract Act; restraint during employment valid, post-employment void | Settled law since 1872; no contradicting source found |
| FCRA vs FEMA | FCRA account at **SBI New Delhi Main Branch, 11 Sansad Marg** | Confirmed — notified 07.10.2020 under amended s.17. Address added |
| | Administrative expenses capped at **20%**, down from 50% | Confirmed |
| | Sub-granting prohibited, even to another FCRA-registered body | Confirmed |
| | Registration needs **3 years** existence + **Rs 15 lakh** on core activities | Confirmed. The draft had hedged both figures; they are now stated |
| DPDP Rules timeline | Notified **13 November 2025** | Confirmed |
| | Phase 1 immediate: Rules 1, 2, 17–21 | Confirmed |
| | Phase 2 **13 November 2026**: Rule 4, Consent Managers | Confirmed |
| | Phase 3 **13 May 2027**: Rules 3, 5–16, 22, 23 | Confirmed |
| POSH | IC mandatory at 10+ employees; composition; half women; 3-year term | Confirmed — s.4 |
| | Inquiry 90 days; penalty Rs 50,000, doubling on repeat | Confirmed — s.26 |

The DPDP article changed most. It previously said "roughly eighteen months from
notification" throughout because the dates could not be confirmed at the time. It
now carries the three actual commencement dates and the rule numbers for each phase.

## blog_seed6.py — three news articles

Written 7 August 2026 with sources open, so nothing needed retrospective checking.
CCFS-2026 came from MCA General Circulars 01/2026 and 03/2026; the perquisite
figures from the KPMG GMS flash alert on the Income-tax Rules, 2026.

## Deliberately not written

**FAST-DS 2026**, the foreign asset disclosure scheme. Introduced by the Finance
Bill 2026 but **commencement not notified** as at 7 August 2026, and a declaration
filed before notification is invalid. Press reports of a 15 August start are
speculation, and two sources gave irreconcilable figures for the charge payable.
Revisit once it is actually notified.

## Two dated items to diarise

- **CCFS-2026 closes 31 August 2026.** After that, rewrite the article in the past
  tense rather than deleting it — people keep searching for closed schemes.
- **DPT-3** was retired on 7 August 2026 because it led with a deadline that had
  passed. It recurs annually, so the content is unpublished rather than deleted and
  the URL redirects to the annual compliance guide. Republish with fresh dates next
  filing season.

## Still outstanding

None of the eight has a hero image, so each falls back to the logo for `og:image`
while every older article has a 1200x630 WebP. Generating them costs a few rupees
through the Gemini key in the local `.env`.

## blog_seed7.py — one news article, 13 August 2026

The site had no e-way bill article at all before this one, so nothing needed
checking against existing content beyond confirming the gap.

| Claim verified | Source | Result |
|---|---|---|
| Ship-to GSTIN mandatory for Bill-to/Ship-to e-way bills | GSTN Advisory dated **20.05.2026** (referenced and superseded by the 17.06 advisory below) | Confirmed via secondary corroboration (TaxGuru, CAclubindia, LiveLaw) — the 20 May PDF itself was not directly fetched, but its content is quoted and dated inside the 17 June advisory, which was fetched directly |
| Requirement extended to e-Invoice API, e-Way Bill by IRN API and a new EWB Closure API | **GSTN Advisory dated 17.06.2026**, "Advisory on e-Invoice API and e-Way Bill by IRN API changes for mandatory capture of Ship-to GSTIN and Voluntary Closure of eWay Bill" | Confirmed — fetched the actual PDF directly from `tutorial.gst.gov.in/downloads/news/advisory_einvoice_api_ewb_by_irn_approved.pdf` and read it page by page |
| Production implementation date **1 August 2026** | Same GSTN PDF, Section 17 | Confirmed, stated verbatim in the source |
| ShipDtls.Gstin conditionally mandatory (IRN+EWB together); Gstin field mandatory under ExpShipDtls (EWB by IRN) | Same GSTN PDF, Sections 3–4 | Confirmed, quoted field names verbatim |
| URP used where Ship-to GSTIN unavailable | Same GSTN PDF, Section 6 | Confirmed |
| Validation rules: valid GSTIN, Bill-to ≠ Ship-to, state code match, PIN code match; error codes 5001/5002/2323/2324/2325/4074/3039 | Same GSTN PDF, Sections 5, 7 | Confirmed, error codes quoted verbatim from the advisory's own tables |
| Export EWB treatment (Ship details replaceable, URP allowed) and B2B/SEZ treatment (Ship details locked at IRN stage) | Same GSTN PDF, Sections 8–9 | Confirmed |
| Voluntary EWB closure: who may close, EWB-wise/date-wise, portal + API (EWB number, closure date, remarks), no separate "Closed" status yet during the stabilisation period | Same GSTN PDF, Sections 10–15 | Confirmed |

Not used: Section 129/130 CGST Act penalty figures (detention, ₹10,000 or tax
amount, up to 200% of tax) were researched as background but left out of the
final draft — they are unrelated to this specific advisory (they predate it and
apply to e-way bill non-generation generally, not to this Ship-to GSTIN field),
and including them risked implying a penalty consequence the advisory itself
does not state.

## blog_seed7.py — compounding of offences under the Companies Act, 13 August 2026

Requested directly by the owner over Telegram ("Write a blog on compounding under
companies act"). The site had extensive Companies Act coverage (ROC adjudication,
CCFS-2026, annual compliance) but nothing on Section 441 itself, so this fills a
genuine gap rather than duplicating anything live.

An earlier run of this same request timed out after 45 minutes mid-workflow —
research and drafting were done and left in `/tmp`, but the article was never
wired in, tested, imaged or staged. This run picked up that draft, independently
re-verified every load-bearing claim against primary sources rather than trusting
the prior session's word, and completed the remaining steps.

| Claim verified | Source | Result |
|---|---|---|
| Regional Director/authorised officer ceiling raised from ₹5 lakh to ₹25 lakh; Section 441(6) rewritten so offences punishable with imprisonment only, or imprisonment and fine together, are not compoundable | Companies (Amendment) Act, 2019, Section 39, amending Section 441(1)(b) and substituting Section 441(6) | Confirmed — fetched the Gazette PDF directly (`cdnbbsr.s3waas.gov.in`, NIC-hosted mirror; `mca.gov.in` itself returned HTTP 403 to every fetch tried from this box) and quoted the amending language verbatim |
| Non-compliance with a compounding authority's filing order now doubles the maximum fine for the compounded offence, replacing the original 2013 text's six-months-imprisonment-or-₹1-lakh-fine consequence | Companies (Amendment) Act, 2020, Section 61, substituting Section 441(5) | Confirmed — fetched the Gazette PDF directly (`prsindia.org` mirror of the official Act) and quoted "shall be twice the amount provided in the corresponding section" verbatim. The original 2013 wording was separately confirmed against a bare-act reproduction (ca2013.com) |
| Form GNL-1 is the application form, filed with the Registrar of Companies under rule 12(2) | Companies (Registration Offices and Fees) Rules, 2014, G.S.R. 268(E) dated 31.03.2014 | Confirmed — fetched the Gazette PDF directly (`thc.nic.in`, a Telangana High Court mirror of the central rules) and located the actual GNL-1 form text |
| Seven-day intimation to the Registrar after compounding; three-year bar on compounding a similar offence again; no prosecution if compounded before institution, discharge if compounded after | Section 441(2)–(3) of the Companies Act, 2013 (unamended by the 2019/2020 Acts) | Confirmed by cross-checking two independent bare-act reproductions (ca2013.com, aubsp.com) against each other, after `indiacode.nic.in` and `mca.gov.in` both returned HTTP 403 to direct fetch. Both reproductions agree on substance and neither is a professional-firm commentary layer — they reproduce the statute text itself |
| Filing defaults such as late annual returns/financial statements were moved out of Section 441 into civil adjudication under Section 454 by the 2018–2020 amendments | General background, consistent with the existing `annual-compliance-companies` and CCFS-2026 articles already on the site | Not re-verified against the Section 454 Gazette text directly in this run — stated at a level of generality (a "large slice… reclassified") that does not depend on a specific figure or date |

Not used: no rupee example of an actual compounding fee was included, since the
amount is fixed case-by-case by the Regional Director or NCLT and no schedule
sets a standard figure — inventing a representative number would have been the
kind of unsourced claim this site doesn't run.
