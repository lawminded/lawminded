"""Law Minded's plain-English summary of each section of the Companies Act, 2013.

These are not decoration. Section 52(1)(q)(ii) of the Copyright Act, 1957 permits
reproducing an Act of a Legislature only where it is published *together with
commentary or other original matter*. The summary is that commentary, which is
why `act.py` refuses to render a section that does not have one.

House rules for writing them, from the owner:

  * Plain English a fifteen-year-old can follow. Not legal language.
  * Short sections get 2 to 4 lines. Long ones get 5 to 7.
  * Nothing goes past 10 lines, however long the section is.
  * Say what the section is about and what it covers — not a paraphrase of
    every sub-clause.

Say what the law does, never what a reader should do about it: this is a
summary, not advice. Where a section is omitted or repealed, say so and say
what replaced it, because that is the question someone landing on it has.

Keyed by section number exactly as it appears in the Act, including letter
suffixes ("3A", "378ZA").
"""

SUMMARIES = {

    # ── Chapter I — Preliminary ──────────────────────────────────────────────
    '1': (
        "This is the section that switches the Act on. It gives the law its name, "
        "says it applies to the whole of India, and explains that different parts "
        "of it could be brought into force on different dates rather than all at "
        "once.\n\n"
        "It also sets out who the Act governs: companies registered under this "
        "Act or any older company law, plus insurance companies, banking "
        "companies, electricity companies and a few other special types — but for "
        "those, only where this Act does not clash with the law made specially "
        "for them.\n\n"
        "Nothing here creates a duty you can breach. It is the boundary line of "
        "everything that follows."
    ),

    '2': (
        "This is the dictionary of the Act, and it is the most quietly powerful "
        "section in it. Around ninety-five terms are defined here, and every one "
        "of those definitions travels into every other section that uses the "
        "word.\n\n"
        "It is where you find out what actually counts as a \"company\", a "
        "\"private company\", a \"subsidiary\", a \"related party\", a \"key "
        "managerial personnel\", \"control\", or a \"small company\". A single "
        "word in this list can decide whether an entire chapter applies to a "
        "business.\n\n"
        "That matters in practice: whether your company is \"small\" changes what "
        "you must file, and whether someone is a \"related party\" changes "
        "whether a contract needs board approval. When a section elsewhere in the "
        "Act seems unclear, the answer is usually a definition sitting here."
    ),

    # ── Chapter II — Incorporation of company and matters incidental thereto ──
    '3': (
        "This is the section that lets a company exist at all, and it sets the "
        "smallest number of people you need to start one.\n\n"
        "Seven or more people can form a public company. Two or more can form a "
        "private company. One person on their own can form a One Person Company, "
        "which the Act treats as a kind of private company.\n\n"
        "It also sets out the three ways the members' liability can be capped: "
        "limited by shares, limited by guarantee, or unlimited — where members "
        "carry the company's debts without any ceiling."
    ),

    '3A': (
        "A short section with sharp teeth. If a company's membership drops below "
        "the legal minimum — seven for a public company, two for a private one — "
        "and it keeps trading for more than six months anyway, the protection of "
        "limited liability falls away.\n\n"
        "Every member who knows about the shortfall and stays on becomes "
        "personally liable for the debts run up during that time, and can be sued "
        "for them individually."
    ),

    '4': (
        "The memorandum is a company's founding document, and this section lists "
        "what it must contain: the name, the state where the registered office "
        "will be, what the company is there to do, how far the members' liability "
        "goes, and how much share capital it starts with.\n\n"
        "The name rules live here too. A name cannot be identical or nearly "
        "identical to an existing company's, cannot be offensive, and cannot "
        "suggest a connection with the government without permission. You can ask "
        "the Registrar to reserve a name before you incorporate.\n\n"
        "Get the reservation by lying about it and the consequences are steep — "
        "the reservation can be cancelled, and the company can be struck off."
    ),

    '5': (
        "If the memorandum is what the company is, the articles are how it runs. "
        "This section says the articles hold the rules for managing the company — "
        "meetings, directors, shares, voting.\n\n"
        "It also allows entrenchment: certain rules can be locked so that changing "
        "them needs more than the usual special resolution. That is how a founder "
        "or an investor protects a right they do not want a future majority to "
        "vote away."
    ),

    '6': (
        "A tie-breaker. Where the Companies Act says one thing and a company's own "
        "memorandum, articles, agreements or board resolutions say another, the "
        "Act wins.\n\n"
        "Anything in those documents that conflicts with the Act is simply void. A "
        "company cannot contract its way out of the law by writing something "
        "different into its own rulebook."
    ),

    '7': (
        "This is the actual act of incorporation — what you file, and what you get "
        "back.\n\n"
        "The subscribers file the memorandum and articles with the Registrar, "
        "along with declarations that the requirements have been met, the address "
        "and identity details of everyone involved, and the first directors' "
        "consent. If the Registrar is satisfied, the company is registered and "
        "issued a certificate of incorporation carrying its CIN — its permanent "
        "identity number.\n\n"
        "The section is unusually severe about lying to get there. False or "
        "incorrect information brings the fraud punishment under section 447, and "
        "if a company was incorporated by fraud, the Tribunal can order almost "
        "anything, including winding it up or removing the members' limited "
        "liability altogether."
    ),

    '8': (
        "Section 8 is the route for non-profit companies — those set up for "
        "charity, education, science, sport, art, research, religion, "
        "environmental protection or social welfare.\n\n"
        "The Central Government grants a licence allowing the company to drop "
        "\"Limited\" or \"Private Limited\" from its name. In exchange, every "
        "rupee of profit has to go back into the objects, and no dividend may be "
        "paid to members.\n\n"
        "The licence can be revoked if the company breaks those terms or works "
        "against the public interest, and conversion into an ordinary company is "
        "tightly controlled."
    ),

    '9': (
        "The moment named on the certificate of incorporation, the company becomes "
        "a legal person in its own right.\n\n"
        "From that date it can own property, sign contracts, sue and be sued in "
        "its own name, and it keeps going regardless of members joining, leaving "
        "or dying. That last quality is called perpetual succession."
    ),

    '10': (
        "Once registered, the memorandum and articles bind the company and every "
        "member as if each of them had personally signed the documents and "
        "promised to keep to them.\n\n"
        "In practice that makes the articles a contract — between the company and "
        "its members, and between the members themselves. Money owed by a member "
        "to the company under those documents counts as a debt."
    ),

    '10A': (
        "A company with share capital cannot simply start trading the day it is "
        "registered.\n\n"
        "Within 180 days of incorporation, a director must file a declaration that "
        "every subscriber has paid for the shares they agreed to take. The company "
        "must also have told the Registrar where its registered office is. Until "
        "both are done, it may not begin business or borrow money.\n\n"
        "Miss it and there are penalties, and the Registrar may conclude the "
        "company is not carrying on business and move to strike its name off."
    ),

    '11': (
        "This section no longer exists. It was omitted by the Companies "
        "(Amendment) Act, 2015, which removed the old requirement to file a "
        "declaration before starting business.\n\n"
        "The requirement came back in a different form in 2019 and now lives in "
        "section 10A. If you are looking for the rule about when a new company may "
        "begin trading, that is the section to read."
    ),

    '12': (
        "Every company must have a registered office within thirty days of "
        "incorporation, and keep one at all times. It is the address where "
        "official letters and legal notices can be delivered.\n\n"
        "The company has to tell the Registrar where it is, and paint or affix its "
        "name and address outside every office it works from, in a language the "
        "area uses. The name has to appear on letterheads, bills, notices and its "
        "seal as well.\n\n"
        "Moving the office is a formal step: within the same city needs a board "
        "resolution, further afield needs the members' approval, and moving to "
        "another state needs the Central Government's confirmation."
    ),

    '13': (
        "The memorandum can be changed, but not casually. Every alteration needs a "
        "special resolution — three-quarters of the votes cast, not a simple "
        "majority.\n\n"
        "Some changes need more than that. Changing the company's name needs the "
        "Central Government's approval. Shifting the registered office from one "
        "state to another needs the Central Government's confirmation, and anyone "
        "whose interests are affected gets a hearing first.\n\n"
        "If the company raised money from the public and has not spent it yet, it "
        "cannot quietly change its objects: it needs a special resolution and it "
        "must offer an exit to any dissenting shareholder."
    ),

    '14': (
        "The articles can be altered by special resolution, and that includes "
        "changing what kind of company it is — private to public, or public to "
        "private.\n\n"
        "Turning a public company private is the harder direction: it needs the "
        "approval of the Tribunal, whose order then has to be filed with the "
        "Registrar. Every alteration must reach the Registrar, who records it."
    ),

    '15': (
        "A housekeeping rule with a real point behind it. Every alteration made to "
        "the memorandum or articles must be written into every copy the company "
        "hands out.\n\n"
        "The idea is that nobody should be given an out-of-date rulebook and left "
        "to act on it. Ignore this and there is a penalty of a thousand rupees for "
        "each copy issued without the change."
    ),

    '16': (
        "This is what happens when a company ends up with a name it should not "
        "have.\n\n"
        "If the Central Government finds the name is identical to, or too close "
        "to, one already registered, it can direct the company to change it. If "
        "the name is too close to a registered trade mark, the trade mark owner "
        "can complain within three years and the government can order a change.\n\n"
        "The company then has a fixed window to adopt a new name by ordinary "
        "resolution. If it does not, the Registrar allots one itself."
    ),

    '17': (
        "A member is entitled to read the documents that govern the company they "
        "part-own.\n\n"
        "Ask, and the company must send a copy of the memorandum, the articles, "
        "and every agreement and resolution that has to be filed with the "
        "Registrar, within seven days. It may charge a prescribed fee. Refusing "
        "carries a penalty on the company and on the officers responsible."
    ),

    '18': (
        "A company can change what class it belongs to — private to public, "
        "limited to unlimited, and so on — by altering its memorandum and articles "
        "under this Chapter.\n\n"
        "The Registrar closes the old registration and issues a fresh certificate "
        "of incorporation. What does not change is the company's history: debts, "
        "contracts and liabilities from before the conversion follow it across "
        "untouched."
    ),

    '19': (
        "A subsidiary is not allowed to hold shares in its own holding company, "
        "and the holding company cannot allot or transfer shares to it. Any such "
        "allotment or transfer is void.\n\n"
        "The reason is circularity: a parent funding itself through a company it "
        "already controls would let the same money count twice.\n\n"
        "There are three narrow exceptions — where the subsidiary holds the shares "
        "as a legal representative of a dead member, where it holds them as a "
        "trustee, and where it was already a shareholder before it became a "
        "subsidiary. Even then it usually cannot vote those shares."
    ),

    '20': (
        "How you deliver a document to a company so that it counts in law.\n\n"
        "Anything sent to the company or one of its officers goes to the "
        "registered office — by registered post, speed post, courier, by hand, or "
        "electronically in the prescribed way.\n\n"
        "Documents for a member go to the address on the register, and a member "
        "can ask for delivery by a particular method if they pay for it. Getting "
        "service wrong is a common way for a case to stall, which is why the "
        "Act spells it out."
    ),

    '21': (
        "A company is not a person and cannot sign anything itself, so this "
        "section says who signs for it.\n\n"
        "Documents, proceedings and contracts may be signed by any key managerial "
        "personnel, or by an officer or employee the Board has authorised for that "
        "purpose. Without that authority, a signature does not bind the company."
    ),

    '22': (
        "This section covers negotiable instruments and formal deeds.\n\n"
        "A bill of exchange, hundi or promissory note counts as the company's own "
        "if it is made, accepted, drawn or endorsed in the company's name by "
        "someone acting with its authority.\n\n"
        "For deeds and contracts signed elsewhere, the company can authorise a "
        "person in writing to act as its attorney, and what that attorney signs "
        "binds the company."
    ),

    # ── Chapter III — Prospectus and allotment of securities ─────────────────
    '23': (
        "There are only two lawful ways for a company to raise money by issuing "
        "securities, and this section names them.\n\n"
        "A public company can make a public offer through a prospectus, or go the "
        "private placement route to a selected group. A private company can only "
        "do the second — it may not invite the public to subscribe at all.\n\n"
        "Everything else in this Chapter hangs off that split: Part I governs "
        "public offers, Part II governs private placements."
    ),

    '24': (
        "This section draws the line between two regulators.\n\n"
        "Where the issue or transfer of securities and the non-payment of dividend "
        "concerns listed companies, or companies that intend to list, SEBI makes "
        "the rules and enforces them. For everything else, and for all other "
        "companies, it is the Central Government and the Registrar.\n\n"
        "It is the reason a listed company answers to both the Companies Act and "
        "the SEBI rulebook, and why the two do not contradict each other on the "
        "same point."
    ),

    '25': (
        "A company cannot dodge the prospectus rules by selling shares to a "
        "middleman and letting the middleman sell them on to the public.\n\n"
        "Where securities are allotted with a view to being offered to the public, "
        "the document that makes that offer is treated as a prospectus issued by "
        "the company itself — with all the duties and liabilities that carries.\n\n"
        "The Act even tells you when to be suspicious: if the offer comes within "
        "six months of allotment, or the company has not been paid in full, the "
        "arrangement is presumed to have been a way around the law."
    ),

    '26': (
        "The contents list for a prospectus. It says what a company must tell "
        "people before asking them for money.\n\n"
        "That includes who runs the company, what it does, what it intends to do "
        "with the money raised, its financial position, the risks, any litigation, "
        "and the terms of the offer. The prospectus must be dated, signed, and "
        "delivered to the Registrar before it goes out.\n\n"
        "Issue one that leaves out what this section requires and there are "
        "penalties for the company and for every person who authorised it."
    ),

    '27': (
        "Money raised on a prospectus has to be used for what the prospectus said "
        "it would be used for.\n\n"
        "Changing those objects, or the terms of a contract mentioned in the "
        "prospectus, needs a special resolution of the members. The company also "
        "has to advertise the proposal so shareholders actually learn of it.\n\n"
        "Anyone who disagrees gets an exit: dissenting shareholders must be offered "
        "the chance to have their shares bought back, on terms SEBI prescribes."
    ),

    '28': (
        "This covers existing shareholders selling their own shares to the public, "
        "rather than the company issuing new ones.\n\n"
        "They may do it in consultation with the Board, and the document offering "
        "the shares counts as a prospectus — so the same disclosure duties and the "
        "same liabilities apply.\n\n"
        "The selling shareholders, not the company, bear the cost of the offer, "
        "in proportion to what each of them sells."
    ),

    '29': (
        "Certain securities can only exist electronically.\n\n"
        "Every company making a public offer must issue those securities in "
        "dematerialised form, held in a depository account rather than as paper "
        "certificates. Other classes of company can be brought into the same rule "
        "by the government.\n\n"
        "Physical share certificates are easy to forge, lose and transfer "
        "invisibly, which is the problem this addresses."
    ),

    '30': (
        "A short rule about advertising.\n\n"
        "Whenever a prospectus is advertised anywhere, the advertisement itself "
        "must carry the company's objects, the liability of its members, the amount "
        "of share capital, and the names of the signatories.\n\n"
        "The point is that a person should not be drawn in by a headline promise "
        "without the basic facts alongside it."
    ),

    '31': (
        "A shelf prospectus saves a company from writing a fresh prospectus for "
        "every tranche of a series of issues.\n\n"
        "It is filed once and stays valid for up to one year from the first offer. "
        "For each later offer within that year, the company files only an "
        "information memorandum updating what has changed — new financial position, "
        "new charges created, and so on.\n\n"
        "The shelf prospectus plus the memorandum together count as the prospectus "
        "for that offer."
    ),

    '32': (
        "A red herring prospectus is issued before the full prospectus and leaves "
        "out the details that are not fixed yet — typically the price of the "
        "securities or the number on offer.\n\n"
        "It has to be filed with the Registrar at least three days before the offer "
        "opens, and it carries the same obligations as a prospectus.\n\n"
        "Once the offer closes, the complete prospectus with the final details goes "
        "to the Registrar and to SEBI."
    ),

    '33': (
        "You cannot hand someone an application form for securities on its own.\n\n"
        "Every form must come with an abridged prospectus — a short-form version of "
        "the real thing — so that nobody applies for securities without at least a "
        "summary of what they are buying.\n\n"
        "The exception is where the form is issued in connection with a genuine "
        "invitation to enter into an underwriting agreement, which is a deal "
        "between professionals rather than an offer to the public."
    ),

    '34': (
        "If a prospectus contains a statement that is untrue or misleading, or "
        "leaves out something that makes it misleading, this is the criminal "
        "consequence.\n\n"
        "Every person who authorised the issue of that prospectus is liable to the "
        "punishment for fraud under section 447 — which can mean imprisonment as "
        "well as a fine.\n\n"
        "There is one way out: a person escapes if they prove the statement was "
        "immaterial, or that they had reasonable grounds to believe it was true and "
        "did believe it, right up until the prospectus was issued."
    ),

    '35': (
        "The same misleading prospectus, but the civil side: compensation for "
        "people who lost money.\n\n"
        "Anyone who subscribed for securities relying on it and suffered a loss can "
        "claim against the company, its directors, its promoters, the experts named "
        "in it, and everyone who authorised its issue. They are liable jointly and "
        "severally, so a claimant can pursue any one of them for the whole loss.\n\n"
        "A director escapes by showing they withdrew before the prospectus was "
        "issued, or that it went out without their knowledge or consent, or that "
        "they reasonably believed the statement was true.\n\n"
        "Where the misleading statement was made to defraud, the people responsible "
        "carry personal liability without limit."
    ),

    '36': (
        "This one is not about prospectuses at all — it is about the sales pitch.\n\n"
        "Anyone who knowingly or recklessly makes a false, deceptive or misleading "
        "statement, promise or forecast, or deliberately hides a material fact, in "
        "order to persuade someone to invest, commits fraud under section 447.\n\n"
        "It reaches agreements to acquire or subscribe for securities, and "
        "agreements whose purpose is to make money from the movement of a security's "
        "price."
    ),

    '37': (
        "A short but useful section: it says who can bring the case.\n\n"
        "An action under section 34, 35 or 36 can be brought not only by one "
        "affected person but by a group of people or an association of them acting "
        "together.\n\n"
        "Small investors rarely sue alone, because the loss is too small to justify "
        "the cost. This lets them combine."
    ),

    '38': (
        "This targets people who apply for securities under false identities, "
        "usually to grab more of an oversubscribed issue than their share.\n\n"
        "Applying in a fictitious name, making multiple applications under different "
        "names or different combinations of names, or inducing a company to allot "
        "securities to a false identity, all attract the fraud punishment under "
        "section 447.\n\n"
        "A court can also order the securities and any profit from them forfeited "
        "to the Investor Education and Protection Fund."
    ),

    '39': (
        "An offer to the public has a floor, and this section sets it.\n\n"
        "No allotment can be made unless the minimum amount stated in the "
        "prospectus has actually been subscribed and the application money "
        "received. That money cannot be less than five per cent of the nominal "
        "value of the security.\n\n"
        "If the minimum is not reached within thirty days, the money has to go back "
        "to the applicants. The idea is that a company should not begin a project "
        "on money that only half arrived."
    ),

    '40': (
        "Before a company makes a public offer, it must apply to one or more "
        "recognised stock exchanges for permission for the securities to be traded "
        "there, and say in the prospectus which exchanges it applied to.\n\n"
        "If permission is refused, the allotment is void and the money must be "
        "returned. Application money is held in a separate bank account and can "
        "only be used for allotment or for repaying it.\n\n"
        "The section is what stops a company selling shares that then turn out to "
        "have nowhere to be sold on."
    ),

    '41': (
        "A single sentence with a wide reach. A company may issue depository "
        "receipts in a foreign country — the instrument that lets an overseas "
        "investor hold an Indian company's shares through a foreign bank.\n\n"
        "It needs a special resolution of the members first, and the manner and "
        "conditions are set by rules."
    ),

    '42': (
        "This is the private placement route: raising money from a chosen group "
        "instead of from the public.\n\n"
        "The offer goes only to people the Board has identified in advance, and to "
        "no more than two hundred people in a financial year for each kind of "
        "security, leaving out qualified institutional buyers and employees holding "
        "stock options. Go past that and it is treated as a public offer, with "
        "every prospectus obligation that brings.\n\n"
        "The money must arrive by banking channels — never in cash — into a "
        "separate account, and it cannot be touched until the return of allotment "
        "is filed. Allotment has to happen within sixty days, or the money goes "
        "back within fifteen more, with interest after that.\n\n"
        "The company also may not advertise the offer to anyone outside the "
        "identified group."
    ),

    # ── Chapter IV — Share capital and debentures ────────────────────────────
    '43': ("A company limited by shares can issue two kinds of share capital: equity and preference.\n\n"
           "Equity shares carry voting rights, or come with differential rights as to dividend or voting. "
           "Preference shares get their dividend first and rank ahead of equity if the company is wound up, "
           "but normally carry no vote on general matters.\n\n"
           "A One Person Company and a private company can be exempted from this split by their own articles."),
    '44': ("Shares and debentures are movable property. You can sell or transfer them the way the company's "
           "articles allow, and they pass like any other asset a person owns.\n\n"
           "It sounds obvious, but it is the legal foundation for every share transfer, inheritance and pledge."),
    '45': ("Every share must carry its own distinctive number, so one can be told apart from another.\n\n"
           "The exception is shares held in electronic form with a depository — there, the depository's records "
           "do the identifying, so numbering is not required."),
    '46': ("A share certificate is the company's formal proof of who owns what.\n\n"
           "It has to be issued under the common seal or signed by two directors, and it names the member, the "
           "shares and how much has been paid on them. In law it is prima facie evidence of ownership.\n\n"
           "Issuing a duplicate certificate fraudulently is treated seriously — the company faces a heavy fine "
           "and the officers responsible face the fraud punishment under section 447."),
    '47': ("The default voting rules. Every equity shareholder votes on every resolution, and their voting power "
           "is proportional to their share of the paid-up capital.\n\n"
           "Preference shareholders normally vote only on resolutions that affect them directly. But if their "
           "dividend goes unpaid for two years or more, they get a vote on everything — the Act's way of giving "
           "them leverage when the company stops paying."),
    '48': ("Where shares are split into classes, the rights of one class cannot be changed at the whim of the "
           "majority.\n\n"
           "Varying them needs the written consent of three-quarters of that class, or a special resolution "
           "passed at a separate meeting of that class. If the change affects another class too, that class has "
           "to agree as well.\n\n"
           "Holders of at least ten per cent of the class who did not consent can apply to the Tribunal to have "
           "the variation cancelled."),
    '49': ("When a company calls for the unpaid part of share money, it must ask everyone in the same class on "
           "the same basis.\n\n"
           "It cannot demand from one shareholder and spare another holding the same kind of share. Shares of "
           "different amounts paid up are not treated as the same class for this purpose."),
    '50': ("A company may, if its articles allow, accept money a shareholder offers on shares before it has "
           "actually called for it.\n\n"
           "The shareholder gains no extra voting rights by paying early — the vote still follows what has been "
           "called up, not what has been paid."),
    '51': ("If the articles permit, a company can pay dividends in proportion to how much has actually been paid "
           "on each share, rather than treating all shares alike.\n\n"
           "So someone who has paid the full amount can receive more than someone who has paid only part."),
    '52': ("When shares are sold above face value, the extra is the premium, and it does not belong to the "
           "company as ordinary profit.\n\n"
           "It goes into a securities premium account and can only be used for a short list of things: issuing "
           "bonus shares, writing off preliminary expenses or the expenses of an issue, providing for the "
           "premium on redeeming redeemable preference shares or debentures, and buying back shares.\n\n"
           "It cannot be paid out as a dividend. The premium is treated almost like capital."),
    '53': ("A company may not issue shares at a discount, and any share it does issue that way is simply void.\n\n"
           "The reason is creditor protection: share capital is what creditors look to, and selling shares below "
           "value quietly hollows it out.\n\n"
           "There are two exceptions — sweat equity shares under section 54, and shares issued to lenders when a "
           "debt is converted into shares under a statutory resolution scheme."),
    '54': ("Sweat equity shares are issued to directors or employees for what they have contributed rather than "
           "for cash — know-how, intellectual property, or value they have added.\n\n"
           "They are the one ordinary exception to the ban on issuing shares at a discount. The issue needs a "
           "special resolution stating the number, the price, the consideration and who gets them, and the "
           "shares carry the same rights as ordinary equity."),
    '55': ("Preference shares must be redeemable. A company cannot issue preference shares that last forever.\n\n"
           "They have to be redeemed within twenty years, except for infrastructure projects, where a longer "
           "period is allowed if a portion is redeemed each year from the twenty-first.\n\n"
           "Only fully paid shares can be redeemed, and the money must come out of profits available for "
           "dividend or from a fresh issue made for the purpose — never out of capital. Where profits are used, "
           "an equivalent amount goes into the capital redemption reserve."),
    '56': ("How ownership of shares actually moves from one person to another.\n\n"
           "For a transfer, a proper instrument of transfer signed by both sides must reach the company within "
           "sixty days. For a transmission — where shares pass on death or insolvency — the law does the "
           "transferring and the company needs proof rather than a transfer deed.\n\n"
           "The company must deliver the new certificates within a month of receiving the transfer. Registering "
           "a transfer fraudulently attracts the section 447 fraud punishment."),
    '57': ("Pretending to be the owner of someone else's shares in order to get them transferred, or to collect "
           "money due on them, is a criminal offence.\n\n"
           "It carries imprisonment of at least one year and up to three, and a fine between one lakh and five "
           "lakh rupees."),
    '58': ("A private company can refuse to register a transfer of its shares — that restriction is part of what "
           "makes it private. But it must give reasons, in writing, within thirty days.\n\n"
           "The person refused can appeal to the Tribunal: within thirty days of getting the notice, or within "
           "sixty days of sending the transfer if no notice ever came.\n\n"
           "Shares of a public company are freely transferable, and the Tribunal can order a refused transfer to "
           "be registered and compensation to be paid."),
    '59': ("The register of members decides who legally owns shares, so this section provides the way to correct "
           "it when it is wrong.\n\n"
           "Anyone whose name has been entered without good reason, or wrongly left out or removed, can apply to "
           "the Tribunal. It can order the register rectified and damages paid.\n\n"
           "Where shares were transferred or transmitted in breach of the law, the Tribunal can direct the "
           "company to set the transfer aside."),
    '60': ("If a company states its authorised capital on a notice, advertisement, letterhead or bill, it must "
           "state the subscribed and paid-up capital just as prominently.\n\n"
           "Authorised capital is only a ceiling. Showing it alone lets a company look far larger than the money "
           "actually put into it, which is precisely what this prevents."),
    '61': ("A limited company with share capital can reshape that capital in general meeting, if its articles "
           "allow.\n\n"
           "It can increase the authorised amount, consolidate shares into larger ones, split them into smaller "
           "ones, convert fully paid shares into stock and back, or cancel shares that were never taken up.\n\n"
           "Consolidation that changes the voting rights of shareholders also needs the Tribunal's approval. "
           "Cancelling unissued shares is not a reduction of capital, so it does not need the section 66 route."),
    '62': ("When a company issues new shares, existing shareholders get first refusal. This is the pre-emption "
           "right, and it exists so that a shareholding is not quietly diluted.\n\n"
           "The offer must go to existing holders in proportion to what they already hold, by notice giving at "
           "least fifteen days and not more than thirty to accept. The right can be renounced in someone else's "
           "favour unless the articles say otherwise, and shares nobody takes can then be offered elsewhere.\n\n"
           "There are two ways round it: an issue to employees under an approved stock option scheme, and an "
           "issue to anyone else where the members pass a special resolution.\n\n"
           "Shares issued to a lender when a government-approved debt conversion takes effect fall outside the "
           "section altogether."),
    '63': ("Bonus shares are fully paid shares given free to existing members, funded from the company's own "
           "reserves.\n\n"
           "They can only come from free reserves, the securities premium account or the capital redemption "
           "reserve — never from a revaluation of assets, because that would be issuing shares against a paper "
           "gain.\n\n"
           "The articles must permit it, the members must approve, and the company must not have defaulted on "
           "deposits, debentures or employee dues. Once announced, a bonus issue cannot be withdrawn."),
    '64': ("Whenever a company alters its share capital, redeems preference shares, or has its capital changed by "
           "a government order, the Registrar has to be told within thirty days.\n\n"
           "The notice includes the altered memorandum. The public register is only useful if it matches "
           "reality, and this is the section that keeps it matching."),
    '65': ("An unlimited company converting into a limited one can set aside part of its capital as reserve — an "
           "amount that can only ever be called up if the company is wound up.\n\n"
           "It is a cushion held back for creditors at the end, and once designated it cannot be called for "
           "ordinary trading purposes."),
    '66': ("Reducing share capital means giving capital back to shareholders or writing off capital already "
           "lost, and creditors have an obvious interest in it.\n\n"
           "So it needs a special resolution and confirmation by the Tribunal. The Tribunal notifies the "
           "Registrar, SEBI where the company is listed, and every creditor, and it will not confirm a reduction "
           "while any creditor's objection is unsettled — unless the debt is secured or the creditor has agreed.\n\n"
           "A company cannot reduce capital at all while it is in arrears on repaying deposits or the interest "
           "on them. Hiding a creditor's name from the list is a fraud offence under section 447."),
    '67': ("A company generally may not buy its own shares, and may not lend money or give security to help "
           "anyone else buy them.\n\n"
           "The concern is a company funding the purchase of itself, which weakens the capital creditors rely "
           "on.\n\n"
           "There are exceptions: a lending company doing it in the ordinary course of business, loans to a "
           "trust that holds shares for employees, and loans to employees other than directors and key "
           "managerial personnel, up to their salary for six months."),
    '68': ("Buy-back is the controlled route by which a company may purchase its own shares.\n\n"
           "The money can only come from free reserves, the securities premium account or the proceeds of a "
           "fresh issue. The buy-back cannot exceed twenty-five per cent of paid-up capital and free reserves, "
           "and after it, debt must not be more than twice capital and free reserves.\n\n"
           "Up to ten per cent can be done on a board resolution; beyond that it needs a special resolution. "
           "The shares bought back must be destroyed within seven days, and the company cannot make a further "
           "issue of the same kind of shares for a year.\n\n"
           "A declaration of solvency signed by directors has to be filed first."),
    '69': ("Where a company buys back shares out of free reserves or the securities premium account, an amount "
           "equal to the nominal value of those shares must be moved into the capital redemption reserve.\n\n"
           "The reserve keeps the company's capital base intact on paper even though shares have gone. It can be "
           "used to issue fully paid bonus shares."),
    '70': ("Some buy-backs are barred outright.\n\n"
           "A company cannot buy its own shares through a subsidiary, through an investment company or group of "
           "them, or at any time when it is in default on deposits, debentures, preference share redemption, "
           "dividends or loans from a bank.\n\n"
           "It also cannot buy back if it has failed to comply with the rules on annual returns, dividends or "
           "financial statements. The default has to be made good and three years passed."),
    '71': ("Debentures are borrowing, not ownership, and this section governs them.\n\n"
           "They may be issued convertible into shares, wholly or partly, if the members approve by special "
           "resolution. They cannot carry voting rights — a lender does not get to vote.\n\n"
           "Where debentures are offered to the public or to more than five hundred people, the company must "
           "appoint a debenture trustee to protect holders' interests and create a debenture redemption reserve "
           "out of profits. A holder who is not paid can go to the Tribunal, which can order repayment."),
    '72': ("Any holder of shares or debentures can name a person to inherit them on death.\n\n"
           "The nomination overrides anything in a will or any other law about who gets the securities, which is "
           "why it matters that it is kept up to date.\n\n"
           "Where the nominee is a minor, the holder can appoint someone to take them if the minor is still "
           "under age at the time."),

    # ── Chapter V — Acceptance of deposits by companies ──────────────────────
    '73': ("A company cannot take deposits from the general public. This is the section that closes that door.\n\n"
           "A private company may accept deposits from its own members, and only after a long list of conditions: "
           "a circular to members, a copy filed with the Registrar, a deposit repayment reserve holding at least "
           "twenty per cent of the deposits due next year, deposit insurance, and a certificate that the company "
           "has not defaulted before.\n\n"
           "It also has to disclose any past default. The point is to stop unregulated deposit-taking dressed up "
           "as company finance."),
    '74': ("Deposits taken before this Act came into force could not simply be left outstanding.\n\n"
           "A company holding them had to file details with the Registrar and repay within three years, or by "
           "whatever date the deposit fell due, whichever came first.\n\n"
           "The Tribunal can allow more time if the company can show it will be able to pay."),
    '75': ("If a company fails to repay a deposit and it turns out the deposits were accepted with intent to "
           "defraud depositors, the protection of the company's separate personality falls away.\n\n"
           "Every officer responsible becomes personally liable, without any limit, for the losses depositors "
           "suffered — on top of the fraud punishment under section 447.\n\n"
           "The claim can be brought by any depositor affected."),
    '76': ("Some public companies can take deposits from people who are not members, but only if they are large "
           "enough and only on stricter terms.\n\n"
           "They must meet a prescribed net worth or turnover, get a credit rating every year, and follow "
           "everything section 73 requires.\n\n"
           "Where the deposits are secured, a charge must be created on the company's assets within thirty days."),
    '76A': ("The penalty section for deposit-taking gone wrong, and it is deliberately severe.\n\n"
            "A company that accepts deposits in breach of the rules repays the deposit with interest and pays a "
            "penalty of at least one crore rupees or twice the deposit, whichever is lower, up to ten crore.\n\n"
            "Every officer in default can face imprisonment of up to seven years plus a fine. Where the default "
            "was knowingly done to defraud, it is also fraud under section 447."),

    # ── Chapter VI — Registration of charges ─────────────────────────────────
    '77': ("A charge is security given over a company's property for a loan, and it has to be on the public "
           "record.\n\n"
           "The company must register every charge it creates with the Registrar within thirty days. Late "
           "registration is possible on payment of additional fees — up to sixty days more, and a further sixty "
           "beyond that on an application with reasons.\n\n"
           "The consequence of not registering is the real point: an unregistered charge cannot be relied on "
           "against a liquidator or any other creditor. The lender falls back to being unsecured, which is where "
           "the money is actually lost."),
    '78': ("If a company does not register a charge it created, the lender does not have to wait and lose its "
           "security.\n\n"
           "The person in whose favour the charge was made can apply to the Registrar and register it "
           "themselves, and recover the cost from the company.\n\n"
           "The Registrar gives the company fourteen days to object first."),
    '79': ("The registration rules apply beyond the simple case of a company creating a fresh charge.\n\n"
           "They cover a company buying property that already has a charge on it, and any change to the terms, "
           "the amount secured, or the identity of the charge-holder."),
    '80': ("Once a charge is registered, everyone dealing with that property is treated as knowing about it.\n\n"
           "A buyer cannot later claim they had no idea the asset was already secured. This deemed notice is "
           "what makes the public register worth keeping."),
    '81': ("The Registrar keeps a register of all charges for every company, and it is open to inspection by "
           "anyone on payment of a fee.\n\n"
           "That openness is the whole mechanism: a lender can check what is already secured before agreeing to "
           "lend."),
    '82': ("When a charge is paid off, the company must tell the Registrar within thirty days so the entry can "
           "be closed.\n\n"
           "Late intimation is allowed on additional fees. The Registrar notifies the charge-holder and gives "
           "fourteen days to object before recording the satisfaction.\n\n"
           "A charge left on the register after the debt is gone makes the company look more encumbered than it "
           "is, which quietly raises the cost of its next loan."),
    '83': ("The Registrar does not have to wait for the company to report that a charge is finished.\n\n"
           "On satisfactory evidence that the debt has been paid, or that part of the property has been released "
           "or has ceased to be the company's, the Registrar can enter that on the register directly and inform "
           "the company."),
    '84': ("When a receiver or manager is appointed over property that is subject to a charge, the Registrar has "
           "to be told within thirty days — by whoever obtained the order or made the appointment.\n\n"
           "The same applies when that person stops acting. A receiver taking control of secured assets is "
           "something anyone dealing with the company needs to be able to see."),
    '85': ("Separately from the Registrar's register, every company keeps its own register of charges at its "
           "registered office, together with copies of the instruments creating them.\n\n"
           "It is open to members and creditors free of charge, and to anyone else on payment. The company's "
           "records have to be preserved for eight years after the charge is satisfied."),
    '86': ("The penalty for breaking any rule in this Chapter: five lakh rupees on the company, and up to fifty "
           "thousand on every officer in default.\n\n"
           "Where someone wilfully gives false information or suppresses it in a charge filing, that is fraud "
           "under section 447."),
    '87': ("A safety valve. Where a charge was not registered in time, or a satisfaction was not reported, "
           "because of genuine oversight or accident — or where leaving it uncorrected would prejudice "
           "creditors or shareholders — the Central Government can order the record corrected.\n\n"
           "It cannot be used to rewrite a charge after someone has relied on the register in good faith."),

    # ── Chapter VII — Management and administration ──────────────────────────
    '88': ("Every company keeps registers of who owns it: a register of members, one of debenture holders, and "
           "one of any other security holders.\n\n"
           "The register of members has to show each person's shareholding and whether anyone else holds the "
           "beneficial interest behind it. Companies with more than fifty members also keep an index.\n\n"
           "A foreign register may be kept abroad for members living outside India."),
    '89': ("Sometimes the person named in the register is not the person who really owns the shares. This "
           "section makes both of them declare it.\n\n"
           "The registered holder files a declaration saying they are not the beneficial owner; the real owner "
           "files one saying they are. The company then records it and tells the Registrar within thirty days.\n\n"
           "Until that declaration is made, no right attached to those shares can be enforced by the person "
           "hiding behind them."),
    '90': ("This is the beneficial ownership section — the law aimed at finding the human being at the end of a "
           "chain of companies and trusts.\n\n"
           "Anyone holding a significant beneficial interest, alone or with others, must declare it, and the "
           "company keeps a register of significant beneficial owners and files it with the Registrar.\n\n"
           "A company can require any member it believes holds such an interest to answer. If they do not, it "
           "applies to the Tribunal, which can freeze the shares altogether — no transfer, no dividend, no vote.\n\n"
           "Making a false declaration is fraud under section 447."),
    '91': ("A company can close its register of members or security holders for a period, typically so it can "
           "fix who is entitled to a dividend or to vote.\n\n"
           "It must give at least seven days' notice, and cannot close the register for more than thirty days at "
           "a time or forty-five days in a year."),
    '92': ("The annual return is the company's yearly statement of what it is and who runs it.\n\n"
           "It covers the registered office, the business, shareholding, changes in members and directors, "
           "meetings held, remuneration of directors and key managerial personnel, and any penalties imposed.\n\n"
           "It is signed by a director and the company secretary, and for larger companies certified by a "
           "practising company secretary. Filing late carries penalties on the company and its officers.\n\n"
           "Along with the financial statements, this is the filing that keeps a company on the register."),
    '93': ("This section no longer exists. It was omitted by the Companies (Amendment) Act, 2017, with effect "
           "from June 2018.\n\n"
           "It used to require a listed company to file a return whenever a promoter's or top shareholder's "
           "stake changed by two per cent or more. That disclosure is now handled by SEBI's own rules for listed "
           "companies rather than by this Act."),
    '94': ("Registers and annual returns are normally kept at the registered office, where members can inspect "
           "them.\n\n"
           "They can be kept somewhere else in the same city if members approve by special resolution and the "
           "Registrar is given advance notice.\n\n"
           "Members and debenture holders may inspect free of charge; anyone else on payment. Refusing "
           "inspection carries a penalty."),
    '95': ("A short evidential rule. The registers, their indices and the annual returns count as prima facie "
           "evidence of what they contain.\n\n"
           "In a dispute, that means the register is taken as correct unless someone proves otherwise — the "
           "burden sits with the person challenging it."),
    '96': ("Every company except a One Person Company must hold an annual general meeting each year.\n\n"
           "The first one comes within nine months of the end of the first financial year; after that, within "
           "six months of the year end, and never more than fifteen months after the last one.\n\n"
           "It must be held during business hours, on a day that is not a national holiday, at the registered "
           "office or somewhere in the same city. The Registrar can extend the deadline by up to three months, "
           "but not for the first meeting."),
    '97': ("If a company simply does not hold its annual general meeting, a member can ask the Tribunal to order "
           "one.\n\n"
           "The Tribunal can call the meeting, direct how it is to be held, and even rule that a meeting of one "
           "member present in person or by proxy counts as a valid general meeting.\n\n"
           "A meeting held on that order is treated as the company's annual general meeting."),
    '98': ("Where it has become impracticable to call or conduct any other meeting, the Tribunal can step in.\n\n"
           "It can order the meeting to be held and give directions about how, including the one-member rule. It "
           "acts on its own motion, or on the application of a director or a member entitled to vote."),
    '99': ("The penalty for failing to hold a meeting required by sections 96 to 98, or to obey the Tribunal's "
           "directions about one.\n\n"
           "The company and every officer in default face a fine of up to one lakh rupees, and a further five "
           "thousand a day for each day the default continues."),
    '100': ("An extraordinary general meeting is any general meeting that is not the annual one — called when "
            "something cannot wait a year.\n\n"
            "The Board can call one whenever it sees fit, and must call one if members holding at least one "
            "tenth of the paid-up voting capital requisition it.\n\n"
            "If the Board does not proceed within twenty-one days of a valid requisition, the requisitionists can "
            "call the meeting themselves within three months, and the company must reimburse their expenses out "
            "of the fees owed to the defaulting directors."),
    '101': ("A general meeting needs at least twenty-one clear days' notice, in writing or electronically.\n\n"
            "The notice states the place, date, time and the business to be transacted, and goes to every "
            "member, legal representative of a deceased member, assignee of an insolvent member, auditor and "
            "director.\n\n"
            "Shorter notice is possible if enough members agree — ninety-five per cent for an extraordinary "
            "general meeting, and for an annual general meeting the consent of ninety-five per cent of those "
            "entitled to vote. An accidental failure to give notice to someone does not invalidate the meeting."),
    '102': ("For any item of special business, the notice must be accompanied by a statement setting out the "
            "material facts — what the item really involves, and the nature and extent of any interest held by "
            "a director, manager, key managerial personnel or their relatives.\n\n"
            "The point is that nobody votes blind, and nobody hides a personal stake in what they are asking "
            "shareholders to approve.\n\n"
            "If a benefit reaches a promoter or director because a fact was left out, they must compensate the "
            "company for it."),
    '103': ("Quorum is the minimum attendance a meeting needs to be valid.\n\n"
            "For a public company it rises with size: five members present in person where there are up to a "
            "thousand members, fifteen up to five thousand, and thirty beyond that. For a private company, two "
            "members present.\n\n"
            "If quorum is not there within half an hour, a meeting called by requisition is cancelled; any other "
            "meeting stands adjourned to the same day next week. If quorum fails again, those present are the "
            "quorum."),
    '104': ("Unless the articles say otherwise, the members present elect one of themselves as chairman by a "
            "show of hands.\n\n"
            "If a poll is demanded on that election, it is taken immediately, and the chairman elected on the "
            "show of hands continues until the poll result is known."),
    '105': ("A member entitled to attend and vote can appoint a proxy to attend and vote for them.\n\n"
            "A proxy cannot speak at the meeting, and can only vote on a poll — not on a show of hands, unless "
            "the company has no share capital. The proxy form has to reach the company at least forty-eight "
            "hours before the meeting.\n\n"
            "One person cannot act as proxy for more than fifty members, or for members holding more than ten "
            "per cent of the voting capital. Every notice of a meeting must tell members, prominently, that they "
            "have this right."),
    '106': ("The articles may bar a member from voting while calls on their shares are unpaid, or where the "
            "company has exercised a lien over the shares.\n\n"
            "Apart from those grounds, no other restriction may be imposed. A member who votes cannot be "
            "stopped from splitting their votes on the same resolution."),
    '107': ("The default method of voting at a general meeting is a show of hands — one person, one hand, "
            "regardless of shareholding.\n\n"
            "The chairman's declaration of the result, recorded in the minutes, is conclusive proof unless a "
            "poll is demanded under section 109 or the voting is done electronically."),
    '108': ("A short enabling section. The Central Government can prescribe which classes of company must let "
            "members vote by electronic means, and how.\n\n"
            "It is what makes remote e-voting possible for listed and larger companies, so a shareholder does "
            "not have to travel to vote."),
    '109': ("A poll replaces the show of hands with voting by shareholding, so a large holder's vote counts for "
            "what it is worth.\n\n"
            "The chairman can order one, and must order one if it is demanded by members holding at least a "
            "tenth of the voting power or shares on which at least five lakh rupees is paid up.\n\n"
            "A poll on adjournment or on the chairman's election is taken at once. Any other poll is taken "
            "within forty-eight hours. A demand can be withdrawn by the person who made it."),
    '110': ("Some business must be transacted by postal ballot rather than at a meeting, and the Central "
            "Government says which.\n\n"
            "The company sends a notice with the draft resolution and a form, and members return it or vote "
            "electronically. A resolution passed by postal ballot counts as if it had been passed at a properly "
            "held general meeting.\n\n"
            "Ordinary business, and anything on which the law requires the auditors or directors to be heard, "
            "cannot go to a postal ballot."),
    '111': ("Members are not limited to voting on what the Board puts in front of them.\n\n"
            "On a requisition by members holding the same stake needed to call an extraordinary general meeting, "
            "the company must give notice of a resolution they propose, and circulate a statement of up to a "
            "thousand words about any matter to be dealt with at the meeting.\n\n"
            "The requisitionists pay the cost unless the company resolves otherwise. The company can refuse if "
            "the Tribunal agrees the right is being abused to secure needless publicity or defame someone."),
    '112': ("Where the President of India or a Governor of a State is a member of a company, they may appoint "
            "someone to represent them at meetings.\n\n"
            "That representative has all the rights an individual member would have, including the right to "
            "appoint a proxy."),
    '113': ("A company or other body corporate cannot personally attend a meeting, so it authorises a "
            "representative by resolution of its board.\n\n"
            "That person can exercise all the powers the body corporate itself would have — speaking, voting on "
            "a show of hands, and appointing a proxy.\n\n"
            "The same applies where a body corporate is a creditor and attends a meeting of creditors."),
    '114': ("The Act's two levels of shareholder approval.\n\n"
            "An ordinary resolution passes if the votes in favour outnumber the votes against. A special "
            "resolution needs at least three times as many votes for as against — the three-quarters "
            "majority — and the notice must have said that it is being proposed as a special resolution.\n\n"
            "Which one applies is set by the section dealing with the subject, which is why the distinction "
            "runs through the whole Act."),
    '115': ("Certain resolutions need special notice — for example removing an auditor or a director before "
            "their term ends.\n\n"
            "Members holding at least one per cent of the voting power, or shares on which five lakh rupees is "
            "paid up, give the company notice of their intention, and the company then notifies the members."),
    '116': ("A resolution passed at an adjourned meeting is treated as having been passed on the day it was "
            "actually passed, not backdated to the original meeting.\n\n"
            "It settles what would otherwise be an argument about which date governs the resolution's effect."),
    '117': ("Certain resolutions and agreements have to be filed with the Registrar within thirty days, so they "
            "become part of the public record.\n\n"
            "They include every special resolution, resolutions the members agreed to unanimously that would "
            "otherwise need a special resolution, board resolutions on borrowing and investment powers, and "
            "resolutions to wind up voluntarily.\n\n"
            "Failing to file carries penalties on the company and its officers. Banking companies do not have to "
            "file resolutions about ordinary lending."),
    '118': ("Minutes are the official record of what a meeting decided, and this section makes keeping them "
            "compulsory.\n\n"
            "Every general meeting, board meeting, committee meeting and postal ballot resolution must be minuted "
            "within thirty days, in books kept for the purpose, with pages numbered consecutively.\n\n"
            "Minutes must be a fair and correct summary. The chairman decides what goes in, and can leave out "
            "anything defamatory, irrelevant or detrimental to the company. Once signed, they are evidence that "
            "the meeting happened and the resolutions were passed.\n\n"
            "Tampering with them is an offence, and the secretarial standards on minutes must be followed."),
    '119': ("Members can inspect the minute books of general meetings free of charge during business hours, and "
            "ask for copies within seven days on payment.\n\n"
            "Refusing inspection carries a penalty, and the Tribunal can order the inspection or the copy to be "
            "provided immediately.\n\n"
            "The right covers general meetings, not board meetings — board minutes are not open to members."),
    '120': ("Anything a company must keep or allow to be inspected — records, registers, minutes, returns — may "
            "be kept in electronic form instead of on paper.\n\n"
            "It is what allows a modern company to run without physical registers, subject to the manner "
            "prescribed by rules."),
    '121': ("Every listed public company must prepare a report on each annual general meeting, confirming that "
            "the meeting was called, held and conducted as the Act requires.\n\n"
            "The report goes to the Registrar within thirty days. Failing to file it carries penalties on the "
            "company and on the officers in default."),
    '122': ("A One Person Company has one member, so most of the machinery of meetings makes no sense for it.\n\n"
            "Sections 98 and 100 to 111 do not apply. It need not hold an annual general meeting at all.\n\n"
            "Instead, the member simply communicates the resolution, enters it in the minutes book, signs and "
            "dates it — and that is the date the meeting is treated as having been held. Where the company has "
            "one director, a board resolution works the same way."),

    # ── Chapter VIII — Declaration and payment of dividend ───────────────────
    '123': ("Dividend is a share of profit, and this section controls where it can come from.\n\n"
            "It may be paid out of the year's profits after providing for depreciation, out of profits from "
            "previous years left undistributed, or out of money the government has provided for the purpose. "
            "Capital cannot be used.\n\n"
            "Where profits are inadequate, a company can dip into free reserves, but only on prescribed terms. "
            "A company that has not repaid deposits or their interest cannot declare a dividend at all.\n\n"
            "Dividend goes to a separate bank account within five days of declaration, and interim dividend is "
            "declared by the Board out of surplus or the current year's profits."),
    '124': ("Dividend that is declared but not claimed does not stay with the company.\n\n"
            "Anything unpaid or unclaimed thirty days after declaration goes into a special Unpaid Dividend "
            "Account within seven days. The company publishes the list of names on its website.\n\n"
            "Money still unclaimed after seven years goes to the Investor Education and Protection Fund — and so "
            "do the shares it relates to. The shareholder can still claim them back from the Fund, which is why "
            "the transfer is not a forfeiture."),
    '125': ("The Investor Education and Protection Fund is where unclaimed investor money ends up.\n\n"
            "It receives unpaid dividends, matured deposits and debentures, application money due for refund, "
            "and the interest on all of them, once seven years have passed.\n\n"
            "The Fund is used to refund claimants who come forward, to promote investor education and awareness, "
            "and to reimburse the legal costs of class actions brought by members or depositors.\n\n"
            "It is administered by an authority appointed by the Central Government and audited by the "
            "Comptroller and Auditor-General."),
    '126': ("Where a share transfer has been lodged with the company but not yet registered, the dividend and "
            "any rights or bonus shares are held in abeyance.\n\n"
            "The company keeps the dividend in the Unpaid Dividend Account unless the registered holder "
            "authorises paying it to the transferee.\n\n"
            "It stops the money going to the wrong person while the paperwork is still moving."),
    '127': ("Declaring a dividend and then not paying it is an offence, not merely a debt.\n\n"
            "If the dividend is not paid or the warrant not posted within thirty days of declaration, every "
            "director who knew about the default can face imprisonment of up to two years and a fine of at least "
            "one thousand rupees for each day it continues. The company pays eighteen per cent interest.\n\n"
            "There are defences — where the failure was the shareholder's own doing, or a lawful adjustment, or "
            "a dispute over entitlement, or where it was not the company's fault."),

    # ── Chapter IX — Accounts of companies ───────────────────────────────────
    '128': ("Every company keeps proper books of account at its registered office, showing all money received "
            "and spent, all sales and purchases, its assets and liabilities.\n\n"
            "They can be kept electronically, and at another place in India if the Registrar is told. Books must "
            "be preserved for at least eight financial years.\n\n"
            "Directors can inspect them. Keeping them badly is not a paperwork slip: officers in default face a "
            "fine, and books are the foundation everything else in this Chapter rests on."),
    '129': ("Financial statements must give a true and fair view of the company's affairs and follow the "
            "accounting standards.\n\n"
            "The Board lays them before the annual general meeting each year. Where a company has subsidiaries, "
            "associates or joint ventures, it also prepares consolidated statements covering the whole group.\n\n"
            "\"True and fair\" is the legal standard: statements that technically comply with a standard but "
            "leave a misleading impression do not meet it."),
    '129A': ("A short enabling section. The Central Government can require prescribed classes of unlisted "
             "companies to prepare financial results during the year, not just at the end of it.\n\n"
             "Those results must be approved by the Board, audited or reviewed, and filed with the Registrar. It "
             "brings some unlisted companies closer to the quarterly rhythm listed ones already follow."),
    '130': ("Accounts once approved are normally final. This section is the narrow exception.\n\n"
            "A court or the Tribunal can order a company to re-open its books and recast its financial "
            "statements — but only on an application by the Central Government, an income-tax authority, SEBI, "
            "another regulator, or a person the Tribunal permits.\n\n"
            "The grounds are serious: the accounts were prepared fraudulently, or the company's affairs were "
            "mismanaged and the accounts cannot be relied on. Books cannot be re-opened beyond eight financial "
            "years back."),
    '131': ("Where the directors themselves realise the accounts or the Board's report do not comply with the "
            "Act, they can revise them voluntarily.\n\n"
            "It needs the Tribunal's approval, and the Tribunal hears the Central Government and the income-tax "
            "authorities first. Revision is allowed only for the three preceding financial years, and only once "
            "in a year.\n\n"
            "The point is that a company can correct itself without waiting to be caught, but not quietly."),
    '132': ("This constitutes the National Financial Reporting Authority — the regulator that oversees auditors "
            "and accounting standards.\n\n"
            "It recommends accounting and auditing standards to the Central Government, monitors compliance, and "
            "oversees the quality of the audit profession.\n\n"
            "It can investigate professional misconduct by chartered accountants and firms, and where it finds "
            "misconduct it can impose penalties and debar a member or firm from practice for up to ten years. "
            "Its proceedings carry the powers of a civil court."),
    '133': ("The Central Government prescribes the accounting standards, on the recommendation of the Institute "
            "of Chartered Accountants of India and in consultation with the National Financial Reporting "
            "Authority.\n\n"
            "It is the section that gives the standards their legal force — without it they would be professional "
            "guidance rather than law."),
    '134': ("This section covers what goes out with the accounts: the Board's report.\n\n"
            "The financial statements are approved by the Board and signed by the chairperson or two directors, "
            "including the managing director, along with the chief executive, chief financial officer and "
            "company secretary where appointed.\n\n"
            "The Board's report must cover the state of the company's affairs, dividend recommended, reserves, "
            "material changes since the year end, conservation of energy, risk management, related party "
            "contracts and corporate social responsibility.\n\n"
            "It also carries the directors' responsibility statement — a signed declaration that the accounts "
            "were properly prepared and that internal controls were adequate."),
    '135': ("Corporate social responsibility is a spending obligation, not a suggestion.\n\n"
            "A company with net worth of five hundred crore or more, turnover of a thousand crore or more, or "
            "net profit of five crore or more in a financial year must form a CSR Committee of the Board with at "
            "least one independent director.\n\n"
            "It must spend at least two per cent of its average net profits of the preceding three years on the "
            "activities listed in Schedule VII. If it does not, the Board explains why in its report.\n\n"
            "Unspent money attached to an ongoing project moves to a special account and must be used within "
            "three years; anything else goes to a fund named in Schedule VII."),
    '136': ("A member is entitled to see the accounts before the meeting that adopts them.\n\n"
            "The financial statements, the auditor's report and every document to be laid at the annual general "
            "meeting must be sent to every member, trustee for debenture holders and other entitled person at "
            "least twenty-one days beforehand.\n\n"
            "Listed companies also place them on their website. A company with a subsidiary must make the "
            "subsidiary's accounts available too."),
    '137': ("The accounts do not stay inside the company. A copy of the financial statements, adopted at the "
            "annual general meeting, goes to the Registrar within thirty days.\n\n"
            "If they were not adopted, they are still filed as unadopted, and the adopted set follows within "
            "thirty days of the adjourned meeting.\n\n"
            "Filing late carries penalties on the company, on the managing director or the director responsible, "
            "and on the chief financial officer."),
    '138': ("Prescribed classes of company must appoint an internal auditor — a chartered accountant, cost "
            "accountant, or another professional the Board decides on.\n\n"
            "The internal auditor checks the company's own systems and controls as it goes along, which is a "
            "different job from the statutory audit at the end of the year."),

    # ── Chapter X — Audit and auditors ───────────────────────────────────────
    '139': ("How a company gets its auditor, and for how long.\n\n"
            "At the first annual general meeting a company appoints an auditor to hold office until the "
            "conclusion of the sixth annual general meeting — a five-year term, ratified as prescribed.\n\n"
            "Listed and prescribed companies must rotate: an individual auditor for one term of five years, an "
            "audit firm for two terms of five years, and then a cooling-off of five years before returning. The "
            "idea is that familiarity between auditor and company should not be allowed to set.\n\n"
            "The first auditor is appointed by the Board within thirty days of incorporation, and a casual "
            "vacancy is filled by the Board — or by the members if the vacancy came from a resignation."),
    '140': ("Getting rid of an auditor is deliberately hard, because an auditor who can be dismissed easily "
            "cannot report honestly.\n\n"
            "Removal before the term ends needs a special resolution and the Central Government's prior "
            "approval, and the auditor must be given a chance to be heard.\n\n"
            "A resigning auditor files a statement of the reasons with the company and the Registrar within "
            "thirty days. Where the Tribunal is satisfied an auditor acted fraudulently or colluded with the "
            "company, it can order a change of auditor, and that auditor cannot be appointed by any company for "
            "five years."),
    '141': ("Who may be an auditor, and who may not.\n\n"
            "Only a chartered accountant, or a firm where the majority of partners practising in India are "
            "chartered accountants, is eligible.\n\n"
            "Disqualified are: a body corporate other than an LLP, an officer or employee of the company, a "
            "partner or employee of such a person, anyone holding securities in the company or indebted to it "
            "beyond the prescribed limit, anyone with a business relationship with it, a relative of a director, "
            "and a person already auditing twenty companies.\n\n"
            "A person convicted of fraud cannot be appointed for ten years."),
    '142': ("The auditor's fee is fixed in general meeting, or in the manner the members decide there — not by "
            "the management the auditor is checking.\n\n"
            "The first auditor's fee can be fixed by the Board. The fee includes out-of-pocket expenses, but not "
            "payment for other services rendered at the company's request."),
    '143': ("This is the heart of the audit: what an auditor may do and must do.\n\n"
            "The auditor has a right of access at all times to the company's books and vouchers, wherever they "
            "are kept, and can require information from officers. For a holding company, the same access extends "
            "to subsidiaries and associates.\n\n"
            "The report must say whether the accounts give a true and fair view, whether the company has adequate "
            "internal financial controls, and answer a list of specific questions including whether loans made "
            "are prejudicial to the company's interests.\n\n"
            "The duty that matters most is reporting fraud. Where an auditor has reason to believe an offence "
            "involving fraud is being committed, they must report it — to the Central Government above the "
            "prescribed amount, and to the audit committee or Board below it. Failing to report is itself "
            "punishable."),
    '144': ("An auditor cannot audit work they did themselves, so this section lists the services they may not "
            "provide to the company, its holding company or its subsidiary.\n\n"
            "Barred are accounting and book-keeping, internal audit, design of financial information systems, "
            "actuarial services, investment advisory, investment banking, outsourced financial services and "
            "management services.\n\n"
            "Anything else needs the approval of the Board or the audit committee."),
    '145': ("The person appointed as auditor signs the audit report personally.\n\n"
            "Qualifications, observations or comments on financial matters in that report must be read out at "
            "the general meeting, and are open to inspection by any member. An adverse remark cannot be buried "
            "in a document nobody reads aloud."),
    '146': ("Auditors receive notice of every general meeting and are entitled to attend, either personally or "
            "through an authorised representative who is qualified to be an auditor.\n\n"
            "They have the right to be heard at the meeting on any part of the business that concerns them as "
            "auditor. Unless the company exempts them, attendance is expected."),
    '147': ("The penalties for breaking the audit provisions.\n\n"
            "A company in contravention faces a fine, and its officers in default a fine and possible "
            "imprisonment. An auditor who contravenes sections 139 to 146 faces a fine from twenty-five thousand "
            "to five lakh rupees, or four times the audit fee, whichever is less.\n\n"
            "Where the auditor acted knowingly or wilfully with intent to deceive, it becomes imprisonment of up "
            "to one year plus a larger fine, and the auditor must refund the fee and pay damages. Where a firm's "
            "partner acted fraudulently, the firm is jointly and severally liable."),
    '148': ("Some companies must audit not just their money but their costs.\n\n"
            "For prescribed classes engaged in production, processing, manufacturing or mining, the Central "
            "Government can direct that particulars of cost be included in the books, and order a cost audit.\n\n"
            "The cost audit is done by a cost accountant, appointed by the Board, and the report goes to the "
            "Board and then to the Central Government. The auditor of the accounts cannot do the cost audit."),

    # ── Chapter XI — Appointment and qualifications of directors ─────────────
    '149': ("Every company has a Board made up of individuals — never another company.\n\n"
            "The minimum is three directors for a public company, two for a private one and one for a One "
            "Person Company; the maximum is fifteen, and more than that needs a special resolution.\n\n"
            "Every company must have at least one director who stayed in India for 182 days or more in the "
            "previous year. Listed companies must have at least one woman director and at least a third of the "
            "Board independent.\n\n"
            "The section defines what independence means — no pecuniary relationship, no relatives among the "
            "directors, no past employment — and independent directors are not entitled to stock options and can "
            "serve two consecutive five-year terms at most."),
    '150': ("Independent directors can be picked from a data bank maintained by an approved institute, holding "
            "the names and qualifications of eligible people.\n\n"
            "The company remains responsible for checking that the person it appoints is suitable, and the "
            "appointment is approved by the members at a general meeting."),
    '151': ("A listed company may have one director elected by its small shareholders — those holding shares of "
            "nominal value of twenty thousand rupees or less.\n\n"
            "It gives the smallest investors a seat rather than leaving the Board entirely to the large holders "
            "who can outvote them."),
    '152': ("The general rules for appointing directors.\n\n"
            "Where the articles are silent, the individual subscribers to the memorandum are the first directors "
            "until the first annual general meeting. Every director is appointed by the members in general "
            "meeting, must have a Director Identification Number, and must give written consent, which the "
            "company files with the Registrar.\n\n"
            "In a public company, at least two-thirds of the directors are liable to retire by rotation, and a "
            "third of them retire at each annual general meeting — the longest-serving first."),
    '153': ("Anyone who intends to be a director applies to the Central Government for a Director Identification "
            "Number, in the prescribed form and with the prescribed fee.\n\n"
            "The DIN is the permanent identifier that follows a person across every company they serve, which is "
            "what makes disqualification enforceable."),
    '154': ("The Central Government allots the Director Identification Number within one month of receiving the "
            "application.\n\n"
            "A short procedural section, but it is the step that turns an applicant into someone eligible to be "
            "appointed."),
    '155': ("No one may hold more than one Director Identification Number.\n\n"
            "A second number would let a disqualified person reappear as somebody new, which is exactly what the "
            "single-number rule prevents."),
    '156': ("Every existing director must tell all the companies where they are a director of their DIN, within "
            "one month of receiving it.\n\n"
            "It is how the number reaches the company's own records and, from there, the public register."),
    '157': ("Once a director gives their DIN, the company passes it to the Registrar within fifteen days.\n\n"
            "Failure carries a penalty on the company and on every officer in default. The chain is deliberate: "
            "person to company, company to Registrar, so the identity is verifiable at both ends."),
    '158': ("Whenever a person or company files a return, information or particulars under this Act that relate "
            "to a director, the DIN must be mentioned.\n\n"
            "It makes every filing traceable to a specific individual rather than to a common name."),
    '159': ("The penalty for failing to comply with the DIN provisions — sections 152, 155 and 156.\n\n"
            "The individual or director in default faces a penalty of up to fifty thousand rupees, and a further "
            "five hundred rupees for each day the default continues."),
    '160': ("Someone who is not a retiring director can still stand for the Board.\n\n"
            "They, or a member proposing them, give the company at least fourteen days' notice before the "
            "meeting along with a deposit of one lakh rupees. The deposit comes back if the person is elected or "
            "gets more than twenty-five per cent of the votes cast.\n\n"
            "The deposit is not required for an independent director or a person recommended by the Board."),
    '161': ("Three ways a director can join the Board between general meetings, if the articles allow.\n\n"
            "An additional director can be appointed by the Board, but only holds office until the next annual "
            "general meeting. An alternate director can be appointed to act for a director absent from India for "
            "at least three months. A nominee director can be appointed by a financial institution, the "
            "government or under an agreement.\n\n"
            "The Board can also fill a casual vacancy caused by a director leaving before their term ends."),
    '162': ("At a general meeting, two or more directors cannot be appointed by a single resolution.\n\n"
            "Each appointment is voted on separately, unless the members first agree unanimously to do it "
            "together. A resolution passed in breach of this is void.\n\n"
            "It stops a Board being presented as a package, where members must accept an unwanted candidate to "
            "get a wanted one."),
    '163': ("A company's articles may provide for at least two-thirds of its directors to be appointed by "
            "proportional representation — by single transferable vote or cumulative voting.\n\n"
            "Under ordinary majority voting, a group holding just over half the shares elects the entire Board. "
            "Proportional representation lets a substantial minority elect someone. Those appointments are made "
            "once every three years."),
    '164': ("The list of things that stop a person being a director.\n\n"
            "Unsoundness of mind, undischarged insolvency, a pending insolvency application, conviction for an "
            "offence with a sentence of six months or more in the last five years, a court order disqualifying "
            "them, unpaid calls on shares for six months, and conviction for related party dealings in the last "
            "five years.\n\n"
            "The one that catches most people is sub-section (2): a director of a company that has failed to "
            "file financial statements or annual returns for three continuous years, or failed to repay deposits "
            "or debentures for a year, cannot be reappointed there or appointed anywhere else for five years."),
    '165': ("A person may hold directorships in up to twenty companies, and of those no more than ten may be "
            "public companies.\n\n"
            "The members can set a lower number for their own company by special resolution.\n\n"
            "Someone over the limit must resign from the excess within a year. Continuing beyond that carries a "
            "penalty of two thousand rupees a day, and there is a ceiling on the total."),
    '166': ("The statutory statement of what a director owes the company.\n\n"
            "A director must act in accordance with the articles, in good faith to promote the objects of the "
            "company for the benefit of its members as a whole, and in the best interests of the company, its "
            "employees, the shareholders, the community and the environment.\n\n"
            "They must exercise reasonable care, skill and independent judgement, must not put themselves in a "
            "position where their interest conflicts with the company's, must not make any undue gain, and must "
            "not assign their office to someone else.\n\n"
            "A director who makes an undue gain has to hand it back to the company."),
    '167': ("When a director's seat empties automatically, without anyone voting.\n\n"
            "It happens on incurring a disqualification, on missing every Board meeting for twelve months, on "
            "breaching the related-party rules in section 184 or 188, on being disqualified by a court or "
            "Tribunal order, on conviction with a sentence of six months or more, and on being removed under the "
            "Act.\n\n"
            "Someone who carries on acting as a director after their office has become vacant faces imprisonment "
            "of up to a year or a fine, or both."),
    '168': ("A director resigns by giving written notice to the company, and the resignation takes effect from "
            "the date the company receives it or a later date stated in it.\n\n"
            "The Board takes note, the company tells the Registrar, and the resignation appears in the next "
            "Board's report. The director may also send a copy with reasons to the Registrar themselves.\n\n"
            "Resigning does not wipe the slate: a director stays liable for offences committed while in office."),
    '169': ("Members can remove a director by ordinary resolution before their term ends, after giving the "
            "director a reasonable opportunity of being heard.\n\n"
            "A director appointed by the Tribunal under section 242 cannot be removed this way, and neither can "
            "one appointed by proportional representation under section 163.\n\n"
            "The director has the right to be heard at the meeting, and to have their written representation "
            "circulated to members. If it arrives too late, they can require it to be read out."),
    '170': ("Every company keeps a register at its registered office of its directors and key managerial "
            "personnel — their particulars and their shareholding, including in the holding, subsidiary and "
            "associate companies.\n\n"
            "A return of the register and of any change in it goes to the Registrar within thirty days."),
    '171': ("The register of directors and key managerial personnel is open to members for inspection during "
            "business hours, free of charge, and they can take extracts.\n\n"
            "It must also be kept open at the annual general meeting and made accessible to anyone attending. "
            "Refusing inspection carries a penalty, and the Tribunal can order it immediately."),
    '172': ("The residual penalty for this Chapter. Where a company breaks any provision about directors and no "
            "specific punishment is set out for it, the company and every officer in default face a penalty of "
            "fifty thousand rupees, and five hundred rupees a day while it continues, up to a ceiling."),

    # ── Chapter XII — Meetings of Board and its powers ───────────────────────
    '173': ("The Board must meet, and this section sets the rhythm.\n\n"
            "The first meeting comes within thirty days of incorporation. After that, at least four meetings a "
            "year, with no more than one hundred and twenty days between two of them.\n\n"
            "Meetings need at least seven days' notice in writing. Directors can take part by video conference or "
            "other audio-visual means, though certain sensitive items — approving accounts, a merger — may be "
            "barred from being decided that way.\n\n"
            "A One Person Company, small company or dormant company needs only one meeting in each half of the "
            "year, at least ninety days apart."),
    '174': ("Quorum for a Board meeting is one-third of the total strength or two directors, whichever is "
            "higher.\n\n"
            "Directors joining by video conference count towards it. If interested directors have to be excluded "
            "and the remaining number falls below quorum, those left — if two or more — become the quorum.\n\n"
            "Where a meeting cannot be held for want of quorum, it stands adjourned to the same day, time and "
            "place next week."),
    '175': ("Not every Board decision needs a meeting. A resolution can be passed by circulation — the draft is "
            "sent to every director at their registered address and approved by a majority.\n\n"
            "But if at least one-third of the directors want the matter decided at a meeting, it has to be. And "
            "a circulated resolution must still be noted at the next Board meeting and recorded in the minutes."),
    '176': ("A safety net for third parties. If it later turns out a director's appointment was invalid or had "
            "ended, the acts they did in the meantime are still valid.\n\n"
            "Someone dealing with a company cannot be expected to audit its internal appointments. The section "
            "stops that being a way to escape a contract — though it does not validate acts done after the "
            "defect was known."),
    '177': ("Every listed public company and prescribed classes must have an audit committee of at least three "
            "directors, a majority of them independent, and a majority able to read financial statements.\n\n"
            "It recommends the appointment and remuneration of auditors, reviews the financial statements and "
            "the auditor's report, examines related party transactions, evaluates internal controls, and can "
            "call for outside professional advice.\n\n"
            "It also runs the vigil mechanism — the whistle-blower channel — which prescribed companies must "
            "establish, with safeguards against victimisation and direct access to the committee's chairperson."),
    '178': ("Two more committees for listed public companies and prescribed classes.\n\n"
            "The Nomination and Remuneration Committee, of three or more non-executive directors with at least "
            "half independent, identifies who is fit to be a director, evaluates performance and frames the "
            "remuneration policy for directors, key managerial personnel and other employees.\n\n"
            "The Stakeholders Relationship Committee is required where a company has more than a thousand "
            "shareholders, debenture holders or deposit holders, and deals with their grievances."),
    '179': ("The Board can exercise every power the company itself has, subject to the Act and the articles.\n\n"
            "Some powers can only be exercised at a Board meeting, by resolution: calls on shares, buy-back "
            "under section 68, issuing securities, borrowing, investing the company's funds, granting loans, "
            "approving financial statements and the Board's report, diversifying the business, approving a "
            "merger, and taking over another company.\n\n"
            "Certain of those can be delegated to a committee, the managing director or the manager, on terms "
            "the Board sets."),
    '180': ("Four things the Board cannot do without the members' consent by special resolution.\n\n"
            "Selling or leasing the whole or substantially the whole of an undertaking. Investing the "
            "compensation from a compulsory acquisition in anything other than trust securities. Borrowing "
            "beyond the company's paid-up capital, free reserves and securities premium taken together — "
            "temporary bank loans in the ordinary course excepted. And giving time or waiving repayment of a "
            "debt owed by a director.\n\n"
            "A borrowing beyond the limit is not valid against the lender unless the lender did not know."),
    '181': ("The Board may contribute to genuine charitable funds.\n\n"
            "But if the total in a financial year exceeds five per cent of the company's average net profits for "
            "the three preceding years, prior permission of the members in general meeting is needed."),
    '182': ("Political contributions, and the limits on them.\n\n"
            "A government company cannot contribute at all, and neither can a company less than three years old. "
            "Any other company can, but only with a Board resolution.\n\n"
            "Contributions must be made only by a route other than cash, and disclosed in the profit and loss "
            "account. Contravening carries a fine of up to five times the amount contributed, and imprisonment "
            "of up to six months for officers in default."),
    '183': ("A company can contribute to the National Defence Fund or any other fund the Central Government "
            "approves for national defence.\n\n"
            "This one is deliberately unrestricted — there is no ceiling — and the Board or anyone exercising "
            "its powers can decide it. The total contributed in a year is disclosed in the profit and loss "
            "account."),
    '184': ("Every director must disclose their interest.\n\n"
            "At the first Board meeting they attend, and at the first meeting of each financial year, and "
            "whenever their interests change, a director discloses their concern or interest in any company, "
            "firm or other body.\n\n"
            "Where a contract is proposed with a body in which a director is interested, they must disclose it "
            "at the meeting and must not take part in the discussion or the vote. A contract entered in breach "
            "is voidable at the company's option, and the director faces a penalty."),
    '185': ("A company generally may not lend to its own directors, or to anyone connected with them, or give a "
            "guarantee or security for their borrowing.\n\n"
            "The prohibition covers directors of the company and of its holding company, their partners and "
            "relatives, and firms in which they are partners.\n\n"
            "A company can lend to a person in whom a director is interested if the members approve by special "
            "resolution and the loan is used for the borrowing company's principal business. There are "
            "exceptions for a managing or whole-time director under a scheme available to all employees, and for "
            "companies whose ordinary business is lending."),
    '186': ("Limits on how far a company can lend, invest, or guarantee for others.\n\n"
            "Investments are normally made through no more than two layers of investment companies. Loans, "
            "guarantees and securities to any other body corporate are capped at sixty per cent of paid-up "
            "capital, free reserves and securities premium, or one hundred per cent of free reserves and "
            "securities premium, whichever is more.\n\n"
            "Going beyond needs a special resolution. The interest charged cannot be below the yield on "
            "government securities of comparable tenure, and a company in default on deposits cannot lend at "
            "all. Every loan, guarantee and investment goes into a register open to members."),
    '187': ("A company must hold its investments in its own name.\n\n"
            "It stops assets being parked in a nominee's name where they are hard to trace and easy to move.\n\n"
            "There are exceptions — shares held through a depository, shares in a subsidiary held by nominees to "
            "meet the minimum member requirement, and deposits with a bank as security. Where an investment is "
            "not held in the company's own name, the reason goes in a register kept for the purpose."),
    '188': ("Related party transactions — deals between a company and people close to it.\n\n"
            "Sale or purchase of goods or property, leasing, availing or rendering services, appointing an agent, "
            "appointing a related party to an office of profit, and underwriting the company's securities all "
            "need the Board's consent by resolution at a meeting.\n\n"
            "Beyond prescribed limits, they also need a prior resolution of the members, and a member who is a "
            "related party cannot vote on it. Deals in the ordinary course of business on an arm's length basis "
            "fall outside the section.\n\n"
            "A contract made without approval is voidable, the director must indemnify the company for its loss, "
            "and in a listed company the officer in default faces a penalty."),
    '189': ("Every company keeps a register of the contracts and arrangements in which its directors are "
            "interested, with the particulars of each.\n\n"
            "The register is placed before the next Board meeting and signed by the directors present. It is "
            "kept at the registered office and is open to members, who can take extracts.\n\n"
            "It is the written trail behind section 184's disclosure duty."),
    '190': ("Where a company has a contract of service with a managing or whole-time director, it keeps a copy "
            "at its registered office — or a written memorandum of the terms if the contract is not in "
            "writing.\n\n"
            "Members can inspect it without charge. A private company is exempt."),
    '191': ("A director cannot take a personal payment for loss of office in connection with the transfer of the "
            "company's undertaking, property or shares, unless the members approve it.\n\n"
            "The concern is a director being quietly bought off to support a deal that is not in the company's "
            "interest.\n\n"
            "Where the payment is made without approval, the money is held in trust for the company — or, where "
            "it relates to a share transfer, for the shareholders who sold."),
    '192': ("A company cannot enter into an arrangement to buy an asset from a director, or sell one to them, "
            "for consideration other than cash, unless the members approve it in general meeting.\n\n"
            "The same applies to directors of the holding, subsidiary or associate company, and to people "
            "connected with them. The notice of the meeting must include a valuation of the asset by a "
            "registered valuer.\n\n"
            "An arrangement made without approval is voidable at the company's option."),
    '193': ("A One Person Company where the sole member is also the sole director presents an obvious problem: "
            "there is nobody on the other side of the table.\n\n"
            "So where such a company contracts with that member, and the contract is not in the ordinary course "
            "of business, the terms must be recorded in the minutes of the first Board meeting after it.\n\n"
            "The company must also inform the Registrar of every such contract."),
    '194': ("This section no longer exists. It was omitted by the Companies (Amendment) Act, 2017, with effect "
            "from February 2018.\n\n"
            "It used to prohibit directors and key managerial personnel from forward dealing in the company's "
            "securities. That conduct is now dealt with under SEBI's regulations rather than this Act."),
    '195': ("This section no longer exists either. It was omitted at the same time as section 194, in February "
            "2018.\n\n"
            "It contained the Companies Act's own prohibition on insider trading. Insider trading is now governed "
            "entirely by SEBI's Prohibition of Insider Trading Regulations, which is where that subject lives."),

    # ── Chapter XIII — Appointment and remuneration of managerial personnel ──
    '196': ("A company cannot have a managing director and a manager at the same time — the two roles overlap "
            "and the Act makes you choose.\n\n"
            "The term is up to five years at a time, and reappointment cannot be made earlier than one year "
            "before the current term expires.\n\n"
            "The person must be at least twenty-one and under seventy, though someone over seventy can be "
            "appointed by special resolution. They must not be an undischarged insolvent, must not have "
            "suspended payment to creditors, and must not have been convicted of an offence carrying more than "
            "six months. Appointment is approved by the Board and then by the members."),
    '197': ("The ceiling on what a public company can pay its managerial people.\n\n"
            "Total managerial remuneration cannot exceed eleven per cent of net profits. Within that, one "
            "managing or whole-time director or manager is capped at five per cent, and all of them together at "
            "ten per cent; other directors at one per cent where there is a managing director, three per cent "
            "where there is not.\n\n"
            "Paying more needs a resolution of the members, and if the company has defaulted to banks or "
            "debenture holders, their prior approval as well.\n\n"
            "Where profits are inadequate, Schedule V applies. Money paid over the limit has to be refunded, and "
            "the company cannot waive it without approval."),
    '198': ("This is the arithmetic behind section 197: how net profit is worked out for remuneration.\n\n"
            "It says which credits go in and which are left out, and which expenses are deducted and which are "
            "not.\n\n"
            "Profits from the sale of undertakings or immovable property, and unrealised gains on revaluation, "
            "are excluded. Income tax is not deducted; voluntary compensation, damages and legitimate business "
            "expenses are. The point is a consistent figure that cannot be shaped to enlarge a pay packet."),
    '199': ("Where a company has to restate its financial statements because of fraud or non-compliance, it must "
            "claw back what it overpaid.\n\n"
            "Remuneration, including stock options, received by any past or present managing director, "
            "whole-time director, manager or chief executive in excess of what the restated accounts justify has "
            "to be recovered for the two preceding financial years."),
    '200': ("When approving an appointment or a remuneration package, the Central Government or the company must "
            "have regard to a list of factors.\n\n"
            "They include the financial position of the company, the remuneration of comparable people elsewhere, "
            "the person's professional qualifications and experience, responsibilities, past performance, and "
            "the industry standard.\n\n"
            "It exists so a figure can be justified against something other than the Board's own goodwill."),
    '201': ("The procedural section for applications to the Central Government under this Chapter.\n\n"
            "The application must be in the prescribed form, and before it is made the company must publish a "
            "notice in newspapers — one in English and one in the regional language of the district where the "
            "registered office is — inviting objections from members.\n\n"
            "A copy of the notice goes to the members, and any objections received go to the government with the "
            "application."),
    '202': ("A company may compensate a managing director, whole-time director or manager for loss of office — "
            "but not any other director.\n\n"
            "No compensation is payable where the director resigns because of a reconstruction and is "
            "reappointed, where they resign otherwise, where their office is vacated under section 167, where "
            "the company is wound up through their own fault, or where they were guilty of fraud, breach of "
            "trust or gross negligence.\n\n"
            "The amount cannot exceed the remuneration they would have earned for the unexpired term, or three "
            "years, whichever is shorter."),
    '203': ("Prescribed classes of company must appoint whole-time key managerial personnel: a managing "
            "director or chief executive officer or manager and, where there is none of those, a whole-time "
            "director; a company secretary; and a chief financial officer.\n\n"
            "They are appointed by a Board resolution setting out the terms. A person cannot hold office as key "
            "managerial personnel in more than one company at a time, apart from its subsidiary.\n\n"
            "A vacancy has to be filled within six months. Failing to appoint carries a penalty on the company "
            "and on every director and officer in default."),
    '204': ("Every listed company, and prescribed classes of other companies, must attach a secretarial audit "
            "report to the Board's report.\n\n"
            "The audit is carried out by a company secretary in practice, and it examines whether the company has "
            "complied with the applicable laws — not just the Companies Act.\n\n"
            "The Board must explain in its report any qualification or observation the secretarial auditor "
            "makes. It is the compliance equivalent of a financial audit."),
    '205': ("What a company secretary is actually for.\n\n"
            "Reporting to the Board on compliance with this Act, the rules and other laws; ensuring the company "
            "follows the applicable secretarial standards; and discharging the other duties prescribed.\n\n"
            "The section makes the role a statutory one rather than an administrative title, which is why the "
            "secretary is one of the key managerial personnel who signs the accounts."),

}


def get(number):
    """The summary for a section, or None. `act.py` treats None as 'do not
    publish this section yet' rather than falling back to the bare text."""
    return SUMMARIES.get(str(number))


def covered(numbers):
    """Which of these section numbers have a summary written. A chapter goes
    live only when every one of its sections is covered."""
    return [n for n in numbers if str(n) in SUMMARIES]
