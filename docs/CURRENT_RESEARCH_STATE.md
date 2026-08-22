# Current Research State

**Last synchronized:** 2026-08-22

**Active branch:** `agent/temporal-information-resource-law`

Paper 1 Rev11 and Paper 2 Rev7 are frozen.

**Grand Challenge science frontier:** **WP27**.

**Preferred manuscript:** **Rev10 — Spectral Resource Laws for Temporal Fisher Information**, frozen after full local publication preflight.

## Read first

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV10_REFEREE_CLOSURE_PREFLIGHT_2026-08-22.md`
3. `grand_challenge/notes/WP27_SHARP_HIGH_RETENTION_EXPONENT_AND_REV10_REFEREE_CLOSURE.md`
4. `grand_challenge/notes/WP26_HERGLOTZ_COMMON_MEASUREMENT_RETENTION.md`
5. `grand_challenge/notes/WP25_COMPLETE_MONOTONE_SATURATION_CLASSIFICATION.md`
6. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
7. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
8. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
9. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`

# Result hierarchy

## 1. Finite-copy arbitrary-POVM tail law

For exact periodic random-time encoding,

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`, `T_k=sum_(m>=k)q_m`,

for any finite number of independently encoded copies and any joint POVM, including arbitrary entangled collective measurements.

Consequently `sum_(k>=1)R_N(k)<=nbar`.

## 2. Controlled continuum survival law

For controlled periodic-to-continuum limits,

`R(nu)<=Pr(Omega>=nu)`.

`Ebar+=hbar<Omega>` is excess energy above the participating lower edge. The area law and `hfR` relation are first-moment corollaries, not the headline theorem.

## 3. Fixed one-copy common-measurement spectral consistency

For one fixed one-copy POVM,

`R_M(k)=int cos(k theta)J_M(dtheta)`.

Thus `[R_M(i-j)]` is positive semidefinite for every finite Toeplitz block. Retention at distinct temporal harmonics is globally constrained.

For `q=R_M(nu)`,

`Ebar+>=hbar nu A(q)`,

with

`A(q)~1/sqrt(2(1-q))` as `q->1`.

Therefore near-unit retention requires divergent mean excess energy in this fixed-one-copy/common-POVM setting. For the continuum Herglotz extension, Bochner is invoked only for a normalized positive-definite controlled limit continuous at the origin.

## 4. Sharp divergence exponent

The finite sine-profile family

`a_n=sqrt(2/(L+1))sin((n+1)pi/(L+1))`

under canonical phase measurement has

`R_L(1)=cos^2(pi/(L+1))`, `nbar_L=(L-1)/2`,

so

`nbar_L~pi/[2sqrt(1-R_L(1))]`.

Hence the inverse-square-root divergence exponent is sharp. No globally optimal prefactor is claimed. The sine state is established phase-estimation prior art and is used only as the achievability witness.

## 5. Complete one-copy extremizers

On the full contiguous pure-sector chain with positive populations:

`first-harmonic saturation`

`<=> geometric-mixture populations`

`<=> Hausdorff-moment survival tails`

`<=> one common source-adapted POVM saturates every harmonic simultaneously`.

Controlled continuum limits of exponential mixtures give the completely monotone equality cone, including algebraic exact-retention laws.

## 6. Nonextremal physical relevance

The transform-limited truncated-Gaussian single-photon example remains: canonical covariant timing reaches about 96.6% of the survival ceiling at `nu=0.5 sigma` and 88.5% at `nu=sigma`.

## 7. Source-to-record inheritance and no-go boundary

Independent quantum-marked Poisson sources inherit the modewise tail law through arbitrary parameter-independent field formation and detector processing by POVM pullback.

The coherent-sideband counterexample remains the explicit boundary: arbitrary parameter-dependent waveform-state synthesis cannot be constrained by baseline mean energy alone without accounting for encoding/control resources.

# Prior-art boundary

Do not claim novelty for `U(1)` mode decomposition, weighted twirling, Herglotz/Bochner, Hausdorff/Bernstein moment theory, geometric/exponential mixtures, canonical phase POVMs, sine states, generic QFI/Holevo machinery, or generic Poisson/CPTP processing.

Candidate contribution is the operational combination of Fisher-tail coefficients, common-measurement positive-definite retention geometry, semibounded near-lossless divergence with sharp exponent, complete one-copy saturation classification, and source-to-record inheritance.

**Priority remains unverified, not certified.**

# Rev10 preflight

- full LaTeX/BibTeX build: **PASS**;
- pages: **11**;
- PDF size: **444,063 bytes**;
- PDF SHA-256: `a5c2d9e12bba045b76bbfb710428e5424e2c5cb5eb83d6aec6215a5996dbc6fb`;
- unresolved references/citations: **0**;
- overfull boxes: **0**;
- 11-page 200-dpi visual inspection: **PASS**;
- sine-profile sharpness validator: **PASS**;
- source ZIP SHA-256: `cfa2452f9ce4e99d0cd56f931151f6bb166fd90d4332d86faf3ea2485dec1db9`.

The current connector does not expose the branch-push GitHub Actions run; no remote-run inspection is claimed. The equivalent generation/build/render gate passed locally.

# Target and freeze

**PRX Quantum — Research Article** first; **Physical Review A — Regular Article** fallback.

**Freeze Rev10.** Reopen only for a concrete theorem defect, priority collision, build/journal-format issue, or new referee-level objection. Do not introduce a human-verification research gate.
