# Practical temporal-information benchmarks

**Branch:** `agent/practical-temporal-information-benchmarks`

## Purpose

Develop a fourth, deliberately grounded paper that translates the existing temporal-information resource program into standard detector physics and explicit falsification tests.

This program is **not** another abstraction layer and does not alter the frozen theorem/proof stacks of the three existing papers.

Working paper concept:

> **Operational benchmarks for temporal information in photodetection**

Alternative working title:

> **Falsifiable temporal-information bounds for photodetection: from noise-equivalent power to spectral survival and sideband synthesis**

## Core thesis

For conventional linear photodetection, temporal Fisher information can be written directly in terms of experimentally familiar quantities such as frequency-dependent responsivity and noise power spectral density. For photon-counting detectors it can be extracted directly from timestamp likelihoods. These ordinary measurement languages can then be used to formulate explicit experimental falsification tests of the survival/synthesis resource laws.

The intended logical bridge is:

`responsivity + noise PSD -> Fisher-information spectrum`

`timestamp likelihood -> Fisher-information spectrum`

`pre-existing sideband occupancy -> survival regime`

`baseline-empty sideband generation -> synthesis regime`

`prescribed synthesis curvature -> minimum unitary coupling in the companion implementation class`

## Initial target results

1. Derive the exact convention-controlled relation between two-quadrature Fisher-information rate and NEP for a linear detector in additive stationary Gaussian noise.
2. Define and audit whether a generalized Fisher-equivalent input-noise metric is useful beyond the Gaussian/linear limit; do not claim novelty before a dedicated prior-art gate.
3. Derive the ideal Poisson timestamp Fisher spectrum and the exact independent-jitter attenuation factor.
4. Connect dead time/recovery/memory models to the existing random-time spectral-resource paper using measurable timestamp statistics.
5. Construct a standard optical sideband model that interpolates between pre-seeded spectral survival and baseline-empty second-order synthesis.
6. State every central prediction in a falsifiable form: required measurements, predicted inequality/equality, and what observation would contradict it.
7. Translate the unitary-coupling companion theorem into at least one textbook resonant-exchange Hamiltonian without changing the theorem's scope.

## Model set

Keep the practical paper small enough to remain coherent. Default examples:

- linear photodiode / RC or transit-time limited detector;
- photoconductor with lifetime pole and colored noise;
- photon counter with timing jitter and dead time/recovery;
- optical phase/amplitude sideband generation as a survival-to-synthesis crossover model.

## Claim discipline

- No claim that conventional NEP is new.
- No claim that Fisher information as a detector metric is new without a dedicated literature review.
- No claim that `NEP_F` or any proposed generalized metric is novel until exact prior art is checked.
- No experimental result may be implied unless actual data are analyzed.
- The paper may propose executable experiments and falsification protocols, but theoretical predictions must be clearly separated from measured validation.
- Preserve the distinction between unitary coupling cost and thermodynamic work, peak interaction strength, controller bandwidth, or fixed-controller-spectrum cost.

## Relationship to the three existing papers

1. **Two spectral-resource regimes for autonomous temporal information** — supplies the survival/synthesis taxonomy and sharp resource inequalities.
2. **Spectral Resource Laws for Temporal Fisher Information** — supplies the broader random-time/timestamp spectral theory.
3. **Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature** — supplies the exact implementation interpretation of prescribed rank-changing curvature.

This fourth program translates those results into detector observables and falsification procedures. It should remain scientifically useful even to readers who never adopt the full abstract resource language.

## Documentation rule

Every material derivation, failed derivation, convention correction, prior-art collision, model choice, falsification criterion, or publication-scope decision must be recorded in `practical_temporal_information/notes/` and reflected in `AGENTS.md` and the repository landing files when it changes the program frontier.
