# Owner-requested topic, queued automation/queue.md 2026-09-04 for on-or-after
# 2026-09-06, written 2026-09-12.
#
# The queue entry asked for the full treatment of Article 32 vs Article 226:
# the five writs, what "and for any other purpose" lets a High Court reach that
# the Supreme Court cannot, why Article 32 is itself a fundamental right while
# 226 is a power given to a court, alternate remedy, territorial jurisdiction,
# and the High Court's discretion to refuse. Distinct from rti-vs-pil-difference
# (blog_seed20.py), which touches the 32/226 split only far enough to explain
# why a PIL usually goes to a High Court first — this article covers ground
# that one deliberately left out, and links to it and to fundamental-rights
# rather than repeating either.
#
# Verified against the Constitution of India itself, Government of India CDN
# copy, "As on 1st May, 2024", 402 pages, read directly with pypdf:
#   https://cdnbbsr.s3waas.gov.in/s380537a945c7aaa788ccfcdf1b99b5d8f/uploads/
#   2024/07/20240716890312078.pdf
#
# Quoted or relied on directly from that text:
#   Art 32(1)  "The right to move the Supreme Court by appropriate proceedings
#              for the enforcement of the rights conferred by this Part is
#              guaranteed."
#   Art 32(2)  Supreme Court "shall have power to issue directions or orders or
#              writs, including writs in the nature of habeas corpus, mandamus,
#              prohibition, quo warranto and certiorari... for the enforcement
#              of any of the rights conferred by this Part" — Part III only, no
#              "any other purpose" clause.
#   Art 32(3)  Parliament may by law empower any other court to exercise, within
#              its local limits, all or any of the powers under clause (2).
#   Art 32(4)  "The right guaranteed by this article shall not be suspended
#              except as otherwise provided for by this Constitution."
#   Art 32 sits in Part III under the Constitution's own sub-heading "Right to
#              Constitutional Remedies" (confirmed from both the contents page
#              and the body text).
#   Art 226(1) "every High Court shall have power... to issue to any person or
#              authority... directions, orders or writs, including writs in the
#              nature of habeas corpus, mandamus, prohibition, quo warranto and
#              certiorari, or any of them, for the enforcement of any of the
#              rights conferred by Part III and for any other purpose."
#   Art 226(2) the same power may be exercised by a High Court "exercising
#              jurisdiction in relation to the territories within which the
#              cause of action, wholly or in part, arises," even where the seat
#              of the government or authority, or the residence of the person,
#              is outside those territories.
#   Art 226 sits in Part VI ("The States"), Chapter V, headed "THE HIGH COURTS
#              IN THE STATES" — confirmed from the body text header, not the
#              contents page alone.
#
# The "Art 32 is a right, Art 226 is a power" distinction is drawn from the
# text itself — clause (1) calls it a right that "is guaranteed" and clause (4)
# calls it "the right guaranteed by this article," while 226(1) says a High
# Court "shall have power" — and from where each article is placed (Part III,
# Fundamental Rights, versus Part VI, the chapter on High Courts).
#
# Deliberately left out, or handled without a case citation: the doctrine that
# a High Court will usually decline a writ petition where an equally efficacious
# alternate remedy exists, and the general principle that writ jurisdiction is
# discretionary rather than a matter of right. Both are settled practice built
# up by the courts over decades, not text found in the Constitution itself, so
# no specific judgment is named here — consistent with how rti-vs-pil-difference
# handled the relaxation of locus standi for a PIL without naming S.P. Gupta or
# Hussainara Khatoon.
#
# Format matches the earlier seeds: (title, slug, category, act, read_time,
# summary, content).

