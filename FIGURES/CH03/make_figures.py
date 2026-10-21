"""Figures for Chapter 3 (Bridge A: The Quantum Descent)."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax
from scipy.integrate import trapezoid


def dirac_dispersion():
    """§3.4.3 Antimatter: E = +/- sqrt(p^2 c^2 + m^2 c^4), the two branches.

    Units E/mc^2 against p/mc. Gap of 2 mc^2 between branches; dashed is the
    non-relativistic limit E = mc^2 + p^2/2m (and its mirror).
    """
    p = np.linspace(-3, 3, 600)
    E = np.sqrt(p**2 + 1)
    fig, ax = fig_ax(h=4.2)
    ax.axhspan(-1, 1, color=SHADE, alpha=0.12)
    ax.plot(p, E, color=C[0], label=r"$E=+\sqrt{p^2c^2+m^2c^4}$ (electron)")
    ax.plot(p, -E, color=C[1],
            label=r"$E=-\sqrt{p^2c^2+m^2c^4}$ (negative energy $\to$ positron)")
    pn = np.linspace(-1.9, 1.9, 300)
    ax.plot(pn, 1 + pn**2 / 2, "--", color=GREY, lw=1.2,
            label=r"non-relativistic $mc^2+p^2/2m$")
    ax.plot(pn, -(1 + pn**2 / 2), "--", color=GREY, lw=1.2)
    ax.plot(p, np.abs(p), ":", color=INK, lw=0.9)
    ax.plot(p, -np.abs(p), ":", color=INK, lw=0.9)
    ax.text(2.35, 1.75, r"$E=\pm pc$", fontsize=8.5, color=INK, rotation=0)
    ax.annotate("", (0.35, 1), (0.35, -1),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.0))
    ax.text(0.45, 0.0, r"gap $2mc^2$" "\n(no states)", va="center", fontsize=9)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3.6, 4.6)
    ax.set_xlabel(r"momentum $p/mc$")
    ax.set_ylabel(r"energy $E/mc^2$")
    ax.set_title("Free Dirac particle: two energy branches")
    ax.legend(loc="upper center", fontsize=8.2, ncol=1)
    save(fig, __file__, "dirac-dispersion")


def hydrogen_fine_structure():
    """§3.4.4 Fine Structure of Hydrogen: exact Dirac levels vs Bohr.

    E_nj = mc^2 [1 + (alpha / (n - (j+1/2) + sqrt((j+1/2)^2 - alpha^2)))^2]^(-1/2);
    binding energy E_nj - mc^2 compared with Bohr -alpha^2 mc^2 / 2n^2.
    Shifts plotted in units of alpha^2 Ry (Ry = alpha^2 mc^2 / 2).
    """
    alpha = 1 / 137.035999
    mc2 = 510998.95  # eV
    Ry = alpha**2 * mc2 / 2

    def dirac(n, j):
        k = j + 0.5
        return mc2 * (1 + (alpha / (n - k + np.sqrt(k**2 - alpha**2)))**2) ** -0.5 - mc2

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.0, 4.2),
                                 gridspec_kw=dict(width_ratios=[1, 1.7]))
    for n in (1, 2, 3):
        a1.hlines(-Ry / n**2, 0.2, 0.8, color=INK, lw=2)
        a1.text(0.85, -Ry / n**2, f"$n={n}$", va="center", fontsize=9)
    a1.set_xlim(0, 1.15)
    a1.set_ylim(-14.5, 0.5)
    a1.set_xticks([])
    a1.grid(axis="x", visible=False)
    a1.set_ylabel("binding energy (eV)")
    a1.set_title("Full scale: Bohr $-13.6/n^2$ eV")
    a1.text(0.5, -7.5, "Dirac levels coincide\nwith Bohr at this scale\n"
            r"(shifts $\sim10^{-4}$ eV)", ha="center", fontsize=8.5, color=GREY)

    letters = "SPD"
    unit = alpha**2 * Ry
    for col, n in enumerate((1, 2, 3)):
        x0 = col * 1.0
        a2.hlines(0, x0 + 0.05, x0 + 0.85, color=GREY, ls="--", lw=1)
        for j2 in range(1, 2 * n, 2):  # 2j = 1, 3, ...
            j = j2 / 2
            shift = (dirac(n, j) + Ry / n**2) / unit
            ls = [l for l in range(n) if abs(l - j) == 0.5]
            lab = "=".join(f"{n}{letters[l]}$_{{{j2}/2}}$" for l in ls)
            a2.hlines(shift, x0 + 0.05, x0 + 0.85, color=C[j2 // 2], lw=2.2)
            ylab = shift + ({1: -0.006, 3: -0.002, 5: 0.008}[j2] if n == 3 else 0)
            a2.text(x0 + 0.88, ylab, lab, ha="left", va="center",
                    fontsize=8.5, color=C[j2 // 2])
        a2.text(x0 + 0.45, 0.012, "Bohr", ha="center", va="bottom", fontsize=8,
                color=GREY)
    # 2P3/2 - 2P1/2 splitting
    d2 = dirac(2, 1.5) - dirac(2, 0.5)
    y1, y2 = (dirac(2, 0.5) + Ry / 4) / unit, (dirac(2, 1.5) + Ry / 4) / unit
    a2.annotate("", (1.1, y2), (1.1, y1),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=0.9))
    a2.text(1.06, (y1 + y2) / 2,
            "2P$_{3/2}-$2P$_{1/2}$\n" + f"{d2:.2e} eV".replace("e-05", r"$\times10^{-5}$"),
            fontsize=8.5, va="center", ha="right")
    a2.set_xticks([0.45, 1.45, 2.45], ["$n=1$", "$n=2$", "$n=3$"])
    a2.grid(axis="x", visible=False)
    a2.set_xlim(0, 3.55)
    a2.set_ylim(-0.29, 0.05)
    a2.set_ylabel(r"$(E_{nj}-mc^2-E_n^{\rm Bohr})\ /\ \alpha^2\,\mathrm{Ry}$")
    a2.set_title("Zoom: exact Dirac shift from Bohr (depends on $n$, $j$ only)")
    save(fig, __file__, "hydrogen-fine-structure")


def gaussian_uncertainty():
    """§3.11 Uncertainty: Gaussian packets saturate Delta x Delta k = 1/2.

    psi(x) = (2 pi sigma^2)^(-1/4) exp(-x^2 / 4 sigma^2), so |psi|^2 has
    standard deviation sigma; its Fourier transform |psi~(k)|^2 has
    standard deviation 1/(2 sigma). Both widths are computed numerically.
    """
    x = np.linspace(-40, 40, 2**14)
    dx = x[1] - x[0]
    k = 2 * np.pi * np.fft.fftshift(np.fft.fftfreq(x.size, dx))
    fig, (a1, a2) = fig_ax(ncols=2, h=3.6)
    for i, s in enumerate((0.5, 1.0, 2.0)):
        psi = (2 * np.pi * s**2) ** -0.25 * np.exp(-x**2 / (4 * s**2))
        P = np.abs(psi) ** 2
        phik = np.fft.fftshift(np.fft.fft(np.fft.ifftshift(psi))) * dx / np.sqrt(2 * np.pi)
        Pk = np.abs(phik) ** 2
        Dx = np.sqrt(trapezoid(x**2 * P, x) / trapezoid(P, x))
        Dk = np.sqrt(trapezoid(k**2 * Pk, k) / trapezoid(Pk, k))
        a1.plot(x, P, color=C[i], label=rf"$\sigma_x={s}$")
        a2.plot(k, Pk, color=C[i],
                label=rf"$\Delta k={Dk:.2f}$,  $\Delta x\Delta k={Dx * Dk:.3f}$")
    a1.set_xlim(-6, 6)
    a1.set_xlabel("position $x$")
    a1.set_ylabel(r"$|\psi(x)|^2$")
    a1.set_title("Narrow in $x$ ...")
    a1.legend()
    a2.set_xlim(-4, 4)
    a2.set_xlabel("wavenumber $k$")
    a2.set_ylabel(r"$|\tilde\psi(k)|^2$")
    a2.set_title("... means broad in $k$")
    a2.legend(fontsize=8.5, loc="upper right")
    a2.set_ylim(0, 1.25 * a2.get_ylim()[1])
    save(fig, __file__, "gaussian-uncertainty")


if __name__ == "__main__":
    dirac_dispersion()
    hydrogen_fine_structure()
    gaussian_uncertainty()
