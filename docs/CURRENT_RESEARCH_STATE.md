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

`Tr F/T=2/NEP(f)^2` for peak optical-power quadratures under a one-sided PSD convention. Standard measurement bridge; no novelty claim.

### WP02 — ideal timestamp bridge

`Tr F/T=lambda_0` for fractional Poisson modulation; optical-power form exactly matches ideal shot-noise NEP. Independent timing jitter gives factor `|Phi_J(Omega)|^2`. Standard bridge; no novelty claim.

### WP03 — detector-memory benchmark from frozen Paper 2

For arbitrary finite-mean iid Type-II recovery, fixing mean recovery fixes the complete homogeneous saturation curve `r=lambda exp(-lambda m)` but not temporal information. At the common maximum, complete timestamp DC FI vanishes iff recovery is deterministic. Exact equal-mean/equal-variance/equal-saturation recovery laws have different timestamp statistics and accessible FI.

These are existing results of the frozen random-time paper. Paper 4 may translate them into an experimental characterization/falsification protocol and must cite that paper; do not republish them as new Paper-4 theorems.

### WP04 — primary candidate new support result

A seeded carrier/sideband family obeys finite-radius survival; at zero seed the sideband becomes a rank-changing kernel direction and second-order population curvature takes over. Exact crossover:

`lim_(p->0+)4p/R_lin^2=Delta P_s(0)`.

Ordinary ideal weak phase modulation saturates the bilateral boundary-curvature law under a fixed phase-sensitive analyzer.

Targeted WP07 prior-art search found no direct collision for this exact support-controlled survival-to-synthesis crossover. Priority remains unverified, not certified.

### WP05 — standard Hamiltonian implementation benchmark

A resonant two-mode beam splitter in the fixed `N_tot=2` shell gives

`V_min=8(g t)^2=(1/2)Tr C`,

`A_ex=hbar nu V_min`,

while the total bare-energy distribution remains exactly fixed. For fixed duration,

`V_impl=(t^2/hbar^2)sum_j Var(H_j)`.

The beam-splitter Hamiltonian is standard; its role is an independently calibratable benchmark for the companion implementation theorem.

### WP06 — scope/falsification gate

The minimum practical paper architecture is:

1. concise NEP/timestamp measurement bridge;
2. Paper-2 memory benchmark made experimentally actionable;
3. new WP04 support crossover;
4. compact WP05 resonant-exchange implementation benchmark;
5. integrated falsification matrix.

Falsification is stratified into detector-model/reduction failure, resource-law challenge under verified assumptions, and failure of a model-specific saturating equality.

### WP07 — prior-art/significance gate

**PASS WITH NARROWED CLAIMS.**

Established prior ingredients include dead-time information theory, variable/random dead time, interval-based detector characterization, paralyzable correlation distortion, weak-sideband Fisher metrology, seeded/vacuum interferometry, generic rank-boundary QFI curvature, and standard beam-splitter metrology. Do not claim novelty for them.

The distinct Paper-4 core is therefore narrower: WP04's support-controlled crossover plus a rigorous experimental/falsification architecture, with WP03 used as a cited practical benchmark rather than duplicated.

## Current active task — WP08

Final pre-manuscript gate:

1. derive an explicit conventional detector-misranking example showing why response bandwidth or a single sensitivity number can fail for temporal-information tasks;
2. lock assumptions, units, PSD conventions and parameterizations;
3. classify every retained statement as new Paper-4 theorem, cited upstream theorem, or standard bridge;
4. decide final manuscript architecture and figures;
5. create the manuscript workspace only if this stack remains coherent and non-duplicative.

## Claim discipline

No novelty claim for standard NEP, generic Fisher sensing, Poisson/dead-time formulas, renewal spectra, electro-optic sidebands, beam-splitter Hamiltonians, standard interferometry, or generic boundary-QFI geometry. No prize-level framing. No experimental validation may be implied without data.

Every material WP08 result must update its note and all top-level landing files.
