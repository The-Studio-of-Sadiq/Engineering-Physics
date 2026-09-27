"""
Engineering Physics — MCP Server (deterministic tooling layer)
Repository: The-Studio-of-Sadiq/Engineering-Physics

WHAT THIS IS
------------
This server implements the *deterministic* half of the architecture
described in the repo's own MCP.md, section 16:

                    Engineering Physics
                    Knowledge Repository
                             |
          +------------------+------------------+
          |                  |                  |
    Deterministic       Knowledge          AI reasoning
      validators        graph / MCP           layer
          |                  |                  |
    syntax/math          model ledger      physics audit
    link checks           references       synthesis
    numerical checks     dependencies    contradiction scan

This file is the left+middle columns. It fetches real files from the
live GitHub repo (no local clone required) and runs mechanical checks:
heading structure, links/anchors, fence balance, table shape, LaTeX
delimiter balance, and forbidden numbered-equation syntax. It also
parses the repo's "Model Ledger" convention (MCP.md section 7) into
structured records and assembles a reduction graph from them.

WHAT THIS DELIBERATELY IS NOT
------------------------------
MCP.md section 15 defines audit modes ORIENT, AUDIT_PHYSICS, AUDIT_MATH,
AUDIT_REFERENCES, AUDIT_STRUCTURE, TRACE_MODEL, TRACE_CLAIM, GRAPH.
Of these:

  - AUDIT_STRUCTURE  -> implemented here (audit_structure)
  - ORIENT           -> implemented here (orient)
  - TRACE_MODEL      -> implemented here (trace_model), built ONLY from
                        what Model Ledger blocks literally state
  - GRAPH            -> partially implemented (build_reduction_graph +
                        get_epistemic_tag_index); see docstrings for
                        exactly what is and isn't inferred
  - AUDIT_PHYSICS, AUDIT_MATH, AUDIT_REFERENCES, TRACE_CLAIM
                     -> NOT implemented. Judging whether an equation is
                        dimensionally/physically correct, whether a
                        citation supports a claim, or what a "stronger/
                        weaker wording" would be requires the physics-
                        and-language judgment MCP.md assigns to the "AI
                        reasoning layer" (the calling LLM). Hard-coding
                        that here would silently strengthen or weaken
                        claims without evidence -- exactly what MCP.md
                        section 8 forbids. Use get_file()/list_repo_
                        structure() to pull the text, then reason over
                        it directly.

This server never writes to the repository. There is no commit/PR/
push tool. That matches MCP.md section 17 (Safe Write Policy) and the
machine-readable metadata in section 23: `autonomous_writes: false`.

CONFIGURATION (environment variables)
--------------------------------------
EP_REPO_OWNER   default "The-Studio-of-Sadiq"
EP_REPO_NAME    default "Engineering-Physics"
EP_REPO_BRANCH  default "main"
GITHUB_TOKEN    optional. Unauthenticated GitHub API calls are rate-limited
                to 60/hour; a classic PAT with public_repo (read) scope
                raises that to 5000/hour. Raw file fetches (raw.githubusercontent.com)
                are NOT rate-limited by this token but benefit from it
                being present for the tree-listing call.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from typing import Any, Optional
from urllib.parse import unquote

import httpx
from mcp.server.mcpserver import MCPServer

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

GITHUB_OWNER = os.environ.get("EP_REPO_OWNER", "The-Studio-of-Sadiq")
GITHUB_REPO = os.environ.get("EP_REPO_NAME", "Engineering-Physics")
GITHUB_BRANCH = os.environ.get("EP_REPO_BRANCH", "main")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

GITHUB_API = "https://api.github.com"
RAW_BASE = f"https://raw.githubusercontent.com/{GITHUB_OWNER}/{GITHUB_REPO}/{GITHUB_BRANCH}"

_API_HEADERS = {"Accept": "application/vnd.github+json"}
if GITHUB_TOKEN:
    _API_HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"

mcp = MCPServer("engineering-physics")

# Process-lifetime caches. A restart clears them; there is no
# invalidation-on-push, so long-running processes should be restarted
# after known upstream edits if freshness matters.
_tree_cache: dict[str, Any] = {}
_file_cache: dict[str, str] = {}

ORIENT_FILES = ["README.md", "MCP.md", "METADATA/00 Map.md", "AUTHORING.md"]

# Recognized Model Ledger field names (MCP.md section 7's canonical list,
# plus "Model"/"Reduction" which is what the worked EXAMPLE in that same
# section actually uses -- both forms appear in the repo).
LEDGER_FIELDS = [
    "Level",
    "Parent theory",
    "Origin",
    "Approximation",
    "Reduction",
    "Assumptions",
    "Model type",
    "Model",
    "Validity regime",
    "Validity",
    "Failure regime",
    "Failure",
    "Next reduced model",
]

_LEDGER_FIELD_RE = re.compile(
    r"^(" + "|".join(re.escape(f) for f in LEDGER_FIELDS) + r")\s*:\s*(.*)$",
    re.IGNORECASE,
)

_HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$", re.MULTILINE)
_MD_LINK_RE = re.compile(r'(?<!!)\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
_FENCE_RE = re.compile(r"^(```|~~~)", re.MULTILINE)
_NUMBERED_EQ_RE = re.compile(
    r"\\begin\{(equation|align|eqnarray|gather|multline)\*?\}|\\tag\{[^}]*\}"
)
_TABLE_SEP_RE = re.compile(r"^\s*\|?[\s:|-]+\|[\s:|-]*\|?\s*$")


# --------------------------------------------------------------------------
# GitHub access helpers
# --------------------------------------------------------------------------


async def _fetch_tree() -> list[dict[str, Any]]:
    """Fetch and cache the full recursive blob tree for the configured branch."""
    if "tree" in _tree_cache:
        return _tree_cache["tree"]
    url = f"{GITHUB_API}/repos/{GITHUB_OWNER}/{GITHUB_REPO}/git/trees/{GITHUB_BRANCH}?recursive=1"
    async with httpx.AsyncClient(timeout=20.0) as client:
        resp = await client.get(url, headers=_API_HEADERS)
        resp.raise_for_status()
        data = resp.json()
    tree = [item for item in data.get("tree", []) if item.get("type") == "blob"]
    _tree_cache["tree"] = tree
    _tree_cache["truncated"] = bool(data.get("truncated", False))
    return tree


async def _fetch_file(path: str) -> str:
    """Fetch and cache raw text content of `path` from the configured branch."""
    if path in _file_cache:
        return _file_cache[path]
    url = f"{RAW_BASE}/{path}"
    async with httpx.AsyncClient(timeout=20.0) as client:
        resp = await client.get(url)
        if resp.status_code == 404:
            raise FileNotFoundError(f"'{path}' not found on branch '{GITHUB_BRANCH}'")
        resp.raise_for_status()
    _file_cache[path] = resp.text
    return resp.text


async def _all_markdown_paths() -> list[str]:
    tree = await _fetch_tree()
    return sorted(item["path"] for item in tree if item["path"].lower().endswith(".md"))


def _github_slugify(heading_text: str, seen: dict[str, int]) -> str:
    """Reproduce GitHub's heading-to-anchor slug algorithm closely enough
    for anchor-existence checks: lowercase, strip characters other than
    word chars/spaces/hyphens, spaces -> hyphens, de-duplicate with a
    numeric suffix on repeats."""
    slug = re.sub(r"[^\w\s-]", "", heading_text.strip().lower())
    slug = re.sub(r"\s+", "-", slug)
    if slug in seen:
        seen[slug] += 1
        return f"{slug}-{seen[slug]}"
    seen[slug] = 0
    return slug


# --------------------------------------------------------------------------
# Tool: orient
# --------------------------------------------------------------------------


@mcp.tool()
async def orient() -> str:
    """Return the project's thesis, repository map, layer/bridge
    architecture, and epistemic rules (MCP.md's `ORIENT` mode), by
    reading README.md, MCP.md, METADATA/00 Map.md, and AUTHORING.md
    live from the repository. Always reflects current source, never a
    cached summary -- if a file has moved or been renamed, that shows
    up here as "not found" rather than stale content."""
    parts = []
    for path in ORIENT_FILES:
        try:
            content = await _fetch_file(path)
            parts.append(f"## {path}\n\n{content}")
        except FileNotFoundError:
            parts.append(f"## {path}\n\n[not found at this path on branch '{GITHUB_BRANCH}']")
    return "\n\n---\n\n".join(parts)


# --------------------------------------------------------------------------
# Tool: list_repo_structure / get_file
# --------------------------------------------------------------------------


@mcp.tool()
async def list_repo_structure(path_prefix: str = "") -> str:
    """List every file in the repository (optionally filtered to those
    whose path starts with `path_prefix`, e.g. "CHAPTERS/" or
    "EXAMPLES/"). Returns one path per line, sorted. Use this before
    get_file() to find the exact path/casing GitHub has on record --
    chapter filenames contain spaces (e.g. "CHAPTER 12.md") and are
    easy to mistype."""
    tree = await _fetch_tree()
    paths = sorted(item["path"] for item in tree if item["path"].startswith(path_prefix))
    note = ""
    if _tree_cache.get("truncated"):
        note = (
            "\n\n[NOTE: GitHub truncated this tree response because the repo "
            "exceeds the API's single-response limit; some paths may be "
            "missing. Narrow path_prefix and retry, or use the GitHub API's "
            "paginated contents endpoint for the affected directory.]"
        )
    return "\n".join(paths) + note


@mcp.tool()
async def get_file(path: str) -> str:
    """Fetch the raw text content of one file at `path` (e.g.
    "CHAPTERS/CHAPTER 3.md" or "METADATA/00 Map.md"), exactly as it is
    on the configured branch. Use list_repo_structure() first if
    unsure of the exact path."""
    try:
        return await _fetch_file(path)
    except FileNotFoundError as e:
        return f"ERROR: {e}"


# --------------------------------------------------------------------------
# Tool: audit_structure
# --------------------------------------------------------------------------


@dataclass
class StructureReport:
    path: str
    heading_issues: list[str] = field(default_factory=list)
    link_issues: list[str] = field(default_factory=list)
    fence_issues: list[str] = field(default_factory=list)
    equation_issues: list[str] = field(default_factory=list)
    table_issues: list[str] = field(default_factory=list)

    def is_clean(self) -> bool:
        return not (
            self.heading_issues
            or self.link_issues
            or self.fence_issues
            or self.equation_issues
            or self.table_issues
        )

    def render(self) -> str:
        if self.is_clean():
            return f"### {self.path}\nNo structural issues found."
        lines = [f"### {self.path}"]
        for label, issues in (
            ("Headings", self.heading_issues),
            ("Links/anchors", self.link_issues),
            ("Code/math fences", self.fence_issues),
            ("Equation delimiters/numbering", self.equation_issues),
            ("Tables", self.table_issues),
        ):
            if issues:
                lines.append(f"- **{label}**:")
                lines.extend(f"  - {i}" for i in issues)
        return "\n".join(lines)


def _check_headings(text: str) -> list[str]:
    issues = []
    prev_level = 0
    for m in _HEADING_RE.finditer(text):
        level = len(m.group(1))
        title = m.group(2).strip()
        if prev_level and level > prev_level + 1:
            issues.append(
                f"heading level jumps from H{prev_level} to H{level} at "
                f'"{title}" (skips a level)'
            )
        prev_level = level
    return issues


async def _check_links(text: str, source_path: str, all_paths: set[str]) -> list[str]:
    issues = []
    # anchors available within THIS file, for same-file "#anchor" links
    own_seen: dict[str, int] = {}
    own_anchors = {
        _github_slugify(m.group(2), own_seen) for m in _HEADING_RE.finditer(text)
    }
    source_dir = source_path.rsplit("/", 1)[0] if "/" in source_path else ""

    for m in _MD_LINK_RE.finditer(text):
        target = m.group(2)
        if target.startswith(("http://", "https://", "mailto:")):
            continue  # external links: existence not checked (no crawling)
        file_part, _, anchor = target.partition("#")
        file_part = unquote(file_part)
        if not file_part:
            # pure "#anchor" link into this same file
            if anchor and anchor not in own_anchors:
                issues.append(f'link "#{anchor}" has no matching heading in this file')
            continue
        # resolve relative path against this file's directory
        if file_part.startswith("/"):
            resolved = file_part.lstrip("/")
        elif source_dir:
            resolved = f"{source_dir}/{file_part}"
        else:
            resolved = file_part
        # normalize any ./ and ../
        parts: list[str] = []
        for seg in resolved.split("/"):
            if seg in ("", "."):
                continue
            if seg == "..":
                if parts:
                    parts.pop()
                continue
            parts.append(seg)
        resolved = "/".join(parts)
        if resolved not in all_paths:
            issues.append(f'link target "{target}" -> resolved path "{resolved}" not found in repo')
        elif anchor:
            # can't cheaply verify anchors in OTHER files without fetching
            # them all; flag as unverified rather than silently passing.
            issues.append(
                f'link "{target}" points at anchor "#{anchor}" in another file '
                f"(target file exists; anchor not verified -- fetch and check manually)"
            )
    return issues


def _check_fences(text: str) -> list[str]:
    issues = []
    fences = _FENCE_RE.findall(text)
    if len(fences) % 2 != 0:
        issues.append(
            f"odd number of code-fence markers ({len(fences)}) -- a ``` or ~~~ "
            "fence is likely unclosed"
        )
    return issues


def _check_equations(text: str) -> list[str]:
    issues = []

    numbered = _NUMBERED_EQ_RE.findall(text)
    if numbered:
        kinds = sorted(set(k if k else "\\tag{}" for k in numbered))
        issues.append(
            "uses numbered-equation LaTeX ("
            + ", ".join(f"\\begin{{{k}}}" if k != "\\tag{}" else k for k in kinds)
            + ") -- these render as numbered equations and are known to break "
            "on Google Docs import. Use unnumbered $$ ... $$ or \\[ ... \\] "
            "instead, per this project's no-numbering rule."
        )

    dollar_dollar = text.count("$$")
    if dollar_dollar % 2 != 0:
        issues.append(f"odd number of '$$' delimiters ({dollar_dollar}) -- unbalanced display math")

    # Strip $$...$$ blocks before counting single-$ inline math, so a
    # display-math block's own delimiters don't get miscounted as inline ones.
    stripped = re.sub(r"\$\$.*?\$\$", "", text, flags=re.DOTALL)
    single_dollar = stripped.count("$")
    if single_dollar % 2 != 0:
        issues.append(f"odd number of single '$' delimiters ({single_dollar}) outside $$...$$ blocks")

    open_paren = text.count("\\(")
    close_paren = text.count("\\)")
    if open_paren != close_paren:
        issues.append(f"unbalanced \\( / \\) : {open_paren} open vs {close_paren} close")

    open_brack = text.count("\\[")
    close_brack = text.count("\\]")
    if open_brack != close_brack:
        issues.append(f"unbalanced \\[ / \\] : {open_brack} open vs {close_brack} close")

    return issues


def _check_tables(text: str) -> list[str]:
    issues = []
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("|") and i + 1 < len(lines) and _TABLE_SEP_RE.match(lines[i + 1]):
            header_cols = len([c for c in line.strip().strip("|").split("|")])
            sep_cols = len([c for c in lines[i + 1].strip().strip("|").split("|")])
            if header_cols != sep_cols:
                issues.append(
                    f'table near "{line.strip()[:60]}" has {header_cols} header '
                    f"columns but {sep_cols} separator columns"
                )
            j = i + 2
            row_num = 1
            while j < len(lines) and lines[j].strip().startswith("|"):
                row_cols = len([c for c in lines[j].strip().strip("|").split("|")])
                if row_cols != header_cols:
                    issues.append(
                        f'table near "{line.strip()[:60]}", data row {row_num} has '
                        f"{row_cols} columns, header has {header_cols}"
                    )
                row_num += 1
                j += 1
            i = j
            continue
        i += 1
    return issues


@mcp.tool()
async def audit_structure(path: Optional[str] = None) -> str:
    """Run MCP.md's `AUDIT_STRUCTURE` checks against one file or, if
    `path` is omitted, every .md file in the repo: heading-level
    jumps, broken/relative links and same-file anchors, unclosed code
    fences, unbalanced $ / $$ / \\( \\) / \\[ \\] math delimiters, use
    of numbered-equation LaTeX (\\begin{equation}, \\tag{}, etc. --
    forbidden by this project's own no-numbering rule and a known
    Google-Docs-import breaker), and mismatched markdown-table column
    counts. This is purely mechanical: it cannot and does not judge
    whether the CONTENT of an equation or claim is correct -- that is
    AUDIT_PHYSICS / AUDIT_MATH, which this server intentionally leaves
    to the calling model."""
    if path:
        try:
            text = await _fetch_file(path)
        except FileNotFoundError as e:
            return f"ERROR: {e}"
        all_paths = {item["path"] for item in await _fetch_tree()}
        report = StructureReport(path=path)
        report.heading_issues = _check_headings(text)
        report.link_issues = await _check_links(text, path, all_paths)
        report.fence_issues = _check_fences(text)
        report.equation_issues = _check_equations(text)
        report.table_issues = _check_tables(text)
        return report.render()

    all_paths_list = await _all_markdown_paths()
    all_paths_set = set(all_paths_list)
    reports = []
    for p in all_paths_list:
        try:
            text = await _fetch_file(p)
        except FileNotFoundError:
            reports.append(f"### {p}\nERROR: could not fetch file")
            continue
        r = StructureReport(path=p)
        r.heading_issues = _check_headings(text)
        r.link_issues = await _check_links(text, p, all_paths_set)
        r.fence_issues = _check_fences(text)
        r.equation_issues = _check_equations(text)
        r.table_issues = _check_tables(text)
        reports.append(r.render())
    dirty = [r for r in reports if not r.endswith("No structural issues found.")]
    summary = f"Audited {len(all_paths_list)} markdown files. {len(dirty)} have issues.\n\n"
    return summary + "\n\n".join(reports)


# --------------------------------------------------------------------------
# Tool: extract_model_ledger
# --------------------------------------------------------------------------


def _parse_ledger_block(block_text: str) -> dict[str, str]:
    entry: dict[str, str] = {}
    current_key: Optional[str] = None
    current_lines: list[str] = []

    def _flush():
        if current_key:
            entry[current_key] = " ".join(current_lines).strip()

    for raw_line in block_text.splitlines():
        line = raw_line.strip()
        m = _LEDGER_FIELD_RE.match(line)
        if m:
            _flush()
            # normalize to canonical casing from LEDGER_FIELDS
            matched = m.group(1)
            current_key = next(
                (f for f in LEDGER_FIELDS if f.lower() == matched.lower()), matched
            )
            rest = m.group(2).strip()
            current_lines = [rest] if rest else []
        elif current_key and line:
            current_lines.append(line)
    _flush()
    return entry


def _find_ledger_blocks(text: str) -> list[str]:
    """Return the contents of every fenced code block (``` or ~~~,
    any/no language tag) whose content contains at least two
    recognized Model Ledger field names -- a heuristic that avoids
    treating ordinary code samples as ledger entries."""
    blocks = []
    fence_re = re.compile(r"^(```|~~~)([^\n]*)\n(.*?)^\1\s*$", re.MULTILINE | re.DOTALL)
    for m in fence_re.finditer(text):
        body = m.group(3)
        field_hits = sum(1 for f in LEDGER_FIELDS if re.search(rf"(?im)^{re.escape(f)}\s*:", body))
        if field_hits >= 2:
            blocks.append(body)
    return blocks


@mcp.tool()
async def extract_model_ledger(path: Optional[str] = None) -> str:
    """Parse every Model Ledger block (MCP.md section 7's `Level /
    Parent theory / Origin / Approximation / Assumptions / Model type
    / Validity regime / Failure regime / Next reduced model` fenced
    blocks, including the "Parent theory / Reduction / Model /
    Validity / Failure" shorthand form the worked example uses) out of
    one file or, if `path` is omitted, the whole repo. Returns each
    entry's fields plus its source file, verbatim as stated -- nothing
    here is inferred or filled in."""
    targets = [path] if path else await _all_markdown_paths()
    output = []
    total = 0
    for p in targets:
        try:
            text = await _fetch_file(p)
        except FileNotFoundError as e:
            if path:
                return f"ERROR: {e}"
            continue
        blocks = _find_ledger_blocks(text)
        for block in blocks:
            parsed = _parse_ledger_block(block)
            if not parsed:
                continue
            total += 1
            output.append(f"#### {p} (entry {total})")
            for k, v in parsed.items():
                output.append(f"- **{k}**: {v}")
            output.append("")
    if not output:
        return "No Model Ledger blocks found."
    return f"Found {total} Model Ledger entries.\n\n" + "\n".join(output)


# --------------------------------------------------------------------------
# Tool: get_epistemic_tag_index
# --------------------------------------------------------------------------

_TAG_RE = re.compile(
    r"\[(DERIVATION|APPROXIMATION|STRUCTURAL CONNECTION|ANALOGY|"
    r"PHENOMENOLOGICAL|GAP|MEASURED|THEORETICAL|SYNTHESIS)\]"
)


@mcp.tool()
async def get_epistemic_tag_index(path: Optional[str] = None) -> str:
    """Index every occurrence of the repo's epistemic tags
    ([DERIVATION], [APPROXIMATION], [STRUCTURAL CONNECTION], [ANALOGY],
    [PHENOMENOLOGICAL], [GAP], [MEASURED], [THEORETICAL], [SYNTHESIS] --
    MCP.md section 5) in one file or the whole repo, with the nearest
    preceding heading and a short excerpt of the tagged text. This is
    raw data for building a GRAPH or for an AUDIT_PHYSICS pass -- it
    does NOT judge whether a tag is used correctly (e.g. whether a
    [DERIVATION] claim really is one); that judgment is for the calling
    model, per MCP.md's own division of labor."""
    targets = [path] if path else await _all_markdown_paths()
    rows = []
    for p in targets:
        try:
            text = await _fetch_file(p)
        except FileNotFoundError as e:
            if path:
                return f"ERROR: {e}"
            continue
        headings = list(_HEADING_RE.finditer(text))
        for tm in _TAG_RE.finditer(text):
            nearest_heading = "(before first heading)"
            for hm in headings:
                if hm.start() <= tm.start():
                    nearest_heading = hm.group(2).strip()
                else:
                    break
            excerpt = text[tm.end(): tm.end() + 160].strip().replace("\n", " ")
            rows.append(
                f"- `{tm.group(1)}` in **{p}** under \"{nearest_heading}\": {excerpt}..."
            )
    if not rows:
        return "No epistemic tags found."
    return f"{len(rows)} tagged claims found.\n\n" + "\n".join(rows)


# --------------------------------------------------------------------------
# Tool: build_reduction_graph
# --------------------------------------------------------------------------


@mcp.tool()
async def build_reduction_graph() -> str:
    """Assemble a typed graph strictly from Model Ledger data across
    the whole repo (MCP.md section 15's `GRAPH` mode, narrowed to what
    can be built without interpretation). Nodes are theory/model names
    taken verbatim from ledger "Parent theory" / "Model" / "Next
    reduced model" fields. Edges are:
      - REDUCES_TO   : parent theory -> model (via its stated
                       Approximation/Reduction)
      - FAILS_AT      : model -> its stated failure regime
    Other GRAPH edge types from MCP.md (DERIVES_FROM,
    STRUCTURALLY_MATCHES, ANALOGOUS_TO, SUPPORTED_BY) are NOT produced
    here: distinguishing those requires reading the surrounding prose
    and epistemic tags (see get_epistemic_tag_index) and judging which
    of the "Four Kinds of Same" (MCP.md section 6) applies -- that is
    an interpretive call for the reasoning layer, not this tool."""
    all_paths = await _all_markdown_paths()
    nodes: set[str] = set()
    edges: list[str] = []
    entry_count = 0

    for p in all_paths:
        try:
            text = await _fetch_file(p)
        except FileNotFoundError:
            continue
        for block in _find_ledger_blocks(text):
            parsed = _parse_ledger_block(block)
            if not parsed:
                continue
            entry_count += 1
            parent = parsed.get("Parent theory")
            model = parsed.get("Model")
            reduction = parsed.get("Reduction") or parsed.get("Approximation")
            failure = parsed.get("Failure") or parsed.get("Failure regime")
            next_model = parsed.get("Next reduced model")

            if parent:
                nodes.add(parent)
            if model:
                nodes.add(model)
            if next_model:
                nodes.add(next_model)

            if parent and model:
                label = f' (via "{reduction}")' if reduction else ""
                edges.append(f'REDUCES_TO: "{parent}" -> "{model}"{label}  [source: {p}]')
            if model and failure:
                edges.append(f'FAILS_AT: "{model}" -> "{failure}"  [source: {p}]')
            if model and next_model:
                edges.append(f'REDUCES_TO: "{model}" -> "{next_model}"  [source: {p}]')

    if entry_count == 0:
        return "No Model Ledger entries found in the repository -- graph is empty."

    lines = [
        f"Built from {entry_count} Model Ledger entries across the repo.",
        "",
        f"## Nodes ({len(nodes)})",
    ]
    lines.extend(f"- {n}" for n in sorted(nodes))
    lines.append(f"\n## Edges ({len(edges)})")
    lines.extend(f"- {e}" for e in edges)
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Tool: trace_model
# --------------------------------------------------------------------------


@mcp.tool()
async def trace_model(model_name: str) -> str:
    """Implement MCP.md's `TRACE_MODEL` mode for one named engineering
    model or theory (case-insensitive substring match against ledger
    "Model" / "Parent theory" / "Next reduced model" fields). Returns,
    for each match, exactly the fields MCP.md section 15 specifies:
    engineering model -> reduction -> parent continuum model ->
    assumptions -> failure boundary -- populated only from what the
    Model Ledger entry states. If nothing matches, says so rather than
    guessing a chain (MCP.md: "Never invent intermediate theories.")."""
    all_paths = await _all_markdown_paths()
    needle = model_name.strip().lower()
    matches = []

    for p in all_paths:
        try:
            text = await _fetch_file(p)
        except FileNotFoundError:
            continue
        for block in _find_ledger_blocks(text):
            parsed = _parse_ledger_block(block)
            if not parsed:
                continue
            searchable = " ".join(parsed.values()).lower()
            if needle in searchable:
                matches.append((p, parsed))

    if not matches:
        return (
            f'No Model Ledger entry matches "{model_name}". Either it has no '
            "recorded ledger entry yet, or the name differs from what's on "
            "record -- try get_epistemic_tag_index or get_file on the "
            "relevant chapter to check phrasing."
        )

    out = [f'{len(matches)} matching Model Ledger entr{"y" if len(matches)==1 else "ies"} for "{model_name}":\n']
    for p, parsed in matches:
        out.append(f"### Source: {p}")
        out.append(f"- **engineering model**: {parsed.get('Model', '(not stated)')}")
        out.append(
            f"- **reduction**: {parsed.get('Reduction') or parsed.get('Approximation') or '(not stated)'}"
        )
        out.append(f"- **parent continuum model**: {parsed.get('Parent theory', '(not stated)')}")
        out.append(f"- **assumptions**: {parsed.get('Assumptions', '(not stated)')}")
        out.append(
            f"- **failure boundary**: {parsed.get('Failure') or parsed.get('Failure regime') or '(not stated)'}"
        )
        if parsed.get("Next reduced model"):
            out.append(f"- **next reduced model**: {parsed['Next reduced model']}")
        out.append("")
    return "\n".join(out)


# --------------------------------------------------------------------------
# Entrypoint
# --------------------------------------------------------------------------

if __name__ == "__main__":
    mcp.run(transport="stdio")