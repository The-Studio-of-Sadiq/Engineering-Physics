# Example 6 — Motor → Control System

**A complete worked descent in six steps.** This is the book's capstone example
in miniature: a physical machine, reduced to a transfer function, closed into a
control loop, with the validity limits stated at every stage.

**Source chapters:** [Ch. 17](../CHAPTERS/CHAPTER%2017.md) §17.7 (second-order template) →
[Ch. 19](../CHAPTERS/CHAPTER%2019.md) §19.2 (rotational mechanical systems) →
[Ch. 21](../CHAPTERS/CHAPTER%2021.md) §§21.0.1–21.0.2 (what the capstone claim is, and the boundary of the transfer function),
§§21.2–21.4 (block-diagram algebra, stability, PID), §21.8.1 (DC motor speed control)

**Question answered:** How do you actually design a motor speed controller, and
where does the physics stop being trustworthy?

---

## Step 1 — Theory

A brushed DC motor is two coupled physical laws and nothing else.

**Electrical** (Ohm's law for the armature):
$$V_a = R_a I_a + L_a\frac{dI_a}{dt} - K_b\omega$$

**Mechanical** (Newton's second law for the rotor, Ch. 19 §19.2.1):
$$J\frac{d\omega}{dt} + B\omega = K_t I_a$$

| Symbol | Meaning | Typical value |
|---|---|---|
| $V_a$ | applied armature voltage | 24 V |
| $R_a$ | armature resistance | 0.5 Ω |
| $L_a$ | armature inductance | 5 mH |
| $J$ | rotor + load inertia | $2\times 10^{-4}$ kg·m² |
| $B$ | viscous friction | $2\times 10^{-5}$ N·m·s |
| $K_t$ | torque constant | $8\times 10^{-3}$ N·m/A |
| $K_b$ | back-EMF constant | $8\times 10^{-3}$ V·s/rad |

Two first-order ODEs, one electrical state ($I_a$) and one mechanical state
($\omega$). Nothing about control theory has entered yet.

---

## Step 2 — Approximation

A DC motor is **not** a first-order plant, and treating it as one is the most
common modelling error in motor control. There are two states.

| # | Reduction | Kind | Cost |
|---|---|---|---|
| A | Neglect $L_a\,\dot I_a$ | `[APPROXIMATION]` | valid only if $\omega_e\tau_e \gg 1$ where $\tau_e = L_a/R_a$ |
| B | Linearise $B\omega$ (already linear) | — | none |
| C | Treat $K_t$, $K_b$ as constants | `[APPROXIMATION]` | ignores magnetic saturation |
| D | Lump load inertia into $J$ | `[APPROXIMATION]` | ignores compliant shafts |

Reduction A is the tempting one and it is usually wrong in the wrong direction.
$\tau_e = L_a/R_a = 0.005/0.5 = 10$ ms. The mechanical time constant
$\tau_m = J/R_t$ with $R_t = B + K_tK_b/R_a = 2\times 10^{-5} + 1.28\times 10^{-4} = 1.48\times 10^{-4}$:

$$\tau_m = \frac{2\times 10^{-4}}{1.48\times 10^{-4}} = 1.35\ \text{s}$$

Since $\tau_e \ll \tau_m$, neglecting $L_a$ is justified for *bandwidth* purposes.
But if the control bandwidth were raised above $\sim 1/\tau_e \approx 100$ rad/s,
the electrical pole would re-enter and the plant would become third-order in
the closed loop. **The reduction is valid over a range that depends on the
controller you are about to design** — a fact that must be checked *after* the
design, not before.

---

## Step 3 — Mathematical reduction

Take the Laplace transform with zero initial conditions.

**Electrical:** $(R_a + L_a s)I_a - K_b\Omega = V_a$

**Mechanical:** $(Js + B)\Omega - K_t I_a = 0$

Eliminate $I_a$. From the mechanical equation, $I_a = (Js+B)\Omega/K_t$. Substitute:

$$\left[(R_a + L_a s)(Js + B) - K_tK_b\right]\Omega = K_t V_a$$

Define the electrical resistance seen at the rotor, $R_a + K_tK_b/s$ — the
back-EMF appears as a resistance. This is the standard DC motor reduction and it
is exact.

$$\Omega(s) = \frac{K_t}{(Js+B)(L_a s + R_a) + K_tK_b}\,V_a(s) = \frac{K_t}{L_aJs^2 + (JB + L_aR_a)s + (BR_a + K_tK_b)}\,V_a(s)$$

---

## Step 4 — Reduced model

Normalise to the standard second-order form $s^2/\omega_n^2 + 2\zeta s/\omega_n + 1$:

**DC gain:**
$$K = \frac{K_t}{BR_a + K_tK_b} = \frac{8\times 10^{-3}}{1\times 10^{-5} + 6.4\times 10^{-5}} = \frac{8\times 10^{-3}}{7.4\times 10^{-5}} = 108\ \text{rad/s per V}$$

At 24 V that predicts $2590$ rad/s $\approx 24{,}700$ rpm. **The real motor
cannot do this** — it is friction- and supply-limited. This is the first sign
that the linear model's validity is bounded, and it will be quantified in step 6.

**Natural frequency and damping:**
$$\omega_n^2 = \frac{BR_a + K_tK_b}{L_aJ} = \frac{7.4\times 10^{-5}}{0.005\times 2\times 10^{-4}} = 74\ \text{s}^{-2}$$
$$\omega_n = 8.6\ \text{rad/s} \quad (1.37\ \text{Hz})$$
$$\zeta = \frac{JB + L_aR_a}{2\sqrt{(BR_a + K_tK_b)L_aJ}} = \frac{4\times 10^{-9}\cdot 2 + 0.005\times 0.5}{2\sqrt{7.4\times 10^{-5}\times 0.005\times 2\times 10^{-4}}} = \frac{0.002504}{2\times 8.60\times 10^{-4}} = 1.46$$

**$\zeta = 1.46 > 1$: the open-loop plant is overdamped.** No resonance, no
overshoot. This single number drives the entire control design.

$$\boxed{G(s) = \frac{108}{s^2/\omega_n^2 + 2(1.46)s/\omega_n + 1} \;\approx\; \frac{108}{(1+1.46s)(1+1.05s)}}$$

The two real poles are at $s = -0.68$ and $s = -0.95$ s⁻¹ — matching
$1/\tau_m = 0.74$ and $1/\tau_e = 100$… but the second pole is at
$1/1.05 = 0.95$, not 100. That is because the slow pole dominates and the fast
electrical pole has been *pulled down* by the back-EMF feedback: it sits at
$-(BR_a + K_tK_b)/(L_aB) = -1/(L_a B/R_a)\cdot\ldots$, which is much slower than
$1/\tau_e$. Worth understanding, because it means the electrical dynamics are
*not* independently fast in the closed-loop plant.

---

## Step 5 — Engineering equation

**Design a PI velocity loop.** For an overdamped second-order plant, PI on
velocity is the right structure. With $C(s) = K_p(1 + 1/(\tau_i s))$ and unity
feedback:

$$K_p = \frac{\tau_m}{K} = \frac{1.35}{108} = 0.0125\ \text{V/(rad/s)}$$
$$\tau_i = 2\zeta\tau_m = 2(1.46)(1.35) = 3.94\ \text{s}$$

Closed loop:

$$T(s) = \frac{C(s)G(s)}{1 + C(s)G(s)}$$

Check the step response. The closed-loop bandwidth is approximately
$1/\tau_m$ with the PI zero placed to cancel the dominant lag, giving a
first-order-like response with $\tau_{cl} \approx \tau_m/2 = 0.68$ s and small
overshoot (ζ > 1 in the open loop means the PI zero placement dominates, giving
$\sim 5\%$ overshoot rather than the 16% a matched-damping design would give).

**Now check the real constraint.** The 24 V supply sets a hard speed limit
through the back-EMF:

$$\omega_{max} = \frac{V_a - I_aR_a}{K_b} = \frac{24 - 0.05\times 0.5}{8\times 10^{-3}} \approx 3000\ \text{rad/s}$$

But current is torque-limited: $T = K_tI_a$, and for this motor
$I_{cont} = 4$ A gives $T_{max} = 0.032$ N·m. The friction torque at
$3000$ rad/s is $B\omega = 2\times 10^{-5}\times 3000 = 0.06$ N·m — **almost
twice the available torque.** The motor cannot reach that speed. Solve
$B\omega = K_tI_{max}$:

$$\omega_{stall\text{-}free, friction\text{-}limited} = \frac{K_tI_{max}}{B} = \frac{0.032}{2\times 10^{-5}} = 1600\ \text{rad/s} \approx 15{,}000\ \text{rpm}$$

**Design finding.** The achievable top speed is set by friction against maximum
torque, not by the supply. The linear model predicted 24,700 rpm; the machine
delivers 15,000. A speed setpoint above 15,000 rpm integrates the velocity error
until the controller saturates on current, and the loop then runs in open loop.
Every commissioning procedure must check for this, because the symptom
(controller wound up, plant unresponsive) looks like a control fault rather than
a saturation limit.

---

## Step 6 — Validity limits

| Assumption | Fails when | Consequence |
|---|---|---|
| $L_a$ neglected | $\omega_{cl} > 1/\tau_e \approx 100$ rad/s | plant becomes effectively 3rd order; current spike on step |
| Linear friction $B\omega$ | Coulomb friction, stiction | dead band; limit cycle at low speed |
| No saturation | $V_a$ or $I_a$ limit reached | **integral windup**; the failure above |
| No magnetic saturation | $I_a$ above rated | $K_t$ falls; loop gain drops; heating |
| Rigid load | compliant coupling, backlash | torsional resonance; must be modelled (Ch. 19 §19.2.3) |
| Lumped $J$ | gearbox ratio, reflected inertia | use reflected inertia at the motor shaft |
| No disturbance | load torque varying | steady-state error; needs feedforward or integral action |

**Anti-windup is not optional here.** With an integral term and a saturating
actuator, a setpoint beyond the achievable speed drives the integrator
arbitrarily far. The standard remedies are back-calculation or clamping, and
both must be specified before tuning, not after.

**Anti-aliasing and current loop bandwidth.** Because $L_a$ was neglected, the
model contains no information about the current loop. In practice the current
loop is closed *inner* and *fast* (bandwidth $\gg$ velocity loop), which is what
justifies the reduction retrospectively. If the current loop is slow, the
velocity loop is fighting an unmodelled state.

**What this example demonstrates.** The full chain works and every step is
defensible: physics → two coupled ODEs → second-order transfer function →
closed-loop design → hardware numbers. And the final design finding came from
the *physics* (friction vs available torque), not from the transfer function.
That is the point of the book's architecture — the transfer function is a
powerful tool, but it is valid on a bounded region, and the bounds are set by
the physics that was reduced away.

---

**Model Ledger:** the full nine-row ledgers for this example are in
[Ch. 21 §21.8.1 (DC motor) and §21.8.2 (CSTR)](../CHAPTERS/CHAPTER%2021.md),
which also work through a plant where the nonlinearity *is* the point.

**Next:** this example completes the six-step set. Return to
[`../README.md`](../README.md) for the full chapter architecture, or to
[Example 5](05%20Navier-Stokes-to-Fluid-Network.md) for a network whose
constitutive law is empirical rather than derived.
