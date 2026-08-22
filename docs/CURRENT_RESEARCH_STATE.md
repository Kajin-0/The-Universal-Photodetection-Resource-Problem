# Current Research State

**Last synchronized:** 2026-08-22

**Active branch:** `agent/temporal-information-resource-law`

Paper 1 Rev11 and Paper 2 Rev7 are frozen.

**Grand Challenge science frontier:** **WP28**.

**Preferred manuscript:** **Rev11 — Spectral Resource Laws for Temporal Fisher Information**, frozen after full local publication preflight.

## Read first

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV11_ANHARMONIC_PREFLIGHT_2026-08-22.md`
3. `grand_challenge/notes/WP28_ANHARMONIC_PURE_POINT_GAP_EXTENSION_AND_CONTINUUM_ATTACK.md`
4. `grand_challenge/notes/MANUSCRIPT_REV10_REFEREE_CLOSURE_PREFLIGHT_2026-08-22.md`
5. `grand_challenge/notes/WP27_SHARP_HIGH_RETENTION_EXPONENT_AND_REV10_REFEREE_CLOSURE.md`
6. `grand_challenge/notes/WP26_HERGLOTZ_COMMON_MEASUREMENT_RETENTION.md`
7. `grand_challenge/notes/WP25_COMPLETE_MONOTONE_SATURATION_CLASSIFICATION.md`

# Result hierarchy

## 1. Exact periodic finite-copy arbitrary-POVM law

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`

for any finite number of independently encoded copies and any joint POVM, including arbitrary entangled collective measurements.

## 2. Fixed-Hamiltonian arbitrary-Bohr-gap extension

For an arbitrary semibounded pure-point Hamiltonian, no equal-spacing or commensurability assumption is needed. Long-window random-time averaging at requested modulation `nu` selects exact Bohr pairs and gives

`A_nu=rho0^(1/2)V_nu rho0^(1/2)`.

Hence

`Tr F_N^(nu)/N <= min(D_nu,U_nu) <= S(nu)=Pr(Omega>=nu)`

for every finite `N` and arbitrary joint POVM.

If no exact pair has gap `hbar nu`, the limiting local Fisher response at that gap is zero.

## 3. Controlled continuum survival law

`R(nu)<=Pr(Omega>=nu)`.

The spectral measure is an arbitrary Borel probability measure with finite first moment. No density or smoothness is required; singular-continuous components are allowed.

`Ebar+=hbar<Omega>` is excess energy above the participating lower edge. The area law and `hfR` relation are first-moment corollaries.

## 4. Fixed one-copy common-measurement spectral consistency

For one fixed one-copy POVM,

`R_M(k)=int cos(k theta)J_M(dtheta)`.

Thus every finite Toeplitz block `[R_M(i-j)]` is PSD. Zero-population completion cannot create Fisher information.

For an arbitrary pure-point Hamiltonian the same structure applies across exact multiples `m nu` of a chosen Bohr gap. Combining it with the energy tails gives

`Ebar+>=hbar nu A(q)`,

`A(q)~1/sqrt(2(1-q))` as `q->1`.

For the continuum Herglotz extension, Bochner is invoked only for a normalized positive-definite limit continuous at the origin.

## 5. Sharp near-lossless exponent

The finite sine-profile family under canonical phase measurement has

`R_L(1)=cos^2(pi/(L+1))`, `nbar_L=(L-1)/2`,

so

`nbar_L~pi/[2sqrt(1-R_L(1))]`.

Therefore the inverse-square-root divergence exponent is sharp. No optimal prefactor is claimed.

## 6. Complete one-copy extremizers

The converse remains restricted to the full contiguous pure-sector chain:

`first-harmonic saturation`

`<=> geometric-mixture populations`

`<=> Hausdorff-moment tails`

`<=> one common source-adapted POVM saturates every harmonic simultaneously`.

Controlled exponential-mixture limits give the completely monotone equality cone.

## 7. Physical relevance and source-to-record inheritance

A transform-limited truncated-Gaussian single photon reaches about 96.6% of the survival ceiling at `0.5 sigma` and 88.5% at `sigma` under canonical covariant timing.

Independent quantum-marked Poisson sources inherit the modewise ceiling through arbitrary parameter-independent field formation and detector processing by POVM pullback.

The coherent-sideband counterexample remains the explicit boundary: arbitrary parameter-dependent waveform-state synthesis requires additional encoding/control resource accounting.

# Prior-art boundary

Arbitrary Bohr-frequency / `U(1)` mode decompositions, random-time dephasing, Herglotz/Bochner, Hausdorff/Bernstein theory, geometric/exponential mixtures, phase POVMs, sine states, and generic QFI/Holevo/CPTP machinery are prior art.

Candidate contribution: arbitrary-POVM Fisher-tail coefficients, their arbitrary-pure-point exact-Bohr-gap extension, common-measurement positive-definite retention geometry, sharp near-lossless divergence, complete one-copy saturation classification in the contiguous model, and source-to-record inheritance.

**Priority remains unverified, not certified.**

# Rev11 preflight

- full LaTeX/BibTeX build: **PASS**;
- pages: **12**;
- PDF size: **452,384 bytes**;
- PDF SHA-256: `5e0ac0132a7f4a3f7b07e9c4ba86b046b23bc89c1f7635efe9f737019396d0f0`;
- unresolved references/citations: **0**;
- overfull boxes: **0**;
- 12-page 200-dpi visual inspection: **PASS**;
- all six numerical validators: **PASS**;
- source ZIP SHA-256: `208fd7a2e932507366797658c84dff1666257477143a433bf81d7741a8d0c8a1`;
- fresh source-package compile: **PASS**;
- original/fresh 200-dpi render comparison: **pixel-identical on all 12 pages**.

The current connector does not expose the relevant branch-push GitHub Actions run; no remote-run result is claimed.

# Target and freeze

**PRX Quantum — Research Article** first; **Physical Review A — Regular Article** fallback.

**Freeze Rev11.** Reopen only for a concrete theorem defect, priority collision, substantive referee objection, build/render regression, or unavoidable journal-format issue. Do not introduce a human-verification research gate.
