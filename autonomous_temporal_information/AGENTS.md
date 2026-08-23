# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

**Started:** 2026-08-22

This is a distinct post-Rev11 foundational program. The frozen Rev11 paper remains on `agent/temporal-information-resource-law` and must not be rewritten from this branch absent a concrete defect.

## Grand question

> When signal, clock/reference, controller, detector, and memory are all finite physical systems and no ideal externally timed operation is free, what resource constrains creation, transmission, and recovery of temporal information at frequency `nu`?

Research is analytical/theoretical, falsification-first, and documentation-first. Existing asymmetry, reference-frame, phase-estimation, WAY, Page--Wootters, PSD-cone geometry, singular QFI/Bures geometry, Gaussian displacement/Holevo theory, and finite-clock results are infrastructure unless a genuinely new operational theorem is isolated.

## Current frontier

**WP08 — quadratic spectral-synthesis sum and energy law: analytic PASS.**

The highest-value unresolved target is now the **mixed-endpoint exact-gap problem**: combine WP06 pre-existing spectral support with WP07/WP08 quadratic spectral synthesis in one sharp arbitrary-POVM law.

The theorem hierarchy is:

`finite-radius Fisher x tangent robustness <= pre-existing spectral survival`,

while at a rank-deficient boundary,

`zero-radius two-quadrature Fisher <= quadratic spectral population synthesis`.

For several newly synthesized orthogonal modes, the boundary law adds modewise and admits a sharp frequency/energy weighting.

For autonomous relations, exchange resource remains tied to both sides of the clock--signal cut.

## Completed work packages

### WP01 — prior-art boundary

Do not claim novelty for:

- modes of asymmetry or generic coherence monotones;
- QFI/Fisher geometry as asymmetry;
- finite quantum reference frames, autonomous clocks, Page--Wootters time, or quantitative WAY per se;
- standard phase-estimation sine states / Heisenberg scaling;
- second-order tangent geometry of the PSD cone;
- rank-changing QFI/Bures Hessian corrections;
- Gaussian complex-displacement estimation, heterodyne/double-homodyne, or Holevo/RLD/SLD bounds;
- generic linear quantum waveform-estimation bounds.

The candidate contribution must be a distinct **operational temporal-information resource law**.

### WP02 — local Fisher no-go and robust tangent radius

Fixed baseline mean energy does not bound arbitrarily high-frequency local Fisher information under unrestricted state synthesis. The missing resource is the physical radius of the affine tangent.

For exact gap `nu`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N^(nu)/N] <= min(D_nu,U_nu) <= T(nu)`.

Hence

`Ebar+ >= (hbar nu R_lin^2/4)[Tr F_N^(nu)/N]`.

The fixed-energy/high-frequency counterexample asymptotically saturates.

Read:
`notes/WP02_LOCAL_FISHER_NO_GO_AND_ROBUST_TANGENT_RADIUS_LAW.md`.

### WP03 — globally stationary relational dual-survival law

For

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`,

define

`K_N=(R_lin^2/4)[Tr F_N/N]`.

Then

`K_N(nu) <= min{T_C(nu),T_S(nu)}`

for arbitrary finite-copy collective measurements, so

`Ebar_C^+ + Ebar_S^+ >= 2 hbar nu K_N`.

The coefficient `2` is asymptotically sharp.

Read:
`notes/WP03_RELATIONAL_DUAL_ENERGY_SURVIVAL_LAW.md`.

### WP04 — exact hard total-energy cap law

For structured globally stationary relative-time experiments with

`N_C+N_S<=L`,

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

At the fundamental mode,

`E_max >= hbar nu[pi/arccos(sqrt R)-2]`,

with near-unit asymptotic

`E_max >= pi hbar nu/sqrt(1-R)[1+o(1)]`.

Sine-chain history states attain equality.

Read:
`notes/WP04_EXACT_HARD_CAP_AUTONOMOUS_RELATIONAL_RETENTION.md`.

### WP05 — exact mean-total-energy law

For

`g_L=cos^2[pi/(L+2)]`,

`Lbar=m+lambda`,

the exact one-copy envelope is

`R_M(1) <= (1-lambda)g_m+lambda g_(m+1)`.

Adjacent-shell sine-chain mixtures attain equality, giving the same sharp near-unit coefficient `pi` under a mean total-energy constraint.

