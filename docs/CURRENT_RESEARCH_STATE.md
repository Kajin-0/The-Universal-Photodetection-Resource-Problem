# Current Research State

**Last synchronized:** 2026-08-23

**Active branch:** `agent/practical-temporal-information-benchmarks`

## Frozen upstream scientific layers

The three mature temporal-information papers remain scientifically frozen in their theorem/proof layers. WP31 is superseded; WP32 remains canonical and WP33 remains PASS under stated assumptions.

## Active Paper 4 — practical/falsifiability bridge

Working title:

> **Operational temporal-information benchmarks for photodetection**

Provisional journal target: **Physical Review Applied**, kept provisional so journal formatting cannot drive theorem changes.

## Research-gate status

- WP01–WP06: completed practical theorem/benchmark development and scope control.
- WP07 prior-art/significance gate: **PASS WITH NARROWED CLAIMS**.
- WP08 final pre-manuscript gate: **PASS**.
- WP09 first hostile manuscript audit: **CONDITIONAL PASS** with one substantive strengthening required before scientific freeze.

## Strengthened primary candidate theorem

WP09 embeds the selected carrier/sideband pair in arbitrary inert spectator modes:

`rho_p=a_p|c><c|+p|s><s|+sigma_p`,

where `sigma_p>=0`, `a_p>p`, `a_p->q>0`, and the calibrated local converter acts only on `|c>,|s>`.

Then

`P_s(p;r)=p+(a_p-p)sin^2(kappa r)`,

`R_lin^2=a_p p/[kappa^2(a_p-p)^2]`.

The frozen flagship finite-radius theorem gives

`(R_lin^2/4)Tr F<=p`.

At the zero-seed boundary,

`Delta P_s(0)=4kappa^2 q`.

Hence

**`lim_(p->0+)4p/R_lin^2=4kappa^2 q=Delta P_s(0)`.**

This is independent of arbitrary spectator populations and of the detailed normalization-compensation path, provided `a_p->q` and spectators remain inert under the converter. The previous normalized two-bin result is the `q=1` special case.

The coefficient was rechecked against the frozen PRXQ proof and is correct.

## Other retained content

### Frozen Paper-2 practical benchmark

For arbitrary finite-mean iid Type-II recovery, fixing mean recovery fixes the complete homogeneous saturation curve `r=lambda exp(-lambda m)` but not temporal information. At the common maximum, complete timestamp DC FI vanishes iff recovery is deterministic. Paper 4 operationalizes this but does not claim it as a new theorem.

### Standard detector bridge

`Tr F/T=2/NEP(f)^2` for peak optical-power quadratures under the locked one-sided-PSD convention.

Ideal fractional Poisson timestamps give `Tr F/T=lambda0`; independent timing jitter gives factor `|Phi_J(Omega)|^2`.

WP08's explicit colored-noise model shows equal DC NEP and equal response bandwidth can coexist with a `13/3≈4.3333` FI ratio at the nominal bandwidth.

### Standard Hamiltonian benchmark

The fixed-energy resonant beam-splitter model gives

`V_min=8(gt)^2=(1/2)Tr C`,

`A_ex=hbar nu V_min`,

while the total bare-energy distribution remains fixed.

## Manuscript / CI state

Workspace:

`manuscript/practical_temporal_information/`

First full REVTeX draft created.

Static integrity gate checks theorem provenance, bibliography keys, disclosure/data sections, absence of obvious overclaiming, and the single-new-theorem structure.

Initial PR-triggered CI run `32679522491`:

- static integrity gate — PASS;
- compile — FAIL at the falsification table because REVTeX `ruledtabular` is incompatible with the chosen paragraph-width `p{...}` columns;
- no scientific/static gate failed.

A deterministic R1 transform `apply_r1_compile_fix.py` now removes only that wrapper. R1 re-verification is active.

## Active work

1. finish R1 mechanical build verification;
2. generate scientific R2 with the WP09 spectator-independent crossover;
3. compile and visually inspect R2;
4. run a second hostile manuscript-level audit;
5. only after that, produce figures and publication-style compression.

## Claim discipline

No novelty claim for standard NEP, generic Fisher sensing, Poisson/dead-time formulas, renewal spectra, variable/random dead time, interval characterization, electro-optic sidebands, seeded/vacuum interferometry, beam-splitter Hamiltonians, standard interferometry, or generic boundary-QFI geometry. Priority for the support-seed crossover remains unverified/not certified. No prize-level framing and no implied experimental validation without data.

Every material manuscript advance must update its handoff and all top-level landing files.
