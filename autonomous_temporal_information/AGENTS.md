# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

**Started:** 2026-08-22

This is a distinct post-Rev11 foundational program. The frozen Rev11 paper remains on `agent/temporal-information-resource-law` and must not be rewritten from this branch absent a concrete defect.

## Grand question

> When signal, clock/reference, controller, detector, and memory are all finite physical systems and no ideal externally timed operation is free, what resource constrains creation, transmission, and recovery of temporal information at frequency `nu`?

Research is analytical/theoretical, falsification-first, and documentation-first. Existing asymmetry, reference-frame, phase-estimation, WAY, Page--Wootters, and finite-clock results are infrastructure unless a genuinely new operational theorem is isolated.

## Current frontier

**WP06 — nonstationary robust tail / pre-existing history-state extension: analytic PASS.**

The highest-value unresolved problem is now **WP07: nonlinear `R_lin=0` synthesis**.

The active theorem hierarchy is:

`local Fisher strength x physical tangent robustness <= spectral resource`,

and for an internal clock--signal relation,

`the matching spectral resource must exist on both sides`.

For the structured globally stationary relative-time model, the finite-resource retention law is exactly solved under both hard and mean total energy.

### WP01 — prior-art boundary

Established, not new:

- Marvian--Spekkens modes of asymmetry and mode monotones;
- QFI/Fisher geometry as an asymmetry resource;
- finite quantum reference frames and autonomous clocks;
- Page--Wootters relational time;
- quantitative WAY tradeoffs;
- ordinary phase-estimation sine states / Heisenberg scaling;
- simply charging preparation/control energy.

The program must produce a quantitative **operational temporal-information performance law**, not a repackaging of mode support.

### WP02 — local Fisher no-go and robust tangent radius

For arbitrary state synthesis, fixed baseline mean energy does **not** force local Fisher information to vanish at high Bohr frequency. A two-level family keeps `Tr F` fixed as `nu->infinity` while its physical linear tangent radius shrinks.

Define `R_lin` as the largest disk on which the two-quadrature linear tangent remains positive. For stationary `rho0` and exact positive-gap tangent `A_nu`,

`R_lin = 1 / w(rho0^(-1/2) A_nu rho0^(-1/2))`,

where `w` is numerical radius.

For any finite `N` and any joint POVM,

`(R_lin^2/4)[Tr F_N^(nu)/N] <= min(D_nu,U_nu) <= T(nu)`.

Hence

`Ebar+ >= (hbar nu R_lin^2/4)[Tr F_N^(nu)/N]`.

The fixed-energy/high-frequency counterexample asymptotically saturates this corrected law.

Read:
`notes/WP02_LOCAL_FISHER_NO_GO_AND_ROBUST_TANGENT_RADIUS_LAW.md`.

### WP03 — globally stationary relational dual-survival law

