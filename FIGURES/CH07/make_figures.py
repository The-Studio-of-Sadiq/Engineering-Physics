"""Figures for Chapter 7 (quantum Hall effect, superconductivity, SQUID)."""

import os
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax
from scipy.integrate import quad
from scipy.optimize import brentq


def out(fig, slug):
    """Save SVG; also a PNG preview if FIG_PREVIEW_DIR is set (for review only)."""
    prev = os.environ.get("FIG_PREVIEW_DIR")
    if prev:
        fig.tight_layout()
        fig.savefig(pathlib.Path(prev) / f"{slug}.png", dpi=110, bbox_inches="tight")
    save(fig, __file__, slug)


# ---------------------------------------------------------------------------
def quantum_hall():
    """§7.3.2: integer quantum Hall effect, phenomenological illustration.

    n = 3e15 m^-2, filling factor nu = n h / (e B).  Plateaus rho_xy = R_K / i,
    R_K = h/e^2 = 25812.807 Ohm, with a disorder-smoothed staircase
    i(nu) = sum_j 1/(1 + exp(-(nu - j + 1/2)/w)), w = 0.035 nu (broadening grows
    with nu so the classical line rho_xy = B/(n e) is recovered at low field).
    rho_xx (arb. units) is taken proportional to d i / d nu: zero on plateaus,
    peaked between them.  Spin-resolved levels (every integer nu) assumed.
    """
    h, e = 6.62607015e-34, 1.602176634e-19
    RK = h / e**2
    n = 3e15
    B = np.linspace(0.3, 16, 4000)
    nu = n * h / (e * B)
    w = 0.035 * nu
    j = np.arange(1, 200)[:, None]
    z = (nu - j + 0.5) / w
    step = 1 / (1 + np.exp(-np.clip(z, -60, 60)))
    filled = step.sum(axis=0)
    dstep = (step * (1 - step) / w).sum(axis=0)

    fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.6, 5.2), sharex=True,
                                 gridspec_kw=dict(height_ratios=[2, 1]))
    a1.plot(B, RK / filled / 1e3, color=C[0], label=r"$\rho_{xy}$ (illustrative)")
    a1.plot(B, B / (n * e) / 1e3, color=GREY, ls="--", lw=1, label=r"classical $B/ne$")
    for i in range(1, 5):
        a1.axhline(RK / i / 1e3, color=GREY, lw=0.5, ls=":")
        a1.text(16.2, RK / i / 1e3, fr"$R_K/{i}$", va="center", fontsize=8)
    a1.set_ylabel(r"$\rho_{xy}$ (k$\Omega$)")
    a1.set_ylim(0, 30)
    a1.legend(loc="upper left", fontsize=8)
    a1.set_title(r"2DEG, $n=3\times10^{15}$ m$^{-2}$, $R_K=h/e^2=25\,812.807\ \Omega$")
    a2.plot(B, dstep, color=C[1], label=r"$\rho_{xx}$ (arb. units)")
    for i in range(1, 4):
        Bi = n * h / (e * i)
        a1.text(Bi, RK / i / 1e3 + 0.8, fr"$\nu={i}$", ha="center", fontsize=8, color=C[0])
    a2.set_ylim(0, 6)
    a2.set_ylabel(r"$\rho_{xx}$ (arb.)")
    a2.set_xlabel(r"$B$ (T)")
    a2.set_xlim(0, 16)
    a2.legend(loc="upper left", fontsize=8)
    out(fig, "quantum-hall")


