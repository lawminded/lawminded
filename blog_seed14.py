# Owner-requested article, 28 August 2026.
#
# Owner named this topic directly in automation/queue.md on 2026-08-17 (lost
# before the queue file existed; re-queued 2026-08-22, moved to 28 August on
# the owner's own ask): the PMGEP scheme, what the benefits are, who can
# avail them, and the special benefits for women, SC/ST and other reserved
# categories.
#
# No scheme called "PMGEP" exists. Every search for the term returns results
# for PMEGP, the Prime Minister's Employment Generation Programme, and the
# queue entry's own description -- subsidy benefits, women/SC/ST eligibility
# -- matches PMEGP's actual subsidy structure exactly. Treated as a typo for
# PMEGP throughout. Checked the 135 published slugs first: nothing on the
# site covers PMEGP. Genuine gap, evergreen guide.
#
# Verified against primary and near-primary sources:
#  - PIB Delhi, Ministry of MSME, Release ID 2079789, 2 Dec 2024 ("Expansion
#    of Micro, Small and Medium Enterprises (MSMEs)"), fetched directly via
#    curl with a browser user-agent (WebFetch itself returns 403 on
#    pib.gov.in, consistent with prior sessions' notes on gov.in domains from
#    this box): margin money subsidy 25% rural / 15% urban for General
#    category, 35% rural / 25% urban for Special category (SC/ST/OBC/
#    Minorities/Women/Ex-servicemen/PwD/Transgender/NER/Hill and Border
#    areas/Aspirational Districts); max project cost Rs 50 lakh manufacturing,
#    Rs 20 lakh service; second loan for upgradation of an existing PMEGP/
#    MUDRA unit capped at Rs 1 crore manufacturing / Rs 25 lakh service, 15%
#    subsidy for all categories (20% NER/Hill), quoted directly.
#  - PIB Delhi, Ministry of MSME, Release ID 2222116, 2 Feb 2026, fetched the
#    same way: no collateral security for bank loans up to Rs 10 lakh per RBI
#    guidelines, strictly reemphasised by the Ministry to banks; no
#    educational qualification needed for projects up to Rs 10 lakh
#    manufacturing / Rs 5 lakh service; corroborates the Dec 2024 release on
#    both figures from an independent, more recent written reply.
#  - Delhi Khadi & Village Industries Board (Government of NCT of Delhi),
#    "Salient Features of Revised Scheme Guidelines of PMEGP"
#    (dkvib.delhi.gov.in), a state government page reproducing the central
#    scheme guidelines in full and last updated 21 August 2026: beneficiary's
#    own contribution (10% General / 5% Special), bank finance share (90%
#    General / 95% Special), the 3-year lock-in on margin money adjustment and
#    the refund-to-KVIC rule for underspend at that point, working capital
#    caps (40% manufacturing / 60% service), the one-application-per-family
#    rule (self and spouse), trading/retail restrictions and the 10% state
#    allocation cap on them, documents required (Aadhaar mandatory, or
#    enrolment number, or an alternate ID such as PAN in NER/J&K; caste and
#    special category certificates; project report; training certificate),
#    and the EDP/skill-training exemption for applicants already trained.
#    kviconline.gov.in itself (the scheme's own portal and PDF guidelines)
#    was unreachable from this box (DNS timeout on every attempt), so this
#    state government mirror of the same guidelines was used instead and
#    cross-checked against both PIB releases above -- all three agree on
#    every figure they share in common.
#
# Not used: a claim in several secondary/aggregator sources that Udyam or
# MSME registration is a precondition for a PMEGP application. Neither PIB
# release nor the DKVIB guidelines list Udyam registration among the
# eligibility conditions or the required documents, so the article states
# plainly, in the FAQ, that it isn't required -- an absence-based claim
# grounded in what the primary guidelines actually list, not a guess.
#
# Also not used: any claim that the subsidy is "clawed back" on default or
# early closure. The guidelines only state a refund-to-KVIC obligation where
# actual spending falls short of the sanctioned loan amount at the 3-year
# mark -- a narrower, different rule -- so the article states only that.
#
# Format matches the earlier seeds: (title, slug, category, act, read_time,
# summary, content).

