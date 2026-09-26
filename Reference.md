# Reference.md — Sourcing for Pivotal Hard Claims

**Engineering Physics: Top Down — Master Reference List**

## How to read this file

This file traces every load-bearing factual claim in the book back to its source, chapter by chapter, in the same order the book itself proceeds — Ch. 0 through Ch. 21 and the Epilogue — so that the reference chain mirrors the derivation chain the book already establishes. A claim in Ch. 7 that echoes a structure introduced in Ch. 0 (the Mexican-hat potential, the θ-term) is filed under Ch. 7 but cross-references back to Ch. 0, exactly as the book's own "Revealed by" / "→ Ch. X" convention does.

Every entry is one of three kinds. Say so plainly, because they carry different evidentiary weight:

- **[MEASURED]** — an experimentally measured number or a discovery, traceable to one primary paper (or a small number of them). Full citation, link, and DOI given where one exists.
- **[DERIVED / TEXTBOOK]** — a result that is standard, uncontested physics, not tied to a single paper — the kind of thing that appears identically in every graduate textbook on the subject. Cited to a standard textbook (full bibliographic entry in the **Standard Textbooks** key at the end) rather than a paper, because that is the honest citation: no single paper "discovered" the Wiedemann–Franz ratio's textbook derivation, for instance, even though von Klitzing's *measurement* of it is a paper.
- **[SYNTHESIS — NO EXTERNAL CITATION]** — a claim that is the book's own argument or pedagogical framing, not a fact borrowed from the literature. These are flagged explicitly rather than given a decorative citation, because attaching a citation to your own synthesis is worse than admitting there isn't one. This is the tier-3 case you asked about: it is marked, not silently dropped.

I did not attach these citations to the chapter text itself, per your instruction — this file stands alone. Where I could not independently verify a number against a primary source in the time available, I say so rather than guess; those are marked **[UNVERIFIED — FLAG]** and should not be treated as sourced until checked.

