# Owner-requested comparison article, 4 September 2026.
#
# The owner asked for "more comparisons like pil vs rti — people are getting it
# on Google, we are 1st in it". Checked that against the Search Console export
# at docs/gsc-performance-2026-08-26.xlsx rather than taking it on trust, and it
# holds up better than the phrasing suggested:
#
#   difference between rti and pil   15 impressions   avg position 4.6   0 clicks
#   pil vs rti                        5 impressions   avg position 2.6   0 clicks
#   difference between pil and rti    1 impression    avg position 4.0   0 clicks
#
# 21 impressions is the biggest single query cluster on the site — the next is
# "demat requirement section 8 company" at 12 — and it already ranks on page one.
# It earns zero clicks because THERE IS NO ARTICLE. Google is ranking
# right-to-information-act-guide, which never mentions PIL, so the snippet does
# not answer the question being asked. This article is the missing page.
#
# Built from what the site already has, per the owner's instruction: the RTI half
# leans on /article/right-to-information-act-guide and the PIL half on
# /article/fundamental-rights, both of which are linked rather than repeated.
#
# Every provision verified against primary sources:
#
#  - Right to Information Act, 2005, from the Government of NCT of Delhi mirror
#    of the central Act (colart.delhi.gov.in/sites/default/files/2024-05/
#    rti_act_2005.pdf), fetched with curl and a browser user-agent because
#    indiacode.nic.in returns 403/404 to this box, the same gov.in behaviour
#    recorded for the PMEGP article. Quoted directly from that text:
#      s.3    "all citizens shall have the right to information"
#      s.6(2) an applicant "shall not be required to give any reason for
#             requesting the information or any other personal details except
#             those that may be necessary for contacting him"
#      s.7(1) reply "within thirty days of the receipt of the request"; proviso,
#             where the information "concerns the life or liberty of a person,
#             the same shall be provided within forty-eight hours"
#      s.7(5) no fee for a person below the poverty line
#      s.8(1) the exemptions, opening "there shall be no obligation to give any
#             citizen" the listed categories
#      s.19(1) first appeal within thirty days, to an officer senior in rank
#      s.19(3) second appeal within ninety days, to the CIC or the SIC
#      s.20   penalty of "two hundred and fifty rupees each day", total "not
#             exceed twenty-five thousand rupees"
#
#  - The Constitution of India, from the Government of India CDN copy used by
#    legislative.gov.in (cdnbbsr.s3waas.gov.in/...20240716890312078.pdf),
#    402 pages, read directly:
#      Art 32(1) "The right to move the Supreme Court by appropriate proceedings
#                for the enforcement of the rights conferred by this Part is
#                guaranteed."
#      Art 32(2) writs "for the enforcement of any of the rights conferred by
#                this Part" — Part III only
#      Art 226(1) every High Court may issue writs "for the enforcement of any
#                of the rights conferred by Part III and for any other purpose"
#
# Deliberately left out: the Rs 10 RTI application fee. It is set by the Central
# RTI Rules, not the Act, it differs state to state, and no primary text for it
# was read during this session. The article says "a small prescribed fee" and
# names the one fee rule that IS in the Act, s.7(5).
#
# Also left out: any case name for the relaxation of locus standi in PIL. The
# principle is described from what Art 32 and Art 226 actually say plus what the
# site's own fundamental-rights article already states; naming S.P. Gupta or
# Hussainara Khatoon would mean citing judgments not read in this session.
#
# Format matches the earlier seeds: (title, slug, category, act, read_time,
# summary, content).

