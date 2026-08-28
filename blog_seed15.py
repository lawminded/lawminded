# Owner-requested article, 28 August 2026 (asked for over Telegram: "Go for
# sebi and make a detailed brief blog for laymen remember its for laymen but
# make it full detailed").
#
# Checked the 136 published slugs first. The site already has six SEBI
# articles, and every one of them faces the issuer or the compliance officer:
# sebi-lodr-explained, sebi-pit-insider-trading-explained,
# sebi-pit-compliance-solutions-founders-kmp, ipo-sebi-icdr-eligibility-process,
# fpo-further-public-offer-explained, sebi-sast-takeover-code-open-offer.
# Nothing on the site explains SEBI itself to the person who owns the shares.
# That is the gap this fills: what SEBI is, what it can and cannot touch, how
# an ordinary investor checks a registration, and the exact complaint route.
# Evergreen guide, no overlap.
#
# Written in short sentences with every term explained on first use, per the
# standing note in automation/notes.md dated 14 and 26 August 2026.
#
# Every claim verified against the primary instrument. Full claim-by-claim list
# in REVIEW-BEFORE-PUBLISH.md on this branch. Sources in brief:
#  - SEBI Act, 1992, consolidated text published by SEBI at
#    sebi.gov.in/sebi_data/attachdocs/mar-2019/1552282367672.pdf, read as text.
#    Sections 1(3), 3(3), 4(1), 11(1), 11(3), 11(4), 11(5), 11B, 11C, 11D,
#    12(1), 15C, 15G, 15HA, 15HB, 15T(3), 15Y, 15Z, 24(1), 26(1).
#  - SEBI circular SEBI/HO/DEPA-II/DEPA-II_SRG/P/CIR/2025/86, 11 June 2025,
#    on validated "@valid" UPI IDs, including the thumbs-up-in-green-triangle
#    icon and the 1 October 2025 availability date.
#  - SEBI circular SEBI/HO/MIRSD/MIRSD-PoD-1/P/CIR/2024/143, 22 October 2024,
#    on association with persons giving unregistered advice or making return
#    claims, and the three-month termination window.
#  - SEBI Master Circular for Online Resolution of Disputes in the Indian
#    Securities Market, 28 December 2023, for the SMART ODR timelines, the
#    Rs 30 lakh three-arbitrator threshold, the Rs 1 lakh document-only
#    threshold and the Rs 5 lakh interim release.
#  - SCORES FAQs on SEBI's own platform, scores.sebi.gov.in/faqs, for the
#    21 / 15 / 10 / 15 calendar-day chain and the excluded complaint types.
#
# Category is 'sebi', which the site already uses.

