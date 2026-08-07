"""Static site content (templates, judgments, FAQs, resources, comparisons).

Kept here so that both the page views and the site-wide search read from a
single source of truth.
"""

CATEGORY_MAP = {
    'corp': 'Corporate Compliance',
    'labour': 'Labour & Employment',
    'contracts': 'Contracts & Agreements',
    'tax': 'Tax & GST',
    'property': 'Property & Estate',
    'consumer': 'Consumer & RTI',
    'acts': 'Legal Acts Explained',
    'updates': 'Updates & Amendments',
    'sebi': 'SEBI & Securities Law',
    'fema': 'FEMA & Foreign Investment',
    'competition': 'Competition Law',
}

# Topic hub pages — one indexable landing page per category.
#
# The Knowledge Hub lists all 123 guides on a single /blogs page, which leaves
# each topic with no page of its own: nothing targets "corporate compliance
# India" as a phrase, and the 52 guides under that heading share no parent to
# pass authority between them. Each hub below links down to every article in
# its category and every article links back up through its breadcrumb, which is
# the ordinary hub-and-spoke shape search engines expect of a topic library.
#
# `intro` is what makes these worth indexing — a bare list of links reads as a
# thin directory page and gets ignored. Keep it substantive if you add one.
TOPICS = {
    'corp': {
        'slug': 'corporate-compliance',
        'h1': 'Corporate Compliance in India',
        'desc': 'ROC filings, board meetings, share capital, directors and every '
                'Companies Act obligation a private limited company carries.',
        'intro': [
            "Running a company in India means carrying a calendar of obligations that "
            "never really stops. Some are annual — the AOC-4 and MGT-7 filings, the "
            "audit, the AGM. Others are triggered by an event and come with a clock "
            "attached: a charge registered within 30 days, a director change filed in "
            "DIR-12, a resolution reaching the ROC in MGT-14.",
            "Almost none of it is difficult. What catches founders out is that the "
            "penalties are automatic and rarely capped — Rs 100 a day, running from the "
            "day you missed, with no notice and no reminder. A filing forgotten for a "
            "year quietly becomes a bill for tens of thousands of rupees.",
            "These guides walk through each obligation the way it actually arises: what "
            "triggers it, which form it needs, how long you have, and what happens if "
            "you miss the date.",
        ],
    },
    'acts': {
        'slug': 'legal-acts-explained',
        'h1': 'Indian Legal Acts, Explained in Plain English',
        'desc': 'The Constitution, Companies Act, CPC, the new criminal codes and more '
                '— what each statute actually says, without the legalese.',
        'intro': [
            "Indian statutes are written to be precise, not readable. A single section "
            "can run four hundred words, refer to three other sections, and carve out "
            "exceptions in a proviso that reverses everything before it.",
            "Each guide here takes one Act and rebuilds it around the questions people "
            "actually arrive with: what does this law cover, who does it apply to, what "
            "rights does it give me, and what do I do next. The legal accuracy stays; "
            "the density goes.",
        ],
    },
    'contracts': {
        'slug': 'contracts-and-agreements',
        'h1': 'Contracts & Agreements in India',
        'desc': 'How to draft, sign, enforce and safely exit Indian commercial '
                'contracts — NDAs, service agreements, MSAs and termination.',
        'intro': [
            "A contract can look complete — signed, stamped, full of clauses — and still "
            "collapse the moment it is tested. Usually it fails on something ordinary: "
            "no clear scope, a termination clause nobody read, a signature the law does "
            "not recognise, or stamp duty never paid.",
            "These guides cover the agreements Indian businesses sign most often, clause "
            "by clause: what each one must contain, what quietly makes it unenforceable, "
            "and how to end one without becoming the party in breach.",
        ],
    },
    'property': {
        'slug': 'property-and-estate',
        'h1': 'Property, Wills & Estate Law in India',
        'desc': 'Buying, renting, registering and inheriting property in India — title '
                'checks, stamp duty, rent agreements, wills and gift deeds.',
        'intro': [
            "Property is where India's paperwork bites hardest. The difference between "
            "owning an asset and owning a lawsuit is often a document that was never "
            "registered, a title never traced back far enough, or stamp duty paid at the "
            "wrong rate.",
            "These guides cover the transactions that matter most — buying, letting, "
            "gifting and inheriting — including why almost every rent agreement in India "
            "runs for exactly eleven months, and what a will has to contain to survive a "
            "challenge.",
        ],
    },
    'consumer': {
        'slug': 'consumer-rights-and-rti',
        'h1': 'Consumer Rights & RTI in India',
        'desc': 'Complaints, refunds, cheque bounce, online fraud, RERA and the Right '
                'to Information — the remedies you can actually use.',
        'intro': [
            "Consumer law in India is unusually favourable to the individual: the forums "
            "are cheap, you do not need a lawyer, and you can file online from home. Most "
            "people never use any of it, because nobody explains where to start.",
            "These guides give you the actual route — which forum, which form, what "
            "evidence, how long it takes — for defective goods, bounced cheques, online "
            "fraud, builder delays, and information a public authority is refusing to "
            "hand over.",
        ],
    },
    'labour': {
        'slug': 'labour-and-employment',
        'h1': 'Labour & Employment Law in India',
        'desc': 'The new Labour Codes, wages, PF, ESI, gratuity, notice periods and '
                'settlement — for both employers and employees.',
        'intro': [
            "India's four Labour Codes replaced a tangle of older statutes and changed "
            "how wages are defined — which quietly changes provident fund, gratuity and "
            "take-home pay for almost everyone in formal employment.",
            "These guides explain what actually shifted, what an employer now has to do, "
            "and what an employee is owed on the way out: notice period, full-and-final "
            "settlement, gratuity, and how to enforce any of it when it is withheld.",
        ],
    },
    'tax': {
        'slug': 'tax-and-gst',
        'h1': 'Tax & GST in India',
        'desc': 'GST registration and returns, input tax credit, TDS and income tax '
                'for freelancers — thresholds, deadlines and penalties.',
        'intro': [
            "Most tax trouble in India is not evasion. It is a threshold crossed without "
            "noticing, a return filed late, or credit claimed on something that was "
            "blocked all along.",
            "These guides set out the numbers that decide your obligations — turnover "
            "limits, deduction rates, filing dates — and the mistakes that cost the most, "
            "from reversed input tax credit to TDS deposited a day late.",
        ],
    },
    'sebi': {
        'slug': 'sebi-and-securities-law',
        'h1': 'SEBI & Securities Law',
        'desc': 'Insider trading, UPSI, LODR disclosures, IPOs, FPOs and the Takeover '
                'Code — the rules listed companies and their KMPs live under.',
        'intro': [
            "SEBI regulation punishes process failures as hard as bad intent. A board "
            "decision announced tomorrow instead of within thirty minutes, a trading "
            "window left open, a database that was never maintained — each is a breach on "
            "its own, whatever anyone meant to do.",
            "These guides cover what counts as unpublished price sensitive information, "
            "what a listed company must disclose and how fast, the mechanics of raising "
            "capital under the ICDR Regulations, and the penalties when a system is "
            "missing rather than merely misused.",
        ],
    },
    'fema': {
        'slug': 'fema-and-foreign-investment',
        'h1': 'FEMA & Foreign Investment in India',
        'desc': 'FDI routes and sectoral caps, FC-GPR, FC-TRS, FLA and APR deadlines, '
                'and the penalties for getting cross-border filings wrong.',
        'intro': [
            "FEMA runs on one distinction: current account transactions are free unless "
            "restricted, capital account transactions are prohibited unless permitted. "
            "Which side your transaction falls on decides everything that follows.",
            "These guides cover the routes foreign money can take into India, the caps "
            "that apply by sector, and the reporting that follows every transaction — "
            "along with the Late Submission Fee that can still cure a missed filing, and "
            "the point at which it no longer can.",
        ],
    },
    'competition': {
        'slug': 'competition-law',
        'h1': 'Competition Law in India',
        'desc': 'Cartels, anti-competitive agreements, abuse of dominance and CCI '
                'merger control — thresholds, penalties and landmark cases.',
        'intro': [
            "The Competition Act treats some agreements as presumed harmful and others "
            "on their effects, and it reaches conduct that never looks like wrongdoing "
            "from the inside — a pricing conversation between competitors, a distribution "
            "term, a deal closed before approval came through.",
            "These guides cover what the CCI can act against, the thresholds that force "
            "you to notify a transaction, and penalties that now reach ten per cent of "
            "global turnover.",
        ],
    },
    'updates': {
        'slug': 'updates-and-amendments',
        'h1': 'Legal Updates & Amendments',
        'desc': 'New Indian laws and what changed — the DPDP Act, the BNS/BNSS/BSA '
                'criminal codes, and the deadlines attached to each.',
        'intro': [
            "India has replaced or rewritten a remarkable amount of law in a short "
            "period: the criminal codes, the data protection regime, the labour statutes. "
            "Each came with transition deadlines that are easy to miss.",
            "These guides track what actually changed, when each obligation starts to "
            "bite, and what you have to do differently — not the press release version, "
            "the compliance version.",
        ],
    },
}

