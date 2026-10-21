"""Figures for Example 05 — Navier–Stokes → Fluid network (EXAMPLES/05 Navier-Stokes-to-Fluid-Network.md)."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax

D, L, NU, EPS, G = 0.04, 60.0, 1.0e-6, 0.045e-3, 9.81  # step 5 pipe and water
REL = EPS / D  # 1.125e-3


def colebrook(Re, rel):
    """Solve 1/sqrt(f) = -2 log10(rel/3.7 + 2.51/(Re sqrt f)) by fixed-point iteration."""
    x = np.full_like(np.asarray(Re, float), 8.0)  # x = 1/sqrt(f)
    for _ in range(60):
        x = -2 * np.log10(rel / 3.7 + 2.51 * x / Re)
    return 1 / x**2


def head_loss(Q):
    """Darcy–Weisbach h_f = f (L/D) v^2/(2g), f from Colebrook at Re = vD/nu (Q in m^3/s)."""
    v = Q / (np.pi * D**2 / 4)
    Re = np.maximum(v * D / NU, 1.0)
    f = np.where(Re < 2300, 64 / Re, colebrook(np.maximum(Re, 2300), REL))
    return f * L / D * v**2 / (2 * G)


def moody_colebrook():
    """Step 5: Colebrook f(Re) for eps/D = 1.125e-3 and a smooth pipe; laminar f = 64/Re."""
    Re_l = np.logspace(3, np.log10(2300), 50)
    Re_t = np.logspace(np.log10(3000), 7, 300)
    fig, ax = fig_ax(h=4.0)
    ax.axvspan(2300, 4000, color=GREY, alpha=0.12, lw=0)
    ax.text(3030, 0.0125, "transition", rotation=90, fontsize=8, color=GREY, ha="center")
    ax.loglog(np.logspace(3, np.log10(4000), 50), 64 / np.logspace(3, np.log10(4000), 50),
              color=C[2], ls=":", lw=1.2)
    ax.loglog(Re_l, 64 / Re_l, color=C[2], label="laminar, $f = 64/Re$")
    ax.loglog(Re_t, colebrook(Re_t, REL), color=C[1],
              label=r"Colebrook, $\varepsilon/D = 1.125\times10^{-3}$")
    ax.loglog(Re_t, colebrook(Re_t, 0.0), color=C[0], ls="--", label="Colebrook, smooth pipe")
    f_rough = 0.25 / np.log10(REL / 3.7) ** 2  # Re -> infinity
    ax.axhline(f_rough, color=C[1], lw=0.8, ls=":")
    ax.text(1.1e6, f_rough * 1.04, "fully rough limit",
            fontsize=8, color=C[1])
    # The three iterates of the worked problem, as quoted in the text.
    pts = [(4e4, 0.0251, "guess 1: $v$ = 1 m/s", (1.4e4, 0.052)),
           (1.2e5, 0.0223, "guess 2: $v$ = 3 m/s", (1.6e5, 0.040)),
           (1.38e5, 0.0220, "converged: $v$ = 3.45 m/s", (1.1e6, 0.030))]
    for Re, f, lab, xy in pts:
        ax.plot(Re, f, "o", color=INK, ms=5, zorder=5)
        ax.annotate(f"{lab}\n$Re$ = {Re / 10**np.floor(np.log10(Re)):.3g}$\\times10^{{{int(np.log10(Re))}}}$, $f$ = {f}", (Re, f), xytext=xy,
                    fontsize=8, ha="center", va="bottom",
                    arrowprops=dict(arrowstyle="-", color=GREY, lw=0.7))
    ax.yaxis.set_minor_formatter(plt.NullFormatter())
    ax.set_xlim(1e3, 1e7)
    ax.set_ylim(0.007, 0.08)
    ax.set_yticks([0.008, 0.01, 0.02, 0.03, 0.05, 0.08])
    ax.set_yticklabels(["0.008", "0.01", "0.02", "0.03", "0.05", "0.08"])
    ax.set_xlabel("Reynolds number $Re = vD/\\nu$")
    ax.set_ylabel("Darcy friction factor $f$")
    ax.legend(loc="lower left", fontsize=8.5)
    save(fig, __file__, "moody-colebrook")


def system_curve():
    """Step 5: system curve h_f(Q) for one pipe and two identical pipes in parallel
    (each carries Q/2 at the same head), against the 20 m available head."""
    Q = np.linspace(1e-6, 10e-3, 400)
    h1 = head_loss(Q)
    h2 = head_loss(Q / 2)
    Q1 = np.interp(20.0, h1, Q)
    Q2 = np.interp(20.0, h2, Q)
    fig, ax = fig_ax(h=3.8)
    ax.plot(Q * 1e3, h1, color=C[1], label="one pipe (60 m, 40 mm)")
    ax.plot(Q * 1e3, h2, color=C[0], ls="--", label="two identical pipes in parallel")
    ax.axhline(20, color=GREY, lw=0.9, ls=":")
    ax.text(0.15, 20.8, r"available head $\Delta h$ = 20 m", fontsize=8.5, color=GREY)
    for q, col in ((Q1, C[1]), (Q2, C[0])):
        ax.plot(q * 1e3, 20, "o", color=col, zorder=5)
        ax.plot([q * 1e3] * 2, [0, 20], color=col, lw=0.8, ls=":")
        ax.text(q * 1e3 + 0.12, 2.0, f"{q * 1e3:.2f} L/s", color=col, fontsize=9)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 45)
    ax.set_xlabel("flow rate $Q$ (L/s)")
    ax.set_ylabel("head loss $h_f$ (m)")
    ax.legend(loc="upper left")
    save(fig, __file__, "system-curve")


if __name__ == "__main__":
    moody_colebrook()
    system_curve()
