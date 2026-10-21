# Appendix D — Statistical Mechanics and Linear Response: Ensembles, Quantum Statistics, Kubo, Green–Kubo

This appendix proves the statistical-mechanical results that [Ch. 10](../CHAPTERS/CHAPTER%2010.md) states, and the linear-response results that [Ch. 13](../CHAPTERS/CHAPTER%2013.md) sketches and [Ch. 14](../CHAPTERS/CHAPTER%2014.md) uses in engineering form. The first half (§D.1–§D.8) covers Bridge B.b: the canonical ensemble derived from a reservoir, thermodynamics from the partition function, equipartition and where it fails, the Fermi–Dirac and Bose–Einstein distributions, the classical limit, the Planck and Debye laws, and the Sommerfeld expansion. The second half (§D.9–§D.15) covers Bridge B.e: the Kubo formula derived from first-order perturbation theory, the fluctuation–dissipation theorem, the Green–Kubo expressions, the Drude conductivity under a relaxation-time closure, the Einstein and Wiedemann–Franz relations, and Onsager reciprocity under microscopic reversibility.

The appendix keeps one distinction in view throughout, as Ch. 13 §13.2.2 does. The Kubo formula is an exact statement *within linear response*. Each transport coefficient obtained from it ($\sigma$, $\kappa$, $D$, $\eta$) additionally needs a choice of operators, an order of limits, and in practice a closure such as a relaxation time. These laws are constitutive transport coefficients within appropriate linear-response regimes. No single calculation produces all of them.

Conventions follow Ch. 10 and Ch. 13. $\beta = 1/k_BT$. Electrons carry charge $-e$ with $e > 0$. The spin degeneracy is $g_s$ (equal to 2 for electrons). Fourier transforms are $\tilde X(\omega) = \int X(t)\,e^{i\omega t}\,dt$, so the Drude form is $1/(1 - i\omega\tau)$. $\hat J$ is a total current, and $\hat j = \hat J/V$ is a current density (Ch. 13 §13.4.1).

---

## D.1 — From the Microcanonical to the Canonical Ensemble

Ch. 10 §10.3 obtains $\hat\rho = e^{-\beta\hat H}/Z$ by maximising entropy at fixed mean energy. Here the same result is derived from a different starting point: a small system in contact with a large reservoir. The two routes agree; they rest on different postulates.

### D.1.1 — Assumptions

1. **Isolation.** System $S$ and reservoir $R$ together are isolated, with total energy in a narrow shell $[E_{tot}, E_{tot} + \delta E]$.
2. **Weak coupling.** $\hat H = \hat H_S + \hat H_R + \hat H_{int}$, where $\hat H_{int}$ is strong enough to let energy flow between $S$ and $R$ but contributes negligibly to the energy itself. Each joint state then has energy $E_n + E_R$.
3. **Equal a priori probabilities.** Every joint microstate in the shell is equally likely. This is the microcanonical postulate. It is not derived here.
4. **Large reservoir.** $R$ has many more degrees of freedom than $S$, so that the energies $E_n$ of $S$ that are actually occupied satisfy $E_n \ll E_{tot}$.

### D.1.2 — Derivation

Let $\Omega_R(E)$ be the number of reservoir states in the shell at energy $E$. By assumption 3, the probability that $S$ is in its state $n$ is proportional to the number of reservoir states compatible with it:

$$p_n \propto \Omega_R(E_{tot} - E_n) = \exp\!\left[\frac{S_R(E_{tot} - E_n)}{k_B}\right], \qquad S_R \equiv k_B\ln\Omega_R .$$

Expand the reservoir entropy about $E_{tot}$:

$$\frac{S_R(E_{tot} - E_n)}{k_B} = \frac{S_R(E_{tot})}{k_B} - \beta E_n + \frac{1}{2}\frac{\partial\beta}{\partial E}E_n^2 + \cdots, \qquad \beta \equiv \frac{1}{k_B}\frac{\partial S_R}{\partial E}\bigg|_{E_{tot}} .$$

The first term is the same for every $n$ and is absorbed into the normalisation.

> `[APPROXIMATION]` Drop the quadratic term. Using $\partial\beta/\partial E = -1/(k_BT^2C_R)$, where $C_R$ is the reservoir heat capacity, the ratio of the quadratic term to the linear one is $E_n/(2TC_R)$. That ratio is of order $N_S/N_R$ for comparable materials, and it vanishes as the reservoir grows.

Normalising what remains gives

$$\boxed{p_n = \frac{e^{-\beta E_n}}{Z}, \qquad Z = \sum_n e^{-\beta E_n} = \mathrm{Tr}\,e^{-\beta\hat H_S}}$$

and $\beta$ is fixed by the reservoir, not by the system. Two systems in contact with the same reservoir therefore share the same $\beta$, which is the statistical form of the zeroth law (Ch. 10 §10.5).

### D.1.3 — Energy fluctuations and the equivalence of ensembles

In the canonical ensemble, $\langle H\rangle = -\partial_\beta\ln Z$ and $\langle H^2\rangle - \langle H\rangle^2 = \partial_\beta^2\ln Z = k_BT^2C_V$. Both $U$ and $C_V$ are extensive, so

$$\frac{\Delta E}{U} = \frac{\sqrt{k_BT^2C_V}}{U} \sim N^{-1/2}.$$

For macroscopic $N$ the canonical energy distribution is therefore sharply peaked, and canonical and microcanonical averages of extensive quantities agree to relative order $N^{-1/2}$.

> `[APPROXIMATION]` The equivalence of ensembles holds in the thermodynamic limit ($N, V \to \infty$ at fixed $N/V$). It requires $\ln Z$ to be extensive, which needs short-range interactions, or Coulomb interactions with screening and stability. For the Coulomb case see Lieb and Lebowitz, *Adv. Math.* **9**, 316 (1972), and for the general theory Ruelle, *Statistical Mechanics: Rigorous Results* (1969).

Equivalence fails at first-order phase transitions (where the energy distribution is bimodal), for self-gravitating systems (where $C_V$ can be negative in the microcanonical ensemble), and for small systems.

The thermodynamic limit is not the continuum limit. Taking $N \to \infty$ makes fluctuations of extensive quantities negligible. It does not produce smooth fields; that needs coarse-graining with $\ell_{micro} \ll L$ (Ch. 11).

**What was proved.** If equal a priori probabilities hold for the combined system and the reservoir is much larger than the system, the system's states are Boltzmann distributed, with corrections of relative order $E_n/(TC_R)$. The derivation fails for strongly coupled system–reservoir pairs, where $\hat H_{int}$ is not negligible and the system's own Hamiltonian is no longer well defined.

---

## D.2 — Thermodynamic Potentials from the Partition Function

**Assumptions.** The canonical distribution of §D.1. Energy levels $E_n(V)$ depend on an external parameter (here the volume $V$).

**Internal energy and entropy.**

$$U = \sum_np_nE_n = -\frac{\partial\ln Z}{\partial\beta}, \qquad S = -k_B\sum_np_n\ln p_n = k_B\left(\ln Z + \beta U\right),$$

where the second form uses $\ln p_n = -\beta E_n - \ln Z$.

**Free energy.** $F \equiv U - TS = -k_BT\ln Z$.

**First law, with heat and work separated.** Write $dU = \sum_nE_n\,dp_n + \sum_np_n\,dE_n$. The first sum is the heat term. Using $\sum_n dp_n = 0$,

$$dS = -k_B\sum_n dp_n\ln p_n = k_B\beta\sum_nE_n\,dp_n \quad\Longrightarrow\quad \sum_nE_n\,dp_n = T\,dS .$$

The second sum is the work term. With $dE_n = (\partial E_n/\partial V)\,dV$ it equals $-P\,dV$, where

$$P \equiv -\left\langle\frac{\partial\hat H}{\partial V}\right\rangle = k_BT\frac{\partial\ln Z}{\partial V}\bigg|_T .$$

Hence $dU = T\,dS - P\,dV$ and $dF = -S\,dT - P\,dV$. This reproduces every entry of Ch. 10 §10.4, and $S = -\partial F/\partial T|_V$ follows directly.

> `[DERIVATION]` These identities are exact for the canonical ensemble. Identifying them with the macroscopic $T$, $S$ and $P$ of thermodynamics requires the thermodynamic limit of §D.1.3. Statistical mechanics supplies the microscopic interpretation; the four laws carry separate content and assumptions (Ch. 10 §10.5).

**Grand canonical analogue.** If the reservoir also exchanges particles, the same expansion as in §D.1.2 applied to $S_R(E_{tot} - E, N_{tot} - N)$ gives

$$p \propto e^{-\beta(E - \mu N)}, \qquad \mu \equiv -T\frac{\partial S_R}{\partial N}\bigg|_E, \qquad \Xi = \mathrm{Tr}\,e^{-\beta(\hat H - \mu\hat N)},$$

with $\Omega \equiv -k_BT\ln\Xi = F - \mu N$, $\langle N\rangle = -\partial\Omega/\partial\mu$, and $\Omega = -PV$ for a homogeneous system.

