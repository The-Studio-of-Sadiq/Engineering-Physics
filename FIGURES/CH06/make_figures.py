"""Figures for Chapter 6 (bands, phonons, nuclear binding, fusion)."""

import os
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax


def out(fig, slug):
    """Save SVG; also a PNG preview if FIG_PREVIEW_DIR is set (for review only)."""
    prev = os.environ.get("FIG_PREVIEW_DIR")
    if prev:
        fig.tight_layout()
        fig.savefig(pathlib.Path(prev) / f"{slug}.png", dpi=110, bbox_inches="tight")
    save(fig, __file__, slug)


# ---------------------------------------------------------------------------
def nfe_bands():
    """§6.2.3: nearly-free-electron bands in 1D.

    Near each zone boundary the two coupled plane waves k and k - G give
    E_pm = (eps_k + eps_{k-G})/2 pm sqrt((eps_k - eps_{k-G})^2/4 + |V_G|^2),
    eps_k = hbar^2 k^2 / 2m.  We diagonalise the plane-wave (central-equation)
    matrix with Fourier components V_1 (G = 2pi/a) and V_2 (G = 4pi/a), which
    reproduces that two-wave formula at every boundary.  Units: k in pi/a,
    E in eps(pi/a) = hbar^2 pi^2 / 2 m a^2.  |V_1| = 0.3, |V_2| = 0.25
    (exaggerated so the gaps are visible).
    """
    V = {1: 0.3, 2: 0.25}
    nG = np.arange(-6, 7)

    def bands(k):
        H = np.diag((k - 2 * nG) ** 2.0)
        for i, ni in enumerate(nG):
            for j, nj in enumerate(nG):
                if abs(ni - nj) in V:
                    H[i, j] = V[abs(ni - nj)]
        return np.linalg.eigvalsh(H)

    fig, (a1, a2) = fig_ax(ncols=2, w=10, h=4.2)
    # extended zone: band n plotted in the n-th zone, n-1 < |k| < n (units pi/a)
    for n in (1, 2, 3):
        for sgn in (1, -1):
            kk = sgn * np.linspace(n - 1, n, 400)
            E = np.array([bands(k)[n - 1] for k in kk])
            a1.plot(kk, E, color=C[0], label="nearly free electron" if (n, sgn) == (1, 1) else None)
    ke = np.linspace(-3, 3, 2401)
    a1.plot(ke, ke**2, color=INK, ls="--", lw=0.9, label=r"free electron $\hbar^2k^2/2m$")
    for n in (1, 2):
        lo, hi = bands(float(n))[n - 1], bands(float(n))[n]
        for a in (a1, a2):
            a.axhspan(lo, hi, color=SHADE, alpha=0.15, lw=0)
        a1.annotate("", xy=(n + 0.1, hi), xytext=(n + 0.1, lo),
                    arrowprops=dict(arrowstyle="<->", color=C[1], lw=1))
        a1.text(n + 0.17, (lo + hi) / 2, fr"$E_g\approx2|V_{n}|$", color=C[1], fontsize=8, va="center")
    for x in (-2, -1, 1, 2):
        a1.axvline(x, color=GREY, lw=0.6, ls=":")
    a1.set_xticks([-3, -2, -1, 0, 1, 2, 3])
    a1.set_xticklabels([r"$-3\pi/a$", r"$-2\pi/a$", r"$-\pi/a$", "0", r"$\pi/a$", r"$2\pi/a$", r"$3\pi/a$"])
    a1.set_xlim(-3, 3)
    a1.set_ylim(0, 9.5)
    a1.set_xlabel(r"$k$")
    a1.set_ylabel(r"$E\ /\ (\hbar^2\pi^2/2ma^2)$")
    a1.set_title("Extended zone")
    a1.legend(loc="upper center", fontsize=8)

    # reduced zone: the same bands folded into -pi/a < k < pi/a
    kr = np.linspace(-1, 1, 801)
    Er = np.array([bands(k) for k in kr])
    for G in (0, 2, -2):
        a2.plot(kr, (kr - G) ** 2, color=INK, ls="--", lw=0.9)
    for b in range(3):
        a2.plot(kr, Er[:, b], color=C[0])
        a2.text(0, Er[400, b] + (0.2, -0.95, 0.35)[b], f"band {b + 1}", fontsize=8, color=C[0],
                ha="center", va="bottom", bbox=dict(fc="white", ec="none", pad=0.5))
    a2.set_xticks([-1, 0, 1])
    a2.set_xticklabels([r"$-\pi/a$", "0", r"$\pi/a$"])
    a2.set_xlim(-1, 1)
    a2.set_ylim(0, 9.5)
    a2.set_xlabel(r"$k$ (first Brillouin zone)")
    a2.set_title("Reduced zone (same bands folded back)")
    out(fig, "nfe-bands")


