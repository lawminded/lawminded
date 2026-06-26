"""One-off generator: converts the 45 'Downloads/advance blogs' markdown files
into blog_seed2.py (BLOG_ARTICLES_2) in the site's article format
(HTML: <h2>/<h3>/<p>/<ul>/<ol>/<li>/<strong>/<em>/<code>/<blockquote>/<table>).

This batch differs from batch 1: no '*Reading time*' line (computed from word
count), the intro is the lead paragraph before the first '##', and some files
contain markdown tables.

Run from the project root:  python3 scripts_gen_blogs2.py
"""
import os
import re
import html

SRC = "/Users/piyush_kundnani/Downloads/advance blogs"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "blog_seed2.py")

# filename (without .md) -> (category_code, relevant Act)
META = {
    "epf-esi-social-security-code":        ("labour",    "Code on Social Security, 2020"),
    "50-percent-wage-rule":                ("labour",    "Code on Wages, 2019"),
    "gratuity-new-labour-codes":           ("labour",    "Code on Social Security, 2020"),
    "new-labour-codes-explained":          ("labour",    "The Four Labour Codes, 2019-20"),
    "notice-period-termination-settlement":("labour",    "Industrial Relations Code, 2020"),
    "employee-rights-how-to-enforce":      ("labour",    "Indian Labour Law"),

    "service-agreement-guide":             ("contracts", "Indian Contract Act, 1872"),
    "nda-key-clauses":                     ("contracts", "Indian Contract Act, 1872"),
    "how-to-terminate-a-contract":         ("contracts", "Indian Contract Act, 1872"),
    "vendor-supplier-agreement":           ("contracts", "Indian Contract Act, 1872"),
    "force-majeure-clause":                ("contracts", "Indian Contract Act, 1872"),
    "common-contract-mistakes":            ("contracts", "Indian Contract Act, 1872"),
    "msa-vs-sow":                          ("contracts", "Indian Contract Act, 1872"),
    "indemnity-vs-guarantee":              ("contracts", "Indian Contract Act, 1872"),
    "how-to-send-legal-notice":            ("contracts", "Indian Contract Act, 1872"),
    "electronic-signatures-india":         ("contracts", "Information Technology Act, 2000"),

    "income-tax-freelancers":              ("tax",       "Income-tax Act, 1961"),
    "input-tax-credit-gst":                ("tax",       "CGST Act, 2017"),
    "tds-compliance-guide":                ("tax",       "Income-tax Act, 1961"),
    "gst-returns-explained":               ("tax",       "CGST Act, 2017"),

    "property-title-due-diligence":        ("property",  "Transfer of Property Act, 1882"),
    "lease-vs-leave-and-licence":          ("property",  "Transfer of Property Act, 1882"),
    "rent-agreement-registration":         ("property",  "Registration Act, 1908"),
    "registration-act-guide":              ("property",  "Registration Act, 1908"),
    "indian-stamp-act-guide":              ("property",  "Indian Stamp Act, 1899"),
    "power-of-attorney-india":             ("property",  "Powers of Attorney Act, 1882"),
    "how-to-make-a-valid-will":            ("property",  "Indian Succession Act, 1925"),
    "will-vs-gift-deed-vs-trust":          ("property",  "Indian Succession Act, 1925"),

    "influencer-disclosure-misleading-ads":("consumer",  "Consumer Protection Act, 2019"),
    "right-to-information-act-guide":       ("consumer",  "RTI Act, 2005"),
    "consumer-protection-act-2019-guide":   ("consumer",  "Consumer Protection Act, 2019"),

    "competition-act-2002-guide":          ("acts",      "Competition Act, 2002"),
    "constitution-of-india-guide":         ("acts",      "Constitution of India"),
    "law-of-torts-india":                  ("acts",      "Law of Torts"),
    "anticipatory-bail-section-482-bnss":  ("acts",      "BNSS, 2023"),
    "bharatiya-nagarik-suraksha-sanhita-guide": ("acts", "BNSS, 2023"),
    "bharatiya-sakshya-adhiniyam-guide":   ("acts",      "Bharatiya Sakshya Adhiniyam, 2023"),
    "how-to-file-fir-online":              ("acts",      "BNSS, 2023"),
    "code-of-civil-procedure-guide":       ("acts",      "Code of Civil Procedure, 1908"),
    "limitation-act-1963-guide":           ("acts",      "Limitation Act, 1963"),

    "dpdp-act-compliance-guide":           ("updates",   "DPDP Act, 2023"),
    "dpdp-consent-managers":               ("updates",   "DPDP Act, 2023"),
    "dpdp-childrens-data-parental-consent":("updates",   "DPDP Act, 2023"),
    "dpdp-data-breach-notification":       ("updates",   "DPDP Act, 2023"),
    "dpdp-privacy-policy":                 ("updates",   "DPDP Act, 2023"),
}


TOC_TITLES = {"in this guide", "in this article", "contents",
              "table of contents", "on this page", "what's in this guide"}


def _link_sub(m):
    label, url = m.group(1), m.group(2)
    if url.startswith("#"):           # intra-page anchor -> plain text (anchors stripped)
        return label
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (url, label)


