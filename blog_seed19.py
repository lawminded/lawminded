# Weekly news-driven article, 4 September 2026.
#
# Topic picked from the news: the Supreme Court's 2 September 2026 ruling in
# Kotak Mahindra Bank Ltd v Trupti Sanjay Mehta (2026 INSC 943), which legal
# press covered within a day (LiveLaw, Verdictum, KNN India, HelloBanker,
# LawTrend, AdvocateKhoj). Checked instance/lawminded.db first; nothing on the
# site already covers SARFAESI, debt assignment or NBFC-to-bank loan transfers.
#
# Verified against: the SARFAESI Act's own text for Sections 2(1)(c), 2(1)(m),
# 13(2)-(4) and 17 (fetched from ibclaw.in's bare-act pages, since indiacode.nic.in
# and the SC's own PDF host both refused direct fetches, the same 403 pattern
# notes.md records for mca.gov.in); and the judgment's holding, paragraph
# numbers and per-appeal disposition, cross-checked across four independent
# legal-reporting sources (LiveLaw's case digest, Verdictum, AdvocateKhoj's
# full-text republication, and IndianKanoon's docket page) that agree on the
# citation, bench, facts, quoted paragraphs and outcome for each of the three
# connected matters.
#
# Format matches the earlier seeds: (title, slug, category, act, read_time,
# summary, content).
BLOG_ARTICLES_19 = [

    ("Your NBFC Loan Was Sold to a Bank? The Supreme Court Says SARFAESI Comes With It",
     'sarfaesi-nbfc-loan-sold-to-bank-supreme-court',
     'property',
     'SARFAESI Act, 2002',
     '10 min read',
     "The Supreme Court ruled on 2 September 2026 that a bank can use SARFAESI's fast-track recovery on a loan it bought from an NBFC, even if that NBFC was never covered by the Act. Three borrowers challenged this. Two lost outright; one got a partial win most headlines missed.",
     "<p><em>If you ever borrowed from a housing finance company or an NBFC, there is a good chance your loan has since been sold to a bank without you doing anything at all. Whether that sale hands the bank extra recovery powers you didn't sign up for was, until this month, a genuinely open question.</em></p>"
     "<p><strong>The Supreme Court has now held that it does: once a bank covered by the SARFAESI Act acquires a non-performing secured loan, the loan gets SARFAESI's fast-track recovery powers attached to it, regardless of who the original lender was.</strong></p>"

     "<blockquote><p><strong>The bottom line:</strong> a bank that buys a bad loan from an NBFC not covered by SARFAESI can still invoke the Act against the borrower, because the loan takes on the bank's status the moment it changes hands. What isn't settled is whether the bank wins the individual recovery case; one of the three linked matters here was sent back for a full hearing, with the borrowers made to deposit Rs 25 lakh in the meantime. And none of it touches a loan that stayed with an NBFC never assigned to a covered institution. That loan is still outside SARFAESI.</p></blockquote>"

     "<h2>What the case was actually about</h2>"
     "<p>The case is <strong>Kotak Mahindra Bank Ltd v Trupti Sanjay Mehta and connected matters</strong>, decided on 2 September 2026 by Justices Sanjay Kumar and Sanjeev Sachdeva (2026 INSC 943). It combines three separate disputes, all following the same pattern.</p>"
     "<p>Between 2012 and 2013, Kotak Mahindra Bank bought a set of loan accounts from City Financial Consumer Finance Limited, an NBFC. One loan of about Rs 69.60 lakh had funded a home purchase. Another involved Poorti Rent a Car, on a loan of roughly Rs 2.98 crore. A third involved a family called the Sables. All three loans turned bad, and the bank tried to recover them under the SARFAESI Act.</p>"
     "<p>The borrowers pushed back with one argument in each case: at the time these loans were made, City Financial was not a \"financial institution\" recognised under the SARFAESI Act. It only received that recognition in August 2018, years after Kotak had already bought the accounts. If the original lender never had SARFAESI powers, they argued, buying the loan shouldn't manufacture powers that never existed.</p>"
     "<p>The Bombay High Court agreed with the borrowers. The Supreme Court did not.</p>"

     "<h2>Why it matters whether your lender is a \"financial institution\"</h2>"
     "<p>SARFAESI is not the ordinary route for recovering a debt. A lender outside the Act has to sue you, get a decree, and then execute it, a process that can run for years. SARFAESI skips most of that for lenders who qualify.</p>"
     "<p>Section 2(1)(c) of the Act defines a \"bank\" to include banking companies and the State Bank of India. Section 2(1)(m) defines \"financial institution\" to include public financial institutions and any NBFC the Central Government has separately notified for the purpose. Only a bank or a notified financial institution can use SARFAESI. An ordinary NBFC that hasn't been notified cannot, however large its loan book.</p>"
     "<p>City Financial was in that second category when these loans were made: an NBFC, but not a notified one. The dispute was whether a sale to a bank that <em>is</em> covered changes that.</p>"

     "<h2>What Section 13 actually lets a covered lender do</h2>"
     "<p>This is worth spelling out, because it is the entire reason the borrowers fought this hard. Under Section 13(2), once your loan account is classified as a non-performing asset, the lender can give you sixty days' written notice to pay in full. Miss that window, and Section 13(4) lets the lender take possession of the mortgaged property, take over its management, or sell it, without first going to a civil court for permission.</p>"
     "<p>Your only recourse at that stage is Section 17: an application to the Debt Recovery Tribunal, and you have forty-five days from the date the lender takes action to file it. That is a narrow door compared with a full civil suit, which is exactly why it matters so much whether a given loan sits inside or outside the Act.</p>"

     "<h2>The Court's reasoning</h2>"
     "<p>The bench rejected the idea that a loan's SARFAESI status is frozen at the moment it is created. In its words, once a claim is \"live and owing\" and later comes to be held by an institution the Act already covers, \"the provisions thereof would be available, as and when it becomes applicable to the institution holding that loan account.\" Acquisition by a covered bank, the Court said, immediately \"clothes\" a non-performing loan with the attributes of a secured debt under SARFAESI.</p>"
     "<p>The Court also went after the borrowers' underlying argument directly, and this is the line most coverage skipped. Accepting their position, it said, would mean that \"those who avail financial assistance from NBFCs not covered\" by the Act would \"enjoy greater freedom to commit default in repayment\" than someone who happened to borrow from a bank in the first place. The identity of the original lender was not something a court should let determine how seriously a borrower needs to take a default.</p>"

     "<h2>The detail most headlines dropped</h2>"
     "<p>Nearly every report on this judgment led with a single line: banks can use SARFAESI on loans bought from NBFCs. That is accurate, but it describes only the legal principle, not what actually happened to the three borrowers who fought the case.</p>"
     "<p>The Mehtas' matter was not simply decided against them. The Supreme Court set aside the Bombay High Court's 2015 judgment and sent their case back to the Debt Recovery Tribunal, to be heard on its facts. As a condition, the Mehtas were directed to deposit Rs 25 lakh with the bank within eight weeks, without prejudice to the final outcome. They lost the legal argument about whether SARFAESI applies at all, but they have not yet lost the case.</p>"
     "<p>The Sables fared worse, though for a different reason. Their own application to the Debt Recovery Tribunal had already been dismissed for delay, so the bank's right to invoke Section 14 and take physical possession stood regardless of the SARFAESI question. And in the Poorti Rent a Car matter, the secured property had already been sold by the time the case reached the Supreme Court. There was nothing left to decide.</p>"
     "<p>Three appeals, three different outcomes, and only one of them a clean win for the bank on the facts. The \"banks can now do this\" headline is true of the law. It is not true of every borrower who was in this exact position.</p>"

     "<h2>What this means if your loan started with an NBFC</h2>"
     "<p>Loan sales between lenders happen constantly and rarely need your consent under the loan agreement you signed. A bank buying a distressed loan book from an NBFC, a housing finance company, or an asset reconstruction company is routine. It happens under the Reserve Bank of India's own framework for selling non-performing assets between regulated lenders.</p>"
     "<p>Until this ruling, a borrower whose original lender was not SARFAESI-notified had a real argument that the buyer couldn't invoke the Act either. That argument is now gone. If your account is transferred to a bank or a notified financial institution, treat a SARFAESI notice from the new lender exactly as you would from your original one. Read the sixty-day window carefully. If you intend to contest it, get your Section 17 application to the DRT filed within forty-five days of any action taken against you, not forty-five days from the notice itself.</p>"
     "<p>What has <em>not</em> changed: if your loan is still held by an NBFC that has never been separately notified, SARFAESI does not apply to it at all, no matter how the lender behaves. The trigger is a sale to a covered institution, not merely the passage of time or the size of the default.</p>"

     "<h2>Common mistakes</h2>"
     "<ul>"
     "<li><strong>Assuming a SARFAESI notice from a new lender is invalid</strong> because your original loan predates that lender's involvement. It is not, once the loan has been acquired by a covered bank.</li>"
     "<li><strong>Waiting out the sixty-day notice</strong> hoping the transfer itself is challengeable. This judgment closes that specific door.</li>"
     "<li><strong>Missing the forty-five day Section 17 window</strong> because it is counted from the bank's action, not from when you first learned about the sale. A related point on limitation periods generally is covered in <a href=\"/article/limitation-act-1963-guide\">the Limitation Act guide</a>.</li>"
     "<li><strong>Treating an NBFC loan as permanently outside SARFAESI.</strong> That is true only for as long as the loan stays with an uncovered lender.</li>"
     "<li><strong>Confusing this with property title risk generally.</strong> A SARFAESI notice is about an existing mortgage on the property you already own or are buying into, not a title defect. If you are checking a property before purchase, <a href=\"/article/property-title-due-diligence\">separate due diligence</a> still applies.</li>"
     "</ul>"

     "<h2>Frequently asked questions</h2>"
     "<p><strong>What is the SARFAESI Act, in plain terms?</strong> It lets certain lenders (banks and specifically notified financial institutions) recover secured debts by taking possession of and selling the mortgaged property, without first suing you in a civil court.</p>"
     "<p><strong>Does it matter if my loan started with an NBFC rather than a bank?</strong> It used to be arguable. After this judgment, it does not, provided the NBFC's loan has since been bought by a bank or a notified financial institution.</p>"
     "<p><strong>How much notice does a lender have to give before acting?</strong> Sixty days, under Section 13(2), once the account is classified as non-performing.</p>"
     "<p><strong>What can the lender do if I miss the sixty days?</strong> Under Section 13(4), take possession of the mortgaged property, take over its management, or sell it.</p>"
     "<p><strong>How do I challenge a SARFAESI action?</strong> File an application with the Debt Recovery Tribunal under Section 17, within forty-five days of the date the lender takes action against you.</p>"
     "<p><strong>What did the Supreme Court actually decide on 2 September 2026?</strong> That a bank acquiring a bad loan from an NBFC not covered by SARFAESI can still use the Act, because the loan takes on SARFAESI status the moment a covered institution holds it.</p>"
     "<p><strong>Did the borrowers lose completely?</strong> Not all of them. The Mehtas' case was sent back to the Debt Recovery Tribunal for a hearing on the merits, with a Rs 25 lakh deposit ordered in the meantime. The Sables and Poorti Rent a Car lost for reasons specific to their own cases.</p>"
     "<p><strong>Does this apply to loans that are still held by the original NBFC?</strong> No. An NBFC that has never been notified under Section 2(1)(m) cannot use SARFAESI, regardless of how large or old the default is.</p>"),

]
