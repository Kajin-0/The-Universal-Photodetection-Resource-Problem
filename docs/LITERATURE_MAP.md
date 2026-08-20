# Literature Map and Novelty Risk

## Purpose

This is a living theorem-level map of adjacent theory. It exists to prevent false novelty claims and to identify which existing machinery already implies parts of the Universal Photodetection Resource Problem (UPRP).

The project now distinguishes five questions:

1. Are architecture-specific photodetector tradeoffs known? **Yes.**
2. Are general fully quantum photodetector models known? **Yes.**
3. Are general thermodynamic/kinetic response and precision bounds known? **Yes.**
4. Are optical LDOS / absorption / power-bandwidth limits known? **Yes.**
5. Has the specific missing-resource problem been closed: an architecture-independent optical-input-to-electrical-information speed theorem that explicitly combines microscopic light–matter coupling, finite optical task bandwidth, and thermokinetic detector resources? **Not yet established; remains the current novelty hypothesis.**

---

# A. Quantum photodetector frameworks

## Young, Sarovar, Léonard (2018)

**Fundamental limits to single-photon detection determined by quantum coherence and backaction**  
Phys. Rev. A 97, 033836 (2018)  
DOI `10.1103/PhysRevA.97.033836`

Relevance:

- treats field, optical absorption, internal localization, and amplification in one quantum model;
- identifies coherence/backaction tradeoffs;
- studies efficiency, dark counts, and jitter;
- in the dark-state configuration, reports that near-perfect detection is obtained when optical coupling `gamma` and localization rate are made arbitrarily large compared with the photon-wavepacket timescale.

Novelty consequence:

- generic claims that quantum photodetectors have fundamental tradeoffs are occupied;
- more importantly, the model explicitly contains an **unbounded optical-coupling escape hatch**. UPRP WP4 isolates this same degree of freedom in a reversible Markov no-go theorem.
- A potentially distinct contribution is therefore to identify the physical resource represented by `gamma` and prove what happens once it is bounded by microscopic matter/electromagnetic constraints.

## Young, Sarovar, Léonard (2018)

**General modeling framework for quantum photodetectors**  
Phys. Rev. A 98, 063835 (2018)  
DOI `10.1103/PhysRevA.98.063835`

Relevance:

- general coupled quantum framework for field, absorption, and amplification;
- important target formalism for quantum extension of UPRP.

Novelty risk:

- “general framework for photodetectors” is not new;
- UPRP must contribute a resource theorem/no-go result, not merely a framework.

---

# B. Device-physics gain/speed tradeoffs

## Sorger and Maiti (2020)

**Roadmap for Gain-Bandwidth-Product Enhanced Photodetectors**  
arXiv:2006.16937

Relevance:

- gain/responsivity versus temporal response;
- device-geometry, mobility, resistance, waveguide, and contact scaling.

Novelty consequence:

- conventional photodetector gain-bandwidth limits are architecture/material dependent;
- UPRP must distinguish such scaling laws from a theorem about necessary physical resources.

---

# C. Continuous-measurement and open-system precision bounds

## Hasegawa (2020)

**Quantum Thermodynamic Uncertainty Relation for Continuous Measurement**  
Phys. Rev. Lett. 125, 050601 (2020)  
DOI `10.1103/PhysRevLett.125.050601`

Relevance:

- quantum estimation-theoretic continuous-measurement uncertainty relations;
- bounds involving dynamical activity and entropy production.

Novelty consequence:

- “measurement precision is constrained by thermodynamic/kinetic resources” is not new.

## Hasegawa (2021)

**Thermodynamic Uncertainty Relation for General Open Quantum Systems**  
Phys. Rev. Lett. 126, 010602 (2021)  
DOI `10.1103/PhysRevLett.126.010602`

Relevance:

- general open-system precision bounds and survival activity.

---

# D. Detector thermodynamics

## Schwarzhans et al. (2025/2026)

**Quantum detectors as autonomous machines: assessing the nonequilibrium thermodynamics of information acquisition**

Relevance:

- detector quality versus entropy production;
- efficiency, gain, jitter, dead time, dark counts;
- directly overlaps detector thermodynamics.

Novelty consequence:

- generic dissipation-performance tradeoffs are occupied;
- UPRP must provide a different theorem structure or an explicit insufficiency result.

---

# E. Finite-frequency response and kinetic uncertainty relations

## Dechant (2026)

