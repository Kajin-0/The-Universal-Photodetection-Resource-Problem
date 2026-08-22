# The Universal Photodetection Resource Problem

**Current status: 2026-08-22**

`main` is the landing/index branch. Detailed Grand Challenge derivations and manuscript generation live on `agent/temporal-information-resource-law`.

## Project split

1. **Paper 1 / Rev11** — frozen.
2. **Paper 2 / Rev7** — frozen.
3. **Grand Challenge** — science frontier **WP27**; Rev10 referee-closure manuscript in final build gate.

Authoritative handoff: active-branch `grand_challenge/AGENTS.md`.

# Grand Challenge headline

For exact periodic random-time encoding, any finite-copy joint POVM obeys

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`,

where `T_k=sum_(m>=k)q_m`.

Controlled periodic-to-continuum limits give

`R(nu) <= Pr(Omega>=nu)`,

with `Ebar+=hbar<Omega>` the mean excess energy above the participating lower edge.

## One physical measurement imposes cross-frequency structure

For **one fixed one-copy POVM**, the entire retention sequence has a Herglotz representation

`R_M(k)=int cos(k theta) J_M(dtheta)`,

so every Toeplitz matrix `[R_M(i-j)]` is positive semidefinite.

Combining this spectral consistency with the energy tails gives

`Ebar+ >= hbar nu A(R_M(nu))`,

with

`A(q) ~ 1/sqrt(2(1-q))` as `q->1`.

Thus near-unit retention at nonzero frequency requires divergent mean excess energy in the fixed-one-copy/common-measurement setting.

Rev10 proves that this exponent is **sharp**: the finite sine-profile family

`a_n=sqrt(2/(L+1)) sin((n+1)pi/(L+1))`

under canonical phase measurement has

`R_L(1)=cos^2(pi/(L+1))`,

`nbar_L=(L-1)/2`,

hence

`nbar_L ~ pi/[2 sqrt(1-R_L(1))]`.

The optimal asymptotic constant is not claimed.

## Complete one-copy extremizers

On the full contiguous pure-sector chain:

`first-harmonic equality`

`<=> geometric-mixture populations`

`<=> Hausdorff-moment survival tails`

`<=> one common source-adapted POVM saturates every harmonic simultaneously`.

Controlled continuum limits of exponential mixtures give the completely monotone equality cone.

## Scope

The finite-copy tail theorem allows arbitrary finite-copy entangled collective measurements. The Herglotz/divergence theorem is specifically a **fixed one-copy common-POVM** statement.

For the continuum Herglotz extension, Bochner is invoked only after continuity at the origin is assumed.

Independent quantum-marked Poisson sources inherit the modewise survival law through arbitrary **parameter-independent** source-to-field and detector processing. Arbitrary parameter-dependent waveform synthesis remains outside the theorem and requires additional control-resource accounting.

# Manuscript

Working title: **Spectral Resource Laws for Temporal Fisher Information**.

Rev9 passed a full local 11-page build/render preflight. An external extreme adversarial re-review found no central mathematical failure and rated the manuscript approximately 9.6/10 overall, with PRX Quantum well justified. Rev10 implements the two remaining scope/formal fixes and the review's one high-value optional scientific enhancement: proof that the near-lossless divergence exponent is achievable.

**First target:** PRX Quantum — Research Article.

**Fallback:** Physical Review A — Regular Article.

**Priority remains unverified, not certified.**

# Recovery

Switch to `agent/temporal-information-resource-law` and read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP27_SHARP_HIGH_RETENTION_EXPONENT_AND_REV10_REFEREE_CLOSURE.md`
3. `grand_challenge/notes/MANUSCRIPT_REV9_SPECTRAL_RESOURCE_PREFLIGHT_2026-08-22.md`
4. `grand_challenge/notes/WP26_HERGLOTZ_COMMON_MEASUREMENT_RETENTION.md`
5. `grand_challenge/notes/WP25_COMPLETE_MONOTONE_SATURATION_CLASSIFICATION.md`

# Workflow rule

Do not reintroduce “human verification” as a research/manuscript completion gate. The finished package is produced as far as possible and then submitted by a human. Unknown administrative facts remain placeholders rather than being invented.
