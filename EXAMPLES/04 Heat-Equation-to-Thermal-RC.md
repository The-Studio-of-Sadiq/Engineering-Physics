# Example 4 — Heat Equation → Thermal RC Network

**A complete worked descent in six steps.**

**Source chapters:** [Ch. 15](../CHAPTERS/CHAPTER%2015.md) §15.7 (Navier–Stokes/energy) →
[Ch. 16](../CHAPTERS/CHAPTER%2016.md) §16.2 (diffusion) →
[Ch. 17](../CHAPTERS/CHAPTER%2017.md) §§17.1–17.3 (lumping, effort/flow) →
[Ch. 19](../CHAPTERS/CHAPTER%2019.md) §19.6 (resistances, dimensionless numbers)

**Question answered:** A thermal network looks like a circuit diagram but has no
inductors. What is missing, and why does it matter?

---

## Step 1 — Theory

Start from energy conservation for a solid with internal energy $u$ and heat
flux $\mathbf{q}$:

$$\rho c_p\frac{\partial T}{\partial t} = -\nabla\cdot\mathbf{q}$$

**Energy** is the conserved quantity, not heat. Heat is not a substance that
accumulates — it is energy *in transit*, and it has no independent conserved
density, which is why the balance above is written in terms of internal energy $u$
and flux $\mathbf{q}$ rather than some "heat content." This step is the **first law
of thermodynamics applied locally** — a law of physics, not a definition. What it
does *not* determine is $\mathbf{q}$, and closing that gap is the entire job of the
next line.

For a continuum, the flux follows from irreversible thermodynamics — the
Onsager form of Fourier's law (Ch. 13 §13.5.2):

$$\mathbf{q} = -k\nabla T$$

Substituting gives the heat equation:

$$\boxed{\rho c_p\frac{\partial T}{\partial t} = k\nabla^2 T \qquad\Longleftrightarrow\qquad \frac{\partial T}{\partial t} = \alpha\nabla^2 T,\quad \alpha = \frac{k}{\rho c_p}}$$

**The epistemic status here is mixed, and the ledger depends on not blurring it.**
Energy conservation is a law. Fourier's law is a **constitutive law** —
`[PHENOMENOLOGICAL]` in its macroscopic form. It can be *justified* as a
linear-response limit near equilibrium (the Onsager route of Ch. 13), which is what
earns it more than a bare empirical fit, but it is not an identity and it does not
follow from conservation. The heat equation is therefore a **composition**:

$$\underbrace{\text{energy conservation}}_{\text{law}} + \underbrace{\text{Fourier constitutive law}}_{\text{constitutive}} \;\longrightarrow\; \text{heat equation}$$

not a pure derivation from conservation alone. $\alpha$ is a genuine material
property with units m²/s — a diffusivity — and the linear-response reading also
gets its scaling right, but the constitutive step is where the physics is
*supplied*, and it is the step that fails when $k$ is anisotropic or strongly
temperature-dependent, or when the linear-gradient ansatz breaks down.

---

## Step 2 — Approximation

| # | Reduction | Kind | Cost |
|---|---|---|---|
| A | Constant $k$, $\rho c_p$ | `[APPROXIMATION]` | no temperature-dependent properties, no phase change |
| B | One-dimensional conduction | `[APPROXIMATION]` | no radial or 3D loss |
| C | Lumped: $Bi = hL_c/k \ll 0.1$ | `[APPROXIMATION]` | no internal gradient |
| D | Convection boundary: $q'' = h(T_s - T_\infty)$ | `[PHENOMENOLOGICAL]` | $h$ is empirical, not derived from first principles |

Reduction D deserves attention: it is the one place a thermal model meets a
purely empirical constitutive law. Newton's law of cooling has no microscopic
derivation — $h$ is a fitted number depending on geometry, orientation, and
flow regime. Everything else in a thermal network is `[DERIVATION]` or
`[APPROXIMATION]`; this is `[PHENOMENOLOGICAL]`, and it is usually the dominant
uncertainty in a real thermal design.

