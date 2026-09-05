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

}


def get(number):
    """The summary for a section, or None. `act.py` treats None as 'do not
    publish this section yet' rather than falling back to the bare text."""
    return SUMMARIES.get(str(number))


def covered(numbers):
    """Which of these section numbers have a summary written. A chapter goes
    live only when every one of its sections is covered."""
    return [n for n in numbers if str(n) in SUMMARIES]
