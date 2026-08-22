# Current Research State

**Last synchronized:** 2026-08-22

**Active scientific branch:** `agent/temporal-information-resource-law`

Paper 1 Rev11 and Paper 2 Rev7 are frozen.

**Grand Challenge science checkpoint:** WP24.

**Science freeze:** Rev4.

**Publication-content freeze:** Rev5.

**Current journal package:** Rev6 PRX Quantum style package.

## Read first

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV6_PRXQ_PACKAGING_PREFLIGHT_2026-08-22.md`
3. `grand_challenge/submission/PRX_QUANTUM_TARGET_AND_CHECKLIST_2026-08-22.md`
4. `grand_challenge/submission/APS_AI_AND_DATA_DISCLOSURE_DRAFTS.md`
5. `grand_challenge/notes/MANUSCRIPT_REV5_PUBLICATION_PREFLIGHT_2026-08-22.md`
6. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
7. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
8. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
9. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`

# Strongest theorem

For exact periodic random-time encoding with sector probabilities `q_n`, harmonic `k`, and tail

`T_k=sum_(m>=k)q_m`,

any finite number `N` of independently encoded excitations and any joint POVM obey

`Tr F_N^(k)<=N min(D_k,U_k)<=N T_k`.

Thus

`R_N(k)=Tr F_N^(k)/N<=T_k`,

`sum_(k>=1)R_N(k)<=nbar`.

`R_N(k)` is the two-quadrature / phase-averaged source-normalized Fisher retention. The theorem includes arbitrary finite-copy entangled collective measurements.

# Controlled continuum theorem

For a positive excitation-frequency probability measure `mu` with finite first moment, controlled large-period limits of exact lower-bin periodic approximants satisfy

`R(nu)<=mu([nu,infinity))`.

Therefore

`int_R R(nu)dnu<=2Ebar^+/hbar`,

`Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

Do not remove the controlled-limit qualification.

# Equality / field embedding / scope

Geometric sector populations with the canonical phase POVM saturate every discrete harmonic simultaneously. The controlled continuum equality family is exponential-energy/Cauchy-time.

WP23 transfers the bound to an independent quantum-marked compound-Poisson source followed by arbitrary parameter-independent source-to-bosonic-field and detector processing through POVM pullback.

WP14 blocks extension to arbitrary parameter-dependent coherent waveform synthesis using baseline mean energy alone.

# Secondary QFI envelope

WP10/WP12/WP15 remain correct but secondary:

`sum_(k>=1)G_Q(k)<=2nbar`,

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

WP16 identifies the `pi/4` continuum analytic constant as established Hardy--Hilbert mathematics.

# Priority status

Weighted `U(1)` twirling/modes, canonical phase POVMs, number-constrained phase estimation, generic QFI/Holevo/RLD/SLD bounds, random-unitary estimation, waveform QFI, positive-frequency inequalities, Hardy--Hilbert mathematics, and generic Poisson/CPTP machinery are prior art.

The candidate contribution is the arbitrary-measurement **classical-Fisher tail/survival theorem** for Fourier perturbations of a latent random-time distribution and its paired-population/mean-energy/source-to-record consequences.

**Priority remains unverified, not certified.**

# Manuscript and target status

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

`Rev1 -> Rev2 -> Rev3 -> Rev4 -> Rev5 -> Rev6 PRX Quantum package`.

- Rev4: frozen science/claim content.
- Rev5: publication content; one conceptual figure plus hidden hyperlinks only.
- Rev6: target style only, `pra -> prx` REVTeX option.

Rev5 complete local build/visual/reference preflight: PASS.

Rev6 PRX target-style preflight: PASS. Pages remain 7; no target-style layout regression; dedicated CI compiles Rev6; fresh numerical check sampled 11,825 one-copy and 936 global two-copy POVMs with no violation, and the equality family matched at machine precision.

# Journal target

1. **PRX Quantum — Research Article:** first target.
2. **Physical Review A — Regular Article:** preferred fallback.
3. Physical Review Research: secondary alternative.
4. PRL: stretch only after a deliberate Letter rewrite.

PRX Quantum is fully open access; APS lists a 2026 APC of USD 3,590, subject to institutional agreements/eligible waivers.

# APS compliance

The June 2026 APS AI policy requires disclosure of substantive AI use. This project used AI substantively; final submission requires truthful human verification and disclosure. See `grand_challenge/submission/APS_AI_AND_DATA_DISCLOSURE_DRAFTS.md`.

Data Availability should state that no experimental data were created while citing a stable public source for numerical-validation and manuscript/figure code.

# Remaining blockers

All remaining blockers are human/administrative rather than scientific:

- human verification for APS AI disclosure;
- author name/order and affiliation(s);
- contact email and optional ORCID(s);
- funding/conflict/submission-history facts;
- preprint identifier if used;
- stable repository/archive citation;
- optional referee recommendations/exclusions;
- APC coverage decision.

After these are supplied: generate final administrative Rev6 package, rebuild once, inspect every page, and submit to PRX Quantum.

## Documentation rule

Every material status change must update the detailed note, active landing/handoff files, and `main`. The repository—not chat history—is authoritative.