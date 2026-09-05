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

}


def get(number):
    """The summary for a section, or None. `act.py` treats None as 'do not
    publish this section yet' rather than falling back to the bare text."""
    return SUMMARIES.get(str(number))


def covered(numbers):
    """Which of these section numbers have a summary written. A chapter goes
    live only when every one of its sections is covered."""
    return [n for n in numbers if str(n) in SUMMARIES]
