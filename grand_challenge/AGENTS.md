# AGENTS — Temporal Information Resource Law Program

## Purpose

Durable handoff for the high-risk/high-ceiling theoretical program launched from Paper 2. This program is deliberately separate from the frozen Paper-2 manuscript.

Active branch: `agent/temporal-information-resource-law`.

## Non-negotiable scope

- Analytical/theoretical research only.
- Numerical counterexample searches are allowed.
- Do not require experiments, fabrication, procurement, or laboratory optimization as active next steps.
- Paper 2 Rev7 remains frozen unless a concrete defect is found.
- Do not assume a Nobel-scale result exists. The program is falsification-first.

## Grand question

> For a physically realizable measurement of temporal structure, what fundamental resources constrain source-to-record temporal Fisher-information transfer?

## Read first — authoritative order

1. `grand_challenge/notes/WP12_SHARP_CONTINUUM_QUANTUM_MODE_AREA_LAW.md`
2. `grand_challenge/notes/WP11_WP10_FACTOR_AUDIT_AND_PRIOR_ART.md`
3. `grand_challenge/notes/WP10_QUANTUM_RANDOM_TIME_MODE_BUDGET.md`
4. `grand_challenge/notes/WP09_EXTERNAL_TIME_REFERENCE_NO_GO_AND_ASYMMETRY_BOUNDARY.md`
5. `grand_challenge/notes/WP08_ARBITRARY_MEMORY_LIFT_AND_QUANTUM_REGULARIZATION.md`
6. `grand_challenge/notes/WP07_ENERGY_EDGE_AND_COVARIANT_POVM_PROOF_REPAIR.md`
7. `grand_challenge/notes/WP06_POSITIVE_ENERGY_TEMPORAL_FISHER_AREA_LAW.md`
8. `grand_challenge/notes/WP05_OPERATIONAL_CLOSURE_AND_LOCAL_LANDAUER_BASELINE.md`
9. `grand_challenge/notes/WP04_QUANTUM_WAVEFORM_PRIOR_ART_COLLISION.md`
10. `grand_challenge/notes/WP03_COVARIANT_TIMESTAMP_REGULARITY_AND_QFI_BOUND.md`
11. `grand_challenge/notes/WP02_QUANTUM_TIMING_BANDWIDTH_CANDIDATE.md`
12. `grand_challenge/notes/WP01_LANDSCAPE_AND_FIRST_NO_GOS.md`

## Current strongest theorem — WP10/WP12

### Periodic random-time quantum mode budget

For period `T`, `omega0=2*pi/T`, and nonnegative excitation ladder `H=hbar*omega0*N`, let a latent random event time translate a quantum excitation. Weakly modulate the uniform event-time distribution in Fourier mode `k`.

For a pure excitation with energy-sector probabilities `q_n`, the SLD QFI for either cosine or sine quadrature is

`F_Q^(k)=sum_n q_nq_{n+k}/(q_n+q_{n+k})`.

The latent source-label FI is `1/2`, so maximal source-normalized quantum retention is

`boxed: G_Q(k)=2 sum_n q_nq_{n+k}/(q_n+q_{n+k})`.

For arbitrary mixed states the same population expression is a QFI upper bound by purification.

Mode sum:

`boxed: sum_{k>=1}G_Q(k)<=2nbar`,

`boxed: sum_{k!=0}G_Q(k)<=4nbar`,

with sharp constants in the discrete periodic class.

Every parameter-independent quantum detector, arbitrary coherent memory, apparatus state/reference, joint channel, and final measurement is downstream of this encoded-state QFI, so the bound is detector-independent.

Cosine/sine SLDs are generally not jointly compatible; treat the QFIM as an upper-bound matrix, not a simultaneous-attainability claim.

### Sharp continuum limit — WP12

For a normalized continuous positive-frequency spectral density `q(w)` with finite mean

`wbar=int wq(w)dw`,

the controlled large-period limit gives

`boxed: G_Q(nu)=2 int_0^infinity q(w)q(w+nu)/[q(w)+q(w+nu)] dw`, `nu>0`,

with even extension.

The positive-side spectral area is

`A_+[q]=iint q(x)q(y)/[q(x)+q(y)] dxdy`.

A decreasing-rearrangement + layer-cake transform reduces this to the symmetric Mellin operator with kernel

`L(s,t)=2st/(s+t)^3`.

