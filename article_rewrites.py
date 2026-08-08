"""Wholesale replacement content for articles rewritten after publication.

Applied by `_apply_content_migrations` in database.py. Kept out of that file
because a 15KB HTML string buried in a migration is unreadable, and out of the
blog_seed modules because those only ever INSERT new slugs — these overwrite
articles that already exist in production.

Each entry is a full replacement body. Setting the whole field is deliberate:
chaining six REPLACE() calls against live HTML is how a migration half-applies
and leaves an article in a state nobody designed.
"""

# ── SEBI PIT: three articles merged into one ────────────────────────────────
#
# The site had four PIT articles. Crawling production showed the pillar sharing
# ~40% of its distinctive vocabulary with two of them, because the pillar
# carried a "What is UPSI" section and a "What's the penalty?" section that were
# the entire subject of those two spokes. Google had to choose between them, and
# the pillar was likely to win on every query the spokes were written for.
#
# Merged in: what-is-upsi-regulation-2-1-n, insider-trading-penalties-case-studies.
# Left standing: sebi-pit-compliance-solutions-founders-kmp — an operational
# build-guide for a different reader, which never flagged against the pillar.
PIT_MERGED_TITLE = (
    "SEBI Insider Trading Rules (PIT), Explained: UPSI, the Trading Window, "
    "Penalties and the Landmark Cases"
)

PIT_MERGED_SUMMARY = (
    "What counts as UPSI after the 2025 expansion, when the trading window shuts, "
    "who ends up in default, and the penalties that reach three times the profit."
)

