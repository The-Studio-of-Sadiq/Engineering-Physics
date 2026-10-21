# Appendix F — Linear Systems and Feedback: Laplace, Transfer Functions, Stability Proofs

This appendix proves the results of linear systems and classical control that the chapters state and use: the Laplace-transform properties (with the conditions of the final value theorem, which are routinely dropped), the state-space formula for the transfer function, the second-order step response and its metrics, the Bode asymptotes, the argument principle and the Nyquist criterion $Z = N + P$, the Routh–Hurwitz criterion with a worked example, the root-locus construction rules, steady-state error and system type, the Bode sensitivity integral, and the DC-motor transfer function. The chapters that rely on it are [Ch. 17](../CHAPTERS/CHAPTER%2017.md) (§17.6, §17.7), [Ch. 18](../CHAPTERS/CHAPTER%2018.md) (§18.6.3), and [Ch. 21](../CHAPTERS/CHAPTER%2021.md) (§21.2–§21.8), together with [Example 06](../EXAMPLES/06%20Motor-to-Control-System.md).

**Scope.** Everything here concerns **linear time-invariant (LTI), causal, finite-dimensional** systems, whose transfer functions are rational functions of $s$. The reduction of a physical plant to such a model is a separate step — lumping (Bridge C, Ch. 17 §17.1; Appendix E) followed by linearisation about an operating point (Ch. 21 §21.0.3) — and both are approximations with named regimes. The mathematics below is exact *for the model*; nothing in it repairs a model that has left its regime. Where a statement extends beyond rational functions (time delays, distributed plants) this is said explicitly. Ch. 21 §21.0.2 lists the system classes for which an ordinary transfer function does not exist.

**Notation.** It follows Ch. 21: plant $P(s)$, controller $C(s)$, loop transfer function $L(s) = C(s)P(s)$, sensitivity $S = 1/(1+L)$, complementary sensitivity $T = L/(1+L)$, state-space matrices $\mathbf{A},\mathbf{B},\mathbf{C},D$. The imaginary unit is $j$. Natural frequency and damping ratio are written $\omega_0$, $\zeta$ as in Ch. 17 §17.7 (Ch. 21 writes $\omega_n$; they are the same quantity). For the DC motor the notation of Example 06 is used ($K_b$, $B$); Ch. 21 §21.8.1 writes $K_e$, $b$ for the same constants.

---

## F.1 — The Laplace Transform: Properties Needed for Control

### F.1.1 — Definition and convergence

For $f:[0,\infty)\to\mathbb{C}$ piecewise continuous and of **exponential order** — $|f(t)|\leq Me^{\alpha t}$ for some $M$, $\alpha$ — the unilateral transform

$$F(s) = \mathcal{L}\{f\}(s) = \int_{0^-}^{\infty}f(t)\,e^{-st}\,dt$$

converges absolutely for $\mathrm{Re}\,s > \alpha$ and is analytic there. The lower limit $0^-$ lets impulses at $t = 0$ be included and makes initial conditions enter as $f(0^-)$, the state *before* any input is applied. Ch. 18 §18.6.3 introduces the bilateral transform; for causal signals the two coincide.

### F.1.2 — Derivative and integral

**Derivative.** If $f$ and $f'$ are of exponential order, integration by parts gives, for $\mathrm{Re}\,s > \alpha$,

$$\mathcal{L}\{f'\} = \Big[f(t)e^{-st}\Big]_{0^-}^{\infty} + s\int_{0^-}^\infty f\,e^{-st}\,dt = sF(s) - f(0^-)$$

since $f(t)e^{-st}\to0$ as $t\to\infty$. Iterating, $\mathcal{L}\{f''\} = s^2F(s) - sf(0^-) - f'(0^-)$.

**Integral.** With $g(t) = \int_{0^-}^tf\,d\tau$, $g' = f$ and $g(0^-) = 0$, so $G(s) = F(s)/s$.

**Delay.** For $T\geq0$, $\mathcal{L}\{f(t-T)u(t-T)\} = e^{-sT}F(s)$ — not a rational function, which is why a pure delay sits outside the rational-function machinery of this appendix (Ch. 21 §21.0.2).

### F.1.3 — Convolution

**Theorem.** If $f$, $g$ are causal and of exponential order, then $\mathcal{L}\{f*g\} = F(s)\,G(s)$ with $(f*g)(t) = \int_0^tf(\tau)\,g(t-\tau)\,d\tau$.

*Proof.* For $\mathrm{Re}\,s$ large enough the double integral converges absolutely, so Fubini's theorem permits exchanging the order:

$$\int_0^\infty e^{-st}\int_0^tf(\tau)g(t-\tau)\,d\tau\,dt = \int_0^\infty f(\tau)e^{-s\tau}\int_\tau^\infty g(t-\tau)e^{-s(t-\tau)}\,dt\,d\tau = F(s)\,G(s)\qquad\square$$

This is why an LTI system is characterised by one function: if $y = g*u$ with $g$ the impulse response, then $Y = G\,U$. The ratio $G = Y/U$ is the transfer function, and it exists precisely because the system is linear (superposition) and time-invariant (a shifted input gives a shifted output, so the response is a convolution).

### F.1.4 — The initial and final value theorems

**Initial value theorem.** If $F$ is a strictly proper rational function, $f(0^+) = \lim_{s\to\infty}sF(s)$.

**Final value theorem (FVT).** Let $F$ be rational. If **all poles of $sF(s)$ lie in the open left half-plane** — equivalently, $F$ has at most a simple pole at $s = 0$ and every other pole has negative real part — then $\lim_{t\to\infty}f(t)$ exists and

$$\lim_{t\to\infty}f(t) = \lim_{s\to0}sF(s)$$

*Proof for rational $F$.* Expand in partial fractions. A term $c/s$ contributes the constant $c$ to $f$ and $c$ to $\lim_{s\to0}sF$. Every other term has the form $c/(s-p)^k$ with $\mathrm{Re}\,p < 0$; it contributes $c\,t^{k-1}e^{pt}/(k-1)!\to0$ to $f$ and $\lim_{s\to0}s\,c/(s-p)^k = 0$ to $sF$. Both sides agree term by term. $\square$

The hypothesis is not decoration. Without it the formula returns a finite number for a signal that has no limit:

| $F(s)$ | $\lim_{s\to0}sF(s)$ | actual $f(t)$ | why FVT fails |
|---|---|---|---|
| $1/(s-1)$ | $0$ | $e^t\to\infty$ | pole in the right half-plane |
| $\omega/(s^2+\omega^2)$ | $0$ | $\sin\omega t$, no limit | poles on the imaginary axis |
| $1/s^2$ | $\infty$ | $t\to\infty$ | double pole at the origin |

In control, $F$ is usually $E(s) = S(s)R(s)$, and the hypothesis reduces to **closed-loop stability** plus a reference whose transform has at most a simple pole at the origin (F.8). Ch. 18 §18.6.3 states the FVT without this condition; it should be read with it.

---

## F.2 — State Space and the Transfer Function

### F.2.1 — From state space to $G(s)$

Consider the LTI state-space model of Ch. 21 §21.7.1,

$$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}u, \qquad y = \mathbf{C}\mathbf{x} + Du, \qquad \mathbf{x}\in\mathbb{R}^n$$

