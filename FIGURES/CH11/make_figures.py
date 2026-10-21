"""Figures for Chapter 11 (Bridge B.c: Maxwell's equations)."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax

c = 2.99792458e8


def plane_wave_snapshot():
    """§11.7.2 Polarization: snapshot of a linearly x-polarised plane wave,
    E = E0 cos(kz - wt) x_hat, B = (E0/c) cos(kz - wt) y_hat (in phase), k along z."""
    fig = plt.figure(figsize=(6.4, 3.6))
    ax = fig.add_subplot(projection="3d")
    z = np.linspace(0, 2, 400)                       # in wavelengths
    f = np.cos(2 * np.pi * z)
    ax.plot(z, f, 0 * z, color=C[0], lw=2, label=r"$\mathbf{E}\parallel\hat x$")
    ax.plot(z, 0 * z, f, color=C[1], lw=2, label=r"$\mathbf{B}\parallel\hat y$  ($|B|=|E|/c$)")
    for zi in np.linspace(0, 2, 33):
        fi = np.cos(2 * np.pi * zi)
        ax.plot([zi, zi], [0, fi], [0, 0], color=C[0], lw=0.7, alpha=0.6)
        ax.plot([zi, zi], [0, 0], [0, fi], color=C[1], lw=0.7, alpha=0.6)
    ax.plot([0, 2.2], [0, 0], [0, 0], color=INK, lw=1)
    ax.quiver(2.0, 0, 0, 0.3, 0, 0, color=INK, arrow_length_ratio=0.35, lw=1.5)
    ax.text(2.25, 0, 0.15, r"$\mathbf{k}\parallel\hat z$", fontsize=10)
    ax.text(0, 1.25, 0, r"$x$", color=C[0]); ax.text(0, 0, 1.3, r"$y$", color=C[1])
    for zi in (0, 1, 2):
        ax.plot([zi, zi], [0, 0], [-0.08, 0.08], color=INK, lw=1)
        ax.text(zi, 0, -0.3, rf"${zi}\lambda$" if zi else "0", ha="center", fontsize=9)
    ax.set_xlim(0, 2.5); ax.set_ylim(-1.2, 1.2); ax.set_zlim(-1.2, 1.2)
    ax.view_init(elev=22, azim=-58)
    ax.set_box_aspect((2.4, 1, 1), zoom=1.15)
    ax.set_axis_off()
    ax.legend(loc="lower left", bbox_to_anchor=(0.0, 0.02))
    return fig


def lumping_criterion():
    """§11.12.1 Lumping criterion: L/lambda = L f / c versus f (10 Hz - 100 GHz)
    for L = 1 mm, 1 cm, 10 cm, 1 m; lumped circuit theory OK for L/lambda < 0.1.
    Text examples: 60 Hz (lambda = 5000 km), 1 GHz with L = 3 cm, 10 GHz with L = 1 cm."""
    f = np.logspace(1, 11, 300)
    fig, ax = fig_ax(h=3.8)
    ax.axhspan(1e-11, 0.1, color=C[2], alpha=0.10, lw=0)
    ax.axhline(0.1, color=C[2], lw=1.2)
    ax.text(15, 0.05, r"lumped OK: $L/\lambda < 0.1$", color=C[2], fontsize=9, va="top")
    ax.text(15, 0.2, "distributed (transmission-line / full-wave)", color=C[1], fontsize=9, va="bottom")
    for L, col, lab in [(1e-3, C[3], "1 mm"), (1e-2, C[0], "1 cm"), (0.1, C[4], "10 cm"), (1.0, INK, "1 m")]:
        ax.loglog(f, L * f / c, color=col, label=f"$L$ = {lab}")
    pts = [(60, 1.0, "60 Hz, 1 m\n$\\lambda$ = 5000 km", (14, 3e-5)),
           (1e9, 0.03, "1 GHz, 3 cm\n$L/\\lambda$ = 0.1", (1.5e8, 1e-6)),
           (1e10, 0.01, "10 GHz, 1 cm\n$L/\\lambda$ = 1/3", (3e7, 2.0))]
    for fp, L, txt, xyt in pts:
        y = L * fp / c
        ax.plot(fp, y, "o", color=C[1], ms=6, zorder=5)
        ax.annotate(txt, xy=(fp, y), xytext=xyt, fontsize=8, color=C[1],
                    arrowprops=dict(arrowstyle="->", color=C[1], lw=0.8))
    ax.set_xlim(10, 1e11)
    ax.set_ylim(1e-10, 1e3)
    ax.set_xlabel("frequency $f$ (Hz)")
    ax.set_ylabel(r"$L/\lambda = Lf/c$")
    ax.legend(loc="upper left", ncol=2)
    return fig


def main():
    save(plane_wave_snapshot(), __file__, "plane-wave-snapshot")
    save(lumping_criterion(), __file__, "lumping-criterion")


if __name__ == "__main__":
    main()
