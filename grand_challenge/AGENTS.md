# AGENTS — Temporal Information Resource Law Program

**Last synchronized: 2026-08-21**

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

1. `grand_challenge/notes/WP16_DEEP_PRIORITY_AUDIT_RANDOM_TIME_QFI_AND_HARDY_HILBERT_COLLISION.md`
2. `grand_challenge/notes/WP15_GENERAL_DENSITY_PROOF_OF_SHARP_PI_AREA_INEQUALITY.md`
3. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`
4. `grand_challenge/notes/WP13_SECOND_QUANTIZED_SCOPE_AND_POISSON_EVENT_EMBEDDING.md`
5. `grand_challenge/notes/WP12_SHARP_CONTINUUM_QUANTUM_MODE_AREA_LAW.md`
6. `grand_challenge/notes/WP11_WP10_FACTOR_AUDIT_AND_PRIOR_ART.md`
7. `grand_challenge/notes/WP10_QUANTUM_RANDOM_TIME_MODE_BUDGET.md`
8. `grand_challenge/notes/WP09_EXTERNAL_TIME_REFERENCE_NO_GO_AND_ASYMMETRY_BOUNDARY.md`
9. `grand_challenge/notes/WP08_ARBITRARY_MEMORY_LIFT_AND_QUANTUM_REGULARIZATION.md`
10. `grand_challenge/notes/WP07_ENERGY_EDGE_AND_COVARIANT_POVM_PROOF_REPAIR.md`
11. `grand_challenge/notes/WP06_POSITIVE_ENERGY_TEMPORAL_FISHER_AREA_LAW.md`
12. `grand_challenge/notes/WP05_OPERATIONAL_CLOSURE_AND_LOCAL_LANDAUER_BASELINE.md`
13. `grand_challenge/notes/WP04_QUANTUM_WAVEFORM_PRIOR_ART_COLLISION.md`
14. `grand_challenge/notes/WP03_COVARIANT_TIMESTAMP_REGULARITY_AND_QFI_BOUND.md`
15. `grand_challenge/notes/WP02_QUANTUM_TIMING_BANDWIDTH_CANDIDATE.md`
16. `grand_challenge/notes/WP01_LANDSCAPE_AND_FIRST_NO_GOS.md`

## Current checkpoint

The **theorem stack remains through WP15**. WP16 is a priority/positioning audit, not a new theorem.

### Periodic random-time quantum mode budget — WP10/WP11

For period `T`, `omega0=2*pi/T`, nonnegative total-energy sectors `H=hbar*omega0*N`, and a latent event-time distribution weakly modulated in temporal Fourier mode `k`, a pure excitation with sector probabilities `q_n` has scalar-quadrature SLD QFI

`F_Q^(k)=sum_n q_nq_{n+k}/(q_n+q_{n+k})`.

The latent classical label FI is `1/2`, so maximal source-normalized quantum retention is

`boxed: G_Q(k)=2 sum_n q_nq_{n+k}/(q_n+q_{n+k})`.

For mixed states the same population formula is an upper bound by purification and QFI monotonicity.

Mode sum:

`boxed: sum_{k>=1}G_Q(k)<=2nbar`,

`boxed: sum_{k!=0}G_Q(k)<=4nbar`.

The discrete constants are sharp as suprema. Every parameter-independent quantum detector, coherent memory, apparatus reference state, joint channel, and final measurement is downstream of the encoded-state QFI, so this is detector-independent.

Cosine/sine SLDs are generally not jointly compatible. Do not claim simultaneous attainability of the full two-quadrature SLD QFIM.

### Sharp continuum law — WP12/WP15

For any normalized positive-frequency spectral density `q(w)` with finite first moment

`wbar=int_0^infinity w q(w)dw`,

the continuum random-time maximal QFI retention is

`G_Q(nu)=2 int_0^infinity q(w)q(w+nu)/[q(w)+q(w+nu)] dw`, `nu>0`,

with even extension.

The positive-side area is

`A[q]=iint q(x)q(y)/[q(x)+q(y)] dxdy`.

WP15 gives a general finite-first-moment proof without smoothness assumptions. Rearrangement reduces to decreasing `q`; the superlevel-length function `r(s)` obeys

`wbar=(1/2)||r||_2^2`.

Using

`ab/(a+b)=int_0^a int_0^b 2st/(s+t)^3 dt ds`,

Tonelli gives `A=<r,Tr>` with kernel

`L(s,t)=2st/(s+t)^3`.

The exact norm is

`||T||=pi/4`,

hence

`boxed: int_0^infinity G_Q(nu)dnu <= (pi/2)wbar`,

and two-sided

`boxed: int_R G_Q(nu)dnu <= pi Ebar^+/hbar`.

Flat-band inverse law:

`boxed: Ebar^+ >= (2/pi) h B q0`.

The constant is sharp as a supremum, approached by truncated critical densities `q_R(w) proportional (1+w)^(-2)`.

This remains the strongest measurement-independent Planck-scale temporal-information resource law in the program.

### WP16 priority correction — the analytic `pi/4` constant is classical

WP16 establishes that the WP15 operator inequality is an explicit specialization of classical parameterized Hardy–Hilbert integral inequalities.

The standard sharp form

`iint f(x)g(y)/(x+y)^lambda dxdy`

`<= B(lambda/2,lambda/2)`

`   * [int x^(1-lambda)f(x)^2 dx]^(1/2)`

`   * [int y^(1-lambda)g(y)^2 dy]^(1/2)`

holds for `lambda>0` with best Beta-function constant. Taking `lambda=3`, `f(x)=x r(x)`, `g(y)=y r(y)` gives `B(3/2,3/2)=pi/8`; multiplying by the factor `2` in the WP15 kernel yields exactly `||T||=pi/4`.

Therefore **do not claim mathematical novelty for the `pi/4` operator norm, Mellin constant, or sharp Hilbert-type inequality**. Cite classical Hardy–Hilbert theory, including B. Yang, JMAA 321, 182–192 (2006), DOI `10.1016/j.jmaa.2005.07.071`.

The candidate novelty, if priority survives, is the quantum-statistical and physical synthesis: random latent-time Fourier-mode estimation, exact source-normalized QFI retention, the `2nbar` sum rule, controlled continuum temporal-information law, and detector-independent photodetection interpretation.

## Physical source scope — WP13/WP14

### Included

WP10 depends only on the distribution of the **total time-translation generator**. Fixed-photon-number multiphoton/entangled/multimode pulses and arbitrary degeneracy are included by using total-energy sectors.

For an independent quantum-marked Poisson event source, QFI and total excess energy are additive in event number, so the source-normalized mode-retention law is unchanged. Any subsequent parameter-independent mapping into a common bosonic field, wavepacket overlap, propagation, coherent detector memory, and measurement cannot increase QFI.

### Not included without extra resource accounting

WP14 gives a coherent-field no-go against extending the theorem to arbitrary waveform state engineering based only on baseline mean energy. A carrier coherent state can acquire an arbitrarily high-frequency infinitesimal sideband at first order in amplitude while the additional energy appears only at second order.

The current theorem applies to **random temporal-distribution encoding of a fixed semibounded-energy excitation**, not arbitrary parameter-dependent source-state synthesis.

A broader quantum-waveform theorem would need to include the encoding-map/control resource, e.g. energy curvature or tangent/action cost.

## Covariant timestamp comparison — WP06/WP07/WP08

For a reference-free covariant timestamp readout,

`boxed: int G_timestamp(nu)dnu <=2E_det^+/hbar`,

or `E_det^+>=hBq`.

WP08 proves this is inherited by arbitrary downstream classical detector memory and implies eventual finite-energy quantum regularization of Paper 2's ideal Type-II `1/e` infinite-frequency plateau.

The arbitrary-measurement random-time QFI coefficient is `pi`, versus `2` for the covariant timestamp class. The maximal area ratio allowed by the current upper bounds is `pi/2`. Operational attainability of the `pi` coefficient by one measurement remains open.

## External reference boundary — WP09

Mean energy does not bound deterministic global time-shift QFI if a sparse high-energy tail and an external phase/time reference are allowed. This does not defeat WP10/WP12 because their unknown is a Fourier component of a random event-time distribution; baseline randomization twirls absolute temporal phase before the detector is chosen.

## Major prior-art boundaries

Do not claim novelty for:

- SLD QFI or harmonic-mean denominators;
- Fisher/QFI monotonicity;
- U(1)/time-translation mode decomposition;
- generic waveform QFI kernels;
- covariant time POVMs;
- time-translation asymmetry as resource theory;
- rearrangement/layer cake/Mellin/Carleman analysis;
- Hardy/Gagliardo--Nirenberg inequalities;
- **the sharp Hardy–Hilbert operator constant `pi/4` used in WP15**;
- generic time-energy uncertainty relations.

Close sources include Marvian--Spekkens (PRA 90, 062110, 2014), Tsang--Wiseman--Caves (PRL 106, 090401, 2011), Pocovnicu (Analysis & PDE 4, 379--404, 2011), Kiukas--Ruschhaupt--Werner arrival-time work, Hall (Entropy 24, 1679, 2022), Yang's Hilbert-type operator literature, WAY/asymmetry literature, phase-diffusion/dephasing estimation, and random-unitary/noise-channel estimation.

Targeted searches still have not found the exact **quantum random-time distribution-mode** formula, `2nbar` sum rule, or their source-to-record temporal-information interpretation. Priority is not certified. The next search must target estimation of random-unitary mixing distributions / Fourier coefficients of probability measures on `U(1)`, because generic phase-noise searches are no longer sufficient.

## Immediate hostile gates

1. **Priority Gate 1A:** deep search for estimation of Fourier coefficients or mixing weights of `U(1)` random-unitary channels / probability measures on groups.
2. **Priority Gate 1B:** determine whether the harmonic-mean density inequality itself appears explicitly in analysis literature; its operator constant is already classical.
3. **Operational attainability:** determine whether a single measurement family can approach the integrated `pi` QFI-area coefficient, given per-mode SLD incompatibility, or whether `pi` is only a sum of separately optimized bounds.
4. Strengthen the independent quantum-marked Poisson to field mapping for realistic incoherent optical source models.
5. Explore a broader theorem including the energetic/control resource of arbitrary waveform encoding only if it does not distract from the stronger random-time theorem.
6. If priority survives and operational interpretation remains strong, decide whether WP10--WP15 justify a standalone foundational manuscript.

## Documentation rule

After every material theorem, counterexample, proof repair, prior-art collision, numerical result, or strategy change:

1. update/create `grand_challenge/notes/WP*.md` immediately;
2. update this file when the active theorem/gates change;
3. update active-branch top-level `README.md`, `AGENTS.md`, `docs/CURRENT_RESEARCH_STATE.md`, and `ROADMAP.md` for every project-level change;
4. mirror the active branch/checkpoint into the same landing files on `main` so the repository default view remains current;
5. keep `PROBLEM.md` and `grand_challenge/README.md` from becoming misleading secondary entry points;
6. do not rely on chat history as the only record.