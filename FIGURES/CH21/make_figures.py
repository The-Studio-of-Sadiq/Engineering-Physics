"""Figures for Chapter 21 — Feedback, Control, and the Cross-Branch Capstone."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax

from scipy import signal
from scipy.optimize import brentq


def L_of(w, K):
    """Loop transfer function L(jw) = K / (jw (jw + 1)(jw + 2))."""
    s = 1j * w
    return K / (s * (s + 1) * (s + 2))


def closed_loop_steps():
    """§21.2.2 — unit-step response of
    T(s) = K wn^2 / (s^2 + 2 zeta0 wn s + (1+K) wn^2),  wn = 1, zeta0 = 0.7,
    for K = 1, 4, 10, 25; steady state K/(1+K) dashed.
    """
    wn, z0 = 1.0, 0.7
    t = np.linspace(0, 15, 1500)
    fig, ax = fig_ax(h=3.8)
    for i, K in enumerate([1, 4, 10, 25]):
        sys_ = signal.lti([K * wn**2], [1, 2 * z0 * wn, (1 + K) * wn**2])
        _, y = signal.step(sys_, T=t)
        zcl = z0 / np.sqrt(1 + K)
        ax.plot(t, y, color=C[i], label=rf"$K={K}$  ($\zeta_{{cl}}={zcl:.2f}$)")
        ax.axhline(K / (1 + K), color=C[i], lw=0.9, ls="--")
    ax.axhline(1, color=GREY, lw=0.8, ls=":")
    ax.text(15, 1.01, "reference = 1", ha="right", va="bottom", fontsize=8, color=GREY)
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 1.6)
    ax.set_xlabel(r"time $\omega_n t$")
    ax.set_ylabel("output $y(t)$")
    ax.set_title(r"P-control of a 2nd-order plant, $\zeta_0=0.7$; dashed: $K/(1+K)$")
    ax.legend(loc="upper right", ncol=2)
    save(fig, __file__, "closed-loop-steps")


def bode_margins():
    """§21.3.3 — Bode plot of L(s) = K/(s(s+1)(s+2)), K = 2.

    Phase crossover w_pc = sqrt(2) where |L| = K/6 -> GM = 20 log10(6/K) = 9.5 dB;
    gain crossover w_gc ~ 0.749 rad/s, PM ~ 32.6 deg.
    """
    K = 2.0
    w = np.logspace(-2, 1.3, 1500)
    Lw = L_of(w, K)
    mag = 20 * np.log10(np.abs(Lw))
    ph = -90 - np.degrees(np.arctan(w)) - np.degrees(np.arctan(w / 2))
    wgc = brentq(lambda x: np.abs(L_of(x, K)) - 1, 0.05, 5)
    wpc = np.sqrt(2)
    pm = 180 + (-90 - np.degrees(np.arctan(wgc)) - np.degrees(np.arctan(wgc / 2)))
    gm = 20 * np.log10(6 / K)

    fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.4, 5.6), sharex=True)
    a1.semilogx(w, mag, color=C[0])
    a1.axhline(0, color=GREY, lw=0.8)
    a1.axvline(wgc, color=C[2], lw=0.8, ls="--")
    a1.axvline(wpc, color=C[1], lw=0.8, ls="--")
    a1.annotate("", xy=(wpc, 0), xytext=(wpc, -gm),
                arrowprops=dict(arrowstyle="<->", color=C[1]))
    a1.text(wpc * 1.1, -gm / 2, f"GM = {gm:.1f} dB", color=C[1], fontsize=9, va="center")
    a1.text(wgc * 0.93, 22, rf"$\omega_{{gc}}={wgc:.2f}$", color=C[2], fontsize=9, ha="right")
    a1.set_ylim(-50, 45)
    a1.set_ylabel(r"$|L(j\omega)|$ [dB]")
    a1.set_title(r"$L(s)=K/[s(s+1)(s+2)]$, $K=2$")

    a2.semilogx(w, ph, color=C[0])
    a2.axhline(-180, color=GREY, lw=0.8)
    a2.axvline(wgc, color=C[2], lw=0.8, ls="--")
    a2.axvline(wpc, color=C[1], lw=0.8, ls="--")
    a2.annotate("", xy=(wgc, -180), xytext=(wgc, -180 + pm),
                arrowprops=dict(arrowstyle="<->", color=C[2]))
    a2.text(wgc * 0.93, -165, f"PM = {pm:.0f}°", color=C[2], fontsize=9, ha="right")
    a2.text(wpc * 1.1, -120, r"$\omega_{pc}=\sqrt{2}$", color=C[1], fontsize=9)
    a2.set_ylim(-270, -90)
    a2.set_yticks([-270, -225, -180, -135, -90])
    a2.set_xlabel(r"$\omega$ [rad/s]")
    a2.set_ylabel(r"$\angle L(j\omega)$ [deg]")
    a2.set_xlim(w[0], w[-1])
    save(fig, __file__, "bode-margins")


def nyquist():
    """§21.3.4 — Nyquist plot of L(jw) = K/(jw(jw+1)(jw+2)) for K = 2 and K = 10.

    Real-axis crossing at w = sqrt(2) is -K/6: -1/3 (no encirclement, stable)
    and -5/3 (two clockwise encirclements of -1: two RHP closed-loop poles).
    """
    w = np.logspace(-2.5, 2, 4000)
    fig, axs = fig_ax(ncols=2, w=10.0, h=4.2)
    for ax, K, lim in [(axs[0], 2, (-2.0, 0.6, -1.6, 1.6)), (axs[1], 10, (-4.0, 1.0, -3.0, 3.0))]:
        Lw = L_of(w, K)
        ax.plot(Lw.real, Lw.imag, color=C[0], label=r"$\omega>0$")
        ax.plot(Lw.real, -Lw.imag, color=C[0], ls="--", label=r"$\omega<0$")
        # direction arrow on the omega > 0 branch
        k = np.searchsorted(w, 1.0)
        ax.annotate("", xy=(Lw[k + 40].real, Lw[k + 40].imag), xytext=(Lw[k].real, Lw[k].imag),
                    arrowprops=dict(arrowstyle="->", color=C[0], lw=1.5))
        ax.plot(-1, 0, "+", color=C[1], ms=12, mew=2)
        ax.text(-1, -0.09 * (lim[3] - lim[2]), "$-1$", color=C[1], ha="center", va="top")
        x = -K / 6
        ax.plot(x, 0, "o", color=INK, ms=4)
        ax.annotate(rf"$-K/6={x:.2f}$ at $\omega=\sqrt{{2}}$", xy=(x, 0),
                    xytext=(x + 0.05 * (lim[1] - lim[0]), -0.35 * (lim[3] - lim[2]) / 2),
                    fontsize=8, arrowprops=dict(arrowstyle="->", color=GREY))
        ax.axhline(0, color=GREY, lw=0.8)
        ax.axvline(0, color=GREY, lw=0.8)
        ax.set_xlim(lim[0], lim[1])
        ax.set_ylim(lim[2], lim[3])
        ax.set_aspect("equal")
        ax.set_xlabel(r"Re $L(j\omega)$")
        ax.set_ylabel(r"Im $L(j\omega)$")
        verdict = "stable: $-1$ not encircled" if K < 6 else "unstable: $-1$ encircled twice"
        ax.set_title(f"$K={K}$ — {verdict}", fontsize=10)
        ax.legend(loc="upper left", fontsize=8)
    save(fig, __file__, "nyquist")


def root_locus():
    """§21.5.1 — root locus of 1 + K/(s(s+1)(s+2)) = 0, i.e. s^3 + 3s^2 + 2s + K = 0.

    Asymptotes at +-60 deg and 180 deg from centroid sigma_a = -1;
    breakaway s = -1 + 1/sqrt(3) = -0.423 (K = 0.385); jw crossing at +-j sqrt(2), K = 6.
    """
    Ks = np.concatenate([np.linspace(0, 0.3849, 400), np.logspace(np.log10(0.385), 2.5, 1500)])
    roots = np.array([np.sort_complex(np.roots([1, 3, 2, K])) for K in Ks])
    fig, ax = fig_ax(h=4.6, w=6.0)
    pts = roots.ravel()
    ax.plot(pts.real, pts.imag, ".", color=C[0], ms=1.6)
    for p in [0, -1, -2]:
        ax.plot(p, 0, "x", color=INK, ms=9, mew=2)
    r = np.linspace(0, 6, 2)
    for ang in [60, -60, 180]:
        a = np.radians(ang)
        ax.plot(-1 + r * np.cos(a), r * np.sin(a), color=GREY, lw=0.9, ls="--")
    ax.plot(-1, 0, "D", color=GREY, ms=4)
    ax.text(-1.05, -0.35, r"centroid $\sigma_a=-1$", fontsize=8, ha="right", color=GREY)
    sb = -1 + 1 / np.sqrt(3)
    ax.plot(sb, 0, "o", color=C[1], ms=6, zorder=5)
    ax.annotate(rf"breakaway $s={sb:.3f}$", xy=(sb, 0), xytext=(-3.8, -1.0), fontsize=8,
                color=C[1], arrowprops=dict(arrowstyle="->", color=C[1]))
    for sgn in [1, -1]:
        ax.plot(0, sgn * np.sqrt(2), "s", color=C[2], ms=6, zorder=5)
    ax.annotate(r"$\pm j\sqrt{2}$ at $K=6$", xy=(0, np.sqrt(2)), xytext=(-3.0, 1.75),
                fontsize=8, color=C[2], arrowprops=dict(arrowstyle="->", color=C[2]))
    ax.text(-3.8, 2.55, "dashed: asymptotes at ±60°, 180°", fontsize=8, color=GREY)
    ax.axhline(0, color=GREY, lw=0.8)
    ax.axvline(0, color=INK, lw=0.8)
    ax.set_xlim(-4, 1.5)
    ax.set_ylim(-3, 3)
    ax.set_aspect("equal")
    ax.set_xlabel(r"Re $s$")
    ax.set_ylabel(r"Im $s$")
    ax.set_title(r"Root locus of $K/[s(s+1)(s+2)]$, $0<K<300$")
    save(fig, __file__, "root-locus")


if __name__ == "__main__":
    closed_loop_steps()
    bode_margins()
    nyquist()
    root_locus()
