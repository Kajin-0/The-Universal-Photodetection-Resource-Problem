# Grand Challenge — Temporal Information Resource Law

**Science checkpoint: WP24 — 2026-08-22**

**Frozen science content: Rev4. Frozen publication content: Rev5. Current journal package: Rev6 PRX Quantum.**

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

## Manuscript / target package

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

Generation chain:

`Rev1 -> Rev2 mechanical -> Rev3 hostile-review repair -> Rev4 science/claim polish -> Rev5 publication figure/link pass -> Rev6 PRX Quantum style package`.

- **Rev4:** frozen science/claim checkpoint.
- **Rev5:** frozen publication content; one conceptual two-column figure and hidden hyperlink decorations only.
- **Rev6:** target packaging only; changes REVTeX journal option from `pra` to `prx` and changes no scientific content.

Rev5 has passed the complete local LaTeX/BibTeX, visual, figure, numerical, and bibliography preflight.

Rev6 target-style preflight has also passed: seven pages, no target-style layout regression, no local overfull/fatal-control issue, dedicated CI generation/compile gate, and a fresh numerical hostile check with 11,825 one-copy and 936 global two-copy random POVMs showing no violation. The geometric equality family was verified at machine precision.

The current connector does not expose the relevant branch-push GitHub Actions run, so direct remote-job inspection is not claimed.

## Journal target

**First target: PRX Quantum — Research Article.**

**Preferred fallback: Physical Review A — Regular Article.**

PRL is a stretch only after a deliberate Letter rewrite; do not force the seven-page theorem into a four-page core by hiding essential hypotheses or proof structure.

## APS submission compliance

APS's June 2026 AI policy requires disclosure of substantive AI use. This project used AI substantively in reasoning/literature synthesis, proof checking, code assistance, manuscript drafting/editing, and conceptual figure development. Final submission therefore requires a truthful human verification record and disclosure.

Submission support files:

1. `submission/PRX_QUANTUM_TARGET_AND_CHECKLIST_2026-08-22.md`
2. `submission/PRX_QUANTUM_COVER_LETTER_DRAFT.md`
3. `submission/PRX_QUANTUM_POPULAR_SUMMARY_DRAFT.md`
4. `submission/APS_AI_AND_DATA_DISCLOSURE_DRAFTS.md`
5. `notes/MANUSCRIPT_REV6_PRXQ_PACKAGING_PREFLIGHT_2026-08-22.md`

## Read first

1. `AGENTS.md`
2. `notes/MANUSCRIPT_REV6_PRXQ_PACKAGING_PREFLIGHT_2026-08-22.md`
3. `submission/PRX_QUANTUM_TARGET_AND_CHECKLIST_2026-08-22.md`
4. `submission/APS_AI_AND_DATA_DISCLOSURE_DRAFTS.md`
5. `notes/MANUSCRIPT_REV5_PUBLICATION_PREFLIGHT_2026-08-22.md`
6. `notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`

## Current work order

Do not accumulate another theorem or polish revision by default. Remaining work is human submission completion: verification for APS AI disclosure, author/affiliation/contact/funding metadata, stable code/archive citation for Data Availability, optional referee/preprint information, APC coverage, and final submission.

The repository handoff files must remain sufficient for full context recovery; do not rely on chat history.