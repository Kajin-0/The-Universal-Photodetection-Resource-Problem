# Novelty, Falsification, and Claim Discipline

## 1. What this project is allowed to claim now

As of initialization, the project may claim only that it is investigating the following question:

> Whether normalized optical information acquisition by a photodetector admits a nontrivial architecture-independent bound in terms of explicit thermodynamic, kinetic, optical, and quantum resources.

No universal theorem has yet been proved.

No claim of “first universal photodetector limit” is justified.

No claim that room-temperature LWIR performance is fundamentally bounded by a particular sensitivity-bandwidth-temperature product is justified.

## 2. What is already known nearby

The project starts with the recognition that prior work already establishes:

- architecture-dependent photodetector gain/speed tradeoffs;
- fully quantum photodetector models with coherence/backaction tradeoffs;
- thermodynamic and kinetic uncertainty relations for continuous measurements and stochastic currents;
- explicit nonequilibrium thermodynamic models of detector performance.

Therefore novelty must live in a narrower mathematical statement, stronger specialization, missing-resource theorem, counterexample, or physically important consequence.

## 3. Primary falsification target

The strongest naive conjecture would be something qualitatively like

\[
\mathcal J_{\rm det}
\le f(T,\dot\Sigma),
\]

where \(\mathcal J_{\rm det}\) is a sensitivity-speed/information-rate measure.

This conjecture should be treated as **likely too strong** until it survives explicit counterexamples.

Potential failure mechanisms include:

- arbitrarily high dynamical activity at low thermodynamic affinity;
- parallel replication of independent detector channels;
- omitted absorber area/volume or number of channels;
- externally supplied optical free energy hidden from \(\dot\Sigma\);
- hidden reservoir dissipation;
- metastability and near-zero modes;
- non-Markovian memory;
- quantum coherence or strong coupling;
- unconstrained source amplitude/bandwidth;
- deterministic output gain if the performance metric is badly defined.

## 4. Stronger candidate structure

A more plausible theorem class may require a resource vector

\[
R=(\Phi_\gamma,\mathcal A,\dot\Sigma,N_{\rm ch},E_{\rm bias},\ldots)
\]

and constrain either a frequency-resolved kernel

\[
K(\omega)
\]

or a normalized functional

\[
\mathcal J[K]
\]

rather than a simple scalar product such as detectivity times bandwidth.

## 5. Falsification hierarchy

Every candidate inequality must be attacked in this order.

### F1 — Coordinate invariance

Check invariance under changes of output gain, units, and parameterization.

### F2 — Dimensional closure

Verify both sides have identical dimensions without hidden normalization constants.

### F3 — Source-resource separation

Confirm that unlimited optical input power, bandwidth, squeezing, or prior information cannot trivially increase the left-hand side unless explicitly counted.

### F4 — Extensivity

Replicate the detector \(N\) times in parallel. Determine how both sides scale with \(N\). If the left side grows as \(N\) and the proposed resource is intensive, the bound is incomplete.

### F5 — Rate scaling

Apply \(W\mapsto cW\) in a Markov model. Track response, noise, activity, entropy production, and bandwidth as \(c\to\infty\).

### F6 — Affinity scaling

Take thermodynamic affinity toward zero while maintaining high traffic/activity. Test whether finite precision persists at vanishing entropy production.

### F7 — Metastable scaling

Take one transition rate \(\epsilon\to0\) and examine low-frequency susceptibility/noise divergences.

### F8 — Hidden-state construction

Add unobserved internal cycles or dissipative edges. Check whether the bound depends on total or visible resources.

### F9 — Coarse graining

Compare the complete measurement record to a lossy/coarse-grained output. A valid information statement should respect data processing.

### F10 — Quantum escape routes

Test coherence, nonclassical optical inputs, strong coupling, measurement backaction, and memory against the assumptions.

## 6. Publication-grade result standards

### Universal theorem

Must include:

- exact model class;
- assumptions;
- proof;
- dimensions;
- invariance checks;
- equality or tightness analysis;
- explicit detector interpretation;
- comparison to the closest existing uncertainty relation.

### Counterexample/no-go theorem

Must include:

- explicit physically admissible model family;
- exact or controlled asymptotic calculation;
- demonstration that the proposed resources remain fixed/bounded while the claimed performance escapes the bound;
- identification of the missing assumption/resource where possible.

### Corollary/application result

If a known general theorem already implies the result after variable mapping, label it honestly as a photodetection corollary/application unless the specialization itself creates a new nontrivial bound or engineering consequence.

## 7. Infrared claim discipline

Do not state that cryogenic cooling is fundamentally necessary for high-performance LWIR detection unless a proved theorem actually implies it under clearly stated assumptions.

Similarly, do not infer fundamental possibility merely because no current theorem forbids a room-temperature detector.

The scientifically meaningful outputs are quantitative lower/upper bounds on required resources or rigorous demonstrations that a proposed universal restriction cannot be established from the assumed resources.

## 8. Current status

**OPEN.** The project is in the definition, literature-closure, and finite-state formalism stage.