BLOG_ARTICLES_19 = [

    ('RTI vs PIL: One Gets You Information, the Other Gets a Court to Act',
     'rti-vs-pil-difference',
     'acts',
     'Right to Information Act, 2005',
     '9 min read',
     "An RTI is a letter to a government office asking for information, and it costs a few rupees. A PIL is a case in a High Court or the Supreme Court asking for something to be fixed. People reach for the wrong one all the time. Here is which is which, and why the RTI almost always comes first.",

     "<p><em>Both are ways an ordinary person can push back against a government that is not doing its job. They work so differently that using the wrong one wastes months. One is a form you post. The other is a case you file.</em></p>"

     "<p><strong>An RTI application asks a public authority to hand over information it already holds. A PIL asks a constitutional court to order someone to act. The first is a right every citizen has under a 2005 statute; the second is a court proceeding, and courts decide whether to hear it.</strong></p>"

     "<blockquote>Use an RTI when your question starts with what, when, how much or why — what did the road cost, when was the tender approved, how much was sanctioned. Use a PIL when you already know what is wrong, it affects more than just you, and you need a court to order it stopped or fixed. In practice the RTI usually comes first, because the reply is the evidence a court will want to see.</blockquote>"

     "<h2>What an RTI actually is</h2>"

     "<p>The Right to Information Act, 2005 says in Section 3 that all citizens shall have the right to information. That is the whole idea. Information held by a government body belongs to the public, and you can ask for a copy of it.</p>"

     "<p>You write an application to the Public Information Officer of the department that holds the record, pay a small prescribed fee, and wait. Section 7(5) says a person below the poverty line pays no fee at all.</p>"

     "<p>Section 6(2) contains the part people find hardest to believe. You do not have to explain why you want the information. The Act says an applicant shall not be required to give any reason for requesting it, or any personal details beyond what is needed to contact you. An officer who asks why you want to know is asking something the law does not entitle him to ask.</p>"

     "<p>Section 7(1) gives the officer thirty days to reply. Where the information concerns the life or liberty of a person, that drops to forty-eight hours.</p>"

     "<p>If the answer does not come, Section 19 sets out the ladder. A first appeal goes within thirty days to an officer senior in rank inside the same department. A second appeal goes within ninety days to the Central Information Commission or the State Information Commission. The Commission can impose a penalty under Section 20 of two hundred and fifty rupees for each day of delay, capped at twenty-five thousand rupees, payable by the officer personally.</p>"

     "<p>Not everything can be asked for. Section 8(1) lists what a public authority has no obligation to disclose. The list opens with anything that would prejudicially affect the sovereignty and integrity of India, and runs on through cabinet papers, commercial confidence, and personal information unconnected to any public activity. Our <a href=\"/article/right-to-information-act-guide\">full guide to the RTI Act</a> works through the exemptions and the appeal ladder in detail.</p>"

     "<h2>What a PIL actually is</h2>"

     "<p>A Public Interest Litigation is not a separate law. There is no PIL Act, no PIL form and no PIL fee schedule. It is an ordinary constitutional case, brought by someone who is not personally the victim.</p>"

     "<p>Two provisions carry it. Article 32 lets you move the Supreme Court for the enforcement of a fundamental right, and the Constitution calls that right itself guaranteed. Article 226 lets a High Court issue the same writs for the enforcement of a Part III right <em>and for any other purpose</em>.</p>"

     "<p>Those last five words do a lot of work. A High Court can be approached over a statutory right, a licence, a service matter or an administrative decision, none of which is a fundamental right. The Supreme Court under Article 32 cannot: it is limited to Part III. That is why most PILs are filed in a High Court, and why a matter refused there is not automatically fit for the Supreme Court.</p>"

     "<p>The thing that makes a case a PIL is who is allowed to bring it. Ordinarily a court hears you only about your own injury. In public interest matters, Indian courts relaxed that rule, so a person or organisation with no personal stake can raise the grievance of people who cannot come to court themselves. Our guide to <a href=\"/article/fundamental-rights\">fundamental rights</a> covers the writs a court can issue and what each one does.</p>"

     "<p>A court is not obliged to take it. A High Court's writ jurisdiction is discretionary. A PIL that looks like a private dispute in public clothing, or one filed to settle a score, gets dismissed, sometimes with costs.</p>"

     "<h2>Which one you need</h2>"

     "<p>The test is what you are actually asking for.</p>"

     "<p>A road in your locality was rebuilt last year and is broken again. You want to know what it cost and which contractor did it. That is an RTI, and the answer is a document that already exists.</p>"

     "<p>The same road is now a danger and the municipality has ignored every complaint for two years. You want it repaired. No document answers that. It is a High Court matter under Article 226, and the RTI reply about the contract becomes your evidence.</p>"

     "<p>A government school is charging fees it is not supposed to charge. Ask for the fee circular through an RTI first. If the circular says one thing and the school does another, you are no longer arguing about facts.</p>"

     "<p>Your own pension has not been paid. That is a personal grievance, not a public interest one. A writ petition in your own name under Article 226 is available; calling it a PIL does not help and may get it dismissed.</p>"

     "<h2>Why the RTI comes first</h2>"

     "<p>Courts decide on material. A petition saying a public authority has failed is an assertion. The same petition attached to that authority's own written reply is proof.</p>"

     "<p>An RTI reply is a document from the department itself. Departments cannot easily disown it. Even a refusal is useful, because a refusal has to cite a clause of Section 8, and a bad refusal is itself something to point at.</p>"

     "<p>There is also the possibility that the RTI ends the matter. A file that has been sitting on a desk for a year sometimes moves once somebody has to put in writing why it has not.</p>"

     "<h2>What each one costs you</h2>"

     "<p>An RTI costs a small fee, an envelope and thirty days. You can file it yourself. No lawyer is involved at any stage, including both appeals.</p>"

     "<p>A PIL is a court case. Court fees are modest, but drafting a writ petition is not something most people do unaided, and a matter can run for years. Against that, the court can order things no department will do voluntarily.</p>"

     "<p>One is a tool you can pick up this afternoon. The other is a commitment.</p>"

     "<h2>Common mistakes</h2>"

     "<ul>"
     "<li><strong>Explaining why you want the information.</strong> Section 6(2) says you do not have to, and volunteering a reason invites an officer to argue with it.</li>"
     "<li><strong>Asking an RTI to give an opinion.</strong> The Act covers information a public authority holds. It is not a channel for asking an officer whether something was fair, or what he thinks should be done.</li>"
     "<li><strong>Filing a PIL over a personal dispute.</strong> A private grievance dressed as public interest is the most common reason these get dismissed. If the person harmed is you, file in your own name.</li>"
     "<li><strong>Going to the Supreme Court first.</strong> Article 32 covers fundamental rights only. Article 226 covers those and any other purpose, which makes the High Court the wider door, not the lesser one.</li>"
     "<li><strong>Letting the appeal window close.</strong> Thirty days for the first appeal and ninety for the second are in Section 19. A stale RTI usually has to be started again from the beginning.</li>"
     "<li><strong>Treating silence as a dead end.</strong> No reply within thirty days is itself a deemed refusal you can appeal, and it is what Section 20's daily penalty is built to punish.</li>"
     "</ul>"

     "<h2>Frequently asked questions</h2>"

     "<p><strong>What is the main difference between RTI and PIL?</strong> An RTI gets you information a public authority already holds, under the Right to Information Act, 2005. A PIL asks a High Court or the Supreme Court to order that something be done. One produces a document; the other produces a direction.</p>"

     "<p><strong>Can I file a PIL without a lawyer?</strong> There is no rule requiring one, and courts have accepted petitions written by ordinary people and even letters. In practice a writ petition has a form and a set of grounds, and a badly drafted one gets dismissed on its shape rather than its substance.</p>"

     "<p><strong>Do I have to file an RTI before a PIL?</strong> No, nothing requires it. It is usually worth doing anyway, because the reply is evidence from the department itself, and evidence is what a court decides on.</p>"

     "<p><strong>Who can file an RTI application?</strong> Any citizen. Section 3 of the Act puts the right in exactly those terms, and Section 6(2) says you need not give any reason for asking.</p>"

     "<p><strong>How long does a public authority have to reply to an RTI?</strong> Thirty days under Section 7(1). Forty-eight hours where the information concerns the life or liberty of a person.</p>"

     "<p><strong>What happens if the officer simply does not answer?</strong> Appeal. A first appeal goes within thirty days to an officer senior to him. A second appeal goes within ninety days to the Information Commission, which can fine him two hundred and fifty rupees a day, up to twenty-five thousand, under Section 20.</p>"

     "<p><strong>Should a PIL go to the High Court or the Supreme Court?</strong> Article 32 lets the Supreme Court act only on fundamental rights. Article 226 lets a High Court act on those and, in its own words, for any other purpose. The High Court is therefore the wider jurisdiction and the usual starting point.</p>"

     "<p><strong>Can I use an RTI reply as evidence in a PIL?</strong> Yes, and it is one of the main reasons to file one first. A reply is the public authority's own written statement about its own records.</p>"

     "<p><strong>Is there a PIL Act in India?</strong> No. A PIL is an ordinary writ petition under Article 32 or Article 226, brought by someone who is not personally the injured party. The name describes who is filing and why, not a separate law.</p>"),

]
