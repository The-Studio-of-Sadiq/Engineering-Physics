"""Figures for Chapter 17 — Bridge C: Lumped Elements and the Second-Order Template."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax

from matplotlib.patches import Rectangle, Circle, Arc, Polygon, FancyArrowPatch

ZETAS = [0.1, 0.3, 0.5, 0.707, 1.0, 2.0]


def _zcol(i):
    return C[i % len(C)]


def second_order_poles():
    """§17.7.2 Pole loci of s^2 + 2 zeta w0 s + w0^2 = 0:
    s = -zeta w0 ± w0 sqrt(zeta^2 - 1), zeta from 0 to 2 (w0 = 1)."""
    fig, ax = plt.subplots(figsize=(7.0, 3.9))
    ax.axhline(0, color=INK, lw=0.8)
    ax.axvline(0, color=INK, lw=0.8)
    ax.add_patch(Rectangle((0, -1.5), 0.6, 3.0, color=C[1], alpha=0.08, lw=0))
    ax.text(0.3, 1.32, "unstable", ha="center", fontsize=8.5, color=C[1])
    th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(th), np.sin(th), color=GREY, lw=0.8, ls=":")
    zu = np.linspace(0, 1, 300)
    for sgn in (1, -1):
        ax.plot(-zu, sgn * np.sqrt(1 - zu**2), color=C[0], lw=2.2)
    zo = np.linspace(1, 2, 300)
    ax.plot(-zo + np.sqrt(zo**2 - 1), 0 * zo, color=C[2], lw=3.0, solid_capstyle="butt")
    ax.plot(-zo - np.sqrt(zo**2 - 1), 0 * zo, color=C[2], lw=3.0, solid_capstyle="butt")
    # label alternately on the upper and lower branch so the tags do not collide
    spots = {0: (1, (6, 2), "left"), 0.3: (-1, (4, -13), "left"),
             0.5: (1, (-6, 5), "right"), 0.707: (-1, (-6, -13), "right")}
    for z, (sg, off, ha) in spots.items():
        for sgn in (1, -1):
            ax.plot(-z, sgn * np.sqrt(1 - z**2), "o", color=C[0], ms=5, zorder=4)
        ax.annotate(rf"$\zeta={z:g}$", (-z, sg * np.sqrt(1 - z**2)), xytext=off, ha=ha,
                    textcoords="offset points", fontsize=8.5, color=C[0])
    ax.plot(-1, 0, "s", color=INK, ms=6, zorder=5)
    ax.annotate(r"$\zeta=1$: double pole at $-\omega_0$", (-1, 0), xytext=(-2.45, -0.42),
                fontsize=8.5, arrowprops=dict(arrowstyle="-", lw=0.7))
    for x in (-2 + np.sqrt(3), -2 - np.sqrt(3)):
        ax.plot(x, 0, "o", color=C[2], ms=5, zorder=4)
    ax.annotate(r"$\zeta=2$: $-0.27\,\omega_0$" + "\n(slow)", (-2 + np.sqrt(3), 0), xytext=(-0.72, -0.42),
                fontsize=8.5, color=C[2])
    ax.annotate(r"$\zeta=2$: $-3.73\,\omega_0$", (-2 - np.sqrt(3), 0), xytext=(-3.9, 0.12),
                fontsize=8.5, color=C[2])
    # angle theta for zeta = 0.5
    z = 0.5
    p = (-z, np.sqrt(1 - z**2))
    ax.plot([0, p[0]], [0, p[1]], color=INK, lw=0.8, ls="--")
    ax.add_patch(Arc((0, 0), 0.6, 0.6, theta1=120, theta2=180, color=INK, lw=0.9))
    ax.text(-0.42, 0.13, r"$\theta$", fontsize=10)
    ax.text(-3.9, 1.05, "underdamped $\\zeta<1$: poles on $|s|=\\omega_0$,\n"
            r"$\mathrm{Re}\,s=-\zeta\omega_0$, $\mathrm{Im}\,s=\pm\omega_d$, $\cos\theta=\zeta$",
            fontsize=8.5, color=C[0], va="top")
    ax.text(-3.9, -0.75, "overdamped $\\zeta>1$: two real poles,\none heads to 0 (sluggish), one to $-\\infty$",
            fontsize=8.5, color=C[2], va="top")
    ax.set_aspect("equal")
    ax.set_xlim(-4.0, 0.6)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel(r"$\mathrm{Re}\,s/\omega_0$")
    ax.set_ylabel(r"$\mathrm{Im}\,s/\omega_0$")
    ax.set_title(r"Second-order pole locus as $\zeta$ goes from 0 to 2")
    save(fig, __file__, "second-order-poles")


def _step(z, t):
    """Unit-step response q/(E0 C) of w0^2/(s^2 + 2 z s + 1), w0 = 1."""
    if z < 1:
        wd = np.sqrt(1 - z**2)
        return 1 - np.exp(-z * t) * (np.cos(wd * t) + z / wd * np.sin(wd * t))
    if z == 1:
        return 1 - (1 + t) * np.exp(-t)
    s1, s2 = -z - np.sqrt(z**2 - 1), -z + np.sqrt(z**2 - 1)
    return 1 - (s2 * np.exp(s1 * t) - s1 * np.exp(s2 * t)) / (s2 - s1)


def second_order_step():
    """§17.7.3 Step response q(t)/(E0 C) vs w0 t for zeta = 0.1 … 2;
    M_p, t_r (10–90 %) and t_s (±2 %) marked on zeta = 0.3."""
    t = np.linspace(0, 20, 4000)
    fig, ax = fig_ax(h=3.9)
    ax.axhspan(0.98, 1.02, color=SHADE, alpha=0.12)
    for i, z in enumerate(ZETAS):
        ax.plot(t, _step(z, t), color=_zcol(i), lw=2.2 if z == 0.3 else 1.4,
                label=rf"$\zeta={z:g}$")
    z = 0.3
    y = _step(z, t)
    mp = np.exp(-np.pi * z / np.sqrt(1 - z**2))
    tp = np.pi / np.sqrt(1 - z**2)
    ax.plot(tp, 1 + mp, "o", color=_zcol(1))
    ax.annotate(rf"$M_p=e^{{-\pi\zeta/\sqrt{{1-\zeta^2}}}}={mp:.2f}$", (tp, 1 + mp), xytext=(4.8, 1.58),
                fontsize=8.5, color=_zcol(1), arrowprops=dict(arrowstyle="-", color=_zcol(1), lw=0.7))
    t10, t90 = t[np.argmax(y >= 0.1)], t[np.argmax(y >= 0.9)]
    ax.plot([t10, t90], [0.1, 0.9], "|", color=_zcol(1), ms=10, mew=1.5)
    ax.annotate("", (t90, 0.5), (t10, 0.5), arrowprops=dict(arrowstyle="<->", lw=0.8, color=_zcol(1)))
    ax.text(t90 + 0.25, 0.42, rf"$t_r={t90 - t10:.2f}/\omega_0$" + "\n(10–90 %)", fontsize=8.5,
            color=_zcol(1), va="top")
    outside = np.where(np.abs(y - 1) > 0.02)[0]
    ts = t[outside[-1]]
    ts_est = 4 / z
    ax.axvline(ts, color=_zcol(1), lw=0.8, ls="--")
    ax.text(ts + 0.2, 0.2, rf"$t_s={ts:.1f}/\omega_0$ (±2 %)" + "\n"
            + rf"estimate $4/\zeta\omega_0={ts_est:.1f}/\omega_0$", fontsize=8.5, color=_zcol(1))
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 2.0)
    ax.set_xlabel(r"$\omega_0 t$")
    ax.set_ylabel(r"$q(t)/E_0C$")
    ax.set_title("Second-order step response")
    ax.legend(loc="upper right", ncol=3, fontsize=8.5)
    save(fig, __file__, "second-order-step")


def second_order_bode():
    """§17.7.4 |H| (dB) and phase of H = w0^2/(w0^2 - w^2 + 2 i zeta w0 w) vs w/w0."""
    u = np.logspace(-1, 1, 1000)
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.4, 5.6), sharex=True)
    for i, z in enumerate(ZETAS):
        H = 1 / (1 - u**2 + 2j * z * u)
        a1.semilogx(u, 20 * np.log10(np.abs(H)), color=_zcol(i), label=rf"$\zeta={z:g}$")
        a2.semilogx(u, np.degrees(np.angle(H)), color=_zcol(i))
    hi = u > 1
    a1.semilogx(u[hi], -40 * np.log10(u[hi]), color=GREY, ls="--", lw=1)
    a1.text(4.0, -30, "−40 dB/decade", color=GREY, fontsize=8.5, rotation=-28)
    q = 1 / (2 * 0.1 * np.sqrt(1 - 0.01))
    a1.annotate(rf"peak $\approx Q=1/2\zeta$: {20*np.log10(q):.0f} dB ($Q=5$)", (1, 20 * np.log10(q)),
                xytext=(0.12, 12), fontsize=8.5, color=_zcol(0),
                arrowprops=dict(arrowstyle="-", color=_zcol(0), lw=0.7))
    a1.set_ylim(-45, 20)
    a1.set_ylabel(r"$|H(i\omega)|$ (dB)")
    a1.set_title("Second-order frequency response")
    a1.legend(loc="lower left", ncol=2, fontsize=8.5)
    a2.axhline(-90, color=GREY, lw=0.8, ls="--")
    a2.axvline(1, color=GREY, lw=0.8, ls="--")
    a2.text(1.1, -84, r"$-90°$ at $\omega=\omega_0$ for every $\zeta$", fontsize=8.5, color=GREY)
    a2.set_ylim(-185, 5)
    a2.set_yticks([0, -45, -90, -135, -180])
    a2.set_ylabel(r"$\angle H$ (degrees)")
    a2.set_xlabel(r"$\omega/\omega_0$")
    a2.set_xlim(0.1, 10)
    save(fig, __file__, "second-order-bode")


# ---------- schematic helpers for the R/C/L template figure ----------

def _zigzag(ax, p0, p1, n=6, w=0.09, **kw):
    p0, p1 = np.array(p0, float), np.array(p1, float)
    d = p1 - p0
    L = np.hypot(*d)
    e, nrm = d / L, np.array([-d[1], d[0]]) / L
    s = np.linspace(0.15, 0.85, 2 * n + 1)
    off = np.zeros_like(s)
    off[1:-1:2], off[2:-1:2] = w, -w
    pts = [p0] + [p0 + e * L * si + nrm * oi for si, oi in zip(s, off)] + [p1]
    pts = np.array(pts)
    ax.plot(pts[:, 0], pts[:, 1], color=INK, lw=1.4, **kw)


def _coil(ax, p0, p1, n=4, r=0.09):
    x0, x1, y = p0[0], p1[0], p0[1]
    a, b = x0 + 0.12 * (x1 - x0), x1 - 0.12 * (x1 - x0)
    ax.plot([x0, a], [y, y], color=INK, lw=1.4)
    ax.plot([b, x1], [y, y], color=INK, lw=1.4)
    xs = np.linspace(a, b, n + 1)
    for xa, xb in zip(xs[:-1], xs[1:]):
        th = np.linspace(np.pi, 0, 30)
        ax.plot((xa + xb) / 2 + (xb - xa) / 2 * np.cos(th), y + r * 1.4 * np.sin(th), color=INK, lw=1.4)


def _arrow(ax, p0, p1, col=INK, lw=1.3):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=11, color=col, lw=lw))


def _panel(ax, title):
    ax.set_xlim(-0.35, 2.75)
    ax.set_ylim(-0.95, 1.6)
    ax.set_aspect("equal")
    ax.set_axis_off()
    ax.set_title(title, fontsize=10)


def _ef(ax, e, f):
    ax.text(1.2, -0.62, f"effort $e$ = {e}\nflow $f$ = {f}", ha="center", va="top", fontsize=8.5,
            color=C[0])


def rlc_template():
    """§17.5.3 / §17.7.5 The R/C/L template in four domains: series RLC, mass–spring–damper,
    hydraulic line (inertance + resistance + accumulator), thermal RC (no inductor)."""
    fig, axs = plt.subplots(1, 4, figsize=(11, 3.3))
    lab = dict(fontsize=8.5, ha="center")

    # 1. series RLC
    ax = axs[0]
    _panel(ax, "Series RLC circuit")
    ax.add_patch(Circle((0, 0.5), 0.2, fc="white", ec=INK, lw=1.4))
    ax.text(0, 0.5, "$V_s$", ha="center", va="center", fontsize=9)
    ax.plot([0, 0], [0.7, 1.2], color=INK, lw=1.4)
    ax.plot([0, 0], [0.3, -0.2], color=INK, lw=1.4)
    ax.plot([0, 0.25], [1.2, 1.2], color=INK, lw=1.4)
    _zigzag(ax, (0.25, 1.2), (1.0, 1.2))
    _coil(ax, (1.0, 1.2), (1.85, 1.2))
    ax.plot([1.85, 2.3, 2.3], [1.2, 1.2, 0.58], color=INK, lw=1.4)
    ax.plot([2.12, 2.48], [0.58, 0.58], color=INK, lw=2)
    ax.plot([2.12, 2.48], [0.42, 0.42], color=INK, lw=2)
    ax.plot([2.3, 2.3, 0], [0.42, -0.2, -0.2], color=INK, lw=1.4)
    ax.text(0.62, 1.38, "$R$", **lab)
    ax.text(1.42, 1.42, "$L$", **lab)
    ax.text(2.6, 0.5, "$C$", fontsize=8.5, va="center")
    _arrow(ax, (2.3, 1.05), (2.3, 0.8), col=C[1])
    ax.text(2.42, 0.92, "$I$", color=C[1], fontsize=9)
    _ef(ax, "voltage $V$", "current $I$")

    # 2. mass-spring-damper
    ax = axs[1]
    _panel(ax, "Mass–spring–damper")
    ax.add_patch(Rectangle((-0.25, -0.15), 0.12, 1.45, fc="white", ec="none", hatch="////"))
    ax.plot([-0.13, -0.13], [-0.15, 1.3], color=INK, lw=1.6)
    _zigzag(ax, (-0.13, 0.95), (1.25, 0.95), n=5, w=0.1)
    ax.text(0.56, 1.12, "spring $k$ ($C=1/k$)", **lab)
    # dashpot
    yd = 0.25
    ax.plot([-0.13, 0.35], [yd, yd], color=INK, lw=1.4)
    ax.plot([0.35, 0.85, 0.85, 0.35], [yd + 0.14, yd + 0.14, yd - 0.14, yd - 0.14], color=INK, lw=1.4)
    ax.plot([0.62, 0.62], [yd - 0.1, yd + 0.1], color=INK, lw=2)
    ax.plot([0.62, 1.25], [yd, yd], color=INK, lw=1.4)
    ax.text(0.66, yd - 0.34, "damper $b$ ($R=b$)", **lab)
    ax.add_patch(Rectangle((1.25, 0.05), 0.65, 1.1, fc=C[5], alpha=0.35, ec=INK, lw=1.4))
    ax.text(1.575, 0.68, "$m$", ha="center", va="center", fontsize=11)
    ax.text(1.575, 0.38, "($I=m$)", ha="center", va="center", fontsize=8.5)
    _arrow(ax, (1.9, 0.6), (2.45, 0.6), col=INK)
    ax.text(2.2, 0.68, "$F$", fontsize=9, ha="center")
    _arrow(ax, (1.35, -0.12), (1.85, -0.12), col=C[1])
    ax.text(2.0, -0.17, "$v$", color=C[1], fontsize=9)
    _ef(ax, "force $F$", "velocity $v$")

    # 3. hydraulic line
    ax = axs[2]
    _panel(ax, "Hydraulic line")
    ax.add_patch(Circle((0, 0.5), 0.2, fc="white", ec=INK, lw=1.4))
    ax.text(0, 0.5, "$p_s$", ha="center", va="center", fontsize=9)
    top, bot = 0.62, 0.38
    ax.plot([0.2, 1.1], [top, top], color=INK, lw=1.4)
    ax.plot([0.2, 1.1], [bot, bot], color=INK, lw=1.4)
    ax.add_patch(Rectangle((0.2, bot), 0.9, top - bot, color=C[0], alpha=0.15, lw=0))
    ax.text(0.65, 0.75, r"long pipe:" + "\n" + r"inertance $\rho\ell/A$ ($L$)", **lab)
    # constriction
    ax.plot([1.1, 1.3, 1.5, 1.7], [top, 0.53, 0.53, top], color=INK, lw=1.4)
    ax.plot([1.1, 1.3, 1.5, 1.7], [bot, 0.47, 0.47, bot], color=INK, lw=1.4)
    ax.text(1.4, 0.3, "narrow section:\nresistance $R_{hyd}$", va="top", **lab)
    ax.plot([1.7, 2.05], [top, top], color=INK, lw=1.4)
    ax.plot([1.7, 2.05], [bot, bot], color=INK, lw=1.4)
    ax.add_patch(Rectangle((1.7, bot), 0.35, top - bot, color=C[0], alpha=0.15, lw=0))
    # accumulator: vessel with gas over liquid
    ax.add_patch(Rectangle((2.05, 0.15), 0.5, 1.0, fc="white", ec=INK, lw=1.4))
    ax.add_patch(Rectangle((2.05, 0.15), 0.5, 0.55, color=C[0], alpha=0.15, lw=0))
    ax.plot([2.05, 2.55], [0.7, 0.7], color=INK, lw=0.8, ls="--")
    ax.text(2.3, 0.93, "gas", ha="center", fontsize=8)
    ax.text(2.3, 1.22, "accumulator\n$C_{hyd}$", **lab)
    _arrow(ax, (0.35, 0.5), (0.8, 0.5), col=C[1])
    ax.text(0.9, 0.46, "$Q$", color=C[1], fontsize=9, va="center")
    _ef(ax, "pressure $p$", "volume flow $Q$")

    # 4. thermal RC
    ax = axs[3]
    _panel(ax, "Thermal RC (no $L$)")
    ax.add_patch(Circle((0, 0.5), 0.2, fc="white", ec=INK, lw=1.4))
    _arrow(ax, (0, 0.38), (0, 0.64), col=INK, lw=1.1)
    ax.plot([0, 0], [0.7, 1.2], color=INK, lw=1.4)
    ax.plot([0, 0], [0.3, -0.2], color=INK, lw=1.4)
    ax.text(-0.27, 0.5, r"$\dot Q_{in}$", ha="right", va="center", fontsize=9)
    ax.plot([0, 0.35], [1.2, 1.2], color=INK, lw=1.4)
    _zigzag(ax, (0.35, 1.2), (1.25, 1.2))
    ax.text(0.8, 1.38, r"$R_{th}$", **lab)
    ax.plot([1.25, 1.75, 1.75], [1.2, 1.2, 0.58], color=INK, lw=1.4)
    ax.plot(1.75, 1.2, "o", color=INK, ms=4)
    ax.text(1.75, 1.3, "$T$", ha="center", fontsize=9)
    ax.plot([1.57, 1.93], [0.58, 0.58], color=INK, lw=2)
    ax.plot([1.57, 1.93], [0.42, 0.42], color=INK, lw=2)
    ax.text(2.02, 0.5, r"$C_{th}$", fontsize=8.5, va="center")
    ax.plot([1.75, 1.75, 0], [0.42, -0.2, -0.2], color=INK, lw=1.4)
    ax.text(0.9, -0.12, r"ambient $T_\infty$", **lab)
    ax.text(2.3, 1.05, "no thermal\ninertance:\nfirst order,\nno ringing", fontsize=8, color=C[1],
            ha="left", va="top")
    _ef(ax, "temperature $T$", r"heat flow $\dot Q$")

    fig.subplots_adjust(wspace=0.05)
    save(fig, __file__, "rlc-template")


if __name__ == "__main__":
    second_order_poles()
    second_order_step()
    second_order_bode()
    rlc_template()
