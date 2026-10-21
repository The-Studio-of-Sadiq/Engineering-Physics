"""Figures for Example 01 — Dirac → Pauli (EXAMPLES/01 Dirac-to-Pauli.md)."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax

MU_B_UEV = 57.883818  # Bohr magneton, µeV/T  (9.274e-24 J/T)
UEV_TO_GHZ = 0.241799  # E/h: 1 µeV -> 0.2418 GHz  (so mu_B/h = 13.996 GHz/T)


def zeeman_splitting():
    """Step 5: Delta E = mu_B g_J m_J B for 2S1/2 (g = 2) and 2P3/2 (g_J = 4/3), B = 0-3 T."""
    B = np.linspace(0, 3, 200)
    fig, axes = fig_ax(ncols=2, h=3.8, sharey=True)
    cases = [
        (axes[0], r"$^2S_{1/2}$ (spin only, $g = 2$)", 2.0, [0.5, -0.5]),
        (axes[1], r"$^2P_{3/2}$ ($g_J = 4/3$)", 4 / 3, [1.5, 0.5, -0.5, -1.5]),
    ]
    for ax, title, g, mjs in cases:
        for i, mj in enumerate(mjs):
            E = MU_B_UEV * g * mj * B
            col = C[0] if mj > 0 else C[1]
            ax.plot(B, E, color=col, ls="-" if abs(mj) == 0.5 else "--")
            frac = {0.5: "1/2", 1.5: "3/2"}[abs(mj)]
            sign = "+" if mj > 0 else "−"
            ax.text(3.05, E[-1], f"$m_J$ = {sign}{frac}", va="center", fontsize=8.5, color=col)
        for Bm in (1.5, 3.0):
            ax.axvline(Bm, color=GREY, lw=0.8, ls=":")
        ax.axhline(0, color=INK, lw=0.6)
        ax.set_title(title)
        ax.set_xlabel("magnetic flux density $B$ (T)")
        ax.set_xlim(0, 3.75)
        ax.set_xticks([0, 0.5, 1, 1.5, 2, 2.5, 3])

    # Annotate the g = 2 splitting at 1.5 T and 3 T.
    ax = axes[0]
    for Bm in (1.5, 3.0):
        dE = 2 * MU_B_UEV * Bm  # g mu_B B between m = +-1/2
        ax.annotate("", xy=(Bm, dE / 2), xytext=(Bm, -dE / 2),
                    arrowprops=dict(arrowstyle="<->", color=INK, lw=0.9))
        ax.text(Bm - 0.06, -dE / 2 + 15 if Bm == 3 else dE / 2 + 18,
                f"{dE:.0f} µeV\n{dE * UEV_TO_GHZ:.0f} GHz",
                ha="right" if Bm == 3 else "center", va="bottom", fontsize=8.5)
    axes[0].set_ylabel(r"$\Delta E = \mu_B\, g_J\, m_J\, B$  (µeV)")
    axes[0].set_ylim(-380, 380)

    sec = axes[1].secondary_yaxis("right", functions=(lambda e: e * UEV_TO_GHZ,
                                                       lambda f: f / UEV_TO_GHZ))
    sec.set_ylabel(r"$\Delta E / h$  (GHz)")
    axes[1].spines["right"].set_visible(True)
    save(fig, __file__, "zeeman-splitting")


if __name__ == "__main__":
    zeeman_splitting()
