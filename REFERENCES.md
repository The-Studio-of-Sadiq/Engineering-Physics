# REFERENCES.md — Sources for the Load-Bearing Claims

**Engineering Physics: Top Down** — provenance for every claim that carries
weight in the argument.

---

## How to read this file

This file traces every load-bearing factual claim back to its source, chapter by
chapter, in the order the book proceeds — Ch. 0 through Ch. 21 and the Epilogue —
so the reference chain mirrors the derivation chain. A claim in Ch. 7 that
echoes a structure introduced in Ch. 0 is filed under Ch. 7 and cross-references
back to Ch. 0, exactly as the book's own "Revealed by" / "→ Ch. X" convention
does.

**Design principle: a citation is a liability as well as an asset.** Attaching a
reference to a claim that does not need one, or that the reference does not
actually support, makes the book look better-sourced than it is. So every entry
here is typed, and the typing carries information.

### Evidence tiers

| Tier | Meaning | How it is cited |
|---|---|---|
| **[MEASURED]** | An experimentally measured number or a discovery, traceable to one primary paper (or a small number of them) | Full citation with DOI where one exists |
| **[DERIVED / TEXTBOOK]** | Standard, uncontested physics, not tied to a single paper — the kind of thing that appears identically in every graduate textbook on the subject | Cited to a standard textbook (`T#` below), because that is the honest citation. No single paper "discovered" the textbook derivation of the Wiedemann–Franz ratio, even though von Klitzing's *measurement* of it is a paper |
| **[THEORY]** | An original theoretical result, prediction, or no-go theorem — traceable to one or a small number of primary papers, but not itself an observation | Full citation with DOI to the primary theory paper(s). Kept distinct from [DERIVED / TEXTBOOK]: a *named original result* (BCS, ABJ anomaly, Nielsen–Ninomiya, Higgs mechanism, Abrikosov vortices) is credited to its authors' paper, not to a textbook, and distinct from [MEASURED]: a theoretical prediction is not a measurement even when it is later confirmed |
| **[SYNTHESIS]** | The book's own argument or pedagogical framing, not a fact borrowed from the literature | Flagged explicitly rather than given a decorative citation. This is the tier that matters most: the book's central claims live here, and marking them is the point |
| **[TARGET]** | A forward-looking engineering target, design goal, or institutional projection — documented by the responsible body but *not* an observed result and not yet achieved | Cited to the project's own documentation. Kept distinct from [MEASURED]: a goal is not data, and must never be quoted as though the specification had been met |

### Numbered citation key

Each entry below carries an `[R#]` label and names the chapter(s) it serves, in
the "Ch." column of the key table. **Chapter prose does not carry inline `[R#]`
markers** — the manuscript cites by author and year in the sentence
("Pound and Rebka (1959)", "von Klitzing, 1980"), which reads better in
continuous technical prose than a bracketed number would. The `[R#]` labels are
therefore an index *into this file*, not a citation syntax the text depends on.
When you add a source, give it the next free number, add it to the key table with
its chapter coverage, and put the full entry in that chapter's section below.

Textbook references are numbered `[T#]` and collected in the Textbooks section.

| # | Source | Ch. |
|---|---|---|
| R1 | CODATA recommended values (NIST) | 0, 4, 7, 10, 11 |
| R2 | Particle Data Group, *Review of Particle Physics* | 0 |
| R3 | Englert & Brout; Higgs; Guralnik–Hagen–Kibble (1964) | 0 |
| R4 | Wu et al., parity violation (1957) | 0 |
| R5 | ACME Collaboration, electron EDM bound (2018) | 0 |
| R6 | Georgi, Quinn & Weinberg, coupling unification (1974) | 0 |
| R7 | Dirac, "The Quantum Theory of the Electron" (1928) | 3 |
| R8 | Anderson, positron (1933) | 3 |
| R9 | Foldy & Wouthuysen (1950) | 3 |
| R10 | Rydberg (1890) | 4 |
| R11 | Stern & Gerlach (1922) | 5 |
| R12 | Lamb & Retherford (1947) | 5 |
| R13 | BIPM, *SI Brochure*, 9th ed. | 5, 7 |
| R14 | Bragg (1913) | 6 |
| R15 | von Weizsäcker, semi-empirical mass formula (1935) | 6 |
| R16 | Geiger & Nuttall (1911–12) | 6 |
| R17 | ITER Organization, project goals | 6 |
| R18 | Berry, quantal phase factors (1984) | 7 |
| R19 | von Klitzing, Dorda & Pepper (1980) | 7, 13 |
| R20 | Adler (1969); Bell & Jackiw (1969) | 7 |
| R21 | Nielsen & Ninomiya (1981) | 7 |
| R22 | Huang et al., chiral anomaly in TaAs (2015) | 7 |
| R23 | Bardeen, Cooper & Schrieffer (1957) | 7 |
| R24 | Deaver & Fairbank; Doll & Näbauer (1961) | 7 |
| R25 | Josephson (1962) | 7 |
| R26 | Abrikosov (1957) | 7 |
| R27 | Pound & Rebka (1959) | 8 |
| R28 | Everitt et al., Gravity Probe B (2011) | 8 |
| R29 | Abbott et al., GW150914 (2016) | 8 |
| R30 | Einstein, Mercury precession (1915) | 8 |
| R31 | Dyson, Eddington & Davidson (1920); Shapiro et al. (2004) | 8 |
| R32 | Ashby, relativity in GPS (2003) | 8 |
| R33 | Zurek, decoherence (2003) | 9 |
| R34 | Boltzmann, Stefan's law (1884) | 10 |
| R35 | Wien, displacement law (1896) | 10 |
| R36 | Landau, phase transitions (1937) | 10 |
| R37 | Maxwell, dynamical theory of the EM field (1865) | 11 |
| R38 | Kubo, linear response (1957) | 13 |
| R39 | Wiedemann & Franz (1853) | 13 |
| R40 | Mott & Jones, theory of metals and alloys (1936) | 13 |
| R41 | Hall (1879) | 14 |
| R42 | Richardson; Dushman (1921/1923) | 14 |
| R43 | BIPM Resolution 1, 26th CGPM — 2019 SI redefinition | 14 |
| R44 | IEC 60751:2008, Pt100 RTD | 14 |
| R45 | Reynolds (1883) | 15–20 |
| R46 | Kolmogorov (1941) | 15–20 |
| R47 | Dittus & Boelter (1930) | 19, 20 |
| R48 | Terzaghi, *Erdbaumechanik* (1925) | 20 |
| R49 | Cooley & Tukey, FFT (1965) | 18 |
| R50 | Kalman, general theory of control systems (1960) | 20, 21 |

