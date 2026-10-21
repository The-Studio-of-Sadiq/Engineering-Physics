"""Figures for Example 02 — Quantum → Thermodynamics (EXAMPLES/02 Quantum-to-Thermodynamics.md)."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax

R = 8.314        # J/(mol K)
ATM = 101325.0   # Pa
GAMMA = 5 / 3    # monatomic ideal gas


def pv_adiabatic_work():
    """Step 5: reversible adiabat P V^gamma = const, 1 mol Ar, (1 atm, 300 K) -> 5 atm.

    W_on = -integral P dV = n C_V (T2 - T1); T2 = T1 (P2/P1)^((gamma-1)/gamma).
    """
    n, T1, P1, P2 = 1.0, 300.0, 1.0 * ATM, 5.0 * ATM
    V1 = n * R * T1 / P1
    T2 = T1 * (P2 / P1) ** ((GAMMA - 1) / GAMMA)
    V2 = n * R * T2 / P2
    W_on = n * 1.5 * R * (T2 - T1)

    V = np.linspace(7e-3, 27e-3, 400)
    P_iso = n * R * T1 / V
    P_ad = P1 * (V1 / V) ** GAMMA
    Vs = np.linspace(V2, V1, 300)
    Ps = P1 * (V1 / Vs) ** GAMMA

    fig, ax = fig_ax(h=4.0)
    ax.fill_between(Vs * 1e3, 0, Ps / ATM, color=SHADE, alpha=0.12,
                    label=rf"$W_{{on}} = -\int P\,dV = {W_on / 1e3:.2f}$ kJ")
    ax.plot(V * 1e3, P_iso / ATM, color=GREY, ls="--", lw=1.4, label="isotherm, 300 K")
    ax.plot(V * 1e3, P_ad / ATM, color=C[1], label=r"adiabat, $PV^{5/3}$ = const")
    ax.plot(V * 1e3, n * R * T2 / V / ATM, color=GREY, ls=":", lw=1.2,
            label=f"isotherm, {T2:.0f} K")
    ax.plot([V1 * 1e3], [1], "o", color=INK)
    ax.plot([V2 * 1e3], [5], "o", color=INK)
    ax.annotate(f"1: 1.00 atm, {V1 * 1e3:.1f} L, 300 K", (V1 * 1e3, 1),
                xytext=(V1 * 1e3 - 2.5, 0.35), ha="center", fontsize=9,
                arrowprops=dict(arrowstyle="-", color=GREY, lw=0.7))
    ax.annotate(f"2: 5.00 atm, {V2 * 1e3:.2f} L, {T2:.0f} K", (V2 * 1e3, 5),
                xytext=(V2 * 1e3 + 2.0, 5.6), fontsize=9,
                arrowprops=dict(arrowstyle="-", color=GREY, lw=0.7))
    # Direction of the process: an arrow just above the adiabat, from state 1 toward 2.
    pa = lambda v: P1 * (V1 / (v * 1e-3)) ** GAMMA / ATM
    ax.annotate("", xy=(13.0, pa(13.0) + 0.45), xytext=(19.0, pa(19.0) + 0.45),
                arrowprops=dict(arrowstyle="-|>", color=C[1], lw=1.2))
    ax.text(16.6, pa(16.6) + 0.75, "compression", color=C[1], fontsize=9,
            rotation=-17, ha="center")
    ax.set_xlim(7, 27)
    ax.set_ylim(0, 6.5)
    ax.set_xlabel("volume $V$ (L)")
    ax.set_ylabel("pressure $P$ (atm)")
    ax.legend(loc="upper right")
    save(fig, __file__, "pv-adiabatic-work")


if __name__ == "__main__":
    pv_adiabatic_work()
