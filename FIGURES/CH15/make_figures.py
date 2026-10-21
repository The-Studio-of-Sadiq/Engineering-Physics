"""Figures for Chapter 15 — Continuum Mechanics."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax

from matplotlib.patches import Rectangle, Polygon


def _wall(ax, y, x0, x1, up):
    """Hatched no-slip wall along y between x0 and x1 (hatch on the outside)."""
    h = 0.08
    ax.add_patch(Rectangle((x0, y if up else y - h), x1 - x0, h, fc="white", ec=INK,
                           hatch="////", lw=0))
    ax.plot([x0, x1], [y, y], color=INK, lw=1.5)


def poiseuille_couette():
    """§15.7.1–15.7.2 Laminar profiles.

    Poiseuille: v_z/v_max = 1 - (r/R)^2.  Couette: v_x/U = y/h.
    """
    fig, (a1, a2) = fig_ax(ncols=2, h=3.4)
    for ax in (a1, a2):
        ax.set_aspect("equal")
        ax.grid(False)
        for sp in ax.spines.values():
            sp.set_visible(False)
        ax.set_xticks([])
        ax.set_yticks([])

    # Poiseuille in a pipe, r/R from -1 to 1
    r = np.linspace(-1, 1, 200)
    v = 1 - r**2
    x0 = 0.3
    a1.plot(x0 + 1.6 * v, r, color=C[0], lw=2)
    a1.plot([x0, x0], [-1, 1], color=GREY, lw=1, ls="--")
    for ri in np.linspace(-0.9, 0.9, 9):
        L = 1.6 * (1 - ri**2)
        a1.annotate("", (x0 + L, ri), (x0, ri),
                    arrowprops=dict(arrowstyle="-|>", color=C[0], lw=1, mutation_scale=9))
    _wall(a1, 1, -0.1, 2.4, True)
    _wall(a1, -1, -0.1, 2.4, False)
    a1.plot([-0.05, 2.35], [0, 0], color=GREY, lw=0.6, ls="-.")
    a1.text(x0 + 1.65, 0.05, r"$v_{max}=\frac{GR^2}{4\mu}$", fontsize=9, va="bottom")
    a1.text(1.25, -0.75, r"$\frac{v_z}{v_{max}}=1-\frac{r^2}{R^2}$", fontsize=10)
    a1.text(-0.12, 0.0, "axis", ha="right", va="center", fontsize=8, color=GREY)
    a1.text(-0.12, 1.0, r"$r=R$", ha="right", va="center", fontsize=9)
    a1.text(-0.12, -1.0, r"$r=-R$", ha="right", va="center", fontsize=9)
    a1.set_xlim(-0.7, 2.5)
    a1.set_ylim(-1.25, 1.25)
    a1.set_title("Poiseuille (pressure-driven pipe flow)")

    # Couette between plates, y/h from 0 to 1
    y = np.linspace(0, 1, 50)
    x0 = 0.2
    a2.plot(x0 + 1.6 * y, y, color=C[1], lw=2)
    a2.plot([x0, x0], [0, 1], color=GREY, lw=1, ls="--")
    for yi in np.linspace(0.1, 1.0, 10):
        a2.annotate("", (x0 + 1.6 * yi, yi), (x0, yi),
                    arrowprops=dict(arrowstyle="-|>", color=C[1], lw=1, mutation_scale=9))
    _wall(a2, 1.0, -0.1, 2.4, True)
    _wall(a2, 0.0, -0.1, 2.4, False)
    a2.annotate("", (2.3, 1.18), (1.5, 1.18),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.4, mutation_scale=12))
    a2.text(1.9, 1.22, "moving plate, $U$", ha="center", va="bottom", fontsize=9)
    a2.text(1.2, -0.17, "plate at rest", ha="center", va="top", fontsize=9)
    a2.text(1.15, 0.3, r"$\frac{v_x}{U}=\frac{y}{h}$" + "\n" + r"$\tau_w=\mu U/h$", fontsize=10)
    a2.text(-0.12, 1.0, r"$y=h$", ha="right", va="center", fontsize=9)
    a2.text(-0.12, 0.0, r"$y=0$", ha="right", va="center", fontsize=9)
    a2.set_xlim(-0.7, 2.5)
    a2.set_ylim(-0.4, 1.45)
    a2.set_title("Couette (shear-driven, no pressure gradient)")
    save(fig, __file__, "poiseuille-couette")


def vp_vs_ratio():
    """§15.10.2 v_P/v_S = sqrt(2(1-nu)/(1-2nu)); materials from the §15.10.1 table,
    with nu back-computed from the tabulated speed ratio."""
    nu = np.linspace(0, 0.49, 400)
    ratio = np.sqrt(2 * (1 - nu) / (1 - 2 * nu))
    fig, ax = fig_ax()
    ax.plot(nu, ratio, color=C[0], lw=2, label=r"$\sqrt{2(1-\nu)/(1-2\nu)}$")
    mats = [("Steel", 5960, 3235), ("Aluminum", 6420, 3040), ("Granite", 5950, 3640)]
    spots = {"Steel": (0.22, 3.4), "Aluminum": (0.40, 1.3), "Granite": (0.06, 2.6)}
    for (name, vp, vs), col in zip(mats, C[1:]):
        r = vp / vs
        n = (r**2 - 2) / (2 * (r**2 - 1))
        ax.plot(n, r, "o", color=col, ms=7, zorder=3)
        ax.annotate(f"{name}\n" + rf"$\nu={n:.2f}$, ratio {r:.2f}", (n, r), xytext=spots[name],
                    ha="left", fontsize=8.5, color=col,
                    arrowprops=dict(arrowstyle="-", color=col, lw=0.7))
    ax.plot([0], [np.sqrt(2)], "s", color=GREY)
    ax.annotate(r"$\nu=0$ (cork-like): $\sqrt{2}$", (0, np.sqrt(2)), xytext=(8, 6),
                textcoords="offset points", fontsize=8.5, color=GREY, va="bottom")
    ax.axvline(0.5, color=GREY, lw=1, ls="--")
    ax.text(0.485, 6.5, r"$\nu\to0.5$: incompressible," + "\n" + r"$v_P/v_S\to\infty$", ha="right",
            fontsize=8.5, color=GREY)
    ax.text(0.02, 7.3, r"fluids ($G=0$, water, air): $v_S=0$, ratio $\infty$", fontsize=8.5, color=GREY)
    ax.set_xlim(0, 0.52)
    ax.set_ylim(1, 8)
    ax.set_xlabel(r"Poisson's ratio $\nu_P$")
    ax.set_ylabel(r"$v_P/v_S$")
    ax.set_title("P- to S-wave speed ratio")
    ax.legend(loc="center left")
    save(fig, __file__, "vp-vs-ratio")


def yield_loci():
    """§15.11.1–15.11.2 Plane-stress yield loci (sigma_3 = 0).

    von Mises: s1^2 - s1 s2 + s2^2 = sy^2;  Tresca: max(|s1|, |s2|, |s1-s2|) = sy.
    """
    th = np.linspace(0, 2 * np.pi, 600)
    # ellipse: principal axes along (1,1) and (1,-1): semi-axes sqrt(2) and sqrt(2/3)
    a, b = np.sqrt(2), np.sqrt(2 / 3)
    u, w = a * np.cos(th), b * np.sin(th)
    s1, s2 = (u - w) / np.sqrt(2), (u + w) / np.sqrt(2)
    fig, ax = plt.subplots(figsize=(5.2, 5.0))
    ax.axhline(0, color=INK, lw=0.8)
    ax.axvline(0, color=INK, lw=0.8)
    ax.plot(s1, s2, color=C[0], lw=2, label="von Mises")
    hexv = np.array([[1, 0], [1, 1], [0, 1], [-1, 0], [-1, -1], [0, -1], [1, 0]])
    ax.add_patch(Polygon(hexv[:-1], closed=True, fc=SHADE, alpha=0.10, ec="none"))
    ax.plot(hexv[:, 0], hexv[:, 1], color=C[1], lw=2, label="Tresca")
    ax.plot([-1.5, 1.5], [1.5, -1.5], color=GREY, lw=0.8, ls=":")
    for p in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ax.plot(*p, "o", color=INK, ms=5, zorder=4)
    ax.annotate("uniaxial: both\ncriteria agree", (1, 0), xytext=(1.08, -0.45), fontsize=8.5,
                arrowprops=dict(arrowstyle="-", lw=0.7))
    ax.plot([1, -1], [1, -1], "D", color=INK, ms=4.5, zorder=4)
    ax.annotate("equibiaxial", (1, 1), xytext=(1.05, 1.06), fontsize=8.5)
    tv, tt = 1 / np.sqrt(3), 0.5
    ax.plot([tv, -tv], [-tv, tv], "o", color=C[0], ms=6, zorder=4)
    ax.plot([tt, -tt], [-tt, tt], "o", color=C[1], ms=6, zorder=4)
    ax.annotate(r"pure shear $\sigma_1=-\sigma_2=\tau$:" + "\n"
                + r"von Mises $\tau_y=\sigma_y/\sqrt{3}=0.577\sigma_y$" + "\n"
                + r"Tresca $\tau_y=\sigma_y/2$",
                (tv, -tv), xytext=(0.15, -1.45), fontsize=8.5,
                arrowprops=dict(arrowstyle="-", lw=0.7))
    ax.set_aspect("equal")
    ax.set_xlim(-1.5, 1.6)
    ax.set_ylim(-1.6, 1.5)
    ax.set_xlabel(r"$\sigma_1/\sigma_y$")
    ax.set_ylabel(r"$\sigma_2/\sigma_y$")
    ax.set_title(r"Plane-stress yield loci ($\sigma_3=0$)")
    ax.legend(loc="upper left")
    save(fig, __file__, "yield-loci")


def rheology_curves():
    """§15.12.2 Flow curves tau(gamma_dot): Newtonian tau = mu*g, power law
    tau = K g^n (n = 0.5, 1.5), Bingham tau = tau0 + mu_B g (tau0 = 0.5)."""
    g = np.linspace(0, 2, 400)
    fig, ax = fig_ax()
    ax.plot(g, g, color=INK, label=r"Newtonian, $\tau=\mu\dot\varepsilon$")
    ax.plot(g, g**0.5, color=C[0], label=r"shear-thinning, $n=0.5$")
    ax.plot(g, g**1.5, color=C[1], label=r"shear-thickening, $n=1.5$")
    ax.plot(g, 0.5 + g, color=C[2], label=r"Bingham, $\tau=\tau_0+\mu_B\dot\varepsilon$")
    ax.plot([0, 0], [0, 0.5], color=C[2], lw=2.5)
    ax.text(0.03, 0.66, r"$\tau_0$ (yield stress)", color=C[2], fontsize=8.5, va="bottom")
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2.8)
    ax.set_xlabel(r"shear rate $\dot\varepsilon$ (arb. units)")
    ax.set_ylabel(r"shear stress $\tau$ (arb. units)")
    ax.set_title(r"Flow curves; effective viscosity $\mu_{eff}=\tau/\dot\varepsilon$ is the secant slope")
    ax.legend(loc="upper left")
    save(fig, __file__, "rheology-curves")


if __name__ == "__main__":
    poiseuille_couette()
    vp_vs_ratio()
    yield_loci()
    rheology_curves()
