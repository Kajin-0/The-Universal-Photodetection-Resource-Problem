# Current Research State

**Last synchronized:** 2026-08-23

**Active branch:** `agent/practical-temporal-information-benchmarks`

## Frozen upstream scientific layers

The three mature temporal-information papers remain scientifically frozen in their theorem/proof layers. WP31 is superseded; WP32 remains canonical and WP33 remains PASS under stated assumptions.

## Active Paper 4 — practical/falsifiability bridge

Working title:

> **Operational benchmarks for temporal information in photodetection**

## Completed work

### WP01 — analog Gaussian bridge

`Tr F/T=2/NEP(f)^2` for peak optical-power quadratures under a one-sided PSD convention.

### WP02 — ideal timestamp bridge

`Tr F/T=lambda_0` for fractional Poisson modulation; optical-power form exactly matches ideal shot-noise NEP. Independent timing jitter gives factor `|Phi_J(Omega)|^2`.

### WP03 — detector-memory result

For arbitrary finite-mean iid Type-II recovery, fixing mean recovery fixes the complete homogeneous saturation curve `r=lambda exp(-lambda m)` but not temporal information. At the common maximum, complete timestamp DC FI vanishes iff recovery is deterministic. Exact equal-mean/equal-variance/equal-saturation recovery laws have different timestamp statistics and accessible FI.

### WP04 — optical support result

A seeded carrier/sideband family obeys finite-radius survival; at zero seed the sideband becomes a rank-changing kernel direction and second-order population curvature takes over. Exact crossover:

`lim_(p->0+)4p/R_lin^2=Delta P_s(0)`.

Ordinary ideal weak phase modulation saturates the bilateral boundary-curvature law under a fixed phase-sensitive analyzer.

### WP05 — standard Hamiltonian implementation

A resonant two-mode beam splitter in the fixed `N_tot=2` shell gives

`V_min=8(g t)^2=(1/2)Tr C`,

`A_ex=hbar nu V_min`,

while the total bare-energy distribution remains exactly fixed. For fixed duration,

`V_impl=(t^2/hbar^2)sum_j Var(H_j)`.

### WP06 — scope/falsification gate

The minimum practical paper architecture is now fixed provisionally:

1. concise NEP/timestamp measurement bridge;
2. headline WP03 memory result;
3. headline WP04 support crossover;
4. compact WP05 resonant-exchange completion;
5. integrated falsification matrix.

Falsification is explicitly stratified into detector-model/reduction failure, resource-law challenge under verified assumptions, and failure of a model-specific saturating equality.

Main-text target: roughly 10–14 journal pages before references, maximum four figures.

## Current active task — WP07

No manuscript drafting yet.

Run a dedicated adversarial prior-art/significance gate around:

1. same full Type-II saturation + matched recovery moments not determining temporal FI / accessible timestamp statistics;
2. the exact seeded-to-empty sideband crossover `lim 4p/R_lin^2=Delta P_s` and boundary FI-curvature saturation;
3. the integrated practical falsification framework linking standard detector records to survival/synthesis/coupling.

Search adjacent work on detector FI/NEP metrics, dead-time identifiability, rank-boundary optical metrology, sideband-population curvature, boundary QFI experiments, and beam-splitter generator variance.

If the distinct core does not survive, do not force a fourth paper.

## Claim discipline

No novelty claim for standard NEP, generic Fisher sensing, Poisson/dead-time formulas, renewal spectra, electro-optic sidebands, beam-splitter Hamiltonians, or standard interferometry. No prize-level framing. No experimental validation may be implied without data.

Every material WP07 finding must update the WP07 note and all top-level landing files.
