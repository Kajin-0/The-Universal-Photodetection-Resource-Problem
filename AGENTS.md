# AGENTS.md

## Purpose

This file is the durable handoff record for any future agent working on **The Universal Photodetection Resource Problem (UPRP)**. Read this file, `README.md`, `PROBLEM.md`, `ROADMAP.md`, `docs/FORMALISM.md`, `docs/LITERATURE_MAP.md`, `docs/NOVELTY_AND_FALSIFICATION.md`, and the full `notes/RESEARCH_LOG.md` before doing new research.

The repository is the authoritative project memory. Do not rely on chat context surviving.

## Project objective

Determine whether a material-independent physical bound exists on the rate at which a finite-temperature photodetector can extract information from an optical field as a function of thermodynamic, kinetic, optical, and quantum resources.

A successful result can be:

1. a rigorous universal bound;
2. a rigorous counterexample disproving a proposed universal bound/resource set; or
3. proof that additional resources are necessary and identification of a sufficient resource set.

Do **not** assume the desired theorem exists.

## Research mode

This project is analytical/theoretical. Do not propose laboratory experiments, fabrication campaigns, sample procurement, or measurement programs as required next steps. Numerical algebra/simulation used to test conjectures is acceptable, but the research target is an analytical result.

## Central objects

Linear stationary transducer:

\[
Y(\omega)=\chi_{YP}(\omega)P(\omega)+N(\omega).
\]

Input-referred response-to-noise kernel:

\[
K(\omega)=\frac{|\chi_{YP}(\omega)|^2}{S_Y(\omega)}
=\frac{1}{\mathrm{NEP}^2(\omega)}.
\]

For a parameterized optical waveform, a candidate performance functional is

\[
\dot{\mathcal F}_{\theta}
=\int\frac{d\omega}{2\pi}
\frac{|\partial_\theta P(\omega)|^2}{\mathrm{NEP}^2(\omega)},
\]

with normalization conventions still to be fixed rigorously.

Candidate resource set initially includes

\[
\{T,\hbar\omega_{\rm opt},\Phi_\gamma,\dot\Sigma,\mathcal A,\eta_{\rm abs},\ldots\}.
\]

The ellipsis is intentional: one of the project's central tasks is to determine what resource variables are actually necessary.

## First model class

Finite-state continuous-time Markov detector:

\[
\dot{\mathbf p}=W(P)\mathbf p,
\qquad W(P)=W_0+P W_1+O(P^2).
\]

Measured current/counting record:

\[
I(t)=\sum_{ij}q_{ij}\,dN_{ij}(t).
\]

Initial admissibility assumptions:

- local detailed balance for thermal transitions;
- explicit optical transitions and photon-energy accounting;
- stationary dark state;
- causal response;
- finite entropy-production rate;
- finite dynamical activity;
- explicit observable/output record;
- arbitrary finite number of internal states.

These assumptions are provisional. Every assumption must be labeled as physical, technical, or merely convenient.

## Immediate research priorities

### Priority 1 — Make the performance functional invariant and dimensionally clean

The present Fisher-information-rate expression depends on waveform normalization and PSD conventions. Before proving anything universal, define a detector-only quantity or a properly constrained channel-estimation problem. Check:

- dimensions;
- one-sided versus two-sided PSD;
- finite observation time versus asymptotic rate;
- scaling under redefinition of optical input amplitude;
- scaling under deterministic output gain;
- whether the quantity is invariant under invertible output post-processing.

### Priority 2 — Exact Markov response and noise

Derive \(\chi_{IP}(\omega)\) and \(S_I(\omega)\) for a general finite-state generator using resolvents/pseudoinverses and counting-field formalism. Record assumptions carefully.

### Priority 3 — Test existing uncertainty relations

Determine whether thermodynamic uncertainty relations (TURs), kinetic uncertainty relations (KURs), response uncertainty relations, Cramér-Rao bounds, fluctuation-response relations, or data-processing inequalities can be combined into a photodetector-specific bound.

Do not merely cite these literatures; map their variables to detector observables explicitly.

### Priority 4 — Search for counterexamples before theorem polishing

At minimum test:

- two-state absorber/readout models;
- three-state irreversible amplification cycles;
- parallel independent channels;
- high-rate/low-affinity networks;
- passive noiseless output gain (to verify invariance);
- arbitrarily large state-space replication;
- dark-state metastability;
- near-critical/slow-mode limits;
- zero-temperature and equilibrium limits;
- high photon-flux and weak-signal limits.

If a candidate inequality fails, preserve the counterexample and update the resource set.

## Literature anchors known at project initialization

These are starting points, not a complete novelty review:

