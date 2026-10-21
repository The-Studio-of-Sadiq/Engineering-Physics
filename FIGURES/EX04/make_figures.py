"""Figures for Example 04 — Heat equation → Thermal RC (EXAMPLES/04 Heat-Equation-to-Thermal-RC.md)."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax


def step2(z, t):
    """Unit-step response of w_n^2/(s^2 + 2 zeta w_n s + w_n^2), w_n = 1, 0 < zeta < 1."""
    wd = np.sqrt(1 - z**2)
    return 1 - np.exp(-z * t) * (np.cos(wd * t) + z / wd * np.sin(wd * t))


def first_vs_second_order():
    """Step 4: first-order 1/(1 + s/w_c) vs second-order 1/(s^2/w_n^2 + 2 zeta s/w_n + 1).

    Panel 1: unit-step responses against w_c t (w_c = 1/tau = w_n); zeta = 0.2, 0.7.
    Panel 2: phase vs w/w_c — the first order never passes -90 deg, the second reaches -180 deg.
    """
    t = np.linspace(0, 12, 1200)
    w = np.logspace(-2, 2, 600)
    seconds = [(z, step2(z, t)) for z in (0.2, 0.7)]

    fig, (a1, a2) = fig_ax(ncols=2, h=3.6)
    a1.plot(t, 1 - np.exp(-t), color=C[1], lw=2.2, label="first order (thermal RC)")
    for (z, y2), col in zip(seconds, (C[0], C[5])):
        a1.plot(t, y2, color=col, ls="--" if z == 0.7 else "-",
                label=rf"second order, $\zeta$ = {z}")
    a1.axhline(1, color=GREY, lw=0.8, ls=":")
    a1.annotate("thermal: no overshoot", xy=(3.0, 0.95), xytext=(5.2, 0.45), color=C[1],
                fontsize=9, arrowprops=dict(arrowstyle="-", color=C[1], lw=0.8))
    a1.set_xlabel(r"normalised time $\omega_c t$")
    a1.set_ylabel("step response")
    a1.set_xlim(0, 12)
    a1.set_ylim(0, 1.65)
    a1.legend(loc="upper right", fontsize=8.5)

    a2.semilogx(w, np.degrees(np.angle(1 / (1 + 1j * w))), color=C[1], lw=2.2, label="first order")
    for (z, _), col in zip(seconds, (C[0], C[5])):
        H = 1 / (1 - w**2 + 2j * z * w)
        a2.semilogx(w, np.degrees(np.unwrap(np.angle(H))), color=col,
                    ls="--" if z == 0.7 else "-", label=rf"second order, $\zeta$ = {z}")
    for y in (-90, -180):
        a2.axhline(y, color=GREY, lw=0.8, ls=":")
    a2.text(0.012, -84, "first-order limit −90°", fontsize=8.5, color=C[1])
    a2.text(0.012, -174, "−180° point (Ziegler–Nichols)", fontsize=8.5, color=GREY)
    a2.set_yticks([0, -45, -90, -135, -180])
    a2.set_ylim(-190, 5)
    a2.set_xlabel(r"normalised frequency $\omega/\omega_c$")
    a2.set_ylabel("phase (deg)")
    a2.legend(loc="upper right", fontsize=8.5)
    save(fig, __file__, "first-vs-second-order")


def thermal_cooldown():
    """Step 5: lumped cooling T(t) = T_inf + (T0 - T_inf) e^{-t/tau}, T_inf = 20 C, T0 = 80 C,
    tau = RC = (1/3 K/W)(2900 J/K) = 967 s."""
    tau = 2900 / (50 * 6e-2)
    t = np.linspace(0, 5000, 600)
    T = 20 + 60 * np.exp(-t / tau)
    fig, ax = fig_ax(h=3.6)
    ax.plot(t, T, color=C[1], label=rf"$T(t) = 20 + 60\,e^{{-t/{tau:.0f}\,\mathrm{{s}}}}$")
    ax.axhline(20, color=GREY, lw=0.8, ls=":")
    ax.text(4950, 21.5, r"ambient $T_\infty$ = 20 °C", ha="right", fontsize=8.5, color=GREY)
    T60 = 20 + 60 * np.exp(-60 / tau)
    Ttau = 20 + 60 / np.e
    ax.plot(60, T60, "o", color=INK)
    ax.annotate(f"t = 60 s: {T60:.1f} °C\n(only 6% of excess shed)", (60, T60),
                xytext=(500, 70), fontsize=9,
                arrowprops=dict(arrowstyle="-", color=GREY, lw=0.7))
    ax.plot(tau, Ttau, "o", color=INK)
    ax.plot([tau, tau], [0, Ttau], color=GREY, lw=0.8, ls="--")
    ax.annotate(rf"$t = \tau$ = {tau:.0f} s: {Ttau:.1f} °C", (tau, Ttau),
                xytext=(1500, 52), fontsize=9,
                arrowprops=dict(arrowstyle="-", color=GREY, lw=0.7))
    ax.set_xlim(0, 5000)
    ax.set_ylim(15, 85)
    ax.set_xlabel("time $t$ (s)")
    ax.set_ylabel("block temperature $T$ (°C)")
    ax.legend(loc="upper right")
    save(fig, __file__, "thermal-cooldown")


if __name__ == "__main__":
    first_vs_second_order()
    thermal_cooldown()
