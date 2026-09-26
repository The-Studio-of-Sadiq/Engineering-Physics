# Example 5 — Navier–Stokes → Fluid Network

**A complete worked descent in six steps.**

**Source chapters:** [Ch. 13](../CHAPTERS/CHAPTER%2013.md) §13.7 (Newtonian viscosity from Kubo) →
[Ch. 15](../CHAPTERS/CHAPTER%2015.md) §§15.3–15.7 (stress tensor, continuum conservation, ideal and viscous flow, exact solutions) →
[Ch. 16](../CHAPTERS/CHAPTER%2016.md) §16.10 (lumping) →
[Ch. 19](../CHAPTERS/CHAPTER%2019.md) §§19.7.1–19.7.3 (hydraulic effort–flow pair, pipe networks, pump curves) →
[Ch. 20](../CHAPTERS/CHAPTER%2020.md) §20.3 (open-channel hydraulics)

**Question answered:** How close is pipe-network analysis to Ohm's law, and which
term breaks the analogy? The answer turns out to be friction, not inertia.

---

## Step 1 — Theory

The incompressible Navier–Stokes equations, with a Newtonian stress tensor:

$$\rho\left(\frac{\partial\mathbf{v}}{\partial t} + \mathbf{v}\cdot\nabla\mathbf{v}\right) = -\nabla p + \mu\nabla^2\mathbf{v} + \rho\mathbf{g}$$

$$\nabla\cdot\mathbf{v} = 0$$

Two constitutive choices are embedded here and both are `[DERIVATION]`-level
results of Ch. 13, not postulates:

- **Newtonian viscosity** ($\tau = \mu\,d\mathbf{v}/dy$) — linear stress–rate
  relation, derived from the Kubo formula for momentum transport. Water, air,
  and most liquids and gases satisfy it; blood, toothpaste, and polymer melts
  do not.
- **Incompressibility** ($\nabla\cdot\mathbf{v}=0$) — constant $\rho$.

---

## Step 2 — Approximation

| # | Reduction | Kind | Typical validity |
|---|---|---|---|
| A | Steady, $\partial_t \to 0$ | `[APPROXIMATION]` | quasi-steady network analysis |
| B | Inertia, $\mathbf{v}\cdot\nabla\mathbf{v} \to 0$ | `[APPROXIMATION]` | **$Re \ll 1$** |
| C | Unidirectional, fully developed flow | `[APPROXIMATION]` | straight pipe, away from fittings |
| D | Lumped per segment | `[APPROXIMATION]` | $L \gg D$ |
| E | Empirical friction factor $f(Re,\varepsilon/D)$ | `[PHENOMENOLOGICAL]` | Moody chart / Colebrook |

**Reduction B is the dangerous one.** Dropping inertia is a *low*-Reynolds
assumption, and a whole lot of real pipe flow is high-Reynolds. The resolution
is that inertia can be retained in a lumped form — and, importantly, it comes
out **linear**.

**Inertia is linear.** For uniform (plug) acceleration $a = \dot v$, the pressure
force $\Delta p\,A$ balances the fluid's inertia $\rho A L a$:

$$\Delta p = \rho L\dot v = \frac{\rho L}{A}\dot Q, \qquad \boxed{\mathcal{I}_h = \frac{\rho L}{A}}$$

This is linear in $\dot Q$ and it is *exactly* the inductor law $V = L_{ind}\dot I$.
Hydraulic inertance is a genuine energy-storing element, and the inductor analogy
holds term for term.

**Friction is what is nonlinear.** The steady momentum balance, with friction
retained, gives **Darcy–Weisbach**:

$$\boxed{\Delta p = f\frac{L}{D}\frac{\rho v^2}{2}\ +\ \rho g\,\Delta z} \qquad\text{or in head form}\qquad \boxed{\Delta h = f\frac{L}{D}\frac{v^2}{2g}\ +\ \Delta z}$$

The $v^2$ belongs to *this* term, and this term is quadratic drag, not inertia.
It is worth being explicit about the difference, because conflating them is the
classic error: an inertance whose drop went as $v^2$ would be dimensionally
plausible but physically meaningless, and it would destroy the inductor
correspondence that makes hydraulic networks tractable at all. Darcy–Weisbach
itself contains no time derivative, so it says nothing about inertia either way.

