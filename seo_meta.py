"""Hand-written search-result descriptions, keyed by article slug.

An article's `summary` is on-site card copy: it can run long and often opens
with a narrative hook, which is right on the page and wrong in a search result.
Google and Bing show roughly 155 characters, so anything longer is chopped
mid-phrase — "...and the punishment under Section" — which reads as broken and
costs clicks.

Every entry here is a complete sentence under 155 characters that front-loads
what the reader searched for. A slug with no entry falls back to its summary,
clipped by the `metadesc` filter, so this file never has to be exhaustive.

Kept as a plain module rather than a database column so it deploys with an
ordinary `git push` — no migration, no script run against the production DB.
`test_seo.py` fails if any rendered description exceeds the limit.
"""

SEO_DESCRIPTIONS = {
    '50-percent-wage-rule':
        "How India's new 50% wage definition changes your basic pay, PF and gratuity. "
        "What shifts on your payslip in 2026, explained in plain English.",
    'alteration-of-moa-aoa-section-13-14':
        "Alter your MOA or AOA under Sections 13 and 14: the special resolution, MGT-14 "
        "within 30 days, and the RUN plus INC-24 name-change route.",
    'annual-compliance-companies':
        "The ROC filings every private limited company must make each year, the due "
        "dates, and what late filing actually costs you.",
    'annual-compliance-llps':
        "The annual filings your LLP cannot skip: Form 8, Form 11, the due dates, and "
        "the per-day penalty that runs with no upper cap.",
    'appointment-of-kmp-section-203':
        "Section 203 KMP rules: which companies must appoint an MD, CFO or Company "
        "Secretary, the Rs 10 crore thresholds, and the penalties in lakhs.",
    'auditor-appointment-rotation-removal':
        "First auditor in 30 days, ADT-1 in 15. The 5-year term, when rotation applies, "
        "the cooling-off period, and how removal needs ADT-2 approval.",
    'board-committees-audit-nrc-stakeholders':
        "The three statutory board committees under Sections 177 and 178: who must form "
        "each, their composition rules, and what they actually do.",
    'bonus-issue-of-shares-section-63':
        "Bonus issue under Section 63: which reserves you can capitalise, the "
        "revaluation-reserve bar, the conditions, and why it can't be withdrawn.",
    'buyback-of-shares-unlisted-section-68':
        "Buyback under Section 68 for unlisted companies: the 25% ceiling, the 2:1 "
        "debt-equity cap, SH-8, SH-9, SH-11 and the 7-day extinguishment rule.",
    'cci-merger-control-sun-pharma-ranbaxy':
        "CCI merger control: Section 5 thresholds, the Rs 2,000 crore deal value test, "
        "what counts as gun-jumping, and the Sun Pharma-Ranbaxy case.",
    'change-of-registered-office-section-12':
        "Change your registered office: INC-22 within the city, a special resolution "
        "outside it, and Regional Director approval for inter-state moves.",
    'cheque-bounce-section-138-ni-act':
        "What to do when a cheque bounces: the mandatory legal notice, the 30-day filing "
        "window, the criminal complaint, and the Section 138 punishment.",
    'chg-1-registration-of-charges':
        "Form CHG-1 registers a charge within 30 days. Miss day 120 and the charge is "
        "void forever. Timelines, fees, CHG-4 satisfaction and penalties.",
    'code-of-civil-procedure-guide':
        "How civil cases actually work under the Code of Civil Procedure, 1908: filing "
        "a suit, summons, written statement, trial, decree and appeal.",
    'common-contract-mistakes':
        "The mistakes that quietly make an Indian contract unenforceable, and how to "
        "spot them before you sign rather than when the deal is tested.",
    'company-registration':
        "Register a private limited company in India step by step: DSC, DIN, name "
        "approval, SPICe+ filing, the documents, timelines and real costs.",
    'competition-act-agreements-abuse-dominance':
        "Competition Act 2002: cartels under Section 3(3), vertical agreements, abuse of "
        "dominance under Section 4, and penalties up to 10% of turnover.",
    'conducting-a-valid-board-meeting-section-173':
        "A valid board meeting needs 7 days' notice, the right quorum, four meetings a "
        "year with no 120-day gap, and correct video-conferencing rules.",
    'conducting-agm-egm-companies-act':
        "AGM and EGM rules: the 9-month first AGM, 21 clear days' notice, quorum under "
        "Section 103, proxies, e-voting, and how an EGM is called.",
    'consumer-complaint-guide':
        "A click-by-click walkthrough of filing a consumer case on the e-Jagriti portal: "
        "registration, every screen, the documents, fees and hearings.",
    'consumer-protection-act-2019-guide':
        "Your rights under the Consumer Protection Act, 2019: what counts as a defect or "
        "unfair trade practice, and the forum that enforces them fast.",
    'conversion-private-public-company-section-18':
        "Private to public conversion needs 7 shareholders, 3 directors, MGT-14 and "
        "INC-27. Going back to private needs Regional Director approval.",
    'csr-governance-section-135':
        "CSR under Section 135: the net worth, turnover and profit thresholds, the 2% "
        "spend, CSR-1 and CSR-2, and the penalty for unspent amounts.",
    'cyber-crime-laws':
        "Cyber crime in India: the offences, how to report one, and the remedies you "
        "actually have when your money, identity or reputation is attacked.",
    'dematerialization-of-shares':
        "Why private companies must now dematerialise shares, what it means for "
        "shareholders, and the step-by-step process to convert your holdings.",
    'dir-12-appointment-resignation-directors':
        "Every director appointment, resignation or removal goes to the ROC in DIR-12 "
        "within 30 days. Late filing costs Rs 100 a day, with no cap.",
    'director-duties':
        "What a company director is legally bound to do under the Companies Act, 2013: "
        "the statutory duties and the personal liability for a breach.",
    'dividend-declaration-iepf-compliance':
        "Dividends come only from profits. Pay within 30 days, move unpaid amounts in 7, "
        "and after 7 years both dividend and shares go to the IEPF.",
    'dormant-company-section-455':
        "Park a company legally under Section 455 instead of striking it off: who "
        "qualifies for dormant status, the forms, and what it saves you.",
    'dpdp-act-compliance-guide':
        "A plain-English DPDP Act compliance guide for Indian businesses: what the law "
        "covers, what you must do, and fines of up to Rs 250 crore.",
    'dpdp-childrens-data-parental-consent':
        "The DPDP Act treats under-18 data as a special category. What verifiable "
        "parental consent means, what apps must build, and the penalties.",
    'dpdp-consent-managers':
        "How consent works under the DPDP Act: the notice you must give, the role of "
        "Consent Managers, and the November 2026 compliance deadline.",
    'drafting-maintaining-minutes-section-118':
        "Minutes must be entered within 30 days, signed correctly and never altered. Why "
        "Section 118 makes them evidence of what your board decided.",
    'electronic-signatures-india':
        "Are electronic signatures legally valid in India? What the law recognises, "
        "which documents are excluded, and how to sign so it holds up.",
    'esops-sweat-equity-shares':
        "ESOPs under Section 62(1)(b) and sweat equity under Section 54: the special "
        "resolution, one-year vesting, who is eligible, and the limits.",
    'fdi-reporting-fc-gpr-fc-trs-fla-compliance':
        "FDI reporting deadlines: FC-GPR in 30 days, FC-TRS in 60, FLA by 15 July, APR "
        "by 31 December, and the Late Submission Fee that cures a miss.",
    'fdi-routes-sectoral-caps-press-note-3':
        "FDI in India: automatic vs government route, sectoral caps, prohibited sectors, "
        "and the 2026 Press Note 3 relaxation, explained simply.",
    'fema-1999-explained-current-capital-account':
        "FEMA 1999 explained: current account transactions are free unless restricted, "
        "capital account prohibited unless permitted. Which side you're on.",
    'fema-penalties-violations-case-laws':
        "FEMA penalties: up to three times the sum involved under Section 13, Rs 5,000 a "
        "day for continuing breaches, and Section 37A asset seizure.",
    'fpo-further-public-offer-explained':
        "What an FPO is, how listed companies raise again under the ICDR Regulations, "
        "the fast-track route for seasoned issuers, and the case studies.",
    'fundamental-rights':
        "The Fundamental Rights in Part III of the Constitution, Articles 12 to 35: what "
        "each one guarantees every Indian, and how to enforce them.",
    'gratuity-new-labour-codes':
        "Gratuity in India 2026: who is eligible, how to calculate what you are owed, "
        "and what the Social Security Code quietly changed in your favour.",
    'gst-registration':
        "Do you need to register for GST? The turnover thresholds, who must register "
        "regardless, the process, and the cost of getting it wrong.",
    'how-to-file-fir-online':
        "How to file an FIR online in India: the e-FIR process, when a Zero FIR applies, "
        "and your rights if a police station refuses to register it.",
    'how-to-make-a-valid-will':
        "How to make a legally valid will in India: the requirements, a usable format, "
        "witnesses, and whether registration is actually necessary.",
    'how-to-send-legal-notice':
        "How to send a legal notice in India: the format, the process, what it must "
        "contain, and the cases where sending one is legally mandatory.",
    'how-to-terminate-a-contract':
        "How to end a contract without becoming the party in breach: termination "
        "clauses, notice, frustration, and the mistakes that trigger damages.",
    'increase-authorised-share-capital':
        "Increase authorised share capital with an ordinary resolution and Form SH-7 in "
        "30 days, plus stamp duty. Check the AOA first, and the penalty.",
    'indemnity-vs-guarantee':
        "Indemnity vs guarantee in Indian law: different parties, different liability, "
        "different consequences, and which clause you actually need.",
    'independent-directors-companies-act':
        "Independent directors: who must appoint one, the Section 149(6) test, IICA "
        "databank registration, the proficiency test and the 10-year cap.",
    'input-tax-credit-gst':
        "Input tax credit under GST: the conditions you must meet, the blocked credits "
        "you cannot claim, and the mistakes that get ITC reversed.",
    'ipo-sebi-icdr-eligibility-process':
        "IPO under SEBI ICDR 2018: the Reg 6(1) and 6(2) eligibility tests, promoter "
        "lock-in, investor quotas and the T+3 listing timeline.",
    'law-of-torts-india':
        "The law of torts in India: negligence, liability and the civil remedies you "
        "have when someone's carelessness or lie causes you real harm.",
    'lease-vs-leave-and-licence':
        "Lease vs leave and licence: how the two differ in law, which to use, and why "
        "the wrong choice changes your rights over the property.",
    'llp-registration':
        "Register an LLP in India step by step: DSC and DPIN, name reservation, FiLLiP, "
        "the LLP agreement, timelines, costs and annual compliance.",
    'mergers-amalgamations-companies-act':
        "Mergers under the Companies Act: the NCLT route, the fast-track Section 233 "
        "route for group companies, and how to pick between them.",
    'msa-vs-sow':
        "Master Service Agreement vs Statement of Work: what belongs in each, why "
        "vendors use both, and how the two documents work together.",
    'msme-1-half-yearly-return':
        "MSME Form 1 reports payments to micro and small suppliers delayed past 45 days. "
        "Due 31 Oct and 30 Apr, with penalties up to Rs 3 lakh.",
    'msme-udyam-registration-guide':
        "Who qualifies as an MSME, how free Udyam registration works, and the real "
        "benefits: delayed-payment protection and collateral-free loans.",
    'nda-key-clauses':
        "The NDA clauses you cannot skip in India: what counts as confidential "
        "information, the term, the carve-outs, and what makes one enforceable.",
    'notice-period-termination-settlement':
        "Notice period, termination and full-and-final settlement under the new Labour "
        "Codes: what your employer owes you when you leave, and by when.",
    'online-fraud-remedies':
        "Scammed online? The first hour matters most. How to report it, freeze the "
        "transaction, and give yourself the best chance of getting money back.",
    'private-placement-section-42':
        "Private placement under Section 42: the special resolution, PAS-4, a separate "
        "bank account, allotment in 60 days, and the 200-person cap.",
    'reduction-of-share-capital-section-66':
        "Reduce share capital under Section 66: the special resolution, NCLT "
        "confirmation, the three methods, the RSC forms and creditor protection.",
    'registration-act-guide':
        "The Registration Act, 1908 explained: which documents must be registered, how "
        "the process works, and why it matters most for property.",
    'related-party-transactions-section-188':
        "Related party transactions under Section 188: board approval, audit committee "
        "sign-off, the Rule 15 thresholds, AOC-2 and director recusal.",
    'rent-agreement-registration':
        "Why almost every Indian rent agreement runs 11 months, when registration "
        "becomes mandatory, the stamp duty, and the process step by step.",
    'rera-homebuyer-rights-complaint':
        "How RERA protects homebuyers: mandatory project registration, the carpet-area "
        "rule, delay penalties, and how to file a complaint.",
    'rights-issue-procedure-section-62':
        "Rights issue under Section 62(1)(a): board resolution only, the 15 to 30 day "
        "offer window, renunciation, unsubscribed shares and PAS-3 filing.",
    'sebi-lodr-explained':
        "SEBI LODR disclosure duties: what a listed company must announce, the "
        "30-minute clock after a board decision, and what catches boards out.",
    'sebi-pit-compliance-solutions-founders-kmp':
        "SEBI PIT compliance for founders and KMPs: the nine internal control systems "
        "Regulation 9A puts personally on the CEO or Managing Director.",
    'sebi-pit-insider-trading-explained':
        "SEBI insider trading rules explained: what counts as UPSI, how the trading "
        "window works, and the penalty that reaches Rs 25 crore.",
    'sebi-sast-takeover-code-open-offer':
        "SEBI Takeover Code 2011: the 25% open offer trigger, 5% creeping acquisition, "
        "and why acquiring control triggers an offer at any level.",
    'secretarial-audit-mr-3-section-204':
        "Secretarial audit under Section 204: which companies need Form MR-3, the "
        "capital, turnover and borrowing thresholds, and the peer-review rule.",
    'secretarial-standards-ss-1-ss-2':
        "SS-1 governs board meetings, SS-2 general meetings, and Section 118(10) makes "
        "both mandatory. The 2024 revisions, exemptions and penalties.",
    'section-185-loan-to-directors':
        "Section 185 bans loans to directors, with four narrow exceptions. What counts "
        "as a loan, who is caught, and the penalty for getting it wrong.",
    'section-186-inter-corporate-loans':
        "Inter-corporate loans under Section 186: the 60% limit, the unanimous board "
        "vote, the special resolution above it, and the Rs 5 lakh fine.",
    'section-8-vs-producer-company':
        "Section 8 company vs producer company: how each is formed, what each can do "
        "with grants or CSR money, and which one your group actually needs.",
    'service-agreement-guide':
        "How to draft a service agreement that holds up in an Indian court: scope, "
        "payment, IP, liability, termination and the clauses people forget.",
    'share-transfer-private-company-sh4':
        "How shares change hands in a private limited company: Form SH-4, stamp duty, "
        "right of first refusal, board approval and the register update.",
    'significant-beneficial-owner-ben-2':
        "An SBO owns 10% or more through other entities. BEN-1 from the individual, "
        "BEN-2 from the company in 30 days, and penalties up to Rs 10 lakh.",
    'statutory-registers-and-records':
        "The statutory registers every Indian company must keep: members, charges, SBOs, "
        "contracts and loans, the 7-day update rule, and the penalties.",
    'striking-off-company-stk-2':
        "How to close a defunct private limited company through Form STK-2: eligibility, "
        "documents, the ROC process, and the dormant-status option.",
    'tds-compliance-guide':
        "TDS compliance for FY 2025-26 and 2026-27: the rates, thresholds, deposit and "
        "return due dates, and the interest and penalties for a miss.",
    'vendor-supplier-agreement':
        "How to draft a vendor or supplier agreement in India: pricing, delivery, "
        "quality, liability, termination and the clauses that prevent disputes.",
    'vigil-mechanism-whistleblower-section-177':
        "Which companies must run a vigil mechanism under Section 177(9), how "
        "whistleblowers are protected, and their direct access to the audit chair.",
    'what-is-gst':
        "What GST is and how it replaced excise, VAT, service tax and octroi. CGST, SGST "
        "and IGST explained simply, with what you actually end up paying.",
    'gig-platform-workers-rights-labour-codes':
        "Gig and platform workers are recognised in law from 21 November 2025. The "
        "aggregator levy, what benefits it funds, and why you must register yourself.",
    'non-compete-clause-enforceability-india':
        "A post-employment non-compete is void in India under Section 27 of the Contract "
        "Act, however reasonable. What your employer can still enforce.",
    'fcra-vs-fema-foreign-funds-india':
        "FEMA governs foreign exchange, FCRA governs foreign donations. One question "
        "decides which applies - and only one of them carries criminal consequences.",
    'dpdp-rules-2025-compliance-timeline':
        "The DPDP Rules were notified in November 2025 with a staggered commencement. "
        "What bites now, what lands in 2027, and what to build in between.",
    'posh-internal-committee-small-company':
        "Ten employees means a mandatory Internal Committee with a prescribed "
        "composition. Below ten, complaints go to the Local Committee instead.",
    'ccfs-2026-companies-compliance-facilitation-scheme':
        "Clear overdue ROC filings for 10% of the additional fees under CCFS-2026. "
        "What it covers, who is excluded, and why 31 August 2026 is the real cliff.",
    'income-tax-act-2025-what-changed':
        "The Income-tax Act, 2025 replaced the 1961 Act on 1 April 2026. The tax year "
        "concept, the renumbering, and why your tax bill probably did not move.",
    'perquisite-valuation-rules-2026-salaried':
        "Company car perquisite jumped to Rs 5,000-7,000 a month from April 2026, while "
        "meal, education and HRA limits rose in your favour. The full table.",
    'will-vs-gift-deed-vs-trust':
        "Will vs gift deed vs trust: how each transfers property in India, what each "
        "costs in stamp duty and tax, and how to choose the right one.",
}