Its exact `L2` norm is `pi/4`, because the Mellin multiplier is

`lambda(xi)=|Gamma(3/2+i xi)|^2=pi(1/4+xi^2)/cosh(pi xi)`.

Therefore the sharp continuum theorem is

`boxed: int_0^infinity G_Q(nu)dnu <= (pi/2) wbar`,

and two-sided

`boxed: int_R G_Q(nu)dnu <= pi Ebar^+/hbar`.

Flat-band inverse law:

`boxed: Ebar^+ >= (2/pi) h B q0`.

The constant is sharp as a supremum, approached by truncated critical spectra `q_R(w) proportional (1+w)^(-2)` over an increasingly large range.

This is currently the strongest **measurement-independent** Planck-scale temporal-information resource law in the program.

## Comparison with covariant timestamp law — WP06/WP07

For a reference-free covariant continuous timestamp readout, the sharper measurement-class-specific theorem is

`boxed: int G_timestamp(nu)dnu <=2E_det^+/hbar`,

or `E_det^+>=hBq`.

Thus unrestricted quantum measurement can at most enlarge the spectral-area constant by factor `pi/2` in the current continuum theory:

- covariant timestamp: area coefficient `2`;
- arbitrary quantum readout: sharp QFI coefficient `pi`.

Whether the `pi` bound is operationally approachable by actual measurements over a broad continuous band remains open.

## WP08 bridge to Paper 2

A finite-energy covariant timing layer followed by arbitrary downstream classical memory obeys the same timestamp area law by Fisher-operator data processing. Therefore Paper 2's ideal deterministic Type-II `G->1/e` infinite-frequency plateau cannot persist to infinite frequency once exact latent events are physically regularized by finite-energy quantum timing. It may remain an intermediate-frequency classical regime.

## WP09 boundary

Mean energy does not bound QFI for an arbitrary deterministic global time shift. A sparse high-energy coherent tail gives divergent shift QFI at fixed mean energy if a phase reference is available.

This does **not** defeat WP10/WP12 because their parameter is the Fourier content of a random event-time distribution. Baseline randomization twirls absolute phase; the encoded-state QFI itself has the finite mode budget, and an external reference cannot increase it.

## Major prior-art boundaries

Do not claim novelty for:

- SLD QFI/harmonic-mean denominators;
- Fisher/QFI data processing;
- U(1) modes of asymmetry or their preservation;
- generic waveform QFI kernels;
- covariant time POVMs;
- time-translation asymmetry as a resource;
- rearrangement theory, layer cake, Mellin/Carleman operator methods;
- sharp Hardy/Gagliardo--Nirenberg inequalities;
- generic time-energy uncertainty relations.

Close sources include Marvian--Spekkens (PRA 90, 062110, 2014), Tsang--Wiseman--Caves (PRL 106, 090401, 2011), Pocovnicu (Analysis & PDE 4, 379--404, 2011), Kiukas--Ruschhaupt--Werner arrival-time work, Hall (Entropy 24, 1679, 2022), and the WAY/asymmetry literature.

Targeted searches have not yet found the exact random-time Fisher-mode formula, the `2nbar` sum law, or the sharp continuum area law `int G_Q<=pi E/hbar`. Priority is not certified.

## Immediate hostile gates

1. Search analysis literature for an existing sharp inequality equivalent to
   `iint q(x)q(y)/(q(x)+q(y)) dxdy <= (pi/2) int xq(x)dx`.
2. Search quantum group-distribution / phase-noise estimation literature for the exact continuum QFI functional.
3. Extend the periodic-to-continuum proof from continuous compact support to broad finite-first-moment densities.
4. Map the random-time quantum excitation model to a **genuine second-quantized bosonic optical field**; determine whether overlap/indistinguishability/multiphoton coherence modifies the constant.
5. Determine whether entangled/multiphoton inputs can violate the single-excitation mean-energy coefficient or whether a total-energy version survives.
6. Study operational attainability of the `pi` continuum constant and the factor-`pi/2` gap to covariant timestamps.
7. Only after these gates decide whether WP10--WP12 justify a standalone manuscript.

## Documentation rule

After every material theorem, counterexample, proof repair, prior-art collision, numerical result, or strategy change:

1. update/create `grand_challenge/notes/WP*.md` immediately;
2. update this file when the active theorem/gates change;
3. do not rely on chat history as the only record.
