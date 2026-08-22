# AGENTS.md

## Purpose

Durable repository handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

`main` is the landing/index branch. Active derivations and the Grand Challenge manuscript live on `agent/temporal-information-resource-law`.

Research is analytical/theoretical. Paper 1 Rev11 and Paper 2 Rev7 are frozen.

## Current status

**Grand Challenge science checkpoint: WP24.**

**Preferred Grand Challenge manuscript: Rev4 — locally build-verified, visually inspected, bibliography-audited, and frozen unless a concrete theorem, priority, build, or referee-level defect appears.**

Mandatory first action for a replacement agent: switch to

`agent/temporal-information-resource-law`

and read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV4_LOCAL_BUILD_AND_HOSTILE_REVIEW_2026-08-22.md`
3. `grand_challenge/notes/MANUSCRIPT_REV4_BIBLIOGRAPHY_PROVENANCE_AUDIT_2026-08-22.md`
4. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
5. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
6. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
7. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`
8. `docs/CURRENT_RESEARCH_STATE.md`
9. `ROADMAP.md`

Do not resume the historical HgCdTe/Kane frontier shown in older `main` commits.

# Strongest current theorem

For exact periodic random-time encoding with sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

For any finite number `N` of independently encoded excitations and **any joint POVM**,

`Tr F_N^(k)<=N min(D_k,U_k)<=N T_k`.

Therefore

`R_N(k)=Tr F_N^(k)/N<=T_k`,

`sum_(k>=1)R_N(k)<=nbar`.

`R_N(k)` is the two-quadrature / phase-averaged source-normalized Fisher retention. A scalar guarantee that must hold for every sinusoidal phase obeys the same ceiling.

WP20 proves this directly by Hilbert--Schmidt Cauchy--Schwarz, including arbitrary entangled finite-copy collective measurements.

## Controlled continuum form

For a positive excitation-frequency spectral probability measure `mu` with finite first moment, controlled large-period limits of exact periodic approximants satisfy

`R(nu)<=mu([nu,infinity))`.

Consequently

`int_R R(nu)dnu<=2Ebar^+/hbar`,

and

`Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

The geometric/exponential canonical phase-time family attains the bound exactly.

## Physical scope

WP23 extends this source-normalized theorem to an independent quantum-marked compound-Poisson source followed by arbitrary parameter-independent source-to-bosonic-field formation, wavepacket overlap, coherent detector memory, ancillas, and measurement.

WP14 excludes arbitrary coherent waveform state synthesis based only on baseline mean energy.

# Secondary QFI envelope

WP10/WP12/WP15 remain valid separately optimized SLD-QFI metric bounds:

`sum_(k>=1)G_Q(k)<=2nbar`,

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

They are secondary to the sharp operational theorem. WP16 records that the `pi/4` operator norm is classical Hardy--Hilbert mathematics.

# Prior-art discipline

Do not claim novelty for `U(1)` modes of asymmetry, weighted random phase/time twirling, canonical phase POVMs, photon-number-constrained phase estimation, arbitrary-measurement Fisher/Holevo/RLD/SLD bounds, random-unitary probability estimation, waveform QFI, Hardy--Hilbert/positive-frequency inequalities, or generic CPTP/Poisson machinery.

The candidate contribution is narrowly the **operational classical-Fisher tail/survival law** for Fourier perturbations of the latent random-time mixing distribution and its sharp source-to-record energy consequences.

Priority remains **unverified, not certified**.

# Manuscript status

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

Rev4 has passed full local LaTeX/BibTeX compilation, seven-page visual inspection, deterministic random-POVM sanity tests, and DOI/title bibliography auditing. A real Pocovnicu metadata mismatch was corrected; the DOI had pointed to the scientifically correct sharp-inequality paper but the title was wrong.

The current connector does not expose the branch-push GitHub Actions run. Do not claim direct remote CI inspection; equivalent local build verification is complete.

# Current work order

Do **not** accumulate another theorem by default. Continue with publication engineering only: remote CI inspection if accessible, one figure only if materially useful, conservative priority language, and factual submission metadata when supplied.

# Documentation discipline

Every project-level theorem/status change must update the active notes/landing files and then be mirrored onto `main`. Never leave the frontier only on an agent branch or in chat.