- S. M. Young, M. Sarovar, F. Léonard, **Fundamental limits to single-photon detection determined by quantum coherence and backaction**, Phys. Rev. A 97, 033836 (2018), DOI `10.1103/PhysRevA.97.033836`.
- S. M. Young, M. Sarovar, F. Léonard, **General modeling framework for quantum photodetectors**, Phys. Rev. A 98, 063835 (2018).
- V. J. Sorger, R. Maiti, **Roadmap for Gain-Bandwidth-Product Enhanced Photodetectors**, arXiv:2006.16937 (2020).
- Y. Hasegawa, **Quantum Thermodynamic Uncertainty Relation for Continuous Measurement**, Phys. Rev. Lett. 125, 050601 (2020), DOI `10.1103/PhysRevLett.125.050601`.
- E. Schwarzhans et al., **Quantum detectors as autonomous machines: assessing the nonequilibrium thermodynamics of information acquisition**, arXiv:2508.16375 (2025).
- K. Liu, J. Gu, **Response kinetic uncertainty relation for Markovian open quantum systems**, Phys. Rev. A 113, 062443 (2026), DOI `10.1103/ps1b-8l1x`.
- G. Blasi et al., **Quantum Kinetic Uncertainty Relations in Mesoscopic Conductors at Strong Coupling**, Phys. Rev. Lett. 137, 056302 (2026), DOI `10.1103/9xcz-nlqk`.
- T. Vu et al., **Universal Precision Limits in General Open Quantum Systems**, Phys. Rev. Lett. 136, 190401 (2026), DOI `10.1103/kldv-l3wl`.

Never claim novelty solely because these papers do not obviously contain the target theorem. Perform citation chaining and targeted searches before any publication claim.

## Current novelty hypothesis

**Provisional only:** the likely gap is not “thermodynamics constrains detectors” or “photodetectors have tradeoffs.” Those already exist. The candidate novelty is a **photodetection-specific, architecture-independent information-rate bound expressed in detector-native quantities and tied to explicit thermodynamic/kinetic resources**, or a proof that no such bound exists without additional resources.

This wording should remain conservative until the literature audit is closed.

## Mandatory adversarial checks for every candidate theorem

Before labeling any inequality a theorem candidate, answer all of the following:

1. Is it dimensionally correct?
2. Is it invariant to output gain and unit redefinitions?
3. Does deterministic invertible post-processing leave the detector information unchanged as expected?
4. Can independent parallel detector copies violate it by extensive scaling?
5. Is detector area, number of channels, absorber volume, or another extensivity variable missing?
6. What happens at equilibrium where \(\dot\Sigma=0\)?
7. Can activity diverge while entropy production remains bounded?
8. What happens as a relaxation eigenvalue approaches zero?
9. What happens as rates uniformly scale to infinity?
10. What happens in the weak optical perturbation limit?
11. Does photon shot noise/input quantum noise need to be included on the left, right, or excluded by conditioning on the input field?
12. Does the statement accidentally bound the source rather than the detector?
13. Does coarse graining of the output record weaken or invalidate the claimed bound?
14. Are hidden degrees of freedom carrying uncounted dissipation/activity?
15. Can feedback, nonreciprocity, coherence, squeezing, or non-Markovianity evade the assumptions?

## Recordkeeping protocol

After each substantive research step:

1. update `notes/RESEARCH_LOG.md` with date, question, derivation/result, status, and next action;
2. update the relevant formalism/literature file if the result changes project assumptions;
3. preserve failed conjectures and counterexamples;
4. commit enough context that a new agent can resume from the repository alone.

Do not allow important results to live only in chat.

## Status vocabulary

Use these labels consistently:

- **PROVED** — complete derivation with assumptions explicitly stated.
- **VERIFIED** — independently checked algebraically/numerically but not yet formalized as a proof.
- **CONJECTURE** — plausible unproved statement.
- **COUNTEREXAMPLE** — explicit admissible model violating a conjecture.
- **OPEN** — unresolved.
- **BLOCKED** — cannot proceed without a missing theoretical input or source.
- **REJECTED** — approach shown invalid or redundant.

## Project state at initialization — 2026-08-19

- Repository initialized.
- No universal photodetection resource theorem has been proved.
- No counterexample has yet closed the problem.
- The Fisher-information-rate formulation is a **candidate framework**, not yet normalized sufficiently for a universal theorem.
- Finite-state Markov photodetectors are the first target model class.
- Entropy production alone is not assumed sufficient; dynamical activity and other resources are explicitly under consideration.
- The most important immediate task is to establish an invariant detector performance functional and derive exact general Markov response/noise formulas.