---

## Chapter 0 — The Equation (Standard Model + Einstein–Hilbert action)

**[MEASURED] [R1] Newton's gravitational constant, $G = 6.674\times 10^{-11}\,\text{N·m}^2/\text{kg}^2$**
Source: CODATA recommended values (NIST). This is the least precisely known fundamental constant (relative uncertainty ~2.2×10⁻⁵), a fact worth noting alongside the number itself.
Link: https://physics.nist.gov/cgi-bin/cuu/Value?bg

**[MEASURED] [R2] Weinberg angle, $\theta_W \approx 28.7°$ ($\sin^2\theta_W \approx 0.231$)**
Source: Particle Data Group, *Review of Particle Physics* (current edition), Electroweak Model section.
Link: https://pdg.lbl.gov/

**[MEASURED] [R2] W and Z boson masses ($m_W \approx 80.4$ GeV, $m_Z \approx 91.2$ GeV)**
Source: Particle Data Group, *Review of Particle Physics*, Gauge and Higgs Boson Summary Table.

**[DERIVED / TEXTBOOK] [R2] Higgs vacuum expectation value $v \approx 246$ GeV**
Derived from the measured Fermi constant $G_F$ via $v = (\sqrt{2}G_F)^{-1/2}$; this is a standard electroweak-fit result, not an independent measurement. Tiered [DERIVED / TEXTBOOK] accordingly — the input $G_F$ is [MEASURED] (see R1/R2), the VEV quoted here is a fit-derived quantity.

**[MEASURED] [R3] Higgs boson discovery and mass ($m_h = 125.09$ GeV)**
Source: ATLAS Collaboration, "Observation of a new particle in the search for the Standard Model Higgs boson with the ATLAS detector at the LHC," *Phys. Lett. B* 716, 1–29 (2012). DOI: 10.1016/j.physletb.2012.08.020
Companion paper: CMS Collaboration, "Observation of a new boson at a mass of 125 GeV with the CMS experiment at the LHC," *Phys. Lett. B* 716, 30–61 (2012). DOI: 10.1016/j.physletb.2012.08.021
Combined ATLAS+CMS mass measurement, 125.09 ± 0.24 GeV: ATLAS+CMS Collaborations, *Phys. Rev. Lett.* 114, 191803 (2015). DOI: 10.1103/PhysRevLett.114.191803

**[THEORY] [R3] Original Higgs-mechanism theory papers (1964)**
- Englert, F. & Brout, R., "Broken Symmetry and the Mass of Gauge Vector Mesons," *Phys. Rev. Lett.* 13, 321–323 (1964). DOI: 10.1103/PhysRevLett.13.321
- Higgs, P.W., "Broken Symmetries, Massless Particles and Gauge Fields," *Phys. Lett.* 12, 132–133 (1964). DOI: 10.1016/0031-9163(64)91136-9
- Higgs, P.W., "Broken Symmetries and the Masses of Gauge Bosons," *Phys. Rev. Lett.* 13, 508–509 (1964). DOI: 10.1103/PhysRevLett.13.508
- Guralnik, G.S., Hagen, C.R., Kibble, T.W.B., "Global Conservation Laws and Massless Particles," *Phys. Rev. Lett.* 13, 585–587 (1964). DOI: 10.1103/PhysRevLett.13.585

**[MEASURED] [R4] Wu et al. parity-violation experiment (1957)**
Wu, C.S., Ambler, E., Hayward, R.W., Hoppes, D.D., Hudson, R.P., "Experimental Test of Parity Conservation in Beta Decay," *Phys. Rev.* 105, 1413–1415 (1957). DOI: 10.1103/PhysRev.105.1413
This is the direct source for the book's claim that the cobalt-60 nucleus emitted electrons preferentially opposite to its spin.

**[MEASURED] [R5] Electron electric dipole moment — experimental upper bound, $d_e < 1.8\times 10^{-26}\,e\cdot\text{cm}$**
Source: ACME Collaboration (Andreev, V. et al.), "Improved limit on the electric dipole moment of the electron," *Nature* 562, 355–360 (2018). DOI: 10.1038/s41586-018-0599-8
Tier note: this is an *experimental bound/limit* — a null-result exclusion, not a
measured central value. [MEASURED] is retained because the limit is set by experiment,
but the claim it supports is the inequality, never a value for $d_e$; the number must
not be cited as though $d_e$ had been resolved.
The strong-CP bound $|\theta_{QCD}| < 10^{-10}$ derived from neutron EDM bounds is [DERIVED / TEXTBOOK] — see T8, Ch. 19.

**[SYNTHESIS] [R6] Gauge coupling unification near $10^{16}$ GeV "suggesting a GUT"**
A theoretical extrapolation (running couplings under the MSSM nearly meet), not an experimental measurement — no GUT has been observed. The running-coupling calculation itself is standard: Georgi, H., Quinn, H.R., Weinberg, S., "Hierarchy of Interactions in Unified Gauge Theories," *Phys. Rev. Lett.* 33, 451 (1974), DOI: 10.1103/PhysRevLett.33.451. The word "suggesting" in the book's text is doing real work; this is not a confirmed discovery and must not be cited as one.

---

## Chapter 1 — The Action Principle
No claim in this chapter relies on external experimental data. Lagrangian mechanics, Noether's theorem, and Hamilton–Jacobi theory are [DERIVED / TEXTBOOK] — see T1, T13.