**Finite-Frequency Fluctuation-Response Inequality**  
Phys. Rev. Lett. 136, 207101 (2026)  
DOI `10.1103/3hs9-dz3d`

Relevance:

- general finite-frequency fluctuation-response inequality for Markov dynamics, including jump processes;
- broadband SNR consequences.

Novelty consequence:

- generic finite-frequency `response/noise` bounds are occupied.

## Liu and Gu (2026)

**Response kinetic uncertainty relation for Markovian open quantum systems**  
Phys. Rev. A 113, 062443 (2026)  
DOI `10.1103/ps1b-8l1x`

Relevance:

- response precision bounded by activity-like resources in monitored open quantum systems.

## Gu and Liu (2026)

**Finite-frequency fluctuation-response bounds for open quantum systems**  
arXiv:2605.03340

Relevance:

- downstream measured response precision bounded by output-field QFI and signal-channel activity.

## Zheng and Lu (2026)

arXiv:2602.18631

Relevance:

- finite-frequency kinetic/thermodynamic response bounds for specific perturbation classes.

## Blasi et al. (2026)

**Quantum Kinetic Uncertainty Relations in Mesoscopic Conductors at Strong Coupling**  
Phys. Rev. Lett. 137, 056302 (2026)

Relevance:

- warns that classical activity is not sufficient outside weak-coupling Markov regimes.

## Vu et al. (2026)

**Universal Precision Limits in General Open Quantum Systems**  
Phys. Rev. Lett. 136, 190401 (2026)

Relevance:

- generic open-system precision bounds; high novelty risk for any overly broad quantum claim.

---

# F. Temporal-Fisher speed limits

## Nishiyama and Hasegawa (2026)

**Unified speed limits in classical and quantum dynamics via temporal Fisher information**  
Phys. Rev. E 114, 014120 (2026)  
DOI `10.1103/x95d-fhpq`

Relevance:

- temporal Fisher information bounded by physical costs;
- in open quantum systems the relevant speed resource involves interaction-Hamiltonian energetic fluctuations/effective interaction terms.

Novelty consequence:

- UPRP should not claim that interaction strength limits state-evolution speed as a general principle;
- however, this literature independently supports WP4's conclusion that **entropy production alone does not provide the absolute microscopic timescale**.
- Distinction: temporal FI concerns information about elapsed time/state evolution; UPRP concerns transfer of an externally encoded optical signal into an electrical record.

---

# G. Matter-side optical sum rules

## Thomas–Reiche–Kuhn / f-sum rule

Relevance:

- constrains total oscillator strength / dipole matrix elements;
- provides a matter-side budget for light–matter coupling.

For a free-space electric-dipole transition, combining TRK with the spontaneous-emission formula yields the UPRP free-space corollary

\[
\Gamma_0\le
\frac{N_e e^2\omega_0^2}{2\pi\epsilon_0m_ec^3}.
\]

Novelty consequence:

- this relation is not itself the target novelty;
- `N_e` is extensive and photonic-environment enhancement remains uncontrolled.

Recent semiconductor-specific TRK work: A. Huamán, **The Thomas-Reiche-Kuhn sum rule as a consequence of a non-singular optical susceptibility in semiconductors**, arXiv:2601.00762 (2026).

---

# H. Electromagnetic LDOS / power-bandwidth limits

## Shim, Fan, Johnson, Miller (2019)

**Fundamental Limits to Near-Field Optical Response over Any Bandwidth**  
Phys. Rev. X 9, 011043 (2019)  
DOI `10.1103/PhysRevX.9.011043`

Relevance:

- derives LDOS sum rules and arbitrary-bandwidth power-bandwidth limits from causality and energy conservation;
- directly bounds spontaneous-emission enhancement over finite optical bandwidths;
- separates single-frequency enhancement from finite-band achievable response;
- identifies material susceptibility and geometry/separation as necessary resources.

Key conceptual result relevant to UPRP:

- single-frequency LDOS can become arbitrarily large in some ideal lossless resonant limits;
- average response over any nonzero bandwidth has a finite upper bound once the electromagnetic resource class is specified.

This is extremely important for the next UPRP step because baseband modulation to `Omega_s` generates optical sidebands around the carrier. An optical frontend that only has an infinitesimally narrow enhancement cannot preserve arbitrary modulation bandwidth.

Novelty consequence:

