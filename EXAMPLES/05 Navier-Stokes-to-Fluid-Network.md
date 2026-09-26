# Example 5 — Navier–Stokes → Fluid Network

**A complete worked descent in six steps.**

**Source chapters:** [Ch. 13](../CHAPTERS/CHAPTER%2013.md) §13.7 (Newtonian viscosity from Kubo) →
[Ch. 15](../CHAPTERS/CHAPTER%2015.md) §§15.3–15.7 (stress tensor, continuum conservation, ideal and viscous flow, exact solutions) →
[Ch. 16](../CHAPTERS/CHAPTER%2016.md) §16.10 (lumping) →
[Ch. 19](../CHAPTERS/CHAPTER%2019.md) §§19.7.1–19.7.3 (hydraulic effort–flow pair, pipe networks, pump curves) →
[Ch. 20](../CHAPTERS/CHAPTER%2020.md) §20.3 (open-channel hydraulics)

**Question answered:** Pipe-network analysis uses exactly Ohm's law. Under what
conditions is that legitimate, and what does the condition look like numerically?

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
assumption, and a whole lot of real pipe flow is high-Reynolds. The resolution:
inertia can be retained in a lumped form. The momentum equation integrated
along a pipe gives the **Darcy–Weisbach** relation, which keeps inertia:

$$\Delta p = \underbrace{\left(\rho L\,\frac{v^2}{D}\right)}_{\text{inertance, retained}} \cdot \underbrace{f\frac{v^2}{2g\,D}}_{\text{friction}}\ +\ \underbrace{\rho g\,\Delta z}_{\text{gravity}}$$

So the hydraulic network is a **linear-inertial** model, not a linear one: it has
an $L$-like element (inertance $\mathcal{I} = \rho L/A$) whose pressure drop
depends on $v^2$, not $v$. This is the same $\mathcal{I}$ as a mechanical mass,
with the same quadratic nonlinearity. A pipe network is therefore *not* an
electrical circuit, and the distinction is exactly the $I^2R$ term.

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
| Pipe | $R_h = \Delta p/Q$ | resistor | $R_h \propto L/D^4$ laminar, $\propto L/D^5$ turbulent |
| Fitting / valve | $R_h$ | resistor | K-resistance; highly empirical |
| Fluid column | $\Delta p = \rho(L/A)\dot Q^2/2$ | **inductor, nonlinear** | inertance; $I^2R$ analog |
| Expansion vessel / tank | $C = dV/dp$ | capacitor | compressibility storage |
| Pump | pressure source | voltage source | head–flow curve, not an ideal source |

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

**The design finding.** Velocity and head loss scale as $v^2$, so available head
is consumed by flow rate as the *square root* of the driving head. Adding a
second parallel pipe would roughly double $Q$ — not double it, because each pipe
sees a reduced effective head as flow rises. Networks are not linear even
though each element's *resistance* is.

---

## Step 6 — Validity limits

| Assumption | Fails when | Use instead |
|---|---|---|
| Newtonian fluid | non-Newtonian rheology ($n\ne1$) | power-law model; apparent viscosity |
| Incompressible | $M > 0.3$, cavitation | compressible flow; flashing |
| $Re < 2000$, Hagen–Poiseuille | $Re > 2300$ | Colebrook/Moody; $f$ empirical |
| Fully developed | $L/D < 20$, fittings | entrance lengths; $K$-factors |
| **Inertia dropped** | — | **retained as inertance here; dropped only if $Re \ll 1$** |
| Lumped per segment | fittings, valves, short lines | Ch. 15 §15.8.2 — turbulence has no exact closed-form model |
| Single-phase | two-phase, flashing | two-phase flow correlations |
| $f$ constant with $Q$ | varying $Re$ over the operating range | solve network iteratively |

The $f$-versus-$Re$ dependency is worth flagging as an engineering trap: because
$f \propto Re^{-0.2}$ in turbulent flow, the head loss goes as $Q^{1.8}$, not
$Q^2$. A pump curve intersecting a system curve needs a numerical solution, not
algebra, and treating $f$ as constant is a common source of wrong answers.

**What this example demonstrates.** Ohm's law for pipes is genuinely the same
algebra, and it comes from the same conservation laws. But the *network* is
nonlinear through the inertial term, and one constitutive coefficient ($f$) is
empirical. Pipe-network analysis is circuit theory with a memory and a
curve-fit — close enough that the analogy is productive, different enough that
it must be bounded.

---

**Model Ledger:** see [Ch. 19 §19.9.1](../CHAPTERS/CHAPTER%2019.md) for the
nine-row ledger on a coupled thermofluid network, and
[Ch. 20 §20.4.1](../CHAPTERS/CHAPTER%2020.md) for the four-way classification
that keeps Darcy's law labelled as constitutive correspondence rather than
mathematical identity — they are *not* the same thing, as Step 3 shows.
