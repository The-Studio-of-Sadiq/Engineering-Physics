"""
Smoke test: call every tool function directly (no stdio transport) and
check the results look sane. Runs against the local working copy by
default (EP_SOURCE=local), so it needs no network and sees uncommitted
edits. Set EP_SOURCE=github to exercise the GitHub path instead (the tree
API is rate-limited to 60 requests/hour without GITHUB_TOKEN).

    python smoke_test.py

Exits non-zero if any check fails.
"""

import asyncio
import sys

import server as s

failures: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
    if not ok:
        failures.append(name)


async def main() -> None:
    print(f"source: {s._source_label()}\n")

    out = await s.list_repo_structure("CHAPTERS/")
    n_ch = sum(1 for line in out.splitlines() if line.endswith(".md"))
    check("list_repo_structure(CHAPTERS/)", n_ch == 22, f"{n_ch} chapter files")

    out = await s.orient()
    missing = [f for f in s.ORIENT_FILES if f"## {f}\n\n[not found" in out]
    check("orient", not missing, f"missing: {missing}" if missing else f"{len(out)} chars")

    out = await s.get_file("CHAPTERS/CHAPTER 0.md")
    check("get_file", not out.startswith("ERROR"), out[:60].replace("\n", " "))

    out = await s.get_file("../outside.md")
    check("get_file refuses paths outside the repo", out.startswith("ERROR"))

    out = await s.extract_model_ledger(None)
    check("extract_model_ledger", "ERROR" not in out[:200], out.splitlines()[0] if out else "")

    out = await s.get_epistemic_tag_index(None)
    check("get_epistemic_tag_index", "tagged claims found" in out, out.splitlines()[0])

    out = await s.build_reduction_graph()
    check("build_reduction_graph", bool(out.strip()), out.splitlines()[0] if out else "")

    out = await s.trace_model("Hagen")
    check("trace_model('Hagen')", bool(out.strip()), out.splitlines()[0] if out else "")

    out = await s.get_figure_index(None)
    first = out.splitlines()[0]
    check("get_figure_index", "embedded figures" in first, first)
    broken = [line for line in out.splitlines() if "exists: NO" in line]
    check("every embedded figure exists", not broken, f"{len(broken)} missing")

    out = await s.audit_structure(None)
    first = out.splitlines()[0]
    image_problems = out.count("**Images**")
    check("audit_structure (whole repo)", first.startswith("Audited"), first)
    check("no image-embed issues", image_problems == 0, f"{image_problems} files with image issues")


asyncio.run(main())
if failures:
    sys.exit(f"\n{len(failures)} check(s) failed: {', '.join(failures)}")
print("\nall checks passed")
