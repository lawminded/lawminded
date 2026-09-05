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

}


def get(number):
    """The summary for a section, or None. `act.py` treats None as 'do not
    publish this section yet' rather than falling back to the bare text."""
    return SUMMARIES.get(str(number))


def covered(numbers):
    """Which of these section numbers have a summary written. A chapter goes
    live only when every one of its sections is covered."""
    return [n for n in numbers if str(n) in SUMMARIES]
