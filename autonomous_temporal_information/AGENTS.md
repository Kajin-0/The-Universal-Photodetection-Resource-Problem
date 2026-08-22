# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

**Started:** 2026-08-22

This is a distinct post-Rev11 foundational program. The frozen Rev11 paper remains on `agent/temporal-information-resource-law` and must not be rewritten from this branch absent a concrete defect.

## Grand question

> When signal, clock/reference, controller, detector, and memory are all finite physical systems and no ideal externally timed operation is free, what resource constrains creation, transmission, and recovery of temporal information at frequency `nu`?

Research is analytical/theoretical, falsification-first, and documentation-first. Existing asymmetry, reference-frame, phase-estimation, WAY, and finite-clock results are infrastructure unless a genuinely new operational theorem is isolated.

## Current frontier

**WP04 — exact autonomous relational hard-cap retention law: analytic PASS.**

The new branch now has a coherent theorem hierarchy rather than only an exploratory question.

### WP01 — prior-art boundary

Established, not new:

- Marvian--Spekkens mode support and mode monotones;
- finite quantum reference frames / autonomous clocks;
- QFI as asymmetry resource;
- quantitative WAY tradeoffs;
- ordinary phase-estimation sine states / Heisenberg scaling;
- simply charging preparation/control energy.

### WP02 — local Fisher no-go and robust tangent radius

For arbitrary state synthesis, fixed baseline mean energy does **not** force local Fisher information to vanish at high Bohr frequency. A two-level family keeps `Tr F` fixed as `nu->infinity` while its physical linear tangent radius shrinks.

Define `R_lin` as the largest disk on which the two-quadrature linear tangent remains positive. For stationary `rho0` and exact positive-gap tangent `A_nu`,

`R_lin = 1 / w(rho0^(-1/2) A_nu rho0^(-1/2))`,

where `w` is numerical radius.

For any finite `N` and any joint POVM,

`(R_lin^2/4) [Tr F_N^(nu)/N] <= min(D_nu,U_nu) <= T(nu)`.

Hence

`Ebar+ >= (hbar nu R_lin^2/4)[Tr F_N^(nu)/N]`.

The fixed-energy/high-frequency counterexample asymptotically saturates this robust law.

Read:
`notes/WP02_LOCAL_FISHER_NO_GO_AND_ROBUST_TANGENT_RADIUS_LAW.md`.

### WP03 — globally stationary relational dual-survival law

