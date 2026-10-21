"""Figures for Chapter 19 — ME Systems: Machines, Structures, and Thermofluid Systems."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax


def transmissibility():
    """§19.1.3 — force transmissibility T(r) = sqrt[(1+(2 zeta r)^2) / ((1-r^2)^2 + (2 zeta r)^2)].

    zeta = 0.05, 0.1, 0.2, 0.5, 1; all curves cross T = 1 at r = sqrt(2);
    fan example: f0 = 5 Hz under a 3000 rpm (50 Hz) machine gives r = 10.
    """
    r = np.logspace(-1, 1, 1500)
    fig, ax = fig_ax(h=3.9)
    for i, z in enumerate([0.05, 0.1, 0.2, 0.5, 1.0]):
        T = np.sqrt((1 + (2 * z * r) ** 2) / ((1 - r**2) ** 2 + (2 * z * r) ** 2))
        ax.loglog(r, T, color=C[i], label=rf"$\zeta={z:g}$")
    ax.axhline(1, color=GREY, lw=0.8)
    ax.axvline(np.sqrt(2), color=GREY, lw=0.8, ls="--")
    ax.text(1.47, 4.5, r"$r=\sqrt{2}$", fontsize=9, color=INK)
    ax.axvspan(np.sqrt(2), 10, color=SHADE, alpha=0.08)
    ax.text(2.6, 6, "isolation ($T<1$)", fontsize=9, color=INK)
    ax.text(0.12, 1.25, "amplification ($T>1$)", fontsize=9, color=INK)
    z = 0.05
    T10 = np.sqrt((1 + (2 * z * 10) ** 2) / ((1 - 100) ** 2 + (2 * z * 10) ** 2))
    ax.plot(10, T10, "o", color=INK, ms=5, clip_on=False, zorder=5)
    ax.annotate(f"fan example, $r=10$:\n$T\\approx{T10:.3f}$ ($\\zeta=0.05$)", xy=(10, T10),
                xytext=(2.3, 0.0035), fontsize=8, color=INK,
                arrowprops=dict(arrowstyle="->", color=GREY))
    ax.set_xlim(0.1, 10)
    ax.set_ylim(1e-3, 20)
    ax.set_xlabel(r"frequency ratio $r=\omega/\omega_0$")
    ax.set_ylabel(r"transmissibility $T$")
    ax.legend(loc="lower left", ncol=2)
    save(fig, __file__, "transmissibility")


def otto_diesel_efficiency():
    """§19.5.4 — air-standard efficiencies, gamma = 1.4.

    Otto:   eta = 1 - r^(1-gamma)
    Diesel: eta = 1 - r^(1-gamma) (rc^gamma - 1) / (gamma (rc - 1)), rc = 1.5, 2, 3.
    Shaded: typical gasoline r = 9-12 and diesel r = 16-22.
    """
    g = 1.4
    r = np.linspace(4, 25, 400)
    fig, ax = fig_ax(h=3.8)
    ax.axvspan(9, 12, color=C[1], alpha=0.10)
    ax.axvspan(16, 22, color=C[2], alpha=0.10)
    ax.text(10.5, 0.215, "gasoline\n$r$ = 9–12", ha="center", fontsize=8, color=INK)
    ax.text(19, 0.215, "diesel\n$r$ = 16–22", ha="center", fontsize=8, color=INK)
    ax.plot(r, 1 - r ** (1 - g), color=C[0], label="Otto")
    for i, rc in enumerate([1.5, 2.0, 3.0]):
        eta = 1 - r ** (1 - g) * (rc**g - 1) / (g * (rc - 1))
        ax.plot(r, eta, color=C[[3, 4, 5][i]], ls="--", label=rf"Diesel, $r_c={rc:g}$")
    ax.plot(10, 1 - 10 ** (1 - g), "o", color=C[0], ms=5)
    ax.annotate(r"$r=10$: 60%", xy=(10, 1 - 10 ** (1 - g)), xytext=(11.2, 0.44), fontsize=8,
                arrowprops=dict(arrowstyle="->", color=GREY))
    ax.set_xlim(4, 25)
    ax.set_ylim(0.2, 0.8)
    ax.set_xlabel(r"compression ratio $r=V_{max}/V_{min}$")
    ax.set_ylabel(r"ideal thermal efficiency $\eta$")
    ax.set_title(r"Air-standard Otto and Diesel cycles, $\gamma=1.4$")
    ax.legend(loc="upper left")
    save(fig, __file__, "otto-diesel-efficiency")


def pump_system_curves():
    """§19.7.3 — pump curve H = H0 - A Q^2 against system curve H = H_static + B Q^2.

    Illustrative values: H0 = 40 m, A = 0.020 m/(L/s)^2, H_static = 10 m,
    B = 0.015 m/(L/s)^2.  Second speed N2/N1 = 0.8 via affinity laws
    (Q ~ N, H ~ N^2): H2(Q) = (N2/N1)^2 H0 - A Q^2.
    """
    H0, A, Hs, B = 40.0, 0.020, 10.0, 0.015
    Q = np.linspace(0, 45, 400)
    fig, ax = fig_ax(h=3.8)
    ax.plot(Q, Hs + B * Q**2, color=INK, label=r"system: $H_{static}+BQ^2$")
    for s, col, ls in [(1.0, C[0], "-"), (0.8, C[1], "--")]:
        Hp = s**2 * H0 - A * Q**2
        m = Hp > 0
        ax.plot(Q[m], Hp[m], color=col, ls=ls, label=rf"pump, $N/N_1={s:g}$")
        Qs = np.sqrt((s**2 * H0 - Hs) / (A + B))
        Hst = Hs + B * Qs**2
        ax.plot(Qs, Hst, "o", color=col, ms=6, zorder=5)
        ax.annotate(rf"$Q^*={Qs:.1f}$ L/s" + "\n" + rf"$H^*={Hst:.1f}$ m", xy=(Qs, Hst),
                    xytext=(36.5, 18) if s == 1 else (5, 16.5), fontsize=8, color=col,
                    arrowprops=dict(arrowstyle="->", color=col))
    ax.axhline(Hs, color=GREY, lw=0.8, ls=":")
    ax.text(1, Hs + 0.8, r"$H_{static}$", fontsize=8, color=GREY)
    ax.set_xlim(0, 45)
    ax.set_ylim(0, 45)
    ax.set_xlabel(r"flow rate $Q$ [L/s]")
    ax.set_ylabel(r"head $H$ [m]")
    ax.set_title("Pump and system curves: the operating point")
    ax.legend(loc="upper center", bbox_to_anchor=(0.66, 1.0))
    save(fig, __file__, "pump-system-curves")


if __name__ == "__main__":
    transmissibility()
    otto_diesel_efficiency()
    pump_system_curves()
