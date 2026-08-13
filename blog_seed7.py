# One news-driven article written 13 August 2026, verified against the primary
# GSTN advisory (PDF fetched directly from tutorial.gst.gov.in) rather than
# secondary commentary. Checked against the existing 131 published articles
# first — the site had no e-way bill article of any kind, and this is also
# the only tax/GST guide that touches goods-movement compliance rather than
# returns or ITC.
#
# The underlying change: GSTN advisories dated 20.05.2026 and 17.06.2026 made
# the "Ship-to GSTIN" field mandatory for Bill-to/Ship-to e-way bills, on the
# portal and in the e-Invoice/e-Way Bill-by-IRN/EWB Closure APIs, effective in
# Production from 1 August 2026 — a date that had already passed when this was
# written, meaning some readers will already be hitting the rejection errors
# this article explains.
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
     "<p><em>If your business bills one company and delivers the goods to another — a distributor invoicing a retail chain's head office while trucking stock straight to one of its stores, a manufacturer shipping on a dealer's instructions to the dealer's customer — the way you have generated e-way bills for years stopped working on 1 August 2026. The field a lot of businesses used to leave blank, or fill in carelessly, is now the one that decides whether the e-way bill gets created at all.</em></p>"
     "<p><strong>From 1 August 2026, the Ship-to GSTIN field became mandatory for every e-way bill involving a Bill-to/Ship-to transaction, whether it is generated on the GST portal, through the e-Invoice API, or via an IRN. Leave it blank where it applies and the e-way bill is rejected. Enter your own GSTIN in it and it is rejected too, since the system now insists the Bill-to and Ship-to parties be different registrations.</strong></p>"

     "<blockquote><p><strong>The bottom line</strong></p>"
     "<p><strong>What it costs:</strong> nothing in fees. This is a mandatory data field, not a new tax, form or charge.</p>"
     "<p><strong>What it covers:</strong> every Bill-to/Ship-to e-way bill generated through the portal, the e-Invoice API, e-Way Bill by IRN, or the new EWB Closure API, from 1 August 2026 onward.</p>"
     "<p><strong>What it does not fix:</strong> anything about a straightforward transaction where the buyer and the delivery address share one GSTIN. Those e-way bills are untouched.</p></blockquote>"

     "<h2>What a Bill-to/Ship-to transaction actually is</h2>"
     "<p>Most e-way bills involve two parties. A sells to B, and the goods go to B. Nothing in this change affects that.</p>"
     "<p>A Bill-to/Ship-to transaction has three parties in the picture. A sells to B, but on B's instruction the goods are delivered directly to C — a third GSTIN that never appears on the invoice itself. This is routine in distribution: a manufacturer billing a distributor but shipping to the distributor's retailer, a company head office ordering stock that goes straight to a branch, an e-commerce seller fulfilling an order where the buyer and the delivery point are registered separately. It is exactly this three-party pattern that GSTN has now locked down.</p>"

     "<h2>Where the requirement comes from</h2>"
     "<p>GSTN first announced the change in an <strong>advisory dated 20 May 2026</strong>, which said Ship-to GSTIN would be mandatorily captured in Bill-to/Ship-to transactions, with the value <strong>\"URP\"</strong> entered where the consignee has no GST registration.</p>"
     "<p>That advisory left one thing unclear: what happens when the e-way bill is not generated separately, but produced together with an e-invoice, or later using an IRN. Trade bodies, ERP vendors, GSPs, ASPs and private IRPs asked GSTN to clarify, and a <strong>follow-up advisory dated 17 June 2026</strong> answered by extending the same mandatory field into the e-Invoice API, the e-Way Bill by IRN API, and a new EWB Closure API, all <strong>implemented in Production from 1 August 2026</strong> after a testing window in the Sandbox environment.</p>"
     "<p>It fits a pattern. <a href=\"/article/gst-returns-explained\">GSTR-1 and GSTR-3B were locked together</a> the same way over the past year, moving GST filing from a forgiving system to one where the portal checks your data before it lets a filing through. The e-way bill side of GST is now getting the same treatment on the goods-movement end.</p>"

     "<h2>The validations your data now has to pass</h2>"
     "<p>Getting the field filled in is not enough on its own. GSTN built four checks around it, and any one of them failing stops the e-way bill:</p>"
     "<ul>"
     "<li><strong>A valid GSTIN.</strong> The system checks the Ship-to GSTIN the same way it checks any other GSTIN entered on the portal.</li>"
     "<li><strong>Different from the Bill-to GSTIN.</strong> In a genuine Bill-to/Ship-to transaction the two parties are expected to be distinct, so entering the same GSTIN in both fields is now rejected rather than silently accepted.</li>"
     "<li><strong>State code match.</strong> The Ship-to State Code has to correspond to the state code embedded in the Ship-to GSTIN itself.</li>"
     "<li><strong>PIN code match.</strong> The Ship-to PIN code has to belong to that same declared state.</li>"
     "</ul>"
     "<p>Where the e-way bill is generated together with an IRN, a mandatory field called <strong>ShipDtls.Gstin</strong> now appears in the Generate IRN payload whenever Ship-to details are provided. Where the e-way bill is generated afterward using the IRN, a new field called <strong>Gstin</strong> under <strong>ExpShipDtls</strong> is mandatory in the same way. An ERP or billing system that has not been updated to send this field will see the transaction rejected with a specific error code rather than a generic failure — 5002 or 2323 at the IRN stage, 5001 or 2324 at the e-way-bill-by-IRN stage, and 2325, 4074 or 3039 for the state and PIN code checks, depending on which validation failed.</p>"

     "<h2>When the consignee has no GST registration</h2>"
     "<p>Not every Ship-to party is GST-registered. A retailer might ship on to an individual customer, or to a business below the registration threshold. For these cases GSTN kept the same convention it has used elsewhere: enter <strong>\"URP\"</strong> — unregistered person — in the Ship-to GSTIN field. This is treated as a valid entry, not a workaround, and it applies wherever the Ship-to party genuinely has no GSTIN to declare.</p>"

     "<h2>Exports, and B2B/SEZ transactions</h2>"
     "<p>Two categories get slightly different treatment.</p>"
     "<p><strong>Exports.</strong> Ship details, including GSTIN, that were provided when the IRN was generated may still be replaced when the e-way bill is generated afterward. Where there is no domestic Ship-to GSTIN to declare — the goods are simply leaving the country — URP may be entered instead.</p>"
     "<p><strong>B2B and SEZ transactions.</strong> Here it works the other way: Ship details entered at the IRN stage are locked and cannot be replaced when the e-way bill is generated later. If GSTIN was not provided at the IRN stage, it can still be added at the e-way bill stage, subject to the usual validations. And for older IRNs that were generated with the same GSTIN in both the Bill-to and Ship-to fields — before this rule existed — the e-Way Bill by IRN API will simply produce a regular e-way bill rather than reject the transaction retroactively.</p>"

     "<h2>The other half of the advisory: closing an e-way bill</h2>"
     "<p>Alongside the mandatory field, GSTN introduced something that works in the reader's favour: a <strong>voluntary facility to close an e-way bill</strong> once the goods have actually been delivered. It changes nothing about validity periods or generation, and no one is required to use it. What it does is let the supplier, the recipient, the transporter, or a driver or authorised person whose mobile number was registered for the purpose, mark the e-way bill as delivered — either one at a time or several at once for a given date, through the portal or through a new closure API that takes the e-way bill number, a closure date and a remark.</p>"
     "<p>The practical use is evidentiary. An e-way bill sitting in Active status weeks after the goods clearly moved is one more loose end if a transaction is ever questioned in an audit or a detention dispute. Recording closure on the system, rather than relying only on a delivery challan in a file somewhere, gives the business its own timestamped record that the movement was completed.</p>"
     "<p>One caveat: GSTN has kept the existing status framework of Active, Cancelled and Discarded in place during what it calls an \"initial stabilisation period,\" so a closed e-way bill does not yet show a distinct \"Closed\" status, and actions like updating the transporter or the vehicle remain possible even after closure. A separate Closed status is only proposed for later.</p>"

     "<h2>Worked example</h2>"
     "<p>A Delhi-based electronics distributor sells a consignment worth Rs 4,20,000 to a retail chain's head office in Mumbai. The invoice is billed to the Mumbai head office, but on its instructions the goods are trucked directly to one of the chain's stores in Pune, which holds its own separate GST registration.</p>"
     "<p>Before 1 August, the distributor's ERP may have left the Ship-to GSTIN field blank, or duplicated the Mumbai head office's GSTIN into it out of habit. Either would have gone through. Generating that same e-way bill today needs the <strong>Pune store's own GSTIN</strong> entered as Ship-to. Leaving it blank now triggers error 5002 or 5001 depending on the API path used. Copying in the Mumbai GSTIN triggers error 2323 or 2324, since Bill-to and Ship-to cannot match. If the Pune outlet had instead been an individual buyer with no GST registration, the correct entry would have been <strong>URP</strong>, not a blank field and not the head office's GSTIN either.</p>"

     "<h2>Common mistakes</h2>"
     "<ul>"
     "<li><strong>Assuming this touches every e-way bill.</strong> It only applies where Ship-to details are genuinely different from Bill-to. Ordinary two-party sales are unaffected.</li>"
     "<li><strong>Copying the Bill-to GSTIN into the Ship-to field</strong> to get past the form quickly. The system now hard-rejects this in a Bill-to/Ship-to transaction.</li>"
     "<li><strong>Leaving ERP or GSP integration unupdated</strong> past 1 August and discovering the failure mid-dispatch, when the truck is already loaded.</li>"
     "<li><strong>Treating URP as an occasional shortcut</strong> rather than the correct, required entry whenever the Ship-to party has no GSTIN.</li>"
     "<li><strong>Assuming e-way bill closure is compulsory.</strong> It is not. Skipping it just means the only record of delivery is whatever paperwork the business keeps on its own.</li>"
     "<li><strong>Assuming a closed e-way bill is frozen.</strong> During this stabilisation period, transporter updates, vehicle updates and validity extension all remain available after closure.</li>"
     "</ul>"

     "<h2>Frequently asked questions</h2>"
     "<p><strong>Does the Ship-to GSTIN rule apply to every e-way bill?</strong> No. It applies only to Bill-to/Ship-to transactions, where the party being billed and the party receiving the goods are different. If you bill and ship to the same registration, nothing changes for you.</p>"
     "<p><strong>What do I enter if the person receiving the goods has no GST registration?</strong> Enter \"URP\", which stands for unregistered person, in the Ship-to GSTIN field.</p>"
     "<p><strong>Can I enter my own GSTIN in the Ship-to field to get past the error?</strong> No. The system now rejects a Ship-to GSTIN that matches the Bill-to GSTIN in a Bill-to/Ship-to transaction, since the two are expected to be distinct parties.</p>"
     "<p><strong>From when did this actually become mandatory?</strong> GSTN announced the requirement in an advisory dated 20 May 2026, clarified how it applies to the e-Invoice and e-Way Bill by IRN APIs in a follow-up advisory dated 17 June 2026, and put both changes into Production on 1 August 2026.</p>"
     "<p><strong>Is the e-way bill closure facility compulsory?</strong> No. It is voluntary and only records that delivery is complete. Nothing forces a supplier, recipient or transporter to use it.</p>"
     "<p><strong>Who is allowed to close an e-way bill?</strong> The supplier, the recipient, the transporter, or a driver or authorised person whose mobile number was registered for that purpose.</p>"
     "<p><strong>What happens if my Ship-to State Code doesn't match the GSTIN I entered?</strong> The system rejects the entry. The Ship-to State Code has to correspond to the state code embedded in the Ship-to GSTIN, and the PIN code has to belong to that same state.</p>"
     "<p><strong>Does this change apply to export e-way bills?</strong> Partially. For exports, Ship details including GSTIN given at the IRN stage may still be replaced when the e-way bill is generated, and URP can be used where there is no domestic Ship-to GSTIN to declare.</p>"),

]
