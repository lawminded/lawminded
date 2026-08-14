# Owner-requested article, written 14 August 2026, on changing an LLP's
# capital contribution (increase and reduction). Not a news-driven piece —
# the owner asked for it directly over Telegram — so it's an evergreen guide
# rather than tied to a specific week's development.
#
# Checked against the existing 133 published articles first. The site already
# has 'llp-registration' and 'annual-compliance-llps' (both in blog_seed.py),
# neither of which touches changing capital contribution after incorporation,
# so this fills a genuine gap rather than duplicating either.
#
# Verified against primary sources: LLP Act, 2008 Sections 23, 32 and 33
# (cross-checked across ibclaw.in and advocatekhoj.com, which quote identical
# statutory text); the LLP (Amendment) Rules, 2022 fee schedule (G.S.R. 109(E)
# dated 11.02.2022, effective 1.04.2022, cross-checked across two independent
# summaries with matching multiplier tables); Income
# Tax Act Section 2(23), Section 45(4) and Section 9B as amended by the
# Finance Act, 2021, and CBDT Circular 14/2021 with Rules 8AA(5)/8AB. State
# stamp duty on supplementary LLP deeds was deliberately left unquantified —
# two secondary sources gave contradictory rates for the same states, so no
# figure clears the site's verification bar; the article tells the reader to
# check their state's current schedule instead of repeating an unverified one.
#
# Format matches the earlier seeds: (title, slug, category, act, read_time,
# summary, content).

