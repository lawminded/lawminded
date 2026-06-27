"""One-off generator: converts the 36 'Downloads/all new compliance blogs'
markdown files into blog_seed3.py (BLOG_ARTICLES_3) in the site's article format
(HTML: <h2>/<h3>/<p>/<ul>/<ol>/<li>/<strong>/<em>/<code>/<blockquote>/<table>).

This batch (corporate-compliance guides) differs from earlier batches:
  * 29 files have an SEO frontmatter block (--- ... ---) carrying a hand-written
    'Title tag', 'Meta description' and 'Slug' which we use directly.
  * 7 files start straight at a clean '# H1' (no frontmatter) — H1 is the title,
    slug = filename, summary = auto-extracted lead paragraph.
  * Headings carry '{#anchor}' suffixes and a manual '## On this page' list — both
    dropped (the site's JS auto-builds the TOC from <h2> headings).
  * Callouts use multi-line blockquotes, sometimes with internal '-' bullets.

All 36 are Corporate Compliance ('corp'). Run from project root:
    python3 scripts_gen_blogs3.py
"""
import os
import re
import html
import glob

SRC = "/Users/piyush_kundnani/Downloads/all new compliance blogs"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "blog_seed3.py")

# Per-slug Act override; everything else defaults to "Companies Act 2013".
ACT_OVERRIDE = {
    "sebi-lodr-explained":               "SEBI LODR, 2015",
    "sebi-pit-insider-trading-explained": "SEBI (PIT) Regulations, 2015",
}
DEFAULT_ACT = "Companies Act 2013"
CATEGORY = "corp"   # all of this batch is Corporate Compliance

TOC_TITLES = {"in this guide", "in this article", "contents",
              "table of contents", "on this page", "what's in this guide"}


def _link_sub(m):
    label, url = m.group(1), m.group(2)
    if url.startswith("#"):            # intra-page anchor -> plain text
        return label
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (url, label)


def inline(text):
    """Markdown inline -> HTML, escaping any literal & < > first."""
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", _link_sub, text)            # links
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)         # bold
    text = re.sub(r"(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"<em>\1</em>", text)  # italic
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)                 # inline code
    return text.strip()


def strip_anchor(htext):
    return re.sub(r"\s*\{#[^}]+\}\s*$", "", htext).strip()


def preprocess(lines):
    """Drop raw-HTML anchor lines, horizontal rules, and editorial scaffolding."""
    out = []
    for ln in lines:
        s = ln.strip()
        if re.fullmatch(r'<a\s+(?:id|name)=["\'][^"\']*["\']>\s*</a>', s):
            continue
        if re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", s):
            continue
        if "[REPLACE" in s or "[Author name]" in s or re.match(r"\*?\s*Reviewed by\b", s):
            continue
        if re.match(r"^(Author|Last reviewed|Title tag|Meta description|Slug|Focus keyword|Secondary)\s*:", s):
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


