# Owner-requested article, 25 August 2026.
#
# Owner asked directly over Telegram: how to apply for a free, instant e-PAN
# from the income tax department's own website, and confirmation that a
# physical card costs Rs 50 for delivery within India. Checked the 133
# published slugs and grepped blog_seed*.py for "PAN card", "e-PAN" and
# "instant PAN" first — PAN comes up inside the HUF, freelancer and rent-
# agreement articles, but no article covers how an individual actually
# applies for one. Genuine gap, so this is an evergreen guide.
#
# Verified against primary sources:
#  - incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/instant-e-pan
#    and incometax.gov.in/iec/foportal/help/e-filing-generate-instant-e-pan-faq
#    (Income Tax Department's own Instant e-PAN help pages, fetched directly):
#    free, pre-login service; individual with no PAN already allotted, valid
#    Aadhaar linked to an active mobile number, DigiLocker access; minors,
#    Representative Assessees (Section 160) and foreign citizens (e-KYC mode)
#    excluded; process is Get New e-PAN -> enter Aadhaar -> mobile OTP ->
#    DigiLocker date-of-birth proof -> optional email validation -> submit;
#    Acknowledgement Number and SMS confirmation on success; status checked
#    post-login-free via Aadhaar + OTP; no physical PAN card issued by this
#    service, only the digitally signed e-PAN PDF.
#  - onlineservices.proteantech.in/paam/ReprintEPan.html (Protean, formerly
#    NSDL, the Income Tax Department's authorised PAN service provider;
#    fetched directly): reprint of a physical PAN card costs Rs 50
#    (inclusive of taxes) for dispatch within India, Rs 959 for dispatch
#    outside India; requires PAN number, Aadhaar (individuals) and full date
#    of birth; e-PAN re-download is free within 30 days of allotment/change.
#  - PIB Research Unit, Ministry of Finance, "PAN 2.0: A Digital Leap in
#    Taxpayer Services," 27 November 2024 (static.pib.gov.in PDF, fetched
#    directly): Cabinet approved the PAN 2.0 Project on 25 November 2024 at
#    a cost of Rs 1,435 crore; allotment/updation/correction of PAN stays
#    free of cost with the e-PAN emailed to the applicant; a physical card
#    costs "the prescribed fee of Rs 50 (domestic)" under the same project,
#    confirming the fee independently of the Protean page above; existing
#    PAN cardholders are not required to apply afresh; the QR code itself is
#    not new (present on PAN cards since 2017-18) but becomes dynamic under
#    PAN 2.0.
#  - Form 93 replacing Form 49A for individual Indian citizens, effective 1
#    April 2026 under Rule 158 of the Income-tax Rules, 2026 read with
#    Section 262 of the Income-tax Act, 2025: corroborated across multiple
#    independent professional summaries (taxguru.in, cleartax.in,
#    businesstoday.in, lendingkart.com) that agree on the form numbers, the
#    effective date and the governing rule/section, consistent with the
#    Form 94 detail already verified for the HUF article in blog_seed10.py.
#    The Rs 107 (domestic) / ~Rs 1,017 (foreign) fee for this paid route is
#    corroborated the same way (taxguru.in's reproduced fee table, plus
#    bankbazaar.com, paytm.com and finpulseindia.com agreeing on the same
#    figures) rather than fetched from a single official fee schedule PDF —
#    flagged here as the weaker-sourced figure in this article, on a point
#    that is secondary to the free instant e-PAN process itself.
#  - Section 465 of the Income-tax Act, 2025 as the renumbered successor to
#    Section 272B (penalty for PAN non-compliance) was checked but not used
#    in the article: search aggregation agreed on the section mapping but
#    not clearly enough on the current penalty amount to state a figure, and
#    the point wasn't essential to the how-to-apply focus of this piece.
#
# Format matches the earlier seeds: (title, slug, category, act, read_time,
# summary, content).

