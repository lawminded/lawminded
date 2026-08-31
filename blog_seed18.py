# Owner-requested news article, 31 August 2026.
#
# Asked for over Telegram on the evening of 31 August: the owner had heard that
# MCA had extended CCFS-2026 to 15 September and wanted a "last opportunity,
# 15 days left" piece. An earlier reply that day declined to write it, because
# no circular could be found anywhere — MCA's site 403s every fetch from this
# box, and TaxGuru, Taxscan, CAclubindia and ICSI all still showed 31 August as
# the closing date. The owner then sent the circular itself. It is real:
# General Circular No. 04/2026 dated 31 August 2026.
#
# Verified against the primary documents, all four fetched and read in full,
# not against professional-firm commentary:
#   - MCA General Circular No. 04/2026, 31.08.2026 (the extension to
#     15 September 2026, and "All other terms and conditions of the Scheme
#     shall remain unchanged")
#   - MCA General Circular No. 01/2026, 24.02.2026 (the scheme itself: the 10%
#     additional-fee figure, Rs 100/day since 1 July 2018 with no upper limit,
#     the eligible-forms list, the five excluded categories, the section 454(3)
#     immunity and its 30-day edge, MSC-1 at half fee, STK-2 at 25%, and
#     paragraph 6 on what Registrars do once the scheme closes)
#   - MCA General Circular No. 03/2026, 08.07.2026 (the July extension, and the
#     data-centre fire of 05.06.2026 given as its reason)
#   - ICSI representation G&CL: MCA: AUG:08/2026 dated 28.08.2026, from ICSI's
#     own website (the ask for 30 September, the five grounds, and the closing
#     "We shall not be giving any further proposals with respect to extension
#     for this scheme")
#
# Deliberately not written: the Section 164(2) disqualification point, which
# would have strengthened the "what happens on 16 September" section. Two bare
# Act reproductions were tried and one came back visibly corrupted (it rendered
# "shall be eligible" where the statute reads "shall not be eligible"), so the
# claim is left to the existing CCFS guide, which verified it when it was
# written and which this article links to. Also left out: the 92,859 uptake
# figure attributed to a Lok Sabha reply of 10 August 2026, and that reply's
# statement that no further extension was proposed. Both are interesting and
# both are sourced only to secondary reproductions; the sansad.in PDF could not
# be reached.
#
# This does not duplicate ccfs-2026-companies-compliance-facilitation-scheme
# (blog_seed6.py), which is the evergreen guide to how the scheme works. This
# is the news piece about the extension, the fortnight it buys, and what the
# scheme's own paragraph 6 says happens after it. The guide is now stale on the
# closing date and is corrected by migration 8 in database.py.

