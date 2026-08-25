# Two articles written 13 August 2026.
#
# The first is news-driven, verified against the primary GSTN advisory (PDF
# fetched directly from tutorial.gst.gov.in) rather than secondary commentary.
# Checked against the existing 131 published articles first — the site had no
# e-way bill article of any kind, and this is also the only tax/GST guide that
# touches goods-movement compliance rather than returns or ITC.
#
# The underlying change: GSTN advisories dated 20.05.2026 and 17.06.2026 made
# the "Ship-to GSTIN" field mandatory for Bill-to/Ship-to e-way bills, on the
# portal and in the e-Invoice/e-Way Bill-by-IRN/EWB Closure APIs, effective in
# Production from 1 August 2026 — a date that had already passed when this was
# written, meaning some readers will already be hitting the rejection errors
# this article explains.
#
# The second, requested directly by the owner, is an evergreen gap-fill on
# compounding of offences under the Companies Act — the site covered ROC
# adjudication and the CCFS-2026 late-filing scheme but had nothing on
# Section 441 itself. Verified against the Gazette text of the Companies
# (Amendment) Act, 2019 (raised the Regional Director ceiling from five lakh
# to twenty-five lakh rupees, and rewrote Section 441(6) on what cannot be
# compounded at all), the Companies (Amendment) Act, 2020 (replaced the
# original imprisonment-or-fine consequence for ignoring a compounding
# authority's filing order with a doubled fine instead), and the Companies
# (Registration Offices and Fees) Rules, 2014 (Form GNL-1, filed with the
# Registrar under rule 12(2)). The seven-day intimation and three-year bar in
# Section 441(2)-(3) were cross-checked against two independent bare-act
# reproductions after the canonical indiacode/mca.gov.in pages returned 403 to
# every fetch tried from this box.
#
# Format matches the earlier seeds: (title, slug, category, act, read_time,
# summary, content).
BLOG_ARTICLES_7 = [

    ('Ship-to GSTIN Is Now Mandatory on E-Way Bills: What Changed on 1 August 2026',
     'eway-bill-ship-to-gstin-mandatory-2026',
     'tax',
     'CGST Rules, 2017',
     '7 min read',
     'GSTN made the Ship-to GSTIN field mandatory for every Bill-to/Ship-to e-way bill from 1 August 2026. Leave it blank, or copy in your own GSTIN, and the system now rejects it outright.',
     "<p><em>If your business bills one company and ships the goods to another — a distributor invoicing a retail chain's head office while trucking stock to one of its own stores, a manufacturer shipping on a dealer's instructions straight to the dealer's customer — the way you've generated e-way bills for years stopped working on 1 August 2026. The field most businesses used to leave blank, or fill in without much thought, is now the one that decides whether the e-way bill gets created at all.</em></p>"
     "<p><strong>From 1 August 2026, the Ship-to GSTIN field became mandatory for every e-way bill involving a Bill-to/Ship-to transaction, whether it's generated on the GST portal, through the e-Invoice API, or via an IRN. Leave it blank where it applies and the e-way bill is rejected. Enter your own GSTIN instead and it's rejected too, because the system now requires the Bill-to and Ship-to parties to be different registrations.</strong></p>"
     "<blockquote><p><strong>The bottom line</strong></p>"
     "<p><strong>What it costs:</strong> nothing in fees. This is a mandatory data field, not a new tax, form or charge.</p>"
     "<p><strong>What it covers:</strong> every Bill-to/Ship-to e-way bill generated through the portal, the e-Invoice API, e-Way Bill by IRN, or the new EWB Closure API, from 1 August 2026 onward.</p>"
     "<p><strong>What it does not fix:</strong> a straightforward transaction where the buyer and the delivery address share one GSTIN. Those e-way bills are untouched.</p></blockquote>"

     "<h2>What a Bill-to/Ship-to transaction actually is</h2>"
     "<p>Most e-way bills involve two parties. A sells to B, and the goods go to B. Nothing in this change touches that.</p>"
     "<p>A Bill-to/Ship-to transaction has three parties in the picture. A sells to B, but on B's instruction the goods go straight to C, a third GSTIN that never appears on the invoice itself. It's routine in distribution: a manufacturer billing a distributor but shipping to the distributor's retailer, a head office ordering stock that goes directly to a branch, an e-commerce seller fulfilling an order where the buyer and the delivery point are registered separately. This three-party pattern is exactly what GSTN has now locked down.</p>"

     "<h2>Where the requirement comes from</h2>"
     "<p>GSTN first announced the change in an <strong>advisory dated 20 May 2026</strong>, which said Ship-to GSTIN would be mandatorily captured in Bill-to/Ship-to transactions, with the value <strong>\"URP\"</strong> entered where the consignee has no GST registration.</p>"
     "<p>That advisory left one thing unclear: what happens when the e-way bill isn't generated separately, but produced together with an e-invoice, or later using an IRN. Trade bodies, ERP vendors, GSPs, ASPs and private IRPs asked GSTN to clarify. A <strong>follow-up advisory dated 17 June 2026</strong> answered by extending the same mandatory field into the e-Invoice API, the e-Way Bill by IRN API, and a new EWB Closure API, all <strong>implemented in Production from 1 August 2026</strong> after a testing window in the Sandbox environment.</p>"
     "<p>It fits a pattern. <a href=\"/article/gst-returns-explained\">GSTR-1 and GSTR-3B were locked together</a> the same way over the past year, moving GST filing from a forgiving system to one where the portal checks your data before it lets a filing through. The e-way bill side of GST is now getting the same treatment on the goods-movement end.</p>"

     "<h2>The validations your data now has to pass</h2>"
     "<p>Getting the field filled in isn't enough on its own. GSTN built four checks around it, and any one of them failing stops the e-way bill: the Ship-to GSTIN has to be valid, checked the same way the system checks any other GSTIN on the portal; it has to differ from the Bill-to GSTIN, since a genuine Bill-to/Ship-to transaction is expected to involve two distinct parties; the Ship-to State Code has to correspond to the state code embedded in the GSTIN itself; and the Ship-to PIN code has to belong to that same declared state.</p>"
     "<p>Where the e-way bill is generated together with an IRN, a mandatory field called <strong>ShipDtls.Gstin</strong> now appears in the Generate IRN payload whenever Ship-to details are provided. Where it's generated afterward using the IRN, a new field called <strong>Gstin</strong> under <strong>ExpShipDtls</strong> is mandatory in the same way. An ERP or billing system that hasn't been updated to send this field won't get a generic failure. It will get a specific error code: 5002 or 2323 at the IRN stage, 5001 or 2324 at the e-way-bill-by-IRN stage, and 2325, 4074 or 3039 for the state and PIN code checks, depending on which validation failed.</p>"

     "<h2>When the consignee has no GST registration</h2>"
     "<p>Not every Ship-to party is GST-registered. A retailer might ship to an individual customer, or to a business below the registration threshold. For these cases GSTN kept the convention it uses elsewhere: enter <strong>\"URP\"</strong> (unregistered person) in the Ship-to GSTIN field. It counts as a valid entry wherever the Ship-to party genuinely has no GSTIN to declare.</p>"

     "<h2>Exports, and B2B/SEZ transactions</h2>"
     "<p>Two categories get different treatment.</p>"
     "<p>For exports, Ship details including GSTIN that were provided when the IRN was generated can still be replaced when the e-way bill is generated afterward. If there's no domestic Ship-to GSTIN to declare, because the goods are simply leaving the country, URP can be entered instead.</p>"
     "<p>B2B and SEZ transactions work the other way. Ship details entered at the IRN stage are locked and can't be replaced when the e-way bill is generated later. If GSTIN wasn't provided at the IRN stage, it can still be added at the e-way bill stage, subject to the usual validations. And for older IRNs generated with the same GSTIN in both the Bill-to and Ship-to fields, from before this rule existed, the e-Way Bill by IRN API will simply produce a regular e-way bill instead of rejecting the transaction after the fact.</p>"

     "<h2>The other half of the advisory: closing an e-way bill</h2>"
     "<p>Alongside the mandatory field, GSTN introduced something that actually works in the reader's favour: a <strong>voluntary facility to close an e-way bill</strong> once the goods have been delivered. It changes nothing about validity periods or generation, and nobody is required to use it. What it does is let the supplier, the recipient, the transporter, or a driver or authorised person whose mobile number was registered for the purpose, mark the e-way bill as delivered. That can happen one at a time, or several at once for a given date, through the portal or through a new closure API that takes the e-way bill number, a closure date and a remark.</p>"
     "<p>The practical use is evidentiary. An e-way bill sitting in Active status weeks after the goods clearly moved is one more loose end if a transaction gets questioned in an audit or a detention dispute. Recording closure on the system, instead of relying only on a delivery challan filed away somewhere, gives the business its own timestamped record that the movement was completed.</p>"
     "<p>One caveat: GSTN has kept the existing status framework of Active, Cancelled and Discarded in place during what it calls an \"initial stabilisation period.\" A closed e-way bill doesn't yet show a distinct \"Closed\" status, so actions like updating the transporter or the vehicle remain possible even after closure. A separate Closed status is only proposed for later.</p>"

     "<h2>Worked example</h2>"
     "<p>A Delhi-based electronics distributor sells a consignment worth Rs 4,20,000 to a retail chain's head office in Mumbai. The invoice is billed to the Mumbai head office, but on its instructions the goods go straight to one of the chain's stores in Pune, which holds its own separate GST registration.</p>"
     "<p>Before 1 August, the distributor's ERP might have left the Ship-to GSTIN field blank, or duplicated the Mumbai head office's GSTIN into it out of habit. Either would have gone through. Generating that same e-way bill today needs the <strong>Pune store's own GSTIN</strong> entered as Ship-to. Leave it blank and it now triggers error 5002 or 5001, depending on the API path used. Copy in the Mumbai GSTIN and it triggers error 2323 or 2324, since Bill-to and Ship-to can't match. If the Pune outlet had instead been an individual buyer with no GST registration, the correct entry would have been <strong>URP</strong>, not a blank field, and not the head office's GSTIN either.</p>"

     "<h2>Common mistakes</h2>"
     "<ul>"
     "<li>Assuming this touches every e-way bill, when it only applies where Ship-to details genuinely differ from Bill-to. Ordinary two-party sales are unaffected.</li>"
     "<li>Copying the Bill-to GSTIN into the Ship-to field just to get past the form. The system now hard-rejects this in a Bill-to/Ship-to transaction.</li>"
     "<li>Leaving ERP or GSP integration unupdated past 1 August and finding out mid-dispatch, once the truck is already loaded.</li>"
     "<li>Treating URP as an occasional shortcut instead of the correct entry whenever the Ship-to party has no GSTIN.</li>"
     "<li>Assuming e-way bill closure is compulsory. It isn't. Skip it, and the only record of delivery is whatever paperwork the business keeps on its own.</li>"
     "<li>Assuming a closed e-way bill is frozen. During this stabilisation period, transporter updates, vehicle updates and validity extension all stay available even after closure.</li>"
     "</ul>"

     "<h2>Frequently asked questions</h2>"
     "<p><strong>Does the Ship-to GSTIN rule apply to every e-way bill?</strong> No. It applies only to Bill-to/Ship-to transactions, where the party being billed and the party receiving the goods are different. If you bill and ship to the same registration, nothing changes for you.</p>"
     "<p><strong>What do I enter if the person receiving the goods has no GST registration?</strong> Enter \"URP\", which stands for unregistered person, in the Ship-to GSTIN field.</p>"
     "<p><strong>Can I enter my own GSTIN in the Ship-to field to get past the error?</strong> No. The system now rejects a Ship-to GSTIN that matches the Bill-to GSTIN in a Bill-to/Ship-to transaction, since the two are expected to be distinct parties.</p>"
     "<p><strong>From when did this actually become mandatory?</strong> GSTN announced the requirement in an advisory dated 20 May 2026, clarified how it applies to the e-Invoice and e-Way Bill by IRN APIs in a follow-up advisory dated 17 June 2026, and put both changes into Production on 1 August 2026.</p>"
     "<p><strong>Is the e-way bill closure facility compulsory?</strong> No. It's voluntary and only records that delivery is complete. Nothing forces a supplier, recipient or transporter to use it.</p>"
     "<p><strong>Who is allowed to close an e-way bill?</strong> The supplier, the recipient, the transporter, or a driver or authorised person whose mobile number was registered for that purpose.</p>"
     "<p><strong>What happens if my Ship-to State Code doesn't match the GSTIN I entered?</strong> The system rejects the entry. The Ship-to State Code has to correspond to the state code embedded in the Ship-to GSTIN, and the PIN code has to belong to that same state.</p>"
     "<p><strong>Does this change apply to export e-way bills?</strong> Partially. For exports, Ship details including GSTIN given at the IRN stage may still be replaced when the e-way bill is generated, and URP can be used where there is no domestic Ship-to GSTIN to declare.</p>"),

    ('Compounding Under the Companies Act: What It Costs, Who Decides, and What It Doesn\'t Fix',
     'compounding-offences-companies-act',
     'corp',
     'Companies Act, 2013',
     '7 min read',
     'Compounding lets a company or its officers pay a fixed sum to close a compoundable offence under the Companies Act instead of standing trial for it. What it costs, who decides, and why it will not touch a routine late filing.',
     '<p><em>A company misses a filing, someone points out months later that it also breached a section carrying a fine, and the directors start hearing words like "prosecution" and "special court." Most of the time, that case never gets anywhere near a courtroom.</em></p>'
     '<p><strong>Compounding lets a company or its officers pay a fixed sum to close a compoundable offence under the Companies Act, instead of standing trial for it.</strong></p>'
     '<blockquote>'
     '<p><strong>The bottom line</strong></p>'
     '<p><strong>What it costs:</strong> whatever the Regional Director or the NCLT decides, capped at the maximum fine the offence carries.</p>'
     '<p><strong>What it covers:</strong> it ends the prosecution risk for that specific offence, whether a case has already been filed or not.</p>'
     '<p><strong>What it does not fix:</strong> the underlying default. You still have to file whatever you failed to file, and it is not available at all for offences that carry mandatory imprisonment.</p>'
     '</blockquote>'
     '<h2>What compounding actually does</h2>'
     '<p>Section 441 of the Companies Act, 2013 lets certain offences be settled by paying a sum fixed by an authority, rather than being tried in a special court. The application can be made either before prosecution starts or after — the law does not force a company to wait for a summons before applying. Once an offence is compounded, that specific charge is closed. It is not a criminal conviction, and it does not create the record a conviction would.</p>'
     '<p>What it is not: an amnesty for the underlying paperwork. A company that is late filing its financial statements and also happens to have committed a fine-only offence in the process still owes the filing. Compounding deals with the offence, not the document.</p>'
     '<h2>Which offences actually qualify</h2>'
     '<p>Not everything under the Act can be compounded. The dividing line is the punishment attached to the offence. An offence that carries a fine only, or a fine or imprisonment as alternatives, can be compounded. An offence that carries imprisonment only, or imprisonment and a fine together as a mandatory combination, cannot be. Section 441(6) says so directly, in language the Companies (Amendment) Act, 2019 rewrote specifically to remove any ambiguity on the point. If a section makes both the jail term and the fine compulsory, there is no compounding route out of it, and no authority has discretion to create one.</p>'
     '<p>This matters because directors sometimes assume compounding is a general escape hatch for anything company-law related. It is not. Fraud provisions, and other sections built around mandatory imprisonment, sit outside Section 441 entirely.</p>'
     '<h2>Who decides: Regional Director or NCLT</h2>'
     '<p>Two authorities can compound an offence, and which one you land with depends purely on the size of the maximum fine, not on the size of the company or the nature of the default.</p>'
     "<p>Where the maximum fine for the offence does not exceed twenty-five lakh rupees, the Regional Director, or an officer the Central Government has authorised, can compound it. Above that figure, only the National Company Law Tribunal can. That twenty-five lakh threshold is not the original number. The Companies (Amendment) Act, 2019 raised it from five lakh rupees. Most offences a small or mid-sized company runs into sit comfortably under the current ceiling, so in practice the Regional Director's office handles the bulk of these applications, and the NCLT route stays reserved for the larger exposures.</p>"
     '<p>Whichever authority handles it, the sum they fix cannot exceed the maximum fine the offence carries. They can charge less. They cannot charge more.</p>'
     '<h2>How the application actually moves</h2>'
     "<p>The application does not go straight to the Regional Director or the Tribunal. It goes to the Registrar of Companies first, in Form GNL-1, and the Registrar forwards it on with comments attached. That comment is not a formality: the Registrar's view of the default, and of the company's compliance history, is part of what the deciding authority reads before it fixes a sum.</p>"
     '<p>The compounding authority also has the power to order the company to file whatever returns or documents triggered the default in the first place, as a condition of compounding. This is where two later amendments changed the consequence of getting it wrong. Under the original 2013 text, an officer who ignored that filing direction faced up to six months in prison, or a fine of up to one lakh rupees, or both — a criminal consequence stacked on top of the one just resolved. The Companies (Amendment) Act, 2020 replaced that with something civil instead. If the officer does not comply, the maximum fine for the offence that was compounded simply doubles. Non-compliance still costs money. It no longer risks a second prosecution.</p>'
     '<h2>What happens once it is granted</h2>'
     '<p>The consequence depends on timing. If the offence is compounded before any prosecution was filed, no prosecution can be instituted for it afterward, not by the Registrar, not by a shareholder, not by anyone the Central Government has authorised to bring one. If a prosecution was already running when the compounding order came through, the Registrar brings that order to the notice of the court hearing the case, and the company or officer is discharged.</p>'
     '<p>One procedural step is easy to miss: the company has to intimate the Registrar within seven days of the offence being compounded. It is a short window, and it falls on the company to track, not on the authority that granted the order.</p>'
     '<h2>The three-year catch</h2>'
     '<p>Compounding is not something a company can lean on repeatedly for the same kind of lapse. If a similar offence by the same company or the same officer was compounded within the preceding three years, it cannot be compounded again. The second time around, it goes to full prosecution regardless of the fine amount. A director who treats compounding as a standing fallback for a recurring compliance gap will eventually find that door closed, at exactly the point the gap becomes routine enough to actually need it.</p>'
     '<h2>Why fewer offences reach this stage than they used to</h2>'
     '<p>Between 2018 and 2020, a large slice of what used to be prosecutable company law offences moved out of Section 441 entirely. Filing defaults that once carried a criminal fine, like a late annual return or a delayed financial statement, were reclassified as civil penalties handled through in-house adjudication under Section 454, where the Registrar of Companies acts as the adjudicating officer and imposes a penalty directly. There is no prosecution to compound in that process, because there is no longer a criminal offence attached to the default. Our guide to <a href="/article/annual-compliance-companies">annual ROC compliance for companies</a> covers what those routine filings actually require.</p>'
     '<p>The practical effect is that most small companies who miss an ordinary filing deadline today are dealing with adjudication, not compounding. Section 441 still matters, but for a narrower set of offences than it covered a decade ago: the ones the 2019 and 2020 amendments left as genuine offences rather than converting into penalties. A company still carrying old, uncompounded prosecutable offences from before that shift is a different situation, and one worth taking to a professional rather than treating as routine paperwork.</p>'
     '<p>If the underlying problem is simply that filings are late and the penalty itself is the pain point, it is also worth checking whether the <a href="/article/ccfs-2026-companies-compliance-facilitation-scheme">CCFS-2026 late-filing relief scheme</a> applies before assuming compounding is the tool needed. The two solve different problems and are sometimes confused with each other.</p>'
     '<h2>Common mistakes</h2>'
     '<ul>'
     '<li>Assuming compounding is available for anything filed late. Most routine filing defaults are now civil penalties under adjudication, not offences that need compounding at all.</li>'
     '<li>Applying for compounding without first fixing the underlying default. The authority can order the filing anyway, and turning up with it already done makes the application move faster.</li>'
     '<li>Missing the seven-day intimation to the Registrar after an offence is compounded. It is easy to treat the order as the end of the process when one small step still remains.</li>'
     "<li>Assuming a Regional Director's compounding order is available a second time for a repeat of the same lapse inside three years. It is not.</li>"
     '<li>Confusing an offence that allows imprisonment or fine with one that mandates both. Only the first can be compounded; the second cannot, whatever the officer offers to pay.</li>'
     '</ul>'
     '<h2>Frequently asked questions</h2>'
     '<p><strong>Can compounding be applied for before a prosecution is even filed?</strong> Yes. Section 441 allows an application either before or after prosecution starts, and applying early avoids the case being formally instituted at all.</p>'
     '<p><strong>Does paying the compounding amount count as a criminal conviction?</strong> No. Compounding closes the offence without a trial or a conviction; it is a different outcome from being tried and found guilty.</p>'
     '<p><strong>Who decides whether the Regional Director or the NCLT handles an application?</strong> The maximum fine the offence carries decides it. Up to twenty-five lakh rupees goes to the Regional Director; above that, only the NCLT can compound it.</p>'
     '<p><strong>Can every company law offence be compounded if the company is willing to pay?</strong> No. Offences punishable with imprisonment only, or with imprisonment and a fine both mandatorily, cannot be compounded under any circumstances.</p>'
     '<p><strong>What happens if the same kind of offence happens again soon after compounding?</strong> If a similar offence by the same company or officer is committed within three years of the earlier compounding, it cannot be compounded again.</p>'
     '<p><strong>Does compounding also take care of the filing that triggered the offence?</strong> No. The compounding authority can separately order the company to file the pending document, and failing to comply doubles the fine for the offence that was compounded.</p>'
     '<p><strong>Where does the application actually get filed?</strong> With the Registrar of Companies, in Form GNL-1. The Registrar forwards it, with comments, to the Regional Director or the Tribunal depending on the fine involved.</p>'),

]
