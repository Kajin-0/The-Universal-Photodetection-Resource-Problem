# AGENTS.md

## Purpose

Durable project handoff for The Universal Photodetection Resource Problem. The repository, not chat history, is authoritative.

## Active branch

`agent/practical-temporal-information-benchmarks`

The three mature temporal-information papers remain scientifically frozen. The active fourth program is a standard-physics/falsifiability bridge.

## Read first

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `practical_temporal_information/AGENTS.md`
3. `practical_temporal_information/notes/WP09_HOSTILE_MANUSCRIPT_AUDIT_AND_SPECTATOR_INDEPENDENT_CROSSOVER.md`
4. `practical_temporal_information/notes/WP08_FINAL_PREMANUSCRIPT_STACK_AND_SPEC_INCOMPLETENESS.md`
5. `practical_temporal_information/notes/WP07_PRIOR_ART_AND_SIGNIFICANCE_GATE.md`
6. `manuscript/practical_temporal_information/README.md`
7. `manuscript/practical_temporal_information/MANUSCRIPT_ARCHITECTURE.md`

## Paper-4 gate status

- WP07 prior-art/significance: **PASS WITH NARROWED CLAIMS**.
- WP08 pre-manuscript gate: **PASS**.
- WP09 first hostile manuscript audit: **CONDITIONAL PASS**.

The first full REVTeX draft exists and its static provenance gate passed. Initial CI exposed only a mechanical `ruledtabular` incompatibility; R1 generation removes that wrapper deterministically before compilation.

## Strengthened Paper-4 theorem after WP09

For a selected carrier/sideband pair embedded in arbitrary inert spectator modes,

`rho_p=a_p|c><c|+p|s><s|+sigma_p`,

with `a_p->q>0`, the calibrated two-mode converter gives

`R_lin^2=a_p p/[kappa^2(a_p-p)^2]`

and

`Delta P_s(0)=4kappa^2 q`.

Therefore

**`lim_(p->0+)4p/R_lin^2=Delta P_s(0)`.**

The original normalized two-level model is only the `q=1` special case. The generalized result is exact for a lossless selected-mode converter with inert spectators; it is not claimed for arbitrary lossy or parameter-dependent channels.

Targeted prior-art search found no direct collision for this exact identity/interpretation. Priority remains unverified/not certified.

## Other Paper-4 components

- Type-II memory theorem: cited result from the frozen random-time paper, not new Paper-4 theorem.
- `Tr F/T=2/NEP(f)^2`: standard linear-Gaussian bridge under explicit conventions.
- ideal Poisson/jitter relation: standard timestamp bridge.
- WP08 equal-DC-NEP/equal-response-bandwidth but unequal-FI-spectrum example: standard detector illustration.
- resonant beam-splitter cost equality: standard-physics benchmark of the frozen PRA theorem.

## Falsification hierarchy

Always distinguish detector-model/reduction failure, resource-law challenge after independently verifying theorem assumptions, and failure of a model-specific saturating equality.

## Immediate work order

1. complete R1 mechanical build verification;
2. produce R2 with the WP09 generalized crossover theorem;
3. compile and render R2;
4. hostile-audit R2 before any science freeze;
5. only then produce figures and publication-style compression.

## Claim discipline

No prize-level framing. No implied experimental validation without data. No novelty claim for generic dead-time information theory, variable/random dead time, interval characterization, paralyzable correlations, standard NEP/Fisher sensing, sideband metrology, seeded/vacuum interferometry, generic rank-boundary QFI, beam-splitter physics, or standard interferometry.

## Documentation rule

Every material result or scope change must update the dedicated note, practical handoff, root `README.md`, `AGENTS.md`, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`.
