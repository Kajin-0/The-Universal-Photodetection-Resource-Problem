# AGENTS — Practical Temporal-Information Benchmarks

**Active branch:** `agent/practical-temporal-information-benchmarks`

The repository, not chat history, is authoritative.

## Mission

Create a fourth paper that brings the temporal-information resource program down to standard detector physics and builds explicit falsifiability into the presentation.

Do **not** turn this into another general resource-theory paper. The default test for every section is: can an experimental detector physicist identify what quantity would be measured and what observation would contradict the prediction?

## Frozen upstream inputs

Do not modify the scientific theorem/proof layers of:

1. PRX Quantum R3/R4 flagship `Two spectral-resource regimes for autonomous temporal information`;
2. random-time paper `Spectral Resource Laws for Temporal Fisher Information`;
3. PRA R1 `Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature`.

If the practical program exposes a genuine defect in an upstream theorem, record it immediately and stop using the affected claim until repaired. Otherwise upstream modifications should be limited to later small cross-reference/application paragraphs and only after Paper 4 has a stable result.

## Current frontier

WP01 has started the detector-language bridge.

Primary practical observables:

- modulation frequency `f` or angular frequency `Omega`;
- transfer responsivity `R(f)` in A/W or V/W;
- one-sided output noise PSD `S_n(f)` in A^2/Hz or V^2/Hz;
- conventional frequency-resolved `NEP(f)=sqrt(S_n(f))/|R(f)|` when the linear/PSD assumptions hold;
- raw photon/event timestamps and their likelihood under modulated illumination;
- timing-jitter distribution and characteristic function;
- dead-time/recovery statistics;
- optical carrier/sideband populations and their modulation curvature.

## Convention lock under development

All Fisher/PSD prefactors must be derived explicitly. Never write `F ~ R^2/S` without stating:

- one-sided versus two-sided PSD;
- peak versus RMS modulation amplitudes;
- observation duration;
- whether Fisher information refers to one quadrature or the trace of cosine/sine quadratures;
- units of the estimated parameters.

The current candidate convention is: for peak input quadratures `x,y` in watts, linear response `R(f)` and one-sided output PSD `S_n(f)`, long-time stationary Gaussian noise should give

`F_xx/T = F_yy/T = |R(f)|^2/S_n(f)`

and therefore

`Tr F/T = 2 |R(f)|^2/S_n(f) = 2/NEP(f)^2`.

This is provisional until WP01 is fully derived and cross-checked.

## Initial work packages

- **WP01:** Linear Gaussian detector: Fisher information, matched filtering, NEP, bandwidth, units and prefactors.
- **WP02:** Ideal Poisson timestamps + independent timing jitter.
- **WP03:** Dead time/recovery/memory and connection to the random-time spectral-resource theorem.
- **WP04:** Optical sideband survival-to-synthesis crossover with seeded and empty sidebands.
- **WP05:** Textbook resonant-exchange interpretation of the exact unitary-coupling cost.
- **WP06:** Integrated falsification matrix and minimal practical manuscript theorem stack.
- **WP07:** Dedicated prior-art/significance gate before manuscript drafting.

Work-package numbering may be extended only when necessary; do not create sidequests that do not sharpen measurement, falsifiability, or standard-physics interpretation.

## Publication criterion

Paper 4 is justified only if it produces at least one result beyond a tutorial restatement. Candidate publication-level contributions include:

- a rigorous convention-controlled equivalence between a standard detector metric and temporal Fisher-information rate that clarifies when conventional normalization fails;
- a generalized information-equivalent input-noise benchmark that remains meaningful for nonlinear/non-Gaussian/timestamp detectors, if prior art does not already subsume it;
- a new experimentally accessible survival/synthesis crossover prediction;
- a unified falsification protocol that tests the abstract resource inequalities with standard detector measurements;
- a nontrivial model comparison showing conventional bandwidth/NEP or D* can mis-rank detectors for temporal-information tasks.

If none survives prior-art review, do not force a fourth paper; retain the work as an applications/benchmarking note or additions to existing papers.

## Documentation rule

After every material advance, update the corresponding note and this handoff. When the program frontier changes, also update root `README.md`, `AGENTS.md`, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md` on this branch.