# Reverse lookup for the /topic/<slug> route.
TOPIC_BY_SLUG = {t['slug']: cat for cat, t in TOPICS.items()}

# ─── Free Legal Document Templates ───────────────────────────────────────────
# Each template: slug, icon, title, desc, [tags], blocks.
# Blocks are (kind, text) - kind ∈ {heading, subheading, para, bullet, spacer}.
# Blanks for the user to fill use underscores (____). These are STARTER drafts -
# review/expand before professional use.
TEMPLATES = [
    {
        'slug': 'leave-license',
        'icon': '📄',
        'title': 'Leave & License Agreement',
        'desc': 'Standard 11-month residential rental agreement compliant with Indian law. Editable Word format.',
        'tags': ['Residential', 'Rental', 'DOCX'],
        'blocks': [
            ('heading', 'LEAVE AND LICENSE AGREEMENT'),
            ('para', 'This Leave and License Agreement is made at ____________ on this ____ day of __________, 20____.'),
            ('subheading', 'BETWEEN'),
            ('para', '____________________, residing at ____________________ (hereinafter the "Licensor"), of the ONE PART;'),
            ('para', 'AND'),
            ('para', '____________________, residing at ____________________ (hereinafter the "Licensee"), of the OTHER PART.'),
            ('subheading', 'NOW THIS AGREEMENT WITNESSETH AS FOLLOWS:'),
            ('para', '1. The Licensor grants the Licensee a license to use and occupy the premises at ____________________ (the "Licensed Premises") for residential purposes only.'),
            ('para', '2. The license is for 11 (eleven) months commencing ____________ and ending ____________, renewable on mutual consent.'),
            ('para', '3. The Licensee shall pay a monthly license fee of Rs. ____________ (Rupees ____________________) on or before the ____ day of each month.'),
            ('para', '4. The Licensee has paid an interest-free refundable security deposit of Rs. ____________, refundable on expiry after deducting dues, if any.'),
            ('para', '5. The Licensee shall not sublet, assign, or part with possession of the Licensed Premises.'),
            ('para', '6. The Licensee shall bear electricity, water, and other utility charges as per actual usage.'),
            ('para', '7. Either party may terminate this Agreement by giving ____ month(s) prior written notice.'),
            ('para', '8. The Licensee shall maintain the premises in good condition and hand over vacant possession on expiry/termination.'),
            ('spacer', ''),
            ('para', 'IN WITNESS WHEREOF the parties have set their hands on the day and year first above written.'),
            ('spacer', ''),
            ('para', '____________________                    ____________________'),
            ('para', 'Licensor                                              Licensee'),
            ('para', 'Witness 1: ____________            Witness 2: ____________'),
        ],
    },
    {
        'slug': 'commercial-lease',
        'icon': '🏢',
        'title': 'Commercial Lease Agreement',
        'desc': 'Commercial property lease with lock-in period, CAM charges, and security deposit clauses.',
        'tags': ['Commercial', 'Property', 'DOCX'],
        'blocks': [
            ('heading', 'COMMERCIAL LEASE AGREEMENT'),
            ('para', 'This Lease Agreement is made at ____________ on this ____ day of __________, 20____.'),
            ('subheading', 'BETWEEN'),
            ('para', '____________________ (the "Lessor") AND ____________________ (the "Lessee").'),
            ('subheading', 'TERMS'),
            ('para', '1. The Lessor leases to the Lessee the commercial premises at ____________________ admeasuring ________ sq. ft. for office/commercial use.'),
            ('para', '2. The lease term is ____ years commencing ____________, with a lock-in period of ____ months.'),
            ('para', '3. Monthly rent: Rs. ____________, with an escalation of ____% every ____ months.'),
            ('para', '4. Security deposit: Rs. ____________ (interest-free, refundable on hand-over).'),
            ('para', '5. Common Area Maintenance (CAM) charges of Rs. ____________ per month shall be borne by the Lessee.'),
            ('para', '6. The Lessee shall pay applicable GST, electricity, and water charges.'),
            ('para', '7. The Lessee shall not sublet or use the premises for any unlawful purpose.'),
            ('para', '8. The Lessee may carry out interior fit-outs with the prior written consent of the Lessor.'),
            ('para', '9. After the lock-in, either party may terminate by giving ____ months’ written notice.'),
            ('para', '10. This Agreement shall be registered; stamp duty and registration charges shall be borne by ____________.'),
            ('spacer', ''),
            ('para', '____________________                    ____________________'),
            ('para', 'Lessor                                                Lessee'),
            ('para', 'Witness 1: ____________            Witness 2: ____________'),
        ],
    },
    {
        'slug': 'nda',
        'icon': '🔒',
        'title': 'Non-Disclosure Agreement (NDA)',
        'desc': 'Mutual NDA for business discussions, partnerships, or employment - Indian law governed.',
        'tags': ['Business', 'Startups', 'DOCX'],
        'blocks': [
            ('heading', 'MUTUAL NON-DISCLOSURE AGREEMENT'),
            ('para', 'This Non-Disclosure Agreement is entered into on ____________ between ____________________ and ____________________ (each a "Party").'),
            ('para', '1. Purpose: The Parties wish to explore ____________________ (the "Purpose") and may share confidential information for this purpose.'),
            ('para', '2. "Confidential Information" means any non-public information disclosed by one Party to the other, in any form, marked or reasonably understood to be confidential.'),
            ('para', '3. The Receiving Party shall use the Confidential Information solely for the Purpose and shall not disclose it to any third party without prior written consent.'),
            ('para', '4. Exclusions: Information that is public, independently developed, or rightfully received from a third party is not Confidential Information.'),
            ('para', '5. The obligations of confidentiality shall survive for ____ years from the date of disclosure.'),
            ('para', '6. Upon written request, the Receiving Party shall promptly return or destroy all Confidential Information.'),
            ('para', '7. This Agreement is governed by the laws of India, and the courts at ____________ shall have exclusive jurisdiction.'),
            ('spacer', ''),
            ('para', '____________________                    ____________________'),
            ('para', 'Party 1                                              Party 2'),
        ],
    },
    {
        'slug': 'consultant-agreement',
        'icon': '💼',
        'title': 'Freelancer / Consultant Agreement',
        'desc': 'Service agreement for independent contractors covering scope, payment, IP, and termination.',
        'tags': ['Freelancers', 'Consulting', 'DOCX'],
        'blocks': [
            ('heading', 'CONSULTANT / FREELANCER AGREEMENT'),
            ('para', 'This Agreement is made on ____________ between ____________________ (the "Client") and ____________________ (the "Consultant").'),
            ('para', '1. Scope of Services: The Consultant shall provide the following services: ____________________.'),
            ('para', '2. Term: This engagement begins on ____________ and continues until ____________ / completion of the services.'),
            ('para', '3. Fees: The Client shall pay Rs. ____________ (per ____________ / lump sum), payable within ____ days of invoice.'),
            ('para', '4. The Consultant is an independent contractor and not an employee; no PF/ESI or employee benefits shall apply.'),
            ('para', '5. Intellectual Property: All work product created under this Agreement shall be the exclusive property of the Client upon full payment.'),
            ('para', '6. Confidentiality: The Consultant shall keep all Client information confidential during and after the engagement.'),
            ('para', '7. Termination: Either party may terminate with ____ days’ written notice; the Client shall pay for services rendered till termination.'),
            ('para', '8. Governing Law: India; jurisdiction at ____________.'),
            ('spacer', ''),
            ('para', '____________________                    ____________________'),
            ('para', 'Client                                                Consultant'),
        ],
    },
    {
        'slug': 'share-purchase-agreement',
        'icon': '🤝',
        'title': 'Share Purchase Agreement (SPA)',
        'desc': 'Agreement for the sale and purchase of company shares - covers consideration, warranties, and closing conditions.',
        'tags': ['Corporate', 'M&A', 'DOCX'],
        'blocks': [
            ('heading', 'SHARE PURCHASE AGREEMENT'),
            ('para', 'This Share Purchase Agreement is made on ____________ between ____________________ (the "Seller") and ____________________ (the "Purchaser"), in respect of the shares of ____________________ Private Limited (the "Company").'),
            ('para', '1. Sale of Shares: The Seller agrees to sell and the Purchaser agrees to purchase ____________ equity shares of Rs. ____ each, constituting ____% of the paid-up share capital of the Company.'),
            ('para', '2. Consideration: The total purchase consideration is Rs. ____________, payable on Closing in the manner agreed.'),
            ('para', '3. Closing: Completion shall take place on ____________, on which date the Seller shall deliver duly executed share transfer forms (SH-4) and the original share certificates.'),
            ('para', '4. Seller’s Warranties: The Seller warrants that the shares are fully paid, free from any encumbrance, and that the Company’s accounts are true and fair.'),
            ('para', '5. Conditions Precedent: Completion is subject to ____________________ (e.g., board approval, satisfactory due diligence, regulatory approvals).'),
            ('para', '6. Indemnity: The Seller shall indemnify the Purchaser against any loss arising from a breach of the warranties.'),
            ('para', '7. Governing Law: India; jurisdiction at ____________.'),
            ('spacer', ''),
            ('para', '____________________                    ____________________'),
            ('para', 'Seller                                                Purchaser'),
        ],
    },
    {
        'slug': 'shareholders-agreement',
        'icon': '📑',
        'title': "Shareholders' Agreement (SHA)",
        'desc': 'Governs the relationship between shareholders - rights, transfer restrictions, board composition, and exit terms.',
        'tags': ['Corporate', 'Governance', 'DOCX'],
        'blocks': [
            ('heading', "SHAREHOLDERS' AGREEMENT"),
            ('para', "This Shareholders' Agreement is made on ____________ among the shareholders of ____________________ Private Limited (the \"Company\") and the Company."),
            ('para', '1. Shareholding: The Parties hold shares in the Company in the proportion set out in Schedule A.'),
            ('para', '2. Board Composition: The Board shall consist of ____ directors; ____________________ shall have the right to nominate ____ director(s).'),
            ('para', '3. Reserved Matters: Certain decisions (e.g., issue of shares, borrowing above Rs. ____________, related-party transactions) shall require the consent of ____% of the shareholders.'),
            ('para', '4. Transfer Restrictions: No shareholder shall transfer shares except in accordance with the Right of First Refusal set out in this Agreement.'),
            ('para', '5. Tag-Along & Drag-Along: ____________________.'),
            ('para', '6. Dividend Policy: ____________________.'),
            ('para', '7. Exit: The Parties shall endeavour to provide an exit by way of IPO / strategic sale by ____________.'),
            ('para', '8. Dispute Resolution: Disputes shall be resolved by arbitration under the Arbitration and Conciliation Act, 1996, seated at ____________.'),
            ('spacer', ''),
            ('para', 'Signed by the Shareholders and the Company:'),
            ('para', '____________________      ____________________      ____________________'),
        ],
    },
    {
        'slug': 'llp-agreement',
        'icon': '⚖️',
        'title': 'LLP Agreement',
        'desc': 'Foundational agreement for a Limited Liability Partnership - capital contribution, profit sharing, and partner duties.',
        'tags': ['LLP', 'Partnership', 'DOCX'],
        'blocks': [
            ('heading', 'LIMITED LIABILITY PARTNERSHIP (LLP) AGREEMENT'),
            ('para', 'This LLP Agreement is made on ____________ among the partners of ____________________ LLP.'),
            ('para', '1. Name & Registered Office: The LLP shall carry on business under the name ____________________ LLP with its registered office at ____________________.'),
            ('para', '2. Business: The LLP shall engage in the business of ____________________.'),
            ('para', '3. Capital Contribution: The total contribution is Rs. ____________, contributed by the partners as per Schedule A.'),
            ('para', '4. Profit Sharing: Profits and losses shall be shared among the partners in the ratio ____________________.'),
            ('para', '5. Designated Partners: ____________________ and ____________________ shall be the Designated Partners responsible for compliance under the LLP Act, 2008.'),
            ('para', '6. Rights & Duties: Each partner shall act in good faith and devote the necessary time and attention to the business of the LLP.'),
            ('para', '7. Banking: The bank account of the LLP shall be operated by ____________________.'),
            ('para', '8. Admission & Retirement: A new partner may be admitted with the consent of all existing partners; a partner may retire by giving ____ days’ notice.'),
            ('para', '9. Dissolution: The LLP may be wound up in accordance with the provisions of the LLP Act, 2008.'),
            ('para', '10. Dispute Resolution: Disputes shall be referred to arbitration seated at ____________.'),
            ('spacer', ''),
            ('para', 'Signed by the Designated Partners:'),
            ('para', '____________________      ____________________'),
        ],
    },
]