# ---------------------------------------------------------------------------
def diatomic_phonons():
    """§6.7.1: diatomic-chain dispersion, M1 = 2 M2, spring constant K.

    omega^2 = K(1/M1 + 1/M2) pm K sqrt((1/M1 + 1/M2)^2 - 4 sin^2(ka/2)/(M1 M2)).
    omega in units of sqrt(K/M2); gap from sqrt(2K/M1) to sqrt(2K/M2).
    """
    M2, M1, K = 1.0, 2.0, 1.0
    k = np.linspace(-np.pi, np.pi, 801)          # k a
    s = 1 / M1 + 1 / M2
    root = np.sqrt(s**2 - 4 * np.sin(k / 2) ** 2 / (M1 * M2))
    w_opt = np.sqrt(K * (s + root))
    w_ac = np.sqrt(np.clip(K * (s - root), 0, None))
    lo, hi = np.sqrt(2 * K / M1), np.sqrt(2 * K / M2)

    fig, ax = fig_ax()
    ax.plot(k, w_opt, color=C[1], label="optical branch (+)")
    ax.plot(k, w_ac, color=C[0], label="acoustic branch (−)")
    ax.axhspan(lo, hi, color=SHADE, alpha=0.15, lw=0)
    ax.text(0, (lo + hi) / 2, "gap: no propagating modes", ha="center", va="center", fontsize=9)
    ax.text(np.pi * 1.02, lo, r"$\sqrt{2K/M_1}$", va="center", fontsize=9)
    ax.text(np.pi * 1.02, hi, r"$\sqrt{2K/M_2}$", va="center", fontsize=9)
    ax.text(np.pi * 1.02, np.sqrt(2 * K * s), r"$\sqrt{2K(1/M_1+1/M_2)}$", va="center", fontsize=9)
    ax.set_xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])
    ax.set_xticklabels([r"$-\pi/a$", r"$-\pi/2a$", "0", r"$\pi/2a$", r"$\pi/a$"])
    ax.set_xlim(-np.pi, np.pi)
    ax.set_ylim(0, 2.0)
    ax.set_xlabel(r"wavevector $k$")
    ax.set_ylabel(r"$\omega\ /\ \sqrt{K/M_2}$")
    ax.set_title(r"Diatomic chain, $M_1=2M_2$")
    ax.legend(loc="lower right", fontsize=8)
    out(fig, "diatomic-phonons")


