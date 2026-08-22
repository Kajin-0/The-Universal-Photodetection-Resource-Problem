# Grand Challenge — Temporal Information Resource Law

**Science checkpoint: WP24 — 2026-08-22**

**Preferred manuscript: Rev4 — locally build-verified and frozen unless a concrete theorem, priority, build, or referee-level defect is found.**

This directory contains the active theoretical program launched from the frozen Paper-2 result on Fisher spectra of autonomous detector channels.

## Grand question

> For a physically realizable measurement of temporal structure, what fundamental resources constrain source-to-record temporal Fisher-information transfer?

## Current strongest theorem

For the exact periodic random-time model with sector probabilities `q_n`, let

`T_k=sum_(m>=k)q_m`.

For any finite number `N` of independently encoded excitations and any joint POVM,

`Tr F_N^(k)<=N min(D_k,U_k)<=N T_k`.

Hence

`R_N(k)=Tr F_N^(k)/N<=T_k`,

`sum_(k>=1)R_N(k)<=nbar`.

`R_N(k)` is the two-quadrature / phase-averaged source-normalized Fisher retention. WP20 proves the theorem directly for arbitrary entangled finite-copy collective measurements.

## Controlled continuum limit

For a positive excitation-frequency spectral probability measure `mu` with finite mean, controlled large-period limits of exact lower-bin periodic approximants satisfy

`R(nu)<=mu([nu,infinity))`.

Therefore

`int_R R(nu)dnu<=2Ebar^+/hbar`,

and

`Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

The geometric-sector / exponential-spectrum canonical phase-time family saturates the bound exactly.

## Physical source scope

WP23 extends the theorem to an independent quantum-marked compound-Poisson event source followed by arbitrary parameter-independent formation of a common bosonic field, wavepacket overlap, coherent detector memory, ancillas, and measurement.

This is not a theorem for every field with Poisson photocount statistics and not a theorem for arbitrary coherent waveform synthesis.

## Secondary QFI envelope

WP10/WP12/WP15 remain correct as separately optimized SLD-QFI metric bounds:

`sum_(k>=1)G_Q(k)<=2nbar`,

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

They are secondary to the operational theorem. WP16 identifies the `pi/4` analytic operator norm as established Hardy--Hilbert mathematics.

## Prior-art boundary

Weighted `U(1)` twirling/energy-gap modes, canonical phase measurements, phase Fourier methods, photon-number-constrained phase estimation, arbitrary-measurement information bounds, random-unitary probability estimation, waveform QFI, sharp positive-frequency inequalities, and Hardy--Hilbert mathematics are prior art.

The candidate contribution is narrowly the arbitrary-measurement **classical-Fisher tail law** for perturbations of the latent random-time mixing distribution, its paired-population/mean-energy evaluation, and source-to-record consequences.

Targeted searches have not located an exact predecessor. **Priority remains unverified, not certified.**

## Preferred manuscript — Rev4

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

Generation chain:

`manuscript/energy_survival_temporal_fisher_rev1.tex`

`-> manuscript/apply_rev2_mechanical.py`

`-> manuscript/apply_rev3_hostile_review.py`

`-> manuscript/apply_rev4_final_polish.py`.

Rev4 has passed:

- full local LaTeX/BibTeX build;
- seven-page render/visual inspection;
- unresolved-reference/citation and overfull-box gates;
- deterministic random-POVM theorem validation;
- DOI/title/provenance bibliography audit.

The bibliography audit corrected a real Pocovnicu title mismatch while preserving the scientifically correct DOI/source and upgraded Gill to the published 2008 chapter metadata.

The current connector does not expose the relevant branch-push GitHub Actions run, so direct remote-job inspection is not claimed. Equivalent full local build verification is complete.

## Read first

1. `AGENTS.md`
2. `notes/MANUSCRIPT_REV4_LOCAL_BUILD_AND_HOSTILE_REVIEW_2026-08-22.md`
3. `notes/MANUSCRIPT_REV4_BIBLIOGRAPHY_PROVENANCE_AUDIT_2026-08-22.md`
4. `notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
5. `notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
6. `notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
7. `notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`

## Current work order

Do not accumulate another theorem by default. Continue with publication engineering only. Add a figure only if it materially improves comprehension.

The repository handoff files must remain sufficient for full context recovery; do not rely on chat history.