The complete lumped pipe segment, for a transient, is the sum of the three
separate contributions:

$$\Delta p = \underbrace{\frac{\rho L}{A}\dot Q}_{\text{inertance, linear}} \ +\ \underbrace{f\frac{L}{D}\frac{\rho Q^2}{2A^2}}_{\text{friction, quadratic, } f\text{ empirical}} \ +\ \underbrace{\rho g\,\Delta z}_{\text{gravity, static}}$$

So the hydraulic network is a linear RLC-like circuit *plus* one nonlinear,
curve-fitted element. The nonlinearity is real, but it enters in one place only,
and it is the empirical one.

---

## Step 3 — Mathematical reduction

For a straight uniform pipe, assuming a velocity profile, integrating
$\nabla\cdot\mathbf{v}=0$ along the axis gives the volume flow:

$$Q = vA = v\frac{\pi D^2}{4}$$

and the momentum balance gives Darcy–Weisbach. Identify the effort/flow pair:

| Role | Quantity | Units |
|---|---|---|
| Effort | pressure $p$ (or head $h = p/\rho g$) | Pa, or m |
| Flow | volume flow $Q$ | m³/s |

For laminar flow, integrating the parabolic profile profile-for-profile (Hagen–Poiseuille) gives an *exact* linear law:

$$\Delta p = \frac{128\mu L}{\pi D^4}Q \qquad\Longrightarrow\qquad R_h = \frac{\Delta p}{Q} = \frac{128\mu L}{\pi D^4}$$

That $D^4$ is the reason pipe sizing is dominated by diameter rather than
length. It is also why the laminar resistance is a clean `[DERIVATION]` and the
turbulent one is not.

---

## Step 4 — Reduced model

Network elements, exactly parallel to the electrical case:

| Physical element | Hydraulic form | Electrical analog | Notes |
|---|---|---|---|
| Pipe, laminar | $R_h = \frac{128\mu L}{\pi D^4}$, $R_h = \Delta p/Q$ | resistor | linear; exact, `[DERIVATION]` |
| Pipe, turbulent | $R_h = \frac{fL}{D}\frac{\rho v}{2}$, $f = f(Re,\varepsilon/D)$ | nonlinear resistor | $I^2R$-like; $f$ empirical |
| Fitting / valve | $R_h$ | resistor | K-resistance; highly empirical |
| Fluid column in transit | $\Delta p = \frac{\rho L}{A}\dot Q$ | **inductor** | inertance $\mathcal{I}_h = \rho L/A$; **linear**, energy-storing |
| Expansion vessel / tank | $C = dV/dp$ | capacitor | compressibility storage |
| Pump | pressure source | voltage source | head–flow curve, not an ideal source |

Note the asymmetry that trips people up: the **inertance row is linear** and the
**friction row is not**. A pipe is therefore an $RLC$ segment in the linear
regime, and it is the turbulent $f$ — not the inertia — that makes real
networks nonlinear.

**Node and loop rules are exact.**

- **QCL** (flow sums to zero at a junction) is mass conservation: $\partial(\rho)/\partial t = 0$.
- **Loop rule** (head sums to zero around a loop) is Bernoulli along a streamline, valid under the same assumptions as §2.

Both are identities given the assumptions; neither is an electrical coincidence.

---

## Step 5 — Engineering equation

**Worked problem.** A 40 mm nominal steel pipe, 60 m long, carries water
($\nu = 1.0\times 10^{-6}$ m²/s, $\varepsilon = 0.045$ mm) from a reservoir at
the 30 m mark to a tank at the 10 m mark. Find the flow rate.

**Available head:** $\Delta h = 30 - 10 = 20$ m.

**Iterate on $Re$ because $f$ depends on it.** Guess $v = 1$ m/s:
$Re = vD/\nu = 1\times 0.04/10^{-6} = 4\times 10^4$ (turbulent).
$\varepsilon/D = 0.000045/0.04 = 1.125\times 10^{-3}$; Colebrook gives $f \approx 0.0216$.

$$h_f = f\frac{L}{D}\frac{v^2}{2g} = 0.0216\times\frac{60}{0.04}\times\frac{1}{19.62} = 32.4\times 0.051 = 1.65\ \text{m}$$

