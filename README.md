# The Universal Photodetection Resource Problem

**Status synchronized:** 2026-08-23

The repository is authoritative; chat history is not.

## Mature papers — preserve separately

1. PRX Quantum flagship — *Two spectral-resource regimes for autonomous temporal information*.
2. Broad random-time/timestamp spectral-information paper.
3. PRA dynamical completion — *Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature*.

The active fourth program is `agent/practical-temporal-information-benchmarks`.

Working title:

> **Operational temporal-information benchmarks for photodetection**

## Paper-4 gate status

- WP07 prior-art/significance: **PASS WITH NARROWED CLAIMS**.
- WP08 final pre-manuscript stack: **PASS**.
- WP09 first hostile manuscript audit: **CONDITIONAL PASS** pending integration of a generalized crossover theorem.

The first full REVTeX draft exists. Its first CI run passed the scientific/static gate and failed only on a REVTeX table-environment incompatibility. A deterministic R1 transform now removes only the incompatible `ruledtabular` wrapper before compilation.

## Strengthened candidate new Paper-4 theorem

WP09 shows that the support crossover is not restricted to a normalized two-level state.

For

`rho_p=a_p|c><c|+p|s><s|+sigma_p`,

with arbitrary positive spectator sector `sigma_p`, selected carrier population `a_p->q>0`, and a calibrated local converter acting only on the carrier/sideband pair,

`P_s=p+(a_p-p)sin^2(kappa r)`,

`R_lin^2=a_p p/[kappa^2(a_p-p)^2]`.

The finite-radius law gives

`(R_lin^2/4)Tr F<=p`.

At zero seed,

`Delta P_s(0)=4kappa^2 q`.

Therefore

**`lim_(p->0+)4p/R_lin^2=4kappa^2 q=Delta P_s(0)`.**

Thus arbitrary inert spectator populations do not change the selected-mode survival-to-synthesis crossover. The previous `q=1` two-bin model is only the simplest special case.

No direct collision for this exact support-controlled identity/interpretation was found in the targeted WP07 search. Priority remains unverified, not certified.

## Practical benchmark imported from frozen Paper 2

For generalized iid Type-II recovery, fixing mean recovery fixes the complete homogeneous saturation curve `r=lambda exp(-lambda m)` but not temporal information. At the common maximum, timestamp DC FI vanishes iff recovery is deterministic; explicit matched-mean/matched-variance laws have different accessible timestamp information.

These are frozen Paper-2 results. Paper 4 operationalizes them but must not present them as new theorems.

## Conventional detector bridge

For peak optical-power quadratures under the locked one-sided-PSD convention,

`Tr F/T=2/NEP(f)^2`.

Ideal fractional Poisson timestamps give `Tr F/T=lambda0`; independent jitter multiplies the spectrum by `|Phi_J(Omega)|^2`.

WP08 gives an explicit example in which equal DC NEP and equal responsivity bandwidth coexist with a `13/3≈4.3333` FI ratio at the nominal bandwidth.

## Compact Hamiltonian benchmark

A resonant two-mode beam splitter in the fixed `N_tot=2` shell gives

`V_min=8(gt)^2=(1/2)Tr C`,

`A_ex=hbar nu V_min`,

with the total bare-energy distribution exactly fixed.

## Falsification discipline

Paper 4 distinguishes:

1. detector-model/reduction failure;
2. resource-law violation only after all theorem hypotheses are independently verified;
3. failure of a model-specific saturating equality.

## Current work order

1. finish the mechanical R1 build verification;
2. generate scientific R2 with the WP09 spectator-independent crossover theorem;
3. compile/render R2;
4. run a second hostile manuscript-level audit;
5. only then produce figures and publication-style compression.

## Claim discipline

No prize-level framing. No novelty claim for standard NEP, generic Fisher sensing, Poisson/dead-time formulas, random/variable dead time, inter-arrival characterization, paralyzable correlations, sideband generation/metrology, seeded/vacuum interferometry, generic boundary-QFI geometry, beam-splitter physics, or standard interferometry.

## Frozen publication packages

PRXQ R4: run `32674844366` PASS; artifact `9502376602`.

PRA R1: run `32673160217` PASS; artifact `9501942180`.
