"""Figures for Chapter 0 (The Standard Model Lagrangian)."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax


def mexican_hat():
    """§0.7 The Potential in Detail: V = -mu^2 |phi|^2 + lambda |phi|^4.

    Dimensionless units mu = lambda = 1, so v = sqrt(mu^2/lambda) = 1, the
    minimum sits at |phi| = v/sqrt(2) and the depth is -mu^4/(4 lambda) = -1/4.
    Two real components only: a cross-section of the true four-component case.
    """
    mu2, lam = 1.0, 1.0
    v = np.sqrt(mu2 / lam)
    rmin, Vmin = v / np.sqrt(2), -mu2**2 / (4 * lam)
    V = lambda r: -mu2 * r**2 + lam * r**4

    fig = plt.figure(figsize=(10.0, 4.2))
    ax3 = fig.add_subplot(1, 2, 1, projection="3d")
    r = np.linspace(0, 1.0, 60)
    th = np.linspace(0, 2 * np.pi, 90)
    R, TH = np.meshgrid(r, th)
    X, Y = R * np.cos(TH), R * np.sin(TH)
    ax3.plot_surface(X, Y, V(R), cmap="viridis", rstride=2, cstride=2,
                     linewidth=0, antialiased=True, alpha=0.9)
    t = np.linspace(0, 2 * np.pi, 200)
    ax3.plot(rmin * np.cos(t), rmin * np.sin(t), np.full_like(t, Vmin),
             color=C[1], lw=2.2, label="degenerate minima")
    ax3.set_xlabel(r"$\phi_1$")
    ax3.set_ylabel(r"$\phi_2$")
    ax3.set_zlabel(r"$V/(\mu^4/\lambda)$", labelpad=10)
    ax3.tick_params(axis="z", pad=6)
    ax3.set_zlim(-0.3, 0.05)
    ax3.view_init(elev=24, azim=-58)
    ax3.set_title("Two-component cross-section")
    ax3.legend(loc="upper left", fontsize=8)

    ax = fig.add_subplot(1, 2, 2)
    x = np.linspace(-1.0, 1.0, 400)
    ax.plot(x, V(np.abs(x)), color=C[0])
    ax.axhline(0, color=GREY, lw=0.8)
    ax.plot([0], [0], "o", color=INK)
    ax.annotate("local maximum\n(symmetric point)", (0, 0), (0, 0.11),
                ha="center", fontsize=8.5,
                arrowprops=dict(arrowstyle="->", color=INK, lw=0.8))
    for s in (-1, 1):
        ax.plot([s * rmin], [Vmin], "o", color=C[1])
    ax.annotate("", (rmin, Vmin), (rmin, 0),
                arrowprops=dict(arrowstyle="<->", color=GREY, lw=0.8))
    ax.text(rmin + 0.03, Vmin / 2, r"depth $-\mu^4/4\lambda$", fontsize=8.5,
            va="center")
    ax.axvline(rmin, color=C[1], ls=":", lw=0.9)
    ax.axvline(-rmin, color=C[1], ls=":", lw=0.9)
    ax.text(rmin, 0.21, r"$|\phi| = v/\sqrt{2}$", color=C[1], ha="center",
            fontsize=9)
    # Higgs (radial, curved) vs Goldstone (around the rim, flat) directions
    ax.annotate("", (rmin + 0.2, V(rmin + 0.2)), (rmin, Vmin + 0.005),
                arrowprops=dict(arrowstyle="->", color=C[2], lw=1.6,
                                connectionstyle="arc3,rad=0.25"))
    ax.text(0.92, 0.0, "Higgs $h$:\nradial,\ncurved\n(massive)", color=C[2],
            fontsize=8.5, ha="center", va="bottom")
    ax.text(0.0, -0.33,
            "Goldstone: along the rim of minima (out of the page),\n"
            "flat direction, massless",
            color=C[3], fontsize=8.5, ha="center", va="center")
    ax.set_xlim(-1.0, 1.0)
    ax.set_ylim(-0.38, 0.28)
    ax.set_xlabel(r"$\phi_1$  (slice at $\phi_2=0$),  units of $v$")
    ax.set_ylabel(r"$V/(\mu^4/\lambda)$")
    ax.set_title(r"Slice: $V=-\mu^2|\phi|^2+\lambda|\phi|^4$")
    save(fig, __file__, "mexican-hat")


def running_couplings():
    """§0.4.4 SU(3)_C term: one-loop running of the three gauge couplings.

    1/alpha_i(mu) = 1/alpha_i(M_Z) - (b_i / 2 pi) ln(mu / M_Z),
    b = (41/10, -19/6, -7) with GUT-normalised U(1)_Y; standard SM inputs
    1/alpha_i(M_Z) = 59.0, 29.6, 8.5 (not quoted in the text).
    """
    MZ = 91.19
    inv0 = np.array([59.0, 29.6, 8.5])
    b = np.array([41 / 10, -19 / 6, -7.0])
    mu = np.logspace(2, 19, 400)
    L = np.log(mu / MZ)
    inv = inv0[:, None] - b[:, None] / (2 * np.pi) * L

    fig, ax = fig_ax(h=4.0)
    labels = [r"$1/\alpha_1$  U(1)$_Y$ (GUT norm.)", r"$1/\alpha_2$  SU(2)$_L$",
              r"$1/\alpha_3$  SU(3)$_C$"]
    for i in range(3):
        ax.plot(mu, inv[i], color=C[i], label=labels[i])
    # pairwise crossings
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        Lx = (inv0[i] - inv0[j]) * 2 * np.pi / (b[i] - b[j])
        mux = MZ * np.exp(Lx)
        yx = inv0[i] - b[i] / (2 * np.pi) * Lx
        ax.plot([mux], [yx], "o", ms=4, color=INK)
    ax.axvspan(1e13, 1e17, color=SHADE, alpha=0.10)
    ax.text(3e14, 57, "near miss:\nthree pairwise crossings\n$10^{13}$–$10^{17}$ GeV",
            ha="center", va="top", fontsize=8.5)
    ax.set_xscale("log")
    ax.set_xlim(1e2, 1e19)
    ax.set_ylim(0, 62)
    ax.set_xlabel(r"energy scale $\mu$ (GeV)")
    ax.set_ylabel(r"inverse coupling $1/\alpha_i$")
    ax.set_title("One-loop Standard Model running (no unification)")
    ax.legend(loc="lower right")
    save(fig, __file__, "running-couplings")


def fermion_masses():
    """§0.8 The Objects: charged-fermion masses m_f = y_f v / sqrt(2).

    PDG central values; Yukawa y = sqrt(2) m / v with v = 246 GeV.
    Neutrinos shown only as the direct upper bound m < 0.8 eV.
    """
    v = 246.0  # GeV
    gen = np.array([1, 2, 3])
    up = np.array([2.16e-3, 1.27, 172.7])       # u c t   (GeV)
    down = np.array([4.67e-3, 93.4e-3, 4.18])   # d s b
    lep = np.array([0.511e-3, 105.66e-3, 1.7769])  # e mu tau
    names = {"up": ["u", "c", "t"], "down": ["d", "s", "b"],
             "lep": ["e", r"$\mu$", r"$\tau$"]}

    fig, ax = fig_ax(h=4.2)
    off = {"up": -0.12, "down": 0.0, "lep": 0.12}
    sets = [("up", up, C[1], "up-type quarks"),
            ("down", down, C[0], "down-type quarks"),
            ("lep", lep, C[2], "charged leptons")]
    for key, m, col, lab in sets:
        x = gen + off[key]
        ax.plot(x, m, "o-", color=col, label=lab, ms=6, lw=1.0)
        for xi, mi, nm in zip(x, m, names[key]):
            ax.text(xi + 0.05, mi, nm, color=col, fontsize=9, va="center")
    nu = 0.8e-9  # GeV
    for g in gen:
        ax.plot([g + 0.24], [nu], marker="v", color=C[3], ms=7, ls="none",
                label="neutrinos: $m<0.8$ eV (bound)" if g == 1 else None)
        ax.annotate("", (g + 0.24, nu / 30), (g + 0.24, nu),
                    arrowprops=dict(arrowstyle="->", color=C[3], lw=0.9))
    ax.annotate("", (2.84, 172.7), (1.2, 0.511e-3),
                arrowprops=dict(arrowstyle="<->", color=GREY, lw=0.8, ls="--"))
    ax.text(2.25, 2e-3, r"$m_t/m_e \approx 3.4\times10^5$", color=INK,
            fontsize=9, ha="center")
    ax.axhline(v / np.sqrt(2), color=GREY, lw=0.8, ls=":")
    ax.text(0.62, v / np.sqrt(2) * 1.5, r"$v/\sqrt{2}$ ($y=1$)", color=GREY,
            fontsize=8.5)
    ax.set_yscale("log")
    ax.set_ylim(1e-11, 3e3)
    ax.set_xlim(0.55, 3.55)
    ax.set_xticks(gen, ["generation 1", "generation 2", "generation 3"])
    ax.grid(axis="x", visible=False)
    ax.set_ylabel("mass (GeV)")
    sec = ax.secondary_yaxis("right", functions=(lambda m: np.sqrt(2) * m / v,
                                                 lambda y: y * v / np.sqrt(2)))
    sec.set_ylabel(r"Yukawa coupling $y_f=\sqrt{2}\,m_f/v$")
    ax.set_title("Fermion masses by generation")
    ax.legend(loc="lower left", bbox_to_anchor=(0.0, 0.2), fontsize=8.5)
    save(fig, __file__, "fermion-masses")


if __name__ == "__main__":
    mexican_hat()
    running_couplings()
    fermion_masses()
