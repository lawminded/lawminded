# One news-driven article written 14 August 2026, verified against the actual
# bill text (Bill No. LXXII of 2026, "as introduced in the Rajya Sabha on the
# 28th July, 2026", fetched from prsindia.org) rather than secondary summaries
# of it. Two rounds of secondary-source fetching produced conflicting penalty
# figures and invented classification thresholds that aren't in the bill at
# all (they belong to the existing 2020 classification notification, which
# this bill does not alter); the article below is checked clause-by-clause
# against the primary PDF instead.
#
# The underlying event: Parliament passed the Micro, Small and Medium
# Enterprises Development (Amendment) Bill, 2026 — Rajya Sabha on 3 August,
# Lok Sabha on 7 August. As of 14 August 2026 it has not received Presidential
# assent and no commencement notification has been issued, so none of it is
# in force. The article says that plainly and dates every "once notified"
# claim back to the bill's own clauses, rather than reporting it as already
# live the way several secondary write-ups did.
#
# Checked against the existing 132 published articles first. The site already
# has 'msme-udyam-registration-guide' (registration process, current Section
# 16 delayed-payment interest rule) and 'msme-1-half-yearly-return' (the
# existing half-yearly disclosure return) — both describe law that is still
# in force unchanged by this bill, so this is a new, forward-looking article
# rather than an update to either.
#
# Format matches the earlier seeds: (title, slug, category, act, read_time,
# summary, content).

