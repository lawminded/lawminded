# Owner-requested topic, 16 August 2026: Hindu Undivided Family (HUF).
# Not news-driven — the owner named the topic directly over Telegram — so
# this is an evergreen guide.
#
# Checked against the existing 133 published articles first (live DB dump,
# 16 Aug 2026). HUF appears only as a rate label inside a table cell in
# tds-compliance-guide ("1% (ind/HUF)"); no article covers HUF formation,
# taxation, partition or coparcenary rights. Genuine gap.
#
# Verified against primary sources:
#  - Income-tax Act, 2025, Section 2(93): definition of "person", includes
#    Hindu undivided family. (eztax.in bare-text mirror of the Act.)
#  - Income-tax Act, 2025, Section 202: tax rates for individuals/HUF/AOP
#    under the new regime; FY 2025-26 slabs cross-checked against the
#    Income Tax Department's own AY 2026-27 HUF help page
#    (incometax.gov.in/iec/foportal/help/individual/return-applicable),
#    which also confirms the Rs 2,50,000 old-regime exemption for HUF and
#    that HUF return forms are ITR-2/3/4.
#  - Income-tax Act, 2025, Section 156 (rebate, formerly Section 87A of the
#    1961 Act): restricted to "resident individual", HUF excluded. Cross-
#    checked eztax.in bare text against incometaxindia.gov.in's own 87A
#    explainer and two independent professional summaries.
#  - Income-tax Act, 2025, Section 92 (formerly Section 56(2)(x)): gifts
#    without consideration, Rs 50,000 threshold, and the Explanation that
#    "relative" for an HUF means any member of that HUF. eztax.in bare text.
#  - Income-tax Act, 2025, Section 99(3)-(4) (formerly Section 64(2)):
#    clubbing of income where an individual converts separate property into
#    HUF property without adequate consideration; carve-out for conversions
#    on or before 31 December 1969. eztax.in bare text.
#  - Income-tax Act, 2025, Section 315 (formerly Section 171): assessment
#    after partition of an HUF, total and partial; partial partitions after
#    31 December 1978 not recognised for tax purposes. eztax.in bare text,
#    cross-checked against incometaxindia.gov.in's own Section 171 page for
#    the equivalent 1961 provision.
#  - Hindu Succession Act, 1956, Section 6, as substituted by the Hindu
#    Succession (Amendment) Act, 2005: daughters are coparceners by birth,
#    with the same rights and liabilities as sons.
#  - Vineeta Sharma v Rakesh Sharma, (2020) 9 SCC 576 (Supreme Court,
#    11 August 2020): daughters' coparcenary right applies regardless of
#    whether the father was alive on 9 September 2005.
#  - Sujata Sharma v Manu Gupta, Delhi High Court, CS(OS) 2011/2006
#    (single judge, 22 December 2015; upheld on appeal, RFA(OS) 13/2016,
#    division bench, 4 December 2023): the eldest female coparcener of an
#    HUF can be its karta.
#  - PAN application forms: Form 49A (individual) and Form 49AA
#    (non-individual) retired from 1 April 2026. HUF applications now use
#    Form 94 (non-individual Indian entities, including HUFs by name),
#    filed by the karta, under Rule 158 of the Income-tax Rules, 2026
#    (notified by CBDT on 20 March 2026, in force from 1 April 2026) read
#    with Section 262 of the Income-tax Act, 2025. Cross-checked across
#    three independent CA/professional summaries that agree on the specific
#    rule and section numbers; no single official notification URL was
#    fetched directly, so this is noted in REVIEW-BEFORE-PUBLISH.md as
#    corroborated-but-not-instrument-verified.
#
# Added 16 August 2026, same day, owner asked for a clarification on
# (1) whether an HUF needs children to exist, (2) what "date of formation"
# to use, and (3) how separate the HUF's PAN really is. Verified before
# writing:
#  - C. Krishna Prasad v CIT, (1974) 97 ITR 493 (SC): "plurality of persons
#    is an essential attribute of a family... a single person, male or
#    female, does not constitute a family"; HUF assessment needs two or
#    more members. Confirmed by direct read of the judgment on IndianKanoon.
#  - Surjit Lal Chhabda v CIT, (1975) 101 ITR 776 (SC): a joint Hindu family
#    (not a coparcenary) can consist of a husband, wife and unmarried
#    daughter with no son; but the assessee could not convert his own
#    self-acquired property into HUF property by declaration alone, because
#    there was no pre-existing joint family property for it to "blend" with.
#    Confirmed via the judgment text reproduced on courtkutchehry.com and
#    cross-checked against itatonline.org's case-law digest, which also
#    cites CIT v Parshottamdas K Panchal (2002) 257 ITR 96 (Guj) and W.P.A.R
#    Rajagopalan v CWT (2000) 241 ITR 344 (Mad) for the same husband-and-wife
#    point using ancestral/partition property instead of self-acquired.
#  - "Date of formation" = karta's date of marriage: this is professional
#    convention, not a statutory rule, so it is stated as such in the
#    article. Corroborated across a CAclubindia expert thread and multiple
#    HUF-deed guides (taxbuddy.com, setindiabiz.com); no CBDT form or
#    circular prescribes this date, because nothing about an HUF is
#    registered. Weakest-sourced claim in this addition — flagged here.
#  - HUF PAN as a fully separate identity, its own return (ITR-2/3/4)
#    distinct from each member's personal return: consistent with the
#    Income Tax Department's own AY 2026-27 HUF help page already cited
#    above for the return-form point, and with the general PAN/HUF guides
#    consulted for the Form 94 fact.
#
# Format matches the earlier seeds: (title, slug, category, act, read_time,
# summary, content).