---

## Chapter 2 — Phenomena Catalogue
An index, not a source of new claims. Every phenomenon listed is sourced under the chapter where it is actually derived (see the "Revealed by → Ch. X" column in the book). No separate entries needed; cross-reference the chapter listed.

---

## Chapter 3 — Bridge A: Dirac → Schrödinger

**[THEORY] [R7] Anomalous magnetic moment $g_e = 2$ as a pre-1928 mystery, resolved by the Dirac equation**
Historical mystery: no single citable "discovery" — $g=2$ emerged from spectroscopic anomalies (anomalous Zeeman effect) through the 1920s. The resolution is the theory paper: Dirac, P.A.M., "The Quantum Theory of the Electron," *Proc. R. Soc. Lond. A* 117, 610–624 (1928). DOI: 10.1098/rspa.1928.0023
Tier note: tiered [THEORY] because the cited source is Dirac's theoretical prediction of $g=2$; the 1920s spectroscopic anomaly that motivated it is the empirical observation, the resolution is not.

**[MEASURED] [R8] Discovery of the positron (Anderson, 1932/1933)**
Anderson, C.D., "The Positive Electron," *Phys. Rev.* 43, 491–494 (1933). DOI: 10.1103/PhysRev.43.491
The particle was photographed 2 August 1932; this is the full data paper. A short note appeared earlier in *Science* 76, 238 (1932).

**[DERIVED / TEXTBOOK] [R9] Foldy–Wouthuysen transformation and its terms (Zeeman, spin-orbit, Darwin)**
Foldy, L.L. & Wouthuysen, S.A., "On the Dirac Theory of Spin 1/2 Particles and Its Non-Relativistic Limit," *Phys. Rev.* 78, 29–36 (1950). DOI: 10.1103/PhysRev.78.29

---

## Chapter 4 — Schrödinger Equation, Hydrogen Atom

**[MEASURED] [R10] Rydberg formula (empirical, 1888/1890) and Rydberg constant**
Rydberg, J.R., "On the Structure of the Line-Spectra of the Chemical Elements," *Phil. Mag.*, Series 5, Vol. 29, 331–337 (1890). Formula first presented in a paper read to the Lund Physiographic Society, 1888.
Modern precision value $R_\infty = 1.0973731568539\times 10^7\,\text{m}^{-1}$: CODATA (NIST), one of the most precisely measured constants in physics.
Link: https://physics.nist.gov/cgi-bin/cuu/Value?ryd

---

## Chapter 5 — Spin, Many-Electron Systems, Periodic Table

**[MEASURED] [R11] Stern–Gerlach experiment (1922)**
Gerlach, W. & Stern, O., "Der experimentelle Nachweis der Richtungsquantelung im Magnetfeld," *Zeitschrift für Physik* 9, 349–352 (1922). DOI: 10.1007/BF01326983

**[MEASURED] [R12] Lamb shift measurement**
Lamb, W.E. & Retherford, R.C., "Fine Structure of the Hydrogen Atom by a Microwave Method," *Phys. Rev.* 72, 241–243 (1947). DOI: 10.1103/PhysRev.72.241
The modern precision value of ~1057.8 MHz splitting comes from later refinements; the 1947 paper is the original discovery.

**[DERIVED / TEXTBOOK] [R13] Cesium atomic clock definition of the SI second (9,192,631,770 Hz hyperfine transition)**
Source: BIPM, *The International System of Units (SI Brochure)*, 9th edition, definition of the second.
Link: https://www.bipm.org/en/publications/si-brochure
Tier note: the second is a DEFINITION (SI Brochure), fixed exactly, not a measured frequency — same class as the 2019 redefinition (R43). Tiered with the standards, not with measurements.

**[MEASURED] [R1] Bohr magneton, $\mu_B = 9.274\times 10^{-24}$ J/T**
Source: CODATA recommended values (NIST).
Link: https://physics.nist.gov/cgi-bin/cuu/Value?mub

---

## Chapter 6 — Band Theory, Bonding, Nuclear Physics

**[MEASURED] [R14] Bragg reflection condition**
Bragg, W.L., "The Diffraction of Short Electromagnetic Waves by a Crystal," *Proc. Camb. Phil. Soc.* 17, 43–57 (1913).
Bragg's law itself, $n\lambda = 2d\sin\theta$; the book's application to electron-wave band gaps at the Brillouin zone boundary is [DERIVED / TEXTBOOK] — see T2, Ch. 7–9.

**[DERIVED / TEXTBOOK] [R15] Semi-Empirical Mass Formula (Bethe–Weizsäcker) and its coefficients**
Weizsäcker, C.F. von, "Zur Theorie der Kernmassen," *Zeitschrift für Physik* 96, 431–458 (1935). DOI: 10.1007/BF01337700
Current best-fit coefficients ($a_V=15.8$ MeV, $a_S=18.3$ MeV, $a_C=0.714$ MeV, $a_A=23.2$ MeV, $\delta=\pm12$ MeV): standard textbook values — see T4, Ch. 3.
Binding-energy-per-nucleon data (peak at $^{56}$Fe, 8.79 MeV): NNDC Atomic Mass Evaluation. Link: https://www.nndc.bnl.gov/

**[DERIVED / TEXTBOOK] [R16] Geiger–Nuttall law**
Geiger, H. & Nuttall, J.M., "The ranges of the α particles from various radioactive substances," *Phil. Mag.* 22, 613–621 (1911); follow-up, *Phil. Mag.* 23, 439 (1912).
Modern half-life data spanning $^{212}$Po to $^{232}$Th: NNDC.

**[TARGET] [R17] ITER fusion energy gain target, $Q \geq 10$**
Source: ITER Organization, official project documentation. Link: https://www.iter.org/sci/Goals
Tier note: this is a design TARGET, not an achieved or measured value - $Q\ge10$ is a forward-looking engineering goal, and the achieved gain to date is well below unity. Flagged so the projection is never cited as a measurement.

---

