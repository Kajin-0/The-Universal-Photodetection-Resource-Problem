# Research Roadmap

## Guiding principle

The project should advance by **closing logical gates**, not by accumulating loosely related calculations. A work package is complete only when its assumptions, result, adversarial checks, and consequences are recorded.

---

## WP0 — Definitions, invariances, and novelty closure

**Status:** OPEN

### Questions

1. What exactly is the optical input variable: power, photon flux, field quadrature, occupation perturbation, or transition-rate drive?
2. What output record is considered accessible?
3. What normalized detector performance functional is invariant to output gain and does not reward unlimited source energy?
4. Which quantities are extensive under parallel replication?
5. Which nearby general uncertainty relations already imply part of the desired result?

### Required outputs

- dimension table for every variable;
- explicit PSD convention;
- finite-time and asymptotic definitions;
- proof of invariance under output scaling;
- statement of source constraints;
- citation-chained novelty matrix.

### Gate WP0

Do not call any inequality “universal” until the left-hand performance functional and right-hand resources are operationally and dimensionally unambiguous.

---

## WP1 — General finite-state Markov photodetector calculus

**Status:** OPEN

### 1. Stationary state and projectors

For generator \(W_0\), construct

\[
W_0\pi=0,\qquad \mathbf 1^T\pi=1,
\]

and projectors

\[
\Pi=\pi\mathbf 1^T,\qquad Q=I-\Pi.
\]

Define the reduced resolvent/Drazin inverse needed to handle the stationary mode.

### 2. Linear susceptibility

For optical perturbation

\[
W(t)=W_0+\delta P(t)W_1,
\]

derive the state response and then the current response

\[
\chi_{IP}(\omega).
\]

Separate contributions from:

- modulation of occupation probabilities;
- direct modulation of counted transition intensities, if optical transitions are themselves counted/output-coupled.

### 3. Noise PSD

Derive exact stationary finite-frequency current noise for arbitrary counted edges using at least two independent methods where possible:

- counting-field tilted generator;
- correlation/resolvent method.

The result must include both singular shot-noise terms and dynamical correlations.

### 4. Thermodynamic bookkeeping

Write edge currents

\[
J_{ij}=W_{ij}\pi_j-W_{ji}\pi_i,
\]

edge activities

\[
A_{ij}=W_{ij}\pi_j+W_{ji}\pi_i,
\]

and steady-state entropy production in a local-detailed-balance representation.

### Gate WP1

A symbolic formula set that can reproduce two- and three-state examples and is independent of a specific photodetector architecture.

---

## WP2 — Minimal-model theorem/counterexample search

**Status:** OPEN

### Model ladder

1. two-state equilibrium absorber;
2. two-state driven absorber with explicit photon reservoir;
3. three-state detector with irreversible readout cycle;
4. three-state metastable gain detector;
5. parallel copies of the above;
6. high-activity/low-affinity cycle;
7. networks with hidden dissipative edges.

### For each model compute

- stationary distribution;
- response \(\chi_{IP}(\omega)\);
- PSD \(S_I(\omega)\);
- \(K(\omega)\);
- information functional(s);
- \(\dot\Sigma\);
- \(\mathcal A\);
- absorbed photon flux;
- equality/slack for every candidate inequality.

### Adversarial scalings

Explicitly study:

\[
W\mapsto cW,
\]

parallel replication \(N\to\infty\), weak affinity, strong affinity, metastable rates \(\epsilon\to0\), and optical coupling \(g\to0\) or \(g\to\infty\) where physically admissible.

### Gate WP2

Either:

- identify a candidate inequality surviving the full minimal-model suite; or
- produce a decisive counterexample and update the resource set.

---

## WP3 — Derive the first rigorous bound

**Status:** BLOCKED on WP0–WP2

Candidate mathematical tools:

- thermodynamic uncertainty relations;
- kinetic uncertainty relations;
- response uncertainty relations;
- Cauchy–Schwarz bounds in path space;
- Fisher-information identities for Markov trajectories;
- Cramér–Rao inequalities;
- data-processing inequalities;
- fluctuation-response identities;
- spectral-gap/resolvent inequalities;
- variational formulas for large-deviation rate functions.

### Target hierarchy

Rather than force one scalar product law, seek results such as

\[
K(\omega)\le B(\omega;\mathcal A,\dot\Sigma,\Phi_\gamma,\ldots)
\]

or

\[
\int d\omega\,w(\omega)K(\omega)
\le B(\mathcal A,\dot\Sigma,\Phi_\gamma,\ldots).
\]

The frequency-resolved form may be more fundamental than a single bandwidth number.

---

## WP4 — Tightness, saturation, and missing resources

**Status:** BLOCKED

For any proved inequality:

1. solve the equality conditions;
2. search for finite-state saturating models;
3. determine whether saturation requires singular limits;
4. quantify the gap for ordinary detector topologies;
5. determine whether the bound is useful or merely formally true.

A theorem too loose to exclude any physically relevant detector performance should not be oversold.

---

## WP5 — Semiclassical detector correspondence

**Status:** BLOCKED

Map the abstract resources onto conventional photodetector models:

- photoconductors;
- photodiodes;
- phototransistors;
- avalanche photodiodes;
- bolometric/thermal detectors where the input-output structure differs.

Important detector-native quantities to recover or reinterpret:

- responsivity \(R(\omega)\);
- NEP;
- \(D^*\);
- quantum efficiency;
- photoconductive gain;
- lifetime/transit-time gain-bandwidth relation;
- generation-recombination noise;
- shot noise;
- Johnson noise;
- dark current.

Determine which familiar engineering tradeoffs are special cases and which are unrelated to the universal theorem.

---

## WP6 — Quantum extension

**Status:** BLOCKED

Replace the classical generator with an open-quantum-system model, initially Markovian Lindblad dynamics with continuously monitored output trajectories.

Investigate:

- quantum Fisher information versus classical information in the measured record;
- coherence and backaction;
- quantum dynamical activity;
- perturbation-induced intersubspace terms;
- strong-coupling generalized activity;
- nonclassical optical inputs;
- detector/source entanglement;
- measurement inefficiency and hidden entropy production.

The quantum theorem must state whether the input field is treated as a resource, a prescribed signal, or part of the dynamical system.

---

## WP7 — Beyond Markovianity

**Status:** BLOCKED

Only after WP6 is stable, examine whether memory, structured reservoirs, non-Markovian feedback, or strong coupling permit violations of the Markov result or require generalized asymmetry/activity terms.

---

## WP8 — Infrared consequence

**Status:** BLOCKED

Apply only rigorously established results to the question:

> Can fundamental physics rule out, constrain, or permit a room-temperature MWIR/LWIR detector with simultaneously extreme sensitivity and bandwidth?

Avoid substituting known HgCdTe, InAsSb, T2SL, QWIP, graphene, or superconducting-device limitations for a universal statement.

Possible outputs:

- a true material-independent room-temperature LWIR bound;
- proof that no such bound follows from thermodynamics alone;
- a lower bound on required free-energy dissipation/activity at specified information rate;
- a resource cost comparison among detector classes.

---

## Publication logic

Potential papers should emerge from closed logical results, e.g.:

1. **Finite-state photodetection response–noise theorem/counterexample.**
2. **Thermokinetic resource bound for continuous photodetection.**
3. **Quantum photodetection information-resource bound.**
4. **Consequences for infrared detector sensitivity–bandwidth–temperature limits.**

No publication framing should be fixed before the mathematics identifies which of these actually exists.
