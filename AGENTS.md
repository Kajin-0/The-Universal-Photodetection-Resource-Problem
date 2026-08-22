# AGENTS.md

## Purpose

Durable repository handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

Research is analytical/theoretical. Numerical work is allowed for validation. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

## Current status

The default branch `main` is the **landing/index branch**, not the active derivation branch.

Current project split:

1. **Paper 1 / Rev11** — frozen; submission metadata/compliance only.
2. **Paper 2 / Rev7** — frozen preferred science draft.
3. **Grand Challenge** — ACTIVE on `agent/temporal-information-resource-law`.

The Grand Challenge **theorem stack is through WP15**. The **latest checkpoint is WP16**, a deep priority audit.

## Mandatory first action for a replacement agent

Switch to:

`agent/temporal-information-resource-law`

Then read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP16_DEEP_PRIORITY_AUDIT_RANDOM_TIME_QFI_AND_HARDY_HILBERT_COLLISION.md`
3. `grand_challenge/notes/WP15_GENERAL_DENSITY_PROOF_OF_SHARP_PI_AREA_INEQUALITY.md`
4. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`
5. `grand_challenge/notes/WP13_SECOND_QUANTIZED_SCOPE_AND_POISSON_EVENT_EMBEDDING.md`
6. `grand_challenge/notes/WP12_SHARP_CONTINUUM_QUANTUM_MODE_AREA_LAW.md`
7. `grand_challenge/notes/WP11_WP10_FACTOR_AUDIT_AND_PRIOR_ART.md`
8. `grand_challenge/notes/WP10_QUANTUM_RANDOM_TIME_MODE_BUDGET.md`
9. `docs/CURRENT_RESEARCH_STATE.md`
10. `ROADMAP.md`

Do **not** resume the old HgCdTe/Kane WP24 frontier shown in historical main-branch commits. That is not the current program.

## Current strongest result

For random temporal-distribution encoding of a fixed semibounded-energy excitation,

`G_Q(nu)=2 int_0^infinity q(omega)q(omega+nu)/[q(omega)+q(omega+nu)]domega`, `nu>0`,

with even extension, and

`boxed: int_0^infinity G_Q(nu)dnu <= (pi/2) omega_bar`,

hence

`boxed: int_R G_Q(nu)dnu <= pi E_bar^+/hbar`.

A flat-band guarantee gives

`boxed: E_bar^+ >= (2/pi) h B q0`.

The coefficient is sharp as a supremum.

## WP16 priority correction

The WP15 operator norm

`||T||=pi/4`, for `L(s,t)=2st/(s+t)^3`,

is a direct specialization of established parameterized Hardy–Hilbert integral inequalities. With `lambda=3`, `f(x)=xr(x)`, `g(y)=yr(y)`, the classical best constant is `B(3/2,3/2)=pi/8`; the kernel factor `2` gives `pi/4`.

Therefore **do not claim mathematical novelty for the sharp operator constant, Mellin/Hilbert inequality, or Beta/Gamma evaluation**.

The remaining priority question is quantum-statistical: targeted searches have not yet found an exact predecessor for

`G_Q(k)=2 sum_n q_n q_{n+k}/(q_n+q_{n+k})`

as Fisher retention of the `k`th Fourier coefficient of a latent random `U(1)` translation distribution, nor the sum rule

`sum_{k>=1}G_Q(k)<=2 nbar`.

Priority remains uncertified.

## Critical scope boundary

WP14 proves baseline mean energy does **not** bound arbitrary parameter-dependent coherent waveform synthesis. The strongest theorem is therefore about random-time distribution encoding of fixed semibounded-energy excitations. Any broader theorem needs an explicit encoding/control/action resource.

## Immediate active gates

1. Search estimation of Fourier coefficients/mixing weights of `U(1)` random-unitary channels and probability measures on compact groups.
2. Determine whether the harmonic-mean density inequality itself has appeared explicitly; its sharp operator constant is already classical.
3. Determine whether a single measurement family can approach the integrated `pi` coefficient; separately optimized temporal-mode SLDs need not be compatible.
4. Strengthen the quantum-marked Poisson/event-to-field embedding.
5. Only after those gates decide whether to draft a standalone foundational manuscript.

## Documentation discipline

The user must be able to open `main` and immediately see the active branch/checkpoint.

After every project-level theorem/gate change:

- update the active `grand_challenge/notes/WP*.md`;
- update `grand_challenge/AGENTS.md`;
- update the active-branch top-level `README.md`, `AGENTS.md`, `docs/CURRENT_RESEARCH_STATE.md`, and `ROADMAP.md`;
- keep `PROBLEM.md` and `grand_challenge/README.md` from becoming stale secondary entry points;
- mirror the active branch/checkpoint into these landing files on `main`.

Never leave the current scientific state visible only on an agent branch or in chat.