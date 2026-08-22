# AGENTS.md

## Purpose

Durable repository handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

Research is analytical/theoretical. Numerical work is allowed for validation. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

## Current status

The default branch `main` is now the **landing/index branch**, not the active derivation branch.

Current project split:

1. **Paper 1 / Rev11** — frozen; submission metadata/compliance only.
2. **Paper 2 / Rev7** — frozen preferred science draft.
3. **Grand Challenge** — ACTIVE on `agent/temporal-information-resource-law`.

## Mandatory first action for a replacement agent

Switch to:

`agent/temporal-information-resource-law`

Then read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP15_GENERAL_DENSITY_PROOF_OF_SHARP_PI_AREA_INEQUALITY.md`
3. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`
4. `grand_challenge/notes/WP13_SECOND_QUANTIZED_SCOPE_AND_POISSON_EVENT_EMBEDDING.md`
5. `grand_challenge/notes/WP12_SHARP_CONTINUUM_QUANTUM_MODE_AREA_LAW.md`
6. `grand_challenge/notes/WP11_WP10_FACTOR_AUDIT_AND_PRIOR_ART.md`
7. `grand_challenge/notes/WP10_QUANTUM_RANDOM_TIME_MODE_BUDGET.md`
8. `docs/CURRENT_RESEARCH_STATE.md`
9. `ROADMAP.md`

Do **not** resume the old HgCdTe/Kane WP24 frontier shown in historical main-branch commits. That is not the current program.

## Current strongest result

The active theorem stack is through **WP15**.

For random temporal-distribution encoding of a fixed semibounded-energy excitation, the continuum quantum temporal-mode retention obeys

`G_Q(nu)=2 int_0^infinity q(omega)q(omega+nu)/[q(omega)+q(omega+nu)]domega`, `nu>0`,

with even extension, and

`boxed: int_0^infinity G_Q(nu)dnu <= (pi/2) omega_bar`,

hence

`boxed: int_R G_Q(nu)dnu <= pi E_bar^+/hbar`.

A flat-band guarantee gives

`boxed: E_bar^+ >= (2/pi) h B q0`.

The constant is sharp as a supremum. WP15 supplies the general-density proof using rearrangement/layer cake and a positive Mellin-convolution operator with exact norm `pi/4`.

## Critical scope boundary

WP14 proves baseline mean energy does **not** bound arbitrary parameter-dependent coherent waveform synthesis. The strongest theorem is therefore about random-time distribution encoding of fixed semibounded-energy excitations. Any broader theorem needs an explicit encoding/control/action resource.

## Immediate active gates

1. Deep priority audit for exact equivalents of WP10/WP12/WP15.
2. Determine whether a single measurement family can approach the integrated `pi` coefficient; separately optimized temporal-mode SLDs need not be compatible.
3. Strengthen the quantum-marked Poisson/event-to-field embedding.
4. Only after those gates decide whether to draft a standalone foundational manuscript.

## Documentation discipline

The user must be able to open `main` and immediately see the active branch/checkpoint.

After every project-level theorem/gate change:

- update the active `grand_challenge/notes/WP*.md`;
- update `grand_challenge/AGENTS.md`;
- update the active-branch top-level `README.md`, `AGENTS.md`, `docs/CURRENT_RESEARCH_STATE.md`, and `ROADMAP.md`;
- mirror the active branch/checkpoint into these same landing files on `main`.

Never leave the current scientific state visible only on an agent branch or in chat.