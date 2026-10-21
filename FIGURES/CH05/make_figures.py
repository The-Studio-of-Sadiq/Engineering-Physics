"""Figures for Chapter 5 (spin, many-electron atoms, bonding)."""

import os
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax


def out(fig, slug):
    """Save SVG; also a PNG preview if FIG_PREVIEW_DIR is set (for review only)."""
    prev = os.environ.get("FIG_PREVIEW_DIR")
    if prev:
        fig.tight_layout()
        fig.savefig(pathlib.Path(prev) / f"{slug}.png", dpi=110, bbox_inches="tight")
    save(fig, __file__, slug)


# ---------------------------------------------------------------------------
def penetration_2s_2p():
    """§5.3.2: radial probability r^2|R_nl|^2 for hydrogenic 2s and 2p (Z = 1).

    R_20 = (2 - r/a0) e^{-r/2a0} / (2 sqrt2 a0^{3/2}),
    R_21 = (r/a0) e^{-r/2a0} / (2 sqrt6 a0^{3/2}).
    The inner 2s lobe (r < 2 a0) is the part that penetrates the core.
    """
    r = np.linspace(0, 16, 1200)
    R20 = (2 - r) * np.exp(-r / 2) / (2 * np.sqrt(2))
    R21 = r * np.exp(-r / 2) / (2 * np.sqrt(6))
    P20, P21 = r**2 * R20**2, r**2 * R21**2

    fig, ax = fig_ax()
    ax.plot(r, P20, color=C[0], label=r"$2s$  ($\ell=0$)")
    ax.plot(r, P21, color=C[1], label=r"$2p$  ($\ell=1$)")
    inner = r <= 2
    ax.fill_between(r[inner], 0, P20[inner], color=SHADE, alpha=0.25, lw=0)
    w = np.trapezoid(P20[inner], r[inner])
    ax.text(8.3, 0.125, f"shaded: inner $2s$ lobe,\n{w*100:.0f}% of the probability\nlies inside $r=2a_0$",
            fontsize=9, va="bottom")
    ax.axvline(2, color=GREY, lw=0.8, ls=":")
    ax.text(2.1, 0.19, "2s node", color=GREY, fontsize=8)
    ax.set_xlabel(r"$r\ /\ a_0$")
    ax.set_ylabel(r"$r^2|R_{n\ell}(r)|^2\ \ (a_0^{-1})$")
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 0.21)
    ax.legend(loc="upper right")
    out(fig, "penetration-2s-2p")


