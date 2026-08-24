# Research Roadmap

**Updated:** 2026-08-23

**Active branch:** `agent/practical-temporal-information-benchmarks`

## Mature papers — frozen separately

1. PRX Quantum flagship — survival/synthesis conceptual law.
2. Broad random-time/timestamp spectral-information paper.
3. PRA exact unitary-coupling completion.

Do not concatenate them.

## Active Paper 4

Working title:

> **Operational benchmarks for temporal information in photodetection**

Goal: translate temporal Fisher/resource results into standard detector measurements and explicit falsification conditions.

## Completed work packages

### WP01 — analog Gaussian

`Tr F/T=2/NEP(f)^2` under the locked convention. Full weak-waveform FI is the `1/NEP(f)^2` matched-filter metric.

### WP02 — ideal timestamps

`Tr F/T=lambda_0` for fractional Poisson modulation; optical-power form exactly matches ideal shot-noise NEP. Independent jitter gives `|Phi_J|^2`.

### WP03 — detector memory

Standard saturation/low-order recovery characterization can be information-incomplete. Deterministic Type-II recovery at the count maximum is DC-information blind but retains every nonzero mode. Arbitrary finite-mean iid recovery shares the same saturation curve for fixed mean, yet only deterministic recovery is timestamp-FI singular at the common maximum.

### WP04 — optical support crossover

Seeded sideband:

`(R_lin^2/4)Tr F<=p`.

Empty-sideband boundary:

`Tr F<=Delta P_s`,

with exact limiting identity

`lim_(p->0+)4p/R_lin^2=Delta P_s`.

Ordinary ideal weak phase modulation saturates the bilateral curvature law.

### WP05 — resonant exchange implementation

Two equal-frequency bosonic modes with standard beam-splitter coupling remain inside a fixed total-excitation shell.

For baseline `|1,1>` and parameterized interaction `U=exp[-i g t(xB_x+yB_y)]`,

`V_impl=8(g t)^2`,

`Tr C=16(g t)^2`,

**`V_min=(1/2)Tr C=8(g t)^2`,**

**`A_ex=hbar nu V_min=8 hbar nu(g t)^2`.**

The total bare-energy distribution remains a delta function at `2hbar nu`.

For fixed duration,

`V_impl=(t^2/hbar^2)sum_j Var(H_j)`.

This supplies the standard Hamiltonian meaning of the abstract coupling functional while preserving the explicit non-work limitation.

## WP06 — next: minimum paper stack and falsification matrix

Do not simply carry WP01–WP05 wholesale into a manuscript. Rank them by scientific function:

- which results are central claims;
- which are bridges/background;
- which are merely examples;
- which require separate data sets;
- which can be tested with common laboratory observables.

Build one table with measured quantities, prediction, calibration assumptions, and falsification criterion for every retained headline result.

A likely minimal paper will center WP03 + WP04, use WP01/WP02 to establish the common information language, and use WP05 as a compact Hamiltonian interpretation rather than a second full theory section.

## WP07 — prior-art/significance gate

Before manuscript drafting, search specifically for the exact integrated claims and practical crossovers. Demote or remove anything already standard. If only pedagogical material remains, do not force Paper 4.

## Current candidate thesis

> Conventional detector figures of merit can fail to determine temporal-information transfer. Frequency-resolved response/noise and full timestamp structure provide a common falsifiable benchmark, while seeded versus generated spectral populations identify the survival/synthesis transition and a standard resonant exchange gives its exact minimum-coupling realization.

## Claim discipline

No novelty claim for standard NEP/detectivity, generic Fisher sensing, Poisson/dead-time formulas, renewal spectra, electro-optic sidebands, SU(2)/beam-splitter physics, or standard interferometry. No implied experimental validation without data. No prize-level framing.

## Documentation cadence

Update `practical_temporal_information/notes/`, `practical_temporal_information/AGENTS.md`, and all top-level landing files after every material advance.
