# Research Roadmap

**Updated:** 2026-08-22

**Active scientific branch:** `agent/temporal-information-resource-law`

Paper 1 Rev11 and Paper 2 Rev7 are frozen.

Grand Challenge science checkpoint: **WP24**.

- **Rev4:** frozen science/claim content.
- **Rev5:** frozen publication content.
- **Rev6:** current PRX Quantum target package; style-only conversion from Rev5.

# Established theorem hierarchy

## G1 — finite-copy operational survival law — WP20/WP24

For exact periodic random-time encoding with sector probabilities `q_n`, harmonic `k`, and

`T_k=sum_(m>=k)q_m`,

any finite `N` and any joint POVM obey

`Tr F_N^(k)<=N min(D_k,U_k)<=N T_k`.

Thus

`R_N(k)=Tr F_N^(k)/N<=T_k`,

and

`sum_(k>=1)R_N(k)<=nbar`.

`R_N(k)` is the two-quadrature / phase-averaged source-normalized retention. The result includes arbitrary finite-copy collective measurements.

## G2 — controlled continuum survival law — WP22

For a positive excitation-frequency spectral probability measure `mu` with finite mean, controlled large-period limits of exact lower-bin periodic approximants satisfy

`R(nu)<=mu([nu,infinity))`.

Therefore

`int_R R(nu)dnu<=2Ebar^+/hbar`,

and

`Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

## G3 — exact sharpness

Geometric sector populations with the canonical phase POVM saturate every discrete harmonic simultaneously. The controlled continuum equality family is exponential-energy/Cauchy-time.

## G4 — independent Poisson source to field — WP23

The source-normalized bound survives an independent quantum-marked compound-Poisson source followed by arbitrary parameter-independent bosonic field formation and detector processing.

## G5 — secondary QFI envelope

WP10/WP12/WP15 remain valid but secondary:

`sum_(k>=1)G_Q(k)<=2nbar`,

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

WP16 records the classical Hardy--Hilbert provenance of the `pi/4` analytic constant.

## G6 — arbitrary coherent waveform synthesis — WP14

**NO-GO.** Baseline mean energy alone does not constrain arbitrary parameter-dependent state-valued waveform synthesis.

# Priority status

The candidate contribution is the exact operational classical-Fisher tail/survival theorem and its source-to-record consequences. Generic `U(1)` mode theory, phase estimation, quantum-information bounds, waveform QFI, Hardy--Hilbert analysis, and Poisson/CPTP machinery are prior art.

**Priority remains unverified, not certified.**

# Manuscript / target gates

## Science gate — PASSED

WP24 / Rev4.

## Publication-content gate — PASSED

Rev5. One conceptual architecture figure and `hidelinks` only; no science changes.

## PRX Quantum packaging gate — PASSED

Rev6 changes only the REVTeX journal option from `pra` to `prx`.

Target-style checks:

- 7 pages;
- no local overfull/fatal-control regression;
- visual page flow unchanged;
- dedicated CI generates/compiles Rev6;
- fresh randomized validation: 11,825 one-copy + 936 global two-copy POVMs, no theorem violation;
- equality family verified at machine precision.

# Journal ladder

1. **PRX Quantum — Research Article**: first target.
2. **Physical Review A — Regular Article**: preferred fallback, including APS transfer if offered after a selectivity rejection.
3. Physical Review Research: secondary alternative.
4. PRL: stretch only after a deliberate Letter rewrite; do not compress Rev5/Rev6 by hiding essential assumptions or proof structure.

PRX Quantum has no Research Article length limit and directly covers quantum metrology/sensing plus photon sources/detectors. APS lists a 2026 APC of USD 3,590 for PRX Quantum.

# Submission files

- `grand_challenge/submission/PRX_QUANTUM_TARGET_AND_CHECKLIST_2026-08-22.md`
- `grand_challenge/submission/PRX_QUANTUM_COVER_LETTER_DRAFT.md`
- `grand_challenge/submission/PRX_QUANTUM_POPULAR_SUMMARY_DRAFT.md`
- `grand_challenge/submission/APS_AI_AND_DATA_DISCLOSURE_DRAFTS.md`
- `grand_challenge/notes/MANUSCRIPT_REV6_PRXQ_PACKAGING_PREFLIGHT_2026-08-22.md`

# Current work order — human submission completion

No new theorem or polish work by default.

1. Human author performs and records the verification required by APS's 2026 AI policy.
2. Supply author name/order, affiliation(s), contact email, optional ORCID(s), funding/conflict/submission-history facts.
3. Decide preprint/e-print status.
4. Select a stable repository/archive citation for Data Availability.
5. Decide optional referee recommendations/exclusions.
6. Confirm PRX Quantum APC coverage/institutional agreement.
7. Generate final administrative Rev6 package.
8. Run one final build/checksum/visual pass.
9. Submit to PRX Quantum.

If PRX Quantum declines on selectivity rather than correctness, prefer transfer to PRA rather than broadening the claims.

# Documentation discipline

Every material theorem, prior-art collision, manuscript defect, or publication-status change must update the detailed notes, active landing/handoff files, and `main`.