# Current Research State

**Last synchronized:** 2026-08-23

**Active branch:** `agent/practical-temporal-information-benchmarks`

## Frozen upstream layers

The three mature temporal-information papers remain scientifically frozen in their theorem/proof layers. WP31 is superseded; WP32 remains canonical and WP33 remains PASS under stated assumptions.

## Active Paper 4 — practical/falsifiability bridge

Working title:

> **Operational benchmarks for temporal information in photodetection**

Purpose: translate temporal Fisher/resource results into ordinary detector observables and explicit falsification tests.

## Completed practical results

### WP01 — analog Gaussian detector

For peak optical-power quadratures and one-sided output PSD,

`Tr F/T=2|R(f)|^2/S_n(f)=2/NEP(f)^2`.

### WP02 — ideal event timestamps

For fractional Poisson modulation,

`Tr F/T=lambda_0`.

The optical-power form exactly equals ideal shot-noise NEP. Independent timing jitter gives factor `|Phi_J(Omega)|^2`.

### WP03 — dead time/recovery information incompleteness

Deterministic Type-II recovery at `lambda tau=1` is complete-record DC-information blind while every nonzero temporal mode survives. For arbitrary finite-mean iid recovery with mean `m`, all distributions share `r=lambda exp(-lambda m)`, yet `G_DC=0` at the common maximum iff recovery is deterministic. Exact equal-mean/equal-variance/equal-saturation recovery laws have different timestamp information.

### WP04 — optical survival-to-synthesis crossover

Seeded two-bin model:

`R_lin^2=p(1-p)/[kappa^2(1-2p)^2]`,

`(R_lin^2/4)Tr F<=p`.

At the empty-sideband boundary:

`Delta P_s=4kappa^2`,

`Tr F<=Delta P_s`,

with

`lim_(p->0+)4p/R_lin^2=Delta P_s`.

Ordinary ideal weak phase modulation gives `Delta P_+=Delta P_-=1` and a fixed phase-sensitive measurement attaining `Tr F=4`, saturating the bilateral curvature law.

### WP05 — standard resonant-exchange implementation

Use two resonant modes

`H_0=hbar nu(N_C+N_S)`

and the textbook beam-splitter exchange in the fixed `N_tot=2` shell

`|2,0>, |1,1>, |0,2>`.

For `U=exp[-i g t(xB_x+yB_y)]` with baseline `|1,1>`:

`Var(K_x)=Var(K_y)=4(g t)^2`,

**`V_impl=8(g t)^2`.**

Measured endpoint curvatures are

`Delta P_L=Delta P_U=8(g t)^2`,

so

**`Tr C=16(g t)^2`,**

**`V_min=(1/2)Tr C=8(g t)^2`.**

The exact autonomous spectral action is

**`A_ex=hbar nu V_min=8 hbar nu(g t)^2`.**

Because the beam-splitter generators commute with `H_0`, the total bare-energy distribution remains a delta function at `2hbar nu` for the entire family.

For a fixed-duration physical Hamiltonian family,

**`V_impl=(t^2/hbar^2)sum_j Var(H_j)`.**

This is a generator-variance/coupling-strength quantity. It is not work, consumed RF energy, average interaction energy, operator norm, peak coupling, controller bandwidth, or fixed-controller-spectrum optimum.

Practical test: independently calibrate `g t` and independently measure endpoint-population Hessians, then compare

`8(g t)^2=(1/2)[Delta P_L+Delta P_U]`.

## Current significance assessment

The likely central Paper-4 content is now:

1. WP03 — conventional detector saturation/low-order recovery summaries can provably fail to determine temporal-information transfer;
2. WP04 — the survival/synthesis transition has an exact measurable optical-sideband realization;
3. WP05 — the resulting rank-changing curvature has a standard fixed-energy Hamiltonian implementation whose exact minimum coupling is independently calibratable.

WP01/WP02 are likely supporting common-language results rather than headline novelty.

## Immediate next work

1. WP06 — integrated falsification matrix, scientific-value ranking, and minimum practical paper stack.
2. WP07 — dedicated prior-art/significance gate before manuscript drafting.

## Claim discipline

No novelty claim for standard NEP, generic Fisher sensing, Poisson/dead-time formulas, renewal spectra, electro-optic sidebands, beam-splitter Hamiltonians, bosonic exchange matrix elements, or standard interferometry. No prize-level framing. No experimental validation may be implied without data.

Every material Paper-4 advance must update the practical notes and all top-level landing files so a future agent can continue without chat history.