For an exact relational exchange tangent,

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`,

so

`[H_C+H_S,A_nu]=0`.

Define

`K_N(nu)=(R_lin^2/4)[Tr F_N^(nu)/N]`.

Then, for arbitrary finite-copy collective measurements,

`K_N(nu) <= min{T_C(nu),T_S(nu)}`.

Thus

`Ebar_C^+ >= hbar nu K_N`,

`Ebar_S^+ >= hbar nu K_N`,

and

`Ebar_C^+ + Ebar_S^+ >= 2 hbar nu K_N`.

The coefficient `2` is asymptotically sharp. In the symmetric two-qubit exchange model, weak SLD commutativity makes the SLD/Holevo limit asymptotically attainable by collective measurements, simultaneously saturating both local tails.

On a common lattice,

`sum_(k>=1) K_N(k) <= min(nbar_C,nbar_S)`.

Read:
`notes/WP03_RELATIONAL_DUAL_ENERGY_SURVIVAL_LAW.md`.

### WP04 — exact hard total-energy cap law

For the structured globally stationary relative-time experiment inside a fixed/hard-capped total-excitation shell,

`N_C+N_S<=L`,

the exchange coordinate is a finite shift. For one fixed one-copy POVM,

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

Equivalently, for `nu=k omega0` and `E_max=hbar omega0 L`,

`R_M(nu) <= cos^2{pi/[floor(E_max/(hbar nu))+2]}`.

At the fundamental frequency,

`E_max >= hbar nu[pi/arccos(sqrt R)-2]`,

and near perfect retention

`E_max >= pi hbar nu/sqrt(1-R)[1+o(1)]`.

Globally stationary sine-chain history states with canonical relative-phase readout attain equality. The sine-state/finite-shift mathematics is phase-estimation prior art; candidate novelty is the autonomous Fisher-retention interpretation.

Read:
`notes/WP04_EXACT_HARD_CAP_AUTONOMOUS_RELATIONAL_RETENTION.md`.

### WP05 — exact mean-total-energy law

Let

`g_L=cos^2[pi/(L+2)]`.

For baseline total-excitation shell probabilities `W_L`,

`R_M(1) <= sum_L W_L g_L`.

The sequence `{g_L}` is discretely concave. Writing

`Lbar=m+lambda`, `m=floor(Lbar)`, `0<=lambda<1`,

the exact sharp envelope is

`R_M(1) <= G(Lbar)=(1-lambda)g_m+lambda g_(m+1)`.

Equality is constructive: mix the sine-chain extremizers in shells `m` and `m+1` with probabilities `1-lambda` and `lambda`, resolve total energy, and then perform canonical relative-phase readout.

Therefore

`Ebar_C^+ + Ebar_S^+ >= pi hbar nu/sqrt(1-R)[1+o(1)]`

with leading constant `pi` sharp in the one-copy structured mean-energy problem.

Read:
`notes/WP05_EXACT_MEAN_ENERGY_AUTONOMOUS_RELATIONAL_RETENTION.md`.

### WP06 — arbitrary coherent baseline / history-state extension

WP02/WP03 originally used baseline stationarity with respect to the relevant local Hamiltonian. That assumption is unnecessary for the robust tail theorem.

For arbitrary density operator `rho`, positive tangent radius `R_lin`, and complex tangent `A`, define on `supp(rho)`

`B=rho^(-1/2) A rho^(-1/2)`.

Positivity still gives

`R_lin=1/w(B)`

and

`||B||<=2/R_lin`.

For any POVM,

`Tr F_1 <= Tr(A rho^+ A^dagger)`.

If the range of `A` lies in projector `P_U`, then

`A rho^+ A^dagger <= (4/R_lin^2)rho`

and therefore

`(R_lin^2/4) Tr F_1 <= Tr(P_U rho)`.

The finite-copy extension gives, for arbitrary joint POVMs,

`(R_lin^2/4)[Tr F_N/N] <= Tr(P_U rho)`.

For an exact positive gap, `P_U` is the upper spectral tail projector, so the same energy-survival law holds with **no baseline stationarity assumption**.

In the autonomous relational setting this allows

`[rho_CS,H_C+H_S]=0`

while generally

`[rho_CS,H_C] != 0`, `[rho_CS,H_S] != 0`.

Hence pre-existing Page--Wootters/history-state relational coherence does **not** evade

`K_N(nu) <= min{T_C(nu),T_S(nu)}`.

Read:
`notes/WP06_NONSTATIONARY_ROBUST_TAIL_AND_HISTORY_STATE_EXTENSION.md`.

## Numerical gates

- `numerics/verify_robust_tangent_radius_law.py`
- `numerics/verify_relational_autonomous_laws.py`

The validators cover the fixed-energy/high-frequency no-go, numerical-radius formula, random one-copy and collective-POVM robust bounds, asymptotic sharpness, random dual-tail tests, weak-commutativity sharpness, finite-shift numerical radii, sine extremizers, and higher-harmonic cosine laws.

## Current open frontier — WP07

### 1. Nonlinear `R_lin=0` synthesis — highest priority

A rank-deficient baseline can support an exact smooth nonlinear family with a nonzero first-order off-diagonal tangent even though the affine tangent has zero physical radius. Second-order population/curvature restores positivity.

This is the main loophole left by the robust local theorem and is the natural mathematical model of coherent-sideband-style arbitrary waveform synthesis.

Required tasks:

1. construct the minimal exact family exhibiting `R_lin=0` and isolate its positivity mechanism;
2. derive the sharp relation between first-order high-gap coherence and second-order upper-level population/curvature;
3. determine which finite-amplitude operational metric admits a spectral-energy bound: trace distance, fidelity/Bures angle, Chernoff/hypothesis-testing error, or a finite-difference Fisher analogue;
4. test whether a curvature-weighted local law can be universal or whether finite distinguishability is indispensable;
5. extend any surviving statement to the globally stationary relational clock--signal setting;
6. search aggressively for collisions with quantum Hellinger/Bures geometry, boundary QFI, second-order perturbation theory of positive semidefinite matrices, quantum speed limits, phase estimation, and asymmetry robustness.

### 2. Collective-N mean-energy law

Determine whether entangled collective measurements can beat the one-copy envelope `G(Lbar)` per copy in the structured model.

### 3. Many-body cut theorem

Test whether temporal information across an autonomous bipartition obeys matched spectral-tail constraints on both sides of the cut.

### 4. Autonomous control resource

If interactions are not restricted to energy-conserving/covariant processing, identify the dynamical resource that must be charged: interaction norm, spectral diameter, action, power, or another invariant.

## Priority status

Targeted searches have not identified exact predecessors for WP02 robust tangent-radius Fisher survival, WP03/WP06 dual survival with arbitrary coherent baseline, or the WP04/WP05 autonomous Fisher-retention formulations. This is **not certification**. Priority remains unverified.

## Read first

1. `notes/WP06_NONSTATIONARY_ROBUST_TAIL_AND_HISTORY_STATE_EXTENSION.md`
2. `notes/WP05_EXACT_MEAN_ENERGY_AUTONOMOUS_RELATIONAL_RETENTION.md`
3. `notes/WP04_EXACT_HARD_CAP_AUTONOMOUS_RELATIONAL_RETENTION.md`
4. `notes/WP03_RELATIONAL_DUAL_ENERGY_SURVIVAL_LAW.md`
5. `notes/WP02_LOCAL_FISHER_NO_GO_AND_ROBUST_TANGENT_RADIUS_LAW.md`
6. `notes/WP01_FOUNDATIONAL_SCOPE_AND_PRIOR_ART_BOUNDARY.md`
7. `ROADMAP.md`
8. frozen parent handoff: `../grand_challenge/AGENTS.md`

## Documentation rule

Every material theorem, counterexample, priority collision, or killed conjecture must be recorded immediately in this directory and reflected in `README.md`, `AGENTS.md`, and `ROADMAP.md`. Do not depend on chat history. Keep Rev11 frozen and separately advertised until this branch reaches its own publication gate.