Read:
`notes/WP05_EXACT_MEAN_ENERGY_AUTONOMOUS_RELATIONAL_RETENTION.md`.

### WP06 — arbitrary coherent baseline / history-state extension

Baseline stationarity is unnecessary for the finite-radius robust theorem.

For arbitrary `rho`, positive `R_lin`, tangent range projector `P_U`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N/N] <= Tr(P_U rho)`.

Thus globally stationary Page--Wootters/history states with pre-existing local energy coherence do not evade the relational dual-tail law.

Read:
`notes/WP06_NONSTATIONARY_ROBUST_TAIL_AND_HISTORY_STATE_EXTENSION.md`.

### WP07 — nonlinear zero-radius spectral synthesis

Let `P=supp(rho0)` and suppose a two-quadrature complex tangent enters a baseline-empty endpoint sector:

`A=P_U A P`, `P_U P=0`.

Define

`J(A|rho0)=Tr(A rho0^+ A^dagger)`.

A direct weighted Hilbert--Schmidt Cauchy--Schwarz proof gives, for **every finite N and every entangled collective POVM**,

`Tr F_N/N <= J(A|rho0)`.

Established second-order PSD-cone geometry applied to the two real quadratures gives

`J(A|rho0) <= Delta T_U(0)`,

where

`T_U(x,y)=Tr[P_U rho(x,y)]`.

Hence

`boxed: Tr F_N/N <= J(A|rho0) <= Delta T_U(0)`.

Equivalently,

`boxed: (1/4)[Tr F_N/N] <= (1/4)Delta T_U(0)`.

The minimal pure qubit saturates both inequalities at one copy using a fixed four-outcome equatorial POVM.

The scalar one-parameter relation `F_Q<=2T_U''` is close to established rank-changing QFI/Bures geometry and must not be advertised as the novelty.

The inherited coherent-sideband no-go exactly saturates the sharper operational coefficient when promoted to two quadratures:

`alpha_sb=(A/2)(x+i y)`,

`Delta n_sb=Nbar`,

`Tr F_het=Nbar`.

A finite-amplitude two-endpoint `pi` phase-pair law also gives

`D_tr^2/4 <= min{T_C(nu),T_S(nu)}`

and

`Ebar_C^+ + Ebar_S^+ >= (hbar nu/2)D_tr^2`.

Read:
`notes/WP07_NONLINEAR_ZERO_RADIUS_CURVATURE_AND_FINITE_AMPLITUDE_LAW.md`.

### WP08 — quadratic spectral-synthesis sum and energy law

Let `{P_k}` be mutually orthogonal baseline-empty endpoint sectors, with mode parameters `(x_k,y_k)` and

`A_k=P_k A_k P`.

For a **single fixed POVM** on `N` copies, let `F_(N,k)` be the `2 x 2` Fisher block for mode `k`. WP07 applies modewise to that same record:

`Tr F_(N,k)/N <= Delta_k T_k(0)`.

Therefore, for arbitrary nonnegative weights `w_k`,

`boxed: sum_k w_k [Tr F_(N,k)/N] <= sum_k w_k Delta_k T_k(0)`.

Define

`S_syn^(2)=(1/4)sum_k Delta_k T_k(0)`.

Then

`sum_k Tr F_(N,k)/(4N) <= S_syn^(2)`.

With temporal-gap weights,

`E_gap,syn^(2)=(hbar/4)sum_k nu_k Delta_k T_k(0)`,

so

`boxed: sum_k hbar nu_k [Tr F_(N,k)/(4N)] <= E_gap,syn^(2)`.

This is a **quadratic spectral-synthesis budget**. It does not use baseline mean energy and should not be replaced blindly by signed total-energy curvature; it counts the positive endpoint populations synthesized at second order.

For mutually orthogonal coherent sideband modes

`alpha_k=g_k(x_k+i y_k)`,

`Delta_k n_k=4|g_k|^2`.

Multimode heterodyne gives

`Tr F_k=4|g_k|^2`,

so every mode and every nonnegative weighted sum are saturated simultaneously by one fixed measurement.

With physical photon-energy weights `hbar omega_k`,

`sum_k (hbar omega_k/4)Tr F_k`

`= (1/4)sum_k Delta_k E_k(0)`.

Thus the earlier coherent-waveform loophole is quantitatively closed in the correct variable: newly synthesized sideband population/energy.

Coherent displacement/Holevo/heterodyne theory is prior art; candidate novelty is the frequency-resolved resource sum law and its connection to the baseline-energy no-go.

Read:
`notes/WP08_QUADRATIC_SPECTRAL_SYNTHESIS_SUM_AND_ENERGY_LAW.md`.

## Numerical gates

- `numerics/verify_robust_tangent_radius_law.py`
- `numerics/verify_relational_autonomous_laws.py`
- `numerics/verify_nonlinear_zero_radius_law.py`
- `numerics/verify_quadratic_synthesis_sum_rule.py`

WP08 validation covers same-record random mode sums, arbitrary random positive weights, random two-copy collective POVMs, and exact multimode coherent heterodyne population/energy saturation.

## Current open frontier — mixed endpoint theorem

### 1. General exact-gap support/resource geometry — highest priority

A general tangent can combine:

- a finite-radius pre-existing component;
- support-to-kernel synthesis;
- kernel-to-support synthesis in the opposite endpoint orientation.

The simple support projection of an exact energy-gap operator need not itself remain an exact gap when `supp(rho)` does not commute with the Hamiltonian. Do **not** assume that the mixed problem decomposes into independent energy-gap operators by projecting with `P=supp(rho)`.

The correct theorem may need an operator-valued resource geometry involving both the energy endpoint projector and the baseline support geometry.

### 2. Score-space interference / scalar-additivity test

For `A=A_1+A_2`, an arbitrary POVM has score amplitude

`z_y=Tr(A_1M_y)+Tr(A_2M_y)`.

Cross terms in `|z_y|^2/p_y` need not vanish even if the operator pieces are Hilbert--Schmidt orthogonal.

Required work:

- derive the best universal Minkowski/Gram bound;
- search for explicit counterexamples to naive additive scalar formulas;
- determine whether a matrix-valued resource, shorted operator, or principal-angle quantity is the natural sharp object;
- preserve WP06 and WP07 coefficients in their pure limits.

### 3. Full finite-amplitude phase orbit

Extend beyond binary Helstrom discrimination to continuous relative-time recovery with support change. Seek a phase-orbit functional that reduces locally to WP07 and recovers WP04/WP05 near-unit divergence where appropriate.

### 4. Gaussian families beyond displacement

WP08 solves multimode coherent displacement synthesis sharply. Test covariance-changing Gaussian families, squeezing, and mixed Gaussian baselines.

### 5. Autonomous synthesis/control law

When the parameter-dependent sideband/resource sector is generated dynamically, identify what positive interaction/action resource supplies the WP07/WP08 curvature.

### 6. Collective-N mean-energy retention / many-body cut law

These remain secondary after the mixed-endpoint problem.

## Priority status

Targeted searches have not identified exact predecessors for WP02 robust tangent-radius Fisher survival, WP03/WP06 dual survival with arbitrary coherent baseline, or the WP07/WP08 finite-copy frequency-resolved synthesis laws. This is **not certification**. Priority remains unverified.

## Read first

1. `notes/WP08_QUADRATIC_SPECTRAL_SYNTHESIS_SUM_AND_ENERGY_LAW.md`
2. `notes/WP07_NONLINEAR_ZERO_RADIUS_CURVATURE_AND_FINITE_AMPLITUDE_LAW.md`
3. `notes/WP06_NONSTATIONARY_ROBUST_TAIL_AND_HISTORY_STATE_EXTENSION.md`
4. `notes/WP05_EXACT_MEAN_ENERGY_AUTONOMOUS_RELATIONAL_RETENTION.md`
5. `notes/WP04_EXACT_HARD_CAP_AUTONOMOUS_RELATIONAL_RETENTION.md`
6. `notes/WP03_RELATIONAL_DUAL_ENERGY_SURVIVAL_LAW.md`
7. `notes/WP02_LOCAL_FISHER_NO_GO_AND_ROBUST_TANGENT_RADIUS_LAW.md`
8. `notes/WP01_FOUNDATIONAL_SCOPE_AND_PRIOR_ART_BOUNDARY.md`
9. `ROADMAP.md`
10. inherited coherent-sideband no-go: `../grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`

## Documentation rule

Every material theorem, counterexample, priority collision, or killed conjecture must be recorded immediately in this directory and reflected in `README.md`, `AGENTS.md`, and `ROADMAP.md`. Do not depend on chat history. Keep Rev11 frozen and separately advertised until this branch reaches its own publication gate.
