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

### WP01 — linear Gaussian FI/NEP

`F_xx/T=F_yy/T=1/NEP(f)^2`,

`Tr F/T=2/NEP(f)^2`

under the locked peak-quadrature / one-sided-PSD convention.

### WP02 — Poisson timestamps and jitter

`Tr F/T=lambda_0`

for fractional two-quadrature modulation; optical-power form exactly matches ideal shot-noise NEP. Independent jitter gives factor `|Phi_J(Omega)|^2`.

### WP03 — dead time/recovery

At deterministic Type-II paralysis maximum, `G(0)=0` but every nonzero frequency survives; `G>=0.51697536` at `f=1/(2tau)` and `G->1/e` at high frequency.

For arbitrary finite-mean iid recovery, all distributions with mean `m` share `r=lambda exp(-lambda m)`, but `G_DC=0` at `lambda m=1` iff recovery is deterministic. Equal-mean/equal-variance/equal-saturation recovery laws can have different timestamp information.

### WP04 — optical sideband survival/synthesis

Seeded two-bin baseline:

`rho_p=(1-p)|c><c|+p|s><s|`.

With local mixing coefficient `kappa`,

`R_lin^2=p(1-p)/[kappa^2(1-2p)^2]`.

Finite-radius regime:

`(R_lin^2/4)Tr F<=p`.

Empty-sideband boundary:

`Delta P_s(0)=4kappa^2`,

`Tr F<=Delta P_s(0)`.

Exact crossover:

**`lim_(p->0+)4p/R_lin^2=Delta P_s(0)`.**

A fixed common-record frequency-bin POVM saturates the boundary value.

Ordinary weak phase modulation yields `Delta P_+=Delta P_-=1` and a fixed phase-sensitive three-mode analyzer achieves

**`Tr F=4=[sqrt(Delta P_+)+sqrt(Delta P_-)]^2`.**

This is an exact ideal standard-optics saturation example of the bilateral rank-boundary curvature law.

## Remaining work packages

### WP05 — autonomous resonant-exchange implementation bridge

Include the controller/clock explicitly. Reduce the companion theorem

`V_min=(1/2)Tr C`,

`A_ex=hbar nu V_min`

to a textbook energy-conserving beam-splitter/frequency-conversion interaction. Identify exactly what `V_impl=sum Var(K_j)` becomes in measurable/calibrated coupling parameters. Keep it separate from work, consumed RF power, peak Hamiltonian norm, controller bandwidth, and fixed-controller-spectrum optimization.

### WP06 — integrated falsification matrix

For every headline result specify measured inputs, predicted equality/inequality, nuisance assumptions, statistical test, and contradiction criterion. Select the minimum practical result stack; remove anything merely pedagogical.

### WP07 — prior-art/significance gate

Search specifically for:

- FI/NEP detector metrics and information bandwidth;
- dead-time recovery distributions with identical saturation but different information/identifiability;
- sideband-population curvature bounds on modulation FI;
- seeded-to-empty support crossovers in optical metrology;
- experimentally framed rank-boundary QFI/FI tests.

Do not draft Paper 4 until this gate determines which claims are genuinely distinct.

## Current candidate thesis

> Conventional detector figures of merit can fail to determine temporal-information transfer. Frequency-resolved response/noise and full timestamp structure provide a common falsifiable benchmark, while pre-existing versus generated optical sideband population realizes the survival/synthesis distinction in standard photonics.

## Claim discipline

No novelty claim for standard NEP/detectivity, generic Fisher sensing, Poisson/dead-time formulas, renewal spectra, electro-optic sideband generation, SU(2) conversion, or standard frequency-bin interferometry. No implied experimental validation without data. No prize-level framing.

## Documentation cadence

Update `practical_temporal_information/notes/`, `practical_temporal_information/AGENTS.md`, and all top-level landing files after every material advance.