# Phrases that should become in-body links, mapped to the article they point at.
#
# Before this existed the site had 123 articles and 7 links between them, all
# external — every guide was a dead end for readers and an island for crawlers.
# Rather than editing 150,000 words of stored HTML (which would need a script run
# against the production database), the `autolink` filter applies this map at
# render time: new articles get linked automatically, and a slug rename is a
# one-line fix here.
#
# Rules for adding an entry:
#   * the phrase must be unambiguous — "Section 185" is fine, bare "guarantee"
#     is not, because it appears in unrelated statutory text;
#   * write it lowercase (matching is case-insensitive, display case is kept);
#   * longer phrases win over shorter overlapping ones ("GST registration"
#     beats "GST"), so both can coexist.
INTERNAL_LINKS = {
    # Added Aug 2026 after the Search Console page report: these five guides
    # were earning impressions (how-to-terminate-a-contract at position 9.9,
    # how-to-make-a-valid-will at 20.9) while receiving zero in-body links from
    # anywhere on the site. They already had entries here, but the phrases were
    # ones no other article happens to use, so autolink never fired for them.
    # Each phrase below was checked to occur in at least one other guide.
    #
    # Deliberately excluded: 'will' (appears in 47 articles, almost always the
    # auxiliary verb — linking "the company will file" to a will-drafting guide
    # would be worse than no link) and 'dividend' (too generic, and the only
    # phrase that actually occurs for the IEPF guide; a forced link there would
    # be link-building for its own sake).
    'breach of contract': 'how-to-terminate-a-contract',
    'probate': 'how-to-make-a-valid-will',
    'legal heir': 'how-to-make-a-valid-will',
    'tenancy': 'lease-vs-leave-and-licence',
    'licence agreement': 'lease-vs-leave-and-licence',
    'wrongful termination': 'employee-rights-how-to-enforce',
    'industrial dispute': 'employee-rights-how-to-enforce',

    # ─── Corporate compliance ───────────────────────────────────────────
    'alteration of moa': 'alteration-of-moa-aoa-section-13-14',
    'moa and aoa': 'alteration-of-moa-aoa-section-13-14',
    'inc-24': 'alteration-of-moa-aoa-section-13-14',
    'annual compliance': 'annual-compliance-companies',
    'aoc-4': 'annual-compliance-companies',
    'mgt-7': 'annual-compliance-companies',
    'roc filings': 'annual-compliance-companies',
    'llp annual compliance': 'annual-compliance-llps',
    'section 203': 'appointment-of-kmp-section-203',
    'key managerial personnel': 'appointment-of-kmp-section-203',
    'adt-1': 'auditor-appointment-rotation-removal',
    'auditor rotation': 'auditor-appointment-rotation-removal',
    'section 139': 'auditor-appointment-rotation-removal',
    'audit committee': 'board-committees-audit-nrc-stakeholders',
    'nomination & remuneration committee': 'board-committees-audit-nrc-stakeholders',
    'bonus issue': 'bonus-issue-of-shares-section-63',
    'section 63': 'bonus-issue-of-shares-section-63',
    'buyback': 'buyback-of-shares-unlisted-section-68',
    'buy-back': 'buyback-of-shares-unlisted-section-68',
    'section 68': 'buyback-of-shares-unlisted-section-68',
    'inc-22': 'change-of-registered-office-section-12',
    'registered office': 'change-of-registered-office-section-12',
    'chg-1': 'chg-1-registration-of-charges',
    'registration of charges': 'chg-1-registration-of-charges',
    'company registration': 'company-registration',
    'spice+': 'company-registration',
    'board meeting': 'conducting-a-valid-board-meeting-section-173',
    'section 173': 'conducting-a-valid-board-meeting-section-173',
    'annual general meeting': 'conducting-agm-egm-companies-act',
    'agm': 'conducting-agm-egm-companies-act',
    'egm': 'conducting-agm-egm-companies-act',
    'inc-27': 'conversion-private-public-company-section-18',
    'corporate governance': 'corporate-governance',
    'csr': 'csr-governance-section-135',
    'section 135': 'csr-governance-section-135',
    'dematerialisation': 'dematerialization-of-shares',
    'dematerialization': 'dematerialization-of-shares',
    'director identification number': 'din-allotment-kyc-disqualification',
    'dir-3 kyc': 'din-allotment-kyc-disqualification',
    'dir-12': 'dir-12-appointment-resignation-directors',
    'director duties': 'director-duties',
    'duties of a director': 'director-duties',
    'iepf': 'dividend-declaration-iepf-compliance',
    'unpaid dividend': 'dividend-declaration-iepf-compliance',
    'dormant company': 'dormant-company-section-455',
    'section 455': 'dormant-company-section-455',
    'dpt-3': 'annual-compliance-companies',
    'minute book': 'drafting-maintaining-minutes-section-118',
    'section 118': 'drafting-maintaining-minutes-section-118',
    'esop': 'esops-sweat-equity-shares',
    'esops': 'esops-sweat-equity-shares',
    'sweat equity': 'esops-sweat-equity-shares',
    'gst registration': 'gst-registration',
    'authorised share capital': 'increase-authorised-share-capital',
    'sh-7': 'increase-authorised-share-capital',
    'independent director': 'independent-directors-companies-act',
    'independent directors': 'independent-directors-companies-act',
    'llp registration': 'llp-registration',
    'limited liability partnership': 'llp-registration',
    'amalgamation': 'mergers-amalgamations-companies-act',
    'fast-track merger': 'mergers-amalgamations-companies-act',
    'msme-1': 'msme-1-half-yearly-return',
    'msme form 1': 'msme-1-half-yearly-return',
    'msme registration': 'msme-udyam-registration-guide',
    'udyam registration': 'msme-udyam-registration-guide',
    'private placement': 'private-placement-section-42',
    'section 42': 'private-placement-section-42',
    'pas-4': 'private-placement-section-42',
    'reduction of share capital': 'reduction-of-share-capital-section-66',
    'section 66': 'reduction-of-share-capital-section-66',
    'related party transaction': 'related-party-transactions-section-188',
    'related party transactions': 'related-party-transactions-section-188',
    'section 188': 'related-party-transactions-section-188',
    'aoc-2': 'related-party-transactions-section-188',
    'rights issue': 'rights-issue-procedure-section-62',
    'lodr': 'sebi-lodr-explained',
    'insider trading': 'sebi-pit-insider-trading-explained',
    'secretarial audit': 'secretarial-audit-mr-3-section-204',
    'mr-3': 'secretarial-audit-mr-3-section-204',
    'section 204': 'secretarial-audit-mr-3-section-204',
    'secretarial standards': 'secretarial-standards-ss-1-ss-2',
    'ss-1': 'secretarial-standards-ss-1-ss-2',
    'ss-2': 'secretarial-standards-ss-1-ss-2',
    'section 185': 'section-185-loan-to-directors',
    'section 186': 'section-186-inter-corporate-loans',
    'section 8 company': 'section-8-vs-producer-company',
    'producer company': 'section-8-vs-producer-company',
    'sh-4': 'share-transfer-private-company-sh4',
    'share transfer': 'share-transfer-private-company-sh4',
    'significant beneficial owner': 'significant-beneficial-owner-ben-2',
    'ben-2': 'significant-beneficial-owner-ben-2',
    'startup india': 'startup-india-registration',
    'dpiit': 'startup-india-registration',
    'statutory registers': 'statutory-registers-and-records',
    'stk-2': 'striking-off-company-stk-2',
    'striking off': 'striking-off-company-stk-2',
    'trademark registration': 'trademark-registration',
    'vigil mechanism': 'vigil-mechanism-whistleblower-section-177',
    'whistleblower': 'vigil-mechanism-whistleblower-section-177',
    'proprietorship': 'convert-proprietorship-partnership-to-company',

    # ─── Acts explained ─────────────────────────────────────────────────
    'anticipatory bail': 'anticipatory-bail-section-482-bnss',
    'bnss': 'bharatiya-nagarik-suraksha-sanhita-guide',
    'bharatiya nagarik suraksha sanhita': 'bharatiya-nagarik-suraksha-sanhita-guide',
    'bharatiya sakshya adhiniyam': 'bharatiya-sakshya-adhiniyam-guide',
    'code of civil procedure': 'code-of-civil-procedure-guide',
    'companies act, 2013': 'companies-act-2013-guide',
    'companies act 2013': 'companies-act-2013-guide',
    'competition act': 'competition-act-2002-guide',
    'constitution of india': 'constitution-of-india-guide',
    'cyber crime': 'cyber-crime-laws',
    'fundamental rights': 'fundamental-rights',
    'zero fir': 'how-to-file-fir-online',
    'intellectual property': 'ipr-explained',
    'law of torts': 'law-of-torts-india',
    'limitation act': 'limitation-act-1963-guide',
    'right to education': 'rte-act',
    'e-stamping': 'stamp-duty-agreements-estamping',
    'gst': 'what-is-gst',

    # ─── Competition ────────────────────────────────────────────────────
    'gun-jumping': 'cci-merger-control-sun-pharma-ranbaxy',
    'merger control': 'cci-merger-control-sun-pharma-ranbaxy',
    'abuse of dominance': 'competition-act-agreements-abuse-dominance',
    'cartel': 'competition-act-agreements-abuse-dominance',
    'cartels': 'competition-act-agreements-abuse-dominance',

    # ─── Consumer ───────────────────────────────────────────────────────
    'cheque bounce': 'cheque-bounce-section-138-ni-act',
    'section 138': 'cheque-bounce-section-138-ni-act',
    'e-jagriti': 'consumer-complaint-guide',
    'consumer complaint': 'consumer-complaint-guide',
    'consumer protection act': 'consumer-protection-act-2019-guide',
    'misleading ads': 'influencer-disclosure-misleading-ads',
    'online fraud': 'online-fraud-remedies',
    'rera': 'rera-homebuyer-rights-complaint',
    'right to information': 'right-to-information-act-guide',
    'rti': 'right-to-information-act-guide',

    # ─── Contracts ──────────────────────────────────────────────────────
    'electronic signature': 'electronic-signatures-india',
    'e-signature': 'electronic-signatures-india',
    'force majeure': 'force-majeure-clause',
    'legal notice': 'how-to-send-legal-notice',
    'termination clause': 'how-to-terminate-a-contract',
    'indemnity': 'indemnity-vs-guarantee',
    'master service agreement': 'msa-vs-sow',
    'statement of work': 'msa-vs-sow',
    'non-disclosure agreement': 'nda-key-clauses',
    'nda': 'nda-key-clauses',
    'service agreement': 'service-agreement-guide',
    'vendor agreement': 'vendor-supplier-agreement',
    'supplier agreement': 'vendor-supplier-agreement',

    # ─── FEMA ───────────────────────────────────────────────────────────
    'fc-gpr': 'fdi-reporting-fc-gpr-fc-trs-fla-compliance',
    'fc-trs': 'fdi-reporting-fc-gpr-fc-trs-fla-compliance',
    'fla return': 'fdi-reporting-fc-gpr-fc-trs-fla-compliance',
    'press note 3': 'fdi-routes-sectoral-caps-press-note-3',
    'sectoral cap': 'fdi-routes-sectoral-caps-press-note-3',
    'automatic route': 'fdi-routes-sectoral-caps-press-note-3',
    'fema': 'fema-1999-explained-current-capital-account',
    'section 37a': 'fema-penalties-violations-case-laws',

    # ─── Labour ─────────────────────────────────────────────────────────
    '50% wage rule': '50-percent-wage-rule',
    'wage definition': '50-percent-wage-rule',
    'employee rights': 'employee-rights-how-to-enforce',
    'epf': 'epf-esi-social-security-code',
    'esi': 'epf-esi-social-security-code',
    'gratuity': 'gratuity-new-labour-codes',
    'labour codes': 'new-labour-codes-explained',
    'notice period': 'notice-period-termination-settlement',
    'full-and-final settlement': 'notice-period-termination-settlement',

    # ─── Property ───────────────────────────────────────────────────────
    'valid will': 'how-to-make-a-valid-will',
    'indian stamp act': 'indian-stamp-act-guide',
    'leave and licence': 'lease-vs-leave-and-licence',
    'power of attorney': 'power-of-attorney-india',
    'title due diligence': 'property-title-due-diligence',
    'registration act': 'registration-act-guide',
    'rent agreement': 'rent-agreement-registration',
    'gift deed': 'will-vs-gift-deed-vs-trust',

    # ─── SEBI ───────────────────────────────────────────────────────────
    'further public offer': 'fpo-further-public-offer-explained',
    'disgorgement': 'sebi-pit-insider-trading-explained',
    'section 15g': 'sebi-pit-insider-trading-explained',
    'icdr': 'ipo-sebi-icdr-eligibility-process',
    'regulation 9a': 'sebi-pit-compliance-solutions-founders-kmp',
    'pit regulations': 'sebi-pit-insider-trading-explained',
    'connected person': 'sebi-pit-insider-trading-explained',
    'takeover code': 'sebi-sast-takeover-code-open-offer',
    'open offer': 'sebi-sast-takeover-code-open-offer',
    'upsi': 'sebi-pit-insider-trading-explained',

    # ─── Tax ────────────────────────────────────────────────────────────
    'gstr-1': 'gst-returns-explained',
    'gstr-3b': 'gst-returns-explained',
    'gst returns': 'gst-returns-explained',
    'presumptive taxation': 'income-tax-freelancers',
    'input tax credit': 'input-tax-credit-gst',
    'tds': 'tds-compliance-guide',

    # ─── Updates ────────────────────────────────────────────────────────
    'new criminal laws': 'bns-bnss-bsa-new-criminal-laws',
    'dpdp act': 'dpdp-act-compliance-guide',
    'parental consent': 'dpdp-childrens-data-parental-consent',
    'consent manager': 'dpdp-consent-managers',
    'consent managers': 'dpdp-consent-managers',
    'data breach': 'dpdp-data-breach-notification',
    'privacy policy': 'dpdp-privacy-policy',

    # ─── Added to close orphan gaps: every article needs at least one way in ──
    'encumbrance certificate': 'property-title-due-diligence',
    'title search': 'property-title-due-diligence',
    'vendor contract': 'vendor-supplier-agreement',
    'negligence': 'law-of-torts-india',
    'digital signature': 'electronic-signatures-india',
    'breach notification': 'dpdp-data-breach-notification',
    'strike off': 'striking-off-company-stk-2',
    'defunct company': 'striking-off-company-stk-2',
    'section 18': 'conversion-private-public-company-section-18',
    'lease agreement': 'lease-vs-leave-and-licence',
    'sbo': 'significant-beneficial-owner-ben-2',
    'ben-1': 'significant-beneficial-owner-ben-2',
    'limitation period': 'limitation-act-1963-guide',
    'time-barred': 'limitation-act-1963-guide',
    'demand notice': 'how-to-send-legal-notice',
    'form 11': 'annual-compliance-llps',
    'form 8': 'annual-compliance-llps',
    'terminate a contract': 'how-to-terminate-a-contract',
    'termination of contract': 'how-to-terminate-a-contract',
    "women's rights": 'rights-of-women',
    'rights of women': 'rights-of-women',
    'fpo': 'fpo-further-public-offer-explained',
    'section 44ada': 'income-tax-freelancers',
    'presumptive scheme': 'income-tax-freelancers',
    'labour commissioner': 'employee-rights-how-to-enforce',
    'cpc': 'code-of-civil-procedure-guide',
    'civil suit': 'code-of-civil-procedure-guide',
    'sast': 'sebi-sast-takeover-code-open-offer',
    'interim dividend': 'dividend-declaration-iepf-compliance',
    'declaration of dividend': 'dividend-declaration-iepf-compliance',
    'practising company secretary': 'secretarial-audit-mr-3-section-204',
    'unenforceable': 'common-contract-mistakes',
    'making a will': 'how-to-make-a-valid-will',
    'confidentiality agreement': 'nda-key-clauses',
    'memorandum of association': 'alteration-of-moa-aoa-section-13-14',
    'articles of association': 'alteration-of-moa-aoa-section-13-14',
    'ipr': 'ipr-explained',
    'section 482': 'anticipatory-bail-section-482-bnss',

    # ─── Content-gap articles (July 2026) ───────────────────────────────
    'gig worker': 'gig-platform-workers-rights-labour-codes',
    'gig workers': 'gig-platform-workers-rights-labour-codes',
    'platform worker': 'gig-platform-workers-rights-labour-codes',
    'aggregator': 'gig-platform-workers-rights-labour-codes',
    'non-compete': 'non-compete-clause-enforceability-india',
    'restraint of trade': 'non-compete-clause-enforceability-india',
    'section 27': 'non-compete-clause-enforceability-india',
    'fcra': 'fcra-vs-fema-foreign-funds-india',
    'foreign contribution': 'fcra-vs-fema-foreign-funds-india',
    'dpdp rules': 'dpdp-rules-2025-compliance-timeline',
    'data protection board': 'dpdp-rules-2025-compliance-timeline',
    'posh': 'posh-internal-committee-small-company',
    'internal committee': 'posh-internal-committee-small-company',
    'sexual harassment': 'posh-internal-committee-small-company',

    # ─── News-driven articles, Aug 2026 ─────────────────────────────────
    'ccfs': 'ccfs-2026-companies-compliance-facilitation-scheme',
    'ccfs-2026': 'ccfs-2026-companies-compliance-facilitation-scheme',
    'compliance facilitation scheme': 'ccfs-2026-companies-compliance-facilitation-scheme',
    'additional fees': 'ccfs-2026-companies-compliance-facilitation-scheme',
    'income-tax act, 2025': 'income-tax-act-2025-what-changed',
    'income tax act 2025': 'income-tax-act-2025-what-changed',
    'tax year': 'income-tax-act-2025-what-changed',
    'perquisite': 'perquisite-valuation-rules-2026-salaried',
    'perquisites': 'perquisite-valuation-rules-2026-salaried',
    'hra': 'perquisite-valuation-rules-2026-salaried',
    'house rent allowance': 'perquisite-valuation-rules-2026-salaried',
}