PIT_MERGED_CONTENT = (
    "<p>A senior executive knows the quarterly numbers will beat the market's expectations. "
    "Results go public on Friday; on Wednesday she buys shares, telling herself she'd have "
    "bought anyway. That intent doesn't matter. She traded while holding unpublished "
    "price-sensitive information, and under the PIT Regulations the penalty can reach the "
    "higher of ₹25 crore or three times her gain — before any criminal exposure.</p>"

    "<blockquote><p><strong>The bottom line</strong></p>"
    "<p>The PIT Regulations ban trading in a listed company's securities while you possess "
    "<strong>unpublished price-sensitive information (UPSI)</strong>, and ban passing that "
    "information to others except for a legitimate purpose.</p>"
    "<p>A <strong>2025 amendment (effective 10 June 2025)</strong> widened UPSI to roughly "
    "<strong>16 categories</strong> aligned with LODR's material events; companies must log "
    "UPSI in a <strong>structured digital database</strong> and close the "
    "<strong>trading window</strong> when insiders may hold it.</p>"
    "<p>Penalties run to the <strong>higher of ₹25 crore or three times the profit</strong>, "
    "plus imprisonment of up to <strong>10 years</strong>.</p></blockquote>"

    "<h2>What do the PIT Regulations actually prohibit?</h2>"
    "<p>The <strong>SEBI (Prohibition of Insider Trading) Regulations, 2015</strong> — in "
    "force since <strong>15 May 2015</strong> — do two core things.</p>"
    "<p>First, <strong>Regulation 4</strong> bars an insider from trading in securities when in "
    "possession of UPSI. Note the word: <em>possession</em>, not use. You do not have to act "
    "<em>because</em> of the information for the prohibition to bite.</p>"
    "<p>Second, <strong>Regulation 3</strong> bars communicating UPSI to anyone, or procuring it "
    "from anyone, except where it is needed for a <strong>legitimate purpose</strong>, to "
    "perform duties, or to discharge a legal obligation. The person who passes the information "
    "is liable even if they never trade a single share.</p>"

    "<h2>What is UPSI? The two limbs</h2>"
    "<p><em>Governs this section: Regulation 2(1)(n), PIT Regulations, 2015</em></p>"
    "<p>Information is UPSI only when <strong>both</strong> limbs are satisfied:</p>"
    "<ol>"
    "<li><strong>Unpublished</strong> — not \"generally available\", meaning not accessible "
    "to the public on a non-discriminatory basis. Dissemination through the stock exchanges is "
    "the gold standard of generally available.</li>"
    "<li><strong>Price sensitive</strong> — likely to <em>materially</em> affect the price "
    "of the securities once it does become generally available.</li>"
    "</ol>"
    "<p>Two things follow that people get wrong. A rumour circulating widely on social media is "
    "not \"generally available\" merely because it is circulating. And information is price "
    "sensitive in <em>either</em> direction — bad news is UPSI exactly as much as good news.</p>"

    "<h2>The expanded UPSI list after 10 June 2025</h2>"
    "<p><em>Governs this section: Regulation 2(1)(n) as amended by the SEBI (PIT) (Amendment) "
    "Regulations, 2025</em></p>"
    "<p>For years the definition leaned on five illustrative categories — financial results, "
    "dividends, capital-structure changes, mergers and changes in key personnel — and "
    "companies treated anything outside them as fair game. SEBI closed that gap by aligning UPSI "
    "with Regulation 30 and Schedule III of the LODR Regulations, taking the list to roughly "
    "<strong>16 categories</strong>. Among the additions:</p>"
    "<ul>"
    "<li><strong>decisions on proposed fund raising</strong>;</li>"
    "<li><strong>agreements which may impact the management or control</strong> of the company;</li>"
    "<li><strong>initiation of a forensic audit</strong> for financial misstatement, siphoning or "
    "diversion of funds, and <strong>receipt of the final report</strong>;</li>"
    "<li><strong>fraud or defaults</strong> by the company, its promoters, directors, KMP or "
    "subsidiary, and <strong>arrests</strong> of key persons;</li>"
    "<li><strong>changes in rating(s)</strong>, other than ESG ratings;</li>"
    "<li><strong>resolution plans and restructuring</strong> of loans or borrowings;</li>"
    "<li><strong>one-time settlements</strong> with banks, and admission into insolvency "
    "proceedings;</li>"
    "<li><strong>grant, withdrawal, surrender, cancellation or suspension of key licences or "
    "regulatory approvals</strong>;</li>"
    "<li><strong>guarantees, indemnities or surety</strong> given for third parties outside the "
    "normal course of business;</li>"
    "<li><strong>material litigation or disputes</strong>, and awards or orders of regulators, "
    "courts or tribunals.</li>"
    "</ul>"
    "<p>The amendment came with two flexibilities. UPSI that <strong>originates outside</strong> "
    "the company can be entered in the database within <strong>2 calendar days</strong> of "
    "receipt, and the trading window need not close for such externally-sourced UPSI where "
    "designated persons are unlikely to hold it.</p>"

    "<h2>When does UPSI stop being UPSI?</h2>"
    "<p><em>Governs this section: Regulation 2(1)(e) — \"generally available information\"</em></p>"
    "<p>UPSI dies the moment the information becomes generally available, which in practice means "
    "dissemination through the stock exchanges. This is why trading windows reopen only "
    "<strong>48 hours after</strong> results are declared — the market needs time to absorb "
    "the disclosure.</p>"
    "<p>Selective disclosure does not help. Telling one analyst, one fund or one journalist does "
    "not make information generally available; it simply multiplies the number of insiders.</p>"

    "<h2>Who is an \"insider\" and a \"connected person\"?</h2>"
    "<p>An <strong>insider</strong> is anyone who is a connected person, or who is in possession "
    "of or has access to UPSI. Possession alone is enough — you do not need a job title.</p>"
    "<p>A <strong>connected person</strong> is anyone associated with the company in the six "
    "months before the act, in a position giving access to UPSI. That reaches directors, "
    "employees, bankers, auditors, lawyers and consultants.</p>"
    "<p><strong>Immediate relatives</strong> of connected persons are presumed to be connected. "
    "The presumption reverses the burden of proof: it is for them to show they had no access, "
    "not for SEBI to show they did.</p>"

    "<h2>What is the trading window, and when does it close?</h2>"
    "<p>The trading window is the period in which designated persons may deal in the company's "
    "securities. It <strong>closes</strong> when UPSI is likely to exist — most obviously "
    "from the end of a quarter until 48 hours after results are published.</p>"
    "<p>While it is shut, designated persons cannot trade even with pre-clearance. When it is "
    "open, trades above the prescribed value still need <strong>pre-clearance</strong> from the "
    "compliance officer, and a <strong>contra-trade</strong> within six months of an earlier "
    "trade is barred.</p>"

    "<h2>The structured digital database</h2>"
    "<p><em>Governs this section: Regulations 3(5) and 3(6), PIT Regulations, 2015</em></p>"
    "<p>Every listed company must maintain a <strong>structured digital database (SDD)</strong> "
    "recording the nature of each item of UPSI along with the names and PANs of everyone who "
    "shared it and everyone who received it. Entries need time-stamped, non-tamperable audit "
    "trails, and must be preserved for at least <strong>eight years</strong>.</p>"
    "<p>UPSI originating outside the company — a regulator's communication, an acquirer's "
    "approach — must reach the SDD within <strong>2 calendar days</strong> of receipt.</p>"
    "<blockquote><p><strong>Practitioner's note</strong></p>"
    "<p>The SDD is SEBI's first stop in every insider trading investigation. If someone traded "
    "profitably and the SDD shows they were in on the UPSI, the case is largely built. If the SDD "
    "is incomplete, the company itself faces action for the lapse. Keep it contemporaneous — "
    "retro-fitted entries show up in the audit trail and are worse than no entry at all.</p>"
    "</blockquote>"

    "<h2>What is a trading plan, and what changed in 2024?</h2>"
    "<p>A <strong>trading plan</strong> under Regulation 5 lets someone who is permanently in "
    "possession of UPSI — a CFO, say — trade lawfully by committing to trades well in "
    "advance, then losing all discretion over them.</p>"
    "<p>SEBI eased the mechanics in 2024: the cool-off period between submitting a plan and its "
    "first trade came down from six months to <strong>120 days</strong>, and the minimum plan "
    "duration from twelve months to <strong>two consecutive quarters</strong>. The plan must be "
    "approved by the compliance officer and disclosed to the exchanges, and once approved it is "
    "irrevocable.</p>"

    "<h2>The penalty architecture</h2>"
    "<p><em>Governs this section: Sections 11, 11B, 11(4), 15G, 15HB and 24, SEBI Act, 1992</em></p>"
    "<ul>"
    "<li><strong>Adjudication (s.15G):</strong> trading on UPSI, communicating it, or procuring it "
    "each attract a penalty of <strong>not less than ₹10 lakh, up to ₹25 crore or three "
    "times the profit made, whichever is higher</strong>. Related lapses such as disclosure "
    "defaults and code violations fall under separate sections including 15A and 15HB.</li>"
    "<li><strong>Directions (ss.11, 11B, 11(4)):</strong> SEBI can restrain a person from the "
    "securities market, suspend them from holding office in listed companies, freeze alleged "
    "gains through interim orders often passed without hearing them first, and order "
    "<strong>disgorgement</strong> — handing back profits with interest, credited to the "
    "Investor Protection and Education Fund.</li>"
    "<li><strong>Prosecution (s.24):</strong> imprisonment up to <strong>10 years</strong> or a "
    "fine up to <strong>₹25 crore</strong>, or both. Section 24 prosecutions are rare but "
    "real, and settlement is unavailable for serious, market-wide frauds.</li>"
    "<li><strong>Settlement:</strong> many PIT matters end through SEBI's settlement mechanism "
    "— settlement amounts, voluntary debarment and disgorgement, without admission of guilt.</li>"
    "</ul>"
    "<p>The three-times multiplier is the part insiders underestimate. On a large gain it dwarfs "
    "the ₹25 crore figure, and after-the-fact rationalisation is no defence once possession "
    "and trading coincide.</p>"

    "<h2>Who ends up \"in default\"?</h2>"
    "<p><em>Governs this section: Regulations 3, 4, 9 and 10, PIT Regulations, 2015</em></p>"
    "<ol>"
    "<li><strong>The trading insider</strong> — the person who dealt while in possession of "
    "UPSI (Reg 4).</li>"
    "<li><strong>The tipper</strong> — the insider who communicated UPSI outside a legitimate "
    "purpose (Reg 3(1)).</li>"
    "<li><strong>The tippee</strong> — the person who procured or induced communication of "
    "UPSI (Reg 3(2)) and traded.</li>"
    "<li><strong>Immediate relatives and connected persons</strong> — presumed to possess "
    "UPSI, with the burden of proof reversed onto them.</li>"
    "<li><strong>The listed company and its compliance officer</strong> — for Code of Conduct "
    "failures, missed exchange reporting and SDD gaps.</li>"
    "</ol>"

    "<h2>The landmark cases</h2>"
    "<p><strong>Hindustan Lever v SEBI (1998) — what \"unpublished\" means.</strong> HLL "
    "bought 8 lakh shares of Brooke Bond Lipton from UTI weeks before the HLL–BBLIL merger "
    "announcement. SEBI treated HLL as an insider trading on unpublished merger information. The "
    "appellate authority set the compensation direction aside, reasoning that the impending merger "
    "was already widely reported and so generally known. The case forced Indian law to sharpen "
    "what \"unpublished\" actually means.</p>"
    "<p><strong>Rakesh Agrawal v SEBI (SAT, 2004) — motive under the old regime.</strong> The "
    "managing director of ABS Industries bought shares through his brother-in-law ahead of Bayer's "
    "takeover, knowing the deal. SAT accepted he possessed UPSI but found he acted to help the "
    "acquisition succeed in the company's interest, which diluted the charge under the 1992 "
    "regulations. The 2015 regulations answered this case directly by making <em>possession</em>, "
    "not motive, the operative test.</p>"
    "<p><strong>SEBI v Abhijit Rajan (Supreme Court, 2022) — the direction of advantage.</strong> "
    "Gammon Infrastructure's managing director sold shares before the company announced termination "
    "of certain shareholder agreements. The Supreme Court held the terminated contracts were a "
    "small fraction of the order book, and that he had sold <em>against</em> his informational "
    "advantage rather than exploiting it. The judgment reintroduced a narrow profit-motive lens — "
    "but only where the trade runs contrary to what the information would suggest.</p>"
    "<p><strong>Balram Garg v SEBI (Supreme Court, 2022) — proximity is not proof.</strong> "
    "The Court held that a family relationship alone does not establish that UPSI was communicated. "
    "Cogent evidence of actual communication is needed, though trading patterns plus proximity can "
    "still build a circumstantial case.</p>"

    "<h2>Disclosure obligations</h2>"
    "<p><em>Governs this section: Regulations 6 and 7, PIT Regulations, 2015</em></p>"
    "<ul>"
    "<li><strong>Initial disclosure:</strong> every promoter, member of the promoter group, KMP "
    "and director discloses their holdings within 7 days of appointment or of becoming a promoter.</li>"
    "<li><strong>Continual disclosure (Reg 7(2)):</strong> promoters, promoter group, designated "
    "persons and directors must disclose to the company within <strong>2 trading days</strong> "
    "every trade, or series of trades in a calendar quarter, whose value exceeds "
    "<strong>₹10 lakh</strong>. The company passes it to the exchanges within 2 trading days "
    "of receipt.</li>"
    "</ul>"

    "<h2>Worked example</h2>"
    "<p>A designated person learns of an unannounced large order win — UPSI under the expanded "
    "2025 list — buys shares for ₹40 lakh, and sells after the announcement for "
    "₹70 lakh. A ₹30 lakh profit.</p>"
    "<p>Under Section 15G the adjudicating officer may impose up to ₹25 crore, or three times "
    "₹30 lakh, whichever is higher — so up to ₹25 crore, with ₹10 lakh as the "
    "floor. In parallel an 11B direction can disgorge the ₹30 lakh with interest and debar him "
    "from the market for years, and the company must report the code violation to the exchanges. "
    "If SEBI prosecutes under Section 24, imprisonment up to 10 years is on the table.</p>"
    "<p>The ₹30 lakh gain carries a worst case several orders of magnitude larger.</p>"

    "<h2>Common mistakes</h2>"
    "<ol>"
    "<li><strong>Testing only the old five categories.</strong> The list is now roughly 16 — "
    "fund-raising decisions, forensic audits, licence actions and control-impacting agreements are "
    "expressly in.</li>"
    "<li><strong>Treating rumours as generally available.</strong> Only non-discriminatory public "
    "dissemination kills UPSI.</li>"
    "<li><strong>Believing motive is a defence.</strong> Possession while trading suffices. "
    "<em>Abhijit Rajan</em> helps only where the trade runs against the insider's informational "
    "advantage.</li>"
    "<li><strong>Tipping \"harmlessly\".</strong> The communicator is liable under Regulation 3 "
    "even if they never trade.</li>"
    "<li><strong>Forgetting external UPSI.</strong> Information received from outside must reach "
    "the SDD within 2 calendar days.</li>"
    "<li><strong>Reopening the window at announcement.</strong> It reopens 48 hours <em>after</em> "
    "the information becomes generally available.</li>"
    "<li><strong>Assuming small trades escape notice.</strong> Surveillance flags pre-announcement "
    "trades of all sizes; ₹10 lakh is a disclosure threshold, not an enforcement floor.</li>"
    "<li><strong>Ignoring interim orders.</strong> Gains can be frozen and you can be barred from "
    "the market without being heard first, years before the case is finally decided.</li>"
    "</ol>"

    "<h2>Compliance checklist</h2>"
    "<ol>"
    "<li>Map all UPSI categories into the Code of Fair Disclosure and the internal materiality "
    "policy.</li>"
    "<li>Log every UPSI event in the SDD contemporaneously, with external UPSI inside 2 calendar "
    "days.</li>"
    "<li>Close the trading window on UPSI crystallisation; reopen 48 hours after dissemination.</li>"
    "<li>Restrict UPSI sharing to need-to-know recipients and capture every recipient's name and "
    "PAN.</li>"
    "<li>Run pre-clearance for trades above the threshold and block contra-trades inside six "
    "months.</li>"
    "<li>File initial and continual disclosures on time, and report code violations to the "
    "exchanges.</li>"
    "<li>Preserve SDD entries, pre-clearance records and window-closure notices for at least eight "
    "years.</li>"
    "<li>Train designated persons that forwarding results on WhatsApp <em>is</em> communication of "
    "UPSI.</li>"
    "</ol>"

    "<h2>FAQ</h2>"
    "<p><strong>What is UPSI in simple terms?</strong> Information about a company or its "
    "securities that is not yet public and that would likely move the price materially once it "
    "is. Both limbs must be met.</p>"
    "<p><strong>What is the minimum penalty for insider trading?</strong> ₹10 lakh under "
    "Section 15G. The ceiling is ₹25 crore or three times the profit made, whichever is "
    "higher.</p>"
    "<p><strong>Can insider trading lead to jail in India?</strong> Yes. Section 24 of the SEBI Act "
    "provides imprisonment up to 10 years, a fine up to ₹25 crore, or both.</p>"
    "<p><strong>Is profit necessary for liability?</strong> No. Trading while in possession of UPSI "
    "is the contravention. Profit only scales the penalty and the disgorgement.</p>"
    "<p><strong>Do I have to have used the information?</strong> No. Regulation 4 turns on "
    "possession, not use.</p>"
    "<p><strong>When did the expanded UPSI list take effect?</strong> 10 June 2025, ninety days "
    "from the March 2025 notification.</p>"
    "<p><strong>Are ESG rating changes UPSI?</strong> The 2025 amendment covers changes in ratings "
    "<em>other than</em> ESG ratings.</p>"
    "<p><strong>How long must the SDD be preserved?</strong> At least eight years, with "
    "time-stamped, non-tamperable audit trails, and longer where proceedings are pending.</p>"
    "<p><strong>Does a family relationship prove UPSI was shared?</strong> Not by itself. "
    "<em>Balram Garg</em> requires cogent evidence of actual communication.</p>"
    "<p><strong>Can a case be settled?</strong> Many PIT proceedings conclude under SEBI's "
    "settlement regulations with monetary terms and voluntary restraints, subject to SEBI's "
    "discretion.</p>"

    "<h2>Primary sources</h2>"
    "<ul>"
    "<li>Regulations 2(1)(e), 2(1)(n), 3, 4, 5, 6, 7, 9 and 10, SEBI (Prohibition of Insider "
    "Trading) Regulations, 2015</li>"
    "<li>SEBI (Prohibition of Insider Trading) (Amendment) Regulations, 2025 — notification "
    "dated 11 March 2025, effective 10 June 2025</li>"
    "<li>Sections 11, 11B, 11(4), 12A, 15G, 15HB and 24, SEBI Act, 1992</li>"
    "<li>Regulation 30 and Schedule III, SEBI (LODR) Regulations, 2015</li>"
    "<li>Hindustan Lever Ltd. v SEBI (1998); Rakesh Agrawal v SEBI (SAT, 2004); SEBI v Abhijit "
    "Rajan (SC, 2022); Balram Garg v SEBI (SC, 2022)</li>"
    "</ul>"
)


