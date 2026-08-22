# Grand Challenge — Temporal Information Resource Law

**Science frontier: WP28 — 2026-08-22**

**Preferred PRX Quantum manuscript: Rev11 — frozen.**

Working title: **Spectral Resource Laws for Temporal Fisher Information**.

## Grand question

> For a physically realizable measurement of temporal structure, what fundamental resources constrain source-to-record temporal Fisher-information transfer?

## 1. Exact periodic finite-copy theorem

For exact periodic random-time encoding,

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`

for every finite `N` and arbitrary joint POVM, including entangled collective measurements. Summing gives `sum_(k>=1)R_N(k)<=nbar`.

## 2. Rev11 fixed-Hamiltonian Bohr-gap theorem

The modewise mechanism is **not** restricted to an equally spaced generator. For an arbitrary semibounded pure-point Hamiltonian and requested gap `nu`, long-window random-time averaging selects exact Bohr pairs and gives

`A_nu=rho0^(1/2)V_nu rho0^(1/2)`.

Therefore

`Tr F_N^(nu)/N <= min(D_nu,U_nu) <= Pr(Omega>=nu)`

for arbitrary finite-copy joint measurements. No global equal spacing or commensurability is required.

If there is no exact Bohr pair at `hbar nu`, the limiting local Fisher response at that frequency is zero.

## 3. Controlled continuum survival law

`R(nu)<=Pr(Omega>=nu)`.

The spectral measure is an arbitrary Borel probability measure with finite first moment; atomic, absolutely continuous, singular-continuous, and mixed components are allowed. The controlled hypothesis concerns convergence of the physical measurement/source limit, not smoothness of the spectrum.

`Ebar+=hbar<Omega>` is excess energy above the participating lower edge. The area and `hfR` inequalities are first-moment corollaries.

## 4. One fixed measurement: cross-frequency law

For one fixed one-copy POVM, the retention sequence is positive definite:

`R_M(k)=int cos(k theta)J_M(dtheta)`.

Zero-population completion cannot create Fisher information. For an arbitrary pure-point Hamiltonian the same construction applies across exact multiples of a chosen Bohr gap.

Combining Herglotz consistency with semibounded energy tails gives

`Ebar+>=hbar nu A(R)`,

with `A(R)~1/sqrt(2(1-R))` as `R->1`.

A finite sine-profile family proves that the `(1-R)^(-1/2)` divergence exponent is **sharp**. The optimal prefactor is not claimed.

## 5. Complete one-copy extremizers

The converse remains restricted to the full contiguous pure-sector chain:

`first-harmonic equality`

`<=> geometric-mixture populations`

`<=> Hausdorff-moment tails`

`<=> one source-adapted POVM saturates every harmonic simultaneously`.

Controlled exponential-mixture limits give the completely monotone continuum equality cone.

## 6. Physical relevance and boundary

A transform-limited truncated-Gaussian single photon reaches about 96.6% of the survival ceiling at `0.5 sigma` and 88.5% at `sigma` under canonical covariant timing.

Independent quantum-marked Poisson sources inherit the modewise ceiling through arbitrary parameter-independent source-to-field and detector processing.

Arbitrary parameter-dependent waveform-state synthesis remains outside the theorem; the coherent-sideband no-go shows why extra encoding/control resources must be included there.

## Prior-art boundary

Arbitrary Bohr-frequency / `U(1)` mode decomposition, random-time dephasing, Herglotz/Bochner theory, Hausdorff/Bernstein theory, phase POVMs, finite sine states, and generic QFI/CPTP machinery are prior art.

The candidate contribution is the operational synthesis: arbitrary-POVM Fisher-tail coefficients, their exact-Bohr-gap extension, common-measurement positive-definite retention geometry, sharp near-lossless energy divergence, complete one-copy equality classification in the contiguous model, and source-to-record inheritance.

**Priority remains unverified, not certified.**

## Rev11 preflight

- full LaTeX/BibTeX build: **PASS**;
- **12 pages**;
- PDF size: **452,384 bytes**;
- unresolved citations/references: **0**;
- overfull boxes: **0**;
- all 12 pages rendered at 200 dpi and inspected: **PASS**;
- all six numerical validators: **PASS**;
- PDF SHA-256: `5e0ac0132a7f4a3f7b07e9c4ba86b046b23bc89c1f7635efe9f737019396d0f0`;
- source ZIP SHA-256: `208fd7a2e932507366797658c84dff1666257477143a433bf81d7741a8d0c8a1`;
- fresh source-package compile: **PASS**;
- 200-dpi render diff against fresh compile: **0 changed pixels on all 12 pages**.

## Read first

1. `AGENTS.md`
2. `notes/MANUSCRIPT_REV11_ANHARMONIC_PREFLIGHT_2026-08-22.md`
3. `notes/WP28_ANHARMONIC_PURE_POINT_GAP_EXTENSION_AND_CONTINUUM_ATTACK.md`
4. `notes/MANUSCRIPT_REV10_REFEREE_CLOSURE_PREFLIGHT_2026-08-22.md`
5. `notes/WP27_SHARP_HIGH_RETENTION_EXPONENT_AND_REV10_REFEREE_CLOSURE.md`
6. `notes/WP26_HERGLOTZ_COMMON_MEASUREMENT_RETENTION.md`
7. `notes/WP25_COMPLETE_MONOTONE_SATURATION_CLASSIFICATION.md`

## Journal target

**First target:** PRX Quantum — Research Article.

**Fallback:** Physical Review A — Regular Article.

## Current work order

**Freeze Rev11.** Reopen only for a concrete theorem defect, priority collision, substantive referee objection, build/render regression, or unavoidable journal-format issue.

Do not reintroduce “human verification” as a research/manuscript gate. The finished package is handed to a human for submission; unknown administrative facts remain placeholders.
