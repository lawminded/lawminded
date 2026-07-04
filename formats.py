"""Ready-to-use document formats (real .docx files served as free downloads).

These are actual Word files stored in ``static/formats/`` and offered for
download on the Free Templates page. Unlike the DB-managed templates/resolutions
(which are generated on the fly from text), these are the genuine documents the
owner supplied — reviewed and stripped of any real names, firm names, FRNs,
membership/practice numbers and other personal data before publishing.

Each entry is (filename, title, description). The slug is derived from the
filename so links stay stable. ``FORMATS_BY_SLUG`` maps slug -> entry for the
download route; ``FORMAT_CATEGORIES`` drives the grouped listing on the page.
"""

import re


def _slug(filename):
    stem = filename.rsplit('.docx', 1)[0]
    s = stem.lower()
    s = s.replace('&', ' and ')
    s = re.sub(r"[^a-z0-9]+", '-', s)
    return s.strip('-')


# (category name, emoji icon, [ (filename, title, description), ... ])
_CATEGORIES = [
    ("Board Resolutions", "🗂️", [
        ("Board Resolution (General Template).docx",
         "Board Resolution – General Template",
         "A blank board resolution you can adapt for any decision taken by the directors."),
        ("Board Resolution - Activation of Bank Account.docx",
         "Board Resolution – Activation of Bank Account",
         "Resolution to activate or reactivate the company's bank account."),
        ("Board Resolution - Appointment of Cost Auditor.docx",
         "Board Resolution – Appointment of Cost Auditor",
         "Resolution appointing a cost auditor under the Companies Act."),
        ("Board Resolution - Appointment of First Auditor.docx",
         "Board Resolution – Appointment of First Auditor",
         "Resolution appointing the company's first statutory auditor after incorporation."),
        ("Board Resolution - Appointment of Secretarial Auditor and Internal Auditor.docx",
         "Board Resolution – Appointment of Secretarial & Internal Auditor",
         "Resolution appointing a secretarial auditor and an internal auditor."),
        ("Board Resolution - Authorisation (General).docx",
         "Board Resolution – General Authorisation",
         "Resolution authorising a director or officer to act for the company in a transaction."),
        ("Board Resolution - Authorisation for Signing of Account Documents.docx",
         "Board Resolution – Signing of Account Documents",
         "Resolution authorising named persons to sign the company's accounting documents."),
        ("Board Resolution - Authority for Banking Operations.docx",
         "Board Resolution – Authority for Banking Operations",
         "Resolution setting out who can operate the company's bank accounts and how."),
        ("Board Resolution - Authority for Purchase of Plot.docx",
         "Board Resolution – Authority for Purchase of Plot",
         "Resolution authorising a person to sign documents for buying a plot of land."),
        ("Board Resolution - Authority to Director (Litigation).docx",
         "Board Resolution – Authority to Director (Litigation)",
         "Resolution authorising a director to file or defend cases on the company's behalf."),
        ("Board Resolution - Declaration of Interim Dividend.docx",
         "Board Resolution – Declaration of Interim Dividend",
         "Resolution by the board declaring an interim dividend to shareholders."),
        ("Board Resolution - Dividend Account Closure.docx",
         "Board Resolution – Dividend Account Closure",
         "Resolution to close a dividend / unpaid-dividend bank account."),
        ("Board Resolution - Incorporation of Wholly Owned Subsidiary (WOS).docx",
         "Board Resolution – Incorporation of Wholly Owned Subsidiary",
         "Resolution approving the setting up of a wholly owned subsidiary company."),
        ("Board Resolution - Issue of Duplicate Share Certificate.docx",
         "Board Resolution – Issue of Duplicate Share Certificate",
         "Resolution approving the issue of a duplicate share certificate."),
        ("Board Resolution - Opening Bank Account.docx",
         "Board Resolution – Opening Bank Account",
         "Resolution to open a new current account in the company's name."),
        ("Board Resolution - Opening ISIN Account.docx",
         "Board Resolution – Opening ISIN Account",
         "Resolution approving opening of an ISIN for dematerialising the company's shares."),
    ]),
    ("Meetings, Notices & Minutes", "📜", [
        ("AGM - Notice, Directors Report & Annual Return.docx",
         "AGM Pack – Notice, Directors' Report & Annual Return",
         "A combined set covering the AGM notice, directors' report and annual return."),
        ("Notice - Annual General Meeting.docx",
         "Notice – Annual General Meeting",
         "Notice convening the company's annual general meeting."),
        ("Notice - Annual General Meeting (with Directors Report).docx",
         "Notice – AGM (with Directors' Report)",
         "AGM notice that also includes the directors' report."),
        ("Notice and Agenda - Board Meeting.docx",
         "Notice & Agenda – Board Meeting",
         "Notice and agenda for calling a board meeting."),
        ("Explanatory Statement (Section 102).docx",
         "Explanatory Statement (Section 102)",
         "Explanatory statement attached to a meeting notice for special-business items."),
        ("Minutes - First Board Meeting.docx",
         "Minutes – First Board Meeting",
         "Minutes for the first board meeting held after a company is incorporated."),
        ("Minutes - Board Meeting.docx",
         "Minutes – Board Meeting",
         "Standard minutes format for a board meeting."),
        ("Minutes - Audit Committee Meeting.docx",
         "Minutes – Audit Committee Meeting",
         "Minutes format for a meeting of the audit committee."),
        ("Minutes 38TH AGM.docx",
         "Minutes – Annual General Meeting",
         "Minutes format for an annual general meeting of members."),
        ("Compliance Calendar - Listed Company.docx",
         "Compliance Calendar – Listed Company",
         "Year-round calendar of key compliance due dates for a listed company."),
    ]),
    ("Director's Reports", "📑", [
        ("Director's Report (Annual).docx",
         "Director's Report – Annual",
         "Standard annual directors' report for a company."),
        ("Director's Report (Annual) - Alternate.docx",
         "Director's Report – Annual (Alternate)",
         "An alternate drafting of the annual directors' report."),
        ("Director's Report (Annual) - Finalised.docx",
         "Director's Report – Annual (Finalised)",
         "A finalised, ready-to-adapt annual directors' report."),
        ("Director's Report (Annual) - Draft (Variant).docx",
         "Director's Report – Annual (Draft Variant)",
         "A draft variant of the annual directors' report for reference."),
        ("Director's Report (Annual) - Service Company.docx",
         "Director's Report – Service Company",
         "Annual directors' report tailored for a service company."),
        ("Director's Report - Private Company.docx",
         "Director's Report – Private Company",
         "Annual directors' report tailored for a private limited company."),
    ]),
    ("Shares, Certificates & Demat", "📈", [
        ("Form SH-2 - Share Transfer Form.docx",
         "Form SH-2 – Share Transfer Form",
         "Form used to record a transfer of shares from one holder to another."),
        ("Deed of Gift of Shares.docx",
         "Deed of Gift of Shares",
         "Deed gifting shares from one person to another without payment."),
        ("Affidavit - Loss of Share Certificate.docx",
         "Affidavit – Loss of Share Certificate",
         "Sworn affidavit declaring that a share certificate has been lost."),
        ("Declaration of Loss - Share Certificate.docx",
         "Declaration of Loss – Share Certificate",
         "Declaration recording the loss of a share certificate."),
        ("Indemnity Bond - Loss of Share Certificate.docx",
         "Indemnity Bond – Loss of Share Certificate",
         "Indemnity bond given to the company when claiming a duplicate certificate."),
        ("Notice - Lost Share Certificates.docx",
         "Public Notice – Lost Share Certificates",
         "Newspaper-style public notice announcing the loss of share certificates."),
        ("Application - Issuance of Duplicate Share Certificate.docx",
         "Application – Duplicate Share Certificate",
         "Application to the company requesting a duplicate share certificate."),
        ("Request Letter - Duplicate Share Certificate.docx",
         "Request Letter – Duplicate Share Certificate",
         "Request letter to the company for issue of a duplicate share certificate."),
        ("Letter to Company - Duplicate Share Certificate.docx",
         "Letter to Company – Duplicate Share Certificate",
         "Letter from a shareholder asking the company for a duplicate certificate."),
        ("Letter - Issue of Duplicate Share Certificate.docx",
         "Letter – Issue of Duplicate Share Certificate",
         "Covering letter from the company issuing a duplicate share certificate."),
        ("Dematerialisation Checklist.docx",
         "Dematerialisation Checklist",
         "Checklist of documents needed to convert physical shares into demat form."),
        ("Duplicate Share Certificate & Dematerialisation Checklist (2).docx",
         "Duplicate Share Certificate & Demat Checklist",
         "Combined checklist for issuing a duplicate certificate and dematerialising shares."),
        ("Document Checklist - ISIN on NSDL.docx",
         "Document Checklist – ISIN on NSDL",
         "Checklist of papers required to obtain an ISIN with NSDL."),
        ("ISIN Opening Procedure.docx",
         "ISIN Opening Procedure",
         "Step-by-step procedure for opening an ISIN to dematerialise shares."),
    ]),
    ("Agreements & Deeds", "🤝", [
        ("Leave and License Agreement (Commercial).docx",
         "Leave & License Agreement – Commercial",
         "Leave-and-license agreement for commercial premises."),
        ("Leave and License Agreement (Warehouse).docx",
         "Leave & License Agreement – Warehouse",
         "Leave-and-license agreement for a warehouse or godown."),
        ("Letter of Consent from Lessor.docx",
         "Letter of Consent from Lessor",
         "Lessor's consent letter, e.g. for mortgaging or using leased property."),
        ("Deed of Cancellation.docx",
         "Deed of Cancellation",
         "Deed cancelling an earlier agreement by mutual consent."),
    ]),
    ("Declarations & Other Filings", "📝", [
        ("Declaration - GST.docx",
         "Declaration – GST",
         "Declaration relating to the company's GST registration and compliance."),
        ("Declaration for financials.docx",
         "Declaration – Financial Statements",
         "Declaration accompanying the company's financial statements."),
        ("List of Directors with Address.docx",
         "List of Directors with Address",
         "Format listing the company's directors with their DIN and addresses."),
        ("Note - Section 186 Non-Compliance.docx",
         "Note – Section 186 Non-Compliance",
         "Explanatory note on non-compliance under Section 186 (loans & investments)."),
        ("Significance of Name of Proposed Company.docx",
         "Significance of Name – Proposed Company",
         "Note explaining the meaning of a proposed company name for name approval."),
    ]),
]


FORMAT_CATEGORIES = []
FORMATS_BY_SLUG = {}
for _name, _icon, _items in _CATEGORIES:
    _cat = {"name": _name, "icon": _icon, "docs": []}
    for _file, _title, _desc in _items:
        _entry = {"slug": _slug(_file), "file": _file, "title": _title, "desc": _desc}
        if _entry["slug"] in FORMATS_BY_SLUG:
            raise ValueError(f"Duplicate format slug: {_entry['slug']}")
        FORMATS_BY_SLUG[_entry["slug"]] = _entry
        _cat["docs"].append(_entry)
    FORMAT_CATEGORIES.append(_cat)

FORMATS_COUNT = len(FORMATS_BY_SLUG)

# Category metadata used by the admin (upload form dropdown) and the public page.
CATEGORY_ICONS = {name: icon for (name, icon, items) in _CATEGORIES}
CATEGORY_NAMES = [name for (name, icon, items) in _CATEGORIES]
DEFAULT_CATEGORY_ICON = "📄"
