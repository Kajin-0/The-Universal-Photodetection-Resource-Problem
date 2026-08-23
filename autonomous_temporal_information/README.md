# Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

The frozen Rev11 paper remains untouched on `agent/temporal-information-resource-law`.

## Grand challenge

Determine the physical resource that constrains temporal information when clock/reference, signal, controller, detector, and memory are finite internal systems and no ideal external timing operation is supplied for free.

## Current theorem hierarchy

### WP02 — finite-radius robust survival

For exact temporal gap `nu`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N^(nu)/N] <= T(nu)`.

### WP03 / WP06 — autonomous relational dual survival

For a globally stationary exact clock--signal exchange tangent,

`K_N=(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`,

including arbitrary pre-existing Page--Wootters/history-state coherence after WP06.

### WP04 / WP05 — exact structured autonomous retention

Hard total-excitation cap:

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

Mean excitation:

`R_M(1) <= (1-lambda)g_m+lambda g_(m+1)`.

The near-lossless coefficient `pi` is exactly sharp.

### WP07 / WP08 — zero-radius quadratic synthesis

One baseline-empty endpoint:

`Tr F_N/N <= J <= Delta T_U(0)`.

Multimode same-record weighted sum:

`sum_k w_k Tr F_(N,k)/N <= sum_k w_k Delta_k T_k(0)`.

### WP09 — bilateral zero-radius Minkowski law

`sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

For clean empty endpoints,

`Tr F_N/N <= [sqrt(Delta T_+)+sqrt(Delta T_-)]^2`.

The factor-two departure from additive synthesis is exactly sharp.

### WP10 — sharp one-sided mixed survival+synthesis

For energy-invariant support and one synthesized orientation,

`Tr F_N/N <= 4T_pre/R_B^2 + Delta T_syn(0)`.

The corresponding `hbar nu/4` local energy/action coefficient is exactly sharp.

### WP11 — noncommuting-support shorted-endpoint law

For arbitrary coherent support,

`B=PAP`, `K_+=QAP`, `K_-=QA^dagger P`,

and

`sqrt[Tr F_N/N]`

`<= min{sqrt(J_B^+ + J_+) + sqrt(J_-),`

`       sqrt(J_B^- + J_-) + sqrt(J_+)}`.

Compressed energy endpoint projectors require shorting/principal-angle factors. A four-level exact-gap model proves that omitting this geometry yields an actually false observable Fisher bound.

### WP12 — exact shared-curvature allocation

Second-order positivity gives

`Z_+ + Z_- <= C_Delta`.

For

`Phi_a(C;R_+,R_-)=sup [sqrt(a+Tr Z_+) + sqrt(Tr Z_-)]^2`,

one has

`Phi_a=inf_(0<eta<1){a/eta+h_(1/eta,1/(1-eta))}`,

where `h_(alpha,beta)` is an SDP with dual

`min_(W>=0) Tr(CW)`

subject to

`R_+ W R_+>=alpha R_+`,

`R_- W R_->=beta R_-`.

### WP13 — positive spectral-action allocation

For one positive kernel cost operator `G`,

`A_G^(2)=(1/4)Tr(G C_Delta)`.

With restricted costs `g_+,g_-`,

`g_+J_+ + g_-J_- <= 4A_G^(2)`.

Pure bilateral synthesis has harmonic effective price

`(1/g_+ + 1/g_-)^(-1)`.

Clean equal gap costs give the sharp `hbar nu/8` coefficient; one-sided synthesis gives `hbar nu/4`.

### WP14 — rank-one curvature-metric principal-angle law

For rank-one synthesized ranges, short `C` to their span and define inverse-curvature capacities `s_u,s_v` and whitened overlap `c`.

The exact feasible frontier is

`y_max(x)=s_v[1-x/s_u]/[1-(1-c^2)x/s_u]`.

The relevant angle is in the inverse shorted-curvature metric, not ordinary Hilbert-space geometry.

### WP15 — exact shared-kernel qutrit common-record optimum

For the WP12 qutrit benchmark,

`physical resource =12`,

`Tr F_Q=43/4`,

but

`boxed: sup_(one-copy POVMs) Tr F_1=55/8`.

The upper bound is an explicit optimal quadratic witness; a regular projective sequence approaches the value. Thus physical resource, SLD geometry, and common-record accessibility are genuinely distinct layers.

### WP16 — generic rank-one-kernel common-record Minkowski law

Let

`rho0=P/r`, `rank(Q)=1`,

and

`A=[[B,b],[a^dagger,0]]`.

Define the exact singular boundary coupling

`kappa=||a||^2+||b||^2+2|a^dagger b|`

and the support-only common-record functional `R(B)`.

Then every one-copy arbitrary POVM obeys

`boxed: sqrt(Tr F_1)<=sqrt(R(B))+sqrt(r kappa)`.

For qutrits, `r=2`, `Tr B=0`, and

`R(B)=4w(B)^2`,

so

`boxed: Tr F_1<=[2w(B)+sqrt(2kappa)]^2`.

The signed three-cycle

`A=[[0,1,0],[0,0,-1],[1,0,0]]`

saturates the bound exactly at `Tr F_1=9`. The naive additive law would give only `5`, so regular and singular score amplitudes must combine by Minkowski geometry.

A second model with the same `(R(B),kappa)` has the independent WP11 ceiling `6<9`; therefore those two scalars do not determine the exact model-specific optimum. Additional phase/orientation geometry is irreducible.

WP16 also gives the exact common-record convex dual

`F_CR(rho,A)=inf_Y Tr Y`

subject to

`|<phi|A|phi>|^2<=<phi|rho|phi><phi|Y|phi>`

for every vector, equivalently

`lambda rho+lambda^(-1)Y >= e^(i theta)A+e^(-i theta)A^dagger`

for all `lambda>0,theta`. For positive interior witnesses this is a generalized weighted numerical-radius condition.

### WP17 — operator/action Pareto redundancy no-go

A generic “WP14 operator geometry + WP13 scalar action” Pareto theorem is not intrinsically new.

If exact `C_Delta` is retained, `Tr(GC_Delta)` is a derived linear statistic and adds no constraint.

If `C_Delta` is discarded and only the action budget is kept, optimization over unknown positive curvature collapses exactly to WP13.

A nontrivial Pareto problem requires an additional independent operator constraint not currently supplied by the physical model. This direction is killed unless such physics appears.

### WP18 — sharp autonomous dual synthesis-action law

Return to a globally stationary exact exchange:

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`.

In the clean zero-radius pure-boundary regime, define positive local absolute-gap synthesis actions

`A_S^(2)=(hbar nu/4)[Delta T_(S,+)+Delta T_(S,-)]`,

`A_C^(2)=(hbar nu/4)[Delta T_(C,+)+Delta T_(C,-)]`.

For every finite `N` and arbitrary collective POVM,

`boxed: A_C^(2)+A_S^(2) >= (hbar nu/4)[Tr F_N/N]`

in the bilateral case.

If only one support orientation is synthesized, the sharper law is

`boxed: A_C^(2)+A_S^(2) >= (hbar nu/2)[Tr F_N/N]`.

Both constants are exact.

Bilateral extremizer: the fixed-total-energy shell

`|2_C,0_S>, |1_C,1_S>, |0_C,2_S>`

with baseline `|1,1>` and exchange tangent

`A_nu=c(|0,2><1,1|+|1,1><2,0|)`.

A Fourier measurement gives `Tr F_1=4c^2` and saturates the total `hbar nu/4` coefficient. The entire nonlinear family remains in one total-energy eigenspace, so global time-translation asymmetry is identically zero.

The one-sided fixed-total-energy two-state exchange saturates the `hbar nu/2` coefficient.

WP18 therefore closes the central `R_lin=0` loophole left by WP03 in a sharp autonomous setting: relative temporal information still requires matched resources on both sides, but the resource moves from zeroth-order survival to second-order positive exchange action.

## Current frontier

Highest-value remaining targets:

1. extend WP18 beyond clean baseline-empty endpoints using WP11/WP12 shorted geometry on **both** clock and signal sides;
2. determine whether one joint curvature allocation couples the two local action bounds more tightly than simple addition;
3. derive a multi-gap autonomous synthesis-action budget;
4. perform a hostile priority/significance audit of WP03+WP18 against Page--Wootters, relative-phase metrology, asymmetry/resource theories, quantitative WAY, and 2025--2026 energy-constrained metrology;
5. only then decide whether this post-Rev11 program warrants a new foundational manuscript.

## Validation

Independent validators now include:

- `verify_robust_tangent_radius_law.py`
- `verify_relational_autonomous_laws.py`
- `verify_nonlinear_zero_radius_law.py`
- `verify_quadratic_synthesis_sum_rule.py`
- `verify_bilateral_synthesis_minkowski_law.py`
- `verify_one_sided_mixed_survival_synthesis_law.py`
- `verify_shorted_endpoint_master_law.py`
- `verify_operator_curvature_allocation_law.py`
- `verify_positive_spectral_action_allocation_law.py`
- `verify_rank_one_curvature_metric_angle_law.py`
- `verify_exact_common_record_fisher_supremum.py`
- `verify_rank_one_kernel_common_record_minkowski.py`
- `verify_autonomous_dual_synthesis_action_law.py`

## Priority discipline

Page--Wootters relational time, asymmetry/reference-frame resource theory, energy-conserving exchange, numerical-radius/Ando theory, POVM convex duality, shorted operators, SDP/SOCP duality, weighted principal angles, Gill--Massar/Holevo compatibility, PSD-cone curvature, rank-changing QFI/Bures geometry, and energy-constrained metrology are established. Candidate novelty is restricted to the **frequency-resolved rank-changing temporal-resource bridge theorems** and their sharp autonomous two-sided consequences.

Priority remains **unverified, not certified**.

Read `AGENTS.md`, `ROADMAP.md`, and WP01--WP18 before continuing. Record every material theorem, counterexample, priority collision, or killed conjecture immediately; do not rely on chat history.
