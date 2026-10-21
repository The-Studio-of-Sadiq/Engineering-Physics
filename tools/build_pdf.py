"""
Compile the whole repository into one PDF: Engineering-Physics-Top-Down.pdf.

Order: README, Master Map, Chapters 0-21, Epilogue, worked examples,
Appendices A-F, then References, CONTRIBUTING, MCP.md and the MCP server
README. Figures are embedded from FIGURES/, math is typeset with KaTeX, and
headless Chrome (or Edge) prints the result to A4.

One-time setup (from the repo root):

    pip install markdown-it-py mdit-py-plugins
    npm install --prefix tools

Build:

    python tools/build_pdf.py            # writes Engineering-Physics-Top-Down.pdf
    python tools/build_pdf.py --check    # also report math KaTeX can't typeset
    python tools/build_pdf.py --html-only

Set CHROME=/path/to/chrome if the browser isn't found automatically.
The intermediate HTML goes to tools/build/ (git-ignored).
"""

from __future__ import annotations

import argparse
import html
import os
import pathlib
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote

from markdown_it import MarkdownIt
from mdit_py_plugins.anchors import anchors_plugin
from mdit_py_plugins.dollarmath import dollarmath_plugin

TOOLS = pathlib.Path(__file__).resolve().parent
ROOT = TOOLS.parent
KATEX = TOOLS / "node_modules" / "katex" / "dist"
BUILD = TOOLS / "build"
PDF_NAME = "Engineering-Physics-Top-Down.pdf"

PARTS = [
    ("Front matter", ["README.md", "METADATA/00 Map.md"]),
    ("Chapters", [f"CHAPTERS/CHAPTER {i}.md" for i in range(22)]),
    ("Epilogue", ["METADATA/EPILOGUE.md"]),
    ("Worked examples", ["EXAMPLES/README.md"] + sorted(
        p.relative_to(ROOT).as_posix() for p in (ROOT / "EXAMPLES").glob("0*.md"))),
    ("Appendices", [f"APPENDIX/APPENDIX {x}.md" for x in "ABCDEF"]),
    ("Back matter", ["REFERENCES.md", "CONTRIBUTING.md", "MCP.md", "mcp-server/README.md"]),
]

# --------------------------------------------------------------------------
# Markdown -> HTML
# --------------------------------------------------------------------------


def doc_id(rel: str) -> str:
    return "doc-" + re.sub(r"[^a-z0-9]+", "-", rel.lower()).strip("-")


def gh_slug(text: str) -> str:
    """GitHub's heading anchor: one hyphen per space, so "A — B" -> "a--b"."""
    return re.sub(r"[^\w\s-]", "", text.strip().lower()).replace(" ", "-")


def title_of(md: str, rel: str) -> str:
    m = re.search(r"^#\s+(.+)$", md, re.M)
    return re.sub(r"[*_`]", "", m.group(1)).strip() if m else rel


_CALLOUT = re.compile(r"^(>\s*)\[!(\w+)\][+-]?\s*(.*)$", re.M)


def convert_callouts(md: str) -> str:
    """Obsidian "> [!note] Title" -> a bold label inside the blockquote."""
    return _CALLOUT.sub(
        lambda m: f"{m.group(1)}**{m.group(2).capitalize()}{': ' + m.group(3) if m.group(3) else ''}**",
        md,
    )


def split_display_pairs(md: str) -> str:
    """'$$a$$ $$b$$' on a line that starts with $$ is two display equations,
    as GitHub renders it; mid-paragraph pairs are left to render inline."""
    return re.sub(r"(?m)^(\s*\$\$.*)$",
                  lambda m: re.sub(r"\$\$[ \t]+\$\$", "$$\n\n$$", m.group(1)), md)


