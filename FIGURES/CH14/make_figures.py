"""Figures for Chapter 14 — Transport Phenomena and Thermoelectrics."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax

from matplotlib.patches import Rectangle, FancyArrowPatch
from scipy.integrate import quad
from scipy.special import erfc


def bloch_gruneisen():
    """§14.1.1 Matthiessen's rule with the Bloch–Grüneisen phonon term.

    rho(T) = rho0 + 4A (T/T_D)^5 ∫_0^{T_D/T} x^5 / ((e^x-1)(1-e^-x)) dx,
    asymptotes A T/T_D (T >> T_D) and 497.6 A (T/T_D)^5 (T << T_D).
    """
    t = np.logspace(-2.3, 1, 300)  # T / T_D

    def J5(u):
        f = lambda x: x**5 / (np.expm1(x) * -np.expm1(-x)) if x > 0 else 0.0
        return quad(f, 0, u, limit=200)[0]

    rho_ph = np.array([4 * ti**5 * J5(1 / ti) for ti in t])  # in units of A
    low = 4 * 120 * 1.0369277551 * t**5  # 4 * 5! zeta(5) = 497.7
    fig, ax = fig_ax()
    ax.loglog(t, rho_ph, color=INK, lw=2.2, label=r"phonon only, $\rho_{ph}(T)$")
    td_cu = 343.0  # Debye temperature of Cu (K), for the RRR labels
    for rho0, col in zip([1e-3, 1e-2, 1e-1], C):
        r300 = rho0 + 4 * (300 / td_cu) ** 5 * J5(td_cu / 300)
        rrr = r300 / rho0
        ax.loglog(t, rho0 + rho_ph, color=col,
                  label=rf"$\rho_0={rho0:g}\,A$  (RRR $\approx$ {rrr:,.0f} if $T_D$=343 K)")
    ax.loglog(t, t, ls="--", color=GREY, lw=1.2)
    m = t < 0.25
    ax.loglog(t[m], low[m], ls=":", color=GREY, lw=1.5)
    ax.text(3.0, 0.9, r"$A\,T/T_D$", color=GREY, va="top")
    ax.text(0.03, 4e-6, r"$497.6\,A\,(T/T_D)^5$", color=GREY)
    ax.set_xlim(t[0], t[-1])
    ax.set_ylim(1e-7, 20)
    ax.set_xlabel(r"$T/T_D$")
    ax.set_ylabel(r"$\rho\,/\,A$")
    ax.set_title("Bloch–Grüneisen resistivity plus residual floor")
    ax.legend(loc="lower right", fontsize=8)
    save(fig, __file__, "bloch-gruneisen")


def thermoelectric_efficiency():
    """§14.4.1 TEG efficiency relative to Carnot.

    eta_max/eta_C = (sqrt(1+ZT) - 1) / (sqrt(1+ZT) + T_C/T_H), T_C/T_H = 300/600.
    """
    zt = np.linspace(0, 6, 400)
    fig, ax = fig_ax()
    for r, col, ls in [(0.5, C[0], "-"), (0.75, C[1], "--"), (0.25, C[2], "--")]:
        s = np.sqrt(1 + zt)
        lab = rf"$T_C/T_H={r}$" + (" (table)" if r == 0.5 else "")
        ax.plot(zt, (s - 1) / (s + r), color=col, ls=ls, lw=2.2 if r == 0.5 else 1.3, label=lab)
    pts = np.array([0.5, 1, 2, 5])
    vals = (np.sqrt(1 + pts) - 1) / (np.sqrt(1 + pts) + 0.5)
    ax.plot(pts, vals, "o", color=C[0], ms=5)
    for p, v in zip(pts, vals):
        ax.annotate(f"{v:.2f}", (p, v), xytext=(3, -16), textcoords="offset points",
                    color=C[0], fontsize=8.5)
    ax.axvspan(2, 3, color=SHADE, alpha=0.12)
    ax.text(2.05, 0.62, "best current\nmaterials", fontsize=8.5, color=INK)
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 0.7)
    ax.set_xlabel(r"figure of merit $ZT_M$")
    ax.set_ylabel(r"$\eta_{max}/\eta_{Carnot}$")
    ax.set_title("Thermoelectric generator efficiency vs. ZT")
    ax.legend(loc="upper left")
    save(fig, __file__, "thermoelectric-efficiency")


def solar_cell_iv():
    """§14.5.5 Solar-cell I–V: I = I0 (e^{V/V_T} - 1) - I_SC, P = -IV.

    I0 = 1e-12 A, I_SC = 30 mA, V_T = k_B T/e at 300 K.
    """
    I0, Isc, VT = 1e-12, 30e-3, 0.025852
    voc = VT * np.log(Isc / I0 + 1)
    v = np.linspace(-0.1, 0.72, 800)
    dark = I0 * np.expm1(v / VT)
    light = dark - Isc
    p = -v * light
    vv = np.linspace(0, voc, 20000)
    pp = -vv * (I0 * np.expm1(vv / VT) - Isc)
    k = np.argmax(pp)
    vm, pm = vv[k], pp[k]
    im = pm / vm
    fig, ax = fig_ax(h=3.9)
    ax.axhline(0, color=INK, lw=0.8)
    ax.axvline(0, color=INK, lw=0.8)
    ax.plot(v, dark * 1e3, color=GREY, ls="--", label="dark")
    ax.plot(v, light * 1e3, color=C[0], label="illuminated")
    ax.add_patch(Rectangle((0, -im * 1e3), vm, im * 1e3, color=SHADE, alpha=0.12))
    ax.plot([voc], [0], "o", color=C[0])
    ax.plot([0], [-Isc * 1e3], "o", color=C[0])
    ax.plot([vm], [-im * 1e3], "s", color=C[1])
    ax.annotate(rf"$V_{{OC}}={voc:.2f}$ V", (voc, 0), xytext=(-62, 14), textcoords="offset points")
    ax.annotate(rf"$-I_{{SC}}=-{Isc*1e3:.0f}$ mA", (0, -Isc * 1e3), xytext=(6, -14),
                textcoords="offset points")
    ax.annotate(f"MPP: {vm:.2f} V, {im*1e3:.1f} mA", (vm, -im * 1e3), xytext=(-150, 18),
                textcoords="offset points", color=C[1],
                arrowprops=dict(arrowstyle="-", color=C[1], lw=0.8))
    ax.set_xlim(-0.1, 0.72)
    ax.set_ylim(-40, 20)
    ax.set_xlabel("voltage $V$ (V)")
    ax.set_ylabel("current $I$ (mA)")
    ax2 = ax.twinx()
    ax2.plot(v[v >= 0], p[v >= 0] * 1e3, color=C[1], lw=1.4)
    ax2.plot([vm], [pm * 1e3], "s", color=C[1])
    ax2.set_ylim(-20, 40)
    ax2.set_ylabel(r"delivered power $-IV$ (mW)", color=C[1])
    ax2.tick_params(axis="y", colors=C[1])
    ax2.spines["right"].set_visible(True)
    ax2.spines["right"].set_color(C[1])
    ax2.grid(False)
    ax2.text(0.06, pm * 1e3 * 0.62, rf"$P_{{max}}={pm*1e3:.1f}$ mW", color=C[1])
    ff = pm / (voc * Isc)
    ax.set_title(rf"Solar cell, $I_0=10^{{-12}}$ A, $I_{{SC}}=30$ mA, 300 K (fill factor {ff:.2f})")
    ax.legend(loc="upper left")
    save(fig, __file__, "solar-cell-iv")


def erfc_diffusion():
    """§14.8.1 Constant-source diffusion: (c-c0)/(cs-c0) = erfc(x / 2 sqrt(Dt)).

    Phosphorus in Si at 1000 °C, D = 2.5e-14 cm^2/s, t = 0.25, 1, 4 h.
    """
    D = 2.5e-14 * 1e14  # nm^2/s  (1 cm^2 = 1e14 nm^2)
    x = np.linspace(0, 600, 600)
    fig, ax = fig_ax()
    for th, col in zip([0.25, 1, 4], C):
        L = np.sqrt(D * th * 3600)
        ax.plot(x, erfc(x / (2 * L)), color=col, label=rf"$t={th:g}$ h, $\sqrt{{Dt}}={L:.0f}$ nm")
        ax.plot([L], [erfc(0.5)], "o", color=col, ms=5)
        ax.plot([2 * L], [erfc(1.0)], "s", color=col, ms=4.5, mfc="white")
    ax.axhline(erfc(0.5), color=GREY, lw=0.8, ls=":")
    ax.axhline(erfc(1.0), color=GREY, lw=0.8, ls=":")
    ax.text(590, erfc(0.5) + 0.015, r"$x=\sqrt{Dt}$: erfc(1/2)=0.48", ha="right", color=GREY, fontsize=8.5)
    ax.text(590, erfc(1.0) + 0.015, r"$x=2\sqrt{Dt}$: erfc(1)=0.16", ha="right", color=GREY, fontsize=8.5)
    ax.set_xlim(0, 600)
    ax.set_ylim(0, 1.02)
    ax.set_xlabel("depth $x$ (nm)")
    ax.set_ylabel(r"$(c-c_0)/(c_s-c_0)$")
    ax.set_title(r"P in Si at 1000 °C, $D=2.5\times10^{-14}$ cm$^2$/s")
    ax.legend(loc="upper right", bbox_to_anchor=(1, 0.93))
    save(fig, __file__, "erfc-diffusion")


def thermoelectric_module():
    """§14.4.1 Schematic of a TE module: P/N legs electrically in series,
    thermally in parallel, between a hot (T_H) and cold (T_C) plate (generator mode)."""
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    ax.set_axis_off()
    ax.set_aspect("equal")
    W, H, gap = 0.8, 1.6, 0.5
    xs = [0.6 + i * (W + gap) for i in range(4)]
    kinds = ["P", "N", "P", "N"]
    yb, yt = 0.0, H
    # ceramic plates
    ax.add_patch(Rectangle((0.2, yt + 0.18), 5.6, 0.35, color=C[1], alpha=0.25, lw=0))
    ax.add_patch(Rectangle((0.2, yb - 0.53), 5.6, 0.35, color=C[0], alpha=0.25, lw=0))
    ax.text(3.0, yt + 0.355, r"hot side $T_H$ (heat in, $\dot Q_H$)", ha="center", va="center")
    ax.text(3.0, yb - 0.355, r"cold side $T_C$ (heat out, $\dot Q_C$)", ha="center", va="center")
    for x, k in zip(xs, kinds):
        col = C[3] if k == "P" else C[2]
        ax.add_patch(Rectangle((x, yb), W, H, fc=col, alpha=0.35, ec=INK, lw=1))
        ax.text(x + W / 2, H / 2, k, ha="center", va="center", fontsize=14, weight="bold")
        # current direction: down P legs, up N legs (generator mode)
        y0, y1 = (H * 0.8, H * 0.2) if k == "P" else (H * 0.2, H * 0.8)
        ax.add_patch(FancyArrowPatch((x + W * 0.82, y0), (x + W * 0.82, y1),
                                     arrowstyle="-|>", mutation_scale=10, color=INK, lw=1))
    strap = dict(color="#b87333", lw=0)
    # top straps join N(i)–P(i+1); bottom straps join P(i)–N(i)
    for i in (0, 2):
        ax.add_patch(Rectangle((xs[i], yb - 0.18), xs[i + 1] + W - xs[i], 0.18, **strap))
    ax.add_patch(Rectangle((xs[1], yt), xs[2] + W - xs[1], 0.18, **strap))
    ax.add_patch(Rectangle((xs[0], yt), W, 0.18, **strap))
    ax.add_patch(Rectangle((xs[3], yt), W, 0.18, **strap))
    # leads to load
    ax.plot([0.0, xs[0]], [yt + 0.09, yt + 0.09], color=INK, lw=1.2)
    ax.plot([xs[3] + W, 6.0], [yt + 0.09, yt + 0.09], color=INK, lw=1.2)
    ax.plot([0.0, 0.0, 6.0, 6.0], [yt + 0.09, -1.0, -1.0, yt + 0.09], color=INK, lw=1.2)
    ax.add_patch(Rectangle((2.6, -1.12), 0.8, 0.24, fc="white", ec=INK, lw=1.2))
    ax.text(3.0, -1.35, r"load $R_L$", ha="center", va="top")
    ax.text(-0.08, yt + 0.1, "−", ha="right", va="center", fontsize=12)
    ax.text(6.08, yt + 0.1, "+", ha="left", va="center", fontsize=12)
    ax.text(6.35, H / 2, "copper\nstraps", color="#b87333", fontsize=8.5, va="center")
    ax.set_xlim(-0.4, 7.2)
    ax.set_ylim(-1.6, yt + 0.6)
    ax.set_title("Thermoelectric module: electrically in series, thermally in parallel", fontsize=10)
    save(fig, __file__, "thermoelectric-module")


if __name__ == "__main__":
    bloch_gruneisen()
    thermoelectric_efficiency()
    solar_cell_iv()
    erfc_diffusion()
    thermoelectric_module()
