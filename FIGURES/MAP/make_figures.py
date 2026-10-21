"""Figures for the Layer Map (METADATA/00 Map.md)."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch, Rectangle

LINE_H = 1.75  # data units per text line in the graph canvas

# Edge styles by tag (README "Notation and Conventions").
STYLE = {
    "D": dict(color=C[0], ls="-", lw=1.6),       # [DERIVATION]
    "A": dict(color=C[1], ls="--", lw=1.5),      # [APPROXIMATION]
    "S": dict(color=C[3], ls=":", lw=1.8),       # [STRUCTURAL CONNECTION]
    "u": dict(color=GREY, ls="-", lw=0.9),       # untagged narrative connective
}

# key: (x, y, width, text, kind)   kind: "hub" = layer node, "br" = bridge sub-box, "n" = node
NODES = {
    "L0": (50, 96.5, 30, "L$_0$  FUNDAMENTAL PHYSICS\nfields · symmetries · action", "hub"),
    "QFT": (28, 89, 26, "Quantum field theory\ngauge · matter · θ-term (Ch. 0)", "n"),
    "GR": (84, 89, 24, "General relativity\nmetric · curvature (Ch. 0, 8)", "n"),
    "L1": (50, 76, 28, "L$_1$  QUANTUM PHYSICS\nψ(x,t) · spin · bands · nuclei", "hub"),
    "MAT": (22, 69, 28, "Matter\norbitals, bonds, bands, nuclei (Ch. 4–6)", "n"),
    "SCA": (50, 69, 24, "Scattering\nS-matrix, phonons, impurities (Ch. 6)", "n"),
    "FLD": (76, 69, 24, "Fields / topology\nBerry phase, Chern numbers (Ch. 7)", "n"),
    "Bb": (12, 56.5, 17, "B.b  N → ∞,\nensemble average (Ch. 10)", "br"),
    "Ba": (31, 56.5, 17, "B.a  ħ → 0\n(Ch. 9)", "br"),
    "Bc": (50, 56.5, 17, "B.c  classical\nEM-field limit (Ch. 11)", "br"),
    "Be": (69, 56.5, 17, "B.e  Kubo linear\nresponse (Ch. 13)", "br"),
    "Bd": (88, 56.5, 17, "B.d  weak-field\nmetric (Ch. 8)", "br"),
    "THE": (12, 46, 17, "Thermodynamics\nfour laws, ensembles,\nLandau transitions (Ch. 10)", "n"),
    "MEC": (31, 46, 17, "Mechanics\nNewton, Lagrangian (Ch. 9);\nelasticity, fluids (Ch. 15–16)", "n"),
    "EM": (50, 46, 17, "Electromagnetism\nMaxwell, waves, optics\n(Ch. 11–12); D=εE, J=σE", "n"),
    "GTL": (69, 46, 17, "Generalized\nTransport Law\nflux = −L·∇φ (Ch. 13)", "n"),
    "NGR": (88, 46, 17, "Newtonian\ngravity", "n"),
    "CONT": (50, 38.5, 46, "L$_2$  CONTINUUM PHYSICS\nNavier–Stokes · Navier elasticity · wave · diffusion · Maxwell", "hub"),
    "PDE": (20, 23.5, 22, "PDE kept\n(distributed parameter)", "n"),
    "FEM": (50, 23.5, 22, "FEM / discretised\nstiffness, FD (Ch. 16, 20)", "n"),
    "NET": (80, 23.5, 24, "Network\neffort/flow, R/C/L (Ch. 17–19)", "n"),
    "L3": (50, 16.5, 38, "L$_3$  ENGINEERING SYSTEMS\ncircuits · machines · structures · reactors", "hub"),
    "ELE": (14, 9.5, 17, "Electrical\nCh. 18 · R, C, L", "n"),
    "ME3": (35, 9.5, 17, "Mechanical\nCh. 19 · m, c, b", "n"),
    "CIV": (56, 9.5, 17, "Civil\nCh. 20 · k, R, C", "n"),
    "CHE": (77, 9.5, 17, "Chemical\nCh. 20 · R, C, k", "n"),
    "EF": (30, 1.5, 40, "EFFORT/FLOW UNIFICATION  P = e·f\nR/C/L template:  L ẍ + R ẋ + x/C = e", "hub"),
    "CTRL": (78, 1.5, 30, "CONTROL (Ch. 21)\nPID, state space, observers, MPC", "hub"),
}

# (from, to, tag, label)
EDGES = [
    ("L0", "QFT", "u", None), ("L0", "GR", "u", None),
    ("QFT", "L1", "A", None),
    ("L1", "MAT", "u", None), ("L1", "SCA", "u", None), ("L1", "FLD", "u", None),
    ("SCA", "Be", "D", "1/τ; ensemble\naverage → Kubo"),
    ("Bb", "THE", "A", None), ("Ba", "MEC", "A", None), ("Bc", "EM", "A", None),
    ("Be", "GTL", "D", None), ("Bd", "NGR", "A", None),
    ("THE", "CONT", "u", None), ("MEC", "CONT", "u", None), ("EM", "CONT", "u", None),
    ("GTL", "CONT", "u", None), ("NGR", "CONT", "u", None),
    ("CONT", "PDE", "u", None), ("CONT", "FEM", "A", None), ("CONT", "NET", "A", None),
    ("PDE", "L3", "u", None), ("FEM", "L3", "u", None), ("NET", "L3", "u", None),
    ("L3", "ELE", "u", None), ("L3", "ME3", "u", None), ("L3", "CIV", "u", None), ("L3", "CHE", "u", None),
    ("ELE", "EF", "S", None), ("ME3", "EF", "S", None), ("CIV", "EF", "S", None), ("CHE", "EF", "S", None),
]


def _box(key):
    x, y, w, text, kind = NODES[key]
    h = LINE_H * (text.count("\n") + 1) + 0.9
    return x, y, w, h


def _arrow(ax, p, q, tag, label=None):
    st = STYLE[tag]
    ax.annotate("", xy=q, xytext=p,
                arrowprops=dict(arrowstyle="-|>", color=st["color"], lw=st["lw"], ls=st["ls"],
                                shrinkA=0, shrinkB=0, mutation_scale=9))
    if label:
        ax.text((p[0] + q[0]) / 2 - 1.0, (p[1] + q[1]) / 2 - 2.4, label, fontsize=7.2,
                color=st["color"], va="center", ha="right")


def dependency_graph():
    """§M: the master dependency graph L0 -> L1 -> L2 -> L3, aggregated from the ASCII
    diagram into ~30 nodes; bridges A, B (B.a-B.e), C drawn as bands; edges styled by tag."""
    fig, ax = plt.subplots(figsize=(11, 8.6))
    ax.set_xlim(-9, 103)
    ax.set_ylim(-2, 100.5)
    ax.axis("off")

    # Layer bands and labels.
    for y0, y1, lab in [(85.5, 100.5, "L$_0$"), (65.5, 79.5, "L$_1$"), (35.5, 50.5, "L$_2$"),
                        (-2, 20, "L$_3$")]:
        ax.add_patch(Rectangle((-9, y0), 112, y1 - y0, color=SHADE, alpha=0.05, lw=0))
        ax.text(-7.5, (y0 + y1) / 2, lab, fontsize=13, fontweight="bold", color=C[0],
                va="center", ha="left")
    # Bridge bands.
    bands = [
        (80.3, 84.7, "BRIDGE A", "isolate matter sector, E ≪ mc², v ≪ c — discards pair creation, "
                                 "QED loops O(α/π ≈ 0.002), gravitational effects"),
        (51.8, 63.6, "BRIDGE B", "four simultaneous descents — NOT one limit"),
        (27.6, 34.6, "BRIDGE C", "control-volume integration · discretisation · lumping · linearisation\n"
                                 "criteria: L ≪ λ, Bi ≪ 1, modal separation, mixing  ·  bridge zone: "
                                 "transmission line, Euler–Bernoulli beam"),
    ]
    for y0, y1, name, desc in bands:
        ax.add_patch(Rectangle((-9, y0), 112, y1 - y0, color=C[4], alpha=0.13, lw=0))
        ax.text(-7.5, y1 - 0.5, name, fontsize=9, fontweight="bold", color="#8a5a00", va="top")
        ax.text(8 if name != "BRIDGE A" else 4, y1 - 0.5, desc, fontsize=7.6, color="#8a5a00",
                va="top", ha="left")

    # Nodes.
    for key, (x, y, w, text, kind) in NODES.items():
        _, _, _, h = _box(key)
        fc = {"hub": "#eaf2fa", "br": "#fff3dc", "n": "white"}[kind]
        ec = {"hub": C[0], "br": "#b07a00", "n": INK}[kind]
        ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.8",
                                    fc=fc, ec=ec, lw=1.0, zorder=3))
        lines = text.split("\n")
        title, rest = lines[0], "\n".join(lines[1:])
        ax.text(x, y + h / 2 - 0.45, title, ha="center", va="top", fontsize=8,
                fontweight="bold", zorder=4)
        if rest:
            ax.text(x, y + h / 2 - 0.45 - LINE_H, rest, ha="center", va="top", fontsize=7.4,
                    zorder=4, linespacing=1.15)

    # Tagged edges, bottom-centre of source to top-centre of target.
    for a, b, tag, label in EDGES:
        xa, ya, _, ha_ = _box(a)
        xb, yb, _, hb = _box(b)
        _arrow(ax, (xa, ya - ha_ / 2), (xb, yb + hb / 2), tag, label)

    # Routed edges.
    xg, yg, wg, hg = _box("GR")
    xd, yd, wd, hd = _box("Bd")
    _arrow(ax, (94, yg - hg / 2), (94, yd + hd / 2), "A")
    ax.text(95, 80.0, "weak field\nh$_{μν}$ ≪ 1", fontsize=7.2, color=C[1], va="top")
    for key in ("MAT", "FLD"):          # these feed Bridge B as a whole
        x, y, w, h = _box(key)
        _arrow(ax, (x, y - h / 2), (x, 63.6), "u")
    xe, ye, we, he = _box("EF")
    xc, yc, wc, hc = _box("CTRL")
    _arrow(ax, (xe + we / 2, ye), (xc - wc / 2, yc), "u")

    # Structural connections (no causal direction: plain dotted lines).
    sty = STYLE["S"]
    xq, yq, wq, hq = _box("QFT")
    xt, yt, wt, ht = _box("THE")
    ax.plot([xq - wq / 2, -3, -3, xt - wt / 2], [yq, yq, yt, yt], **sty, zorder=2)
    ax.text(-2.4, 72, "Higgs ↔ Landau (§0.3)", rotation=90,
            fontsize=7.2, color=sty["color"], va="center", ha="left")
    xf, yf, wf, hf = _box("FLD")
    ax.plot([xf + wf / 2, 101, 101, xc + wc / 2], [yf, yf, yc, yc], **sty, zorder=2)
    ax.text(101.6, 36, "winding number: θ-term ↔ Chern ↔ Nyquist encirclement (§0.4)",
            rotation=90, fontsize=7.2, color=sty["color"], va="center", ha="left")

    handles = [Line2D([], [], **STYLE["D"], label="[DERIVATION]"),
               Line2D([], [], **STYLE["A"], label="[APPROXIMATION]"),
               Line2D([], [], **STYLE["S"], label="[STRUCTURAL CONNECTION]"),
               Line2D([], [], **STYLE["u"], label="untagged (narrative)")]
    ax.legend(handles=handles, loc="upper right", bbox_to_anchor=(1.0, 1.0), fontsize=8,
              handlelength=3)
    save(fig, __file__, "dependency-graph")


def r_c_l_step():
    """Bridge C.2: unit-step response of L x'' + R x' + x/C = e, normalised to
    x'' + 2 zeta w_n x' + w_n^2 x = w_n^2 u(t), for zeta = 0.2, 0.7, 2 (plus the L = 0 first-order case)."""
    t = np.linspace(0, 15, 1500)

    def step(z):
        if z < 1:
            wd = np.sqrt(1 - z**2)
            return 1 - np.exp(-z * t) * (np.cos(wd * t) + z / wd * np.sin(wd * t))
        r1, r2 = -z + np.sqrt(z**2 - 1), -z - np.sqrt(z**2 - 1)
        return 1 - (r2 * np.exp(r1 * t) - r1 * np.exp(r2 * t)) / (r2 - r1)

    fig, ax = fig_ax(h=3.6)
    for z, col, ls, what in [(0.2, C[0], "-", "underdamped"), (0.7, C[2], "--", "near-optimal"),
                             (2.0, C[1], "-.", "overdamped")]:
        ax.plot(t, step(z), color=col, ls=ls, label=rf"$\zeta$ = {z} ({what})")
    ax.axhline(1, color=GREY, lw=0.8, ls=":")
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 1.65)
    ax.set_xlabel(r"normalised time $\omega_n t$,  $\omega_n = 1/\sqrt{LC}$")
    ax.set_ylabel(r"normalised response $x/(Ce)$")
    ax.text(14.8, 0.08, r"$\zeta = \frac{R}{2}\sqrt{C/L}$", ha="right", fontsize=10)
    ax.legend(loc="upper right")
    save(fig, __file__, "r-c-l-step")


if __name__ == "__main__":
    dependency_graph()
    r_c_l_step()
