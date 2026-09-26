# A Map of Physical Phenomena

### Every named physical effect in this book — located, described, and connected

---

## 2.0 — How to Use This Chapter

This chapter is a **reference map**, not a reading chapter. Every named physical effect that appears anywhere in this book is listed here, briefly described, and placed on the four-layer framework from Chapters 0 and 1.

**Read it now once, lightly.** You will not understand every entry. That is expected and fine. The goal of the first read is to get a sense of the territory — to see how many different phenomena trace back to the same few mathematical structures.

**Return to it often.** Whenever a subsequent chapter introduces a named effect, find it here. The layer code and cross-references will tell you where it sits in the framework and what it connects to.

---

### Layer Codes

|Code|Scale|What lives here|
|---|---|---|
|**L0**|Framework scale|Particle physics, QFT, general relativity|
|**L0→L1**|Bridge A|Effects with QFT origin that manifest in single-particle QM|
|**L1**|Quantum / atomic scale|Wavefunctions, atoms, bands, nuclear structure|
|**L1→L2**|Bridge B|Effects quantum in origin but classical/continuum in manifestation|
|**L2**|Classical continuum scale|Maxwell, Newton, thermodynamics, continuum mechanics|
|**L2→L3**|Bridge C|Distributed-to-lumped transition|
|**L3**|Engineering systems scale|Circuits, machines, structures, processes|

---

### Format of Each Entry

**Effect Name** _What it is, in one or two sentences._ **Layer:** code | **Revealed by:** chapter/section | **Branch:** disciplines | **→ Ch. X**

---

## 2.1 — Quantum and Atomic Phenomena

---

**Photoelectric Effect** Monochromatic light above a threshold frequency ejects electrons from a metal with kinetic energy K = hν − W; below the threshold no electrons are emitted regardless of intensity. **Layer:** L0→L1 | **Revealed by:** Ch. 3 Bridge A: photon is a quantum of the U(1) gauge field; electron absorbs one quantum | **Branch:** EEE (photovoltaics, photodetectors, photomultipliers) | **→ Ch. 4**

---

**Compton Scattering** A photon scattered by a free electron shifts to longer wavelength Δλ = (h/mₑc)(1 − cosθ); both momentum and energy are conserved as if the photon were a particle. **Layer:** L0→L1 | **Revealed by:** Ch. 3: relativistic electron-photon kinematics in QED | **Branch:** EEE (X-ray imaging, radiation dosimetry) | **→ Ch. 3**

---

**de Broglie Matter Waves** Every particle with momentum p has wavelength λ = h/p; matter produces interference and diffraction patterns. **Layer:** L1 | **Revealed by:** Ch. 3 Bridge A: momentum eigenstates of the Schrödinger equation are plane waves e^(ik·r) with p = ħk | **Branch:** EEE (electron microscopy, neutron diffractometry) | **→ Ch. 4**

---

**Heisenberg Uncertainty Principle** Conjugate observables satisfy ΔxΔp ≥ ħ/2 and ΔEΔt ≥ ħ/2; the more precisely one is known the less precisely the other can be. **Layer:** L1 | **Revealed by:** Ch. 1 §1.8 + Ch. 3 §3.11: the Fourier bandwidth theorem applied to wavefunctions; p̂ = −iħ∇ makes position and momentum Fourier conjugates | **Branch:** All (fundamental measurement limit; transistor scaling limits) | **→ Ch. 4**

---

**Quantum Tunneling** A quantum particle has nonzero probability of crossing a classically forbidden barrier; amplitude decays as e^(−2κd) inside the barrier. **Layer:** L1 | **Revealed by:** Ch. 3 Bridge A: Schrödinger equation has exponentially decaying solutions in forbidden regions; WKB from Ch. 1 §1.8.4 | **Branch:** EEE (tunnel diodes, Josephson junctions, STM, MOSFET gate leakage) | **→ Ch. 4**

---

**Zero-Point Energy** A quantum oscillator in its ground state has energy E₀ = ħω/2 > 0; quantum systems cannot be at rest even at absolute zero. **Layer:** L1 | **Revealed by:** Ch. 3: the uncertainty principle forbids x = p = 0 simultaneously | **Branch:** EEE (laser threshold; squeezed light); ME (helium never solidifies at 1 atm) | **→ Ch. 4**

---

**Zeeman Effect (Normal and Anomalous)** An external magnetic field splits degenerate atomic energy levels; the anomalous splitting pattern requires spin-1/2. **Layer:** L1 | **Revealed by:** Ch. 3 Bridge A: spin-1/2 falls from the Dirac equation; Zeeman Hamiltonian −μ·B from minimal coupling | **Branch:** EEE (NMR, MRI, magnetometers, atomic clocks) | **→ Ch. 5**

---

**Stark Effect** An external electric field shifts and splits atomic energy levels; linear for degenerate states, quadratic for non-degenerate. **Layer:** L1 | **Revealed by:** Ch. 3 + perturbation theory: add eEz to the Coulomb potential | **Branch:** EEE (electro-optic modulators, electric-field sensing, Stark-shift clocks) | **→ Ch. 5**

---

**Fine Structure** Spectral lines split into closely spaced doublets from spin-orbit coupling (L·S interaction) and the relativistic kinetic energy correction; splitting of order α²mₑc² × α². **Layer:** L1 | **Revealed by:** Ch. 3 §3.5 Foldy-Wouthuysen at order (v/c)² | **Branch:** Metrology (fine structure constant α; precision spectroscopy) | **→ Ch. 5**

---

**Hyperfine Structure** Further splitting from the interaction between the electron and nuclear magnetic moments; the 21-cm hydrogen line (1420 MHz) is the most famous instance. **Layer:** L1 | **Revealed by:** Ch. 3 Bridge A: contact interaction of electron wavefunction with nuclear spin | **Branch:** EEE (atomic hydrogen maser; GPS atomic clocks; radio astronomy) | **→ Ch. 5**

---

**Lamb Shift** The 2s₁/₂ and 2p₁/₂ hydrogen levels, predicted degenerate by the Dirac equation, are split by 1057.8 MHz due to QED vacuum fluctuations. **Layer:** L0 (requires full QED) | **Revealed by:** One-loop QED; beyond Bridge A | **Branch:** Metrology (Rydberg constant definition) | **→ Epilogue**

---

**Spontaneous Emission** An excited atom decays to its ground state by emitting a photon even with no external radiation; rate given by Einstein's A coefficient. **Layer:** L0→L1 | **Revealed by:** Ch. 3 + quantized EM field: vacuum fluctuations drive decay; Fermi's Golden Rule gives the rate | **Branch:** EEE (LED efficiency; laser threshold; amplifier noise) | **→ Ch. 5**

---

**Stimulated Emission** An incident photon triggers a second identical photon from an excited atom, enabling coherent amplification. **Layer:** L0→L1 | **Revealed by:** Ch. 3 Bridge A: Einstein B coefficient from Fermi's Golden Rule; bosonic stimulation factor (n+1) | **Branch:** EEE (operating principle of every laser and optical amplifier) | **→ Ch. 5**

---

