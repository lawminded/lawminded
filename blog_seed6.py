# Three news-driven articles written 7 August 2026, each verified against live
# sources rather than model memory (MCA circulars, KPMG and Khaitan alerts,
# professional-firm commentary). Checked against the existing 126 published
# guides first — none of these three subjects was covered anywhere on the site.
#
# CCFS-2026 is deadline-bound: the scheme closes 31 August 2026. Once that date
# passes the article needs a retrospective edit, not deletion, since people will
# keep searching for what the scheme was.
#
# Format matches the earlier seeds: (title, slug, category, act, read_time,
# summary, content).
BLOG_ARTICLES_6 = [

    ('CCFS-2026: The MCA Scheme That Cuts Late-Filing Penalties by 90%, and Closes on 31 August',
     'ccfs-2026-companies-compliance-facilitation-scheme',
     'corp',
     'Companies Act, 2013',
     '9 min read',
     'The Companies Compliance Facilitation Scheme lets a company clear years of overdue ROC filings for 10% of the additional fees. Nearly 93,000 companies have used it. It shuts on 31 August 2026.',
     "<p><em>If your company has stopped filing with the Registrar at some point over the last few years, there is a window open right now that cuts the penalty by ninety per cent. It closes on 31 August 2026, and it is unlikely to come back.</em></p>"
     "<p><strong>Under CCFS-2026 a company pays normal filing fees plus only 10% of the accumulated additional fees on overdue annual forms. Dormant status costs half the usual fee, strike-off a quarter. The scheme ends 31 August 2026.</strong></p>"
     "<p>Additional fees under the Companies Act are the reason small lapses turn into large bills. They accrue daily, they do not stop, and there is no upper limit. A company that quietly skipped its AOC-4 and MGT-7 for three years can be looking at additional fees running into lakhs before anyone has issued a notice. The Ministry of Corporate Affairs opened the Companies Compliance Facilitation Scheme, 2026 to let those companies come back into compliance without the accumulated penalty deciding whether they can afford to.</p>"
     "<p>The response has been substantial. By 13 July 2026 the MCA reported that 92,859 companies had used the scheme, of which 92,826 were Indian companies and 33 were foreign companies. Another 11,829 had filed for strike-off under it and 99 had applied for dormant status.</p>"

     "<blockquote><p><strong>The bottom line</strong></p>"
     "<p><strong>What it costs:</strong> normal fees, plus 10% of the additional fees you would otherwise owe. A 90% reduction.</p>"
     "<p><strong>What it covers:</strong> overdue annual filings, not every form. Cost audit forms, LLP forms, DIR-3 KYC and DPT-3 are outside it.</p>"
     "<p><strong>What it does not fix:</strong> director disqualification under Section 164(2). That runs its five years regardless.</p></blockquote>"

     "<h2>Where the scheme comes from</h2>"
     "<p>The MCA notified CCFS-2026 through <strong>General Circular No. 01/2026 dated 24 February 2026</strong>, exercising its powers under Section 460 read with Section 403 of the Companies Act, 2013. The scheme came into force on 15 April 2026 and was originally to run until 15 July 2026.</p>"
     "<p>It was then extended. <strong>General Circular No. 03/2026 dated 8 July 2026</strong> pushed the closing date to <strong>31 August 2026</strong>. The reason was practical rather than generous: a fire at the MCA21 data centre on 5 June 2026 forced an unscheduled switchover to the disaster recovery site, and several MCA21 services were partly unavailable for days during the heaviest filing period of the year. The same episode moved the DPT-3 deadline for FY 2025-26 from 30 June to 31 July 2026 and extended a set of name reservations.</p>"
     "<p>That history matters for one reason. The extension was compensation for lost filing days, so treating it as a sign that further extensions will follow is a bad bet.</p>"

     "<h2>Which forms are covered</h2>"
     "<p>The scheme is built around annual filings. Under the Companies Act, 2013 it covers:</p>"
     "<ul>"
     "<li><strong>MGT-7 and MGT-7A</strong> — annual return, and the abridged return for small companies and OPCs</li>"
     "<li><strong>AOC-4</strong> and its variants, including the XBRL and CFS versions — financial statements</li>"
     "<li><strong>ADT-1</strong> — auditor appointment</li>"
     "<li><strong>FC-3 and FC-4</strong> — annual accounts and annual return of a foreign company</li>"
     "</ul>"
     "<p>Companies still carrying defaults from the previous statute are covered too. The old Companies Act, 1956 forms in scope include <strong>20B, 21A, 23AC, 23ACA, 66 and 23B</strong>, along with their XBRL versions. A company that stopped filing more than a decade ago is therefore not shut out.</p>"
     "<p>CSR-2 is handled through AOC-4 on the V3 portal, so it travels with the financial statements rather than separately.</p>"

     "<h2>Which forms are not covered</h2>"
     "<p>This is where most of the disappointment happens, so it is worth being blunt about it.</p>"
     "<ul>"
     "<li><strong>Cost audit forms</strong> — CRA-2 and CRA-4 are outside the scheme.</li>"
     "<li><strong>All LLP forms.</strong> CCFS-2026 is a companies scheme. Form 8 and Form 11 defaults get no relief, and no parallel LLP scheme has been notified. The last one was the LLP Settlement Scheme in 2020.</li>"
     "<li><strong>DIR-3 KYC and DPT-3</strong> do not appear in the eligible list.</li>"
     "<li>Filings for the current year that are not yet late, which need no relief anyway.</li>"
     "</ul>"

     "<h2>The three options, and what each costs</h2>"
     "<p>A company using the scheme is choosing between three destinations rather than one.</p>"
     "<p><strong>Option A: come back into compliance.</strong> File the overdue annual forms and pay normal fees plus 10% of the additional fees. This is the route for a company that intends to keep trading.</p>"
     "<p><strong>Option B: go dormant.</strong> File <strong>MSC-1</strong> at 50% of the normal fee. This suits a company that is not doing business now but that the owners want to keep alive, perhaps to hold a name or a future idea. Dormant status has its own continuing obligations, so it is a change of gear rather than a stop.</p>"
     "<p><strong>Option C: close it.</strong> File <strong>STK-2</strong> at 25% of the applicable fee. For a company nobody is using and nobody intends to use, this is usually the honest answer, and abandoning a company without striking it off leaves the directors exposed rather than free.</p>"

     "<h2>What immunity you actually get</h2>"
     "<p>The scheme grants immunity from penalty under Section 454(3) for defaults relating to Sections 92 and 137, which are the annual return and the financial statement filings. There is no separate immunity form. Filing the overdue form under the scheme is what triggers it.</p>"
     "<p>The immunity has edges, and they are sharp:</p>"
     "<ul>"
     "<li>You get it if you file <strong>before</strong> an adjudicating officer issues a notice, or <strong>within 30 days</strong> of such a notice.</li>"
     "<li>You do not get it if an <strong>adjudication order has already been passed</strong>.</li>"
     "<li>You do not get it if a <strong>prosecution has already been filed</strong>, or where adjudication proceedings began before you filed.</li>"
     "<li>For ADT-1 and the FC forms, immunity depends on no prosecution or show-cause notice having come first.</li>"
     "</ul>"
     "<p>So the value of the scheme falls sharply the moment the department moves first. If a notice has landed on your desk, the thirty-day clock is the whole game.</p>"

     "<h2>Who cannot use it</h2>"
     "<p>Five categories are excluded:</p>"
     "<ol>"
     "<li>Companies where the Registrar has already issued the final strike-off notice in <strong>Form STK-7</strong>.</li>"
     "<li>Companies with a strike-off application already pending.</li>"
     "<li>Companies with a dormant status application already pending.</li>"
     "<li>Companies being dissolved through amalgamation.</li>"
     "<li>Companies identified as vanishing companies.</li>"
     "</ol>"

     "<h2>The thing the scheme does not do</h2>"
     "<p>A director disqualified under Section 164(2) for failing to file financial statements or annual returns for three continuous financial years stays disqualified for the full five years. Using CCFS-2026 does not shorten that, reverse it, or wipe the record.</p>"
     "<p>The scheme is financial relief. It reduces what you pay. It does not restore a director to eligibility, and anyone selling it as a way to fix a disqualification is describing something the circular does not say.</p>"

     "<h2>How to actually use it</h2>"
     "<p>There is no application form for the scheme itself, which surprises people who go looking for one. You file the overdue form the normal way on the MCA-21 V3 portal, and the reduced fee is calculated automatically at the payment stage.</p>"
     "<p>The practical sequence for a company with several years of backlog:</p>"
     "<ol>"
     "<li>Pull the company's filing history from the MCA portal and list exactly which forms are missing, for which years.</li>"
     "<li>Get the accounts for those years audited and adopted. This is the step that takes real time, and it is the reason a company that starts on 25 August will not finish.</li>"
     "<li>Hold the board meetings and general meetings the filings depend on, and record the minutes properly.</li>"
     "<li>File in chronological order — the older years first, because later filings often depend on the earlier ones going through.</li>"
     "<li>Check the fee shown at payment reflects the 10% figure before you pay.</li>"
     "</ol>"

     "<h2>Worked example</h2>"
     "<p>A private limited company last filed for FY 2020-21. It has missed AOC-4 and MGT-7 for four financial years, and ADT-1 twice.</p>"
     "<p>Additional fees on a delay of this length run at Rs 100 per day per form with no ceiling. On ten overdue forms with delays stretching past a thousand days on the oldest, the additional fees alone are comfortably into several lakhs.</p>"
     "<p>Under the scheme the company pays the normal fee on each form, plus <strong>10%</strong> of that additional-fee figure. If the additional fees came to Rs 6,00,000, it pays Rs 60,000 of them.</p>"
     "<p>What the company still has to do is get four years of accounts audited and adopted before it can file anything. That is weeks of work, not days, which is why the useful deadline is not 31 August but whatever date the auditor needs to start.</p>"

     "<h2>Common mistakes</h2>"
     "<ul>"
     "<li><strong>Assuming LLPs are covered.</strong> They are not, and the list of eligible forms contains no LLP form.</li>"
     "<li><strong>Waiting for another extension.</strong> The July extension replaced days lost to the data centre fire. That reason has expired.</li>"
     "<li><strong>Starting in the last week.</strong> The audit and adoption work sits ahead of the filing, and no scheme shortens it.</li>"
     "<li><strong>Reading it as a disqualification amnesty.</strong> Section 164(2) is untouched.</li>"
     "<li><strong>Ignoring a notice already received</strong>, when responding inside 30 days is the difference between immunity and none.</li>"
     "<li><strong>Filing out of order</strong>, when later years frequently depend on earlier filings being accepted first.</li>"
     "<li><strong>Choosing Option A for a company nobody will use again</strong>, when strike-off at 25% is cheaper and ends the obligation.</li>"
     "</ul>"

     "<h2>FAQ</h2>"
     "<p><strong>What is the last date for CCFS-2026?</strong> 31 August 2026, extended from 15 July 2026 by General Circular No. 03/2026.</p>"
     "<p><strong>How much do I actually save?</strong> You pay 10% of the additional fees instead of 100%, so the saving is 90% of the penalty component. Normal filing fees are unchanged.</p>"
     "<p><strong>Does it cover LLPs?</strong> No. It applies to companies only, and there is no LLP equivalent notified for 2026.</p>"
     "<p><strong>Do I need to submit a separate application?</strong> No. File the overdue form on MCA-21 V3 and the reduced fee is applied at the payment stage.</p>"
     "<p><strong>Will it remove my director disqualification?</strong> No. Disqualification under Section 164(2) runs its five-year course independently.</p>"
     "<p><strong>An adjudication order has already been passed against my company. Can I still use it?</strong> You can still file and pay the reduced fee, but the immunity from penalty is not available once an order has been passed.</p>"
     "<p><strong>My company received a strike-off notice in STK-7. Am I eligible?</strong> No. A final strike-off notice puts the company outside the scheme.</p>"
     "<p><strong>Can I use it to close a company instead of reviving it?</strong> Yes, through STK-2 at 25% of the applicable fee, which is often the sensible answer for a company nobody intends to trade again.</p>"),

    ('The Income-tax Act, 2025 Is Now in Force: What Changed on 1 April 2026, and What Did Not',
     'income-tax-act-2025-what-changed',
     'tax',
     'Income-tax Act, 2025',
     '8 min read',
     'India replaced its 1961 income tax law on 1 April 2026. The "tax year" now does the work of both previous year and assessment year. Most of what you owe did not change.',
     "<p><em>India has been taxing income under the same statute since 1961. On 1 April 2026 that ended. The replacement is shorter, renumbered and reorganised, and the most common question about it has an unsatisfying answer: for most taxpayers, the amount owed is much the same.</em></p>"
     "<p><strong>The Income-tax Act, 2025 replaced the Income-tax Act, 1961 with effect from 1 April 2026. Its headline change is drafting, not rates: a single \"tax year\" now replaces both \"previous year\" and \"assessment year\".</strong></p>"
     "<p>The 1961 Act had grown to more than 800 sections after six decades of amendment, layered with provisos, explanations and clauses that referred to other clauses. The 2025 Act reorganises the same subject matter into <strong>536 sections across 23 chapters</strong>, with the word count cut by roughly half. Tables and formulas replace long descriptive passages in many places.</p>"
     "<p>This is a rewrite of how the law is expressed. It is worth being clear about that up front, because a lot of coverage has implied a change in what you pay.</p>"

     "<blockquote><p><strong>The bottom line</strong></p>"
     "<p><strong>Changed:</strong> terminology, section numbers, chapter structure, and how TDS provisions are organised.</p>"
     "<p><strong>Unchanged:</strong> the 1 April to 31 March cycle, and the substantive basis on which most income is taxed.</p>"
     "<p><strong>Still governed by the old Act:</strong> anything relating to AY 2024-25 and earlier, including pending litigation.</p></blockquote>"

     "<h2>The tax year, and why the change is smaller than it sounds</h2>"
     "<p>Under the old law you dealt with two years at once. Income earned in the <strong>previous year</strong> 2024-25 was taxed in the <strong>assessment year</strong> 2025-26. Getting the two the wrong way round on a form was one of the most common filing errors in the country.</p>"
     "<p>Section 3 of the 2025 Act collapses them. There is now one <strong>tax year</strong>, running 1 April to 31 March, covering both the earning and the assessment of that income.</p>"
     "<p>What has not moved is the calendar itself. The year still starts on 1 April and ends on 31 March, and the term \"financial year\" survives elsewhere in the legislation. So the change is that you stop translating between two labels, not that any date shifts.</p>"
     "<p>The mapping is worth keeping somewhere you can find it. Tax year 2024-25 under the new Act corresponds to previous year 2024-25 under the old Act, which corresponds to assessment year 2025-26. The new terminology applies from <strong>tax year 2026-27</strong> onward and does not reach back to income earned before 1 April 2026.</p>"

     "<h2>What happened to the section numbers you know</h2>"
     "<p>Every section number you have memorised has moved. Section 80C, Section 143(1), Section 194 — the concepts survive, the numbers do not.</p>"
     "<p>The chapter structure gives a rough map of where things went:</p>"
     "<table class=\"prose-table\"><thead><tr><th>Subject</th><th>1961 Act</th><th>2025 Act</th></tr></thead><tbody>"
     "<tr><td>Charging provisions</td><td>Chapters I-II</td><td>Chapters I-II</td></tr>"
     "<tr><td>Heads of income</td><td>Chapter IV, scattered</td><td>Chapter III, consolidated</td></tr>"
     "<tr><td>Deductions</td><td>Chapters VI, VI-A</td><td>Chapters IV-V</td></tr>"
     "<tr><td>TDS and TCS</td><td>Chapter XVII</td><td>Chapter VII</td></tr>"
     "<tr><td>Assessment</td><td>Chapter XIV</td><td>Chapter VIII</td></tr>"
     "<tr><td>Appeals</td><td>Chapter XX</td><td>Chapter XI</td></tr>"
     "<tr><td>Penalties</td><td>Chapter XXI</td><td>Chapter XII</td></tr>"
     "</tbody></table>"
     "<p>The TDS move is the one that changes daily work. Under the old Act the deduction provisions were spread across a long run of sections in the 190s and beyond, each with its own threshold and rate, and finding the right one meant knowing where to look. The 2025 Act pulls them into a single structured chapter with the rates and thresholds tabulated.</p>"

     "<h2>Does sixty years of case law still apply?</h2>"
     "<p>Largely, yes, and this is the question professionals asked first.</p>"
     "<p>Where a substantive provision has been carried into the new Act without a change in meaning, judicial precedent decided under the old provision continues to apply. A rewrite that renumbers a section without altering what it does should not disturb the interpretation courts have already settled.</p>"
     "<p>The caution is that \"without a change in meaning\" does the heavy lifting in that sentence. Where the 2025 Act has compressed several provisos into a table or restated a passage in different words, whether the meaning survived intact is a question that will take some years and some litigation to answer. Anyone relying on a fine point of an old judgment should check the new wording rather than assume.</p>"

     "<h2>The transition, in practical terms</h2>"
     "<p>Two statutes are running side by side for a while, and which one applies depends on the year the income belongs to.</p>"
     "<ul>"
     "<li><strong>AY 2024-25 and earlier:</strong> the 1961 Act governs, including any assessment, appeal or litigation still pending.</li>"
     "<li><strong>From 1 April 2026:</strong> the 2025 Act governs.</li>"
     "<li>The <strong>Income-tax Rules, 2026</strong> replace the 1962 Rules from the same date, with the old Rules continuing to apply to the earlier years.</li>"
     "</ul>"
     "<p>So a notice you receive in 2026 about AY 2023-24 is a 1961 Act notice, and answering it means working with the old section numbers.</p>"

     "<h2>What this does not change</h2>"
     "<p>Slab rates and the choice between tax regimes are set by the annual Finance Act, not by this restructuring. The 2025 Act is the machinery; the rates are decided each year as before. If your tax bill moved this year, look to the Finance Act and to the new Rules rather than to the new statute.</p>"
     "<p>The compliance calendar is also broadly intact. Advance tax instalments, TDS deposit dates and the general shape of the filing year continue as they were.</p>"

     "<h2>Worked example</h2>"
     "<p>A salaried taxpayer filing in 2026 for income earned between April 2025 and March 2026 is dealing with the old regime: previous year 2025-26, assessment year 2026-27, under the 1961 Act.</p>"
     "<p>Income earned from 1 April 2026 onward falls into <strong>tax year 2026-27</strong> under the new Act, with no separate assessment year to name.</p>"
     "<p>For a year or so the two vocabularies overlap, which is exactly the period in which people file under the wrong label. The safest habit is to state the actual dates — \"income earned in the year ending 31 March 2027\" — rather than the shorthand.</p>"

     "<h2>Common mistakes</h2>"
     "<ul>"
     "<li><strong>Expecting a lower tax bill.</strong> The Act restructures the law; the Finance Act sets the rates.</li>"
     "<li><strong>Assuming old section numbers still work.</strong> They do not, and quoting Section 80C in a 2026-27 filing context will not match the statute.</li>"
     "<li><strong>Treating old case law as void.</strong> Precedent survives where the substantive provision was carried over unchanged.</li>"
     "<li><strong>Applying the new Act to an old year.</strong> Anything from AY 2024-25 or earlier stays under the 1961 Act.</li>"
     "<li><strong>Assuming the year dates moved.</strong> The tax year still runs 1 April to 31 March.</li>"
     "<li><strong>Forgetting the Rules changed too.</strong> The Income-tax Rules, 2026 replaced the 1962 Rules on the same date and carry real changes of their own.</li>"
     "</ul>"

     "<h2>FAQ</h2>"
     "<p><strong>When did the Income-tax Act, 2025 come into force?</strong> 1 April 2026, replacing the Income-tax Act, 1961.</p>"
     "<p><strong>What is a tax year?</strong> The twelve months from 1 April to 31 March, defined in Section 3. It replaces both \"previous year\" and \"assessment year\".</p>"
     "<p><strong>Did tax rates change?</strong> Not through this Act. Rates come from the annual Finance Act, as they always have.</p>"
     "<p><strong>How many sections does the new Act have?</strong> 536, across 23 chapters, against more than 800 in the 1961 Act.</p>"
     "<p><strong>Is old case law still valid?</strong> Where the provision was carried over without a change in meaning, yes. Where the drafting changed materially, expect argument.</p>"
     "<p><strong>Which Act applies to my pending appeal for AY 2022-23?</strong> The 1961 Act. The old law continues to govern earlier years.</p>"
     "<p><strong>Do I file my return differently?</strong> The filing mechanics are broadly familiar. The terminology on the forms is what changed, along with the Rules sitting underneath them.</p>"),

    ('New Perquisite Rules from April 2026: Company Car Tax Nearly Triples, HRA Extends to Four More Cities',
     'perquisite-valuation-rules-2026-salaried',
     'tax',
     'Income-tax Rules, 2026',
     '8 min read',
     'The Income-tax Rules, 2026 revalued almost every salary perk from 1 April 2026. Meal vouchers and education allowances rose sharply in your favour. The company car went the other way.',
     "<p><em>Some of these figures had not moved since the early 2000s. A children's education allowance exempt at Rs 100 a month was a real benefit when it was set and a rounding error by 2026. The Income-tax Rules, 2026 finally repriced the lot, and the direction of travel is not the same for every item.</em></p>"
     "<p><strong>From 1 April 2026 the taxable value of an employer-provided car rose from Rs 1,800 to Rs 5,000 a month for smaller cars and from Rs 2,400 to Rs 7,000 for larger ones. Meal vouchers, education and hostel allowances moved sharply the other way, in your favour. Four more cities now qualify for the 50% HRA exemption.</strong></p>"
     "<p>These are valuation rules. They do not change your salary or your slab; they change what portion of a non-cash benefit is treated as income in your hands. For anyone with a company car and a driver, the arithmetic got noticeably worse. For anyone with school-age children and a meal card, it got better.</p>"

     "<blockquote><p><strong>The bottom line</strong></p>"
     "<p>Company car with chauffeur: the monthly taxable value roughly quadrupled once the chauffeur component is included.</p>"
     "<p>Children's education allowance: Rs 100 to Rs 3,000 per child per month. Hostel allowance: Rs 300 to Rs 9,000.</p>"
     "<p>HRA at 50% of basic now reaches Ahmedabad, Bengaluru, Hyderabad and Pune, alongside the four original metros.</p></blockquote>"

     "<h2>The company car, in numbers</h2>"
     "<p>This is the change people noticed first, because it is the one that costs money.</p>"
     "<p>Where the employer owns or hires the car and <strong>meets the running expenses</strong>:</p>"
     "<table class=\"prose-table\"><thead><tr><th>Car</th><th>Old value</th><th>New value</th></tr></thead><tbody>"
     "<tr><td>Up to 1.6 litres, or electric</td><td>Rs 1,800 / month</td><td>Rs 5,000 / month</td></tr>"
     "<tr><td>Above 1.6 litres</td><td>Rs 2,400 / month</td><td>Rs 7,000 / month</td></tr>"
     "<tr><td>Chauffeur, added to either</td><td>Rs 900 / month</td><td>Rs 3,000 / month</td></tr>"
     "</tbody></table>"
     "<p>Where the employer provides the car but the <strong>employee meets the running expenses</strong>:</p>"
     "<table class=\"prose-table\"><thead><tr><th>Car</th><th>Old value</th><th>New value</th></tr></thead><tbody>"
     "<tr><td>Up to 1.6 litres, or electric</td><td>Rs 600 / month</td><td>Rs 2,000 / month</td></tr>"
     "<tr><td>Above 1.6 litres</td><td>Rs 900 / month</td><td>Rs 3,000 / month</td></tr>"
     "<tr><td>Chauffeur, added to either</td><td>Rs 900 / month</td><td>Rs 3,000 / month</td></tr>"
     "</tbody></table>"
     "<p>An employee with a large company car and a driver, fully expensed, goes from Rs 3,300 a month of taxable perquisite to Rs 10,000. Over a year that is Rs 1,20,000 added to taxable income instead of Rs 39,600. At a 30% marginal rate the extra tax is roughly Rs 24,000 a year.</p>"
     "<p>Note that electric vehicles sit in the lower bracket alongside cars up to 1.6 litres, whatever their actual power.</p>"

     "<h2>The changes that go in your favour</h2>"
     "<p>Most of the other revisions raised exemption limits that inflation had made meaningless.</p>"
     "<table class=\"prose-table\"><thead><tr><th>Benefit</th><th>Old limit</th><th>New limit</th></tr></thead><tbody>"
     "<tr><td>Children's education allowance</td><td>Rs 100 / month per child</td><td>Rs 3,000 / month per child</td></tr>"
     "<tr><td>Children's hostel allowance</td><td>Rs 300 / month per child</td><td>Rs 9,000 / month per child</td></tr>"
     "<tr><td>Free or subsidised education</td><td>Rs 1,000 / month per child</td><td>Rs 3,000 / month per child</td></tr>"
     "<tr><td>Meal vouchers</td><td>Rs 50 per meal</td><td>Rs 200 per meal</td></tr>"
     "<tr><td>Gifts and vouchers</td><td>Rs 5,000 / year</td><td>Rs 15,000 / year</td></tr>"
     "<tr><td>Transport allowance</td><td>Rs 10,000</td><td>Rs 25,000, or 70%, whichever is lower</td></tr>"
     "<tr><td>Interest-free loan, specified medical treatment</td><td>Rs 20,000</td><td>Rs 2,00,000</td></tr>"
     "</tbody></table>"
     "<p>The meal voucher change is the one most employees will feel monthly. At Rs 50 per meal the exemption covered almost nothing in a metro; at Rs 200 it covers a real lunch.</p>"
     "<p>The education allowance moving from Rs 100 to Rs 3,000 per child per month is a thirtyfold increase, which tells you how long it had been left alone.</p>"

     "<h2>HRA: four cities join the 50% list</h2>"
     "<p>House rent allowance exemption is the lowest of three figures: the actual HRA received, the rent paid minus 10% of salary, or a percentage of salary that depends on where you live.</p>"
     "<p>That last percentage was <strong>50% for Delhi, Mumbai, Kolkata and Chennai</strong> and 40% everywhere else, a list that had not been revisited as other cities grew and their rents with them.</p>"
     "<p>The 2026 Rules add <strong>Ahmedabad, Bengaluru, Hyderabad and Pune</strong> to the 50% group. An employee renting in Bengaluru can now compute the exemption on 50% of basic salary rather than 40%, which on a Rs 12,00,000 basic is a Rs 1,20,000 difference in the ceiling before the other two limbs are applied.</p>"
     "<p>The declaration you give your employer now also asks you to state your <strong>relationship with the landlord</strong>. Rent paid to a parent or spouse has always attracted scrutiny where the arrangement was not genuine; the form now asks the question directly rather than leaving it to be discovered.</p>"

     "<h2>Worked example</h2>"
     "<p>An employee in Bengaluru has basic salary of Rs 12,00,000 a year, pays Rs 30,000 a month in rent, has two children in school, uses a meal card, and drives a company-provided 1.4 litre car with a chauffeur, fully expensed.</p>"
     "<p><strong>Car:</strong> Rs 5,000 plus Rs 3,000 for the chauffeur is Rs 8,000 a month, so Rs 96,000 of taxable perquisite for the year. Under the old rules that was Rs 2,700 a month, or Rs 32,400. An extra Rs 63,600 in taxable income.</p>"
     "<p><strong>Education allowance:</strong> two children at Rs 3,000 a month each is Rs 72,000 a year exempt, against Rs 2,400 previously.</p>"
     "<p><strong>Meal card:</strong> at Rs 200 a meal for around 22 working days, roughly Rs 4,400 a month exempt instead of Rs 1,100.</p>"
     "<p><strong>HRA:</strong> the salary-based ceiling rises from Rs 4,80,000 to Rs 6,00,000. Whether that helps depends on the other two limbs, since rent of Rs 3,60,000 minus 10% of salary gives Rs 2,40,000, and the exemption is the lowest of the three.</p>"
     "<p>On these facts the education and meal changes roughly offset the car increase. Change the car to a 2 litre model and the balance tips the other way.</p>"

     "<h2>What to do about it</h2>"
     "<ol>"
     "<li>Ask your payroll team which perquisite values they are applying from April 2026, since some systems were slow to update.</li>"
     "<li>If you have a company car, work out the annual cost at the new valuation before renewing the arrangement. A cash allowance may now be cheaper for you.</li>"
     "<li>Claim the education and hostel allowances if you have children and were ignoring a Rs 100 limit as not worth the paperwork. At Rs 3,000 it is.</li>"
     "<li>Check whether your meal card limit was set at the old Rs 50 and ask for it to be revised.</li>"
     "<li>If you rent in Ahmedabad, Bengaluru, Hyderabad or Pune, make sure your employer is computing HRA at 50%.</li>"
     "<li>Keep rent receipts and the landlord's PAN where required, and answer the landlord-relationship question honestly.</li>"
     "</ol>"

     "<h2>Common mistakes</h2>"
     "<ul>"
     "<li><strong>Assuming the car perquisite is still Rs 1,800.</strong> It is the single largest increase in the set.</li>"
     "<li><strong>Treating an electric car as exempt.</strong> It sits in the lower bracket, which is not the same as nil.</li>"
     "<li><strong>Forgetting the chauffeur component,</strong> which more than tripled on its own.</li>"
     "<li><strong>Leaving education and hostel allowances unclaimed</strong> out of habit from when they were negligible.</li>"
     "<li><strong>Assuming your city is on the 50% HRA list.</strong> Eight cities qualify now, not all large ones.</li>"
     "<li><strong>Overstating rent paid to a relative,</strong> when the declaration now asks about the relationship directly.</li>"
     "<li><strong>Expecting these to apply under the new tax regime,</strong> when several exemptions of this kind are tied to the old regime. Check which regime you are in before planning around them.</li>"
     "</ul>"

     "<h2>FAQ</h2>"
     "<p><strong>When did the new perquisite values take effect?</strong> 1 April 2026, with the Income-tax Rules, 2026.</p>"
     "<p><strong>How much is a company car taxed at now?</strong> Rs 5,000 a month up to 1.6 litres or electric, Rs 7,000 above that, plus Rs 3,000 if a chauffeur is provided, where the employer meets running costs.</p>"
     "<p><strong>Are electric cars treated better?</strong> They fall in the lower bracket with cars up to 1.6 litres, rather than being exempt.</p>"
     "<p><strong>Which cities get 50% HRA now?</strong> Delhi, Mumbai, Kolkata and Chennai, joined by Ahmedabad, Bengaluru, Hyderabad and Pune.</p>"
     "<p><strong>What is the meal voucher exemption?</strong> Rs 200 per meal, up from Rs 50.</p>"
     "<p><strong>How much children's education allowance is exempt?</strong> Rs 3,000 per month per child, up from Rs 100, with hostel allowance at Rs 9,000 up from Rs 300.</p>"
     "<p><strong>Do these apply if I am on the new tax regime?</strong> Several of these exemptions are associated with the old regime. Confirm which regime you have opted for before relying on them.</p>"
     "<p><strong>Why does my form ask about my landlord?</strong> The declaration now requires you to state your relationship with the landlord, which makes rent paid to a family member a disclosed fact rather than an assumed one.</p>"),

]
