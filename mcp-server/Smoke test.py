import asyncio
import server as s

# GitHub API tree endpoint is rate-limited (60/hr unauthenticated) and this
# sandbox's shared IP is already exhausted for the hour. Raw file fetches
# (raw.githubusercontent.com) are NOT subject to that limit, so patch in a
# static tree (from MCP.md section 3's own repository-structure listing)
# to exercise every tool's logic against real file content without
# depending on the rate-limited endpoint.
_STATIC_TREE = [
    {"path": p, "type": "blob"}
    for p in [
        "README.md", "MCP.md", "AUTHORING.md", "REFERENCES.md",
        "METADATA/00 Map.md", "METADATA/EPILOGUE.md",
        *[f"CHAPTERS/CHAPTER {i}.md" for i in range(0, 22)],
        "EXAMPLES/README.md",
        "EXAMPLES/01 Dirac-to-Pauli.md",
        "EXAMPLES/02 Quantum-to-Thermodynamics.md",
        "EXAMPLES/03 Maxwell-to-Circuit.md",
        "EXAMPLES/04 Heat-Equation-to-Thermal-RC.md",
        "EXAMPLES/05 Navier-Stokes-to-Fluid-Network.md",
        "EXAMPLES/06 Motor-to-Control-System.md",
    ]
]


async def _patched_fetch_tree():
    return _STATIC_TREE


s._fetch_tree = _patched_fetch_tree


async def main():
    print("=== list_repo_structure(CHAPTERS/) ===")
    print((await s.list_repo_structure("CHAPTERS/"))[:800])

    print("\n=== orient() [first 500 chars] ===")
    print((await s.orient())[:500])

    print("\n=== extract_model_ledger() [whole repo] ===")
    print((await s.extract_model_ledger(None))[:2000])

    print("\n=== get_epistemic_tag_index() [whole repo, first 1500 chars] ===")
    print((await s.get_epistemic_tag_index(None))[:1500])

    print("\n=== build_reduction_graph() ===")
    print((await s.build_reduction_graph())[:2000])

    print("\n=== trace_model('Hagen') ===")
    print(await s.trace_model("Hagen"))

    print("\n=== audit_structure('EXAMPLES/05 Navier-Stokes-to-Fluid-Network.md') ===")
    print(await s.audit_structure("EXAMPLES/05 Navier-Stokes-to-Fluid-Network.md"))


asyncio.run(main())