def rewrite_links(md: str, rel: str, known: set[str]) -> str:
    """Images -> absolute file URIs; links to other documents -> in-PDF
    anchors; links to anything not in the PDF -> plain text. Fenced code
    blocks (quoted examples) are left untouched."""
    src_dir = (ROOT / rel).parent

    def fix(m):
        bang, text, target = m.group(1), m.group(2), m.group(3)
        if target.startswith(("http://", "https://", "mailto:")):
            return m.group(0)
        path, _, anchor = target.partition("#")
        if bang:
            return f"![{text}]({(src_dir / unquote(path)).resolve().as_uri()})"
        if not path:
            return f"[{text}](#{doc_id(rel)}--{anchor})"
        try:
            trel = (src_dir / unquote(path)).resolve().relative_to(ROOT).as_posix()
        except ValueError:
            return text
        if trel in known:
            return f"[{text}](#{doc_id(trel)}{'--' + anchor if anchor else ''})"
        return text

    parts = re.split(r"(?ms)(^[ \t]*```.*?^[ \t]*```[ \t]*$)", md)
    return "".join(p if p.lstrip(" \t").startswith("```") else
                   re.sub(r"(!?)\[([^\]]*)\]\(([^)\s]+)\)", fix, p) for p in parts)


def make_md(prefix: str) -> MarkdownIt:
    md = MarkdownIt("commonmark", {"html": True}).enable("table").enable("strikethrough")
    md.validateLink = lambda url: True  # figures are local file: URIs (trusted repo content)
    md.use(dollarmath_plugin, allow_space=True, allow_digits=True, double_inline=True)
    md.use(anchors_plugin, min_level=1, max_level=6,
           slug_func=lambda t: f"{prefix}--{gh_slug(t)}")

    def math_inline(self, tokens, idx, options, env):
        return f'<span class="math-i">{html.escape(tokens[idx].content)}</span>'

    def math_block(self, tokens, idx, options, env):
        return f'<div class="math-d">{html.escape(tokens[idx].content)}</div>\n'

    md.add_render_rule("math_inline", math_inline)
    md.add_render_rule("math_inline_double", math_block)
    md.add_render_rule("math_block", math_block)
    md.add_render_rule("math_block_label", math_block)
    return md


STYLE = """
@page { size: A4; margin: 18mm 16mm 18mm 16mm; }
body { font-family: "Georgia", "Cambria", serif; font-size: 10.5pt; line-height: 1.45; color: #1a1a1a; }
h1 { font-size: 20pt; margin: 0 0 6pt; } h2 { font-size: 14pt; margin-top: 16pt; }
h3 { font-size: 12pt; } h4,h5,h6 { font-size: 11pt; }
h1,h2,h3,h4 { font-family: "Segoe UI", Arial, sans-serif; color: #12355b; break-after: avoid; }
.doc { break-before: page; }
.src { font: 8pt "Segoe UI", Arial, sans-serif; color: #888; margin-bottom: 4pt; }
p, li { orphans: 3; widows: 3; }
img { display: block; max-width: 100%; max-height: 190mm; margin: 8pt auto 2pt; break-inside: avoid; }
pre { font: 8pt Consolas, monospace; background: #f5f5f5; padding: 6pt; white-space: pre-wrap; break-inside: avoid; }
code { font: 8.5pt Consolas, monospace; background: #f3f3f3; padding: 0 2px; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; margin: 6pt 0; font-size: 9pt; width: 100%; }
th, td { border: 1px solid #ccc; padding: 3pt 5pt; vertical-align: top; }
th { background: #eef2f7; } tr { break-inside: avoid; }
blockquote { margin: 6pt 0; padding: 4pt 10pt; border-left: 3px solid #12355b; background: #f6f8fb; }
.math-d { margin: 6pt 0; overflow: hidden; break-inside: avoid; }
.katex-display { margin: 0; } .katex { font-size: 1.05em; }
.katex-error { color: #b00; font-family: Consolas, monospace; font-size: 8pt; }
a { color: #12355b; text-decoration: none; }
.cover { height: 240mm; display: flex; flex-direction: column; justify-content: center; text-align: center; }
.cover h1 { font-size: 32pt; } .cover p { font-size: 13pt; color: #444; }
.toc { break-before: page; } .toc ol { list-style: none; padding-left: 12pt; }
.toc-part { font: bold 11pt "Segoe UI", Arial, sans-serif; margin-top: 8pt; }
.toc-part li { font: normal 10pt Georgia, serif; margin: 1pt 0; }
"""

