# Literature Map and Novelty Risk

## Purpose

This is a **living map of adjacent theory**, not a completed review. Its main role is to prevent false novelty claims and identify which mathematical machinery may already imply parts of the Universal Photodetection Resource Problem.

The project should distinguish four questions:

1. Are there known architecture-specific photodetector tradeoffs?
2. Are there known general quantum-photodetector performance frameworks?
3. Are there known thermodynamic/kinetic uncertainty relations for monitored stochastic or quantum systems?
4. Has anyone already specialized those results into a detector-native, optical-information-rate bound with explicit photonic and thermodynamic resources?

Only Question 4 corresponds closely to the present novelty hypothesis.

---

## A. Photodetector-specific performance limits

### Young, Sarovar, Léonard (2018)

**Fundamental limits to single-photon detection determined by quantum coherence and backaction**  
Phys. Rev. A 97, 033836 (2018)  
DOI: `10.1103/PhysRevA.97.033836`

Relevance:

- fully quantum treatment of field, absorption, and amplification;
- exposes tradeoffs caused by coherence and amplification backaction;
- explicitly studies efficiency, dark counts, and timing behavior;
- demonstrates that detector architecture and the quantum-classical interface matter.

Novelty risk:

- high for any claim phrased broadly as “first fundamental photodetector performance limit”;
- lower for a continuous, finite-temperature, thermodynamic/kinetic information-rate theorem if that result is genuinely absent.

### Young, Sarovar, Léonard (2018)

**General modeling framework for quantum photodetectors**  
Phys. Rev. A 98, 063835 (2018)  
DOI: `10.1103/PhysRevA.98.063835`

Relevance:

- provides a general coupled quantum framework for photon field, absorption, and amplification;
- defines ideal photodetector performance and studies architecture-induced tradeoffs;
- likely important for later quantum-phase mapping.

Novelty risk:

- any “general framework for photodetectors” claim is already occupied;
- our contribution must be a different mathematical statement: resource-bounded information acquisition or a no-go theorem.

### Sorger and Maiti (2020)

**Roadmap for Gain-Bandwidth-Product Enhanced Photodetectors**  
arXiv:2006.16937

Relevance:

- emphasizes sensitivity/gain versus temporal response tradeoffs;
- derives practical/scaling constraints tied to detector dimensions, mobility, resistance, optical confinement, and contacts.

Novelty risk:

- shows that gain-bandwidth limits already have a substantial device-physics literature;
- a universal theorem must clearly separate material/geometry scaling laws from thermodynamic or information-theoretic bounds.

---

## B. Continuous-measurement thermodynamic uncertainty relations

### Hasegawa (2020)

**Quantum Thermodynamic Uncertainty Relation for Continuous Measurement**  
Phys. Rev. Lett. 125, 050601 (2020)  
DOI: `10.1103/PhysRevLett.125.050601`

Relevance:

- uses quantum estimation theory;
- derives universal fluctuation bounds for continuous measurements under stated scaling conditions;
- provides bounds involving dynamical activity and entropy production.

Novelty risk:

- **very high**. Any claim that “continuous measurement precision is universally bounded by entropy production/activity” is not new.
- Critical task: determine whether its inequalities can be mapped directly to optical response sensitivity and detector Fisher information. If yes, the project may become a specialization/tightening/counterexample study rather than a wholly new theorem class.

### Hasegawa (2021)

**Thermodynamic Uncertainty Relation for General Open Quantum Systems**  
Phys. Rev. Lett. 126, 010602 (2021)  
DOI: `10.1103/PhysRevLett.126.010602`

Relevance:

- extends uncertainty-relation logic beyond standard Markov-process formulations;
- introduces survival activity and discusses continuous measurement.

Novelty risk:

- reinforces that generic “quantum measurement precision bound” language is too broad for novelty.

---

## C. Detector thermodynamics

### Schwarzhans et al. (2025)

**Quantum detectors as autonomous machines: assessing the nonequilibrium thermodynamics of information acquisition**  
arXiv:2508.16375 (2025)

Relevance:

- explicitly treats a quantum particle detector as an autonomous thermal machine;
- studies entropy production against detection efficiency, gain, jitter, dead time, and dark counts;
- directly connects detector quality to nonequilibrium resource expenditure.

Novelty risk:

- **very high** for any generic statement that “better detector performance costs dissipation.”
- The present project must go beyond this by deriving a detector-native information-rate bound valid across a broader class, or by proving such a universal reduction is impossible.

