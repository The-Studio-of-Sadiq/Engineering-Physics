"""Figures for Chapter 13 (Bridge B.e: Kubo formula and transport laws)."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax

kB_meV = 8.617333e-2  # meV / K


def fermi_window():
    """§13.4.2 Linearized Boltzmann transport: the Fermi window
    -df0/de = (1/4kT) sech^2((e - mu)/2kT) at T = 30, 100, 300 K.
    Unit area; FWHM = 3.53 kT, so only states within a few kT of mu conduct."""
    e = np.linspace(-150, 150, 3001)
    fig, ax = fig_ax(h=3.4)
    for T, col in [(30, C[1], ), (100, C[2]), (300, C[0])]:
        kT = kB_meV * T
        w = 1 / (4 * kT) / np.cosh(e / (2 * kT))**2
        ax.plot(e, w, color=col, label=rf"$T={T}$ K  ($k_BT={kT:.1f}$ meV)")
    kT = kB_meV * 300
    hw = 1.7627 * kT                       # half width at half maximum
    ax.annotate("", xy=(hw, 1 / (8 * kT)), xytext=(-hw, 1 / (8 * kT)),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.0))
    ax.text(hw + 4, 0.009, r"FWHM $=3.53\,k_BT$ (300 K)", color=INK, fontsize=8)
    ax.set_xlim(-150, 150)
    ax.set_ylim(0, 0.105)
    ax.set_xlabel(r"$\epsilon-\mu$ (meV)")
    ax.set_ylabel(r"$-\partial f_0/\partial\epsilon$ (meV$^{-1}$)")
    ax.legend(loc="upper right")
    return fig


def drude_conductivity():
    """§13.4.2 Frequency dependence: sigma(w)/sigma0 = 1/(1 - i w tau);
    Re = 1/(1 + w^2 tau^2), Im = w tau/(1 + w^2 tau^2); crossover at w tau = 1."""
    wt = np.logspace(-2, 2, 500)
    fig, ax = fig_ax(h=3.4)
    ax.semilogx(wt, 1 / (1 + wt**2), color=C[0], label=r"Re $\sigma/\sigma_0$ (dissipative)")
    ax.semilogx(wt, wt / (1 + wt**2), color=C[1], label=r"Im $\sigma/\sigma_0$ (reactive)")
    ax.axvline(1, color=GREY, ls="--", lw=1)
    ax.plot(1, 0.5, "o", color=INK, ms=5)
    ax.annotate(r"$\omega\tau=1$: Re = Im = 1/2", xy=(1, 0.5), xytext=(2.2, 0.68), fontsize=8,
                arrowprops=dict(arrowstyle="->", color=INK, lw=0.8))
    ax.text(0.012, 0.06, "Ohmic\n(DC-like)", fontsize=8, color=GREY)
    ax.text(25, 0.2, "inductive\n(kinetic\ninductance)", fontsize=8, color=GREY, ha="center")
    ax.text(0.98, 0.98, r"$\tau\sim10^{-14}$ s $\Rightarrow$ $\omega\tau=1$ at $f\approx16$ THz (far IR)",
            transform=ax.transAxes, ha="right", va="top", fontsize=8, color=GREY)
    ax.set_xlim(1e-2, 1e2)
    ax.set_ylim(0, 1.08)
    ax.set_xlabel(r"$\omega\tau$")
    ax.set_ylabel(r"$\sigma(\omega)/\sigma_0$")
    ax.legend(loc="center left", bbox_to_anchor=(0.0, 0.42))
    return fig


def green_kubo_vacf():
    """§13.6.1 Green-Kubo diffusion: C_vv(t) = <v_a(0) v_a(t)> = (kT/m) e^{-t/tau};
    the shaded area is D = int_0^inf C_vv dt = kT tau / m."""
    t = np.linspace(0, 5, 500)
    fig, ax = fig_ax(h=3.2)
    y = np.exp(-t)
    ax.fill_between(t, y, color=SHADE, alpha=0.18, lw=0)
    ax.plot(t, y, color=C[0], label=r"$C_{vv}(t)\,/\,(k_BT/m) = e^{-t/\tau}$")
    ax.plot([0, 1], [1, 0], color=GREY, ls="--", lw=1)
    ax.text(1.02, 0.02, r"$\tau$", color=GREY)
    ax.annotate("shaded area:\n" r"$D=\int_0^\infty C_{vv}\,dt = \dfrac{k_BT\,\tau}{m}$",
                xy=(1.3, 0.12), xytext=(2.0, 0.5), fontsize=10, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=0.8))
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel(r"$t/\tau$")
    ax.set_ylabel(r"$C_{vv}(t)\,/\,(k_BT/m)$")
    ax.legend(loc="upper right")
    return fig


def landauer_steps():
    """§13.11.1 Landauer formula G = (2e^2/h) sum_n T_n for a quantum point contact.
    Saddle-point transmissions T_n = 1/(1 + exp(-(V_g - V_n)/w)), modes opening at
    evenly spaced V_n (illustrative gate units), at two smearing widths w."""
    Vg = np.linspace(-0.5, 6.5, 1400)
    Vn = np.arange(0, 7)
    fig, ax = fig_ax(h=3.4)
    ideal = np.sum(Vg[:, None] >= Vn[None, :] + 0.5, axis=1)
    ax.plot(Vg, ideal, color=GREY, lw=1, ls="--", label="ideal ($T_n$ = 0 or 1)")
    for w, col, lab in [(0.06, C[0], "sharp saddle / low $T$"), (0.2, C[1], "smoother / warmer")]:
        G = np.sum(1 / (1 + np.exp(-(Vg[:, None] - Vn[None, :] - 0.5) / w)), axis=1)
        ax.plot(Vg, G, color=col, label=lab)
    for n in range(1, 7):
        ax.axhline(n, color="#e0e0e0", lw=0.6, zorder=0)
    ax.set_yticks(range(0, 8))
    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(0, 7.3)
    ax.set_xlabel("gate voltage $V_g$ (arb. units; more positive = wider channel)")
    ax.set_ylabel(r"$G\;/\;(2e^2/h)$")
    ax.text(6.4, 0.3, r"$2e^2/h = 77.5\ \mu$S $= 1/12.9$ kΩ", ha="right", fontsize=8, color=GREY)
    ax.legend(loc="upper left")
    return fig


def main():
    save(fermi_window(), __file__, "fermi-window")
    save(drude_conductivity(), __file__, "drude-conductivity")
    save(green_kubo_vacf(), __file__, "green-kubo-vacf")
    save(landauer_steps(), __file__, "landauer-steps")


if __name__ == "__main__":
    main()