---

## D.3 — Equipartition and Its Failure

### D.3.1 — The generalised equipartition theorem

**Assumptions.**

1. The system is classical: phase-space variables $x_i$ (coordinates and momenta) commute, and the canonical density is $\propto e^{-\beta H(x)}$.
2. Each $x_i$ ranges over the whole real line, or over an interval at whose ends $e^{-\beta H}$ vanishes.

Integrating by parts in $x_j$,

$$\left\langle x_i\frac{\partial H}{\partial x_j}\right\rangle = \frac{1}{Z}\int d\Gamma\;x_i\frac{\partial H}{\partial x_j}e^{-\beta H} = -\frac{1}{\beta Z}\int d\Gamma\;x_i\frac{\partial}{\partial x_j}e^{-\beta H} = \frac{\delta_{ij}}{\beta Z}\int d\Gamma\;e^{-\beta H} = \delta_{ij}k_BT .$$

The boundary terms vanish by assumption 2. For a term $\tfrac12\alpha q^2$ in $H$, choosing $x_i = x_j = q$ gives

$$\left\langle\tfrac12\alpha q^2\right\rangle = \tfrac12k_BT ,$$

which is the statement of Ch. 10 §10.7.2. For a potential $V \propto |q|^s$, the same identity gives $\langle V\rangle = k_BT/s$. So "$\tfrac12k_BT$ per degree of freedom" is specific to quadratic terms.

> `[DERIVATION]` Equipartition is exact in classical statistical mechanics.

### D.3.2 — Failure for quantised modes

For a quantum harmonic oscillator with levels $(n + \tfrac12)\hbar\omega$, the canonical sum is geometric:

$$Z = \frac{e^{-x/2}}{1 - e^{-x}}, \qquad x = \beta\hbar\omega, \qquad \langle E\rangle = \frac{\hbar\omega}{2} + \frac{\hbar\omega}{e^{x} - 1}, \qquad C = k_B\frac{x^2e^x}{(e^x - 1)^2} .$$

**High temperature, $x \ll 1$.** Using $1/(e^x - 1) = 1/x - 1/2 + x/12 + O(x^3)$,

$$\langle E\rangle = k_BT + \frac{(\hbar\omega)^2}{12k_BT} + \cdots$$

This recovers equipartition, the full $k_BT$ for a kinetic plus a potential quadratic term, with a quantum correction of relative size $x^2/12$.

**Low temperature, $x \gg 1$.** $C \simeq k_Bx^2e^{-x}$. The mode is frozen out, as in Ch. 10 §10.7.3.

The classical theorem fails here because the levels are discrete. Assumption 1 is violated: $q$ and $p$ do not commute, and the integral over phase space is not the trace.

> `[APPROXIMATION]` The small parameter is $\hbar\omega/k_BT$. For a general system, the classical partition function $Z_{cl} = (N!\,h^{3N})^{-1}\int d\Gamma\,e^{-\beta H}$ is the leading term of an expansion in $\hbar$. Its first correction is $F = F_{cl} + \frac{\hbar^2\beta^2}{24}\sum_i\frac{\langle(\nabla_iV)^2\rangle_{cl}}{m_i} + O(\hbar^4)$, the Wigner–Kirkwood expansion (Landau and Lifshitz, *Statistical Physics, Part 1*, §33). The classical result requires the thermal wavelength to be small compared with the scale on which $V$ varies.

**What was proved.** Equipartition is exact for quadratic terms in classical statistics. It is the high-temperature limit of the quantum result, and it fails for any mode with $\hbar\omega \gtrsim k_BT$.

---

## D.4 — Fermi–Dirac and Bose–Einstein from the Grand Canonical Ensemble

### D.4.1 — Assumptions

1. Grand canonical ensemble (§D.2).
2. Non-interacting particles: $\hat H = \sum_j\varepsilon_j\hat n_j$ and $\hat N = \sum_j\hat n_j$ in a basis of single-particle states $j$.
3. Occupation numbers: $n_j \in \{0, 1\}$ for fermions, and $n_j \in \{0, 1, 2, \dots\}$ for bosons.

The fermion restriction is not an extra postulate here. It follows from the anticommutation $\{\hat c_j, \hat c_j^\dagger\} = 1$, $\hat c_j^2 = 0$ (Ch. 0; Ch. 5), which gives $\hat n_j^2 = \hat n_j$.

### D.4.2 — Factorisation and the distributions

Because $\hat H - \mu\hat N = \sum_j(\varepsilon_j - \mu)\hat n_j$ is a sum of commuting single-mode terms, the grand partition function factorises over modes:

$$\Xi = \prod_j\xi_j, \qquad \xi_j = \sum_{n}e^{-\beta(\varepsilon_j - \mu)n} .$$

**Fermions.**

$$\xi_j = 1 + e^{-\beta(\varepsilon_j - \mu)}, \qquad \bar n_j = -\frac{1}{\beta}\frac{\partial\ln\xi_j}{\partial\varepsilon_j} = \frac{1}{e^{\beta(\varepsilon_j - \mu)} + 1} .$$

**Bosons.** The geometric series converges only if $\mu < \varepsilon_j$ for every $j$, that is, $\mu < \varepsilon_{min}$. Then

$$\xi_j = \frac{1}{1 - e^{-\beta(\varepsilon_j - \mu)}}, \qquad \bar n_j = \frac{1}{e^{\beta(\varepsilon_j - \mu)} - 1} .$$

These are the boxed results of Ch. 10 §10.8.2.

> `[DERIVATION]` Given non-interacting modes and the grand canonical ensemble, the derivation is exact. In an interacting system the same functions describe quasiparticles only approximately; that is Fermi-liquid theory, which is not derived here.

### D.4.3 — Fluctuations and the grand potential

Differentiating once more,

$$\langle\delta n_j^2\rangle = -\frac{1}{\beta}\frac{\partial\bar n_j}{\partial\varepsilon_j} = \bar n_j(1 \mp \bar n_j),$$

with the upper sign for fermions and the lower for bosons. Fermion occupation fluctuations are suppressed relative to Poisson, which is the origin of sub-Poissonian shot noise in Ch. 13 §13.3.3; boson fluctuations are enhanced. Occupations of different modes are statistically independent: $\langle n_jn_{j'}\rangle = \bar n_j\bar n_{j'}$ for $j \neq j'$. This fact is used in §D.12.

The grand potential is $\Omega = \mp k_BT\sum_j\ln\!\left(1 \pm e^{-\beta(\varepsilon_j - \mu)}\right)$, again with the upper sign for fermions.

**Photons, $\mu = 0$.** Photon number is not conserved: the dynamics does not commute with $\hat N$. There is then no reservoir variable conjugate to $N$, and at fixed $T$ and $V$ the equilibrium value of $N$ minimises $F$, so $\partial F/\partial N = \mu = 0$. The same holds for phonons.

**What was proved.** The Fermi–Dirac and Bose–Einstein distributions follow exactly for ideal quantum gases in the grand canonical ensemble. They fail as exact statements once interactions are present.

---

## D.5 — The Classical (Maxwell–Boltzmann) Limit and $n\lambda^3 \ll 1$

### D.5.1 — The condition

Both quantum distributions reduce to $\bar n \simeq e^{-\beta(\varepsilon - \mu)}$ when $e^{\beta(\varepsilon - \mu)} \gg 1$ for every occupied state. Since $\varepsilon \geq 0$, this requires the fugacity to be small: $z \equiv e^{\beta\mu} \ll 1$.

To relate $z$ to the density, take an ideal gas in a box with $\varepsilon = \hbar^2k^2/2m$ and degeneracy $g_s$:

$$n = g_s\int\frac{d^3k}{(2\pi)^3}\frac{1}{z^{-1}e^{\beta\varepsilon} \pm 1} = \frac{g_s}{\lambda_{th}^3}\left(z \mp \frac{z^2}{2^{3/2}} + \cdots\right), \qquad \lambda_{th} = \frac{h}{\sqrt{2\pi mk_BT}} .$$

The first term uses $\int\frac{d^3k}{(2\pi)^3}e^{-\beta\hbar^2k^2/2m} = (mk_BT/2\pi\hbar^2)^{3/2} = \lambda_{th}^{-3}$. To leading order, then, $z = n\lambda_{th}^3/g_s$, and

$$\boxed{z \ll 1 \quad\Longleftrightarrow\quad \frac{n\lambda_{th}^3}{g_s} \ll 1}$$

This is the criterion of Ch. 10 §10.7.1 and §10.8.2: the mean interparticle spacing $n^{-1/3}$ is large compared with $\lambda_{th}$.

### D.5.2 — First quantum correction

The pressure is $P/k_BT = (g_s/\lambda_{th}^3)(z \mp z^2/2^{5/2} + \cdots)$. Eliminating $z$ with $y \equiv n\lambda_{th}^3/g_s$ and $z = y \pm y^2/2^{3/2} + O(y^3)$ gives

$$P = nk_BT\left(1 \pm \frac{n\lambda_{th}^3}{2^{5/2}g_s} + \cdots\right).$$

