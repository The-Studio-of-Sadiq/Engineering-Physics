# Transport Phenomena and Thermoelectrics

### The Kubo Coefficients in Engineering Practice

---

> _In science, there is no distinction between theory and application._ _The equations that describe the flow of electrons in a wire are the same ones_ _that describe the flow of heat through a wall — because they are both_ _the same equation, applied to the same phenomenon._ — paraphrased from Lars Onsager

---

## 14.0 — Overview

Chapter 13 derived all five transport laws from the Green-Kubo formula — with no additional input beyond equilibrium quantum mechanics. The coefficients $\sigma$, $\kappa$, $D$, $\eta$, $C_{ijkl}$ are time-integrated current autocorrelations; the Onsager matrix gives the off-diagonal effects.

This chapter applies those results to concrete engineering problems. It is **Layer 2 applied** — the transport laws in their full engineering detail, with quantitative worked results, before Bridge C lumps them into circuit elements and control volumes in Chapter 17.

The chapter divides into three groups:

**Electrical transport** (§§14.1–14.2): resistivity vs. temperature, Hall sensors, contact resistance.

**Thermoelectric transport** (§§14.3–14.5): the full Onsager matrix in engineering form — thermocouples, Peltier coolers, thermoelectric generators, the ZT optimization problem.

**Coupled transport** (§§14.6–14.8): semiconductor drift-diffusion, thermionic emission, the thermal resistance network as bridge to Layer 3.

---

## 14.1 — Electrical Resistivity in Practice

### 14.1.1 — Matthiessen's Rule

From Ch. 13 §13.4.2, the conductivity $\sigma = ne^2\tau/m$ requires knowing $\tau$. In real metals, electrons scatter from multiple sources simultaneously. Each scattering mechanism contributes an independent rate $1/\tau_i$:

$$\frac{1}{\tau} = \frac{1}{\tau_{phonon}} + \frac{1}{\tau_{impurity}} + \frac{1}{\tau_{grain}} + \cdots$$

Since $\rho = m/ne^2\tau$, this gives **Matthiessen's rule**:

$$\rho(T) = \rho_0 + \rho_{phonon}(T) + \rho_{other}$$

- **$\rho_0$** (residual resistivity): from impurities and defects; temperature-independent. Sets the $T\to 0$ floor.
- **$\rho_{phonon}(T) \propto T$**: at room temperature (Bloch-Grüneisen, Ch. 6 §6.7.3). At high $T$ (above Debye temperature): linear. At low $T$: $\rho_{phonon} \propto T^5$ (only small-angle phonon scattering survives).
- **$\rho_{grain}$**: grain boundary scattering in polycrystalline materials; roughly temperature-independent.

**Bloch-Grüneisen formula** for phonon contribution:

$$\rho_{phonon}(T) = A\left(\frac{T}{T_D}\right)^5\int_0^{T_D/T}\frac{x^5}{(e^x-1)(1-e^{-x})}dx$$

Limits:

- $T \gg T_D$: $\rho_{phonon} \to AT/T_D$ (linear, observed in room-temperature metals)
- $T \ll T_D$: $\rho_{phonon} \to 4.18A(T/T_D)^5$ (steep $T^5$ power law)

### 14.1.2 — The Residual Resistivity Ratio

The **residual resistivity ratio (RRR)** is the single most informative measure of metal purity for cryogenic and superconducting applications:

$$RRR = \frac{\rho(300;\text{K})}{\rho(4;\text{K})}$$

For copper: commercial purity (99.9%) gives $RRR \sim 40$–$100$. Ultra-pure copper (99.9999%) gives $RRR > 10{,}000$.

Higher RRR means lower residual resistivity, which means lower heat load in superconducting magnet coil leads, better signal integrity in cryogenic detectors, and higher purity for electron beam lithography.

### 14.1.3 — Resistance Temperature Detectors (RTDs)

The nearly linear $\rho(T)$ of platinum is exploited in RTDs. The Callendar-Van Dusen equation (empirical fit to the Bloch-Grüneisen result):

$$R(T) = R_0\left(1 + A,T + B,T^2 + C,T^3(T-100)\right)$$

For Pt100 ($R_0 = 100;\Omega$ at 0°C): $A = 3.9083\times10^{-3}$, $B = -5.775\times10^{-7}$, $C = -4.183\times10^{-12}$ (IEC 60751 standard).

Sensitivity: $dR/dT \approx 0.385;\Omega/°$C for Pt100.

**Why platinum?** Stable crystal structure, reproducible RRR, chemically inert over a wide temperature range, well-characterized impurity scattering. The NIST Pt resistance standard is the most precise thermometer from 14 K to 962°C.