# ─── Landmark Judgments ──────────────────────────────────────────────────────
# (year, title, description, area)
JUDGMENTS = [
    {'slug': 'kesavananda-bharati', 'year': '1973', 'area': 'Constitutional Law',
     'title': 'Kesavananda Bharati v. State of Kerala',
     'summary': 'Established the Basic Structure doctrine - Parliament cannot amend the Constitution to destroy its essential features.',
     'brief':
        "<h3>The background</h3>"
        "<p>Swami Kesavananda Bharati, head of a Hindu mutt in Kerala, challenged state land-reform laws that restricted the management of religious property. The case quickly grew into the biggest constitutional question of the era: how far can Parliament go in amending the Constitution? After earlier rulings and a wave of amendments seeking to override fundamental rights, a record 13-judge bench was assembled to settle it.</p>"
        "<h3>The decision</h3>"
        "<p>By a wafer-thin 7-6 majority, the Supreme Court held that Parliament has wide power to amend any part of the Constitution, including fundamental rights - but it <strong>cannot alter or destroy the 'basic structure'</strong> or essential framework of the Constitution. Features such as the supremacy of the Constitution, rule of law, separation of powers, judicial review, federalism, and secularism are beyond the amending power.</p>"
        "<h3>What it changed</h3>"
        "<p>The judgment created the <strong>Basic Structure doctrine</strong>, the single most important check on Parliament's power in India. Courts have since used it to strike down constitutional amendments that threaten the Constitution's core. It permanently shifted the balance between Parliament and the judiciary and remains the bedrock of Indian constitutional law.</p>"},

    {'slug': 'maneka-gandhi', 'year': '1978', 'area': 'Fundamental Rights',
     'title': 'Maneka Gandhi v. Union of India',
     'summary': 'Expanded Article 21 to include the right to live with dignity; any procedure affecting personal liberty must be fair, just, and reasonable.',
     'brief':
        "<h3>The background</h3>"
        "<p>The government impounded journalist Maneka Gandhi's passport 'in the public interest' without giving any reasons. She challenged the action as a violation of her fundamental rights to equality (Article 14), freedom (Article 19), and life and personal liberty (Article 21).</p>"
        "<h3>The decision</h3>"
        "<p>The Court held that the 'procedure established by law' under Article 21 cannot be arbitrary - it must be <strong>fair, just, and reasonable</strong>. It ruled that Articles 14, 19, and 21 are not water-tight compartments but an interconnected 'golden triangle', and that the right to life means far more than mere animal existence - it includes the right to live with dignity.</p>"
        "<h3>What it changed</h3>"
        "<p>This case transformed Article 21 from a narrow guarantee into the engine of almost every modern right in India. By reading <strong>due process</strong> into Indian law, it opened the door to later rights to privacy, livelihood, a clean environment, legal aid, and a speedy trial. Virtually every rights-expanding judgment since traces its logic back to Maneka Gandhi.</p>"},

    {'slug': 'olga-tellis', 'year': '1985', 'area': 'Fundamental Rights',
     'title': 'Olga Tellis v. Bombay Municipal Corporation',
     'summary': 'Held that the right to livelihood is part of the right to life under Article 21 - pavement dwellers cannot be evicted arbitrarily.',
     'brief':
        "<h3>The background</h3>"
        "<p>The Bombay Municipal Corporation moved to evict thousands of pavement and slum dwellers from the city's footpaths without notice. The residents argued that losing their place of shelter would also destroy their livelihood, and therefore their very right to life under Article 21.</p>"
        "<h3>The decision</h3>"
        "<p>The Supreme Court held that the <strong>right to livelihood is an integral part of the right to life</strong> - because no one can live without the means of living. While the Court allowed the removal of encroachments, it ruled that eviction must follow a <strong>fair and reasonable procedure</strong>, with proper notice and a humane approach, not arbitrary force.</p>"
        "<h3>What it changed</h3>"
        "<p>The judgment connected economic survival to the constitutional right to life, shaping decades of jurisprudence on housing, resettlement, and the dignity of the urban poor. It established that the State must act fairly before depriving the most vulnerable of their means of survival.</p>"},

    {'slug': 'mc-mehta-absolute-liability', 'year': '1985', 'area': 'Environmental Law',
     'title': 'M.C. Mehta v. Union of India (Oleum Gas Leak)',
     'summary': 'Introduced the rule of Absolute Liability - enterprises in hazardous activities are absolutely liable for harm, with no exceptions.',
     'brief':
        "<h3>The background</h3>"
        "<p>Soon after the Bhopal gas tragedy, oleum gas leaked from the Shriram factory in Delhi in 1985, harming the public. Public-interest litigation by lawyer M.C. Mehta forced the Court to decide how liable an enterprise should be when a hazardous activity causes harm.</p>"
        "<h3>The decision</h3>"
        "<p>The Court went beyond the old English rule of 'strict liability' (which allowed exceptions) and laid down the principle of <strong>Absolute Liability</strong>: an enterprise engaged in a hazardous or inherently dangerous activity is <strong>absolutely liable</strong> for any harm it causes, with no exceptions whatsoever. It also held that compensation must be proportionate to the size and capacity of the enterprise, so that it acts as a real deterrent.</p>"
        "<h3>What it changed</h3>"
        "<p>India adopted a uniquely strict, home-grown standard of corporate and environmental responsibility. The ruling became the foundation of Indian environmental law, feeding into the polluter-pays principle, later statutes, and the creation of the National Green Tribunal.</p>"},

    {'slug': 'vishaka', 'year': '1997', 'area': 'Labour Law',
     'title': 'Vishaka v. State of Rajasthan',
     'summary': 'Laid down the Vishaka Guidelines against workplace sexual harassment - the foundation of the POSH Act, 2013.',
     'brief':
        "<h3>The background</h3>"
        "<p>After the brutal gang-rape of Bhanwari Devi, a social worker in Rajasthan, and faced with the complete absence of any law on sexual harassment at the workplace, women's groups filed a public-interest petition asking the Court to fill the gap.</p>"
        "<h3>The decision</h3>"
        "<p>Drawing on international conventions such as CEDAW, the Court defined workplace sexual harassment and laid down the binding <strong>Vishaka Guidelines</strong> - placing a duty on every employer to prevent, prohibit, and redress it. The guidelines were to have the force of law until Parliament enacted proper legislation.</p>"
        "<h3>What it changed</h3>"
        "<p>For the first time, workplace sexual harassment was recognised as a violation of the fundamental rights to equality, life, and the freedom to practise any profession. The guidelines governed Indian workplaces for sixteen years and became the direct basis of the <strong>Sexual Harassment of Women at Workplace (POSH) Act, 2013</strong>. It is also a landmark example of the judiciary making interim law to fill a legislative vacuum.</p>"},

    {'slug': 'dk-basu', 'year': '1997', 'area': 'Criminal Law',
     'title': 'D.K. Basu v. State of West Bengal',
     'summary': 'Laid down binding safeguards on arrest and detention to prevent custodial torture and deaths.',
     'brief':
        "<h3>The background</h3>"
        "<p>A letter to the Chief Justice highlighting a series of custodial deaths in West Bengal was treated as a public-interest petition. The Court took up the wider question of how to protect citizens from torture and death in police custody.</p>"
        "<h3>The decision</h3>"
        "<p>The Court issued a set of <strong>binding guidelines for every arrest and detention</strong>: police must wear clear identification, prepare an arrest memo signed by a witness, inform a relative or friend of the arrest, allow the arrestee a medical examination, and record the grounds of arrest. Breach of these safeguards invites departmental action and contempt of court.</p>"
        "<h3>What it changed</h3>"
        "<p>The judgment converted the abstract protections of Articles 21 and 22 into concrete, enforceable rights for anyone who is arrested. The D.K. Basu safeguards were later absorbed into the criminal procedure code and remain the benchmark for a lawful arrest in India.</p>"},

    {'slug': 'nalsa-transgender-rights', 'year': '2014', 'area': 'Fundamental Rights',
     'title': 'NALSA v. Union of India',
     'summary': 'Recognised transgender persons as a third gender with full fundamental rights and directed affirmative action.',
     'brief':
        "<h3>The background</h3>"
        "<p>Transgender persons in India faced deep discrimination and had no legal recognition of their gender identity. The National Legal Services Authority approached the Supreme Court seeking recognition and protection of their rights.</p>"
        "<h3>The decision</h3>"
        "<p>The Court recognised transgender persons as a <strong>'third gender'</strong> and upheld the right of every person to <strong>self-identify their gender</strong> as part of the fundamental rights to equality, non-discrimination, dignity, and personal liberty. It directed governments to treat them as a socially and educationally backward class and to provide reservations and welfare measures.</p>"
        "<h3>What it changed</h3>"
        "<p>This was the first authoritative legal recognition of transgender identity in India. It expanded the meaning of equality and dignity under the Constitution and laid the groundwork for later transgender-rights legislation and welfare schemes.</p>"},

    {'slug': 'shreya-singhal', 'year': '2015', 'area': 'Digital Rights',
     'title': 'Shreya Singhal v. Union of India',
     'summary': 'Struck down Section 66A of the IT Act as unconstitutional - a landmark victory for online free speech.',
     'brief':
        "<h3>The background</h3>"
        "<p>Section 66A of the Information Technology Act criminalised sending 'offensive' or 'menacing' messages online in vague, sweeping terms. People were arrested for ordinary social-media posts, prompting a challenge that the provision violated the freedom of speech and expression.</p>"
        "<h3>The decision</h3>"
        "<p>The Court <strong>struck down Section 66A as unconstitutional</strong>, holding it vague and overbroad and a chilling restriction on free speech under Article 19(1)(a) that could not be saved by the reasonable restrictions in Article 19(2). It also clarified the limits of intermediary liability, reading down the related rules.</p>"
        "<h3>What it changed</h3>"
        "<p>The judgment is a cornerstone of digital free speech in India. It established that laws restricting speech must be precise and narrow, and that vague, open-ended speech offences will not survive constitutional scrutiny - protecting millions of internet users from arbitrary prosecution.</p>"},

    {'slug': 'puttaswamy-right-to-privacy', 'year': '2017', 'area': 'Privacy & Data',
     'title': 'Justice K.S. Puttaswamy v. Union of India',
     'summary': "Declared the Right to Privacy a fundamental right under Article 21 - the foundation of India's data protection law.",
     'brief':
        "<h3>The background</h3>"
        "<p>Challenges to the Aadhaar programme raised a foundational question: is privacy a fundamental right? Older judgments had suggested it was not, so a nine-judge bench was constituted to settle the issue once and for all.</p>"
        "<h3>The decision</h3>"
        "<p>The Court <strong>unanimously held that the Right to Privacy is a fundamental right</strong>, intrinsic to the right to life and personal liberty under Article 21 and to the freedoms guaranteed in Part III of the Constitution. It expressly overruled the earlier decisions that had denied privacy this status.</p>"
        "<h3>What it changed</h3>"
        "<p>Puttaswamy is one of the most consequential modern judgments. It became the foundation for India's <strong>Digital Personal Data Protection Act, 2023</strong>, shaped limits on state surveillance and the use of Aadhaar, and underpinned later rulings on individual autonomy and dignity.</p>"},
]

