"""Regenerate every figure: runs FIGURES/*/make_figures.py in turn."""

import pathlib
import runpy
import sys

ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

failed = []
for script in sorted(ROOT.glob("*/make_figures.py")):
    print(f"== {script.parent.name}")
    try:
        runpy.run_path(str(script), run_name="__main__")
    except Exception as exc:  # keep going; report at the end
        failed.append((script.parent.name, exc))
        print(f"   FAILED: {exc!r}")

if failed:
    sys.exit(f"{len(failed)} folder(s) failed: {', '.join(n for n, _ in failed)}")
