# AGENTS.md

## Purpose

Durable repository handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

`main` is the landing/index branch. Active derivations live on `agent/temporal-information-resource-law`.

Research is analytical/theoretical. Paper 1 Rev11 and Paper 2 Rev7 are frozen.

## Current status

**Grand Challenge latest checkpoint: WP24.**

Mandatory first action for a replacement agent: switch to

`agent/temporal-information-resource-law`

and read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
3. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
4. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
5. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`
6. `grand_challenge/notes/WP21_TARGETED_PRIORITY_AUDIT_SURVIVAL_FUNCTION_LAW.md`
7. `docs/CURRENT_RESEARCH_STATE.md`
8. `ROADMAP.md`

Do not resume the historical HgCdTe/Kane frontier shown in older `main` commits.

# Strongest current theorem

For periodic random-time encoding of a fixed semibounded-energy excitation with sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

For any finite number `N` of independently encoded excitations and **any joint POVM**,

`boxed: Tr F_N^(k)<=N T_k`.

Therefore

`boxed: R_N(k)=Tr F_N^(k)/N<=T_k`,

`boxed: sum_(k>=1)R_N(k)<=nbar`.

A support-sensitive refinement is

`R_N(k)<=min(D_k,U_k)<=T_k`.

WP20 proves this directly by Hilbert--Schmidt Cauchy--Schwarz, including arbitrary entangled collective measurements.

## Continuum

For a positive excitation-frequency spectral probability measure `mu` with finite first moment,

`boxed: R(nu)<=mu([nu,infinity))`.

Consequently

`boxed: int_R R(nu)dnu<=2Ebar^+/hbar`,

and

`boxed: Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

The geometric/exponential canonical phase-time family attains the bound exactly.

## Physical scope

WP23 extends this source-normalized theorem to an independent quantum-marked compound-Poisson source followed by arbitrary parameter-independent source-to-bosonic-field formation, wavepacket overlap, coherent detector memory, ancillas, and measurement.

WP14 excludes arbitrary coherent waveform state synthesis based only on baseline mean energy.

# Secondary QFI envelope

WP10/WP12/WP15 remain valid separately optimized SLD-QFI bounds:

`sum_(k>=1)G_Q(k)<=2nbar`,

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

They are secondary to the sharp jointly operational theorem. WP16 records that the `pi/4` operator norm is classical Hardy--Hilbert mathematics.

# Prior-art discipline

Do not claim novelty for `U(1)` modes of asymmetry, weighted random phase/time twirling, canonical phase POVMs, photon-number-constrained phase estimation, arbitrary-measurement Fisher/Holevo/RLD/SLD bounds, random-unitary probability estimation, QFI/asymmetry resource theory, Hardy--Hilbert analysis, or generic CPTP/Poisson machinery.

Marvian--Spekkens, Phys. Rev. A **90**, 062110 (2014), already establish weighted `U(1)` twirling `sigma^(k)=p_(-k)rho^(k)`.

The candidate contribution is narrowly the **operational Fisher tail/survival law** for perturbations of the latent random-time mixing distribution and its sharp source-to-record energy consequences.

Priority remains unverified.

# Publication status

WP24 integrated hostile review: **PASS** after support-gap repair and prior-art narrowing.

The project is at a reasonable standalone-manuscript formation threshold. Immediate next work is manuscript architecture plus continued focused historical priority checking.

# Documentation discipline

Every project-level theorem/gate change must update the active WP notes and active landing files, then be mirrored onto `main`. Never leave the scientific frontier only on an agent branch or in chat.