---

## Step 3 — Mathematical reduction

**Step 3a — integrate over the body** (exact):

$$\rho c_p V\frac{d\bar T}{dt} = -\oint \mathbf{q}\cdot\hat n\,dA$$

**Step 3b — split the boundary into convection, radiation, and contact terms:**

$$\rho c_p V\frac{d\bar T}{dt} = hA(T_\infty - \bar T) + \varepsilon\sigma A\left(T_{sur}^4 - \bar T^4\right) + \cdots$$

**Step 3c — linearise radiation about the operating point** (the small-$\Delta T$
approximation):

$$\varepsilon\sigma A(T_{sur}^4 - \bar T^4) \approx 4\varepsilon\sigma A\bar T^3\,(T_{sur} - \bar T)$$

**Step 3d — identify the network elements:**

| Physical term | Lumped element | Value |
|---|---|---|
| $\rho c_p V\,\dot T$ | capacitance $C$ | $C = \rho c_p V$ [J/K] |
| $hA\,(T_\infty - T)$ | resistance $R_{conv}$ | $R_{conv} = 1/hA$ [K/W] |
| $4\varepsilon\sigma A\bar T^3$ | added resistance | $R_{rad} = 1/(4\varepsilon\sigma A\bar T^3)$ |
| conduction through a wall | resistance | $R_{cond} = \delta/(kA)$ |

Steps 3a–3b are exact. Step 3c is an approximation that fails for large
temperature swings. Step 3d is a definition.

---

## Step 4 — Reduced model

The energy balance becomes a first-order ODE:

$$C\dot T + \frac{T - T_\infty}{R_{conv}} = \dot Q_{source}$$

Read as a circuit: a capacitor $C$ to ground, a resistor $R_{conv}$ to the
ambient node, a current source injecting $\dot Q_{source}$.

**The missing element.** There is no $L$. Thermal energy has no inertial term
because heat is not a conserved *quantity in motion* with momentum — it is energy
being transferred, and the transfer rate is set by the resistance alone. So:

| Domain | Order | Resonance? | Overshoot? |
|---|---|---|---|
| Electrical | 2nd order | yes | yes |
| Mechanical | 2nd order | yes | yes |
| **Thermal** | **1st order** | **no** | **no** |

**This is a design constraint, not a curiosity.** A first-order loop has no
phase lag beyond $-90°$, so a PID tuned on a mechanical second-order plant will
be systematically mistuned on a thermal one — typically too aggressive, because
the plant never rings. Ziegler–Nichols ultimate-gain tuning, which deliberately
drives a plant to its $-180°$ phase point, cannot even be applied: a
first-order plant has no such point.

---

## Step 5 — Engineering equation

**Worked problem.** A 100 mm cube of aluminium ($k = 205$ W/m·K,
$\rho c_p = 2.90\times 10^6$ J/m³·K) is cooled by forced air, $h = 50$ W/m²·K, on
all six faces in ambient air at 20 °C. Initially at 80 °C. Find $\tau$ and the
temperature after 60 s, and state whether the lumped model was justified.

**Check the criterion first** — this is the step most solutions skip:

$$L_c = \frac{V}{A} = \frac{10^{-3}\ \text{m}^3}{6\times 10^{-2}\ \text{m}^2} = 1.667\times 10^{-2}\ \text{m} = 16.67\ \text{mm},\qquad Bi = \frac{hL_c}{k} = \frac{50 \times 0.01667}{205} = 4.07\times 10^{-3}$$

$Bi \ll 0.1$: the lumped model is justified, with a large margin. (At $Bi = 0.1$ the internal gradient reaches 10% of the surface value and lumping fails.)

**Capacitance and resistance:**

