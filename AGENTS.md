# AGENTS.md

## Purpose

Durable project handoff for The Universal Photodetection Resource Problem. The repository, not chat history, is authoritative.

## Active branch and current program

**Active branch:** `agent/practical-temporal-information-benchmarks`

The three mature temporal-information papers remain scientifically frozen in their theorem/proof layers. A separate fourth program is now active to connect them to standard detector physics and explicit falsification tests.

Read first:

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `practical_temporal_information/AGENTS.md`
3. `practical_temporal_information/README.md`
4. `practical_temporal_information/notes/WP01_LINEAR_GAUSSIAN_FISHER_NEP_BRIDGE.md`
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

The fourth paper must translate theory into ordinary observables such as

- small-signal responsivity;
- output noise PSD;
- NEP/detectivity;
- response and information bandwidth;
- raw timestamps;
- timing jitter;
- dead time/recovery/memory;
- optical carrier/sideband populations;
- calibrated interaction/coupling parameters where the PRA theorem is invoked.

Every central statement should identify what is measured and what observation would contradict it.

## Current frontier — WP01 complete

With peak optical-power quadratures `x,y`, one-sided output PSD `S_n(f)`, and linear responsivity `R(f)`, the stationary Gaussian model gives

`F_xx/T = F_yy/T = |R(f)|^2/S_n(f)`

and

`Tr F/T = 2|R(f)|^2/S_n(f)`.

When conventional frequency-resolved NEP is valid,

`NEP(f)=sqrt(S_n(f))/|R(f)|`,

so

`F_xx/T=1/NEP(f)^2`,

`Tr F/T=2/NEP(f)^2`.

For arbitrary weak waveform coordinates `q_i`,

`F_ij = 4 Re integral_0^infinity q_i*(f) q_j(f)/NEP(f)^2 df`.

This provides the first exact detector-language bridge. It also shows that responsivity 3-dB bandwidth is not generally the same as Fisher-information bandwidth when noise is frequency dependent.

No novelty claim is made for NEP or generic Fisher sensing. The possible new contribution lies in the integrated temporal-information benchmark/falsification framework and any new crossover/ranking laws that survive prior-art review.

## Immediate work order

1. WP02 — ideal Poisson timestamps and independent timing jitter, with exact Fisher prefactors and finite-time assumptions.
2. WP03 — dead time/recovery/memory and connection to the existing random-time theorem.
3. WP04 — seeded-to-empty sideband survival/synthesis crossover.
4. WP05 — textbook resonant-exchange interpretation of the exact unitary-coupling cost.
5. WP06 — integrated falsification matrix.
6. WP07 — dedicated prior-art/significance gate before manuscript drafting.

Do not create sidequests that do not improve measurement accessibility, falsifiability, or standard-physics interpretation.

## Claim discipline

Priority remains unverified/not certified. Do not use Nobel/prize-level framing in scientific materials. Do not claim a proposed Fisher-equivalent input-noise metric is novel until a dedicated search establishes its relationship to prior information-equivalent noise/sensitivity metrics.

## Documentation rule

After every material derivation, failed derivation, convention correction, prior-art collision, model decision, or falsification criterion, update the practical-program note and handoff. When the frontier moves, also update root `README.md`, `AGENTS.md`, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`.