BLOG_ARTICLES_22 = [

    ('Article 32 vs Article 226: Why One Is a Right and the Other Is a Power of the Court',
     'article-32-vs-article-226',
     'acts',
     'Constitution of India',
     '10 min read',
     'Article 32 lets you move the Supreme Court to enforce a fundamental right, and the Constitution calls that a guaranteed right. Article 226 gives a High Court the same writs plus a wider reach, but as a power it can decline to use. Here is what separates them, and which one actually fits your case.',

     "<p><em>Two articles of the Constitution let an Indian court order a government body to act, or to stop acting. People use the names interchangeably. That is the mistake. One is a right the Constitution guarantees you personally. The other is a power it hands to a court, and a court can choose not to use a power.</em></p>"

     "<p><strong>Article 32 guarantees every person the right to move the Supreme Court to enforce a fundamental right, and nothing else. Article 226 gives every High Court the power to issue the same writs for a fundamental right, and for any other legal purpose besides. But it is a power, not a guarantee, and a High Court can decline to use it.</strong></p>"

     "<blockquote>Article 32 covers one thing: a fundamental right under Part III. The Supreme Court cannot turn you away simply because it would rather not hear a fundamental-rights case. Article 226 covers that plus almost anything else a government body does. A High Court can, and often does, send you elsewhere first — to a tribunal, to an appeal, to a lower court. Neither article decides your case. Both only decide which door you may knock on.</blockquote>"

     "<h2>The five writs, in plain terms</h2>"

     "<p>Both articles name the same five writs. Neither invents a sixth. A writ is a court order directed at a person or authority. English law had given each type a name long before the Constitution borrowed them.</p>"

     "<ul>"
     "<li><strong>Habeas corpus</strong> — produce the body. Used when someone is detained and the detention may be illegal; the court orders the person be brought before it and the detention justified.</li>"
     "<li><strong>Mandamus</strong> — we command. Orders a public authority to perform a legal duty it is refusing to perform, such as processing an application it has no ground to sit on.</li>"
     "<li><strong>Prohibition</strong> — stops a lower court or tribunal from proceeding with a matter that is outside its jurisdiction, before it decides anything.</li>"
     "<li><strong>Certiorari</strong> — quashes an order a court or authority has already passed without jurisdiction, or in breach of natural justice.</li>"
     "<li><strong>Quo warranto</strong> — by what authority. Challenges a person's right to hold a public office they may not be legally entitled to.</li>"
     "</ul>"

     "<p>Both Article 32(2) and Article 226(1) list all five by name. The difference between the two articles is not which writs exist. It is who can issue them, for what, and how freely.</p>"

     "<h2>Article 32: a right, not a favour</h2>"

     "<p>Article 32(1) reads: \"The right to move the Supreme Court by appropriate proceedings for the enforcement of the rights conferred by this Part is guaranteed.\" The Constitution is not describing a facility it has set up. It is calling this a right, in the same breath as the rights it protects.</p>"

     "<p>That phrasing is deliberate. Article 32 sits inside Part III, the Fundamental Rights chapter, under the Constitution's own sub-heading \"Right to Constitutional Remedies.\" Article 32(4) reinforces it: \"The right guaranteed by this article shall not be suspended except as otherwise provided for by this Constitution.\" A right that ordinarily cannot be suspended, sitting inside the chapter of rights, carries more weight than a job description handed to a court.</p>"

     "<p>The scope is narrow on purpose. Article 32(2) confines the Supreme Court's writ power to \"the enforcement of any of the rights conferred by this Part\" — Part III, and nothing beyond it. Lose a service dispute, a licence, a contract, and Article 32 will not carry you, however unfair the outcome feels. The Supreme Court has declined petitions on exactly this ground before: the grievance was real, but it fell outside Part III.</p>"

     "<h2>Article 226: a power, and a wider one</h2>"

     "<p>Article 226(1) is built differently: \"every High Court shall have power... to issue... directions, orders or writs... for the enforcement of any of the rights conferred by Part III and for any other purpose.\" It opens with \"shall have power,\" not \"the right... is guaranteed.\" Article 226 sits in Part VI, the chapter on the States, inside Chapter V, headed \"The High Courts in the States.\" It describes what a court can do. It does not promise anything to a person.</p>"

     "<p>The five words \"and for any other purpose\" do the heavy lifting. A High Court can be approached over a statutory right, a service matter, an administrative order, a licence refusal, or a tribunal's decision. None of those is a fundamental right, and the Supreme Court cannot touch any of them under Article 32 alone. That reach is why most writ petitions in India, fundamental-rights cases included, go to a High Court rather than the Supreme Court. Our <a href=\"/article/fundamental-rights\">guide to fundamental rights</a> covers what falls inside Part III, if you need to check whether your grievance qualifies.</p>"

     "<h2>Territorial jurisdiction: which High Court</h2>"

     "<p>Article 226(2) settles a question people get wrong by default: which High Court to approach when the authority you are challenging sits in a different state. The power can be exercised by \"any High Court exercising jurisdiction in relation to the territories within which the cause of action, wholly or in part, arises,\" even where the government or authority's seat, or the person's residence, is outside those territories.</p>"

     "<p>The test is where the cause of action arose, not where the authority's head office sits. A Delhi-headquartered regulator's order affecting a business in Chennai can sometimes be challenged in the Madras High Court, depending on where the relevant facts occurred. Article 226 pulls ahead of Article 32 in one respect here: the Supreme Court is a single court for the whole country, so no equivalent territorial choice arises there.</p>"

     "<h2>Alternate remedy: why a High Court can send you away</h2>"

     "<p>Article 226 sets no condition that you try anything else first. The text does not require it. But over decades of use, courts have built a practice around it. Where a statute already gives an equally effective way to get relief — an appeal, a tribunal, a civil suit — a High Court will usually decline the writ petition. It points you to that forum instead.</p>"

     "<p>This is not a constitutional bar. It is a rule of restraint the courts apply to themselves. They have also carved out their own exceptions: an order passed with no jurisdiction at all, a breach of natural justice, a challenge to the validity of the law itself rather than to a decision under it, or an alternate remedy that is not genuinely adequate. None of this sits in the text of Article 226. It is built case by case, argued both ways depending on the facts. A lawyer's read of your specific situation matters more here than in most of writ practice.</p>"

     "<h2>Discretion to refuse: why neither article guarantees a hearing on the merits</h2>"

     "<p>Article 226 says a High Court \"shall have power.\" Courts read that as permissive, not as a duty to act on demand. Writ jurisdiction under Article 226 is discretionary. A High Court can decline a petition that is delayed without explanation, brought in bad faith, or better suited to another remedy, without ever reaching whether the underlying complaint has merit.</p>"

     "<p>Article 32 works differently, in the Supreme Court's favour, where your case genuinely is a Part III matter. The Constitution frames it as a guaranteed right, not a power, so the Supreme Court has much less room to turn away a properly framed fundamental-rights petition than a High Court has to turn away a general writ petition. That asymmetry is the reason the two articles exist separately rather than one covering both jobs.</p>"

     "<h2>Which one actually fits your case</h2>"

     "<p>Start with what you are complaining about. Say it is squarely a Part III right: your personal liberty, your freedom of speech, discrimination on a ground Article 15 or 16 forbids. Both articles are technically open to you. Article 226 is usually still the practical first stop, because a High Court is closer, faster to approach, and its writ jurisdiction covers the same ground.</p>"

     "<p>Say it is not a Part III right at all: a pension not released, a licence wrongly refused, an authority sitting on a file it has a duty to decide. Article 32 is not available, no matter how strongly you feel wronged. Article 226 is the only writ route, and even that is subject to the alternate-remedy practice above. Check first whether a tribunal or statutory appeal already exists for exactly this complaint.</p>"

     "<p>Readers who reach this page from a right-to-information angle should also see our <a href=\"/article/rti-vs-pil-difference\">RTI vs PIL comparison</a>. It covers the narrower question of when a public-interest writ petition is the right tool, against when a simple information request is enough.</p>"

     "<h2>Common mistakes</h2>"
     "<ul>"
     "<li><strong>Going to the Supreme Court first because it sounds more serious.</strong> Article 32 only covers Part III rights. A matter outside that scope gets sent to a High Court regardless, and the delay is on you.</li>"
     "<li><strong>Assuming Article 226 requires exhausting every other remedy.</strong> There is no such requirement in the text. Courts apply it as a practice, with well-recognised exceptions, not as an absolute rule.</li>"
     "<li><strong>Filing in the wrong High Court by only looking at the authority's head office.</strong> Article 226(2) turns on where the cause of action arose, which is often a different state.</li>"
     "<li><strong>Treating a High Court's refusal to entertain a petition as a ruling on the merits.</strong> A dismissal on the ground of an available alternate remedy or delay says nothing about who was right.</li>"
     "<li><strong>Waiting too long to file.</strong> Neither article sets a limitation period, but courts weigh delay heavily in deciding whether to exercise a discretionary power, and an unexplained gap of months can sink an otherwise sound case.</li>"
     "</ul>"

     "<h2>Frequently asked questions</h2>"

     "<p><strong>Can I file the same writ petition in both the Supreme Court and a High Court?</strong> Not at the same time over the same cause. You choose one forum, though a fundamental-rights matter refused at the High Court stage does not automatically become fit for Article 32 — the Supreme Court decides that independently.</p>"

     "<p><strong>Does Article 226 apply to private companies, or only the government?</strong> It reaches \"any person or authority,\" which courts have read to include some private bodies performing a public function or duty, not only government departments. A purely private commercial dispute is generally outside it.</p>"

     "<p><strong>What does \"for any other purpose\" actually let a High Court do that the Supreme Court cannot?</strong> It extends the High Court's writ power beyond Part III to any legal right or duty — a statutory entitlement, an administrative decision, a tribunal's order — which Article 32 does not reach at all.</p>"

     "<p><strong>Is there a time limit to file a writ petition?</strong> The Constitution sets none. Courts nonetheless expect a petition to be filed without unreasonable delay, and can refuse relief on that ground alone under their discretionary power.</p>"

     "<p><strong>Can Article 32 itself be suspended?</strong> Article 32(4) says the right cannot be suspended except as the Constitution itself otherwise provides, which points to the separate emergency provisions in Part XVIII rather than to any ordinary law.</p>"

     "<p><strong>Why does it matter whether Article 226 is called a \"power\" and Article 32 a \"right\"?</strong> A right the Constitution guarantees is much harder for a court to decline to hear. A power the Constitution confers on a court is one the court can choose whether, and how, to use. That is why the alternate-remedy practice and the discretion to refuse both attach far more visibly to Article 226 than to Article 32.</p>"),

]
