# The Universal Photodetection Resource Problem

**Status synchronized: 2026-08-22**

## Project split

1. **Paper 1 / Rev11** — frozen and technically validated.
2. **Paper 2 / Rev7** — frozen preferred science draft.
3. **Grand Challenge** — science checkpoint **WP24**; Rev4 freezes science; Rev5 freezes publication content; **Rev6 is the current PRX Quantum target package**.

Active Grand Challenge branch: `agent/temporal-information-resource-law`.

Authoritative handoff: `grand_challenge/AGENTS.md`.

# Strongest result — operational survival-function law

For the exact periodic random-time experiment with sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

For any finite number `N` of independent encoded excitations and any joint POVM,

`Tr F_N^(k)<=N min(D_k,U_k)<=N T_k`.

Thus

`R_N(k)=Tr F_N^(k)/N<=T_k`,

and

`sum_(k>=1)R_N(k)<=nbar`.

`R_N(k)` is the two-quadrature / phase-averaged source-normalized Fisher retention. WP20 proves the result directly for arbitrary entangled finite-copy collective measurements.

## Controlled continuum form

For a positive excitation-frequency probability measure `mu` with finite mean, controlled large-period limits of exact periodic approximants obey

`R(nu)<=mu([nu,infinity))=P(Omega>=nu)`.

Therefore

`int_R R(nu)dnu<=2Ebar^+/hbar`,

and

`Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

A phase-averaged retention `q0`, or a scalar-retention guarantee `q0` for every sinusoidal phase, at ordinary frequency `B` requires `Ebar^+>=hBq0`.

## Exact equality family

Geometric sectors `q_n=(1-r)r^n` with the canonical phase POVM give `R(k)=r^k=T_k` for every harmonic simultaneously. The controlled continuum limit is exponential. With `beta=2a`, the Cauchy timestamp characteristic function is `exp(-a|nu|)` and its Fisher retention is `exp(-2a|nu|)`.

## Independent Poisson source to common bosonic field — WP23

For independent quantum-marked Poisson events with mean `Lambda`, event-number side information gives `Tr F^(k)<=Lambda T_k`. Any subsequent parameter-independent source-to-field/detector CPTP map can be pulled back to the event register, so bosonic overlap, mode mixing, coherent detector memory, ancillas, and final measurement cannot evade the same normalized tail law.

This is an explicit independent-event source class, not a theorem for every quantum field with Poisson photocount statistics.

# Secondary QFI envelope and scope boundary

WP10/WP12/WP15 remain valid as separately optimized SLD-QFI metric bounds:

`sum_(k>=1)G_Q(k)<=2nbar`,

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

They are secondary to the sharp operational `2E/hbar` law. WP16 records that the `pi/4` analytic constant is classical Hardy--Hilbert mathematics.

WP14 proves baseline mean energy does not constrain arbitrary parameter-dependent waveform-state synthesis; a broader theorem needs encoding/control/action resource accounting.

# Prior-art boundary

Weighted `U(1)` twirling/energy-gap modes, canonical phase measurements, number/energy-constrained phase estimation, arbitrary-measurement quantum-information bounds, random-unitary probability estimation, waveform QFI, positive-frequency sharp inequalities, Hardy--Hilbert best constants, and generic Poisson/CPTP machinery are prior art.

The candidate contribution is narrowly the arbitrary-measurement **classical-Fisher tail/survival law** for Fourier perturbations of a latent random-time distribution and its paired-population/mean-energy/source-to-record consequences.

Targeted searches have not found an exact predecessor. **Priority remains unverified, not certified.**

# Manuscript and journal target

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

Deterministic generation:

`Rev1 -> Rev2 -> Rev3 -> Rev4 -> Rev5 -> Rev6 PRX Quantum style package`.

- **Rev4:** frozen science/claim content.
- **Rev5:** preferred publication content; adds one conceptual architecture figure and `hidelinks` only.
- **Rev6:** changes only the REVTeX journal option `pra -> prx`; no scientific content changes.

Rev5 complete build/visual/bibliography preflight: PASS.

Rev6 target-style preflight:

- pages remain **7**;
- no overfull boxes or fatal controls in local target-style reproduction;
- visual page-flow regression: none found;
- Figure 1 remains readable;
- dedicated CI now generates/compiles Rev6;
- fresh randomized theorem check: 11,825 one-copy and 936 global two-copy POVMs, no violation; equality family verified at machine precision.

**First target: PRX Quantum, Research Article.**

**Preferred fallback: Physical Review A, Regular Article.**

PRL is a stretch only after a deliberate Letter rewrite; do not force the seven-page theorem into PRL by hiding essential assumptions or proof structure.

PRX Quantum is fully open access; APS lists a 2026 APC of USD 3,590, subject to institutional agreements/eligible waivers.

# APS submission compliance

APS's June 2026 AI policy requires disclosure of substantive AI use. This project used AI substantively in scientific reasoning/literature synthesis, proof checking, code assistance, manuscript drafting/editing, and conceptual figure development. Final submission therefore requires a truthful human verification record and disclosure.

See:

- `grand_challenge/submission/PRX_QUANTUM_TARGET_AND_CHECKLIST_2026-08-22.md`
- `grand_challenge/submission/PRX_QUANTUM_COVER_LETTER_DRAFT.md`
- `grand_challenge/submission/PRX_QUANTUM_POPULAR_SUMMARY_DRAFT.md`
- `grand_challenge/submission/APS_AI_AND_DATA_DISCLOSURE_DRAFTS.md`

Do not invent author, affiliation, funding, conflict, ORCID, prior-submission, referee, preprint, or APC-coverage facts.

## Read first

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV6_PRXQ_PACKAGING_PREFLIGHT_2026-08-22.md`
3. `grand_challenge/submission/PRX_QUANTUM_TARGET_AND_CHECKLIST_2026-08-22.md`
4. `grand_challenge/notes/MANUSCRIPT_REV5_PUBLICATION_PREFLIGHT_2026-08-22.md`
5. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`

## Current work order

Do not accumulate another theorem or polish revision by default. Remaining work is human submission completion: verification for APS AI disclosure, author/affiliation/contact/funding metadata, stable code/archive citation for Data Availability, optional referee/preprint information, APC coverage, and final submission.

## Documentation discipline

Every material result/status change must be recorded in the repository and mirrored onto `main`; do not rely on chat history.