BLOG_ARTICLES_12 = [

    ('Instant e-PAN: How to Apply for a PAN Card Online for Free (2026 Guide)',
     'instant-e-pan-apply-online-free',
     'tax',
     'Income-tax Act, 2025',
     '6 min read',
     "The Income Tax Department's e-filing portal lets most first-time applicants get a digitally signed e-PAN for free, in minutes, using nothing but Aadhaar OTP and DigiLocker. No agent, no form to fill by hand, no fee. A physical card costs Rs 50 for delivery within India if you want the plastic version too.",
     "<p><em>Most people discover they need a PAN at the worst possible moment: a new bank account stuck at the KYC stage, or a mutual fund application that simply won't submit without one. The instinct is to search for an agent nearby who \"does PAN cards,\" which usually means a service fee on top of a wait. There's a faster route that costs nothing.</em></p>"
     "<p><strong>If you've never had a PAN, have an Aadhaar card with a mobile number linked to it, and are an adult, you can get a legally valid e-PAN from the Income Tax Department's own website in a few minutes, for free.</strong></p>"
     "<blockquote><strong>Bottom line:</strong> Instant e-PAN through the e-filing portal costs nothing and typically completes within minutes to a couple of hours. It covers most first-time individual applicants. It does not cover minors, people without an Aadhaar-linked mobile number, foreign citizens, or anyone who already holds a PAN and needs a correction. A physical card, if you want one, costs Rs 50 for delivery within India.</blockquote>"

     "<h2>Who the free instant route actually covers</h2>"
     "<p>The Income Tax Department runs a service called Instant e-PAN on its e-filing portal, incometax.gov.in. It's built for one specific situation: an individual who has never been allotted a PAN before, and who has a valid Aadhaar with a mobile number linked to it. That's the whole eligibility test in practice, but a few groups fall outside it.</p>"
     "<p>You can't use this route if you already have a PAN (in which case you'd be requesting a correction or reprint, not a new one), if you're a minor at the time of applying, or if you're what the tax law calls a \"representative assessee\" (someone applying on behalf of another person or entity, such as a legal guardian or an estate's executor). Foreign citizens also can't use this specific route, because it depends on Aadhaar-based e-KYC, which foreign nationals typically don't have.</p>"
     "<p>If any of that describes you, skip ahead to the section on the paid application route below. Everyone else can use the free process.</p>"

     "<h2>The step-by-step process</h2>"
     "<p>The whole thing happens on incometax.gov.in and needs no paperwork, no photograph, and no signature upload.</p>"
     "<ol>"
     "<li>Go to the e-filing portal and find \"Instant e-PAN\" under Quick Links on the homepage. Click \"Get New e-PAN.\"</li>"
     "<li>Enter your 12-digit Aadhaar number and confirm you agree to the terms.</li>"
     "<li>You'll get a 6-digit OTP on the mobile number linked to your Aadhaar. Enter it to verify.</li>"
     "<li>The portal redirects you to DigiLocker, where you consent to it pulling a date-of-birth document already stored there, such as your Aadhaar record, driving licence, birth certificate, or Class X marksheet.</li>"
     "<li>You'll have the option to validate an email address for future correspondence. This step is optional but worth doing.</li>"
     "<li>Submit the application. You'll get an Acknowledgement Number on screen, and a confirmation message on your linked mobile number.</li>"
     "</ol>"
     "<p>You can track the application afterward without logging in: there's a \"Check Status/Download PAN\" option on the same portal that asks for your Aadhaar number and an OTP. Once it's approved, a digitally signed e-PAN in PDF form is generated. That PDF, on its own, is a fully valid PAN for tax filing, bank KYC, and most other purposes that ask for one.</p>"

     "<h2>Getting a physical card, if you want one</h2>"
     "<p>The e-PAN is a document, not a card. Plenty of people never need the plastic version; the PDF works for e-filing, for most bank and demat account KYC, and for quoting your PAN on forms. But some situations, particularly older or more cautious institutions, still ask to see a physical card.</p>"
     "<p>If you want one, you apply separately through Protean (the company formerly known as NSDL, which along with UTIITSL runs India's PAN infrastructure on the department's behalf) using its reprint service. You'll need your PAN number, your Aadhaar number, and your full date of birth. The fee for delivery within India is Rs 50, inclusive of tax. Delivery abroad costs more and is charged separately based on the destination. The card typically reaches the address on file with the department by India Post Speed Post within 15 to 20 working days.</p>"
     "<p>The Cabinet approved the broader PAN 2.0 modernisation project in November 2024, which is gradually merging the department's three separate PAN portals into one. That project sets the same fee: allotment stays free, and a physical card costs Rs 50 for a domestic address, confirming the Protean figure from an independent source.</p>"

     "<h2>If Aadhaar details don't match, or you're not eligible</h2>"
     "<p>If your Aadhaar has an outdated name, address, or date of birth, fix that first at UIDAI's own portal before applying for e-PAN, since the tax department pulls your details directly from Aadhaar and won't reconcile mismatches for you. If your mobile number isn't linked to Aadhaar at all, you'll need to visit a nearby Aadhaar enrolment centre to link it before the OTP step will work.</p>"
     "<p>If you're not eligible for the instant route at all, either because you're not an individual (a Hindu Undivided Family or a company applies differently, as covered in our <a href=\"/article/hindu-undivided-family-huf-tax-guide\">guide to HUF taxation</a>), a minor, a foreign national, or someone needing a correction to an existing PAN, you apply through the standard paid channel instead. As of 1 April 2026, the old Form 49A was retired; individual Indian citizens now use Form 93, filed online through Protean or UTIITSL or in person at a PAN centre, under Rule 158 of the Income-tax Rules, 2026. This route isn't free: current fee schedules put it at roughly Rs 107 for a card delivered within India, more for delivery abroad. It also takes longer than instant e-PAN, since it isn't a same-day Aadhaar-verified process.</p>"

     "<h2>Common mistakes</h2>"
     "<ul>"
     "<li>Paying an agent for something the portal does free. Search results for \"PAN card apply\" are full of paid intermediary sites that charge a service fee for the same instant e-PAN application you can file yourself in minutes.</li>"
     "<li>Applying for a second PAN because you've forgotten or misplaced your old number. Holding more than one PAN is not allowed under the Income-tax Act, and the fix if it happens by accident is to get the duplicate deactivated through your jurisdictional Assessing Officer, not to apply fresh.</li>"
     "<li>Giving up because the OTP step fails, without realising the actual problem is an Aadhaar mobile number that was never linked, or was linked to a number you no longer use.</li>"
     "<li>Assuming the PDF isn't \"real\" and spending money on a physical card you don't actually need for whatever you're doing right then, whether that's e-filing a return or completing a demat account's KYC.</li>"
     "</ul>"

     "<h2>Frequently asked questions</h2>"
     "<p><strong>Is the e-PAN from the income tax website really free?</strong> Yes. Allotment of a new PAN through the Instant e-PAN service costs nothing, and the digitally signed e-PAN PDF is sent to you at no charge.</p>"
     "<p><strong>How long does instant e-PAN actually take?</strong> Most applications complete within minutes once Aadhaar OTP verification and the DigiLocker step go through, though the department doesn't guarantee a fixed turnaround, and some applications can take longer if there's a name or address mismatch to resolve.</p>"
     "<p><strong>Can I apply for instant e-PAN without a smartphone?</strong> You need access to a browser, your Aadhaar-linked mobile for the OTP, and a DigiLocker account, which you can also access through a desktop browser rather than only an app, so a smartphone helps but isn't strictly required.</p>"
     "<p><strong>Do I need a physical PAN card at all?</strong> Not usually. The e-PAN PDF is a valid PAN for filing returns and for KYC at most banks and financial institutions. Get the physical card only if a specific institution insists on seeing one.</p>"
     "<p><strong>What if I already applied years ago and never got a card?</strong> If a PAN was already allotted to you, even long ago, you're not eligible for Instant e-PAN as a \"new\" applicant. Use Protean's or UTIITSL's reprint or correction service instead, quoting your existing PAN number.</p>"
     "<p><strong>I'm a freelancer. Do I need this PAN for anything besides opening a bank account?</strong> Yes. Any client deducting TDS on your professional fees needs your PAN to credit it against your name, and a missing or wrong PAN means that tax shows up nowhere you can claim it. See our <a href=\"/article/income-tax-freelancers\">guide to freelancer income tax</a> for how that credit works.</p>"
     "<p><em>This article is for legal awareness and education only and is not tax or legal advice. Fees and procedures are set by the Income Tax Department and its authorised service providers and can change; confirm current details on incometax.gov.in before applying.</em></p>"),

]