RETIRED_ARTICLES = {
    # Same topic, same category, published the same day. The survivor has the
    # sharper editorial angles (fake-website warnings, the GeM portal, how the
    # delayed-payment remedy actually plays out); the current 1 April 2025
    # thresholds from this one were merged into it first.
    'udyam-registration': 'msme-udyam-registration-guide',
    # Both explained the PIT Regulations end to end at the same depth. The
    # survivor is longer, covers the 2025 UPSI expansion, and carries the FAQ
    # and checklist; this one's disclosure section was merged into it first.
    'sebi-pit-regulations-2015-framework': 'sebi-pit-insider-trading-explained',

    # An earlier round of de-duplication (RETIRED_SLUGS in database.py, which
    # deletes the row outright) left these seven URLs returning 404. Any link or
    # index entry pointing at them has been dropped on the floor ever since;
    # sending them to their replacement recovers it.
    # Merged Aug 2026 into the PIT pillar: all three covered the same ground,
    # and the pillar was going to win every query the spokes targeted.
    'what-is-upsi-regulation-2-1-n': 'sebi-pit-insider-trading-explained',
    'insider-trading-penalties-case-studies': 'sebi-pit-insider-trading-explained',

    # Retired Aug 2026: led with a filing deadline that has since passed.
    # DPT-3 recurs annually, so the content is kept for a refreshed version.
    'dpt-3-fy-2025-26': 'annual-compliance-companies',

    'rti-act': 'right-to-information-act-guide',
    'rti-complete-guide': 'right-to-information-act-guide',
    'consumer-protection-act': 'consumer-protection-act-2019-guide',
    'annual-compliance-pvt-ltd': 'annual-compliance-companies',
    'gst-registration-thresholds-composition': 'gst-registration',
    'trademark-registration-india-guide': 'trademark-registration',
    'llp-compliance-calendar': 'annual-compliance-llps',
}
