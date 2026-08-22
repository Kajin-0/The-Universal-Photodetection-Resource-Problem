# AGENTS — Temporal Information Resource Law Program

## Purpose

Durable handoff for the high-risk/high-ceiling theoretical program launched from Paper 2. This program is deliberately separate from the frozen Paper-2 manuscript.

Active branch: `agent/temporal-information-resource-law`.

## Non-negotiable scope

- Analytical/theoretical research only.
- Numerical counterexample searches are allowed.
- Do not require experiments, fabrication, procurement, or laboratory optimization as active next steps.
- Paper 2 Rev7 remains frozen unless a concrete defect is found.
- Do not assume a Nobel-scale result exists. The program is falsification-first.

## Grand question

> For an arbitrary physically realizable autonomous measurement apparatus with memory, what physical resources constrain the temporal spectrum of information transferable from a weak time-dependent perturbation to an accessible measurement record?

Paper 2 supplies the classical local observable:

`F_out[u,v] = Phi0/(2*pi) int G(omega) U*(omega)V(omega) domega`,

with `0 <= G <= 1` a.e. for autonomous parameter-independent classical Poisson detector channels.

The goal here is not merely to extend that theorem. It is to determine whether physical realizability imposes additional universal structure or resource costs on `G(omega)` (or on a quantum generalization), and to identify sharp counterexamples when it does not.

## Current decisive literature constraints

1. **Entropy production alone is not a universal information-acquisition resource.** Barato, Hartich, and Seifert (PRE 87, 042104, 2013) explicitly found no universal inequality forcing sensory-network information acquisition rate below thermodynamic entropy production.
2. **Frequency-domain nonequilibrium response/resource theory already exists.** Kwon et al. (arXiv:2605.05038, 2026) derive frequency-domain fluctuation-response identities and kinetic/thermodynamic uncertainty relations for Langevin and Markov jump systems.
3. **Dynamical activity already bounds generic Markov response precision.** Liu and Gu (Commun. Phys. 8, 62, 2025) derive response kinetic uncertainty relations using path Fisher information and dynamical activity.
4. **Autonomous quantum detector thermodynamics is an active frontier.** Schwarzhans et al., PRX Quantum 7, 033001 (2026), construct a minimal autonomous quantum detector thermal machine and find model-dependent tradeoffs among entropy production, efficiency, jitter, dead time, and dark counts.
5. Quantum continuous-measurement work already studies retrieval of output-field quantum Fisher information, so a generic claim that QFI should be optimized over temporally nonlocal measurements is not new.

Therefore the program must not claim novelty for generic FI-vs-dissipation, frequency-domain response uncertainty, dynamical-activity bounds, or autonomous-detector thermodynamics.

## Immediate research strategy

### Gate G1 — destroy naive resource laws

Construct explicit abstract detector/channel counterexamples against proposed universal lower bounds involving only:

- housekeeping entropy production;
- total entropy production;
- average power;
- ordinary dynamical activity;
- dead time / mean recovery time;
- finite-dimensional memory size.

Any surviving law must state the operational assumptions that exclude these counterexamples (durable record, reset, amplification, fixed input-event energy, finite timing reference, etc.).

### Gate G2 — classify information singularities

Study operating points where static/local homogeneous FI vanishes but dynamic Fisher spectrum is nonzero. Determine which structural mechanisms can create such zeros:

- non-injective stationary parameter maps;
- branch coalescence;
- conservation/symmetry constraints;
- hidden-state cancellation;
- quantum measurement-accessibility loss.

Seek a theorem beyond Type-II counters.

### Gate G3 — test causal spectral-factor structure

For causal autonomous channels, determine whether the conditional-score projection admits a causal factorization `A = B* B` and what, if anything, physical finite-memory/Markov assumptions add beyond arbitrary nonnegative Fourier multipliers. Do not assume causality alone constrains `G`; spectral factorization may make the class nearly arbitrary.

### Gate G4 — quantum accessibility gap

Formulate a careful quantum analogue only after the classical no-go structure is clear. Highest-interest target:

`G_accessible(omega) < G_quantum(omega)`

at an information singularity, with a physically meaningful alternative measurement recovering information inaccessible to a conventional detector record.

## Documentation rule

After every material theorem, counterexample, literature collision, or change in strategy:

1. update/create `grand_challenge/notes/WP*.md` immediately;
2. update this file if the active gates or central hypothesis change;
3. do not rely on chat history as the only record.