BLOG_ARTICLES_15 = [

    ('SEBI Explained in Plain English: What It Regulates, What It Can Punish, and How You Complain',
     'what-is-sebi-plain-english-guide',
     'sebi',
     'SEBI Act 1992',
     '9 min read',
     "SEBI is the statutory regulator of India's securities market. It registers brokers, mutual funds and advisers, can fine them crores and bar them from the market, and runs a free complaint system called SCORES. Here is what it can do for an ordinary investor, what it cannot, and the exact steps to complain.",
     '<p><em>Almost anyone with a demat account, a mutual fund SIP or a handful of shares is dealing with a business that SEBI regulates. Very few could say what SEBI actually is, what it can do when something goes wrong, or how to reach it. That knowledge becomes urgent on the day a broker stops answering the phone.</em></p>'
     '<p><strong>SEBI is the statutory regulator of India\'s securities market. It registers and polices brokers, mutual funds, investment advisers and listed companies. It can fine them, ban them from the market and freeze their money, and it runs a free online complaint system that any investor can use.</strong></p>'
     '<blockquote><strong>Bottom line:</strong> SEBI protects the process, not your profits. It can force a broker or a listed company to deal with you properly, fine them Rs 1 lakh a day for ignoring your grievance, and throw them out of the market. It cannot turn a bad investment into a good one or recover a loss on a share that simply fell. It has nothing to do with your bank account, your insurance policy or a dispute with an unlisted company. Complaining through SCORES is free. Getting money back is a separate route called SMART ODR.</blockquote>'

     '<h2>What SEBI is</h2>'
     '<p>SEBI stands for the Securities and Exchange Board of India. Parliament created it through the SEBI Act, 1992, which is deemed to have come into force on 30 January 1992. Its head office is in Mumbai.</p>'
     '<p>Section 11(1) of that Act describes the job in a single sentence. SEBI must protect the interests of investors in securities, promote the development of the securities market, and regulate it. Every power it has flows from that line.</p>'
     '<p>The Board itself is small. Under Section 4, it has a Chairman, two members from the central government ministry that deals with finance and company law, one member from the Reserve Bank of India, and five others appointed by the central government. At least three of those five must be full-time.</p>'

     '<h2>What SEBI covers, and what it does not</h2>'
     '<p>SEBI\'s territory is the securities market. That means shares, debentures, bonds listed on an exchange, mutual funds, derivatives, and the businesses that sell and handle all of it.</p>'
     '<p>A great many money problems are not securities problems. This is where complaints get bounced. Your savings account, home loan, credit card and NBFC deposit belong to the Reserve Bank of India. Your life or health insurance policy belongs to IRDAI. Your NPS account belongs to PFRDA. A fight with a private unlisted company is an ordinary civil or company law matter. Listed companies are a different case, because SEBI sets what they must tell you and when, through the <a href="/article/sebi-lodr-explained">LODR disclosure rules</a>.</p>'
     '<p>SEBI\'s complaint system says this openly. It will not take up a complaint that does not relate to investment in the securities market, or one that falls under another regulator, or one about a company that is not listed.</p>'

     '<h2>Anyone who takes your money has to be registered</h2>'
     '<p>Section 12(1) of the SEBI Act is short and strict. A stock broker, share transfer agent, banker to an issue, registrar to an issue, merchant banker, underwriter, portfolio manager or investment adviser cannot buy, sell or deal in securities without a certificate of registration from SEBI.</p>'
     '<p>For an ordinary investor this is the single most useful check available. If someone is taking your money to invest, or charging you a fee for stock recommendations, they must hold a SEBI registration number. Registered intermediaries can be looked up on SEBI\'s own intermediary portal. No number, no deal.</p>'
     '<p>SEBI closed the loop from the other side in 2024. A circular dated 22 October 2024 bars any SEBI-regulated person, and their agents, from associating with certain unregistered people. It rests on amendments to the Intermediaries Regulations notified on 26 August 2024. Two activities trigger the bar: giving advice or recommendations on securities without registration, and making any claim about returns or performance without SEBI\'s permission. Regulated firms were told to end existing contracts with such people within three months.</p>'
     '<p>This is the rule aimed at unregistered stock tipsters online. Someone genuinely doing investor education is not caught by it, provided they stop short of recommendations and return claims.</p>'

     '<h2>The @valid UPI handle</h2>'
     '<p>SEBI added a check at the payment stage in 2025. Under a circular dated 11 June 2025, every SEBI-registered intermediary that collects money from investors must obtain a special UPI address. The handle after the "@" reads "valid" followed by the bank\'s name. A broker\'s address might look like abc.brk@validhdfc, and a mutual fund\'s like xyz.mf@validhdfc. The part before the "@" carries a short code for what kind of intermediary they are.</p>'
     '<p>Pay to one of these addresses and your UPI app shows a thumbs-up icon inside a green triangle. SEBI\'s stated reasoning is blunt. The icon assures you that the money is going to a verified registered intermediary, and its absence should warn you that it may not be. These IDs have been available to investors since 1 October 2025. Using them is optional for you. Offering one is mandatory for the intermediary.</p>'

     '<h2>What SEBI can actually do to a wrongdoer</h2>'
     '<p>SEBI is not only a complaints desk. Its powers under the Act are wide, and it can use most of them while an inquiry is still going on.</p>'
     '<p>Under Section 11C it can order an investigation into anyone in the securities market when it has reasonable grounds to believe transactions are harming investors, or that a rule has been broken. The investigating officer can demand books and records, and examine people on oath.</p>'
     '<p>Under Section 11B it can issue directions to any intermediary or person connected with the market. The Act spells out that this includes ordering someone to disgorge, meaning hand over, an amount equal to the wrongful gain they made or the loss they avoided.</p>'
     '<p>Under Section 11D it can pass a cease and desist order, which simply tells a person to stop doing something, or to stop before they start.</p>'
     '<p>Section 11(4) carries the sharpest tools. SEBI can suspend trading in a security on an exchange. It can bar a person from accessing the securities market altogether. It can impound the proceeds or securities of a transaction under investigation. It can attach bank accounts or other property for up to ninety days, and it must get that attachment confirmed by a Special Court within those ninety days if it is to continue.</p>'
     '<p>When SEBI calls for information or runs an inquiry, Section 11(3) gives it the same powers a civil court has when trying a suit: to summon people, to examine them on oath, and to order the production of documents.</p>'

     '<h2>The fines, in actual numbers</h2>'
     '<p>The penalties in Chapter VIA of the Act are large, and they are not discretionary in the way people assume.</p>'
     '<p>Insider trading, under Section 15G, carries a penalty of Rs 25 crore or three times the profit made, whichever is higher. The same figure applies under Section 15HA to fraudulent and unfair trade practices in securities. Our separate guide on <a href="/article/sebi-pit-insider-trading-explained">SEBI\'s insider trading rules</a> goes into how those cases are actually built.</p>'
     '<p>Section 15C is the one that matters most to an ordinary complainant. Suppose SEBI writes to a listed company or a registered intermediary and calls on it to redress an investor grievance. If it fails to do so in the time SEBI sets, the penalty is Rs 1 lakh for every day the failure continues, up to Rs 1 crore.</p>'
     '<p>Section 15HB is the catch-all. Any breach of the Act, the rules, the regulations or a SEBI direction that has no separate penalty attracts a penalty of up to Rs 1 crore.</p>'
     '<p>Beyond fines, Section 24(1) makes contravention of the Act a criminal offence, punishable with imprisonment of up to ten years, or a fine of up to Rs 25 crore, or both. Failing to pay a penalty or comply with an order carries the same maximum, with a minimum of one month\'s imprisonment. A court can only take up such a case on a complaint made by SEBI itself, under Section 26(1).</p>'

     '<h2>How to complain, step by step</h2>'
     '<p>The route is fixed, and skipping a step gets your complaint rejected.</p>'
     '<p><strong>First, complain to the entity itself.</strong> Write to the broker, the mutual fund, the registrar or the listed company, and keep the acknowledgement. SEBI expects you to have tried this.</p>'
     '<p><strong>Second, file on SCORES.</strong> SCORES is SEBI\'s free online complaint platform, at scores.sebi.gov.in. Since the SCORES 2.0 upgrade the clock is tight. The entity has 21 calendar days from receiving your complaint to resolve it and upload an Action Taken Report, which is its written account of what it did.</p>'
     '<p><strong>Third, ask for a review if the answer is poor.</strong> You have 15 calendar days from the date of that report to ask for a first review. The review goes to a designated body, usually the stock exchange or depository that oversees the entity, and it has 10 calendar days to come back to you.</p>'
     '<p><strong>Fourth, escalate to SEBI.</strong> If the designated body\'s answer is also unsatisfactory, you have another 15 calendar days to seek a second review, and that one is handled by SEBI.</p>'
     '<p>Some things SCORES will not accept at all: anonymous complaints, complaints with no supporting documents, matters already pending before a court or a quasi-judicial body, disputes with unlisted or delisted companies, and anything belonging to another regulator. Reporting a suspected violation is also treated differently. SEBI logs that as market intelligence rather than as a complaint, so do not expect a personal reply.</p>'

     '<h2>Getting money back: SMART ODR</h2>'
     '<p>SCORES fixes conduct. It does not decide who owes whom how much. For a monetary claim against a broker, a depository participant or a listed company, SEBI runs a separate route called online dispute resolution, on a portal known as SMART ODR. Its framework comes from a master circular dated 28 December 2023.</p>'
     '<p>You reach it after trying the entity and SCORES. The exchange or depository reviews the dispute first, within 21 calendar days, and tries to settle it. If that fails, the matter goes to an independent dispute resolution institution, which appoints a single neutral conciliator within 5 days. A conciliator is a mediator, not a judge, and gets 21 calendar days to help both sides agree, extendable by 10 days if both sides consent.</p>'
     '<p>If conciliation fails, either side can go to online arbitration, which does produce a binding decision. One arbitrator hears the matter, unless the claims and counter-claims together exceed Rs 30 lakh, in which case three arbitrators sit. The award must come within 30 calendar days of appointment, extendable by a further 30 days for a complicated matter. Claims of Rs 1 lakh or less are decided on documents alone, with no hearing unless the arbitrator wants one.</p>'
     '<p>One detail is worth knowing before you start. The market participant has to deposit money once arbitration begins. If you apply, the exchange or depository can release up to Rs 5 lakh of that deposit to you while the arbitration is still running. You have to give an undertaking to return it if you lose. The consequences of not returning it are severe. You are barred from trading anywhere in the Indian securities market, and your demat holdings and mutual fund units are frozen until you repay.</p>'

     '<h2>If you disagree with SEBI itself</h2>'
     '<p>SEBI orders are not final. Anyone aggrieved by an order of SEBI, or of one of its adjudicating officers, can appeal to the Securities Appellate Tribunal within 45 days of receiving a copy of the order, under Section 15T(3). SAT can condone a delay if you show sufficient cause.</p>'
     '<p>From SAT, an appeal lies to the Supreme Court within 60 days, under Section 15Z, but only on a question of law. The Supreme Court can allow a further 60 days for good reason.</p>'
     '<p>What you cannot do is go to an ordinary civil court. Section 15Y bars civil courts from entertaining any suit on a matter that an adjudicating officer or SAT is empowered to decide, and bars them from granting injunctions against action taken under the Act.</p>'

     '<h2>What SEBI will not do for you</h2>'
     '<p>This is where most investor disappointment comes from, so it is worth stating plainly.</p>'
     '<p>SEBI will not compensate you for a market loss. A share that fell, a fund that underperformed, an <a href="/article/ipo-sebi-icdr-eligibility-process">IPO</a> that listed below its issue price: none of these is a regulatory failure, and no complaint route will get that money back.</p>'
     '<p>SEBI also does not hand disgorged money to individual complainants. Section 11(5) directs that amounts disgorged under a SEBI order go into the Investor Protection and Education Fund, which SEBI runs under its own regulations. The wrongdoer loses the gain. That does not mean it arrives in your account.</p>'
     '<p>And SEBI does not guarantee anyone. A SEBI registration means an intermediary met the eligibility conditions and is subject to SEBI\'s rules. It is not an endorsement of their advice, their returns or their solvency.</p>'

     '<h2>Common mistakes</h2>'
     '<ul>'
     '<li>Filing on SCORES before complaining to the entity. The system expects you to have approached them first, and a complaint filed cold usually comes straight back.</li>'
     '<li>Missing the 15-day review window. The clock runs from the date of the Action Taken Report, not from the day you get around to reading it.</li>'
     '<li>Expecting SCORES to award you money. It moves the entity to act. A monetary claim needs the SMART ODR route, and eventually arbitration.</li>'
     '<li>Paying an unregistered adviser because they showed screenshots of past returns. Making return or performance claims without SEBI\'s permission is exactly what the October 2024 circular targets.</li>'
     '<li>Filing an anonymous complaint. SCORES rejects them outright, so you gain nothing by leaving your name off.</li>'
     '<li>Going to a civil court against a SEBI order. Section 15Y shuts that door. The appeal lies to SAT, within 45 days.</li>'
     '</ul>'

     '<h2>Frequently asked questions</h2>'
     '<p><strong>Is filing a complaint on SCORES free?</strong> Yes. SCORES is SEBI\'s own platform and costs nothing to use. You do not need a lawyer to file, and you can track the complaint online.</p>'
     '<p><strong>How long does the entity have to respond to my SCORES complaint?</strong> 21 calendar days from receiving it. In that time it must resolve the complaint and upload an Action Taken Report. If it does not, the designated body takes up the matter for review.</p>'
     '<p><strong>Can SEBI get my trading losses back?</strong> No. SEBI regulates conduct in the securities market, not investment outcomes. If you lost money because a share fell, there is nothing to complain about. If you lost money because a broker misused your account or ignored your instructions, that is a genuine complaint, and the money claim goes through SMART ODR.</p>'
     '<p><strong>How do I check whether someone is SEBI registered?</strong> Ask for the registration number and look it up on SEBI\'s intermediary portal. If they collect payments from you, they should also have a UPI address ending in "@valid" followed by their bank name, and your app will show a thumbs-up in a green triangle when you pay it.</p>'
     '<p><strong>My complaint is against my bank, not a broker. Will SEBI handle it?</strong> No. Banking matters go to the Reserve Bank of India, insurance to IRDAI and pension to PFRDA. SCORES specifically excludes complaints falling under another regulator.</p>'
     '<p><strong>What is the fine if a company simply ignores my grievance?</strong> Section 15C covers this. Once SEBI has written to a listed company or registered intermediary asking it to redress a grievance, failure to do so in time costs Rs 1 lakh for each day it continues, capped at Rs 1 crore.</p>'
     '<p><strong>Can I appeal a SEBI order, and to whom?</strong> Yes. The appeal goes to the Securities Appellate Tribunal within 45 days of receiving the order, and from there to the Supreme Court within 60 days on a question of law. Civil courts have no jurisdiction, under Section 15Y.</p>'
     '<p><strong>Does a SEBI registration mean my adviser is trustworthy?</strong> It means they met SEBI\'s eligibility conditions and are bound by its rules, which is worth a lot when something goes wrong. It is not a guarantee of their advice or their returns.</p>'
     '<p><em>This article is for legal awareness and education only and is not investment advice. Timelines, thresholds and penalty figures are set by the SEBI Act and by SEBI circulars and can change; check the current position on sebi.gov.in before acting.</em></p>'),

]
