"""Figures for Chapter 8 (weak-field GR, gravitational waves, GPS)."""

import os
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax
from scipy.integrate import solve_ivp


def out(fig, slug):
    """Save SVG; also a PNG preview if FIG_PREVIEW_DIR is set (for review only)."""
    prev = os.environ.get("FIG_PREVIEW_DIR")
    if prev:
        fig.tight_layout()
        fig.savefig(pathlib.Path(prev) / f"{slug}.png", dpi=110, bbox_inches="tight")
    save(fig, __file__, slug)


# ---------------------------------------------------------------------------
def gw_polarizations():
    """§8.6.1: ring of free test particles in the z = 0 plane under a GW along z.

    h_+ :  dx = +(h/2) x cos(wt),  dy = -(h/2) y cos(wt)
    h_x :  dx = +(h/2) y cos(wt),  dy = +(h/2) x cos(wt)
    with h = 0.3 (wildly exaggerated; real strains are ~1e-21).
    """
    h = 0.3
    th = np.linspace(0, 2 * np.pi, 16, endpoint=False)
    tc = np.linspace(0, 2 * np.pi, 200)
    phases = [0, np.pi / 2, np.pi, 3 * np.pi / 2]
    plabels = ["0", r"\pi/2", r"\pi", r"3\pi/2"]
    fig, axes = plt.subplots(2, 4, figsize=(9.0, 4.8))
    for row, pol in enumerate(("+", "x")):
        for col, ph in enumerate(phases):
            ax = axes[row, col]
            c = np.cos(ph)
            for xs, ys, kw in ((np.cos(th), np.sin(th), dict(ls="none", marker="o", ms=5, color=C[row])),
                               (np.cos(tc), np.sin(tc), dict(color=C[row], lw=0.8))):
                if pol == "+":
                    X, Y = xs * (1 + h / 2 * c), ys * (1 - h / 2 * c)
                else:
                    X, Y = xs + h / 2 * ys * c, ys + h / 2 * xs * c
                ax.plot(X, Y, **kw)
            ax.plot(np.cos(tc), np.sin(tc), color=GREY, lw=0.6, ls=":")
            ax.set_aspect("equal")
            ax.set_xlim(-1.35, 1.35)
            ax.set_ylim(-1.35, 1.35)
            ax.set_xticks([])
            ax.set_yticks([])
            ax.grid(False)
            for sp in ax.spines.values():
                sp.set_visible(False)
            if row == 0:
                ax.set_title(fr"$\omega t={plabels[col]}$")
        axes[row, 0].set_ylabel(r"$h_+$" if pol == "+" else r"$h_\times$", rotation=0,
                                fontsize=13, labelpad=18, va="center")
    out(fig, "gw-polarizations")