## Chapter 7 — Topology, Quantum Hall Effect, Superconductivity

**[THEORY] [R18] Berry phase**
Berry, M.V., "Quantal Phase Factors Accompanying Adiabatic Changes," *Proc. R. Soc. Lond. A* 392, 45–57 (1984). DOI: 10.1098/rspa.1984.0023
Tier note: tiered [THEORY] - Berry's 1984 adiabatic-phase paper is a theoretical result; experimental realisations (e.g. polarisation as a spin-1 Berry phase) are demonstrations, not the cited source.

**[MEASURED] [R19] Von Klitzing's discovery of the (integer) quantum Hall effect (1980)**
Klitzing, K. von, Dorda, G., Pepper, M., "New Method for High-Accuracy Determination of the Fine-Structure Constant Based on Quantized Hall Resistance," *Phys. Rev. Lett.* 45, 494–497 (1980). DOI: 10.1103/PhysRevLett.45.494
Quantization to 1 part in $10^9$ is repeatedly re-confirmed metrologically; see BIPM/NIST resistance-standard documentation for current figures.

**[THEORY] [R20] Adler–Bell–Jackiw chiral anomaly (original theory papers, 1969)**
- Adler, S.L., "Axial-Vector Vertex in Spinor Electrodynamics," *Phys. Rev.* 177, 2426–2438 (1969). DOI: 10.1103/PhysRev.177.2426
- Bell, J.S. & Jackiw, R., "A PCAC puzzle: $\pi^0\to\gamma\gamma$ in the $\sigma$-model," *Nuovo Cimento A* 60, 47–61 (1969). DOI: 10.1007/BF02823296

**[THEORY] [R21] Nielsen–Ninomiya (no-go) theorem for chiral fermions on a lattice**
Nielsen, H.B. & Ninomiya, M., "Absence of Neutrinos on a Lattice: I. Proof by Homotopy Theory," *Nucl. Phys. B* 185, 20–40 (1981). DOI: 10.1016/0550-3213(82)90011-6
Part II: *Nucl. Phys. B* 193, 173–194 (1981). DOI: 10.1016/0550-3213(81)90524-1

**[MEASURED] [R22] Negative longitudinal magnetoresistance from the chiral anomaly, observed in TaAs (2015)**
Huang, X. et al., "Observation of the Chiral-Anomaly-Induced Negative Magnetoresistance in 3D Weyl Semimetal TaAs," *Phys. Rev. X* 5, 031023 (2015). DOI: 10.1103/PhysRevX.5.031023

**[THEORY] [R23] BCS theory of superconductivity (1957)**
Bardeen, J., Cooper, L.N., Schrieffer, J.R., "Theory of Superconductivity," *Phys. Rev.* 108, 1175–1204 (1957). DOI: 10.1103/PhysRev.108.1175
The universal gap ratio $2\Delta(0)/k_BT_c = 3.528$ is a prediction of this paper, confirmed across conventional superconductors — [DERIVED / TEXTBOOK] for the confirming measurements; see T5, Ch. 3, for the standard compiled comparison table.

**[MEASURED] [R24] Flux quantization in superconducting rings (1961, two independent groups)**
- Deaver, B.S. & Fairbank, W.M., "Experimental Evidence for Quantized Flux in Superconducting Cylinders," *Phys. Rev. Lett.* 7, 43–46 (1961). DOI: 10.1103/PhysRevLett.7.43
- Doll, R. & Näbauer, M., "Experimental Proof of Magnetic Flux Quantization in a Superconducting Ring," *Phys. Rev. Lett.* 7, 51–52 (1961). DOI: 10.1103/PhysRevLett.7.51
Flux quantum $\Phi_0 = h/2e = 2.067833848\times 10^{-15}$ Wb: CODATA (NIST). Link: https://physics.nist.gov/cgi-bin/cuu/Value?flxquhs2e

**[THEORY] [R25] Josephson effect (theory, 1962)**
Josephson, B.D., "Possible new effects in superconductive tunnelling," *Phys. Lett.* 1, 251–253 (1962). DOI: 10.1016/0031-9163(62)91369-0
Josephson constant $K_J = 2e/h = 483597.8484\ldots\times 10^9$ Hz/V (exact since the 2019 SI redefinition): CODATA (NIST). Link: https://physics.nist.gov/cgi-bin/cuu/Value?kjos

**[THEORY] [R26] Abrikosov vortices (theory, 1957; Nobel Prize 2003)**
Abrikosov, A.A., "On the Magnetic Properties of Superconductors of the Second Group," *Sov. Phys. JETP* 5, 1174–1182 (1957) [Zh. Eksp. Teor. Fiz. 32, 1442 (1957)].

**[MEASURED] [R27] Quantized conductance of a point contact (1988)**
van Wees, B.J. et al., "Quantized Conductance of Point Contacts in a Two-Dimensional Electron Gas," *Phys. Rev. Lett.* 60, 848–850 (1988). DOI: 10.1103/PhysRevLett.60.848
Independently: Wharam, D.A. et al., *J. Phys. C* 21, L209 (1988).

---

## Chapter 8 — Bridge B.d: General Relativity → Newton's Law

**[MEASURED] [R28] Pound–Rebka gravitational redshift experiment (1959)**
Pound, R.V. & Rebka, G.A., "Gravitational Red-Shift in Nuclear Resonance," *Phys. Rev. Lett.* 3, 439–441 (1959). DOI: 10.1103/PhysRevLett.3.439
Measured $\Delta\nu/\nu \approx -2.5\times 10^{-15}$ over 22.5 m, confirmed to ~10%; refined by Pound & Snider, *Phys. Rev. Lett.* 13, 539 (1964), to ~1%.

**[MEASURED] [R29] Gravity Probe B: frame dragging and geodetic precession (2011)**
Everitt, C.W.F. et al., "Gravity Probe B: Final Results of a Space Experiment to Test General Relativity," *Phys. Rev. Lett.* 106, 221101 (2011). DOI: 10.1103/PhysRevLett.106.221101
Measured frame-dragging drift: $-37.2 \pm 7.2$ mas/yr vs. GR prediction $-39.2$ mas/yr — consistent with the book's 39 mas/yr figure within quoted precision.