# ---------------------------------------------------------------------------
def paschen_back():
    """§5.6.3: hydrogen 2p manifold, H = xi L.S + mu_B B (L_z + 2 S_z).

    Exact diagonalisation in the 6-state |m_l, m_s> basis.  xi is fixed by the
    zero-field 2P_3/2 - 2P_1/2 splitting (3/2) xi hbar^2 = 4.53e-5 eV.
    """
    muB = 5.7884e-5           # eV/T
    dE = 4.53e-5              # eV, fine-structure splitting of 2p
    xi = 2 * dE / 3           # eV (hbar = 1)
    basis = [(ml, ms) for ml in (1, 0, -1) for ms in (0.5, -0.5)]
    n = len(basis)
    LS = np.zeros((n, n))
    Z = np.zeros((n, n))
    for i, (ml, ms) in enumerate(basis):
        LS[i, i] = ml * ms
        Z[i, i] = ml + 2 * ms
        for j, (ml2, ms2) in enumerate(basis):
            # (L+S- + L-S+)/2 off-diagonal terms
            if ml2 == ml + 1 and ms2 == ms - 1:
                v = 0.5 * np.sqrt(2 - ml * (ml + 1)) * np.sqrt(0.75 - ms * (ms - 1))
                LS[j, i] = LS[i, j] = v
    B = np.linspace(0, 3, 601)
    # m_J = m_l + m_s is conserved, so diagonalise each m_J block separately.
    # Energies are measured from the zero-field centre of gravity of 2p.
    fig, ax = fig_ax(w=6.8, h=4.2)
    mj_vals = sorted({ml + ms for ml, ms in basis})
    colors = {1.5: C[0], 0.5: C[2], -0.5: C[4], -1.5: C[3]}
    names = {1.5: "+3/2", 0.5: "+1/2", -0.5: "-1/2", -1.5: "-3/2"}
    for mj in mj_vals:
        idx = [i for i, (ml, ms) in enumerate(basis) if ml + ms == mj]
        ev = np.array([np.linalg.eigvalsh(xi * LS[np.ix_(idx, idx)] + muB * b * Z[np.ix_(idx, idx)])
                       for b in B])
        for k in range(ev.shape[1]):
            ax.plot(B, ev[:, k] / 1e-5, color=colors[mj], lw=1.6,
                    label=f"$m_J={names[mj]}$" if k == 0 else None)
    # strong-field asymptotes  mu_B B (m_l + 2 m_s) + xi m_l m_s
    for ml, ms in basis:
        asym = muB * B * (ml + 2 * ms) + xi * ml * ms
        ax.plot(B, asym / 1e-5, color=GREY, lw=0.7, ls="--")
    end_labels = {(1, 0.5): r"$m_\ell=+1,\ m_s=+\frac{1}{2}$",
                  (0, 0.5): r"$m_\ell=0,\ m_s=+\frac{1}{2}$",
                  (1, -0.5): r"$m_\ell=\pm1,\ m_s=\mp\frac{1}{2}$",
                  (0, -0.5): r"$m_\ell=0,\ m_s=-\frac{1}{2}$",
                  (-1, -0.5): r"$m_\ell=-1,\ m_s=-\frac{1}{2}$"}
    for (ml, ms), lab in end_labels.items():
        y = (muB * 3 * (ml + 2 * ms) + xi * ml * ms) / 1e-5
        ax.text(3.03, y, lab, fontsize=7.5, va="center")
    ax.axvline(dE / muB, color=GREY, lw=0.8, ls=":")
    ax.text(dE / muB + 0.04, 36, r"$B\approx\Delta E_{fs}/\mu_B\approx0.8$ T", fontsize=8, color=GREY)
    ax.text(0.05, 6.0, r"$^2P_{3/2}$, slope $g_J m_J$, $g_J=4/3$", fontsize=8)
    ax.text(0.05, -9.5, r"$^2P_{1/2}$, $g_J=2/3$", fontsize=8)
    ax.plot([], [], color=GREY, lw=0.7, ls="--",
            label=r"$\mu_B B(m_\ell+2m_s)+\xi\hbar^2 m_\ell m_s$")
    ax.set_xlabel(r"$B$ (T)")
    ax.set_ylabel(r"$E$ ($10^{-5}$ eV)")
    ax.set_xlim(0, 3)
    ax.legend(loc="lower left", fontsize=8, ncol=2)
    out(fig, "paschen-back")