BLOG_ARTICLES_10 = [

    ('Hindu Undivided Family (HUF): What It Is, How to Set One Up, and What It Actually Saves in Tax (2026)',
     'hindu-undivided-family-huf-tax-guide',
     'tax',
     'Income-tax Act, 2025',
     '7 min read',
     "An HUF is a separate taxpayer that a Hindu, Sikh, Jain or Buddhist joint family can use to hold ancestral property, inheritance or genuine gifts, and pay tax on that income under its own exemption and slabs. It will not let you move your own salary into it, and it gets no Section 156 rebate, so the saving is real only for families with income-producing assets outside their personal earnings.",
     "<p><em>A father is renting out a flat that used to belong to his own father, and the rent is about to push him into a higher tax bracket. A friend mentions an HUF PAN card that has sat in a drawer since an uncle opened it years ago and never used it. The idea sounds like a loophole. It is closer to a piece of legal machinery the family already owns, which works well if funded correctly and badly if it isn't.</em></p>"
     "<p><strong>A Hindu Undivided Family, or HUF, is a separate taxpayer recognised by Indian tax law. A Hindu, Sikh, Jain or Buddhist joint family can use it to hold ancestral property, inheritance or gifts, and pay tax on that income under its own basic exemption and slabs, separate from what each member already pays on their own earnings. It cannot absorb your salary or professional fees; the law specifically pulls that income back to you.</strong></p>"
     "<blockquote><p><strong>The bottom line</strong></p>"
     "<p><strong>What it costs:</strong> nothing to the government to create, since Hindu law does not register an HUF into existence. In practice, you pay for a stamped HUF deed and, once the HUF earns taxable income, for its own PAN, bank account and annual return.</p>"
     "<p><strong>What it covers:</strong> a second basic exemption and slab structure for rent, capital gains or business income earned from ancestral property, inheritance, or a genuine gift into the HUF.</p>"
     "<p><strong>What it does not fix:</strong> you cannot move your own salary or fees into the HUF to save tax. The HUF also gets no Section 156 rebate, the one that makes income up to Rs 12 lakh effectively tax-free for an individual under the new regime.</p></blockquote>"

     "<h2>What an HUF actually is</h2>"
     "<p>An HUF is not something you incorporate. It comes from Hindu personal law, and it exists the moment a Hindu, Sikh, Jain or Buddhist family has, or has ever had, property held jointly across generations rather than owned by one person outright. The Income-tax Act, 2025 does not invent the HUF; it simply picks it up as one of the categories of taxpayer the law recognises. Section 2(93) defines \"person\" for tax purposes as including an individual, a Hindu undivided family, a company, a firm, and a few other categories, putting the HUF on the same footing as any of them.</p>"
     "<p>Two words are worth pinning down first, since families tend to use them loosely. A <strong>coparcener</strong> is a family member with a right by birth to a share of the HUF's property: someone who could demand a partition and get a slice, not merely a relative living under the same roof. \"Member\" is the wider circle. A coparcener's wife, for instance, is a member with a right to be maintained out of the HUF's income, but she has no independent right to force a partition. The <strong>karta</strong> is whoever manages the HUF's affairs day to day, signs cheques, and files its return.</p>"

     "<h2>Daughters are coparceners now, not just members</h2>"
     "<p>Until 2005, sons became coparceners by birth and daughters did not. The Hindu Succession (Amendment) Act, 2005 rewrote Section 6 of the Hindu Succession Act, 1956, giving daughters the same coparcenary right by birth as sons, with the same rights and the same liabilities.</p>"
     "<p>For fifteen years, courts disagreed about whether this reached daughters whose fathers had already died before the 2005 amendment took effect. The Supreme Court settled it in <em>Vineeta Sharma v Rakesh Sharma</em> (2020): a daughter's coparcenary right attaches by birth, regardless of whether her father was alive on 9 September 2005, the date the amendment came into force.</p>"
     "<p>That change reaches further than inheritance. In <em>Sujata Sharma v Manu Gupta</em>, the Delhi High Court held that the eldest coparcener, male or female, can be karta, letting a woman run the family HUF rather than only inherit from it. A division bench upheld that ruling on appeal in December 2023, so it is settled law in Delhi and persuasive authority elsewhere, not a single-judge outlier.</p>"

     "<h2>Setting one up: deed, PAN, bank account</h2>"
     "<p>Because Hindu law does not register an HUF into being, there is no certificate that creates one. What you actually need, before a bank or the tax department will treat the HUF as a going concern, is three things. First, an HUF deed: a declaration on stamp paper naming the karta, listing the coparceners and members, and recording where the initial money or property came from. There is no date of incorporation the way a company has one, because nothing gets registered anywhere. The deed and the PAN form still ask for a date the HUF is treated as having started, and the convention most practitioners use is the karta's date of marriage, since that is when a family capable of holding joint property first existed, whether or not it owned anything yet. Where the HUF actually continues one from an earlier generation, say the karta inherited both the property and the HUF status from his own father, the date used is when that succession happened, not the current karta's wedding date. Second, a PAN in the HUF's own name, applied for by the karta. From 1 April 2026, this goes through Form 94 under Rule 158 of the Income-tax Rules, 2026. That form replaced the old Form 49A/49AA pair with a four-form system split by applicant type, and an HUF falls into the non-individual category Form 94 covers by name. That PAN is a fully separate identity, not an extension of the karta's own. It carries its own ten-digit number, opens the HUF's own bank account and any investment or demat accounts in its name, and covers the HUF's own annual return (ITR-2 or ITR-3, sometimes ITR-4, depending on its income), filed separately from what each member files for their personal income. Rent sitting in the HUF's account is not the karta's income just because the karta operates the account. Third, a bank account in the HUF's name, which most banks will only open once the deed and PAN are in hand.</p>"
     "<p>None of this, by itself, saves any tax. What the HUF is funded with decides that, and that's the part people get wrong.</p>"

     "<h2>What actually saves tax, and what doesn't</h2>"
     "<p>An HUF pays tax at the same rates as an individual. Section 202 of the Income-tax Act, 2025 sets a common rate schedule for individuals, HUFs and a few other categories, and for the tax year running from April 2025, the new-regime slabs look like this.</p>"
     "<div class=\"table-wrap\"><table class=\"prose-table\"><thead><tr><th>Income slab</th><th>Rate</th></tr></thead><tbody>"
     "<tr><td>Up to Rs 4,00,000</td><td>Nil</td></tr>"
     "<tr><td>Rs 4,00,001 - Rs 8,00,000</td><td>5%</td></tr>"
     "<tr><td>Rs 8,00,001 - Rs 12,00,000</td><td>10%</td></tr>"
     "<tr><td>Rs 12,00,001 - Rs 16,00,000</td><td>15%</td></tr>"
     "<tr><td>Rs 16,00,001 - Rs 20,00,000</td><td>20%</td></tr>"
     "<tr><td>Rs 20,00,001 - Rs 24,00,000</td><td>25%</td></tr>"
     "<tr><td>Above Rs 24,00,000</td><td>30%</td></tr>"
     "</tbody></table></div>"
     "<p>An HUF can instead choose the old regime, where its basic exemption is Rs 2,50,000, and claim the usual deductions available under that regime against its own income. Either way, this is a genuinely separate exemption and a genuinely separate set of slabs, layered on top of whatever each family member already pays individually.</p>"
     "<p>Here is the catch that trips up a lot of family tax planning. Under the new regime, a resident individual with income up to Rs 12 lakh pays no tax at all, because Section 156 gives a rebate that wipes out the liability entirely. That rebate is written for \"resident individual\" only. An HUF does not qualify, so its income is taxed from the very first slab above the exemption, with no cushion. A family comparing \"tax as an individual\" with \"tax through the HUF\" needs to run both numbers, not assume the HUF automatically wins because it has its own slab.</p>"
     "<p>Funding the HUF correctly matters more than any of this. A gift from a member to the HUF is exempt outright. Section 92 defines \"relative\" for an HUF as any member of that HUF, so money a father, mother or sibling gives to the family HUF they belong to falls outside the usual Rs 50,000 gift-tax threshold altogether.</p>"
     "<p>Funding it by converting your own property is a different story, and this is where most of the tax saving people expect quietly disappears. If you take an asset you already own individually and \"throw it into the family hotchpot\", the traditional phrase for declaring it HUF property, the income from that asset is not the HUF's for tax purposes. Section 99(3) treats you as having transferred the property through the family for the benefit of all its members, and taxes the resulting income in your own hands regardless. The only exception is a conversion that happened on or before 31 December 1969, which will not apply to anyone setting up an HUF today. In practice, the tax saving an HUF genuinely offers comes from ancestral property, an inheritance, or a gift from someone outside the family HUF, not from moving your own salary or savings into it. For how the Income-tax Act, 2025 reorganised these section numbers generally, see our <a href=\"/article/income-tax-act-2025-what-changed\">guide to what changed on 1 April 2026</a>.</p>"

     "<h2>Can an HUF exist with just husband and wife, before children come along?</h2>"
     "<p>Yes. The Supreme Court's test for whether a family counts as an HUF at all has nothing to do with children; it's plurality of members. In <em>C. Krishna Prasad v CIT</em> (1974), the Court held that a single person, male or female, does not constitute a family, and that an HUF can be assessed as one only where it has two or more members. A husband and wife clear that bar on their wedding day.</p>"
     "<p>What a child changes is the coparcenary, not the HUF's existence. A coparcener is the member with a birthright to demand a share of the property: sons only, historically, and since the Hindu Succession (Amendment) Act, 2005, sons and daughters alike. A wife is a member, entitled to maintenance from the HUF's income, but she isn't a coparcener herself and can't demand a partition. So a childless couple's HUF has exactly one coparcener, the husband, until a child is born and becomes a coparcener automatically, by birth, no paperwork required.</p>"
     "<p>There's a limit worth knowing before anyone treats this as a shortcut. In <em>Surjit Lal Chhabda v CIT</em> (1975), the Supreme Court held that a husband can't create HUF property simply by declaring his own earnings to be HUF property if there was no joint family property already there for it to join; his wife and unmarried daughter, in that case, had no claim strong enough to turn his self-acquired property into family property just because he said so. A childless couple's HUF gets exactly the same tax treatment as any other HUF, using the same funding rules covered above: ancestral property, an inheritance, a partition share, or a gift from someone outside the HUF. Children aren't the precondition. Where the property came from is.</p>"

     "<h2>Partition: the part families get wrong</h2>"
     "<p>Section 315 governs what happens when an HUF splits up, and it is stricter than most families expect. On a total partition, the joint family is assessed as an HUF for all income up to the date of partition, and every member remains jointly and severally liable for tax the HUF owed from before that date. Splitting up the property doesn't split up the old tax bill.</p>"
     "<p>The bigger trap is partial partition: dividing one asset among the members while leaving the rest of the HUF's property jointly held. For any partial partition after 31 December 1978, Section 315 simply refuses to recognise it for tax purposes. The Income-tax Department goes on assessing the whole HUF as undivided, taxing the income from the \"divided\" asset as HUF income, exactly as if the family had never split it. Say a family informally splits a rental property among its members, and each one starts collecting and declaring their own share of the rent. The department can still tax that same rent as HUF income all over again, because nothing short of a full partition of the entire HUF counts.</p>"

     "<h2>Common mistakes</h2>"
     "<ul>"
     "<li>Assuming salary or professional fees can be routed through the HUF to use its exemption a second time. They can't; that income stays taxable in the individual's hands.</li>"
     "<li>Converting personal savings or property into HUF property and expecting the income to shift with it. Section 99(3) taxes it in the converting individual's hands regardless.</li>"
     "<li>Treating an informal split of one HUF asset as ending the HUF's ownership of it for tax purposes. Section 315 disregards any partial partition after 1978.</li>"
     "<li>Letting an HUF earn taxable income for years without a PAN or a return filed in its own name. Once it has income, it needs both, the same as any other taxpayer.</li>"
     "<li>Never updating who the karta is, even after the position should have passed to an eldest coparcener, male or female. Banks and the tax department go by whatever the deed and PAN records say, not by family understanding.</li>"
     "</ul>"

     "<h2>Frequently asked questions</h2>"
     "<p><strong>Can a daughter be the karta of an HUF?</strong> Yes. Since the 2005 amendment gave daughters an equal coparcenary right by birth, the Delhi High Court has held that the eldest coparcener, whether son or daughter, can be karta, in a ruling upheld on appeal in 2023.</p>"
     "<p><strong>Can I save tax by transferring my own property into my family's HUF?</strong> Not usually. Section 99(3) of the Income-tax Act, 2025 taxes the income from that property in your own hands, because you converted it yourself without adequate consideration.</p>"
     "<p><strong>Is a gift from a family member to the HUF taxable?</strong> No. Any member of the HUF counts as its \"relative\" under Section 92, so a gift from a member is exempt regardless of amount.</p>"
     "<p><strong>Does an HUF get the same tax-free threshold as an individual under the new regime?</strong> No. The Section 156 rebate that makes income up to Rs 12 lakh effectively tax-free applies only to resident individuals, not to an HUF.</p>"
     "<p><strong>If we informally divide one HUF asset among the members, does that end the HUF's ownership of it?</strong> Not for tax purposes. Section 315 does not recognise a partial partition made after 31 December 1978, and the Income-tax Department continues to assess the whole HUF as undivided.</p>"
     "<p><strong>Do we need children to set up an HUF?</strong> No. A husband and wife alone meet the Supreme Court's test of two or more members, which is all Hindu law requires for a family to be assessed as an HUF. A child becomes a coparcener automatically once born, but a child isn't a precondition for the HUF itself.</p>"
     "<p><strong>What date do we give as the HUF's date of formation?</strong> There's no registered date, since nothing about an HUF gets registered anywhere. Practitioners conventionally use the karta's date of marriage on the deed and PAN application, since that's the day the family unit began, unless the HUF continues one inherited from an earlier generation, in which case the date of that succession is used instead.</p>"
     "<p><strong>Is the HUF's PAN different from the karta's own PAN?</strong> Yes. It's a separate ten-digit PAN in the HUF's name, used for its own bank account and its own income tax return, distinct from each member's personal PAN and return.</p>"
     "<p><em>This article is for legal awareness and education only and is not tax or legal advice. HUF taxation, partition rules and PAN procedures involve family-specific facts; confirm current figures or consult a qualified professional before acting.</em></p>"),

]