**[MEASURED] [R30] LIGO first direct detection of gravitational waves, GW150914 (2016)**
Abbott, B.P. et al. (LIGO Scientific and Virgo Collaborations), "Observation of Gravitational Waves from a Binary Black Hole Merger," *Phys. Rev. Lett.* 116, 061102 (2016). DOI: 10.1103/PhysRevLett.116.061102

**[MEASURED] [R31] Mercury's anomalous perihelion precession (43″/century) explained by GR**
Original resolution: Einstein, A., "Erklärung der Perihelbewegung des Merkur aus der allgemeinen Relativitätstheorie," *Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften*, 831–839 (1915).
The anomaly was identified observationally by Le Verrier (1859) and refined by Newcomb; modern confirmation via radar ranging and ephemerides is [DERIVED / TEXTBOOK] — see T6, Ch. 40, or Will, C.M., "The Confrontation between General Relativity and Experiment," *Living Reviews in Relativity* 17, 4 (2014). DOI: 10.12942/lrr-2014-4
Tier note: mixed provenance, tiered [MEASURED] for the observed quantity. The perihelion anomaly (43"/century) is an empirical astronomical measurement (Le Verrier, Newcomb); Einstein's 1915 explanation is [THEORY]. The header tracks the measurement because that is the claim the book leans on, and the theoretical resolution is cited in the same entry.

**[MEASURED] [R32] Light deflection by the Sun (1.75″) — Eddington 1919, modern VLBI confirmation**
Dyson, F.W., Eddington, A.S., Davidson, C., "A Determination of the Deflection of Light by the Sun's Gravitational Field, from Observations Made at the Total Eclipse of May 29, 1919," *Phil. Trans. R. Soc. A* 220, 291–333 (1920). DOI: 10.1098/rsta.1920.0009
Modern VLBI confirmation to $10^{-4}$: Shapiro, S.S. et al., "Measurement of the Solar Gravitational Deflection of Radio Waves using Geodetic Very-Long-Baseline Interferometry Data, 1979–1999," *Phys. Rev. Lett.* 92, 121101 (2004). DOI: 10.1103/PhysRevLett.92.121101

**[DERIVED / TEXTBOOK] [R33] GPS relativistic clock corrections (GR +45.7 μs/day, SR −7.2 μs/day, net +38.5 μs/day)**
Canonical citation for the full worked calculation: Ashby, N., "Relativity in the Global Positioning System," *Living Reviews in Relativity* 6, 1 (2003). DOI: 10.12942/lrr-2003-1
Every number in that section traces back to this review.

---

## Chapter 9 — Bridge B.a: Quantum Mechanics → Classical Mechanics
No new external claims beyond what is already sourced above. Ehrenfest's theorem, WKB, and decoherence timescales are [DERIVED / TEXTBOOK] — see T3, Ch. 2 and 4; for decoherence, Zurek, W.H., "Decoherence, einselection, and the quantum origins of the classical," *Rev. Mod. Phys.* 75, 715 (2003). DOI: 10.1103/RevModPhys.75.715

---

## Chapter 10 — Bridge B.b: Statistical Mechanics and Thermodynamics

**[DERIVED / TEXTBOOK] [R34] Stefan–Boltzmann law and constant, $\sigma = 5.670\times 10^{-8}\,\text{W/m}^2\text{K}^4$**
Original derivation: Boltzmann, L., "Ableitung des Stefan'schen Gesetzes," *Annalen der Physik* 258, 291–294 (1884). DOI: 10.1002/andp.18842580616
Current CODATA value: https://physics.nist.gov/cgi-bin/cuu/Value?sigma

**[DERIVED / TEXTBOOK] [R35] Wien displacement law constant, $b = 2.898\times 10^{-3}$ m·K**
Wien, W., "Über die Energieverteilung im Emissionsspectrum eines schwarzen Körpers," *Annalen der Physik* 294, 662–669 (1896). DOI: 10.1002/andp.18962940803
Current CODATA value: https://physics.nist.gov/cgi-bin/cuu/Value?bwien

**[DERIVED / TEXTBOOK] [R1] Copper Fermi energy / Fermi temperature ($E_F = 7.0$ eV, $T_F \approx 81{,}000$ K)**
Standard free-electron-model value — see T2, Table 2.1.

**[SYNTHESIS] [R36] Framing of the Higgs mechanism, BCS superconductivity, and Landau theory as "independent instances of one mathematical template"**
This cross-thread claim (echoed in Ch. 21, Thread 2) is the book's own organising argument, not a claim from any single source. The three underlying physical theories are separately and correctly cited above (Ch. 0, Ch. 7, and Landau, L.D., "On the theory of phase transitions," *Zh. Eksp. Teor. Fiz.* 7, 19 and 627 (1937)) — but the *unification narrative itself* is the book's pedagogical synthesis and must be presented as such.

---

## Chapter 11 — Bridge B.c: Maxwell's Equations from the U(1) Gauge Sector

**[DERIVED / TEXTBOOK] [R37] Speed of light from $\mu_0\,\epsilon_0$; Maxwell's identification of light as an EM wave**
Maxwell, J.C., "A Dynamical Theory of the Electromagnetic Field," *Phil. Trans. R. Soc. Lond.* 155, 459–512 (1865). DOI: 10.1098/rstl.1865.0008
Modern value $c = 299{,}792{,}458$ m/s (exact, by SI definition since 1983): https://physics.nist.gov/cgi-bin/cuu/Value?c

---

## Chapter 12 — EM Waves, Optics, Photonics
Standard, uncontested optics — distributed Bragg reflectors, Fabry–Perot linewidths, the Kerr coefficient of silica fibre ($n_2 = 2.6\times 10^{-20}$ m²/W): all [DERIVED / TEXTBOOK]. See T7 (optics); T9, Ch. 2 (Kerr coefficient value).

---

## Chapter 13 — Kubo Formula → Generalized Transport Law

**[THEORY] [R38] Kubo's linear-response theory (1957)**
Kubo, R., "Statistical-Mechanical Theory of Irreversible Processes. I," *J. Phys. Soc. Jpn.* 12, 570–586 (1957). DOI: 10.1143/JPSJ.12.570
Tier note: this is a theoretical framework — a general linear-response construction
that *yields* correlation functions and fluctuation–dissipation relations — not a
measurement. The experimentally measured quantities built on top of it (thermal
conductivity, diffusion coefficients) are cited separately as [MEASURED].

**[DERIVED / TEXTBOOK] [R39] Wiedemann–Franz law and the Lorenz number, $L_0 = 2.44\times 10^{-8}\,\text{W}\cdot\Omega\cdot\text{K}^{-2}$**
Original empirical law: Wiedemann, G. & Franz, R., "Ueber die Wärme-Leitungsfähigkeit der Metalle," *Annalen der Physik* 165, 497–531 (1853). DOI: 10.1002/andp.18531650802
Tier note: this entry carries two different provenances and is tiered by the number it
headlines. The 1853 Wiedemann–Franz relation is *empirical* — a regularities-in-data
observation with no microscopic basis at the time. The Lorenz number
$L_0 = \pi^2 k_B^2/3e^2 = 2.44\times 10^{-8}\,\text{W}\cdot\Omega\,\text{K}^{-2}$
quoted in the title is a *derivation*, exact only in the free-electron/Sommerfeld model
— see T2, Ch. 13, and the Ch. 13 Model Ledger for the scattering assumptions this
universality depends on.

**[DERIVED / TEXTBOOK] [R40] Mott formula for thermopower**
Mott, N.F. & Jones, H., *The Theory of the Properties of Metals and Alloys*, Oxford (1936), Ch. 7. Standard modern reference: T2, Ch. 13, eq. 13.62.

**[MEASURED] [R27] First direct measurement of conductance quantization (quantum point contacts, 1988)**
Cited under Ch. 7; the value $G_0 = 2e^2/h$ is the same constant referenced here.

---

## Chapter 14 — Sensors, Semiconductor Devices, Thermal/Electrical Metrology

**[MEASURED] [R41] Hall effect (original discovery, 1879)**
Hall, E.H., "On a New Action of the Magnet on Electric Currents," *American Journal of Mathematics* 2, 287–292 (1879). DOI: 10.2307/2369245

**[DERIVED / TEXTBOOK] [R42] Richardson–Dushman thermionic emission equation and Richardson constant**
Richardson, O.W., "The Emission of Electricity from Hot Bodies," Longmans, Green & Co. (1921/1924 editions summarize his 1901–1911 work).
Dushman, S., "Electron Emission from Metals as a Function of Temperature," *Phys. Rev.* 21, 623–636 (1923). DOI: 10.1103/PhysRev.21.623

**[DERIVED / TEXTBOOK] [R43] SI redefinition of the second/kilogram/ampere via exact $h$, $e$ (2019)**
Source: BIPM, Resolution 1 of the 26th CGPM (2018), "On the revision of the International System of Units (SI)," effective 20 May 2019.
Link: https://www.bipm.org/en/measurement-units/rev-si/
Tier note: this is an authoritative *definitional standard*, not an experimental
measurement paper — a metrological act of definition, not a result. The constants it
fixes ($h$, $e$) are **exact by definition** after the redefinition, not fitted or
measured values; tied to it, CODATA-derived uncertainties on formerly-measured
constants became exact. Cited because the book's reported values must be pinned to a
specific SI edition, not because a number was observed.

**[DERIVED / TEXTBOOK] [R44] IEC 60751 Pt100 RTD coefficients ($A$, $B$, $C$)**
Source: IEC 60751:2008, "Industrial platinum resistance thermometers and platinum temperature sensors."
Link: https://webstore.iec.ch/publication/3376

**[DERIVED / TEXTBOOK] [GAP] Silicon dopant diffusion coefficients, minority-carrier lifetimes, solar-cell $I_0/I_{SC}$ figures**
Standard semiconductor-device values. The textbook pointer originally given here (T10)
is absent from the table above and its intended identity could not be recovered, so no
source is cited rather than a guessed one. These are routine tabulated device
parameters; pin a recognised semiconductor-device textbook and the relevant chapters on
dopant diffusion and p-n junctions before press.

---

## Chapters 15–20 — Continuum Engineering Physics (Fluids, Thermal, Structural, Geotechnical)

These chapters draw on established textbook-level engineering correlations rather
than single discovery papers. Cite the textbook, not a paper, unless noted.

**[DERIVED / TEXTBOOK] [R45] Reynolds number regime table (laminar/transitional/turbulent boundaries)**
Reynolds, O., "An Experimental Investigation of the Circumstances Which Determine Whether the Motion of Water Shall Be Direct or Sinuous...," *Phil. Trans. R. Soc. Lond.* 174, 935–982 (1883). DOI: 10.1098/rstl.1883.0029
Modern correlation tables: T11, Ch. 6.

**[DERIVED / TEXTBOOK] [R46] Kolmogorov length scale, DNS intractability at high $Re$**
Kolmogorov, A.N., "The local structure of turbulence in incompressible viscous fluid for very large Reynolds numbers," *Dokl. Akad. Nauk SSSR* 30, 299–303 (1941).

**[DERIVED / TEXTBOOK] [R47] Dittus–Boelter correlation (turbulent pipe-flow heat transfer)**
Dittus, F.W. & Boelter, L.M.K., University of California Publications in Engineering, Vol. 2, 443 (1930); reprinted *Int. Comm. Heat Mass Transfer* 12, 3–22 (1985). DOI: 10.1016/0735-1933(85)90003-X
Standard modern reference: T12, Ch. 8.

**[DERIVED / TEXTBOOK] [R48] Terzaghi consolidation theory ($t_{90\%}$ formula, hydraulic conductivity ranges by soil type)**
Terzaghi, K., "Erdbaumechanik auf bodenphysikalischer Grundlage," Deuticke, Vienna (1925).
Standard modern reference: T16, Ch. 9 (Consolidation).

**[DERIVED / TEXTBOOK] [R50] Separation principle (state feedback + observer design independence)**
Standard control result — see T17, Ch. 10, or Kalman, R.E., "On the general theory of control systems," *Proc. 1st IFAC Congress* (1960), for the original state-space formulation.

**[DERIVED / TEXTBOOK] Manning's equation; Froude number; open-channel regime classification**
Empirical/derived engineering correlations — see T15, Ch. 4 (open-channel flow) and T11, Ch. 10.

**[DERIVED / TEXTBOOK] Bond-graph formalism; effort-flow variable pairs**
Payne, H.T., "Analysis and Design of Elastic Systems," Academic Press; and the standard bond-graph treatment in Karnopp, D.C., Margolis, R.C., Rosenberg, R.C., *System Bond Graphs: Fundamentals and Applications*, Elsevier (2012) — see T14 for the effort/flow reference table.

---

## Chapter 18 — Circuit Theory / Signal Processing Cross-Threads

**[DERIVED / TEXTBOOK] [R49] Cooley–Tukey FFT algorithm (1965)**
Cooley, J.W. & Tukey, J.W., "An algorithm for the machine calculation of complex Fourier series," *Mathematics of Computation* 19, 297–301 (1965). DOI: 10.1090/S0025-5718-1965-0178586-1
The book's operation-count comparison ($10^{12}$ vs. $2\times 10^7$ for $N=10^6$) follows directly from the $O(N\log N)$ complexity established in this paper.
Tier note: tiered [DERIVED / TEXTBOOK] - the FFT is an algorithm (a mathematical/computational method with a complexity result), not a measured quantity; cited because the book's operation-count comparison rests on its $O(N\log N)$ analysis.

---

## Chapter 21 — Synthesis, Cross-Layer Threads, Open Problems

**[SYNTHESIS] "Thread 2: The Mexican Hat" — framing Higgs/BCS/Landau as independent instances of one template, not a causal chain**
Same flag as the Ch. 10 entry. Correctly cited components (Higgs mechanism, BCS, Landau) are sourced under their chapters; the unifying claim itself is the book's argument.

**[SYNTHESIS] The Generalized Transport Law as the book's "convergence chapter" unifying Ohm, Fourier, Fick, and Newtonian viscosity under one Kubo-formula linear-response scheme, with Hooke's law entering as static response**
The individual transport laws and the Kubo formula are separately and correctly citable (see Ch. 13); their explicit unification under this framing is original pedagogical synthesis specific to this book. This is the most important claim in the book to keep honestly labelled, since it is the thesis the convergence chapter rests on. The claim must also be stated precisely: the four dissipative coefficients $\sigma$, $\kappa$, $D$, $\eta$ share a linear-response framework in which the transport coefficient is expressed through an equilibrium current-correlation integral, subject to the relevant quantum/classical and closure assumptions. The elastic modulus $C_{ijkl}$ is not a member of that family — it is a static, nondissipative response coefficient relating stress to strain, so Hooke's law is a constitutive relation arising from static response, not a fifth dissipative Green–Kubo transport coefficient. See the Ch. 13 §13.0 caveat on which members of the family use which part of the Kubo expression.

**[SYNTHESIS] The four-way classification of CE/ChE correspondence in Ch. 20 (§20.0.1)**
The distinction between mathematical identity, constitutive correspondence, shared statistical origin, and shared dimensionless framework is the book's own contribution. The underlying results it sorts (Terzaghi consolidation, Darcy's law, Arrhenius kinetics, NTU methods) are textbook material — T16, T15, T18, T12 respectively.