The upper sign is for fermions. Fermi statistics acts like an effective repulsion, and Bose statistics like an effective attraction.

### D.5.3 — Numbers

| System | $n$ (m⁻³) | $\lambda_{th}$ at 300 K | $n\lambda_{th}^3$ | Regime |
|---|---|---|---|---|
| N₂ gas at 1 atm | $2.5\times10^{25}$ | $1.9\times10^{-11}$ m | $\sim2\times10^{-7}$ | classical |
| Conduction electrons in Cu | $8.5\times10^{28}$ | $4.3\times10^{-9}$ m | $\sim7\times10^{3}$ | degenerate |

**The Gibbs factor emerges.** In the regime $z \ll 1$, multiply occupied states are negligible. The quantum partition function then reduces to $Z = Z_1^N/N!$, so the Gibbs correction of Ch. 10 §10.7.1 is a *consequence* of quantum indistinguishability in this limit, not an extra rule.

> `[APPROXIMATION]` The small parameter is $n\lambda_{th}^3/g_s$. The approximation fails for degenerate electrons, for liquid helium, and for cold atomic gases near Bose–Einstein condensation, which for bosons occurs at $n\lambda_{th}^3 = \zeta(3/2) \approx 2.612$ per spin state.

---

## D.6 — Planck's Law from Mode Counting

**Assumptions.**

1. Electromagnetic radiation in a cavity of volume $V$, in equilibrium with the walls at temperature $T$.
2. The field is a set of independent harmonic modes. This is exact for the free Maxwell field.
3. Two polarisations per wavevector.
4. Each mode is occupied with the Bose–Einstein distribution at $\mu = 0$ (§D.4.3).

**Counting modes.** With periodic boundary conditions, $\mathbf{k} = 2\pi\mathbf{n}/L$, so each mode occupies a volume $(2\pi)^3/V$ in $k$-space. The number of modes with angular frequency in $[\omega, \omega + d\omega]$, using $\omega = ck$, is

$$dN_{modes} = 2\cdot\frac{V\,4\pi k^2\,dk}{(2\pi)^3} = \frac{V\omega^2}{\pi^2c^3}\,d\omega .$$

The large-volume mode density does not depend on the cavity shape or the boundary conditions. That is Weyl's law; see Courant and Hilbert, *Methods of Mathematical Physics*, Vol. 1, Ch. VI.

**Energy density.** Multiplying by the mean thermal energy per mode,

$$u(\omega, T)\,d\omega = \frac{\hbar\omega^3}{\pi^2c^3}\frac{d\omega}{e^{\beta\hbar\omega} - 1} .$$

The zero-point energy $\tfrac12\hbar\omega$ per mode has been dropped. It is $T$-independent and does not appear in thermal emission; its differences between geometries are the Casimir effect. Converting with $\omega = 2\pi\nu$ and $d\omega = 2\pi\,d\nu$ gives $\hbar(2\pi)^4\nu^3/\pi^2c^3 = 8\pi h\nu^3/c^3$, so

$$u(\nu, T) = \frac{8\pi h\nu^3}{c^3}\frac{1}{e^{h\nu/k_BT} - 1},$$

which is the boxed result of Ch. 10 §10.8.4.

> `[DERIVATION]` Given the assumptions, Planck's law is exact. Real emitters depart from it through emissivity below 1 and through finite size, when the cavity is no longer much larger than the thermal wavelength $hc/k_BT$.

**Integrals.**

- Using $\int_0^\infty x^3/(e^x - 1)\,dx = \pi^4/15$, the total energy density is $U/V = \pi^2k_B^4T^4/(15\hbar^3c^3)$.
- The flux through a hole is $j = cU/4V = \sigma T^4$ with $\sigma = \pi^2k_B^4/(60\hbar^3c^2) = 2\pi^5k_B^4/(15h^3c^2)$.

**Peaks.** The peak depends on the variable used.

- Maximising $u(\nu)$ gives $x = 3(1 - e^{-x})$, so $h\nu_{max} = 2.821\,k_BT$.
- Maximising the per-wavelength density $u_\lambda$ gives $x = 5(1 - e^{-x})$, so $hc/\lambda_{max} = 4.965\,k_BT$ and $\lambda_{max}T = 2.898\times10^{-3}$ m·K.

These are different statements, since $\lambda_{max} \neq c/\nu_{max}$. Ch. 10 §10.8.4 quotes them together.

---

## D.7 — Debye Heat Capacity and the $T^3$ Law

**Assumptions.**

1. A harmonic crystal of $N$ atoms in a monatomic Bravais lattice, with $3N$ normal modes (Ch. 6 §6.7.1; Ch. 9 §9.8.4).
2. Each mode is an independent quantum oscillator (§D.3.2).
3. The Debye model:
   - `[APPROXIMATION]` Replace the true dispersion by $\omega = v_sk$ for all three acoustic branches, with an averaged speed $3/v_s^3 = 1/v_L^3 + 2/v_T^3$.
   - Cut the spectrum off at $\omega_D$, chosen so that the total number of modes is $3N$.

**Density of states.** Counting as in §D.6 with three branches, $g(\omega) = 3V\omega^2/2\pi^2v_s^3$. The cutoff condition $\int_0^{\omega_D}g\,d\omega = 3N$ gives $\omega_D^3 = 6\pi^2(N/V)v_s^3$, and therefore

$$g(\omega) = \frac{9N\omega^2}{\omega_D^3} .$$

**Heat capacity.** Each mode contributes the oscillator heat capacity of §D.3.2. With $x = \beta\hbar\omega$ and $T_D = \hbar\omega_D/k_B$,

$$C_V = \int_0^{\omega_D}g(\omega)\,k_B\frac{x^2e^x}{(e^x - 1)^2}\,d\omega = 9Nk_B\left(\frac{T}{T_D}\right)^3\int_0^{T_D/T}\frac{x^4e^x}{(e^x - 1)^2}\,dx,$$

which is the result of Ch. 10 §10.7.3.

**High-temperature limit.** For $T \gg T_D$, the integrand is $\simeq x^2$, the integral is $\tfrac13(T_D/T)^3$, and $C_V \to 3Nk_B$ (Dulong–Petit).

**Low-temperature limit.** For $T \ll T_D$, extend the upper limit to infinity. Integration by parts gives

$$\int_0^\infty\frac{x^4e^x}{(e^x - 1)^2}\,dx = \left[-\frac{x^4}{e^x - 1}\right]_0^\infty + 4\int_0^\infty\frac{x^3}{e^x - 1}\,dx = \frac{4\pi^4}{15},$$

and hence

$$\boxed{C_V \simeq \frac{12\pi^4}{5}Nk_B\left(\frac{T}{T_D}\right)^3, \qquad T \ll T_D}$$

**What is robust and what is model.** At $T \ll T_D$ only modes with $\hbar\omega \lesssim k_BT$ are excited. Those are long-wavelength acoustic phonons, for which linear dispersion is asymptotically exact. The $T^3$ law therefore does not depend on the cutoff or on the details of the dispersion: its coefficient involves only the sound speeds. The interpolation between the two limits is the model.

> `[APPROXIMATION]` The small parameter for the $T^3$ law is $T/T_D$, more precisely $k_BT$ compared with the energy at which the dispersion departs from linear. Debye fails at intermediate $T$ wherever the real $g(\omega)$ has van Hove structure or optical branches. In amorphous solids an additional low-$T$ contribution appears that is not phononic.

---

## D.8 — The Sommerfeld Expansion and $C_{el} \propto T$

### D.8.1 — The expansion

**Assumptions.**

1. $H(\varepsilon)$ is smooth near $\mu$ on the scale of $k_BT$.
2. $H(\varepsilon)$ vanishes for $\varepsilon < 0$ (the band bottom) and grows at most polynomially.
3. The system is degenerate: $k_BT \ll \mu$.

Let $f$ be the Fermi function and $K(\varepsilon) = \int_0^\varepsilon H\,d\varepsilon'$. Integration by parts gives

$$I = \int_0^\infty H(\varepsilon)f(\varepsilon)\,d\varepsilon = \int_0^\infty K(\varepsilon)\left(-\frac{\partial f}{\partial\varepsilon}\right)d\varepsilon .$$

The function $-\partial f/\partial\varepsilon$ is even in $\varepsilon - \mu$, integrates to 1, and has width of order $k_BT$. Expand $K$ about $\mu$ and extend the lower limit to $-\infty$, at a cost of order $e^{-\beta\mu}$. The odd moments vanish. The second moment is

$$\int_{-\infty}^\infty y^2\frac{e^y}{(e^y + 1)^2}\,dy = 4\int_0^\infty\frac{y}{e^y + 1}\,dy = 4\cdot\frac{\pi^2}{12} = \frac{\pi^2}{3} .$$

Therefore

$$\boxed{\int_0^\infty H(\varepsilon)f(\varepsilon)\,d\varepsilon = \int_0^\mu H(\varepsilon)\,d\varepsilon + \frac{\pi^2}{6}(k_BT)^2H'(\mu) + O\!\left((k_BT)^4H'''\right)}$$

