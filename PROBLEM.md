# Formal Problem Statement

**Updated:** 2026-08-22

**Default branch role:** landing/index only.

**Active scientific branch:** `agent/temporal-information-resource-law`

## Current problem

For a fixed semibounded-energy quantum excitation emitted at a latent random time, how much Fisher information about Fourier components of the **event-time probability distribution** can any physically realizable source-to-record measurement retain?

The current theorem class is deliberately narrower than arbitrary waveform state synthesis. The unknown temporal parameters enter through the random translation distribution; all later source-to-field and detector dynamics are parameter independent.

## Strongest result

For periodic total-generator sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

For any finite number `N` of independently encoded excitations and any joint POVM,

`boxed: Tr F_N^(k)<=N T_k`.

Thus the two-quadrature source-normalized operational retention satisfies

`boxed: R_N(k)<=T_k`,

and

`boxed: sum_(k>=1)R_N(k)<=nbar`.

A support-sensitive refinement is

`R_N(k)<=min(D_k,U_k)<=T_k`.

The proof is a direct finite-copy Hilbert--Schmidt Cauchy--Schwarz argument using the energy-gap partial-shift factorization of the random-time tangent.

## Continuum

For a positive excitation-frequency spectral probability measure `mu` with finite mean,

`boxed: R(nu)<=mu([nu,infinity))=P(Omega>=nu)`.

Therefore

`boxed: int_R R(nu)dnu<=2Ebar^+/hbar`,

and pointwise

`boxed: Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

The geometric sector / exponential continuum canonical phase-time family attains the bound exactly.

## Source-to-field scope

For an independent quantum-marked compound-Poisson event source, revealing event number and applying the finite-copy theorem gives `Tr F^(k)<=mu T_k`.

Any subsequent physical emission/source-to-bosonic-field/detector process whose dynamics are fixed after encoding is a parameter-independent CPTP map. Pulling the final POVM back through that map proves the same normalized survival law after arbitrary wavepacket overlap and coherent detector memory.

This does not follow merely from observing Poisson photocount statistics.

## Secondary QFI envelope

Separately optimized SLD-QFI obeys

`sum_(k>=1)G_Q(k)<=2nbar`,

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

This is an incompatible modewise quantum envelope, not the main operational theorem.

## Mandatory boundary

WP14 proves baseline mean energy cannot constrain arbitrary parameter-dependent coherent waveform synthesis. A broader theorem would require explicit encoding/control/action resource accounting.

## Prior-art boundary

`U(1)` modes of asymmetry and weighted twirling are established. Marvian--Spekkens, Phys. Rev. A 90, 062110 (2014), already show

`sigma^(k)=p_(-k)rho^(k)`.

Canonical phase measurements, energy/photon-number constrained phase estimation, arbitrary collective Fisher/Holevo bounds, random-unitary probability estimation, asymmetry resource theory, and the Hardy--Hilbert mathematics underlying earlier QFI bounds are also prior art.

The candidate contribution is narrowly the **operational Fisher ceiling for perturbations of the random-time mixing distribution**, its explicit population-tail/mean-energy law, and source-to-record photodetection interpretation.

Targeted searches have not located the exact theorem. Priority is **unverified**, not certified.

## Current status

WP24 integrated hostile review: **PASS** after direct-proof replacement, support-gap repair, continuum hardening, source-to-field formalization, and prior-art narrowing.

The project is at a reasonable standalone manuscript-formation threshold.

## Recovery

Switch to `agent/temporal-information-resource-law` and read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
3. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
4. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
5. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`
6. `ROADMAP.md`
7. `docs/CURRENT_RESEARCH_STATE.md`

Do not resume historical semiconductor-resource work by default.