# ── DPDP: the guide's timeline section defers to the dedicated article ──────
#
# The compliance-timeline section of dpdp-act-compliance-guide and the whole of
# dpdp-rules-2025-compliance-timeline covered identical ground with identical
# dates — the highest overlap on the site at 43%. The guide keeps a short
# orientation and hands the detail to the article built for it.
DPDP_TIMELINE_OLD_MARKER = "<h2>The compliance timeline: three phases</h2>"

DPDP_TIMELINE_NEW = (
    "<h2>The compliance timeline</h2>"
    "<p>The Rules were notified on <strong>13 November 2025</strong> and commence in three stages. "
    "In short: the Data Protection Board and the penalty framework are already live; "
    "<strong>Consent Manager registration opens 13 November 2026</strong>; and the obligations "
    "that take real work — notice, security safeguards, breach notification, retention limits, "
    "children's data and data principal rights — bite on <strong>13 May 2027</strong>.</p>"
    "<p>That last date is the one to plan against, and it is closer than it looks: the data "
    "inventory alone takes most organisations several months. Our "
    "<a href=\"/article/dpdp-rules-2025-compliance-timeline\">guide to the DPDP Rules commencement "
    "timeline</a> sets out which rule numbers land in which phase and what to build before each.</p>"
)


# ── DPT-3: year-locked article rebuilt as the evergreen annual guide ─────────
#
# Published as "DPT-3 for FY 2025-26" around one filing season, then unpublished
# in migration 3 once 31 July 2026 passed — while Search Console had it ranking
# at position 8.8. Retiring a page-1 result for a filing that recurs every year
# was the wrong call; the fix is to stop writing it as a one-season article.
#
# The deadline is now stated as the standing rule (position as on 31 March,
# filed by 30 June), with the concrete next date, and the 31 July 2026
# relaxation demoted to a historical note so it reads as the one-off it was —
# an MCA Data Centre fire — rather than as a precedent anyone can rely on.
DPT3_TITLE = 'DPT-3 Return: Who Must File, the 30 June Deadline & Penalties'

