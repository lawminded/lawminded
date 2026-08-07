# Five articles filling gaps found by reading the existing 123 guides against
# recent statutory changes — NOT by SERP or keyword-volume analysis, which has
# not been run. Each targets a subject with real reader demand that no page here
# covered, chosen because the site can plausibly compete: specific statutory
# questions rather than head terms already owned by ClearTax and IndiaFilings.
#
# Verified against live sources on 7 August 2026: the Labour Codes commencement
# date, Section 114(4) of the Social Security Code, the FCRA 2020 amendment
# provisions, the DPDP Rules commencement schedule, and the POSH Act thresholds
# all checked out. Hedged language was replaced with the confirmed dates.
#
# Format matches the earlier seeds: (title, slug, category, act, read_time,
# summary, content). New slugs are inserted by seed_articles() on startup;
# existing rows are never overwritten.
BLOG_ARTICLES_5 = [

    # ── Gap 1: the Labour Codes came into force 21 Nov 2025 and created a
    #    statutory category that did not exist before. Coverage so far is law-firm
    #    client alerts written for employers; nothing addresses the worker.
    ('Gig and Platform Workers Under the Labour Codes: Your Rights, the Aggregator Levy and What Actually Changed',
     'gig-platform-workers-rights-labour-codes',
     'labour',
     'Code on Social Security, 2020',
     '8 min read',
     'India now recognises gig and platform workers in statute for the first time, with aggregators required to contribute towards their social security. What the law gives you, and what it still does not.',
     "<p><em>For years, delivery riders and cab drivers sat in a legal gap: not employees, not quite independent, and outside every social security law India had. The Code on Social Security closed part of that gap — but not the part most people assume.</em></p>"
     "<p><strong>Gig and platform workers are now a recognised statutory category, and aggregators must contribute 1-2% of annual turnover towards their social security. It does not make you an employee, and it does not give you PF, gratuity or notice pay.</strong></p>"
     "<p>India's four Labour Codes were brought into force on <strong>21 November 2025</strong>, replacing a tangle of older statutes. Most of the coverage focused on wages and working hours. The quieter change was that the <strong>Code on Social Security, 2020</strong> wrote gig and platform work into law for the first time — creating definitions, a funding mechanism, and a registration route where previously there was nothing at all.</p>"
     "<p>This guide sets out what that actually means if you drive, deliver, or take work through an app — and, just as importantly, what it does not mean.</p>"
     "<blockquote><p><strong>The bottom line</strong></p>"
     "<p>You are now a <em>recognised</em> category of worker with a statutory route to accident cover, health and maternity benefit, old-age protection and life and disability cover.</p>"
     "<p>You are <em>not</em> an employee. Provident fund, gratuity, notice period, minimum wage and unfair-dismissal protection still do not apply to you.</p>"
     "<p>The benefits arrive through government schemes funded by an aggregator levy — so how much you actually receive depends on schemes that are still being framed.</p></blockquote>"

     "<h2>Who counts as a gig worker, and who counts as a platform worker?</h2>"
     "<p>The Code draws a distinction that sounds academic but decides which rules reach you.</p>"
     "<p>A <strong>gig worker</strong> is a person who performs work or participates in a work arrangement and earns from it <em>outside a traditional employer-employee relationship</em>. That is deliberately wide — it catches anyone doing paid work who is not on a payroll.</p>"
     "<p>A <strong>platform worker</strong> is narrower and sits inside that first group: someone who accesses other organisations or individuals <em>through an online platform</em> to solve a specific problem or provide a service, in exchange for payment. A rider taking orders through a delivery app is a platform worker. A freelancer found through word of mouth is a gig worker but not a platform worker.</p>"
     "<p>The distinction matters because the funding obligation attaches to <strong>aggregators</strong> — digital intermediaries that connect a buyer with a seller or a service provider. The Code lists the aggregator categories in a schedule, covering ride-hailing, food and grocery delivery, logistics, e-marketplaces, professional services, healthcare, travel and hospitality, and content and media services.</p>"

     "<h2>The aggregator levy: 1-2% of turnover</h2>"
     "<p>This is the mechanism that makes the rest of it possible, and it is worth understanding precisely.</p>"
     "<p>Aggregators must contribute an amount between <strong>1% and 2% of their annual turnover</strong> towards social security for gig and platform workers. There is a ceiling: the contribution cannot exceed <strong>5% of the total amount payable by the aggregator to its gig and platform workers</strong>.</p>"
     "<p>Two features of that design are easy to miss:</p>"
     "<ul>"
     "<li>It is charged on <strong>turnover, not profit</strong>, so a loss-making aggregator still contributes. Turnover for this purpose excludes any tax, levy or cess paid to the Central Government.</li>"
     "<li>The 5% cap ties the levy back to what the platform actually pays workers, so a company with enormous turnover and few workers does not pay without limit.</li>"
     "</ul>"
     "<p>The money flows into a social security fund rather than to you directly. You do not receive a monthly credit the way an employee sees provident fund on a payslip. It funds the schemes described below.</p>"

     "<h2>What benefits does this actually buy?</h2>"
     "<p>The Code empowers the Central Government to frame schemes for gig and platform workers covering:</p>"
     "<ul>"
     "<li><strong>Life and disability cover</strong></li>"
     "<li><strong>Accident insurance</strong> — the most immediately relevant for anyone on a two-wheeler for eight hours a day</li>"
     "<li><strong>Health and maternity benefit</strong></li>"
     "<li><strong>Old age protection</strong></li>"
     "<li><strong>Creche facilities</strong></li>"
     "</ul>"
     "<p>Note the wording: the government <em>may frame</em> schemes. The Code builds the pipe and fills it with money; the benefits reach you through schemes notified separately. Several are at various stages of design, and state rules are still being issued unevenly. So the honest position in 2026 is that the funding obligation is real and the entitlement framework exists, while the individual benefits are arriving in stages.</p>"

     "<h2>Registration: the step you have to take yourself</h2>"
     "<p>Nothing reaches you automatically. To be eligible for any of these schemes you must be <strong>registered</strong>, and registration is on you rather than on the platform.</p>"
     "<p>Registration is done on the government portal on the basis of a self-declaration, using Aadhaar. The broad conditions are that you have completed 16 years of age and submit the required details electronically. Once registered, you receive a distinguishable identification number.</p>"
     "<p>If you work through more than one app — which most riders do — you register once as a worker, not once per platform.</p>"

     "<h2>What has <em>not</em> changed</h2>"
     "<p>This is where most of the confusion sits, and it is the part worth being clear-eyed about.</p>"
     "<p>Recognition as a gig or platform worker is <strong>not</strong> a finding that you are an employee. The Code creates a third category rather than moving you into the first. As things stand:</p>"
     "<ul>"
     "<li>There is <strong>no provident fund</strong> contribution of the kind an employee receives.</li>"
     "<li>There is <strong>no gratuity</strong>, which depends on continuous service under an employer.</li>"
     "<li>There is <strong>no notice period or retrenchment compensation</strong>. An app can deactivate your account without the process an employer would owe an employee.</li>"
     "<li><strong>Minimum wage guarantees</strong> attach to employment; per-order or per-trip earnings are not covered in the same way.</li>"
     "</ul>"
     "<p>Whether a particular arrangement is genuinely gig work or is really disguised employment is a question courts decide on the substance of the relationship — how much control the platform exercises, whether you can refuse work, whether you can substitute someone else — not on what the contract calls it. That question has not gone away; the Code sits alongside it.</p>"

     "<h2>Worked example</h2>"
     "<p>A delivery platform has annual turnover of ₹800 crore and pays ₹120 crore to its riders across the year.</p>"
     "<p>Its contribution obligation is 1-2% of ₹800 crore, so between <strong>₹8 crore and ₹16 crore</strong>. The cap is 5% of ₹120 crore, which is <strong>₹6 crore</strong>. The cap is lower, so the cap applies and the contribution is ₹6 crore.</p>"
     "<p>A rider on that platform who has not registered on the portal receives nothing from that ₹6 crore, because eligibility runs through registration. A rider who has registered becomes eligible for whichever schemes have been notified and apply to them.</p>"

     "<h2>Common mistakes</h2>"
     "<ul>"
     "<li><strong>Assuming the platform registers you.</strong> Aggregators have their own reporting duties, but your individual registration is yours to complete.</li>"
     "<li><strong>Reading recognition as employment.</strong> It is a distinct status with its own, narrower set of entitlements.</li>"
     "<li><strong>Expecting a visible monthly deduction or credit.</strong> The levy is on the aggregator's turnover and goes to a fund, not to a personal account.</li>"
     "<li><strong>Registering separately for each app.</strong> Registration is worker-level.</li>"
     "<li><strong>For aggregators — treating the 5% figure as the contribution rate.</strong> It is a ceiling on the 1-2% turnover charge, not the charge itself.</li>"
     "</ul>"

     "<h2>Checklist</h2>"
     "<ol>"
     "<li>Confirm whether you are a gig worker, a platform worker, or arguably an employee in substance.</li>"
     "<li>Register on the government portal with Aadhaar and keep the identification number safe.</li>"
     "<li>Keep your own record of trips, orders and earnings — you have no payslip to fall back on.</li>"
     "<li>Check which schemes have actually been notified for your category and state, since these are rolling out in stages.</li>"
     "<li>If you are an aggregator: identify your schedule category, compute 1-2% of turnover, apply the 5% cap, and check your state's rules.</li>"
     "</ol>"

     "<h2>FAQ</h2>"
     "<p><strong>Am I an employee now?</strong> No. The Code creates a separate recognised category. Employment status is still decided on the substance of the working relationship, not on this recognition.</p>"
     "<p><strong>Do I get provident fund?</strong> Not as a gig or platform worker. PF attaches to employment. The Code routes social security to you through schemes funded by the aggregator levy instead.</p>"
     "<p><strong>How much does the aggregator pay?</strong> Between 1% and 2% of its annual turnover, capped at 5% of what it pays its gig and platform workers.</p>"
     "<p><strong>Do I have to register?</strong> Yes, and it is the single most important step. Benefits run through registration on the government portal, using Aadhaar and a self-declaration.</p>"
     "<p><strong>I work on three different apps. Does that change anything?</strong> You register once as a worker rather than once per platform. Each aggregator carries its own contribution obligation separately.</p>"
     "<p><strong>Can an app deactivate me without notice?</strong> The Code does not create notice-period or unfair-dismissal protection for gig and platform workers. What your platform agreement says still governs, subject to general contract law.</p>"
     "<p><strong>When do the benefits actually start?</strong> The funding obligation is in force. Individual benefit schemes and state rules are being notified in stages through 2026, so check what applies in your state rather than assuming full coverage.</p>"

     "<h2>Key takeaways</h2>"
     "<ul>"
     "<li>Gig and platform workers are recognised in statute for the first time, in force from 21 November 2025.</li>"
     "<li>Aggregators contribute 1-2% of annual turnover, capped at 5% of what they pay their workers.</li>"
     "<li>The money funds government schemes for accident, health, maternity, old-age and disability cover.</li>"
     "<li>You must register yourself on the government portal — nothing is automatic.</li>"
     "<li>This is not employment: no PF, no gratuity, no notice pay, no minimum wage guarantee.</li>"
     "</ul>"),

    # ── Gap 2: Section 27 makes India an outlier, and readers arrive having read
    #    US/UK content that does not apply. Existing Indian coverage is written
    #    for lawyers, not for the person who just signed the contract.
    ('Are Non-Compete Clauses Enforceable in India After You Resign? Section 27 and What Courts Actually Do',
     'non-compete-clause-enforceability-india',
     'contracts',
     'Indian Contract Act, 1872',
     '8 min read',
     'A post-employment non-compete is void in India under Section 27 of the Contract Act, however reasonable it looks. What your employer can still enforce, and why the clause is in your contract anyway.',
     "<p><em>Almost every Indian employment contract contains a clause saying you will not join a competitor for six or twelve months after you leave. Almost every one of those clauses is unenforceable. Both things are true at the same time, and the gap between them is where people lose sleep they did not need to lose.</em></p>"
     "<p><strong>Under Section 27 of the Indian Contract Act, an agreement restraining anyone from exercising a lawful profession, trade or business is void to that extent. Indian courts do not apply a reasonableness test to post-employment non-competes the way English and American courts do.</strong></p>"
     "<p>This is one of the few areas where Indian law is markedly more employee-friendly than the systems people usually read about online. If you have been searching this question and finding articles about whether a restraint is \"reasonable in scope, geography and duration\", you have almost certainly been reading US or UK material. That test is not the Indian test.</p>"

     "<blockquote><p><strong>The bottom line</strong></p>"
     "<p>A clause stopping you joining a competitor <em>after</em> your employment ends is void, and courts will not rewrite it into something narrower.</p>"
     "<p>A restraint operating <em>during</em> employment — including a garden-leave period while you are still on the payroll — is generally valid.</p>"
     "<p>Confidentiality and IP-assignment obligations survive your exit and are enforceable. They protect information, not your ability to earn.</p></blockquote>"

     "<h2>What Section 27 actually says</h2>"
     "<p>The provision is unusually blunt for a statute drafted in 1872:</p>"
     "<blockquote><p>Every agreement by which any one is restrained from exercising a lawful profession, trade or business of any kind, is to that extent void.</p></blockquote>"
     "<p>Two words carry the weight. <strong>\"Every\"</strong> leaves no room for a judicial reasonableness exception — Parliament wrote a rule, not a standard. <strong>\"To that extent\"</strong> means the offending clause falls away while the rest of the contract survives; your whole employment agreement does not collapse because the non-compete is bad.</p>"
     "<p>The section contains one express exception, and it is not about employment: someone who <strong>sells the goodwill of a business</strong> may agree not to carry on a similar business within specified local limits, so long as those limits are reasonable. That is why non-competes in share purchase agreements and business sales stand on very different ground from the one in your offer letter.</p>"

     "<h2>The during-versus-after line</h2>"
     "<p>This is the distinction that decides almost every case.</p>"
     "<p>Indian courts have consistently held that a negative covenant operating <strong>during the term of employment</strong> is not a restraint of trade at all — it is part of what you agreed to do while being paid. An employee who has agreed to work exclusively for one employer can be held to that during the contract.</p>"
     "<p>Once the employment ends, the analysis flips. A covenant that restrains you <em>after</em> the relationship is over falls squarely within Section 27 and is void — and the Supreme Court has taken this position even where the restraint looked perfectly reasonable in duration and scope. Reasonableness is simply not the question the Indian court asks.</p>"
     "<p>Indian High Courts have continued to apply this position in recent employment disputes, including where a company sought to stop a departing employee joining a client or competitor. The consistent answer is that the employer's remedy lies in protecting its confidential information, not in blocking the person from working.</p>"

     "<h2>What your employer <em>can</em> still enforce</h2>"
     "<p>Section 27 kills the non-compete. It does not leave the employer without protection, and this is the part people miss.</p>"
     "<h3>Confidentiality</h3>"
     "<p>An obligation not to disclose or use trade secrets, customer data, pricing, source code or internal know-how is enforceable after you leave. It restrains what you may <em>do with specific information</em>, not whether you may work in your field. Courts draw that line firmly, and injunctions to protect genuinely confidential material are granted.</p>"
     "<h3>Intellectual property assignment</h3>"
     "<p>Work you created during employment generally belongs to the employer where the contract says so. Leaving does not change ownership.</p>"
     "<h3>Garden leave</h3>"
     "<p>If you remain on the payroll and are paid during a notice period while being kept away from work, that is a restraint during employment and is generally valid. Note the condition: you must actually still be employed and paid.</p>"
     "<h3>Non-solicitation</h3>"
     "<p>This is the genuinely unsettled area, so treat any confident answer with suspicion. Clauses preventing a departing employee from poaching former colleagues or approaching clients have been enforced in some cases and struck down in others, depending on how the court characterises the restraint and how the clause is drafted. A narrow, specific non-solicit is on better ground than a broad one, but nobody should promise you an outcome.</p>"

     "<h2>So why is the clause in my contract?</h2>"
     "<p>Three reasons, none of them legal strength.</p>"
     "<p><strong>Deterrence.</strong> Most people never test it. A clause that would fail in court works perfectly well if it stops you applying in the first place — which is exactly what it is designed to do.</p>"
     "<p><strong>Template inheritance.</strong> A great many Indian employment contracts are adapted from US or UK precedents where post-employment restraints are enforceable if reasonable. The clause is often there because nobody removed it.</p>"
     "<p><strong>Leverage.</strong> Even an unenforceable clause gives an employer something to point at in a negotiation over your exit, your notice period, or your final settlement.</p>"

     "<h2>Worked example</h2>"
     "<p>A product manager resigns from a SaaS company. Her contract says she will not join a competing business anywhere in India for twelve months. She has an offer from a direct competitor.</p>"
     "<p>The twelve-month post-employment restraint is void under Section 27, and a court will not narrow it to, say, three months or one city. She can take the job.</p>"
     "<p>What she cannot do is take the customer list, the pricing model or the product roadmap with her, or use them in the new role. If she does, the confidentiality obligation is enforceable and an injunction is a real possibility. The distinction is between competing — allowed — and using the former employer's confidential material to do it.</p>"
     "<p>If instead she had <em>sold her shareholding</em> in that company as part of a business sale and signed a non-compete in the share purchase agreement, the goodwill exception could apply and the restraint might well hold.</p>"

     "<h2>Common mistakes</h2>"
     "<ul>"
     "<li><strong>Applying the reasonableness test.</strong> It governs England and much of the United States. It does not govern a post-employment restraint in India.</li>"
     "<li><strong>Assuming the whole contract is void.</strong> Only the offending restraint falls away.</li>"
     "<li><strong>Treating confidentiality as equally unenforceable.</strong> It is not, and this is where departing employees actually get into trouble.</li>"
     "<li><strong>Confusing garden leave with a non-compete.</strong> Paid, still employed, kept away from work is valid. Unpaid, employment over is not.</li>"
     "<li><strong>Assuming a business-sale non-compete fails too.</strong> The goodwill exception is written into Section 27.</li>"
     "<li><strong>Signing a bond and assuming it is void.</strong> Training bonds requiring repayment of genuine training costs are analysed differently from restraints on working, and are sometimes upheld.</li>"
     "</ul>"

     "<h2>Checklist before you resign</h2>"
     "<ol>"
     "<li>Read the clause and separate it into its parts: non-compete, non-solicit, confidentiality, IP, notice, bond.</li>"
     "<li>Treat the post-employment non-compete as void, but the rest as live.</li>"
     "<li>Return every device, document and file. Do not forward work material to a personal account — this is the single most common way a defensible exit becomes an indefensible one.</li>"
     "<li>Check whether any period is garden leave, where you remain paid and still bound.</li>"
     "<li>Check for a training bond and what it actually claims to recover.</li>"
     "<li>If the employer sends a legal notice, take advice rather than reacting — an unenforceable clause is still capable of generating a lawsuit you have to answer.</li>"
     "</ol>"

     "<h2>FAQ</h2>"
     "<p><strong>Is a non-compete legally valid in India?</strong> A restraint operating after employment ends is void under Section 27 of the Indian Contract Act. A restraint operating during employment is generally valid.</p>"
     "<p><strong>What if the clause is only for three months and one city?</strong> Indian courts do not save a post-employment restraint by finding it reasonable. Duration and geography do not rescue it.</p>"
     "<p><strong>Can my employer sue me anyway?</strong> Yes. Being unenforceable does not stop a suit being filed or a notice being sent. It affects the outcome, not whether you are put to the trouble.</p>"
     "<p><strong>Is a non-solicitation clause enforceable?</strong> Genuinely unsettled. Courts have gone both ways depending on drafting and on how the restraint is characterised. Do not rely on either answer without advice.</p>"
     "<p><strong>Does this apply to consultants and freelancers too?</strong> Section 27 is not limited to employment — it applies to agreements restraining any lawful profession, trade or business.</p>"
     "<p><strong>What about a non-compete in a business sale?</strong> Different rules. The exception to Section 27 allows a seller of goodwill to accept reasonable local restrictions.</p>"
     "<p><strong>Can they withhold my final settlement over it?</strong> Withholding dues to enforce a void clause is not a strong position, but recovering them may take a demand and, if ignored, a claim.</p>"

     "<h2>Key takeaways</h2>"
     "<ul>"
     "<li>Section 27 voids post-employment non-competes, with no reasonableness exception.</li>"
     "<li>Restraints during employment, including paid garden leave, are generally valid.</li>"
     "<li>Confidentiality and IP obligations survive your exit and are enforced.</li>"
     "<li>Non-solicitation is contested — outcomes vary with drafting.</li>"
     "<li>The goodwill exception makes business-sale non-competes a different question entirely.</li>"
     "</ul>"),

    # ── Gap 3: two regulators, two statutes, one recurring confusion. Existing
    #    coverage is consultancy lead-gen; the site's FEMA articles are 100%
    #    inbound FDI and never touch foreign donations at all.
    ('FCRA vs FEMA: Which Law Applies to Foreign Money Coming Into India?',
     'fcra-vs-fema-foreign-funds-india',
     'fema',
     'FCRA, 2010 and FEMA, 1999',
     '8 min read',
     'FEMA governs foreign exchange; FCRA governs foreign donations. The test is whether the money is payment for something or a gift — and getting it wrong carries criminal, not just civil, consequences.',
     "<p><em>Two different laws, two different ministries, two completely different consequences for getting it wrong — and one question that decides which applies: was the money paid <strong>for</strong> something, or <strong>given</strong>?</em></p>"
     "<p><strong>FEMA governs foreign exchange transactions and is administered by the RBI under the Ministry of Finance. FCRA governs foreign contributions — donations and grants with nothing given in return — and is administered by the Ministry of Home Affairs.</strong></p>"
     "<p>The confusion is understandable. Both deal with money arriving from outside India. Both involve registration, designated bank accounts and reporting. But they sit under different ministries for a reason: FEMA is economic regulation, concerned with managing foreign exchange. FCRA is a security statute, concerned with who is funding activity inside India and why.</p>"
     "<p>That difference in purpose explains the difference in consequences. A FEMA contravention is civil, and there is a compounding route. An FCRA contravention can be criminal.</p>"

     "<blockquote><p><strong>The bottom line</strong></p>"
     "<p>Ask one question: <em>did the sender receive goods, services or any consideration in return?</em></p>"
     "<p><strong>Yes</strong> — it is a commercial transaction. FEMA territory. An export of services, consultancy income, investment.</p>"
     "<p><strong>No</strong> — it is a gift, grant or donation. FCRA territory, and you need FCRA registration or prior permission <em>before</em> the money arrives.</p></blockquote>"

     "<h2>The two statutes side by side</h2>"
     "<table class=\"prose-table\"><thead><tr><th></th><th>FEMA, 1999</th><th>FCRA, 2010</th></tr></thead><tbody>"
     "<tr><td><strong>Regulator</strong></td><td>RBI / Ministry of Finance</td><td>Ministry of Home Affairs</td></tr>"
     "<tr><td><strong>Governs</strong></td><td>Foreign exchange transactions</td><td>Foreign contribution — donations, gifts, grants</td></tr>"
     "<tr><td><strong>Purpose</strong></td><td>Managing foreign exchange and the external sector</td><td>National security and sovereignty</td></tr>"
     "<tr><td><strong>Typical user</strong></td><td>Businesses, investors, exporters, NRIs</td><td>NGOs, trusts, societies, Section 8 companies</td></tr>"
     "<tr><td><strong>Consideration flows back?</strong></td><td>Yes — payment for something</td><td>No — nothing given in return</td></tr>"
     "<tr><td><strong>Nature of breach</strong></td><td>Civil, compoundable</td><td>Can be criminal</td></tr>"
     "</tbody></table>"

     "<h2>What counts as \"foreign contribution\"</h2>"
     "<p>FCRA reaches the donation, delivery or transfer by a <strong>foreign source</strong> of any article, currency or security. The critical qualifier is that nothing of value passes back the other way.</p>"
     "<p>\"Foreign source\" is broader than most people expect. It includes foreign governments, foreign companies, international agencies (with some carve-outs), and citizens of other countries. A company registered in India but with majority foreign shareholding above the prescribed threshold can also be treated as a foreign source — which catches people out.</p>"
     "<p>Money received from a <strong>non-resident Indian who holds an Indian passport</strong> is generally <em>not</em> foreign contribution, because the person is an Indian citizen. The same money from someone who has taken foreign citizenship generally <em>is</em>. Citizenship, not residence, is the operative fact — a distinction worth checking before accepting a large donation from a relative abroad.</p>"

     "<h2>The case that causes the most trouble</h2>"
     "<p>An Indian NGO does research work for a foreign university and invoices it. The money arrives from abroad, into an organisation that also receives donations.</p>"
     "<p>That receipt is a <strong>fee for services rendered</strong>. Consideration flowed back — the research. It is therefore commercial income under FEMA, not foreign contribution, and it should not go anywhere near the FCRA account. Routing it there is itself a compliance problem.</p>"
     "<p>Reverse the facts. The same university gives the NGO a grant to run a literacy programme, expecting nothing back beyond reports on how the money was spent. Reporting obligations are not consideration. That is foreign contribution, and it requires FCRA registration or prior permission first.</p>"
     "<p>An organisation can lawfully receive both — but the two streams must be kept rigidly separate, in different bank accounts, with different reporting.</p>"

     "<h2>What FCRA compliance actually involves</h2>"
     "<p>There are two routes in.</p>"
     "<p><strong>Registration</strong> is the standard route for an organisation with a track record. The entity must have existed for <strong>three years</strong> and have spent at least <strong>Rs 15 lakh</strong> on its core activities for the benefit of society over the last three financial years. Registration is granted for a fixed term and must be renewed before it lapses.</p>"
     "<p><strong>Prior permission</strong> is the route for a newer organisation or a one-off receipt. It is tied to a specific donor, a specific amount and a specific purpose.</p>"
     "<p>The 2020 amendments tightened the regime considerably, and these are the provisions that trip up organisations working from older guidance:</p>"
     "<ul>"
     "<li>Foreign contribution must first be received into a <strong>designated FCRA account at the State Bank of India, New Delhi Main Branch, 11 Sansad Marg</strong> — the branch notified by the Central Government in October 2020 under the amended Section 17. Funds can be moved to another account for utilisation afterwards, but that first landing point is mandatory.</li>"
     "<li><strong>Administrative expenses are capped at 20%</strong> of foreign contribution received in a financial year — reduced from the earlier 50%.</li>"
     "<li><strong>Sub-granting is prohibited.</strong> An FCRA-registered organisation cannot pass foreign contribution on to another organisation, even one that is itself FCRA-registered. This broke a common funding model overnight.</li>"
     "<li>Aadhaar identification is required for office bearers and key functionaries.</li>"
     "</ul>"
     "<p>Certain categories of person are barred from accepting foreign contribution at all, including election candidates, judges, government servants, members of legislatures, and people connected with registered newspapers and broadcast media.</p>"

     "<h2>Worked example</h2>"
     "<p>A Section 8 company running education programmes has three inflows in a year:</p>"
     "<ol>"
     "<li><strong>₹40 lakh grant from a foreign foundation</strong> to run a school programme. No consideration back. Foreign contribution — FCRA applies, must land in the SBI New Delhi account, subject to the 20% administrative cap.</li>"
     "<li><strong>₹12 lakh from a foreign company</strong> for a commissioned impact-assessment report. Consideration flowed back. FEMA territory — ordinary export of services, and it must be kept out of the FCRA account.</li>"
     "<li><strong>₹5 lakh from a founder's brother, an Indian citizen working in Dubai.</strong> Indian passport, so generally not foreign contribution — but worth documenting the citizenship position on file.</li>"
     "</ol>"
     "<p>Put inflow 2 into the FCRA account and you have created a problem where none existed. Put inflow 1 into the ordinary account and the problem is considerably more serious.</p>"

     "<h2>Common mistakes</h2>"
     "<ul>"
     "<li><strong>Treating residence as the test.</strong> For NRI donations, the question is citizenship.</li>"
     "<li><strong>Mixing service income and grants in one account.</strong> The separation is not a formality.</li>"
     "<li><strong>Sub-granting to a partner NGO.</strong> Prohibited since 2020, regardless of the recipient's own registration.</li>"
     "<li><strong>Working from the old 50% administrative expense limit.</strong> It is 20%.</li>"
     "<li><strong>Missing the renewal window</strong> and continuing to receive funds on a lapsed registration.</li>"
     "<li><strong>Assuming an Indian-registered company is never a foreign source.</strong> Majority foreign ownership above the threshold can make it one.</li>"
     "<li><strong>Accepting funds while an application is pending.</strong> Prior permission means prior.</li>"
     "</ul>"

     "<h2>Checklist</h2>"
     "<ol>"
     "<li>For each inflow, ask whether the sender received anything in return.</li>"
     "<li>If nothing was given back, confirm the sender's status as a foreign source — for individuals, check citizenship rather than residence.</li>"
     "<li>Confirm FCRA registration or prior permission is in force <em>before</em> the money moves.</li>"
     "<li>Ensure foreign contribution lands first in the designated SBI New Delhi Main Branch account.</li>"
     "<li>Track administrative expenses against the 20% cap through the year, not at year end.</li>"
     "<li>Never sub-grant foreign contribution to another organisation.</li>"
     "<li>Keep commercial receipts entirely outside the FCRA account and report them under the ordinary tax and FEMA route.</li>"
     "<li>Diarise the renewal date well ahead of expiry.</li>"
     "</ol>"

     "<h2>FAQ</h2>"
     "<p><strong>What is the single difference between FCRA and FEMA?</strong> FEMA governs foreign exchange transactions where value flows both ways. FCRA governs foreign contributions where nothing is given in return.</p>"
     "<p><strong>Does my NGO need FCRA to invoice a foreign client?</strong> No. Fees for services are commercial receipts under FEMA. Keep them out of the FCRA account.</p>"
     "<p><strong>Is money from an NRI foreign contribution?</strong> Generally not, if the person holds an Indian passport. If they have taken foreign citizenship, it generally is.</p>"
     "<p><strong>Can I give FCRA funds to a partner NGO?</strong> No. Sub-granting foreign contribution has been prohibited since the 2020 amendments.</p>"
     "<p><strong>How much can I spend on salaries and overheads?</strong> Administrative expenses are capped at 20% of the foreign contribution received in a financial year.</p>"
     "<p><strong>Can a company receive foreign contribution?</strong> A Section 8 company can, with registration or prior permission. An ordinary trading company receiving investment or payment is in FEMA territory, not FCRA.</p>"
     "<p><strong>What happens if I get it wrong?</strong> FEMA breaches are civil and compoundable. FCRA breaches can attract cancellation of registration, prosecution and imprisonment, so the asymmetry matters.</p>"

     "<h2>Key takeaways</h2>"
     "<ul>"
     "<li>One question decides it: did anything of value flow back to the sender?</li>"
     "<li>FEMA is economic regulation under the RBI; FCRA is a security statute under the Home Ministry.</li>"
     "<li>Foreign contribution must land first in the designated SBI New Delhi Main Branch account.</li>"
     "<li>Administrative expenses are capped at 20%, and sub-granting is prohibited.</li>"
     "<li>For NRI donations, citizenship decides the answer, not where the person lives.</li>"
     "</ul>"),

    # ── Gap 4: the Act has been law since 2023 but was unenforceable without
    #    rules. The rules landed in Nov 2025 with a staggered commencement, and
    #    the existing DPDP articles all describe the Act, not the calendar.
    ('The DPDP Rules 2025: The Compliance Calendar and What You Must Do Before Each Deadline',
     'dpdp-rules-2025-compliance-timeline',
     'updates',
     'Digital Personal Data Protection Act, 2023',
     '7 min read',
     'The DPDP Act finally has rules, notified in November 2025 with a staggered commencement running into 2027. What bites now, what bites later, and what to build in the meantime.',
     "<p><em>The Digital Personal Data Protection Act was passed in August 2023 and then sat largely dormant, because a law that depends on rules cannot operate until the rules exist. They now do — and they arrive with a deliberately staggered commencement rather than a single switch.</em></p>"
     "<p><strong>The DPDP Rules were notified on 13 November 2025. A small set of provisions took effect immediately, Consent Manager registration opens on 13 November 2026, and the substantive compliance obligations bite on 13 May 2027.</strong></p>"
     "<p>That staggering is the most commercially useful fact in the whole regime, and it is the one most coverage skips. It means the enforcement date for the obligations that will actually cost you money is not today — but the work needed to meet them takes longer than the time remaining, which is why starting now matters.</p>"
     "<p>This guide is about the <em>calendar</em>. For what the Act itself requires, start with our DPDP Act compliance guide.</p>"

     "<blockquote><p><strong>The bottom line</strong></p>"
     "<p><strong>Phase 1 — 13 November 2025:</strong> Rules 1, 2 and 17 to 21. Definitions and the machinery of the Data Protection Board.</p>"
     "<p><strong>Phase 2 — 13 November 2026:</strong> Rule 4. Consent Manager registration and obligations.</p>"
     "<p><strong>Phase 3 — 13 May 2027:</strong> Rules 3, 5 to 16, 22 and 23. The substantive duties: notice, security safeguards, breach notification, retention limits, children's data, data principal rights.</p></blockquote>"

     "<h2>Phase 1: what took effect on 13 November 2025</h2>"
     "<p>The provisions that commenced on notification are structural rather than operational. They put the definitions in place and stand up the <strong>Data Protection Board of India</strong> — the adjudicating body that will eventually hear complaints and impose penalties.</p>"
     "<p>Nothing in this phase requires a business to change how it handles data. What it does is create the institution that will enforce the later phases, which is why it had to come first.</p>"

     "<h2>Phase 2: Consent Managers</h2>"
     "<p>On <strong>13 November 2026</strong>, one year after notification, Rule 4 brings the <strong>Consent Manager</strong> framework into force.</p>"
     "<p>A Consent Manager is a registered intermediary through which a person can give, manage, review and withdraw consent across different organisations from a single interface. It is one of the genuinely novel features of the Indian regime — there is no direct GDPR equivalent — and it exists because the Act runs almost entirely on consent rather than on multiple lawful bases.</p>"
     "<p>This phase matters directly if you intend to <em>become</em> a Consent Manager, since registration with the Board and the associated obligations begin here. For most businesses, the relevance is indirect: it is the point at which the plumbing for consent withdrawal starts to exist, and you should know whether you will interact with it.</p>"

     "<h2>Phase 3: the obligations that actually bite</h2>"
     "<p>This is the phase to plan for. On <strong>13 May 2027</strong> the substantive duties come into force together:</p>"
     "<ul>"
     "<li><strong>Notice.</strong> A clear, standalone, plain-language notice telling people what personal data you collect, for what purpose, how to withdraw consent, and how to complain — not a clause buried in terms of service.</li>"
     "<li><strong>Security safeguards.</strong> Reasonable technical and organisational measures, including encryption or comparable protection, access controls, logging, and contractual obligations on processors.</li>"
     "<li><strong>Breach notification.</strong> Intimation to affected individuals and to the Board, on the prescribed timelines — see our data breach guide for the mechanics.</li>"
     "<li><strong>Retention and erasure.</strong> Data deleted once the purpose is served, with specified retention periods for certain classes of large platform.</li>"
     "<li><strong>Data principal rights.</strong> Access, correction, erasure and grievance redressal, with a published route to exercise them and defined response timelines.</li>"
     "<li><strong>Children's data.</strong> Verifiable parental consent for anyone under 18, and prohibitions on tracking and targeted advertising directed at children.</li>"
     "<li><strong>Significant Data Fiduciaries.</strong> Additional duties for organisations notified as such — a Data Protection Officer based in India, independent audits and periodic impact assessments.</li>"
     "</ul>"
     "<p>Penalties under the Act run to substantial sums, with the highest bracket reaching <strong>₹250 crore</strong> for failure to take reasonable security safeguards.</p>"

     "<h2>What to do in the meantime</h2>"
     "<p>May 2027 sounds distant. It is not, because three of these tasks take longer than people expect and none can be done in the final month.</p>"
     "<p><strong>Build a data inventory.</strong> You cannot write an accurate notice, honour an erasure request or notify a breach if you do not know what personal data you hold, where it lives, who can reach it, and which vendors touch it. For most organisations this is the single largest piece of work in the whole programme, and it is entirely doable today.</p>"
     "<p><strong>Fix your consent capture.</strong> Consent under the Act must be free, specific, informed, unconditional and unambiguous, given by a clear affirmative action. Pre-ticked boxes and bundled consent do not qualify. Most existing Indian signup flows will need rebuilding, and rebuilding a signup flow is a product project, not a legal one.</p>"
     "<p><strong>Paper your processors.</strong> If a vendor processes personal data for you, the contract needs to reflect that. Renegotiating a supplier contract takes months.</p>"

     "<h2>Worked example</h2>"
     "<p>A 30-person Indian SaaS company holds email addresses, names, usage logs and support tickets for its customers' end users, and uses three sub-processors abroad.</p>"
     "<p><strong>Today:</strong> no operative obligation, but it begins mapping what it holds and where, and lists every vendor that touches personal data.</p>"
     "<p><strong>Over the following months:</strong> it rewrites its signup consent so it is specific and unbundled, builds a self-service route for access and deletion requests, sets a retention rule for support tickets, and adds data-processing terms to its three vendor contracts.</p>"
     "<p><strong>Before 13 May 2027:</strong> it publishes a standalone privacy notice, appoints someone accountable, and runs a tabletop exercise on breach notification so the first time it works out who calls the Board is not during an actual incident.</p>"
     "<p>Every one of those steps is available now. None depends on a further notification.</p>"

     "<h2>Common mistakes</h2>"
     "<ul>"
     "<li><strong>Reading May 2027 as \"not yet my problem\".</strong> The data inventory alone takes most organisations several months.</li>"
     "<li><strong>Assuming the Act is a copy of GDPR.</strong> It runs on consent rather than six lawful bases, and it has no direct equivalent of legitimate interests.</li>"
     "<li><strong>Treating the privacy policy as the notice.</strong> The Act contemplates a specific, standalone notice.</li>"
     "<li><strong>Overlooking the under-18 rule.</strong> India's threshold is 18, higher than in many other regimes, and it catches consumer apps that never thought of themselves as children's services.</li>"
     "<li><strong>Forgetting processors.</strong> Your obligations do not stop at your own systems.</li>"
     "<li><strong>Waiting for perfect clarity.</strong> Some operational detail will keep emerging; the inventory and consent work does not depend on it.</li>"
     "</ul>"

     "<h2>Checklist</h2>"
     "<ol>"
     "<li>Map every category of personal data you hold, its location, and who can access it.</li>"
     "<li>List every vendor and sub-processor that touches personal data.</li>"
     "<li>Audit consent capture — remove pre-ticked boxes and unbundle consents.</li>"
     "<li>Draft a standalone, plain-language notice separate from your terms.</li>"
     "<li>Build a route for access, correction and erasure requests, with an owner and a response time.</li>"
     "<li>Set retention periods per data category and a mechanism that actually deletes.</li>"
     "<li>Add data-processing terms to vendor contracts.</li>"
     "<li>Write and rehearse a breach response runbook.</li>"
     "<li>Check whether you handle under-18 data, and design verifiable parental consent if you do.</li>"
     "</ol>"

     "<h2>FAQ</h2>"
     "<p><strong>Is the DPDP Act in force now?</strong> The Act is law and the Rules were notified on 13 November 2025, but commencement is staggered. The substantive obligations arrive on 13 May 2027.</p>"
     "<p><strong>When exactly must I comply?</strong> 13 May 2027 for almost everything. The exception is Consent Manager registration, which opens a year earlier on 13 November 2026.</p>"
     "<p><strong>Does this apply to a small business?</strong> Yes. The Act does not carry a general small-business exemption, though Significant Data Fiduciary duties apply only to organisations notified as such.</p>"
     "<p><strong>Does it apply to companies outside India?</strong> It reaches processing outside India where that processing relates to offering goods or services to people in India.</p>"
     "<p><strong>What is a Consent Manager?</strong> A registered intermediary letting a person manage and withdraw consent across organisations from one place. Registration begins in the second phase.</p>"
     "<p><strong>What is the maximum penalty?</strong> The highest bracket under the Act reaches ₹250 crore, for failing to take reasonable security safeguards.</p>"
     "<p><strong>What single thing should I start with?</strong> The data inventory. Every other obligation depends on knowing what you hold.</p>"

     "<h2>Key takeaways</h2>"
     "<ul>"
     "<li>The Rules were notified on 13 November 2025 with a three-phase commencement.</li>"
     "<li>Phase 1 set up the Data Protection Board; Phase 2 covers Consent Managers; Phase 3 brings the substantive duties.</li>"
     "<li>The obligations that cost money land on 13 May 2027.</li>"
     "<li>The data inventory, consent redesign and vendor contracts take longer than the runway suggests.</li>"
     "</ul>"),

    # ── Gap 5: real statutory liability for very small employers, and the
    #    under-10 position (Local Committee, not IC) is almost never explained.
    ('POSH Compliance for Small Companies: Internal Committee Rules, the Under-10 Position and the ₹50,000 Penalty',
     'posh-internal-committee-small-company',
     'labour',
     'Sexual Harassment of Women at Workplace Act, 2013',
     '8 min read',
     'Ten or more employees means a mandatory Internal Committee with a specific composition. Fewer than ten does not mean the law stops applying — it means complaints go elsewhere.',
     "<p><em>Most small employers believe POSH is a large-company problem. It is not. The obligation to constitute an Internal Committee starts at ten employees, the composition is prescribed down to who may sit on it, and getting it wrong carries a fine plus something more damaging — an inquiry that a tribunal can set aside entirely.</em></p>"
     "<p><strong>Ten or more employees at a workplace means a mandatory Internal Committee. Below ten, there is no IC requirement, but complaints go to the district Local Committee and the employer's other duties continue to apply.</strong></p>"
     "<p>The Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013 applies to every workplace, not to companies above a size threshold. What the threshold decides is <em>where the complaint is heard</em>, not whether the law reaches you.</p>"

     "<blockquote><p><strong>The bottom line</strong></p>"
     "<p><strong>10 or more employees:</strong> constitute an Internal Committee with the prescribed composition, including a mandatory external member.</p>"
     "<p><strong>Fewer than 10:</strong> no IC, but a complaint goes to the Local Committee constituted by the District Officer, and your duties on prevention, awareness and assistance continue.</p>"
     "<p><strong>Either way:</strong> the count includes contract staff, interns, probationers and volunteers — not just people on your payroll.</p></blockquote>"

     "<h2>Counting to ten</h2>"
     "<p>This is where small employers most often get the answer wrong, because the Act's definition of \"employee\" is far broader than the payroll.</p>"
     "<p>It covers people engaged on a <strong>regular, temporary, ad hoc or daily wage basis</strong>, whether directly or through an agent or contractor, with or without the knowledge of the principal employer, for remuneration or <strong>on a voluntary basis</strong>, and whether the terms are express or implied. It expressly includes a <strong>co-worker, contract worker, probationer, trainee, apprentice</strong> or a person called by any other name.</p>"
     "<p>So a company with six people on the payroll, three contractors working from the office and two unpaid interns is at eleven, not six. The IC obligation is live.</p>"
     "<p>\"Workplace\" is similarly broad, extending to any place visited by the employee arising out of or during employment, including transport provided by the employer. Remote and hybrid arrangements do not remove the obligation.</p>"

     "<h2>Who must sit on the Internal Committee</h2>"
     "<p>The composition is prescribed, and a committee constituted incorrectly is a committee whose findings can be challenged.</p>"
     "<ul>"
     "<li><strong>A Presiding Officer</strong> — must be a <em>woman employed at a senior level</em> at the workplace. If no senior woman is available at that workplace, one may be nominated from another office, unit or workplace of the same employer.</li>"
     "<li><strong>At least two members from among the employees</strong> — preferably committed to the cause of women, or who have experience in social work, or legal knowledge.</li>"
     "<li><strong>One external member</strong> — from a non-governmental organisation or association committed to the cause of women, or a person familiar with issues relating to sexual harassment.</li>"
     "</ul>"
     "<p>Two further rules apply. <strong>At least one-half of the total members must be women.</strong> And members hold office for a term not exceeding <strong>three years</strong>.</p>"
     "<p>The external member is the requirement small companies most often skip, usually because it seems like an unnecessary expense for a ten-person office. It is not optional, and its absence is the easiest way for a respondent to challenge the entire inquiry later.</p>"

     "<h2>If you have fewer than ten employees</h2>"
     "<p>You do not constitute an IC. That is the only thing the threshold changes.</p>"
     "<p>A woman who wishes to complain approaches the <strong>Local Committee</strong>, which every District Officer is required to constitute for exactly this situation — small establishments, and cases where the complaint is against the employer themselves.</p>"
     "<p>Your remaining duties are unaffected. The employer must still provide a safe working environment, display the penal consequences of sexual harassment and the details of the Local Committee at a conspicuous place, organise awareness and orientation, assist the woman if she chooses to file a criminal complaint, and treat sexual harassment as misconduct under the service rules.</p>"
     "<p>Note the second limb above: even in a large company with a properly constituted IC, a complaint <em>against the employer</em> goes to the Local Committee, not the IC.</p>"

     "<h2>The timelines</h2>"
     "<p>These are short, and they are the ones committees miss.</p>"
     "<ul>"
     "<li><strong>Complaint:</strong> within three months of the incident, or of the last incident in a series. The committee may extend this by a further three months for recorded reasons.</li>"
     "<li><strong>Inquiry:</strong> completed within <strong>90 days</strong>.</li>"
     "<li><strong>Report:</strong> submitted to the employer within <strong>10 days</strong> of completing the inquiry.</li>"
     "<li><strong>Action:</strong> the employer acts on the recommendations within <strong>60 days</strong> of receiving the report.</li>"
     "<li><strong>Appeal:</strong> available to either party, generally within 90 days.</li>"
     "</ul>"
     "<p>Separately, the IC must file an <strong>annual report</strong> with the District Officer, and companies must disclose their POSH compliance in the Board's report.</p>"

     "<h2>What non-compliance costs</h2>"
     "<p>The direct penalty is a fine of up to <strong>₹50,000</strong> — for failing to constitute an IC, failing to act on recommendations, or failing to file the annual return.</p>"
     "<p>The consequences that actually hurt are the indirect ones. A <strong>repeat offence</strong> attracts twice the punishment and can lead to <strong>cancellation of the licence or registration</strong> required to conduct the business. And an inquiry conducted by a defectively constituted committee can be set aside, leaving the employer having dismissed someone on findings that no longer stand — a far more expensive outcome than the fine.</p>"

     "<h2>Worked example</h2>"
     "<p>A design studio has seven people on payroll, engages two contract illustrators who work from the studio three days a week, and hosts one intern.</p>"
     "<p>The headcount for POSH purposes is <strong>ten</strong>, so an IC is mandatory. The studio has four women, one of whom is a senior designer — she can be the Presiding Officer. Two more employees join as members, and the studio engages an external member from a local NGO working on women's issues, paid the prescribed fee per sitting.</p>"
     "<p>That gives a four-member committee, at least half women. It displays the penal consequences and the committee's details in the studio, runs an awareness session, and diarises the annual report.</p>"
     "<p>Had the studio counted only its seven payroll employees, it would have concluded no IC was needed — and been wrong, with the error surfacing at the worst possible moment.</p>"

     "<h2>Common mistakes</h2>"
     "<ul>"
     "<li><strong>Counting only payroll employees.</strong> Contractors, interns, trainees and volunteers all count.</li>"
     "<li><strong>Skipping the external member.</strong> The most common defect, and the easiest ground on which to challenge an inquiry.</li>"
     "<li><strong>Appointing a man as Presiding Officer.</strong> The Presiding Officer must be a woman employed at a senior level.</li>"
     "<li><strong>Letting the committee lapse.</strong> Members hold office for a maximum of three years; committees are frequently constituted once and forgotten.</li>"
     "<li><strong>Treating it as an HR process.</strong> The IC exercises powers of a civil court in respect of the inquiry; it is not an internal chat.</li>"
     "<li><strong>Assuming remote workers are outside the workplace.</strong> \"Workplace\" is defined broadly.</li>"
     "<li><strong>Routing a complaint against the employer to the IC.</strong> That goes to the Local Committee.</li>"
     "<li><strong>Forgetting the annual report</strong> to the District Officer.</li>"
     "</ul>"

     "<h2>Checklist</h2>"
     "<ol>"
     "<li>Count everyone — payroll, contract, agency, interns, trainees, volunteers.</li>"
     "<li>At ten or above, constitute the IC: senior woman as Presiding Officer, two or more employee members, one external member, at least half women.</li>"
     "<li>Record the constitution in writing with a defined term of not more than three years.</li>"
     "<li>Below ten, identify your District Officer's Local Committee and display its details.</li>"
     "<li>Display the penal consequences of sexual harassment conspicuously at the workplace.</li>"
     "<li>Adopt a written POSH policy and make sexual harassment misconduct under your service rules.</li>"
     "<li>Run awareness sessions and keep attendance records.</li>"
     "<li>Diarise the inquiry timelines and the annual report to the District Officer.</li>"
     "<li>Cover POSH compliance in the Board's report where applicable.</li>"
     "</ol>"

     "<h2>FAQ</h2>"
     "<p><strong>Does POSH apply to a company with five employees?</strong> Yes, the Act applies — but you do not constitute an IC. Complaints go to the district Local Committee, and your prevention, display and assistance duties continue.</p>"
     "<p><strong>Do interns and contractors count towards ten?</strong> Yes. The definition of employee covers contract workers, probationers, trainees, apprentices and people working on a voluntary basis.</p>"
     "<p><strong>Can a man chair the Internal Committee?</strong> No. The Presiding Officer must be a woman employed at a senior level at the workplace.</p>"
     "<p><strong>Is the external member really mandatory?</strong> Yes, and omitting them is the most common way an inquiry is later challenged.</p>"
     "<p><strong>How long does an inquiry take?</strong> It must be completed within 90 days, with the report to the employer within 10 days and action within 60 days.</p>"
     "<p><strong>What if the complaint is against the employer?</strong> It goes to the Local Committee rather than the IC.</p>"
     "<p><strong>What is the penalty for not having an IC?</strong> A fine up to ₹50,000, with a repeat offence attracting double the punishment and possible cancellation of the business licence or registration.</p>"
     "<p><strong>Does the Act cover men?</strong> The Act as enacted provides redress to women. Employers who wish to extend equivalent protection to all employees commonly do so through their internal policy, which is permitted but sits outside the statute.</p>"

     "<h2>Key takeaways</h2>"
     "<ul>"
     "<li>Ten or more employees means a mandatory Internal Committee; below ten, complaints go to the Local Committee.</li>"
     "<li>The headcount includes contractors, interns, trainees and volunteers.</li>"
     "<li>Composition is prescribed: senior woman as Presiding Officer, two employee members, one external member, at least half women.</li>"
     "<li>Inquiry in 90 days, report in 10, employer action in 60.</li>"
     "<li>₹50,000 fine, doubling on repeat, with possible cancellation of licence — and a defective committee can invalidate the entire inquiry.</li>"
     "</ul>"),

]