# ---------------------------------------------------------------------------
def lcao_h2():
    """§5.8.1: LCAO for H2 along the bond axis, R = 1.4 a0 (H2 equilibrium).

    phi_A,B = e^{-|r - R_A,B|}/sqrt(pi) (a0 = 1); psi_pm = (phi_A pm phi_B)/sqrt(2(1 pm S)),
    S = e^{-R}(1 + R + R^2/3).  Inset: schematic MO levels (antibonding raised
    more than bonding is lowered, because of the 1 pm S denominator).
    """
    R = 1.4
    S = np.exp(-R) * (1 + R + R**2 / 3)
    x = np.linspace(-4.5, 4.5, 1500)
    pA = np.exp(-np.abs(x + R / 2)) / np.sqrt(np.pi)
    pB = np.exp(-np.abs(x - R / 2)) / np.sqrt(np.pi)
    psp = (pA + pB) / np.sqrt(2 * (1 + S))
    psm = (pA - pB) / np.sqrt(2 * (1 - S))

    fig, (a1, a2) = fig_ax(ncols=2, w=10, h=3.8)
    a1.plot(x, pA, color=GREY, lw=1, ls="--", label=r"$\phi^A_{1s}$, $\phi^B_{1s}$")
    a1.plot(x, pB, color=GREY, lw=1, ls="--")
    a1.plot(x, psp, color=C[0], label=r"$\psi_+$ (bonding)")
    a1.plot(x, psm, color=C[1], label=r"$\psi_-$ (antibonding)")
    a1.axhline(0, color=INK, lw=0.6)
    a1.plot([0], [0], "o", ms=5, mfc="white", mec=C[1])
    a1.annotate(r"node of $\psi_-$", xy=(0, 0), xytext=(0.9, -0.42),
                arrowprops=dict(arrowstyle="->", color=INK), fontsize=9)
    a1.set_title(r"Wavefunctions on the bond axis ($R=1.4\,a_0$)")
    a1.set_xlabel(r"$z\ /\ a_0$")
    a1.set_ylabel(r"$\psi\ \ (a_0^{-3/2})$")
    a1.legend(loc="upper left", fontsize=8)
    a1.set_ylim(-0.75, 0.75)

    a2.plot(x, psp**2, color=C[0], label=r"$|\psi_+|^2$")
    a2.plot(x, psm**2, color=C[1], label=r"$|\psi_-|^2$")
    a2.plot(x, (pA**2 + pB**2) / 2, color=GREY, lw=1, ls="--", label=r"$(|\phi^A|^2+|\phi^B|^2)/2$")
    for a in (a1, a2):
        for xn in (-R / 2, R / 2):
            a.axvline(xn, color=GREY, lw=0.6, ls=":")
    a2.text(-R / 2, 0.02, "H", ha="center", fontsize=9)
    a2.text(R / 2, 0.02, "H", ha="center", fontsize=9)
    a2.set_title("Densities: bonding piles charge between nuclei")
    a2.set_xlabel(r"$z\ /\ a_0$")
    a2.set_ylabel(r"$|\psi|^2\ \ (a_0^{-3})$")
    a2.legend(loc="upper left", fontsize=8)
    a2.set_ylim(0, 0.62)

    # inset: MO energy diagram (schematic)
    ins = a2.inset_axes([0.66, 0.46, 0.33, 0.52])
    ins.set_xlim(0, 3)
    ins.set_ylim(-1.3, 1.7)
    ins.axis("off")
    ins.hlines([0, 0], [0.05, 2.35], [0.65, 2.95], color=INK, lw=1.5)
    ins.hlines(-0.8, 1.15, 1.85, color=C[0], lw=2)
    ins.hlines(1.2, 1.15, 1.85, color=C[1], lw=2)
    for xs, ys in (((0.65, 1.15), (0, -0.8)), ((2.35, 1.85), (0, -0.8)),
                   ((0.65, 1.15), (0, 1.2)), ((2.35, 1.85), (0, 1.2))):
        ins.plot(xs, ys, color=GREY, lw=0.6, ls=":")
    ins.text(0.35, 0.12, "1s", ha="center", fontsize=7)
    ins.text(2.65, 0.12, "1s", ha="center", fontsize=7)
    ins.text(1.5, -1.15, r"$E_+$", ha="center", fontsize=7, color=C[0])
    ins.text(1.5, 1.35, r"$E_-$", ha="center", fontsize=7, color=C[1])
    ins.annotate("", xy=(1.42, -0.5), xytext=(1.42, -1.05), arrowprops=dict(arrowstyle="-|>", lw=0.8))
    ins.annotate("", xy=(1.58, -1.05), xytext=(1.58, -0.5), arrowprops=dict(arrowstyle="-|>", lw=0.8))
    out(fig, "lcao-h2plus")


if __name__ == "__main__":
    penetration_2s_2p()
    paschen_back()
    lcao_h2()
