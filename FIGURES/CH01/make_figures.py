"""Figures for Chapter 1 (The Action Principle)."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _style import plt, np, C, GREY, INK, SHADE, save, fig_ax
from scipy.integrate import solve_ivp, trapezoid
from scipy.special import ellipk


def action_variation():
    """§1.4.2 Hamilton's Principle: S[q] = int (q'^2/2 - q^2/2) dt, m = k = 1.

    Endpoints q(0) = 0, q(pi/2) = 1; classical path q_cl = sin t; varied
    paths q_cl + eps sin 2t (vanishing at both ends). S(eps) is computed
    numerically; analytically S = (3 pi / 8) eps^2, stationary at eps = 0.
    """
    t = np.linspace(0, np.pi / 2, 2001)

    def S(eps):
        q = np.sin(t) + eps * np.sin(2 * t)
        qd = np.cos(t) + 2 * eps * np.cos(2 * t)
        return trapezoid(0.5 * qd**2 - 0.5 * q**2, t)

    fig, (a1, a2) = fig_ax(ncols=2, h=3.6)
    cmap = plt.get_cmap("coolwarm")
    for eps in np.linspace(-0.3, 0.3, 7):
        if abs(eps) < 1e-12:
            continue
        a1.plot(t, np.sin(t) + eps * np.sin(2 * t), lw=1.0,
                color=cmap(0.5 + eps / 0.7))
    a1.plot(t, np.sin(t), color=INK, lw=2.4, label=r"classical $q=\sin t$")
    a1.plot([0, np.pi / 2], [0, 1], "o", color=INK)
    a1.set_xlabel("time $t$")
    a1.set_ylabel("$q(t)$")
    a1.set_xticks([0, np.pi / 4, np.pi / 2], ["0", r"$\pi/4$", r"$\pi/2$"])
    a1.set_title(r"Paths $q_{cl}+\epsilon\sin 2t$, $|\epsilon|\leq0.3$")
    a1.legend(loc="upper left")

    eps = np.linspace(-0.3, 0.3, 121)
    Svals = np.array([S(e) for e in eps])
    a2.plot(eps, Svals, color=C[0], label="numerical $S(\\epsilon)$")
    a2.plot(eps, 3 * np.pi / 8 * eps**2, "--", color=C[1], lw=1.2,
            label=r"$(3\pi/8)\,\epsilon^2$")
    a2.plot([0], [S(0.0)], "o", color=INK)
    a2.annotate(r"$dS/d\epsilon=0$ at $\epsilon=0$" "\n(classical path)",
                (0, 0), (0.0, 0.075), ha="center", fontsize=8.5,
                arrowprops=dict(arrowstyle="->", color=INK, lw=0.8))
    a2.set_xlabel(r"variation amplitude $\epsilon$")
    a2.set_ylabel(r"action $S$")
    a2.set_ylim(-0.01, 0.12)
    a2.set_title("Action is stationary on the true path")
    a2.legend(loc="upper right", fontsize=8.5)
    save(fig, __file__, "action-variation")


def pendulum_nonlinear():
    """§1.5.3 The Pendulum: theta'' + (g/l) sin theta = 0 vs small-angle.

    Released from rest at theta0 = 10, 90, 170 degrees; time in units of
    T0 = 2 pi sqrt(l/g). Right panel: exact period T/T0 = (2/pi) K(m),
    m = sin^2(theta0/2) (scipy ellipk uses the parameter m = k^2).
    """
    w0 = 2 * np.pi  # so that T0 = 1 in these units
    tt = np.linspace(0, 3, 1500)
    fig, (ax, ins) = plt.subplots(1, 2, figsize=(10.0, 3.8),
                                  gridspec_kw=dict(width_ratios=[2.4, 1]))
    for i, th0d in enumerate([10, 90, 170]):
        th0 = np.radians(th0d)
        sol = solve_ivp(lambda t, y: [y[1], -w0**2 * np.sin(y[0])], (0, 3),
                        [th0, 0.0], t_eval=tt, rtol=1e-10, atol=1e-12)
        ax.plot(tt, sol.y[0] / th0, color=C[i],
                label=rf"$\theta_0={th0d}^\circ$")
    ax.plot(tt, np.cos(w0 * tt), "--", color=GREY, lw=1.2,
            label=r"small-angle $\cos(2\pi t/T_0)$")
    ax.set_xlabel(r"$t/T_0$,   $T_0=2\pi\sqrt{\ell/g}$")
    ax.set_ylabel(r"$\theta(t)/\theta_0$")
    ax.set_xlim(0, 3)
    ax.set_ylim(-1.15, 1.6)
    ax.set_title("Nonlinear pendulum vs small-angle approximation")
    ax.legend(loc="upper left", ncol=4, fontsize=8.2)

    th = np.linspace(0, 179.5, 400)
    ins.plot(th, 2 / np.pi * ellipk(np.sin(np.radians(th) / 2) ** 2), color=INK,
             label=r"$(2/\pi)\,K(\sin^2\frac{\theta_0}{2})$")
    for i, th0d in enumerate([10, 90, 170]):
        r = 2 / np.pi * ellipk(np.sin(np.radians(th0d) / 2) ** 2)
        ins.plot([th0d], [r], "o", ms=5, color=C[i])
        ins.annotate(f"{r:.3f}", (th0d, r), (6, -12) if th0d < 150 else (-36, 0),
                     textcoords="offset points", fontsize=8, color=C[i])
    ins.set_xlim(0, 180)
    ins.set_ylim(0.9, 3.2)
    ins.set_xticks([0, 45, 90, 135, 180])
    ins.set_xlabel(r"amplitude $\theta_0$ (deg)")
    ins.set_ylabel(r"period $T/T_0$")
    ins.set_title("Exact period")
    ins.legend(loc="upper left", fontsize=8.5)
    save(fig, __file__, "pendulum-nonlinear")


if __name__ == "__main__":
    action_variation()
    pendulum_nonlinear()
