"""Figures for Chapter 10 (Bridge B.b: statistical mechanics and thermodynamics)."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax

from scipy.integrate import quad

h, c, kB = 6.62607015e-34, 2.99792458e8, 1.380649e-23
WIEN_B = 2.897771955e-3  # m K


def debye_heat_capacity():
    """§10.7.3 Failure of equipartition: C_V/3Nk vs T/T_D for Dulong-Petit,
    Einstein (T_E = sqrt(3/5) T_D, matching the Debye second moment) and
    Debye C_V = 9Nk (T/T_D)^3 int_0^{T_D/T} x^4 e^x/(e^x-1)^2 dx.
    Diamond (T_D = 2230 K) and lead (T_D = 105 K) marked at 300 K."""
    def debye(t):
        f = lambda x: x**4 * np.exp(-x) / (-np.expm1(-x))**2
        return 3 * t**3 * quad(f, 0, 1 / t)[0]          # C_V / 3Nk

    def einstein(t, tE):
        x = tE / t
        return x**2 * np.exp(-x) / (-np.expm1(-x))**2

    tE = np.sqrt(3 / 5)
    t = np.linspace(0.005, 3.2, 600)
    cd = np.array([debye(ti) for ti in t])
    ce = einstein(t, tE)

    fig, ax = fig_ax(h=3.8)
    ax.axhline(1, color=GREY, ls="--", lw=1.2, label="Dulong–Petit (classical)")
    ax.plot(t, ce, color=C[1], label=rf"Einstein, $T_E={tE:.2f}\,T_D$")
    ax.plot(t, cd, color=C[0], lw=2.2, label="Debye")
    for name, TD, col in [("diamond", 2230, C[2]), ("lead", 105, C[3])]:
        x = 300 / TD
        y = debye(x)
        ax.plot(x, y, "o", color=col, ms=7, zorder=5)
        ax.annotate(f"{name} at 300 K\n$T/T_D={x:.2f}$", xy=(x, y),
                    xytext=(x + 0.2, y - 0.13) if name == "diamond" else (x - 0.75, y - 0.2),
                    fontsize=8, color=col, arrowprops=dict(arrowstyle="->", color=col, lw=0.8))
    ax.set_xlim(0, 3.2)
    ax.set_ylim(0, 1.12)
    ax.set_xlabel(r"$T\,/\,T_D$")
    ax.set_ylabel(r"$C_V\,/\,3Nk_B$")
    ax.legend(loc="lower left", bbox_to_anchor=(0.17, 0.3))

    ins = ax.inset_axes([0.64, 0.12, 0.33, 0.42])
    tl = np.logspace(-2, 0.3, 120)
    ins.loglog(tl, [debye(ti) for ti in tl], color=C[0], lw=1.6)
    ins.loglog(tl, einstein(tl, tE), color=C[1], lw=1.2)
    ins.loglog(tl, 4 * np.pi**4 / 5 * tl**3, color=INK, ls=":", lw=1.2)
    ins.set_ylim(1e-6, 2)
    ins.set_xlim(1e-2, 2)
    ins.text(0.012, 3e-4, r"$\frac{4\pi^4}{5}\left(\frac{T}{T_D}\right)^3$", fontsize=8)
    ins.tick_params(labelsize=7)
    ins.set_title(r"low-$T$: Debye $T^3$ law", fontsize=8)
    ins.grid(True, which="major")
    return fig


def quantum_occupations():
    """§10.8.2 Mean occupation numbers: n_BE = 1/(e^x - 1), n_FD = 1/(e^x + 1),
    n_MB = e^{-x}, x = (eps - mu)/kT, log scale; all converge for x >> 1."""
    x = np.linspace(-3, 6, 900)
    xb = x[x > 0.02]
    fig, ax = fig_ax(h=3.5)
    ax.semilogy(xb, 1 / np.expm1(xb), color=C[0], label="Bose–Einstein  $1/(e^x-1)$")
    ax.semilogy(x, 1 / (np.exp(x) + 1), color=C[1], label="Fermi–Dirac  $1/(e^x+1)$")
    ax.semilogy(x, np.exp(-x), color=INK, ls="--", lw=1.4, label="Maxwell–Boltzmann  $e^{-x}$")
    ax.axhline(1, color=GREY, lw=0.8, ls=":")
    ax.text(-2.9, 1.15, "FD ceiling $\\bar n = 1$ (Pauli)", fontsize=8, color=GREY, va="bottom")
    ax.axvline(0, color=GREY, lw=0.8)
    ax.text(0.15, 40, r"BE diverges as $\epsilon\to\mu^+$", fontsize=8, color=C[0])
    ax.text(3.2, 0.12, "all three agree\nfor $\\epsilon-\\mu \\gg k_BT$", fontsize=8, color=INK)
    ax.set_xlim(-3, 6)
    ax.set_ylim(1e-3, 1e2)
    ax.set_xlabel(r"$x = (\epsilon-\mu)/k_BT$")
    ax.set_ylabel(r"mean occupation $\bar n$")
    ax.legend(loc="lower left")
    return fig


def planck_spectrum():
    """§10.8.4 Blackbody: u(lambda, T) = (8 pi h c / lambda^5) / (e^{hc/lambda kT} - 1)
    for T = 3000, 4000, 5000, 5800 K; Wien locus lambda_max T = 2.898e-3 m K;
    Rayleigh-Jeans 8 pi k T / lambda^4 dashed for 5000 K."""
    lam = np.linspace(0.08e-6, 3.0e-6, 1200)
    def u(l, T):  # J m^-3 per metre of wavelength
        return 8 * np.pi * h * c / l**5 / np.expm1(h * c / (l * kB * T))

    fig, ax = fig_ax(h=3.7)
    ax.axvspan(0.38, 0.75, color=C[6], alpha=0.18, lw=0)
    ax.text(0.565, 0.02, "visible", ha="center", fontsize=8, color=GREY,
            transform=ax.get_xaxis_transform())
    for T, col in zip([3000, 4000, 5000, 5800], [C[1], C[4], C[2], C[0]]):
        ax.plot(lam * 1e6, u(lam, T) * 1e-6, color=col, label=f"{T} K")
    Tl = np.linspace(2600, 6300, 100)
    lm = WIEN_B / Tl
    ax.plot(lm * 1e6, u(lm, Tl) * 1e-6, color=INK, ls=":", lw=1.4,
            label=r"Wien locus $\lambda_{max}T = 2.898\times10^{-3}$ m·K")
    ax.plot(lam * 1e6, 8 * np.pi * kB * 5000 / lam**4 * 1e-6, color=C[2], ls="--", lw=1.2,
            label="Rayleigh–Jeans, 5000 K")
    ax.set_xlim(0, 3.0)
    ax.set_ylim(0, 1.25)
    ax.set_xlabel(r"wavelength $\lambda$ (μm)")
    ax.set_ylabel(r"$u_\lambda$ (J m$^{-3}$ μm$^{-1}$)")
    ax.legend(loc="upper right")
    return fig


def landau_free_energy():
    """§10.9.2 Landau free energy F - F0 = a0 (T - Tc) phi^2 + b phi^4 (a0 = b = 1)
    above, at and below Tc; right: order parameter (1 - T/Tc)^beta for the
    mean-field beta = 1/2 and the 3D Ising beta = 0.326 (both normalised to 1 at T = 0)."""
    fig, (ax1, ax2) = fig_ax(ncols=2, h=3.4)
    phi = np.linspace(-1.1, 1.1, 500)
    for dT, col, lab in [(0.5, C[1], r"$T>T_c$"), (0.0, INK, r"$T=T_c$"), (-0.5, C[0], r"$T<T_c$")]:
        F = dT * phi**2 + phi**4
        ax1.plot(phi, F, color=col, label=lab)
        if dT < 0:
            pm = np.sqrt(-dT / 2)
            ax1.plot([-pm, pm], [-dT**2 / 4] * 2, "o", color=col, ms=6)
            ax1.annotate(r"$\phi_{eq}=\pm\sqrt{-a/2b}$", xy=(pm, -dT**2 / 4), xytext=(0.15, -0.28),
                         fontsize=8, color=col, arrowprops=dict(arrowstyle="->", color=col, lw=0.8))
    ax1.set_ylim(-0.32, 0.8)
    ax1.set_xlim(-1.1, 1.1)
    ax1.set_xlabel(r"order parameter $\phi$")
    ax1.set_ylabel(r"$F-F_0$  (units $a_0=b=1$)")
    ax1.legend(loc="upper center")

    T = np.linspace(0, 1.3, 600)
    for beta, col, lab in [(0.5, C[0], r"mean field $\beta=\frac{1}{2}$"),
                           (0.326, C[1], r"3D Ising $\beta\approx0.326$")]:
        ax2.plot(T, np.where(T < 1, np.clip(1 - T, 0, None)**beta, 0), color=col, label=lab)
    ax2.axvline(1, color=GREY, ls="--", lw=1)
    ax2.text(1.02, 0.9, r"$T_c$", color=GREY)
    ax2.set_xlim(0, 1.3)
    ax2.set_ylim(0, 1.08)
    ax2.set_xlabel(r"$T/T_c$")
    ax2.set_ylabel(r"$|\phi_{eq}|\propto(T_c-T)^\beta$")
    ax2.legend(loc="lower left")
    return fig


def main():
    save(debye_heat_capacity(), __file__, "debye-heat-capacity")
    save(quantum_occupations(), __file__, "quantum-occupations")
    save(planck_spectrum(), __file__, "planck-spectrum")
    save(landau_free_energy(), __file__, "landau-free-energy")


if __name__ == "__main__":
    main()