**[DERIVED / TEXTBOOK] Strong CP problem statement ($|\theta_{QCD}| < 10^{-10}$)**
See the Ch. 0 entry above (neutron/electron EDM bounds). Standard pedagogical reference: T8, Ch. 19, or T8b, §23.6.

---

## Textbooks [T#]

Full citations for the [DERIVED / TEXTBOOK] tier. Chapter text cites these as
`[T#]`.

### Physics

| # | Reference |
|---|---|
| T1 | Goldstein, H., Poole, C., Safko, J., *Classical Mechanics*, 3rd ed., Addison-Wesley (2002) |
| T2 | Ashcroft, N.W. & Mermin, N.D., *Solid State Physics*, Harcourt (1976) |
| T3 | Sakurai, J.J. & Napolitano, J., *Modern Quantum Mechanics*, 3rd ed., Cambridge University Press (2020) |
| T4 | Krane, K.S., *Introductory Nuclear Physics*, Wiley (1988) |
| T5 | Tinkham, M., *Introduction to Superconductivity*, 2nd ed., Dover (2004) |
| T6 | Misner, C.W., Thorne, K.S., Wheeler, J.A., *Gravitation*, W.H. Freeman (1973) |
| T7 | Hecht, E., *Optics*, 5th ed., Pearson (2016) |
| T8 | Peskin, M.E. & Schroeder, D.V., *An Introduction to Quantum Field Theory*, Westview Press (1995) |
| T8b | Weinberg, S., *The Quantum Theory of Fields, Vol. II*, Cambridge University Press (1996) |
| T9 | Agrawal, G.P., *Nonlinear Fiber Optics*, 5th ed., Academic Press (2012) |
| T13 | Pathria, R.K. & Beale, P.D., *Statistical Mechanics*, 4th ed., Academic Press (2021) |
| T19 | Jackson, J.D., *Classical Electrodynamics*, 3rd ed., Wiley (1998) |
| T20 | Griffiths, D.J., *Introduction to Quantum Mechanics*, 3rd ed., Cambridge University Press (2018) |

