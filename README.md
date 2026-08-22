# The Universal Photodetection Resource Problem

**Status synchronized: 2026-08-22**

## Project split

1. **Paper 1 / Rev11** — frozen and technically validated.
2. **Paper 2 / Rev7** — frozen preferred science draft.
3. **Grand Challenge** — science checkpoint **WP24**; preferred publication draft **Rev5**, frozen unless a concrete defect appears.

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

# Preferred Grand Challenge manuscript — Rev5

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

Deterministic generation:

`Rev1 -> Rev2 -> Rev3 -> Rev4 -> Rev5`.

Rev5 adds only one conceptual architecture figure and `hidelinks` to the frozen Rev4 science.

Final Rev5 preflight:

- full local LaTeX/BibTeX build: PASS;
- pages: **7**;
- final local PDF: **393,530 bytes**;
- unresolved citations/references: **0**;
- overfull boxes: **0**;
- undefined controls/fatal errors: **0**;
- all seven pages rendered at 160 dpi and visually inspected: PASS;
- Figure 1 readable and materially useful without increasing page count;
- visible hyperlink boxes: **0**;
- bibliography page: PASS;
- deterministic random-POVM theorem validation committed;
- DOI/title/provenance bibliography audit completed.

Figure 1 shows the source-class/theorem architecture: latent random-time law -> fixed excitation -> arbitrary parameter-independent field/detector channel -> accessible record, with the survival-tail/energy ceiling and the excluded arbitrary waveform-synthesis class.

The current connector does not expose the relevant branch-push GitHub Actions run. Direct remote-job inspection is therefore not claimed; equivalent full local build verification is complete.

**Rev5 is frozen unless a concrete theorem, priority, build/rendering, referee, or factual-submission defect appears.**

## Read first

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV5_PUBLICATION_PREFLIGHT_2026-08-22.md`
3. `grand_challenge/notes/MANUSCRIPT_REV4_LOCAL_BUILD_AND_HOSTILE_REVIEW_2026-08-22.md`
4. `grand_challenge/notes/MANUSCRIPT_REV4_BIBLIOGRAPHY_PROVENANCE_AUDIT_2026-08-22.md`
5. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
6. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
7. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
8. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`

## Current work order

Do not accumulate another theorem or polish revision by default. Proceed with journal targeting/submission engineering, conservative priority language, remote CI inspection only if accessible, and factual submission metadata when supplied.

## Documentation discipline

Every material result/status change must be recorded in the repository and mirrored onto `main`; do not rely on chat history.
