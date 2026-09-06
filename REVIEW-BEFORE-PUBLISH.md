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

Hero image, added 26 August 2026 on the owner's ask, after the article had already
been published. Gemini is still returning HTTP 429 ("prepayment credits are
depleted") — a billing state, not a transient error, so it will keep failing for
every article until the Google project is topped up. A Pexels key is configured
now, so the licensed-photograph fallback answered instead.

The photograph is Pexels 7382460 by Polina Tankilevitch
(https://www.pexels.com/photo/person-in-white-dress-shirt-using-smartphone-7382460/),
centre-cropped to the 1200x630 WebP the site expects. The Pexels licence permits
commercial use and modification with no attribution required, which is what makes
it safe on a monetised site; the credit above is recorded for provenance, not
because the licence demands it.

Chosen over the closer keyword matches deliberately. Pexels' "tax document" and
"application form" results are US Form 1040s and paper forms — the wrong country,
covered in readable text, and contradicting the one thing the article is about,
which is that the e-PAN route is online and paperless. This frame is hands
entering something on a phone over a laptop keyboard: the Aadhaar mobile-OTP step,
with no text, no logos, no government emblems and no faces.

## blog_seed13.py — lifting the corporate veil, case study, 26 August 2026

Requested directly by the owner over Telegram: a detailed case study with
fictional characters and setup, explaining the corporate veil as a blanket over
directors that is removed when something goes wrong, using proper company law
sections. Checked the 133 published slugs first — the site has `director-duties`,
`corporate-governance`, `din-allotment-kyc-disqualification` and
`striking-off-company-stk-2`, but nothing on the veil itself or on when the
protection stops. No duplication.

**The narrative is fiction and says so.** Meridian Weaves Private Limited, Rohan
Deshmukh, Anjali Rao, Vikram Sethi, Priya Nair, Mehta Fabrics, Northgate Retail
and Vasant Looms do not exist, and every rupee figure in the story is invented to
illustrate the provisions. The first FAQ states this outright so no reader mistakes
it for a reported case. Every section number, penalty, threshold and judgment below
is real and was read in the primary instrument, not in commentary.

Bare Acts were downloaded and converted to text locally so sections could be quoted
from the statute rather than from a summary. `mca.gov.in` and several
`indiacode.nic.in` paths returned HTTP 403 to direct fetch from this box; where that
happened the alternative source used is named in the table.

| Claim verified | Source | Result |
|---|---|---|
| Separate legal personality from the date of incorporation | Companies Act 2013, Section 9 | Confirmed — India Code bare-act PDF (`indiacode.nic.in/bitstream/123456789/2114/5/A2013-18.pdf`), quoted from the statute text |
| "The company is at law a different person altogether from the subscribers to the memorandum…" | *Salomon v A Salomon & Co Ltd* [1897] AC 22 (HL), 16 Nov 1896 | Confirmed verbatim. BAILII returned an empty body to direct fetch; the passage was taken from Trans-Lex's reproduction of the law report and matched word-for-word against a second independent reproduction before use |
| "Officer who is in default" — whole-time director, KMP, person charged with filings who knowingly fails to prevent a default, and a director who received Board papers and did not object | Companies Act 2013, Section 2(60), clauses (i)–(vii) | Confirmed — quoted from the bare Act, including clause (vi) which is the one relied on for Anjali and Vikram |
| Annual return late-filing penalty: ₹10,000 plus ₹100/day, capped ₹2 lakh (company) and ₹50,000 (officer in default) | Companies Act 2013, Section 92(5) as substituted | Confirmed from the bare Act |
| Financial statement late-filing penalty, and that it names the MD and CFO specifically | Companies Act 2013, Section 137(3) | Confirmed from the bare Act |
| Three continuous years of non-filing disqualifies every director for five years, in that company and any other | Companies Act 2013, Section 164(2)(a) | Confirmed from the bare Act |
| Office falls vacant in all companies other than the defaulting one | Companies Act 2013, proviso to Section 167(1)(a) | Confirmed from the bare Act |
| Duties of directors: good faith, due and reasonable care skill and diligence, no conflict, no undue gain; undue gain repayable to the company; fine ₹1–5 lakh | Companies Act 2013, Section 166(1)–(7) | Confirmed from the bare Act |
| Independent and non-executive (non-promoter, non-KMP) directors liable only for acts with their knowledge attributable through Board processes, with consent or connivance, or where they did not act diligently | Companies Act 2013, Section 149(12) | Confirmed from the bare Act |
| Fraudulent conduct of business: Tribunal may declare a director "personally responsible, without any limitation of liability" for the company's debts; everyone knowingly party is liable under Section 447 | Companies Act 2013, Section 339(1) and 339(3) | Confirmed — quoted verbatim from the bare Act |
| Tribunal may order repayment with interest for misapplication or misfeasance; application within five years of the winding-up order or the misapplication, whichever is longer | Companies Act 2013, Section 340(1)–(2) | Confirmed from the bare Act |
| Strike-off obtained to evade liabilities or deceive creditors: management jointly and severally liable "notwithstanding that the company has been notified as dissolved", plus Section 447 | Companies Act 2013, Section 251(1) | Confirmed — quoted verbatim from the bare Act |
| Company may apply for removal of its name; creditor may apply to restore | Companies Act 2013, Sections 248(2) and 252 | Confirmed from the bare Act |
| Fraud: definition in the Explanation, ₹10 lakh / 1% of turnover threshold, 6 months to 10 years plus fine of 1× to 3× the amount | Companies Act 2013, Section 447 | Confirmed — quoted from the bare Act including the amended threshold and the lower-value proviso |
| Wrongful withholding of company property: fine ₹1–5 lakh, court may order return, default imprisonment up to two years | Companies Act 2013, Section 452(1)–(2) | Confirmed from the bare Act |
| Auditor's duty to report fraud to the Central Government / audit committee | Companies Act 2013, Section 143(12) | Confirmed from the bare Act. **The ₹1 crore threshold was deliberately left out** — it sits in Rule 13 of the Companies (Audit and Auditors) Rules 2014, `mca.gov.in` returned 403 to every fetch attempted, and no primary text of the rule could be opened. The article describes the duty in the Act's own words ("such amount as may be prescribed") and states no figure |
| Fraudulent trading, and wrongful trading where a director knew or ought to have known there was no reasonable prospect of avoiding insolvency and did not exercise due diligence to minimise creditor loss | Insolvency and Bankruptcy Code 2016, Section 66(1)–(2) and the Explanation | Confirmed — IBBI's consolidated bare Code (updated to 12.08.2021), quoted from the statute |
| Directors of a private company jointly and severally liable for unrecoverable income tax unless they prove no gross neglect, misfeasance or breach of duty; "tax due" includes penalty, interest, fees | Income-tax Act 2025, Section 323(1)–(2) | Confirmed against the **Gazette of India** as published 22 Aug 2025 (`egazette.gov.in/WriteReadData/2025/265620.pdf`). Note: a widely mirrored secondary source shows a third sub-section carrying a private-to-public conversion exception; the enacted Gazette text has only two. The Gazette was followed. Section 323 replaces Section 179 of the 1961 Act, and the article says so |
| Same structure for GST, with the burden of proof on the director | CGST Act 2017, Section 89(1) | Confirmed — CBIC's consolidated CGST Act PDF (`cbic-gst.gov.in`), quoted from the statute |
| Cheque dishonour: up to two years, or fine up to twice the cheque amount, or both; Section 141(1) "in charge of, and was responsible to"; Section 141(2) consent, connivance or neglect | Negotiable Instruments Act 1881, Sections 138 and 141 | Confirmed — India Code bare-act PDF, quoted from the statute |
| PF: every person in charge of and responsible to the company deemed guilty; sub-section (2) reaches consent, connivance or neglect; proviso requires proof of no knowledge or all due diligence | EPF & MP Act 1952, Section 14A(1)–(2) | Confirmed — India Code bare-act PDF, quoted from the statute |
| "It is the cardinal principle of criminal jurisprudence that there is no vicarious liability unless the statute specifically provides so" | *Sunil Bharti Mittal v CBI*, Supreme Court, 9 Jan 2015 (Dattu CJ, Lokur and Sikri JJ) | Confirmed against the judgment text; case name, date and bench checked |
| Veil pierced only where the company is "a mere camouflage or sham deliberately created… for the purpose of avoiding liability", applied restrictively | *Balwant Rai Saluja v Air India Ltd*, Supreme Court, 25 Aug 2014, (2014) 9 SCC 407, at para 71 | Confirmed against the judgment text; the paragraph number cited in the article was checked, not assumed |
| Veil lifted and properties across family companies treated as one estate where the corporate form was used to defraud purchasers | *Delhi Development Authority v Skipper Construction Co (P) Ltd*, Supreme Court | Confirmed. **The article deliberately cites no SCC citation or date for this one** — the litigation ran across several judgments (1996 and 1999 among them) and the specific report carrying the veil-lifting holding could not be pinned down to one citation with confidence from the sources opened |
| Section 141(1) requires "was in charge of" and "was responsible to" read conjunctively; merely managing the affairs of the company is not enough | *Ashok Shewakramani v State of Andhra Pradesh*, Supreme Court, 3 Aug 2023 (Oka and Karol JJ) | Confirmed against the judgment text. The Supreme Court's own API (`api.sci.gov.in`) timed out repeatedly, so the judgment reproduction was used and the holding cross-checked against a second report of the same case |

Not used, and why:
- **The ₹1 crore auditor fraud-reporting threshold** — see the Section 143(12) row. No primary text, so no figure.
- **A citation for *DDA v Skipper*** — see that row. The holding is well established and is described without a citation rather than with a guessed one.
- **Section 7(7)** (Tribunal may direct that members' liability be unlimited where a company was incorporated on false information) was verified in the bare Act but left out of the article — Meridian was incorporated honestly, so forcing it in would have been a section listed for its own sake.

Length: about 4,700 words, against the 1,200–1,800 in `automation/weekly-post.md`.
That is deliberate and outside house range — the owner asked for a detailed case
study readers could go deep into. Flagged to the owner in the reply so it can be
cut back if they would rather have the usual length.

Hero image: Gemini returned HTTP 429 ("prepayment credits are depleted") — the same
billing failure recorded above for blog_seed7, so no retry. `gen_image.py` fell back
to a licensed Pexels photograph of a textile mill, which suits the subject.

### Revision, 26 August 2026 — plain English, personal guarantee removed

The owner read the draft and asked for two changes: simpler language ("a laymen
would not be able to understand or absorb it"), and the personal-guarantee thread
taken out because it was causing confusion.

Both done. **No verified claim changed.** Every section number, penalty,
threshold, date, rupee figure and judgment is exactly as it was in the table
above — only the sentences around them were rewritten. Terms that had been used
bare are now explained on first use: whole-time director, non-executive director,
key managerial personnel, jointly and severally, connivance, proviso, DIN,
vicarious liability, Adjudicating Authority. Average sentence length went from
18.8 words to 16.7, the longest sentence from 85 words to 49, and sentences over
40 words from 18 to 5 (the remainder are verbatim statutory quotes).

Removed with the guarantee: the line in the blockquote listing personal
guarantees among what the veil does not cover, Rohan's one-crore guarantee to the
bank in Act one, the paragraph distinguishing a guarantee from veil-lifting, and
the FAQ "What is the difference between lifting the veil and a personal
guarantee?". Eight FAQs are now seven; `faqs()` in app.py parses all seven, so
the FAQPage schema is still populated. Nothing in the fact-check table above
depended on the guarantee — it was a general contract point, not a sourced claim.

## blog_seed14.py — PMEGP scheme, owner-requested, 28 August 2026

Owner named this topic in `automation/queue.md` on 2026-08-17 (lost before the
queue file existed, re-queued 2026-08-22, moved to 28 August on the owner's own
ask): "PMGEP scheme — what the benefits are, who can avail them, and the special
benefits for women, SC/ST and other reserved categories."

No scheme called "PMGEP" exists. Every web search for the term returns results
for PMEGP, the Prime Minister's Employment Generation Programme, and the queue
entry's own description — a subsidy, with named benefits for women and SC/ST
applicants — matches PMEGP's actual subsidy structure exactly. Treated as a typo
for PMEGP throughout. Checked the 135 published slugs first: nothing on the site
covers PMEGP. Genuine gap, evergreen guide.

`kviconline.gov.in`, the scheme's own portal and PDF guidelines host, was
unreachable from this box on every attempt (DNS timeout, not a 403), so the
scheme's central guidelines were verified through a state government mirror
instead and cross-checked against two PIB releases.

| Claim verified | Source | Result |
|---|---|---|
| Margin money subsidy: 25% rural / 15% urban (General), 35% rural / 25% urban (Special: SC/ST/OBC/Minorities/Women/Ex-servicemen/PwD/Transgender/NER/Hill and Border areas/Aspirational Districts) | PIB Delhi, Ministry of MSME, Release ID 2079789, 2 Dec 2024, "Expansion of Micro, Small and Medium Enterprises (MSMEs)" | Confirmed — fetched directly (curl with a browser user-agent; WebFetch itself returns 403 on pib.gov.in, consistent with prior sessions' notes on gov.in domains from this box), quoted verbatim |
| Max project cost Rs 50 lakh manufacturing, Rs 20 lakh service; balance above that fundable by a bank without subsidy | Same PIB release | Confirmed |
| Second (upgradation) loan: 15% subsidy for all categories, 20% in NER/Hill states; capped Rs 1 crore manufacturing, Rs 25 lakh service | Same PIB release | Confirmed |
| No collateral security for bank loans up to Rs 10 lakh, per RBI guidelines, reemphasised by the Ministry to banks | PIB Delhi, Ministry of MSME, Release ID 2222116, 2 Feb 2026 | Confirmed — fetched directly, same method. Independent, more recent written reply than the Dec 2024 release, corroborating rather than contradicting it |
| No educational qualification needed for projects up to Rs 10 lakh manufacturing / Rs 5 lakh service | Same Feb 2026 PIB release | Confirmed, and consistent with the Dec 2024 release and the DKVIB guidelines below — unchanged across three sources of different vintages |
| Beneficiary's own contribution: 10% General / 5% Special; bank finances 90% General / 95% Special of project cost | Delhi Khadi & Village Industries Board (Government of NCT of Delhi), "Salient Features of Revised Scheme Guidelines of PMEGP," dkvib.delhi.gov.in, page last updated 21 August 2026 | Confirmed — a state government page reproducing the central scheme guidelines in full, fetched directly |
| 3-year lock-in before margin money is adjusted against the loan; if actual spending at that point falls short of the sanctioned loan amount, the shortfall in subsidy is refunded to KVIC | Same DKVIB page | Confirmed. Note: an earlier draft paragraph said the subsidy "can be clawed back" on default or early closure — not stated anywhere in the source. Corrected to state only the underspend-refund rule that is actually there |
| Working capital capped at 40% of project cost for manufacturing, 60% for service/trading | Same DKVIB page | Confirmed |
| One PMEGP application per family (self and spouse only) | Same DKVIB page | Confirmed |
| Trading/retail restrictions: standalone trading only in NER, LWE-affected districts and A&N Islands; retail selling KVIC/village-industry or PMEGP/SFURTI-cluster products, or backed by the applicant's own manufacturing/service work, permitted nationwide; all trading and retail together capped at 10% of a state's yearly PMEGP allocation | Same DKVIB page | Confirmed |
| Documents required: Aadhaar (or enrolment number, or an alternate ID such as PAN in NER/J&K where Aadhaar coverage is thin), caste certificate, special category certificate where relevant, rural area certificate, project report, education/training certificate; exemption from EDP/skill training if already trained at least 10 days offline or 60 hours online | Same DKVIB page | Confirmed |

Not used: the claim, repeated across several secondary/aggregator sites, that
Udyam or MSME registration is a precondition for a PMEGP application. Neither PIB
release nor the DKVIB guidelines list Udyam registration among the eligibility
conditions or the documents required to apply, so the FAQ states plainly that it
isn't required — an absence-based claim grounded in what the primary guidelines
actually list, not a guess.

The worked example in the "What this actually looks like" section (a woman
setting up a Rs 12 lakh unit versus a general-category applicant doing the same)
uses invented names-free, illustrative numbers to show the formula, not a
reported case — consistent with how illustrative examples are used elsewhere on
the site (LLP capital contribution, HUF guides) and not the kind of narrative
case study that needs the fiction-disclaimer treatment from `automation/notes.md`.

Sentence length checked against the owner's 2026-08-26 standing note: average
17.0 words, longest sentence 39 words, nothing over 40.

`INTERNAL_LINKS` entries added for 'pmegp', 'margin money subsidy' and 'khadi
and village industries commission', pointing here. None of the site's existing
articles currently contain those phrases, so — honestly — this doesn't yet pull
an inbound autolink from anywhere; it only takes effect for future articles that
use these terms. No existing article had a phrase that fit this topic without
forcing a mismatched link (checked "micro enterprise," "collateral-free,"
"Scheduled Caste," and "self-employment," each already anchored to a different,
unrelated meaning in its existing context), so none of those were repurposed.
Two links were added in the body instead, hand-written rather than via autolink:
to `msme-udyam-registration-guide` and `msme-1-half-yearly-return`, where the
"Common mistakes" section explains how PMEGP differs from Udyam registration.

Hero image: Gemini returned HTTP 429 ("prepayment credits are depleted"), the
same billing failure recorded for every article since blog_seed11. Fell back to
a licensed Pexels photograph (ID 38178433, by Ashutosh Kumar, a picture-framing
shop owner in Jodhpur) after checking the first search result for a different
query ("small business workshop tailoring india") and rejecting it — a tailor
photo with a distracting bare-feet close-up in the foreground, unsuitable for a
hero image regardless of licence. The framing-shop photo is dignified, on-topic
for a small-business-owner subsidy article, and free of text or logos.

---

## Subhash Chandra's Rs 22,006 Crore, Settled for Rs 6.5 Crore: What the NCLT Order Actually Says
`subhash-chandra-nclt-order-personal-guarantee` · category `acts` · staged 28 August 2026

Owner-requested by name over Telegram on 28 August 2026: "Write a proper blog
with detailed nclt order of Subhash Chandra's loan settlement. Give a hot tag
line super seo." Not a queued topic, so `automation/queue.md` is untouched.

Written from the order, not from the coverage. The 144-page order was downloaded
from the IBBI order database (row dated 25 Aug 2026, subject "Approval of
Repayment Plan in PG case") and read in full:
https://ibbi.gov.in/uploads/order/4ca65f75be889080e510bb4f21ea5d95.pdf

| Claim in the article | Source | Status |
|---|---|---|
| Cause title: IA-5505/ND/2024 and connected IAs in CP(IB)-97(ND)/2022, Indiabulls Housing Finance Ltd v. Dr Subhash Chandra, NCLT New Delhi Special Bench (Single Member), Nilesh Sharma Member (Judicial), pronounced 25.08.2026 | Order, cause title and coram, pp. 1-6 | Confirmed |
| Petition filed 2022 under s.95; RP Raj Kamal Saraogi appointed 30.05.2022; SC interim order 05.08.2022 in WP(C) 567/2022; report kept in abeyance 18.08.2022; SC vacated 22.04.2024 and petition admitted same day; Shiv Nandan Sharma replaced Saraogi 27.05.2024 | Order, opening narrative | Confirmed |
| Loan agreement dated 13.12.2016 with Vivek Infracon Pvt Ltd; Indiabulls' petition against the borrower, CP (IB)-236 of 2022, withdrawn 23.05.2023 on settlement | Order, PG's contentions VIII | Confirmed |
| Reference to a third member under s.419(5) Companies Act 2013 r/w Rule 60(2) & (3) NCLT Rules 2016, made by the NCLT President on 09.02.2026, on the split between Ashok Kumar Bhardwaj (J) and Reena Sinha Puri (T) | Order, first paragraph under ORDER | Confirmed |
| Admitted claims ~Rs 22,006.57 crore; plan value Rs 6.50 crore; Rs 25 lakh IRP cost; Rs 6.25 crore to creditors | Order, LICHFL submissions and the answer to Issue II(f) | Confirmed |
| PG's assets as on 31.07.2024: Rs 31,79,49,981, including jewellery Rs 9,81,329 and Rs 9,85,033 in Subhash Chandra & Sons; less the Rs 25 crore Jolly Maker I flat | Order, answer to Issue II(f), citing pp. 58-62 of the plan | Confirmed |
| Jolly Maker I, Cuffe Parade flat plus two garages mortgaged to STCI Finance against ~Rs 250 crore lent March 2018 to Essel Corporate Resources and Jayneer Infrapower; STCI did not vote, so s.110 leaves its security intact and the flat sits outside the plan | Order, STCI's IA-274/2025 and the answer to Issue II(f) | Confirmed |
| Voting closed 12:01 pm 01.11.2024 at 80.814%; World Crest 28.49%, Lemonade 16.85%, Catalyst (CINDA FPI) 11.85%, Corpcall 10.30%; LIC HF 6.09%, IDBI Trusteeship (Franklin Templeton) 3.36%, HDFC 3.17%, Axis 2.86%, Canara 1.60%, Union Bank (UK) 0.76%, RBL 0.55% against; IndusInd 1.11% did not vote; banks' combined share put at 19.186% | Order, voting table reproduced from para 4.6 of Canara Bank's IA-6125/2024 | Confirmed |
| LIC Housing Finance: admitted claim Rs 1,322.39 crore, plan payout Rs 38,09,294, ~0.028% | Order, LICHFL's post-hearing written submissions | Confirmed |
| Net worth certificates: RBL 2017 USD 7.17 bn (~Rs 45,888 crore), Canara 2018 Rs 40,562 crore, against Rs 31.79 crore declared | Order, objectors' case and Issue II(c) | Confirmed |
| Associate test: s.79(2)(g) needs >50% of share capital or control of board appointments; family/business/commercial proximity insufficient; entities not shown to be associates, so no s.109(4)(b) violation | Order, answers to Member (J) Q11 and Member (T) Q1(b); s.79(2)(g) checked against the bare Act | Confirmed |
| RP lapses established: admitting claims filed through Mr Anil Kumar (960 individuals) and Mr Sunil Jain (300 individuals) without supporting material, and breach of the s.106(4)(a) / s.107(1) timelines (six days' notice given; creditors had resolved to cut it to five) | Order, paras 89-90 and 97-100 | Confirmed |
| Approval expressly made subject to excluding those two sets of claims and redistributing their share | Order, para 113 and operative clauses (a) and (b) | Confirmed |
| Approval does not immunise fraud; approval and discharge orders can be recalled if concealed assets surface, an order obtained by fraud being a nullity | Order, paras 45, 50 and 51 | Confirmed |
| s.115 binds assenting and dissenting creditors alike; the tribunal cannot apply it selectively | Order, answers to Member (J) Q4-Q8, and operative clause (c) | Confirmed |
| The order is a third member's opinion; the matter goes back to the original division bench to pass orders on the majority view | Order, operative clause (d) | Confirmed |
| s.60(2), 79(2)(g), 79(14), 95(4)(b), 96, 100, 101, 105, 106(4)(a), 107(1), 109(4)(b), 110, 111, 112, 114, 115, 119(4) as described | IBC bare Act, IBBI copy amended upto 18-03-2020: https://ibbi.gov.in/uploads/legalframwork/547c9c2af074c90ac5919fa8a5c60bd4.pdf — Part III has not been amended since | Confirmed |
| MCA notification S.O. 4126(E) dated 15.11.2019 brought ss.94-187 into force from 1 December 2019 only so far as they relate to personal guarantors to corporate debtors | Notification reproduced verbatim at para 63 of the Supreme Court judgment PDF on IBBI: https://ibbi.gov.in/uploads/order/8cff46ae7049df781ad8ce6c4694dcfd.pdf | Confirmed |
| Lalit Kumar Jain v. Union of India, decided 21 May 2021: approval of a resolution plan does not ipso facto discharge a personal guarantor; s.128 Contract Act makes the surety's liability co-extensive | Same judgment, paras 111-112, and s.128 as quoted in it | Confirmed |

Left out on purpose:

* **"Rs 170 crore loan to Vivek Infracon."** Widely reported (Bar & Bench among
  others) and not in the order. The order gives the loan agreement date, so the
  article uses that and no figure.
* **"Only ~Rs 2,574 crore was guaranteed at origination."** Reported by IANS and
  Business Today, sourced to unnamed government officials, with no instrument
  behind it. The same point is made instead from s.119(4) of the Code, which is
  verifiable.
* **The PG's own defences** (guarantee obtained by misrepresentation; released on
  a Rs 225 crore payment in June 2020; Rs 3,992 crore is the real claim figure).
  These are pleadings and public statements, not findings, and the third member
  did not decide them.
* **The Rs 1,494 crore "already repaid by principal borrowers"** figure in the
  coverage. In the order it appears as a *proposal by the PG to facilitate*
  payment through entities he says are unrelated to him, and it appears there as
  something the Technical Member objected to. Reporting it as money recovered
  would invert its meaning.

Deliberately not covered: veil-lifting, per the owner's standing note of
2026-08-26 that personal guarantees and veil-lifting must not sit side by side.
Nothing in the body mentions it and no in-body link points at the case study.
(The related-articles module on the rendered page is category-driven and outside
this article's control.)

Sentence length against the owner's 2026-08-26 and 2026-08-28 standing notes:
3,542 words, average sentence 14.1 words, Flesch reading ease 63.3, grade 7.9.
The three sentences over 35 words are comma-separated lists of vote shares and a
near-verbatim rendering of s.79(2)(g), not stacked clauses. Length is over the
1,200-1,800 house band on purpose: the owner asked for "a proper blog" and
"detailed", and the 2026-08-28 note says the band is a default for the weekly
run, not a cap on what the owner asks for by name.

`INTERNAL_LINKS` entries added for 'personal guarantee' and 'personal
guarantees', pointing here. Verified these actually pull inbound autolinks from
`director-duties`, `indemnity-vs-guarantee` and `vendor-supplier-agreement`.
Four links hand-placed in the body: `indemnity-vs-guarantee`, `director-duties`,
`companies-act-2013-guide` and `common-contract-mistakes`. A fifth fires
automatically on "demand notice" to `how-to-send-legal-notice`, which is apt. An
earlier draft accidentally triggered `notice-period-termination-settlement` (an
employment article) on the phrase "notice period"; reworded to "that
requirement" so the stray link no longer fires.

Schema checked on the rendered page: Organization/WebSite graph, Article,
BreadcrumbList (Home / Knowledge Hub / Legal Acts Explained / title) and FAQPage
with all nine questions populated.

Hero image: Gemini returned HTTP 429 ("prepayment credits are depleted"), the
same billing failure recorded since blog_seed11. Fell back to a licensed Pexels
photograph. The first fallback result was rejected outright — a sheet of paper
rubber-stamped "INNOCENT" beside a gavel, which on an article about a named
living person's civil insolvency would imply a criminal acquittal that has not
happened, quite apart from the house rule against text in the frame. Re-ran with
"accountant desk paperwork ledger" and took the replacement: hands working
through stamped financial documents with a calculator, no legible or misleading
text, on-topic for a piece about claims and figures.

`python3 test_seo.py` and `python3 test_draft.py` both pass. Note for the next
run: `test_seo.py` fails on a local checkout whose `instance/lawminded.db` still
holds the pending SEBI draft, because that article's `seo_meta.py` entry lives on
`post/what-is-sebi-plain-english-guide` and not on main. Deleting the local DB so
it reseeds from main clears it. Nothing to do with this article.

### Retitled the same evening, on the owner's ask

The owner asked for the trending framing to lead: "99.97 point something haircut
… three paise for every hundred rupees, whatever the headlines are going on".
Checked what the coverage is actually running before rewriting the headline —
Free Press Journal ("Creditors Face 99.97% Haircut On ₹22,006 Crore Claims"),
NewsDrum ("Why are lenders getting just 3 paise per Rs 100"), Business Standard,
and Business Today's counter-piece of 27 Aug ("Why ₹22,006 crore claims do not
mean a 99.97% bank haircut, govt explains"). Both phrases are live query terms,
so both now appear in the H1, the SERP title, the description and an FAQ.

| Change | Was | Now |
|---|---|---|
| Headline | Subhash Chandra's Rs 22,006 Crore, Settled for Rs 6.5 Crore: What the NCLT Order Actually Says | Subhash Chandra's 99.97% Haircut: Why Lenders Get 3 Paise for Every Rs 100 |
| `SEO_TITLES` | Subhash Chandra NCLT Order: Rs 6.5 Crore Settlement (50) | Subhash Chandra 99.97% Haircut: 3 Paise Per Rs 100 (50) |
| `SEO_DESCRIPTIONS` | led on the two rupee figures | leads on 99.97% and 3 paise (142 chars) |
| New section | — | "Where the 99.97 per cent and the three paise come from", placed before the glossary |
| New FAQ | — | "Is it true that lenders get only 3 paise for every Rs 100?", now first of ten |
| Section heading | Why this is not a Rs 22,006 crore loss for the banks | Why a 99.97 per cent haircut is not a Rs 22,006 crore loss for the banks |

No new facts were taken from the coverage. Both headline numbers are arithmetic
on figures already verified from the order: 6.25 / 22,006.57 = 0.028 per cent,
so 2.8 paise per Rs 100, which the press rounds to three. The article says 2.8
and notes the rounding, rather than repeating the rounded figure as its own.

The one thing added from the coverage is the existence of the public row —
opposition criticism, and a government pushback that this settles one man's
guarantee rather than writing off Rs 22,000 crore of bank loans. Reported by
both Free Press Journal and Business Today on 27 Aug. Written as the fact of a
row, with no figure attributed to unnamed officials, for the same reason the
Rs 2,574 crore claim was left out above. The article immediately grounds the
government's line in s.119(4), which it can verify, instead of leaving it as an
assertion by officials.

Re-checked after the edit: 3,815 words, average sentence 14.0 words, nothing
over 40 words. Page renders with the new `<title>` (50 chars), description (142),
FAQPage schema carrying all ten questions, 13 in-body article links and no
self-link. `test_seo.py` passes.

### Humanizer pass, run afterwards

The owner asked whether the draft had been through the `humanizer` skill. Nothing
in this entry said it had, and the sections added during the retitle were written
without it, so the honest answer was no and the skill was run over the whole body.

Vocabulary was already clean — a scan for the flagged list (delve, robust,
crucial, pivotal, landscape, showcase, underscore, Additionally, Moreover, and
the rest) returned nothing, and sentence length already ranged from 1 to 39
words. Every tell that survived was structural:

* The "bottom line" box was three bolded inline headers with a colon each, which
  is one of the most recognisable shapes in model output. Rewritten as a prose
  blockquote, which is also what the PMEGP article does.
* Negative parallelism, four times. "The reason has little to do with who he is.
  It has a lot to do with…", "That line is not spin. It is what Section 119(4)
  says", "The banks did not just say the money was too little", and the four
  stacked "X is not enough" sentences in the associate test.
* Announced enumerations: "The third member's answer had three parts", "the case
  teaches five things". The content stayed; the counting went.
* Didactic asides: "This part surprises people, so it is worth being precise
  about it", "Here is why", "Read the last clauses and you will see".
* Significance filler: "This is the part that made the case notorious", "and it
  is a real one".
* "Most reports round that to three paise" and "Government sources quoted in the
  press" name nobody. The first is now the article's own claim about the
  headlines; the second is attributed to Business Today, 27 August.
* One duplication fixed while in there: LIC Housing Finance's Rs 38,09,294
  against Rs 1,322.39 crore appeared in full twice, once in the new opening
  section and again lower down. The second is now a clause on the end of the
  arithmetic rather than its own paragraph.

Kept deliberately, against the checklist: "Not three-fourths of all creditors.
Three-fourths of the value of the votes actually cast." That is the misreading
readers actually arrive with, so the correction is doing real work. Same for "He
is not the debtor's lawyer and he is not the bank's agent."

3,722 words after the pass, average sentence 14.6, longest 39. Ten FAQ pairs
still parse for the schema. `test_seo.py` passes.

### Hero image replaced with a courthouse, on the owner's ask

"Use some court image like NCLT or Supreme Court or anything." Gemini is still
returning RESOURCE_EXHAUSTED, and the Mac's `.env` has no `PEXELS_API_KEY` — the
writer box (92.4.76.145) does, so `gen_image.py` was run there and the WebP
copied back. Worth noting for next time: image work needs the writer box, not the
Mac.

Four candidates were pulled and looked at rather than taking the first hit:

* **Pexels 38958649** — sandstone colonnade, Delhi. **Used.** Indian, dignified,
  no text, no logos, no people, warm stone that sits in the site's cream/gold
  palette.
* Pexels 4267308 — rejected. The alt text calls it a government building in
  Lucknow; it is the UP-112 emergency helpline building, with a large "112" logo
  across the frame. Text in the image, and the wrong institution.
* Pexels 795602 — rejected. A domed campus-style building with a logo on the
  facade. Not a court.
* Pexels 13038593 — rejected, though it is genuinely a courthouse (neoclassical,
  European). The house style asks for Indian context and this was the one
  candidate that had it going against it.

The US Supreme Court photographs that "supreme court india" returns were not
considered. On an article about an Indian tribunal order they would be plainly
wrong, in the same category as the "INNOCENT" stamp rejected for the first
version of this image.

`SEARCH_META_CHANGED` deliberately **not** bumped. It is a floor for every
article's `<lastmod>` in the sitemap, and only this one unpublished slug's title
changed; moving it would claim 135 other pages were revised today.

## blog_seed16.py — ITR due date, weekly news post, 29 August 2026

`itr-due-date-31-august-2026` · category `tax` · staged 29 August 2026

Topic picked from the news, not from a scheme page: the 31 August ITR due date
for non-audit business/professional taxpayers was trending across tax-advisory
coverage all week, with the deadline two days out at the time of writing.
Checked the live DB (`SELECT slug, title, category FROM articles WHERE
published=1`, 149 rows) before committing to the topic — no article on the site
covers ITR due dates as its own subject.

| Claim in the article | Source | Status |
|---|---|---|
| 31 August 2026 due date for business/professional income where accounts are not required to be audited; full four-row table (30 Nov / 31 Oct / 31 Aug / 31 Jul) | Finance Act, 2026, Section 5, amending Explanation 2 to s.139(1) of the Income-tax Act, 1961. Read from the actual notified Gazette of India, Extraordinary, Part II Section 1, dated 31.03.2026, CG-DL-E-31032026-271439: https://egazette.gov.in/WriteReadData/2026/271439.pdf | Confirmed |
| The amendment is given effect from 1 March 2026 — before the Finance Act itself was notified — making it retrospective for this filing season rather than a future-year change | Same gazette PDF, opening line of Section 5 | Confirmed |
| Gazette text is identical to the Bill as introduced, so nothing changed during passage | Cross-checked against Finance Bill, 2026 (as introduced in Lok Sabha): https://www.indiabudget.gov.in/doc/Finance_Bill.pdf | Confirmed |
| Old (pre-amendment) Explanation 2 had three categories only, with non-audit business bundled into "any other assessee" alongside salaried taxpayers, both at 31 July | Same gazette PDF, the amendment's "for Explanation 2 ... substituted" clause names what it replaces | Confirmed |
| Revised-return window (s.139(5)) extended to the end of the relevant assessment year (31 March 2027 for AY 2026-27), from a narrower earlier window | Same gazette PDF, Section 5(b) | Confirmed |
| AY 2026-27 stays governed by the Income-tax Act, 1961, not the Income-tax Act, 2025, even though returns are filed after the new Act's 1 April 2026 commencement — this is the basis for the article's central "it's Section 139, not Section 263" correction | Income Tax Department's own page on the new Act's scope: https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act | Confirmed |
| Section 234F late fee: ₹5,000 generally, capped at ₹1,000 where total income does not exceed ₹5 lakh | Bare-text reproduction of s.234F: https://www.incometaxindia.gov.in/w/section-234f | Confirmed |
| Tax audit thresholds: ₹1 crore turnover (₹10 crore at ≥95% digital receipts/payments) for business; ₹50 lakh gross receipts (₹75 lakh at the same digital condition) for professionals | Confirmed unchanged in this Finance Act (no amendment to s.44AB in the same gazette text); cross-checked against current secondary guidance and against the figures already used in the published `income-tax-freelancers` article | Confirmed |
| 7+ crore ITRs filed for AY 2026-27 as of 27 August 2026, cited to the Income Tax Department's own statement | The Tribune, 27 August 2026, quoting the Department directly — attributed in-text rather than folded into the site's own voice; not used as a load-bearing figure | Confirmed, attributed |

Left out on purpose:

* **"Section 263 of the Income-tax Act, 2025" as the legal basis.** A large share
  of the secondary coverage cites this. It is wrong for AY 2026-27 returns —
  confirmed against the Income Tax Department's own transition guidance above —
  and the article says so directly rather than repeating the error or hedging
  around it.
* Any claim that this is a "CBDT extension." It reads that way in some coverage
  because a due-date change close to a deadline usually is administrative. This
  one is a permanent statutory amendment with retrospective effect from 1 March
  2026, not a circular, and the article states that distinction plainly.
* The ₹10,000 late-fee tier that Section 234F's text still carries ("in any
  other case"). Section 139(4)'s belated-return window closes 31 December, so
  there is no practical "later" filing this tier could apply to under current
  law; including it would have implied a filing path that doesn't exist. Left
  out rather than explained away.

**Important finding, flagged for a separate fix:** the published
`income-tax-freelancers` article (`blog_seed2.py`) currently states, in both its
FAQ and its checklist, that the ITR due date for freelancers is "31 July 2026."
That is now wrong for anyone filing under presumptive taxation (44ADA) or
otherwise not required to audit their accounts — per the amendment verified
above, they get 31 August. This is a live, indexed, published page carrying an
incorrect date two days before it matters. Not corrected in this run: per
`automation/weekly-post.md`, updating a live article needs a
`_apply_content_migrations` block in `database.py`, a deliberate, separate job,
not something to bundle into a new-article run. Surfaced here and in the run's
final report so it gets picked up.

Also fixed while in there: the site-wide `INTERNAL_LINKS` phrase `'section 139'`
(pointing at `auditor-appointment-rotation-removal`, a Companies Act guide) would
otherwise have auto-linked this article's first "Section 139(1)" mention to the
wrong Act's wrong provision, since the autolink regex matches "Section 139" as a
standalone phrase inside "Section 139(1)" (the character after "139" is `(`,
which satisfies the phrase-boundary lookahead). Added longer, more specific
phrases — `'section 139(1)'`, `'section 139(4)'`, `'section 139(5)'` — which
outrank the shorter entry under the "longer phrase wins" rule and route to this
article instead. Verified by running `autolink()` directly against the rendered
content: it now links to `income-tax-freelancers` (via "presumptive taxation"),
`tds-compliance-guide` (via "TDS") and `income-tax-act-2025-what-changed` (via
"Income-tax Act, 2025") — not to the auditor-rotation article.

1,354 words. Average sentence 16.6 words (excluding table cells and heading
line-breaks, which the naive splitter miscounts), longest genuine sentence 39
words, none over 40. `faqs()` confirmed to return all 5 FAQ pairs correctly
(verified via direct call, not just visual inspection) for the FAQPage schema.
`test_seo.py` and `test_draft.py` both pass.

Hero image: Gemini returned `RESOURCE_EXHAUSTED` (prepayment credits depleted),
so `gen_image.py` fell back to its documented Pexels path automatically. Not
manually reviewed against alternates the way the NCLT article's replacement
image was; flagged here in case the owner wants a second look before publishing.

## blog_seed17.py — SEBI bars Goenka and Chandra, weekly news post, 30 August 2026

`sebi-bars-goenka-chandra-zee-land-pledge-order` · category `sebi` · staged 30
August 2026

Topic picked from the news, not from a regulator's document list: SEBI's order
against Zee Entertainment, Punit Goenka and Subhash Chandra was the live
corporate-governance story through August 2026 — the order itself, then the SAT
appeal, then the interim relief on the warrant issue kept it in the coverage all
month. Checked the live DB (`SELECT slug, title, category FROM articles WHERE
published=1`, 150 rows) before committing: the site already has one Subhash
Chandra article (`subhash-chandra-nclt-order-personal-guarantee`), but that
covers his personal insolvency plan under the IBC — a different law, a
different tribunal, a different set of lenders. Confirmed neither "Zee",
"ZEEL", "Punit Goenka" nor "Hyderabad" appears anywhere in that article's body,
so the two do not overlap or need cross-editing.

Every figure, date and finding below is read directly from the primary source —
the actual 150-page SEBI order — not from secondary coverage.

| Claim in the article | Source | Status |
|---|---|---|
| Order dated 31 July 2026; Zee Entertainment restrained from the securities market for 2 months, Punit Goenka and Subhash Chandra for 12 months each | SEBI final order, "DIRECTIONS" section, para 438(a), p.147 | Confirmed, read directly from the PDF |
| Penalties: Zee ₹30 lakh, Goenka ₹58 lakh, Chandra ₹60 lakh — total ₹1.48 crore | Same order, penalty tables, paras 438(c), pp.148-149. Arithmetic checked by hand: 30+58+60 = 148 lakh | Confirmed |
| Of the individual penalties, ₹30 lakh (Goenka) and ₹40 lakh (Chandra) is specifically under Section 15HA (the PFUTP/fraud provision); Zee's own ₹30 lakh carries no Section 15HA line at all | Same penalty tables — checked row-by-row which penal provision (15A(b), 15HB or 15HA) each amount sits under | Confirmed. This distinction (fraud vs. disclosure-only) is not clearly made in most secondary coverage, which reports "₹1.48 crore fine" as one undifferentiated figure |
| Hyderabad land: Road No. 78, Jubilee Hills, Shaikpet village, 17,639.64 sq m, owned by ZEEL | Same order, para 3.1, p.2 | Confirmed |
| Four loans totalling ₹726 crore (₹116cr + ₹170cr + ₹230cr + ₹210cr) from IHFL to four Essel Group entities (Gnex Projects, Vivek Infracon, Gnex Infrabuild, Renu Realtech) on 13 December 2016, Essel Home as co-borrower | Same order, paras 3.1-3.2, p.2 | Confirmed. Sum checked by hand: 116+170+230+210 = 726 |
| 27 December 2018: Subhash Chandra signed the "Declaration and Acknowledgment" on ZEEL's behalf, depositing the original title deeds and creating a first-ranking mortgage | Same order, para 3.7, p.3 | Confirmed |
| No prior approval of ZEEL's audit committee, board or shareholders for the mortgage | Same order, para 3.10, p.4 | Confirmed, direct quote of the finding |
| Clause 18 of the 2018 declaration stated all requisite permissions/approvals had been obtained | Same order, para 3.9, p.3 | Confirmed, phrase quoted verbatim |
| ZEEL's April 2024 email stating management/board had no knowledge of the mortgage | Same order, para 3.11, p.4 | Confirmed |
| Deloitte Haskins & Sells' CARO report, 17 May 2019, flagging missing title deeds; Goenka's management representation letter to auditors, same date | Same order, paras 3.16-3.17, p.5 | Confirmed |
| Goenka's CEO-CFO certificates for FY 2018-19 and FY 2019-20 found false; Regulation 17(8) LODR violation | Same order, paras 412-418, pp.141-142 | Confirmed |
| IHFL's Section 9 arbitration application, Delhi HC interim protection granted 1 May 2019, not disclosed to exchanges; non-disposal undertaking; title deeds released 1 June 2020 | Same order, paras 3.14-3.15 (p.4-5) and para 407 (p.140) | Confirmed |
| Fraud finding against Goenka and Chandra under Section 12A SEBI Act and PFUTP Regulations, 2003; direct quotes on "misused his position and authority" / "at risk for his personal benefit" / "abuse of position and authority for personal benefit while risking the interest of the listed company and its shareholders" | Same order, paras 422-425, pp.143-144 | Confirmed, all three fragments quoted verbatim |
| Goenka and Chandra NOT liable under Section 27 SEBI Act for the original December 2018 non-disclosure (pre-amendment), but ARE liable under the post-amendment Section 27 for ZEEL's post-8 March 2019 failure to disclose the litigation, undertaking and deed release | Same order, paras 406-411, pp.139-141 | Confirmed. This is the finding most of the secondary coverage skipped entirely — flagged in the article's own "What the order found that most of the coverage didn't mention" section |
| SAT hearing 12 August 2026; SAT questioned SEBI's basis for ZEEL's 2-month ban | Business Standard, reported and attributed in-text, not the site's own voice | Attributed, not independently verified against a SAT order (not published on a site searched) |
| SAT's partial interim relief permitting a ~₹3,143.5 crore preferential warrant issue, conditional on ZEEL and Goenka depositing their ₹30 lakh / ₹58 lakh SEBI penalties within a week | India Legal, reported and attributed in-text | Attributed, not independently verified against a SAT order |

Left out on purpose:

* **Chandra's personal guarantee** (Deed of Personal Guarantee, 5 December
  2018, discussed at order para 421) securing the same borrowers' loans. It's
  a genuine finding in the order but tangential to this article's central
  story about board approval and disclosure; including it risked pulling the
  piece toward personal-guarantee territory the way the corporate-veil case
  study did, which `automation/notes.md` specifically flagged as confusing
  when combined with a different legal concept in one article.
* Exact figures on what portion of the SAT's warrant-issue relief has actually
  been paid or completed as of this writing — the secondary reporting gives
  the conditions SAT imposed, not confirmation the payment was made.

1,681 words. Average sentence 15.2 words (regex-based count, adjusted to treat
a quotation mark after terminal punctuation as part of the same boundary),
longest genuine sentence 48 words — the direct quote from order para 422-425,
allowed under the house rule for verbatim quotes from a judgment/order.
`faqs()` confirmed to return all 5 FAQ pairs correctly via direct call (not
just visual inspection) for the FAQPage schema; JSON round-tripped through
`json.dumps`/`json.loads` to confirm valid output. `test_seo.py` and
`test_draft.py` both pass.

Also fixed while in there: the site-wide `INTERNAL_LINKS` bare phrase
`'section 27'` (pointing at `non-compete-clause-enforceability-india`, i.e.
Section 27 of the Indian Contract Act) would otherwise have auto-linked this
article's own bare mentions of "Section 27" — meaning Section 27 of the SEBI
Act, an unrelated provision — to the wrong Act's wrong page. Same bug class as
the ITR article's Section 139 fix two weeks earlier. Fixed two ways: added a
longer, more specific `'section 27 of the sebi act'` phrase entry, and edited
the article's own text so every mention of "Section 27" is followed by "of the
SEBI Act," so the bare phrase never appears standalone. Verified by running
`autolink()` directly against the rendered content in an app context: it now
links to `sebi-lodr-explained`, `board-committees-audit-nrc-stakeholders`,
`appointment-of-kmp-section-203`, `related-party-transactions-section-188` and
`subhash-chandra-nclt-order-personal-guarantee` — not to the non-compete
article.

Hero image: Gemini again returned `RESOURCE_EXHAUSTED` (prepayment credits
still depleted as of this run), so `gen_image.py` fell back to its documented
Pexels path automatically, same as the ITR article. Confirmed the output is a
valid 1200×630 WebP.

## blog_seed18.py — CCFS-2026 extended to 15 September 2026, owner-requested, 31 August 2026

Asked for over Telegram on the evening of 31 August: the owner had heard MCA had
extended CCFS-2026 to 15 September and wanted a "last opportunity, 15 days left"
piece. The first reply that evening **declined to write it**, because no circular
could be found. `mca.gov.in` returns HTTP 403 to every fetch from this box and
from the web server, and TaxGuru, Taxscan, CAclubindia and ICSI's own site all
still showed 31 August as the closing date at around 8pm IST. The only live
development was ICSI's representation asking for an extension. The topic was
queued in `automation/queue.md` instead, conditional on a circular appearing.

The owner then sent the circular. It is real. Retrieved by following the
`share.google` wrapper to its MCA destination and reading the PDF through
`r.jina.ai`, which reaches `mca.gov.in` where direct fetches do not. Every
document below was read in full that way.

| Claim verified | Source | Result |
|---|---|---|
| CCFS-2026 extended to **15 September 2026** by **General Circular No. 04/2026 dated 31 August 2026**, F.No. Policy-02/2/2020-CL-V-MCA, signed Nupur Aishwarya, Deputy Director (Policy) | The circular PDF itself (`mca.gov.in/bin/dms/getdocument?mds=yUMlZDLGsXa%252BZT6QKuxDag%253D%253D`) | Confirmed, quoted verbatim |
| "in view of the representations received from various stakeholders" and "All other terms and conditions of the Scheme shall remain unchanged" | Same circular, paragraph 3 | Confirmed, quoted verbatim. The circular gives **no** technical or operational reason, unlike July's |
| Scheme introduced by **General Circular No. 01/2026 dated 24 February 2026**, in force 15.04.2026 to 15.07.2026, under section 460 read with section 403 | General Circular No. 01/2026, 5 pages (`mca.gov.in/bin/ebook/dms/getdocument?doc=NjM4NTY0NzE1`) | Confirmed |
| Rs 100 per day additional fee on late annual returns and financial statements since **1 July 2018**, with no upper limit | Circular 01/2026, paragraph 1 | Confirmed, stated in the circular's own words |
| 10% of additional fees; MSC-1 dormancy at one-half of normal fee; STK-2 strike-off at 25% of filing fees | Circular 01/2026, paragraphs 4 and 5(iv) | Confirmed |
| Five excluded categories (final strike-off notice issued, strike-off already applied for, dormancy applied for before the scheme, dissolved by amalgamation, vanishing companies) | Circular 01/2026, paragraph 5(iii) | Confirmed |
| Immunity: section 92 / 137 proceedings concluded and no penalty leviable only if filed before the adjudicating officer's notice, or within 30 days of it; an adjudication order already passed is unaffected | Circular 01/2026, paragraph 5(v)(a), which cites the proviso to section 454(3) | Confirmed, including the carve-out |
| **Paragraph 6:** "At the conclusion of the Scheme, the Registrars of Companies concerned shall take necessary action under the Act against the companies who have not availed this Scheme and are in default of filing these documents in a timely manner." | Circular 01/2026, paragraph 6 | Confirmed, quoted verbatim. This is the under-reported part and gets its own section |
| Previous extension to 31 August 2026 by **General Circular No. 03/2026 dated 8 July 2026**, reason given as the data centre fire of 05.06.2026 | Circular 03/2026 PDF | Confirmed |
| ICSI asked for an extension "preferably up to 30 September 2026" by letter **G&CL: MCA: AUG:08/2026 dated 28 August 2026** to MCA Secretary Dr Pallavi Jain Govil, following an earlier letter of 20.08.2026 | The ICSI letter itself, on icsi.edu (`/media/webmodules/GCL/submitted.pdf`) | Confirmed. MCA gave 15 September, half of what was asked |
| ICSI's five grounds (open income-tax/audit work, tracing old records, inactive DINs needing KYC / DSC renewal / reactivation, the August-September tax-audit and GST crunch, companies simultaneously seeking section 252 restoration before the NCLT) | Same ICSI letter, pages 1-2 | Confirmed |
| "We shall not be giving any further proposals with respect to extension for this scheme." | Same ICSI letter, closing paragraph | Confirmed, quoted verbatim |
| 15 September 2026 is a Tuesday; 1-15 September is fifteen days containing two weekends | Calendar | Confirmed |

The rupee example (six forms, ~4,500 days of aggregate delay, Rs 4,50,000 of
additional fees becoming Rs 45,000) is arithmetic on the circular's own
Rs 100/day/form figure, presented as an illustration rather than as a reported
case.

### Deliberately left out

- **Section 164(2) director disqualification.** It would have strengthened the
  "what happens on 16 September" section, but `indiacode.nic.in` returned an
  empty document and the `ca2013.com` reproduction came back visibly corrupted,
  rendering "shall be eligible" where the statute reads "shall not be eligible".
  The point stays in the existing CCFS guide, which verified it when written and
  which this article links to.
- **The 92,859 uptake figure** and the statement in Lok Sabha Unstarred Question
  No. 3496 (answered 10 August 2026) that no further extension was proposed —
  which the 31 August circular has since overtaken. Both are sourced only to
  secondary reproductions; the sansad.in PDF could not be reached.

### Migration 8: the existing guide was corrected, not duplicated

`ccfs-2026-companies-compliance-facilitation-scheme` is the evergreen guide to
how the scheme works and stays that. But its title, its summary and five places
in its body said 31 August, and two of its paragraphs argued that a further
extension was not coming. Migration 8 in `database.py` fixes the title, the
summary, the opening, the blockquote, the worked example, the FAQ, and rewrites
those two paragraphs, one of which now links forward to this article. The three
remaining "31 August 2026" strings in that body were checked individually and are
all correct history (the July circular's target date, and 04/2026's own date).

### Readability and humanizer

Drafted inside the `humanizer` skill, then revised against it. 1,821 words,
126 sentences, **average sentence length 14.5 words**. Two sentences exceed 40
words and both are verbatim quotations, one from Circular 01/2026 paragraph 6
and one from the ICSI letter. One didactic aside ("One difference from July is
worth noticing") was cut on the revision pass. The "not a fine, a meter" line is
deliberate negative parallelism: it corrects a misconception readers actually
arrive with.

`test_seo.py` and `test_draft.py` both pass. FAQPage parses to 8 questions.

### Hero image

Gemini returned HTTP 429 (prepaid credits depleted on the account behind
`GEMINI_API_KEY`), so `gen_image.py` fell back to a licensed Pexels photograph,
which is the documented fallback. Worth topping up before the next run.

### CCFS extension page, review pass 1 September 2026

Owner asked for a full AI-marks, humanizer and SEO pass on this page, published
the previous evening, with the scheme's last date now fourteen days away.

**AI marks:** none found. Scanned the stored HTML for invisible and format
characters (Cf/Co/Cs categories, zero-width space, ZWNJ, ZWJ, word joiner, BOM):
zero. No smart quotes or en/em dashes either. The `remove-ai-marks` skill's
service was not reachable from this machine, so its automated inspect/clean was
not run and nothing is claimed on its behalf beyond the character scan above.

**Humanizer:** the article already passed. The bottom-line box is prose rather
than the stacked `<strong>Label:</strong>` shape, headings are varied, average
sentence 14.4 words, no flagged vocabulary, no announced enumerations, no
didactic asides. The two sentences a naive scan flags as over 40 words are a
statutory quote running into the next heading, not real sentences. One change
made: "the part of CCFS-2026 that most summaries leave out" attributed a claim to
unnamed sources, and is now the site's own statement.

Kept deliberately: "A company that stopped filing four years ago is not facing a
fine. It is facing a meter." That is negative parallelism, and it corrects a
misconception readers genuinely hold about additional fees.

**SEO — the real finding.** The branch carrying this article and the SEBI Zee
order had never been merged, although both were published on 30 and 31 August.
Live consequences, all now fixed by merging and deploying:

* The hand-written `SEO_TITLES` and `SEO_DESCRIPTIONS` entries were not deployed,
  so Google was being served an auto-shortened title and a description **cut off
  mid-phrase** — "Everything else about the".
* The evergreen CCFS guide still told readers, in its `<title>` and its `<h1>`,
  that the scheme closed on 31 August. Migration 8 was sitting unmerged on the
  same branch. Both articles now agree on 15 September, and the guide links to
  this one.
* Neither article existed in a seed file, so a database reset would have lost
  both.

One title changed on top of that: `CCFS-2026 Extended to 15 September 2026: 15
Days Left` became `CCFS-2026 Extended: New Last Date 15 September 2026`. A
countdown in a `<title>` is wrong by the next morning and Google can keep serving
a cached copy of it; "last date" is also the query people actually type.

`SEARCH_META_CHANGED` bumped to 2026-09-01, which is what it is for — three
entries genuinely changed today.

Verified live after deploy: title and description as written, FAQPage schema
carrying all eight questions, Article/BreadcrumbList/Person/ImageObject present,
hero image serving, sitemap `lastmod` 2026-09-01, and the guide no longer saying
31 August anywhere.

---

## RTI vs PIL: One Gets You Information, the Other Gets a Court to Act
`rti-vs-pil-difference` · category `acts` · staged 4 September 2026

Owner asked for "more comparisons like pil vs rti — people are getting it on
Google, we are 1st in it", built from content the site already has.

**The premise checked out, and was stronger than stated.** From
`docs/gsc-performance-2026-08-26.xlsx`:

| Query | Impressions | Avg position | Clicks |
|---|---|---|---|
| difference between rti and pil | 15 | 4.6 | 0 |
| pil vs rti | 5 | 2.6 | 0 |
| difference between pil and rti | 1 | 4.0 | 0 |

21 impressions is the biggest single query cluster on the site — the next is
"demat requirement section 8 company" at 12 — and it already ranks on page one.
It earns **zero clicks because there was no article**. Google was ranking
`right-to-information-act-guide`, which never mentions PIL, so the snippet did
not answer the question. This is the missing page, not a new topic.

Built on the two guides the site already had, both linked rather than repeated:
`right-to-information-act-guide` (RTI, 9 mentions) and `fundamental-rights`
(the only article that mentioned PIL at all, once).

| Claim in the article | Source | Status |
|---|---|---|
| s.3 — "all citizens shall have the right to information" | RTI Act 2005 | Confirmed |
| s.6(2) — applicant "shall not be required to give any reason for requesting the information or any other personal details except those that may be necessary for contacting him" | RTI Act 2005 | Confirmed |
| s.7(1) — reply "within thirty days of the receipt of the request" | RTI Act 2005 | Confirmed |
| s.7(1) proviso — where it "concerns the life or liberty of a person, the same shall be provided within forty-eight hours" | RTI Act 2005 | Confirmed |
| s.7(5) — no fee for a person below the poverty line | RTI Act 2005 | Confirmed |
| s.8(1) — "there shall be no obligation to give any citizen" the listed categories, opening with sovereignty and integrity of India | RTI Act 2005 | Confirmed |
| s.19(1) — first appeal within thirty days to an officer senior in rank | RTI Act 2005 | Confirmed |
| s.19(3) — second appeal within ninety days to the CIC or SIC | RTI Act 2005 | Confirmed |
| s.20 — "two hundred and fifty rupees each day", total "not exceed twenty-five thousand rupees" | RTI Act 2005 | Confirmed |
| Art 32(1) — "The right to move the Supreme Court by appropriate proceedings for the enforcement of the rights conferred by this Part is guaranteed" | Constitution of India | Confirmed |
| Art 32(2) — writs "for the enforcement of any of the rights conferred by this Part", i.e. Part III only | Constitution of India | Confirmed |
| Art 226(1) — every High Court may issue writs "for the enforcement of any of the rights conferred by Part III **and for any other purpose**" | Constitution of India | Confirmed |

Sources actually read, not cited from memory:

* **RTI Act, 2005** — the Government of NCT of Delhi mirror of the central Act,
  `colart.delhi.gov.in/sites/default/files/2024-05/rti_act_2005.pdf`, 49 pages.
  `indiacode.nic.in` returned 403 to WebFetch and 404 to curl, the same gov.in
  behaviour recorded for the PMEGP article; the state mirror was fetched with a
  browser user-agent and read in full.
* **Constitution of India** — the Government of India CDN copy behind
  legislative.gov.in, `cdnbbsr.s3waas.gov.in/...20240716890312078.pdf`,
  402 pages. Note for next time: neither PDF could be read until `pypdf` was
  installed for the system python; the Read tool needs poppler, which this Mac
  does not have.

Left out on purpose:

* **The Rs 10 RTI application fee.** Set by the Central RTI Rules, not the Act,
  and it varies by state. No primary text for it was read, so the article says
  "a small prescribed fee" and names only the fee rule that is in the Act, s.7(5).
* **Any case name for the relaxation of locus standi in PIL.** S.P. Gupta and
  Hussainara Khatoon are the usual citations, but neither judgment was read in
  this session. The principle is described from what Articles 32 and 226 say,
  plus what `fundamental-rights` already states.

`SEO_TITLES` "RTI vs PIL: The Difference, and Which One You Need" (50 chars) —
both halves of the query, because the cluster splits between "rti and pil" and
"pil vs rti". `SEO_DESCRIPTIONS` 147 chars. `INTERNAL_LINKS` gained 'public
interest litigation', 'pil', 'rti application' and 'writ petition'; the bare
'rti' and 'fundamental rights' entries still point at the two deep guides, which
is right for a first-time reader, and the longer phrases win over them. Verified
the autolinks actually fire: 1 inbound from the RTI guide, 3 from
fundamental-rights.

Humanizer run over the finished draft. 1,716 words, average sentence 14.2,
nothing over 40 after two statutory enumerations were split. No bolded-label
stacks, no flagged vocabulary, no announced enumerations, no didactic asides.
Two "it is not" constructions kept deliberately: "A Public Interest Litigation
is not a separate law" corrects a belief readers genuinely arrive with, and the
Common-mistakes line about an RTI not being a channel for opinions is a
clarification rather than a manufactured reveal.

Schema on the rendered page: Article, BreadcrumbList, Person with credential,
ImageObject, and FAQPage carrying all nine questions.

Hero image: Gemini still returns RESOURCE_EXHAUSTED, so this is a licensed
Pexels photograph generated on the writer box (the only machine with
`PEXELS_API_KEY`) — hands going through a box of filed papers. On topic for
retrieving records, no text, no logos, no courtroom imagery that would imply the
article is only about litigation.

`test_seo.py` passes at 228 pages.

**Not written, and why.** The same export shows `pas 3 vs pas 4` at 6
impressions and average position 2.8 with no dedicated page — the second-best
comparison gap, and `private-placement-section-42` already carries the material.
Worth doing next. Separately, `lease-vs-leave-and-licence` ranks at positions
72-88 for "rent agreement" and "rental agreement" phrasings it never uses; that
is a vocabulary fix to a live article, which needs a content migration rather
than a new page.
## blog_seed19.py — SARFAESI on loans sold by an NBFC to a bank, weekly news post, 4 September 2026

Housekeeping first: queried the live DB for both branches sitting from the
previous run. `ccfs-2026-extended-15-september-2026` had `published=1` — already
an ancestor of `main` from an earlier session, so only the branch itself needed
deleting (local and remote, remote already gone). `what-is-sebi-plain-english-guide`
is still `published=0`, one draft pending, under the two-draft stop limit.

`automation/queue.md` had nothing pending or due, so this ran the news search
rather than the queue.

Topic: the Supreme Court's 2 September 2026 ruling in **Kotak Mahindra Bank Ltd
v Trupti Sanjay Mehta** (2026 INSC 943), covered within a day by LiveLaw,
Verdictum, KNN India, HelloBanker, LawTrend and AdvocateKhoj. Checked
`instance/lawminded.db` first — nothing on the site covers SARFAESI, debt
assignment, or NBFC-to-bank loan transfers.

| Claim | Verified against |
|---|---|
| Citation 2026 INSC 943, bench Sanjay Kumar J. and Sanjeev Sachdeva J., decided 2 Sep 2026 | LiveLaw case digest, Verdictum, AdvocateKhoj, IndianKanoon docket — all four agree |
| CFCFL notified as a "financial institution" under s.2(1)(m) only on 27.08.2018 | Verdictum, AdvocateKhoj |
| Mehtas' loan ≈ Rs 69.60 lakh, KMBL acquired the account 13.07.2012 | IndianKanoon, AdvocateKhoj |
| Poorti Rent a Car loan ≈ Rs 2.98 crore, KMBL acquired 18.07.2012 | IndianKanoon |
| Sables: KMBL acquired 09.04.2013, demand notice 13.11.2013, SLP(C) 33113/2018 dismissed | IndianKanoon |
| Bombay HC judgment set aside dated 16.07.2015 | AdvocateKhoj |
| Holding, quoted: "the provisions thereof would be available, as and when it becomes applicable to the institution holding that loan account" (Para 36) | LiveLaw, IndianKanoon, AdvocateKhoj — same paragraph number, same quote, across all three |
| Holding, quoted: "those who avail financial assistance from NBFCs not covered... enjoy greater freedom to commit default" (Para 32) | IndianKanoon, AdvocateKhoj |
| Disposition: Mehtas' appeal allowed, case restored to DRT, Rs 25 lakh deposit ordered within 8 weeks; Sables' and Poorti's SLPs dismissed, on grounds specific to each | AdvocateKhoj (full-text republication with operative order), cross-checked against Verdictum |
| SARFAESI s.2(1)(c) "bank", s.2(1)(m) "financial institution" — exact statutory text | ibclaw.in bare-act pages |
| SARFAESI s.13(2): 60-day notice after NPA classification | ibclaw.in, corroborated by Bajaj Finserv's plain-English explainer |
| SARFAESI s.13(4): possession, management takeover, or sale without a civil suit | ibclaw.in |
| SARFAESI s.17: 45 days from the s.13(4) measure to apply to the DRT | ibclaw.in |

**Could not reach:** the Supreme Court's own judgment PDF. `indiacode.nic.in`
returned 403 on direct fetch (same pattern notes.md records for `mca.gov.in`),
and the `api.sci.gov.in` PDF host also 403'd; the exact diary-number path needed
to construct the direct URL wasn't recoverable from search. Treated AdvocateKhoj
(which republishes full judgment text with paragraph numbers, not just a
digest) as the closest available primary source, cross-verified against three
independent legal-reporting outlets that agree on every fact, quote and
disposition above. Left out: the exact RBI circular number/date for the
NPA-sale framework mentioned in the judgment (KMBL v Trupti Sanjay Mehta names
RBI as a respondent over its 2005 NPA-sale guidelines) — could confirm the
guidelines exist and their general shape, not the precise circular reference,
so the article states the RBI framework's existence without citing a specific
circular number.

**The gap between the coverage and the document:** nearly every report led with
"banks can use SARFAESI on loans bought from NBFCs" as a flat, one-line result.
The document shows three separate appeals with three different outcomes — the
Mehtas' case was sent back to the DRT for a merits hearing, not simply decided
against them, with a Rs 25 lakh interim deposit condition. The article gives
this its own section ("The detail most headlines dropped").

**Humanizer pass:** first draft had the blockquote as three bolded labels
("What it settles:", "What it does not settle:", "What it does not touch:"),
which is exactly the vertical bolded-header shape the skill flags. Rewritten as
prose with one bold lead-in. Also removed four spaced em dashes used as clause
punctuation (unspaced or comma/parenthesis substituted throughout) and one
trailing "-ing" clause ("leaving nothing left to decide" → two plain sentences).
Sentence-length check: 1,746 words, 98 sentences, average 17.8 words. The two
sentences over 40 words are both verbatim court quotes (Paras 32 and 36),
consistent with the "unless it's a verbatim quote" exception.

**Wiring:** `blog_seed19.py` created (19 was the next free number; the site has
moved well past `blog_seed7.py`, so this run followed the actual sequence in
`database.py` rather than the literal filename in weekly-post.md). Category
`property` — the case turns on recovery of a mortgaged flat, and `corp` is
already over-represented. `SEO_TITLES`, `SEO_DESCRIPTIONS` (144 chars) and four
`INTERNAL_LINKS` phrases (`sarfaesi`, `sarfaesi act`, `debt recovery tribunal`,
`secured creditor`) added; none of those phrases existed elsewhere in the map,
so no ranking conflict to resolve. `test_seo.py` and `test_draft.py` both pass.

**Hero image:** Gemini returned HTTP 429 (prepayment credits depleted on the
project this run's `GEMINI_API_KEY` points at), so `gen_image.py` fell back to
a licensed Pexels photograph automatically. Image generated and copied to the
web server.
