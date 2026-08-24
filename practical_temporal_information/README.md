# Practical temporal-information benchmarks

**Branch:** `agent/practical-temporal-information-benchmarks`

## Purpose

Develop a fourth, deliberately grounded paper that translates the existing temporal-information resource program into standard detector physics and explicit falsification tests. This is not another abstraction layer and does not alter the frozen theorem/proof stacks of the three mature papers.

Working title:

> **Operational temporal-information benchmarks for photodetection**

## Gate status

- WP07 prior-art/significance gate: **PASS WITH NARROWED CLAIMS**.
- WP08 final pre-manuscript gate: **PASS**.
- WP09 first hostile manuscript audit: **CONDITIONAL PASS**.

The first full REVTeX manuscript exists. Its static claim/provenance gate passed on the first CI attempt. That attempt then exposed a purely mechanical incompatibility between REVTeX `ruledtabular` and the paragraph-width falsification-table columns; a deterministic R1 transform now removes only that wrapper before compilation.

## Strengthened scientific center after WP09

The original two-level support crossover was mathematically correct but unnecessarily specialized. WP09 generalizes it to a selected carrier/sideband pair embedded in arbitrary inert spectator modes.

Take

`rho_p = a_p |c><c| + p |s><s| + sigma_p`,

with `sigma_p>=0` on the spectator subspace, `a_p>p`, `a_p->q>0`, and a local lossless converter that acts only on `|c>,|s>`.

Then

`P_s(p;r)=p+(a_p-p)sin^2(kappa r)`,

`R_lin^2=a_p p/[kappa^2(a_p-p)^2]`,

and finite-radius survival gives

`(R_lin^2/4)Tr F<=p`.

At the zero-seed boundary,

`Delta P_s(0)=4kappa^2 q`.

Hence the strengthened identity is

**`lim_(p->0+)4p/R_lin^2=4kappa^2 q=Delta P_s(0)`.**

The result is insensitive to arbitrary spectator populations and to how seed normalization is compensated outside the selected mode pair, provided the selected carrier occupation tends to `q` and spectators are inert under the calibrated converter.

The normalized two-bin model `a_p=1-p`, `sigma_p=0`, `q=1` is retained only as the simplest special case for plotting and intuition.

## Other retained results

### Memory benchmark from frozen Paper 2

For fixed mean Type-II recovery `m`, every iid recovery law shares `r=lambda exp(-lambda m)` while timestamp information is not fixed; at the common maximum deterministic recovery is uniquely information-singular. Paper 4 makes this experimentally actionable but does not republish it as a new theorem.

### Standard measurement bridge

- linear Gaussian: `Tr F/T=2/NEP(f)^2` under the locked one-sided-PSD convention;
- ideal fractional Poisson timestamps: `Tr F/T=lambda0`;
- independent jitter: factor `|Phi_J(Omega)|^2`.

### WP08 conventional-specification example

Two detectors can share DC NEP and responsivity `f_3dB` yet differ by `13/3≈4.3333` in FI at `f_c`; one remains above half its DC FI until `2.9703 f_c` because its excess noise rolls off faster than its response.

### Standard Hamiltonian benchmark

The fixed-energy resonant beam-splitter model gives

`V_min=8(gt)^2=(1/2)Tr C`,

`A_ex=hbar nu V_min`,

with unchanged total bare-energy distribution.

## Manuscript architecture

I. What conventional detector specifications do not determine.

II. Detector-language FI bridge and memory benchmark.

III. Spectral support: selected-mode seeded survival -> empty-sideband synthesis.

IV. Standard Hamiltonian implementation.

V. Integrated falsification matrix.

VI. Discussion.

## Immediate work

1. complete R1 mechanical build verification;
2. generate R2 with the WP09 generalized crossover theorem;
3. compile and render R2;
4. run a second hostile manuscript-level audit;
5. only after that, generate the four planned figures and compress for publication.

## Claim discipline

No novelty claim for generic dead-time information theory, variable/random dead time, interval characterization, paralyzable correlations, standard NEP/Fisher sensing, sideband generation/metrology, seeded/vacuum interferometry, generic boundary-QFI curvature, beam-splitter physics, or standard interferometry. Priority for the selected-mode crossover remains unverified, not certified. No experimental validation is implied without data.

## Authoritative notes

- `notes/WP01_LINEAR_GAUSSIAN_FISHER_NEP_BRIDGE.md`
- `notes/WP02_POISSON_TIMESTAMPS_AND_JITTER.md`
- `notes/WP03_DEAD_TIME_RECOVERY_INFORMATION_BENCHMARKS.md`
- `notes/WP04_OPTICAL_SIDEBAND_SURVIVAL_SYNTHESIS_CROSSOVER.md`
- `notes/WP05_RESONANT_EXCHANGE_UNITARY_COUPLING_BRIDGE.md`
- `notes/WP06_MINIMUM_PAPER_STACK_AND_FALSIFICATION_MATRIX.md`
- `notes/WP07_PRIOR_ART_AND_SIGNIFICANCE_GATE.md`
- `notes/WP08_FINAL_PREMANUSCRIPT_STACK_AND_SPEC_INCOMPLETENESS.md`
- `notes/WP09_HOSTILE_MANUSCRIPT_AUDIT_AND_SPECTATOR_INDEPENDENT_CROSSOVER.md`

## Documentation rule

Every material advance must update the corresponding note, this handoff, root `README.md`, root `AGENTS.md`, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`.