# ---------------------------------------------------------------------------
def gr_effective_potential():
    """§8.7.1: (a) per-unit-mass effective potential, Newton vs GR;
    (b) exaggerated precessing orbit.

    (a) V/c^2 = -r_s/(2r) + l^2/(2r^2) - r_s l^2/(2 r^3), r in units of r_s,
        l = L/(m r_s c); here l^2 = 4 (above the ISCO value l^2 = 3).
    (b) u'' + u = GM/l^2 + 3 GM u^2/c^2  ->  w'' + w = 1 + eps w^2, w = u p,
        p = l^2/GM, eps = 3 GM/(c^2 p); eps = 0.04, e = 0.5.  Precession per
        orbit ~ 2 pi eps = 6 pi GM/(c^2 p).
    """
    fig, (a1, a2) = fig_ax(ncols=2, w=10.5, h=4.3)
    r = np.linspace(1.0, 40, 3000)
    l2 = 4.0
    VN = -1 / (2 * r) + l2 / (2 * r**2)
    VG = VN - l2 / (2 * r**3)
    a1.plot(r, VN, color=C[0], label=r"Newton: $-\dfrac{GM}{r}+\dfrac{L^2}{2m^2r^2}$")
    a1.plot(r, VG, color=C[1], label=r"GR: $\ldots-\dfrac{GML^2}{m^2c^2r^3}$")
    a1.axhline(0, color=INK, lw=0.6)
    a1.set_xlim(1, 40)
    a1.set_ylim(-0.08, 0.16)
    a1.set_xlabel(r"$r\ /\ r_s$")
    a1.set_ylabel(r"$V_{\rm eff}/(mc^2)$")
    a1.set_title(r"(a) Effective potential, $L/(m r_s c)=2$")
    rmax = r[np.argmax(VG)]
    a1.annotate("GR barrier peak:\nfall-in possible", xy=(rmax, VG.max()), xytext=(7, 0.11),
                arrowprops=dict(arrowstyle="->", color=INK), fontsize=8)
    a1.legend(loc="lower right", fontsize=8)

    eps, e = 0.04, 0.5
    phi = np.linspace(0, 12 * np.pi, 6000)
    sol = solve_ivp(lambda p, y: [y[1], 1 + eps * y[0] ** 2 - y[0]], (phi[0], phi[-1]),
                    [1 + e, 0.0], t_eval=phi, rtol=1e-10, atol=1e-12)
    rr = 1 / sol.y[0]
    a2.plot(rr * np.cos(phi), rr * np.sin(phi), color=C[1], lw=1.0, label="GR orbit (6 revolutions)")
    rn = 1 / (1 + e * np.cos(phi[:1200]))
    a2.plot(rn * np.cos(phi[:1200]), rn * np.sin(phi[:1200]), color=C[0], ls="--", lw=1.2,
            label="Newtonian ellipse (closed)")
    # perihelion directions
    wv = sol.y[0]
    idx = [i for i in range(1, len(wv) - 1) if wv[i] > wv[i - 1] and wv[i] >= wv[i + 1]]
    for i in [0] + idx:
        a2.plot([0, rr[i] * np.cos(phi[i])], [0, rr[i] * np.sin(phi[i])], color=GREY, lw=0.6)
    a2.plot(0, 0, "o", color=C[4], ms=8)
    a2.set_aspect("equal")
    a2.set_title(r"(b) Precessing orbit (exaggerated: $6\pi GM/c^2p\approx14°$/orbit)")
    a2.set_xlabel(r"$x\ /\ p$")
    a2.set_ylabel(r"$y\ /\ p$")
    a2.legend(loc="upper right", fontsize=8)
    lim = 2.3
    a2.set_xlim(-lim, lim)
    a2.set_ylim(-lim, lim)
    out(fig, "gr-effective-potential")


# ---------------------------------------------------------------------------
def gps_clock():
    """§8.8: fractional rate offset of an orbiting clock vs a ground clock.

    GR:  +GM(1/R_E - 1/r)/c^2;  SR (circular orbit): -GM/(2 r c^2);  in us/day.
    Ground-clock rotation (~0.1 us/day effect) neglected, as in the text.
    """
    GM, c, RE = 3.986004e14, 2.99792458e8, 6.371e6
    day = 86400e6
    x = np.linspace(1.0, 7.0, 600)
    r = x * RE
    gr = GM * (1 / RE - 1 / r) / c**2 * day
    sr = -GM / (2 * r * c**2) * day
    fig, ax = fig_ax(w=6.6, h=4.0)
    ax.plot(x, gr, color=C[0], label=r"gravitational (GR): $+GM(1/R_\oplus-1/r)/c^2$")
    ax.plot(x, sr, color=C[1], label=r"velocity (SR): $-GM/2rc^2$")
    ax.plot(x, gr + sr, color=INK, label="net")
    ax.axhline(0, color=INK, lw=0.6)
    rg = 2.659e7 / RE
    for val, col in ((GM * (1 / RE - 1 / 2.659e7) / c**2 * day, C[0]), (-GM / (2 * 2.659e7 * c**2) * day, C[1]),
                     (GM * (1 / RE - 1.5 / 2.659e7) / c**2 * day, INK)):
        ax.plot(rg, val, "o", color=col, ms=5)
        ax.text(rg + 0.1, val - 1.5, f"{val:+.1f}", fontsize=9, color=col, va="top")
    ax.axvline(rg, color=GREY, lw=0.7, ls=":")
    ax.text(rg + 0.08, -12, "GPS\n$r=2.659\\times10^7$ m", fontsize=8, ha="left", va="top")
    ax.plot(1.5, 0, "s", color=INK, ms=5)
    ax.annotate(r"net $=0$ at $r=1.5R_\oplus$", xy=(1.5, 0), xytext=(1.9, -18),
                arrowprops=dict(arrowstyle="->", color=INK), fontsize=8)
    riss = (RE + 4.2e5)
    net_iss = (GM * (1 / RE - 1 / riss) - GM / (2 * riss)) / c**2 * day
    ax.plot(riss / RE, net_iss, "D", color=C[3], ms=5)
    ax.annotate(f"ISS (420 km): net {net_iss:+.0f} μs/day\n(clock runs slow)", xy=(riss / RE, net_iss),
                xytext=(1.25, -38), arrowprops=dict(arrowstyle="->", color=C[3]), fontsize=8, color=C[3])
    ax.set_xlim(1, 7)
    ax.set_ylim(-45, 55)
    ax.set_xlabel(r"orbital radius $r\ /\ R_\oplus$")
    ax.set_ylabel(r"clock rate vs ground ($\mu$s/day)")
    ax.legend(loc="lower right", fontsize=8)
    out(fig, "gps-clock")


