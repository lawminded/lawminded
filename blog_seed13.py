# Owner-requested case study, 26 August 2026 (asked for by name over Telegram:
# "a detailed case study with all the fictional characters and setup for
# understanding the corporate veil and how on directors default it will be
# removed").
#
# Revised 26 August 2026 on the owner's feedback: the first draft read as legal
# writing rather than plain English, and the personal-guarantee thread was
# confusing readers by sitting next to veil-lifting without being the same thing.
# The guarantee is gone entirely, and the prose was rewritten in shorter
# sentences with every legal term explained the first time it appears. No section
# number, penalty, threshold, date or rupee figure changed in the rewrite.
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

     "<p><em>Most founders are told the same thing when they set up a private limited company: if the business goes under, your home and your savings stay out of it. That is broadly true, and it is most of the reason companies exist at all. What nobody explains is where the protection stops. It stops far more quietly than you would expect. So here is a company that never existed, run by three people who never existed, under law that is entirely real.</em></p>"

     "<p><strong>The company protects you when a business fails honestly. That protection goes when directors default, and it usually goes piece by piece, through tax, labour and cheque laws that name directors directly, rather than through a judge announcing that the company was a sham.</strong></p>"

     "<blockquote><p><strong>The bottom line</strong></p>"
     "<p><strong>What it covers:</strong> debts the company ran up in its own name while the directors were acting honestly. Shareholders lose the money they put in, and nothing beyond that.</p>"
     "<p><strong>What it does not cover:</strong> money the company collected from someone else and kept, such as PF or GST; cheques a director signed; and assets moved out of a creditor's reach.</p>"
     "<p><strong>What losing it costs:</strong> Section 339 of the Companies Act can make a director personally liable for the company's debts, with no upper limit. Section 164(2) bans him from being a director anywhere for five years. Section 447 is fraud, and it carries up to ten years in jail.</p></blockquote>"

     "<h2>The company, and the people in it</h2>"

     "<p>Meridian Weaves Private Limited was incorporated on 4 March 2019 at Bhiwandi, Maharashtra. Power looms, mostly grey fabric for two garment buyers in Tiruppur. Fifteen lakh rupees of capital, put in by three shareholders.</p>"

     "<p><strong>Rohan Deshmukh</strong> holds 60 per cent and is the managing director. He runs the floor, deals with the buyers, and signs almost everything.</p>"

     "<p><strong>Anjali Rao</strong> holds 25 per cent. She is a whole-time director, which means a director who also works in the company full time, and she looks after the accounts. She is the second signatory on the bank account and she prepares the numbers the auditor sees.</p>"

     "<p><strong>Vikram Sethi</strong> represents the family office that put in the remaining 15 per cent. He is a non-executive director: he sits on the board but does not work in the business. Four board meetings a year over video, a question about receivables, and he has never been to Bhiwandi.</p>"

     "<p>Two other people matter later. <strong>Priya Nair</strong> is the company's auditor. <strong>Mehta Fabrics</strong> is a yarn supplier in Ichalkaranji that had given Meridian credit for four years without a single late payment.</p>"

     "<h2>Act one: the company doing exactly what it is meant to do</h2>"

     "<p>By FY 2021-22 Meridian was doing 9.6 crore rupees of business a year, with 41 workers on its rolls. The bank gave it a working capital limit of 2.4 crore, with the looms pledged as security.</p>"

     "<p>In August 2023 Northgate Retail, which took roughly a third of Meridian's output, stopped paying. One crore eighty lakh went unpaid, and then Northgate's own lenders moved in. Meridian never saw the money. It could not pay Mehta Fabrics, could not service the bank, and by early 2024 it was insolvent in any practical sense.</p>"

     "<p>So what could Mehta Fabrics do to Rohan personally at that point? Nothing. Section 9 of the Companies Act says that from the date on the incorporation certificate, the company becomes a person in its own right in the eyes of the law. It can own property, sign contracts, and sue and be sued in its own name. The debt belonged to Meridian. Rohan owned most of Meridian, but he was not Meridian. That gap between a company and the people who own it is what lawyers call the corporate veil, and it is really just a curtain. The company stands in front. The people stand behind.</p>"

     "<p>This is the oldest rule in company law and it comes from an English case decided in 1896, <em>Salomon v A Salomon &amp; Co Ltd</em>. Aron Salomon turned his leather business into a company he almost entirely owned. When it collapsed, the unsecured creditors argued that he should pay them himself, because the company was really just him. The House of Lords said no. \"The company is at law a different person altogether from the subscribers to the memorandum,\" Lord Macnaghten wrote: the same people may run it and the same hands may take the profits, but the company is not their agent and does not hold its property in trust for them. Indian courts have been quoting that line ever since.</p>"

     "<p>Had the story ended there, Meridian's directors would have lost their shareholding and nothing else. A business failed. That is allowed.</p>"

     "<h2>The first crack, and no fraud anywhere in sight</h2>"

     "<p>Meridian's last filing with the Registrar of Companies was for FY 2021-22. After Northgate defaulted, the annual return (Form MGT-7) and the accounts (Form AOC-4) simply stopped going in, for FY 2022-23, then 2023-24, then 2024-25. Nobody decided to hide anything. There was no money for the company secretary's fee and there were louder fires to put out.</p>"

     "<p>This is where most founders get it wrong. They assume a late-filing penalty lands on the company, and that if the company has no money, that is the end of the matter. Section 92(5) says otherwise. Miss the deadline for the annual return, and the penalty falls on the company <em>and on every officer of it who is in default</em>. Ten thousand rupees each, plus a hundred rupees for every further day. It stops at two lakh for the company and fifty thousand for the officer. Section 137(3) does the same for the accounts, and it names the managing director and the chief financial officer by title.</p>"

     "<p>\"Officer who is in default\" is not a loose phrase. Section 2(60) sets out exactly who it catches, and it is worth going through slowly, because this is the list that decides who pays out of their own pocket. It covers any whole-time director. It covers key managerial personnel, the law's term for the managing director, the chief executive, the chief financial officer and the company secretary. It covers anyone working under the board who was put in charge of the accounts or the filings and knowingly did nothing to stop the default. And clause (vi) covers any director who knew about the breach because it came up in the board papers he received, and who sat through the meeting without objecting.</p>"

     "<p>So the penalty is not the company's alone. It is Rohan's and Anjali's, out of their own money. No court has disregarded the company here. The veil is technically intact. The statute has simply walked around it.</p>"

     "<p>Then, in September 2025, something worse happened, and it happened by itself. Section 164(2)(a) deals with a company that has not filed its accounts or annual returns for three financial years in a row. Anyone who is or has been a director of that company cannot be reappointed there, and cannot be appointed a director of any other company, for five years. There is no notice, no hearing, and nothing for anyone to decide. Three years of silence, and the disqualification simply exists.</p>"

     "<p>Vikram Sethi found out when an unrelated company he sat on tried to file a form and his DIN, the director identification number every director holds, came back deactivated. A proviso to Section 167(1)(a), which is a short rider attached to the main rule, then does the rest: he loses his seat on every board except the one that actually defaulted. He had never seen a rupee of Meridian's money and had no idea the filings had lapsed. He was caught anyway, because Section 164(2) attaches to the fact of being a director, not to anything he did. Our guide to <a href=\"/article/din-allotment-kyc-disqualification\">DIN, KYC and director disqualification</a> covers what happens next and how narrow the ways out are.</p>"

     "<h2>The month a bad year turns into a default</h2>"

     "<p>Through late 2025 Rohan kept the looms running on the belief that one large order would fix everything. To do it, he used money that was never Meridian's to use.</p>"

     "<p><strong>Provident fund.</strong> Meridian cut the employees' share of PF from 41 workers' wages for nine months and never deposited it. About 4.7 lakh rupees. Section 14A of the Employees' Provident Funds and Miscellaneous Provisions Act, 1952 covers what happens next. When a company commits an offence under that Act, the people who were in charge of the business are treated as guilty along with the company. Sub-section (2) goes further. Any director or manager who agreed to it, quietly went along with it (the Act calls that connivance), or was simply careless enough to let it happen is guilty too. There is a way out, but it is narrow, and it is not \"the company had no cash\". The director has to show the offence happened without his knowledge, or that he did everything he reasonably could to stop it.</p>"

     "<p><strong>GST.</strong> Meridian charged GST on its invoices, collected it from its customers, and stopped paying it over. Section 89(1) of the CGST Act, 2017 begins by saying it applies whatever the Companies Act says. Say GST, interest or penalty is owed by a private company and cannot be recovered from the company. Every person who was a director in that period is then liable, jointly and severally. That phrase matters: the department can recover the whole amount from any one of them, not a share each. A director escapes only if he proves the failure to recover cannot be put down to serious carelessness, misuse of his position or breach of duty on his part. Notice who has to prove what. The department does not have to show the director was careless. The director has to show he was not.</p>"

     "<p><strong>Income tax.</strong> The same structure again, in Section 323 of the Income-tax Act, 2025, which replaced Section 179 of the old 1961 Act. Where tax owed by a private company cannot be recovered, everyone who was a director at any point in that tax year is jointly and severally liable, on the same terms. And \"tax due\" is defined widely: it takes in penalty, interest, fees and any other sum payable under the Act. This section also opens by overriding the Companies Act, which tells you the drafting was deliberate.</p>"

     "<p><strong>Cheques.</strong> In November and December 2025 Rohan wrote three cheques to Mehta Fabrics for 22 lakh rupees in total, knowing the account could not cover them. Anjali countersigned two. All three bounced. Section 138 of the Negotiable Instruments Act, 1881 makes that an offence carrying up to two years in jail, or a fine of up to twice the cheque amount, or both. Section 141 then extends it to \"every person who, at the time the offence was committed, was in charge of, and was responsible to, the company for the conduct of the business of the company\". For the procedure and the notice deadlines, we have a full guide to <a href=\"/article/cheque-bounce-section-138-ni-act\">cheque bounce under Section 138</a>.</p>"

     "<p>Notice what those four laws have in common. Not one of them asks a court to pretend Meridian does not exist. Each one simply says: the company owes this, and so does the person who was running the company. That is how directors are actually reached in India, far more often than by the doctrine everybody has heard of.</p>"

     "<h2>The looms move, and the company applies to disappear</h2>"

     "<p>What Rohan did in January 2026 was a different kind of act.</p>"

     "<p>He incorporated Vasant Looms Private Limited at the same Bhiwandi address, with his brother-in-law and an employee as its two directors. Meridian then sold its looms to Vasant for eighteen lakh rupees. In Meridian's own books, after depreciation, those looms were worth 1.1 crore. The workers came in on Monday to the same machines under a new name. In March, Rohan applied under Section 248(2) to have Meridian's name struck off the register, and the company was notified as dissolved.</p>"

     "<p>He thought that was the end of it. It was the beginning.</p>"

     "<p><strong>Section 251</strong> was written for precisely this move. It applies where an application to strike a company off was made to escape the company's liabilities, or to deceive its creditors, or to defraud anyone else. Where that is found, the people who were running the company become personally liable, jointly and severally, to anyone who lost money because the company was dissolved, and they can be prosecuted for fraud under Section 447. The section says this applies \"notwithstanding that the company has been notified as dissolved\". The dissolution does not protect them. It becomes one of the facts used against them. We have a separate walkthrough of <a href=\"/article/striking-off-company-stk-2\">strike-off under STK-2</a>, including when it is the right thing to do and when it is a trap.</p>"

     "<p><strong>Section 447</strong> is the one Rohan should have read before he signed the strike-off declaration. Fraud is defined broadly there. Any act, omission, hiding of a fact or misuse of a position, done with intent to deceive, to gain an unfair advantage, or to harm the company, its creditors or anyone else. It counts whether or not anybody actually gained or lost. The punishment applies where the amount involved is at least ten lakh rupees, or one per cent of turnover, whichever is lower. It is a minimum of six months in jail and a maximum of ten years, with a fine of at least the amount involved and up to three times that. The gap between the eighteen lakh Rohan paid and the 1.1 crore the looms were worth clears that threshold on its own.</p>"

     "<p><strong>Section 339</strong> is the one people actually mean when they say the veil has been lifted. Mehta Fabrics applied to the National Company Law Tribunal under Section 252 to have Meridian's name put back on the register. Once the company is back and in winding up, Section 339 becomes available. The trigger is a finding that the company's business was carried on with intent to defraud creditors, or for any fraudulent purpose. The Tribunal can then declare that anyone who is or was a director, manager or officer, or anyone who knowingly took part, \"shall be personally responsible, without any limitation of liability, for all or any of the debts or other liabilities of the company as the Tribunal may direct\". Without any limitation of liability. That is the whole protection, removed by an order. Sub-section (3) adds that everyone knowingly involved is separately liable under Section 447.</p>"

     "<p><strong>Section 340</strong> is the milder version, for cases with no fraud in them, where a director has misused or held on to the company's money, or otherwise broken the trust placed in him. The Tribunal can order him to pay it back with interest. The application has to be made within five years of the winding up order or of the misuse, whichever period is longer.</p>"

     "<p>Had Meridian gone into insolvency under the IBC instead, the equivalent is Section 66. Sub-section (1) mirrors fraudulent trading. Sub-section (2) is the one directors underestimate. A director can be ordered to pay into the company's pot if two things are true. Before the insolvency began, he knew or ought to have known there was no reasonable prospect of avoiding it. And he did not do what he could to keep the losses to creditors down. Rohan had known since early 2024. He kept trading on hope. Under Section 66(2) hope is not a defence, and the Explanation judges him against what could reasonably be expected of someone doing his job.</p>"

     "<p>There is also a small, sharp provision that catches a very common act. Take <strong>Section 452</strong>. An officer of a company who wrongly takes company property including cash, or holds on to it, or knowingly spends it on something it was not meant for, faces a fine of one to five lakh rupees. The court can also order him to hand the property back by a fixed date, and jail him for up to two years if he does not. Section 166(5) adds that a director who makes an unfair gain for himself or his relatives has to pay the company an amount equal to that gain. Money moving from a company to the people who run it is regulated long before it becomes fraud, which is what <a href=\"/article/section-185-loan-to-directors\">Section 185 on loans to directors</a> is for.</p>"

     "<h2>Three directors, three different mornings</h2>"

     "<p>Now the part that decides how this ends for each of them, because the protection does not come off evenly.</p>"

     "<p><strong>Rohan</strong> is exposed on every front, and there is no serious argument the other way. He was the managing director. He signed the cheques, he moved the assets, he filed the strike-off application. Section 166 sets out what a director is supposed to do. Act in good faith, for the company's objects, and in the best interests of the company, its employees, its shareholders and the community. Take due and reasonable care. Stay out of conflicts of interest. Take no unfair gain. He breached all of it, and Section 166(7) on its own carries a fine of one to five lakh rupees before anything else is counted.</p>"

     "<p><strong>Anjali</strong> is in a worse position than she expects. She stole nothing. But she was a whole-time director, she countersigned two of the bounced cheques, she prepared the accounts, and she was the officer responsible for the filings that never happened. Section 2(60) catches her twice over. The PF and GST provisions ask her to prove she was not seriously careless, and she knew the PF was being cut from wages while the money was not going out, which makes that proof very hard to produce. Her best argument is on the cheque she did not sign, and even there Section 141(2) reaches a director where the offence happened with her agreement or connivance, or because she was careless.</p>"

     "<p><strong>Vikram</strong> is the interesting one. Section 164(2) catches him and does not care what he knew. Most of the rest does not touch him, and the reason is worth understanding.</p>"

     "<p>Section 149(12) protects two kinds of director: an independent director, and a non-executive director who is neither a promoter nor key managerial personnel. They answer only for what the company did or failed to do where it happened with their knowledge and reached them through board processes, or where they agreed to it or went along with it, or where they did not act diligently. Vikram is a non-executive nominee and not a promoter. So he sits inside that protection for anything that never reached the board.</p>"

     "<p>On the criminal side, the Supreme Court in <em>Sunil Bharti Mittal v CBI</em> (9 January 2015) put it plainly: \"It is the cardinal principle of criminal jurisprudence that there is no vicarious liability unless the statute specifically provides so.\" Vicarious liability means being punished for what somebody else did. A director can be made an accused where there is real evidence that he took an active part and meant to, or where a statute expressly says directors are liable. Simply holding the office is neither of those.</p>"

     "<p>On the cheques, <em>Ashok Shewakramani v State of Andhra Pradesh</em> (3 August 2023) is directly useful. Section 141(1) catches a person who \"was in charge of\" the business and who \"was responsible to the company for the conduct of the business\". The Court held that both of those have to be true, not one or the other, and that a person does not become in charge of the conduct of the business merely because he manages the company's affairs. A complaint that says nothing about what a particular director actually did will not stand.</p>"

     "<p>So Vikram loses his directorships for five years over a filing default he never heard about, and walks away from the fraud. Both of those outcomes come out of the same body of law, which tells you something about how it is built. If you sit on a board you did not build, our note on <a href=\"/article/independent-directors-companies-act\">independent directors under the Companies Act</a> is the companion piece.</p>"

     "<h2>What courts actually do with the veil itself</h2>"

     "<p>Everything above came from statutes. The judge-made doctrine, where a court simply looks past the company at the people behind it, does exist in India, but it is used sparingly.</p>"

     "<p>In <em>Balwant Rai Saluja v Air India Ltd</em> (25 August 2014) the Supreme Court refused to treat canteen workers employed by a wholly owned Air India subsidiary as Air India's own employees. Owning and controlling the subsidiary was not enough. Summing up at paragraph 71, the Court set the bar. A court may disregard a company's separate legal personality only where it is clear the company was a mere camouflage or sham, deliberately created to avoid a liability. And the principle has been, and should be, applied restrictively. A parent company does not become liable for its subsidiary just because it owns it.</p>"

     "<p>Where the company form really is being used as a device, courts do move. In <em>Delhi Development Authority v Skipper Construction Co (P) Ltd</em>, the promoters had sold the same unbuilt office space to several buyers at once, through a web of family companies. The Supreme Court lifted the veil, treated the properties held across those companies and family members as a single pot available to pay the claims, and the promoters' personal assets went into it.</p>"

     "<p>Put the two cases side by side and the rule is reasonably clear. Control is not enough. Somebody losing money is not enough. What moves a court is the company being misused to dodge or hide a liability. And even then, most Indian directors who end up paying personally do so because Section 164, Section 339, Section 89 of the CGST Act or Section 141 of the NI Act named them, not because a judge reached for a doctrine.</p>"

     "<h2>Common mistakes</h2>"

     "<ul>"
     "<li><strong>Treating the company's bank account as a personal wallet.</strong> Paying household bills out of the company account is not just a tax question. It is Section 452 and Section 166(5), and it is the single most common piece of evidence used to argue the company was never really treated as separate.</li>"
     "<li><strong>Assuming a dormant company is a safe company.</strong> Stopping the filings is what triggers Section 164(2). A company that is doing nothing still has to say so, every year, on time. See <a href=\"/article/annual-compliance-companies\">annual compliance for companies</a> for the actual list.</li>"
     "<li><strong>Believing that resigning fixes it.</strong> Section 164(2), Section 89 of the CGST Act and Section 323 of the Income-tax Act 2025 all attach to the period when you were a director. Resigning stops the clock going forward. It does not wipe out what is behind you.</li>"
     "<li><strong>Using PF, ESI, TDS and GST as working capital.</strong> That money was collected from somebody else. Every one of those laws has a director-liability clause, and none of them treats a cash crunch as an answer.</li>"
     "<li><strong>Signing board minutes you have not read.</strong> Section 2(60)(vi) makes a director an officer in default where the breach was in the board papers he received and he said nothing. The minutes are the record of what you knew.</li>"
     "<li><strong>Striking off a company to get away from its creditors.</strong> Section 251 exists for exactly that move, and it survives the dissolution.</li>"
     "</ul>"

     "<h2>What would have kept the protection in place</h2>"

     "<p>Almost nothing in this story needed money Meridian did not have.</p>"

     "<p>The filings were the cheapest item on the list and the omission that did the most damage: three years of silence cost all three directors five years of disqualification, one of them for something he never knew about. Keeping the statutory dues paid would have taken four separate personal-liability provisions off the board, even if the trade creditors had to wait. And the board should have written down the Northgate default and its decision to keep trading, with dates and reasons. That record is exactly what a director points to under Section 66(2) of the IBC, when he is asked whether he did what he could to limit the loss to creditors. Meridian's minute book had a two-line entry for the whole of 2024. Our guide to <a href=\"/article/drafting-maintaining-minutes-section-118\">drafting and maintaining minutes under Section 118</a> covers what that record is supposed to contain.</p>"

     "<p>And when Rohan decided in January 2026 to move the looms, that was the moment a lawyer would have earned their fee. A proper insolvency, with the assets sold under supervision at a valuation, would have left the three of them as people who ran a business into the ground. What he did instead made them people who took something. The law treats those two very differently, and the difference is roughly the distance between losing your shareholding and Section 447.</p>"

     "<p>For the duties sitting behind all of this, our guide to <a href=\"/article/director-duties\">the duties of directors</a> covers Section 166 in detail.</p>"

     "<h2>Frequently asked questions</h2>"

     "<p><strong>Is Meridian Weaves a real company?</strong> No. The company, the people, the dates and every rupee figure in the story are invented to teach the law. Every section number, penalty, threshold and judgment quoted is real and was checked against the bare Act or the judgment itself.</p>"

     "<p><strong>Does the company still protect me if my business simply fails?</strong> Yes, and that is its main job. If you traded honestly, kept the company's money separate from your own, filed what you were required to file and stopped when there was no reasonable prospect of carrying on, the company's debts stay the company's debts. Shareholders lose their capital and creditors take the loss. That is the bargain limited liability was built to strike.</p>"

     "<p><strong>Can I be disqualified as a director without doing anything wrong?</strong> Yes. Section 164(2)(a) disqualifies every director of a company that has not filed its accounts or annual returns for three financial years in a row, for five years, whether or not that director knew. It is automatic, and it follows you into your other companies through a proviso to Section 167(1)(a).</p>"

     "<p><strong>Am I safer as a non-executive or nominee director?</strong> Somewhat, and only for some things. Section 149(12) covers an independent director, and a non-executive director who is neither a promoter nor key managerial personnel. It limits what they answer for to things that happened with their knowledge through board processes, or that they agreed to or went along with, or where they did not act diligently. It does nothing about Section 164(2), and it does not help if the matter was in your board papers and you kept quiet.</p>"

     "<p><strong>Does striking off the company end the directors' liability?</strong> No. Where the strike-off application was made to escape liabilities or to deceive creditors, Section 251 makes the people running the company jointly and severally liable for the loss the dissolution caused, and open to prosecution under Section 447. A creditor can also apply under Section 252 to have the company restored to the register.</p>"

     "<p><strong>What is the difference between Section 339 of the Companies Act and Section 66 of the IBC?</strong> Section 339 applies in a winding up under the Companies Act and lets the Tribunal declare a director personally responsible for the company's debts without any limit. Section 66 applies in insolvency under the IBC and lets the Adjudicating Authority, which is the NCLT again, order a director to pay money into the company's assets. That includes Section 66(2), where he kept trading knowing there was no reasonable prospect of avoiding insolvency.</p>"

     "<p><strong>If the company owes GST and income tax, can the department come after me directly?</strong> If it is a private company and the money cannot be recovered from the company, yes. Section 89(1) of the CGST Act and Section 323 of the Income-tax Act 2025 both make every director of that period jointly and severally liable. The only escape is to prove that the failure to recover cannot be put down to serious carelessness, misuse of position or breach of duty on his part. The burden sits on the director, not on the department.</p>"),

]