BLOG_ARTICLES_14 = [

    ('PMEGP Scheme: The Government Subsidy to Start a Business, and Who Gets More',
     'pmegp-scheme-subsidy-guide',
     'corp',
     'PMEGP Scheme',
     '8 min read',
     "PMEGP pays first-time entrepreneurs a one-time subsidy of 15% to 35% of their project cost to set up a new manufacturing or service business, with women, SC/ST and several other categories getting the higher rate and a smaller share to put in themselves. Here's how the subsidy, the bank loan and the three-year lock-in actually work.",
     '<p><em>A lot of people who want to start a small business assume the only options are a bank loan at full interest, or borrowing from family. Fewer know that the central government will hand you a real subsidy toward the cost. If you are setting up a new manufacturing or service unit and can get a bank to back the rest, no repayment is required on that portion.</em></p><p><strong>The Prime Minister\'s Employment Generation Programme, PMEGP, gives first-time entrepreneurs a subsidy of 15% to 35% of their project cost to set up a new business. Women, SC/ST applicants and a few other groups get the higher end of that range, and put in less of their own money.</strong></p><blockquote><strong>Bottom line:</strong> PMEGP pays 15 to 35% of your project cost as a one-time subsidy. The exact share depends on your category and whether the unit is rural or urban. You put in 5 to 10% yourself. A bank funds the rest as a loan. It covers new units up to Rs 50 lakh in manufacturing or Rs 20 lakh in services and trading. It does not cover an existing business, land, or a project with no capital spending at all.</blockquote><h2>What PMEGP actually is</h2><p>PMEGP is a central sector scheme run by the Ministry of Micro, Small and Medium Enterprises. The Khadi and Village Industries Commission, KVIC, is the national nodal agency. On the ground, applications move through State KVIC offices, State Khadi and Village Industries Boards, and District Industries Centres.</p><p>It helps to know it is credit-linked, not a straight cash grant. You do not get government money in hand before you start. You apply, a bank sanctions and disburses a loan for the full project cost, and the government\'s share, called margin money, sits against that loan. After you have run the unit for three years, the margin money is adjusted against what you owe, cutting your real loan burden. If you have spent less than the bank sanctioned by then, the shortfall in subsidy goes back to KVIC rather than to you.</p><h2>Who can apply</h2><p>Any individual above 18 can apply. There is no income ceiling.</p><p>Education requirements are lighter than most people expect. You need no more than a Class 8 pass, and even that is required only if your project costs more than Rs 10 lakh in manufacturing or more than Rs 5 lakh in services. Below those numbers, there is no education requirement at all.</p><p>The unit has to be genuinely new. An existing business does not qualify, and neither does a unit that already received a subsidy under PMRY, REGP, MUDRA, or any other central or state government scheme.</p><p>Only one person per family can get PMEGP assistance. Here, family means you and your spouse. A sibling or a parent can still apply as a separate individual for their own unit.</p><p>Pure trading businesses are mostly excluded. Retail outlets selling Khadi or village-industry products, or backed by your own manufacturing or service work, are allowed nationwide. Standalone trading is permitted only in the Northeast, Left Wing Extremism-affected districts, and the Andaman and Nicobar Islands. All trading and retail activity together, including these exceptions, is capped at 10% of a state\'s yearly PMEGP allocation.</p><h2>How much subsidy you get, and how much you put in</h2><p>General category applicants contribute 10% of the project cost themselves and get a subsidy of 15% in urban areas or 25% in rural areas. Special category applicants contribute only 5% and get 25% in urban areas or 35% in rural areas.</p><p>The bank covers the balance either way, sanctioning 90% of project cost for general applicants and 95% for special category applicants, and disbursing the full loan up front. Your own contribution and the bank loan fund the business from day one. The subsidy only comes off your loan balance after the three-year lock-in.</p><h2>Who counts as "special category"</h2><p>The higher rate applies to Scheduled Castes, Scheduled Tribes, Other Backward Classes, religious minorities, women, ex-servicemen, persons with disabilities, and transgender applicants. It also applies to anyone setting up a unit in the Northeast, a notified hill or border area, or a government-declared Aspirational District.</p><p>Meeting more than one of these does not stack the benefit. A Scheduled Caste woman in a rural area still gets the same 35% rural rate as any other special category applicant there, not a higher one.</p><h2>Project cost limits, and what happens if you need more</h2><p>Margin money subsidy applies up to Rs 50 lakh for manufacturing projects and Rs 20 lakh for service or trading projects. If your actual project costs more, a bank can still lend you the extra amount, just without any government subsidy on that portion.</p><p>Working capital is capped as a share of project cost too: no more than 40% for manufacturing, and up to 60% for service and trading units, since those businesses typically carry less fixed investment.</p><h2>How to apply</h2><p>The entire process runs online through the PMEGP e-portal. There is no manual, paper-based route.</p><p>Aadhaar is mandatory for identity verification. If you do not have one yet, an Aadhaar enrolment number is accepted instead, and in the Northeast and Jammu & Kashmir, where Aadhaar coverage is thinner, an alternate ID such as PAN can be used.</p><p>You will upload a caste certificate if you are claiming SC, ST or OBC status, a special category certificate where one applies, a rural area certificate if relevant, a project report, and proof of any education or entrepreneurship training. If you have already completed at least 10 days of offline training, or 60 hours online, under a government entrepreneurship or skill development programme, you are exempt from doing it again before applying.</p><p>Once submitted, your application is scored and appraised by the implementing agency you picked, whether that is a KVIC office, a KVIB, or a District Industries Centre, and then forwarded to a bank for sanction.</p><h2>After the loan: the three-year lock-in, and a second loan later</h2><p>Your subsidy is not paid out immediately. It sits with the bank and gets adjusted against your loan only after three years of running the unit. If your actual spending falls short of the sanctioned loan by then, the difference in subsidy is refunded to KVIC rather than kept by you.</p><p>Run it successfully, repay the first loan, and you become eligible for a second PMEGP loan to expand or upgrade. This one has a single rate for every category: 10% own contribution and 15% subsidy, rising to 20% in the Northeast and hill states. The cap is Rs 1 crore for manufacturing and Rs 25 lakh for services.</p><h2>What this actually looks like</h2><p>Say a woman entrepreneur sets up a Rs 12 lakh stitching and garment unit in a village. As a special category, rural applicant, she puts in Rs 60,000, about 5%. The bank sanctions Rs 11.4 lakh as a loan and disburses it in full. After three years of running the unit, a subsidy of Rs 4.2 lakh, 35% of project cost, is adjusted against that loan, so her real repayment burden ends up being about 60% of the original cost.</p><p>Compare that to a general category applicant setting up a similar Rs 12 lakh unit in a city. He puts in Rs 1.2 lakh, 10%, and the bank loans Rs 10.8 lakh. His eventual subsidy adjustment is only Rs 1.8 lakh, 15%, so he ends up repaying about 75% of the project cost over time. Same idea, a meaningfully different outcome, purely from category and location.</p><h2>Common mistakes</h2><ul><li>Treating the subsidy as cash you get before you start. It is a bank loan first; the subsidy only reduces your balance after the three-year lock-in.</li><li>Inflating the project cost on paper to chase a bigger subsidy figure. Appraisers score applications specifically to catch this, and an unrealistic project report slows down or kills your sanction.</li><li>Assuming a spouse can file a second, "separate" application for the same household. PMEGP treats you and your spouse as one family and funds only one unit between you.</li><li>Confusing PMEGP with <a href="/article/msme-udyam-registration-guide">Udyam registration</a>. They solve different problems. PMEGP is the one-time subsidy that helps you start a new unit. Udyam is the ongoing MSME classification you register for afterward, and it unlocks separate benefits such as the <a href="/article/msme-1-half-yearly-return">45-day payment rule against buyers</a>.</li><li>Claiming special category status without the certificate to back it. The portal asks for the actual document at the application stage, not a self-declaration.</li></ul><h2>Frequently asked questions</h2><p><strong>Do I need collateral for the bank loan under PMEGP?</strong> For loans up to Rs 10 lakh, no. RBI guidelines bar banks from asking for collateral security on loans in that range, and the Ministry of MSME has told banks to follow this strictly.</p><p><strong>Can I apply if I already run a small, unregistered business?</strong> No. PMEGP funds only new units. An existing business, even an informal or unregistered one, does not qualify.</p><p><strong>What happens if my project costs more than the subsidy cap?</strong> The bank can still lend you the extra amount above Rs 50 lakh, manufacturing, or Rs 20 lakh, services, but that portion carries no government subsidy.</p><p><strong>Does belonging to more than one special category, say a Scheduled Caste woman, increase the subsidy further?</strong> No. You get the same special category rate, 35% rural or 25% urban, whichever applies once, not a combined or higher figure.</p><p><strong>Can my spouse apply separately for their own PMEGP unit?</strong> No. PMEGP treats an applicant and their spouse as a single family, and only one person from that family can receive assistance.</p><p><strong>Do I need an existing Udyam or MSME registration before I apply?</strong> No. Nothing in the scheme guidelines lists Udyam registration among the documents needed to apply. You register the unit afterward, once it is running.</p><p><strong>Is the subsidy the same for a second loan if I want to expand later?</strong> No. A second, upgradation loan carries one flat rate for every category, 10% own contribution and 15% subsidy, higher only in the Northeast and hill states, rather than the tiered general-versus-special rates that apply to a first loan.</p><p><em>This article is for legal awareness and education only and is not financial advice. Subsidy rates, project cost limits and eligibility conditions are set by the Ministry of MSME and KVIC and can change; confirm current terms on the PMEGP portal before applying.</em></p>'),

]
