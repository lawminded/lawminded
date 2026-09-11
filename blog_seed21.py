# Owner-requested comparison article, queued 5 September 2026, written
# 11 September 2026.
#
# The owner asked for this off the Search Console data (docs/gsc-performance-
# 2026-08-26.xlsx): "pas 3 vs pas 4" sits at 6 impressions, average position
# 2.8, no page of its own on the site — the second-best comparison gap after
# RTI vs PIL, which blog_seed20.py already filled.
#
# The material on the full Section 42 private-placement process already lives
# in private-placement-section-42 (PAS-3 mentioned 9 times, PAS-4 8 times in
# that article's own text). This piece deliberately does not repeat that
# process — it links to it — and instead answers the one question the search
# term actually asks: these are not two options, they are two steps of one
# private placement, and they run on different clocks.
#
# Every figure checked against primary text before writing, not taken from
# secondary commentary alone:
#
#  - Section 42(6), (8), (9), Companies Act 2013 — 60-day allotment window,
#    return of allotment requirement, and the Rs 1,000/day (capped Rs 25 lakh)
#    penalty for late filing. Cross-checked across indiankanoon.org's mirror
#    of the section and ca2013.com's Integrated Ready Reckoner, which agreed
#    independently on every figure.
#  - Rule 14(6), Companies (Prospectus and Allotment of Securities) Rules,
#    2014 — PAS-3 due within FIFTEEN days of allotment for a Section 42
#    private placement. Confirmed three times independently: indiankanoon.org's
#    mirror of Rule 14, ca2013.com's Rule 14 page, and ibclaw.in's consolidated
#    text of the Rules, all quoting "within fifteen days of allotment"
#    verbatim from sub-rule (6).
#  - Rule 12, same Rules — PAS-3 due within THIRTY days for an allotment made
#    outside Section 42 (ESOP exercise, bonus issue, rights issue). This is
#    the distinction the search term is actually confused about: the 30-day
#    figure people remember from an ordinary allotment does not apply to a
#    private placement. Confirmed on ca2013.com's Rule 12 page and ibclaw.in's
#    consolidated Rules text.
#  - One AI-summarised fetch, before these three-way checks, wrongly claimed a
#    2022 amendment (G.S.R. 338(E), 5 May 2022) had moved the private-placement
#    PAS-3 deadline from 15 to 30 days. Fetching ibclaw.in's own text of that
#    notification directly showed this was wrong — the 2022 amendment only
#    added a land-border-country FDI proviso to Rule 14(1) and a matching
#    checkbox to PAS-4. The 15-day figure was never touched by it. Left out of
#    the article entirely, since it does not survive verification, but noted
#    here because it is exactly the kind of confidently-wrong AI summary this
#    process exists to catch.
#  - The 2018 removal of PAS-4/PAS-5 from ROC filing (Companies (Prospectus
#    and Allotment of Securities) Second Amendment Rules, 2018) is carried
#    over from private-placement-section-42, which verified it in an earlier
#    session; not re-verified from the primary notification text here, since
#    mca.gov.in returns 403 to direct fetch (see automation/notes.md) and the
#    r.jina.ai proxy attempt on this specific PDF returned a 404 rather than
#    the document.
#  - Hexafun Private Limited, ROC Delhi adjudication order under Section
#    42(9), dated 29 September 2025: 200 CCDs allotted 19 December 2023,
#    PAS-3 due within 15 days (the article computes ~3 January 2024 from that
#    date), filed 23 February 2024 — 51 days late. Penalty Rs 25,500 on the
#    company and Rs 25,500 each on the two directors who were officers in
#    default, Rs 76,500 total; a third director appointed after the default
#    was exempted. Reported by TaxGuru and independently by Studycafe with
#    matching figures; both are professional-commentary write-ups of a real
#    ROC adjudication order rather than the order PDF itself, which was not
#    directly retrievable in this session — flagged here as a lead followed
#    as far as it could be, not a primary document read cover to cover.
#
# Format matches the earlier seeds: (title, slug, category, act, read_time,
# summary, content).

