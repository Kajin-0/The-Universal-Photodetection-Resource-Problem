# Current Research State

**Last synchronized:** 2026-08-22

**Default branch role:** landing/index only.

**Active scientific branch:** `agent/temporal-information-resource-law`

Paper 1 Rev11 and Paper 2 Rev7 are frozen. Grand Challenge science checkpoint: **WP24**. **Rev4 freezes the science content; Rev5 is the preferred frozen publication draft.**

## Replacement-agent recovery

Switch to `agent/temporal-information-resource-law`, then read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV5_PUBLICATION_PREFLIGHT_2026-08-22.md`
3. `grand_challenge/notes/MANUSCRIPT_REV4_LOCAL_BUILD_AND_HOSTILE_REVIEW_2026-08-22.md`
4. `grand_challenge/notes/MANUSCRIPT_REV4_BIBLIOGRAPHY_PROVENANCE_AUDIT_2026-08-22.md`
5. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
6. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
7. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
8. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`
9. active-branch `ROADMAP.md`.

# Strongest current theorem

For the exact periodic random-time model with sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

For any finite `N` and **any joint POVM**,

`Tr F_N^(k)<=N min(D_k,U_k)<=N T_k`.

Thus

`R_N(k)=Tr F_N^(k)/N<=T_k`,

and

`sum_(k>=1)R_N(k)<=nbar`.

`R_N(k)` is the two-quadrature / phase-averaged source-normalized retention. WP20 proves the result directly for arbitrary finite-copy collective measurements.

# Controlled continuum form

For a positive excitation-frequency spectral probability measure `mu` with finite mean, controlled large-period limits of exact periodic approximants satisfy

`R(nu)<=mu([nu,infinity))`.

Consequently

`int_R R(nu)dnu<=2Ebar^+/hbar`,

and

`Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

The geometric/exponential canonical phase-time family attains the bound exactly.

# Source-to-field scope

WP23 extends the same normalized theorem to an independent quantum-marked compound-Poisson event source followed by arbitrary parameter-independent physical source-to-bosonic-field dynamics, wavepacket overlap, coherent detector memory, ancillas, and final measurement.

This is not a theorem for every source with Poisson count statistics.

# Secondary QFI envelope

WP10/WP12/WP15 remain correct as separately optimized SLD-QFI metric bounds:

`sum_(k>=1)G_Q(k)<=2nbar`,

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

They are secondary to the sharp operational `2E/hbar` law. WP16 records the classical Hardy--Hilbert provenance of the `pi/4` analytic constant.

# Scope and prior-art boundaries

WP14 excludes arbitrary coherent waveform synthesis based only on baseline energy.

Weighted `U(1)` twirling/gap modes, canonical phase measurements, energy-constrained phase estimation, arbitrary collective Fisher/Holevo bounds, random-unitary estimation, waveform QFI, positive-frequency sharp inequalities, and Hardy--Hilbert mathematics are prior art.

The candidate contribution is narrowly the **operational classical-Fisher tail/survival law** for perturbations of the latent random-time mixing distribution and its sharp mean-energy/source-to-record consequences.

Targeted searches have not located an exact predecessor. **Priority remains unverified, not certified.**

# Preferred publication draft — Rev5

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

Rev4 is the frozen science/claim checkpoint. Rev5 adds only one conceptual two-column architecture figure and hidden hyperlink decorations.

Rev5 on the active branch has passed:

- full local LaTeX/BibTeX build;
- seven-page visual inspection;
- unresolved-reference/citation and overfull-box gates;
- Figure 1 readability/scope-value review;
- deterministic random-POVM numerical checks;
- DOI/title/provenance bibliography audit.

The branch-push GitHub Actions job is not exposed by the current connector, so remote-job inspection is not claimed. Equivalent full local build verification is complete.

**Rev5 is frozen unless a concrete theorem, priority, build, or referee-level defect is found.**

## Immediate next action

No new theorem accumulation by default. Continue with **journal targeting and submission engineering**, conservative priority language, and factual submission metadata only.

## Documentation requirement

Every project-level state change must be reflected both on the active branch and in these default-branch landing documents.