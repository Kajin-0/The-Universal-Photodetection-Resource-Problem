# Research Roadmap

**Updated:** 2026-08-22

**Active branch:** `agent/temporal-information-resource-law`

Paper 1 Rev11 and Paper 2 Rev7 are frozen.

**Grand Challenge science frontier:** **WP28**.

**Preferred manuscript:** **Rev11 — Spectral Resource Laws for Temporal Fisher Information**, frozen after full local preflight.

# Established hierarchy

## G1 — exact periodic finite-copy Fisher-tail law

For exact periodic random-time encoding,

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`

for any finite `N` and any joint POVM, including arbitrary entangled collective measurements.

## G2 — arbitrary semibounded pure-point Bohr-gap law

For an arbitrary semibounded pure-point Hamiltonian, long-window random-time averaging at frequency `nu` isolates exact Bohr pairs and gives

`A_nu=rho0^(1/2)V_nu rho0^(1/2)`.

Therefore

`Tr F_N^(nu)/N <= min(D_nu,U_nu) <= Pr(Omega>=nu)`

for any finite `N` and joint POVM, with no global equal-spacing or commensurability assumption.

This is the main WP28/Rev11 strengthening.

## G3 — controlled continuum survival law

`R(nu)<=Pr(Omega>=nu)`.

The spectral measure may be atomic, absolutely continuous, singular-continuous, or mixed. `Ebar+=hbar<Omega>` is excess energy above the participating lower edge; the area and `hfR` laws are first-moment corollaries.

## G4 — common-measurement Herglotz geometry

For one fixed one-copy POVM,

`R_M(k)=int cos(k theta)J_M(dtheta)`.

Every Toeplitz matrix `[R_M(i-j)]` is PSD. Zero-population completion cannot create Fisher information.

For arbitrary pure-point spectra the same geometry holds across exact multiples of a chosen Bohr gap.

## G5 — near-lossless divergence with sharp exponent

`Ebar+>=hbar nu A(q)`,

`A(q)~1/sqrt(2(1-q))`.

The sine-profile family realizes

`nbar_L~pi/[2sqrt(1-R_L(1))]`,

so the inverse-square-root exponent is sharp. Do not claim the optimal prefactor.

## G6 — complete one-copy extremizer classification

Only on the full contiguous pure-sector chain:

`first-harmonic saturation`

`<=> geometric-mixture populations`

`<=> Hausdorff-moment tails`

`<=> one source-adapted POVM saturates every harmonic simultaneously`.

Do not generalize this converse to arbitrary anharmonic/sparse/mixed spectra or arbitrary entangled `N>1` equality cases.

## G7 — nonextremal photon relevance

A transform-limited truncated-Gaussian single photon reaches about 96.6% of the survival ceiling at `0.5 sigma` and 88.5% at `sigma` under canonical covariant timing.

## G8 — independent Poisson source to field

For an independent quantum-marked Poisson source, arbitrary parameter-independent field formation and detector processing cannot evade the normalized modewise ceiling because final POVMs pull back to the upstream event register.

## G9 — arbitrary waveform synthesis boundary

The coherent-sideband no-go remains: baseline mean energy alone cannot constrain arbitrary parameter-dependent waveform-state synthesis. Broader laws require explicit encoding/control/action resources.

## Retired from manuscript main line

The separately optimized SLD-QFI envelope remains mathematically valid in WP10/WP12/WP15 but was **removed from Rev11** because it is peripheral relative to the anharmonic Bohr-gap theorem. Do not restore it unless a specific editorial need arises.

# Prior-art discipline

Do not claim novelty for arbitrary Bohr-frequency / `U(1)` modes, random-time dephasing, Herglotz/Bochner, Hausdorff/Bernstein theory, canonical phase POVMs, geometric/exponential mixtures, finite sine states, generic QFI/Holevo machinery, or generic Poisson/CPTP processing.

Candidate contribution: arbitrary-POVM Fisher-tail coefficients, exact-Bohr-gap extension to arbitrary semibounded pure-point Hamiltonians, common-measurement spectral geometry, semibounded near-lossless divergence with sharp exponent, complete one-copy equality classification in the contiguous model, and source-to-record inheritance.

**Priority remains unverified, not certified.**

# Rev11 gate — PASSED locally

- full LaTeX/BibTeX build: **PASS**;
- **12 pages**;
- PDF size: **452,384 bytes**;
- unresolved citations/references: **0**;
- overfull boxes: **0**;
- all 12 pages rendered at 200 dpi and visually inspected: **PASS**;
- all six numerical validators: **PASS**;
- PDF SHA-256: `5e0ac0132a7f4a3f7b07e9c4ba86b046b23bc89c1f7635efe9f737019396d0f0`;
- source ZIP SHA-256: `208fd7a2e932507366797658c84dff1666257477143a433bf81d7741a8d0c8a1`;
- fresh source-package compile: **PASS**;
- fresh compile visually pixel-identical at 200 dpi on all pages.

Detailed record:
`grand_challenge/notes/MANUSCRIPT_REV11_ANHARMONIC_PREFLIGHT_2026-08-22.md`.

# Journal ladder

1. **PRX Quantum — Research Article**.
2. **Physical Review A — Regular Article**.
3. Physical Review Research — secondary alternative.
4. PRL — only after a deliberate Letter rewrite; do not hide hypotheses or proof structure.

# Current work order

**Freeze Rev11.** Do not add the optional finite-amplitude trace-distance result, optimize constants, or broaden the extremizer theorem by default. Reopen only for:

- a concrete theorem defect;
- historical-priority collision;
- substantive referee objection;
- build/rendering or journal-format defect.

Complete publication engineering as far as possible autonomously. Do not introduce “human verification” as a research/manuscript gate.

# Documentation discipline

Every material theorem, prior-art collision, manuscript defect, or publication-status change must update the detailed notes, active handoff files, and `main`.
