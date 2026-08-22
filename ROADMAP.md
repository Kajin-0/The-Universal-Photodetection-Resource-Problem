# Research Roadmap

**Updated:** 2026-08-22

`main` is landing/index only.

**Active branch:** `agent/temporal-information-resource-law`

**Grand Challenge science frontier:** **WP27**.

**Preferred manuscript:** **Rev10 — Spectral Resource Laws for Temporal Fisher Information**, frozen.

## Established theorem hierarchy

1. **Finite-copy arbitrary-POVM tail law**
   
   `Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`
   
   for any finite `N`, including entangled collective measurements.

2. **Controlled continuum survival law**
   
   `R(nu)<=Pr(Omega>=nu)`.

3. **Fixed-one-copy common-measurement Herglotz law**
   
   `R_M(k)=int cos(k theta)J_M(dtheta)`, so `[R_M(i-j)]` is PSD.

4. **Near-lossless energy divergence**
   
   `Ebar+>=hbar nu A(R)`, with `A(R)~1/sqrt(2(1-R))` as `R->1`.

5. **Sharp divergence exponent**
   
   A finite sine-profile source under canonical phase measurement has
   `R_L(1)=cos^2(pi/(L+1))` and `nbar_L=(L-1)/2`, hence
   `nbar_L~pi/[2sqrt(1-R_L(1))]`.
   The inverse-square-root exponent is sharp; the optimal prefactor is not claimed.

6. **Complete one-copy extremizers**
   
   `first-harmonic equality <=> geometric-mixture populations <=> Hausdorff-moment tails <=> one common source-adapted POVM saturates all harmonics`.

7. **Completely monotone continuum equality cone** through exponential mixtures.

8. **Nonextremal photon relevance**, **independent-Poisson source inheritance**, and the **coherent-sideband no-go boundary** remain in force.

## Scope discipline

The modewise tail theorem is finite-copy and collective-measurement general. The Herglotz/divergence theorem is a **fixed one-copy common-POVM** result. Bochner in the continuum extension requires continuity at the origin of the normalized positive-definite controlled limit.

Do not claim novelty for `U(1)` mode decomposition, Herglotz/Bochner, Hausdorff/Bernstein theory, geometric/exponential mixtures, canonical phase POVMs, sine states, generic QFI/Holevo machinery, or generic Poisson/CPTP processing.

**Priority remains unverified, not certified.**

## Rev10 gate

- 11 pages;
- full LaTeX/BibTeX build: **PASS**;
- unresolved citations/references: **0**;
- overfull boxes: **0**;
- 11/11 pages rendered at 200 dpi and inspected: **PASS**;
- sharpness validator: **PASS**;
- PDF SHA-256: `a5c2d9e12bba045b76bbfb710428e5424e2c5cb5eb83d6aec6215a5996dbc6fb`.

Detailed preflight lives on the active branch:
`grand_challenge/notes/MANUSCRIPT_REV10_REFEREE_CLOSURE_PREFLIGHT_2026-08-22.md`.

## Journal ladder

1. **PRX Quantum — Research Article**.
2. **Physical Review A — Regular Article**.
3. Physical Review Research — secondary alternative.
4. PRL only after a deliberate Letter rewrite.

## Current work order

**Freeze Rev10.** Reopen only for a concrete theorem defect, historical-priority collision, build/journal-format defect, or new referee-level objection. Do not introduce a human-verification research gate.
