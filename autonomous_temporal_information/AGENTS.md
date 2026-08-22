# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

**Started:** 2026-08-22

This branch is a distinct theoretical program. The Rev11 random-time paper on `agent/temporal-information-resource-law` remains frozen and must not be rewritten from this branch unless a concrete defect is discovered.

## Grand question

> When the signal, clock/reference frame, controller, probe, detector, and memory are all finite physical systems and no ideal externally timed operation is free, what physical resource constrains the creation, transmission, and recovery of temporal information at frequency `nu`?

The target is not merely another bandwidth or quantum-speed-limit inequality. The desired endpoint is a general autonomous **temporal-information resource law** in which externally supplied timing/control is explicitly represented as a physical resource.

## Research standard

- Analytical/theoretical only.
- Falsification-first: attack every proposed law with minimal counterexamples before generalizing it.
- Existing asymmetry/reference-frame results are infrastructure, not novelty claims.
- Record all theorem attempts, counterexamples, literature collisions, and numerical checks immediately in this directory.
- Do not rely on chat history for recovery.
- Do not claim Nobel-level significance prospectively; judge significance only after a theorem survives proof and priority review.

## Current frontier

**WP02 — local-Fisher no-go and robust tangent-radius law: analytic PASS.**

Read:

`autonomous_temporal_information/notes/WP02_LOCAL_FISHER_NO_GO_AND_ROBUST_TANGENT_RADIUS_LAW.md`

### Prior-art boundary from WP01

The qualitative statement

`a quantum reference frame can simulate only channel/measurement modes contained in the reference-frame state`

is already prior art: Marvian and Spekkens, *Phys. Rev. A* 90, 062110 (2014), DOI `10.1103/PhysRevA.90.062110`.

Likewise, finite autonomous quantum clocks/control, QFI as an asymmetry resource, generic mode trace-norm monotones, and energy-constrained multistep metrology are established. Do not claim novelty for them.

### WP02 no-go

Local Fisher information by itself cannot obey a universal high-frequency mean-energy ceiling for arbitrary state synthesis.

For a two-level Hamiltonian with gap `hbar nu`, choose baseline excited population

`p=E/(hbar nu)`

so the mean excess energy is exactly `E`. There exists an affine two-quadrature family whose Fisher trace under one fixed equatorial POVM is independent of `nu`. As `nu` increases, the physical disk on which the tangent can be extended linearly shrinks as `nu^(-1/2)`.

Thus the hidden resource discarded by a purely local Fisher metric is the **physical robustness/radius of the tangent**.

### WP02 theorem

Let `rho0` be stationary under a semibounded Hamiltonian and let `A_nu` be a positive exact-Bohr-gap tangent. Define

`D_c=(A_nu+A_nu^dagger)/2`,

`D_s=(A_nu-A_nu^dagger)/(2i)`.

Define `R_lin` as the largest radius such that

`rho0 + eps_c D_c + eps_s D_s >= 0`

for every `eps_c^2+eps_s^2 <= R_lin^2`.

For `R_lin>0`, with

`B_nu=rho0^(-1/2) A_nu rho0^(-1/2)`,

positivity gives the exact numerical-radius identity

`R_lin = 1/w(B_nu)`.

Using `||B||<=2w(B)` plus the Rev11-style Hilbert--Schmidt argument yields, for **any finite N and any joint POVM**, including entangled collective measurements,

`(R_lin^2/4) [Tr F_N^(nu)/N] <= min(D_nu,U_nu) <= T(nu)`.

Hence

`Ebar+ >= (hbar nu R_lin^2/4) [Tr F_N^(nu)/N]`.

This does **not** assume random-time encoding. It applies to arbitrary exact-gap tangents about a stationary baseline.

The two-level no-go family asymptotically saturates the robust energy law as `nu->infinity` at fixed mean energy, showing that the missing `R_lin` factor is not cosmetic.

### Important boundary

`R_lin` is the radius of the **linearized tangent**, not the physical range of an arbitrary nonlinear family. Coherent-sideband synthesis can remain physical through second-order population even when its linear tangent radius is zero.

Therefore the grand autonomous problem is not solved. WP02 identifies why arbitrary local Fisher geometry escapes energy bounds and provides a robust law for the nonzero-linear-radius sector.

## Current next target — WP03

Reference-assisted parameter-to-time conversion:

1. `D` — time-symmetric data/program register carrying unknown parameter;
2. `R` — finite clock/reference/controller;
3. `S` — target signal/output;
4. parameter-independent globally time-translation-covariant processing;
5. no free asymmetric readout.

Established modes-of-asymmetry theory gives only the structural identity

`dot rho_out^(nu) = Phi(eta_R^(nu) tensor dot tau_D)`.

The candidate new target is a **quantitative autonomous performance law** connecting the generated temporal Fisher/finite distinguishability at `nu` to a finite reference/controller resource, ideally using or generalizing the WP02 robust tangent quantity.

In parallel, attack the nonlinear loophole: determine the weakest finite-amplitude/curvature/control assumption that yields a nontrivial theorem when `R_lin=0`.

## Numerical gate

`autonomous_temporal_information/numerics/verify_robust_tangent_radius_law.py`

checks:

- fixed-energy/high-frequency local-Fisher no-go;
- tangent-radius positivity/numerical-radius relation;
- random one-copy POVM bounds;
- random two-copy collective POVM bounds;
- asymptotic two-level sharpness of the energy corollary.

## Read first

1. `autonomous_temporal_information/notes/WP02_LOCAL_FISHER_NO_GO_AND_ROBUST_TANGENT_RADIUS_LAW.md`
2. `autonomous_temporal_information/notes/WP01_FOUNDATIONAL_SCOPE_AND_PRIOR_ART_BOUNDARY.md`
3. `autonomous_temporal_information/ROADMAP.md`
4. frozen parent-program handoff: `grand_challenge/AGENTS.md`

## Documentation rule

Every material result must update this file and `autonomous_temporal_information/ROADMAP.md`. When a result becomes stable enough to change the project-level frontier, mirror the status onto the repository landing files. Until then, keep Rev11 advertised as the finished Grand Challenge paper and this program as the new exploratory branch.
