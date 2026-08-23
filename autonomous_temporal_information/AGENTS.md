# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

**Started:** 2026-08-22

This is a distinct post-Rev11 foundational program. The frozen Rev11 paper remains on `agent/temporal-information-resource-law` and must not be rewritten from this branch absent a concrete defect.

## Grand question

> When signal, clock/reference, controller, detector, and memory are all finite physical systems and no ideal externally timed operation is free, what resource constrains creation, transmission, and recovery of temporal information at frequency `nu`?

Research is analytical/theoretical, falsification-first, and documentation-first. Existing asymmetry, reference-frame, phase-estimation, WAY, Page--Wootters, PSD-cone geometry, and finite-clock results are infrastructure unless a genuinely new operational theorem is isolated.

## Current frontier

**WP07 — nonlinear zero-radius curvature and finite-amplitude laws: analytic PASS in the support-to-kernel/two-sector settings.**

The next target is a **unified interior/boundary law** combining WP06 pre-existing spectral support with WP07 quadratic spectral synthesis.

The theorem hierarchy is now:

`finite-radius local Fisher x tangent robustness <= pre-existing spectral survival`,

while at a rank-deficient boundary,

`zero-radius local Fisher <= quadratic creation of previously absent spectral population`.

For autonomous relations, the required exchange resource remains tied to both sides of the clock--signal cut.

For the structured globally stationary relative-time model, the finite-resource retention law is exactly solved under both hard and mean total energy.

## Completed work packages

### WP01 — prior-art boundary

Established, not new:

- Marvian--Spekkens modes of asymmetry and mode monotones;
- QFI/Fisher geometry as an asymmetry resource;
- finite quantum reference frames and autonomous clocks;
- Page--Wootters relational time;
- quantitative WAY tradeoffs;
- ordinary phase-estimation sine states / Heisenberg scaling;
- generic PSD-cone curvature and boundary-QFI geometry;
- simply charging preparation/control energy.

The program must produce a quantitative **operational temporal-information performance law**, not a repackaging of mode support or standard phase estimation.

### WP02 — local Fisher no-go and robust tangent radius

For arbitrary state synthesis, fixed baseline mean energy does **not** force local Fisher information to vanish at high Bohr frequency. A two-level family keeps `Tr F` fixed as `nu->infinity` while its physical linear tangent radius shrinks.

Define `R_lin` as the largest disk on which the two-quadrature linear tangent remains positive. For stationary `rho0` and exact positive-gap tangent `A_nu`,

`R_lin = 1 / w(rho0^(-1/2) A_nu rho0^(-1/2))`.

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

`Ebar_C^+ + Ebar_S^+ >= 2 hbar nu K_N`.

The coefficient `2` is asymptotically sharp under collective measurements.

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

Globally stationary sine-chain history states with canonical relative-phase readout attain equality.

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

Equality is constructive via adjacent-shell sine-chain extremizers.

Therefore

`Ebar_C^+ + Ebar_S^+ >= pi hbar nu/sqrt(1-R)[1+o(1)]`

with leading constant `pi` sharp in the one-copy structured mean-energy problem.

Read:
`notes/WP05_EXACT_MEAN_ENERGY_AUTONOMOUS_RELATIONAL_RETENTION.md`.

### WP06 — arbitrary coherent baseline / history-state extension

The robust tail theorem does not require baseline stationarity.

For arbitrary density operator `rho`, positive tangent radius `R_lin`, and tangent `A`, one obtains for every finite `N` and arbitrary collective POVM

`(R_lin^2/4)[Tr F_N/N] <= Tr(P_U rho)`

whenever the range of `A` lies in resource projector `P_U`.

For an exact positive gap, this is the same upper-tail energy-survival theorem as WP02 without any commutation assumption on `rho`.

Consequently the relational law survives a globally stationary but locally coherent history state:

`[rho_CS,H_C+H_S]=0`,

while generally

`[rho_CS,H_C] != 0`, `[rho_CS,H_S] != 0`.

Pre-existing relational clock coherence therefore does not evade

`K_N(nu) <= min{T_C(nu),T_S(nu)}`.

Read:
`notes/WP06_NONSTATIONARY_ROBUST_TAIL_AND_HISTORY_STATE_EXTENSION.md`.

### WP07 — nonlinear `R_lin=0` curvature and finite-amplitude laws

Let

`rho(theta)=rho0+theta D+(theta^2/2)C+o(theta^2)`

be a two-sided `C^2` physical curve at a rank-deficient baseline. Let

`P=supp(rho0)`, `Q=I-P`, `R=P rho0 P`, `K=QDP`.

Second-order PSD-cone geometry gives the necessary condition

`Q C Q >= 2 K R^(-1)K^dagger`.

This matrix geometry is prior art. The temporal-resource consequence is:

if the first-order tangent enters a previously empty upper resource sector `P_U<=Q`, then

`F_Q(0) <= 2 T_U''(0)`.

For arbitrary finite-copy collective readout,

`(1/4)[F_N(0)/N] <= J_U^(2)`,

