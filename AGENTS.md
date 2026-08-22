# AGENTS.md

## Purpose

Durable project handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

Research is analytical/theoretical. Numerical work is allowed for validation. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

## Current project split

1. **Paper 1 / Rev11** — scientifically frozen and technically validated; submission metadata/compliance only.
2. **Paper 2 / Rev7** — preferred frozen science draft; locally build-verified and visually inspected.
3. **Grand Challenge** — active high-risk/high-ceiling theory program on quantum resources for temporal information transfer.

**Active scientific branch:** `agent/temporal-information-resource-law`.

**Latest research checkpoint:** **WP24**.

## Mandatory first read

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
3. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
4. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
5. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`
6. `grand_challenge/notes/WP21_TARGETED_PRIORITY_AUDIT_SURVIVAL_FUNCTION_LAW.md`
7. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`
8. `paper2/AGENTS_PAPER2.md` only if frozen Paper-2 context is needed.

# Current strongest result

For random temporal-distribution encoding of a fixed semibounded-energy excitation with periodic total-generator sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

For **any finite number N of independently encoded excitations and any joint POVM**, including arbitrary entangled collective measurements,

`boxed: Tr F_N^(k)<=N T_k`.

Thus

`boxed: R_N(k):=Tr F_N^(k)/N<=T_k`,

and

`boxed: sum_(k>=1)R_N(k)<=nbar`.

WP20 proves this directly by Hilbert--Schmidt Cauchy--Schwarz. A support-sensitive strengthening is

`boxed: R_N(k)<=min(D_k,U_k)<=T_k`,

where `D_k` and `U_k` are the paired source/range probability masses separated by harmonic `k`.

## Continuum

For a general positive excitation-frequency probability measure `mu` with finite mean,

`boxed: R(nu)<=mu([nu,infinity))=P(Omega>=nu)`.

Consequently

`boxed: int_R R(nu)dnu<=2Ebar^+/hbar`,

and pointwise

`boxed: Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

Hence retaining fraction `q0` at ordinary frequency `B` requires

`boxed: Ebar^+>=hBq0`.

The geometric/exponential canonical phase/time family attains the bound exactly.

## Physical source-to-record scope

WP23 proves the same normalized survival law for an **independent quantum-marked compound-Poisson event source** followed by arbitrary parameter-independent source-to-bosonic-field formation, wavepacket overlap, coherent detector memory, ancillas, and final measurement. The final measurement pulls back through the CPTP channel to a POVM on the upstream event register, where WP20 applies.

This does not cover arbitrary coherent waveform synthesis or every field with Poisson photocount statistics.

# Secondary QFI envelope

WP10/WP12/WP15 remain correct as separately optimized modewise SLD-QFI results:

`sum_(k>=1)G_Q(k)<=2nbar`,

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

They are now secondary. One physical detector obeys the sharper operational `2E/hbar` coefficient. WP16 records that the `pi/4` continuum operator norm is classical Hardy--Hilbert mathematics.

# Scope boundary

WP14 proves baseline mean energy does not constrain arbitrary parameter-dependent coherent waveform state engineering. The operational theorem requires that the unknown temporal parameter enter through the random event-time distribution of a fixed excitation; later hardware is parameter independent.

# Prior-art discipline

Do **not** claim novelty for:

- `U(1)` modes of asymmetry / energy-gap decompositions;
- weighted random phase/time twirling multiplying gap modes by Fourier coefficients;
- canonical phase POVMs or phase Fourier moments;
- phase estimation under photon-number/energy constraints;
- generic Fisher/QFI/Holevo/RLD/SLD measurement bounds;
- random-unitary probability estimation;
- Hardy--Hilbert/Mellin/rearrangement mathematics;
- compound Poisson/CPTP/Stinespring machinery.

Marvian--Spekkens, Phys. Rev. A **90**, 062110 (2014), is a particularly close predecessor for the harmonic encoding: weighted `U(1)` twirling gives `sigma^(k)=p_(-k)rho^(k)`.

The candidate contribution is narrowly the **operational Fisher resource law for perturbations of the latent random-time mixing distribution**, its explicit population-tail value, sharp mean-energy sum/area law, and source-to-record photodetection interpretation.

Targeted searches have not located the exact tail/survival Fisher theorem. **Priority remains unverified, not certified.**

# Current publication gate

WP24 integrated hostile review: **PASS** after support-gap repair and prior-art narrowing.

The previous major scientific blockers are addressed:

1. arbitrary collective measurement — WP20;
2. continuum rigor — WP22;
3. independent Poisson event-to-bosonic-field mapping — WP23.

The project has reached a reasonable standalone-manuscript formation threshold with conservative novelty language.

## Immediate work order

1. synchronize all active landing docs and `main` through WP24;
2. create a standalone manuscript architecture centered on the operational survival-function theorem;
3. continue one final focused historical search during drafting;
4. retain WP14's source-class boundary explicitly;
5. keep the `pi` QFI envelope secondary.

## Frozen papers

Paper 1 Rev11 and Paper 2 Rev7 are not active theorem-development branches. Reopen only for a concrete defect, referee objection, or submission requirement.

## Mandatory documentation rule

After every material theorem, proof repair, prior-art collision, or strategy change:

- update/create `grand_challenge/notes/WP*.md` immediately;
- update `grand_challenge/AGENTS.md`;
- update top-level `README.md`, this file, `docs/CURRENT_RESEARCH_STATE.md`, `ROADMAP.md`, and relevant secondary entry points;
- mirror the checkpoint onto `main`.

Do not allow the authoritative state to exist only on a hidden branch or in chat.