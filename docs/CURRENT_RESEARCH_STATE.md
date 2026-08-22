# Current Research State

**Last synchronized:** 2026-08-22

`main` is landing/index only.

**Active branch:** `agent/temporal-information-resource-law`

- Paper 1 Rev11: frozen.
- Paper 2 Rev7: frozen.
- Grand Challenge science frontier: **WP28**.
- Preferred Grand Challenge manuscript: **Rev11 — Spectral Resource Laws for Temporal Fisher Information**, frozen.

## Recovery

Switch to `agent/temporal-information-resource-law` and read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV11_ANHARMONIC_PREFLIGHT_2026-08-22.md`
3. `grand_challenge/notes/WP28_ANHARMONIC_PURE_POINT_GAP_EXTENSION_AND_CONTINUUM_ATTACK.md`
4. `docs/CURRENT_RESEARCH_STATE.md`
5. `ROADMAP.md`

## Current theorem hierarchy

### Exact periodic finite-copy law

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`

for any finite number of independently encoded copies and any joint POVM, including arbitrary entangled collective measurements.

### Arbitrary pure-point Bohr-gap law

For an arbitrary semibounded pure-point Hamiltonian, long-window random-time averaging at frequency `nu` isolates exact Bohr pairs and yields

`Tr F_N^(nu)/N <= min(D_nu,U_nu) <= Pr(Omega>=nu)`.

No global equal-spacing or commensurability assumption is required.

### Controlled continuum survival law

`R(nu)<=Pr(Omega>=nu)`.

The spectral measure need not be smooth or absolutely continuous; atomic and singular-continuous components are allowed.

### Fixed-one-copy common-measurement law

For one fixed one-copy POVM,

`R_M(k)=int cos(k theta)J_M(dtheta)`.

The retention sequence is positive definite. The same structure applies across exact multiples of a chosen Bohr gap for arbitrary semibounded pure-point spectra.

Combining this with energy tails gives

`Ebar+>=hbar nu A(R)`,

`A(R)~1/sqrt(2(1-R))` as `R->1`.

The finite sine-profile witness proves the inverse-square-root divergence exponent is sharp; the optimal prefactor is not claimed.

### Complete one-copy extremizers

Only on the full contiguous pure-sector chain:

`first-harmonic equality <=> geometric-mixture populations <=> Hausdorff-moment tails <=> one common source-adapted POVM saturates every harmonic simultaneously`.

## Scope discipline

The modewise tail theorem includes arbitrary finite-copy collective POVMs. The Herglotz/divergence theorem is a **fixed one-copy common-POVM** result. The complete extremizer converse is not generalized to arbitrary anharmonic/sparse spectra.

Independent quantum-marked Poisson sources inherit the modewise law through arbitrary parameter-independent source-to-field and detector processing. Arbitrary parameter-dependent waveform-state synthesis remains outside the theorem.

## Rev11 publication preflight

- 12 pages;
- full LaTeX/BibTeX build: **PASS**;
- unresolved references/citations: **0**;
- overfull boxes: **0**;
- all pages rendered at 200 dpi and visually inspected: **PASS**;
- all six numerical validators: **PASS**;
- PDF SHA-256: `5e0ac0132a7f4a3f7b07e9c4ba86b046b23bc89c1f7635efe9f737019396d0f0`;
- source ZIP SHA-256: `208fd7a2e932507366797658c84dff1666257477143a433bf81d7741a8d0c8a1`;
- fresh source-package recompile visually pixel-identical on all 12 pages.

## Target

**PRX Quantum — Research Article** first; **Physical Review A — Regular Article** fallback.

**Priority remains unverified, not certified.**

**Freeze Rev11.** Reopen only for a concrete theorem defect, priority collision, substantive referee objection, build/journal-format issue, or render regression. Do not introduce a human-verification research gate.