BLOG_ARTICLES_8 = [

    ('The MSME Amendment Bill Has Cleared Parliament: What Changes for Delayed Payments, and What Doesn\'t Yet',
     'msme-development-amendment-bill-2026',
     'contracts',
     'MSMED Act, 2006',
     '7 min read',
     'Parliament passed the MSME Development (Amendment) Bill, 2026 in the first week of August: a guaranteed 50% payout when a buyer contests an award, 90-day mediation and arbitration deadlines, and a mandatory TReDS route for government buyers. It still needs presidential assent and a notification before any of it applies.',
     "<p><em>If you run a small business and a large company has ever sat on your invoice for months while you paid your own suppliers and salaries on time, this bill was written with you in mind. None of it is law yet, and knowing exactly what stage it's at matters more than the headlines suggest.</em></p>"
     "<p><strong>Parliament passed the MSME Development (Amendment) Bill, 2026 in the first week of August. Once it receives the President's assent and the government notifies it, buyers who contest a payment award will have to hand over at least half the disputed amount if their court challenge drags on past six months, mediation and arbitration will run to fixed 90-day clocks, and every central government enterprise will have to route MSME payments through a single electronic platform. As of today, none of it is in force.</strong></p>"
     "<blockquote><p><strong>The bottom line</strong></p>"
     "<p><strong>What it costs:</strong> nothing to an MSME supplier. The cost lands on buyers, through a mandatory partial payout during disputes and a tougher penalty scale for non-disclosure and false registration information.</p>"
     "<p><strong>What it covers:</strong> payment disputes referred to a Micro and Small Enterprises Facilitation Council, and every Central Public Sector Enterprise buying goods or services from an MSME.</p>"
     "<p><strong>What it does not fix:</strong> nothing changes today. The Bill needs Presidential assent and a commencement notification before any clause takes effect, and the existing 45-day payment rule under Section 16 of the MSMED Act is untouched either way.</p></blockquote>"

     "<h2>What Parliament actually passed, and what still has to happen</h2>"
     "<p>The Bill was introduced in the Rajya Sabha on 28 July 2026 by Jitan Ram Manjhi, the Minister of Micro, Small and Medium Enterprises. The Rajya Sabha passed it on 3 August, and the Lok Sabha followed on 7 August. That clears Parliament, but an Act only takes effect once the President signs it and the Central Government issues a commencement notification in the Official Gazette — and the Bill gives the government room to notify different provisions on different dates rather than switching the whole Act on at once. Neither had happened as of 14 August 2026, though several early write-ups described the changes as though a supplier could already invoke the new 90-day clock. They can't, yet. What follows is what changes once each provision is switched on.</p>"

     "<h2>The new floor: a guaranteed payout when a buyer fights the award</h2>"
     "<p>A buyer who wants to challenge an arbitral award or a Facilitation Council decision in court must first deposit 75% of the award amount — that rule isn't new. What happens to that deposit while the case is pending is where the Bill changes things. Currently, a court can order part of it paid out to the supplier if it thinks that's reasonable, but there's no floor: it can just as easily order nothing paid out until the case is decided, which can take years.</p>"
     "<p>The Bill adds one. Once notified, if the buyer's application to set aside the award has been pending for more than six months, the court must order at least 50% of the awarded amount released to the supplier. Say a small enterprise wins an award of Rs. 10 lakh and the buyer deposits 75%, or Rs. 7.5 lakh, to contest it. If the challenge is still pending after six months, the court has to release at least Rs. 5 lakh regardless of how the underlying dispute eventually turns out — a partial win now instead of an uncertain full win years later.</p>"

     "<h2>Faster clocks for mediation and arbitration</h2>"
     "<p>Payment disputes under the MSMED Act go through a Facilitation Council: first mediation, and if that fails, arbitration. Mediation currently runs on the general timelines in the Mediation Act, 2023. The Bill carves MSME payment disputes out of that and sets its own: the Council or mediation provider must complete mediation within 90 days of the first appearance. If mediation fails and the matter goes to arbitration, a second clock applies — the award must be made within 90 days of the pleadings being completed, once notified. That's worth comparing to ordinary commercial arbitration: under Section 29A of the Arbitration and Conciliation Act, 1996, a tribunal ordinarily gets twelve months from completion of pleadings, extendable by six with the parties' consent. MSME disputes get a quarter of that.</p>"

     "<h2>Getting paid by the government: the TReDS mandate</h2>"
     "<p>A new Section 15A requires every Central Public Sector Enterprise to route its settlement of MSME invoices through a Trade Receivables Discounting System (TReDS) platform authorised by the RBI, once notified. TReDS is the electronic platform that already lets an MSME sell its unpaid invoices to a financier at a discount instead of waiting out the credit period; it exists today, but using it has been optional. The Central Government can extend the mandate to other notified bodies, and State Governments may separately require it of their own public sector enterprises, though states aren't obliged to. None of this touches private buyers.</p>"

     "<h2>Udyam registration gets simpler, not stricter</h2>"
     "<p>The current law is more layered than most people assume: filing for <a href=\"/article/msme-udyam-registration-guide\">Udyam registration</a> is optional for a micro or small enterprise and for a medium enterprise providing services, but mandatory, with a 180-day filing window, for a medium enterprise engaged in manufacturing. The Bill replaces that with one rule — a national digital platform for free, voluntary registration open to every micro, small and medium enterprise, with no carve-out that forces any category to register. States get the option to run a parallel state platform for their own benefits. None of this changes what registering gets you; it only changes who is required to do it, which after notification will be nobody.</p>"

     "<h2>Penalties move from criminal fines to graded civil penalties</h2>"
     "<p>Right now, giving false information on a Udyam memorandum, or a buyer failing to disclose overdue MSME dues in its accounts, is a criminal offence carrying a fine on conviction: up to Rs. 1,000 for a first conviction and up to Rs. 10,000 thereafter for the registration offence, and a flat fine of at least Rs. 10,000 for non-disclosure. The Bill decriminalises both. In their place: a warning for a first violation, then an escalating penalty imposed by an adjudicating officer rather than a court.</p>"
     "<p>For false registration information, the penalty on a second or later violation runs from Rs. 1,000 up to Rs. 50,000. For non-disclosure the scale is steeper: a warning the first time, Rs. 10,000 to Rs. 50,000 the second, and Rs. 50,000 to Rs. 1 lakh from the third violation onward. All these minimums rise by 10% every three years from commencement. The Bill names the Development Commissioner, the senior official heading that office within the Ministry of MSME, as the adjudicating officer, with a right of appeal to the Ministry's Secretary within 30 days, to be decided within 60.</p>"

     "<h2>What this Bill doesn't touch</h2>"
     "<p>Three things stay exactly as they are. The current classification thresholds — micro up to Rs. 1 crore investment and Rs. 5 crore turnover, small up to Rs. 10 crore and Rs. 50 crore, medium up to Rs. 50 crore and Rs. 250 crore — are untouched; the Bill only changes how future thresholds get set, moving that power into a general notification, and a savings clause keeps every existing one in force until it's actually revised. The underlying 45-day payment rule and the compound-interest penalty at three times the RBI bank rate under Sections 15 and 16, the core protection described in our Udyam registration guide above, is not amended at all. And the existing <a href=\"/article/msme-1-half-yearly-return\">MSME Form 1 half-yearly return</a>, which companies file to report payments overdue past 45 days, is a Companies Act obligation that sits outside this Bill entirely.</p>"

     "<h2>Common mistakes to avoid right now</h2>"
     "<ul><li>Citing the 90-day mediation or arbitration clock, or the 50% deposit rule, in a legal notice or Facilitation Council filing today. Until notified, the older Mediation Act and general arbitration timelines still apply.</li>"
     "<li>Assuming Udyam registration has already become optional for a medium manufacturing enterprise that was previously required to file. The current Section 8, with its 180-day mandatory window for that category, stays in force until the amended section is specifically notified.</li>"
     "<li>Treating the TReDS mandate as something a private-sector buyer now has to comply with. It runs to Central Public Sector Enterprises and whatever the Centre separately notifies, not to ordinary private companies.</li></ul>"

     "<h2>What to do while you wait</h2>"
     "<p>If you supply goods or services as a registered MSME, your existing rights haven't changed: the 45-day rule and the 3x bank rate interest penalty under Section 16 already apply, and a Facilitation Council reference is already available if a buyer is stalling. If you're not registered on Udyam, that's unaffected by this Bill and remains free, so there's no reason to wait for the amendment to sign up. If you're a large company or CPSE buying from MSME suppliers, review how your accounts team currently discloses overdue MSME dues under Section 22 — the requirement isn't new, but getting it wrong is about to get considerably more expensive.</p>"

     "<h2>Frequently asked questions</h2>"
     "<p><strong>Is the MSME Development (Amendment) Bill, 2026 already law?</strong> No. Parliament passed it on 7 August 2026, but it still needs the President's assent and a Central Government notification before any provision takes effect, and different provisions can be notified on different dates.</p>"
     "<p><strong>Does this change the existing 45-day payment rule for MSME suppliers?</strong> No. Sections 15 and 16 of the MSMED Act, which set the 45-day payment period and the compound interest penalty at three times the RBI bank rate, are not amended by this Bill.</p>"
     "<p><strong>What is the new 50% rule everyone is talking about?</strong> Once notified, if a buyer's court application to set aside a payment award is pending for more than six months, the court must order at least 50% of the awarded amount paid to the supplier out of the 75% deposit the buyer was already required to make to file that application.</p>"
     "<p><strong>Will Udyam registration become compulsory or stay voluntary?</strong> It becomes voluntary for every category, including medium manufacturing enterprises, which currently have a mandatory 180-day filing window. That change takes effect only once the relevant section is notified.</p>"
     "<p><strong>Does the TReDS mandate apply to private companies?</strong> No. It applies to Central Public Sector Enterprises and any other body the Central Government separately notifies. States may extend an equivalent requirement to their own public sector enterprises, but private buyers aren't covered.</p>"
     "<p><strong>What happens if a buyer still doesn't disclose overdue MSME dues after this Bill is notified?</strong> A first violation draws a warning, a second a penalty of Rs. 10,000 to Rs. 50,000, and a third or later violation Rs. 50,000 to Rs. 1 lakh, imposed by the Development Commissioner rather than a criminal court. These minimums rise by 10% every three years from commencement.</p>"),

]
