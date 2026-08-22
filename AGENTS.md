# AGENTS.md

## Purpose

Durable project handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

Research is analytical/theoretical. Numerical work is allowed for validation. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

## Current project split

1. **Paper 1 / Rev11** — scientifically frozen and technically validated; submission metadata/compliance only.
2. **Paper 2 / Rev7** — preferred frozen science draft; locally build-verified and visually inspected.
3. **Grand Challenge** — active high-risk/high-ceiling theory program on quantum resources for temporal information transfer.

**Active scientific branch:** `agent/temporal-information-resource-law`.

**Theorem stack:** through WP15.

**Latest research checkpoint:** WP16 priority audit.

## Read first — current frontier

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP16_DEEP_PRIORITY_AUDIT_RANDOM_TIME_QFI_AND_HARDY_HILBERT_COLLISION.md`
3. `grand_challenge/notes/WP15_GENERAL_DENSITY_PROOF_OF_SHARP_PI_AREA_INEQUALITY.md`
4. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`
5. `grand_challenge/notes/WP13_SECOND_QUANTIZED_SCOPE_AND_POISSON_EVENT_EMBEDDING.md`
6. `grand_challenge/notes/WP12_SHARP_CONTINUUM_QUANTUM_MODE_AREA_LAW.md`
7. `grand_challenge/notes/WP11_WP10_FACTOR_AUDIT_AND_PRIOR_ART.md`
8. `grand_challenge/notes/WP10_QUANTUM_RANDOM_TIME_MODE_BUDGET.md`
9. `grand_challenge/notes/WP09_EXTERNAL_TIME_REFERENCE_NO_GO_AND_ASYMMETRY_BOUNDARY.md`
10. `grand_challenge/notes/WP08_ARBITRARY_MEMORY_LIFT_AND_QUANTUM_REGULARIZATION.md`
11. `paper2/AGENTS_PAPER2.md` only if frozen Paper-2 context is needed.

## Current strongest grand-challenge theorem stack

### WP10/WP11 — discrete/periodic random-time quantum mode budget

For a random temporal-distribution mode `k`, source-normalized maximal quantum retention is

`G_Q(k)=2 sum_n q_n q_{n+k}/(q_n+q_{n+k})`.

Mode sum:

`sum_{k>=1} G_Q(k) <= 2 nbar`,

`sum_{k!=0} G_Q(k) <= 4 nbar`.

The constants are sharp as suprema. The bound is detector-independent because all subsequent parameter-independent detector dynamics and measurements are downstream of encoded-state QFI.

### WP12/WP15 — sharp continuum positive-energy area law

For normalized `q(omega)>=0` with finite first moment `omega_bar`, define

`G_Q(nu)=2 int_0^infinity q(omega)q(omega+nu)/[q(omega)+q(omega+nu)] d omega`, `nu>0`,

with even extension.

WP15 proves for every finite-first-moment density:

`boxed: int_0^infinity G_Q(nu)dnu <= (pi/2) omega_bar`,

hence

`boxed: int_R G_Q(nu)dnu <= pi E_bar^+/hbar`.

Flat-band inverse law:

`boxed: E_bar^+ >= (2/pi) h B q0`.

The constant is sharp as a supremum, approached by truncated critical densities proportional to `(1+omega)^(-2)`.

### WP16 — priority correction

The WP15 operator

`L(s,t)=2st/(s+t)^3`

with exact norm

`||T||=pi/4`

is a direct specialization of classical parameterized Hardy–Hilbert integral inequalities. Setting `lambda=3`, `f(x)=xr(x)`, `g(y)=yr(y)` gives the classical best constant `B(3/2,3/2)=pi/8`; the factor `2` in `L` yields `pi/4`.

Therefore **the sharp `pi/4` operator constant, Mellin/Hilbert inequality, and Beta/Gamma evaluation are established mathematics, not novelty claims**.

The candidate novelty, if priority survives, is instead the quantum-statistical/physical synthesis: estimation of Fourier modes of a latent random time distribution, the exact source-normalized `G_Q(k)`, the `2 nbar` sum rule, continuum temporal-information interpretation, and arbitrary-detector inheritance.

No exact predecessor for that quantum random-distribution problem has yet been located. Priority remains uncertified.

### WP06-WP08 — covariant timestamp subclass

For reference-free covariant timestamp readouts:

`int_R G_timestamp(nu)dnu <= 2 E_det^+/hbar`,

or

`E_det^+ >= h B q`.

WP08 lifts this through arbitrary downstream classical detector memory and gives finite-energy quantum regularization of Paper 2's ideal Type-II infinite-frequency plateau.

## Scope/no-go boundaries

The strongest general theorem applies to **random temporal-distribution encoding of a fixed semibounded-energy excitation**.

WP14 proves baseline mean energy does **not** bound arbitrary parameter-dependent quantum waveform state engineering: infinitesimal high-frequency coherent sidebands can enter at first order while added energy is second order. A broader waveform theorem needs an explicit encoding/control/action resource.

Do not use entropy production, ordinary dynamical activity, or detector thermodynamic cost inferred from `G` as a universal scalar resource; explicit literature/counterexamples already rule out those naive formulations.

## Novelty discipline

Do not claim novelty for generic:

- SLD QFI or monotonicity;
- waveform QFI kernels;
- time-covariant POVMs;
- time-translation asymmetry;
- Hardy/Gagliardo–Nirenberg inequalities;
- Hardy–Hilbert best-constant inequalities or the WP15 `pi/4` operator norm;
- rearrangement/layer-cake/Mellin analysis;
- time-energy uncertainty relations.

Close literature includes Tsang–Wiseman–Caves, Marvian–Spekkens, Pocovnicu, Kiukas–Ruschhaupt–Werner, Hall, Yang's Hilbert-type operator literature, WAY/asymmetry, phase-diffusion/dephasing estimation, and random-unitary/noise-channel estimation.

## Immediate gates

1. **Priority Gate 1A:** search estimation of Fourier coefficients/mixing weights of `U(1)` random-unitary channels and probability measures on compact groups.
2. **Priority Gate 1B:** determine whether the harmonic-mean density inequality itself appears explicitly; its sharp operator constant is already classical.
3. Determine whether one measurement family can operationally approach the integrated `pi` coefficient; separately optimized per-mode SLDs are generally incompatible.
4. Strengthen the independent quantum-marked Poisson-to-field embedding.
5. Only then decide whether WP10–WP15 justify a standalone foundational manuscript.
6. Explore general waveform-encoding resource laws only if the extra control/action resource is explicit and noncircular.

## Frozen papers

Paper 1 Rev11 and Paper 2 Rev7 are not active theorem-development branches. Reopen only for a concrete defect, referee objection, or submission requirement.

## Mandatory documentation rule

After every material theorem, counterexample, proof repair, prior-art collision, numerical result, or strategy change:

- update/create `grand_challenge/notes/WP*.md` immediately;
- update `grand_challenge/AGENTS.md` when the theorem stack/gates change;
- update top-level `README.md`, this file, `docs/CURRENT_RESEARCH_STATE.md`, and `ROADMAP.md` when project-level status changes;
- keep `PROBLEM.md` and `grand_challenge/README.md` from becoming stale secondary entry points;
- keep `main` current enough that a user opening the repository can immediately see the active branch and checkpoint.

Do not allow the authoritative state to exist only on a hidden branch or in chat.