# ─── External Resources ──────────────────────────────────────────────────────
# (icon, title, description, type, url)
RESOURCES = [
    ('🏛', 'MCA21 Portal',
     'Official Ministry of Corporate Affairs portal for company filings, DIN, and ROC records.',
     'Government Portal', 'https://www.mca.gov.in/'),
    ('📋', 'e-Jagriti - Consumer Cases',
     'The new unified portal for filing and tracking consumer complaints with District, State, and National Commissions.',
     'Government Portal', 'https://e-jagriti.gov.in/'),
    ('🔍', 'RTI Online Portal',
     'File RTI applications to Central Government departments online at rtionline.gov.in.',
     'Government Portal', 'https://rtionline.gov.in/'),
    ('⚖', 'India Code - Laws Database',
     'Official repository of all Central Acts and Regulations of India at indiacode.nic.in.',
     'Legal Database', 'https://www.indiacode.nic.in/'),
]

# ─── FAQs ────────────────────────────────────────────────────────────────────
# (question, answer)
FAQS = [
    ('What is ROC compliance and is it mandatory for my company?',
     'ROC (Registrar of Companies) compliance refers to mandatory filings that every company registered under the Companies Act, 2013 must make with the Ministry of Corporate Affairs. Yes, it is mandatory. Non-compliance attracts penalties and can lead to striking off of the company.'),
    ('What is the difference between a Private Limited Company and an LLP?',
     'A Private Limited Company has shareholders and directors, is governed by the Companies Act 2013, and has stricter compliance requirements. An LLP (Limited Liability Partnership) has partners, is governed by the LLP Act 2008, and has lighter compliance obligations. Both offer limited liability protection.'),
    ('What annual filings does a Private Limited Company need to do?',
     'A Private Limited Company must file Form AOC-4 (financial statements) and Form MGT-7 (annual return) with the ROC every year. It must also hold an Annual General Meeting (AGM) within 6 months of the financial year end.'),
    ('What are the compliance requirements for an LLP in India?',
     'An LLP must file Form 11 (Annual Return) by 30th May and Form 8 (Statement of Account & Solvency) by 30th October every year with the MCA. LLPs with turnover above Rs 40 lakh or contribution above Rs 25 lakh must also get their accounts audited.'),
    ('How do I file a consumer complaint online in India?',
     'You can file a consumer complaint online through the e-Jagriti portal at e-jagriti.gov.in, which has replaced the earlier eDaakhil system. For claims up to Rs 50 lakh, file at the District Consumer Disputes Redressal Commission. No lawyer is mandatory for consumer cases.'),
    ('Is content on Law Minded legal advice?',
     'No. All content on Law Minded is for legal awareness and educational purposes only. It does not constitute legal advice. Always consult a qualified legal professional for advice specific to your situation.'),
]