- UPRP must not claim optical power-bandwidth limits themselves;
- the possible new result is their **composition with photodetection information transfer and thermokinetic transduction constraints**.

## Chao et al. (2022+)

**Maximum Electromagnetic Local Density of States via Material Structuring**  
arXiv:2209.08668 and subsequent work.

Relevance:

- geometry-independent/numerically tight LDOS bounds over bandwidths using material susceptibility and footprint.

## Miller et al. (2016)

**Fundamental limits to optical response in absorptive systems**

Relevance:

- per-volume bounds on absorption/scattering/LDOS based on material susceptibility figure of merit.

## Yu, Raman, Fan (2012)

**Thermodynamic Upper Bound on Broadband Light Coupling with Photonic Structures**  
Phys. Rev. Lett. 109, 173901 (2012)

Relevance:

- upper bound on aggregate external coupling rates of optical modes;
- another possible route to an optical coupling resource for UPRP.

## 2026 broadband absorption work

Recent PRX Energy work derives upper bounds on broadband absorption in open dissipative systems using overlapping resonances and decay-rate structure. Relevant as a modern absorption-side comparison; do not assume it directly implies the UPRP information theorem.

---

# I. Spontaneous emission / LDOS dependence

Primary literature establishes that spontaneous-emission rates depend on the electromagnetic Green tensor / LDOS and can be strongly modified by photonic environments (Purcell physics). Relevant examples include Sauvan et al., Phys. Rev. Lett. 110, 237401 (2013), and quantum-dot LDOS measurements such as Leistikow et al., Phys. Rev. B 79, 045301 (2009).

For active/gain media, simple LDOS-only golden-rule formulas require correction; see Franke et al., Phys. Rev. Lett. 127, 013602 (2021). UPRP should therefore restrict any LDOS-based completion theorem to passive linear environments unless the active-medium quantum noise/pumping resource is explicitly included.

---

# J. Current novelty hypothesis after WP4

The following are **not novel**:

- sensitivity-speed/gain-bandwidth tradeoffs in photodetectors;
- quantum photodetector coherence/backaction tradeoffs;
- thermodynamic precision bounds;
- finite-frequency fluctuation-response bounds;
- detector dissipation versus jitter/dark-count tradeoffs;
- oscillator-strength sum rules;
- LDOS and optical power-bandwidth limits.

The current candidate novelty is much narrower:

> **A photodetection-specific no-go/completion theorem showing that fixed temperature, photon energy, optical detailed balance, useful throughput, stationary activity, and entropy production do not determine an absolute detector speed scale; an explicit microscopic light–matter coupling resource is necessary, and when a physically bounded matter+electromagnetic coupling functional is supplied, it combines with detector thermokinetic constraints to bound optical-to-electrical information bandwidth.**

WP4 already proves the no-go part for a nontrivial reversible finite-state Markov event-detector class. The completion with an architecture-independent matter+EM finite-band resource remains OPEN.

---

# K. Mandatory comparison questions

For every theorem candidate:

1. Is the left side just a known response precision after notation changes?
2. Is the right side a known TUR/KUR/activity bound?
3. Does the theorem add a genuine optical input/resource constraint?
4. Is the microscopic coupling resource independent, or merely a restatement of detector bandwidth?
5. Does TRK constrain only matter while LDOS/environment remains free?
6. Does an optical power-bandwidth theorem already imply the proposed result without detector thermodynamics?
7. Does the result survive detector replication / increasing participating electron number?
8. Does it require passive, reciprocal, Markovian, or weak-coupling assumptions?
9. Is coherent optical drive being incorrectly represented as a thermal jump reservoir?
10. Can the theorem be stated directly in the fully quantum input-output formalism?

---

# L. Highest-priority literature/theorem work

1. Extract a usable finite-band LDOS/coupling inequality from Shim et al. and later LDOS-bound work in notation suitable for photodetection.
2. Derive the carrier-sideband/baseband information mapping.
3. Determine whether TRK + finite-band LDOS is sufficient to bound the optical coupling functional for a fixed absorber size/electron number and passive environment class.
4. Map the result into Young–Sarovar–Léonard's coupling operator `L` / optical rate `gamma`.
5. Compare the resulting quantum resource with `Var(H_int)` in Nishiyama–Hasegawa.
6. Search for any existing theorem already composing optical power-bandwidth limits with detector Fisher information or DQE. Until that search is closed, novelty remains provisional.
