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
     "<p><em>If you run a small business and a large company has ever sat on your invoice for months while you paid your own suppliers and staff on time, this bill was written for you. None of it is law yet. Knowing exactly what stage it's at matters more than the headlines suggest.</em></p>"
     "<p><strong>Parliament passed the MSME Development (Amendment) Bill, 2026 in the first week of August. Once the President signs it and the government notifies it, a buyer who fights a payment award in court will have to hand over at least half the disputed amount if the case drags on past six months. Mediation and arbitration will have to finish within 90 days. And every central government company will have to pay its MSME suppliers through one electronic platform. As of today, none of this is in force.</strong></p>"
     "<blockquote><p><strong>The bottom line</strong></p>"
     "<p><strong>What it costs:</strong> nothing for an MSME supplier. The cost falls on buyers, through a compulsory partial payout during disputes and stricter penalties for hiding overdue dues or giving false registration details.</p>"
     "<p><strong>What it covers:</strong> payment disputes taken to a Micro and Small Enterprises Facilitation Council, and every Central Public Sector Enterprise that buys goods or services from an MSME.</p>"
     "<p><strong>What it does not fix:</strong> nothing changes today. The Bill still needs the President's assent and an official notification before any part of it applies, and the existing 45-day payment rule under Section 16 of the MSMED Act stays exactly as it is either way.</p></blockquote>"

     "<h2>What Parliament actually passed, and what still has to happen</h2>"
     "<p>The Bill was introduced in the Rajya Sabha on 28 July 2026 by Jitan Ram Manjhi, the Minister of Micro, Small and Medium Enterprises. The Rajya Sabha passed it on 3 August, and the Lok Sabha passed it on 7 August. That clears Parliament. But a Bill only becomes law once the President signs it and the government publishes a notification saying when it starts, and different sections can start on different dates. Neither had happened as of 14 August 2026, though some early news reports described the changes as if a supplier could already use the new 90-day clock. They can't, yet. Everything below is what changes once each part is switched on.</p>"

     "<h2>The new floor: a guaranteed payout when a buyer fights the award</h2>"
     "<p>A buyer who wants to challenge a payment award in court, whether it came from arbitration or from a Facilitation Council, must first deposit 75% of the award amount. That rule already exists. What happens to that money while the case is pending is what the Bill changes. Right now, a court can order some of it paid to the supplier if it wants to, but there's no minimum: it can just as easily order nothing paid out until the case is fully decided, and that can take years.</p>"
     "<p>The Bill fixes a minimum. Once notified, if the buyer's case has been pending for more than six months, the court must release at least 50% of the award to the supplier. Say a small business wins an award of Rs. 10 lakh, and the buyer deposits 75%, or Rs. 7.5 lakh, to contest it. If the case is still pending after six months, the court has to hand over at least Rs. 5 lakh, whatever happens to the case later. That's a partial win now, instead of an uncertain full win years from now.</p>"

     "<h2>Faster clocks for mediation and arbitration</h2>"
     "<p>Payment disputes under the MSMED Act go through a Facilitation Council. It tries mediation first, and if that fails, the case moves to arbitration. Mediation currently follows the general timelines set by the Mediation Act, 2023. The Bill gives MSME payment disputes their own, shorter clock instead: mediation must finish within 90 days of the first hearing. If mediation fails and the case goes to arbitration, a second clock applies once notified: the arbitrator must give an award within 90 days of both sides finishing their submissions. Compare that to ordinary commercial arbitration, where Section 29A of the Arbitration and Conciliation Act, 1996 gives a tribunal twelve months from that same point, extendable by six more if both sides agree. MSME disputes get a quarter of that time.</p>"

     "<h2>Getting paid by the government: the TReDS mandate</h2>"
     "<p>A new Section 15A will require every Central Public Sector Enterprise to pay its MSME suppliers through a Trade Receivables Discounting System, or TReDS, platform approved by the RBI, once notified. TReDS already exists: it lets an MSME sell an unpaid invoice to a financier at a discount instead of waiting out the full credit period, but using it has been optional so far. The central government can extend this requirement to other government bodies, and states can choose to apply it to their own public sector companies too, though they don't have to. None of this touches private buyers.</p>"

     "<h2>Udyam registration gets simpler, not stricter</h2>"
     "<p>The current rule is more complicated than most people assume. Filing for <a href=\"/article/msme-udyam-registration-guide\">Udyam registration</a> is optional for a micro or small business, and for a medium business that provides services. But it's compulsory, with a 180-day deadline, for a medium business that manufactures goods. The Bill scraps all of that and replaces it with one rule: a free, voluntary national platform, open to every micro, small and medium business, with no exception that forces any category to register. States can also run their own parallel platform for their own schemes. Registering still gets you the same benefits as before; the only thing changing is that, once notified, nobody will be required to do it.</p>"

     "<h2>Penalties move from criminal fines to graded civil penalties</h2>"
     "<p>Right now, giving false information on a Udyam application, or a buyer failing to disclose overdue MSME dues in its accounts, is a criminal offence. It carries a fine on conviction: up to Rs. 1,000 for a first offence and up to Rs. 10,000 after that for the registration offence, and a flat fine of at least Rs. 10,000 for hiding overdue dues. The Bill takes both out of the criminal courts. In their place: a warning for a first offence, then a penalty that rises each time, decided by an official rather than a judge.</p>"
     "<p>For false registration details, a second or later offence draws a penalty of Rs. 1,000 to Rs. 50,000. Hiding overdue dues is punished more heavily: a warning the first time, Rs. 10,000 to Rs. 50,000 the second time, and Rs. 50,000 to Rs. 1 lakh from the third offence onward. These minimums rise by 10% every three years after the law starts. The Development Commissioner, the senior officer heading that office within the Ministry of MSME, decides these cases. Anyone penalised can appeal to the Ministry's Secretary within 30 days, and the appeal must be decided within 60.</p>"

     "<h2>What this Bill doesn't touch</h2>"
     "<p>Three things stay exactly as they are. The current size limits for classifying a business as micro, small or medium — micro up to Rs. 1 crore invested and Rs. 5 crore turnover, small up to Rs. 10 crore and Rs. 50 crore, medium up to Rs. 50 crore and Rs. 250 crore — don't change. The Bill only changes how future limits get set, by giving the government a general power to notify new ones, and keeps today's limits in force until that happens. The core protection for suppliers, the 45-day payment rule and the interest penalty at three times the RBI's bank rate under Sections 15 and 16 (covered in our Udyam registration guide above), isn't touched at all. And the existing <a href=\"/article/msme-1-half-yearly-return\">MSME Form 1 half-yearly return</a>, filed to report payments overdue past 45 days, comes from the Companies Act and has nothing to do with this Bill.</p>"

     "<h2>Common mistakes to avoid right now</h2>"
     "<ul><li>Citing the 90-day mediation or arbitration deadline, or the 50% deposit rule, in a legal notice or a Facilitation Council filing today. Until these sections are notified, the older Mediation Act timelines and general arbitration rules still apply.</li>"
     "<li>Assuming Udyam registration is already optional for a medium manufacturing business that used to be required to register. The current Section 8, with its 180-day compulsory window for that category, stays in force until the new section is specifically notified.</li>"
     "<li>Treating the TReDS mandate as something a private company already has to follow. It applies to Central Public Sector Enterprises and whatever else the Centre separately notifies, not to ordinary private businesses.</li></ul>"

     "<h2>What to do while you wait</h2>"
     "<p>If you supply goods or services as a registered MSME, nothing about your existing rights has changed: the 45-day rule and the 3x bank rate interest penalty under Section 16 already apply, and you can already take a stalling buyer to a Facilitation Council. If you haven't registered on Udyam yet, this Bill doesn't affect that either — registration is still free, so there's no reason to wait for the amendment before signing up. If you run a large company or a CPSE that buys from MSME suppliers, check now how your accounts team discloses overdue MSME dues under Section 22. That requirement isn't new, but getting it wrong is about to cost a lot more.</p>"

     "<h2>Frequently asked questions</h2>"
     "<p><strong>Is the MSME Development (Amendment) Bill, 2026 already law?</strong> No. Parliament passed it on 7 August 2026, but it still needs the President's assent and a government notification before any part of it takes effect, and different parts can be notified on different dates.</p>"
     "<p><strong>Does this change the existing 45-day payment rule for MSME suppliers?</strong> No. Sections 15 and 16 of the MSMED Act, which set the 45-day payment period and the interest penalty at three times the RBI bank rate, are not amended by this Bill.</p>"
     "<p><strong>What is the new 50% rule everyone is talking about?</strong> Once notified, if a buyer's court case to overturn a payment award is pending for more than six months, the court must order at least 50% of the awarded amount paid to the supplier, out of the 75% deposit the buyer already had to make to bring that case.</p>"
     "<p><strong>Will Udyam registration become compulsory or stay voluntary?</strong> It becomes voluntary for every category, including medium manufacturing businesses, which currently have a compulsory 180-day filing window. That change takes effect only once the relevant section is notified.</p>"
     "<p><strong>Does the TReDS mandate apply to private companies?</strong> No. It applies to Central Public Sector Enterprises and any other body the central government separately notifies. States may extend a similar requirement to their own public sector companies, but private buyers aren't covered.</p>"
     "<p><strong>What happens if a buyer still doesn't disclose overdue MSME dues after this Bill is notified?</strong> A first offence draws a warning, a second one a penalty of Rs. 10,000 to Rs. 50,000, and a third or later offence Rs. 50,000 to Rs. 1 lakh, decided by the Development Commissioner rather than a criminal court. These minimum amounts rise by 10% every three years after the law starts.</p>"),

]
