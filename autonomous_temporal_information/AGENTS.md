# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

**Started:** 2026-08-22

The frozen Rev11 paper remains on `agent/temporal-information-resource-law` and must not be rewritten absent a concrete defect.

## Grand question

> When signal, clock/reference, controller, detector, and memory are finite physical systems and no ideal externally timed operation is free, what resource constrains creation, transmission, and recovery of temporal information at frequency `nu`?

Research is analytical/theoretical, falsification-first, and documentation-first. Standard asymmetry/reference-frame theory, phase estimation, WAY, Page--Wootters, PSD-cone geometry, singular QFI/Bures geometry, shorted operators, principal angles, SDP/SOCP theory, energy-constrained metrology, Gaussian metrology, and Holevo compatibility are infrastructure unless a distinct operational temporal-information theorem is isolated.

## Current status

**WP14 — rank-one curvature-metric principal-angle law: analytic PASS.**

The local resource hierarchy now has four layers:

1. **pre-existing support survival** weighted by finite tangent robustness;
2. **second-order kernel curvature** when the physical tangent radius collapses to zero;
3. **positive spectral action** obtained by pricing shared curvature with one positive endpoint-cost operator;
4. **operator overlap geometry** determining how multiple synthesized score directions compete for the same curvature.

The next target is measurement compatibility and/or a two-sided autonomous relational lift, not another scalar patch.

## Compact theorem stack

### WP02 — finite-radius survival

`(R_lin^2/4)[Tr F_N^(nu)/N] <= T(nu)`.

### WP03 / WP06 — autonomous relational dual survival

`K_N=(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`,

including arbitrary pre-existing history-state coherence.

### WP04 / WP05 — exact structured autonomous retention

Hard cap:

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

Mean excitation:

`R_M(1) <= (1-lambda)g_m+lambda g_(m+1)`.

The near-lossless coefficient `pi` is exactly sharp.

### WP07 / WP08 — quadratic synthesis

One-sided boundary:

`Tr F_N/N <= J <= Delta T_U(0)`.

Multimode one-sided sum:

`sum_k w_k Tr F_(N,k)/N <= sum_k w_k Delta_k T_k(0)`.

### WP09 — bilateral synthesis

`sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

Clean empty endpoints:

`Tr F_N/N <= [sqrt(Delta T_+)+sqrt(Delta T_-)]^2`.

The factor-two bilateral enhancement is exactly sharp.

### WP10 — one-sided mixed survival+synthesis

For `[P,H]=0` and one synthesized orientation,

`Tr F_N/N <= 4T_pre/R_B^2 + Delta T_syn(0)`.

The corresponding `hbar nu/4` energy/action coefficient is exactly sharp.

### WP11 — noncommuting-support shorted endpoint geometry

For

`B=PAP`, `K_+=QAP`, `K_-=QA^dagger P`,

`boxed: sqrt[Tr F_N/N]`

`<= min{sqrt(J_B^+ + J_+) + sqrt(J_-),`

`       sqrt(J_B^- + J_-) + sqrt(J_+)}`.

Compressed endpoint projectors are essential. A four-level exact-gap model gives `lambda_U=1/4`, `mu_U=3/4`; dropping the geometry produces an actually false observable Fisher bound.

### WP12 — exact shared-curvature allocation

`Z_+ + Z_- <= C_Delta`.

Define

`Phi_a(C;R_+,R_-)`

`=sup [sqrt(a+Tr Z_+) + sqrt(Tr Z_-)]^2`.

Then

`Phi_a=inf_(0<eta<1){a/eta+h_(1/eta,1/(1-eta))}`,

where

`h_(alpha,beta)=max alpha Tr Z_+ + beta Tr Z_-`

is an SDP with dual

`min_(W>=0) Tr(CW)`

subject to

`R_+ W R_+>=alpha R_+`,

`R_- W R_->=beta R_-`.

This eliminates the WP11 double counting of shared curvature.

### WP13 — positive spectral-action law

Choose one positive kernel cost operator

`G=epsilon_U QPi_UQ + epsilon_D QPi_DQ`

and define

`A_G^(2)=(1/4)Tr(G C_Delta)`.

For synthesized ranges,

`g_+=lambda_min[R_+ G R_+ |_(R_+)]`,

`g_-=lambda_min[R_- G R_- |_(R_-)]`.

Then

`boxed: g_+J_+ + g_-J_- <= 4A_G^(2)`.

If a relevant `g` is zero, there is no finite action-only bound for that orientation.

For `e=4A_G^(2)`, `p=g_+`, `q=g_-`, internal resource `a`,

`boxed: Psi_a(e;p,q)=`

- `(sqrt(a)+sqrt(e/q))^2` if `e<=a p^2/q`;
- `(e+p a)(1/p+1/q)` if `e>=a p^2/q`.

Pure bilateral synthesis gives

`Psi_0=e(1/p+1/q)`.

For clean equal costs `p=q=hbar nu`,

`A_G^(2) >= (hbar nu/8)[Tr F_N/N]`.

One-sided synthesis recovers the `hbar nu/4` law. An unequal-cost exact-gap qutrit plus one Fourier measurement saturates the harmonic coefficient for arbitrary positive `p,q`.

Read:
`notes/WP13_POSITIVE_SPECTRAL_ACTION_ALLOCATION_LAW.md`.

### WP14 — rank-one curvature-metric angle law

For

`R_+=|u><u|`, `R_-=|v><v|`,

short the curvature to

`C_S=Short_span{u,v}(C)`.

Define

`s_u=1/<u|C_S^(-1)|u>`,

`s_v=1/<v|C_S^(-1)|v>`,

`c=|<u|C_S^(-1)|v>|/sqrt(<u|C_S^(-1)|u><v|C_S^(-1)|v>)`.

The exact feasible boundary is

`boxed: y_max(x)=s_v[1-x/s_u]/[1-(1-c^2)x/s_u]`.

For

`r=alpha s_u/(beta s_v)`,

the exact WP12 linear allocation is

`boxed: h_(alpha,beta)=`

- `beta s_v` if `r<=c^2`;
- `[alpha s_u+beta s_v-2c sqrt(alpha beta s_u s_v)]/(1-c^2)` if `c^2<r<c^(-2)`;
- `alpha s_u` if `r>=c^(-2)`.

Thus rank-one WP12 instances require no SDP; only the outer scalar `eta` minimization remains.

The angle `c` is curvature-whitened, not the ordinary Hilbert-space principal angle. The same ordinary overlap `1/2` can yield `c=1/sqrt(13)` or `c=2/sqrt(7)` under different positive curvature operators.

Read:
`notes/WP14_RANK_ONE_CURVATURE_METRIC_PRINCIPAL_ANGLE_LAW.md`.

## Numerical gates

- `numerics/verify_robust_tangent_radius_law.py`
- `numerics/verify_relational_autonomous_laws.py`
- `numerics/verify_nonlinear_zero_radius_law.py`
- `numerics/verify_quadratic_synthesis_sum_rule.py`
- `numerics/verify_bilateral_synthesis_minkowski_law.py`
- `numerics/verify_one_sided_mixed_survival_synthesis_law.py`
- `numerics/verify_shorted_endpoint_master_law.py`
- `numerics/verify_operator_curvature_allocation_law.py`
- `numerics/verify_positive_spectral_action_allocation_law.py`
- `numerics/verify_rank_one_curvature_metric_angle_law.py`

## Current frontier

### 1. Measurement compatibility — highest immediate priority

The WP12 shared-kernel benchmark has resource ceiling `12` but SLD-QFI trace `10.75`. Determine whether the exact common-record/Holevo optimum accounts for the entire residual gap. If yes, separate the final theorem cleanly into

`physical resource ceiling x measurement compatibility`.

### 2. Operator + action Pareto law

WP13 intentionally compresses `C_Delta` to one scalar action and therefore loses the WP14 overlap invariant `c`. Derive the sharp Pareto relation retaining both spectral action and operator curvature geometry.

### 3. Autonomous relational lift

Apply the operator/action hierarchy from both clock and signal viewpoints to a globally stationary exact exchange tangent. Determine whether matching positive action resources are unavoidable on both sides of the relational cut.

### 4. Gaussian covariance-changing synthesis

Test squeezed-vacuum and mixed Gaussian temporal families. Determine whether the relevant resource remains kernel curvature priced by a positive spectral operator or requires a covariance-specific extension.

### 5. Priority audit

Explicitly compare against Longyun Chen and Yuxiang Yang, *Optimal Quantum Metrology under Energy Constraints*, Phys. Rev. Lett. 136, 070801 (2026), DOI `10.1103/6ghs-frtx`, plus rank-one semidefinite packing/SOCP and waveform-Holevo literature.

## Priority status

Shorted operators, SDP/SOCP duality, weighted principal angles, harmonic costs, energy-constrained metrology, and multiparameter Holevo theory are established. Candidate novelty is restricted to their frequency-resolved **rank-changing temporal-information resource** consequences. Priority remains **unverified, not certified**.

## Documentation rule

Every material theorem, counterexample, prior-art collision, or killed conjecture must be recorded immediately and reflected in `README.md`, `AGENTS.md`, and `ROADMAP.md`. The repository, not chat history, is authoritative.
