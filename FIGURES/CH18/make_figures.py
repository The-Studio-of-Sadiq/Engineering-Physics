"""Figures for Chapter 18 — EEE Systems: Circuits, Devices, and Signals."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax

from scipy import signal

VT = 0.025852  # k_B T / e at 300 K [V]


def diode_iv():
    """§18.3.1 — diode law I = I0 (exp(V/(eta VT)) - 1), eta = 1 and 2.

    Left: linear current, -1..0.8 V, with a schematic reverse-breakdown knee.
    Right: log|I| in forward bias, showing eta VT ln10 = 60 / 120 mV per decade.
    """
    cases = [(1, 1e-12, C[0]), (2, 1e-9, C[1])]  # (eta, I0 [A], colour)
    VBR = 0.9  # schematic breakdown voltage [V], not to scale

    fig, (a1, a2) = fig_ax(ncols=2, w=10.0, h=3.8)

    V = np.linspace(-1.0, 0.8, 2000)
    for eta, I0, col in cases:
        I = I0 * np.expm1(V / (eta * VT))
        # schematic avalanche knee: steep exponential below -VBR
        I = I - 1e-3 * np.expm1(np.clip(-(V + VBR) / 0.012, 0, None))
        a1.plot(V, I * 1e3, color=col, label=rf"$\eta={eta}$, $I_0=10^{{{round(np.log10(I0))}}}$ A")
    a1.set_xlim(-1.0, 0.8)
    a1.set_ylim(-10, 10)
    a1.axhline(0, color=GREY, lw=0.8)
    a1.axvline(0, color=GREY, lw=0.8)
    a1.set_xlabel(r"$V_D$ [V]")
    a1.set_ylabel(r"$I_D$ [mA]")
    a1.annotate("breakdown\n(schematic,\n$V_{BR}$ not to scale)", xy=(-0.93, -6),
                xytext=(-0.78, -7.5), fontsize=8, color=INK,
                arrowprops=dict(arrowstyle="->", color=GREY))
    a1.text(-0.55, 0.7, r"reverse: $I_D\approx -I_0$ (invisible here)", fontsize=8, color=INK)
    a1.legend(loc="upper left")
    a1.set_title("Linear scale")

    Vf = np.linspace(0.0, 0.8, 400)
    for eta, I0, col in cases:
        I = I0 * np.expm1(Vf / (eta * VT))
        a2.semilogy(Vf, np.abs(I), color=col, label=rf"$\eta={eta}$")
        s = eta * VT * np.log(10) * 1e3
        v0 = 0.45 if eta == 1 else 0.55
        i0 = I0 * np.exp(v0 / (eta * VT))
        a2.annotate(f"≈{10*round(s/10):.0f} mV/decade", xy=(v0, i0),
                    xytext=(v0 - 0.33 if eta == 1 else v0 + 0.02, i0 * (30 if eta == 1 else 1 / 80)),
                    fontsize=8, color=col, arrowprops=dict(arrowstyle="->", color=col))
    a2.set_xlim(0, 0.8)
    a2.set_ylim(1e-13, 1e0)
    a2.set_xlabel(r"$V_D$ [V]")
    a2.set_ylabel(r"$|I_D|$ [A]")
    a2.legend(loc="lower right")
    a2.set_title("Log scale (forward bias)")
    save(fig, __file__, "diode-iv")


def mosfet_output():
    """§18.3.3 — NMOS output characteristics I_D(V_DS) for V_GS = 1..3 V.

    Triode:     I_D = k[(V_GS-Vth)V_DS - V_DS^2/2](1 + lam V_DS)
    Saturation: I_D = (k/2)(V_GS-Vth)^2 (1 + lam V_DS),  k = mu_n Cox W/L.
    Vth = 0.7 V, lam = 0.05 /V, k = 1 mA/V^2.
    """
    k, Vth, lam = 1e-3, 0.7, 0.05
    VDS = np.linspace(0, 4, 600)
    fig, ax = fig_ax(h=3.8)
    for i, VGS in enumerate([1.0, 1.5, 2.0, 2.5, 3.0]):
        Vov = VGS - Vth
        tri = k * (Vov * VDS - VDS**2 / 2)
        sat = 0.5 * k * Vov**2 * np.ones_like(VDS)
        ID = np.where(VDS < Vov, tri, sat) * (1 + lam * VDS)
        ax.plot(VDS, ID * 1e3, color=C[i % len(C)])
        ax.text(4.03, ID[-1] * 1e3, rf"$V_{{GS}}={VGS:g}$ V", va="center", fontsize=8,
                color=C[i % len(C)])
    Vb = np.linspace(0, 3.0 - Vth, 200)
    ax.plot(Vb, 0.5 * k * Vb**2 * (1 + lam * Vb) * 1e3, "--", color=GREY, lw=1.2)
    ax.text(1.55, 2.75, r"$V_{DS}=V_{GS}-V_{th}$", color=GREY, fontsize=9, ha="right")
    ax.text(0.25, 1.6, "triode", fontsize=9, color=INK)
    ax.text(3.0, 1.6, "saturation", fontsize=9, color=INK)
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 3.3)
    ax.set_xlabel(r"$V_{DS}$ [V]")
    ax.set_ylabel(r"$I_D$ [mA]")
    ax.set_title(r"NMOS: $V_{th}=0.7$ V, $\mu_nC_{ox}W/L=1$ mA/V$^2$, $\lambda=0.05$ V$^{-1}$")
    save(fig, __file__, "mosfet-output")


def filter_responses():
    """§18.5.3 — |H(jw)| of 4th-order analog low-pass prototypes (w_c = 1).

    Butterworth (-3 dB at w_c), Chebyshev I (1 dB ripple, edge w_c),
    Bessel (magnitude-normalised, -3 dB at w_c), elliptic (1 dB / 40 dB).
    """
    w = np.logspace(-1, 1, 2000)
    protos = [
        ("Butterworth", signal.butter(4, 1, analog=True)),
        ("Chebyshev I (1 dB)", signal.cheby1(4, 1, 1, analog=True)),
        ("Bessel", signal.bessel(4, 1, analog=True, norm="mag")),
        ("Elliptic (1 dB, 40 dB)", signal.ellip(4, 1, 40, 1, analog=True)),
    ]
    fig, ax = fig_ax(h=3.8)
    for i, (name, (b, a)) in enumerate(protos):
        _, h = signal.freqs(b, a, worN=w)
        ax.semilogx(w, 20 * np.log10(np.maximum(np.abs(h), 1e-12)), color=C[i], label=name)
    ax.axvline(1, color=GREY, lw=0.8, ls=":")
    ax.axhline(-40, color=GREY, lw=0.8, ls=":")
    ax.text(0.105, -38, "−40 dB stopband floor (elliptic)", fontsize=8, color=GREY)
    ax.set_xlim(0.1, 10)
    ax.set_ylim(-100, 5)
    ax.set_xlabel(r"$\omega/\omega_c$")
    ax.set_ylabel(r"$|H(j\omega)|$ [dB]")
    ax.set_title("4th-order analog low-pass prototypes")
    ax.legend(loc="lower left")
    save(fig, __file__, "filter-responses")


def converter_gain():
    """§18.8.2 — ideal CCM conversion ratios vs duty cycle D.

    Buck D, boost 1/(1-D), buck-boost |D/(1-D)| (output inverted).
    """
    D = np.linspace(0, 0.95, 500)
    fig, ax = fig_ax(h=3.6)
    ax.plot(D, D, color=C[0], label=r"buck: $D$")
    ax.plot(D, 1 / (1 - D), color=C[1], label=r"boost: $1/(1-D)$")
    ax.plot(D, D / (1 - D), color=C[2], label=r"buck-boost: $|{-D}/(1-D)|$")
    ax.axhline(1, color=GREY, lw=0.8, ls=":")
    ax.axvline(0.5, color=GREY, lw=0.8, ls=":")
    ax.text(0.51, 4.6, "buck-boost: $|V_{out}|=V_{in}$ at $D=0.5$", fontsize=8, color=GREY)
    ax.set_xlim(0, 0.95)
    ax.set_ylim(0, 6)
    ax.set_xlabel(r"duty cycle $D = t_{on}/T_{sw}$")
    ax.set_ylabel(r"$|V_{out}/V_{in}|$")
    ax.set_title("Ideal switching-converter gain (continuous conduction)")
    ax.legend(loc="upper left")
    save(fig, __file__, "converter-gain")


if __name__ == "__main__":
    diode_iv()
    mosfet_output()
    filter_responses()
    converter_gain()