### 14.1.4 — Contact Resistance and the Ballistic Limit

At a metal contact, resistance arises from three sources:

**Spreading resistance** (current flowing from a small contact area into a large bulk — current funnels through the contact):

$$R_{spread} = \frac{\rho}{4a}$$

for a circular contact of radius $a$.

**Interface/contact resistance** (imperfect bonding, oxide layer, phonon mismatch at metal-semiconductor interfaces): characterized by contact resistivity $\rho_c$ (Ω·m²).

**Sharvin resistance** (ballistic limit when contact size $a < \ell_{mfp}$):

$$R_{Sharvin} = \frac{h}{2e^2}\frac{1}{\langle T\rangle N_{modes}} = \frac{4\rho\ell_{mfp}}{3\pi a^2}$$

Sharvin resistance is geometry-limited, not scattering-limited — it represents the quantum resistance of the few ballistic modes that fit through the contact. For an aluminum nanocontact ($a = 1$ nm, $\ell_{mfp} = 18$ nm): $R_{Sharvin} \approx 4;\text{k}\Omega$.

**Engineering implication:** As interconnect widths in semiconductor ICs approach $\ell_{mfp}$ (currently $\sim 10$–$20$ nm), Matthiessen's rule breaks down, resistivity increases beyond bulk values (sidewall scattering), and quantum resistance becomes significant. This is the physical wall constraining Moore's Law.

---

## 14.2 — The Hall Effect in Engineering

### 14.2.1 — Classical Hall Effect Revisited

