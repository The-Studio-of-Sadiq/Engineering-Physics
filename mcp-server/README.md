# Engineering Physics — MCP Server

An MCP server for `The-Studio-of-Sadiq/Engineering-Physics`, implementing the
**deterministic tooling layer** described in the repo's own `MCP.md`
(section 16). It reads the live repo over GitHub's HTTP APIs — no local
clone needed — and runs mechanical checks and extraction that don't
require physics judgment.

## What it does, and deliberately does not do

`MCP.md` (section 15/16) splits work between a deterministic layer and an
"AI reasoning layer." This server is the deterministic layer only:

| Tool | MCP.md mode | What it actually does |
|---|---|---|
| `orient` | `ORIENT` | Fetches README.md, MCP.md, 00 Map.md, AUTHORING.md live and returns them |
| `list_repo_structure` | — | Lists every file path in the repo (optionally filtered by prefix) |
| `get_file` | — | Returns one file's raw content |
| `audit_structure` | `AUDIT_STRUCTURE` | Heading-level jumps, broken/relative links, same-file anchor checks, unclosed code fences, unbalanced `$`/`$$`/`\(\)`/`\[\]` math delimiters, **numbered-equation LaTeX** (`\begin{equation}`, `\tag{}`, etc.) flagged as forbidden, mismatched table columns |
| `extract_model_ledger` | (section 7) | Parses "Model Ledger" fenced blocks into structured fields, verbatim |
| `get_epistemic_tag_index` | (section 5, feeds `GRAPH`) | Indexes every `[DERIVATION]`/`[APPROXIMATION]`/etc. tag with its nearest heading and an excerpt |
| `build_reduction_graph` | `GRAPH` (partial) | Builds `REDUCES_TO` and `FAILS_AT` edges strictly from Model Ledger fields |
| `trace_model` | `TRACE_MODEL` | Returns the ledger-stated chain for a named model: model → reduction → parent theory → assumptions → failure boundary |

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
  silently passing. Fetching and slugifying every linked file's headings
  for every link would work but multiplies GitHub requests considerably;
  left out for now.
- **A "heading skips a level" warning fires on a `#` title immediately
  followed by a `###` subtitle/tagline** (as in this repo's own
  `README.md`), which is a common and reasonable style choice, not
  necessarily an error — read these as prompts to check, not verdicts.
- **GitHub's tree API is rate-limited** to 60 requests/hour unauthenticated
  (raw file fetches are not). Any tool that needs the *whole* file list
  (`list_repo_structure`, `audit_structure` with no `path`,
  `extract_model_ledger`/`get_epistemic_tag_index`/`build_reduction_graph`
  with no `path`) will hit this eventually on a shared or busy network. Set
  `GITHUB_TOKEN` (see `.env.example`) to raise it to 5000/hour.
- **In-memory caching only, per process, no invalidation on push.** If you
  edit the repo while the server is running, restart it to see the change.

## Setup

```bash
pip install -r requirements.txt
# or: pip install -r requirements.txt --break-system-packages   (on systems
# that refuse system-wide installs otherwise)
```

Requires `mcp>=2.0`, whose Python API renamed `FastMCP` to `MCPServer`
(same decorator style: `@mcp.tool()`). If you have an older `mcp<2`
pinned elsewhere, either upgrade it or change the two lines in
`server.py`:
```python
from mcp.server.mcpserver import MCPServer   # -> from mcp.server.fastmcp import FastMCP
mcp = MCPServer("engineering-physics")        # -> mcp = FastMCP("engineering-physics")
```

Copy `.env.example` to `.env` (or set the variables another way) if you
want to point at a fork/branch or add a `GITHUB_TOKEN`. All variables are
optional — with none set, it reads `The-Studio-of-Sadiq/Engineering-Physics`
at `main`, unauthenticated.

Run it directly to confirm it starts:
```bash
python3 server.py
```
(It will sit waiting for stdio MCP messages — that's expected; Ctrl+C to
stop when just checking it starts cleanly.)

### Wiring it into Claude Desktop / Claude Code

Add to your MCP client's config (e.g. `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "engineering-physics": {
      "command": "python3",
      "args": ["/absolute/path/to/server.py"],
      "env": {
        "GITHUB_TOKEN": "ghp_..."
      }
    }
  }
}
```

Omit the `env` block (or the token) entirely to run unauthenticated.

## Testing without a full MCP client

`smoke_test.py` calls the tool functions directly (no stdio transport
needed) against the live repo — a quick way to sanity-check after any
edit:

```bash
python3 smoke_test.py
```

It patches around the GitHub tree API's rate limit using a static file
list, since raw content fetches (which is what does the real work) aren't
rate-limited. Remove that patch if you have a `GITHUB_TOKEN` set and want
to exercise the real tree-fetch path too.