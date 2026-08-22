# Current Research State

**Last synchronized:** 2026-08-22

**Default branch role:** landing/index only.

**Active scientific branch:** `agent/temporal-information-resource-law`

Paper 1 Rev11 and Paper 2 Rev7 are frozen.

**Grand Challenge science checkpoint:** WP24.

**Rev4:** frozen science content.

**Rev5:** frozen publication content.

**Rev6:** current PRX Quantum style package.

## Recovery order

Switch to `agent/temporal-information-resource-law`, then read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV6_PRXQ_PACKAGING_PREFLIGHT_2026-08-22.md`
3. `grand_challenge/submission/PRX_QUANTUM_TARGET_AND_CHECKLIST_2026-08-22.md`
4. `grand_challenge/submission/APS_AI_AND_DATA_DISCLOSURE_DRAFTS.md`
5. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
6. active-branch `docs/CURRENT_RESEARCH_STATE.md`
7. active-branch `ROADMAP.md`.

# Current theorem

For exact periodic random-time encoding with sector probabilities `q_n`, define `T_k=sum_(m>=k)q_m`. Any finite number `N` of independently encoded excitations and any joint POVM obey

`Tr F_N^(k)<=N min(D_k,U_k)<=N T_k`.

Hence

`R_N(k)=Tr F_N^(k)/N<=T_k`,

`sum_(k>=1)R_N(k)<=nbar`.

`R_N(k)` is the two-quadrature / phase-averaged source-normalized Fisher retention.

Controlled large-period limits satisfy

`R(nu)<=P(Omega>=nu)`,

`int_R R(nu)dnu<=2Ebar^+/hbar`,

`Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

WP23 provides the independent compound-Poisson source-to-field embedding. WP14 retains the arbitrary-waveform no-go boundary.

# Priority

The candidate contribution is the operational **classical-Fisher tail/survival theorem** for Fourier perturbations of the latent random-time distribution and its paired-population/energy/source-to-record consequences. Generic `U(1)` modes/twirling, phase estimation, quantum-information bounds, waveform QFI, Hardy--Hilbert analysis, and generic Poisson/CPTP machinery are prior art.

**Priority remains unverified, not certified.**

# Manuscript / journal package

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

- Rev4 freezes scientific content.
- Rev5 freezes publication content and adds one conceptual architecture figure only.
- Rev6 changes only the REVTeX journal option from `pra` to `prx` for the current target.

Rev5 passed complete local build, visual, numerical, figure, and bibliography preflight. Rev6 remains seven pages with no target-style page-flow regression in local reproduction; dedicated CI is configured to generate/compile Rev6. The current connector does not expose the branch-push Actions run, so direct remote-job inspection is not claimed.

# Journal target

**First target:** PRX Quantum, Research Article.

**Fallback:** Physical Review A, Regular Article.

PRL is a stretch only after a deliberate Letter rewrite.

# Remaining blockers

Scientific work is frozen. Remaining work is human submission completion:

- human verification for APS substantive AI-use disclosure;
- final author/order/affiliation/contact details;
- optional ORCID;
- funding/conflict/submission-history facts;
- preprint/e-print decision;
- stable repository/archive citation for Data Availability;
- optional referee recommendations/exclusions;
- APC coverage/institutional agreement.

Do not invent these facts.

## Documentation requirement

Every project-level status change must be reflected both on the active branch and `main`.