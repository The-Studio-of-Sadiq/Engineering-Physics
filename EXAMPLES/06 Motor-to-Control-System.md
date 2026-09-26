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

**Electrical** (Ohm's law for the armature, with the back-EMF written as a
voltage *drop* in the direction that opposes the applied source — Lenz's law):
$$V_a = R_a I_a + L_a\frac{dI_a}{dt} + K_b\omega$$

The sign matters and is worth being explicit about. In motoring, $\omega$ and
$I_a$ have the same sign, so $K_b\omega$ is a drop in series with the applied
voltage; it can never *add* energy. Writing it as $-K_b\omega$ on the
right-hand side would make the back-EMF a source, and every sign downstream
(the $K_tK_b$ term in the transfer-function denominator) would be wrong.

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
| A | Neglect $L_a\,\dot I_a$ | `[APPROXIMATION]` | valid only if $\omega_{cl}\tau_e \ll 1$ where $\tau_e = L_a/R_a$ |
| B | Linearise $B\omega$ (already linear) | — | none |
| C | Treat $K_t$, $K_b$ as constants | `[APPROXIMATION]` | ignores magnetic saturation |
| D | Lump load inertia into $J$ | `[APPROXIMATION]` | ignores compliant shafts |

Reduction A is the tempting one and it is usually wrong in the wrong direction.
Neglecting $L_a$ *deletes a state*, so the question is not "is the term small
compared with the others" but "is the pole it creates outside the band I care
about". That pole is the bare electrical pole, at $-1/\tau_e = -R_a/L_a$. It is
negligible only when the **closed-loop** bandwidth sits far *below* it:
$\omega_{cl}\tau_e \ll 1$. (The condition is a $\ll 1$, not a $\gg 1$: neglecting
an inductance is justified when the frequency is small compared with the
inductance's own cutoff, exactly as a low-pass filter passes signals below its
corner. An inductance may only be dropped at frequencies well below $R_a/L_a$.)
Here $\tau_e = L_a/R_a = 0.005/0.5 = 10$ ms, so $\omega_{cl} \ll 100$ rad/s.

The mechanical time constant is
$\tau_m = J/R_t$ with $R_t = B + K_tK_b/R_a = 2\times 10^{-5} + 1.28\times 10^{-4} = 1.48\times 10^{-4}$:

$$\tau_m = \frac{2\times 10^{-4}}{1.48\times 10^{-4}} = 1.35\ \text{s}$$

Since $\tau_e \ll \tau_m$, the two poles are widely separated and reducing to
first order is defensible — but only once step 4 confirms where the poles
actually sit, and only for a bandwidth well under 100 rad/s. **The reduction is
valid over a range that depends on the controller you are about to design** —
a fact that must be checked *after* the design, not before. Step 5 does exactly
that, and step 6 states where it breaks.

---

## Step 3 — Mathematical reduction

Take the Laplace transform with zero initial conditions.

**Electrical:** $(R_a + L_a s)I_a + K_b\Omega = V_a$, i.e.
$(R_a+L_as)I_a = V_a - K_b\Omega$

**Mechanical:** $(Js + B)\Omega - K_t I_a = 0$

Eliminate $I_a$. From the mechanical equation, $I_a = (Js+B)\Omega/K_t$. Substitute:

$$\left[(R_a + L_a s)(Js + B) + K_tK_b\right]\Omega = K_t V_a$$

The $K_tK_b$ enters with a **plus** sign, and it is worth seeing why. The
mechanical side feeds the electrical side back: since $\Omega = \frac{K_t}{Js+B}I_a$,
the induced voltage $K_b\Omega = \frac{K_tK_b}{Js+B}I_a$ is an impedance
$K_tK_b/(Js+B)$ seen by the armature, in parallel with $R_a+L_as$. A parallel
impedance lowers the effective impedance, which shows up as an *increased*
constant term in the denominator. The $s$-coefficient is untouched by the
back-EMF, because the coupling feeds back through the mechanical state, which is
already in the denominator. This is the standard DC motor reduction, and it is
exact within the model.

$$\boxed{\frac{\Omega(s)}{V_a(s)} = \frac{K_t}{(L_a s + R_a)(Js + B) + K_tK_b} = \frac{K_t}{L_aJs^2 + (L_aB + R_aJ)s + (R_aB + K_tK_b)}}$$

**The middle coefficient is $L_aB + R_aJ$.** Each term pairs an electrical
quantity with the mechanical quantity of the same role: $L_a$ (electrical
inertia) with $B$ (rotational damping), and $R_a$ (electrical resistance) with
$J$ (rotational inertia). Pairing them the other way round, $JB + L_aR_a$, is
not a convention difference — it is dimensionally wrong ($JB$ cannot be a
coefficient of $s$ in this polynomial) and it is the single most consequential
error this example is here to prevent.

---

## Step 4 — Reduced model

Normalise to the standard second-order form $s^2/\omega_n^2 + 2\zeta s/\omega_n + 1$:

**Coefficients**, with the values from step 1:

$$L_aJ = 1\times 10^{-6} \qquad L_aB + R_aJ = \underbrace{1\times 10^{-7}}_{L_aB} + \underbrace{1\times 10^{-4}}_{R_aJ} = 1.001\times 10^{-4} \qquad R_aB + K_tK_b = 7.4\times 10^{-5}$$

Note how lopsided that middle coefficient is: $R_aJ = 10^{-4}$ dominates $L_aB = 10^{-7}$
by three orders of magnitude.

**DC gain:**
$$K = \frac{K_t}{R_aB + K_tK_b} = \frac{8\times 10^{-3}}{7.4\times 10^{-5}} = 108\ \text{rad/s per V}$$

At 24 V that predicts $2595$ rad/s $\approx 24{,}800$ rpm. **The real motor
cannot do this** — it is torque-limited, not supply-limited. This is the first
sign that the linear model's validity is bounded, and it is quantified in step 5.

**Natural frequency and damping:**
$$\omega_n^2 = \frac{R_aB + K_tK_b}{L_aJ} = \frac{7.4\times 10^{-5}}{1\times 10^{-6}} = 74\ \text{s}^{-2} \qquad \omega_n = 8.60\ \text{rad/s} \quad (1.37\ \text{Hz})$$
$$\zeta = \frac{L_aB + R_aJ}{2\sqrt{(R_aB + K_tK_b)\,L_aJ}} = \frac{1.001\times 10^{-4}}{2\sqrt{7.4\times 10^{-5}\times 1\times 10^{-6}}} = \frac{1.001\times 10^{-4}}{2\times 8.60\times 10^{-6}} = 5.82$$

**$\zeta = 5.82 \gg 1$: the open-loop plant is strongly overdamped.** No
resonance, no overshoot. This single number drives the entire control design.

$$\boxed{G(s) = \frac{108}{s^2/\omega_n^2 + 2(5.82)s/\omega_n + 1} = \frac{8000}{s^2 + 100.1\,s + 74} = \frac{8000}{(s+0.745)(s+99.36)}}$$

The two real poles are at $s = -0.745$ and $s = -99.36$ s⁻¹, i.e. time
constants of $1.34$ s and $10.1$ ms. Two things are worth understanding here,
because both are counter-intuitive:

- **The electrical pole is essentially where it was supposed to be.** $1/\tau_e = R_a/L_a = 100$ rad/s, and the actual fast pole is $-99.36$ s⁻¹. The back-EMF has barely moved it, exactly as step 3 predicts: the $K_tK_b$ coupling changes only the constant term, so it shifts $\omega_n$ and the DC gain but leaves the $s$-coefficient — and hence the fast pole — essentially alone. (A *closed-loop* design can move this pole; the open-loop plant cannot.)
- **The back-EMF's real job is to damp the mechanical side.** Without it, the mechanical pole would sit at $-B/J = -0.1$ s⁻¹ ($\tau = 10$ s). With it, the pole is at $-0.745$ s⁻¹ ($\tau = 1.34$ s) — a factor of 7.5 faster. The back-EMF behaves like an added resistance referred through the gearbox ratio $K_t/K_b$, and resistance is damping.

---

## Step 5 — Engineering equation

**Design a PI velocity loop.** For a strongly overdamped plant, PI on velocity is
the right structure. The plant's poles are far apart ($0.745$ vs $99.4$ s⁻¹), so
over any sane velocity-loop bandwidth it is well approximated by its dominant
first-order pole:

$$G(s) \approx \frac{K}{1+\tau_m s} \qquad K = 108\ \text{rad/s per V}, \quad \tau_m = 1.34\ \text{s}$$

Take $C(s) = K_p\left(1 + \frac{1}{\tau_i s}\right)$ with unity feedback, and
place the PI zero on the dominant plant pole, $\tau_i = \tau_m$. The
$\left(1 + \tau_m s\right)$ then cancels exactly:

$$C(s)G(s) = \frac{K_pK(\tau_m s + 1)}{\tau_m s(1 + \tau_m s)} = \frac{K_pK}{\tau_m s} \qquad\Longrightarrow\qquad T(s) = \frac{K_pK}{\tau_m s + K_pK} = \frac{1}{1 + \tau_{cl} s}$$

That is a **pure first-order closed loop**: unity DC gain, no overshoot at all,
and — because the integrator survives the cancellation — exactly zero
steady-state error to a velocity step. Choosing a closed loop about twice as
fast as the open loop, $\tau_{cl} = \tau_m/2 = 0.67$ s:

$$K_p = \frac{\tau_m}{K\,\tau_{cl}} = \frac{1.34}{108\times 0.67} = 0.0185\ \text{V/(rad/s)} \qquad \tau_i = 1.34\ \text{s}$$

**Now the check step 2 promised.** The closed-loop bandwidth is
$\sim 1/\tau_{cl} = 1.5$ rad/s, which sits a factor of 66 below the neglected
electrical pole at $99.4$ rad/s. So $\omega_{cl}\tau_e = 0.015 \ll 1$, reduction A
is self-consistent, and the plant really was first order over this band. Had we
demanded a closed loop ten times faster, the check would have failed and the
second-order plant would have had to be kept.

**Now check the real constraint.** There are two candidate speed limits, and
the point of the example is that they do not agree.

*Supply-limited.* At speed $\omega$ the steady-state current is whatever
friction demands, $I_a = B\omega/K_t$, so the supply equation
$V_a = R_aI_a + K_b\omega$ gives

$$\omega_{max} = \frac{V_a}{K_b + R_aB/K_t} = \frac{24}{8\times 10^{-3} + 1.25\times 10^{-3}} = 2595\ \text{rad/s}$$

which is just $K V_a$, the linear model's own prediction.

*Torque-limited.* Current is torque-limited: $T = K_tI_a$, and $I_{cont} = 4$ A
gives $T_{max} = K_t I_{cont} = 0.032$ N·m. Setting friction torque equal to
available torque:

$$\omega_{max} = \frac{K_tI_{cont}}{B} = \frac{0.032}{2\times 10^{-5}} = 1600\ \text{rad/s} \approx 15{,}300\ \text{rpm}$$

**Design finding.** $1600 < 2595$, so the *torque* limit binds, not the supply —
the friction-limited speed is 62% of what the linear transfer function promises.
The diagnosis is visible in one number: at $1600$ rad/s the motor draws its full
$4$ A and the friction torque is $B\omega = 0.032$ N·m, exactly the available
torque, so there is nothing left to accelerate with. (For completeness, the
$1600$ rad/s operating point needs $V_a = R_aI + K_b\omega = 2 + 12.8 = 14.8$ V
of the available 24 V, so supply is not close to binding either.) The linear
model predicted 24,800 rpm; the machine delivers 15,300. A speed setpoint above
15,300 rpm integrates the velocity error until the controller saturates on
current, and the loop then runs in open loop. Every commissioning procedure must
check for this, because the symptom (controller wound up, plant unresponsive)
looks like a control fault rather than a saturation limit.

---

## Step 6 — Validity limits

| Assumption | Fails when | Consequence |
|---|---|---|
| $L_a$ neglected | $\omega_{cl} \gtrsim 1/\tau_e = 100$ rad/s (i.e. $\omega_{cl}\tau_e \gtrsim 1$) | neglected pole re-enters; current spike on step |
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