BLOG_ARTICLES_9 = [

    ('How to Increase or Reduce an LLP\'s Capital Contribution — and the Tax Bill a Reduction Can Trigger',
     'llp-capital-contribution-increase-reduction',
     'tax',
     'LLP Act, 2008',
     '8 min read',
     'An LLP can raise or lower a partner\'s capital contribution any time, since the LLP Act sets no minimum or maximum. It takes the partners\' written consent and a Form 3 filing within 30 days either way, but a reduction that pays a partner out can leave the LLP itself owing capital gains tax under a rule most partners have never checked.',
     "<p><em>Two partners want to put more money into their LLP, or one wants to take some of theirs back out. Both feel like a private decision between partners, right up until the paperwork catches up with the LLP that treated it that way, and in one of the two cases, so does the tax department.</em></p>"
     "<p><strong>An LLP can raise or lower a partner's capital contribution at any time, because the LLP Act sets no minimum or maximum figure. Either way, the partners have to agree to it in writing and file the change with the Registrar within 30 days. But if money actually leaves the LLP to pay down someone's contribution, that payout can be taxed as a capital gain in the LLP's own hands, under a provision most partners only discover after the return is filed.</strong></p>"
     "<blockquote><p><strong>The bottom line</strong></p>"
     "<p><strong>What it costs:</strong> a Registrar filing fee of Rs 50 to Rs 600 depending on the LLP's total contribution, stamp duty on the supplementary agreement under your state's law, and, only where a reduction pays a partner out, a possible capital gains tax bill for the LLP itself.</p>"
     "<p><strong>What it covers:</strong> any change to how much each partner has put into the LLP, whether that's fresh money coming in or a partial withdrawal going out.</p>"
     "<p><strong>What it does not fix:</strong> a creditor who lent money relying on a partner's original, higher contribution can still hold that partner to the old figure, and cutting a partner's stake doesn't erase what they already owed the LLP before the change.</p></blockquote>"

     "<h2>What \"capital contribution\" means in an LLP</h2>"
     "<p>An LLP's capital contribution isn't share capital in the company-law sense. There's no face value attached to it, no floor and no ceiling. Section 32 of the Limited Liability Partnership Act, 2008 lets a partner contribute cash, property, or even a promise to perform services, and the LLP Agreement, the document you would have filed in Form 3 when you set up the LLP (see our <a href=\"/article/llp-registration\">LLP registration guide</a>), fixes each partner's figure. Two consultants can start an LLP with Rs 10,000 between them or Rs 10 crore; the Act treats both the same way. That's also why changing the figure later is a matter of what the partners agree to, not a regulatory threshold to clear.</p>"

     "<h2>Increasing the contribution</h2>"
     "<p>Bringing in more capital, whether from an existing partner or as part of admitting a new one, needs three things done in order.</p>"
     "<p>First, the partners agree to it in writing, following whatever voting rule their LLP Agreement sets for amending itself. Most agreements require every partner's consent for a change like this. If yours doesn't say, the Act's own default rules fill the gap, and those also call for unanimous consent on matters like this.</p>"
     "<p>Second, that agreement becomes a supplementary LLP Agreement: a short deed adding to the original one, signed by every partner, not a replacement for it. Where a partner is contributing something other than cash, such as property or a running service commitment, Rule 23 of the LLP Rules, 2009 requires a practising chartered accountant, cost accountant, or a government-approved valuer to certify its money value before it enters the LLP's books.</p>"
     "<p>Third, the LLP tells the Registrar. Section 23(2) of the Act requires any change to the LLP Agreement to be filed within 30 days, in Form 3, with a copy of the supplementary deed attached. The government fee for that filing is banded by the LLP's total contribution: Rs 50 up to Rs 1 lakh, rising in steps to Rs 600 above Rs 1 crore. Miss the 30-day window and the fee doesn't just double. Since April 2022, a filing more than a year late costs up to 50 times the normal fee for most LLPs, or 25 times for a \"small LLP\" (one with contribution under Rs 25 lakh and turnover under Rs 40 lakh in the year before).</p>"
     "<p>One more cost to plan for: the supplementary deed is itself a stamped instrument, and duty is charged again on the increased amount under your state's Stamp Act. Rates and caps differ by state and change without much notice, so check the current schedule on your state's e-stamping or registration portal before you execute the deed, rather than relying on a figure quoted somewhere online.</p>"

     "<h2>Reducing the contribution</h2>"
     "<p>The steps look identical: partner consent, a supplementary deed, Form 3 within 30 days. That similarity is exactly what leads people astray. A company cutting its share capital needs Tribunal approval, a solvency declaration, and a window for creditors to object, under Section 66 of the Companies Act, 2013. The LLP Act has no equivalent machinery built into a contribution reduction. There's no Tribunal, no government approval, and no mandatory notice to creditors written into the process itself.</p>"
     "<p>That doesn't mean creditors are unprotected. Section 33(2) of the LLP Act lets a creditor who extended credit relying on a partner's stated contribution enforce that original obligation against the partner, if the creditor had no notice of the change. Say a bank sanctioned a loan partly on the strength of a partner's Rs 20 lakh commitment. Quietly cutting that to Rs 2 lakh afterwards doesn't automatically let the partner off the hook with the bank.</p>"
     "<p>The bigger trap sits on the tax side, and it catches people because a capital account withdrawal feels like a bookkeeping entry between partners rather than something the tax department needs to know about.</p>"

     "<h2>The tax the LLP can end up owing</h2>"
     "<p>The Income Tax Act treats an LLP as a \"firm\" for this purpose. Section 2(23) extends the definitions of firm, partner and partnership to LLPs by name, so provisions written for ordinary partnerships reach LLPs too. Since the Finance Act, 2021, Section 45(4) taxes money or a capital asset that a partner receives from the firm \"in connection with the reconstitution\" of that firm, and taxes it as the firm's own capital gain, not the partner's income. Section 9B does the same job where the firm hands over property or stock instead of cash.</p>"
     "<p>\"Reconstitution\" isn't limited to a partner leaving. The definition added by the same 2021 amendment also covers a case where every partner stays on, but their respective shares change. If a reduction in one partner's capital comes with an actual cash payout to that partner, and it also shifts how capital or profits are split among the rest, the LLP can end up owing capital gains tax on that payout under a section the partners never thought to check, because nothing about a capital account entry looked like a \"transfer\" from where they were sitting. The CBDT set out how to compute that gain in a July 2021 circular, backed by two rules inserted the same year.</p>"
     "<p>Take three partners with equal shares, each holding Rs 30 lakh of the LLP's Rs 90 lakh contribution. One wants to scale back involvement and takes Rs 20 lakh out as a partial withdrawal, dropping to Rs 10 lakh, while the other two now hold larger shares of a smaller total. That's a payout tied to a change in shares: on the facts, it's exactly the kind of reconstitution Section 45(4) is written to catch, and the LLP, not the exiting-in-part partner, is the one who owes tax on the gain the computation throws up.</p>"
     "<p>None of this touches an increase. Money coming into the LLP from a partner isn't a reconstitution payout in either direction the section taxes. It also doesn't automatically catch every reduction: a change that leaves every partner's share exactly as it was, with no money actually moving out, sits outside Section 45(4) on the wording of the section itself. But the moment a reduction involves a real payment to a partner alongside any change in shares, get a chartered accountant to check the computation before the money moves, not after the return is filed.</p>"

     "<h2>Common mistakes</h2>"
     "<ul><li>Filing Form 3 late and assuming the old flat daily penalty still applies. Since April 2022, the additional fee is a multiple of the normal fee that climbs with the length of the delay, not a flat daily rate. It's a different filing from the Form 8 and Form 11 you already handle every year (see our <a href=\"/article/annual-compliance-llps\">LLP annual compliance guide</a>), and it's only due when the agreement itself changes.</li>"
     "<li>Treating a capital withdrawal as a private adjustment between partners that needs no filing. Any change to the contribution figure in the LLP Agreement goes to the Registrar within 30 days, exactly like an increase does.</li>"
     "<li>Paying a partner out of a capital reduction without checking Section 45(4) first, then finding out later that the LLP owes capital gains tax on money that already left its account.</li>"
     "<li>Assuming a majority of partners is enough to approve the change, when most LLP Agreements, and the Act's own default rule, call for every partner's consent.</li>"
     "<li>Contributing property or a service commitment without the chartered accountant or approved-valuer certificate Rule 23 requires, leaving the LLP's books unsupported if a lender or the Registrar later asks how the figure was arrived at.</li></ul>"

     "<h2>Frequently asked questions</h2>"
     "<p><strong>Is there a minimum or maximum capital contribution for an LLP?</strong> No. The LLP Act sets neither a floor nor a ceiling; the partners decide the figure in the LLP Agreement.</p>"
     "<p><strong>Does increasing an LLP's capital need approval from the Registrar or a court?</strong> No. It needs the partners' consent as the LLP Agreement sets out, followed by a Form 3 filing within 30 days. No prior government or court approval is required.</p>"
     "<p><strong>Does reducing an LLP's capital need Tribunal approval, the way a company cutting share capital does?</strong> No. The LLP Act has no equivalent to Section 66 of the Companies Act, 2013. The change still has to be filed with the Registrar within 30 days.</p>"
     "<p><strong>Can reducing a partner's capital contribution create a tax liability?</strong> Yes, if the LLP pays money or hands over an asset to a partner and that payment is connected to a change in the partners' shares. Section 45(4) of the Income Tax Act can tax that payout as the LLP's own capital gain.</p>"
     "<p><strong>What happens if Form 3 is filed late?</strong> The LLP pays an additional fee that rises with the delay, from the normal one-time fee up to 15 days late, to as much as 50 times the normal fee (25 times for a small LLP) beyond a year, under the fee schedule in force since April 2022.</p>"),

]