$$C = \rho c_p V = 2.90\times 10^6 \times 10^{-3} = 2900\ \text{J/K}$$
$$R = \frac{1}{hA} = \frac{1}{50 \times 6\times 10^{-2}} = 0.333\ \text{K/W}$$

**Time constant and transient:**

$$\tau = RC = 0.333 \times 2900 = 968\ \text{s} \approx 16\ \text{min}$$
$$T(t) = T_\infty + (T_0 - T_\infty)e^{-t/\tau}$$
$$T(60) = 20 + 60\,e^{-60/968} = 20 + 60\times 0.940 = 76.4\ ^\circ\text{C}$$

After one minute the block has shed only 6% of its excess temperature. **That is
the design finding.** A 60 s dwell is thermally meaningless for this part, and
any process timed to it will run out of equilibrium long before it starts.

---

## Step 6 — Validity limits

| Assumption | Fails when | Consequence |
|---|---|---|
| $Bi \ll 0.1$ | $Bi \gtrsim 0.1$ — thin plates, low $k$, low $h$ | internal gradients; surface $T$ ≠ mean $T$ |
| Constant $h$ | flow regime changes, natural convection, boiling | $h$ is itself a function of the answer |
| Constant properties | high $T$; phase change | conductivity falls; latent heat adds a plateau |
| Lumped radiation | $\Delta T$ large | $T^4$ cannot be linearised |
| Steady $h$, no radiation coupling | enclosure geometry matters | view factors |
| **Time-invariant $\alpha$** | transient conduction at short $t$ | **see below** |

**The subtle one.** Two different criteria get confused here, and they are
opposites. For a **semi-infinite** solid — one whose depth greatly exceeds the
conduction depth — the surface response never settles: the conduction front
spreads as $\sqrt{\alpha t}$, the effective resistance behaves like
$1/\sqrt{\alpha t}$, and there is no constant $R$ in the lumped sense at all.
Lumping requires the **opposite** limit. The body must be *small* compared with
the diffusion length, so that heat has time to spread through it and it becomes
nearly isothermal.

Here $\alpha = k/(\rho c_p) = 205/(2.90\times 10^6) = 7.07\times 10^{-5}$ m²/s, so
over the thermal time constant $\tau = RC = 968$ s the diffusion length is
$\sqrt{\alpha\tau} = \sqrt{7.07\times 10^{-5}\times 968} = 0.26$ m — about five
times the 50 mm half-width. In Fourier-number form,
$Fo = \alpha\tau/L_c^2 = (7.07\times 10^{-5}\times 968)/(0.01667)^2 = 246$
$\gg 1$. **The body is therefore well mixed internally, and the single-node RC
model is self-consistent** — which is exactly what the $Bi \ll 0.1$ check
already said. $Bi$ compares surface resistance against internal resistance; $Fo$
compares diffusion against the time available. Both are required, and together
they are the lumped regime.

Had $\sqrt{\alpha t}$ come out *smaller* than $L_c$, the conclusion inverts: the
lumped assumption fails, and the one-node model has to be replaced by a spatial
discretisation — a semi-infinite or fin analysis, depending on geometry. Getting
this one inequality backwards is the standard way a thermal RC model turns out to
be wrong at the edge of its validity window.

**What this example demonstrates.** The thermal network is a real circuit — the
same conservation laws, the same algebra, the same solution methods. It is also
not an electrical circuit: it is first order, it has no inertia, and its single
constitutive parameter ($h$) is empirical rather than derived. Recognising
*which* engineering template applies is the skill the cross-branch identity is
supposed to build.

---

**Model Ledger:** see [Ch. 17 §17.1.1](../CHAPTERS/CHAPTER%2017.md) and
[Ch. 19 §19.9.1](../CHAPTERS/CHAPTER%2019.md) for the nine-row ledgers, including
the HVAC example that shows why a lumped thermal model has a *time-dependent*
validity window rather than a bandwidth.