# ---------------------------------------------------------------------------
def bcs_gap():
    """§7.6.2: weak-coupling BCS gap Delta(T)/Delta(0) versus T/Tc.

    Dimensionless gap equation (cutoff eliminated using the T = 0 solution):
        ln(Delta0/Delta) = 2 * int_0^inf dxi f(E)/E,  E = sqrt(xi^2 + Delta^2),
    with f the Fermi function and k_B T = (T/Tc) * Delta0 / 1.764.
    Near Tc:  Delta/Delta0 -> 1.74 sqrt(1 - T/Tc).
    """
    r = np.pi / np.exp(np.euler_gamma)       # Delta0 / (k_B Tc) = 1.764

    def rhs(d, t):
        kT = t / r
        f = lambda x: 1 / (np.exp(np.sqrt(x * x + d * d) / kT) + 1) / np.sqrt(x * x + d * d)
        return 2 * quad(f, 0, 50 * kT + 5, limit=200)[0]

    t = np.concatenate([np.linspace(0.02, 0.9, 45), np.linspace(0.905, 0.9995, 40)])
    d = np.array([brentq(lambda dd: np.log(1 / dd) - rhs(dd, ti), 1e-6, 1.0) for ti in t])
    t = np.concatenate([[0.0], t, [1.0]])
    d = np.concatenate([[1.0], d, [0.0]])

    fig, ax = fig_ax(w=6.0, h=3.8)
    ax.plot(t, d, color=C[0], label="BCS gap equation (numerical)")
    tt = np.linspace(0.55, 1, 200)
    ax.plot(tt, 1.74 * np.sqrt(1 - tt), color=C[1], ls="--", lw=1.3,
            label=r"near $T_c$: $1.74\sqrt{1-T/T_c}$")
    ax.text(0.05, 0.25, r"$\Delta(0)=1.764\,k_BT_c$" "\n" r"$2\Delta(0)/k_BT_c=3.53$", fontsize=9)
    ax.set_xlim(0, 1.05)
    ax.set_ylim(0, 1.12)
    ax.set_xlabel(r"$T/T_c$")
    ax.set_ylabel(r"$\Delta(T)/\Delta(0)$")
    ax.legend(loc="lower left", fontsize=8, bbox_to_anchor=(0.0, 0.42))
    out(fig, "bcs-gap")


# ---------------------------------------------------------------------------
def landau_gl_free_energy():
    """§7.6.3: Ginzburg-Landau free energy F = a0 (T - Tc) |Delta|^2 + b |Delta|^4.

    Slice along Re(Delta) (Im Delta = 0) for T/Tc = 1.2, 1.0, 0.8, 0.5,
    with a0 = b = 1 (units a0 Tc for F).  Minima at |Delta| = sqrt(-a/2b).
    """
    x = np.linspace(-0.75, 0.75, 600)
    fig, ax = fig_ax(w=6.2, h=3.9)
    for tr, col in zip((1.2, 1.0, 0.8, 0.5), (C[3], C[4], C[2], C[0])):
        a = tr - 1.0
        F = a * x**2 + x**4
        ax.plot(x, F, color=col, label=fr"$T/T_c={tr}$")
        if a < 0:
            xm = np.sqrt(-a / 2)
            Fm = -a * a / 4
            ax.plot([-xm, xm], [Fm, Fm], "o", color=col, ms=5)
    xm = np.sqrt(0.5 / 2)
    ax.annotate(r"$|\Delta|=\sqrt{-a/2b}$", xy=(xm, -0.0625), xytext=(0.42, -0.11),
                arrowprops=dict(arrowstyle="->", color=INK), fontsize=9)
    ax.axhline(0, color=INK, lw=0.6)
    ax.set_xlim(-0.75, 0.75)
    ax.set_ylim(-0.13, 0.2)
    ax.set_xlabel(r"order parameter $\mathrm{Re}\,\Delta$ (slice at $\mathrm{Im}\,\Delta=0$)")
    ax.set_ylabel(r"$F - F_n$ (arb. units)")
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), fontsize=8, ncol=4)
    out(fig, "landau-gl-free-energy")


# ---------------------------------------------------------------------------
def squid_ic():
    """§7.8.3: dc-SQUID critical current I_c(Phi) = 2 I_c0 |cos(pi Phi/Phi0)|."""
    p = np.linspace(-3, 3, 2000)
    fig, ax = fig_ax(w=6.2, h=3.2)
    ax.plot(p, 2 * np.abs(np.cos(np.pi * p)), color=C[0])
    ax.annotate("", xy=(1, 2.12), xytext=(0, 2.12),
                arrowprops=dict(arrowstyle="<->", color=C[1], lw=1))
    ax.text(0.5, 2.18, r"period $\Phi_0=h/2e$", ha="center", fontsize=9, color=C[1])
    ax.set_xlim(-3, 3)
    ax.set_ylim(0, 2.45)
    ax.set_xlabel(r"applied flux $\Phi/\Phi_0$")
    ax.set_ylabel(r"$I_c\ /\ I_{c0}$")
    out(fig, "squid-ic")


if __name__ == "__main__":
    quantum_hall()
    bcs_gap()
    landau_gl_free_energy()
    squid_ic()
