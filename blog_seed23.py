# Weekly run, 2026-09-13. Follow-up to the Subhash Chandra personal-guarantee
# article already on the site (subhash-chandra-nclt-order-personal-guarantee,
# blog_seed15.py) and to the SEBI Zee land-pledge article (blog_seed17.py).
# Not a duplicate of either: this covers a new event — the five-member NCLT
# bench that stayed the 25 August 2026 order on 1 September 2026 — and the
# still-unresolved fight over whether NCLT had the power to form that bench
# at all. Story picked because it was leading Indian business-law coverage
# in the seven days before this run (Bar and Bench, LiveLaw, Business
# Standard, Moneylife, ThePrint, The Bar Bulletin all covered it), and
# because it is a live sequel to a case this site's readers already searched
# for once.
#
# Primary source for the 25 August 2026 order (Nilesh Sharma, Member
# (Judicial), Third Member, in CP(IB)-97(ND)/2022, Indiabulls Housing
# Finance Ltd v Dr Subhash Chandra): the 144-page order itself, fetched
# directly from Bar and Bench's own hosting and read with pypdf --
#   https://images.assettype.com/barandbench/2026-08-27/0evinhod/India_Bulls_v__Dr__Subhash_Chandra_order.pdf
# Confirmed directly from that PDF text:
#   - admitted claims Rs 22,006.57 crore; repayment plan Rs 6.25 crore to
#     creditors plus Rs 25 lakh process cost (page ~104-105 of the order,
#     cited within LIC Housing Finance's own submission)
#   - LIC Housing Finance's claim Rs 1,322.39 crore repaid Rs 38,09,294
#   - creditor approval by 80.814% of voting share (page ~15-16)
#   - final ORDER (page 144): approval under Section 114 IBC subject to
#     exclusion of claims filed by Anil Kumar (960 individuals) and Sunil
#     Jain (300 individuals); plan binding on all creditors under Section
#     115; matter to go back to "the Original Division Bench for passing
#     appropriate orders in terms of the majority opinion under Section
#     419(5) of the Companies Act, 2013"
#   - Section 60(5) of the IBC (Chapter VI, Part II) held not to apply to
#     this proceeding, because it is a Part III (individual/personal
#     guarantor) matter, not a corporate insolvency matter
#
# Section 419 of the Companies Act, 2013, verified against its own text
# across four independent bare-act mirrors that agreed word for word
# (ca2013.com, ibclaw.in, corporatelawreporter.com, and a kanoongpt.in /
# indiankanoon-sourced compilation) -- indiacode.nic.in and the MCA's own
# PDF both refused direct fetch/extraction, consistent with the mca.gov.in
# 403 behaviour already logged in automation/notes.md:
#   419(4) "The President shall, for the disposal of any case relating to
#          rehabilitation, restructuring, reviving of companies, constitute
#          one or more Special Benches consisting of three or more Members,
#          majority necessarily being of Judicial Members."
#   419(5) "If the Members of a Bench differ in opinion on any point or
#          points, it shall be decided according to the majority, if there
#          is a majority, but if the Members are equally divided, they
#          shall state the point or points on which they differ, and the
#          case shall be referred by the President for hearing on such
#          point or points by one or more of the other Members of the
#          Tribunal and such point or points shall be decided according to
#          the opinion of the majority of Members who have heard the case,
#          including those who first heard it."
#
# Everything after the 25 August order (the 31 August finding of "no
# majority," the 1 September five-member bench, the stay, the asset
# restraint, Chandra's Section 419 objection before NCLAT, and the two
# forward hearing dates) is not yet on a court website in usable form, so
# it rests on named, converging news reporting rather than a second PDF:
#   - 31 August "no majority" finding and referral back to the President:
#     Business Standard and LiveLaw, both 1 September 2026
#   - 1 September order (bench composition, stay, asset restraint, notice,
#     23 September date): Bar and Bench and Moneylife, both 1-2 September
#     2026, corroborated by Business Standard, BusinessToday and
#     Newslaundry
#   - Chandra's Section 419 objection (Sasmit Patra, senior advocate) and
#     NCLAT's refusal to rule on it (Justice Yogesh Khanna, 2 September):
#     ThePrint and Business Standard, both 2 September 2026
#   - 7 October NCLAT date and the lenders represented (LIC Housing
#     Finance, Canara Bank, Union Bank; Solicitor General Tushar Mehta):
#     ANI, 2 September 2026
#   - the specific legal question of whether Section 419(5) permits
#     replacing a bench outright rather than adding members one at a time:
#     an analysis published by The Bar Bulletin, attributed to it by name
#     in the article rather than folded into the site's own voice
#
# Deliberately left out: any prediction of how the 23 September or 7
# October hearings will go. Both are still pending as of 13 September 2026.
#
# Format matches the earlier seeds: (title, slug, category, act, read_time,
# summary, content).