def render_blockquote(blk):
    """Multi-line blockquote -> <blockquote> with paragraphs and any internal
    '-' bullets preserved as a <ul>, so 'BOTTOM LINE' callouts read cleanly."""
    stripped = [re.sub(r"^\s*>\s?", "", l) for l in blk]
    parts, bullets = [], []
    def flush():
        if bullets:
            parts.append("<ul>%s</ul>" % "".join("<li>%s</li>" % inline(b) for b in bullets))
            bullets.clear()
    for line in stripped:
        s = line.strip()
        if not s:
            flush(); continue
        mb = re.match(r"^[-*]\s+(.*)$", s)
        if mb:
            bullets.append(mb.group(1))
        else:
            flush()
            parts.append("<p>%s</p>" % inline(s))
    flush()
    return "<blockquote>%s</blockquote>" % "".join(parts)


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
        is_list = all(re.match(r"^\s*(?:[-*]|\d+\.)\s+", l) for l in blk)
        if skip_next_list and is_list:        # drop the TOC link list (bullet or numbered)
            skip_next_list = False
            continue
        skip_next_list = False
        if first.startswith("## "):
            seen_heading = True
            htext = strip_anchor(first[3:].strip())
            if htext.lower() in TOC_TITLES:    # drop redundant "On this page" TOC heading
                skip_next_list = True
                continue
            parts.append("<h2>%s</h2>" % inline(htext))
        elif first.startswith("### "):
            seen_heading = True
            parts.append("<h3>%s</h3>" % inline(strip_anchor(first[4:].strip())))
        elif first.startswith("#### "):
            seen_heading = True
            parts.append("<h4>%s</h4>" % inline(strip_anchor(first[5:].strip())))
        elif len(blk) >= 2 and "|" in blk[0] and is_table_sep(blk[1]):
            parts.append(render_table(blk))
        elif all(l.lstrip().startswith(">") for l in blk):
            parts.append(render_blockquote(blk))
        elif all(re.match(r"^\s*[-*]\s+", l) for l in blk):
            items = "".join("<li>%s</li>" % inline(re.sub(r"^\s*[-*]\s+", "", l)) for l in blk)
            parts.append("<ul>%s</ul>" % items)
        elif all(re.match(r"^\s*\d+\.\s+", l) for l in blk):
            items = "".join("<li>%s</li>" % inline(re.sub(r"^\s*\d+\.\s+", "", l)) for l in blk)
            parts.append("<ol>%s</ol>" % items)
        else:
            txt = " ".join(l.strip() for l in blk)
            parts.append("<p>%s</p>" % inline(txt))
            if intro_text is None and not seen_heading:   # lead paragraph = summary source
                intro_text = txt

    base = re.sub(r"[*_`>]", "", intro_text or "").strip()
    base = re.sub(r"\s+", " ", base)
    if len(base) <= 240:
        summary = base
    else:
        cut = base[:240]
        summary = cut[:cut.rfind(" ")].rstrip(" ,;:—-") + "…"
    return "".join(parts), summary


def parse_file(path):
    text = open(path, encoding="utf-8").read()
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    fm_title = fm_desc = fm_slug = None
    m = re.match(r"\s*---\s*\n(.*?)\n---\s*\n", text, re.S)
    if m:
        fm = m.group(1)
        def field(name):
            mm = re.search(rf"^{name}\s*:\s*(.+)$", fm, re.M | re.I)
            return mm.group(1).strip() if mm else None
        fm_title = field("Title tag")
        fm_desc = field("Meta description")
        fm_slug = field("Slug")
        text = text[m.end():]

    lines = text.splitlines(keepends=True)
    h1, body = None, []
    for ln in lines:
        s = ln.strip()
        if h1 is None and s.startswith("# "):
            h1 = s[2:].strip()
            continue
        body.append(ln)

    title = (fm_title or h1 or "").strip().strip('"')
    content, auto_summary = to_html_and_summary(body)
    summary = (fm_desc or auto_summary or "").strip()
    summary = re.sub(r"\s+", " ", summary)[:240].strip()
    words = len(re.findall(r"\w+", " ".join(body)))
    read_time = "%d min read" % max(5, round(words / 200))
    return title, summary, content, read_time, fm_slug


def main():
    out = ["# Auto-generated by scripts_gen_blogs3.py - 36 corporate-compliance blog articles.",
           "# Format: (title, slug, category, act, read_time, summary, content)",
           "BLOG_ARTICLES_3 = ["]
    seen = set()
    for path in sorted(glob.glob(os.path.join(SRC, "*.md"))):
        fname = os.path.splitext(os.path.basename(path))[0]
        title, summary, content, read_time, fm_slug = parse_file(path)
        slug = (fm_slug or fname).strip()
        slug = re.sub(r"[^a-z0-9-]", "", slug.lower().replace(" ", "-"))
        if slug in seen:
            base = slug; i = 1
            while slug in seen:
                slug = f"{base}-{i}"; i += 1
        seen.add(slug)
        act = ACT_OVERRIDE.get(fname, DEFAULT_ACT)
        out.append("    %r," % ((title, slug, CATEGORY, act, read_time, summary, content),))
        print(f"{fname:42} slug={slug:38} rt={read_time:11} sum={len(summary):3}c html={len(content):6}c")
    out.append("]")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print(f"\nWrote {OUT}  ({len(seen)} articles)")


if __name__ == "__main__":
    main()