### Continuum mechanics and numerical methods

| # | Reference |
|---|---|
| T21 | Lai, J., Rubin, D., Krempl, E., *Introduction to Continuum Mechanics*, Cambridge University Press (2004) |
| T22 | Spencer, P.A., *The Mechanics of Structures*, Cambridge University Press (1997) |
| T23 | Marsden, J.E. & Hughes, T.J.R., *Mathematical Foundations of Elasticity*, Cambridge University Press (1999) |
| T24 | Zienkiewicz, O.C., Taylor, R.L., Nitschke, P., *The Finite Element Method: Its Basis and Fundamentals*, 7th ed., Butterworth-Heinemann (2014) |
| T25 | Bathe, K.-J., *Finite Element Procedures*, 2nd ed., Prentice Hall (2016) |
| T26 | LeVeque, R.J., *Finite Difference Methods for Ordinary and Partial Differential Equations*, SIAM (2007) |
| T27 | Versteeg, M.H.C. & Malalasekera, W., *An Introduction to Computational Fluid Dynamics*, 3rd ed., Prentice Hall (2010) |

### Fluids, heat, and mass transfer

| # | Reference |
|---|---|
| T11 | White, F.M., *Fluid Mechanics*, 8th ed., McGraw-Hill (2015) |
| T12 | Incropera, F.P., DeWitt, D.P., Bergman, T.L., Lavine, A.S., *Fundamentals of Heat and Mass Transfer*, 8th ed., Wiley (2017) |
| T28 | Geankoplis, T.J., *Transport Processes and Separation Process Principles*, 5th ed., Prentice Hall (2018) |
| T29 | Welty, J.R., Wicks, C.J., Wilson, R., Rorrer, G.L., *Fundamentals of Momentum, Heat and Mass Transfer*, 5th ed., Wiley (2007) |
| T30 | Çengel, Y.A. & Cimbala, J.M., *Fluid Mechanics: Fundamentals and Applications*, 4th ed., McGraw-Hill (2018) |
| T31 | Landau, L.D. & Lifshitz, E.M., *Fluid Mechanics*, Course of Theoretical Physics Vol. 6, Pergamon (1987) |

