"""Figures for Example 06 — Motor → Control system (EXAMPLES/06 Motor-to-Control-System.md)."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax

# Step 1 parameters
RA, LA, J, B, KT, KB = 0.5, 5e-3, 2e-4, 2e-5, 8e-3, 8e-3
A2, A1, A0 = LA * J, LA * B + RA * J, RA * B + KT * KB   # denominator of Omega/V_a
P_SLOW, P_FAST = sorted(np.roots([1, A1 / A2, A0 / A2]).real, reverse=True)  # -0.745, -99.36
K_DC = KT / A0                                            # 108 rad/s per V


def open_loop_step(t):
    """Speed per volt for G(s) = 8000/((s - p1)(s - p2)): two real poles, no free integrator."""
    p1, p2 = P_SLOW, P_FAST
    return K_DC * (1 - (p2 * np.exp(p1 * t) - p1 * np.exp(p2 * t)) / (p2 - p1))


def motor_poles():
    """Step 4: poles of Omega/V_a = K_t/(L_a J s^2 + (L_a B + R_a J) s + R_a B + K_t K_b)
    = 8000/(s^2 + 100.1 s + 74), against the uncoupled references -B/J and -R_a/L_a;
    and the open-loop step response it implies."""
    fig, (ax, ay) = fig_ax(ncols=2, h=3.6)
    ax.set_xscale("symlog", linthresh=0.05)
    ax.axhline(0, color=INK, lw=0.6)
    ax.axvline(0, color=INK, lw=0.6)
    ax.plot([P_SLOW, P_FAST], [0, 0], "x", color=C[1], ms=11, mew=2.2, label="coupled motor poles")
    ax.plot([-B / J, -RA / LA], [0, 0], "o", mfc="none", color=C[0], ms=10, mew=1.4,
            label="uncoupled: $-B/J$, $-R_a/L_a$")
    ax.annotate("", xy=(P_SLOW, 0.12), xytext=(-B / J, 0.12),
                arrowprops=dict(arrowstyle="-|>", color=C[2], lw=1.2))
    ax.text(-0.27, 0.2, "back-EMF\ndamping ×7.5", ha="center", fontsize=8.5, color=C[2])
    ax.text(P_SLOW, -0.25, f"{P_SLOW:.3f}\n(τ = {-1 / P_SLOW:.2f} s)", ha="center", va="top", fontsize=8.5)
    ax.text(P_FAST, -0.25, f"{P_FAST:.2f}\n(τ = {-1e3 / P_FAST:.1f} ms)", ha="center", va="top", fontsize=8.5)
    ax.set_xlim(-400, 0.05)
    ax.set_xticks([-100, -10, -1, -0.1, 0])
    ax.set_xticklabels(["−100", "−10", "−1", "−0.1", "0"])
    ax.set_ylim(-1, 1)
    ax.set_yticks([])
    ax.set_xlabel(r"Re $s$ (s$^{-1}$, symmetric-log scale)")
    ax.set_ylabel(r"Im $s$")
    ax.set_title("s-plane: two real poles, none at the origin", fontsize=10)
    ax.legend(loc="upper left", fontsize=8)

    t = np.linspace(0, 8, 800)
    ay.plot(t, open_loop_step(t), color=C[1], label="two-pole model $G(s)$")
    ay.plot(t, K_DC * (1 - np.exp(P_SLOW * t)), color=C[0], ls="--", lw=1.3,
            label=rf"dominant pole only, $\tau_m$ = {-1 / P_SLOW:.2f} s")
    ay.axhline(K_DC, color=GREY, lw=0.8, ls=":")
    ay.text(7.9, K_DC + 2, f"DC gain K = {K_DC:.0f} rad/s per V", ha="right", fontsize=8.5, color=GREY)
    ay.set_xlim(0, 8)
    ay.set_ylim(0, 125)
    ay.set_xlabel("time $t$ (s)")
    ay.set_ylabel(r"speed per volt $\omega/V_a$ (rad/s per V)")
    ay.set_title("open-loop step: settles, does not ramp", fontsize=10)
    ay.legend(loc="lower right", fontsize=8.5)
    save(fig, __file__, "motor-poles")


def pi_closed_loop():
    """Step 5: PI with tau_i = tau_m cancels the dominant pole -> T(s) = 1/(1 + 0.67 s),
    step 1 - e^{-t/0.67}, compared with the normalised open-loop plant response."""
    tau_cl = 0.67
    t = np.linspace(0, 6, 600)
    fig, ax = fig_ax(h=3.6)
    ax.plot(t, 1 - np.exp(-t / tau_cl), color=C[2],
            label=r"closed loop (PI, $\tau_i = \tau_m$): $1 - e^{-t/0.67\,\mathrm{s}}$")
    ax.plot(t, open_loop_step(t) / K_DC, color=C[1], ls="--", label=r"open-loop plant, normalised by $K$")
    ax.axhline(1, color=GREY, lw=0.8, ls=":")
    ax.axhline(1 - np.exp(-1), color=GREY, lw=0.6, ls=":")
    ax.text(5.95, 1 - np.exp(-1) - 0.06, "63%", ha="right", fontsize=8.5, color=GREY)
    for tau, col, name in ((tau_cl, C[2], r"$\tau_{cl}$ = 0.67 s"), (-1 / P_SLOW, C[1], r"$\tau_m$ ≈ 1.34 s")):
        ax.plot([tau, tau], [0, 1 - np.exp(-1)], color=col, lw=0.9, ls=":")
        ax.text(tau + 0.05, 0.22 if tau < 1 else 0.05, name, color=col, fontsize=9)
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 1.1)
    ax.set_xlabel("time $t$ (s)")
    ax.set_ylabel(r"normalised speed $\omega/\omega_{ref}$")
    ax.legend(loc="lower right")
    save(fig, __file__, "pi-closed-loop")


if __name__ == "__main__":
    motor_poles()
    pi_closed_loop()