**Rabi Oscillations** A two-level atom driven at resonance coherently oscillates between ground and excited states at the Rabi frequency ΩR = dε/ħ. **Layer:** L1 | **Revealed by:** Ch. 3 + time-dependent perturbation theory on two-level Schrödinger equation | **Branch:** EEE (qubit control; pulsed NMR π-pulses; atomic clocks) | **→ Ch. 5**

---

**Fermi's Golden Rule** The transition rate between states under a weak perturbation is Γ = (2π/ħ)|⟨f|V|i⟩|²ρ(Ef); proportional to matrix element squared times density of final states. **Layer:** L1 | **Revealed by:** Ch. 3 Bridge A: first-order time-dependent perturbation theory | **Branch:** All (scattering rates → transport coefficients; optical rates; chemical reaction rates) | **→ Ch. 6**

---

**Pauli Exclusion Principle** No two identical fermions can occupy the same quantum state; the many-body wavefunction is antisymmetric under particle exchange. **Layer:** L0→L1 | **Revealed by:** Ch. 0 §0.5: anticommutation relations of fermion fields in L_SM | **Branch:** All (periodic table; why matter is rigid; Fermi-Dirac statistics for metals and semiconductors) | **→ Ch. 5**

---

**Spin-Statistics Theorem** Half-integer spin → Fermi-Dirac statistics + Pauli exclusion; integer spin → Bose-Einstein statistics + stimulation. **Layer:** L0 | **Revealed by:** Ch. 0 §0.5: requires relativistic QFT; proven from Lorentz invariance and locality | **Branch:** All (Fermi sea → metals/semiconductors; Bose enhancement → lasers, BEC, superfluids) | **→ Ch. 5**

---

