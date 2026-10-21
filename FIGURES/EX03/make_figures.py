"""Figures for Example 03 — Maxwell → Circuit (EXAMPLES/03 Maxwell-to-Circuit.md)."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax

R_S, CAP = 2.2e3, 10e-9   # series resistor and shunt capacitor (step 5)
C0 = 299_792_458.0


def rc_loading_bode():
    """Step 5: RC low-pass loaded by the scope input R_L across C.

    Thevenin: H(jw) = [R_L/(R+R_L)] / (1 + j w R_eq C),  R_eq = R || R_L.
    Unloaded: f_c = 1/(2 pi R C) = 7.2 kHz; 1 MOhm: ~unchanged; 50 Ohm: 325 kHz at -33 dB.
    """
    f = np.logspace(1, 7, 600)
    w = 2 * np.pi * f
    cases = [("unloaded", np.inf, C[0], "-"),
             (r"1 M$\Omega$ scope", 1e6, C[2], "--"),
             (r"50 $\Omega$ scope", 50.0, C[1], "-")]
    fig, (am, ap) = fig_ax(nrows=2, h=2.6, sharex=True)
    for label, RL, col, ls in cases:
        k = 1.0 if np.isinf(RL) else RL / (R_S + RL)
        Req = R_S if np.isinf(RL) else R_S * RL / (R_S + RL)
        H = k / (1 + 1j * w * Req * CAP)
        fc = 1 / (2 * np.pi * Req * CAP)
        am.semilogx(f, 20 * np.log10(abs(H)), color=col, ls=ls,
                    label=f"{label}: $f_c$ = {fc / 1e3:.2f} kHz" if fc < 1e5
                    else f"{label}: $f_c$ = {fc / 1e3:.1f} kHz, flat gain {20 * np.log10(k):.0f} dB")
        ap.semilogx(f, np.degrees(np.angle(H)), color=col, ls=ls)
        am.plot(fc, 20 * np.log10(k) - 3.01, "o", color=col, ms=4)
        ap.plot(fc, -45, "o", color=col, ms=4)
    am.set_ylabel("|H| (dB)")
    am.set_ylim(-80, 5)
    am.legend(loc="lower left", fontsize=8.5)
    ap.set_ylabel("phase (deg)")
    ap.set_yticks([0, -45, -90])
    ap.set_xlabel("frequency $f$ (Hz)")
    ap.set_xlim(10, 1e7)
    save(fig, __file__, "rc-loading-bode")


def lumped_limit_fr4():
    """Step 6: L/lambda = L f sqrt(eps_eff)/c on FR-4 microstrip, eps_eff = 3.25."""
    eps = 3.25
    f = np.logspace(7, np.log10(5e9), 400)
    lam = C0 / (f * np.sqrt(eps))
    fig, ax = fig_ax(h=3.8)
    for L, col in [(0.01, C[2]), (0.10, C[0]), (0.30, C[1])]:
        ax.loglog(f, L / lam, color=col, label=f"trace length {L * 100:.0f} cm")
    for y, txt in [(0.1, r"$L/\lambda = 0.1$"),
                   (0.25, r"$L/\lambda = 0.25$ ($\lambda/4$)")]:
        ax.axhline(y, color=GREY, lw=0.9, ls="--")
        ax.text(1.15e7, y * 1.12, txt, fontsize=8.5, color=GREY)
    f0 = 500e6
    r = 0.10 * f0 * np.sqrt(eps) / C0
    ax.plot(f0, r, "o", color=INK, zorder=5)
    ax.annotate(f"10 cm at 500 MHz:\n$L/\\lambda$ = {r:.2f}", (f0, r), xytext=(1.2e8, 1.1),
                fontsize=9, arrowprops=dict(arrowstyle="-", color=GREY, lw=0.7))
    ax.set_xlim(1e7, 5e9)
    ax.set_ylim(3e-4, 5)
    ax.set_xlabel("frequency $f$ (Hz)")
    ax.set_ylabel(r"electrical length $L/\lambda$")
    ax.legend(loc="lower right")
    save(fig, __file__, "lumped-limit-fr4")


if __name__ == "__main__":
    rc_loading_bode()
    lumped_limit_fr4()
