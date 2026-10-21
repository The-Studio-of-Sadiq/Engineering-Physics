"""Figures for Chapter 4 (The Schrödinger Equation and the Hydrogen Atom)."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax
from math import factorial
from scipy.integrate import trapezoid
from scipy.special import eval_hermite


def infinite_well():
    """§4.2.2 The Solution: psi_n = sqrt(2/L) sin(n pi x / L), E_n = n^2 E_1.

    n = 1..4, x in units of L. Left: psi_n drawn on its energy level;
    right: |psi_n|^2 (n - 1 interior nodes, n humps).
    """
    x = np.linspace(0, 1, 500)
    fig, (a1, a2) = fig_ax(ncols=2, h=4.2)
    for ax, sq in ((a1, False), (a2, True)):
        for n in range(1, 5):
            psi = np.sqrt(2) * np.sin(n * np.pi * x)
            y = psi**2 if sq else psi
            E = n**2
            ax.axhline(E, color=GREY, lw=0.6, ls=":")
            ax.plot(x, E + 1.1 * y, color=C[n - 1])
            elab = "E_1" if n == 1 else f"{n**2}E_1"
            ax.text(1.03, E, f"$n={n}$\n$E={elab}$", va="center", fontsize=8.5,
                    color=C[n - 1])
        ax.axvline(0, color=INK, lw=2.5)
        ax.axvline(1, color=INK, lw=2.5)
        ax.set_xlim(-0.05, 1.3)
        ax.set_ylim(-0.3, 19.5)
        ax.set_xticks([0, 0.5, 1], ["0", "$L/2$", "$L$"])
        ax.set_xlabel("position $x$")
        ax.grid(False)
    a1.set_ylabel(r"energy $E/E_1$  (curves offset to $E_n$)")
    a1.set_title(r"$\psi_n(x)=\sqrt{2/L}\,\sin(n\pi x/L)$")
    a2.set_title(r"Probability density $|\psi_n(x)|^2$")
    save(fig, __file__, "infinite-well")


def harmonic_oscillator():
    """§4.3.3 Wavefunctions: psi_n ∝ H_n(xi) exp(-xi^2/2), E_n = (n + 1/2) hbar omega.

    xi = sqrt(m omega / hbar) x; potential V = xi^2/2 in units of hbar omega.
    Classical turning points at xi = +/- sqrt(2n + 1).
    """
    xi = np.linspace(-4.5, 4.5, 800)
    fig, ax = fig_ax(h=4.6, w=6.4)
    ax.plot(xi, 0.5 * xi**2, color=INK, lw=1.4, label=r"$V=\frac{1}{2}\xi^2$")
    for n in range(5):
        norm = np.pi**-0.25 / np.sqrt(2**n * factorial(n))
        psi = norm * eval_hermite(n, xi) * np.exp(-xi**2 / 2)
        E = n + 0.5
        xt = np.sqrt(2 * n + 1)
        ax.hlines(E, -xt, xt, color=GREY, lw=0.7, ls=":")
        ax.plot(xi, E + 0.7 * psi, color=C[n % len(C)])
        ax.plot([-xt, xt], [E, E], "|", color=INK, ms=8)
        ax.text(4.6, E, f"$n={n}$", va="center", fontsize=8.5, color=C[n % len(C)])
    ax.set_xlim(-4.5, 5.3)
    ax.set_ylim(0, 6.0)
    ax.set_xlabel(r"$\xi=\sqrt{m\omega/\hbar}\,x$")
    ax.set_ylabel(r"energy $E/\hbar\omega$  (curves offset to $n+\frac{1}{2}$)")
    ax.set_title("Oscillator eigenfunctions; ticks mark classical turning points")
    ax.legend(loc="upper left")
    save(fig, __file__, "harmonic-oscillator")


def barrier_tunnelling():
    """§4.4.3 Transmission Coefficient: exact rectangular-barrier T(E/V0).

    E < V0: T = [1 + sinh^2(kappa d) / (4 eps (1 - eps))]^-1,
    E > V0: T = [1 + sin^2(k' d) / (4 eps (eps - 1))]^-1, eps = E/V0,
    kappa d = kappa0 d sqrt(1 - eps), k' d = kappa0 d sqrt(eps - 1),
    kappa0 = sqrt(2 m V0)/hbar. Dashed: thick-barrier 16 eps(1-eps) e^{-2 kappa d}.
    """
    fig, ax = fig_ax(h=4.0)
    e_lo = np.linspace(1e-4, 1 - 1e-6, 1500)
    e_hi = np.linspace(1 + 1e-6, 3, 1500)
    for i, g in enumerate((1, 3, 5)):
        T_lo = 1 / (1 + np.sinh(g * np.sqrt(1 - e_lo))**2 / (4 * e_lo * (1 - e_lo)))
        T_hi = 1 / (1 + np.sin(g * np.sqrt(e_hi - 1))**2 / (4 * e_hi * (e_hi - 1)))
        ax.plot(np.r_[e_lo, e_hi], np.r_[T_lo, T_hi], color=C[i],
                label=rf"$\kappa_0 d={g}$")
        T_thick = 16 * e_lo * (1 - e_lo) * np.exp(-2 * g * np.sqrt(1 - e_lo))
        ax.plot(e_lo, T_thick, "--", color=C[i], lw=1.1)
    ax.plot([], [], "--", color=GREY, lw=1.1, label=r"thick-barrier $16\epsilon(1-\epsilon)e^{-2\kappa d}$")
    ax.axvline(1, color=GREY, lw=0.8)
    ax.text(0.5, 1.6, "tunnelling\n$E<V_0$", ha="center", va="bottom", fontsize=8.5)
    ax.text(2.0, 1.6, "over the barrier $E>V_0$\n(resonances $T=1$ at $k'd=N\\pi$)",
            ha="center", va="bottom", fontsize=8.5)
    ax.set_yscale("log")
    ax.set_ylim(1e-5, 8)
    ax.set_xlim(0, 3)
    ax.set_xlabel(r"$\epsilon=E/V_0$")
    ax.set_ylabel("transmission $T$")
    ax.set_title("Rectangular barrier: exact transmission")
    ax.legend(loc="lower right", fontsize=8.5)
    save(fig, __file__, "barrier-tunnelling")


def hydrogen_radial():
    """§4.8.1 Explicit Wavefunctions: radial probability r^2 |R_nl(r)|^2.

    Standard R_nl in units a0 = 1 (1s, 2s, 2p read off psi_100, psi_200,
    psi_210 in the text; 3s, 3p, 3d standard forms). Normalisation
    int r^2 R^2 dr = 1 is checked numerically. 1s peaks at r = a0.
    """
    r = np.linspace(0, 80, 16000)  # long tail for the normalisation check
    R = {
        "1s": 2 * np.exp(-r),
        "2s": (2 - r) * np.exp(-r / 2) / (2 * np.sqrt(2)),
        "2p": r * np.exp(-r / 2) / (2 * np.sqrt(6)),
        "3s": 2 / (81 * np.sqrt(3)) * (27 - 18 * r + 2 * r**2) * np.exp(-r / 3),
        "3p": 4 / (81 * np.sqrt(6)) * (6 * r - r**2) * np.exp(-r / 3),
        "3d": 4 / (81 * np.sqrt(30)) * r**2 * np.exp(-r / 3),
    }
    for k, v in R.items():
        nrm = trapezoid(r**2 * v**2, r)
        assert abs(nrm - 1) < 1e-6, (k, nrm)
    fig, axs = plt.subplots(3, 1, figsize=(6.4, 6.6), sharex=True)
    groups = [["1s"], ["2s", "2p"], ["3s", "3p", "3d"]]
    for ax, grp in zip(axs, groups):
        for k in grp:
            l = "spd".index(k[1])
            P = r**2 * R[k]**2
            ax.plot(r, P, color=C[l], label=k)
        ax.set_ylabel(r"$r^2|R_{n\ell}|^2$")
        ax.legend(loc="upper right")
        ax.set_ylim(0, None)
    axs[0].axvline(1, color=GREY, ls=":", lw=1)
    axs[0].annotate("most probable $r=a_0$", (1, 4 * np.exp(-2)), (3.0, 0.45),
                    fontsize=8.5, arrowprops=dict(arrowstyle="->", color=INK, lw=0.8))
    axs[1].axvline(4, color=GREY, ls=":", lw=1)
    axs[1].text(4.3, 0.04, r"2p peak $4a_0$", fontsize=8.5)
    axs[2].axvline(9, color=GREY, ls=":", lw=1)
    axs[2].set_ylim(0, 0.13)
    axs[2].text(8.7, 0.12, r"3d peak $9a_0$", fontsize=8.5, ha="right")
    axs[0].set_title(r"Hydrogen radial probability densities ($\ell=n-1$ peaks at $n^2a_0$)")
    axs[2].set_xlim(0, 30)
    axs[2].set_xlabel(r"$r/a_0$")
    save(fig, __file__, "hydrogen-radial")


if __name__ == "__main__":
    infinite_well()
    harmonic_oscillator()
    barrier_tunnelling()
    hydrogen_radial()