---

## D. Response and kinetic uncertainty relations

### Liu and Gu (2026)

**Response kinetic uncertainty relation for Markovian open quantum systems**  
Phys. Rev. A 113, 062443 (2026)  
DOI: `10.1103/ps1b-8l1x`

Relevance:

- directly bounds response precision for measured trajectory observables under perturbations;
- involves conventional quantum dynamical activity plus a perturbation-induced intersubspace transition term;
- especially relevant because photodetection is inherently a response problem.

Novelty risk:

- **critical**. This may contain mathematical machinery closest to the target theorem.
- Required action: derive the classical limit and attempt an explicit mapping \(\delta P\to\) optical perturbation and measured trajectory current \(\to\) detector output.

### Blasi et al. (2026)

**Quantum Kinetic Uncertainty Relations in Mesoscopic Conductors at Strong Coupling**  
Phys. Rev. Lett. 137, 056302 (2026)  
DOI: `10.1103/9xcz-nlqk`

Relevance:

- generalizes dynamical activity to strong system-reservoir coupling;
- shows standard KURs can break down at strong coupling;
- introduces a quantum KUR with intrinsic coherent contributions.

Novelty risk:

- indicates that “activity” is not a unique/simple resource outside weak-coupling Markov limits;
- any quantum photodetector theorem may require generalized activity rather than the classical jump-rate definition.

### Vu, Honma, Saito (2026)

**Universal Precision Limits in General Open Quantum Systems**  
Phys. Rev. Lett. 136, 190401 (2026)  
DOI: `10.1103/kldv-l3wl`

Relevance:

- derives precision bounds for generic observables in general open quantum systems;
- includes entropy-production/asymmetry structure and generalized activity;
- reaches beyond conventional Markovian weak-coupling assumptions.

Novelty risk:

- high for any ultimate quantum-generalization claim;
- the likely value of UPRP is therefore not generic precision theory itself, but the **photodetection-specific mapping, optical resource accounting, detector-native objective, and resulting consequences/counterexamples**.

---

## E. Current novelty hypothesis

The following broad claims are **not** novel:

- photodetectors possess sensitivity-speed or gain-bandwidth tradeoffs;
- fully quantum photodetector models exhibit coherence/backaction tradeoffs;
- continuous-measurement precision can be constrained by entropy production or dynamical activity;
- detector performance can depend on nonequilibrium dissipation;
- kinetic uncertainty relations constrain current precision.

The candidate open gap is narrower:

> Determine whether one can derive a **photodetection-specific, architecture-independent bound on normalized optical information acquisition**, written in detector-native quantities such as input-referred response/noise and tied to explicit optical, thermodynamic, and kinetic resources; or prove that no finite bound exists for a proposed resource set.

Even this is **PROVISIONAL** until citation chaining and theorem-level comparison are complete.

---

## F. Mandatory literature-comparison questions

For each candidate theorem we derive, compare it line-by-line against the closest prior uncertainty relation:

1. Is our left-hand quantity mathematically identical to a known response precision or trajectory SNR after a change of notation?
2. Is our right-hand resource identical to entropy production/activity already used in a known theorem?
3. Does explicit optical photon-flux/energy bookkeeping add a genuinely new constraint?
4. Does frequency resolution \(K(\omega)\) produce a stronger statement than known time-integrated current bounds?
5. Does the theorem survive arbitrary detector architectures inside the stated class?
6. Does it imply a detector-specific engineering consequence that the generic theorem does not?
7. If the generic theorem already implies ours, is our contribution only a corollary/application?
8. If known bounds fail in a photodetection setting, can we prove the failure and identify the missing resource?

---

## G. Search branches still required

This literature map is incomplete. Priority searches include:

- classical response uncertainty relations for continuous-time Markov chains;
- Fisher information of Markov jump trajectories under rate perturbations;
- information-thermodynamic sensor bounds;
- biochemical sensing speed-accuracy-energy tradeoffs;
- communication-channel bounds for photodetection;
- quantum-limited linear amplifiers and photodetection noise;
- Bode/Fano, causality, passivity, and response-bandwidth integral bounds;
- optical absorption bandwidth/sum-rule bounds;
- stochastic thermodynamics of sensing and transduction;
- speed-limit literature for Markov and open quantum systems;
- non-Markovian precision bounds;
- input-output quantum estimation under finite photon flux.

No novelty claim should be finalized until these branches are reviewed.