BLOG_ARTICLES_21 = [

    ('PAS-3 vs PAS-4: Not Two Options, But Two Steps of the Same Private Placement',
     'pas-3-vs-pas-4',
     'corp',
     'Companies Act 2013',
     '7 min read',
     "PAS-4 is the offer letter a company sends to investors before allotment. PAS-3 is the return it files with the Registrar after. They are not alternatives on a checklist, and the deadline for PAS-3 after a private placement is 15 days, not the 30 most people expect.",

     "<p><em>Search \"PAS-3 vs PAS-4\" and most of what comes up treats it like a choice — debit card or credit card, pick one. If a compliance checklist just handed you both forms while you're raising a private placement round, the question that actually matters isn't which one to file. It's which one first, and by when.</em></p>"

     "<p><strong>PAS-4 is the offer letter a company sends to investors before it allots shares; PAS-3 is the return it files with the Registrar after. A private placement under Section 42 of the Companies Act needs both, in that order, not a choice between them.</strong></p>"

     "<blockquote><p><strong>BOTTOM LINE</strong></p><p>PAS-4 goes outward, to named investors, before any money is allotted — and since a 2018 rule change, it isn't filed with the Registrar at all, only issued and kept on record. PAS-3 goes the other way: it's filed with the Registrar after allotment, and for a private placement the deadline is fifteen days, not the thirty days that applies to an ordinary allotment under Section 39. That fifteen-day clock, more than the choice between forms, is where companies actually get penalised.</p></blockquote>"

     "<h2>Two forms, two directions</h2>"
     "<p>Both names start with PAS because both sit inside the same rulebook, the Companies (Prospectus and Allotment of Securities) Rules, 2014. That's most of why they get confused. Past that, they don't do the same job at all.</p>"
     "<p>PAS-4 is addressed to people outside the company — the investors a board has already identified by name. PAS-3 is addressed to the Registrar of Companies, a government filing, and it only exists because an allotment has already happened. One opens the transaction, the other closes it. A company that has filed PAS-3 without ever having issued PAS-4 hasn't taken a shortcut; it has skipped a step that Section 42 treats as mandatory.</p>"

     "<h2>PAS-4: the offer letter that starts the clock</h2>"
     "<p>Form PAS-4 is the private placement offer-cum-application letter, governed by Rule 14 of the PAS Rules. A few things about it surprise people who've only heard of it in passing.</p>"
     "<p>It can only go to persons the board has identified and recorded by name before the offer is made — there's no \"and others we may add later.\" It also has to be serially numbered. And it can't be issued until the company has passed a special resolution and filed Form MGT-14 for that resolution. The person receiving it can accept the offer or refuse it; they cannot pass it on to someone else, since private placement carries no right of renunciation.</p>"
     "<p>Here's the detail that trips up anyone reading an older guide: since the Companies (Prospectus and Allotment of Securities) Second Amendment Rules, 2018, PAS-4 is no longer filed with the Registrar. Before that amendment, a copy went to the ROC within 30 days of circulation. Now the company issues it to investors and keeps a record of every offer made, in Form PAS-5, but nothing about PAS-4 itself reaches the government until much later, through PAS-3. <a href=\"/article/private-placement-section-42\">This site's Section 42 guide</a> covers the full mechanics of a private placement — the 200-person cap, the valuation report, the separate bank account, the 60-day allotment window. This article only deals with where the two PAS forms sit in that sequence.</p>"

     "<h2>PAS-3: the return that closes it, and the fifteen-day trap</h2>"
     "<p>Form PAS-3 is the return of allotment — a filing that tells the Registrar shares (or debentures, or any other security) have actually been issued, to whom, and for how much. Every company files it after every allotment, regardless of how the shares were issued. What changes is the deadline, and this is the part that actually causes confusion.</p>"
     "<p>An ordinary allotment — say, shares issued on an ESOP exercise, a bonus issue, or a rights issue under Section 62 — is governed by Rule 12 of the PAS Rules. There, the company has <strong>30 days</strong> from the date of allotment to file PAS-3. An allotment made through a private placement under Section 42 is governed by a different provision, Rule 14(6), and the window there is <strong>15 days</strong>, exactly half.</p>"
     "<p>A company secretary who has filed PAS-3 a dozen times for ESOP allotments, always on the familiar 30-day rhythm, can walk straight into this. The form looks the same, the section of the MCA portal is the same, and nothing on the face of it announces that the clock just got shorter. It did, because the money came in through a private placement rather than an ordinary issue. The company also can't touch that money at all until PAS-3 is filed — so the fifteen days isn't just a filing deadline, it's how long the funds sit frozen.</p>"

     "<h2>What fifteen days late actually costs</h2>"
     "<p>Hexafun Private Limited allotted 200 compulsorily convertible debentures through a private placement on 19 December 2023. Rule 14(6) gave it until roughly 3 January 2024 to file PAS-3. It filed on 23 February 2024 — 51 days after the deadline.</p>"
     "<p>The Registrar of Companies, Delhi, adjudicated the default under Section 42(9) in September 2025. The company was fined ₹25,500. Two directors who counted as officers in default at the time were fined ₹25,500 each — ₹76,500 in total. A third director, appointed only after the default had already occurred, was let off.</p>"
     "<p>Section 42(9) prices the delay at ₹1,000 a day, for each defaulting party, capped at ₹25 lakh, and the clock keeps running for every day the return stays unfiled — it isn't a one-time fine for missing the date. Hexafun's own filing shows the arithmetic works close to exactly: 51 days at roughly ₹500 a day per party comes out near the ₹25,500 figure the order records. This is a routine adjudication, not a scandal, which is exactly the point — the fifteen-day deadline gets missed often enough that the ROC has a standard template for penalising it.</p>"

     "<h2>Common mistakes</h2>"
     "<ul>"
     "<li><strong>Assuming PAS-3 always has a 30-day window.</strong> That's true only for allotments outside Section 42. A private placement halves it.</li>"
     "<li><strong>Trying to file PAS-4 with the Registrar.</strong> Since 2018 it isn't a ROC filing at all — issue it to investors and keep it on record instead.</li>"
     "<li><strong>Spending the money before PAS-3 is filed.</strong> The funds are legally frozen until the return goes in, private placement or not.</li>"
     "<li><strong>Treating the two forms as alternatives on a checklist.</strong> Every private placement needs both, in sequence — PAS-4 before allotment, PAS-3 after.</li>"
     "<li><strong>Losing track of who counted as an officer in default.</strong> The Hexafun order shows a director who joined after the breach wasn't penalised; the ones who were on the board at the time were, individually.</li>"
     "</ul>"

     "<h2>Frequently asked questions</h2>"
     "<p><strong>What is the actual difference between PAS-3 and PAS-4?</strong> PAS-4 is the offer letter a company sends to named investors before allotment. PAS-3 is the return of allotment it files with the Registrar after allotment. They aren't alternatives — a private placement needs both.</p>"
     "<p><strong>Do I file PAS-3 or PAS-4 first?</strong> PAS-4 goes out first, to investors, before any shares are allotted. PAS-3 is filed afterward, once allotment has happened.</p>"
     "<p><strong>What is the deadline for filing PAS-3 after a private placement?</strong> Fifteen days from the date of allotment, under Rule 14(6) of the Companies (Prospectus and Allotment of Securities) Rules, 2014.</p>"
     "<p><strong>Is the PAS-3 deadline always fifteen days?</strong> No. Fifteen days applies only to allotments made through a Section 42 private placement. An ordinary allotment, such as one from an ESOP exercise or a rights issue, has thirty days under Rule 12.</p>"
     "<p><strong>Do I still need to file PAS-4 with the Registrar of Companies?</strong> No. Since the 2018 amendment to the PAS Rules, PAS-4 is issued to investors and kept on record in Form PAS-5, not filed with the ROC.</p>"
     "<p><strong>What happens if PAS-3 is filed late?</strong> The company and every officer in default are liable to a penalty of ₹1,000 for each day of delay, capped at ₹25 lakh, under Section 42(9). The company also cannot use the subscription money until PAS-3 is filed.</p>"

     "<p><strong>Primary sources</strong></p>"
     "<ul>"
     "<li>Section 42, Companies Act, 2013, including sub-sections (6), (8), (9)</li>"
     "<li>Rule 12 and Rule 14, Companies (Prospectus and Allotment of Securities) Rules, 2014</li>"
     "<li>Companies (Prospectus and Allotment of Securities) Second Amendment Rules, 2018</li>"
     "<li>Registrar of Companies, Delhi — adjudication order against Hexafun Private Limited under Section 42(9), September 2025</li>"
     "</ul>"
     "<p><em>Disclaimer: This article is general information on a fast-changing area of company law, current at the time of writing. It is not legal or professional advice for any specific company. Verify the position against the live MCA rules and consult your company secretary before filing.</em></p>"),

]
