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

## blog_seed8.py — one news article, 14 August 2026

The site already had `msme-udyam-registration-guide` (registration process, the
current 45-day/3x-bank-rate delayed-payment rule) and `msme-1-half-yearly-return`
(the existing half-yearly disclosure return). Neither is amended by this Bill, so
this is a new forward-looking article rather than an update to either.

Two rounds of secondary-source fetching (Lexology, LiveLaw's public summary,
StudyIQ, an initial automated PDF summary) produced conflicting penalty figures
and invented classification thresholds that are not in the bill at all — those
numbers belong to the existing 2020 classification notification, which this bill
does not touch. The article was checked clause-by-clause against the primary
document instead of any secondary summary.

| Claim verified | Source | Result |
|---|---|---|
| Bill No. LXXII of 2026, introduced Rajya Sabha 28 July 2026 by Jitan Ram Manjhi | Primary bill PDF, `prsindia.org/files/bills_acts/bills_parliament/2026/MSME_Bill_2026.pdf` | Confirmed — fetched and read the full 16-page PDF directly, page by page |
| Passed Rajya Sabha 3 August 2026, Lok Sabha 7 August 2026 | PIB India's own tweet (`x.com/PIB_India/status/2085961326841762167`), corroborated by PRS India's bill tracker | Confirmed by two independent primary/near-primary sources |
| Not yet in force: needs Presidential assent + Gazette commencement notification; different provisions may be notified on different dates | Bill clause 1(2), read directly from the PDF | Confirmed verbatim from the bill's own commencement clause. No assent or notification found as of 14 August 2026 — checked PIB, PRS, and general search; stated as unconfirmed/pending throughout the article rather than reported as already in force |
| New Section 19: 50% minimum payout to supplier if a buyer's set-aside application is pending over 6 months, out of the existing 75% deposit | Bill clause 10 (substituted s.19(2) and proviso) | Confirmed, quoted near-verbatim from the bill text. The existing 75% deposit rule itself is unchanged — verified against the bill's own Annexure reproducing the current s.19 |
| New s.18(3A): mediation must complete within 90 days of first appearance, overriding the general Mediation Act, 2023 timeline | Bill clause 8(b)–(c) | Confirmed |
| New s.18(4A): arbitral award within 90 days of completion of pleadings | Bill clause 8(d) | Confirmed |
| Comparison figure: ordinary commercial arbitration gets 12 months from completion of pleadings, extendable by 6 | Arbitration and Conciliation Act, 1996, s.29A (background, not itself part of the Bill) | Confirmed via secondary corroboration (IBC Laws, Lexology) — well-settled, widely cited provision; not independently fetched from the bare Act text this session |
| New s.15A: CPSEs must route MSME invoice settlement through an RBI-authorised TReDS platform; extendable to other notified bodies; states may opt their own PSEs in | Bill clause 7 | Confirmed |
| Section 8 substituted: Udyam filing becomes free and voluntary for every MSME category, dropping the existing mandatory 180-day window for medium manufacturing enterprises | Bill clause 5, cross-checked against the Annexure's reproduction of the current s.8 | Confirmed — the current mandatory carve-out for medium manufacturing enterprises is visible in the Annexure and absent from the substituted section |
| New s.27/27A penalty structure: warning first, then Rs 1,000–50,000 (registration false info) or Rs 10,000–50,000 then Rs 50,000–1 lakh (buyer non-disclosure), rising 10% every 3 years; Development Commissioner as adjudicating officer; 30-day appeal to the Secretary, decided within 60 | Bill clause 14, cross-checked against the Annexure's current s.27 (straight conviction-based fines: up to Rs 1,000 first conviction / Rs 1,000–10,000 second; flat Rs 10,000 minimum for buyers) | Confirmed both the new figures and the old ones being replaced |
| Classification thresholds (micro Rs 1cr/5cr, small Rs 10cr/50cr, medium Rs 50cr/250cr) are unchanged by this Bill; only the mechanism for setting future thresholds moves to a general notification power, with a savings clause preserving the existing one | Bill clauses 4 and 17 | Confirmed — this directly corrects the invented "new thresholds" claim that appeared in early secondary write-ups and in the first automated PDF summary this session produced |

Not used: several outlets' claim that the Bill "makes Udyam registration
mandatory" was checked against the primary text and found to be the opposite —
the substituted Section 8 removes the one existing mandatory case rather than
adding one. Corrected in the article rather than repeated.
