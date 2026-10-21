"""Figures for Chapter 20 — CE and ChE Systems: Structures, Hydraulics, and Process Engineering."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax


def beam_deflections():
    """§20.2.2 — Euler-Bernoulli elastic curves, normalised by the table's w_max.

    xi = x/L measured from the fixed end (cantilever) or left support.
      cantilever, tip load P:   w = P x^2 (3L - x) / 6EI          max PL^3/3EI
      cantilever, UDL q:        w = q x^2 (6L^2 - 4Lx + x^2)/24EI  max qL^4/8EI
      simply supported, P mid:  w = P x (3L^2 - 4x^2)/48EI (x<L/2) max PL^3/48EI
      simply supported, UDL q:  w = q x (L^3 - 2Lx^2 + x^3)/24EI   max 5qL^4/384EI
      fixed-fixed, P mid:       w = P x^2 (3L - 4x)/48EI (x<L/2)   max PL^3/192EI
    """
    xi = np.linspace(0, 1, 801)
    h = np.minimum(xi, 1 - xi)  # symmetric half-span coordinate
    cases = [
        ("cantilever, tip load", xi**2 * (3 - xi) / 6, 1 / 3),
        ("cantilever, UDL", xi**2 * (6 - 4 * xi + xi**2) / 24, 1 / 8),
        ("simply supported, centre load", h * (3 - 4 * h**2) / 48, 1 / 48),
        ("simply supported, UDL", xi * (1 - 2 * xi**2 + xi**3) / 24, 5 / 384),
        ("fixed–fixed, centre load", h**2 * (3 - 4 * h) / 48, 1 / 192),
    ]
    fig, ax = fig_ax(h=3.8, w=8.4)
    for i, (name, w, table_max) in enumerate(cases):
        # closed-form curve (in units of load*L^n/EI) must peak at the table value
        assert abs(w.max() / table_max - 1) < 1e-4, name
        ax.plot(xi, -w / table_max, color=C[i], ls="-" if i < 2 else "--" if i < 4 else ":",
                label=name)
    ax.axhline(0, color=INK, lw=0.8)
    ax.set_xlim(0, 1)
    ax.set_ylim(-1.08, 0.05)
    ax.set_xlabel(r"position $x/L$ (from fixed end or left support)")
    ax.set_ylabel(r"deflection $-w(x)/w_{max}$")
    ax.set_title("Normalised elastic curves of the standard beam cases")
    ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.5), fontsize=8)
    save(fig, __file__, "beam-deflections")


def specific_energy():
    """§20.3.2 — specific energy E = y + q^2/(2 g y^2) in a rectangular channel.

    q = 2 m^2/s: y_c = (q^2/g)^(1/3) = 0.742 m, E_min = 1.5 y_c = 1.11 m.
    Upper branch (y > y_c) subcritical, lower branch supercritical.
    """
    g, q = 9.81, 2.0
    yc = (q**2 / g) ** (1 / 3)
    Emin = 1.5 * yc
    y = np.linspace(0.2, 3.0, 1000)
    E = y + q**2 / (2 * g * y**2)
    fig, ax = fig_ax(h=4.0, w=5.8)
    sub, sup = y >= yc, y <= yc
    ax.plot(E[sub], y[sub], color=C[0], label="subcritical ($Fr<1$)")
    ax.plot(E[sup], y[sup], color=C[1], label="supercritical ($Fr>1$)")
    ax.plot([0, 3], [0, 3], color=GREY, lw=0.8, ls=":")
    ax.text(2.45, 2.30, "$E=y$", color=GREY, fontsize=8)
    ax.plot(Emin, yc, "o", color=INK, ms=5, zorder=5)
    ax.plot([Emin, Emin], [0, yc], color=GREY, lw=0.8, ls="--")
    ax.plot([0, Emin], [yc, yc], color=GREY, lw=0.8, ls="--")
    ax.annotate("critical point\n" + rf"$y_c={yc:.2f}$ m" + "\n"
                + rf"$E_{{min}}=1.5y_c={Emin:.2f}$ m",
                xy=(Emin, yc), xytext=(0.08, 1.05), fontsize=8,
                arrowprops=dict(arrowstyle="->", color=GREY))
    # alternate depths at E = 1.5 m
    E1 = 1.5
    roots = np.roots([1, -E1, 0, q**2 / (2 * g)])
    alt = sorted(r.real for r in roots if abs(r.imag) < 1e-9 and r.real > 0)
    ax.axvline(E1, color=C[2], lw=0.8)
    for ya in alt:
        ax.plot(E1, ya, "s", color=C[2], ms=4)
    ax.text(E1 + 0.07, 0.85, f"$E={E1}$ m: alternate\ndepths {alt[0]:.2f} m\nand {alt[1]:.2f} m",
            fontsize=8, color=C[2])
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_aspect("equal")
    ax.set_xlabel(r"specific energy $E$ [m]")
    ax.set_ylabel(r"depth $y$ [m]")
    ax.set_title(r"Rectangular channel, $q=2$ m$^2$/s")
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, 0.86))
    save(fig, __file__, "specific-energy")


def terzaghi_consolidation():
    """§20.4.2 — average degree of consolidation
    U = 1 - (8/pi^2) sum_n exp(-(2n+1)^2 pi^2 T_v / 4) / (2n+1)^2   (50 terms),
    with early-time asymptote U = sqrt(4 T_v / pi) and T_v = 0.848 -> U = 90%.
    """
    Tv = np.logspace(-3, 1, 600)
    m = 2 * np.arange(50)[:, None] + 1
    U = 1 - (8 / np.pi**2) * np.sum(np.exp(-(m**2) * np.pi**2 * Tv / 4) / m**2, axis=0)
    fig, ax = fig_ax(h=3.8)
    ax.semilogx(Tv, 100 * U, color=C[0], label="series solution (50 terms)")
    early = Tv < 0.5
    ax.semilogx(Tv[early], 100 * np.sqrt(4 * Tv[early] / np.pi), "--", color=C[1],
                label=r"early asymptote $U=\sqrt{4T_v/\pi}$")
    for T, lab in [(0.197, "50%"), (0.848, "90%")]:
        Ut = 1 - (8 / np.pi**2) * np.sum(np.exp(-(m[:, 0] ** 2) * np.pi**2 * T / 4) / m[:, 0] ** 2)
        ax.plot(T, 100 * Ut, "o", color=INK, ms=5, zorder=5)
        ax.annotate(rf"$T_v={T}$: $U={100*Ut:.0f}\%$", xy=(T, 100 * Ut),
                    xytext=(T * 0.04, 100 * Ut + 6), fontsize=8,
                    arrowprops=dict(arrowstyle="->", color=GREY))
    ax.set_xlim(1e-3, 10)
    ax.set_ylim(0, 105)
    ax.set_xlabel(r"time factor $T_v=c_vt/H_{dr}^2$")
    ax.set_ylabel(r"degree of consolidation $U$ [%]")
    ax.set_title("Terzaghi one-dimensional consolidation, uniform initial $u_e$")
    ax.legend(loc="lower right")
    save(fig, __file__, "terzaghi-consolidation")


def levenspiel():
    """§20.8.2 — Levenspiel plot for a first-order reaction, -r_A = k C_A0 (1 - X).

    F_A0/(-r_A) = (v0/k) / (1 - X); in units of v0/k:
    PFR volume = -ln(1 - X) = 1.61 at X = 0.8, CSTR volume = X/(1 - X) = 4.0.
    """
    X = np.linspace(0, 0.9, 400)
    y = 1 / (1 - X)
    Xf = 0.8
    fig, ax = fig_ax(h=3.8)
    m = X <= Xf
    ax.fill_between(X[m], 0, y[m], color=C[0], alpha=0.30,
                    label=rf"PFR volume = area: $-\ln(1-X)={-np.log(1-Xf):.2f}$")
    ax.add_patch(plt.Rectangle((0, 0), Xf, 1 / (1 - Xf), fill=False, hatch="//",
                               edgecolor=C[1], lw=1.2,
                               label=rf"CSTR volume = rectangle: $X/(1-X)={Xf/(1-Xf):.1f}$"))
    ax.plot(X, y, color=INK, label=r"$F_{A0}/(-r_A) = 1/(1-X)$")
    ax.set_xlim(0, 0.9)
    ax.set_ylim(0, 10)
    ax.set_xlabel(r"conversion $X_A$")
    ax.set_ylabel(r"$F_{A0}/(-r_A)$  [units of $v_0/k$]")
    ax.set_title(r"First-order reaction, target $X_A=0.8$: $V_{CSTR}/V_{PFR}\approx2.5$")
    ax.legend(loc="upper left")
    save(fig, __file__, "levenspiel")


if __name__ == "__main__":
    beam_deflections()
    specific_energy()
    terzaghi_consolidation()
    levenspiel()