Transform with F.1.2: $s\mathbf{X}(s) - \mathbf{x}(0^-) = \mathbf{A}\mathbf{X}(s) + \mathbf{B}U(s)$. For $s$ not an eigenvalue of $\mathbf{A}$, $s\mathbf{I} - \mathbf{A}$ is invertible and

$$Y(s) = \underbrace{\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{x}(0^-)}_{\text{zero-input response}} + \underbrace{\left[\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B} + D\right]}_{G(s)}U(s)$$

The transfer function is defined with $\mathbf{x}(0^-) = 0$:

$$\boxed{G(s) = \mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B} + D}$$

> **[DERIVATION]** The formula is exact for LTI state-space models. The zero-input term is why Ch. 21 §21.0.2 lists "no internal initial-condition dependence" as a condition: the transfer function describes the forced response only.

In the time domain, $\mathcal{L}\{e^{\mathbf{A}t}\} = (s\mathbf{I}-\mathbf{A})^{-1}$, and the impulse response is $g(t) = \mathbf{C}e^{\mathbf{A}t}\mathbf{B}\,u(t) + D\,\delta(t)$; the full solution is $\mathbf{x}(t) = e^{\mathbf{A}t}\mathbf{x}(0) + \int_0^te^{\mathbf{A}(t-\tau)}\mathbf{B}u(\tau)\,d\tau$.

### F.2.2 — Properties

1. **Rationality and properness.** $(s\mathbf{I}-\mathbf{A})^{-1} = \mathrm{adj}(s\mathbf{I}-\mathbf{A})/\det(s\mathbf{I}-\mathbf{A})$. The adjugate's entries are polynomials of degree at most $n-1$ and the determinant has degree $n$, so $\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}$ is strictly proper, and $G$ is proper, strictly proper iff $D = 0$.
2. **Poles are eigenvalues — but not necessarily all of them.** Every pole of $G$ is an eigenvalue of $\mathbf{A}$. The converse holds iff the realisation is **minimal** (controllable and observable); otherwise some eigenvalues cancel between numerator and denominator (T. Kailath, *Linear Systems*, Prentice-Hall 1980, Ch. 2 and Ch. 6). Ch. 21 §21.7.1's statement "eigenvalues of $\mathbf{A}$ = poles of $P(s)$" assumes minimality.
3. **Coordinate invariance.** Under $\mathbf{x} = \mathbf{T}\mathbf{z}$, $(\mathbf{A},\mathbf{B},\mathbf{C},D)\to(\mathbf{T}^{-1}\mathbf{A}\mathbf{T},\mathbf{T}^{-1}\mathbf{B},\mathbf{C}\mathbf{T},D)$ and $G$ is unchanged, since $\mathbf{C}\mathbf{T}(s\mathbf{I} - \mathbf{T}^{-1}\mathbf{A}\mathbf{T})^{-1}\mathbf{T}^{-1}\mathbf{B} = \mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}$.

The practical danger of property 2: an unstable eigenvalue that cancels from $G$ is a *hidden* mode. The input–output map is then bounded while an internal state grows. This is why closed-loop stability in F.5 is stated for the characteristic polynomial, not just for one transfer function.

### F.2.3 — Example: the series RLC circuit

With states $x_1 = v_C$, $x_2 = i$, KVL (Appendix E §E.10) and the capacitor law give $C\dot x_1 = x_2$ and $L\dot x_2 = v_{in} - Rx_2 - x_1$:

$$\mathbf{A} = \begin{pmatrix}0 & 1/C\\ -1/L & -R/L\end{pmatrix}, \qquad \mathbf{B} = \begin{pmatrix}0\\ 1/L\end{pmatrix}, \qquad \mathbf{C} = \begin{pmatrix}1 & 0\end{pmatrix}, \qquad D = 0$$

Then $\det(s\mathbf{I}-\mathbf{A}) = s^2 + (R/L)s + 1/(LC)$, and the first row of the adjugate is $(s + R/L,\ 1/C)$, so

$$G(s) = \frac{V_C}{V_{in}} = \frac{1/(LC)}{s^2 + (R/L)s + 1/(LC)} = \frac{\omega_0^2}{s^2 + 2\zeta\omega_0s + \omega_0^2}$$

with $\omega_0 = 1/\sqrt{LC}$ and $\zeta = (R/2)\sqrt{C/L}$, the result of Ch. 17 §17.6.2.

### F.2.4 — BIBO stability and pole locations

**Theorem.** A proper rational $G(s)$ is bounded-input bounded-output stable iff every pole has negative real part.

*Proof sketch.* (i) An LTI system $y = g*u$ is BIBO stable iff $\int_0^\infty|g(t)|\,dt < \infty$, plus a possible finite impulse at $t = 0$ from $D$. Sufficiency: $|y(t)|\leq\sup|u|\int|g|$. Necessity: for fixed $t_0$ choose $u(\tau) = \mathrm{sgn}\,g(t_0-\tau)$; then $y(t_0) = \int_0^{t_0}|g|$, which must stay bounded. (ii) By partial fractions, $g$ is a finite sum of terms $t^ke^{pt}$; each is integrable iff $\mathrm{Re}\,p < 0$. $\square$

This is the statement of Ch. 21 §21.3.1. Poles on the imaginary axis, called "marginally stable" in Ch. 18 §18.6.3, are **not** BIBO stable: a bounded input at the pole frequency produces an unbounded (resonant) output.

---

## F.3 — The Standard Second-Order Step Response

### F.3.1 — Setting

$G(s) = \omega_0^2/(s^2 + 2\zeta\omega_0s + \omega_0^2)$ with $\omega_0 > 0$, $\zeta > 0$, unit DC gain, no zeros, and a unit step input $U = 1/s$, zero initial state. The poles are $s_{1,2} = -\zeta\omega_0\pm\omega_0\sqrt{\zeta^2-1}$ (Ch. 17 §17.7.2). Then $Y(s) = \omega_0^2/[s(s^2 + 2\zeta\omega_0s + \omega_0^2)]$.

### F.3.2 — Underdamped, $0 < \zeta < 1$

Let $\sigma = \zeta\omega_0$ and $\omega_d = \omega_0\sqrt{1-\zeta^2}$, so the denominator is $(s+\sigma)^2 + \omega_d^2$. Partial fractions:

$$Y(s) = \frac1s - \frac{s + 2\sigma}{(s+\sigma)^2 + \omega_d^2} = \frac1s - \frac{s+\sigma}{(s+\sigma)^2+\omega_d^2} - \frac{\sigma}{\omega_d}\,\frac{\omega_d}{(s+\sigma)^2+\omega_d^2}$$

(check: over the common denominator, $(s^2 + 2\sigma s + \omega_0^2) - s(s + 2\sigma) = \omega_0^2$, using $(s+\sigma)^2 + \omega_d^2 = s^2 + 2\sigma s + \omega_0^2$). Inverting with the frequency-shift rule $\mathcal{L}\{e^{-\sigma t}f(t)\} = F(s+\sigma)$,

$$y(t) = 1 - e^{-\sigma t}\left(\cos\omega_dt + \frac{\zeta}{\sqrt{1-\zeta^2}}\sin\omega_dt\right) = 1 - \frac{e^{-\sigma t}}{\sqrt{1-\zeta^2}}\sin\left(\omega_dt + \phi\right), \quad \cos\phi = \zeta$$