BLOG_ARTICLES_23 = [

    ("Subhash Chandra's Rs 6.25 Crore Repayment Plan Is on Hold: Why NCLT Needed Five Members to Decide What Its Own Order Meant",
     'subhash-chandra-nclt-five-member-bench-stay',
     'updates',
     'Insolvency and Bankruptcy Code, 2016',
     '9 min read',
     "On 1 September 2026, a five-member NCLT bench stayed the tribunal's own 25 August order approving Subhash Chandra's Rs 6.25 crore repayment plan against Rs 22,006.57 crore in claims, after finding no valid majority had actually approved it. Here is what Section 419 of the Companies Act required, why the stay is not a reversal, and what two separate hearings on 23 September and 7 October will each decide.",

     "<p><em>Three months ago this site explained how a Rs 22,006 crore claim against Zee founder Subhash Chandra could be settled for Rs 6.25 crore. That order has now been paused. The tribunal that approved it is the one that paused it. If you are one of the lenders in this case, or you are just trying to work out what a \"stay\" actually undoes, here is what changed on 1 September and what did not.</em></p>"

     "<p><strong>On 1 September 2026, a new five-member bench of the NCLT put the 25 August order approving Subhash Chandra's repayment plan on hold. It did not find the plan wrong. It found that the tribunal could not agree a majority had actually approved it in the first place.</strong></p>"

     "<blockquote>The stay pauses the Rs 6.25 crore repayment plan. It does not revive the Rs 22,006.57 crore in claims as money anyone now expects to recover. It does not find the plan unlawful either. What it decides, for now, is only that nobody, not even the tribunal itself, is sure a valid majority approved it. NCLT reopens the question on 23 September. A separate appeal by dissenting lenders sits with the NCLAT until 7 October. Neither date settles the matter on its own.</blockquote>"

     "<h2>What the 25 August order actually held</h2>"

     "<p>Our <a href=\"/article/subhash-chandra-nclt-order-personal-guarantee\">earlier report</a> covered this case in detail. Here are the numbers that matter for this update. Dr Subhash Chandra is personal guarantor for loans taken by Essel Group companies. Admitted claims against him run to Rs 22,006.57 crore. His repayment plan offered creditors Rs 6.25 crore, plus another Rs 25 lakh for the cost of the process.</p>"

     "<p>Judicial Member Nilesh Sharma approved that plan on 25 August 2026, in a 144-page order. He relied on Section 114 of the Insolvency and Bankruptcy Code, 2016. Under Section 115, he held the plan binding on every creditor, including those who had voted against it.</p>"

     "<p>Sharma's approval was not unconditional. He excluded claims filed by two individuals, Anil Kumar and Sunil Jain, on behalf of 960 and 300 people. He found the resolution professional had admitted those claims \"without adequate basis or supporting material.\" Everything else, including claims from entities the objecting banks called Chandra's associates, he let stand.</p>"

     "<h2>Why it took a third member to get there</h2>"

     "<p>Sharma was never meant to have the last word. Two members heard the case before him and split. Judicial Member Ashok Kumar Bhardwaj wanted the plan approved, but only for creditors who had voted for it. Technical Member Reena Sinha Puri wanted it rejected outright, citing irregularities in the claims and the voting. Neither view had a majority on its own. So the case went to a third member, under the Companies Act's rule for exactly this situation.</p>"

     "<p>That rule is Section 419(5) of the Companies Act, 2013: \"If the Members of a Bench differ in opinion on any point or points, it shall be decided according to the majority, if there is a majority, but if the Members are equally divided, they shall state the point or points on which they differ, and the case shall be referred by the President for hearing on such point or points by one or more of the other Members of the Tribunal and such point or points shall be decided according to the opinion of the majority of Members who have heard the case, including those who first heard it.\"</p>"

     "<p>The President appointed Sharma under this provision in February 2026. Sharma's own order asked for the case to go back to \"the Original Division Bench for passing appropriate orders in terms of the majority opinion under Section 419(5).\" He clearly expected his approval to combine with Bhardwaj's. Two members out of three, both approving, should have been a majority.</p>"

     "<h2>Where that expectation broke down</h2>"

     "<p>It did not work out that way. On 31 August, the original two-member bench looked at Sharma's order again. Business Standard and LiveLaw both reported what they found: Sharma's approval did not actually match Bhardwaj's. Bhardwaj wanted the plan to bind only the creditors who had voted for it. Sharma approved a plan binding on everyone, and excluded a different set of claims to get there. The original bench treated this as a fresh, independent order, not the second half of a majority. They referred the question back to the President instead of acting on it themselves.</p>"

     "<p>Here is the point most of the coverage skipped. Section 419(5) does not just need two out of three members to reach the same result. It needs that result to be \"the opinion of the majority,\" which the original bench read as requiring the reasoning to line up too, not only the outcome. A 2-1 split on whether to approve is not automatically a majority, if the two approvals are conditional on different terms.</p>"

     "<h2>Five members, and a freeze on Chandra's assets</h2>"

     "<p>The President did not refer the case to a fourth member. Instead, NCLT President Justice (retd) Anupinder Singh Grewal formed a five-member special bench. It included Judicial Members Bachu Venkat Balaram Das and Mahendra Khandelwal, and Technical Members Atul Chaturvedi and Ravindra Chaturvedi, alongside Grewal himself. On 1 September, this bench stayed the 25 August order. It restrained Chandra from alienating any property, directly or indirectly. It issued notice to all parties and set 23 September to hear the whole repayment plan afresh.</p>"

     "<p>Bar and Bench and Moneylife both reported the bench's reasoning: no clear majority view existed on the earlier verdict. That finding is narrower than it sounds. The bench did not rule that Bhardwaj or Sharma got the law wrong. It ruled that their combined view could not be certified as a majority under Section 419(5). So the order that view was said to produce cannot stand as it is.</p>"

     "<h2>\"Under what power\": the challenge nobody has answered yet</h2>"

     "<p>Chandra's own lawyers do not accept that a five-member bench was the right fix. Before the NCLAT, senior advocate Sasmit Patra argued NCLT has no power to convene one for a reference like this. ThePrint and Business Standard reported his argument in detail. Section 419(5) lets the President add \"one or more of the other Members\" to break a specific tie. It says the disputed point is decided by \"the majority of Members who have heard the case, including those who first heard it.\" That wording keeps the original members in the room. It does not describe swapping out the whole bench for five new members who never heard the earlier arguments.</p>"

     "<p>A different provision does allow a full special bench. Section 419(4) lets the President \"constitute one or more Special Benches consisting of three or more Members\" for cases \"relating to rehabilitation, restructuring, reviving of companies.\" Chandra is not a company. He is an individual guarantor, proceeded against under Part III of the IBC. Sharma's own order noted that this Part operates separately from the corporate insolvency provisions in Part II. An analysis by The Bar Bulletin has flagged the resulting question: did Parliament mean Section 419(5) to let a tie be broken one member at a time, or did it also permit what happened here?</p>"

     "<p>The NCLAT has not answered that question. Justice Yogesh Khanna heard the lenders' separate appeal on 2 September. He said the \"constitution of the five-member bench was not a question before challenge for us,\" and adjourned that appeal to 7 October. By then, NCLT's own fresh hearing will already have happened.</p>"

     "<h2>Two dates, two different questions</h2>"

     "<p>Keep the two forums apart. They are not deciding the same thing. On 23 September, the five-member NCLT bench is meant to rehear the merits of the plan itself. That means deciding, fresh, whether Rs 6.25 crore against Rs 22,006.57 crore in claims deserves approval at all, with all five members party to the outcome this time. On 7 October, the NCLAT hears a different appeal. Dissenting lenders, among them LIC Housing Finance, Canara Bank and Union Bank, are challenging the process behind the original approval. Solicitor General Tushar Mehta represents them. Chandra's objection to the five-member bench's existence sits inside that same appeal, still unresolved.</p>"

     "<p>Picture the two outcomes that would clash. Say the NCLT approves the plan again on 23 September. That would not end the case if the NCLAT later agrees with Chandra that the five-member bench had no power to hear it at all. And say the lenders win on process at the NCLAT. That would not, by itself, change what a properly constituted bench eventually decides on the merits. Both questions have to close before any number in this case becomes final.</p>"

     "<h2>What this means if you have signed a personal guarantee</h2>"

     "<p>The underlying law has not moved. A guarantor's repayment plan can still bind every creditor once a tribunal approves it, dissenters included. The size of the haircut is not, by itself, a ground to reject a plan. Sharma's order restated that, and our earlier report on the 25 August ruling explains it in full. What this month adds is a reminder that \"approved by NCLT\" is not always the last word. A bench can revisit its own order. In a case that split three ways at the first stage, it did.</p>"

     "<h2>Common mistakes</h2>"

     "<ul>"
     "<li><strong>Reading the stay as a reversal.</strong> The five-member bench paused the order. It has not held the plan invalid, and it has not reinstated the full Rs 22,006.57 crore as recoverable.</li>"
     "<li><strong>Assuming the lenders have won.</strong> Their NCLAT appeal is still pending, adjourned to 7 October, and it is about process, not a finding in their favour.</li>"
     "<li><strong>Treating \"no majority\" as a comment on the plan's merits.</strong> The finding was procedural. It said Section 419(5) had not produced a valid majority, not that the plan itself was wrong.</li>"
     "<li><strong>Missing that two forums are now involved.</strong> NCLT's 23 September hearing and NCLAT's 7 October hearing address different questions. Either one can change what the other's outcome means.</li>"
     "</ul>"

     "<h2>Frequently asked questions</h2>"

     "<p><strong>Has Subhash Chandra's Rs 6.25 crore settlement been cancelled?</strong> No. It has been stayed, meaning it cannot be acted on for now, while a five-member NCLT bench reconsiders the whole repayment plan starting 23 September 2026.</p>"

     "<p><strong>Why did NCLT need five members when the case started with two?</strong> The original two-member bench split, so a third member was added under Section 419(5) of the Companies Act to break the tie. The original bench later found his order did not actually match either of their positions closely enough to form a majority. The President then formed a five-member bench instead of adding a fourth member.</p>"

     "<p><strong>Is it legal for NCLT to form a five-member bench this way?</strong> That is disputed. Chandra's lawyers argue Section 419(5) only permits adding members to resolve a specific point of difference, not replacing the bench entirely. They also argue that full special benches under Section 419(4) are meant for company cases, not individual insolvency. The NCLAT has not yet ruled on this question.</p>"

     "<p><strong>Can Subhash Chandra sell or transfer his assets right now?</strong> No. The five-member bench has restrained him from alienating any property, directly or indirectly, while the matter is reheard.</p>"

     "<p><strong>What happens on 23 September and 7 October?</strong> On 23 September, the five-member NCLT bench is due to rehear the repayment plan on its merits. On 7 October, the NCLAT hears a separate appeal by dissenting lenders challenging the process behind the original approval. That appeal also includes Chandra's objection to how the five-member bench was formed.</p>"),

]
