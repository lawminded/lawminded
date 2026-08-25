# Owner-requested case study, 26 August 2026 (asked for by name over Telegram:
# "a detailed case study with all the fictional characters and setup for
# understanding the corporate veil and how on directors default it will be
# removed").
#
# Checked the 133 published slugs first (live DB dump, 26 Aug 2026). The site
# has director-duties, corporate-governance, din-allotment-kyc-disqualification
# and striking-off-company-stk-2, but nothing on the corporate veil itself or on
# when directors stop being protected by it. No overlap.
#
# The company, the people and every rupee figure in the narrative are invented.
# Every section number, penalty, threshold and judgment is verified against the
# primary instrument — see REVIEW-BEFORE-PUBLISH.md on this branch for the
# claim-by-claim list.
#
# Category is 'acts' rather than 'corp': the subject is a doctrine running across
# the Companies Act, the IBC, the Income-tax Act 2025, CGST, the NI Act and the
# EPF Act, and 'corp' is already heavily over-represented.
#
# Format matches the earlier seeds: (title, slug, category, act, read_time,
# summary, content).
BLOG_ARTICLES_13 = [

    ('Lifting the Corporate Veil: A Case Study in How Directors End Up Paying Personally',
     'lifting-corporate-veil-director-liability-case-study',
     'acts',
     'Companies Act, 2013',
     '18 min read',
     'A fictional company, three directors, and every real provision of Indian law that takes their protection away. Meridian Weaves survives an honest business failure. It does not survive what its managing director does next.',

     "<p><em>Every founder is told that a private limited company keeps business risk away from the flat they live in. That is true, and it is most of the reason the form exists. What gets explained far less clearly is where the protection stops, and how ordinary it looks on the day it does. So here is a company that never existed, run by three people who never existed, and a body of law that is entirely real.</em></p>"

     "<p><strong>The corporate veil holds when a business fails honestly. It comes off when directors default, and it usually comes off in pieces, through statutes that name directors by their office, rather than through a judge dramatically declaring the company a sham.</strong></p>"

     "<blockquote><p><strong>The bottom line</strong></p>"
     "<p><strong>What it covers:</strong> debts the company took on in its own name while its directors were acting in good faith. Shareholders lose the money they put in and nothing more.</p>"
     "<p><strong>What it does not cover:</strong> personal guarantees, money the company collected on someone else's behalf and kept, cheques a director signed, and anything done to put assets out of a creditor's reach.</p>"
     "<p><strong>What losing it costs:</strong> unlimited personal liability for company debts under Section 339 of the Companies Act, disqualification for five years under Section 164(2), and prosecution for fraud under Section 447, which carries up to ten years.</p></blockquote>"

     "<h2>The company, and the people in it</h2>"

     "<p>Meridian Weaves Private Limited was incorporated on 4 March 2019 at Bhiwandi, Maharashtra. Power looms, mostly grey fabric for two garment buyers in Tiruppur. Paid-up capital of fifteen lakh rupees, split between three shareholders.</p>"

     "<p><strong>Rohan Deshmukh</strong> holds 60 per cent and is the managing director. He runs the floor, negotiates with buyers, and signs almost everything.</p>"

     "<p><strong>Anjali Rao</strong> holds 25 per cent and is a whole-time director looking after accounts. She is the second signatory on the company's current account and she prepares the numbers the auditor sees.</p>"

     "<p><strong>Vikram Sethi</strong> is the nominee of the family office that put in the remaining 15 per cent. He is a non-executive director. He attends four board meetings a year over video, asks about receivables, and has never been to Bhiwandi.</p>"

     "<p>Two other people matter later. <strong>Priya Nair</strong> is the statutory auditor. <strong>Mehta Fabrics</strong> is a yarn supplier in Ichalkaranji that gave Meridian credit for four years without a single delay.</p>"

     "<h2>Act one: the veil doing exactly what it is supposed to do</h2>"

     "<p>By FY 2021-22 Meridian was turning over 9.6 crore rupees with 41 workers on the rolls. The bank sanctioned a working capital limit of 2.4 crore against hypothecation of the looms. Rohan signed a personal guarantee for one crore of that. Remember the guarantee. It matters, and it is not what most people think it is.</p>"

     "<p>In August 2023 Northgate Retail, which took roughly a third of Meridian's output, stopped paying. One crore eighty lakh went unpaid, then the buyer's own lenders moved in. Meridian never saw the money. The company could not pay Mehta Fabrics, could not service the bank, and by early 2024 was insolvent in any practical sense.</p>"

     "<p>At this point, what could Mehta Fabrics do to Rohan personally? Nothing. Section 9 of the Companies Act says that from the date on the certificate of incorporation the subscribers become a body corporate, able to hold property, contract, and sue and be sued in its own name. The debt was Meridian's debt. Rohan owned most of Meridian, but he was not Meridian.</p>"

     "<p>This is the oldest principle in company law and it comes from an English case decided in 1896, <em>Salomon v A Salomon &amp; Co Ltd</em>. Aron Salomon converted his leather business into a company he almost wholly owned, took debentures over its assets, and when the company collapsed the unsecured creditors argued he should pay them himself. The House of Lords refused. Lord Macnaghten's line has been quoted in Indian courts ever since: \"The company is at law a different person altogether from the subscribers to the memorandum; and, though it may be that after incorporation the business is precisely the same as it was before, and the same persons are managers, and the same hands receive the profits, the company is not in law the agent of the subscribers or trustee for them.\"</p>"

     "<p>The bank was in a different position, but not because of any veil-lifting. Rohan had signed a guarantee, which is simply a contract in which he promised to pay if the company did not. A creditor who wants access to a director's personal assets can ask for that in writing before lending, and banks routinely do. It is worth being precise about the difference, because founders often confuse the two. A guarantee is protection the director gave away voluntarily. Veil-lifting is protection the law takes back.</p>"

     "<p>Had the story ended here, Meridian's directors would have lost their shareholding and nothing else. A business failed. That is allowed.</p>"

     "<h2>The first tear, and it has nothing to do with fraud</h2>"

     "<p>Meridian's last annual filing with the Registrar was for FY 2021-22. After Northgate defaulted, the annual return in MGT-7 and the financial statements in AOC-4 simply stopped going in, for FY 2022-23, then 2023-24, then 2024-25. Nobody decided to hide anything. There was no money for the company secretary's fee and there were more urgent fires.</p>"

     "<p>Here is where most founders get the law wrong. They assume a penalty for late filing lands on the company, and if the company has no money, that is the end of it. Read Section 92(5) again. If a company fails to file its annual return in time, \"such company and its every officer who is in default\" is liable to a penalty of ten thousand rupees, plus a hundred rupees for every further day, capped at two lakh for the company and fifty thousand for the officer. Section 137(3) does the same for financial statements, and names the managing director and the chief financial officer specifically.</p>"

     "<p>The phrase \"officer who is in default\" is defined in Section 2(60), and it is worth reading slowly because it decides who pays. It covers the whole-time director. It covers key managerial personnel. It covers any person under the immediate authority of the Board who is charged with maintaining or filing accounts and who \"knowingly fails to take active steps to prevent\" the default. And in clause (vi), it covers every director who knew about the contravention because it came up in Board papers he received, and who sat through the meeting without objecting.</p>"

     "<p>So the penalty is not the company's alone. It is Rohan's, and Anjali's, out of their own pockets. The veil is intact, in the sense that no court has disregarded the company. The statute has simply gone around it.</p>"

     "<p>Then, in September 2025, something worse and entirely automatic happened. Section 164(2)(a) deals with a company that has not filed financial statements or annual returns for three continuous financial years. A person who is or has been a director of such a company cannot be reappointed there, and cannot be appointed in any other company, for five years. No notice, no hearing, no discretion. Three years of silence and the disqualification exists.</p>"

     "<p>Vikram Sethi found out when a completely unrelated company he sat on tried to file a form and his DIN came back deactivated. Under the proviso to Section 167(1)(a) his office falls vacant in every company other than the defaulting one. He had never seen a rupee of Meridian's money and had no idea the filings had lapsed. He was still caught, because Section 164(2) attaches to the status of being a director, not to conduct. Our guide on <a href=\"/article/din-allotment-kyc-disqualification\">DIN, KYC and director disqualification</a> goes through what happens next and how narrow the escape routes are.</p>"

     "<h2>The month it stops being a bad year and starts being a default</h2>"

     "<p>Through late 2025 Rohan kept the looms running on the theory that one large order would fix everything. To do it, he used money that was never Meridian's to use.</p>"

     "<p><strong>Provident fund.</strong> Meridian deducted the employees' share of PF from 41 workers' wages for nine months and did not deposit it. Around 4.7 lakh rupees. Section 14A of the Employees' Provident Funds and Miscellaneous Provisions Act, 1952 says that where an offence under the Act is committed by a company, every person who at the time was in charge of, and was responsible to, the company for the conduct of its business is deemed guilty along with the company. Sub-section (2) goes further: where the offence was committed with the consent or connivance of, or is attributable to any neglect on the part of, any director or manager, that person is deemed guilty too. The escape in the proviso is narrow, and it is not \"the company had no cash\". It is proof that the offence happened without his knowledge, or that he exercised all due diligence to prevent it.</p>"

     "<p><strong>GST.</strong> Meridian charged GST on its invoices, collected it from customers, and stopped remitting it. Section 89(1) of the CGST Act, 2017 opens with the words \"Notwithstanding anything contained in the Companies Act, 2013\". Where tax, interest or penalty due from a private company cannot be recovered, every person who was a director during that period is jointly and severally liable, unless he proves that the non-recovery cannot be attributed to any gross neglect, misfeasance or breach of duty on his part. Note where the burden sits. The department does not have to prove the director was careless. The director has to prove he was not.</p>"

     "<p><strong>Income tax.</strong> The same structure, in Section 323 of the Income-tax Act, 2025, which replaced Section 179 of the 1961 Act. Where tax due from a private company cannot be recovered, every person who was a director at any time during the relevant tax year is jointly and severally liable on the same terms, and \"tax due\" is defined to include penalty, interest, fees or any other sum payable under the Act. This one also begins by overriding the Companies Act, which tells you how deliberate the drafting is.</p>"

     "<p><strong>Cheques.</strong> In November and December 2025 Rohan issued three cheques to Mehta Fabrics totalling 22 lakh rupees, knowing the account could not honour them. Anjali countersigned two. All three bounced. Section 138 of the Negotiable Instruments Act, 1881 makes that an offence punishable with up to two years' imprisonment, or a fine of up to twice the cheque amount, or both. Section 141 then extends it to \"every person who, at the time the offence was committed, was in charge of, and was responsible to, the company for the conduct of the business of the company\". If you want the procedure and the notice timelines, we have a full guide to <a href=\"/article/cheque-bounce-section-138-ni-act\">cheque bounce under Section 138</a>.</p>"

     "<p>Look at what those four statutes have in common. Not one of them asks a court to pretend Meridian does not exist. Each of them says: the company is liable, and so is the person who was running it. That is how directors are actually reached in India, far more often than by the doctrine everybody has heard of.</p>"

     "<h2>The looms move, and the company applies to disappear</h2>"

     "<p>What happened in January 2026 is a different kind of act.</p>"

     "<p>Rohan incorporated Vasant Looms Private Limited at the same Bhiwandi address, with his brother-in-law and an employee as the two directors. Meridian then sold its looms to Vasant for eighteen lakh rupees. Their written down value in Meridian's own books was 1.1 crore. The workers turned up on Monday to the same machines under a new name. In March, Rohan filed an application under Section 248(2) to have Meridian's name struck off the register, and the company was notified as dissolved.</p>"

     "<p>He thought that was the end of it. It was the beginning.</p>"

     "<p><strong>Section 251</strong> deals with exactly this. It applies where an application under Section 248(2) is found to have been made to evade the company's liabilities, or to deceive creditors, or to defraud any other person. In that case the persons in charge of the management become jointly and severally liable to anyone who suffered loss because of the dissolution, and punishable for fraud under Section 447. The words the section uses are \"notwithstanding that the company has been notified as dissolved\". The dissolution does not protect them. It is one of the facts used against them. We have a separate walkthrough of <a href=\"/article/striking-off-company-stk-2\">strike-off under STK-2</a>, including when it is the right thing to do and when it is a trap.</p>"

     "<p><strong>Section 447</strong> is the provision Rohan should have read before he signed the STK-2 declaration. Fraud, defined in the Explanation to include any act, omission, concealment of a fact or abuse of position committed with intent to deceive or to gain undue advantage or to injure the interests of the company, its creditors or any other person, whether or not there is any wrongful gain or loss. Where the amount involved is at least ten lakh rupees or one per cent of turnover, whichever is lower, the punishment is imprisonment of not less than six months extending to ten years, with a fine of not less than the amount involved and up to three times that amount. The gap between the eighteen lakh he paid and the 1.1 crore the looms were worth clears the threshold on its own.</p>"

     "<p><strong>Section 339</strong> is the one people mean when they say the veil is lifted. Mehta Fabrics applied to the Tribunal to restore Meridian's name under Section 252, and once the company is back on the register and in winding up, Section 339 becomes available. The trigger is a finding that any business of the company was carried on with intent to defraud creditors, or for any fraudulent purpose. The Tribunal can then declare that a person who is or has been a director, manager or officer of the company, or anyone knowingly party to it, \"shall be personally responsible, without any limitation of liability, for all or any of the debts or other liabilities of the company as the Tribunal may direct\". Without any limitation of liability. That is the whole protection, removed by order. Sub-section (3) adds that everyone knowingly party to it is separately liable under Section 447.</p>"

     "<p><strong>Section 340</strong> covers the softer version, where there is no fraud but a director has misapplied or retained company money or been guilty of misfeasance or breach of trust. The Tribunal can order him to repay it with interest. The application has to be made within five years of the winding up order or of the misapplication, whichever is longer.</p>"

     "<p>If Meridian had gone into insolvency under the IBC instead, the equivalent is Section 66. Sub-section (1) mirrors fraudulent trading. Sub-section (2) is the one directors underestimate: a director can be ordered to contribute personally where, before the insolvency commencement date, he knew or ought to have known that there was no reasonable prospect of avoiding insolvency proceedings, and he did not exercise due diligence in minimising the potential loss to creditors. Rohan had known since early 2024. He kept trading anyway, on hope. Under Section 66(2) hope is not a defence, and the Explanation measures him against what would reasonably be expected of a person carrying out the same functions.</p>"

     "<p>There is also the small, sharp provision that catches a very common act. Under <strong>Section 452</strong>, an officer of a company who wrongfully obtains possession of company property including cash, or having it, wrongfully withholds it or knowingly applies it for purposes other than those authorised, is punishable with a fine of one to five lakh rupees. The court may also order him to hand the property back within a fixed time, failing which he can be imprisoned for up to two years. And Section 166(5) says a director who makes any undue gain for himself or his relatives is liable to pay the company an amount equal to that gain. Money moving from a company to the people who run it is regulated well before it becomes fraud, which is what <a href=\"/article/section-185-loan-to-directors\">Section 185 on loans to directors</a> exists to do.</p>"

     "<h2>Three directors, three different mornings</h2>"

     "<p>Now the part that decides how the story ends for each of them, because the veil does not come off evenly.</p>"

     "<p><strong>Rohan</strong> is exposed on every front and there is no serious argument otherwise. He was managing director, he signed the cheques, he moved the assets, he filed the strike-off application. Section 166 sets out what a director is supposed to do: act in good faith to promote the objects of the company for the benefit of its members as a whole and in the best interests of the company, its employees, the shareholders and the community; exercise due and reasonable care, skill and diligence; avoid conflicts of interest; and take no undue gain. He breached all of it, and Section 166(7) alone carries a fine of one to five lakh rupees before anything else is counted.</p>"

     "<p><strong>Anjali</strong> is in a harder place than she expects. She did not steal anything. But she was a whole-time director, she countersigned two of the bounced cheques, she prepared the accounts, and she was the officer charged with the filings that did not happen. Section 2(60) names her twice over. The PF and GST provisions ask her to prove she was not grossly negligent, and the fact that she knew the deductions were being made and the money was not going out makes that proof hard to produce. Her best argument is on the cheques she did not sign, and even there Section 141(2) reaches a director where the offence was committed with her consent or connivance or is attributable to her neglect.</p>"

     "<p><strong>Vikram</strong> is the interesting one. He is caught by Section 164(2), which does not care what he knew. He is not caught by most of the rest, and the reason is worth understanding.</p>"

     "<p>Section 149(12) says that an independent director, and a non-executive director who is not a promoter or key managerial personnel, is liable only for acts of omission or commission by the company which occurred with his knowledge, attributable through Board processes, and with his consent or connivance, or where he had not acted diligently. Vikram is a nominee non-executive director and not a promoter, so he sits inside that protection for anything that never reached the Board.</p>"

     "<p>On the criminal side, the Supreme Court in <em>Sunil Bharti Mittal v CBI</em> (9 January 2015) put it plainly: \"It is the cardinal principle of criminal jurisprudence that there is no vicarious liability unless the statute specifically provides so.\" A director can be made an accused where there is sufficient evidence of his active role together with criminal intent, or where a statute expressly creates vicarious liability. Holding the office is not, by itself, either of those things.</p>"

     "<p>On the cheques, <em>Ashok Shewakramani v State of Andhra Pradesh</em> (3 August 2023) is directly useful. The Court held that the words \"was in charge of\" and \"was responsible to the company for the conduct of the business\" in Section 141(1) must be read conjunctively, both together, and that merely because somebody is managing the affairs of the company he does not automatically become in charge of the conduct of its business. A complaint that says nothing about what a particular director actually did will not stand.</p>"

     "<p>So Vikram loses his directorships for five years over a filing default he did not know about, and walks away from the fraud. Both of those outcomes come from the same body of law, which tells you something about how it is built. If you sit on a board you did not build, our note on <a href=\"/article/independent-directors-companies-act\">independent directors under the Companies Act</a> is the companion piece.</p>"

     "<h2>What courts actually do with the veil itself</h2>"

     "<p>Everything above came from statutes. The judge-made doctrine, where a court simply looks through the company at the people behind it, exists in India but is used sparingly.</p>"

     "<p>In <em>Balwant Rai Saluja v Air India Ltd</em> (25 August 2014) the Supreme Court refused to treat canteen workers employed by Air India's wholly owned subsidiary as Air India's own employees. Ownership and control were not enough. Summarising the position at paragraph 71, the Court said the doctrine of piercing the veil allows a court to disregard the separate legal personality of a company only where it is evident that the company was a mere camouflage or sham deliberately created for the purpose of avoiding liability, and that the principle has been and should be applied in a restrictive manner. A parent company does not become liable for its subsidiary just because it owns it.</p>"

     "<p>Where the corporate form is genuinely being used as a device, courts do move. In <em>Delhi Development Authority v Skipper Construction Co (P) Ltd</em>, the promoters had sold the same unbuilt office space to multiple buyers through a web of family companies. The Supreme Court lifted the veil and treated the properties held across those entities and family members as one estate available to satisfy the claims, and the promoters' personal assets went with it.</p>"

     "<p>Put the two cases side by side and the rule is fairly clear. Control is not enough. Loss is not enough. Impropriety in the use of the company, linked to avoiding or concealing a liability, is what moves a court. And even then, most Indian directors who end up paying personally do so because Section 164, Section 339, Section 89 of the CGST Act or Section 141 of the NI Act named them, not because a judge invoked a doctrine.</p>"

     "<h2>Common mistakes</h2>"

     "<ul>"
     "<li><strong>Treating the company's bank account as a personal float.</strong> Paying household expenses out of the company account is not a tax question, it is Section 452 and Section 166(5), and it is the single most common piece of evidence used to argue the company was never treated as separate.</li>"
     "<li><strong>Assuming a dormant company is a safe company.</strong> Stopping filings is what triggers Section 164(2). A company that is doing nothing still has to say so, every year, on time. See <a href=\"/article/annual-compliance-companies\">annual compliance for companies</a> for the actual list.</li>"
     "<li><strong>Believing that resigning fixes it.</strong> Section 164(2), Section 89 of the CGST Act and Section 323 of the Income-tax Act 2025 all attach to the period during which you were a director. Resigning stops the clock going forward. It does not erase what is behind you.</li>"
     "<li><strong>Using PF, ESI, TDS and GST as working capital.</strong> That money was collected from someone else. Every one of those statutes has a director-liability clause, and none of them accepts cash flow as an answer.</li>"
     "<li><strong>Signing board minutes you did not read.</strong> Section 2(60)(vi) makes a director an officer in default where the contravention was in the Board papers he received and he did not object. Minutes are the record of what you knew.</li>"
     "<li><strong>Striking off a company to escape its creditors.</strong> Section 251 was written for that exact move, and it survives the dissolution.</li>"
     "</ul>"

     "<h2>What would have kept the veil on</h2>"

     "<p>Almost nothing in this story required money that Meridian did not have.</p>"

     "<p>The filings were the cheapest thing on the list and the omission that did the most damage: three years of silence cost all three directors five years of disqualification, including one who had done nothing wrong. Keeping statutory dues current would have removed four separate personal-liability provisions from the picture, even if trade creditors had to wait. Recording the Northgate default and the board's decision to keep trading, with dates and reasoning, is what a director points to under Section 66(2) of the IBC when asked whether he exercised due diligence in minimising loss to creditors, and Meridian's minute book had a two-line entry for the whole of 2024. Our guide to <a href=\"/article/drafting-maintaining-minutes-section-118\">drafting and maintaining minutes under Section 118</a> covers what that record is supposed to contain.</p>"

     "<p>And when Rohan decided in January 2026 to move the looms, that was the moment a lawyer would have earned their fee. An orderly insolvency, with the assets sold under supervision at a valuation, would have left the directors as people who ran a business into the ground. What he did instead made them people who took something. Those are treated very differently, and the difference is roughly the distance between losing your shareholding and Section 447.</p>"

     "<p>For the underlying obligations that sit behind all of this, our guide to <a href=\"/article/director-duties\">the duties of directors</a> covers Section 166 in detail.</p>"

     "<h2>Frequently asked questions</h2>"

     "<p><strong>Is Meridian Weaves a real company?</strong> No. The company, the people, the dates and every rupee figure in the narrative are invented for teaching. Every section number, penalty, threshold and judgment cited is real and was checked against the bare Act or the judgment itself.</p>"

     "<p><strong>Does the corporate veil protect me if my business simply fails?</strong> Yes, and that is its main job. If you traded honestly, kept the company's money separate, filed what you were required to file and stopped when there was no reasonable prospect of continuing, the company's debts stay the company's debts. Shareholders lose their capital and creditors take the loss. That is the bargain limited liability was created to strike.</p>"

     "<p><strong>What is the difference between lifting the veil and a personal guarantee?</strong> A personal guarantee is a contract you signed, promising to pay if the company does not. Nobody has to lift anything to enforce it. Lifting the veil is a court or a statute reaching a director who never agreed to be liable. Most founders who lose their house lose it to a guarantee, not to a doctrine.</p>"

     "<p><strong>Can I be disqualified as a director without doing anything wrong?</strong> Yes. Section 164(2)(a) disqualifies every director of a company that has not filed financial statements or annual returns for three continuous financial years, for five years, whether or not that director knew. It is automatic and it follows you into your other companies through the proviso to Section 167(1)(a).</p>"

     "<p><strong>Am I safer as a non-executive or nominee director?</strong> Somewhat, and only for some things. Section 149(12) limits the liability of an independent director and of a non-executive director who is not a promoter or KMP to acts that occurred with his knowledge through Board processes, or with his consent or connivance, or where he did not act diligently. It does not touch Section 164(2), and it does not help if the matter was in your Board papers and you said nothing.</p>"

     "<p><strong>Does striking off the company end the directors' liability?</strong> No. Section 251 makes the persons in charge of the management jointly and severally liable for loss caused by the dissolution, and punishable under Section 447, where the strike-off application was made to evade liabilities or deceive creditors. A creditor can also apply under Section 252 to have the company restored to the register.</p>"

     "<p><strong>What is the difference between Section 339 of the Companies Act and Section 66 of the IBC?</strong> Section 339 applies in a winding up under the Companies Act and lets the Tribunal declare a director personally responsible without limitation of liability for the company's debts. Section 66 applies in insolvency proceedings under the IBC and lets the Adjudicating Authority order a contribution to the corporate debtor's assets, including under Section 66(2) where the director kept trading knowing there was no reasonable prospect of avoiding insolvency.</p>"

     "<p><strong>If the company owes GST and income tax, can the department come after me directly?</strong> If it is a private company and the dues cannot be recovered from the company, yes. Section 89(1) of the CGST Act and Section 323 of the Income-tax Act 2025 both make every director of the relevant period jointly and severally liable unless the director proves the non-recovery cannot be attributed to any gross neglect, misfeasance or breach of duty on his part. The burden is on the director, not on the department.</p>"),

]