### Structural, geotechnical, and chemical engineering

| # | Reference |
|---|---|
| T14 | Karnopp, D.C., Margolis, R.C., Rosenberg, R.C., *System Bond Graphs: Fundamentals and Applications*, Elsevier (2012) |
| T15 | Das, B.M., *Principles of Geotechnical Engineering*, 9th ed., Cengage (2016) |
| T16 | Das, B.M., *Principles of Foundation Engineering*, 9th ed., Cengage (2016) |
| T18 | Felder, R.M., Rousseau, R.M., Bullard, L.G., *Elementary Principles of Chemical Processes*, 4th ed., Wiley (2019) |
| T32 | Bird, R.B., Stewart, W.E., Lightfoot, E.N., *Transport Phenomena*, 2nd ed., Wiley (2006) |
| T33 | Timoshenko, S.P. & Young, D.H., *Theory of Structures*, 2nd ed., McGraw-Hill (1965) |
| T34 | Gere, J.M. & Goodno, B.J., *Mechanics of Materials*, 9th ed., Cengage (2018) |
| T35 | Levenspiel, O., *Chemical Reaction Engineering*, 3rd ed., Wiley (1999) |

### Control theory

| # | Reference |
|---|---|
| T17 | Ogata, K., *Modern Control Engineering*, 5th ed., Prentice Hall (2010) |
| T36 | Nise, N.S., *Control Systems Engineering*, 8th ed., Pearson (2019) |
| T37 | Kuo, B.C., *Automatic Control Systems*, 10th ed., Wiley (2017) |
| T38 | Åström, K.J. & Murray, R.M., *Feedback Systems*, 2nd ed., Princeton University Press (2021) |
| T39 | Franklin, G.F., Powell, J.D., Emami, A., *Feedback Control of Dynamic Systems*, 8th ed., Pearson (2019) |

---

## Gaps and flags

Recorded honestly rather than papered over. These are known-unfinished items.

- **[GAP] Dangling identifier T10.** The Ch. 14 semiconductor-device entry (dopant diffusion coefficients, minority-carrier lifetimes, solar-cell $I_0/I_{SC}$) cited textbook "T10", but no T10 entry exists in the textbook key above — the table runs T1–T9, then T13 in the core block, with T11/T12 relocated to the fluids/heat block. The intended textbook could not be identified from the surrounding numbering (it is not sequential by subject). Rather than guess an entry, the in-text citation is flagged and no source is asserted. Resolve by adding a verified semiconductor-device text as T10 (or renumbering); do not leave a bare "T10" pointer in the table.
- **[GAP] Chapters 16, 17, 19, 20** contain further named correlations — acoustic cavitation and Rayleigh–Plesset dynamics, MEMS resonator $Q$-factors, the fissility parameter, geological dating precision — not individually traced to primary sources. These are almost certainly [DERIVED / TEXTBOOK], and the textbook key above now names the standard references for each domain (T21, T22, T27, T11, T12, T30, T4), but no page-level citation has been pinned. Flagged rather than manufactured.
- **[FLAG] CODATA/PDG links** point to live NIST/PDG reference pages rather than a fixed dataset year. These bodies update periodically (CODATA roughly every 4 years; PDG annually). A print bibliography must pin the specific edition actually used, or "current CODATA value" will silently drift.
- **[FLAG] Section numbers** were matched to chapters, not re-verified line-by-line against the manuscript after the Chapter 20, Chapter 7, and Chapter 13 rewrites changed section numbering. Re-pin against the chapter files before press.
- **[FLAG] The book's three synthesis claims** — the convergence thesis (Ch. 13), the Mexican-hat cross-thread (Ch. 10/21), and the four-way correspondence classification (Ch. 20) — are original to this work. They are flagged as [SYNTHESIS] here and must be flagged the same way wherever they are restated. A synthesis claim presented with a textbook citation attached is the failure mode this file exists to prevent.
- **[UNVERIFIED]** No entries currently carry this marker. If a new claim is added without a verified source, mark it rather than dropping it.

---

*Cross-referenced from `METADATA/00 Map.md`. Chapter text cites sources as `[R#]` and `[T#]`.*