# ─── Act Comparisons (also used client-side; kept here for search) ────────────
COMPARISONS = {
    'pvt-llp': 'Private Limited Company vs LLP - governing law, ownership, compliance, audit, foreign investment',
    'lease-ll': 'Lease Agreement vs Leave & License Agreement - legal nature, stamp duty, registration, eviction',
    'partner-llp': 'Partnership Firm vs LLP - liability, registration, legal entity, compliance',
    'forum-court': 'Consumer Forum vs Civil Court - jurisdiction, cost, speed, relief, online filing',
    'rti-pil': 'RTI vs PIL - purpose, where filed, cost, timeline, governing law',
}


def search_all(query, articles):
    """Search across articles, templates, judgments, resources, FAQs, comparisons.

    `articles` is a list of sqlite Row objects from the DB.
    Returns a list of result dicts: {type, title, snippet, url_kind, url_arg}.
    """
    q = query.lower().strip()
    results = []
    if not q:
        return results

    # Articles
    for art in articles:
        haystack = ' '.join(str(art[k] or '') for k in
                            ('title', 'summary', 'content', 'act')).lower()
        if q in haystack:
            results.append({
                'type': 'Article',
                'title': art['title'],
                'snippet': art['summary'],
                'url_kind': 'article',
                'url_arg': art['slug'],
            })

    # (Templates & Resolutions are now DB-managed and searched in the /search route.)

    # Judgments (each entry is a dict: slug, year, area, title, summary, brief)
    for j in JUDGMENTS:
        haystack = ' '.join((j['title'], j['summary'], j['area'], j['year'])).lower()
        if q in haystack:
            results.append({
                'type': 'Judgment',
                'title': f"{j['title']} ({j['year']})",
                'snippet': j['summary'],
                'url_kind': 'judgment',
                'url_arg': j['slug'],
            })

    # Resources
    for icon, title, desc, rtype, url in RESOURCES:
        if q in (title + ' ' + desc + ' ' + rtype).lower():
            results.append({
                'type': 'Resource',
                'title': f'{icon} {title}',
                'snippet': desc,
                'url_kind': 'external',
                'url_arg': url,
            })

    # FAQs
    for question, answer in FAQS:
        if q in (question + ' ' + answer).lower():
            results.append({
                'type': 'FAQ',
                'title': question,
                'snippet': answer,
                'url_kind': 'page',
                'url_arg': 'faq',
            })

    # Comparisons
    for key, text in COMPARISONS.items():
        if q in text.lower():
            results.append({
                'type': 'Comparison',
                'title': text.split('-')[0].strip(),
                'snippet': text,
                'url_kind': 'page',
                'url_arg': 'compare',
            })

    return results


