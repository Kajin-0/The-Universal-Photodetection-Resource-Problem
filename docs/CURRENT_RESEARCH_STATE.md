# Current Research State

**Last synchronized:** 2026-08-22

`main` is landing/index only.

**Active branch:** `agent/temporal-information-resource-law`

- Paper 1 Rev11: frozen.
- Paper 2 Rev7: frozen.
- Grand Challenge science frontier: **WP27**.
- Preferred Grand Challenge manuscript: **Rev10 — Spectral Resource Laws for Temporal Fisher Information**, frozen.

## Recovery

Switch to `agent/temporal-information-resource-law` and read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV10_REFEREE_CLOSURE_PREFLIGHT_2026-08-22.md`
3. `grand_challenge/notes/WP27_SHARP_HIGH_RETENTION_EXPONENT_AND_REV10_REFEREE_CLOSURE.md`
4. `grand_challenge/notes/WP26_HERGLOTZ_COMMON_MEASUREMENT_RETENTION.md`
5. `grand_challenge/notes/WP25_COMPLETE_MONOTONE_SATURATION_CLASSIFICATION.md`

## Current theorem hierarchy

### Finite-copy modewise law

For any finite number of independently encoded copies and any joint POVM,

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`.

### Controlled continuum survival law

`R(nu)<=Pr(Omega>=nu)`,

with `Ebar+=hbar<Omega>` the mean excess energy above the participating lower edge.

### Fixed-one-copy common-measurement law

For one fixed one-copy POVM,

`R_M(k)=int cos(k theta)J_M(dtheta)`.

Hence the retention sequence is positive definite and its Toeplitz matrices are PSD. Combining this with the energy tails gives

`Ebar+>=hbar nu A(R)`,

`A(R)~1/sqrt(2(1-R))` as `R->1`.

### Sharp exponent

The finite sine-profile family under canonical phase measurement has

`R_L(1)=cos^2(pi/(L+1))`, `nbar_L=(L-1)/2`,

so `nbar_L~pi/[2sqrt(1-R_L(1))]`. The inverse-square-root divergence exponent is therefore sharp; the optimal prefactor is not claimed.

### Complete one-copy extremizers

On the full contiguous pure-sector chain:

`first-harmonic equality`

`<=> geometric-mixture populations`

`<=> Hausdorff-moment tails`

`<=> one common source-adapted POVM saturates every harmonic simultaneously`.

Controlled exponential mixtures give the completely monotone continuum equality cone.

## Scope discipline

The finite-copy tail theorem includes arbitrary entangled collective POVMs. The Herglotz/divergence theorem is specifically a **fixed one-copy common-POVM** result. The continuum Herglotz extension invokes Bochner only when the controlled positive-definite limit is continuous at the origin.

Arbitrary parameter-dependent waveform-state synthesis remains outside the theorem; the coherent-sideband no-go demonstrates why additional encoding/control resources are required.

## Rev10 publication preflight

- 11 pages;
- full LaTeX/BibTeX build: **PASS**;
- unresolved references/citations: **0**;
- overfull boxes: **0**;
- all pages rendered at 200 dpi and visually inspected: **PASS**;
- sine-profile sharpness validator: **PASS**;
- PDF SHA-256: `a5c2d9e12bba045b76bbfb710428e5424e2c5cb5eb83d6aec6215a5996dbc6fb`.

The current connector does not expose branch-push Actions runs; no remote-run inspection is claimed. The equivalent local generation/build/render gate passed.

## Target

**PRX Quantum — Research Article** first; **Physical Review A — Regular Article** fallback.

**Priority remains unverified, not certified.**

**Freeze Rev10.** Reopen only for a concrete theorem defect, priority collision, build/journal-format issue, or new referee-level objection. Do not introduce a human-verification research gate.