# ---------------------------------------------------------------------------
def gr_strength_scale():
    """§8.9: compactness r_s/r for the contexts in the validity table (log scale).

    Values computed: r_s = 2GM/c^2 for Earth (8.87 mm), Sun (2.95 km),
    0.6 M_sun white dwarf (R ~ 7000 km), 1.4 M_sun neutron star (R ~ 12 km).
    """
    G, c, Ms = 6.674e-11, 2.99792458e8, 1.989e30
    rsE, rsS = 2 * 3.986004e14 / c**2, 2 * G * Ms / c**2
    rows = [
        ("Civil engineering on Earth", rsE / 6.371e6),
        ("GPS satellite orbit", rsE / 2.659e7),
        ("Mercury's orbit", rsS / 5.79e10),
        ("Solar corona (grazing light)", rsS / 6.96e8),
        ("White dwarf surface", 0.6 * rsS / 7.0e6),
        ("Neutron star surface", 1.4 * rsS / 1.2e4),
        ("Black hole horizon", 1.0),
    ]
    fig, ax = fig_ax(w=7.0, h=3.9)
    y = np.arange(len(rows))[::-1]
    for (name, v), yi in zip(rows, y):
        ax.barh(yi, np.log10(v) + 11, left=-11, color=C[0], height=0.55)
        ax.text(np.log10(v) + 0.15, yi, f"{v:.1e}" if v < 0.99 else "1", va="center", fontsize=8)
    ax.set_yticks(y)
    ax.set_yticklabels([n for n, _ in rows], fontsize=9)
    bands = [(-11, -5, C[2], "Newton adequate\n(PN corrections only for\nprecision timing/astrometry)"),
             (-5, -1, C[4], "post-Newtonian"),
             (-1, 0.8, C[1], "full GR")]
    for lo, hi, col, lab in bands:
        ax.axvspan(lo, hi, color=col, alpha=0.12, lw=0)
        ax.text((lo + hi) / 2, len(rows) - 0.35, lab, ha="center", va="bottom", fontsize=8, color=INK)
    ax.set_xlim(-11, 0.8)
    ax.set_ylim(-0.6, len(rows) + 0.9)
    ax.set_xticks(range(-10, 1, 2))
    ax.set_xticklabels([fr"$10^{{{k}}}$" for k in range(-10, 1, 2)])
    ax.set_xlabel(r"compactness $r_s/r = 2GM/rc^2$")
    ax.grid(axis="y", visible=False)
    out(fig, "gr-strength-scale")


if __name__ == "__main__":
    gw_polarizations()
    gr_effective_potential()
    gps_clock()
    gr_strength_scale()
