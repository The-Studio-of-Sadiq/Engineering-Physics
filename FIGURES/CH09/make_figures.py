"""Figures for Chapter 9 (Bridge B.a: quantum -> classical mechanics)."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax

from numpy.polynomial.hermite import hermval
from math import factorial


def stationary_phase():
    """§9.2.2 Stationary phase: Re exp(iS/hbar) for S(x) = (x - x0)^2, x0 = 0,
    at hbar = 1, 0.1, 0.01. Only the neighbourhood |x - x0| ~ sqrt(hbar) adds
    coherently; elsewhere the integrand oscillates and cancels."""
    x = np.linspace(-2.0, 2.0, 40001)
    fig, axes = fig_ax(nrows=3, h=1.55, sharex=True)
    for ax, hbar, col in zip(axes, [1.0, 0.1, 0.01], C):
        w = np.sqrt(np.pi * hbar)
        ax.axvspan(-w, w, color=SHADE, alpha=0.12, lw=0)
        ax.plot(x, np.cos(x**2 / hbar), color=col, lw=0.8 if hbar < 0.05 else 1.4)
        ax.set_ylim(-1.25, 1.25)
        ax.set_yticks([-1, 0, 1])
        ax.set_ylabel(r"Re $e^{iS/\hbar}$")
        ax.text(1.98, 1.22, rf"$\hbar = {hbar:g}$", ha="right", va="top",
                fontsize=9, bbox=dict(fc="white", ec="none", pad=1.5))
    axes[0].text(0, -1.22, r"$|x-x_0|<\sqrt{\pi\hbar}$", ha="center", va="bottom",
                 fontsize=8, color=SHADE)
    axes[-1].set_xlabel(r"path parameter $x$  (action $S=(x-x_0)^2$, $x_0=0$)")
    return fig


def wkb_vs_exact():
    """§9.3.3 Validity criterion: exact harmonic-oscillator psi_6 vs the WKB form
    C/sqrt(p) cos(int p dx/hbar - pi/4), with hbar = m = omega = 1, E = 6.5.
    Turning points x = ±sqrt(13); WKB diverges there (p -> 0)."""
    n, E = 6, 6.5
    a = np.sqrt(2 * E)
    x = np.linspace(-6, 6, 4001)
    coef = np.zeros(n + 1); coef[n] = 1
    psi = hermval(x, coef) * np.exp(-x**2 / 2) / np.sqrt(2.0**n * factorial(n) * np.sqrt(np.pi))

    Cn = np.sqrt(2 / np.pi)                     # normalises the oscillatory WKB form
    inside = np.abs(x) < a
    xi = x[inside]
    p = np.sqrt(2 * E - xi**2)
    phase = 0.5 * (xi * p + 2 * E * np.arcsin(xi / a)) + E * np.pi / 2  # int_{-a}^{x} p dx'
    wkb_in = Cn / np.sqrt(p) * np.cos(phase - np.pi / 4)
    xo = x[~inside]
    kap = np.sqrt(xo**2 - 2 * E)
    integ = 0.5 * (np.abs(xo) * kap - 2 * E * np.log((np.abs(xo) + kap) / a))  # int_a^|x| kappa
    wkb_out = Cn / (2 * np.sqrt(kap)) * np.exp(-integ)

    fig, ax = fig_ax(h=3.4)
    for s in (-1, 1):
        ax.axvspan(s * a, s * 6.2, color=GREY, alpha=0.12, lw=0)
        ax.axvline(s * a, color=GREY, ls="--", lw=1)
    ax.plot(x, psi, color=INK, lw=2.2, label=r"exact $\psi_6(x)$")
    ax.plot(xi, wkb_in, color=C[1], lw=1.4, ls="-", label="WKB (allowed region)")
    for side in (xo < 0, xo > 0):
        ax.plot(xo[side], wkb_out[side], color=C[0], lw=1.4,
                label="WKB (forbidden region)" if side[0] else None)
    ax.set_ylim(-0.75, 0.75)
    ax.set_xlim(-6, 6)
    ax.text(a, 0.70, r" turning point $x=+\sqrt{13}$", fontsize=8, va="top", color=GREY)
    ax.text(-a, 0.70, r"$x=-\sqrt{13}$ ", fontsize=8, va="top", ha="right", color=GREY)
    ax.text(5.0, -0.45, "classically\nforbidden", fontsize=8, ha="center", color=GREY)
    ax.text(-5.0, -0.45, "classically\nforbidden", fontsize=8, ha="center", color=GREY)
    ax.set_xlabel(r"$x\;/\;\sqrt{\hbar/m\omega}$")
    ax.set_ylabel(r"$\psi(x)$")
    ax.legend(loc="lower center", ncol=3, fontsize=8, bbox_to_anchor=(0.5, -0.02))
    return fig


def pendulum_phase_portrait():
    """§9.6.1 Phase space: contours of H = p^2/(2 m l^2) - m g l cos(theta),
    zero of energy at the pivot height. Units m = l = g = 1, p in m l^2 sqrt(g/l).
    Separatrix H = +mgl (2mgl above the bottom of the well)."""
    th = np.linspace(-2 * np.pi, 2 * np.pi, 801)
    pp = np.linspace(-3.2, 3.2, 641)
    TH, P = np.meshgrid(th, pp)
    H = P**2 / 2 - np.cos(TH)

    fig, ax = fig_ax(h=3.8)
    ax.contour(TH, P, H, levels=[-0.9, -0.6, -0.2, 0.3, 0.7], colors=C[0], linewidths=1.1, linestyles="solid", negative_linestyles="solid")
    ax.contour(TH, P, H, levels=[1.6, 2.6, 4.0], colors=C[1], linewidths=1.1)
    ax.contour(TH, P, H, levels=[1.0], colors=INK, linewidths=2.4)

    # flow arrows: theta_dot = p, p_dot = -sin(theta)
    qt, qp = np.meshgrid(np.linspace(-2 * np.pi, 2 * np.pi, 17), np.linspace(-2.8, 2.8, 9))
    u, v = qp, -np.sin(qt)
    nrm = np.hypot(u, v) + 1e-9
    ax.quiver(qt, qp, u / nrm, v / nrm, color=GREY, alpha=0.55, scale=38, width=0.0035)

    for k in (-1, 1):
        ax.plot(k * np.pi, 0, "o", ms=6, mfc="white", mec=INK, zorder=5)
    for k in (-2, 0, 2):
        ax.plot(k * np.pi, 0, "o", ms=5, color=INK, zorder=5)
    ax.text(np.pi, -0.35, "unstable\n(inverted)", ha="center", va="top", fontsize=8,
            bbox=dict(fc="white", ec="none", pad=1))
    ax.text(0, 0.95, "libration", ha="center", fontsize=9, color=C[0],
            bbox=dict(fc="white", ec="none", pad=1))
    ax.text(-np.pi, 2.75, "rotation", ha="center", fontsize=9, color=C[1],
            bbox=dict(fc="white", ec="none", pad=1))
    ax.annotate(r"separatrix $H=+mg\ell$", xy=(-np.pi / 2, -np.sqrt(2)),
                xytext=(-5.4, -2.6), fontsize=9,
                arrowprops=dict(arrowstyle="->", color=INK, lw=0.8))
    ax.set_xticks(np.arange(-2, 3) * np.pi)
    ax.set_xticklabels([r"$-2\pi$", r"$-\pi$", "0", r"$\pi$", r"$2\pi$"])
    ax.set_xlim(-2 * np.pi, 2 * np.pi)
    ax.set_ylim(-3.2, 3.2)
    ax.set_xlabel(r"angle $\theta$")
    ax.set_ylabel(r"$p_\theta\;/\;m\ell^2\sqrt{g/\ell}$")
    return fig


def main():
    save(stationary_phase(), __file__, "stationary-phase")
    save(wkb_vs_exact(), __file__, "wkb-vs-exact")
    save(pendulum_phase_portrait(), __file__, "pendulum-phase-portrait")


if __name__ == "__main__":
    main()