# ─── Resolution Libraries (Board & Special) ──────────────────────────────────
# Each resolution is a list of blocks: (kind, text)
#   kind ∈ {'heading','subheading','para','bullet','spacer'}
# Blanks for the user to fill use underscores (____).
# NOTE: seeded with sample formats - the full sets are added as the owner supplies them.

BOARD_RESOLUTIONS = [
    {
        'slug': 'opening-bank-account',
        'title': 'Opening a Bank Account',
        'desc': 'Authorising the opening and operation of a company current account with a bank.',
        'blocks': [
            ('heading', 'CERTIFIED TRUE COPY OF THE RESOLUTION PASSED AT THE MEETING OF THE BOARD OF DIRECTORS OF ____________________ PRIVATE LIMITED HELD ON ____________ AT ____________________'),
            ('subheading', 'Opening of Bank Account'),
            ('para', '"RESOLVED THAT a Current Account be opened in the name of the Company, ____________________ Private Limited, with ____________________ Bank, ____________ Branch."'),
            ('para', '"RESOLVED FURTHER THAT the said account be operated by Mr./Ms. ____________________, Director of the Company (singly / jointly), and the Bank is hereby authorised to honour all cheques, drafts, and instructions drawn on the said account on behalf of the Company."'),
            ('para', '"RESOLVED FURTHER THAT a certified true copy of this resolution be furnished to the Bank and shall remain in force until duly revoked by the Board."'),
            ('spacer', ''),
            ('para', 'For ____________________ Private Limited'),
            ('spacer', ''),
            ('para', '____________________'),
            ('para', 'Director'),
            ('para', 'DIN: ____________'),
        ],
    },
    {
        'slug': 'authorising-gst-registration',
        'title': 'Authorising for GST Registration',
        'desc': 'Authorising a director to apply for and obtain GST registration for the company.',
        'blocks': [
            ('heading', 'CERTIFIED TRUE COPY OF THE RESOLUTION PASSED AT THE MEETING OF THE BOARD OF DIRECTORS OF ____________________ PRIVATE LIMITED HELD ON ____________ AT ____________________'),
            ('subheading', 'Authorisation for GST Registration'),
            ('para', '"RESOLVED THAT the Company do apply for registration under the Goods and Services Tax (GST) Act, 2017, with the appropriate authorities."'),
            ('para', '"RESOLVED FURTHER THAT Mr./Ms. ____________________, Director of the Company (DIN: ____________), be and is hereby authorised to sign and submit the application, file documents, appear before the authorities, and act as the Authorised Signatory of the Company for all GST-related matters."'),
            ('para', '"RESOLVED FURTHER THAT a certified true copy of this resolution be submitted to the GST authorities as may be required."'),
            ('spacer', ''),
            ('para', 'For ____________________ Private Limited'),
            ('spacer', ''),
            ('para', '____________________'),
            ('para', 'Director'),
            ('para', 'DIN: ____________'),
        ],
    },
]

