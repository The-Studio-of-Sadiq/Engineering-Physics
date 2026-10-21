"""Figures for Chapter 12 (electromagnetic waves, optics and photonics)."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax

from scipy.special import j1

c = 2.99792458e8


def _fresnel(n1, n2, th):
    """Power reflectances R_s, R_p (complex cos(theta_t) handles TIR)."""
    ci = np.cos(th)
    st = n1 / n2 * np.sin(th)
    ct = np.sqrt((1 - st**2).astype(complex))
    rs = (n1 * ci - n2 * ct) / (n1 * ci + n2 * ct)
    rp = (n2 * ci - n1 * ct) / (n2 * ci + n1 * ct)
    return np.abs(rs)**2, np.abs(rp)**2


def fresnel_reflectance():
    """§12.3.4 Brewster's angle: R_s = |r_s|^2, R_p = |r_p|^2 vs incidence angle,
    air -> glass (n = 1.5, theta_B = 56.3 deg) and glass -> air
    (internal theta_B = 33.7 deg, theta_c = 41.8 deg, TIR beyond)."""
    th = np.radians(np.linspace(0, 89.99, 2000))
    fig, (a1, a2) = fig_ax(ncols=2, h=3.4, sharey=True)
    for ax, n1, n2, title in [(a1, 1.0, 1.5, "air → glass ($n_1=1,\\ n_2=1.5$)"),
                              (a2, 1.5, 1.0, "glass → air ($n_1=1.5,\\ n_2=1$)")]:
        Rs, Rp = _fresnel(n1, n2, th)
        d = np.degrees(th)
        ax.plot(d, Rs, color=C[0], label="$R_s$ (TE)")
        ax.plot(d, Rp, color=C[1], label="$R_p$ (TM)")
        thB = np.degrees(np.arctan(n2 / n1))
        ax.axvline(thB, color=C[1], ls="--", lw=1)
        ax.text(thB - 1.5, 0.55, rf"$\theta_B={thB:.1f}°$", rotation=90, ha="right", color=C[1], fontsize=8)
        if n1 > n2:
            thc = np.degrees(np.arcsin(n2 / n1))
            ax.axvspan(thc, 90, color=GREY, alpha=0.15, lw=0)
            ax.axvline(thc, color=INK, ls=":", lw=1)
            ax.text(thc + 1.5, 0.55, rf"$\theta_c={thc:.1f}°$", rotation=90, color=INK, fontsize=8)
            ax.text(66, 0.88, "total internal\nreflection", ha="center", fontsize=8, color=INK)
        ax.text(2, 0.09, f"normal: R = {((n1 - n2) / (n1 + n2))**2:.3f}", fontsize=8, color=GREY)
        ax.set_title(title)
        ax.set_xlim(0, 90)
        ax.set_xticks(range(0, 91, 15))
        ax.set_xlabel(r"incidence angle $\theta_i$ (°)")
    a1.set_ylim(0, 1.03)
    a1.set_ylabel("reflectance")
    a1.legend(loc="upper left")
    return fig


def fabry_perot():
    """§12.5.4 Fabry-Perot: Airy transmission T = 1/(1 + F sin^2(delta/2)),
    F = 4R/(1-R)^2, for R = 0.5, 0.9, 0.99. FSR is delta = 2 pi; for R = 0.99
    the FWHM is 2(1-R)/sqrt(R) rad and finesse pi sqrt(R)/(1-R) = 313."""
    dl = np.linspace(-0.25, 1.25, 30001)          # delta / 2 pi
    fig, ax = fig_ax(h=3.6)
    for R, col in [(0.5, C[2]), (0.9, C[0]), (0.99, C[1])]:
        F = 4 * R / (1 - R)**2
        ax.plot(dl, 1 / (1 + F * np.sin(np.pi * dl)**2), color=col, lw=1.6,
                label=rf"$R={R}$  ($\mathcal{{F}}={np.pi * np.sqrt(R) / (1 - R):.0f}$)")
    ax.annotate("", xy=(1, 1.07), xytext=(0, 1.07),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1))
    ax.text(0.5, 1.09, r"FSR $= c/2nd$  ($\Delta\delta = 2\pi$)", ha="center", va="bottom", fontsize=9)
    ax.set_xlim(-0.25, 1.25)
    ax.set_ylim(0, 1.2)
    ax.set_xlabel(r"round-trip phase $\delta/2\pi$")
    ax.set_ylabel(r"$I_T/I_0$")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=3)

    R = 0.99
    F = 4 * R / (1 - R)**2
    fw = 2 * (1 - R) / np.sqrt(R) / (2 * np.pi)   # FWHM in units of FSR
    ins = ax.inset_axes([0.34, 0.33, 0.27, 0.42])
    x = np.linspace(1 - 0.012, 1 + 0.012, 2001)
    ins.plot(x - 1, 1 / (1 + F * np.sin(np.pi * x)**2), color=C[1])
    ins.annotate("", xy=(fw / 2, 0.5), xytext=(-fw / 2, 0.5),
                 arrowprops=dict(arrowstyle="<->", color=INK, lw=0.8))
    ins.text(0, 0.56, f"FWHM\n= FSR/{1 / fw:.0f}", ha="center", fontsize=7)
    ins.set_xticks([-0.01, 0, 0.01])
    ins.set_xticklabels(["−0.01", "0", "0.01"])
    ins.tick_params(labelsize=7)
    ins.set_yticks([0, 0.5, 1])
    ins.set_title(r"$R=0.99$, zoom", fontsize=8)
    return fig


def fraunhofer_diffraction():
    """§12.6.2 Fraunhofer diffraction: single slit I = sinc^2(a sin(theta)/lambda);
    double slit with d = 4a, I = sinc^2 * cos^2(pi d sin(theta)/lambda) (every 4th
    order missing); circular aperture [2 J1(x)/x]^2, x = pi D sin(theta)/lambda,
    first zero at D sin(theta)/lambda = 1.22."""
    u = np.linspace(-3, 3, 6001)
    fig, (a1, a2) = fig_ax(ncols=2, h=3.3)
    single = np.sinc(u)**2
    a1.plot(u, single * np.cos(4 * np.pi * u)**2, color=C[0], lw=1.1, label="double slit, $d=4a$")
    a1.plot(u, single, color=INK, lw=1.8, label="single slit (envelope)")
    for z in (-1, 1):
        a1.plot(z, 0, "v", color=C[1], ms=6)
    a1.text(1.05, 0.05, "first zero\n$a\\sin\\theta=\\lambda$\n(4th order missing)", fontsize=8, color=C[1])
    a1.set_xlabel(r"$a\sin\theta/\lambda$")
    a1.set_ylabel(r"$I/I_0$")
    a1.set_xlim(-3, 3); a1.set_ylim(0, 1.15)
    a1.legend(loc="upper left", fontsize=8)

    v = np.linspace(1e-6, 3, 3000)
    x = np.pi * v
    airy = (2 * j1(x) / x)**2
    a2.plot(v, airy, color=C[2], lw=1.8, label=r"circular, $[2J_1(x)/x]^2$")
    a2.plot(v, np.sinc(v)**2, color=INK, ls="--", lw=1.2, label="slit, sinc$^2$")
    a2.axvline(1.2197, color=C[2], ls=":", lw=1)
    a2.text(1.26, 0.7, "first zero\n$D\\sin\\theta=1.22\\lambda$", fontsize=8, color=C[2])
    a2.set_xlabel(r"$D\sin\theta/\lambda$  (or $a\sin\theta/\lambda$)")
    a2.set_xlim(0, 3); a2.set_ylim(0, 1.15)
    a2.legend(loc="upper right", fontsize=8)
    ins = a2.inset_axes([0.5, 0.2, 0.46, 0.3])
    ins.semilogy(v, airy, color=C[2], lw=1)
    ins.semilogy(v, np.sinc(v)**2, color=INK, ls="--", lw=0.8)
    ins.set_ylim(1e-4, 1.2); ins.set_xlim(0, 3)
    ins.tick_params(labelsize=6)
    ins.set_title("log scale", fontsize=7)
    return fig


def waveguide_dispersion():
    """§12.7.1 Rectangular waveguide WR-90 (a = 22.86 mm, b = 10.16 mm):
    f = (c/2 pi) sqrt(beta^2 + (m pi/a)^2 + (n pi/b)^2) for TE10, TE20, TE01,
    light line f = c beta / 2 pi; inset v_g/c = sqrt(1 - (f_c/f)^2) for TE10."""
    a, b = 22.86e-3, 10.16e-3
    beta = np.linspace(0, 600, 600)
    fig, ax = fig_ax(h=3.8)
    ax.plot(beta, c * beta / (2 * np.pi) / 1e9, color=GREY, ls="--", lw=1.2, label="light line $f=c\\beta/2\\pi$")
    modes = [(1, 0, C[0]), (2, 0, C[1]), (0, 1, C[2])]
    for m, n, col in modes:
        kc = np.hypot(m * np.pi / a, n * np.pi / b)
        fc = c * kc / (2 * np.pi) / 1e9
        ax.plot(beta, c * np.hypot(beta, kc) / (2 * np.pi) / 1e9, color=col,
                label=rf"TE$_{{{m}{n}}}$, $f_c$ = {fc:.2f} GHz")
        ax.axhline(fc, color=col, lw=0.6, ls=":")
    f10, f20 = c / (2 * a) / 1e9, c / a / 1e9
    ax.axhspan(f10, f20, color=SHADE, alpha=0.08, lw=0)
    ax.text(8, (f10 + f20) / 2 + 0.2, "single-mode band\n(TE$_{10}$ only)", fontsize=8, color=SHADE)
    ax.set_xlim(0, 600); ax.set_ylim(0, 25)
    ax.set_xlabel(r"propagation constant $\beta$ (rad/m)")
    ax.set_ylabel("frequency $f$ (GHz)")
    ax.legend(loc="upper left", fontsize=8)

    ins = ax.inset_axes([0.64, 0.09, 0.33, 0.28])
    f = np.linspace(f10, 25, 400)
    ins.plot(f, np.sqrt(np.clip(1 - (f10 / f)**2, 0, None)), color=C[0])
    ins.set_xlim(5, 25); ins.set_ylim(0, 1)
    ins.set_xlabel("$f$ (GHz)", fontsize=7, labelpad=1)
    ins.set_ylabel("$v_g/c$", fontsize=7, labelpad=1)
    ins.tick_params(labelsize=7)
    ins.set_title("TE$_{10}$ group velocity", fontsize=7)
    return fig


def main():
    save(fresnel_reflectance(), __file__, "fresnel-reflectance")
    save(fabry_perot(), __file__, "fabry-perot")
    save(fraunhofer_diffraction(), __file__, "fraunhofer-diffraction")
    save(waveguide_dispersion(), __file__, "waveguide-dispersion")


if __name__ == "__main__":
    main()
