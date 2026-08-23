# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

**Started:** 2026-08-22

The frozen Rev11 paper remains on `agent/temporal-information-resource-law` and must not be rewritten absent a concrete defect.

## Grand question

> When signal, clock/reference, controller, detector, and memory are finite physical systems and no ideal externally timed operation is free, what resource constrains creation, transmission, and recovery of temporal information at frequency `nu`?

Research is analytical/theoretical, falsification-first, and documentation-first. Standard asymmetry/reference-frame theory, phase estimation, WAY, Page--Wootters, PSD-cone geometry, singular QFI/Bures geometry, shorted operators, principal angles, SDP/SOCP theory, energy-constrained metrology, Gaussian metrology, numerical-radius theory, Gill--Massar/Fisher-symmetric bounds, and Holevo compatibility are infrastructure unless a distinct operational temporal-information theorem is isolated.

## Current status

**WP15 — exact common-record Fisher supremum in the shared-kernel qutrit: analytic PASS and independently validated.**

The local hierarchy now has three logically distinct layers:

1. **physical temporal-resource geometry** — survival, kernel curvature, positive spectral action, and operator overlap;
2. **quantum-statistical tangent geometry** — SLD/Bures-type ceilings;
3. **single-record measurement accessibility** — the classical Fisher information attainable by one common POVM.

In the WP12 shared-kernel qutrit these ceilings are respectively

`12 > 43/4 > 55/8`.

Do not collapse these layers into one another.

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

Compressed endpoint projectors are essential. A four-level exact-gap example gives `lambda_U=1/4`, `mu_U=3/4`; dropping the geometry produces an actually false observable Fisher bound.

### WP12 — exact shared-curvature allocation

`Z_+ + Z_- <= C_Delta`.

Define

`Phi_a(C;R_+,R_-)=sup [sqrt(a+Tr Z_+) + sqrt(Tr Z_-)]^2`.

Then

`Phi_a=inf_(0<eta<1){a/eta+h_(1/eta,1/(1-eta))}`,

where `h_(alpha,beta)` is an SDP with dual

`min_(W>=0) Tr(CW)`

subject to

`R_+ W R_+>=alpha R_+`,

`R_- W R_->=beta R_-`.

This removes the WP11 double counting of shared curvature.

### WP13 — positive spectral-action law

Choose one positive kernel cost operator

`G=epsilon_U QPi_UQ + epsilon_D QPi_DQ`

and define

`A_G^(2)=(1/4)Tr(G C_Delta)`.

For synthesized ranges,

`g_+=lambda_min[R_+ G R_+ |_(R_+)]`,

`g_-=lambda_min[R_- G R_- |_(R_-)]`.

Then

`g_+J_+ + g_-J_- <= 4A_G^(2)`.

For pure bilateral synthesis the effective endpoint price is harmonic:

`epsilon_parallel=(1/g_+ + 1/g_-)^(-1)`.

Clean equal gap costs recover the sharp `hbar nu/8` bilateral coefficient; one-sided synthesis recovers `hbar nu/4`.

### WP14 — rank-one curvature-metric angle law

For rank-one synthesized ranges, short the curvature to their span and define

`s_u=1/<u|C_S^(-1)|u>`,

`s_v=1/<v|C_S^(-1)|v>`,

`c=|<u|C_S^(-1)|v>|/sqrt(<u|C_S^(-1)|u><v|C_S^(-1)|v>)`.

The exact feasible frontier is

`y_max(x)=s_v[1-x/s_u]/[1-(1-c^2)x/s_u]`.

The overlap invariant is the principal angle in the inverse shorted-curvature metric, not the ordinary Hilbert-space angle.

### WP15 — exact common-record Fisher supremum in the shared-kernel qutrit

For

`rho0=(I-|q><q|)/2`,

`|q>=(1/2)|0>+sqrt(5/8)|1>+[1/(2sqrt(2))]|2>`,

`A=|1><0|-sqrt(2)|2><1|`,

WP12 gives physical resource ceiling `12`, while the SLD trace is `43/4`.

WP15 proves the exact one-copy arbitrary-POVM result

`boxed: sup_POVM Tr F_1 = 55/8`.

The upper bound is certified by the Hermitian quadratic witness

`Y=[[9/16,0,0],[0,9/16,3sqrt(15)/8],[0,3sqrt(15)/8,23/4]]`,

which satisfies

`|<phi|A|phi>|^2 <= <phi|rho0|phi><phi|Y|phi>`

for every vector. The associated `lambda,theta` LMI factors exactly into manifestly nonnegative polynomials.

A sequence of ordinary three-outcome projective measurements with strictly positive baseline probabilities approaches `55/8`; exact regular attainment is not required.

The hierarchy in this benchmark is therefore

`physical resource 12`

`> SLD quantum-statistical 43/4`

`> common-record Fisher 55/8`.

Read:
`notes/WP15_EXACT_COMMON_RECORD_FISHER_SUPREMUM_SHARED_KERNEL_QUTRIT.md`.

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
- `numerics/verify_exact_common_record_fisher_supremum.py`

## Current frontier

### 1. WP16 — generic rank-one-kernel common-record theorem — highest priority

Generalize the WP15 optimization for

`rho0=P/r`, `rank(Q)=1`, `Q=|q><q|`,

and

`A=[[B,b],[a^dagger,0]]`

with `QAQ=0`.

The singular boundary invariant is

`kappa=max_(||t||=1)|<q|A|t>+<t|A|q>|^2`

`      =||a||^2+||b||^2+2|a^dagger b|`.

Do **not** assume the full optimum is simply the support-only optimum plus `r kappa`: early adversarial random qutrit tests show mixed support/kernel outcomes can exceed that naive sum.

Required work:

- derive the exact POVM-dual/semi-infinite witness problem for general `B,a,b`;
- determine whether it reduces to a finite SDP/numerical-radius problem;
- identify a nontrivial closed class containing WP15;
- record explicit counterexamples to any false additive compatibility conjecture.

### 2. Operator + spectral-action Pareto law

Retain both WP14 operator overlap and WP13 positive spectral action instead of compressing either away.

### 3. Autonomous relational lift

Apply the operator/action hierarchy simultaneously to clock and signal sides of a globally stationary exact exchange tangent.

### 4. Gaussian covariance-changing synthesis

Test squeezed-vacuum and mixed Gaussian rank-changing temporal families.

### 5. Priority audit

Explicitly compare against energy-constrained metrology, generalized numerical-radius/Ando-type operator inequalities, POVM design duality, Gill--Massar/Fisher-symmetric bounds, rank-changing QFI, and waveform-Holevo literature.

## Priority status

All generic matrix-analysis and quantum-estimation ingredients above are prior art unless demonstrated otherwise. Candidate novelty remains restricted to their frequency-resolved **rank-changing temporal-information resource** consequences and exact bridge theorems between resource, QFI, and accessible Fisher information. Priority remains **unverified, not certified**.

## Documentation rule

Every material theorem, counterexample, priority collision, or killed conjecture must be recorded immediately and reflected in `README.md`, `AGENTS.md`, and `ROADMAP.md`. The repository, not chat history, is authoritative.
