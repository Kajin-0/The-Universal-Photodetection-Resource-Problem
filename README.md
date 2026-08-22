# The Universal Photodetection Resource Problem

**Current status: 2026-08-22**

`main` is the landing/index branch. Detailed Grand Challenge derivations and manuscript generation live on `agent/temporal-information-resource-law`.

## Project split

1. **Paper 1 / Rev11** — frozen.
2. **Paper 2 / Rev7** — frozen.
3. **Grand Challenge** — science frontier **WP28**; **Rev11 frozen as the preferred PRX Quantum manuscript**.

Authoritative handoff: active-branch `grand_challenge/AGENTS.md`.

# Grand Challenge headline

The exact periodic random-time experiment obeys

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`

for any finite `N` and arbitrary joint POVM, including entangled collective measurements.

Rev11 establishes that this is **not a harmonic-ladder artifact**. For an arbitrary semibounded pure-point Hamiltonian, long-window random-time averaging at a requested frequency `nu` isolates exact Bohr pairs and gives

`Tr F_N^(nu)/N <= min(D_nu,U_nu) <= Pr(Omega>=nu)`

with no global equal-spacing or commensurability assumption.

Controlled periodic-to-continuum limits give the same survival law

`R(nu)<=Pr(Omega>=nu)`.

The continuum spectral measure need not have a density; atomic, absolutely continuous, singular-continuous, and mixed measures are allowed.

## One physical measurement imposes cross-frequency structure

For **one fixed one-copy POVM**, the retention sequence is positive definite:

`R_M(k)=int cos(k theta)J_M(dtheta)`.

The same Herglotz/Toeplitz structure applies across exact multiples of a chosen Bohr gap for arbitrary semibounded pure-point spectra. Combining it with the energy tails gives

`Ebar+>=hbar nu A(R)`,

with `A(R)~1/sqrt(2(1-R))` as `R->1`.

A finite sine-profile family proves the inverse-square-root divergence exponent is **sharp**; the optimal prefactor is not claimed.

## Complete one-copy extremizers

The converse remains narrower. On the full contiguous pure-sector chain:

`first-harmonic equality`

`<=> geometric-mixture populations`

`<=> Hausdorff-moment survival tails`

`<=> one source-adapted POVM saturates every harmonic simultaneously`.

Controlled exponential mixtures give the completely monotone continuum equality cone.

## Scope

The modewise tail theorem includes arbitrary finite-copy collective measurements. The Herglotz/divergence theorem is a **fixed one-copy common-POVM** statement. The extremizer converse is not claimed for arbitrary anharmonic/sparse spectra.

Independent quantum-marked Poisson sources inherit the modewise law through arbitrary **parameter-independent** source-to-field and detector processing. Arbitrary parameter-dependent waveform synthesis remains outside the theorem.

# Rev11 publication gate

- **12 pages**;
- full LaTeX/BibTeX compile: **PASS**;
- unresolved references/citations: **0**;
- overfull boxes: **0**;
- all pages rendered at 200 dpi and inspected: **PASS**;
- all six numerical validators: **PASS**;
- PDF SHA-256: `5e0ac0132a7f4a3f7b07e9c4ba86b046b23bc89c1f7635efe9f737019396d0f0`;
- source ZIP SHA-256: `208fd7a2e932507366797658c84dff1666257477143a433bf81d7741a8d0c8a1`;
- fresh source-package recompile visually pixel-identical on all 12 pages.

**First target:** PRX Quantum — Research Article.

**Fallback:** Physical Review A — Regular Article.

**Priority remains unverified, not certified.**

# Recovery

Switch to `agent/temporal-information-resource-law` and read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV11_ANHARMONIC_PREFLIGHT_2026-08-22.md`
3. `grand_challenge/notes/WP28_ANHARMONIC_PURE_POINT_GAP_EXTENSION_AND_CONTINUUM_ATTACK.md`
4. `docs/CURRENT_RESEARCH_STATE.md`
5. `ROADMAP.md`

# Workflow rule

**Freeze Rev11.** Reopen only for a concrete theorem defect, priority collision, substantive referee objection, build/render regression, or unavoidable journal-format issue.

Do not reintroduce “human verification” as a research/manuscript completion gate. The finished package is produced as far as possible and then submitted by a human. Unknown administrative facts remain placeholders.
