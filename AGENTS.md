# AGENTS.md

## Purpose

Durable project handoff for The Universal Photodetection Resource Problem. The repository, not chat history, is authoritative.

## Active branch and current program

**Active branch:** `agent/practical-temporal-information-benchmarks`

The three mature temporal-information papers remain scientifically frozen in their theorem/proof layers. A separate fourth program is active to connect them to standard detector physics and explicit falsification tests.

Read first:

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `practical_temporal_information/AGENTS.md`
3. `practical_temporal_information/notes/WP01_LINEAR_GAUSSIAN_FISHER_NEP_BRIDGE.md`
4. `practical_temporal_information/notes/WP02_POISSON_TIMESTAMPS_AND_JITTER.md`
5. `manuscript/THREE_PAPER_PUBLICATION_ARCHITECTURE_2026-08-23.md`
6. `manuscript/autonomous_temporal_information/MANUSCRIPT_HANDOFF.md`
7. `manuscript/dynamical_implementation_cost/MANUSCRIPT_HANDOFF.md`

## Mature paper architecture — preserve

1. **PRX Quantum flagship:** *Two spectral-resource regimes for autonomous temporal information* — R3 frozen theorem/proof baseline; R4 current journal-facing bridge revision.
2. **Broad operational spectral paper:** *Spectral Resource Laws for Temporal Fisher Information* — independent random-time/spectral-survival track.
3. **PRA dynamical completion:** *Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature* — frozen reviewer-repaired PRA R1 package.

Do not concatenate these papers and do not import their full proof stacks into Paper 4.

## Paper 4 mission

Working title: **Operational benchmarks for temporal information in photodetection**.

Every central statement should identify measured quantities, predicted equality/inequality, nuisance assumptions, and an observation that would contradict it.

## Current frontier

### WP01 — linear Gaussian detector

For peak optical-power quadratures, one-sided output PSD `S_n(f)`, and linear responsivity `R(f)`,

`F_xx/T = F_yy/T = |R(f)|^2/S_n(f)`

and

`Tr F/T = 2|R(f)|^2/S_n(f) = 2/NEP(f)^2`

when conventional frequency-resolved NEP is valid.

For arbitrary weak waveform coordinates,

`F_ij = 4 Re integral_0^infinity q_i*(f) q_j(f)/NEP(f)^2 df`.

Response bandwidth and Fisher-information bandwidth need not coincide when noise is frequency dependent.

### WP02 — Poisson timestamps and independent timing jitter

For fractional sinusoidal modulation of an ideal Poisson event rate,

**`Tr F/T=lambda_0`**.

For optical-power quadratures this exactly matches the WP01 shot-noise result `2/NEP_shot^2`.

Independent timestamp jitter with characteristic function `Phi_J(Omega)` gives

**`Tr F/T=lambda_0 |Phi_J(Omega)|^2`.**

Gaussian jitter gives

`Tr F/T=lambda_0 exp[-Omega^2 sigma_t^2]`,

`f_F,3dB=sqrt(ln 2)/(2 pi sigma_t)`.

Independent signal and dark Poisson streams give

`Tr F/T=lambda_s^2/(lambda_s+lambda_d)`

before the jitter factor.

## Immediate work order

1. WP03 — dead time/recovery/memory and connection to the random-time spectral-resource theorem.
2. WP04 — seeded-to-empty optical sideband survival/synthesis crossover.
3. WP05 — textbook resonant-exchange interpretation of exact unitary-coupling cost.
4. WP06 — integrated falsification matrix.
5. WP07 — dedicated prior-art/significance gate before manuscript drafting.

Do not create sidequests that do not improve measurement accessibility, falsifiability, or standard-physics interpretation.

## Claim discipline

Priority remains unverified/not certified. Do not use Nobel/prize-level framing in scientific materials. Do not claim novelty for standard NEP, detectivity, matched filtering, generic Fisher sensing, Poisson-process Fisher information, shot-noise formulas, or timing-jitter characteristic-function filtering.

Paper 4 is justified only if WP03–WP06 produce nontrivial experimentally legible consequences beyond tutorial translation.

## Documentation rule

After every material derivation, failed derivation, convention correction, prior-art collision, model decision, or falsification criterion, update the practical-program note and handoff. When the frontier moves, also update root `README.md`, `AGENTS.md`, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`.
