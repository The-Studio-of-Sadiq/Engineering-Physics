"""
Shared figure style for Engineering Physics: Top Down.

Every figure script in FIGURES/<FOLDER>/make_figures.py imports this module,
so all plots share one look: white background (readable in light and dark
Obsidian themes), a fixed colour-blind-safe palette, SI-unit axis labels,
and deterministic SVG output (no timestamp, so reruns diff cleanly).

Usage, from inside a FIGURES/<FOLDER>/make_figures.py script:

    import sys, pathlib
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
    from _style import plt, np, C, save, fig_ax

    fig, ax = fig_ax()
    ax.plot(x, y, color=C[0], label="...")
    save(fig, __file__, "my-figure-slug")

Regenerate everything with:  python FIGURES/build_all.py
"""

from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

# Categorical palette: colour-blind-safe (Okabe-Ito order, black dropped).
C = ["#0072B2", "#D55E00", "#009E73", "#CC79A7", "#E69F00", "#56B4E9", "#F0E442"]
GREY = "#7f7f7f"
INK = "#222222"
SHADE = "#0072B2"  # use with alpha=0.12 for shaded regions

plt.rcParams.update(
    {
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "figure.dpi": 110,
        "font.size": 10,
        "font.family": "DejaVu Sans",
        "mathtext.fontset": "dejavusans",
        "axes.titlesize": 11,
        "axes.labelsize": 10,
        "axes.edgecolor": INK,
        "axes.labelcolor": INK,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": "#e6e6e6",
        "grid.linewidth": 0.6,
        "xtick.color": INK,
        "ytick.color": INK,
        "text.color": INK,
        "legend.frameon": False,
        "legend.fontsize": 9,
        "lines.linewidth": 1.8,
        "svg.fonttype": "path",  # glyphs as paths: identical rendering everywhere
        "axes.prop_cycle": matplotlib.cycler(color=C),
    }
)


def fig_ax(ncols: int = 1, nrows: int = 1, w: float | None = None, h: float = 3.6, **kw):
    """Standard figure size: 6.4 in wide per single panel, capped at 11 in."""
    if w is None:
        w = min(6.4 if ncols == 1 else 4.6 * ncols, 11.0)
    return plt.subplots(nrows, ncols, figsize=(w, h * nrows), **kw)


def save(fig, script_file: str, slug: str) -> pathlib.Path:
    """Write <script folder>/<slug>.svg and close the figure."""
    out = pathlib.Path(script_file).resolve().parent / f"{slug}.svg"
    fig.tight_layout()
    fig.savefig(out, format="svg", bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    print(f"wrote {out.relative_to(out.parents[2])}")
    return out