`J_U^(2)=T_U''(0)/2`.

In multiparameter form,

`F_N(0)/N <= 2 Hess[T_U](0)`.

Thus the zero-radius sector is paid for by **quadratic spectral synthesis** rather than baseline population.

The old coherent-sideband no-go saturates the coefficient exactly:

`n_sb(epsilon)=epsilon^2 Nbar/4`,

`F_Q=Nbar=2 n_sb''(0)`.

A complementary finite-amplitude two-endpoint phase experiment uses block positivity:

`||C||_1^2 <= q_D q_U`.

For a relative pi phase flip,

`D_tr=2||C||_1`,

hence

`D_tr^2/4 <= min(q_D,q_U)`.

In an exact autonomous exchange pair,

`D_tr^2/4 <= min{T_C(nu),T_S(nu)}`,

so

`Ebar_C^+ + Ebar_S^+ >= (hbar nu/2)D_tr^2`.

The PSD-cone, block-coherence, and Helstrom ingredients are prior art; candidate novelty is the frequency-resolved autonomous resource interpretation.

Read:
`notes/WP07_NONLINEAR_ZERO_RADIUS_CURVATURE_AND_FINITE_AMPLITUDE_LAW.md`.

## Numerical gates

- `numerics/verify_robust_tangent_radius_law.py`
- `numerics/verify_relational_autonomous_laws.py`
- `numerics/verify_nonlinear_zero_radius_law.py`

The validators cover the fixed-energy/high-frequency no-go, random robust-tail POVMs, finite-copy collective readout, dual-tail tests, weak-commutativity sharpness, finite-shift numerical radii, sine extremizers, higher-harmonic cosine laws, random zero-radius curvature saturation, two-quadrature equality, random block-coherence bounds, phase-flip trace distance, and the coherent-sideband curvature coefficient.

## Current open frontier — unified interior/boundary theorem

### 1. Exact-gap support decomposition — highest priority

For a general exact-gap tangent at an arbitrary baseline, split the information-bearing operator into:

- support-to-support pieces, which use pre-existing spectral resource and should reduce to WP06;
- support-to-kernel pieces, which synthesize a previously absent sector and should reduce to WP07.

Seek one invariant theorem that combines these contributions without an arbitrary case split or double counting.

### 2. Full finite-amplitude phase orbit

WP07's binary phase-pair theorem is operational but does not reproduce the sharp continuous-time retention divergence of WP04/WP05. Determine the optimal resource law for a complete phase orbit / relative-time estimation task when support can change nonlinearly.

### 3. Bosonic coherent-sideband theorem

Promote the WP14/WP07 consistency check into a general statement for coherent or Gaussian sideband synthesis using sideband number/energy creation, including multiple sidebands and arbitrary phase-sensitive POVMs.

### 4. Collective-N mean-energy retention

Determine whether entangled collective measurements can beat the one-copy envelope `G(Lbar)` per copy in the structured model.

### 5. Many-body cut theorem

Test whether temporal information across an autonomous bipartition obeys matched spectral constraints on both sides of the cut.

### 6. Autonomous control resource

If interactions are not restricted to energy-conserving/covariant processing, identify the dynamical resource that must be charged: interaction norm, spectral diameter, action, power, or another invariant.

## Priority status

Targeted searches have not identified exact predecessors for WP02 robust tangent-radius Fisher survival, WP03/WP06 dual survival with arbitrary coherent baseline, WP04/WP05 autonomous Fisher-retention formulations, or the specific WP07 frequency-resolved Fisher-versus-spectral-synthesis consequence. This is **not certification**. Priority remains unverified.

## Read first

1. `notes/WP07_NONLINEAR_ZERO_RADIUS_CURVATURE_AND_FINITE_AMPLITUDE_LAW.md`
2. `notes/WP06_NONSTATIONARY_ROBUST_TAIL_AND_HISTORY_STATE_EXTENSION.md`
3. `notes/WP05_EXACT_MEAN_ENERGY_AUTONOMOUS_RELATIONAL_RETENTION.md`
4. `notes/WP04_EXACT_HARD_CAP_AUTONOMOUS_RELATIONAL_RETENTION.md`
5. `notes/WP03_RELATIONAL_DUAL_ENERGY_SURVIVAL_LAW.md`
6. `notes/WP02_LOCAL_FISHER_NO_GO_AND_ROBUST_TANGENT_RADIUS_LAW.md`
7. `notes/WP01_FOUNDATIONAL_SCOPE_AND_PRIOR_ART_BOUNDARY.md`
8. `ROADMAP.md`
9. inherited coherent-sideband no-go: `../grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`
10. frozen parent handoff: `../grand_challenge/AGENTS.md`

## Documentation rule

Every material theorem, counterexample, priority collision, or killed conjecture must be recorded immediately in this directory and reflected in `README.md`, `AGENTS.md`, and `ROADMAP.md`. Do not depend on chat history. Keep Rev11 frozen and separately advertised until this branch reaches its own publication gate.