which is the bracket of Ch. 17 §17.7.3.

**Peak time and overshoot.** $y'(t)$ is the impulse response, $g(t) = \frac{\omega_0}{\sqrt{1-\zeta^2}}e^{-\sigma t}\sin\omega_dt$, which vanishes at $t = k\pi/\omega_d$. The first maximum is at $t_p = \pi/\omega_d$, where $\cos\omega_dt_p = -1$ and $\sin\omega_dt_p = 0$:

$$y(t_p) = 1 + e^{-\sigma\pi/\omega_d} \qquad\Longrightarrow\qquad \boxed{M_p = e^{-\pi\zeta/\sqrt{1-\zeta^2}}}$$

> **[DERIVATION]** $M_p$ is exact for the pure second-order system with no zeros. A zero, or a third pole that is not far to the left, changes it; for higher-order systems the formula is used under a dominant-pole approximation (small parameter: ratio of the dominant to the next pole's real part).

### F.3.3 — Critically damped, $\zeta = 1$

$Y(s) = \omega_0^2/[s(s+\omega_0)^2] = 1/s - 1/(s+\omega_0) - \omega_0/(s+\omega_0)^2$, so

$$y(t) = 1 - e^{-\omega_0t}\left(1 + \omega_0t\right)$$

which rises monotonically: $y' = \omega_0^2te^{-\omega_0t}\geq0$.

### F.3.4 — Overdamped, $\zeta > 1$

The poles $s_{1,2} = -\omega_0(\zeta\mp\sqrt{\zeta^2-1})$ are real and negative, with $s_1s_2 = \omega_0^2$. Partial fractions give

$$y(t) = 1 + \frac{s_2e^{s_1t} - s_1e^{s_2t}}{s_1 - s_2}$$

(check: $y(0) = 0$ and $y'(0) = 0$, the latter because $G$ has relative degree 2). There is no overshoot. For $\zeta\gg1$ the slow pole is $s_1\approx-\omega_0/(2\zeta)$ and dominates; the system behaves as first-order with time constant $2\zeta/\omega_0$.

### F.3.5 — Settling time and rise time

The underdamped response lies within the envelope $1\pm e^{-\sigma t}/\sqrt{1-\zeta^2}$. Requiring the envelope to be inside a $2\%$ band gives

$$t_s = \frac{1}{\zeta\omega_0}\left[\ln50 + \ln\frac{1}{\sqrt{1-\zeta^2}}\right] \approx \frac{3.9 + \ln(1/\sqrt{1-\zeta^2})}{\zeta\omega_0}$$

> **[APPROXIMATION]** $t_s\approx4/(\zeta\omega_0)$. Three simplifications: $\ln50 = 3.91$ rounded to 4; the factor $1/\sqrt{1-\zeta^2}$ dropped (adds $0.14$ to the numerator at $\zeta = 0.5$, $0.34$ at $\zeta = 0.7$); and the envelope used in place of the actual last crossing of the band. **Small parameter:** $\zeta^2$, in the sense that the dropped logarithm is $\approx\zeta^2/2$. Numerically, the true $2\%$ settling time is $11.2/\omega_0$ at $\zeta = 0.3$ (formula: $13.3$), $8.1/\omega_0$ at $\zeta = 0.5$ (formula: $8.0$), and $6.0/\omega_0$ at $\zeta = 0.7$ (formula: $5.7$). **Fails when:** $\zeta\to1$ or $\zeta > 1$, where the response is not oscillatory and settling is set by the slow real pole; for a $5\%$ band the constant is $\ln20\approx3$.

The rise time quoted in Ch. 17 §17.7.3, $t_r\approx1.8/\omega_0$, is a curve fit rather than a derivation. The exact $10\%$–$90\%$ rise time is $1.32/\omega_0$ at $\zeta = 0.3$, $1.64/\omega_0$ at $\zeta = 0.5$, and $2.13/\omega_0$ at $\zeta = 0.7$; $1.8/\omega_0$ is a single number representative of the middle of this range (G. F. Franklin, J. D. Powell, A. Emami-Naeini, *Feedback Control of Dynamic Systems*, Pearson, any recent edition, Ch. 3).

---

## F.4 — Bode Asymptotes

### F.4.1 — Factorisation

A rational $G(j\omega)$ with real coefficients factors into gains, integrators $(j\omega)^{\pm1}$, first-order factors $(1 + j\omega/p)^{\pm1}$, and second-order factors $[1 + 2\zeta(j\omega/\omega_0) + (j\omega/\omega_0)^2]^{\pm1}$. Because $\log|G_1G_2| = \log|G_1| + \log|G_2|$ and $\angle G_1G_2 = \angle G_1 + \angle G_2$, magnitude in decibels ($20\log_{10}|G|$) and phase are sums of the contributions of each factor. This additivity is the entire reason the Bode plot is drawn on logarithmic axes.

### F.4.2 — First-order pole

For $G = 1/(1 + j\omega/p)$, $p > 0$:

$$20\log_{10}|G| = -10\log_{10}\left(1 + \omega^2/p^2\right) \to \begin{cases}0 & \omega\ll p\\ -20\log_{10}(\omega/p) & \omega\gg p\end{cases}, \qquad \angle G = -\arctan(\omega/p)$$

The two asymptotes meet at the corner $\omega = p$, where the true value is $-10\log_{10}2 = -3.01$ dB — the largest error of the asymptotic magnitude. The phase passes through $-45°$ at the corner; the straight-line phase approximation from $0°$ at $p/10$ to $-90°$ at $10p$ has maximum error $\arctan(0.1) = 5.7°$ at its ends. A left-half-plane zero mirrors both plots. A right-half-plane zero, $1 - j\omega/z$, has the magnitude of a left-half-plane zero but the phase of a pole: the non-minimum-phase case of Ch. 21 §21.0.2.

### F.4.3 — Integrator

$G = 1/(j\omega)$: a straight line at $-20$ dB/decade through $0$ dB at $\omega = 1$, phase $-90°$ at all frequencies.

### F.4.4 — Second-order pole pair

With $u = \omega/\omega_0$,

$$|G|^2 = \frac{1}{(1-u^2)^2 + 4\zeta^2u^2}$$

The asymptotes are $0$ dB for $u\ll1$ and $-40\log_{10}u$ for $u\gg1$, meeting at $u = 1$, where the true value is $|G| = 1/(2\zeta)$. The error near the corner depends on $\zeta$ and is large for light damping. To find the resonant peak, minimise $Q(x) = (1-x)^2 + 4\zeta^2x$ over $x = u^2$: $Q'(x) = -2(1-x) + 4\zeta^2 = 0$ gives $x = 1 - 2\zeta^2$, which is positive iff $\zeta < 1/\sqrt2$. Then $Q_{min} = 4\zeta^4 + 4\zeta^2(1 - 2\zeta^2) = 4\zeta^2(1-\zeta^2)$, so

$$\omega_r = \omega_0\sqrt{1 - 2\zeta^2}, \qquad M_r = \frac{1}{2\zeta\sqrt{1-\zeta^2}}$$

which are the expressions of Ch. 17 §17.7.4. The phase goes from $0°$ to $-180°$, passing $-90°$ at $\omega_0$, increasingly abruptly as $\zeta\to0$.

> **[APPROXIMATION]** Asymptotic Bode plot. **Small parameter:** distance from the corner frequencies in decades. Errors: $3$ dB at a first-order corner; $|20\log_{10}(2\zeta)|$ at a second-order corner (more than $6$ dB for $\zeta < 0.25$). **Fails when:** corners are closer than about a decade apart (contributions overlap) or a lightly damped pair is present.

For minimum-phase systems the phase is determined by the magnitude (Bode's gain–phase relation), so that a sustained slope of $-20n$ dB/decade implies a phase near $-90n°$ (H. W. Bode, *Network Analysis and Feedback Amplifier Design*, Van Nostrand 1945). This is the basis of the loop-shaping rule in Ch. 21 §21.6.1 that the crossover slope should be about $-20$ dB/decade.

---

## F.5 — The Argument Principle and the Nyquist Criterion

### F.5.1 — The argument principle

**Theorem.** Let $f$ be meromorphic on an open set containing a simple closed contour $\Gamma$ and its interior, with no zeros or poles on $\Gamma$. If $\Gamma$ is traversed once counter-clockwise, then

$$\frac{1}{2\pi j}\oint_\Gamma\frac{f'(s)}{f(s)}\,ds = Z - P$$

where $Z$ and $P$ count zeros and poles inside $\Gamma$ with multiplicity. Equivalently, the image curve $f(\Gamma)$ winds $Z - P$ times counter-clockwise around the origin.

*Proof sketch.* Near a zero $a$ of order $m$, $f(s) = (s-a)^mh(s)$ with $h$ analytic and non-zero, so $f'/f = m/(s-a) + h'/h$: a simple pole with residue $m$. Near a pole of order $m$, the same computation gives residue $-m$. Elsewhere inside $\Gamma$, $f'/f$ is analytic. The residue theorem gives $Z - P$. For the second form, note $f'/f = d(\log f)/ds$, so the integral equals $\frac{1}{2\pi j}$ times the change of $\log f = \ln|f| + j\arg f$ around $\Gamma$; $\ln|f|$ returns to its starting value, and the change of $\arg f$ is $2\pi$ times the winding number of $f(\Gamma)$ about $0$. $\square$

If $\Gamma$ is traversed **clockwise**, both signs flip: $f(\Gamma)$ encircles the origin $Z - P$ times **clockwise**. (Any standard complex-analysis text, e.g. L. V. Ahlfors, *Complex Analysis*, 3rd ed., McGraw-Hill 1979, Ch. 4.)

### F.5.2 — The Nyquist contour

Let $L(s)$ be proper and rational. The **Nyquist contour** $\mathcal{D}$ runs up the imaginary axis from $-jR$ to $+jR$ and closes with a semicircle of radius $R\to\infty$ in the right half-plane; traversed in this direction it is clockwise and encloses the entire open right half-plane. Where $L$ has poles on the imaginary axis (integrators, undamped resonances), $\mathcal{D}$ detours around them by small semicircles of radius $\epsilon\to0$ into the right half-plane, so that those poles are counted as outside.

### F.5.3 — Derivation of $Z = N + P$

Assume a unity-feedback loop with no cancellation of right-half-plane poles or zeros between $C$ and $P$ (otherwise a hidden unstable mode exists, F.2.2). Apply F.5.1 to $f(s) = 1 + L(s)$ on $\mathcal{D}$:

- The **zeros** of $1 + L$ are the closed-loop poles, since $T = L/(1+L)$ and $S = 1/(1+L)$ share the denominator $1 + L$ once common factors are absent. Let $Z$ be the number in the right half-plane.
- The **poles** of $1 + L$ are the poles of $L$, the open-loop poles. Let $P$ be the number in the right half-plane.
- The image $(1 + L)(\mathcal{D})$ encircles the origin exactly as $L(\mathcal{D})$ encircles $-1$. Let $N$ be the number of **clockwise** encirclements of $-1$ by $L(\mathcal{D})$.

Since $\mathcal{D}$ is clockwise, F.5.1 gives $N = Z - P$, that is,

$$\boxed{Z = N + P}$$

The closed loop is stable iff $Z = 0$, i.e. iff $N = -P$: the Nyquist plot must encircle $-1$ **counter-clockwise** exactly $P$ times. For an open-loop-stable $L$ ($P = 0$) this reduces to "no encirclement of $-1$", which is the form in Ch. 21 §21.3.4.

**The large semicircle.** Because $L$ is proper, $L(s)\to D_L$ (a constant, zero if strictly proper) as $|s|\to\infty$: the whole semicircle maps to one point, and in practice only $\omega\in(-\infty,\infty)$ needs plotting. Because $L$ has real coefficients, $L(-j\omega) = \overline{L(j\omega)}$: the negative-frequency half is the mirror image of the positive half in the real axis.

**The indentation at an integrator.** If $L(s)\approx K_v/s$ near $s = 0$ with $K_v > 0$, the detour $s = \epsilon e^{j\theta}$, $\theta$ from $-\pi/2$ to $+\pi/2$, maps to $L\approx(K_v/\epsilon)e^{-j\theta}$: an arc of radius $K_v/\epsilon\to\infty$ swept **clockwise** through $180°$, from $+90°$ to $-90°$. This arc closes the plot at infinity and must be included when counting $N$.

> **[DERIVATION]** The Nyquist criterion is an exact consequence of the argument principle for rational $L$; it extends to $L$ containing a pure delay $e^{-\theta s}$, because the argument principle needs only meromorphy, not rationality. It is a statement about the LTI model, and inherits every approximation that produced that model.

> **[STRUCTURAL CONNECTION]** The encirclement count is the winding number (degree) of a closed curve in $\mathbb{C}\setminus\{-1\}$ — the same mathematical object as the integer invariants of Ch. 7 in that it is unchanged by continuous deformation that avoids the singular point. The connection is mathematical, not a physical genealogy: the Nyquist plot is not a field configuration and nothing in it descends from band topology. Ch. 21 §21.3.4 tags this remark `[ANALOGY]`; the classification in this book's own taxonomy (two systems sharing one mathematical object) is closer to `[STRUCTURAL CONNECTION]`.

### F.5.4 — Gain and phase margins

For an open-loop-stable $L$ whose Nyquist plot crosses the negative real axis and the unit circle once each:

- **Phase crossover** $\omega_{pc}$: $\angle L(j\omega_{pc}) = -180°$. **Gain margin** $GM = 1/|L(j\omega_{pc})|$, i.e. $-20\log_{10}|L(j\omega_{pc})|$ dB: the factor by which the gain can rise before the plot passes through $-1$.
- **Gain crossover** $\omega_{gc}$: $|L(j\omega_{gc})| = 1$. **Phase margin** $PM = 180° + \angle L(j\omega_{gc})$: the extra phase lag that would bring the plot through $-1$.

These are the definitions of Ch. 21 §21.3.3. Their meaning comes from F.5.3: they measure the distance to the critical point along two particular directions. They can mislead when the plot crosses the unit circle or the real axis more than once, or for conditionally stable systems (stable only for an interval of gains). A direction-free measure is the **vector margin** $\min_\omega|1 + L(j\omega)| = 1/\max_\omega|S(j\omega)|$.

### F.5.5 — Worked example: $L(s) = K/[s(s+1)(s+2)]$

$P = 0$; one integrator. The phase is $\angle L(j\omega) = -90° - \arctan\omega - \arctan(\omega/2)$. It equals $-180°$ when $\arctan\omega + \arctan(\omega/2) = 90°$, i.e. when $\omega\cdot\omega/2 = 1$ (the tangent-addition denominator vanishes), so $\omega_{pc} = \sqrt2$ rad/s. There

$$|L(j\sqrt2)| = \frac{K}{\sqrt2\cdot\sqrt{3}\cdot\sqrt{6}} = \frac{K}{6}$$

so $GM = 6/K$, and the loop is closed-loop stable iff $K < 6$. For $K = 1$: $GM = 6$ ($15.6$ dB), and solving $\omega\sqrt{\omega^2+1}\sqrt{\omega^2+4} = 1$ gives $\omega_{gc} = 0.446$ rad/s and $PM = 53.4°$. F.6 recovers $K_u = 6$, $\omega = \sqrt2$ algebraically.

---

## F.6 — The Routh–Hurwitz Criterion

### F.6.1 — Statement

Let $\Delta(s) = a_ns^n + a_{n-1}s^{n-1} + \cdots + a_0$ with real coefficients and $a_n > 0$. Build the Routh array: row $s^n$ holds $a_n, a_{n-2}, a_{n-4},\ldots$; row $s^{n-1}$ holds $a_{n-1}, a_{n-3},\ldots$; each subsequent entry is

$$b_i = \frac{a_{n-1}a_{n-2i} - a_na_{n-2i-1}}{a_{n-1}}$$

formed from the two rows above it, and so on down to row $s^0$ (missing coefficients are zero).

**Theorem (Routh 1877, Hurwitz 1895).** If no first-column entry is zero, the number of roots of $\Delta$ in the open right half-plane equals the number of sign changes in the first column. In particular $\Delta$ is **Hurwitz** (all roots in the open left half-plane) iff every first-column entry is positive.

### F.6.2 — A necessary condition, proved

If $\Delta$ is Hurwitz with $a_n > 0$, every coefficient is positive. *Proof.* $\Delta = a_n\prod(s + \alpha_i)\prod(s^2 + \beta_ks + \gamma_k)$ over real roots $-\alpha_i$ ($\alpha_i > 0$) and complex pairs with $\beta_k = -2\,\mathrm{Re}(\text{root}) > 0$, $\gamma_k = |\text{root}|^2 > 0$. A product of polynomials with positive coefficients has positive coefficients. $\square$ The condition is not sufficient for $n\geq3$: $s^3 + s^2 + s + 6 = (s+2)(s^2 - s + 3)$ has positive coefficients and two right-half-plane roots.

### F.6.3 — Proof sketch

The idea is a reduction lemma. Write $\Delta(s) = r_1(s) + r_2(s)$ where $r_1$ collects the terms of degree $n, n-2, \ldots$ and $r_2$ those of degree $n-1, n-3,\ldots$ (the first two rows of the array). The third row is the polynomial $r_3 = r_1 - c\,s\,r_2$ with $c = a_n/a_{n-1}$, which removes the leading term. **Lemma:** if $c > 0$, then $\Delta$ is Hurwitz iff the degree-$(n-1)$ polynomial $r_2 + r_3$ — whose array is the original array with its first row deleted — is Hurwitz. Applied recursively, this reduces the question to a chain of positivity conditions on the first column. The lemma is proved through the Hermite–Biehler theorem: $\Delta$ is Hurwitz iff its even and odd parts have real, simple, interlacing roots on the imaginary axis with leading coefficients of the same sign — equivalently, iff $\arg\Delta(j\omega)$ increases monotonically by $n\pi/2$ as $\omega$ goes from $0$ to $\infty$ (an argument-principle statement, F.5.1) — and the Routh step preserves interlacing. The count of right-half-plane roots by sign changes follows from Sturm-sequence (Cauchy-index) arguments. A complete proof is in F. R. Gantmacher, *The Theory of Matrices*, Vol. 2, Chelsea 1959, Ch. XV.

### F.6.4 — Special cases

- **A zero in the first column, rest of row non-zero.** Replace it by a small $\epsilon > 0$, continue, and count sign changes as $\epsilon\to0^+$. This is a perturbation argument: roots move continuously with coefficients, and the perturbation does not move any root across the imaginary axis for $\epsilon$ small enough unless one lies on it.
- **An entire row of zeros.** This happens iff $\Delta$ has a factor that is an **even polynomial**, the *auxiliary polynomial* formed from the row above. An even polynomial's roots are symmetric about the origin: they come as $\pm a$ (real), $\pm j\omega$ (imaginary), or quadruples $\pm\alpha\pm j\beta$. A zero row therefore signals roots symmetric about the origin, **not necessarily** imaginary-axis roots; Ch. 21 §21.3.2's gloss "the system has poles on the imaginary axis" covers only one of the three cases. The procedure replaces the zero row by the coefficients of the derivative of the auxiliary polynomial and continues; the roots of the auxiliary polynomial are then found directly.

### F.6.5 — Third order

For $a_3s^3 + a_2s^2 + a_1s + a_0$ with $a_3 > 0$, the array is

$$\begin{array}{c|cc} s^3 & a_3 & a_1\\ s^2 & a_2 & a_0\\ s^1 & (a_2a_1 - a_3a_0)/a_2 & 0\\ s^0 & a_0 & \end{array}$$

so the polynomial is Hurwitz iff $a_2 > 0$, $a_0 > 0$, and $a_2a_1 > a_3a_0$; with $a_3 = 1$ these are the conditions of Ch. 21 §21.3.2.

### F.6.6 — Worked example: $1 + K/[s(s+1)(s+2)] = 0$

The characteristic polynomial is $s(s+1)(s+2) + K = s^3 + 3s^2 + 2s + K$, with array

$$\begin{array}{c|cc} s^3 & 1 & 2\\ s^2 & 3 & K\\ s^1 & (6-K)/3 & 0\\ s^0 & K & \end{array}$$

Stability requires $K > 0$ and $6 - K > 0$: **$0 < K < 6$**, so the ultimate gain is $K_u = 6$. At $K = 6$ the $s^1$ row vanishes; the auxiliary polynomial from the $s^2$ row is $3s^2 + 6$, with roots $s = \pm j\sqrt2$. Indeed $s^3 + 3s^2 + 2s + 6 = (s + 3)(s^2 + 2)$. The loop oscillates at $\omega_u = \sqrt2$ rad/s, period $T_u = 2\pi/\sqrt2 = \pi\sqrt2\approx4.44$ s — the quantities a Ziegler–Nichols experiment (Ch. 21 §21.4.3) would measure. For $K > 6$ the first column reads $1, 3, (6-K)/3 < 0, K > 0$: two sign changes, two right-half-plane poles. This agrees with F.5.5.

---

## F.7 — Root-Locus Rules

### F.7.1 — Angle and magnitude conditions

Let $L(s) = KG(s)$ with $G = N(s)/D(s)$, $N$ and $D$ monic of degrees $m < n$, open-loop zeros $z_i$ and poles $p_i$, and $K\geq0$. The closed-loop poles are the roots of $D(s) + KN(s) = 0$, i.e. $KG(s) = -1$. A point $s$ is on the locus iff

$$\angle G(s) = \sum_i\angle(s - z_i) - \sum_i\angle(s - p_i) = (2k+1)\,180°, \qquad K = \frac{1}{|G(s)|} = \frac{\prod|s - p_i|}{\prod|s - z_i|}$$

The angle condition determines the locus; the magnitude condition then gives the gain at each point.

### F.7.2 — Derivation of the rules

1. **$n$ branches, continuous in $K$.** $D + KN$ has degree $n$ for every $K$, and the roots of a polynomial depend continuously on its coefficients.
2. **Start and end.** At $K = 0$ the roots are those of $D$ — the open-loop poles. Dividing by $K$, $D/K + N = 0$; as $K\to\infty$, $m$ roots approach the zeros of $N$, and the remaining $n - m$ go to infinity.
3. **Real axis.** For real $s$, each complex-conjugate pair of poles or zeros contributes angles that cancel. A real pole or zero to the right of $s$ contributes $180°$; one to the left contributes $0°$. The angle condition holds iff the number of real poles plus zeros to the right of $s$ is **odd**.
4. **Asymptotes and centroid.** Expand for large $|s|$: $D = s^n - (\sum p_i)s^{n-1} + \cdots$ and $N = s^m - (\sum z_i)s^{m-1} + \cdots$, so

$$\frac{D}{N} = s^{n-m} - \left(\sum p_i - \sum z_i\right)s^{n-m-1} + O(s^{n-m-2}) = (s - \sigma_a)^{n-m} + O(s^{n-m-2})$$

with $\sigma_a = (\sum p_i - \sum z_i)/(n - m)$, using $(s - \sigma_a)^q = s^q - q\sigma_as^{q-1} + \cdots$. The characteristic equation $D/N = -K$ becomes $(s - \sigma_a)^{n-m}\approx-K$, so

$$s\approx\sigma_a + K^{1/(n-m)}e^{j(2k+1)\pi/(n-m)}, \qquad k = 0,\ldots,n-m-1$$

$n - m$ straight-line asymptotes radiating from the centroid $\sigma_a$ at angles $(2k+1)180°/(n-m)$, as in Ch. 21 §21.5.1.
5. **Breakaway and break-in points.** Where two branches meet on the real axis, $s$ is a double root of $\Delta(s) = D + KN$: $\Delta(s) = 0$ and $\Delta'(s) = D' + KN' = 0$. Eliminating $K$ ($K = -D/N = -D'/N'$) gives $D'N - DN' = 0$. Since along the real axis $K(s) = -D(s)/N(s)$ and $dK/ds = -(D'N - DN')/N^2$, this is **$dK/ds = 0$**. The condition is necessary, not sufficient: a candidate is accepted only if it lies on a real-axis segment of the locus and gives $K > 0$.
6. **Imaginary-axis crossings.** Found from Routh–Hurwitz (F.6) as the gain at which a row vanishes, or by substituting $s = j\omega$ into $\Delta$ and solving real and imaginary parts.
7. **Departure angles** from a complex pole $p_\ell$ follow from the angle condition at a point infinitesimally close to $p_\ell$: $\theta_{dep} = 180° + \sum\angle(p_\ell - z_i) - \sum_{i\neq\ell}\angle(p_\ell - p_i)$.

### F.7.3 — Worked example: $G(s) = 1/[s(s+1)(s+2)]$

Here $n = 3$, $m = 0$, poles $0$, $-1$, $-2$.

- **Real-axis segments:** $[-1, 0]$ (one pole to the right) and $(-\infty, -2]$ (three poles to the right).
- **Asymptotes:** angles $60°$, $180°$, $300°$; centroid $\sigma_a = (0 - 1 - 2)/3 = -1$.
- **Breakaway:** $K(s) = -s(s+1)(s+2) = -(s^3 + 3s^2 + 2s)$, so $dK/ds = -(3s^2 + 6s + 2) = 0$ gives

$$s = -1\pm\frac{1}{\sqrt3} = -0.423\ \text{or}\ -1.577$$

The point $-1.577$ lies in $(-2,-1)$, which is not on the locus, and gives $K = -0.385 < 0$: rejected. The point **$s = -0.423$** lies on $[-1,0]$. With $u = s + 1 = 1/\sqrt3$, $s(s+1)(s+2) = u(u^2 - 1) = -2/(3\sqrt3)$, so $K = 2/(3\sqrt3)\approx0.385$. At this gain the closed-loop poles are a double pole at $-0.423$ and a third at $-3 + 2(0.423) = -2.155$ (their sum must equal $-3$, the negative of the $s^2$ coefficient).
- **Imaginary-axis crossing:** $K = 6$ at $s = \pm j\sqrt2$ (F.6.6), with the third pole at $-3$.

For $0 < K < 0.385$ all three closed-loop poles are real (overdamped); for $0.385 < K < 6$ the dominant pair is complex and moves toward the $60°$ asymptote, with damping decreasing as $K$ rises; for $K > 6$ it is in the right half-plane. **Reading damping from pole angle:** a pole $-\zeta\omega_0 + j\omega_0\sqrt{1-\zeta^2}$ lies at distance $\omega_0$ from the origin, at angle $\theta$ from the **negative real axis** with $\cos\theta = \zeta$. Ch. 21 §21.5.2 measures this angle "from the imaginary axis"; measured from there, $\zeta$ is the *sine* of the angle.

---

## F.8 — Steady-State Error and System Type

### F.8.1 — Setting

Unity negative feedback, $E(s) = R(s) - Y(s) = S(s)R(s) = R(s)/[1 + L(s)]$. Write $L(s) = \frac{K\,\tilde N(s)}{s^q\,\tilde D(s)}$ with $\tilde N(0)$, $\tilde D(0)$ non-zero and normalised to $1$; the integer $q\geq0$ is the **system type**, the number of open-loop integrators. Assume the closed loop is stable, so that the FVT hypothesis of F.1.4 can hold.

### F.8.2 — Error constants

Apply the FVT to $E(s)$ for references $R = 1/s$, $1/s^2$, $1/s^3$:

$$e_{step} = \lim_{s\to0}\frac{1}{1 + L(s)} = \frac{1}{1 + K_{pos}}, \qquad e_{ramp} = \lim_{s\to0}\frac{1}{s + sL(s)} = \frac{1}{K_v}, \qquad e_{parab} = \lim_{s\to0}\frac{1}{s^2 + s^2L(s)} = \frac{1}{K_a}$$

with $K_{pos} = \lim_{s\to0}L(s)$, $K_v = \lim_{s\to0}sL(s)$, $K_a = \lim_{s\to0}s^2L(s)$. (Ch. 21 §21.4.2 writes the position constant as $K_p$, which collides with the proportional gain of §21.4.1; it is written $K_{pos}$ here.)

| Type $q$ | $K_{pos}$ | $K_v$ | $K_a$ | $e_{step}$ | $e_{ramp}$ | $e_{parab}$ |
|---|---|---|---|---|---|---|
| 0 | $K$ | 0 | 0 | $1/(1+K)$ | $\infty$ | $\infty$ |
| 1 | $\infty$ | $K$ | 0 | 0 | $1/K$ | $\infty$ |
| 2 | $\infty$ | $\infty$ | $K$ | 0 | 0 | $1/K$ |

Where an entry is $\infty$, the FVT hypothesis fails for $E(s)$ — it has a double or higher pole at the origin — and the error grows without bound; the table entry is the correct conclusion, but it is reached by noting the failure, not by applying the formula.

> **[DERIVATION]** The error constants follow from the FVT under closed-loop stability. Without stability the FVT returns a finite number for a diverging error.

**Disturbances.** For a step disturbance entering at the plant input, the error is $-P/(1 + CP)$ times the disturbance, and its steady-state value is zero iff the integrator is in the **controller** $C$ — an integrator in the plant downstream of the disturbance does not reject it. This is the elementary case of the internal model principle.

**Example.** For $L = K/[s(s+1)(s+2)]$ the type is 1, $K_v = \lim sL = K/2$, and $e_{ramp} = 2/K$. Since stability requires $K < 6$, the ramp error cannot be made smaller than $1/3$ with proportional control alone: a concrete instance of the gain–stability trade-off of Ch. 21 §21.1.2.

---

## F.9 — The Bode Sensitivity Integral

### F.9.1 — Statement

**Theorem.** Let $L(s)$ be rational with **relative degree at least 2**, let the closed loop be stable, and let $p_1,\ldots,p_{N_p}$ be the open-loop poles in the open right half-plane. Then

$$\int_0^\infty\ln|S(j\omega)|\,d\omega = \pi\sum_{k=1}^{N_p}\mathrm{Re}\,p_k$$

For a stable open loop the right side is zero. This is the integral of Ch. 21 §21.6.1, which states it without the relative-degree and closed-loop-stability conditions; both are needed. (Bode 1945, as cited in F.4.4, for the stable case; J. S. Freudenberg and D. P. Looze, "Right half plane poles and zeros and design tradeoffs in feedback systems", *IEEE Transactions on Automatic Control* 30(6), 555–565, 1985, for unstable open loops; a textbook treatment is M. M. Seron, J. H. Braslavsky, and G. C. Goodwin, *Fundamental Limitations in Filtering and Control*, Springer 1997.)

### F.9.2 — Proof for a stable open loop

With $P = 0$ and closed-loop stability, $S = 1/(1+L)$ has no poles in the closed right half-plane (closed-loop stability) and no zeros there (its zeros are the poles of $L$). So $\ln S$ has an analytic branch on the right half-plane and is continuous up to the imaginary axis. (If $L$ has imaginary-axis poles, $S$ has zeros there and $\ln|S|\to-\infty$ integrably; the standard indentation argument handles them.) By Cauchy's theorem, the integral of $\ln S$ around the Nyquist contour $\mathcal{D}$ of F.5.2 vanishes. Split it:

- **Imaginary axis**, $s = j\omega$, $ds = j\,d\omega$: the contribution is $j\int_{-R}^R\ln S(j\omega)\,d\omega$. Because $S(-j\omega) = \overline{S(j\omega)}$, $\ln|S|$ is even and $\arg S$ is odd, so this equals $2j\int_0^R\ln|S(j\omega)|\,d\omega$.
- **Semicircle**, $s = Re^{j\theta}$, $\theta$ from $\pi/2$ to $-\pi/2$: for large $|s|$, $L(s)\approx c/s^r$ with $r$ the relative degree, so $\ln S = -\ln(1+L) = -L + O(L^2)\approx-c/s^r$. The arc has length $\pi R$ and the integrand is $O(R^{-r})$, so the contribution is $O(R^{1-r})\to0$ when $r\geq2$.

Hence $\int_0^\infty\ln|S(j\omega)|\,d\omega = 0$. $\square$

For relative degree exactly 1, the arc integral does not vanish: with $L\approx c/s$, $\int_{arc}(-c/s)\,ds = -c\int_{\pi/2}^{-\pi/2}j\,d\theta = j\pi c$, and the result becomes $\int_0^\infty\ln|S|\,d\omega = -\frac{\pi}{2}\lim_{s\to\infty}sL(s)$. For unstable open loops, $S$ has zeros at the $p_k$; factoring out the Blaschke product $\prod(s - p_k)/(s + \bar p_k)$ and repeating the argument gives the $\pi\sum\mathrm{Re}\,p_k$ term (Freudenberg and Looze, cited above).

### F.9.3 — Interpretation: the waterbed

$\ln|S| < 0$ where feedback attenuates disturbances and $\ln|S| > 0$ where it amplifies them. With zero total area, any band of attenuation must be paid for by a band of amplification — the **waterbed effect**. The theorem alone does not force a large peak, because the amplification could be spread thinly over an infinite band. What forces the peak is the combination with a bandwidth limit: actuator limits, sensor noise, and unmodelled high-frequency dynamics make $|L|$ small above some $\omega_{max}$, so $\ln|S|\approx0$ there, and the positive area must be concentrated below $\omega_{max}$. Open-loop unstable poles make the budget strictly positive: they cost sensitivity whatever the controller.

> **[DERIVATION]** The integral is an exact consequence of analyticity for LTI rational loops. Its engineering force depends on a bandwidth constraint that is a modelling statement about the plant and actuators, not part of the theorem.

---

## F.10 — The DC Motor Transfer Function

### F.10.1 — Model and assumptions

The assumptions are those of Example 06 and Ch. 21 §21.8.1: linear magnetics (constant torque constant $K_t$ and back-EMF constant $K_b$), a lumped armature $R_a$–$L_a$ branch, viscous friction $B\omega$, a rigid rotor of inertia $J$, and a load torque $T_L$ treated as a disturbance.

**Electrical side.** By the lumped KVL of Appendix E §E.10 — with the armature inductance carrying its own $L_a\,di_a/dt$ branch voltage, and the motional EMF $K_b\omega$ appearing as a branch voltage in series —

$$V_a = R_aI_a + L_a\frac{dI_a}{dt} + K_b\,\omega$$

**Mechanical side.** Newton's second law for the rotor:

$$J\frac{d\omega}{dt} + B\omega = K_tI_a - T_L$$

**Energy consistency.** The electrical power absorbed by the back-EMF is $K_b\omega I_a$ and the mechanical power produced is $K_tI_a\omega$; for ideal electromechanical conversion these are equal, so $K_t = K_b$ in SI units (N·m/A = V·s/rad). This is the gyrator of Ch. 17 §17.5 and Ch. 21 §21.8.1.

### F.10.2 — Speed transfer function

With zero initial conditions and $T_L = 0$, $(L_as + R_a)I_a = V_a - K_b\Omega$ and $(Js + B)\Omega = K_tI_a$. Eliminating $I_a = (Js + B)\Omega/K_t$:

$$\left[(L_as + R_a)(Js + B) + K_tK_b\right]\Omega = K_tV_a$$

$$\boxed{\frac{\Omega(s)}{V_a(s)} = \frac{K_t}{(L_as + R_a)(Js + B) + K_tK_b} = \frac{K_t}{L_aJs^2 + (L_aB + R_aJ)s + (R_aB + K_tK_b)}}$$

This is Example 06's result. Three facts follow.

1. **No free integrator.** The denominator's constant term is $R_aB + K_tK_b > 0$, so $s = 0$ is not a pole. The DC gain is finite: $\Omega/V_a\to K_t/(R_aB + K_tK_b)$, and even with $B = 0$ it is $1/K_b$. A constant voltage produces a constant speed, not unbounded acceleration.
2. **The back-EMF removes, not creates, the integrator.** Without back-EMF and friction ($K_b = 0$, $B = 0$) the plant would be $K_t/[(L_as + R_a)Js]$, which does contain an integrator: torque proportional to voltage, integrated by inertia. The $K_tK_b$ term is a velocity feedback internal to the motor; it adds damping (Example 06 shows it moving the mechanical pole from $-B/J$ to a much faster value).
3. **Stability.** All coefficients are positive and the polynomial is second order, so both poles are in the left half-plane (F.6.2 is sufficient at $n = 2$).

### F.10.3 — Position transfer function

The shaft angle satisfies $\dot\theta = \omega$, so $\Theta = \Omega/s$ and

$$\frac{\Theta(s)}{V_a(s)} = \frac{K_t}{s\left[(L_as + R_a)(Js + B) + K_tK_b\right]}$$

which has exactly one integrator. A position loop around this plant with proportional control is type 1 (zero steady-state error to a position step, F.8); a speed loop is type 0 and needs integral action for zero steady-state speed error.

### F.10.4 — The reduced first-order speed model

> **[APPROXIMATION]** Neglect of armature inductance. Setting $L_a\to0$ gives
> $$\frac{\Omega}{V_a}\approx\frac{K_m}{\tau_ms + 1}, \qquad K_m = \frac{K_t}{R_aB + K_tK_b}, \qquad \tau_m = \frac{R_aJ}{R_aB + K_tK_b}$$
> **Small parameter:** $\tau_e/\tau_m$, with $\tau_e = L_a/R_a$. Formally, the second-order denominator has two real, widely separated poles near $-1/\tau_e$ and $-1/\tau_m$ when $4L_aJ(R_aB + K_tK_b)\ll(L_aB + R_aJ)^2$; dropping the fast pole is a singular-perturbation (dominant-pole) approximation. **Fails when:** the controller bandwidth approaches $1/\tau_e$, where the neglected electrical pole adds phase lag and the margins computed from the first-order model are optimistic.

With $\tau_m$ written as $J/R_t$, $R_t = B + K_tK_b/R_a$, this is the time constant of Example 06. The form $K_m/[s(\tau_ms + 1)]$ that appears in Ch. 21 §21.8.1 is the **position** plant $\Theta/V_a$ under the same approximation — not the speed plant. Ch. 21 §21.8.1 presents it as $\Omega/V_a$ and attributes its integrator to the back-EMF; by F.10.2 both statements are incorrect, and the $1/s$ belongs to the angle, $\dot\theta = \omega$.

---

## F.11 — Summary

| Result | Statement | Assumptions | Used in |
|---|---|---|---|
| Derivative rule | $\mathcal{L}\{f'\} = sF - f(0^-)$ | $f$, $f'$ of exponential order | Ch. 17 §17.6; Ch. 18 §18.6.3; Ch. 21 §21.7.1 |
| Convolution | $\mathcal{L}\{f*g\} = FG$ | causal, exponential order | Ch. 18 §18.6.3; Ch. 21 §21.2 |
| Final value theorem | $f(\infty) = \lim_{s\to0}sF(s)$ | poles of $sF$ in open LHP | Ch. 18 §18.6.3; Ch. 21 §21.4.2 |
| State space → TF | $G = \mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B} + D$ | LTI; zero initial state | Ch. 21 §21.7.1 |
| Poles vs eigenvalues | poles $\subseteq$ eig$(\mathbf{A})$, equal iff minimal | LTI | Ch. 21 §21.7.1–§21.7.2 |
| BIBO stability | iff all poles have $\mathrm{Re}\,p < 0$ | proper rational $G$ | Ch. 18 §18.6.3; Ch. 21 §21.3.1 |
| Second-order step | $y = 1 - e^{-\zeta\omega_0t}(\cos\omega_dt + \frac{\zeta}{\sqrt{1-\zeta^2}}\sin\omega_dt)$ | standard form, no zeros | Ch. 17 §17.7.3; Ch. 21 §21.2.2 |
| Overshoot | $M_p = e^{-\pi\zeta/\sqrt{1-\zeta^2}}$, $t_p = \pi/\omega_d$ | $0 < \zeta < 1$, no zeros | Ch. 17 §17.7.3; Ch. 21 §21.5.2 |
| Settling time | $t_s\approx4/(\zeta\omega_0)$ (2\% band) | envelope bound; $\zeta^2$ small | Ch. 17 §17.7.3; Ch. 21 §21.5.2 |
| Bode asymptotes | $-20$ dB/dec per pole; $3$ dB corner error; $M_r = 1/(2\zeta\sqrt{1-\zeta^2})$ | rational $G$; corners separated | Ch. 17 §17.6.2, §17.7.4; Ch. 21 §21.6 |
| Argument principle | winding of $f(\Gamma)$ about $0$ $= Z - P$ | $f$ meromorphic, nothing on $\Gamma$ | Ch. 21 §21.3.4 |
| Nyquist criterion | $Z = N + P$ ($N$ clockwise about $-1$) | LTI; no unstable cancellations | Ch. 21 §21.3.4 |
| Margins | $GM = 1/\lvert L(j\omega_{pc})\rvert$, $PM = 180° + \angle L(j\omega_{gc})$ | single crossings; stable $L$ | Ch. 21 §21.3.3, §21.6 |
| Routh–Hurwitz | RHP roots = sign changes in first column | real coefficients; special cases handled | Ch. 21 §21.3.2, §21.5.1 |
| Example $K/[s(s+1)(s+2)]$ | $K_u = 6$, $\omega_u = \sqrt2$; breakaway $-0.423$ at $K = 0.385$ | unity feedback, $K\geq0$ | Ch. 21 §21.3, §21.4.3, §21.5 |
| Root-locus rules | angle/magnitude conditions; centroid $(\sum p - \sum z)/(n-m)$; $dK/ds = 0$ | $m < n$, $K\geq0$ | Ch. 21 §21.5.1 |
| Steady-state error | $1/(1+K_{pos})$, $1/K_v$, $1/K_a$ by type | closed-loop stable | Ch. 21 §21.4.1–§21.4.2 |
| Bode sensitivity integral | $\int_0^\infty\ln\lvert S\rvert\,d\omega = \pi\sum\mathrm{Re}\,p_k$ | relative degree $\geq2$; closed-loop stable | Ch. 21 §21.6.1, §21.10 |
| DC motor speed | $\Omega/V_a = K_t/[(L_as+R_a)(Js+B)+K_tK_b]$, no integrator | linear magnetics; lumped armature; viscous friction | Ch. 21 §21.8.1; Example 06 |
| DC motor position | $\Theta/V_a = (\Omega/V_a)/s$, one integrator | as above | Ch. 21 §21.8.1 |

---

*End of Appendix F*