BLOG_ARTICLES_18 = [

    ("CCFS-2026 Extended to 15 September 2026: Fifteen Days to Clear Every Overdue ROC Filing at 10% of the Late Fee",
     'ccfs-2026-extended-15-september-2026',
     'updates',
     'Companies Act, 2013',
     '8 min read',
     "MCA General Circular 04/2026 moved the CCFS-2026 deadline from 31 August to 15 September 2026 on the day it was due to close. Everything else about the scheme stays the same. What the circular says, what the fortnight is worth in rupees, and what the scheme's own text says happens on 16 September.",

     "<p><em>The scheme had hours left to run. Late on 31 August 2026 the Ministry of Corporate Affairs issued a one-page circular and moved the closing date again. If your company still has old annual returns and balance sheets sitting unfiled with the Registrar, you have just been handed a fortnight.</em></p>"

     "<p><strong>General Circular No. 04/2026 dated 31 August 2026 extends the Companies Compliance Facilitation Scheme, 2026 to 15 September 2026. Every other term of the scheme stays exactly as it was, so overdue annual filings still cost normal fees plus only 10% of the additional fees.</strong></p>"

     "<p>Additional fees are what turn a small lapse into a large bill. Since 1 July 2018, a late annual return or financial statement carries Rs 100 for every day of delay, and the MCA's own circular says there is no upper limit on it. A company that stopped filing four years ago is not facing a fine. It is facing a meter that has been running since the day it stopped.</p>"

     "<blockquote><p>You get fifteen days, counting 1 to 15 September, and two weekends sit inside them. The discount has not moved: 10% of the additional fees on overdue annual forms, half the normal fee to go dormant, a quarter of it to strike off. Nor has eligibility, so a company already served with a final strike-off notice is still shut out. The circular says nothing about what happens on the 16th, because the original scheme circular already did. Registrars are to take action against the companies that did not use it.</p></blockquote>"

     "<h2>What the circular actually says</h2>"

     "<p>It runs to one page and four short paragraphs. The file number is Policy-02/2/2020-CL-V-MCA. It is addressed to all Registrars of Companies, all Regional Directors and all stakeholders, and signed by Nupur Aishwarya, Deputy Director (Policy).</p>"

     "<p>The first two paragraphs are history. The scheme was introduced by General Circular No. 01/2026 of 24 February 2026 and was to run until 15 July 2026. General Circular No. 03/2026 of 8 July 2026 then pushed that to 31 August 2026.</p>"

     "<p>The third paragraph is the one that matters. In the ministry's words, \"in view of the representations received from various stakeholders, it has been decided to further extend the validity of the Companies Compliance Facilitation Scheme, 2026 (CCFS-2026) up to 15th September, 2026. All other terms and conditions of the Scheme shall remain unchanged.\"</p>"

     "<p>That last sentence does the real work. The fee discount, the list of eligible forms, the excluded companies and the immunity have not been reopened or renegotiated. Only the date moved.</p>"

     "<p>July's circular read differently. It gave a reason: a fire at the MCA data centre on 5 June 2026, and the capacity restoration work that followed it. This one names no technical or operational problem at all. It says representations were received, and stops there.</p>"

     "<h2>The ministry gave half of what was asked for</h2>"

     "<p>The Institute of Company Secretaries of India wrote to the MCA Secretary, Dr Pallavi Jain Govil, on 28 August 2026. The letter sits on the ICSI's own website under reference G&amp;CL: MCA: AUG:08/2026, and it followed an earlier letter of 20 August. It asked the ministry to extend the scheme \"preferably up to 30 September 2026\".</p>"

     "<p>The ministry gave 15 September. Half the time requested.</p>"

     "<p>ICSI set out five grounds in that letter, and together they are a fair description of why companies are stuck. Accounts could not be closed because income-tax work, reconciliations and audits were still open. Companies carrying old defaults have to trace records going back years before anything can be signed. Where a director's DIN is inactive or deactivated, the KYC has to be done, the digital signature renewed and the DIN reactivated before a single form can be uploaded. August and September collide with tax audit and GST deadlines. And some of these companies are simultaneously asking the NCLT to restore their names under Section 252, where the pending filings are part of what the tribunal expects to see done.</p>"

     "<p>The letter ends with a line that anyone planning to wait should read twice: \"We shall not be giving any further proposals with respect to extension for this scheme.\"</p>"

     "<h2>What the fifteen days are actually for</h2>"

     "<p>Filing is the last step, and it is the quickest one. Everything that makes a filing possible sits in front of it.</p>"

     "<p>If the accounts for the missing years have never been audited and adopted, that is the job. An auditor needs the books, the bank statements and time. The board has to approve the accounts, the members have to adopt them at a general meeting, and the minutes have to exist before any form can be signed. None of that gets shorter because a circular moved a date.</p>"

     "<p>So the sequence for a company with a real backlog looks like this.</p>"

     "<ol>"
     "<li>Pull the company's filing history from the MCA portal and write down exactly which form is missing, for which year.</li>"
     "<li>Check every signing director's DIN status and DSC validity today. A deactivated DIN needs <a href=\"/article/din-allotment-kyc-disqualification\">DIR-3 KYC</a> done before it will sign anything. This is the step people discover on 14 September.</li>"
     "<li>Get the oldest years audited and adopted first.</li>"
     "<li>File in chronological order. Later years often will not go through until the earlier ones have.</li>"
     "<li>Read the fee on the payment screen and confirm the additional fee has come down to 10% before you pay.</li>"
     "</ol>"

     "<p>If the audit realistically cannot be finished by the 15th, the useful question changes. A company nobody intends to trade again can file STK-2 at 25% of the filing fee and be done. A company being kept alive for its name or a future plan can file MSC-1 at half the normal fee and go dormant. Both are open on the same terms until 15 September, and both are cheaper than a revival you will not finish in time. Our <a href=\"/article/ccfs-2026-companies-compliance-facilitation-scheme\">full guide to CCFS-2026</a> works through all three routes, and the separate guides to <a href=\"/article/striking-off-company-stk-2\">striking off a company</a> and <a href=\"/article/dormant-company-section-455\">dormant status under Section 455</a> explain what each one commits you to afterwards.</p>"

     "<h2>What the fortnight is worth</h2>"

     "<p>Take a private company that last filed for FY 2021-22. <a href=\"/article/annual-compliance-companies\">AOC-4 and MGT-7</a> are missing for three financial years, which is six forms, and the delays across them add up to roughly 4,500 days.</p>"

     "<p>At Rs 100 a day per form with no ceiling, that is about Rs 4,50,000 in additional fees. Under the scheme the company pays Rs 45,000 of it. Normal filing fees are payable in full either way, because the scheme discounts the penalty component and nothing else. So the number at stake in these fifteen days is a little over four lakh rupees, and it goes back to full price on 16 September.</p>"

     "<p>Five kinds of company still cannot use the scheme at all. One already served with the final strike-off notice by the Registrar. One that has already applied to be struck off. One that applied for dormant status before the scheme began. One being dissolved through a scheme of amalgamation. And a company identified as a vanishing company.</p>"

     "<p>The immunity is unchanged too, and it still has a sharp edge. Filing under the scheme concludes the proceedings for the Section 92 and Section 137 defaults, and no penalty is leviable, but only if you file before the adjudicating officer issues a notice, or within thirty days of that notice. Once an adjudication order has been passed, you can still file at the reduced fee. The penalty in that order stands.</p>"

     "<h2>What happens on 16 September</h2>"

     "<p>The founding circular answered this in February, and nothing since has withdrawn it. Paragraph 6 of General Circular No. 01/2026 reads: \"At the conclusion of the Scheme, the Registrars of Companies concerned shall take necessary action under the Act against the companies who have not availed this Scheme and are in default of filing these documents in a timely manner.\"</p>"

     "<p>That is an instruction to the Registrars, written into the scheme itself. It is also the part of CCFS-2026 that most summaries leave out. The scheme is a discount window, and it is the notice period before enforcement.</p>"

     "<p>Enforcement here means adjudication under Section 454 for the Section 92 and Section 137 defaults, with penalties falling on the company and on the officers in default. That is the same Section 454 machinery the scheme's own immunity clause is built on. Until 15 September, filing switches it off. After that, filing is just filing, late and at full price.</p>"

     "<h2>Common mistakes in the next fifteen days</h2>"

     "<ul>"
     "<li><strong>Waiting for a third extension.</strong> The body that asked for this one has told the ministry, in writing, that it will not ask again.</li>"
     "<li><strong>Assuming LLPs are in.</strong> They are not. CCFS-2026 is a companies scheme, and Form 8 and Form 11 defaults get nothing from it.</li>"
     "<li><strong>Leaving DSC renewal and DIN KYC to filing day.</strong> ICSI listed this as a reason companies missed the August date, which makes it a mistake with a track record.</li>"
     "<li><strong>Expecting 10% to apply to the whole bill.</strong> Normal filing fees are payable in full. Only the additional fee is cut.</li>"
     "<li><strong>Starting a four-year audit backlog on 10 September</strong>, when dormancy or strike-off was the realistic answer a week earlier.</li>"
     "<li><strong>Sitting on an adjudication notice that is already more than thirty days old</strong> and assuming the scheme cures it.</li>"
     "</ul>"

     "<h2>Frequently asked questions</h2>"

     "<p><strong>What is the new last date for CCFS-2026?</strong> 15 September 2026, a Tuesday, under General Circular No. 04/2026 dated 31 August 2026. It was 31 August 2026 until that circular was issued.</p>"

     "<p><strong>Did anything else about the scheme change?</strong> No. The circular states that all other terms and conditions remain unchanged, so the fees, the eligible forms, the excluded companies and the immunity are exactly as they were on 30 August.</p>"

     "<p><strong>Will there be another extension?</strong> The circular provides for none. ICSI, which requested this one, told the ministry in the same letter that it would not be making any further proposals on the scheme.</p>"

     "<p><strong>Do I have to apply for the extension?</strong> No. There is no application and no separate form. File the overdue form on MCA-21 V3 and the reduced additional fee is applied at the payment stage.</p>"

     "<p><strong>Does the extension cover LLPs?</strong> No. The scheme applies to companies, and no LLP form appears anywhere in its list of eligible forms.</p>"

     "<p><strong>My company got an adjudication notice three weeks ago. Does filing now help?</strong> Yes, if you file within thirty days of that notice. File on day thirty-one and you pay the reduced fee but keep the penalty exposure.</p>"

     "<p><strong>Can I still choose strike-off or dormancy instead of clearing everything?</strong> Yes. STK-2 at 25% of the filing fee and MSC-1 at half the normal fee are both available until 15 September, on the same terms as before.</p>"

     "<p><strong>Why did the MCA extend it?</strong> The circular gives one reason: representations received from various stakeholders. Unlike the July extension, which cited the data centre fire, it names no technical problem.</p>"),

]
