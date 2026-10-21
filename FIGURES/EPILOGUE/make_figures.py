"""Figures for the Epilogue (METADATA/EPILOGUE.md)."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax


def energy_budget():
    """E.3.1-E.3.2: present-day energy budget, Planck 2018 (rounded as in the text):
    dark energy ~68%, dark matter ~27%, ordinary (baryonic) matter ~5%."""
    parts = [(r"dark energy ($\Lambda$)", 68, C[0]), ("dark matter", 27, C[3]),
             ("ordinary matter", 5, C[4])]
    fig, ax = fig_ax(h=1.9)
    left = 0
    for name, pct, col in parts:
        ax.barh(0, pct, left=left, color=col, height=0.55, edgecolor="white", lw=1.5)
        if pct > 10:
            ax.text(left + pct / 2, 0, f"{name}\n~{pct}%", ha="center", va="center",
                    color="white", fontsize=9.5, fontweight="bold")
        else:
            ax.annotate(f"{name}\n~{pct}%", (left + pct / 2, 0.28),
                        xytext=(left + pct / 2 - 1, 0.62), ha="right", va="bottom", fontsize=8.5,
                        arrowprops=dict(arrowstyle="-", color=GREY, lw=0.7))
        left += pct
    ax.set_xlim(0, 100)
    ax.set_ylim(-0.4, 1.05)
    ax.set_yticks([])
    ax.set_xlabel("share of the universe's energy budget today (%)")
    ax.grid(False)
    ax.spines["left"].set_visible(False)
    save(fig, __file__, "energy-budget")


def sci(x):
    """Format x as mathtext 'a x 10^b'."""
    e = int(np.floor(np.log10(x)))
    if e == 0:
        return "1"
    m = x / 10**e
    return rf"{m:.1f}\times10^{{{e}}}" if abs(m - 1) > 0.05 else rf"10^{{{e}}}"


def energy_scale_ladder():
    """E.3.3: energy scales from 1 eV to the Planck energy, with the quantum-gravity
    suppression factor (E/E_Pl)^2, E_Pl = 1.22e19 GeV = 1.22e28 eV."""
    E_PL = 1.22e28  # eV
    # (energy in eV, label, label position (x, y) in data coords, horizontal alignment)
    marks = [(1.0, "1 eV: chemistry, electronics", (1e2, 1e-60), "left"),
             (246e9, "246 GeV: electroweak scale", (3e4, 1e-24), "left"),
             (13.6e12, "13.6 TeV: LHC collisions", (1e15, 1e-38), "left"),
             (1e25, r"~$10^{16}$ GeV: GUT scale (hypothetical)", (1e10, 1e0), "left"),
             (E_PL, r"$1.22\times10^{19}$ GeV: Planck energy", (6e28, 1e-22), "right")]
    E = np.logspace(0, np.log10(E_PL), 300)
    fig, ax = fig_ax(h=4.0)
    ax.axvspan(0.3, 13.6e12, color=SHADE, alpha=0.08, lw=0)
    ax.text(0.6, 1e-36, "probed directly\n(up to LHC energies)", fontsize=8.5, color=C[0])
    ax.loglog(E, (E / E_PL) ** 2, color=C[0])
    for e, lab, xy, ha in marks:
        s = (e / E_PL) ** 2
        ax.plot(e, s, "o", color=C[1] if e < 1e14 else C[3], zorder=5)
        ax.annotate(lab + "\n" + rf"$(E/E_{{Pl}})^2 \approx {sci(s)}$", (e, s), xytext=xy,
                    fontsize=8.5, ha=ha, va="center",
                    arrowprops=dict(arrowstyle="-", color=GREY, lw=0.6))
    ax.set_xlim(0.3, 1e30)
    ax.set_ylim(1e-66, 1e6)
    ax.set_xticks([1, 1e3, 1e6, 1e9, 1e12, 1e15, 1e18, 1e21, 1e24, 1e27, 1e30])
    ax.set_yticks([1e-60, 1e-48, 1e-36, 1e-24, 1e-12, 1])
    ax.minorticks_off()
    ax.set_xlabel("energy $E$ (eV)")
    ax.set_ylabel(r"quantum-gravity suppression $(E/E_{Pl})^2$")
    save(fig, __file__, "energy-scale-ladder")


if __name__ == "__main__":
    energy_budget()
    energy_scale_ladder()