**Quantum Entanglement** Two particles in a joint quantum state show measurement correlations stronger than any local hidden-variable theory allows (Bell's theorem). **Layer:** L0→L1 | **Revealed by:** Ch. 3: tensor product structure of multi-particle Hilbert space | **Branch:** EEE (quantum key distribution, quantum repeaters, quantum error correction) | **→ Ch. 4**

---

**Quantum Decoherence** A quantum superposition loses phase coherence from interaction with environmental degrees of freedom; off-diagonal density matrix elements decay exponentially. **Layer:** L1→L2 | **Revealed by:** Bridge B.b (Ch. 10): tracing out environment from the density matrix; same operation as the statistical limit | **Branch:** EEE (limits quantum computing; explains classical behavior of macroscopic objects) | **→ Ch. 10**

---

**Quantum Zeno Effect** Frequent measurement freezes a quantum system in its initial state; survival probability → 1 as measurement interval τ → 0. **Layer:** L1 | **Revealed by:** Ch. 3: wavefunction collapse resets the short-time quadratic decay | **Branch:** EEE (decoherence engineering in qubits; error-correction protocols) | **→ Ch. 4**

---

**Born-Oppenheimer Approximation** Electrons adjust instantaneously to slowly-moving nuclei (mₑ/M ≪ 1); electronic and nuclear motions decouple; nuclear dynamics happen on an effective potential surface. **Layer:** L1 | **Revealed by:** Ch. 3 Bridge A: expand Schrödinger equation in mₑ/M | **Branch:** ChE (quantum chemistry, DFT, molecular simulation); ME/CE (first-principles material properties) | **→ Ch. 6**

---

## 2.2 — Condensed Matter and Band Phenomena

---

**Bloch's Theorem** Electron wavefunctions in a periodic crystal take the form ψ_nk(r) = e^(ik·r) u_nk(r), a plane wave modulated by a lattice-periodic function. **Layer:** L1 | **Revealed by:** Ch. 1 Noether + Ch. 3: discrete translation symmetry conserves crystal momentum ħk | **Branch:** EEE/ME/CE (foundation of all band-structure-based materials analysis) | **→ Ch. 6**

---

**Band Gaps** Allowed electron energies cluster into bands separated by forbidden gaps; gaps open from Bragg reflection at Brillouin zone boundaries. **Layer:** L1 | **Revealed by:** Ch. 6: nearly-free-electron + degenerate perturbation theory at zone boundary | **Branch:** EEE (conductor/semiconductor/insulator distinction; all device physics); ME (optical and electrical material properties) | **→ Ch. 6**

---

**Hall Effect (Classical)** A transverse voltage develops across a current-carrying conductor in a magnetic field; R_H = 1/ne gives carrier density and sign directly. **Layer:** L2 | **Revealed by:** Bridge B.c (Ch. 11): Lorentz force on classical charge carrier | **Branch:** EEE (Hall sensors, current probes, material characterization) | **→ Ch. 14**

---

**Quantum Hall Effect (Integer)** Hall conductance in a 2D electron gas at low T and high B is precisely quantized: σ_xy = n e²/h for integer n, regardless of disorder. **Layer:** L1→L2 | **Revealed by:** Ch. 7: Landau levels + Chern number of occupied bands; topology protects the quantization | **Branch:** EEE (primary resistance standard; R_K = h/e² ≈ 25812.807 Ω by SI definition since 2019) | **→ Ch. 7**

---

**Fractional Quantum Hall Effect** Hall conductance at σ_xy = (p/q)e²/h for fractional p/q; quasiparticles carry fractional charge e/q; non-Abelian anyons emerge. **Layer:** L0→L1 | **Revealed by:** Beyond single-particle theory; many-body Laughlin wavefunction; topological order; relevant to f(φ) discussion in Ch. 0 | **Branch:** EEE (topological quantum computing platform) | **→ Epilogue**

---

**Landau Levels** Electrons in a uniform B-field occupy discrete energy levels E_n = ħω_c(n + 1/2) where ω_c = eB/mₑ is the cyclotron frequency. **Layer:** L1 | **Revealed by:** Ch. 4: Schrödinger equation with minimal coupling p̂ → p̂ − eA/c maps to a harmonic oscillator | **Branch:** EEE (basis of QHE; magneto-oscillations; magnetoresistance) | **→ Ch. 7**

---

**Aharonov-Bohm Effect** The wavefunction phase is shifted by the vector potential A even where B = ∇×A = 0; the topological phase produces observable interference in ring geometries. **Layer:** L1 | **Revealed by:** Ch. 3 §3.9.4: minimal coupling in Schrödinger equation; A (not B) is the fundamental object | **Branch:** EEE (mesoscopic physics; flux qubit; SQUID interference) | **→ Ch. 5**

---

**Berry Phase** Adiabatic evolution around a closed loop in parameter space gives a geometric phase γ_n = i∮⟨n|∇_R|n⟩·dR independent of the evolution rate. **Layer:** L1 | **Revealed by:** Ch. 7: adiabatic theorem; Berry connection A_n = i⟨n|∇_k|n⟩ is the gauge field of band topology | **Branch:** EEE (anomalous velocity; topological insulators; Weyl semimetals; quantum gate operations) | **→ Ch. 7**

---

**Superconductivity (BCS)** Below T_c, phonon-mediated attraction forms Cooper pairs that condense into a macroscopic quantum state carrying current with zero resistance. **Layer:** L1→L2 | **Revealed by:** Ch. 7: phonon-mediated pairing from Fermi's Golden Rule; spontaneous U(1) breaking (same Mexican hat as Higgs in Ch. 0, at meV scale) | **Branch:** EEE (MRI magnets, accelerators, power transmission R&D, quantum computing) | **→ Ch. 7**

---

**Meissner Effect** A superconductor expels all magnetic flux on cooling below T_c (B = 0 inside), distinguishing it from a perfect conductor. **Layer:** L1→L2 | **Revealed by:** Ch. 7: London equations from broken U(1) symmetry of BCS state; photon acquires effective mass inside — Higgs mechanism analog | **Branch:** EEE/ME (MRI shielding; Maglev trains; flux exclusion in SQUID design) | **→ Ch. 7**

---

**Josephson Effect (DC and AC)** A supercurrent tunnels through an insulating barrier with no voltage (DC); applied voltage V drives AC supercurrent at f = 2eV/h (AC). **Layer:** L1 | **Revealed by:** Ch. 7: quantum tunneling of Cooper pairs; macroscopic BCS wavefunction phase difference is the dynamical variable | **Branch:** EEE (voltage standard 1 V ≡ f/483597.8 GHz exact; SQUID magnetometers; superconducting qubits) | **→ Ch. 7**

---

**Flux Quantization** Magnetic flux through a superconducting loop is quantized in units Φ₀ = h/2e = 2.067 × 10⁻¹⁵ Wb; the 2e reflects Cooper pair charge. **Layer:** L1→L2 | **Revealed by:** Ch. 7: single-valuedness of BCS macroscopic wavefunction around the loop | **Branch:** EEE (SQUID sensing; flux qubit; type-II vortex physics) | **→ Ch. 7**

---

**Casimir Effect** Two uncharged parallel conductors in vacuum attract each other due to suppression of vacuum EM fluctuations in the gap; F/A = −ħcπ²/240d⁴. **Layer:** L0→L1 | **Revealed by:** Ch. 3 Bridge A: quantized photon field zero-point energy; plates change mode spectrum in gap relative to outside | **Branch:** EEE/ME (stiction in MEMS/NEMS at sub-micron gaps; nanotechnology design) | **→ Ch. 5**

---

**Kondo Effect** A magnetic impurity in a metal creates a resistance minimum below the Kondo temperature T_K; resistance shows logarithmic upturn before saturating as T → 0. **Layer:** L1→L2 | **Revealed by:** Bridge B.e (Ch. 13): many-body scattering resonance at Fermi level; requires non-perturbative renormalization group | **Branch:** EEE (limits quantum device performance at millikelvin; heavy-fermion materials) | **→ Ch. 13**

---

**Anderson Localization** Sufficient disorder spatially localizes all electron wavefunctions; a disordered metal becomes an insulator through quantum interference of multiply-scattered waves. **Layer:** L1 | **Revealed by:** Ch. 6/13: backscattered paths interfere constructively, suppressing diffusion; weak localization correction to conductivity | **Branch:** EEE (thin-film resistance; mesoscopic conductance fluctuations; weak localization in 2DEG) | **→ Ch. 13**

---

**Spin Hall Effect** A longitudinal charge current generates a transverse spin current in materials with strong spin-orbit coupling, without a magnetic field. **Layer:** L1 | **Revealed by:** Ch. 7: intrinsic spin Hall from Berry curvature (topological); extrinsic from spin-dependent impurity scattering (Fermi's Golden Rule) | **Branch:** EEE (spintronics; spin-orbit torque MRAM; spin current generation) | **→ Ch. 7**

---

**Giant Magnetoresistance (GMR)** Resistance of a ferromagnet/metal/ferromagnet trilayer is much lower when magnetic layers are parallel vs. antiparallel; effect up to 80%. **Layer:** L1→L2 | **Revealed by:** Ch. 7: spin-dependent scattering rates from Fermi's Golden Rule differ for majority and minority spin channels | **Branch:** EEE (HDD read heads since 1997; magnetic field sensors) | **→ Ch. 7**

---

**Topological Insulator Surface States** Bulk is insulating but time-reversal-protected metallic surface states with spin-momentum locking cannot be backscattered by non-magnetic perturbations. **Layer:** L1 | **Revealed by:** Ch. 7: non-trivial Z₂ topological invariant of bulk bands; same topology thread as QCD θ-term in Ch. 0 §0.9 | **Branch:** EEE (spin-polarized currents; topological transistors; quantum computing) | **→ Ch. 7**

---

**Weyl Semimetal** Band-touching Weyl nodes in the Brillouin zone host electrons behaving as massless relativistic Weyl fermions with definite chirality; each node is a Berry curvature monopole. **Layer:** L1 | **Revealed by:** Ch. 7: Weyl node carries Chern number ±1; chiral anomaly (from Ch. 0 ABJ anomaly) manifests as negative magnetoresistance | **Branch:** EEE (ultralow dissipation transport; potential quantum devices) | **→ Ch. 7**

---

**Bose-Einstein Condensation (BEC)** Below T_c a macroscopic fraction of bosons occupies the single-particle ground state, forming a coherent macroscopic quantum state. **Layer:** L1→L2 | **Revealed by:** Bridge B.b (Ch. 10): Bose-Einstein statistics + thermodynamic limit; same U(1) breaking as Higgs and BCS, at μeV scale | **Branch:** EEE (atom lasers; quantum simulation); ME (cryogenic systems) | **→ Ch. 10**

---

**Superfluidity** Liquid He-4 below 2.17 K flows with exactly zero viscosity; persistent current; quantized vortices. **Layer:** L1→L2 | **Revealed by:** Bridge B.b (Ch. 10): BEC + weak interactions; broken U(1); Landau two-fluid model | **Branch:** ME (dilution refrigerators; cryogenic technology for quantum computing) | **→ Ch. 10**

---

**Piezoelectric Effect** A crystal without inversion symmetry develops electric polarization under stress (direct: Pᵢ = dᵢⱼₖσⱼₖ) or deforms under applied field (converse). **Layer:** L1→L2 | **Revealed by:** Bridge B (Ch. 13): broken inversion symmetry in crystal + quantum-mechanical coupling of strain to charge distribution | **Branch:** EEE/ME (quartz oscillators, ultrasound transducers, MEMS, accelerometers, inkjet actuators) | **→ Ch. 13**

---

**Ferroelectric Effect** Spontaneous switchable electric polarization with hysteresis; analogous to ferromagnetism but for electric dipoles. **Layer:** L1→L2 | **Revealed by:** Bridge B.b (Ch. 10): Landau double-well free energy for electric polarization order parameter — same Mexican hat as Ch. 0 §0.7 | **Branch:** EEE (FeRAM non-volatile memory; electro-optic devices) | **→ Ch. 10**

---

**Magnetostriction** A ferromagnetic material changes dimensions when magnetized (Joule magnetostriction); stress changes its magnetization (Villari effect). **Layer:** L1→L2 | **Revealed by:** Bridge B (Ch. 13): spin-orbit coupling couples magnetic order to elastic strain | **Branch:** ME/EEE (sonar transducers — Terfenol-D; vibration energy harvesting; magnetomechanical sensors) | **→ Ch. 13**

---

**Shape Memory Effect** Deformation at low temperature is fully recovered on heating through a reversible martensitic phase transformation. **Layer:** L2 | **Revealed by:** Bridge B.b (Ch. 10): first-order structural phase transition; Landau theory with shear strain as order parameter | **Branch:** ME/CE/Biomedical (arterial stents; actuators; orthodontic wires; pipe couplings) | **→ Ch. 10**

---

**Coulomb Blockade** In a nanoscale conductor with small capacitance C, charging energy E_C = e²/2C suppresses tunneling unless exactly compensated by gate voltage; conductance shows Coulomb oscillations. **Layer:** L1→L2 | **Revealed by:** Ch. 7: classical charging energy (L2 capacitance) + quantum tunneling (L1 Ch. 4) meet in the mesoscopic regime | **Branch:** EEE (single-electron transistors; charge sensing; qubit implementations) | **→ Ch. 7**

---

## 2.3 — Electromagnetic Phenomena

---

**Faraday's Law of Induction** A changing magnetic flux through a loop induces EMF ε = −dΦ_B/dt; Lenz's law says the induced current opposes the change. **Layer:** L2 | **Revealed by:** Bridge B.c (Ch. 11): Bianchi identity ∂[μFνρ] = 0 gives ∇×E = −∂B/∂t directly from the U(1) sector of Ch. 0 | **Branch:** EEE (transformers, generators, motors, inductive charging, wireless power) | **→ Ch. 11**

---

**Skin Effect** AC current concentrates near the conductor surface; penetration depth δ = √(2/μσω) decreasing as 1/√f. **Layer:** L2 | **Revealed by:** Bridge B.c + Ohm's law: diffusion equation ∇²E = μσ ∂_t E has exponentially decaying solutions | **Branch:** EEE (RF conductor design, transformer iron losses, induction heating, EMI shielding) | **→ Ch. 11**

---

**Eddy Currents** Closed current loops induced in a bulk conductor by changing magnetic flux; dissipate energy and oppose the inducing change. **Layer:** L2 | **Revealed by:** Bridge B.c (Ch. 11): Faraday's law + Ohm's law inside a bulk conductor | **Branch:** EEE/ME (transformer losses; induction motors; eddy-current brakes; non-destructive testing) | **→ Ch. 11**

---

**Faraday Rotation** Plane of polarization rotates in a magnetized medium by θ_F = VBd; sign is independent of propagation direction (non-reciprocal). **Layer:** L2 | **Revealed by:** Bridge B.c (Ch. 12): B breaks time-reversal symmetry; off-diagonal dielectric tensor elements from Zeeman splitting | **Branch:** EEE (optical isolators; fiber-optic current sensors; gyroscopes) | **→ Ch. 12**

---

**Pockels Effect** Refractive index changes linearly with electric field (Δn ∝ E) in non-centrosymmetric crystals; enables phase modulation at GHz rates. **Layer:** L1→L2 | **Revealed by:** Bridge B (Ch. 13): broken inversion + field perturbation of electronic states gives χ⁽²⁾ ≠ 0 | **Branch:** EEE (electro-optic modulators in fiber-optic communications; LiNbO₃ devices) | **→ Ch. 13**

---

**Kerr Electro-Optic Effect** Refractive index changes quadratically with field (Δn ∝ E²); exists in all media including centrosymmetric. **Layer:** L1→L2 | **Revealed by:** Bridge B (Ch. 13): third-order susceptibility χ⁽³⁾ always nonzero | **Branch:** EEE (ultrafast optical switching; Q-switching; Kerr-lens mode-locking) | **→ Ch. 13**

---

**Birefringence** Anisotropic medium has different refractive indices for different polarizations; incident beam splits into ordinary and extraordinary rays. **Layer:** L2 | **Revealed by:** Bridge B.c (Ch. 12): anisotropic dielectric tensor εᵢⱼ from crystal symmetry | **Branch:** EEE (waveplates, polarizing beam splitters, LCD displays, optical coherence tomography) | **→ Ch. 12**

---

**Thermionic Emission** Electrons heated above the work function escape from a metal surface; Richardson-Dushman: J = AT²exp(−W/k_BT). **Layer:** L1→L2 | **Revealed by:** Bridge B.b (Ch. 14): high-energy tail of Fermi-Dirac distribution at elevated T | **Branch:** EEE (electron guns, X-ray tubes, vacuum tubes, thermionic energy converters) | **→ Ch. 14**

---

**Seebeck Effect** A temperature gradient across dissimilar materials drives EMF V = SαβΔT; the operating principle of thermocouples. **Layer:** L1→L2 | **Revealed by:** Bridge B.e (Ch. 13): off-diagonal Kubo coefficient L_QE relates temperature gradient to charge current | **Branch:** ME/EEE (thermocouples; thermoelectric generators for waste-heat recovery) | **→ Ch. 13**

---

**Peltier Effect** Current through a thermoelectric junction absorbs/releases heat at rate Q̇ = ΠI (Peltier coefficient Π = ST by Kelvin's relation). **Layer:** L1→L2 | **Revealed by:** Bridge B.e (Ch. 13): same Onsager off-diagonal element as Seebeck | **Branch:** EEE/ME (solid-state cooling; laser diode stabilization; precision calorimetry) | **→ Ch. 13**

---

**Thomson Effect** Current in a temperature-gradient conductor absorbs/releases heat at rate q̇ = τJ dT/dx (Thomson coefficient τ); distinct from Joule heating (∝ J²). **Layer:** L1→L2 | **Revealed by:** Bridge B.e (Ch. 13): third Onsager coefficient; τ = T dS/dT | **Branch:** EEE/ME (complete thermoelectric module efficiency requires all three effects) | **→ Ch. 13**

---

**Joule Heating** Current I through resistance R dissipates power P = I²R = V²/R regardless of current direction. **Layer:** L2→L3 | **Revealed by:** Bridge B.e (Ch. 13): diagonal Kubo → Ohm's law → P = J·E per unit volume | **Branch:** EEE/ME (conductor sizing; fuse design; electric heating; thermal management in electronics) | **→ Ch. 13, 15**

---

## 2.4 — Optical and Wave Effects

---

**Wave Interference** Coherent waves superpose; amplitude enhancement where phases align, cancellation where they oppose. **Layer:** L2 | **Revealed by:** Bridge B.c (Ch. 11): linearity of Maxwell's equations → superposition; same in acoustics from linear Navier-Stokes | **Branch:** EEE (antenna arrays, interferometric sensors, thin-film coatings, holography) | **→ Ch. 12**

---

**Diffraction** A wave at an aperture spreads beyond geometric shadow; far-field pattern is the Fourier transform of the aperture function. **Layer:** L2 | **Revealed by:** Bridge B.c (Ch. 11): Huygens-Fresnel from Maxwell; Kirchhoff diffraction integral | **Branch:** EEE (imaging resolution limits; X-ray crystal structure determination) | **→ Ch. 12**

---

**Snell's Law (Refraction)** At an interface: n₁sinθ₁ = n₂sinθ₂; wave bends toward normal when entering denser medium. **Layer:** L2 | **Revealed by:** Bridge B.c (Ch. 11): tangential E, H boundary conditions; equivalent to Fermat's principle (Ch. 1) | **Branch:** EEE (lens design, fiber optics, waveguides); CE (acoustic refraction in layered soils) | **→ Ch. 12**

---

**Total Internal Reflection** Above critical angle θ_c = arcsin(n₂/n₁), the wave in the denser medium is completely reflected; an evanescent field decays into the less dense medium. **Layer:** L2 | **Revealed by:** Bridge B.c (Ch. 11): Snell → sinθ_t > 1 has no real solution; |r|² = 1 | **Branch:** EEE (optical fiber waveguiding; integrated photonics; frustrated TIR biosensors) | **→ Ch. 12**

---

**Brewster's Angle** At θ_B = arctan(n₂/n₁), reflected p-polarization vanishes; reflected beam is completely s-polarized. **Layer:** L2 | **Revealed by:** Bridge B.c (Ch. 11): Fresnel r_p = 0 when reflected and refracted rays are orthogonal | **Branch:** EEE (anti-reflection for laser systems; polarizing beam splitters) | **→ Ch. 12**

---

**Rayleigh Scattering** Scattered intensity ∝ λ⁻⁴ from particles much smaller than wavelength; sky is blue, sunsets are red. **Layer:** L2 | **Revealed by:** Bridge B.c (Ch. 11): oscillating dipole radiation power ∝ ω⁴ | **Branch:** EEE (dominant fiber-optic attenuation below 1550 nm); CE/ME (atmospheric optics, LIDAR) | **→ Ch. 12**

---

**Raman Scattering** Inelastically scattered light shifts in frequency by a molecular/crystal vibration frequency; Stokes (photon loses energy) and anti-Stokes (photon gains energy). **Layer:** L1→L2 | **Revealed by:** Ch. 6 + nonlinear optics: photon-phonon interaction via χ⁽²⁾ or χ⁽³⁾ | **Branch:** ChE/ME (material identification; semiconductor stress measurement; in-situ reaction monitoring) | **→ Ch. 6**

---

**Brillouin Scattering** Light scattered by acoustic phonons (thermal sound waves) shifts by the phonon frequency; used for distributed structural sensing. **Layer:** L1→L2 | **Revealed by:** Bridge B (Ch. 13): quantized elastic waves + photoelastic coupling | **Branch:** EEE/CE (Brillouin OTDR for structural health monitoring in pipelines, bridges, dams) | **→ Ch. 13**

---

**Cherenkov Radiation** Charged particle traveling faster than c/n emits a cone of radiation; cosθ = c/nv. **Layer:** L2 | **Revealed by:** Bridge B.c (Ch. 11): constructive interference of the classical radiation cone; nuclear reactor pool glows blue from this | **Branch:** EEE (particle detectors; Cherenkov counters for particle ID) | **→ Ch. 12**

---

**Bremsstrahlung** Decelerated charged particle emits a broad photon spectrum; high-energy cutoff at hν_max = eV (Duane-Hunt). **Layer:** L0→L2 | **Revealed by:** Bridge B.c (Ch. 11) classically; quantum correction gives the spectrum | **Branch:** EEE (X-ray tubes; synchrotrons; radiation shielding design) | **→ Ch. 12**

---

**Doppler Effect** Wave frequency shifts with relative motion of source and observer; EM: f_obs = f₀√((1−β)/(1+β)); acoustic formula differs because sound has a medium. **Layer:** L2 | **Revealed by:** Bridge B.c (Ch. 11 EM): Lorentz transform of wave 4-vector; classical waves for acoustics | **Branch:** EEE (radar, lidar, Doppler ultrasound); ME/CE (acoustic flow meters, vibration analysis) | **→ Ch. 12**

---

**Blackbody Radiation** Thermal equilibrium emission follows Planck's law B_ν = (2hν³/c²)/(e^(hν/k_BT)−1); total power ∝ T⁴ (Stefan-Boltzmann); peak wavelength ∝ 1/T (Wien). **Layer:** L0→L2 | **Revealed by:** Bridge B.b (Ch. 10): quantized EM field energy (L0) + Bose-Einstein distribution (Bridge B.b); classical Rayleigh-Jeans gives the UV catastrophe | **Branch:** ME/CE/EEE (furnace design, thermal imaging, solar cell spectrum, satellite thermal control) | **→ Ch. 10**

---

**Optical Activity** A chiral medium rotates the polarization plane of light; opposite enantiomers rotate in opposite directions. **Layer:** L1→L2 | **Revealed by:** Bridge A+B (Ch. 12): molecular chirality at L1 → non-symmetric susceptibility tensor at L2 | **Branch:** ChE (pharmaceutical purity; sugar concentration); Biomedical (circular dichroism spectroscopy) | **→ Ch. 12**

---

**Second Harmonic Generation (SHG)** High-intensity light at ω in a non-centrosymmetric medium generates output at 2ω; requires phase matching. **Layer:** L1→L2 | **Revealed by:** Bridge B (Ch. 13): χ⁽²⁾ from broken inversion symmetry; nonlinear polarization P⁽²⁾ = ε₀χ⁽²⁾E² at 2ω | **Branch:** EEE (green laser pointers from 1064 nm YAG; frequency doubling in photonics labs) | **→ Ch. 13**

---

## 2.5 — Mechanical, Fluid, and Acoustic Effects

---

**Bernoulli Effect** Steady inviscid flow: p + ½ρv² + ρgz = const along a streamline; pressure decreases where flow speed increases. **Layer:** L2 | **Revealed by:** Bridge B.b (Ch. 16): Euler equation (Navier-Stokes, η = 0) integrated along a streamline | **Branch:** ME/CE (aerodynamics, hydraulics, Venturi meters, Pitot tubes, carburetors) | **→ Ch. 16**

---

**Magnus Effect** Spinning body in cross-flow experiences lift F_L = ρΓL perpendicular to both velocity and spin axis (Kutta-Joukowski). **Layer:** L2 | **Revealed by:** Bridge B.b (Ch. 16): Navier-Stokes + rotation creates asymmetric pressure distribution | **Branch:** ME/CE (sports aerodynamics; Flettner rotor ships; gyroplane rotors) | **→ Ch. 16**

---

**Coanda Effect** A fluid jet attaches to and follows an adjacent curved surface due to entrainment and resulting low pressure. **Layer:** L2 | **Revealed by:** Bridge B.b (Ch. 16): viscous entrainment creates sub-ambient pressure between jet and surface | **Branch:** ME/CE (fluidic devices; VTOL aircraft; high-lift airfoils; industrial burners) | **→ Ch. 16**

---

**Reynolds Number Transition / Turbulence** Flow is laminar below critical Re = ρvL/η; nonlinear inertial terms dominate above it and flow becomes chaotic turbulence; no closed-form Layer-3 model exists. **Layer:** L2 | **Revealed by:** Bridge B.b (Ch. 16): nonlinear (v·∇)v term in Navier-Stokes; where L2 refuses to lump cleanly | **Branch:** ME/CE/ChE (pipe flow, aerodynamics, reactor mixing, heat exchanger performance) | **→ Ch. 16**

---

**Kelvin-Helmholtz Instability** Small perturbations at a shear interface between fluids of different velocities grow exponentially into vortices. **Layer:** L2 | **Revealed by:** Bridge B.b (Ch. 16): linear stability of Navier-Stokes at a shear interface | **Branch:** ME/CE (ocean-atmosphere interface; fuel atomization; wind-driven waves; cloud streaks) | **→ Ch. 16**

---

**Rayleigh-Taylor Instability** Dense fluid on top of light fluid is unstable; perturbations grow with rate γ = √(Akg) where A is the Atwood number. **Layer:** L2 | **Revealed by:** Bridge B.b + B.d (Ch. 16): Navier-Stokes + gravity; buoyancy on density perturbations | **Branch:** CE/ME (geophysical flows; nuclear fusion implosion; ocean overturning; salt diapirs) | **→ Ch. 16**

---

**Rayleigh-Bénard Convection** Organized convection cells form above critical Rayleigh number Ra = gαΔTd³/νκ in a fluid heated from below; canonical pattern-formation example. **Layer:** L2 | **Revealed by:** Bridge B.b (Ch. 16): Navier-Stokes + thermal diffusion + buoyancy; linear stability → critical Ra | **Branch:** ME/CE/ChE (building HVAC, electronics cooling, geophysical convection, industrial furnaces) | **→ Ch. 16**

---

**Acoustic Cavitation** Large rarefaction pressures nucleate bubbles that collapse violently, producing ~5000 K and ~1000 atm locally. **Layer:** L2 | **Revealed by:** Bridge B.b (Ch. 16): Rayleigh-Plesset bubble dynamics from Navier-Stokes | **Branch:** ME/ChE (ultrasonic cleaning, sonochemistry, food processing); CE (pump and propeller erosion) | **→ Ch. 16**

---

**Resonance** A system driven at natural frequency ω₀ = 1/√(LC) responds maximally; Q factor quantifies sharpness; all domains share the same second-order ODE. **Layer:** L2→L3 | **Revealed by:** Bridge C (Ch. 15/18): Lẍ + Rẋ + x/C = F has a resonant peak identical in every physical domain | **Branch:** All (RLC circuits, mechanical vibration, acoustic cavities, MEMS, optical resonators) | **→ Ch. 18**

---

**Surface Acoustic Waves (SAW)** Acoustic waves guided along a solid surface, decaying exponentially with depth; Rayleigh waves (elliptical motion) and Love waves (transverse) are primary modes. **Layer:** L2 | **Revealed by:** Bridge B (Ch. 9/16): elastic wave equation + free-surface boundary condition | **Branch:** EEE/ME/CE (SAW filters in mobile phones; chemical sensors; structural health monitoring) | **→ Ch. 16**

---

**Thermal Expansion** Most materials expand on heating because thermal vibrations in an anharmonic interatomic potential give a positive mean displacement. **Layer:** L1→L2 | **Revealed by:** Bridge B (Ch. 10): anharmonic interatomic potential (L1) → positive Grüneisen parameter → macroscopic α = (1/V)(∂V/∂T)_P | **Branch:** ME/CE (expansion joints, bimetallic actuators, precision machining, bridge joints) | **→ Ch. 10**

---

## 2.6 — Gravitational and Relativistic Effects

---

**Equivalence Principle** Gravitational and inertial mass are exactly equal; free fall is locally indistinguishable from absence of gravity. **Layer:** L0 | **Revealed by:** Ch. 0 §0.3 + Ch. 8: geodesic equation describes free fall with no force; gravity is geometry | **Branch:** ME (inertial navigation; GPS/INS fusion needed because accelerometers cannot separate gravity from acceleration) | **→ Ch. 8**

---

**Gravitational Time Dilation** Clocks deeper in a gravitational well run slower; Δf/f = ΔΦ/c². **Layer:** L0 | **Revealed by:** Ch. 8 Bridge B.d: metric g₀₀ = 1 + 2Φ/c²; proper time dτ² = g₀₀ dt² | **Branch:** EEE (GPS: without +45 μs/day correction positional error is ~11 km/day) | **→ Ch. 8**

---

**Gravitational Redshift** Photons climbing out of a gravitational well lose energy and shift to lower frequency; Δν/ν = −ΔΦ/c². **Layer:** L0 | **Revealed by:** Ch. 8: energy conservation for photon E = hν in gravitational field; confirmed by Pound-Rebka 1959 | **Branch:** EEE (precision atomic clocks; gravitational wave detector calibration) | **→ Ch. 8**

---

**Gravitational Waves** Accelerating masses produce spacetime ripples propagating at c; strain h = ΔL/L; first detected by LIGO in 2015. **Layer:** L0 | **Revealed by:** Ch. 8: linearized Einstein equations give wave equation for hμν; two transverse-traceless polarizations | **Branch:** EEE (gravitational wave detectors are precision optical interferometers at Layer 3) | **→ Ch. 8**

---

**Gravitational Lensing** Massive objects deflect light by α = 4GM/c²b (twice Newtonian); confirmed by Eddington 1919. **Layer:** L0 | **Revealed by:** Ch. 8: photon geodesic in Schwarzschild metric; factor 2 over Newton because both spatial and temporal metric components contribute | **Branch:** Astronomy (dark matter mapping; gravitational telescopes) | **→ Ch. 8**

---

**Frame Dragging (Lense-Thirring)** Rotating massive body drags surrounding spacetime; satellite orbital plane precesses at Ω_LT = 2GJ/c²r³. **Layer:** L0 | **Revealed by:** Ch. 8: off-diagonal g₀ᵢ components of Kerr metric; confirmed Gravity Probe B 2011 | **Branch:** EEE (precise orbit determination for navigation satellites) | **→ Ch. 8**

---

## 2.7 — Nuclear and Particle Effects

---

**Radioactive Decay (α, β, γ)** Unstable nuclei transform spontaneously: α-decay (He nucleus tunnels through Coulomb barrier); β-decay (n↔p via weak SU(2) force); γ-emission (nuclear excitation photon). **Layer:** L0→L1 | **Revealed by:** Ch. 0 §0.4.3 (SU(2) → β); Ch. 4 tunneling → α; Ch. 5 nuclear levels → γ | **Branch:** ME/CE/ChE (nuclear reactors, radiation shielding, medical imaging, geological dating) | **→ Ch. 6**

---

**Nuclear Fission** A fissile nucleus absorbs a slow neutron, splits into two lighter nuclei, releases ~2.4 neutrons and ~200 MeV per event; chain reaction possible. **Layer:** L0→L1 | **Revealed by:** Ch. 6: nuclear binding energy curve (SU(3) residual) + fission barrier tunneling | **Branch:** ME/ChE (nuclear power plants; naval propulsion; weapon physics) | **→ Ch. 6**

---

**Nuclear Fusion** Light nuclei fuse under extreme conditions; stellar fusion requires quantum tunneling through Coulomb barrier at thermal velocities. **Layer:** L0→L1 | **Revealed by:** Ch. 6: strong nuclear force + Gamow tunneling peak; plasma confinement physics | **Branch:** ME (fusion reactor engineering — ITER; plasma engineering) | **→ Ch. 6**

---

**Pair Production and Annihilation** Photon near nucleus converts to e⁺e⁻ pair (hν ≥ 2mₑc² = 1.022 MeV); pair annihilates into two back-to-back 511-keV photons. **Layer:** L0 | **Revealed by:** Ch. 0 §0.5: antimatter solutions of Dirac equation; fundamental QED process | **Branch:** EEE (PET scanners; radiation detectors; radiotherapy) | **→ Ch. 3**

---

**Mössbauer Effect** A nucleus in a crystal emits or absorbs a γ-ray with no recoil (whole crystal recoils); linewidth ΔE/E ~ 10⁻¹³. **Layer:** L1 | **Revealed by:** Ch. 6: zero-phonon transition; Lamb-Mössbauer factor gives recoil-free fraction | **Branch:** ME/CE (residual stress in steel; geological dating; Pound-Rebka gravitational redshift test) | **→ Ch. 6**

---

**Neutrino Oscillations** Neutrinos produced in flavor eigenstates (νₑ, νμ, ντ) propagate as mass eigenstate superpositions; flavor oscillates with distance L_osc ∝ E/Δm². **Layer:** L0 | **Revealed by:** Ch. 0 §0.8 (PMNS matrix); requires neutrino masses → extension of L_SM → in f(φ) placeholder; direct evidence the action in Ch. 0 is incomplete | **Branch:** Metrology (reactor neutrino monitoring); physics frontier | **→ Epilogue**

---

## 2.8 — Surface and Interface Phenomena

---

**Surface Tension / Young-Laplace** Liquid-vapor interface has surface energy γ per area; pressure difference across curved interface Δp = γ(1/R₁ + 1/R₂). **Layer:** L1→L2 | **Revealed by:** Bridge B.b (Ch. 10): broken bonds at surface raise free energy; thermodynamic minimization gives Young-Laplace | **Branch:** ChE/ME/CE (bubble dynamics, droplet coalescence, capillary pressure in porous media, coating flows) | **→ Ch. 16**

---

**Capillary Action** Liquid rises in a narrow tube to h = 2γcosθ/(ρgr); balance of surface tension and hydrostatic pressure. **Layer:** L2 | **Revealed by:** Bridge B.b + B.d (Ch. 10 + Ch. 8): Young-Laplace pressure + hydrostatic equilibrium | **Branch:** CE/ChE (groundwater, inkjet, microfluidics, concrete moisture, lab-on-chip) | **→ Ch. 16**

---

**Wetting and Contact Angle** Contact angle θ satisfies Young's equation γ_SV = γ_SL + γ_LV cosθ; determines whether a liquid spreads on a surface. **Layer:** L1→L2 | **Revealed by:** Bridge B.b (Ch. 10): free energy minimization over three interface energies; molecular origins (L1) determine γ values | **Branch:** ME/ChE/CE (waterproofing; adhesion; coating; microfluidic valves; anti-icing surfaces) | **→ Ch. 16**

---

**Osmotic Pressure** Solution separated from pure solvent by semipermeable membrane develops pressure Π = cRT (van't Hoff, dilute limit). **Layer:** L2 | **Revealed by:** Bridge B.b (Ch. 10): solute lowers chemical potential of solvent (entropy of mixing); thermodynamic equilibrium gives van't Hoff | **Branch:** ChE/CE/Biomedical (desalination, drug delivery, cell mechanics, wastewater treatment) | **→ Ch. 10**

---

**Marangoni Effect (Thermocapillary Flow)** Gradients in surface tension (from T or concentration gradients) drive surface flow from low to high surface tension; causes "tears of wine." **Layer:** L2 | **Revealed by:** Bridge B.b + B.c (Ch. 16): temperature/concentration-dependent γ → tangential stress boundary condition in Navier-Stokes | **Branch:** ME/ChE (crystal growth, thin-film uniformity, welding pool dynamics, inkjet) | **→ Ch. 16**

---

**Leidenfrost Effect** A droplet on a surface far above boiling point levitates on a vapor cushion, dramatically reducing heat transfer and extending lifetime. **Layer:** L2 | **Revealed by:** Bridge B.b (Ch. 16): vapor pressure exceeds ambient; vapor film insulates droplet by buoyancy and pressure | **Branch:** ME/ChE (spray cooling; nuclear safety — departure from nucleate boiling; quenching; droplet manipulation) | **→ Ch. 16**

---

**Electrowetting** Applied voltage modifies contact angle of a conducting droplet: cosθ(V) = cosθ₀ + εV²/2γd; contact angle decreases with voltage. **Layer:** L1→L2 | **Revealed by:** Bridge B.c + B.b (Ch. 11, 10): electric field energy in dielectric modifies effective solid-liquid surface energy | **Branch:** EEE/ChE (lab-on-chip; digital microfluidics; electrowetting displays; adaptive lenses) | **→ Ch. 16**

---

**Triboelectric Effect** Contact and separation of dissimilar materials transfers charge via surface electron transfer; sign depends on triboelectric series. **Layer:** L1→L2 | **Revealed by:** Bridge A+B (Ch. 13): work function difference (L1) drives charge transfer; detailed mechanism for insulators still debated | **Branch:** EEE (triboelectric nanogenerators for energy harvesting; ESD hazard in manufacturing) | **→ Ch. 13**

---

## 2.9 — Cross-Domain and Emerging Phenomena

---

**Johnson-Nyquist Noise (Thermal Noise)** A resistor R at temperature T generates voltage noise S_V = 4k_BTR (white spectrum); unavoidable floor on electronic signal detection. **Layer:** L1→L2 | **Revealed by:** Bridge B.e (Ch. 13): fluctuation-dissipation theorem connects Kubo conductivity to equilibrium fluctuations; S_V = 4k_BT Re[Z(ω)] | **Branch:** EEE (noise floor of all analog systems; antenna temperature; precision measurement) | **→ Ch. 13**

---

**Shot Noise** Discreteness of electron charge gives current noise S_I = 2eI (Poissonian); Fano factor F = S_I/2eI measures deviation from Poissonian due to correlations. **Layer:** L1→L2 | **Revealed by:** Bridge B.e (Ch. 13): quantized charge (Noether U(1) from Ch. 0) + Poisson statistics of independent tunnel events | **Branch:** EEE (detector sensitivity limits; qubit readout noise; characterizing quantum transport) | **→ Ch. 13**

---

**Surface Plasmon Resonance (SPR)** Collective electron oscillations at metal-dielectric interface couple resonantly to evanescent EM waves; resonance is exquisitely sensitive to dielectric environment. **Layer:** L1→L2 | **Revealed by:** Bridge B.c (Ch. 11): plasma frequency ω_p = √(ne²/ε₀m) (L1 electron density) + evanescent wave phase-matching condition | **Branch:** EEE/ChE (label-free biosensors for antigen-antibody binding; nanophotonic circuits) | **→ Ch. 13**

---

**Photovoltaic Effect** Photons absorbed in a p-n junction generate electron-hole pairs; built-in field separates them; quasi-Fermi level splitting gives open-circuit voltage. **Layer:** L1→L2 | **Revealed by:** Bridge A+B: photoelectric effect (L0→L1, Ch. 4) + band structure (L1, Ch. 6) + drift-diffusion from Kubo (Bridge B.e) | **Branch:** EEE (solar cells; photodetectors; image sensors) | **→ Ch. 13**

---

**Phonons** Quantized collective lattice vibrations; acoustic (gapless, in-phase) and optical (gapped, out-of-phase) branches; carry most heat in dielectrics. **Layer:** L1 | **Revealed by:** Ch. 6: many-body quantization of lattice vibrations; phonon is the boson of the elastic field, parallel to photon in EM | **Branch:** ME/EEE (thermal conductivity; electron-phonon scattering → R vs. T in metals; thermoelectric optimization) | **→ Ch. 6**

---

**Plasma Oscillations (Langmuir Waves)** Free electrons displaced from equilibrium oscillate collectively at ω_p = √(ne²/ε₀mₑ); EM waves cannot propagate for ω < ω_p. **Layer:** L1→L2 | **Revealed by:** Bridge B.c (Ch. 11): Kubo conductivity → complex ε(ω) → Re[ε] = 0 at ω_p | **Branch:** EEE (RF shielding; waveguide cutoff; surface plasmonics; UV reflectance edge of metals) | **→ Ch. 13**

---

**Electrophoresis** Charged particles migrate in an applied electric field at velocity v = μ_E E where μ_E = εζ/η (zeta potential ζ, viscosity η); electric and drag forces balance. **Layer:** L2 | **Revealed by:** Bridge B.c + B.b (Ch. 11, 16): Lorentz force on charged particle + Stokes drag from Navier-Stokes | **Branch:** ChE/Biomedical (gel electrophoresis for DNA; capillary electrophoresis; colloid separation) | **→ Ch. 16**

---

**Fluorescence** Photon absorption excites a molecule; after rapid vibrational relaxation, emission occurs at longer wavelength (Stokes shift); lifetime 1–10 ns. **Layer:** L1 | **Revealed by:** Ch. 5: electronic transitions between molecular orbitals; Franck-Condon (Born-Oppenheimer); Fermi's Golden Rule gives the rate | **Branch:** EEE/ChE/Biomedical (fluorescence microscopy; FRET sensors; LEDs; laser media; flow cytometry) | **→ Ch. 5**

---

**NMR and MRI** Nuclei with nonzero spin precess at Larmor frequency ω_L = γ_N B₀ in static field B₀; resonant RF pulse tips magnetization; free induction decay encodes structural information. **Layer:** L1 | **Revealed by:** Ch. 5: nuclear Zeeman effect; nuclear spin precession from the Pauli equation | **Branch:** EEE/Biomedical (MRI for medical imaging; NMR spectroscopy; NMR quantum computing) | **→ Ch. 5**

---

## 2.10 — Master Index (Alphabetical)

|Effect|Layer|Chapter|
|---|---|---|
|Acoustic cavitation|L2|16|
|Aharonov-Bohm effect|L1|5|
|Anderson localization|L1|13|
|Band gaps|L1|6|
|Bernoulli effect|L2|16|
|Berry phase|L1|7|
|Birefringence|L2|12|
|Blackbody radiation|L0→L2|10|
|Bloch's theorem|L1|6|
|Born-Oppenheimer approximation|L1|6|
|Bose-Einstein condensation|L1→L2|10|
|Bremsstrahlung|L0→L2|12|
|Brewster's angle|L2|12|
|Brillouin scattering|L1→L2|13|
|Capillary action|L2|16|
|Casimir effect|L0→L1|5|
|Cherenkov radiation|L2|12|
|Coanda effect|L2|16|
|Compton scattering|L0→L1|3|
|Coulomb blockade|L1→L2|7|
|de Broglie matter waves|L1|4|
|Quantum decoherence|L1→L2|10|
|Diffraction|L2|12|
|Doppler effect (EM)|L2|12|
|Doppler effect (acoustic)|L2|16|
|Eddy currents|L2|11|
|Electrophoresis|L2|16|
|Electrowetting|L1→L2|16|
|Equivalence principle|L0|8|
|Faraday rotation|L2|12|
|Faraday's law|L2|11|
|Fermi's golden rule|L1|6|
|Ferroelectric effect|L1→L2|10|
|Fine structure|L1|5|
|Flux quantization|L1→L2|7|
|Fluorescence|L1|5|
|Fractional QHE|L0→L1|Epilogue|
|Frame dragging (Lense-Thirring)|L0|8|
|Giant magnetoresistance (GMR)|L1→L2|7|
|Gravitational lensing|L0|8|
|Gravitational redshift|L0|8|
|Gravitational time dilation|L0|8|
|Gravitational waves|L0|8|
|Hall effect (classical)|L2|14|
|Heisenberg uncertainty principle|L1|4|
|Hyperfine structure|L1|5|
|Integer QHE|L1→L2|7|
|Johnson-Nyquist noise|L1→L2|13|
|Josephson effect|L1|7|
|Joule heating|L2→L3|13, 15|
|Kelvin-Helmholtz instability|L2|16|
|Kerr electro-optic effect|L1→L2|13|
|Kondo effect|L1→L2|13|
|Lamb shift|L0|Epilogue|
|Landau levels|L1|7|
|Leidenfrost effect|L2|16|
|Magnus effect|L2|16|
|Magnetostriction|L1→L2|13|
|Marangoni effect|L2|16|
|Meissner effect|L1→L2|7|
|MRI / NMR|L1|5|
|Mössbauer effect|L1|6|
|Neutrino oscillations|L0|Epilogue|
|Nuclear fission|L0→L1|6|
|Nuclear fusion|L0→L1|6|
|Optical activity|L1→L2|12|
|Osmotic pressure|L2|10|
|Pair production and annihilation|L0|3|
|Pauli exclusion principle|L0→L1|5|
|Peltier effect|L1→L2|13|
|Phonons|L1|6|
|Photoelectric effect|L0→L1|4|
|Photovoltaic effect|L1→L2|13|
|Piezoelectric effect|L1→L2|13|
|Plasma oscillations|L1→L2|13|
|Pockels effect|L1→L2|13|
|Quantum entanglement|L0→L1|4|
|Quantum Hall effect (integer)|L1→L2|7|
|Quantum Hall effect (fractional)|L0→L1|Epilogue|
|Quantum tunneling|L1|4|
|Quantum Zeno effect|L1|4|
|Rabi oscillations|L1|5|
|Radioactive decay|L0→L1|6|
|Raman scattering|L1→L2|6|
|Rayleigh scattering|L2|12|
|Rayleigh-Bénard convection|L2|16|
|Rayleigh-Taylor instability|L2|16|
|Refraction / Snell's law|L2|12|
|Resonance|L2→L3|18|
|Reynolds transition / turbulence|L2|16|
|Second harmonic generation|L1→L2|13|
|Seebeck effect|L1→L2|13|
|Shape memory effect|L2|10|
|Shot noise|L1→L2|13|
|Skin effect|L2|11|
|Spin Hall effect|L1|7|
|Spin-statistics theorem|L0|5|
|Spontaneous emission|L0→L1|5|
|Stark effect|L1|5|
|Stimulated emission|L0→L1|5|
|Superconductivity (BCS)|L1→L2|7|
|Superfluidity|L1→L2|10|
|Surface acoustic waves (SAW)|L2|16|
|Surface plasmon resonance|L1→L2|13|
|Surface tension / Young-Laplace|L1→L2|16|
|Thermal expansion|L1→L2|10|
|Thermionic emission|L1→L2|14|
|Thomson effect|L1→L2|13|
|Topological insulator states|L1|7|
|Total internal reflection|L2|12|
|Triboelectric effect|L1→L2|13|
|Wave interference|L2|12|
|Weyl semimetal|L1|7|
|Wetting and contact angle|L1→L2|16|
|Zeeman effect|L1|5|
|Zero-point energy|L1|4|

---

_End of Chapter 2. Return to it whenever a named effect appears in a later chapter._

---

_Next: Chapter 3 — Bridge A: The Quantum Descent_