The expansion is asymptotic, not convergent: it misses terms of order $e^{-\beta\mu}$.

### D.8.2 — Chemical potential and heat capacity

Let $g(\varepsilon)$ be the density of states per unit volume including spin, and $n$ the electron density.

**Chemical potential.** Fixed $n = \int g f\,d\varepsilon$ requires $0 = (\mu - E_F)g(E_F) + \frac{\pi^2}{6}(k_BT)^2g'(E_F)$, so

$$\mu = E_F - \frac{\pi^2}{6}(k_BT)^2\frac{g'(E_F)}{g(E_F)} .$$

**Energy.** $u = \int\varepsilon g f\,d\varepsilon = u_0 + E_Fg(E_F)(\mu - E_F) + \frac{\pi^2}{6}(k_BT)^2\left[g(E_F) + E_Fg'(E_F)\right]$. Substituting $\mu - E_F$ cancels the $g'$ terms, leaving

$$u = u_0 + \frac{\pi^2}{6}(k_BT)^2g(E_F), \qquad \boxed{c_{el} = \frac{\partial u}{\partial T} = \frac{\pi^2}{3}k_B^2T\,g(E_F)}$$

**Free electrons.** Here $g(E_F) = 3n/2E_F$. Multiplying by $V$ for $N$ electrons, $C_{el} = \frac{\pi^2}{2}Nk_B\,T/T_F$, which is the Ch. 10 §10.8.3 result. In this case $g'/g = 1/2E_F$, so $\mu = E_F[1 - \frac{\pi^2}{12}(k_BT/E_F)^2]$.

> `[APPROXIMATION]` The small parameter is $k_BT/E_F$, about $4\times10^{-3}$ for Cu at 300 K. The expansion fails when $g(\varepsilon)$ has structure on the scale of $k_BT$ (van Hove singularities, narrow $d$ or $f$ bands, band edges), in non-degenerate semiconductors, and as $T \to T_F$.

---

## D.9 — The Kubo Formula from First-Order Perturbation Theory

### D.9.1 — Assumptions

1. **Equilibrium in the past.** The unperturbed system is in equilibrium in the distant past: $\hat\rho(-\infty) = \hat\rho_0 = e^{-\beta\hat H_0}/Z$.
2. **Weak coupling to one classical field.** A perturbation $\hat H(t) = \hat H_0 - \hat A\,F(t)$ acts, with $F$ a classical c-number field (as in Ch. 13 §13.1.1) switched on adiabatically, $F(t) \propto e^{\eta t}$ with $\eta \to 0^+$.
3. **Linearity.** Only the response linear in $F$ is kept.

> `[APPROXIMATION]` The small parameter is the ratio of the field-induced change in the state to the equilibrium state over the time window of interest. It is not simply "$F$ small". Absorbed energy heats the system at second order in $F$, so a truly steady dissipative state also requires coupling to a bath, or a limit in which $V \to \infty$ is taken before $t \to \infty$. This is the substance of van Kampen's objection to linear response (*Physica Norvegica* **5**, 279 (1971)). The standard answer is that the linear coefficient is well defined in these limits, even if the microscopic trajectories respond nonlinearly.

### D.9.2 — Derivation

The von Neumann equation (Ch. 10 §10.1.2) is $i\hbar\,\partial_t\hat\rho = [\hat H(t), \hat\rho]$. In the interaction picture,

$$\hat\rho_I(t) = e^{i\hat H_0t/\hbar}\,\hat\rho(t)\,e^{-i\hat H_0t/\hbar}, \qquad \hat X_I(t) = e^{i\hat H_0t/\hbar}\,\hat X\,e^{-i\hat H_0t/\hbar},$$

the equation becomes $i\hbar\,\partial_t\hat\rho_I = [\hat H'_I(t), \hat\rho_I]$ with $\hat H'_I = -\hat A_I(t)F(t)$. Note that $\hat\rho_0$ is stationary, since it commutes with $\hat H_0$. Integrating once, and keeping only first order in $F$:

$$\hat\rho_I(t) = \hat\rho_0 + \frac{1}{i\hbar}\int_{-\infty}^t[\hat H'_I(t'), \hat\rho_0]\,dt' + O(F^2) = \hat\rho_0 + \frac{i}{\hbar}\int_{-\infty}^t F(t')\,[\hat A_I(t'), \hat\rho_0]\,dt' + O(F^2).$$

The response of an observable $\hat B$ is $\langle\hat B\rangle(t) = \mathrm{Tr}[\hat\rho(t)\hat B] = \mathrm{Tr}[\hat\rho_I(t)\hat B_I(t)]$. Use the cyclic identity

$$\mathrm{Tr}\big([\hat X, \hat\rho_0]\hat Y\big) = \mathrm{Tr}\big(\hat\rho_0[\hat Y, \hat X]\big).$$

Then

$$\delta\langle\hat B\rangle(t) = \int_{-\infty}^{\infty}\chi_{BA}(t - t')\,F(t')\,dt', \qquad \boxed{\chi_{BA}(t) = \frac{i}{\hbar}\,\Theta(t)\,\big\langle[\hat B_I(t), \hat A_I(0)]\big\rangle_0}$$

The response depends only on $t - t'$ because $\hat\rho_0$ is stationary.

> `[DERIVATION]` This is the result of Ch. 13 §13.1.2, exact to first order in $F$.

**Sign check.** For a perturbation written $\hat H'$, the first-order correction is $\delta\hat\rho_I = -(i/\hbar)\int[\hat H'_I, \hat\rho_0]\,dt'$. Ch. 13 §13.2.1 writes it with $+i/\hbar$. That sign is right only after substituting $\hat H' = -\hat AF$; its final $\chi_{BA}$ is correct.

**Causality.** The factor $\Theta(t)$ makes $\tilde\chi(\omega) = \int_0^\infty\chi(t)\,e^{i\omega t - \eta t}\,dt$ analytic in the upper half of the complex $\omega$ plane. That analyticity gives the Kramers–Kronig relations between $\tilde\chi'$ and $\tilde\chi''$, where $\tilde\chi = \tilde\chi' + i\tilde\chi''$.

### D.9.3 — The Kubo canonical form

For many applications it is useful to rewrite $\chi$ in terms of the time derivative of $\hat A$.

**Kubo identity.** Define $G(\beta) = e^{\beta\hat H_0}[\hat A, e^{-\beta\hat H_0}]$. Then $G(0) = 0$ and $dG/d\beta = e^{\beta\hat H_0}[\hat H_0, \hat A]e^{-\beta\hat H_0}$. Integrating, and using $[\hat H_0, \hat A] = -i\hbar\dot{\hat A}$ with $e^{\lambda\hat H_0}\dot{\hat A}e^{-\lambda\hat H_0} = \dot{\hat A}(-i\hbar\lambda)$,

$$[\hat A, \hat\rho_0] = -i\hbar\,\hat\rho_0\int_0^\beta\dot{\hat A}(-i\hbar\lambda)\,d\lambda .$$

Substituting into $\langle[\hat B(t), \hat A]\rangle_0 = \mathrm{Tr}([\hat A, \hat\rho_0]\hat B(t))$ gives

$$\chi_{BA}(t) = \Theta(t)\int_0^\beta\big\langle\dot{\hat A}(-i\hbar\lambda)\,\hat B(t)\big\rangle_0\,d\lambda \;\xrightarrow{\;\hbar\to0\;}\; \beta\,\Theta(t)\,\big\langle\dot A(0)\,B(t)\big\rangle_0 .$$

The classical limit on the right is the same result that one obtains by linearising the classical Liouville equation directly.

**What was proved.** To first order in a weak classical field, the response is the retarded commutator in the equilibrium state. Equivalently it is the Kubo canonical correlation of $\dot{\hat A}$ with $\hat B$, whose classical limit is $\beta\langle\dot AB(t)\rangle$. Nothing in this derivation specifies a transport law. It specifies how to compute one, once $\hat A$ and $\hat B$ are chosen.

---

## D.10 — The Fluctuation–Dissipation Theorem

### D.10.1 — Classical limit

**Assumptions.** Classical commuting variables, the classical Kubo form of §D.9.3 with $B = A$, and $\langle A\rangle_0 = 0$.

Let $C(t) = \langle A(0)A(t)\rangle_0$. Stationarity gives $\frac{d}{ds}\langle A(s)A(t + s)\rangle = 0$, hence $\langle\dot A(0)A(t)\rangle = -\dot C(t)$, and so

$$\chi_{AA}(t) = -\beta\,\Theta(t)\,\dot C(t) .$$

Classically $C(t)$ is real and even, so $\dot C$ is odd. Therefore

$$\tilde\chi''(\omega) = -\beta\int_0^\infty\dot C\sin\omega t\,dt = -\frac{\beta}{2}\int_{-\infty}^\infty\dot C\sin\omega t\,dt = \frac{\beta\omega}{2}\int_{-\infty}^\infty C(t)\cos\omega t\,dt,$$

after integrating by parts. That is,

$$\boxed{\tilde\chi''_{AA}(\omega) = \frac{\omega}{2k_BT}\,S_A(\omega), \qquad S_A(\omega) = \int_{-\infty}^\infty C(t)\,e^{i\omega t}\,dt}$$

which is the classical boxed formula of Ch. 13 §13.3.1.

**Static limit.** At $\omega = 0$, $\tilde\chi_{AA}(0) = -\beta\int_0^\infty\dot C\,dt = \beta[C(0) - C(\infty)] = \beta\langle\delta A^2\rangle$. A static susceptibility equals $\beta$ times an equilibrium variance. The heat-capacity formula of Ch. 10 §10.4 has this structure.

### D.10.2 — Why $\tilde\chi''$ is dissipation

Under $F = F_0\cos\omega t$, the power absorbed is $\langle d\hat H/dt\rangle = -\langle\hat A\rangle\dot F$. Averaged over a period, only the out-of-phase part of $\langle\hat A\rangle$ survives:

$$\bar P = \frac{\omega F_0^2}{2}\,\tilde\chi''(\omega).$$

Passivity of an equilibrium state requires $\bar P \geq 0$. That is guaranteed by the spectral representation below.

### D.10.3 — Quantum form, with the operator ordering explicit

Define the two orderings

$$S_>(\omega) = \int_{-\infty}^\infty\langle\hat A(t)\hat A(0)\rangle_0\,e^{i\omega t}\,dt, \qquad S_<(\omega) = \int_{-\infty}^\infty\langle\hat A(0)\hat A(t)\rangle_0\,e^{i\omega t}\,dt = S_>(-\omega).$$

The equilibrium state satisfies the KMS condition $\langle\hat A(t)\hat B\rangle_0 = \langle\hat B\hat A(t + i\hbar\beta)\rangle_0$. Shifting the contour by $i\hbar\beta$ gives the detailed-balance relation

$$S_>(-\omega) = e^{-\beta\hbar\omega}S_>(\omega).$$

From §D.9.2, $\tilde\chi''(\omega) = \frac{1}{2\hbar}\int\langle[\hat A(t), \hat A(0)]\rangle e^{i\omega t}\,dt = \frac{1}{2\hbar}\big[S_>(\omega) - S_>(-\omega)\big]$. Therefore

$$\tilde\chi''_{AA}(\omega) = \frac{1 - e^{-\beta\hbar\omega}}{2\hbar}\,S_>(\omega) = \frac{e^{\beta\hbar\omega} - 1}{2\hbar}\,S_<(\omega).$$

The spectral form $S_>(\omega) = 2\pi\sum_{nm}p_n|A_{nm}|^2\,\delta\big(\omega - (E_m - E_n)/\hbar\big) \geq 0$ shows that $\tilde\chi''(\omega) \geq 0$ for $\omega > 0$, as passivity requires.

**Ordering note.** Ch. 13 §13.3.1 defines $S_A$ with the ordering $\langle\hat A(0)\hat A(t)\rangle$, which is $S_<$ here. Its prefactor $(1 - e^{-\beta\hbar\omega})/2\hbar$ and its detailed-balance relation $S_A(-\omega) = e^{-\beta\hbar\omega}S_A(\omega)$ hold for the opposite ordering, $S_>$, with the $e^{+i\omega t}$ convention. All orderings agree in the classical limit $\beta\hbar\omega \to 0$, and the symmetrised $\coth$ form quoted there is unaffected. See Kubo, *Rep. Prog. Phys.* **29**, 255 (1966), and Callen and Welton, *Phys. Rev.* **83**, 34 (1951).

> `[DERIVATION]` Given equilibrium (KMS) and linear response, the FDT is exact. The classical form is the limit $\hbar\omega \ll k_BT$. The FDT does not hold in non-equilibrium steady states, such as driven or aging systems, where violations of it are a diagnostic.

---

## D.11 — Green–Kubo Expressions: Diffusion and Conductivity

### D.11.1 — Diffusion from the velocity autocorrelation

**Assumptions.**

1. A tagged particle in an equilibrium, stationary environment.
2. The velocity autocorrelation $C_v(t) = \langle v_x(0)v_x(t)\rangle$ decays fast enough that $\int_0^\infty C_v\,dt$ and $\int_0^\infty t\,C_v\,dt$ converge.
3. At long times and long wavelengths, the tagged-particle density obeys the diffusion equation $\partial_tc = D\nabla^2c$.

Assumption 3 is the hydrodynamic hypothesis, which supplies the definition of $D$.

**From displacement to correlation.** Since $x(t) - x(0) = \int_0^tv_x(s)\,ds$, stationarity gives

$$\langle[x(t) - x(0)]^2\rangle = \int_0^t\!\!\int_0^tC_v(s - s')\,ds\,ds' = 2\int_0^t(t - u)\,C_v(u)\,du \;\xrightarrow{\;t\,\gg\,\tau_c\;}\; 2t\int_0^\infty C_v\,du - 2\int_0^\infty u\,C_v\,du .$$

**From the diffusion equation.** A point source spreading under the diffusion equation has $\langle x^2\rangle = 2Dt$ per Cartesian direction. Matching the coefficients of $t$:

$$\boxed{D = \int_0^\infty\langle v_x(0)v_x(t)\rangle\,dt = \frac13\int_0^\infty\langle\mathbf{v}(0)\cdot\mathbf{v}(t)\rangle\,dt}$$

which is the formula of Ch. 13 §13.6.1.

> `[APPROXIMATION]` The small parameters are $\tau_c/t$, the correlation time compared with the observation time, and $\ell/L$, the microscopic length compared with the length over which the concentration varies. Assumption 2 can fail. In fluids, $C_v$ has a hydrodynamic long-time tail $\propto t^{-d/2}$ (Alder and Wainwright, *Phys. Rev. A* **1**, 18 (1970)). In $d = 3$ the tail is integrable and $D$ exists. In $d = 2$ the integral diverges logarithmically, and a strictly two-dimensional fluid has no finite $D$.

**Example: Langevin dynamics.** For $m\dot v = -mv/\tau + \xi(t)$ with white noise $\xi$ normalised so that $\langle v^2\rangle = k_BT/m$ (equipartition, legitimate for a non-degenerate tracer), $C_v = (k_BT/m)e^{-|t|/\tau}$ and $D = k_BT\tau/m$. This is the example of Ch. 13 §13.6.1.

### D.11.2 — Conductivity

Couple a uniform field to the total dipole: $\hat H' = -\hat{\mathbf{P}}\cdot\mathbf{E}(t)$ with $\hat{\mathbf{P}} = \sum_iq_i\hat{\mathbf{x}}_i$, so that $\dot{\hat{\mathbf{P}}} = \hat{\mathbf{J}}$, the total current. Take the response $\hat j_\alpha = \hat J_\alpha/V$. Then §D.9.3 gives

$$\sigma_{\alpha\beta}(\omega) = \frac1V\int_0^\infty dt\,e^{i\omega t - \eta t}\int_0^\beta d\lambda\,\big\langle\hat J_\beta(-i\hbar\lambda)\,\hat J_\alpha(t)\big\rangle_0 .$$

Two remarks on this expression:

- **Index order.** $\sigma_{\alpha\beta}$ is the response of $j_\alpha$ to $E_\beta$, so the *driven* index $\beta$ sits on the imaginary-time argument. Ch. 13 §13.4.1 places it the other way round. For an isotropic system, or for symmetric $\sigma$, this is immaterial. For the Hall response it is a transposition, $\sigma_{\alpha\beta} \leftrightarrow \sigma_{\beta\alpha}$, which by §D.15 is equivalent to $\mathbf{B} \to -\mathbf{B}$.
- **Dipole coupling.** $\hat{\mathbf{P}}$ is ill-defined under periodic boundary conditions. The careful derivation couples to a vector potential, with $\mathbf{E} = -\partial_t\mathbf{A}$. That produces a paramagnetic current–current term plus a diamagnetic term $ne^2/m$, which combine into the expression above. See Mahan, *Many-Particle Physics*, chapter on linear response.

**DC limit.** In the classical limit, the $\lambda$ integral gives a factor $\beta$. For an isotropic system,

$$\sigma_{DC} = \frac{1}{3Vk_BT}\int_0^\infty\langle\hat{\mathbf{J}}(0)\cdot\hat{\mathbf{J}}(t)\rangle_0\,dt,$$

as in Ch. 13 §13.4.1. Quantum mechanically, the $\lambda$ integral reduces to $\beta$ exactly whenever $\hat J$ commutes with $\hat H_0$ (§D.12). Otherwise it reduces to $\beta$ only in the classical limit, so the statement in Ch. 13 that "the $\omega = 0$ correlator is $\lambda$-independent" should be read as one of these two cases.

**Other coefficients.** The thermal conductivity $\kappa = (Vk_BT^2)^{-1}\int_0^\infty\langle\hat J_Q\hat J_Q(t)\rangle\,dt$ and the viscosity $\eta$ have the same Green–Kubo structure. But $\nabla T$ is not a term in the Hamiltonian, so the derivation of §D.9 does not apply directly. Luttinger's device of a fictitious gravitational potential coupled to the energy density, *Phys. Rev.* **135**, A1505 (1964), or a hydrodynamic regression argument, supplies it. That derivation is out of scope here.

---

## D.12 — The Drude Conductivity under the Relaxation-Time Assumption

### D.12.1 — The exact free-gas correlator

**Assumptions.**

1. Non-interacting electrons with quadratic dispersion $\varepsilon_k = \hbar^2k^2/2m$.
2. The grand canonical ensemble.

Then $\hat J_x = -(e\hbar/m)\sum_k k_x\hat n_k$, where the sum includes spin. This operator commutes with $\hat H_0$, so it is conserved. Hence $\hat J_x(-i\hbar\lambda) = \hat J_x$, and the Kubo correlation reduces to $\beta\langle\hat J_x^2\rangle$.

Using the mode independence of §D.4.3, $\langle n_kn_{k'}\rangle = f_kf_{k'} + \delta_{kk'}f_k(1 - f_k)$. The first term contributes $(\sum_kk_xf_k)^2 = 0$. Then:

- Use $f(1 - f) = -k_BT\,\partial f/\partial\varepsilon$.
- Use $\partial f/\partial k_x = (\hbar^2k_x/m)\,\partial f/\partial\varepsilon$.
- Integrate by parts in $k_x$.

The result is

$$\frac{\beta}{V}\langle\hat J_x^2\rangle = \frac{\beta e^2\hbar^2}{m^2V}\sum_kk_x^2f_k(1 - f_k) = \frac{e^2}{mV}\sum_kf_k = \frac{ne^2}{m} .$$

This holds **at any degeneracy**. The factor $k_BT$ that appears is not equipartition. It comes from $f(1 - f) = -k_BT\,\partial f/\partial\varepsilon$, which converts the sum into a Fermi-surface integral, exactly as in the Boltzmann route of Ch. 13 §13.4.2.

The exact Kubo result for the free gas is therefore

$$\sigma(\omega) = \frac{ne^2}{m}\int_0^\infty e^{i\omega t - \eta t}\,dt = \frac{ne^2}{m}\,\frac{i}{\omega + i\eta},$$

a pure Drude weight, with $\sigma_{DC} = \infty$ as $\eta \to 0$. This agrees with Ch. 13 §13.4.2, obstruction 1.

**Note on the occupation correlator.** Ch. 13 §13.4.2 writes $\langle\hat n_k\hat n_{k'}\rangle_0 = \delta_{kk'}f_k$. For $k \neq k'$ the correct value is $f_kf_{k'}$, and the connected part $\delta_{kk'}f_k(1 - f_k)$ is precisely what enters the current correlator. That chapter's conclusion, that a closure is required, is unaffected.

### D.12.2 — The relaxation-time closure

> `[PHENOMENOLOGICAL]` Assume momentum-relaxing collisions make the current correlator decay as $\langle\hat J_x;\hat J_x(t)\rangle = \langle\hat J_x;\hat J_x\rangle\,e^{-t/\tau}$, with a single $\tau$ and the equal-time value of §D.12.1 unchanged. Here $\langle\,\cdot\,;\,\cdot\,\rangle$ denotes the Kubo canonical correlation of §D.9.3.

Then

$$\boxed{\sigma(\omega) = \frac{ne^2}{m}\int_0^\infty e^{-t/\tau}e^{i\omega t}\,dt = \frac{\sigma_0}{1 - i\omega\tau}, \qquad \sigma_0 = \frac{ne^2\tau}{m}}$$

The Boltzmann route of Ch. 13 §13.4.2 gives the same result with $\partial_t\delta f = -i\omega\,\delta f$ retained, since $(-i\omega + 1/\tau)\,\delta f$ replaces $\delta f/\tau$.

**A check independent of $\tau$.** The real part satisfies

$$\int_0^\infty\mathrm{Re}\,\sigma\,d\omega = \sigma_0\frac{\pi}{2\tau} = \frac{\pi ne^2}{2m}$$

for any $\tau$. This is the f-sum rule. Scattering redistributes spectral weight; it does not create or remove it.

> `[APPROXIMATION]` The closure requires well-defined quasiparticles, $\hbar/\tau \ll E_F$, a momentum-relaxing scattering mechanism, and $\tau$ independent of energy on the scale $k_BT$. It fails for:
> - interband transitions at optical frequencies;
> - the anomalous skin effect, where the mean free path $\ell = v_F\tau$ exceeds the field penetration depth;
> - ballistic samples with $\ell > L$ (Ch. 13 §13.11);
> - strongly correlated metals.
>
> Replacing $m$ by an effective mass $m^*$ is a band-structure correction, not part of the closure.

---

## D.13 — The Einstein Relation

### D.13.1 — From Kubo, for a non-degenerate particle

**Assumptions.** A classical tagged particle, with the perturbation $\hat H' = -xF$ from a constant force $F$. Then $\dot A = \dot x = v$, and the classical form of §D.9.3 gives the drift velocity

$$\langle v\rangle = F\beta\int_0^\infty\langle v(0)v(t)\rangle\,dt = \frac{D}{k_BT}F .$$

The second equality uses §D.11.1. So the force mobility is $\mu_F = \langle v\rangle/F = D/k_BT$. For charge $q$ the electrical mobility is $\mu_{mob} = q\mu_F$, so

$$\boxed{D = \frac{k_BT}{q}\,\mu_{mob}}$$

as in Ch. 13 §13.6.2. The Kubo route makes explicit that this is the FDT applied to one particle: the same correlation function controls both spreading ($D$) and drift ($\mu$).

### D.13.2 — General (degenerate) form

**Assumptions.** Local equilibrium, and a single diffusion constant governing the particle flux $-D\nabla n$.

In equilibrium in an electrostatic potential $\phi$, the electrochemical potential $\mu(n(\mathbf{x})) - e\phi(\mathbf{x})$ is constant. Hence

$$\nabla n = -e\frac{\partial n}{\partial\mu}\mathbf{E} .$$

The electrical current density is the drift term $\sigma\mathbf{E}$ plus the diffusive term $(-e)(-D\nabla n)$, and it must vanish in equilibrium:

$$\mathbf{j} = \sigma\mathbf{E} - e^2D\frac{\partial n}{\partial\mu}\mathbf{E} = 0 \quad\Longrightarrow\quad \boxed{\sigma = e^2\frac{\partial n}{\partial\mu}D}$$

**Limits.**

- **Non-degenerate.** $\partial n/\partial\mu = n/k_BT$, which gives $D = \mu_{mob}k_BT/e$. This is the semiconductor relation used in Ch. 14 §14.5.1, with $V_T = k_BT/e$.
- **Degenerate.** $\partial n/\partial\mu = g(E_F)$, which gives $\sigma = e^2g(E_F)D$ with $D = v_F^2\tau/3$.

For degenerate electrons the factor $k_BT/e$ is replaced by $n/(e\,g(E_F)) = 2E_F/3e$ for free electrons. Using $k_BT/e$ for metals or degenerate semiconductors is an error.

---

## D.14 — Wiedemann–Franz and the Lorenz Number

### D.14.1 — Assumptions

1. Linearised Boltzmann transport with a relaxation time $\tau(\varepsilon)$ that may depend on energy but is the same for charge and heat currents.
2. **Elastic scattering.** This is what makes assumption 1 legitimate: an elastic collision degrades a charge current and a heat current carried by the same electron equally.
3. Isotropy.
4. Degeneracy, $k_BT \ll E_F$, with $\tau(\varepsilon)$, $v(\varepsilon)$ and $g(\varepsilon)$ smooth on the scale $k_BT$.
5. Heat is carried by electrons only; phonon conduction is neglected.

### D.14.2 — Transport integrals

**The distribution.** With a local equilibrium $f_0$ whose $\mu$ and $T$ vary in space, an electric field $\mathbf{E}$, and $\mathbf{F} = -e\mathbf{E}$, the steady linearised Boltzmann equation gives

$$\delta f = \tau(\varepsilon)\left(-\frac{\partial f_0}{\partial\varepsilon}\right)\mathbf{v}\cdot\left[-e\boldsymbol{\mathcal{E}} - (\varepsilon - \mu)\frac{\nabla T}{T}\right], \qquad \boldsymbol{\mathcal{E}} \equiv \mathbf{E} + \frac{\nabla\mu}{e} .$$

This reduces to Ch. 13 §13.4.2 when $\nabla T = \nabla\mu = 0$.

**The integrals.** Define $\sigma(\varepsilon) = e^2\tau(\varepsilon)v(\varepsilon)^2g(\varepsilon)/3$ and

$$\mathcal{L}^{(\alpha)} = \int d\varepsilon\left(-\frac{\partial f_0}{\partial\varepsilon}\right)(\varepsilon - \mu)^\alpha\,\sigma(\varepsilon) .$$

**The currents.** The charge current $\mathbf{j} = -e\int\mathbf{v}\,\delta f$ and the heat current $\mathbf{j}_Q = \int(\varepsilon - \mu)\mathbf{v}\,\delta f$ are then

$$\mathbf{j} = \mathcal{L}^{(0)}\boldsymbol{\mathcal{E}} + \frac{\mathcal{L}^{(1)}}{eT}\nabla T, \qquad \mathbf{j}_Q = -\frac{\mathcal{L}^{(1)}}{e}\boldsymbol{\mathcal{E}} - \frac{\mathcal{L}^{(2)}}{e^2T}\nabla T .$$

**The coefficients.** At $\mathbf{j} = 0$ the field is $\boldsymbol{\mathcal{E}} = S\nabla T$. This gives

$$\sigma = \mathcal{L}^{(0)}, \qquad S = -\frac{\mathcal{L}^{(1)}}{eT\mathcal{L}^{(0)}}, \qquad \kappa = \frac{1}{e^2T}\left[\mathcal{L}^{(2)} - \frac{(\mathcal{L}^{(1)})^2}{\mathcal{L}^{(0)}}\right].$$

### D.14.3 — Sommerfeld evaluation

The moments of $-\partial f_0/\partial\varepsilon$ from §D.8 give

$$\mathcal{L}^{(0)} = \sigma(\mu) + O(T^2), \qquad \mathcal{L}^{(1)} = \frac{\pi^2}{3}(k_BT)^2\sigma'(\mu), \qquad \mathcal{L}^{(2)} = \frac{\pi^2}{3}(k_BT)^2\sigma(\mu).$$

The term $(\mathcal{L}^{(1)})^2/\mathcal{L}^{(0)}$ is $O(T^4)$, so

$$\boxed{\frac{\kappa}{\sigma T} = \frac{\pi^2}{3}\left(\frac{k_B}{e}\right)^2 = 2.443\times10^{-8}\ \mathrm{W\,\Omega\,K^{-2}}}$$

with corrections of relative order $(k_BT/E_F)^2$. This is Ch. 13 §13.5.2. The derivation needs neither parabolic dispersion nor energy-independent $\tau$: $\sigma(\varepsilon)$ is arbitrary as long as it is smooth. What it needs is the *same* $\tau(\varepsilon)$ for both currents, which is assumption 2. Ch. 13 §13.5.2 lists "Galilean-invariant parabolic dispersion" among the requirements, which is stronger than necessary.

> `[APPROXIMATION]` Small parameters: $k_BT/E_F$, and the inelasticity of scattering. Inelastic small-angle electron–phonon scattering at intermediate $T$ relaxes heat currents more efficiently than charge currents, pushing $\kappa/\sigma T$ below $L_0$. This is the regime table of Ch. 13 §13.5.2.

### D.14.4 — By-product: the Mott formula

From the same integrals,

$$S = -\frac{\pi^2k_B^2T}{3e}\frac{\sigma'(\mu)}{\sigma(\mu)} = -\frac{\pi^2k_B^2T}{3eE_F}\left.\frac{d\ln\sigma}{d\ln\varepsilon}\right|_{E_F}.$$

For free electrons $\sigma(\varepsilon) \propto \varepsilon^{3/2}\tau(\varepsilon)$, so $d\ln\sigma/d\ln\varepsilon = 3/2 + d\ln\tau/d\ln\varepsilon$:

- Constant $\tau$ gives $S = -\pi^2k_B^2T/2eE_F$.
- Constant mean free path ($\tau \propto \varepsilon^{-1/2}$) gives $S = -\pi^2k_B^2T/3eE_F$, the form quoted in Ch. 13 §13.9.3.

**Numerical check.** At 300 K with $E_F = 7$ eV, these give $-1.6\,\mu$V/K and $-1.05\,\mu$V/K respectively. The measured thermopower of Cu at room temperature is about $+1.8\,\mu$V/K. The sign is positive because $\sigma'(\mu)/\sigma$ for copper's real Fermi surface and scattering is not the free-electron value. The Mott formula still holds; the free-electron input to it fails. Both the sign and the magnitude quoted in Ch. 13 §13.9.3 should therefore be treated with care.

---

## D.15 — Onsager Reciprocity

### D.15.1 — Statement

Let fluxes $J_i$ and forces $X_i$ be chosen so that the entropy production is $\dot s = \sum_iJ_iX_i$. In the linear regime, $J_i = \sum_jL_{ij}X_j$. Then

$$\boxed{L_{ij}(\mathbf{B}) = \varepsilon_i\varepsilon_j\,L_{ji}(-\mathbf{B})}$$

where $\varepsilon_i = \pm1$ is the time-reversal parity of the quantity whose rate is $J_i$, and $\mathbf{B}$ is any external magnetic field. A rotation rate $\boldsymbol{\Omega}$ is treated the same way as $\mathbf{B}$. Charge and heat currents have the same parity, so $\varepsilon_i\varepsilon_j = +1$ for thermoelectric coefficients.

### D.15.2 — Assumptions

1. **Microscopic reversibility.** If $\Gamma(t)$ is a trajectory with field $\mathbf{B}$, then $\Theta\Gamma(-t)$ is a trajectory with field $-\mathbf{B}$, where $\Theta$ maps $(\mathbf{q}, \mathbf{p}) \to (\mathbf{q}, -\mathbf{p})$. For the flow map this reads $\varphi_t^{\mathbf{B}}\Theta = \Theta\,\varphi_{-t}^{-\mathbf{B}}$.
2. **Invariant equilibrium.** $\rho_0^{\mathbf{B}}(\Theta\Gamma) = \rho_0^{-\mathbf{B}}(\Gamma)$, and the phase-space measure is $\Theta$-invariant.
3. **Definite parity.** $J_i(\Theta\Gamma) = \varepsilon_iJ_i(\Gamma)$.
4. **Green–Kubo representation.** $L_{ij} = c\int_0^\infty\langle J_i(0)J_j(t)\rangle_0\,dt$, with the same positive constant $c$ (for example $1/Vk_B$ for forces normalised as in §D.15.4) for every pair. For mechanical forces this is §D.9. For thermal forces it is the Luttinger or regression argument of §D.11.2, which is an additional assumption.
5. **Classical variables.** The quantum proof uses the Kubo canonical correlation and an antiunitary $\Theta$, and goes through the same way (Kubo, *J. Phys. Soc. Jpn.* **12**, 570 (1957)).

### D.15.3 — Proof

Let $C_{ij}(t;\mathbf{B}) = \int d\Gamma\,\rho_0^{\mathbf{B}}(\Gamma)\,J_i(\Gamma)\,J_j(\varphi_t^{\mathbf{B}}\Gamma)$. Substitute $\Gamma = \Theta\Gamma'$ and use assumptions 1–3:

$$C_{ij}(t;\mathbf{B}) = \int d\Gamma'\,\rho_0^{-\mathbf{B}}(\Gamma')\,\varepsilon_iJ_i(\Gamma')\,J_j\big(\Theta\varphi_{-t}^{-\mathbf{B}}\Gamma'\big) = \varepsilon_i\varepsilon_j\,C_{ij}(-t;-\mathbf{B}).$$

Stationarity and commuting classical variables give $C_{ij}(-t) = \langle J_i(t)J_j(0)\rangle = C_{ji}(t)$. Hence $C_{ij}(t;\mathbf{B}) = \varepsilon_i\varepsilon_j\,C_{ji}(t;-\mathbf{B})$, and integrating over $t$ with assumption 4 proves the statement.

> `[DERIVATION]` Reciprocity follows from microscopic reversibility plus a Green–Kubo representation. It is not a separate empirical law.

Ch. 13 §13.9.2 gives the argument without $\mathbf{B}$ and without the parities. With a magnetic field present, the correct statement is the Onsager–Casimir form above (Casimir, *Rev. Mod. Phys.* **17**, 343 (1945)), for example $\sigma_{xy}(\mathbf{B}) = \sigma_{yx}(-\mathbf{B})$ for the Hall effect. Onsager's original papers are *Phys. Rev.* **37**, 405 and **38**, 2265 (1931).

### D.15.4 — The Kelvin relation as a check

The entropy production of §D.14 is $\dot s = \mathbf{j}\cdot\boldsymbol{\mathcal{E}}/T + \mathbf{j}_Q\cdot(-\nabla T/T^2)$. With the conjugate forces $X_1 = \boldsymbol{\mathcal{E}}/T$ and $X_2 = -\nabla T/T^2$, the currents of §D.14.2 become

$$L_{11} = T\mathcal{L}^{(0)}, \qquad L_{12} = -\frac{T\mathcal{L}^{(1)}}{e}, \qquad L_{21} = -\frac{T\mathcal{L}^{(1)}}{e}, \qquad L_{22} = \frac{T\mathcal{L}^{(2)}}{e^2},$$

so $L_{12} = L_{21}$ as required.

**Kelvin relation.** The Peltier coefficient at $\nabla T = 0$ is $\Pi = j_Q/j = -\mathcal{L}^{(1)}/e\mathcal{L}^{(0)} = TS$, which is the Kelvin relation of Ch. 13 §13.9.3.

**Convention note.** With these conjugate forces, $\sigma = L_{11}/T$ and $\kappa = (L_{22} - L_{12}L_{21}/L_{11})/T^2$. Ch. 13 §13.9.1 uses these same $1/T$ and $1/T^2$ factors, but defines its forces as $\mathbf{X}_E = \mathbf{E} - \nabla\mu/e$ and $\mathbf{X}_Q = -\nabla T/T$. Those forces correspond to different normalisations of $L$, so the factors and the forces there should be made consistent. The sign of the $\nabla\mu$ term also depends on the carrier charge: it is $+\nabla\mu/e$ for electrons of charge $-e$.

**Where reciprocity fails.** Outside linear response (for example, rectification in non-centrosymmetric conductors at second order). When $\Theta$-invariance of the equilibrium state fails for reasons not captured by external fields, as in spontaneously magnetised systems, the order parameter must be reversed together with $\mathbf{B}$. And when the chosen fluxes and forces are not thermodynamically conjugate, the matrix of coefficients need not be symmetric.

---

## D.16 — The Scope of Kubo, Stated Once

The derivations above support a precise version of the convergence claim of Ch. 13, which is *synthesis* in the sense of CONTRIBUTING §6.

1. **Exact within its domain.** Kubo gives every linear transport coefficient as an equilibrium correlation function. This is exact to first order in the driving field (§D.9).
2. **What turns it into a number.** Reaching a specific value of $\sigma$, $\kappa$, $D$ or $\eta$ requires several further inputs: the correct operator pair; the order of limits (the volume limit $V \to \infty$ before $\omega \to 0$); the separation of diamagnetic, contact and Drude-weight pieces (§D.12.1); for thermal forces, a further argument (§D.11.2); and in practice a closure such as $\tau$ (§D.12.2), which is `[PHENOMENOLOGICAL]`.
3. **What the laws are.** Ohm's, Fourier's, Fick's and Newton's viscosity laws are constitutive relations whose coefficients can be expressed in this framework, each in its own linear-response regime. No single calculation produces them all. Where the framework does not apply (ballistic transport, Ch. 13 §13.11; far from equilibrium), other descriptions such as Landauer's take over. The statement in Ch. 14 §14.7.1 that Fourier's and Ohm's laws are "the same Kubo result applied to different currents" is a `[STRUCTURAL CONNECTION]`: they are the same template, not the same calculation.

---

## D.17 — Summary

| Result | Statement | Assumptions | Used in |
|---|---|---|---|
| Canonical ensemble | $p_n = e^{-\beta E_n}/Z$, $\beta = \partial_ES_R/k_B$ | equal a priori probabilities; weak coupling; $E_n/(TC_R) \to 0$ | Ch. 10 §10.3 |
| Thermodynamics from $Z$ | $F = -k_BT\ln Z$; $T\,dS = \sum E_n\,dp_n$; $P = k_BT\,\partial_V\ln Z$ | canonical ensemble; thermodynamic limit for identification | Ch. 10 §10.4 |
| Equipartition | $\langle x_i\partial_jH\rangle = \delta_{ij}k_BT$; $\tfrac12k_BT$ per quadratic term | classical phase space; vanishing boundary terms | Ch. 10 §10.7.2 |
| Its failure | $\langle E\rangle = k_BT + (\hbar\omega)^2/12k_BT + \cdots$; frozen for $\hbar\omega \gg k_BT$ | quantised oscillator | Ch. 10 §10.7.3 |
| FD and BE | $\bar n = 1/(e^{\beta(\varepsilon - \mu)} \pm 1)$; $\langle\delta n^2\rangle = \bar n(1 \mp \bar n)$ | ideal quantum gas, grand canonical; $\mu < \varepsilon_{min}$ for bosons | Ch. 10 §10.8.2 |
| Classical limit | MB when $n\lambda_{th}^3/g_s \ll 1$; $P = nk_BT(1 \pm n\lambda_{th}^3/2^{5/2}g_s)$ | ideal gas | Ch. 10 §10.7.1, §10.8.2 |
| Planck law | $u(\nu) = (8\pi h\nu^3/c^3)/(e^{h\nu/k_BT} - 1)$ | free field; 2 polarisations; $\mu = 0$; large cavity | Ch. 10 §10.8.4 |
| Debye $T^3$ | $C_V \simeq (12\pi^4/5)Nk_B(T/T_D)^3$ | harmonic crystal; $T \ll T_D$; coefficient set by sound speeds | Ch. 10 §10.7.3 |
| Sommerfeld | $\int Hf = \int_0^\mu H + (\pi^2/6)(k_BT)^2H'(\mu)$; $c_{el} = (\pi^2/3)k_B^2T\,g(E_F)$ | $k_BT \ll E_F$; smooth $g$ | Ch. 10 §10.8.3 |
| Kubo formula | $\chi_{BA}(t) = (i/\hbar)\Theta(t)\langle[\hat B(t), \hat A(0)]\rangle_0$ | equilibrium past; first order in a classical field | Ch. 13 §13.1–§13.2 |
| FDT | classical $\tilde\chi'' = (\omega/2k_BT)S$; quantum $\tilde\chi'' = (1 - e^{-\beta\hbar\omega})S_>/2\hbar$ | equilibrium (KMS); linear response | Ch. 13 §13.3 |
| Green–Kubo $D$ | $D = \tfrac13\int_0^\infty\langle\mathbf{v}(0)\cdot\mathbf{v}(t)\rangle\,dt$ | integrable VACF; hydrodynamic diffusion; $d = 3$ | Ch. 13 §13.6.1 |
| Green–Kubo $\sigma$ | $\sigma_{\alpha\beta}(\omega) = V^{-1}\int dt\,e^{i\omega t}\int d\lambda\,\langle J_\beta(-i\hbar\lambda)J_\alpha(t)\rangle$ | as Kubo; $V \to \infty$ before $\omega \to 0$ | Ch. 13 §13.4.1 |
| Drude | $\sigma(\omega) = \sigma_0/(1 - i\omega\tau)$, $\sigma_0 = ne^2\tau/m$; f-sum $\pi ne^2/2m$ | exact free-gas weight plus single-$\tau$ closure | Ch. 13 §13.4.2; Ch. 14 §14.1 |
| Einstein relation | $D = k_BT\mu_{mob}/q$ (non-degenerate); $\sigma = e^2(\partial n/\partial\mu)D$ (general) | linear response; local equilibrium | Ch. 13 §13.6.2; Ch. 14 §14.5 |
| Wiedemann–Franz | $\kappa/\sigma T = \pi^2k_B^2/3e^2$ | elastic scattering (same $\tau(\varepsilon)$); $k_BT \ll E_F$; electrons only | Ch. 13 §13.5.2; Ch. 14 §14.4 |
| Mott formula | $S = -(\pi^2k_B^2T/3e)\,\sigma'(\mu)/\sigma(\mu)$ | as Wiedemann–Franz | Ch. 13 §13.9.3; Ch. 14 §14.3 |
| Onsager–Casimir | $L_{ij}(\mathbf{B}) = \varepsilon_i\varepsilon_jL_{ji}(-\mathbf{B})$; Kelvin $\Pi = TS$ | microscopic reversibility; Green–Kubo form; conjugate forces | Ch. 13 §13.9; Ch. 14 §14.3 |

---

## D.18 — References

Standard sources used in this appendix (see also [`REFERENCES.md`](../REFERENCES.md)):

- F. Reif, *Fundamentals of Statistical and Thermal Physics*, McGraw-Hill (1965) — reservoir derivation, equipartition, quantum gases.
- R. K. Pathria and P. D. Beale, *Statistical Mechanics*, 3rd ed., Elsevier (2011) — quantum gases, virial expansion, Bose condensation.
- L. D. Landau and E. M. Lifshitz, *Statistical Physics, Part 1*, §33 (Wigner–Kirkwood expansion).
- N. W. Ashcroft and N. D. Mermin, *Solid State Physics*, Saunders (1976) — Sommerfeld expansion, Debye model, Boltzmann transport, Wiedemann–Franz, thermopower.
- R. Kubo, *J. Phys. Soc. Jpn.* **12**, 570 (1957); R. Kubo, *Rep. Prog. Phys.* **29**, 255 (1966).
- H. B. Callen and T. A. Welton, *Phys. Rev.* **83**, 34 (1951).
- L. Onsager, *Phys. Rev.* **37**, 405 (1931); **38**, 2265 (1931). H. B. G. Casimir, *Rev. Mod. Phys.* **17**, 343 (1945).
- J. M. Luttinger, *Phys. Rev.* **135**, A1505 (1964).
- B. J. Alder and T. E. Wainwright, *Phys. Rev. A* **1**, 18 (1970).
- N. G. van Kampen, *Physica Norvegica* **5**, 279 (1971).
- G. D. Mahan, *Many-Particle Physics*, Springer — linear response and the conductivity with diamagnetic term.
- E. H. Lieb and J. L. Lebowitz, *Adv. Math.* **9**, 316 (1972); D. Ruelle, *Statistical Mechanics: Rigorous Results*, Benjamin (1969).
