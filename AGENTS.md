# AGENTS.md

## Purpose

Durable repository handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

`main` is the landing/index branch. Active derivations and Grand Challenge manuscript generation live on `agent/temporal-information-resource-law`.

Research is analytical/theoretical. Paper 1 Rev11 and Paper 2 Rev7 are frozen.

## Current status

**Grand Challenge science checkpoint: WP24.**

**Rev4 freezes science. Rev5 freezes publication content. Rev6 is the current PRX Quantum style package.**

Mandatory first action for a replacement agent: switch to `agent/temporal-information-resource-law` and read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV6_PRXQ_PACKAGING_PREFLIGHT_2026-08-22.md`
3. `grand_challenge/submission/PRX_QUANTUM_TARGET_AND_CHECKLIST_2026-08-22.md`
4. `grand_challenge/submission/APS_AI_AND_DATA_DISCLOSURE_DRAFTS.md`
5. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
6. `docs/CURRENT_RESEARCH_STATE.md`
7. `ROADMAP.md`

# Strongest theorem

For exact periodic random-time encoding with sector probabilities `q_n`,

`T_k=sum_(m>=k)q_m`,

and any finite number `N` of independently encoded excitations and any joint POVM,

`Tr F_N^(k)<=N min(D_k,U_k)<=N T_k`.

Hence `R_N(k)=Tr F_N^(k)/N<=T_k` and `sum_(k>=1)R_N(k)<=nbar`.

`R_N(k)` is the two-quadrature / phase-averaged source-normalized Fisher retention. Controlled large-period limits obey `R(nu)<=P(Omega>=nu)`, `int_R R<=2Ebar^+/hbar`, and `Ebar^+>=hbar nu R(nu)`.

WP23 extends the source-normalized law to an independent quantum-marked compound-Poisson source under arbitrary parameter-independent bosonic-field/detector processing. WP14 excludes arbitrary parameter-dependent waveform-state synthesis from baseline-energy-only control.

# Priority discipline

Do not claim novelty for weighted `U(1)` twirling, energy-gap modes, canonical phase POVMs, number/energy-constrained phase estimation, generic QFI/Holevo/RLD/SLD bounds, random-unitary estimation, waveform QFI, Hardy--Hilbert/positive-frequency inequalities, or generic Poisson/CPTP machinery.

The candidate contribution is narrowly the operational **classical-Fisher tail/survival law** and its energy/source-to-record consequences. **Priority remains unverified, not certified.**

# Manuscript / target state

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

- Rev4: frozen science content.
- Rev5: frozen publication content; one conceptual figure + hidden links only.
- Rev6: PRX Quantum packaging only; REVTeX `pra -> prx`.

Rev5 passed complete local build/visual/bibliography/numerical preflight. Rev6 remains seven pages and has no target-style layout regression in local reproduction; dedicated CI is configured to compile it. Do not claim direct remote Actions inspection.

**First target: PRX Quantum — Research Article.**

**Fallback: Physical Review A — Regular Article.**

# Human-only blockers

No new theorem work by default. Remaining blockers are:

1. human verification sufficient for truthful APS AI disclosure;
2. author name/order and affiliation(s);
3. contact email and optional ORCID(s);
4. funding/conflict/submission-history facts;
5. preprint/e-print decision;
6. stable repository/archive citation for Data Availability;
7. optional referee recommendations/exclusions;
8. APC coverage/institutional agreement.

APS's June 2026 AI policy requires substantive AI-use disclosure for this project. Never fabricate human verification or administrative facts.

# Documentation discipline

Every material project-status change must update the active branch and then be mirrored onto `main`.