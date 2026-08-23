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

For a globally stationary clock--signal exchange tangent,

`K_N=(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`,

including arbitrary pre-existing Page--Wootters/history-state coherence.

### WP04 / WP05 — exact structured autonomous retention

Hard total excitation cap:

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

Mean total excitation:

`R_M(1) <= (1-lambda)g_m+lambda g_(m+1)`,

`g_L=cos^2[pi/(L+2)]`.

The near-lossless coefficient `pi` is exactly sharp under both hard and mean total energy.

### WP07 / WP08 — zero-radius quadratic synthesis

For one baseline-empty endpoint,

`boxed: Tr F_N/N <= J <= Delta T_U(0)`.

For orthogonal modes and one common arbitrary collective measurement,

`boxed: sum_k w_k Tr F_(N,k)/N <= sum_k w_k Delta_k T_k(0)`.

Gap weighting gives

`boxed: sum_k hbar nu_k Tr F_(N,k)/(4N) <= E_gap,syn^(2)`.

### WP09 — bilateral zero-radius Minkowski law

For opposite support orientations,

`boxed: sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

For clean empty upper/lower endpoints,

`boxed: Tr F_N/N <= [sqrt(Delta T_+)+sqrt(Delta T_-)]^2`.

The exact-gap qutrit Fourier extremizer proves the factor-two departure from additive synthesis exactly sharp.

### WP10 — sharp one-sided mixed survival+synthesis

For energy-invariant baseline support and one-sided synthesis,

`boxed: Tr F_N/N <= 4T_pre/R_B^2 + Delta T_syn(0)`.

The energy/action form

`boxed: Ebar+/R_B^2 + E_syn^(2) >= (hbar nu/4)[Tr F_N/N]`

is exactly sharp.

### WP11 — noncommuting-support shorted-endpoint law

For arbitrary coherent support, decompose

`B=PAP`, `K_+=QAP`, `K_-=QA^dagger P`.

Then

`boxed: sqrt[Tr F_N/N]`

`<= min{sqrt(J_B^+ + J_+) + sqrt(J_-),`

`       sqrt(J_B^- + J_-) + sqrt(J_+)}`.

Compressed endpoint projectors and shorting/principal-angle factors are required to reduce these norms to spectral resources. A four-level exact-gap counterexample proves omission of that geometry produces a false observable Fisher bound.

### WP12 — exact shared-curvature operator allocation

Second-order positivity gives

`Z_+ + Z_- <= C_Delta`.

For positive `C` and synthesized output projectors `R_+,R_-`, define

`Phi_a(C;R_+,R_-)`

`= sup [sqrt(a+Tr Z_+) + sqrt(Tr Z_-)]^2`

over positive support-constrained allocations `Z_++Z_-<=C`.

Then

`boxed: Phi_a`

`= inf_(0<eta<1) {a/eta + h_(1/eta,1/(1-eta))(C;R_+,R_-)}`,

where `h_(alpha,beta)` is an SDP with dual

`boxed: h_(alpha,beta)=min_(W>=0) Tr(CW)`

subject to

`R_+ W R_+ >= alpha R_+`,

`R_- W R_- >= beta R_-`.

Exact limits include one-sided shorted curvature, decoupled orthogonal ranges, and the coincident-subspace crossover

`Phi=(sqrt(a)+sqrt(s))^2` for `s<=a`,

`Phi=2(a+s)` for `s>=a`.

### WP13 — positive spectral-action allocation

Choose one positive kernel cost operator

`G=epsilon_U Q Pi_U Q + epsilon_D Q Pi_D Q`

or any `G>=0`, and define

`A_G^(2)=(1/4)Tr(G C_Delta)`.

For synthesized ranges `R_+,R_-`, define

`g_+=lambda_min[R_+ G R_+ |_(R_+)]`,

`g_-=lambda_min[R_- G R_- |_(R_-)]`.

Then

`boxed: g_+J_+ + g_-J_- <= 4A_G^(2)`.

If a relevant `g` vanishes, no finite scalar action-only theorem exists for that orientation.

For upper-oriented internal resource `a`, write

`e=4A_G^(2)`, `p=g_+`, `q=g_-`.

The exact action-only envelope is

`boxed: Psi_a(e;p,q)=`

- `(sqrt(a)+sqrt(e/q))^2`, for `e<=a p^2/q`;
- `(e+p a)(1/p+1/q)`, for `e>=a p^2/q`.

For pure bilateral synthesis,

`Psi_0=e(1/p+1/q)`.

Thus the effective bilateral spectral cost is harmonic. Equal clean gap costs `p=q=hbar nu` recover the sharp WP09 `hbar nu/8` coefficient; one-sided synthesis recovers the WP07/WP10 `hbar nu/4` coefficient. An unequal-cost exact-gap qutrit plus one Fourier measurement saturates the harmonic coefficient for arbitrary positive `p,q`.

### WP14 — rank-one curvature-metric principal-angle law

For rank-one synthesized ranges

`R_+=|u><u|`, `R_-=|v><v|`,

short first to

`C_S=Short_span{u,v}(C)`.

Define

`s_u=1/<u|C_S^(-1)|u>`,

`s_v=1/<v|C_S^(-1)|v>`,

and

`c=|<u|C_S^(-1)|v>|/sqrt(<u|C_S^(-1)|u><v|C_S^(-1)|v>)`.

The complete feasible boundary is

`boxed: y_max(x)=s_v[1-x/s_u]/[1-(1-c^2)x/s_u]`.

For `r=alpha s_u/(beta s_v)`, the exact linear allocation is

`boxed: h_(alpha,beta)=`

- `beta s_v`, if `r<=c^2`;
- `[alpha s_u+beta s_v-2c sqrt(alpha beta s_u s_v)]/(1-c^2)`, if `c^2<r<c^(-2)`;
- `alpha s_u`, if `r>=c^(-2)`.

Thus rank-one WP12 instances contain no SDP. The governing overlap is the principal angle in the inverse shorted-curvature metric, not the ordinary Hilbert-space angle. The same ordinary overlap `1/2` can yield `c=1/sqrt(13)` or `c=2/sqrt(7)` under different positive curvature operators.

### WP15 — exact common-record Fisher supremum in the shared-kernel qutrit

For the WP12 rank-one-kernel benchmark,

`rho0=P/2`,

`A=|1><0|-sqrt(2)|2><1|`,

WP12 gives the physical resource ceiling

`Phi=12`,

while the SLD-QFI matrix is

`F_Q=diag(39/8,47/8)`,

so

`Tr F_Q=43/4`.

WP15 solves the remaining one-copy arbitrary-POVM optimization exactly. In a support/kernel basis, the Hermitian witness

`Y=[[9/16,0,0],`

`   [0,9/16,3sqrt(15)/8],`

`   [0,3sqrt(15)/8,23/4]]`

satisfies for every vector `|phi>`

`boxed: |<phi|A|phi>|^2`

`<= <phi|rho0|phi><phi|Y|phi>`.

The proof uses the exact LMI family

`lambda rho0+lambda^(-1)Y-(e^(i theta)A+e^(-i theta)A^dagger)>=0`.

With `x=lambda^2`, `t=cos^2 theta`, the nontrivial leading principal minors factor into

`t(8x-9)^2+(1-t)(64x^2+112x+81)`

and

`t(8x-9)^2+(1-t)(40x+81)`,

so positivity is manifest.

Rank-one refinement then gives every POVM

`Tr F_1<=Tr Y=55/8`.

A regular three-outcome projective sequence approaches this value: the support numerical-radius basis contributes `9/8`, while a nearly dark outcome tilted toward

`i(a-b)/||a-b||`, `||a-b||^2=23/8`,

contributes `23/4`.

Therefore

`boxed: sup_(one-copy POVMs) Tr F_1=55/8`.

The benchmark hierarchy is now exactly

`physical resource: 12=96/8`,

`SLD quantum-statistical: 43/4=86/8`,

`common-record Fisher: 55/8`.

The resource-to-SLD gap is `5/4`; the SLD-to-common-record gap is `31/8`. The earlier provisional interpretation of the whole `12 -> 10.75` difference as measurement compatibility was therefore incorrect.

## Current frontier

The local hierarchy is now separated into physical resource, quantum-statistical tangent geometry, and actually accessible common-record information. Highest-value next targets are:

1. generalize the WP15 dual-witness method to a class of rank-one-kernel two-quadrature models;
2. retain both WP14 operator overlap and WP13 spectral action in a sharp Pareto law;
3. lift the full operator/action resource simultaneously to clock and signal sides of a globally stationary exact exchange tangent;
4. test covariance-changing Gaussian temporal families;
5. perform a hostile priority/significance review of WP07--WP15 before deciding whether a new manuscript is justified.

## Validation

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

## Priority discipline

Energy-constrained quantum metrology, shorted operators, rank-one SDP/SOCP reductions, weighted principal angles, numerical-radius theory, Gill--Massar/Holevo compatibility, PSD-cone curvature, rank-changing QFI/Bures geometry, and Gaussian metrology are established. Candidate novelty is restricted to their **frequency-resolved rank-changing temporal-information resource consequences** and the exact hierarchy connecting survival, synthesis curvature, spectral action, and arbitrary-POVM Fisher information.

Priority remains **unverified, not certified**.

Read `AGENTS.md`, `ROADMAP.md`, and WP01--WP15 before continuing. Record every material theorem, counterexample, prior-art collision, or killed conjecture immediately; do not rely on chat history.
