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

## blog_seed9.py — one owner-requested article, 14 August 2026

Requested directly by the owner over Telegram (increase and reduction of LLP
capital contribution), not a news-driven pick, so this is an evergreen guide
rather than tied to a dated development. The site already had `llp-registration`
and `annual-compliance-llps` (both in `blog_seed.py`); neither touches changing
contribution after incorporation, so this fills a genuine gap.

| Claim verified | Source | Result |
|---|---|---|
| S.23(1)–(4) LLP Act 2008: LLP Agreement governs mutual rights; any change must be filed with the Registrar in prescribed form/fee | Statutory text cross-checked across ibclaw.in and advocatekhoj.com (independent databases quoting identical wording) | Confirmed |
| S.32(1)–(2): contribution can be cash, tangible/intangible property, or a service contract; monetary value must be disclosed in the accounts | Same two sources, cross-checked | Confirmed |
| S.33(2): a creditor who extended credit relying on a partner's stated contribution, without notice of a compromise, can enforce the original obligation against that partner | Same two sources, cross-checked | Confirmed |
| Form 3 filed under S.23(2)/(3) read with Rule 21(1) LLP Rules 2009, within 30 days of the change | Consistent across multiple independent professional-commentary sources citing the same rule number and period | Confirmed by consistency, not a single fetched PDF of the Rules themselves — flagged here for the record |
| Non-cash contribution valued by a practising CA, Cost Accountant, or an approved valuer, under Rule 23(2) LLP Rules 2009 | Same basis as above | Confirmed by consistency |
| LLP (Amendment) Rules, 2022 — G.S.R. 109(E) dated 11.02.2022, effective 1.04.2022 — replaced the flat additional-fee model with a multiplier of the normal fee (2x/4x rising to 25x/50x for small/other LLPs beyond 360 days) | Two independent secondary summaries (Taxguru's clause-by-clause analysis and IndiaFilings), both reproducing matching multiplier tables and the same notification number/date | Confirmed by cross-source agreement |
| Normal Form 3 filing fee banded by contribution: Rs 50 (up to Rs 1 lakh) rising to Rs 600 (above Rs 1 crore) | Two independent sources (Taxguru's Annexure A reproduction, faallp.com) with matching figures | Confirmed |
| Small LLP threshold: contribution ≤ Rs 25 lakh AND turnover ≤ Rs 40 lakh in the preceding year | Same sources, and consistent with the existing `llp-registration`/`annual-compliance-llps` articles' own stated audit threshold | Confirmed |
| IT Act S.2(23): "firm", "partner" and "partnership" are each defined to include an LLP, its partners, and LLP partnership respectively | Direct search-extracted statutory text, consistent across sources | Confirmed |
| IT Act S.45(4) (substituted by Finance Act 2021, AY 2021-22 onward): money/capital asset received by a partner from the firm "in connection with reconstitution" is taxed as the firm's own capital gain | Statutory text quoted across multiple sources referencing the Finance Act 2021 and CBDT Circular 14/2021 | Confirmed |
| S.9B: same treatment where the firm hands over a capital asset or stock-in-trade instead of money | Same basis | Confirmed |
| "Reconstitution" (Explanation 1 to S.45(4)) includes a case where every partner continues but their respective shares change, not only a partner's exit | Direct extraction of the Explanation's text from a clause-by-clause analysis (Taxguru) | Confirmed |
| CBDT Circular 14/2021 (2 July 2021) and Rules 8AA(5)/8AB prescribe how the gain under S.45(4) is computed | Multiple independent sources citing the same circular number/date and rule numbers | Confirmed |
| Companies Act 2013 S.66: a company reducing share capital needs Tribunal (NCLT) confirmation, unlike an LLP contribution change | General, settled company-law knowledge, not separately re-verified this session | Treated as background comparison, not a disputed figure |

Deliberately left unquantified: state stamp duty on a supplementary LLP deed.
Two secondary sources gave contradictory rates and caps for the same states
(e.g. Maharashtra at "1% capped Rs 15,000" in one source and "0.2% or Rs 1,500"
in another) within minutes of each other. Neither clears the site's bar, so no
figure appears in the article — it tells the reader to check their state's
current e-stamping schedule instead of repeating a number that might be wrong.

Also produced, at the owner's request and outside the blog pipeline: a
Partners' Resolution and a Supplementary LLP Deed template for a capital
contribution change, sent directly to the owner for review rather than added to
the site's Document Formats Library or Resolution Library — the DB-managed
Resolution Library deliberately retired LLP partner resolutions on 2026-07-04
(see `database.py`, `seed_documents()`), so adding one back without being asked
would reverse a prior decision.

## blog_seed10.py — one owner-requested article, 16 August 2026

Owner named the topic directly over Telegram: Hindu Undivided Family (HUF).
Not news-driven, so this is an evergreen guide. Checked the live DB's 133
published slugs first — HUF appears only inside a rate table cell in
`tds-compliance-guide` ("1% (ind/HUF)"); no article covers HUF formation,
taxation, coparcenary rights, or partition. Genuine gap.

| Claim verified | Source | Result |
|---|---|---|
| Income-tax Act, 2025, s.2(93): "person" includes an individual, a Hindu undivided family, a company, a firm, and others | Bare-text mirror of the Act, eztax.in | Confirmed |
| Income-tax Act, 2025, s.202: common rate schedule for individuals, HUF and others under the new regime; FY 2025-26 slabs (nil to 4L, then 5/10/15/20/25/30% in 4L steps to above 24L) | eztax.in bare text, cross-checked against the Income Tax Department's own AY 2026-27 HUF help page (incometax.gov.in/iec/foportal/help/individual/return-applicable), which also gave the Rs 2,50,000 old-regime exemption and confirmed HUF return forms are ITR-2/3/4 | Confirmed by two independent sources, one of them the Department's own site |
| Income-tax Act, 2025, s.156 (formerly s.87A): rebate restricted to "resident individual"; HUF excluded, both regimes | eztax.in bare text, cross-checked against incometaxindia.gov.in's own s.87A explainer and two independent professional summaries | Confirmed |
| Income-tax Act, 2025, s.92 (formerly s.56(2)(x)): gifts without consideration, Rs 50,000 threshold; Explanation defines "relative" for an HUF as any member of that HUF | eztax.in bare text | Confirmed |
| Income-tax Act, 2025, s.99(3)-(4) (formerly s.64(2)): income from an individual's property converted into HUF property without adequate consideration is taxed in the individual's own hands; carve-out for conversions on or before 31 December 1969 | eztax.in bare text | Confirmed |
| Income-tax Act, 2025, s.315 (formerly s.171): total partition — HUF assessed as undivided up to the date of partition, members jointly and severally liable for tax from before that date; partial partitions after 31 December 1978 not recognised for tax purposes at all | eztax.in bare text, cross-checked against incometaxindia.gov.in's own s.171 page for the equivalent 1961-Act wording | Confirmed |
| Hindu Succession Act, 1956, s.6, as substituted by the Hindu Succession (Amendment) Act, 2005: daughters are coparceners by birth, same rights and liabilities as sons | Statutory text, cross-checked across two independent case-law summaries | Confirmed |
| *Vineeta Sharma v Rakesh Sharma*, (2020) 9 SCC 576: daughters' coparcenary right applies regardless of whether the father was alive on 9 September 2005 | IndianKanoon judgment text and two independent case summaries (iPleaders, Drishti Judiciary) | Confirmed |
| *Sujata Sharma v Manu Gupta*, Delhi HC, CS(OS) 2011/2006 (single judge, 22 December 2015): eldest female coparcener can be karta; upheld on appeal, RFA(OS) 13/2016, division bench, 4 December 2023 | IndianKanoon judgment text, SCC Online blog coverage of the 2023 appeal decision | Confirmed, including that the 2023 appeal upheld rather than reversed the 2015 ruling |
| PAN application: Form 49A/49AA retired from 1 April 2026; HUF applications now use Form 94 (non-individual Indian entities, HUF named explicitly) filed by the karta, under Rule 158 of the Income-tax Rules, 2026 (CBDT notified 20 March 2026, in force 1 April 2026) read with s.262 of the Income-tax Act, 2025 | Three independent CA/professional summaries agreeing on the specific rule and section numbers | Corroborated by consistent secondary sourcing; no single official CBDT notification URL was fetched directly, so this is the weakest-sourced claim in the piece — flagged here for the record |

Not used: one secondary source's claim that Form 94 requires a "family tree
declaration" from the karta was not independently corroborated elsewhere, so
it was left out of the documentation list in the article rather than stated as
fact.

### Addition, same day: children, date of formation, PAN separateness

Owner asked, over Telegram, for a clarification on whether an HUF can be
formed with just husband and wife (no children), what date counts as the
HUF's "date of formation", and more detail on the HUF having its own PAN.

| Claim verified | Source | Result |
|---|---|---|
| *C. Krishna Prasad v CIT*, (1974) 97 ITR 493 (SC): "plurality of persons is an essential attribute of a family... a single person, male or female, does not constitute a family"; HUF assessment needs two or more members | Direct read of the judgment text on IndianKanoon | Confirmed |
| *Surjit Lal Chhabda v CIT*, (1975) 101 ITR 776 (SC): a joint Hindu family (not a coparcenary) can consist of husband, wife and unmarried daughter with no son; but self-acquired property isn't converted into HUF property by declaration alone where there's no pre-existing joint family property for it to blend with | Judgment text on courtkutchehry.com, cross-checked against itatonline.org's case-law digest | Confirmed. The same digest cites *CIT v Parshottamdas K Panchal* (2002) 257 ITR 96 (Guj) and *W.P.A.R Rajagopalan v CWT* (2000) 241 ITR 344 (Mad) for husband-and-wife HUFs funded by ancestral/partition property rather than self-acquired money — not independently fetched, used only as corroboration that the husband-wife point is settled beyond one case |
| "Date of formation" for the HUF deed/PAN conventionally taken as the karta's date of marriage | CAclubindia expert thread, cross-checked against HUF-deed guides (taxbuddy.com, setindiabiz.com) | Corroborated by consistent professional practice, not any CBDT form or circular — there is none, since nothing about an HUF is registered. Stated in the article as convention, not law. Weakest-sourced claim in this addition |
| HUF PAN is a separate identity from the karta's personal PAN; HUF files its own return (ITR-2/3/4) distinct from each member's personal return | Same Income Tax Department AY 2026-27 HUF help page already cited above, plus general PAN/HUF application guides | Confirmed |

## blog_seed11.py — weekly news post, 21 August 2026

News hook: SEBI circular dated 14 August 2026 lets Online Bond Platform
Providers sell Section 54EC / Section 85 capital gains bonds directly, with
new mandatory disclosures, and separately lets them offer IFSCA-regulated
products. Checked the 131 published slugs first (live DB dump, 21 Aug 2026)
and grepped blog_seed*.py for "54EC", "capital gain bonds" and "OBPP" —
nothing on the site covers the Section 54EC exemption or these bonds.
Genuine gap, and the circular changes something a reader can act on this
week: how they buy the bonds, not just whether the exemption exists.

| Claim verified | Source | Result |
|---|---|---|
| SEBI Circular HO/17/11/(2)2026-DDHS-POD1/I/18769/2026, dated 14 August 2026: OBPPs may now offer (a) bonds under Section 54EC of the Income Tax Act, 1961 or Section 85 of the Income-tax Act, 2025, and (b) IFSCA-regulated products/securities/services | Downloaded and read the full 4-page circular PDF directly from sebi.gov.in (`sebi_data/attachdocs/aug-2026/1786705729757.pdf`, linked from the circular's own listing page) | Confirmed by direct primary-source read |
| Mandatory disclosures for 54EC bonds sold via an OBPP: disclaimer that they are tax-specific instruments; grievance redressal lies with the issuer, not SEBI; features disclosure covering eligible issuers, lock-in, investment limit, non-transferability, tax features, application size, and the LODR listing exemption | Same circular PDF, clause 3.1(b)-(d) | Confirmed by direct primary-source read |
| IFSCA products offered via an OBPP must be labelled "international or overseas instruments" and comply with FEMA/LRS rules; OBPP compliance-officer rule changed from "must be a Company Secretary" to a NISM-certified compliance officer under SEBI (Stock Brokers) Regulations, 2026; circular in force with immediate effect | Same circular PDF, clauses 3.1(d) and 3.2, and paragraph 5 | Confirmed by direct primary-source read |
| Section 54EC (Income Tax Act, 1961): exemption applies only to long-term capital gains from the transfer of land or a building, or both; 6-month reinvestment window from the date of transfer; Rs 50 lakh cap on investment made in a financial year, for investment on/after 1 April 2007; lock-in raised from 3 to 5 years for bonds acquired on/after 1 April 2018 | Bare statutory text reproduced on IndianKanoon (doc/82271184 and doc/172643298) | Confirmed by direct read of the bare-act text |
| CBDT Notification No. 31/2025, dated 7 April 2025: HUDCO bonds issued on/after 1 April 2025 and redeemable after 5 years notified as a long-term specified asset under Section 54EC | TaxScan, CAclubindia and TaxManagement India, which independently quote the same notification number, date and terms | Corroborated across three independent professional sources quoting the same notification; the notification itself was not fetched directly |
| Current 54EC issuers (REC, PFC, IRFC, HUDCO as of mid-2026), coupon (5.25% p.a., paid annually), and ticket size (Rs 10,000 minimum, Rs 50 lakh per PAN per financial year) | bondscanner.com's REC and NHAI explainers, cross-checked against zfunds.in | Corroborated across two independent professional sources; no issuer's own rate notice was fetched, so the article states the coupon as "the rate on offer in mid-2026" and tells the reader to confirm the live rate rather than treating it as fixed |
| Section 85, Income-tax Act, 2025, as the renumbered successor to Section 54EC, same substantive terms | Three independent professional summaries (rrfinance.com, thefixedincome.com, mytaxexpert.co.in) agreeing the terms carried over unchanged | Corroborated by consistent secondary sourcing; the Income-tax Act, 2025 bare text for Section 85 itself was not independently fetched this session |

Hero image: `automation/gen_image.py` failed with HTTP 429 ("prepayment
credits are depleted") — a billing issue on the Gemini project, not a
transient error, so no retry was attempted. The article ships without a
hero image; `_article_image_url` returns None and the page falls back to
the site default, confirmed by rendering the page locally before staging.

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

## blog_seed12.py — Instant e-PAN: how to apply for a PAN card online for free, 25 August 2026

Requested directly by the owner over Telegram: how to apply for a free, instant
e-PAN from the income tax department's own website, and confirmation that a
physical card costs Rs 50 for delivery. Checked all published slugs and grepped
`blog_seed*.py` for "PAN card", "e-PAN" and "instant PAN" first — PAN comes up
inside the HUF, freelancer and rent-agreement articles, but no article covers how
an individual actually applies for one. Genuine gap, so this is an evergreen guide
rather than a news piece.

| Claim verified | Source | Result |
|---|---|---|
| Instant e-PAN is free, pre-login, for an individual with no PAN already allotted, valid Aadhaar linked to an active mobile number, DigiLocker access; minors, Representative Assessees (Section 160) and foreign citizens (e-KYC mode) excluded; process is Get New e-PAN → Aadhaar number → mobile OTP → DigiLocker date-of-birth proof → optional email validation → submit; Acknowledgement Number and SMS confirmation on success; status checked post-login-free via Aadhaar + OTP; only a digitally signed e-PAN PDF is issued, no physical card | incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/instant-e-pan and incometax.gov.in/iec/foportal/help/e-filing-generate-instant-e-pan-faq (Income Tax Department's own Instant e-PAN help pages) | Confirmed — fetched directly |
| Reprint of a physical PAN card costs Rs 50 (inclusive of taxes) for dispatch within India, Rs 959 outside India; requires PAN number, Aadhaar (individuals) and full date of birth; e-PAN re-download is free within 30 days of allotment/change | onlineservices.proteantech.in/paam/ReprintEPan.html (Protean, formerly NSDL, the Income Tax Department's authorised PAN service provider) | Confirmed — fetched directly |
| Cabinet approved the PAN 2.0 Project on 25 November 2024 at a cost of Rs 1,435 crore; allotment/updation/correction stays free with the e-PAN emailed to the applicant; a physical card costs "the prescribed fee of Rs 50 (domestic)" under the same project; existing PAN cardholders are not required to apply afresh | PIB Research Unit, Ministry of Finance, "PAN 2.0: A Digital Leap in Taxpayer Services," 27 November 2024 (static.pib.gov.in PDF) | Confirmed — fetched directly, and corroborates the Protean fee independently |
| Form 93 replaces Form 49A for individual Indian citizens, effective 1 April 2026, under Rule 158 of the Income-tax Rules, 2026 read with Section 262 of the Income-tax Act, 2025; paid-route fee is roughly Rs 107 domestic / ~Rs 1,017 foreign | taxguru.in, cleartax.in, businesstoday.in, lendingkart.com, bankbazaar.com, paytm.com, finpulseindia.com | Corroborated across multiple independent professional summaries that agree on form numbers, effective date and governing rule/section, consistent with the Form 94 detail already verified for the HUF article (`blog_seed10.py`). Not fetched from a single official fee schedule PDF — flagged as the weaker-sourced figure in the article, on a point secondary to the free instant e-PAN process |

Not used: Section 465 of the Income-tax Act, 2025 as the renumbered successor to
Section 272B (PAN non-compliance penalty) was checked but left out — the section
mapping was consistent across sources but the current penalty amount wasn't
confirmed clearly enough to state a figure, and it wasn't essential to a
how-to-apply article.

No hero image: Gemini returned HTTP 429 ("prepayment credits are depleted"), a
billing issue rather than a transient error, and no Pexels key is configured. The
article ships without one; `_article_image_url` returns None and the page falls
back to the site default.
