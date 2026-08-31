# Weekly news-driven article, 30 August 2026.
#
# Topic picked from what people were actually reading this month: SEBI's final
# order against Zee Entertainment, Punit Goenka and Subhash Chandra over the
# unauthorised pledge of ZEEL's Hyderabad land. The order itself is dated 31
# July 2026, made public around 1-3 August, but coverage was still active
# through the month (the SAT appeal, the interim relief on the warrant issue)
# and it remains the live corporate-governance story with a document behind
# it. Checked against the existing 150 published slugs first (via `SELECT
# slug, title, category FROM articles WHERE published=1`) — the site already
# has a Subhash Chandra article (subhash-chandra-nclt-order-personal-guarantee)
# but that covers his personal insolvency plan under the IBC, a different
# matter, different Act, different tribunal. No article on the site covers
# SEBI's related-party/LODR enforcement machinery through a live case study.
#
# Verified against the primary source, not secondary coverage: the actual
# 150-page SEBI order, fetched directly as a PDF from
# https://www.sebi.gov.in/sebi_data/attachdocs/aug-2026/1785554147160.pdf
# (linked from the order's listing page at sebi.gov.in/enforcement/orders/
# jul-2026/final-order-in-the-matter-of-unauthorised-pledge-of-immovable-
# property-of-zee-entertainment-enterprises-ltd-_103299.html). Every figure,
# date, regulation citation and finding below is read directly from that PDF,
# paragraph numbers noted in REVIEW-BEFORE-PUBLISH.md. The post-order SAT
# developments (the appeal, the interim relief on the warrant issue) are not
# in the SEBI order itself and are attributed in-text to the outlets that
# reported them (Business Standard, India Legal), not folded into the site's
# own voice.
#
# Format matches the earlier seeds: (title, slug, category, act, read_time,
# summary, content).
BLOG_ARTICLES_17 = [

    ("SEBI Bars Punit Goenka and Subhash Chandra for a Year: What the ₹726 Crore Zee Land-Pledge Order Actually Found",
     'sebi-bars-goenka-chandra-zee-land-pledge-order',
     'sebi',
     'SEBI Act, 1992 & LODR Regulations, 2015',
     '9 min read',
     "SEBI has barred Subhash Chandra and Punit Goenka from the securities market for a year and fined the two of them and Zee Entertainment ₹1.48 crore, over a Hyderabad plot pledged to secure ₹726 crore in loans to companies linked to the Chandra family, without board or shareholder approval. What the 150-page order found, and what most of the coverage left out.",
     "<p><em>A company's land can end up as collateral for a loan its own board never approved. Often the first outside sign is one flagged line in an auditor's report. That is roughly how Zee Entertainment's Hyderabad land pledge came to light. The regulator has now spent 150 pages explaining what happened next.</em></p>"
     "<p><strong>SEBI has barred Subhash Chandra and Punit Goenka, Zee Entertainment's former chairman and former MD and CEO, from the securities market for a year each. It has also fined the two of them and Zee ₹1.48 crore in total. The penalty covers a Hyderabad plot that Chandra pledged to secure ₹726 crore in loans for companies his own family controlled, without the board's approval.</strong></p>"
     "<blockquote><p>SEBI's order is dated 31 July 2026. It restrains Zee Entertainment from the securities market for two months, and Chandra and Goenka for twelve months each. It fines Zee ₹30 lakh, Goenka ₹58 lakh and Chandra ₹60 lakh. Of that, ₹30 lakh on Goenka and ₹40 lakh on Chandra is specifically for fraud under the SEBI Act. Zee's own penalty carries no fraud finding, only disclosure and governance lapses. The order does not decide any criminal case, and it does not order anyone compensated for the land's use. A separate arbitration over the same property is still pending before the Delhi High Court.</p></blockquote>"

     "<h2>What actually got pledged, and to whom</h2>"
     "<p>The land at the centre of the case sits on Road No. 78, Jubilee Hills, in Shaikpet village, Hyderabad. It measures 17,639.64 square metres and belongs to Zee Entertainment Enterprises Ltd (ZEEL). In December 2016, four companies in the Essel Group took loans from Indiabulls Housing Finance Ltd (IHFL): Gnex Projects, Vivek Infracon, Gnex Infrabuild and Renu Realtech. Together the four loans added up to ₹726 crore, with Essel Home Private Ltd as co-borrower. SEBI's investigation traced the ownership of these borrowing companies back, through several corporate layers, to Chandra's own family.</p>"
     "<p>By late 2018, IHFL wanted more security for those loans. On 27 December 2018, Chandra signed a document called a Declaration and Acknowledgment on ZEEL's behalf. He was then the company's non-executive chairman. The document handed IHFL the original title deeds to the Hyderabad land. It recorded a first-ranking mortgage over ZEEL's own property. The loans it secured were not ZEEL's. They benefited companies that Chandra's own family ultimately controlled.</p>"

     "<h2>The approval nobody signed off on</h2>"
     "<p>SEBI's investigators looked for a prior approval from ZEEL's audit committee, its board, or its shareholders. None existed. Under Regulation 23(2) of the <a href=\"/article/sebi-lodr-explained\">SEBI LODR Regulations</a>, a transaction like this needs the <a href=\"/article/board-committees-audit-nrc-stakeholders\">audit committee's</a> sign-off before it happens, not after. That is because the borrowing companies counted as related parties of ZEEL. Their ownership traced back to Chandra's family and to the company's own key managerial personnel. The Companies Act has a similar rule for related-party transactions generally; we cover that separately in our <a href=\"/article/related-party-transactions-section-188\">guide to Section 188 approvals</a>. This case turned on the SEBI listing-regulation version of the same idea.</p>"
     "<p>The document Chandra signed said the opposite of what the investigation found. Clause 18 of the 2018 declaration stated that ZEEL had \"obtained all requisite permissions and approvals\" for the mortgage. SEBI's order calls that declaration incorrect. Investigators later asked ZEEL about it directly, in an email dated 10 April 2024. The company said its own management and board had no knowledge the mortgage had happened at all. That is directly at odds with what Chandra had told the lender six years earlier.</p>"

     "<h2>How the missing title deeds came to light</h2>"
     "<p>ZEEL's statutory auditor, Deloitte Haskins and Sells, filed its CARO report on 17 May 2019. It said the original title deeds to a ZEEL property could not be located. That property was the same Hyderabad land already sitting with IHFL.</p>"
     "<p>On the same date, Goenka signed a management representation letter to the auditors, in his capacity as MD and CEO. It stated that ZEEL's assets carried no liens or encumbrances. SEBI found he already knew about the mortgage when he signed it. That was one part of a wider problem. Goenka had separately signed CEO-CFO certificates for FY 2018-19 and FY 2019-20, stating that ZEEL's financial statements did not omit any material fact. He held knowledge of the unauthorised mortgage when he signed both. SEBI found the certificates false, a violation of Regulation 17(8) of the LODR Regulations.</p>"
     "<p>There was more ZEEL didn't tell the exchanges. IHFL had gone to the Delhi High Court under Section 9 of the Arbitration and Conciliation Act, seeking to protect its security over the land. The court granted interim protection on 1 May 2019. ZEEL never disclosed that litigation to the stock exchanges. It stayed quiet later too, when it gave IHFL a non-disposal undertaking over the property, and when IHFL finally released the title deeds on 1 June 2020.</p>"

     "<h2>Why SEBI called it fraud, not just a disclosure lapse</h2>"
     "<p>Most of the violations SEBI found sit under the LODR Regulations. These are disclosure and governance failures, penalised under Sections 15A(b) and 15HB of the SEBI Act. Against Goenka and Chandra personally, SEBI went further. It found they had violated Section 12A of the SEBI Act and the Prohibition of Fraudulent and Unfair Trade Practices Regulations, 2003. SEBI's order is direct about it: Chandra, as chairman, \"misused his position and authority\" and put ZEEL's asset \"at risk for his personal benefit\" — which the order calls \"abuse of position and authority for personal benefit while risking the interest of the listed company and its shareholders.\"</p>"
     "<p>That fraud finding, and its separate penalty under Section 15HA, applies only to Chandra and Goenka. Zee Entertainment's own ₹30 lakh penalty is entirely for LODR violations, the missing audit-committee approval and the disclosure failures. It carries no fraud finding.</p>"

     "<h2>What the order found that most of the coverage didn't mention</h2>"
     "<p>One distinction shaped the size of the individual penalties, and most of the coverage skipped it. SEBI held that Goenka and Chandra could not be held personally liable for ZEEL's original failure to disclose the December 2018 mortgage. The reason is technical. Section 27 of the SEBI Act fixes personal liability on officers for a company's contravention. But the version of Section 27 of the SEBI Act that applies here was amended after December 2018. The amended version cannot apply retrospectively, to an event that happened before it existed.</p>"
     "<p>But that let-off was narrow. SEBI held both men liable for a separate, later failure, under the post-amendment Section 27 of the SEBI Act. From March 2019 onward, ZEEL stayed silent about several material developments: the Delhi High Court litigation, the non-disposal undertaking, and the eventual release of the title deeds. The company never told its shareholders about any of them. The original pledge escaped one liability on a technicality. The years of silence that followed it did not.</p>"

     "<h2>What Zee and Goenka did next</h2>"
     "<p>Zee Entertainment and Goenka took the order to the Securities Appellate Tribunal, or SAT. Business Standard reported that the matter was heard on 12 August 2026. SAT questioned SEBI's basis for the two-month market restriction on ZEEL specifically. By the middle of August, it had granted partial interim relief. According to India Legal, SAT allowed ZEEL to go ahead with a pending preferential warrant issue to a promoter-group entity, worth roughly ₹3,143.5 crore. The condition: ZEEL and Goenka first had to deposit their SEBI penalties — ₹30 lakh and ₹58 lakh — within a week. That relief covers one specific transaction. It is not a ruling on the underlying appeal, which was still pending as this was written.</p>"
     "<p>Throughout this, ZEEL's shares kept trading normally on the exchanges. The stock moved sharply on the news, both times. The debarment stops Zee, Goenka and Chandra themselves from dealing in or accessing the securities market. It does not halt other investors from buying or selling ZEEL shares already listed.</p>"

     "<h2>Common mistakes boards make with related-party transactions</h2>"
     "<ul>"
     "<li>Treating a declaration signed by one director as board or audit-committee approval. Regulation 23(2) needs the committee's own sign-off before the transaction, not a signatory's word afterward.</li>"
     "<li>Signing a CEO-CFO certificate as a yearly formality, without checking what the finance and legal teams actually know about pending litigation or encumbrances.</li>"
     "<li>Deciding a pending arbitration isn't material because it hasn't produced a final order yet. SEBI treated the interim relief itself, and its eventual settlement, as disclosable events in their own right.</li>"
     "<li>Assuming a related company's borrowing is none of the listed parent's concern, when the parent's own title documents are what secure the loan.</li>"
     "</ul>"

     "<h2>Frequently asked questions</h2>"
     "<p><strong>Does this SEBI order find Subhash Chandra or Punit Goenka guilty of a crime?</strong> No. It is a civil and regulatory order under the SEBI Act, imposing monetary penalties and market debarment. A criminal conviction would need separate proceedings under different law, which this order does not touch.</p>"
     "<p><strong>Can investors still buy or sell Zee Entertainment shares during the ban?</strong> Yes. The debarment stops Zee, Goenka and Chandra themselves from dealing in or accessing the securities market. It does not stop other investors from trading ZEEL's already-listed shares on the exchanges.</p>"
     "<p><strong>Does the order remove Chandra or Goenka as directors of Zee?</strong> No. SEBI's directions bar them from the securities market for a fixed period. They say nothing about removing anyone from a directorship. That is a separate question under company law, which this order does not address.</p>"
     "<p><strong>How much of the ₹1.48 crore penalty is specifically for fraud?</strong> ₹30 lakh of Goenka's ₹58 lakh is for fraud, under Section 12A of the SEBI Act and the PFUTP Regulations. So is ₹40 lakh of Chandra's ₹60 lakh. The rest of their penalties, and all of Zee's ₹30 lakh, is for disclosure and governance violations under the LODR Regulations.</p>"
     "<p><strong>Is this related to Subhash Chandra's personal insolvency case before the NCLT?</strong> No. That is a separate proceeding, under a different law, over personal guarantees Chandra gave to a different set of lenders. We cover it in our <a href=\"/article/subhash-chandra-nclt-order-personal-guarantee\">report on the NCLT order</a>. This SEBI order is about ZEEL's own listing-regulation and disclosure duties as a company.</p>"),

]