# ---------------------------------------------------------------------------
def binding_energy_curve():
    """§6.9.2-6.9.3: SEMF binding energy per nucleon along the valley of stability.

    B = a_V A - a_S A^{2/3} - a_C Z(Z-1)/A^{1/3} - a_A (A-2Z)^2/A (+ pairing),
    a_V = 15.8, a_S = 18.3, a_C = 0.714, a_A = 23.2 MeV (text table);
    Z = A / (2 + 0.0153 A^{2/3}).  Pairing (+-12/sqrt(A)) averages to zero
    over even/odd nuclei and is omitted from the smooth curve.
    """
    aV, aS, aC, aA = 15.8, 18.3, 0.714, 23.2
    A = np.linspace(4, 250, 1000)
    Z = A / (2 + 0.0153 * A ** (2 / 3))
    B = aV * A - aS * A ** (2 / 3) - aC * Z * (Z - 1) / A ** (1 / 3) - aA * (A - 2 * Z) ** 2 / A
    BA = B / A
    data = {r"$^2$H": (2, 1.1), r"$^{12}$C": (12, 7.7), r"$^{56}$Fe": (56, 8.79), r"$^{238}$U": (238, 7.6)}

    fig, ax = fig_ax(w=6.8, h=4.0)
    ax.plot(A, BA, color=C[0], label="semi-empirical mass formula")
    for name, (a, ba) in data.items():
        ax.plot(a, ba, "o", color=C[1], ms=6, zorder=3)
        dx, dy = {"$^2$H": (8, 0), "$^{12}$C": (6, -0.7), "$^{56}$Fe": (-10, 0.35),
                  "$^{238}$U": (-8, 0.35)}.get(name, (5, 0.3))
        ax.text(a + dx, ba + dy, f"{name}  {ba} MeV", fontsize=9, ha="left" if dx > 0 else "center")
    ax.plot([], [], "o", color=C[1], label="measured (values from text)")
    ax.annotate("", xy=(48, 6.2), xytext=(8, 6.2),
                arrowprops=dict(arrowstyle="-|>", color=C[2], lw=1.8))
    ax.text(10, 5.7, "fusion", color=C[2], fontsize=10)
    ax.annotate("", xy=(100, 6.2), xytext=(235, 6.2),
                arrowprops=dict(arrowstyle="-|>", color=C[3], lw=1.8))
    ax.text(185, 5.7, "fission", color=C[3], fontsize=10)
    ax.axvline(56, color=GREY, lw=0.7, ls=":")
    ax.text(30, 2.4, "light nuclei: shell effects (e.g. $^4$He)\nand few-body physics make\nthe liquid-drop formula fail",
            fontsize=8, color=GREY)
    ax.set_xlim(0, 250)
    ax.set_ylim(0, 9.8)
    ax.set_xlabel("mass number $A$")
    ax.set_ylabel(r"$B/A$ (MeV per nucleon)")
    ax.legend(loc="lower right", fontsize=8)
    out(fig, "binding-energy-curve")


# ---------------------------------------------------------------------------
def gamow_peak():
    """§6.11.2: Gamow peak for D-T at k_B T = 10 keV.

    Rate integrand  e^{-E/kT} * e^{-sqrt(E_G/E)},  E_G = 2 m_r c^2 (pi alpha Z1 Z2)^2.
    Peak at E_0 = (E_G (kT)^2 / 4)^{1/3}; 1/e width Delta = 4 sqrt(E_0 kT / 3).
    """
    u = 931494.1                       # keV
    mr = (2.014102 * 3.016049) / (2.014102 + 3.016049) * u
    alpha = 1 / 137.036
    EG = 2 * mr * (np.pi * alpha) ** 2  # keV  (Z1 = Z2 = 1)
    kT = 10.0
    E0 = (EG * kT**2 / 4) ** (1 / 3)
    D = 4 * np.sqrt(E0 * kT / 3)
    E = np.linspace(0.05, 120, 2000)
    mb = np.exp(-E / kT)
    tun = np.exp(-np.sqrt(EG / E))
    prod = mb * tun
    fig, ax = fig_ax(w=6.6, h=3.9)
    ax.plot(E, mb, color=C[0], label=r"Maxwell–Boltzmann $e^{-E/k_BT}$")
    ax.plot(E, tun / tun[-1], color=C[1],
            label=r"tunnelling $e^{-\sqrt{E_G/E}}$ (scaled to 1 at 120 keV)")
    ax.fill_between(E, 0, prod / prod.max(), color=C[2], alpha=0.25, lw=0)
    ax.plot(E, prod / prod.max(), color=C[2], label="product (scaled to peak 1): Gamow peak")
    ax.axvline(E0, color=INK, lw=0.8, ls=":")
    ax.text(E0 - 1.5, 1.02, fr"$E_0\approx{E0:.0f}$ keV", fontsize=9, ha="right")
    ax.set_xlim(0, 120)
    ax.set_ylim(0, 1.08)
    ax.set_xlabel(r"centre-of-mass energy $E$ (keV)")
    ax.set_ylabel("relative weight")
    ax.legend(loc="upper right", fontsize=8, title_fontsize=9,
              title=fr"D–T, $k_BT=10$ keV, $E_G={EG:.0f}$ keV")
    print(f"   D-T: E_G = {EG:.1f} keV, E0 = {E0:.2f} keV, width = {D:.1f} keV")
    out(fig, "gamow-peak")


if __name__ == "__main__":
    nfe_bands()
    diatomic_phonons()
    binding_energy_curve()
    gamow_peak()
