# AGENTS.md

## Purpose

Durable repository handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

`main` is the landing/index branch. Active derivations and manuscript generation live on `agent/temporal-information-resource-law`.

## Current frontier

- Paper 1 Rev11: frozen.
- Paper 2 Rev7: frozen.
- Grand Challenge science frontier: **WP28**.
- Preferred Grand Challenge manuscript: **Rev11 — Spectral Resource Laws for Temporal Fisher Information**, frozen.
- First target: **PRX Quantum — Research Article**.
- Fallback: **Physical Review A — Regular Article**.

A replacement agent must switch to `agent/temporal-information-resource-law` and read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV11_ANHARMONIC_PREFLIGHT_2026-08-22.md`
3. `grand_challenge/notes/WP28_ANHARMONIC_PURE_POINT_GAP_EXTENSION_AND_CONTINUUM_ATTACK.md`
4. `docs/CURRENT_RESEARCH_STATE.md`
5. `ROADMAP.md`

## Theorem hierarchy

### Exact periodic finite-copy law

For any finite number of independently encoded copies and any joint POVM,

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`.

### Arbitrary pure-point Bohr-gap law

For an arbitrary semibounded pure-point Hamiltonian, long-window random-time averaging at requested frequency `nu` isolates exact Bohr pairs and gives

`Tr F_N^(nu)/N <= min(D_nu,U_nu) <= Pr(Omega>=nu)`

for arbitrary finite-copy joint POVMs. No global equal-spacing or commensurability assumption is required.

### Controlled continuum law

`R(nu)<=Pr(Omega>=nu)`.

The spectral measure may be atomic, absolutely continuous, singular-continuous, or mixed.

### Fixed-one-copy common-measurement law

For one fixed one-copy POVM,

`R_M(k)=int cos(k theta)J_M(dtheta)`.

Thus every finite Toeplitz block is PSD. The same structure applies across exact multiples of a chosen Bohr gap for arbitrary semibounded pure-point spectra.

Combining with energy tails gives

`Ebar+>=hbar nu A(R)`,

`A(R)~1/sqrt(2(1-R))`.

The finite sine-profile witness proves the inverse-square-root divergence exponent is sharp; the optimal prefactor is not claimed.

### Complete one-copy extremizers

Only on the full contiguous pure-sector chain:

`first-harmonic equality <=> geometric-mixture populations <=> Hausdorff-moment tails <=> one common source-adapted POVM saturates all harmonics`.

Do not broaden this converse to arbitrary anharmonic/sparse spectra or arbitrary collective-copy equality cases.

## Physical scope

Independent quantum-marked Poisson sources inherit the modewise law through arbitrary parameter-independent source-to-field and detector processing. Arbitrary parameter-dependent waveform-state synthesis remains outside the theorem.

## Priority discipline

Do not claim novelty for arbitrary Bohr-frequency / `U(1)` mode decomposition, random-time dephasing, Herglotz/Bochner, Hausdorff/Bernstein theory, canonical phase POVMs, geometric/exponential mixtures, sine states, generic QFI/Holevo machinery, or generic Poisson/CPTP processing.

Candidate contribution: arbitrary-POVM Fisher-tail coefficients, their exact-Bohr-gap extension to arbitrary semibounded pure-point Hamiltonians, common-measurement spectral geometry, sharp near-lossless energy divergence, contiguous-chain extremizer classification, and source-to-record inheritance.

**Priority remains unverified, not certified.**

## Rev11 preflight

- 12 pages;
- full LaTeX/BibTeX build: **PASS**;
- unresolved references/citations: **0**;
- overfull boxes: **0**;
- all pages rendered at 200 dpi and inspected: **PASS**;
- all six numerical validators: **PASS**;
- PDF SHA-256: `5e0ac0132a7f4a3f7b07e9c4ba86b046b23bc89c1f7635efe9f737019396d0f0`;
- source ZIP SHA-256: `208fd7a2e932507366797658c84dff1666257477143a433bf81d7741a8d0c8a1`;
- fresh source-package recompile visually pixel-identical at 200 dpi.

## Workflow rule

Do **not** reintroduce “human verification” as a research/manuscript completion gate. Carry work autonomously through hostile review, research, derivation, code checks, manuscript, figures, builds, and submission engineering. The finished package is handed to a human for submission.

Unknown administrative facts may remain placeholders; never invent affiliation, funding, conflicts, or similar metadata.

## Freeze

**Freeze Rev11** unless a concrete theorem defect, historical-priority collision, substantive referee objection, build/journal-format problem, or render regression appears.

Every material state change must be reflected on the active branch and mirrored onto `main`.
