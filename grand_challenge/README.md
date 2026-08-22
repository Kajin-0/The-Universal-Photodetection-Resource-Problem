# Grand Challenge — Temporal Information Resource Law

**Current checkpoint: WP24 — 2026-08-22**

This directory contains the active theoretical program launched from the frozen Paper-2 result on Fisher spectra of autonomous detector channels.

## Grand question

> For a physically realizable measurement of temporal structure, what fundamental resources constrain source-to-record temporal Fisher-information transfer?

## Current strongest theorem

For periodic random-time encoding of a fixed semibounded-energy excitation with sector probabilities `q_n`, let

`T_k=sum_(m>=k)q_m`.

For any finite number `N` of independently encoded excitations and any joint POVM,

`boxed: Tr F_N^(k)<=N T_k`.

Hence

`boxed: R_N(k)<=T_k`,

`boxed: sum_(k>=1)R_N(k)<=nbar`.

WP20 proves this directly for arbitrary entangled collective measurements. A support-sensitive refinement is

`R_N(k)<=min(D_k,U_k)<=T_k`.

## Continuum

For a general positive excitation-frequency spectral probability measure `mu` with finite mean,

`boxed: R(nu)<=mu([nu,infinity))`.

Therefore

`boxed: int_R R(nu)dnu<=2Ebar^+/hbar`,

and

`boxed: Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

The geometric sector distribution / exponential continuum spectrum with canonical phase/time measurement saturates the bound exactly.

## Physical source scope

WP23 extends the theorem to an independent quantum-marked compound-Poisson event source followed by arbitrary parameter-independent formation of a common bosonic field, wavepacket overlap, coherent detector memory, and measurement. The final detector POVM pulls back through the source-to-field CPTP channel to the upstream event register.

This is not a theorem for every field with Poisson photocount statistics and not a theorem for arbitrary coherent waveform synthesis.

## Secondary QFI envelope

WP10/WP12/WP15 remain correct as separately optimized SLD-QFI bounds:

`sum_(k>=1)G_Q(k)<=2nbar`,

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

The operational theorem has the sharper attainable coefficient `2E/hbar`. WP16 identifies the `pi/4` analytic operator norm as established Hardy--Hilbert mathematics.

## Prior-art boundary

Marvian--Spekkens, Phys. Rev. A 90, 062110 (2014), already establish `U(1)` energy-gap modes and weighted twirling of the form

`sigma^(k)=p_(-k)rho^(k)`.

Canonical phase measurements, phase Fourier moments, photon-number-constrained phase estimation, arbitrary collective Fisher/Holevo bounds, random-unitary estimation, and asymmetry resource theory are also prior art.

The candidate contribution is narrowly the arbitrary-measurement **Fisher** ceiling for perturbations of the latent random-time mixing distribution, its explicit population-tail/mean-energy law, and the source-to-record photodetection consequence.

Targeted searches have not located an exact predecessor. Priority remains unverified.

## Current status

WP24 integrated hostile review: **PASS**, after repairing support-gap notation and narrowing novelty language.

The project is now at a reasonable standalone-manuscript formation threshold.

## Read first

1. `AGENTS.md`
2. `notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
3. `notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
4. `notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
5. `notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`
6. `notes/WP21_TARGETED_PRIORITY_AUDIT_SURVIVAL_FUNCTION_LAW.md`

The repository handoff files must remain sufficient for full context recovery; do not rely on chat history.