# Weekly news-driven article, 29 August 2026.
#
# Topic picked from what people are actually searching for right now: the ITR
# due date for non-audit business/professional taxpayers falls on 31 August
# 2026, two days after this was written, and the deadline was trending across
# tax-advisory coverage all week. Checked against the existing 149 published
# slugs first (via `SELECT slug, title, category FROM articles WHERE
# published=1`, not the seed files) — no article on the site covers ITR due
# dates specifically. The closest is income-tax-freelancers (blog_seed2.py),
# whose FAQ and checklist both still say "31 July 2026" for freelancers filing
# ITR-3/ITR-4. That is now wrong for anyone not required to audit their
# accounts, per the amendment below. Flagged in REVIEW-BEFORE-PUBLISH.md and
# in the run's final report; fixing a live article needs a
# _apply_content_migrations block, which is a separate, deliberate job, not
# something to bundle into a new-article run.
#
# Verified against the primary sources, not secondary tax-portal commentary:
#   - Finance Act, 2026, Section 5 (amends Explanation 2 to Section 139(1) of
#     the Income-tax Act, 1961), from the actual notified Gazette of India,
#     Extraordinary, Part II Section 1, dated 31 March 2026
#     (CG-DL-E-31032026-271439, egazette.gov.in/WriteReadData/2026/271439.pdf)
#     — confirmed identical to the Finance Bill, 2026 as introduced in Lok
#     Sabha (indiabudget.gov.in/doc/Finance_Bill.pdf), so the clause was not
#     altered during passage. Gives the exact four-row due-date table (30 Nov /
#     31 Oct / 31 Aug / 31 Jul) and the retrospective effective date of 1 March
#     2026 — before the Finance Act itself was notified.
#   - The same Section 5, sub-clause (b): the rewritten Section 139(5), which
#     extended the revised-return window to the end of the relevant assessment
#     year (31 March 2027 for AY 2026-27), read from the same gazette PDF.
#   - Income Tax Department's official page on the Income-tax Act, 2025's
#     scope (incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/
#     objective-and-scope-new-act), which states plainly that AY 2026-27
#     returns stay governed by the 1961 Act, not the 2025 Act — this is what
#     resolves the "Section 139 or Section 263" confusion running through a
#     lot of the secondary coverage this week.
#   - Section 234F bare text (incometaxindia.gov.in/w/section-234f) for the
#     ₹5,000 / ₹1,000 late-fee figures.
#   - The ₹1 crore / ₹10 crore business and ₹50 lakh / ₹75 lakh professional
#     tax-audit thresholds under Section 44AB are unchanged by this Finance
#     Act (confirmed no amendment to that section in the same gazette text)
#     and are already used consistently in income-tax-freelancers.
#
# Format matches the earlier seeds: (title, slug, category, act, read_time,
# summary, content).
BLOG_ARTICLES_16 = [

    ("ITR Due Date 31 August 2026: Who Gets the Extra Month, and Why It's Section 139, Not Section 263",
     'itr-due-date-31-august-2026',
     'tax',
     'Income-tax Act, 1961',
     '7 min read',
     "The ITR due date for non-audit business and professional income is 31 August 2026, not 31 July, under a permanent Finance Act 2026 amendment to the old Income-tax Act. It has nothing to do with the new Income-tax Act, 2025, whatever a lot of the coverage says.",
     "<p><em>If you run a small business or freelance and haven't filed yet, you may have seen two different deadlines this week: 31 July and 31 August. Both are correct, just for different people, and picking the wrong one costs you a fee you didn't need to pay.</em></p>"
     "<p><strong>If you have business or professional income and your accounts don't require an audit, your ITR for FY 2025-26 is due on 31 August 2026, not 31 July. The change comes from the old Income-tax Act, 1961 — not the new one that took over this April.</strong></p>"
     "<blockquote><p>The extra month applies only to non-audit business and professional taxpayers filing ITR-3 or ITR-4: freelancers, consultants, shopkeepers, most partnership firms. Salaried individuals filing ITR-1 or ITR-2 still had to file by 31 July. Miss 31 August and you can file until 31 December 2026, but a late fee applies, and any TDS refund sits unclaimed until you do.</p></blockquote>"

     "<h2>Who actually gets the extra month</h2>"
     "<p>The due date for filing a return depends on what kind of income you have, not on which form you use. For assessment year 2026-27 — the return filed in 2026 for money earned between April 2025 and March 2026 — the law sorts taxpayers into four groups.</p>"
     "<div class='table-wrap'><table class='prose-table'><thead><tr><th>Who you are</th><th>Due date</th></tr></thead><tbody>"
     "<tr><td>Anyone covered by transfer pricing rules under Section 92E</td><td>30 November 2026</td></tr>"
     "<tr><td>Companies, and other assessees whose accounts must be audited (not covered by 92E)</td><td>31 October 2026</td></tr>"
     "<tr><td>Business or professional income, accounts not required to be audited</td><td>31 August 2026</td></tr>"
     "<tr><td>Everyone else, mainly salaried individuals with no business income</td><td>31 July 2026</td></tr>"
     "</tbody></table></div>"
     "<p>The third row is new. Until this year, non-audit business income sat in the same bucket as salaried taxpayers, both due 31 July. The amendment split that bucket in two. The business and professional group — anyone under the presumptive schemes in Sections 44AD or 44ADA, and most partners in unaudited firms — got an extra month.</p>"
     "<p>Whether your accounts need an audit depends on turnover. A business crosses the audit threshold at ₹1 crore, or ₹10 crore if at least 95% of receipts and payments are digital. A professional crosses it at ₹50 lakh in gross receipts (₹75 lakh under the same digital condition). Below those figures, you sit in the 31 August group by default, whether or not you actually opted for presumptive taxation.</p>"

     "<h2>Where this actually comes from</h2>"
     "<p>This isn't a one-off CBDT extension of the kind the tax department sometimes issues under pressure close to a deadline. It's a permanent change to the statute.</p>"
     "<p>Section 5 of the Finance Act, 2026 rewrites Explanation 2 to Section 139(1) of the Income-tax Act, 1961 — the clause that defines \"due date\" for return filing. The Gazette of India published the amended text on 31 March 2026. It gave the change effect from 1 March 2026, a date before the Finance Act itself was even notified. That backdating is the government confirming the new table was always meant to govern this filing season, not a future one.</p>"
     "<p>Before the amendment, Explanation 2 had three categories: transfer-pricing cases, audit cases, and \"any other assessee.\" Non-audit business income fell into that third, catch-all category, alongside salaried taxpayers, both due 31 July. The amendment adds a fourth, dedicated category for business and professional income where no audit is required, and gives it 31 August.</p>"

     "<h2>Why it isn't Section 263</h2>"
     "<p>Search for this deadline and a good share of the results credit \"Section 263 of the Income-tax Act, 2025.\" That's the new Act, the one that replaced the 1961 law on 1 April 2026. It's the wrong section for this filing season. The mistake is understandable, because Section 263 is the section that will eventually do this exact job.</p>"
     "<p>The Income Tax Department's own guidance on the transition is specific. Assessment year 2026-27 is the last assessment year under the old Act. Returns, revisions and assessments relating to it stay governed by the Income-tax Act, 1961, even though you file them after the new Act came into force. The Income-tax Act, 2025 takes over from tax year 2026-27 onward: income earned from 1 April 2026, filed in 2027. Section 263 of the new Act does carry a similar due-date table with its own August category. But it has no bearing on the return due in the next few days.</p>"
     "<p>Put plainly: much of the coverage got the number right and the law wrong. The number is the useful part for a reader with a deadline this week. The section matters more if you're a chartered accountant citing it in an appeal, or explaining to a client why two advisories disagree.</p>"

     "<h2>What it costs to miss it</h2>"
     "<p>Missing 31 August doesn't shut the door. You can still file a belated return under Section 139(4). For this assessment year, that window stays open until 31 December 2026, or until your assessment is completed, whichever comes first.</p>"
     "<p>It isn't free. Section 234F charges a late fee of ₹5,000 for filing after the due date. If your total income is ₹5 lakh or less, the fee is capped at ₹1,000. That fee sits separately from any interest owed under Sections 234A, 234B and 234C if you also underpaid tax during the year.</p>"
     "<p>There's a cost beyond the fee, too. If a client deducted TDS on your invoices during the year, that money sits credited against your PAN until you file and claim it. A freelancer who skips filing because \"no tax is due\" isn't avoiding a bill. They're leaving a refund uncollected.</p>"

     "<h2>The revised return window is longer now</h2>"
     "<p>The same Finance Act amendment touched Section 139(5), the provision for correcting a return after you've filed it. Previously, a revised return had to be filed within a fairly tight window. The rewritten sub-section now lets you file a revised return any time up to the end of the relevant assessment year, or before your assessment is completed, whichever is earlier.</p>"
     "<p>For AY 2026-27, that end date is 31 March 2027. File by 31 August, spot an error later, and you now have until the end of March 2027 to fix it, not a matter of weeks.</p>"

     "<h2>Common mistakes</h2>"
     "<ul>"
     "<li>Assuming 31 August applies to everyone with business income. It doesn't apply if your accounts require an audit; that group is due 31 October.</li>"
     "<li>Filing under ITR-1 or ITR-2 by 31 July when you actually have presumptive business income that belongs in ITR-4. Using the wrong form doesn't move your due date.</li>"
     "<li>Treating the extra month as a reason to delay. Belated filing still triggers a fee under Section 234F, and any advance tax shortfall keeps accruing interest regardless of when you eventually file.</li>"
     "<li>Citing \"Section 263\" for a return you're filing this season. That section governs tax year 2026-27 onward, not assessment year 2026-27.</li>"
     "</ul>"

     "<h2>Frequently asked questions</h2>"
     "<p><strong>Is 31 August 2026 a fixed rule now, or could it be pushed further?</strong> It's a statutory due date under Section 139(1), not an administrative extension, so it doesn't move on its own. The government can still issue a one-off extension close to the deadline, as it has in some past years. No such extension is in effect as of this date.</p>"
     "<p><strong>I file under Section 44ADA. Which date applies to me?</strong> 31 August 2026, because your accounts aren't required to be audited below the ₹50 lakh receipts threshold (₹75 lakh where cash receipts are 5% or less).</p>"
     "<p><strong>What if I miss 31 August — how long do I actually have?</strong> You can file a belated return until 31 December 2026, or before your assessment is completed, whichever is earlier. A late fee under Section 234F applies once you cross 31 August.</p>"
     "<p><strong>Does the new Income-tax Act, 2025 apply to this year's return at all?</strong> No. Assessment year 2026-27, including this due-date change, is governed by the Income-tax Act, 1961. The new Act governs tax year 2026-27 onward, filed from 2027.</p>"
     "<p><strong>Do partners in an unaudited firm also get 31 August?</strong> Yes. Partners of a firm whose accounts aren't required to be audited, and their spouse where Section 5A applies, fall in the same 31 August category as the firm.</p>"),

]