SPECIAL_RESOLUTIONS = [
    {
        'slug': 'change-registered-office',
        'title': 'Change of Registered Office (Outside City)',
        'desc': 'Special resolution for shifting the registered office of the company.',
        'blocks': [
            ('heading', 'SPECIAL RESOLUTION PASSED AT THE EXTRAORDINARY GENERAL MEETING OF THE MEMBERS OF ____________________ PRIVATE LIMITED HELD ON ____________ AT ____________________'),
            ('subheading', 'Change of Registered Office'),
            ('para', '"RESOLVED AS A SPECIAL RESOLUTION THAT, pursuant to Section 12 and other applicable provisions of the Companies Act, 2013, the registered office of the Company be shifted from ____________________ to ____________________ with effect from ____________."'),
            ('para', '"RESOLVED FURTHER THAT the Board of Directors be and is hereby authorised to take all necessary steps and file the requisite forms with the Registrar of Companies to give effect to this resolution."'),
            ('spacer', ''),
            ('para', 'For ____________________ Private Limited'),
            ('spacer', ''),
            ('para', '____________________'),
            ('para', 'Director'),
            ('para', 'DIN: ____________'),
        ],
    },
    {
        'slug': 'increase-authorised-capital',
        'title': 'Increase in Authorised Share Capital',
        'desc': 'Special resolution to increase the authorised share capital of the company.',
        'blocks': [
            ('heading', 'SPECIAL RESOLUTION PASSED AT THE EXTRAORDINARY GENERAL MEETING OF THE MEMBERS OF ____________________ PRIVATE LIMITED HELD ON ____________ AT ____________________'),
            ('subheading', 'Increase in Authorised Share Capital'),
            ('para', '"RESOLVED AS A SPECIAL RESOLUTION THAT, pursuant to the applicable provisions of the Companies Act, 2013, the authorised share capital of the Company be increased from Rs. ____________ to Rs. ____________ by the creation of ____________ additional equity shares of Rs. ____ each."'),
            ('para', '"RESOLVED FURTHER THAT the Memorandum of Association of the Company be altered accordingly and the Board be authorised to file the necessary forms with the Registrar of Companies."'),
            ('spacer', ''),
            ('para', 'For ____________________ Private Limited'),
            ('spacer', ''),
            ('para', '____________________'),
            ('para', 'Director'),
            ('para', 'DIN: ____________'),
        ],
    },
]