From Ch. 13 §13.10 (Ohm's law): a current $I$ in a conductor of thickness $t$ in transverse field $B$:

$$R_H = \frac{1}{nq}, \qquad V_H = \frac{IB}{nqt} = R_H\frac{IB}{t}$$

The Hall coefficient $R_H = 1/nq$ (positive for holes, negative for electrons) simultaneously gives:

- **Carrier density $n$:** from the magnitude of $R_H$
- **Carrier type:** from the sign of $R_H$
- **Mobility:** $\mu_H = |R_H|\sigma = |R_H|/\rho$

For copper at 300 K: $R_H = -5.5\times10^{-11}$ m³/C → $n = 1/|R_H|e = 1.14\times10^{29}$ m$^{-3}$ (one conduction electron per atom). ✓

For p-type silicon doped at $N_A = 10^{23}$ m$^{-3}$: $R_H = +1/ep = +6.25\times10^{-5}$ m³/C (positive — holes dominate). ✓

### 14.2.2 — Hall Sensors

Hall sensors output a voltage proportional to the product $I\times B$. Keep $I$ constant → $V_H \propto B$: a linear magnetic field sensor. Keep $B$ constant → $V_H \propto I$: a current sensor (no galvanic connection needed).

**Key figures of merit:**

- Sensitivity: $S_A = V_H/IB = 1/nqt$ (higher for thin films, low-n semiconductors)
- Offset voltage: zero-field output from geometry imperfections (trimmed with laser)
- Temperature coefficient: from $\partial R_H/\partial T$ via Fermi-Dirac statistics

InAs and InSb (high mobility $\mu \sim 10^4$ cm²/Vs) give high sensitivity. Si Hall sensors are more stable and CMOS-compatible.

**Applications:** Brushless DC motor commutation, automotive angle/speed sensors, current measurement in EV battery management systems, anti-lock braking systems, compass and positioning sensors in smartphones.

### 14.2.3 — The Quantum Hall Resistance Standard

From Ch. 7 §7.3 and Ch. 13 §13.11.2: at filling factor $\nu$:

$$R_{xy} = \frac{h}{\nu e^2} = \frac{R_K}{\nu}, \qquad R_K = \frac{h}{e^2} = 25812.807;\Omega$$

Since 2019 (SI redefinition), $h$ and $e$ are exact, so $R_K$ is exact. A 2DEG in a cryostat at $T < 1$ K, $B \sim 10$ T holds this value to better than $10^{-9}$ — the most precisely reproducible resistance in physics.

**Metrological use:** National measurement institutes maintain GaAs/AlGaAs QH samples as the primary resistance standard. All secondary resistors (decade boxes, etc.) are calibrated against these. Ultimately, every ohmmeter you use traces back to the topology of Landau levels.

---

## 14.3 — Thermoelectric Effects: Complete Engineering Treatment

### 14.3.1 — The Three Effects, Unified

From Ch. 13 §13.9 (Onsager matrix), the three thermoelectric effects:

**Seebeck effect** — open-circuit EMF from temperature gradient: $$V_{OC} = S\cdot\Delta T \qquad (S\text{: Seebeck coefficient, V/K})$$

**Peltier effect** — heat pumped by current: $$\dot Q_{Peltier} = \Pi\cdot I = ST\cdot I \qquad (S\text{: same coefficient, by Kelvin's relation})$$

**Thomson effect** — heat generated/absorbed in a current-carrying conductor with a temperature gradient: $$\dot q_{Thomson} = \tau_{Th}\cdot J\cdot\nabla T \qquad (\tau_{Th} = T,dS/dT\text{: Thomson coefficient})$$

The three are not independent — they are all encoded in the single Seebeck function $S(T)$: $$\Pi(T) = S(T)\cdot T, \qquad \tau_{Th}(T) = T\frac{dS}{dT}$$

This is the Onsager reciprocal relation (Ch. 13 §13.9.2) made explicit: knowing $S(T)$ completely determines all thermoelectric behavior.

### 14.3.2 — Thermocouples

Two dissimilar conductors A and B, junction at temperature $T$, reference at $T_0$:

$$V = \int_{T_0}^T\left[S_A(T') - S_B(T')\right]dT' = S_{AB}\Delta T\quad\text{(for small }\Delta T\text{)}$$

The relative Seebeck coefficient $S_{AB} = S_A - S_B$ (in $\mu$V/K) defines the thermocouple type. IEC standard thermocouple types:

|Type|Materials|Range|Sensitivity|Note|
|---|---|---|---|---|
|K|NiCr / NiAl|$-200$ to $1260°$C|$\approx 41;\mu$V/°C|Most common; general purpose|
|J|Fe / CuNi|$-210$ to $760°$C|$\approx 52;\mu$V/°C|Oxidises above 760°C|
|T|Cu / CuNi|$-270$ to $370°$C|$\approx 43;\mu$V/°C|Best for cryogenic|
|E|NiCr / CuNi|$-270$ to $1000°$C|$\approx 68;\mu$V/°C|Highest sensitivity|
|N|NiCrSi / NiSi|$-270$ to $1300°$C|$\approx 39;\mu$V/°C|Stable at high T|
|R|Pt13Rh / Pt|$0$ to $1600°$C|$\approx 12;\mu$V/°C|Precision high-T|
|B|Pt30Rh / Pt6Rh|$100$ to $1820°$C|$\approx 10;\mu$V/°C|Very high T; self-compensating|
|S|Pt10Rh / Pt|$0$ to $1600°$C|$\approx 10;\mu$V/°C|Primary standard|

**Cold junction compensation:** The reference junction must be at a known temperature $T_0$. In practice, an isothermal terminal block with an on-board temperature sensor (thermistor or RTD) measures $T_0$; the microcontroller adds $V(T_0)$ from a lookup table to the measured voltage.

**Seebeck coefficient origin:** From the Mott formula (Ch. 13 §13.9.3): $S = -\pi^2k_B^2T/3eE_F \times (d\ln\sigma/dE)|_{E_F}$. Materials with strongly energy-dependent $\sigma(E)$ near $E_F$ (e.g., from a sharp band edge or resonant level) have large $|S|$.

---

## 14.4 — Thermoelectric Device Design

### 14.4.1 — The Thermoelectric Module

A thermoelectric module consists of $N$ thermocouple pairs (P-type and N-type semiconductor legs) electrically in series and thermally in parallel:

```
Hot side (T_H)
├── [P-leg] [N-leg] [P-leg] [N-leg] ...
└── Cold side (T_C)
        ↑                ↑
     (+) current    current flows through external circuit
```

For $N$ couples with matched resistance $R_{total} = NR_0$ and thermal conductance $K_{total} = NK_0$:

**Thermoelectric generator (TEG):**

Open-circuit voltage: $V_{OC} = N,S_{PN}\Delta T$

Maximum power: $P_{max} = N\frac{(S_{PN}\Delta T)^2}{4R_0}$ (matched load $R_L = R_{total}$)

Efficiency at maximum power:

$$\eta_{max} = \frac{\Delta T}{T_H}\cdot\frac{\sqrt{1+ZT_M}-1}{\sqrt{1+ZT_M}+T_C/T_H}$$

where $T_M = (T_H+T_C)/2$ is the mean temperature and:

$$\boxed{ZT = \frac{S^2\sigma}{\kappa}T = \frac{S^2}{\rho\kappa}T}$$

is the **dimensionless figure of merit**. The Carnot efficiency $\eta_C = \Delta T/T_H$ is recovered in the limit $ZT\to\infty$.

**Efficiency at matched load vs. Carnot:**

|$ZT$|$\eta_{max}/\eta_{Carnot}$ (for $T_C/T_H = 300/600$ K)|
|---|---|
|0.5|0.24|
|1.0|0.32|
|2.0|0.42|
|5.0|0.58|
|$\infty$|1.00 (Carnot)|

Current best materials ($ZT \sim 2$–$3$): ~40–50% of Carnot efficiency.

**Thermoelectric cooler (TEC/Peltier module):**

Peltier cooling power (heat pumped from cold side): $$\dot Q_C = S_{PN},T_C,I - \frac{1}{2}I^2 R_{total} - K_{total}\Delta T$$

Maximum $\Delta T$ (at $\dot Q_C = 0$, optimizing over $I$):

$$\boxed{\Delta T_{max} = \frac{1}{2}ZT_C^2}$$

For Bi₂Te₃ module ($ZT = 1$ at 300 K, $T_C = 300$ K): $\Delta T_{max} = 45°$C.

Coefficient of performance at maximum $\Delta T$:

$$COP_{max} = \frac{\dot Q_C}{P_{input}}\bigg|_{I_{opt}} = \frac{T_C}{\Delta T}\cdot\frac{\sqrt{1+ZT_M}-T_H/T_C}{\sqrt{1+ZT_M}+1}$$

The first factor is the Carnot COP; the second factor is the ZT correction.

### 14.4.2 — Materials Engineering for High ZT

$ZT = S^2\sigma T/\kappa$: maximize power factor $S^2\sigma$, minimize $\kappa$.

**The conflict:** High $\sigma$ → high $\kappa$ (Wiedemann-Franz, Ch. 13 §13.5.2). Good thermoelectrics need high $S$ and $\sigma$ (like a metal) but low $\kappa$ (like a glass). The ideal: a "phonon glass, electron crystal" (PGEC).

**Strategies to achieve high ZT:**

|Strategy|Mechanism|Example|
|---|---|---|
|Resonant levels|Sharp feature in DOS near $E_F$ → large $|dS/dE|
|Band convergence|Multiple valleys contributing to transport → high $S$ with high $\sigma$|PbTe (high-T), SnSe|
|Nanostructuring|Phonon scattering at grain boundaries without electron scattering|BiSbTe nanocomposite|
|Lattice softening|Rattler atoms in cages scatter phonons (PGEC)|Skutterudites, clathrates|
|2D/layered|Quantum confinement enhances DOS asymmetry|Bi₂Te₃ thin films|

**Current champions:**

- Room temperature ($\sim 300$ K): BiSbTe alloys, $ZT \sim 2.0$–$2.5$
- Mid-range ($\sim 700$ K): PbTe:Na/Se, $ZT \sim 2.5$
- High temperature ($\sim 900$ K): SiGe alloys for RTG, $ZT \sim 1.0$; SnSe single crystal $ZT \sim 2.6$
- Cryogenic ($< 200$ K): BiSb, $ZT \sim 0.6$

### 14.4.3 — Applications of Thermoelectric Devices

**Radioisotope thermoelectric generators (RTGs):** The Voyager 1 and 2 spacecraft (launched 1977) are still transmitting — powered by ²³⁸Pu RTGs delivering $\sim 40$ W at launch. PbTe thermoelectric couples convert decay heat directly to electricity with $\eta \sim 6%$, no moving parts, 100% reliability over decades.

**Automotive waste heat recovery:** A typical gasoline engine wastes $\sim 60%$ of fuel energy as heat. TEG modules on the exhaust pipe can recover 1–2 kW, reducing alternator load. Currently limited by $ZT$ and cost.

**Precision temperature control:** Peltier coolers maintain laser diode junctions to $\pm 0.001°$C — critical for wavelength stability in fiber-optic communications (DWDM channels are 0.8 nm apart).

**Medical cooling:** Portable vaccine refrigerators, DNA analysis devices, personal cooling vests for MS patients (heat sensitivity).

---

## 14.5 — Semiconductor Drift-Diffusion Equations

### 14.5.1 — Combining Ohm and Fick for Carriers

From Ch. 13, charge transport in a semiconductor involves two mechanisms:

- **Drift**: carriers move in response to electric field (Ohm's law)
- **Diffusion**: carriers move from high to low concentration (Fick's law)

The **total current densities** (using Einstein relation $D = \mu k_BT/e$):

$$\boxed{J_n = e\mu_n n\mathbf{E} + eD_n\nabla n = e\mu_n\left(n\mathbf{E} + \frac{k_BT}{e}\nabla n\right)}$$

$$\boxed{J_p = e\mu_p p\mathbf{E} - eD_p\nabla p = e\mu_p\left(p\mathbf{E} - \frac{k_BT}{e}\nabla p\right)}$$

**Signs:** Electrons drift opposite to $\mathbf{E}$ (negative charge) but diffuse down their concentration gradient. Holes drift with $\mathbf{E}$ but diffuse down their gradient. Both contribute to current in the same direction for most practical configurations.

### 14.5.2 — Continuity Equations

Conservation of electron and hole densities (charge conservation, Noether U(1)):

$$\frac{\partial n}{\partial t} = \frac{1}{e}\nabla\cdot\mathbf{J}_n + (G - R)$$ $$\frac{\partial p}{\partial t} = -\frac{1}{e}\nabla\cdot\mathbf{J}_p + (G - R)$$

where $G$ is the carrier generation rate (thermal or optical) and $R$ is the recombination rate. For low-level injection (minority carrier analysis):

$$R - G = \frac{\Delta n}{\tau_n} \quad\text{(electrons in p-type)}$$

where $\tau_n$ is the minority carrier lifetime (typically $\mu$s–ms in silicon).

### 14.5.3 — Minority Carrier Diffusion and Diffusion Length

For minority electrons in p-type material (no applied field, $\mathbf{E}\approx 0$ in neutral bulk), in steady state:

$$D_n\frac{d^2\Delta n}{dx^2} - \frac{\Delta n}{\tau_n} = 0$$

Solution: $\Delta n(x) = \Delta n_0,e^{-x/L_n}$

**Electron diffusion length:** $L_n = \sqrt{D_n\tau_n}$

This is the average distance a minority carrier diffuses before recombining. It sets the length scale for p-n junction and transistor behavior.

For silicon at 300 K: $D_n \approx 25$ cm²/s, $\tau_n \approx 1;\mu$s → $L_n = \sqrt{25\times10^{-4}\times10^{-6}} = 50;\mu$m.

### 14.5.4 — The p-n Junction and Shockley Equation

At the p-n junction, minority carriers diffuse across the depletion region. The boundary conditions (from Boltzmann factor $e^{eV/k_BT}$):

$$\Delta n_p(0) = n_{p0}(e^{eV/k_BT} - 1), \qquad \Delta p_n(0) = p_{n0}(e^{eV/k_BT}-1)$$

Solving the diffusion equation in each neutral region:

$$\boxed{I = I_0\left(e^{eV/k_BT} - 1\right), \qquad I_0 = Ae^2\left(\frac{D_n n_{p0}}{L_n} + \frac{D_p p_{n0}}{L_p}\right)}$$

**Shockley's ideal diode equation** — derived from drift-diffusion (Ch. 13) applied to a p-n junction (Ch. 6 §6.6.2). Every diode model in circuit simulators (SPICE) starts here.

### 14.5.5 — Solar Cell Physics

Under illumination, minority carriers are generated at rate $G_{opt}$. The short-circuit current:

$$I_{SC} = Aqe(G_{opt}L_n + G_{opt}L_p) = Aq G_{opt}(L_n + L_p)$$

Open-circuit voltage (from $I = 0$):

$$V_{OC} = \frac{k_BT}{e}\ln\left(\frac{I_{SC}}{I_0}+1\right) \approx \frac{k_BT}{e}\ln\frac{I_{SC}}{I_0}$$

For silicon solar cell: $I_0 \approx 10^{-10}$ A, $I_{SC} \approx 30$ mA/cm² → $V_{OC} \approx 0.6$–$0.7$ V at 300 K.

**Maximum power point:** Efficiency limited by the Shockley-Queisser limit ($\eta_{max} \approx 33%$ for single-junction under AM1.5 spectrum) from thermodynamic analysis of blackbody radiation (Ch. 10 §10.8.4) + Carnot considerations at the bandgap.

---

## 14.6 — Thermionic Emission

### 14.6.1 — The Richardson-Dushman Equation

From Ch. 10 §10.8.2 (Fermi-Dirac distribution): electrons in a metal at temperature $T$ have an energy distribution $f(E) = 1/(e^{(E-E_F)/k_BT}+1)$. The fraction with enough energy to escape the surface (energy $> E_F + W$, where $W$ is the work function):

$$J = A_R,T^2,e^{-W/k_BT}$$

$$\boxed{A_R = \frac{4\pi m_e k_B^2 e}{h^3} = 1.20\times 10^6;\text{A/(m}^2\text{K}^2\text{)}}$$

This is the **Richardson-Dushman equation**. $A_R$ is the Richardson constant; experimentally it ranges from $0.5\times 10^6$ to $1.5\times 10^6$ depending on crystal orientation and surface condition.

### 14.6.2 — Work Functions and Schottky Effect

Work functions of common metals:

|Metal|$W$ (eV)|Notes|
|---|---|---|
|Cs|1.95|Lowest; used in photocathodes|
|Ba|2.52|Oxide cathodes|
|W|4.55|High T stability; electron guns|
|Mo|4.36|Vacuum tubes|
|Ni|5.15|Catalyst surfaces|
|Pt|5.65|Highest; inert contacts|
|Au|5.10|Ohmic contacts to p-GaAs|

**Schottky effect:** An applied electric field $E_{field}$ lowers the work function by the image-charge potential:

$$\Delta W = \sqrt{\frac{e^3 E_{field}}{4\pi\epsilon_0}}$$

For $E_{field} = 10^7$ V/m: $\Delta W \approx 0.38$ eV — significant enhancement of emission current at high fields.

### 14.6.3 — Engineering Applications

**X-ray tubes:** Tungsten filament heated to $\sim 2500$ K emits electrons; accelerated to $\sim 100$ kV; decelerated by target (Au or W) → bremsstrahlung X-rays.

**SEM/TEM electron guns:** Thermionic (W or LaB₆) or field emission (cold) sources. LaB₆ has a lower work function ($W = 2.66$ eV) and higher brightness than W, widely used in analytical SEMs.

**Vacuum tubes (historical and niche):** Thermionic triode/pentode — once the backbone of electronics; now confined to audio amplifiers, high-power RF transmitters, and CRT displays.

**Thermionic energy converters:** A hot cathode emits electrons that travel to a cooler anode across a vacuum gap, doing work. Efficiency limited by space-charge effects but potentially higher than Carnot (uses non-equilibrium electron distribution). Research-stage technology for concentrated solar power.

---

## 14.7 — The Thermal Resistance Network: Bridge to Layer 3

### 14.7.1 — Fourier → Thermal Resistance

For steady-state heat flow through a slab (Fourier's law, Ch. 13 §13.5):

$$\dot Q = -\kappa A\frac{dT}{dx}$$

For a uniform slab of length $L$, area $A$, in steady state ($\nabla^2 T = 0$): $T$ is linear, and:

$$\dot Q = \frac{\kappa A}{L}\Delta T = \frac{\Delta T}{R_{th}}$$

**Thermal resistance:**

$$\boxed{R_{th} = \frac{L}{\kappa A}} \qquad\text{(units: K/W)}$$

This is exactly Ohm's law with $\Delta T\leftrightarrow\Delta V$ and $\dot Q\leftrightarrow I$ and $R_{th}\leftrightarrow R$. The analogy is exact because both Fourier's law and Ohm's law are the same Kubo result applied to different currents (Ch. 13 §13.10).

### 14.7.2 — Thermal Resistance Networks

**Series** (heat flows through each layer sequentially):

$$R_{th,total} = \sum_i R_{th,i} = \sum_i \frac{L_i}{\kappa_i A}$$

Example: CPU die → TIM (thermal interface material) → heatspreader → TIM → heatsink:

|Layer|$\kappa$ (W/mK)|$L$ (mm)|$A$ (cm²)|$R_{th}$ (K/W)|
|---|---|---|---|---|
|Si die|150|0.5|1|0.033|
|TIM1 (indium)|80|0.1|1|0.013|
|Cu spreader|400|3.0|100|0.075|
|TIM2 (paste)|8|0.2|100|0.025|
|Al heatsink|200|20|1000|0.010|
|Convection|—|—|—|0.50|
|**Total**||||**0.66 K/W**|

At 100 W TDP: $\Delta T = 66°$C from junction to ambient. Junction at $T_j = 66 + 25 = 91°$C ✓

**Parallel** (heat flows through multiple paths):

$$\frac{1}{R_{th,total}} = \sum_i\frac{1}{R_{th,i}}$$

**Contact thermal resistance (Kapitza resistance):** At an interface between two materials, phonon transmission is imperfect. Contact resistance $R_c = 1/hA$ where $h$ is the interface conductance ($\sim 10^7$–$10^9$ W/m²K). Dominant effect at nanoscale (where $L < \ell_{phonon}$).

### 14.7.3 — Transient Thermal: The RC Thermal Network

Adding thermal mass (the thermal capacitance):

$$C_{th} = \rho c_p V \qquad\text{(J/K)}$$

The thermal RC time constant:

$$\tau_{th} = R_{th}\cdot C_{th}$$

For an LED package ($R_{th} = 5$ K/W, volume $= 1$ cm³, $\rho c_p = 3\times10^6$ J/m³K): $C_{th} = 3\times10^6\times10^{-6} = 3$ J/K → $\tau_{th} = 5\times3 = 15$ s.

A pulsed LED can handle much higher peak power than continuous — the pulse must be shorter than $\tau_{th}$ for the junction temperature not to exceed its limit.

**The thermal RC network is Bridge C applied to heat flow** — the Fourier PDE lumped into a first-order ODE for each thermal node. This is exactly the same lumping operation as Ch. 17 (Bridge C) will perform for all domains. Thermal engineering students are already doing Layer 3 analysis; they just call it "thermal resistance modeling" instead of "control volume lumping."

---

## 14.8 — Diffusion in Engineering: The Error Function Solution

### 14.8.1 — Semi-Infinite Solid with Constant Surface Concentration

Fick's second law: $\partial c/\partial t = D\nabla^2 c$

For a semi-infinite solid ($x > 0$) with surface concentration $c_s$ (constant) and initial uniform concentration $c_0$:

$$\boxed{c(x,t) = c_s + (c_0 - c_s),\text{erf}!\left(\frac{x}{2\sqrt{Dt}}\right)}$$

where $\text{erf}(z) = \frac{2}{\sqrt{\pi}}\int_0^z e^{-u^2},du$.

**Junction depth in semiconductor doping:** After a diffusion anneal at temperature $T$ for time $t$, the dopant profile is approximately Gaussian. The junction depth $x_j$ (where $c = c_{background}$):

$$x_j \approx 2\sqrt{Dt},\text{erfc}^{-1}!\left(\frac{c_{background}}{c_s}\right)$$

For phosphorus in silicon at $1000°$C ($D = 2.5\times10^{-14}$ cm²/s) for $t = 1$ h: $\sqrt{Dt} = \sqrt{2.5\times10^{-14}\times3600} = 9.5\times10^{-6}$ cm $= 95$ nm.

### 14.8.2 — Arrhenius Diffusivity in Solids

Solid-state diffusion requires atoms to jump between lattice sites, overcoming an energy barrier $Q$ (activation energy, from Ch. 6 §6.8.1 — bond breaking):

$$D = D_0,e^{-Q/RT} = D_0,e^{-Q/k_BT N_A}$$

Same Boltzmann factor as reaction kinetics. For self-diffusion in copper: $D_0 = 0.78$ cm²/s, $Q = 211$ kJ/mol.

At 800°C (1073 K): $D = 0.78,e^{-211000/8.314/1073} = 5.2\times10^{-11}$ cm²/s. At 600°C: $D = 2.4\times10^{-13}$ cm²/s — 200× slower. Activated processes are highly sensitive to temperature.

**Engineering applications:**

- **Steel carburization**: carbon diffuses into iron surface; $Q = 135$ kJ/mol for C in γ-Fe
- **Semiconductor doping**: B, P, As in Si; $Q \sim 3$–$4$ eV
- **Oxidation of metals**: O²⁻ diffuses through oxide scale (Pilling-Bedworth ratio)
- **Grain growth**: grain boundary diffusion; $Q < Q_{bulk}$ (less barrier at boundaries)

---

## 14.9 — Magnetoresistance Effects

### 14.9.1 — Ordinary Magnetoresistance

For free electrons, a magnetic field curves the trajectories (Lorentz force) and increases the effective path length between collisions. The resistance increase:

$$\frac{\Delta\rho}{\rho_0} = (\mu B)^2\quad\text{for }\mu B \ll 1$$

For copper ($\mu = 44$ cm²/Vs) at $B = 1$ T: $\mu B = 0.044$ → $\Delta\rho/\rho_0 \approx 0.002$ — tiny.

For high-mobility semiconductors (InSb, $\mu = 7.7$ m²/Vs) at $B = 0.1$ T: $\mu B = 0.77$ → significant magnetoresistance. This is why Hall sensors need low-$\mu$ materials for linear response.

### 14.9.2 — Anisotropic Magnetoresistance (AMR)

In ferromagnetic metals (Ni, Fe, permalloy), the resistivity depends on the angle $\theta$ between the current direction and the magnetization direction:

$$\rho(\theta) = \rho_\perp + (\rho_\parallel - \rho_\perp)\cos^2\theta$$

AMR ratio: $(\rho_\parallel - \rho_\perp)/\rho_\perp \approx 2$–$5%$ for Ni-Fe alloys.

**Application:** Hard disk drive read heads (1990s–early 2000s) used AMR sensors detecting the fringing field of magnetic bits. Superseded by GMR.

### 14.9.3 — Giant Magnetoresistance (GMR) and Tunnel Magnetoresistance (TMR)

From Ch. 7 §7.2 (spin-dependent transport):

**GMR** (spin-valve): $\Delta R/R \sim 5$–$80%$ for metallic spacer. Current HDD read heads use TMR for still higher ratios.

**TMR** (magnetic tunnel junction, MTJ): Two ferromagnetic electrodes separated by a thin ($\sim 1$ nm) insulating barrier. Tunnel current depends on relative magnetization orientation:

$$\text{TMR} = \frac{R_{AP} - R_P}{R_P} = \frac{2P_1P_2}{1-P_1P_2}$$

where $P_i$ is the spin polarization of electrode $i$. For CoFeB/MgO/CoFeB: TMR $> 600%$ at room temperature — the spin-polarized tunneling through crystalline MgO is symmetry-filtered.

**MRAM (Magnetic RAM):** Each MTJ is a non-volatile memory bit — high resistance = "1", low resistance = "0". Written by spin-transfer torque (STT), read by measuring resistance. STT-MRAM offers SRAM-like speed, flash-like non-volatility, and essentially unlimited endurance. In production at 22–28 nm nodes (Everspin, Samsung, GlobalFoundries).

---

## 14.10 — Summary

|Effect|Key equation|Engineering use|
|---|---|---|
|Matthiessen's rule|$\rho = \rho_0 + \rho_{ph}(T) + \ldots$|RTD calibration; purity assessment|
|RTD (Pt100)|Callendar-Van Dusen|Temperature measurement ±0.01°C|
|Hall effect|$V_H = IB/nqt$|Current sensors; carrier density measurement|
|QH resistance|$R_K = h/e^2$ (exact)|SI resistance standard|
|Seebeck|$V = S\Delta T$|Thermocouples; all 8 standard types|
|Peltier|$\dot Q = ST\cdot I$|Laser cooling; solid-state refrigeration|
|TEG efficiency|$\eta = \eta_C[\sqrt{1+ZT}-1]/[\sqrt{1+ZT}+T_C/T_H]$|Waste heat recovery; RTGs|
|TEC $\Delta T_{max}$|$\Delta T_{max} = ZT_C^2/2$|Minimum achievable cold-side temperature|
|Figure of merit|$ZT = S^2\sigma T/\kappa$|Materials optimization target|
|Drift-diffusion|$J = en\mu E + eD\nabla n$|All semiconductor device modeling|
|Shockley equation|$I = I_0(e^{eV/kT}-1)$|Diode, BJT, solar cell analysis|
|Solar cell $V_{OC}$|$V_{OC} = (kT/e)\ln(I_{SC}/I_0)$|PV cell characterization|
|Richardson-Dushman|$J = A_R T^2 e^{-W/kT}$|Electron guns; thermionic converters|
|Thermal resistance|$R_{th} = L/\kappa A$|Junction temperature; heatsink design|
|Transient thermal|$\tau_{th} = R_{th}C_{th}$|Pulsed power; thermal shock analysis|
|Error function diffusion|$c = c_s\text{erfc}(x/2\sqrt{Dt})$|Doping profiles; case hardening|
|Arrhenius diffusion|$D = D_0 e^{-Q/RT}$|Process time-temperature control|
|AMR|$\Delta\rho/\rho \sim 2$–$5%$|Magnetic field sensors|
|GMR/TMR|$\Delta R/R$ up to $600%$|HDD read heads; MRAM|

---

## 14.11 — Engineering Thread

|Physics|Engineering system|
|---|---|
|Matthiessen's rule + Pt100|Industrial process temperature measurement|
|Hall sensors|Brushless DC motor control; current measurement in EVs|
|Seebeck + thermocouples|Furnace control; gas turbine exhaust monitoring|
|Peltier coolers|Laser diode temperature control; CCD sensor cooling|
|TEG|Automotive exhaust recovery; spacecraft power (RTGs)|
|ZT optimization|Next-generation thermoelectric materials research|
|Drift-diffusion|MOSFET design; BJT gain; solar cell efficiency|
|Shockley equation|SPICE device models; analog circuit design|
|Thermal resistance|CPU/GPU thermal design; LED luminaire design; power module packaging|
|Arrhenius diffusion|IC process recipe development; steel heat treatment|
|STT-MRAM|Embedded non-volatile memory in advanced CMOS nodes|

---

## 14.12 — Looking Ahead

Chapter 14 completed the "Layer 2 Applied" section — taking the transport laws derived in Chapters 8–13 and working through their engineering applications in detail. The next two chapters complete Layer 2 itself:

**Chapter 15** covers **continuum mechanics** — deriving the Navier-Stokes equations for fluids and the elasticity equations for solids. These are the remaining Layer-2 PDEs that, alongside Maxwell (Ch. 11) and the transport equations (Ch. 13), complete the classical continuum description.

**Chapter 16** reveals the **unified PDE structure** — showing that the wave equation and diffusion equation appear identically across acoustics, electromagnetism, elasticity, heat, and mass transport. This is the last unification before Bridge C begins the descent to Layer 3.

---

_End of Chapter 14._

---

_Next: Chapter 15 — Continuum Mechanics: Fluids and Solids_