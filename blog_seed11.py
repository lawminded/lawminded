# News-driven, week of 21 August 2026.
#
# Checked the 131 published articles first (live DB dump, 21 Aug 2026; also
# grepped blog_seed*.py for "54EC", "capital gain bonds", "OBPP"). Section
# 54EC / capital gains bonds is not covered anywhere on the site. The tax
# category has HUF, freelancers, perquisites, TDS, ITC and the Income-tax
# Act 2025 explainer, but nothing on the property-sale capital-gains exemption.
#
# News hook: SEBI circular dated 14 August 2026 lets Online Bond Platform
# Providers sell Section 54EC / Section 85 capital gains bonds directly,
# with new mandatory disclosures, and separately lets them offer
# IFSCA-regulated products. Genuinely new (within the 7-day window), and it
# changes something a reader can act on this week: how they buy the bonds,
# not just whether the bonds exist.
#
# Verified against primary sources:
#  - SEBI Circular HO/17/11/(2)2026-DDHS-POD1/I/18769/2026, dated 14 August
#    2026, "Modification in the regulatory framework for Online Bond
#    Platform Providers (OBPPs) including measures for promoting ease of
#    doing business." Fetched and read the full 4-page PDF directly from
#    sebi.gov.in (sebi_data/attachdocs/aug-2026/1786705729757.pdf, linked
#    from the circular's own listing page). Confirmed: clause 5.2.6 adds
#    "Bonds issued under section 54EC of the Income Tax Act, 1961 or Section
#    85 of Income-tax Act, 2025" to the list of products an OBPP may offer;
#    clause 5.2.5 adds IFSCA-regulated products/securities/services;
#    mandatory disclosures for 54EC bonds (tax-specific-instrument
#    disclaimer, grievance redressal lies with the issuer not SEBI, features
#    disclosure covering eligible issuers/lock-in/investment
#    limit/non-transferability/tax features/application size/LODR listing
#    exemption); IFSCA products must be labelled "international or overseas
#    instruments" and follow FEMA/LRS rules; Annexure-XXIA compliance
#    officer requirement changed from "must be a Company Secretary" to a
#    NISM-certified compliance officer under SEBI (Stock Brokers)
#    Regulations, 2026; circular in force with immediate effect, signed by
#    Rohit Dubey, GM, Department of Debt and Hybrid Securities.
#  - Section 54EC of the Income Tax Act, 1961, bare text reproduced on
#    IndianKanoon (doc/82271184 and doc/172643298): long-term capital asset
#    must be land or building or both; 6-month reinvestment window from the
#    date of transfer; Rs 50 lakh cap on investment made in a financial year
#    on/after 1 April 2007; lock-in raised from 3 to 5 years for bonds
#    acquired on or after 1 April 2018; "long-term specified asset" defined
#    by reference to bonds issued by NHAI, REC or another entity the central
#    government notifies.
#  - CBDT Notification No. 31/2025, dated 7 April 2025 (via TaxScan,
#    CAclubindia and TaxManagement India, which all independently quote the
#    same notification number, date and terms): HUDCO bonds issued on or
#    after 1 April 2025 and redeemable after 5 years notified as a
#    long-term specified asset under Section 54EC.
#  - Current 54EC issuers, coupon and ticket size: cross-checked across
#    bondscanner.com's REC and NHAI explainers and zfunds.in — REC, PFC,
#    IRFC and HUDCO as of mid-2026; coupon 5.25% p.a., paid annually on 30
#    June for REC specifically; minimum application one bond of Rs 10,000;
#    Rs 50 lakh per PAN per financial year. No official issuer coupon
#    notice was fetched directly (coupons reset per tranche), so the
#    article states 5.25% as "the coupon on offer in mid-2026" rather than
#    a fixed rate, and tells the reader to confirm the live rate before
#    applying.
#  - Section 85, Income-tax Act, 2025, as the renumbered successor to
#    Section 54EC, corroborated across three independent professional
#    summaries (rrfinance.com, thefixedincome.com, mytaxexpert.co.in) that
#    agree the substantive terms carried over unchanged.
#
# Format matches the earlier seeds: (title, slug, category, act, read_time,
# summary, content).