# KaTeX lacks \dddot; a middle dot inside \text{...} (units like N·m) is
# math-only in KaTeX, so it is moved out of the \text group before rendering.
SCRIPT = r"""
var bad = 0;
var macros = {"\\dddot": "\\overset{\\cdot\\cdot\\cdot}{#1}"};
function src(el) {
  return el.textContent.replace(/\\text\{([^{}]*)\}/g, function(m, c) {
    return "\\text{" + c.replace(/\u00b7/g, "}\\cdot\\text{") + "}";
  });
}
function tex(el, display) {
  try { katex.render(src(el), el, {displayMode: display, throwOnError: true, strict: false, trust: true, macros: macros}); }
  catch (e) { bad++; console.log("KATEX " + e.message.slice(0, 160));
              katex.render(src(el), el, {displayMode: display, throwOnError: false, strict: false, macros: macros}); }
}
document.querySelectorAll(".math-i").forEach(function(e) { tex(e, false); });
document.querySelectorAll(".math-d").forEach(function(e) { tex(e, true); });
document.body.setAttribute("data-katex-errors", bad);
"""


def build_html(out: pathlib.Path) -> int:
    known = {f for _, files in PARTS for f in files if (ROOT / f).exists()}
    toc, body = [], []
    for part, files in PARTS:
        toc.append(f'<li class="toc-part">{html.escape(part)}<ol>')
        for rel in files:
            if rel not in known:
                continue
            raw = (ROOT / rel).read_text(encoding="utf-8")
            raw = rewrite_links(convert_callouts(split_display_pairs(raw)), rel, known)
            did = doc_id(rel)
            toc.append(f'<li><a href="#{did}">{html.escape(title_of(raw, rel))}</a></li>')
            body.append(f'<section class="doc" id="{did}"><div class="src">{html.escape(rel)}</div>\n'
                        f"{make_md(did).render(raw)}</section>")
        toc.append("</ol></li>")

    out.write_text(f"""<!doctype html><html><head><meta charset="utf-8">
<title>Engineering Physics: Top Down</title>
<link rel="stylesheet" href="{(KATEX / 'katex.min.css').as_uri()}">
<style>{STYLE}</style></head><body>
<div class="cover"><h1>Engineering Physics: Top Down</h1>
<p>A conceptual descent from fundamental fields to engineering systems</p>
<p>Chapters 0–21 · Epilogue · Worked Examples · Appendices A–F · References</p>
<p style="font-size:10pt">© 2026 Golam Kuadir Khan Prince · CC BY 4.0</p></div>
<nav class="toc"><h1>Contents</h1><ol>{''.join(toc)}</ol></nav>
{''.join(body)}
<script src="{(KATEX / 'katex.min.js').as_uri()}"></script>
<script>{SCRIPT}</script></body></html>""", encoding="utf-8")
    return len(body)


# --------------------------------------------------------------------------
# HTML -> PDF
# --------------------------------------------------------------------------


def find_browser() -> str:
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    for name in ("google-chrome", "chromium", "chromium-browser", "chrome", "msedge"):
        if shutil.which(name):
            return shutil.which(name)
    sys.exit("No Chrome/Chromium/Edge found; set CHROME=/path/to/browser")


def browser(chrome: str, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [chrome, "--headless=new", "--disable-gpu", "--allow-file-access-from-files",
         "--virtual-time-budget=90000", *args],
        capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=900,
    )


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out", default=str(ROOT / PDF_NAME), help="PDF path (default: repo root)")
    ap.add_argument("--check", action="store_true", help="report math KaTeX cannot typeset")
    ap.add_argument("--html-only", action="store_true", help="stop after writing the HTML")
    args = ap.parse_args()

    if not (KATEX / "katex.min.js").exists():
        sys.exit("KaTeX not installed: run  npm install --prefix tools")
    BUILD.mkdir(exist_ok=True)
    page = BUILD / "book.html"
    n = build_html(page)
    print(f"wrote {page.relative_to(ROOT)} ({n} documents)")
    if args.html_only:
        return

    chrome = find_browser()
    if args.check:
        res = browser(chrome, "--enable-logging=stderr", "--v=0", "--dump-dom", page.as_uri())
        m = re.search(r'data-katex-errors="(\d+)"', res.stdout)
        errors = re.findall(r"KATEX ([^\"]+?)\", source", res.stderr)
        print(f"KaTeX errors: {m.group(1) if m else 'unknown'}")
        for e in errors[:20]:
            print(f"  {e}")

    out = pathlib.Path(args.out).resolve()
    res = browser(chrome, "--no-pdf-header-footer", f"--print-to-pdf={out}", page.as_uri())
    if not out.exists():
        sys.exit(f"PDF was not written:\n{res.stderr[-2000:]}")
    print(f"wrote {out.name} ({out.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