PARTNER_RESOLUTIONS = [
    {
        'slug': 'llp-opening-bank-account',
        'title': 'Opening a Bank Account (LLP)',
        'desc': 'Resolution of the partners authorising the opening and operation of an LLP current account.',
        'blocks': [
            ('heading', 'CERTIFIED TRUE COPY OF THE RESOLUTION PASSED AT THE MEETING OF THE PARTNERS OF ____________________ LLP (LLPIN: ____________) HELD ON ____________ AT ____________________'),
            ('subheading', 'Opening of Bank Account'),
            ('para', '"RESOLVED THAT a Current Account be opened in the name of the LLP, ____________________ LLP, with ____________________ Bank, ____________ Branch."'),
            ('para', '"RESOLVED FURTHER THAT the said account be operated by Mr./Ms. ____________________, Designated Partner (singly / jointly with ____________________), and the Bank is hereby authorised to honour all cheques, drafts, and instructions drawn on the said account on behalf of the LLP."'),
            ('para', '"RESOLVED FURTHER THAT a certified true copy of this resolution, signed by the Designated Partners, be furnished to the Bank and shall remain in force until duly revoked by the Partners."'),
            ('spacer', ''),
            ('para', 'For ____________________ LLP'),
            ('spacer', ''),
            ('para', '____________________'),
            ('para', 'Designated Partner'),
            ('para', 'DPIN: ____________'),
        ],
    },
    {
        'slug': 'llp-authorising-gst-registration',
        'title': 'Authorising for GST Registration (LLP)',
        'desc': 'Resolution authorising a designated partner to apply for and obtain GST registration for the LLP.',
        'blocks': [
            ('heading', 'CERTIFIED TRUE COPY OF THE RESOLUTION PASSED AT THE MEETING OF THE PARTNERS OF ____________________ LLP (LLPIN: ____________) HELD ON ____________ AT ____________________'),
            ('subheading', 'Authorisation for GST Registration'),
            ('para', '"RESOLVED THAT the LLP do apply for registration under the Goods and Services Tax (GST) Act, 2017, with the appropriate authorities."'),
            ('para', '"RESOLVED FURTHER THAT Mr./Ms. ____________________, Designated Partner of the LLP (DPIN: ____________), be and is hereby authorised to sign and submit the application, file documents, appear before the authorities, and act as the Authorised Signatory of the LLP for all GST-related matters."'),
            ('para', '"RESOLVED FURTHER THAT a certified true copy of this resolution be submitted to the GST authorities as may be required."'),
            ('spacer', ''),
            ('para', 'For ____________________ LLP'),
            ('spacer', ''),
            ('para', '____________________'),
            ('para', 'Designated Partner'),
            ('para', 'DPIN: ____________'),
        ],
    },
    {
        'slug': 'llp-admission-designated-partner',
        'title': 'Admission of a Designated Partner',
        'desc': 'Resolution for admitting a new partner and designating them as a Designated Partner of the LLP.',
        'blocks': [
            ('heading', 'CERTIFIED TRUE COPY OF THE RESOLUTION PASSED AT THE MEETING OF THE PARTNERS OF ____________________ LLP (LLPIN: ____________) HELD ON ____________ AT ____________________'),
            ('subheading', 'Admission and Appointment of Designated Partner'),
            ('para', '"RESOLVED THAT, pursuant to the LLP Agreement and Section 7 of the Limited Liability Partnership Act, 2008, Mr./Ms. ____________________ (DPIN: ____________) be and is hereby admitted as a Partner and appointed as a Designated Partner of the LLP with effect from ____________, with an agreed contribution of Rs. ____________."'),
            ('para', '"RESOLVED FURTHER THAT the LLP Agreement be amended accordingly and that any Designated Partner be and is hereby authorised to file Form 3 and Form 4 with the Registrar of Companies within the prescribed time."'),
            ('spacer', ''),
            ('para', 'For ____________________ LLP'),
            ('spacer', ''),
            ('para', '____________________'),
            ('para', 'Designated Partner'),
            ('para', 'DPIN: ____________'),
        ],
    },
]


def render_resolution_html(blocks):
    """Render resolution blocks to safe HTML for the preview modal."""
    from markupsafe import escape
    out, bullets = [], []

    def flush_bullets():
        if bullets:
            out.append('<ul>' + ''.join(f'<li>{escape(b)}</li>' for b in bullets) + '</ul>')
            bullets.clear()

    for kind, text in blocks:
        if kind == 'bullet':
            bullets.append(text)
            continue
        flush_bullets()
        if kind == 'heading':
            out.append(f'<h3>{escape(text)}</h3>')
        elif kind == 'subheading':
            out.append(f'<h4>{escape(text)}</h4>')
        elif kind == 'spacer':
            out.append('<div class="res-spacer"></div>')
        else:
            out.append(f'<p>{escape(text)}</p>')
    flush_bullets()
    return ''.join(out)


# ─── Document body <-> blocks (markdown-lite used by the admin document editor) ──
# Format:  "# heading"  "## subheading"  "- bullet"  blank line = spacer  else paragraph.

def blocks_to_body(blocks):
    lines = []
    for kind, text in blocks:
        if kind == 'heading':
            lines.append('# ' + text)
        elif kind == 'subheading':
            lines.append('## ' + text)
        elif kind == 'bullet':
            lines.append('- ' + text)
        elif kind == 'spacer':
            lines.append('')
        else:
            lines.append(text)
    return '\n'.join(lines)


def parse_doc_body(body):
    blocks = []
    for raw in (body or '').split('\n'):
        s = raw.strip()
        if s == '':
            blocks.append(('spacer', ''))
        elif s.startswith('## '):
            blocks.append(('subheading', s[3:].strip()))
        elif s.startswith('# '):
            blocks.append(('heading', s[2:].strip()))
        elif s.startswith('- '):
            blocks.append(('bullet', s[2:].strip()))
        else:
            blocks.append(('para', s))
    return blocks
