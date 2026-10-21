"""Figures for Chapter 16 — Wave and Diffusion Equations."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax


def dispersion_relations():
    """§16.4.2 Dispersion relations in normalised units (k0, w0 = v k0):
    nondispersive w = vk; Klein-Gordon / waveguide w = sqrt(v^2 k^2 + w_c^2) with w_c = w0;
    deep water w = sqrt(g k); flexural w = kappa k^2; diffusion w = -i D k^2."""
    k = np.linspace(0, 2.2, 400)
    fig, (a1, a2) = fig_ax(ncols=2, h=3.8, gridspec_kw=dict(width_ratios=[1.6, 1]))
    a1.plot(k, k, color=INK, label=r"non-dispersive $\omega=vk$")
    a1.plot(k, np.sqrt(k**2 + 1), color=C[0], label=r"Klein–Gordon / waveguide $\sqrt{v^2k^2+\omega_c^2}$")
    a1.plot(k, np.sqrt(k), color=C[2], label=r"deep water $\sqrt{gk}$")
    a1.plot(k, k**2, color=C[1], label=r"flexural $\kappa k^2$")
    # v_p (chord) and v_g (tangent) on the Klein-Gordon branch at k = 1
    k1 = 1.0
    w1 = np.sqrt(k1**2 + 1)
    a1.plot([0, k1 * 2.0], [0, w1 * 2.0], color=C[0], ls=":", lw=1.1)
    vg = k1 / w1
    kt = np.array([0.2, 2.1])
    a1.plot(kt, w1 + vg * (kt - k1), color=C[0], ls="--", lw=1.1)
    a1.plot([k1], [w1], "o", color=C[0], zorder=4)
    a1.text(0.08, 1.78, r"dotted chord: $v_p=\omega/k=\sqrt{2}\,v$", color=C[0], fontsize=8.5)
    a1.text(0.08, 1.58, r"dashed tangent: $v_g=d\omega/dk=v/\sqrt{2}$", color=C[0], fontsize=8.5)
    a1.text(1.3, 0.62, r"water: $v_g=v_p/2$" + "\n" + r"flexural: $v_g=2v_p$" + "\n"
            + r"Klein–Gordon: $v_pv_g=v^2$", fontsize=8.5, color=GREY, va="top")
    a1.axhline(1, color=GREY, lw=0.7, ls="-.")
    a1.text(2.18, 0.96, r"cutoff $\omega_c$", ha="right", va="top", fontsize=8, color=GREY)
    a1.set_xlim(0, 2.2)
    a1.set_ylim(0, 3.0)
    a1.set_xlabel(r"wavenumber $k/k_0$")
    a1.set_ylabel(r"$\mathrm{Re}\,\omega/\omega_0$")
    a1.set_title("Propagating branches")
    a1.legend(loc="upper left", fontsize=8)

    a2.plot(k, -k**2, color=C[3])
    a2.text(1.3, -1.25, r"diffusion $\omega=-iDk^2$", color=C[3], fontsize=9)
    a2.axhline(0, color=INK, lw=0.8)
    a2.text(0.1, -3.6, r"$\mathrm{Re}\,\omega=0$: no propagation" + "\n"
            + r"mode decays as $e^{-Dk^2t}$;" + "\n" + "short wavelengths die first",
            fontsize=8.5, color=GREY)
    a2.set_xlim(0, 2.2)
    a2.set_ylim(-5, 0.3)
    a2.set_xlabel(r"wavenumber $k/k_0$")
    a2.set_ylabel(r"$\mathrm{Im}\,\omega/\omega_0$")
    a2.set_title("Diffusive branch")
    save(fig, __file__, "dispersion-relations")


def greens_functions():
    """§16.6.2 Green's functions. Left: 1D diffusion G = exp(-x^2/4Dt)/sqrt(4 pi D t), D = 1.
    Right: 3D wave G = delta(t - r/v) / (4 pi v r), v = 1 — an infinitely thin shell at r = vt
    whose strength falls as 1/r."""
    ts = [0.1, 0.5, 1, 2]
    x = np.linspace(-6, 6, 1200)
    fig, (a1, a2) = fig_ax(ncols=2, h=3.6)
    for t, col in zip(ts, C):
        a1.plot(x, np.exp(-x**2 / (4 * t)) / np.sqrt(4 * np.pi * t), color=col, label=f"$t={t:g}$")
    a1.set_xlim(-6, 6)
    a1.set_ylim(0, 1.0)
    a1.set_xlabel(r"$x-x'$  (units with $D=1$)")
    a1.set_ylabel(r"$G_{diff}^{1D}$")
    a1.set_title("Diffusion: spreading Gaussian, width $\\sqrt{2Dt}$")
    a1.text(-5.7, 0.62, "nonzero at every $x$\nfor any $t>0$", fontsize=8.5, color=GREY)
    a1.legend(loc="upper right")

    for t, col in zip(ts, C):
        r = t  # v = 1
        h = 1 / (4 * np.pi * r)
        a2.annotate("", (r, h), (r, 0), arrowprops=dict(arrowstyle="-|>", color=col, lw=2,
                                                        mutation_scale=12))
        a2.text(r + 0.04, h + 0.05, f"$t={t:g}$", color=col, ha="left", va="bottom", fontsize=9)
    rr = np.linspace(0.08, 2.4, 200)
    a2.plot(rr, 1 / (4 * np.pi * rr), color=GREY, ls="--", lw=1, label=r"shell strength $1/4\pi vr$")
    a2.axvspan(2.0, 2.5, color=SHADE, alpha=0.12)
    a2.text(2.25, 0.55, "$r>vt$ at\n$t=2$: not yet\nreached, $G=0$", ha="center", fontsize=8.5)
    a2.set_xlim(0, 2.5)
    a2.set_ylim(0, 1.0)
    a2.set_xlabel(r"$r=|\mathbf{r}-\mathbf{r}'|$  (units with $v=1$)")
    a2.set_ylabel(r"weight of $\delta(t-r/v)$ shell")
    a2.set_title("Wave (3D): thin shell at $r=vt$")
    a2.legend(loc="upper right")
    save(fig, __file__, "greens-functions")


def _telegraph(beta, v, x, phi0, t_out, dt):
    """Leapfrog FD for phi_tt + beta phi_t = v^2 phi_xx, phi_t(0) = 0, phi = 0 at the ends."""
    dx = x[1] - x[0]
    r2 = (v * dt / dx) ** 2
    a, b = 1 + beta * dt / 2, 1 - beta * dt / 2
    lap = lambda p: np.concatenate(([0], p[2:] - 2 * p[1:-1] + p[:-2], [0]))
    prev = phi0.copy()
    cur = phi0 + 0.5 * r2 * lap(phi0) / a  # first step with phi_t = 0 (damping term drops out)
    t, out = dt, {0.0: phi0.copy()}
    for target in sorted(t_out):
        while t < target - 1e-12:
            nxt = (2 * cur - b * prev + r2 * lap(cur)) / a
            prev, cur, t = cur, nxt, t + dt
        out[target] = cur.copy()
    return out


def telegraph_pulse():
    """§16.3.2 Lossy transmission line V_tt + beta V_t = v^2 V_zz (omega_c = 0) for a Gaussian
    initial pulse of width 0.5, v = 1. Wave regime beta = 0.1; overdamped beta = 10, which should
    follow diffusion with D = v^2/beta = 0.1."""
    z = np.linspace(-25, 25, 2001)
    s0 = 0.5
    phi0 = np.exp(-z**2 / (2 * s0**2))
    fig, (a1, a2) = fig_ax(ncols=2, h=3.6)
    tw = [4, 8, 16]
    ow = _telegraph(0.1, 1.0, z, phi0, tw, 0.01)
    a1.plot(z, phi0, color=INK, label="$t=0$")
    for t, col in zip(tw, C):
        a1.plot(z, ow[t], color=col, label=f"$t={t}$")
        a1.plot(z, 0.5 * np.exp(-0.05 * t) * (np.exp(-(z - t)**2 / (2 * s0**2)) +
                                                np.exp(-(z + t)**2 / (2 * s0**2))),
                color=GREY, ls=":", lw=1)
    a1.set_xlim(-20, 20)
    a1.set_ylim(-0.05, 1.05)
    a1.set_xlabel(r"position $z$  (units with $v=1$)")
    a1.set_ylabel(r"$V(z,t)/V_0$")
    a1.set_title(r"Wave regime, $\beta=0.1$: two pulses at $\pm vt$")
    a1.text(-19, 0.75, r"dotted: $\frac{1}{2} e^{-\beta t/2}$ ×" + "\n" + "translated pulses", fontsize=8.5,
            color=GREY)
    a1.legend(loc="upper right", fontsize=8)

    beta = 10.0
    D = 1.0 / beta
    td = [10, 40, 160]
    od = _telegraph(beta, 1.0, z, phi0, td, 0.01)
    a2.plot(z, phi0, color=INK, label="$t=0$")
    for t, col in zip(td, C):
        a2.plot(z, od[t], color=col, label=f"$t={t}$")
        s2 = s0**2 + 2 * D * t
        a2.plot(z, s0 / np.sqrt(s2) * np.exp(-z**2 / (2 * s2)), color=GREY, ls=":", lw=1.2)
    a2.set_xlim(-20, 20)
    a2.set_ylim(-0.05, 1.05)
    a2.set_xlabel(r"position $z$  (units with $v=1$)")
    a2.set_title(r"Overdamped, $\beta=10$: diffusive spreading")
    a2.text(-19, 0.75, r"dotted: diffusion with" + "\n" + r"$D=v^2/\beta=0.1$", fontsize=8.5, color=GREY)
    a2.legend(loc="upper right", fontsize=8)
    save(fig, __file__, "telegraph-pulse")


if __name__ == "__main__":
    dispersion_relations()
    greens_functions()
    telegraph_pulse()