def inline(text):
    """Markdown inline -> HTML, escaping any literal & < > first."""
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", _link_sub, text)          # links
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)       # bold
    text = re.sub(r"(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"<em>\1</em>", text)  # italic
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)               # inline code
    return text.strip()


def preprocess(lines):
    """Drop raw-HTML anchor lines (<a id="x"></a>) and horizontal rules (---),
    which this batch sprinkles before headings and between sections."""
    out = []
    for ln in lines:
        s = ln.strip()
        if re.fullmatch(r'<a\s+(?:id|name)=["\'][^"\']*["\']>\s*</a>', s):
            continue
        if re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", s):
            continue
        # Editorial scaffolding that must never reach readers.
        if "[Author name]" in s or re.match(r"\*?\s*Reviewed by\b", s):
            continue
        out.append(ln)
    return out


def is_table_sep(line):
    s = line.strip()
    return ("|" in s) and ("-" in s) and bool(re.fullmatch(r"[\s:|\-]+", s))


def render_table(blk):
    rows = []
    for ln in blk:
        if is_table_sep(ln):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        rows.append(cells)
    if not rows:
        return ""
    head, body = rows[0], rows[1:]
    thead = "<thead><tr>%s</tr></thead>" % "".join("<th>%s</th>" % inline(c) for c in head)
    trs = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in r) for r in body)
    return '<div class="table-wrap"><table class="prose-table">%s<tbody>%s</tbody></table></div>' % (thead, trs)


def to_html_and_summary(body_lines):
    body_lines = preprocess(body_lines)
    blocks, cur = [], []
    for ln in body_lines:
        if ln.strip() == "":
            if cur:
                blocks.append(cur); cur = []
        else:
            cur.append(ln.rstrip("\n"))
    if cur:
        blocks.append(cur)

    parts, intro_text, seen_heading = [], None, False
    skip_next_list = False
    for blk in blocks:
        first = blk[0].strip()
        is_list = all(re.match(r"^\s*[-*]\s+", l) for l in blk)
        if skip_next_list and is_list:        # drop the TOC link list
            skip_next_list = False
            continue
        skip_next_list = False
        if first.startswith("## "):
            seen_heading = True
            htext = first[3:].strip()
            if htext.lower() in TOC_TITLES:   # drop redundant "In this guide" TOC
                skip_next_list = True
                continue
            parts.append("<h2>%s</h2>" % inline(htext))
        elif first.startswith("### "):
            seen_heading = True
            parts.append("<h3>%s</h3>" % inline(first[4:].strip()))
        elif len(blk) >= 2 and "|" in blk[0] and is_table_sep(blk[1]):
            parts.append(render_table(blk))
        elif all(re.match(r"^\s*[-*]\s+", l) for l in blk):
            items = "".join("<li>%s</li>" % inline(re.sub(r"^\s*[-*]\s+", "", l)) for l in blk)
            parts.append("<ul>%s</ul>" % items)
        elif all(re.match(r"^\s*\d+\.\s+", l) for l in blk):
            items = "".join("<li>%s</li>" % inline(re.sub(r"^\s*\d+\.\s+", "", l)) for l in blk)
            parts.append("<ol>%s</ol>" % items)
        elif all(l.lstrip().startswith(">") for l in blk):
            txt = " ".join(re.sub(r"^\s*>\s?", "", l) for l in blk)
            parts.append("<blockquote>%s</blockquote>" % inline(txt))
        else:
            txt = " ".join(l.strip() for l in blk)
            parts.append("<p>%s</p>" % inline(txt))
            if intro_text is None and not seen_heading:   # lead paragraph = summary
                intro_text = txt

    base = re.sub(r"[*_`>]", "", intro_text or "").strip()
    summary = ""
    for sent in re.split(r"(?<=[.!?])\s+", base):
        if len(summary) + len(sent) > 200 and summary:
            break
        summary = (summary + " " + sent).strip()
    summary = summary[:240].strip()
    return "".join(parts), summary


def main():
    out = ["# Auto-generated by scripts_gen_blogs2.py - 45 advanced blog articles.",
           "# Format: (title, slug, category, act, read_time, summary, content)",
           "BLOG_ARTICLES_2 = ["]
    counts = {}
    for slug in sorted(META):
        cat, act = META[slug]
        path = os.path.join(SRC, slug + ".md")
        with open(path, encoding="utf-8") as f:
            text = f.read()
        text = re.sub(r"<!--.*?-->", "", text, flags=re.S)   # drop "do not publish" comments
        lines = text.splitlines(keepends=True)
        title, body = None, []
        for ln in lines:
            s = ln.strip()
            if title is None and s.startswith("# "):
                title = s[2:].strip(); continue
            body.append(ln)
        content, summary = to_html_and_summary(body)
        words = len(re.findall(r"\w+", " ".join(body)))
        read_time = "%d min read" % max(5, round(words / 200))
        out.append("    %r," % ((title, slug, cat, act, read_time, summary, content),))
        counts[cat] = counts.get(cat, 0) + 1
        print(f"{slug:40} cat={cat:9} rt={read_time:11} sum={len(summary):3}c html={len(content):6}c")
    out.append("]")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print("\nPer-category:", counts, " total:", sum(counts.values()))
    print("Wrote", OUT)


if __name__ == "__main__":
    main()