BLOG_ARTICLES_11 = [

    ('54EC Capital Gains Bonds: How to Shelter a Property Sale From Tax, and Why You Can Now Buy Them Online (2026)',
     '54ec-capital-gains-bonds-online-guide',
     'tax',
     'Income-tax Act, 2025',
     '7 min read',
     "Section 54EC lets you avoid long-term capital gains tax on the sale of land or a building by putting the gain, up to Rs 50 lakh a year, into specified bonds within six months of the sale. A SEBI circular dated 14 August 2026 now lets registered online bond platforms sell you those bonds directly, with new disclosure rules attached, instead of routing you through the issuer's own paperwork.",
     "<p><em>Sell a plot or an old flat for a solid profit and the tax on that gain can run into several lakh. The law gives you a narrow way out: buy specified bonds instead of handing the gain to the tax department, and you get to keep it, locked up for five years. Doing that used to mean a paper application, a demand draft, and a trip to a registrar's office before the six-month window closed. As of this month, it doesn't.</em></p>"
     "<p><strong>Section 54EC of the Income Tax Act, 1961, now Section 85 of the Income-tax Act, 2025, exempts long-term capital gains from the sale of land or a building if you invest the gain, up to Rs 50 lakh a financial year, in specified bonds within six months of the sale. A SEBI circular dated 14 August 2026 lets registered Online Bond Platform Providers sell these bonds directly on their websites, with mandatory disclosures attached, instead of requiring you to deal with the bond issuer's own application process.</strong></p>"
     "<blockquote><p><strong>The bottom line</strong></p>"
     "<p><strong>What it costs:</strong> the money you invest is locked up for five years and earns whatever coupon the issuer is offering when you buy, currently around 5.25% a year, which is fully taxable as interest.</p>"
     "<p><strong>What it covers:</strong> long-term capital gains from selling land or a building, or both, up to Rs 50 lakh invested in a financial year, exempt if you buy the bonds within six months of the sale.</p>"
     "<p><strong>What it does not fix:</strong> gains from shares, gold, mutual funds or any capital asset other than land and buildings don't qualify. Miss the six-month window, exceed the cap, or sell or pledge the bonds before five years are up, and the exemption is gone.</p></blockquote>"

     "<h2>What Section 54EC actually exempts</h2>"
     "<p>The exemption is narrower than people assume. It applies only to a long-term capital gain arising from the transfer of land, a building, or both. A gain from selling shares, a business, gold or a mutual fund unit doesn't qualify, no matter how long you held it. You have six months from the date of transfer, usually the date the sale deed is registered, to put the gain into the specified bonds. Miss that window by even a week and the exemption is off the table; there is no condonation for a late purchase.</p>"
     "<p>Unlike Section 54, which is restricted to individuals and Hindu undivided families reinvesting in a residential house, Section 54EC is open to any taxpayer with the right kind of gain: an individual, an HUF, a company, a partnership firm, anyone. The exemption is capped at whichever is lower, the actual capital gain or Rs 50 lakh invested in that financial year. If your gain is Rs 80 lakh, you shelter Rs 50 lakh of it and pay tax on the rest. The Income-tax Act, 2025, which took effect on 1 April 2026, carried this provision over as Section 85 with the same substance; see our <a href=\"/article/income-tax-act-2025-what-changed\">guide to what changed under the new Act</a> for how the renumbering works across the statute generally.</p>"

     "<h2>The bonds: who issues them, and the Rs 50 lakh ceiling</h2>"
     "<p>\"Specified bonds\" means bonds the central government has notified as a long-term specified asset under the section. As of mid-2026 that list runs to four issuers: Rural Electrification Corporation, Power Finance Corporation, Indian Railway Finance Corporation, and, since a CBDT notification dated 7 April 2025, the Housing and Urban Development Corporation. HUDCO's eligibility applies to bonds it issues on or after 1 April 2025 and that are redeemable after five years, matching the other three.</p>"
     "<p>The lock-in itself moved from three years to five for any 54EC bonds bought on or after 1 April 2018, so anyone quoting the older three-year figure is out of date. Redeem, sell, transfer or take a loan against the bonds before the five years are up, and the capital gain you sheltered becomes taxable in the year you did it. The minimum application is one bond, typically priced at Rs 10,000, and the Rs 50 lakh cap applies per PAN per financial year across whichever of these issuers you buy from, not per issuer. The coupon moves with each new tranche the issuers open; it was 5.25% a year, paid annually, going into August 2026. Confirm the live rate on the day you apply rather than assuming last year's number still holds, and remember that interest on 54EC bonds is ordinary taxable income, with no exemption of its own.</p>"

     "<h2>What changed on 14 August</h2>"
     "<p>SEBI has regulated Online Bond Platform Providers, OBPPs, since November 2022, letting retail investors buy listed debt securities, government securities, treasury bills and sovereign gold bonds through a registered website rather than a broker's back office. Until this month, 54EC bonds sat outside that list. Buying them meant going to the issuer's own registrar, an authorised collection bank, or a bond-selling intermediary, filling in a physical or issuer-hosted application form, and attaching proof of the sale that generated the gain.</p>"
     "<p>A SEBI circular dated 14 August 2026 (reference HO/17/11/(2)2026-DDHS-POD1/I/18769/2026) added Section 54EC and Section 85 bonds to the list of products an OBPP may offer, alongside a separate change letting OBPPs offer products regulated by the International Financial Services Centres Authority. Both changes took effect immediately, the same day the circular was issued. The same circular also relaxed who an OBPP can appoint as its compliance officer, replacing a rule that specifically required a Company Secretary with a broader requirement that the officer hold a NISM compliance certification. That last change affects the platforms, not you directly, but it's part of the same easing.</p>"

     "<h2>What the platform now has to tell you</h2>"
     "<p>The circular also attaches conditions on what an OBPP must disclose before selling you a 54EC bond. The platform has to state plainly that these are tax-specific instruments, and that if something goes wrong, your grievance goes to the bond issuer, not to SEBI's own investor-grievance mechanism. It also has to lay out the bond's actual features: which issuers are eligible, the lock-in period, your investment limit, the fact that the bonds can't be transferred, the tax treatment of the coupon, the minimum application size, and that these bonds are exempt from SEBI's listing disclosure rules the way an ordinary listed bond isn't. On top of that, the platform must tell you upfront that the product is meant for someone actually claiming the Section 54EC or Section 85 exemption, not a general fixed-income investor browsing for yield, and that the tax benefit still depends on you meeting the underlying eligibility conditions in the Income-tax Act.</p>"
     "<p>If a platform also starts offering IFSCA-regulated products under the same circular, those have to be labelled as international or overseas instruments so they aren't confused with an ordinary domestic bond, and any money going into them has to comply with FEMA and the Liberalised Remittance Scheme limits, the same rules that already apply if you invest abroad through any other route.</p>"

     "<h2>Using this if you've actually sold a property</h2>"
     "<p>Work out the long-term capital gain first: sale consideration less the indexed cost of acquisition and improvement, and less any selling expenses. Note the exact date of transfer, usually the <a href=\"/article/registration-act-guide\">registration date on the sale deed</a>, since that's what starts the six-month clock, not the date money changed hands or the agreement to sell was signed. Decide whether locking the money away for five years actually suits you; the alternative is paying the capital gains tax now and keeping the rest liquid, which sometimes works out better once you account for the fact that the bond's own interest is taxable too.</p>"
     "<p>If you go ahead, check that the platform you're buying through is actually a SEBI-registered OBPP, not just a website that happens to sell bonds; SEBI publishes the registered list on its own site. Confirm the coupon on offer that day, since it resets with each tranche, and keep the bond allotment advice or demat statement with your tax records. You'll need proof of the investment, the amount, and the date it was made when you claim the exemption in your return for that year.</p>"

     "<h2>Common mistakes</h2>"
     "<ul>"
     "<li>Counting the six months from the sale agreement instead of the registered transfer date, and missing the window by days.</li>"
     "<li>Assuming the exemption covers a gain from shares or gold. It only covers land and buildings.</li>"
     "<li>Treating the bond's annual interest as tax-free because the principal investment saved tax. The interest is fully taxable.</li>"
     "<li>Pledging the bonds as collateral for a loan within the five-year lock-in, which triggers the same tax the exemption was meant to avoid.</li>"
     "<li>Buying through a website that isn't actually SEBI-registered as an OBPP, on the assumption that any bond-selling platform is regulated the same way.</li>"
     "</ul>"

     "<h2>Frequently asked questions</h2>"
     "<p><strong>Does Section 54EC apply to gains from selling shares or gold?</strong> No. The exemption is limited to long-term capital gains from the transfer of land, a building, or both.</p>"
     "<p><strong>What happens if I sell or pledge the bonds before five years are up?</strong> The capital gain you sheltered becomes taxable in the year you sell, transfer or pledge the bonds, even though the original sale happened earlier.</p>"
     "<p><strong>Can I invest more than Rs 50 lakh to shelter a bigger gain?</strong> No. The exemption is capped at Rs 50 lakh invested per financial year per PAN, regardless of how large the actual gain is.</p>"
     "<p><strong>Is the interest on 54EC bonds tax-free?</strong> No. The coupon, currently around 5.25% a year, is ordinary taxable interest income with no exemption of its own.</p>"
     "<p><strong>Can only individuals use Section 54EC?</strong> No. It's open to any taxpayer with a qualifying gain from land or a building: individuals, HUFs, companies and firms alike.</p>"
     "<p><strong>Do I have to buy 54EC bonds through an online bond platform now?</strong> No. The SEBI circular adds a new channel; you can still apply directly through the bond issuer or its registrar if you prefer.</p>"
     "<p><strong>Which bonds currently qualify under Section 54EC?</strong> Bonds issued by REC, PFC, IRFC and, since April 2025, HUDCO, provided they carry the required five-year lock-in.</p>"
     "<p><em>This article is for legal awareness and education only and is not tax or investment advice. Capital gains computation, coupon rates and platform registration status change; confirm current figures or consult a qualified professional before acting.</em></p>"),

]