DPT3_SUMMARY = (
    "DPT-3 falls due 30 June every year, covering loans outstanding on 31 March. Even one director's loan means you file. Next deadline: 30 June 2027.")

DPT3_SLUG = 'dpt-3-return-filing'

DPT3_CONTENT = (
    '<p><em>If a director, a sister company, or a bank has lent you money, you almost certainly have to file DPT-3 — even though none of it is a "deposit."</em></p><p><strong>Due every year: 30 June.</strong> The next return is due <strong>30 June 2027</strong>, for the year ended 31 March 2027.</p><p>A Pune SaaS company has never taken a rupee of public deposit. To bridge a tight payroll month, the founder-director put in ₹18 lakh of her own money. The books call it an unsecured director\'s loan and move on. <strong>That single entry is exactly what DPT-3 exists to capture</strong> — and the company secretary who waves it off as "we have no deposits" has just started a penalty clock.</p><p>That mistake is the most common reason companies miss this filing, year after year. The fix takes an afternoon. The penalty for ignoring it compounds by the day. Here is everything that actually matters — who files, what you report, when it falls due each year, and what it costs to get wrong.</p><blockquote><p><strong>BOTTOM LINE</strong></p><ul><li><strong>Who:</strong> Every company except government, banking, RBI-registered NBFC and NHB-registered housing-finance companies — including a private limited with only a director\'s loan outstanding.</li><li><strong>By when:</strong> 30 June every year, reporting the position as on the 31 March immediately before. The next filing is due <strong>30 June 2027</strong> for the year ended 31 March 2027.</li><li><strong>Miss it:</strong> Additional fee of 2×–12× the normal fee, plus up to ₹5,000 and ₹500/day on the company and every officer in default.</li></ul></blockquote><h2>What is DPT-3, in one minute?</h2><p><em>Governs this section: Rule 16, Companies (Acceptance of Deposits) Rules, 2014</em></p><p>DPT-3 is an annual return where a company tells the Registrar of Companies how much money it is holding that came in as a loan, an advance, or a deposit — and is still outstanding on 31 March.</p><p>The name is misleading. It reads as a "return of deposits," so founders assume it only matters if they ran a chit-fund-style deposit scheme. The 2019 amendment to the Companies (Acceptance of Deposits) Rules widened it far beyond that. Today the form has two jobs: report any actual deposits, <em>and</em> report the long list of borrowings the law specifically says are <strong>not</strong> deposits but still wants on record.</p><p>That second bucket is where almost every private company lives. You probably have nothing in the first.</p><h2>When is DPT-3 due?</h2><p><em>Governs this section: Rule 16, Companies (Acceptance of Deposits) Rules, 2014</em></p><p>The deadline does not move with the calendar. DPT-3 is an annual return, and the rule is the same every year: report the position as it stood on <strong>31 March</strong>, and file by <strong>30 June</strong> of that same year. Three months, every year, no reminder from the Registrar.</p><p>So the return for the year ended <strong>31 March 2027</strong> must be filed by <strong>30 June 2027</strong>. The year after that closes 31 March 2028 and falls due 30 June 2028, and so on. If you file nothing else on time, put this one in the calendar the day the books close.</p><blockquote><p><strong>DEADLINE &mdash; 30 June each year. Next: 30 June 2027.</strong></p><p>There is no grace period built into the rule. The additional fee starts the day after, and it is charged as a multiple of the normal fee rather than a flat late charge &mdash; which is why a filing that costs a few hundred rupees on time can cost several thousand a few months later.</p></blockquote><p><strong>What about extensions?</strong> The MCA occasionally relaxes the date for one year at a time, and only for a specific reason. For the year ended 31 March 2026 it allowed filing up to 31 July 2026 without additional fees, through General Circular No. 02/2026 dated 19 June 2026, after a fire at the MCA Data Centre on 5 June 2026 forced restoration work on the MCA21 V3 portal. That was a one-off tied to that incident. It set no precedent, and it did not change the rule &mdash; unless a circular says otherwise for the year you are filing, the date is 30 June. Check the MCA circulars page before you assume you have extra time.</p><h2>I never took deposits — do I still file?</h2><p><em>The expensive assumption</em></p><p>Almost certainly, yes. This is the single point worth being blunt about: <strong>"no public deposits" does not mean "no DPT-3."</strong> The form captures money the Act calls "not a deposit" — and that category is enormous.</p><p>If any of these were outstanding on the 31 March you are reporting &mdash; 31 March 2027 for the return due this June &mdash; you file:</p><ul><li>a loan from a <strong>director</strong> or a relative of a director;</li><li>a loan from a <strong>holding, subsidiary or associate</strong> company;</li><li>any <strong>inter-corporate loan</strong> from another company;</li><li>a <strong>bank or NBFC</strong> term loan, working-capital facility or overdraft;</li><li>a <strong>convertible note</strong> above ₹25 lakh (subject to conditions);</li><li>customer <strong>advances</strong> that have been sitting for more than 365 days.</li></ul><p>The mental model that actually works is a flowchart, not a definition:</p><blockquote><p><strong>[DIAGRAM 1 — Decision tree: "Do I need to file DPT-3?"]</strong></p><p>Build a simple yes/no flow from this logic:</p><ul><li>Are you a company under the Companies Act, 2013? → if no, stop.</li><li>Are you a govt / banking / RBI-NBFC / NHB housing-finance company? → if <strong>yes → EXEMPT, no DPT-3.</strong></li><li>Any loan, deposit or advance outstanding on 31 March 2027? → if <strong>no → file a NIL return (best practice).</strong> → if <strong>yes → FILE DPT-3 by 30 June 2027, even if it\'s only a director loan.</strong></li></ul><p>Caption: <em>The only test that matters: outstanding ≠ exempt from reporting.</em></p></blockquote><h2>Who is genuinely exempt?</h2><p><em>Governs this section: Rule 16A(3); proviso to Section 73(1)</em></p><p>The exemption list is short and specific. If you are not on it, you file.</p><div class="table-wrap"><table class="prose-table"><thead><tr><th>Exempt entity</th><th>Why it\'s out</th></tr></thead><tbody><tr><td>Government companies</td><td>Carved out at the root of the rule.</td></tr><tr><td>Banking companies</td><td>Regulated by the RBI under separate law.</td></tr><tr><td>NBFCs registered with the RBI</td><td>Already report to the RBI.</td></tr><tr><td>Housing-finance companies (registered with NHB)</td><td>Supervised by the National Housing Bank.</td></tr></tbody></table></div><blockquote><p><strong>PRACTITIONER\'S NOTE</strong></p><p>Insurance companies are the grey area. There is no explicit line for them in the rule, but because they are regulated by IRDAI rather than the RBI, professional practice and MCA helpdesk responses generally treat them as outside DPT-3. If you advise an insurer, document the basis rather than assuming it.</p></blockquote><h2>What exactly do I report?</h2><p><em>Governs this section: Rule 2(1)(c) — the classification test</em></p><p>Three buckets. Get an amount into the right one and the rest of the form is data entry.</p><div class="table-wrap"><table class="prose-table"><thead><tr><th>The money is…</th><th>Example</th><th>In DPT-3?</th></tr></thead><tbody><tr><td>A genuine <strong>deposit</strong></td><td>Public deposit; member deposit by a public company</td><td><strong>Report — deposit</strong></td></tr><tr><td><strong>Not a deposit</strong>, but outstanding</td><td>Director loan, inter-company loan, bank/NBFC loan, convertible note</td><td><strong>Report — exempted</strong></td></tr><tr><td>Creates <strong>no liability</strong> / inside the time window</td><td>Share application money allotted within 60 days; customer advance settled within 365 days</td><td><strong>Not reported</strong></td></tr></tbody></table></div><p>The middle row is the one that trips people. Those amounts are exempt from the <em>deposit rules</em>, not from <em>reporting</em>. When you file them, you cite the specific sub-clause of Rule 2(1)(c) that exempts each — for a director\'s loan in a private company, that\'s Rule 2(1)(c)(viii), and it must be backed by the director\'s written declaration that the money is her own, not on-lent borrowed funds.</p><h2>Do I need an auditor\'s certificate?</h2><p><em>Governs this section: form help-kit — return-type radio buttons 2 &amp; 4</em></p><p>It depends on which return type you pick on the form — and this is genuinely the most misunderstood part:</p><div class="table-wrap"><table class="prose-table"><thead><tr><th>You\'re filing…</th><th>Auditor\'s certificate?</th></tr></thead><tbody><tr><td>Return of <strong>deposits</strong></td><td>Required</td></tr><tr><td>Deposits <strong>and</strong> exempted receipts</td><td>Required</td></tr><tr><td>Only <strong>exempted</strong> receipts (the common case)</td><td>Not required</td></tr></tbody></table></div><p>So the typical private company reporting nothing but a director\'s loan and a bank facility does <strong>not</strong> need an auditor\'s certificate. When one is needed, there is no prescribed format — the ICAI has published an illustrative one auditors generally adapt. And note: the form itself can be signed by a director, manager, CEO, CFO or company secretary; it does not require separate certification by a practising professional.</p><h2>What does it cost if I miss it?</h2><p><em>Governs this section: Rule 21; Fees Rules; Section 73</em></p><p>There are three different cost layers, and conflating them is how blogs scare people with the wrong number.</p><p><strong>Layer one — the late fee.</strong> File after the deadline and the MCA stacks an additional fee on the normal filing fee, scaled to how late you are:</p><div class="table-wrap"><table class="prose-table"><thead><tr><th>Delay</th><th>Additional fee</th></tr></thead><tbody><tr><td>Up to 30 days</td><td>2× normal fee</td></tr><tr><td>30 – 60 days</td><td>4× normal fee</td></tr><tr><td>60 – 90 days</td><td>6× normal fee</td></tr><tr><td>90 – 180 days</td><td>10× normal fee</td></tr><tr><td>Over 180 days</td><td>12× normal fee</td></tr></tbody></table></div><p>The "normal fee" itself is small and based on share capital — from ₹200 (capital under ₹1 lakh or no share capital) up to ₹600 (capital of ₹1 crore or more).</p><p><strong>Layer two — the Rule 21 penalty.</strong> This is the one that bites for plain non-filing:</p><blockquote><p><strong>PENALTY · Rule 21</strong></p><p>The company <strong>and every officer in default</strong> can be fined up to ₹5,000, and where the default continues, a further ₹500 for every day it runs. It attaches to the people who signed, not just the entity.</p></blockquote><p><strong>Layer three — Section 73, the heavy one.</strong> The figures you\'ll see quoted — up to ₹10 crore and imprisonment up to 7 years — are real, but they apply to <em>actually accepting deposits in breach of the law</em>, not to a late DPT-3 on exempt loans. Don\'t let a vendor frame a missed return as a ₹10 crore event. Do take it seriously if your company has genuinely been taking deposits it shouldn\'t.</p><h2>A worked example with the numbers</h2><p><strong>Mini-case — the Pune SaaS company: one director loan, one bank facility, zero deposits</strong></p><p>Back to our company. As on 31 March 2027, its books show:</p><div class="table-wrap"><table class="prose-table"><thead><tr><th>Item</th><th>Amount</th></tr></thead><tbody><tr><td>Director\'s loan (founder)</td><td>₹18,00,000</td></tr><tr><td>Bank working-capital facility</td><td>₹40,00,000</td></tr><tr><td>Customer advance, received Feb 2026</td><td>₹6,00,000</td></tr><tr><td><strong>Reportable as exempted receipts</strong></td><td><strong>₹58,00,000</strong></td></tr></tbody></table></div><p>The director\'s loan goes in citing Rule 2(1)(c)(viii); the bank facility under Rule 2(1)(c)(iii). The ₹6 lakh customer advance is <strong>under 365 days old</strong>, so it stays out — for now. Total deposits: ₹0. So this is <em>not</em> a NIL return — there\'s ₹58 lakh to report — but it needs <strong>no auditor\'s certificate</strong>, because it\'s a return of exempted receipts only.</p><p>Now suppose they\'d believed "no deposits, no filing" and surfaced it 70 days late. Normal fee (capital ₹10 lakh) is ₹400; the 60–90-day slab makes the additional fee 6×, i.e. ₹2,400 on top — plus exposure to the Rule 21 fine on the company and the officers who let it slip. A few thousand rupees and a director\'s name on a default list, to skip an afternoon\'s work.</p><h2>Common mistakes</h2><p>The five mistakes that cause late filings:</p><ol><li><strong>"No deposits, so it doesn\'t apply."</strong> The reason most late filings happen. Exempted loans are still reportable.</li><li><strong>Forgetting the director\'s declaration.</strong> A private company\'s director loan needs a written declaration that the funds are the director\'s own — and a note in the Board\'s report. No declaration, shaky filing.</li><li><strong>Filing the wrong return type.</strong> Picking "Return of Deposits" when you only have exempted receipts triggers a needless auditor\'s-certificate requirement — and a possible query.</li><li><strong>Skipping the NIL return.</strong> Not strictly mandatory when nothing is outstanding, but filing it keeps your compliance trail clean and pre-empts ROC scrutiny. File it.</li><li><strong>Treating revision as easy.</strong> DPT-3 can\'t simply be re-filed. Fixing an error means approaching the ROC to mark the original defective. Get the numbers right the first time.</li></ol><h2>Before-you-file checklist</h2><ol><li>Pull the trial balance as on 31 March 2027 and list every loan, deposit and advance outstanding.</li><li>Classify each amount: deposit, exempted-but-reportable, or out of scope — and note the Rule 2(1)(c) sub-clause for the exempted ones.</li><li>Collect the director\'s declaration for any director/relative loan in a private company.</li><li>Confirm your net worth figure from the latest audited balance sheet.</li><li>Pick the correct return type (most companies: exempted receipts only — no auditor\'s certificate).</li><li>File on the MCA21 V3 portal and pay the fee. Save the SRN and the challan.</li><li>Don\'t wait for 31 July. The portal is still recovering from the June outage.</li></ol><h2>FAQ</h2><p><strong>Is a NIL DPT-3 return mandatory?</strong> Not strictly, when nothing is outstanding on 31 March. But filing a NIL return is strong practice — it documents that you considered the obligation and keeps your ROC record clean. Most company secretaries file it as a default.</p><p><strong>Does a One Person Company (OPC) have to file DPT-3?</strong> Yes. OPCs, private limited, public limited and Section 8 companies all fall within DPT-3. Only the four exempt categories — government, banking, RBI-registered NBFC, NHB housing-finance — are out.</p><p><strong>Are bank loans really reportable, even though they\'re obviously not deposits?</strong> Yes. Loans from banks, NBFCs and financial institutions are "exempted deposits" under Rule 2(1)(c)(iii) — exempt from the deposit rules, but still reported in DPT-3.</p><p><strong>What period does the return cover?</strong> Each return reports the amounts outstanding as on 31 March, and is due by 30 June that same year. The return for the year ended 31 March 2027 is due 30 June 2027.</p><p><strong>Can I revise a DPT-3 after filing?</strong> Not directly. If you find an error, you generally have to ask the Registrar of Companies to treat the original filing as defective before a corrected return is accepted — so accuracy on the first attempt matters.</p><p><strong>Primary sources</strong></p><ul><li>MCA General Circular No. 02/2026 dated 19 June 2026 — DPT-3 fee relaxation (mca.gov.in → Circulars; link the exact PDF)</li><li>Rule 16 &amp; Rule 16A, Companies (Acceptance of Deposits) Rules, 2014</li><li>Rule 2(1)(c) — amounts not considered deposits</li><li>Section 73, Companies Act, 2013 &amp; Rule 21 — penalties</li></ul><p><em>Disclaimer: This article is general information on a fast-changing area of company law, current at the time of writing. It is not legal or professional advice for any specific company. Verify the position against the live MCA notification and consult your company secretary or auditor before filing.</em></p>')
