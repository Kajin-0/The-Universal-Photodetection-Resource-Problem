# Grand Challenge — Temporal Information Resource Law

**Science frontier: WP27 — 2026-08-22**

**Preferred PRX Quantum manuscript: Rev10 — frozen.**

Working title: **Spectral Resource Laws for Temporal Fisher Information**.

## Grand question

> For a physically realizable measurement of temporal structure, what fundamental resources constrain source-to-record temporal Fisher-information transfer?

## Finite-copy modewise theorem

For exact periodic random-time encoding with sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

For any finite `N` and any joint POVM,

`Tr F_N^(k) <= N min(D_k,U_k) <= N T_k`.

Hence

`R_N(k)=Tr F_N^(k)/N <= T_k`,

`sum_(k>=1)R_N(k) <= nbar`.

This includes arbitrary finite-copy entangled collective measurements.

## Controlled periodic-to-continuum survival law

`R(nu)<=Pr(Omega>=nu)`.

`Omega` is excess generator frequency above the participating lower edge, and `Ebar+=hbar<Omega>`. The area law and pointwise `hfR` relation are first-moment corollaries.

## One fixed measurement: cross-frequency resource law

For **one fixed one-copy POVM**,

`R_M(k)=int cos(k theta)J_M(dtheta)`.

Therefore every Toeplitz matrix `[R_M(i-j)]` is positive semidefinite. A single detector record cannot retain independently chosen amounts of Fisher information at different harmonics.

Combining this Herglotz consistency with the spectral tails gives

`Ebar+>=hbar nu A(R)`,

with

`A(R)~1/sqrt(2(1-R))` as `R->1`.

Exact unit retention at a nonzero harmonic is impossible for a normalized semibounded source. The continuum Herglotz extension invokes Bochner only when the controlled normalized positive-definite limit is continuous at the origin.

## Sharp near-lossless exponent

For the finite sine profile

`a_n=sqrt(2/(L+1))sin((n+1)pi/(L+1))`,

canonical phase measurement gives

`R_L(1)=cos^2(pi/(L+1))`,

`nbar_L=(L-1)/2`.

Hence

`nbar_L~pi/[2sqrt(1-R_L(1))]`.

The `(1-R)^(-1/2)` divergence exponent is therefore sharp. The optimal asymptotic prefactor is not claimed. Finite sine states are established phase-estimation prior art; their role here is only to witness achievability of the new retention--energy scaling.

## Complete one-copy extremizers

On the full contiguous pure-sector chain with positive populations:

`first-harmonic saturation`

`<=> geometric-mixture populations`

`<=> Hausdorff-moment survival tails`

`<=> one common source-adapted POVM saturates every harmonic simultaneously`.

Controlled continuum limits of exponential mixtures produce the completely monotone equality cone, including algebraic exact-retention laws.

## Nonextremal physical example

A transform-limited truncated-Gaussian single photon reaches about 96.6% of the survival ceiling at `nu=0.5 sigma` and 88.5% at `nu=sigma` under canonical covariant timing.

## Source-to-record scope and no-go

Independent quantum-marked Poisson events inherit the modewise law through arbitrary **parameter-independent** field formation and detector processing by POVM pullback.

Arbitrary parameter-dependent waveform-state synthesis remains outside the theorem. The coherent-sideband counterexample shows why baseline mean energy alone cannot bound that broader class.

## Prior-art boundary

Do not claim novelty for `U(1)` mode decomposition or weighted twirling, Herglotz/Bochner theory, Hausdorff/Bernstein moment theory, canonical phase POVMs, geometric/exponential mixtures, finite sine states, generic QFI/Holevo machinery, or generic Poisson/CPTP processing.

The candidate contribution is the operational synthesis: arbitrary-POVM Fisher-tail coefficients, common-measurement positive-definite retention geometry, semibounded near-lossless divergence with sharp exponent, complete one-copy equality classification, and source-to-record inheritance.

**Priority remains unverified, not certified.**

## Rev10 preflight

- full LaTeX/BibTeX build: **PASS**;
- **11 pages**;
- PDF size: **444,063 bytes**;
- unresolved citations/references: **0**;
- overfull boxes: **0**;
- all 11 pages rendered at 200 dpi and inspected: **PASS**;
- sine-profile sharpness validator: **PASS**;
- PDF SHA-256: `a5c2d9e12bba045b76bbfb710428e5424e2c5cb5eb83d6aec6215a5996dbc6fb`;
- source ZIP SHA-256: `cfa2452f9ce4e99d0cd56f931151f6bb166fd90d4332d86faf3ea2485dec1db9`.

## Read first

1. `AGENTS.md`
2. `notes/MANUSCRIPT_REV10_REFEREE_CLOSURE_PREFLIGHT_2026-08-22.md`
3. `notes/WP27_SHARP_HIGH_RETENTION_EXPONENT_AND_REV10_REFEREE_CLOSURE.md`
4. `notes/WP26_HERGLOTZ_COMMON_MEASUREMENT_RETENTION.md`
5. `notes/WP25_COMPLETE_MONOTONE_SATURATION_CLASSIFICATION.md`
6. `notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
7. `notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
8. `notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
9. `notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`

## Journal target

**First target:** PRX Quantum — Research Article.

**Fallback:** Physical Review A — Regular Article.

## Current work order

**Freeze Rev10.** Do not optimize the asymptotic prefactor, add more theory/examples, or broaden the source class by default. Reopen only for a concrete theorem defect, priority collision, build/journal-format issue, or new referee-level objection.

Do not reintroduce “human verification” as a research/manuscript gate. The finished package is handed to a human for submission; unknown administrative facts remain placeholders rather than being invented.