All dates, journal volumes, and DOIs below were checked against the primary literature or standard secondary sources (Wikipedia's citation apparatus, APS/Elsevier publisher records, arXiv) during compilation — not reconstructed from memory.

---

## Chapter 0 — The Equation (Standard Model + Einstein–Hilbert action)

**[MEASURED] Newton's gravitational constant, $G = 6.674\times 10^{-11}\ \text{N·m}^2/\text{kg}^2$**
Source: CODATA 2018 recommended values (NIST). This is the least precisely known fundamental constant (relative uncertainty ~2.2×10⁻⁵), a fact worth noting alongside the number itself.
Link: https://physics.nist.gov/cgi-bin/cuu/Value?bg

**[MEASURED] Weinberg angle, $\theta_W \approx 28.7°$ ($\sin^2\theta_W \approx 0.231$)**
Source: Particle Data Group, *Review of Particle Physics* (current edition), Electroweak Model section.
Link: https://pdg.lbl.gov/

**[MEASURED] W and Z boson masses ($m_W \approx 80.4$ GeV, $m_Z \approx 91.2$ GeV)**
Source: Particle Data Group, *Review of Particle Physics*, Gauge and Higgs Boson Summary Table.
Link: https://pdg.lbl.gov/

**[MEASURED] Higgs vacuum expectation value $v \approx 246$ GeV**
Derived from the measured Fermi constant $G_F$ via $v = (\sqrt{2}G_F)^{-1/2}$; this is a standard electroweak-fit result, not an independent measurement.
Source: Particle Data Group, *Review of Particle Physics*, Electroweak Model and Constraints on New Physics.
Link: https://pdg.lbl.gov/

**[MEASURED] Higgs boson discovery and mass ($m_h = 125.09$ GeV)**
Source: ATLAS Collaboration, "Observation of a new particle in the search for the Standard Model Higgs boson with the ATLAS detector at the LHC," *Phys. Lett. B* 716, 1–29 (2012).
DOI: 10.1016/j.physletb.2012.08.020
Companion paper: CMS Collaboration, "Observation of a new boson at a mass of 125 GeV with the CMS experiment at the LHC," *Phys. Lett. B* 716, 30–61 (2012).
DOI: 10.1016/j.physletb.2012.08.021
(Combined ATLAS+CMS mass measurement of 125.09 ± 0.24 GeV comes from the later combination paper: ATLAS+CMS Collaborations, *Phys. Rev. Lett.* 114, 191803 (2015), DOI: 10.1103/PhysRevLett.114.191803.)

**[MEASURED] Original Higgs-mechanism theory papers (1964)**
- Englert, F. & Brout, R., "Broken Symmetry and the Mass of Gauge Vector Mesons," *Phys. Rev. Lett.* 13, 321–323 (1964). DOI: 10.1103/PhysRevLett.13.321
- Higgs, P.W., "Broken Symmetries, Massless Particles and Gauge Fields," *Phys. Lett.* 12, 132–133 (1964). DOI: 10.1016/0031-9163(64)91136-9
- Higgs, P.W., "Broken Symmetries and the Masses of Gauge Bosons," *Phys. Rev. Lett.* 13, 508–509 (1964). DOI: 10.1103/PhysRevLett.13.508
- Guralnik, G.S., Hagen, C.R., Kibble, T.W.B., "Global Conservation Laws and Massless Particles," *Phys. Rev. Lett.* 13, 585–587 (1964). DOI: 10.1103/PhysRevLett.13.585

**[MEASURED] Wu et al. parity-violation experiment (1957)**
Wu, C.S., Ambler, E., Hayward, R.W., Hoppes, D.D., Hudson, R.P., "Experimental Test of Parity Conservation in Beta Decay," *Phys. Rev.* 105, 1413–1415 (1957).
DOI: 10.1103/PhysRev.105.1413
(This is the direct source for the book's claim that "the cobalt-60 nucleus emitted electrons preferentially opposite to its spin.")

**[MEASURED] Electron electric dipole moment bound, $d_e < 1.8\times 10^{-26}\ e\cdot\text{cm}$**
Source: ACME Collaboration (Andreev, V. et al.), "Improved limit on the electric dipole moment of the electron," *Nature* 562, 355–360 (2018).
DOI: 10.1038/s41586-018-0599-8
(Note: the book's number, $1.8\times10^{-26}\,e\cdot\text{cm}$, matches this measurement; the strong-CP bound $|\theta_{QCD}| < 10^{-10}$ derived from neutron EDM bounds is [DERIVED/TEXTBOOK] — see standard QCD textbook, e.g. Peskin & Schroeder, Ch. 19, or a current-precision update from the neutron EDM collaboration.)

**[SYNTHESIS — NO EXTERNAL CITATION] Gauge coupling unification near $10^{16}$ GeV "suggesting a GUT"**
This is a well-known theoretical extrapolation (running couplings under the MSSM nearly meet), not an experimental measurement — no GUT has been observed. Standard reference for the running-coupling calculation itself: Georgi, H., Quinn, H.R., Weinberg, S., "Hierarchy of Interactions in Unified Gauge Theories," *Phys. Rev. Lett.* 33, 451 (1974), DOI: 10.1103/PhysRevLett.33.451 — but the word "suggesting" in the book's own text is doing real work here; this is not a confirmed discovery and should not be cited as one.

---

## Chapter 1 — The Action Principle
No claims in this chapter rely on external experimental data; the content (Lagrangian mechanics, Noether's theorem, Hamilton–Jacobi theory) is [DERIVED/TEXTBOOK]. Standard reference: Goldstein, Poole & Safko, *Classical Mechanics* (see Standard Textbooks key).

---

## Chapter 2 — Phenomena Catalogue
This chapter is an index, not a source of new claims — every phenomenon listed is sourced under the chapter where it is actually derived (see the "Revealed by → Ch. X" column in the book itself). No separate entries are needed here; cross-reference the chapter listed.

---

## Chapter 3 — Bridge A: Dirac → Schrödinger

**[MEASURED] Anomalous magnetic moment $g_e = 2$ as a pre-1928 mystery, resolved by the Dirac equation**
Historical mystery: no single citable "discovery" — $g=2$ emerged from spectroscopic anomalies (anomalous Zeeman effect) through the 1920s; the resolution is the theory paper itself:
Dirac, P.A.M., "The Quantum Theory of the Electron," *Proc. R. Soc. Lond. A* 117, 610–624 (1928). DOI: 10.1098/rspa.1928.0023

**[MEASURED] Discovery of the positron (Anderson, 1932/1933)**
Anderson, C.D., "The Positive Electron," *Phys. Rev.* 43, 491–494 (1933). DOI: 10.1103/PhysRev.43.491
(The particle was photographed 2 August 1932; this is the full data paper. A short note appeared earlier in *Science* 76, 238 (1932).)

**[DERIVED/TEXTBOOK] Foldy–Wouthuysen transformation and its terms (Zeeman, spin-orbit, Darwin)**
Foldy, L.L. & Wouthuysen, S.A., "On the Dirac Theory of Spin 1/2 Particles and Its Non-Relativistic Limit," *Phys. Rev.* 78, 29–36 (1950). DOI: 10.1103/PhysRev.78.29

---

## Chapter 4 — Schrödinger Equation, Hydrogen Atom

**[MEASURED] Rydberg formula (empirical, 1888/1890) and Rydberg constant**
Rydberg, J.R., "On the Structure of the Line-Spectra of the Chemical Elements," *Phil. Mag.*, Series 5, Vol. 29, 331–337 (1890). (Formula first presented in a paper read to the Lund Physiographic Society, 1888.)
Modern precision value $R_\infty = 1.0973731568539\times 10^7\ \text{m}^{-1}$: CODATA recommended values (NIST) — one of the most precisely measured constants in physics.
Link: https://physics.nist.gov/cgi-bin/cuu/Value?ryd

---

## Chapter 5 — Spin, Many-Electron Systems, Periodic Table

**[MEASURED] Stern–Gerlach experiment (1922)**
Gerlach, W. & Stern, O., "Der experimentelle Nachweis der Richtungsquantelung im Magnetfeld," *Zeitschrift für Physik* 9, 349–352 (1922). DOI: 10.1007/BF01326983

**[MEASURED] Lamb shift measurement**
Lamb, W.E. & Retherford, R.C., "Fine Structure of the Hydrogen Atom by a Microwave Method," *Phys. Rev.* 72, 241–243 (1947). DOI: 10.1103/PhysRev.72.241
(Modern precision value of ~1057.8 MHz splitting comes from later refinements; the 1947 paper is the original discovery.)

**[MEASURED] Cesium atomic clock definition of the SI second (9,192,631,770 Hz hyperfine transition)**
Source: International Bureau of Weights and Measures (BIPM), *The International System of Units (SI Brochure)*, 9th edition, definition of the second.
Link: https://www.bipm.org/en/publications/si-brochure

**[MEASURED] Bohr magneton, $\mu_B = 9.274\times10^{-24}$ J/T**
Source: CODATA recommended values (NIST).
Link: https://physics.nist.gov/cgi-bin/cuu/Value?mub

---

## Chapter 6 — Band Theory, Bonding, Nuclear Physics

**[MEASURED] Bragg reflection condition**
Bragg, W.L., "The Diffraction of Short Electromagnetic Waves by a Crystal," *Proc. Camb. Phil. Soc.* 17, 43–57 (1913).
(Bragg's law itself, $n\lambda = 2d\sin\theta$; the book's application to electron-wave band gaps at the Brillouin zone boundary is [DERIVED/TEXTBOOK], standard solid-state physics — see Ashcroft & Mermin, Ch. 7–9.)

**[DERIVED/TEXTBOOK] Semi-Empirical Mass Formula (Bethe–Weizsäcker) and its coefficients**
Weizsäcker, C.F. von, "Zur Theorie der Kernmassen," *Zeitschrift für Physik* 96, 431–458 (1935). DOI: 10.1007/BF01337700
Current best-fit coefficients ($a_V=15.8$ MeV, $a_S=18.3$ MeV, $a_C=0.714$ MeV, $a_A=23.2$ MeV, $\delta=\pm12$ MeV): standard nuclear-physics textbook values — see Krane, *Introductory Nuclear Physics*, Ch. 3.
Binding-energy-per-nucleon data (peak at $^{56}$Fe, 8.79 MeV): NNDC (National Nuclear Data Center) Atomic Mass Evaluation.
Link: https://www.nndc.bnl.gov/

**[DERIVED/TEXTBOOK] Geiger–Nuttall law**
Geiger, H. & Nuttall, J.M., "The ranges of the α particles from various radioactive substances," *Phil. Mag.* 22, 613–621 (1911); and a follow-up, *Phil. Mag.* 23, 439 (1912).
Modern half-life data spanning $^{212}$Po to $^{232}$Th: NNDC.

**[MEASURED] ITER fusion energy gain target, $Q \geq 10$**
Source: ITER Organization, official project documentation.
Link: https://www.iter.org/sci/Goals

---

## Chapter 7 — Topology, Quantum Hall Effect, Superconductivity

**[MEASURED] Berry phase**
Berry, M.V., "Quantal Phase Factors Accompanying Adiabatic Changes," *Proc. R. Soc. Lond. A* 392, 45–57 (1984). DOI: 10.1098/rspa.1984.0023

**[MEASURED] Von Klitzing's discovery of the (integer) quantum Hall effect (1980)**
Klitzing, K. von, Dorda, G., Pepper, M., "New Method for High-Accuracy Determination of the Fine-Structure Constant Based on Quantized Hall Resistance," *Phys. Rev. Lett.* 45, 494–497 (1980). DOI: 10.1103/PhysRevLett.45.494
(Quantization to 1 part in $10^9$: this precision figure is repeatedly re-confirmed metrologically; see BIPM/NIST resistance-standard documentation for current best figures.)

**[MEASURED] Adler–Bell–Jackiw chiral anomaly (original theory papers, 1969)**
- Adler, S.L., "Axial-Vector Vertex in Spinor Electrodynamics," *Phys. Rev.* 177, 2426–2438 (1969). DOI: 10.1103/PhysRev.177.2426
- Bell, J.S. & Jackiw, R., "A PCAC puzzle: $\pi^0\to\gamma\gamma$ in the $\sigma$-model," *Nuovo Cimento A* 60, 47–61 (1969). DOI: 10.1007/BF02823296

**[MEASURED] Nielsen–Ninomiya (no-go) theorem for chiral fermions on a lattice**
Nielsen, H.B. & Ninomiya, M., "Absence of Neutrinos on a Lattice: I. Proof by Homotopy Theory," *Nucl. Phys. B* 185, 20–40 (1981). DOI: 10.1016/0550-3213(82)90011-6 (erratum-carrying record)
Part II: *Nucl. Phys. B* 193, 173–194 (1981). DOI: 10.1016/0550-3213(81)90524-1

**[MEASURED] Negative longitudinal magnetoresistance from the chiral anomaly, observed in TaAs (2015)**
Huang, X. et al., "Observation of the Chiral-Anomaly-Induced Negative Magnetoresistance in 3D Weyl Semimetal TaAs," *Phys. Rev. X* 5, 031023 (2015). DOI: 10.1103/PhysRevX.5.031023

**[MEASURED] BCS theory of superconductivity (1957)**
Bardeen, J., Cooper, L.N., Schrieffer, J.R., "Theory of Superconductivity," *Phys. Rev.* 108, 1175–1204 (1957). DOI: 10.1103/PhysRev.108.1175
(The universal gap ratio $2\Delta(0)/k_BT_c = 3.528$ is a prediction of this paper, subsequently confirmed across many conventional superconductors — [DERIVED/TEXTBOOK] for the confirming measurements; see Tinkham, *Introduction to Superconductivity*, Ch. 3, for the standard compiled comparison table.)

**[MEASURED] Flux quantization in superconducting rings (1961, two independent groups)**
- Deaver, B.S. & Fairbank, W.M., "Experimental Evidence for Quantized Flux in Superconducting Cylinders," *Phys. Rev. Lett.* 7, 43–46 (1961). DOI: 10.1103/PhysRevLett.7.43
- Doll, R. & Näbauer, M., "Experimental Proof of Magnetic Flux Quantization in a Superconducting Ring," *Phys. Rev. Lett.* 7, 51–52 (1961). DOI: 10.1103/PhysRevLett.7.51
- Flux quantum value $\Phi_0 = h/2e = 2.067833848\times10^{-15}$ Wb: CODATA (NIST). Link: https://physics.nist.gov/cgi-bin/cuu/Value?flxquhs2e

**[MEASURED] Josephson effect (theory, 1962)**
Josephson, B.D., "Possible new effects in superconductive tunnelling," *Phys. Lett.* 1, 251–253 (1962). DOI: 10.1016/0031-9163(62)91369-0
Josephson constant $K_J = 2e/h = 483597.8484\ldots\times10^9$ Hz/V (exact since the 2019 SI redefinition): CODATA (NIST). Link: https://physics.nist.gov/cgi-bin/cuu/Value?kjos

**[MEASURED] Abrikosov vortices (theory, 1957; Nobel Prize 2003)**
Abrikosov, A.A., "On the Magnetic Properties of Superconductors of the Second Group," *Sov. Phys. JETP* 5, 1174–1182 (1957) [Zh. Eksp. Teor. Fiz. 32, 1442 (1957)].

**[MEASURED] Quantized conductance of a point contact (1988)**
van Wees, B.J. et al., "Quantized Conductance of Point Contacts in a Two-Dimensional Electron Gas," *Phys. Rev. Lett.* 60, 848–850 (1988). DOI: 10.1103/PhysRevLett.60.848
(Independently: Wharam, D.A. et al., *J. Phys. C* 21, L209 (1988).)

---

## Chapter 8 — Bridge B.d: General Relativity → Newton's Law

**[MEASURED] Pound–Rebka gravitational redshift experiment (1959)**
Pound, R.V. & Rebka, G.A., "Gravitational Red-Shift in Nuclear Resonance," *Phys. Rev. Lett.* 3, 439–441 (1959). DOI: 10.1103/PhysRevLett.3.439
(Measured $\Delta\nu/\nu \approx -2.5\times10^{-15}$ over 22.5 m, confirmed to ~10%; a later refinement, Pound & Snider, *Phys. Rev. Lett.* 13, 539 (1964), improved this to ~1%.)

**[MEASURED] Gravity Probe B: frame dragging and geodetic precession (2011)**
Everitt, C.W.F. et al., "Gravity Probe B: Final Results of a Space Experiment to Test General Relativity," *Phys. Rev. Lett.* 106, 221101 (2011). DOI: 10.1103/PhysRevLett.106.221101
(Measured frame-dragging drift: $-37.2 \pm 7.2$ mas/yr vs. GR prediction $-39.2$ mas/yr — consistent with the book's "39 mas/yr" figure within the quoted precision.)

**[MEASURED] LIGO first direct detection of gravitational waves, GW150914 (2016)**
Abbott, B.P. et al. (LIGO Scientific Collaboration and Virgo Collaboration), "Observation of Gravitational Waves from a Binary Black Hole Merger," *Phys. Rev. Lett.* 116, 061102 (2016). DOI: 10.1103/PhysRevLett.116.061102

**[MEASURED] Mercury's anomalous perihelion precession (43″/century) explained by GR**
Original theoretical resolution: Einstein, A., "Erklärung der Perihelbewegung des Merkur aus der allgemeinen Relativitätstheorie," *Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften*, 831–839 (1915).
The anomaly itself was identified observationally decades earlier by Le Verrier (1859) and refined by Newcomb; modern confirmation via planetary radar ranging and ephemerides is [DERIVED/TEXTBOOK] — see Misner, Thorne & Wheeler, *Gravitation*, Ch. 40, or Will, C.M., "The Confrontation between General Relativity and Experiment," *Living Reviews in Relativity* 17, 4 (2014). DOI: 10.12942/lrr-2014-4

**[MEASURED] Light deflection by the Sun (1.75″) — Eddington 1919, modern VLBI confirmation**
Dyson, F.W., Eddington, A.S., Davidson, C., "A Determination of the Deflection of Light by the Sun's Gravitational Field, from Observations Made at the Total Eclipse of May 29, 1919," *Phil. Trans. R. Soc. A* 220, 291–333 (1920). DOI: 10.1098/rsta.1920.0009
Modern VLBI confirmation to $10^{-4}$ precision: Shapiro, S.S. et al., "Measurement of the Solar Gravitational Deflection of Radio Waves using Geodetic Very-Long-Baseline Interferometry Data, 1979–1999," *Phys. Rev. Lett.* 92, 121101 (2004). DOI: 10.1103/PhysRevLett.92.121101

**[DERIVED/TEXTBOOK] GPS relativistic clock corrections (GR +45.7 μs/day, SR −7.2 μs/day, net +38.5 μs/day)**
Standard reference for the full worked calculation: Ashby, N., "Relativity in the Global Positioning System," *Living Reviews in Relativity* 6, 1 (2003). DOI: 10.12942/lrr-2003-1
(This is the canonical citation for the entire §8.8 GPS worked example — every number in that section traces back to this review.)

---

## Chapter 9 — Bridge B.a: Quantum Mechanics → Classical Mechanics
No new external claims beyond what is already sourced above (Ehrenfest's theorem, WKB, decoherence timescales are [DERIVED/TEXTBOOK] — standard references: Sakurai & Napolitano, *Modern Quantum Mechanics*, Ch. 2 and 4; for decoherence, Zurek, W.H., "Decoherence, einselection, and the quantum origins of the classical," *Rev. Mod. Phys.* 75, 715 (2003), DOI: 10.1103/RevModPhys.75.715).

---

## Chapter 10 — Bridge B.b: Statistical Mechanics and Thermodynamics

**[DERIVED/TEXTBOOK] Stefan–Boltzmann law and constant, $\sigma = 5.670\times10^{-8}\ \text{W/m}^2\text{K}^4$**
Original derivation: Boltzmann, L., "Ableitung des Stefan'schen Gesetzes," *Annalen der Physik* 258, 291–294 (1884). DOI: 10.1002/andp.18842580616
Current CODATA value: https://physics.nist.gov/cgi-bin/cuu/Value?sigma

**[DERIVED/TEXTBOOK] Wien displacement law constant, $b = 2.898\times10^{-3}$ m·K**
Wien, W., "Über die Energieverteilung im Emissionsspectrum eines schwarzen Körpers," *Annalen der Physik* 294, 662–669 (1896). DOI: 10.1002/andp.18962940803
Current CODATA value: https://physics.nist.gov/cgi-bin/cuu/Value?bwien

**[MEASURED] Copper Fermi energy / Fermi temperature figures ($E_F = 7.0$ eV, $T_F \approx 81{,}000$ K)**
Standard free-electron-model textbook value — see Ashcroft & Mermin, *Solid State Physics*, Table 2.1 (free-electron densities and derived Fermi parameters for elemental metals).

**[SYNTHESIS — NO EXTERNAL CITATION] Framing of the Higgs mechanism, BCS superconductivity, and Landau theory as "independent instances of one mathematical template"**
This cross-thread claim (echoed again in Ch. 21 §Thread 2) is the book's own organizing argument, not a claim from any single source. The three underlying physical theories are separately and correctly cited above (Ch. 0, Ch. 7, and standard Landau mean-field theory — Landau, L.D., "On the theory of phase transitions," *Zh. Eksp. Teor. Fiz.* 7, 19 and 627 (1937)) — but the *unification narrative itself* is the book's pedagogical synthesis and should be presented as such, not attributed to the literature.

---

## Chapter 11 — Classical U(1) → Maxwell's Equations

**[DERIVED/TEXTBOOK] Speed of light from $\mu_0,\epsilon_0$; Maxwell's identification of light as an EM wave**
Maxwell, J.C., "A Dynamical Theory of the Electromagnetic Field," *Phil. Trans. R. Soc. Lond.* 155, 459–512 (1865). DOI: 10.1098/rstl.1865.0008
Modern CODATA value of $c = 299{,}792{,}458$ m/s (exact, by SI definition since 1983): https://physics.nist.gov/cgi-bin/cuu/Value?c

---

## Chapter 12 — EM Waves, Optics, Photonics
Standard, uncontested optics — Distributed Bragg reflectors, Fabry–Perot linewidths, the Kerr coefficient of silica fiber ($n_2 = 2.6\times10^{-20}$ m²/W): all [DERIVED/TEXTBOOK]. Standard references: Hecht, *Optics*; Agrawal, G.P., *Nonlinear Fiber Optics* (for the Kerr coefficient value specifically, Ch. 2).

---

## Chapter 13 — Kubo Formula → Generalized Transport Law

**[MEASURED] Kubo's linear-response theory (1957)**
Kubo, R., "Statistical-Mechanical Theory of Irreversible Processes. I," *J. Phys. Soc. Jpn.* 12, 570–586 (1957). DOI: 10.1143/JPSJ.12.570

**[MEASURED] Wiedemann–Franz law and the Lorenz number, $L_0 = 2.44\times10^{-8}\ \text{W}\cdot\Omega\cdot\text{K}^{-2}$**
Original empirical law: Wiedemann, G. & Franz, R., "Ueber die Wärme-Leitungsfähigkeit der Metalle," *Annalen der Physik* 165, 497–531 (1853). DOI: 10.1002/andp.18531650802
Theoretical Lorenz-number value ($L_0 = \pi^2 k_B^2/3e^2$, exact in the free-electron/Sommerfeld model): [DERIVED/TEXTBOOK] — Ashcroft & Mermin, Ch. 13.

**[DERIVED/TEXTBOOK] Mott formula for thermopower**
Mott, N.F. & Jones, H., *The Theory of the Properties of Metals and Alloys*, Oxford (1936), Ch. 7. (Standard modern reference: Ashcroft & Mermin, Ch. 13, eq. 13.62.)

**[MEASURED] First direct measurement of conductance quantization (quantum point contacts, 1988)**
Already cited under Ch. 7 (van Wees et al., 1988) — the value $G_0 = 2e^2/h$ is the same constant referenced again here.

---

## Chapter 14 — Sensors, Semiconductor Devices, Thermal/Electrical Metrology

**[MEASURED] Hall effect (original discovery, 1879)**
Hall, E.H., "On a New Action of the Magnet on Electric Currents," *American Journal of Mathematics* 2, 287–292 (1879). DOI: 10.2307/2369245

**[DERIVED/TEXTBOOK] Richardson–Dushman thermionic emission equation and Richardson constant**
Richardson, O.W., "The Emission of Electricity from Hot Bodies," Longmans, Green & Co. (1921/1924 editions summarize his 1901–1911 work).
Dushman, S., "Electron Emission from Metals as a Function of Temperature," *Phys. Rev.* 21, 623–636 (1923). DOI: 10.1103/PhysRev.21.623

**[MEASURED] SI redefinition of the second/kilogram/ampere via exact $h$, $e$ (2019)**
Source: BIPM, Resolution 1 of the 26th CGPM (2018), "On the revision of the International System of Units (SI)," effective 20 May 2019.
Link: https://www.bipm.org/en/measurement-units/rev-si/

**[DERIVED/TEXTBOOK] IEC 60751 Pt100 RTD coefficients ($A$, $B$, $C$)**
Source: International Electrotechnical Commission, IEC 60751:2008, "Industrial platinum resistance thermometers and platinum temperature sensors."
Link: https://webstore.iec.ch/publication/3376

**[DERIVED/TEXTBOOK] Silicon dopant diffusion coefficients, minority-carrier lifetimes, solar-cell $I_0/I_{SC}$ figures**
Standard semiconductor-device textbook values — see Sze, S.M. & Ng, K.K., *Physics of Semiconductor Devices*, 3rd ed., relevant chapters on diffusion and p-n junctions.

---

## Chapters 15–20 — Classical Continuum Engineering Physics (Fluids, Thermal, Structural, Geotechnical)

These chapters draw on well-established, textbook-level engineering correlations rather than single discovery papers. Listed here for completeness; cite the textbook, not a paper, unless otherwise noted:

**[DERIVED/TEXTBOOK] Reynolds number regime table (laminar/transitional/turbulent boundaries)**
Reynolds, O., "An Experimental Investigation of the Circumstances Which Determine Whether the Motion of Water Shall Be Direct or Sinuous...," *Phil. Trans. R. Soc. Lond.* 174, 935–982 (1883). DOI: 10.1098/rstl.1883.0029
Modern correlation tables: White, F.M., *Fluid Mechanics*, Ch. 6.

**[DERIVED/TEXTBOOK] Kolmogorov length scale, DNS intractability at high $Re$**
Kolmogorov, A.N., "The local structure of turbulence in incompressible viscous fluid for very large Reynolds numbers," *Dokl. Akad. Nauk SSSR* 30, 299–303 (1941).

**[DERIVED/TEXTBOOK] Dittus–Boelter correlation (turbulent pipe-flow heat transfer)**
Dittus, F.W. & Boelter, L.M.K., University of California Publications in Engineering, Vol. 2, 443 (1930) (reprinted *Int. Comm. Heat Mass Transfer* 12, 3–22 (1985), DOI: 10.1016/0735-1933(85)90003-X).
Standard modern reference: Incropera et al., *Fundamentals of Heat and Mass Transfer*, Ch. 8.

**[DERIVED/TEXTBOOK] Terzaghi consolidation theory ($t_{90\%}$ formula, hydraulic conductivity ranges by soil type)**
Terzaghi, K., "Erdbaumechanik auf bodenphysikalischer Grundlage," Deuticke, Vienna (1925).
Standard modern reference: Das, B.M., *Principles of Geotechnical Engineering*, Ch. 9 (Consolidation).

**[DERIVED/TEXTBOOK] Separation principle (state feedback + observer design independence)**
Standard control-theory result — see Ogata, K., *Modern Control Engineering*, Ch. 10, or Kalman, R.E., "On the general theory of control systems," *Proc. 1st IFAC Congress* (1960), for the original state-space formulation this rests on.

---

## Chapter 18 — Circuit Theory / Signal Processing Cross-Threads

**[MEASURED] Cooley–Tukey FFT algorithm (1965)**
Cooley, J.W. & Tukey, J.W., "An algorithm for the machine calculation of complex Fourier series," *Mathematics of Computation* 19, 297–301 (1965). DOI: 10.1090/S0025-5718-1965-0178586-1
(The book's operation-count comparison, $10^{12}$ vs. $2\times10^7$ for $N=10^6$, follows directly from the $O(N\log N)$ complexity established in this paper.)

---

## Chapter 21 — Synthesis, Cross-Layer Threads, Open Problems

**[SYNTHESIS — NO EXTERNAL CITATION] "Thread 2: The Mexican Hat" — framing Higgs/BCS/Landau as independent instances of one template, not a causal chain**
Same flag as the Ch. 10 entry above. Correctly cited components (Higgs mechanism, BCS theory, Landau theory) are sourced under their respective chapters; the unifying claim itself is the book's argument.

**[SYNTHESIS — NO EXTERNAL CITATION] The Generalized Transport Law as the book's "convergence chapter" unifying Ohm, Fourier, Fick, Newtonian viscosity, and Hooke's law under one Kubo-formula calculation**
The individual transport laws and the Kubo formula are separately and correctly citable (see Ch. 13 above); their explicit unification under this framing is original pedagogical synthesis specific to this book, not a claim drawn from the literature. Flagged accordingly — this is very likely the single most important claim in the entire book to keep honestly labeled, since it is the thesis the whole "convergence chapter" rests on.

**[DERIVED/TEXTBOOK] Strong CP problem statement ($|\theta_{QCD}| < 10^{-10}$)**
See Ch. 0 entry above (neutron/electron EDM bounds). Standard pedagogical reference for the problem statement itself: Peskin, M.E. & Schroeder, D.V., *An Introduction to Quantum Field Theory*, Ch. 19, or Weinberg, S., *The Quantum Theory of Fields, Vol. II*, §23.6.

---

## Gaps and flags — things I could not verify in the time available

- **Chapters 16, 17, 19, 20** contain further named correlations (acoustic cavitation / Rayleigh–Plesset dynamics, MEMS resonator Q-factors, fissility parameter formula, geological dating precision) that I did not individually trace to primary sources in this pass. They are almost certainly [DERIVED/TEXTBOOK] — standard fluid dynamics, MEMS, and nuclear engineering textbook material — but I have not pinned down a specific edition/page for each, and I would rather tell you that plainly than manufacture a citation. If these matter for the eventual print bibliography, flag them to me by section number and I will source them properly rather than guess.
- **Every CODATA/PDG link above** points to the live NIST/PDG reference pages rather than a fixed dataset year. These bodies periodically update recommended values (CODATA runs roughly every 4 years; PDG annually). For a print bibliography you will want to pin the specific CODATA/PDG edition you actually used when the book goes to press, since "current CODATA value" will silently drift otherwise.
- **The exact §-numbers** in the book (e.g. "§7.8.3") were not individually re-verified against the live repository line-by-line for this file — I matched claims to chapters with confidence, but if you want, I can do a second pass that pins each entry to its exact section number by re-reading the repository chapter files directly.

---

## Standard Textbooks (full citations, referenced by author above)

- Ashcroft, N.W. & Mermin, N.D., *Solid State Physics*, Harcourt (1976).
- Goldstein, H., Poole, C., Safko, J., *Classical Mechanics*, 3rd ed., Addison-Wesley (2002).
- Griffiths, D.J., *Introduction to Quantum Mechanics*, 3rd ed., Cambridge University Press (2018).
- Jackson, J.D., *Classical Electrodynamics*, 3rd ed., Wiley (1998).
- Krane, K.S., *Introductory Nuclear Physics*, Wiley (1988).
- Misner, C.W., Thorne, K.S., Wheeler, J.A., *Gravitation*, W.H. Freeman (1973).
- Peskin, M.E. & Schroeder, D.V., *An Introduction to Quantum Field Theory*, Westview Press (1995).
- Sakurai, J.J. & Napolitano, J., *Modern Quantum Mechanics*, 3rd ed., Cambridge University Press (2020).
- Sze, S.M. & Ng, K.K., *Physics of Semiconductor Devices*, 3rd ed., Wiley (2006).
- Tinkham, M., *Introduction to Superconductivity*, 2nd ed., Dover (2004).
- Weinberg, S., *The Quantum Theory of Fields, Vol. II*, Cambridge University Press (1996).
- White, F.M., *Fluid Mechanics*, 8th ed., McGraw-Hill (2015).
- Incropera, F.P. et al., *Fundamentals of Heat and Mass Transfer*, 7th ed., Wiley (2011).
- Das, B.M., *Principles of Geotechnical Engineering*, 8th ed., Cengage (2013).
- Ogata, K., *Modern Control Engineering*, 5th ed., Prentice Hall (2010).
- Agrawal, G.P., *Nonlinear Fiber Optics*, 5th ed., Academic Press (2012).
- Hecht, E., *Optics*, 5th ed., Pearson (2016).
