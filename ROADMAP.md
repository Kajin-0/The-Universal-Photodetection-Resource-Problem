# Research Roadmap

**Updated:** 2026-08-22

`main` is landing/index only.

**Active branch:** `agent/temporal-information-resource-law`

**Grand Challenge science frontier:** **WP28**.

**Preferred manuscript:** **Rev11 — Spectral Resource Laws for Temporal Fisher Information**, frozen.

## Established theorem hierarchy

1. **Exact periodic finite-copy arbitrary-POVM law**
   
   `Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`
   
   for any finite `N`, including entangled collective measurements.

2. **Arbitrary semibounded pure-point Bohr-gap law**
   
   Long-window random-time averaging at requested `nu` isolates exact Bohr pairs and gives
   
   `Tr F_N^(nu)/N <= min(D_nu,U_nu) <= Pr(Omega>=nu)`.
   
   No global equal-spacing or commensurability assumption is required.

3. **Controlled continuum survival law**
   
   `R(nu)<=Pr(Omega>=nu)`, with no density/smoothness assumption on the spectral measure.

4. **Fixed-one-copy common-measurement Herglotz law**
   
   `R_M(k)=int cos(k theta)J_M(dtheta)`.
   
   The same structure applies across exact multiples of a chosen Bohr gap for arbitrary semibounded pure-point spectra.

5. **Near-lossless energy divergence with sharp exponent**
   
   `Ebar+>=hbar nu A(R)`, with `A(R)~1/sqrt(2(1-R))`.
   
   A finite sine-profile family realizes the same inverse-square-root exponent; the optimal prefactor is not claimed.

6. **Complete one-copy extremizers — contiguous model only**
   
   `first-harmonic equality <=> geometric-mixture populations <=> Hausdorff-moment tails <=> one common source-adapted POVM saturates all harmonics`.

7. **Completely monotone continuum equality cone** through exponential mixtures.

8. **Nonextremal photon relevance**, **independent-Poisson source inheritance**, and the **coherent-sideband no-go boundary** remain in force.

## Retired main-text material

The separately optimized SLD-QFI envelope remains valid background work but was removed from Rev11 in favor of the more central fixed-Hamiltonian Bohr-gap theorem.

## Scope discipline

The modewise tail theorem is finite-copy and collective-measurement general. The Herglotz/divergence theorem is a **fixed one-copy common-POVM** result. The complete extremizer converse remains restricted to the full contiguous pure-sector chain.

Do not claim novelty for arbitrary Bohr-frequency / `U(1)` mode decomposition, random-time dephasing, Herglotz/Bochner, Hausdorff/Bernstein theory, geometric/exponential mixtures, phase POVMs, sine states, generic QFI/Holevo machinery, or generic Poisson/CPTP processing.

**Priority remains unverified, not certified.**

## Rev11 gate

- 12 pages;
- full LaTeX/BibTeX build: **PASS**;
- unresolved citations/references: **0**;
- overfull boxes: **0**;
- 12/12 pages rendered at 200 dpi and inspected: **PASS**;
- all six numerical validators: **PASS**;
- PDF SHA-256: `5e0ac0132a7f4a3f7b07e9c4ba86b046b23bc89c1f7635efe9f737019396d0f0`;
- source ZIP SHA-256: `208fd7a2e932507366797658c84dff1666257477143a433bf81d7741a8d0c8a1`.

Detailed preflight lives on the active branch:
`grand_challenge/notes/MANUSCRIPT_REV11_ANHARMONIC_PREFLIGHT_2026-08-22.md`.

## Journal ladder

1. **PRX Quantum — Research Article**.
2. **Physical Review A — Regular Article**.
3. Physical Review Research — secondary alternative.
4. PRL only after a deliberate Letter rewrite.

## Current work order

**Freeze Rev11.** Reopen only for a concrete theorem defect, historical-priority collision, substantive referee objection, build/journal-format defect, or render regression. Do not introduce a human-verification research gate.