Let clock `C` and signal `S` have separately stationary baseline `rho0`. Let the tangent exchange an exact gap:

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`.

Then `[H_C+H_S,A_nu]=0`: the entire parameter family is globally time-translation invariant. Temporal information is relational rather than global asymmetry.

Define

`K_N(nu)=(R_lin^2/4)[Tr F_N^(nu)/N]`.

Applying WP02 from each local-generator viewpoint gives, for arbitrary finite-copy collective measurements,

`K_N(nu) <= min{T_C(nu),T_S(nu)}`.

Thus both sides must supply the gap:

`Ebar_C^+ >= hbar nu K_N`,

`Ebar_S^+ >= hbar nu K_N`,

and

`Ebar_C^+ + Ebar_S^+ >= 2 hbar nu K_N`.

The coefficient `2` is asymptotically sharp. In the symmetric two-qubit exchange model, weak SLD commutativity makes the SLD/Holevo limit asymptotically attainable by collective measurements, giving simultaneous equality in both tails and in the total-energy law.

All-mode lattice budget:

`sum_(k>=1) K_N(k) <= min(nbar_C,nbar_S)`.

Read:
`notes/WP03_RELATIONAL_DUAL_ENERGY_SURVIVAL_LAW.md`.

### WP04 — exact hard total-energy cap law

For a structured relative-time experiment inside a globally stationary fixed total-excitation shell

`N_C+N_S=L`,

the exchange coordinate is a finite chain with shift

`V_L=sum_(n=0)^(L-1)|n+1><n|`.

For one fixed one-copy POVM,

`R_M(k)=int |Tr(V_L^k X_y)|^2 p(dy)`.

Classical finite-shift mathematics gives

`w(V_L^k)=cos{pi/[floor(L/k)+2]}`.

Therefore the exact arbitrary-POVM hard-cap law is

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

With relative frequency `nu=k omega0` and hard total-energy cap `E_max=hbar omega0 L`,

`R_M(nu) <= cos^2{pi/[floor(E_max/(hbar nu))+2]}`.

For the fundamental mode,

`E_max >= hbar nu [pi/arccos(sqrt R)-2]`,

so near perfect retention

`E_max >= pi hbar nu / sqrt(1-R) [1+o(1)]`.

The constant and exponent are exactly sharp. A globally stationary sine-chain history state

`|Psi_L>=sum_(n=0)^L sqrt[2/(L+2)] sin[(n+1)pi/(L+2)] |L-n>_C|n>_S`

with the canonical relative-phase POVM attains equality.

The sine state / finite-shift constant is established phase-estimation prior art. Candidate novelty is the exact **Fisher-retention** interpretation for a globally stationary autonomous clock--signal record.

Read:
`notes/WP04_EXACT_HARD_CAP_AUTONOMOUS_RELATIONAL_RETENTION.md`.

## Numerical gates

- `numerics/verify_robust_tangent_radius_law.py`
- `numerics/verify_relational_autonomous_laws.py`

The second validator checks random dual-tail POVMs, weak-commutativity sharpness, finite-shift numerical radii, sine extremizers, and higher-harmonic cosine laws.

## Current open frontier — WP05

Highest-value unresolved problems:

1. **Sharp mean-total-energy law.** Hard cap is solved exactly. Mean total energy only is harder because posterior energy can vary by measurement outcome. Determine the optimal asymptotic constant for Fisher retention, not ordinary phase-error variance.
2. **Pre-existing relational coherence.** Extend beyond separately stationary baselines to general Page--Wootters/history states that already contain relational coherence before the unknown parameter is introduced.
3. **Nonlinear `R_lin=0` synthesis.** Find the weakest finite-amplitude/curvature/control resource that restores a theorem for coherent-sideband-type families.
4. **Many-body cut law.** Test whether any temporal-information mode across a bipartition obeys a dual energy-exchange survival law on both sides of the cut.
5. **Autonomous control resource.** If interactions are not restricted to energy-conserving/covariant processing, identify the generator/action resource that must be charged.

Mean-energy phase-estimation results (e.g. Berry--Hall--Zwierz--Wiseman, PRA 86, 053813 (2012)) are prior art. They may provide mathematical tools, but their phase-error metrics must not be silently identified with the present averaged squared-posterior Fisher-retention functional.

## Priority status

Targeted searches have not identified exact predecessors for WP02 robust tangent-radius Fisher survival, WP03 dual clock/signal survival, or the WP04 Fisher-retention formulation. This is **not certification**. Priority remains unverified.

## Read first

1. `notes/WP04_EXACT_HARD_CAP_AUTONOMOUS_RELATIONAL_RETENTION.md`
2. `notes/WP03_RELATIONAL_DUAL_ENERGY_SURVIVAL_LAW.md`
3. `notes/WP02_LOCAL_FISHER_NO_GO_AND_ROBUST_TANGENT_RADIUS_LAW.md`
4. `notes/WP01_FOUNDATIONAL_SCOPE_AND_PRIOR_ART_BOUNDARY.md`
5. `ROADMAP.md`
6. frozen parent handoff: `../grand_challenge/AGENTS.md`

## Documentation rule

Every material theorem, counterexample, priority collision, or killed conjecture must be recorded immediately in this directory and reflected in `ROADMAP.md`. Do not depend on chat history. Keep Rev11 frozen and separately advertised until this branch reaches its own publication gate.
