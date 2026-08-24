# AGENTS.md

## Purpose

Durable project handoff for The Universal Photodetection Resource Problem. The repository, not chat history, is authoritative.

## Active branch

`agent/practical-temporal-information-benchmarks`

The three mature temporal-information papers remain scientifically frozen. The active fourth program translates them into standard detector measurements and explicit falsification tests.

Read first:

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `practical_temporal_information/AGENTS.md`
3. `practical_temporal_information/notes/WP01_LINEAR_GAUSSIAN_FISHER_NEP_BRIDGE.md`
4. `practical_temporal_information/notes/WP02_POISSON_TIMESTAMPS_AND_JITTER.md`
5. `practical_temporal_information/notes/WP03_DEAD_TIME_RECOVERY_INFORMATION_BENCHMARKS.md`
6. `manuscript/THREE_PAPER_PUBLICATION_ARCHITECTURE_2026-08-23.md`

## Mature paper architecture — preserve

1. PRXQ flagship: *Two spectral-resource regimes for autonomous temporal information*.
2. Broad random-time/timestamp spectral-information paper.
3. PRA dynamical completion: *Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature*.

Do not concatenate these papers and do not copy their full proof stacks into Paper 4.

## Paper 4 mission

Working title: **Operational benchmarks for temporal information in photodetection**.

Every central result should identify measured quantities, predicted equality/inequality, nuisance assumptions, and a result that would contradict the model/theorem.

## Current frontier

WP01: linear Gaussian weak-signal detector gives

`Tr F/T=2|R(f)|^2/S_n(f)=2/NEP(f)^2`

for peak optical-power quadratures and one-sided PSD.

WP02: ideal Poisson timestamps give

`Tr F/T=lambda_0`

for fractional quadratures, exactly matching shot-noise NEP in optical-power coordinates. Independent jitter multiplies the spectrum by `|Phi_J(Omega)|^2`.

WP03: standard dead-time metrics are provably insufficient.

For deterministic paralyzable recovery at `lambda tau=1`,

`G(0)=0`

but `G(omega)>0` for every nonzero frequency. At `f=1/(2tau)`, `G>=0.51697536`; high-frequency `G->1/e`.

For arbitrary finite-mean iid Type-II recovery,

`r(lambda)=lambda exp(-lambda m)`

for every recovery distribution with mean `m`, but at `lambda m=1`

**`G_DC=0 iff T=m almost surely`.**

A simple bounded interval statistic `exp(-sD)` has zero local rate derivative iff recovery is deterministic and positive derivative for every nondegenerate finite-mean recovery law.

Exact same-mean/same-variance example at `m=10 ns`:

- Law A: `5 ns` / `15 ns`, each `1/2`;
- Law B: `2.5 ns` (`2/9`), `10 ns` (`5/9`), `17.5 ns` (`2/9`).

Both have variance `25 ns^2`, CV `0.5`, and identical saturation curve, yet at the common maximum their registered pair correlation at `7.5 ns` is `0.7274957` versus `0.3188718`. The one-bit statistic `1{D<=4 ns}` has zero FI for A and positive FI for B.

This is the current strongest practical message: **homogeneous saturation curves and low-order recovery statistics do not determine temporal-information transfer.**

## Immediate work order

1. WP04 — optical seeded-to-empty sideband survival/synthesis crossover.
2. WP05 — textbook resonant-exchange interpretation of exact unitary-coupling cost.
3. WP06 — integrated falsification matrix.
4. WP07 — dedicated prior-art/significance gate before manuscript drafting.

Do not create sidequests that do not improve measurement accessibility, falsifiability, or standard-physics interpretation.

## Claim discipline

No prize-level framing. No novelty claim for standard NEP, detectivity, Fisher sensing, Poisson/dead-time count laws, renewal spectra, pair-correlation formulas, or timing-jitter filtering. Paper 4's novelty must come from the integrated benchmark/falsification laws and any new sideband/crossover or detector-ranking results that survive WP07.

## Documentation rule

After every material derivation, failed derivation, convention correction, prior-art collision, model decision, or falsification criterion, update the practical-program note and handoff. When the frontier moves, also update root `README.md`, `AGENTS.md`, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`.
