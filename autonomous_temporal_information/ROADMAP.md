# Roadmap — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

## Goal

Seek a foundational physical resource principle for temporal information when clock, signal, controller, detector, and memory are all internal quantum systems. The finished Rev11 random-time law remains frozen on its parent branch.

## Completed foundations

### WP01 — prior-art and model boundary — PASS

Do not claim novelty for:

- modes-of-asymmetry / reference-frame support laws;
- mode trace-norm monotones;
- QFI as an asymmetry resource;
- finite autonomous clocks/control per se;
- quantitative WAY tradeoffs;
- generic quantum speed limits;
- standard phase-estimation sine states / Heisenberg scaling;
- simply charging preparation/control energy.

The program must produce an operational temporal-information resource law.

### WP02 — local-Fisher no-go and robust tangent radius — PASS

At fixed baseline mean energy, arbitrary local state synthesis can retain fixed local Fisher information at arbitrarily high Bohr frequency by shrinking the physical tangent neighborhood.

Define `R_lin` as the largest disk over which the linearized two-quadrature tangent remains positive.

For stationary `rho0` and exact gap `nu`, arbitrary finite-copy collective measurements obey

`(R_lin^2/4)[Tr F_N^(nu)/N] <= min(D_nu,U_nu) <= T(nu)`.

Therefore

`Ebar+ >= (hbar nu R_lin^2/4)[Tr F_N^(nu)/N]`.

The counterexample asymptotically saturates this robust law.

### WP03 — relational dual-energy survival — PASS

For clock `C` and signal `S`, take a globally stationary energy-exchange tangent

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`.

Then, with

`K_N=(R_lin^2/4)[Tr F_N/N]`,

for any finite N and arbitrary joint POVM,

`K_N(nu) <= min{T_C(nu),T_S(nu)}`.

Thus

`Ebar_C^+ + Ebar_S^+ >= 2 hbar nu K_N`.

The factor `2` is asymptotically sharp: a symmetric two-qubit exchange model satisfies weak multiparameter commutativity, so collective measurements asymptotically attain both local tail bounds simultaneously.

All-mode lattice budget:

`sum_k K_N(k) <= min(nbar_C,nbar_S)`.

### WP04 — exact hard total-energy cap law — PASS

For a structured relative-time experiment inside a fixed/hard-capped total-excitation shell `N_C+N_S<=L`, the exchange shift is finite.

For one fixed one-copy POVM,

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

With `nu=k omega0` and `E_max=hbar omega0 L`,

`R_M(nu) <= cos^2{pi/[floor(E_max/(hbar nu))+2]}`.

For the fundamental mode,

`E_max >= hbar nu[pi/arccos(sqrt R)-2]`.

Near unit retention,

`E_max >= pi hbar nu/sqrt(1-R)[1+o(1)]`.

This bound is exactly sharp. A globally stationary fixed-total-energy sine-chain history state and canonical relative-phase POVM attain equality.

The finite-shift/sine-state constant is phase-estimation prior art. Candidate novelty is the exact arbitrary-POVM **Fisher-retention** law for autonomous relational time.

## Current frontier — WP05

### A. Sharp mean-total-energy law

Hard cap is solved exactly; mean total energy only is not.

Questions:

1. What is
   `sup R_M(1)`
   at fixed `Ebar_C+Ebar_S` for a globally stationary relative-time experiment?
2. Does the optimal asymptotic constant coincide with known Airy-function phase-estimation constants, or does the Fisher-retention functional have a different optimizer because it averages squared posterior sharpness?
3. Can the optimization be reduced to a convex envelope over fixed-total-energy shells?
4. Is there an exact or asymptotic extremizer family?

Known phase-estimation mean-generator bounds (Berry--Hall--Zwierz--Wiseman, PRA 86, 053813 (2012)) are prior art and cannot simply be relabeled.

### B. Pre-existing relational coherence

WP03 assumes a baseline separately stationary under clock and signal Hamiltonians, with the unknown parameter introducing the relational exchange coherence.

Extend to general Page--Wootters/history states that are already relationally coherent at baseline while remaining globally stationary.

This is likely essential for a genuinely autonomous clock law.

### C. Nonlinear `R_lin=0` synthesis

Determine the weakest additional physical datum that restores a theorem when second-order population/curvature keeps the exact nonlinear family physical despite zero linear tangent radius.

Candidate resources:

- finite parameter amplitude;
- finite trace distance / hypothesis-testing performance;
- curvature or second derivative;
- explicit control Hamiltonian/action.

### D. Many-body cut law

Test the conjecture:

> temporal information crossing any autonomous bipartition requires matched energy-exchange resources on both sides of the cut.

Seek a cut-set / network generalization of WP03.

### E. Autonomous control-generator resource

If operations do not obey the energy-conserving/covariant structure, arbitrary interaction strength is a loophole. Determine which dynamical resource must be charged: spectral diameter, interaction norm, action, power, or another invariant.

## Later stages

### WP06 — unified apparatus law

Combine reference-state, relational exchange, and control-generator resources into one theorem for

`source + clock + controller + detector + memory`.

### WP07 — finite distinguishability

Replace local Fisher by finite-amplitude trace distance / hypothesis testing.

### WP08 — temporal channel capacity

If the preceding structure survives, seek mutual-information/channel-capacity consequences.

## Publication / significance gate

Do not draft a new foundational manuscript merely because WP02--WP04 are mathematically interesting. First require:

- deep priority audit;
- at least one theorem that is clearly not reducible to known phase estimation/WAY/asymmetry statements;
- hostile mathematical review;
- sharp or near-sharp constructions;
- explicit physical consequence or thought experiment.

## Documentation discipline

Every material theorem, failed conjecture, prior-art collision, or validation result must be recorded immediately in the branch. The repository, not chat history, is authoritative.