That is far below the 20 m available, so the guess was too low. Try $v = 3$ m/s:
$Re = 1.2\times 10^5$, $f \approx 0.0187$,
$$h_f = 0.0187\times 1500\times\frac{9}{19.62} = 28.1\times 0.459 = 12.9\ \text{m}$$

Still below 20. Try $v = 3.7$ m/s: $Re = 1.48\times 10^5$, $f \approx 0.0183$,
$$h_f = 0.0183\times 1500\times\frac{13.69}{19.62} = 27.5\times 0.698 = 19.2\ \text{m}$$

Close. $v \approx 3.8$ m/s gives $h_f \approx 20.4$ m. **Converged: $v \approx 3.76$ m/s.**

$$Q = vA = 3.76\times\frac{\pi(0.04)^2}{4} = 3.76\times 1.257\times 10^{-3} = 4.72\times 10^{-3}\ \text{m}^3/\text{s} \approx 4.7\ \text{L/s}$$

**The design finding.** Head loss scales as $v^2$, so for a fixed pipe the
available head is consumed as the *square root* of the flow rate: $Q\propto\sqrt{\Delta h}$.
That is the nonlinearity that matters, and it is why a pump curve has to be
intersected with a system curve numerically.

**What a second parallel pipe does — and does not — change.** Adding an
identical second pipe between the same two reservoirs **doubles the flow
exactly**: $Q_{total} = 2Q_1$. Each parallel branch spans the same two nodes, so
each sees the *same* head difference of 20 m, each runs at the same $Re$ and the
same $f$, and each independently carries $Q_1 = 4.7$ L/s. For this example that
gives $Q_{total} \approx 9.4$ L/s. Head is *shared* between parallel branches, not
divided among them; it is **series** elements that split the available head, each
taking a share in proportion to its resistance.

(This is exact only while the branches really are in parallel between common
nodes. If the two pipes share a common upstream run of finite resistance, that
shared run develops a pressure drop as total flow rises, the effective head across
each branch falls, and the gain is less than a factor of two. The doubling is the
ideal limit, and stating it as "roughly double, but not quite" is wrong for the
clean case and vague for the imperfect one.)

---

## Step 6 — Validity limits

| Assumption | Fails when | Use instead |
|---|---|---|
| Newtonian fluid | non-Newtonian rheology ($n\ne1$) | power-law model; apparent viscosity |
| Incompressible | $M > 0.3$, cavitation | compressible flow; flashing |
| $Re < 2000$, Hagen–Poiseuille | $Re > 2300$ | Colebrook/Moody; $f$ empirical |
| Fully developed | $L/D < 20$, fittings | entrance lengths; $K$-factors |
| **Inertia dropped** | $Re$ large, or transients of interest | **retained as the linear inertance $\rho L/A$; drop it only for slow, quasi-steady, low-$Re$ analysis** |
| Lumped per segment | fittings, valves, short lines | Ch. 15 §15.8.2 — turbulence has no exact closed-form model |
| Single-phase | two-phase, flashing | two-phase flow correlations |
| $f$ constant with $Q$ | varying $Re$ over the operating range | solve network iteratively |

The $f$-versus-$Re$ dependency is worth flagging as an engineering trap: because
$f \propto Re^{-0.2}$ in turbulent flow, the head loss goes as $Q^{1.8}$, not
$Q^2$. A pump curve intersecting a system curve needs a numerical solution, not
algebra, and treating $f$ as constant is a common source of wrong answers.

**What this example demonstrates.** Ohm's law for pipes is genuinely the same
algebra, and it comes from the same conservation laws. The inertia is linear and
maps cleanly onto an inductor; the nonlinearity enters through *friction*, and
the one coefficient that governs it ($f$) is empirical. So a pipe network is
circuit theory with a curve-fit in the resistive branch — closer to RLC than the
usual "pipes are not circuits" refrain suggests, but different enough that the
$f$ dependence must be respected rather than assumed away.

---

**Model Ledger:** see [Ch. 19 §19.9.1](../CHAPTERS/CHAPTER%2019.md) for the
nine-row ledger on a coupled thermofluid network, and
[Ch. 20 §20.4.1](../CHAPTERS/CHAPTER%2020.md) for the four-way classification
that keeps Darcy's law labelled as constitutive correspondence rather than
mathematical identity — they are *not* the same thing, as Step 3 shows.
