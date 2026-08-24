# Current Research State

**Last synchronized:** 2026-08-23

**Active branch:** `agent/practical-temporal-information-benchmarks`

## Frozen upstream scientific layers

- Paper 1 Rev11;
- Paper 2 Rev7;
- random-time spectral-resource paper;
- autonomous temporal-information R3 theorem/proof baseline;
- PRX Quantum R4 publication-layer bridge;
- D2/WP32 unitary-coupling theorem/proof baseline;
- reviewer-repaired PRA R1 package.

WP31 remains superseded. WP32 is canonical; WP33 hostile audit remains PASS under stated assumptions.

## New active frontier — practical/falsifiability Paper 4

Working title:

> **Operational benchmarks for temporal information in photodetection**

Objective: translate temporal Fisher/resource statements into standard detector observables and make falsifiability explicit.

Workspace:

- `practical_temporal_information/README.md`;
- `practical_temporal_information/AGENTS.md`;
- `practical_temporal_information/notes/`.

## WP01 — linear Gaussian detector bridge

For peak optical-power quadratures `x,y`, linear small-signal responsivity `R(f)`, and one-sided additive stationary Gaussian output-noise PSD `S_n(f)`,

`F_xx/T = F_yy/T = |R(f)|^2/S_n(f)`,

`Tr F/T = 2|R(f)|^2/S_n(f)`.

When conventional frequency-resolved NEP is valid,

`NEP(f)=sqrt(S_n(f))/|R(f)|`,

so

`F_xx/T = 1/NEP(f)^2`,

`Tr F/T = 2/NEP(f)^2`.

For arbitrary weak waveform coordinates,

`F_ij = 4 Re integral_0^infinity q_i*(f) q_j(f)/NEP(f)^2 df`.

Thus inverse-square NEP is exactly the frequency weighting of the local input-waveform Fisher metric in the linear stationary Gaussian regime. Response bandwidth and Fisher-information bandwidth need not coincide when noise is frequency dependent.

Authoritative note: `practical_temporal_information/notes/WP01_LINEAR_GAUSSIAN_FISHER_NEP_BRIDGE.md`.

## WP02 — ideal Poisson timestamps and independent timing jitter

For

`lambda(t)=lambda_0[1+x cos(Omega t)+y sin(Omega t)]`

with fractional peak quadratures, the ideal inhomogeneous-Poisson model gives

**`Tr F/T=lambda_0`**

exactly for the continuously illuminated finite-window model. For long/integer-period records,

`F_xx/T=F_yy/T=lambda_0/2`, `F_xy/T -> 0`.

For optical-power quadratures,

`Tr F_P/T=eta/(hbar omega_opt P_0)`.

This exactly matches the WP01 shot-noise formula `2/NEP_shot^2` for an ideal unity-gain photodiode using one-sided `S_I=2qI_0`.

Independent timestamp jitter with characteristic function `Phi_J(Omega)` gives

**`Tr F_jitter/T=lambda_0 |Phi_J(Omega)|^2`.**

For Gaussian jitter standard deviation `sigma_t`,

`Tr F/T=lambda_0 exp[-Omega^2 sigma_t^2]`,

`f_F,3dB=sqrt(ln 2)/(2 pi sigma_t)`.

Independent unmodulated dark counts with signal rate `lambda_s` and dark rate `lambda_d` give

`Tr F/T=lambda_s^2/(lambda_s+lambda_d)`

before the jitter factor.

Authoritative note: `practical_temporal_information/notes/WP02_POISSON_TIMESTAMPS_AND_JITTER.md`.

## Scientific significance at this stage

WP01–WP02 establish a clean common language between ordinary analog photodetector characterization and raw event-timestamp estimation, but they are not by themselves claimed as novel enough for Paper 4.

The publication-level test now shifts to WP03–WP04:

- can full timestamp information distinguish detector recovery laws that conventional mean count-rate curves cannot distinguish?
- can the survival/synthesis transition be made experimentally visible as a seeded-to-empty optical-sideband crossover with a sharp measurable inequality?

If those fail to produce nontrivial new consequences, do not force a fourth paper.

## Prior-art / claim boundary

No novelty claim for standard NEP, detectivity, matched filtering, generic Fisher information in sensing, Poisson-process Fisher information, shot-noise formulas, or independent timing-jitter characteristic-function attenuation.

A 2025 Nature Photonics consensus statement supports the use of measured frequency-dependent responsivity/noise PSD/NEP and warns against inappropriate white-noise normalization under colored noise. Neighboring optical-sensing work already combines Fisher precision with detector NEP. The new work must therefore earn novelty through integration, memory-sensitive benchmarks, detector ranking, survival/synthesis crossover, or falsification structure.

## Immediate next work

1. WP03 — derive practical dead-time/recovery/memory benchmarks and connect them to the existing random-time spectral-resource theorem.
2. WP04 — construct optical seeded-to-empty sideband survival/synthesis crossover.
3. WP05 — standard resonant-exchange interpretation of the unitary-coupling theorem.
4. WP06 — integrated falsification matrix.
5. WP07 — dedicated prior-art/significance gate before manuscript drafting.

## Publication/claim discipline

The three mature papers remain independent. Paper 4 is not an omnibus synthesis paper and should not duplicate their proof stacks.

Priority remains unverified/not certified. Do not use Nobel/prize-level framing. Do not claim a generalized information-equivalent detector metric is new until dedicated prior-art review.

Every material Paper-4 advance must update the practical notes and top-level landing files so a future agent can continue without chat history.
