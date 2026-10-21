# Engineering Physics — MCP Server

An MCP server for `The-Studio-of-Sadiq/Engineering-Physics`, implementing the
**deterministic tooling layer** described in the repo's own `MCP.md`
(section 16). By default it reads the **local working copy** it ships in,
straight from disk on every call, so uncommitted edits are visible with no
restart. It can instead read the live repo over GitHub's HTTP APIs
(`EP_SOURCE=github`). Either way it runs mechanical checks and extraction
that don't require physics judgment.

## What it does, and deliberately does not do

`MCP.md` (section 15/16) splits work between a deterministic layer and an
"AI reasoning layer." This server is the deterministic layer only:

| Tool | MCP.md mode | What it actually does |
|---|---|---|
| `orient` | `ORIENT` | Returns README.md, MCP.md, 00 Map.md, CONTRIBUTING.md, and which source (local/GitHub) was read |
| `list_repo_structure` | — | Lists every file path in the repo (optionally filtered by prefix) |
| `get_file` | — | Returns one file's raw content (local mode refuses paths outside the repo) |
| `audit_structure` | `AUDIT_STRUCTURE` | Heading-level jumps, broken/relative links (files and folders), same-file anchor checks, **image embeds** (missing file, empty alt text, remote images, Obsidian-only `![[...]]`), unclosed code fences, unbalanced `$`/`$$`/`\(\)`/`\[\]` math delimiters, **numbered-equation LaTeX** (`\begin{equation}`, `\tag{}`, etc.) flagged as forbidden, mismatched table columns |
| `extract_model_ledger` | (section 7) | Parses every Model Ledger — both the Markdown-table form (`\| Field \| Content \|` under a "Model Ledger — *name*" title) and the fenced `Field: value` form — into structured fields, verbatim |
| `get_epistemic_tag_index` | (section 5, feeds `GRAPH`) | Indexes every `[DERIVATION]`/`[APPROXIMATION]`/etc. tag with its nearest heading and an excerpt |
| `build_reduction_graph` | `GRAPH` (partial) | Builds `REDUCES_TO` and `FAILS_AT` edges strictly from Model Ledger fields |
| `trace_model` | `TRACE_MODEL` | Returns the ledger-stated chain for a named model: model → reduction → parent theory → assumptions → failure boundary |
| `get_figure_index` | — | Lists every embedded figure: path, whether the file exists, alt text, caption, nearest heading, and the `FIGURES/<FOLDER>/make_figures.py` script that draws it; also lists figure files nothing embeds |

Figures are SVGs, which a model can't look at. `get_figure_index` returns
each figure's caption, and `get_file` on its `make_figures.py` returns the
exact equation and parameters plotted. Between them, that is the readable
description of a figure.

**Not implemented, on purpose:** `AUDIT_PHYSICS`, `AUDIT_MATH`,
`AUDIT_REFERENCES`, `TRACE_CLAIM`, and the `DERIVES_FROM` /
`STRUCTURALLY_MATCHES` / `ANALOGOUS_TO` / `SUPPORTED_BY` edges of `GRAPH`.
All of these require judging whether an equation, claim, or citation is
*correct* — physics/mathematical/scholarly judgment that `MCP.md` itself
assigns to the calling LLM, not to tooling. Hard-coding that judgment here
would be exactly the kind of silent overclaim `MCP.md` §8 warns against.
Use `get_file` / `list_repo_structure` to pull the text, then reason over
it directly — that's the intended split.

**No write tools.** There is no commit/PR/push capability. This matches
`MCP.md` §17 (Safe Write Policy) and its own metadata: `autonomous_writes:
false`. If/when you want write support, it should implement the full
`READ → ANALYZE → PROPOSE DIFF → VALIDATE → HUMAN APPROVAL → WRITE`
sequence `MCP.md` specifies, not a direct write tool — that's a deliberate
gap, not an oversight, and worth a separate conversation before building.

## Known caveats (mechanical checks, not opinions)

- **Anchors in *other* files aren't verified**, only that the target file
  exists — `audit_structure` says so explicitly in that case rather than
  silently passing.
- **A "heading skips a level" warning fires on a `#` title immediately
  followed by a `###` subtitle/tagline** (as in this repo's own
  `README.md`), which is a common and reasonable style choice, not
  necessarily an error — read these as prompts to check, not verdicts.
- **Ledgers written as plain aligned text** (no colon, no table — the
  illustrative block in `README.md`) are not parsed. Use the table form.
- **GitHub mode only:** the tree API is rate-limited to 60 requests/hour
  unauthenticated (raw file fetches are not); set `GITHUB_TOKEN` to raise it
  to 5000/hour. GitHub mode also caches in memory per process with no
  invalidation on push — restart to see upstream changes.

## Setup

```bash
pip install -r requirements.txt
```

Requires `mcp>=2.0`, whose Python API renamed `FastMCP` to `MCPServer`
(same decorator style: `@mcp.tool()`). If you have an older `mcp<2`
pinned elsewhere, either upgrade it or change the two lines in
`server.py`:
```python
from mcp.server.mcpserver import MCPServer   # -> from mcp.server.fastmcp import FastMCP
mcp = MCPServer("engineering-physics")        # -> mcp = FastMCP("engineering-physics")
```

Configuration is by environment variable; `.env.example` lists them all.
The server doesn't load a `.env` file itself — put the variables in your MCP
client's `env` block (below) or your shell. With none set it reads the local
working copy.

Run it directly to confirm it starts:
```bash
python server.py
```
(It will sit waiting for stdio MCP messages — that's expected; Ctrl+C to
stop when just checking it starts cleanly.) On Windows use `python`, not
`python3`, which is usually the Microsoft Store stub.

### Wiring it into Claude Code

The repo root has a `.mcp.json`, so opening Claude Code **in the repo
root** picks the server up automatically (it asks you to approve it the
first time):

```json
{
  "mcpServers": {
    "engineering-physics": {
      "command": "python",
      "args": ["mcp-server/server.py"],
      "env": { "EP_SOURCE": "local" }
    }
  }
}
```

### Claude Desktop and other clients

Add the same entry to the client's config (e.g. `claude_desktop_config.json`),
with an absolute path, since those clients don't start in the repo:

```json
{
  "mcpServers": {
    "engineering-physics": {
      "command": "python",
      "args": ["/absolute/path/to/mcp-server/server.py"]
    }
  }
}
```

To read GitHub instead of the local copy, add
`"env": { "EP_SOURCE": "github", "GITHUB_TOKEN": "..." }`.

## Testing without a full MCP client

`smoke_test.py` calls every tool function directly (no stdio transport) and
prints PASS/FAIL per check. It exits non-zero on any failure, so it works
as a pre-commit check:

```bash
python smoke_test.py
```

It runs against the local working copy, so it needs no network. Run it with
`EP_SOURCE=github` to exercise the GitHub path.
