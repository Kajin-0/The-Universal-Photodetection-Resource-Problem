# The Universal Photodetection Resource Problem

**Current status: 2026-08-22**

`main` is the repository landing/index branch. Detailed Grand Challenge derivations and manuscript generation live on `agent/temporal-information-resource-law`.

## Project split

1. **Paper 1 / Rev11** — frozen and technically validated.
2. **Paper 2 / Rev7** — frozen preferred science draft.
3. **Grand Challenge** — science checkpoint **WP24**; Rev4 freezes science; Rev5 freezes publication content; **Rev6 is the current PRX Quantum target package**.

Authoritative active handoff: `grand_challenge/AGENTS.md` on `agent/temporal-information-resource-law`.

# Strongest current theorem

For exact periodic random-time encoding with sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

For any finite number `N` of independently encoded excitations and any joint POVM,

`Tr F_N^(k)<=N min(D_k,U_k)<=N T_k`.

Thus

`R_N(k)=Tr F_N^(k)/N<=T_k`,

and

`sum_(k>=1)R_N(k)<=nbar`.

`R_N(k)` is the two-quadrature / phase-averaged source-normalized Fisher retention. WP20 proves the theorem directly for arbitrary finite-copy entangled collective measurement.

## Controlled continuum form

For a positive excitation-frequency probability measure `mu` with finite first moment, controlled large-period limits of exact periodic approximants obey

`R(nu)<=mu([nu,infinity))=P(Omega>=nu)`,

`int_R R(nu)dnu<=2Ebar^+/hbar`,

`Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

The exact equality family is geometric in the periodic model and exponential-energy/Cauchy-time in the controlled continuum limit.

## Physical source scope

WP23 extends the normalized law to an independent quantum-marked compound-Poisson source followed by arbitrary parameter-independent source-to-bosonic-field formation and detector processing. This is not a theorem for every field with Poisson photocount statistics.

# Boundaries and priority

WP10/WP12/WP15 remain valid separately optimized SLD-QFI metric bounds and are secondary to the operational theorem. WP16 identifies the `pi/4` analytic constant as Hardy--Hilbert prior art. WP14 excludes arbitrary parameter-dependent waveform synthesis from baseline-energy-only control.

Weighted `U(1)` twirling/modes, canonical phase measurement, number-constrained phase estimation, generic quantum-information bounds, random-unitary estimation, waveform QFI, Hardy--Hilbert mathematics, and generic Poisson/CPTP machinery are prior art.

The candidate contribution is narrowly the arbitrary-measurement **classical-Fisher tail/survival law** for Fourier perturbations of a latent random-time distribution and its paired-population/mean-energy/source-to-record consequences.

**Priority remains unverified, not certified.**

# Manuscript and journal target

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

`Rev1 -> Rev2 -> Rev3 -> Rev4 -> Rev5 -> Rev6 PRX Quantum style package`.

- **Rev4:** frozen science/claim content.
- **Rev5:** frozen publication content; one conceptual architecture figure and hidden hyperlink decorations only.
- **Rev6:** journal packaging only; REVTeX `pra -> prx`, with no science changes.

Rev5 passed complete local build, bibliography, numerical, and visual preflight. Rev6 remains seven pages with no target-style layout regression; dedicated CI now generates/compiles Rev6. The current connector does not expose the relevant branch-push Actions run, so direct remote-job inspection is not claimed.

**First target: PRX Quantum — Research Article.**

**Preferred fallback: Physical Review A — Regular Article.**

PRL is a stretch only after a deliberate Letter rewrite.

# Remaining gate

All remaining blockers are human submission/compliance items, not scientific research:

- personally verify the AI-assisted research/manuscript work sufficiently to make a truthful APS AI disclosure;
- final author order and affiliation(s);
- contact email and optional ORCID(s);
- funding/conflict/submission-history facts;
- preprint/e-print decision;
- stable repository/archive citation for Data Availability;
- optional referee recommendations/exclusions;
- PRX Quantum APC coverage/institutional agreement.

APS's June 2026 policy requires disclosure of substantive AI use for this project. Do not invent human verification or administrative facts.

## Replacement-agent recovery

Switch to `agent/temporal-information-resource-law`, then read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV6_PRXQ_PACKAGING_PREFLIGHT_2026-08-22.md`
3. `grand_challenge/submission/PRX_QUANTUM_TARGET_AND_CHECKLIST_2026-08-22.md`
4. `grand_challenge/submission/APS_AI_AND_DATA_DISCLOSURE_DRAFTS.md`
5. `docs/CURRENT_RESEARCH_STATE.md`
6. `ROADMAP.md`

## Documentation policy

`main` must always advertise the active branch and current checkpoint. Detailed derivations remain on the active branch.