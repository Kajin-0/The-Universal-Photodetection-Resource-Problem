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

`= inf_(0<eta<1) {a/eta`

`+ h_(1/eta,1/(1-eta))(C;R_+,R_-)}`,

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

This charges the shared curvature only once:

`4A_G^(2) >= Tr(GZ_+)+Tr(GZ_-)`.

For synthesized ranges `R_+,R_-`, define the exact restricted costs

`g_+=lambda_min[R_+ G R_+ |_(R_+)]`,

`g_-=lambda_min[R_- G R_- |_(R_-)]`.

Then

`boxed: g_+J_+ + g_-J_- <= 4A_G^(2)`.

If either relevant `g` vanishes, no finite scalar action-only theorem exists for that orientation.

For upper-oriented internal resource `a`, write

`e=4A_G^(2)`, `p=g_+`, `q=g_-`.

The exact action-only envelope is

`boxed: Psi_a(e;p,q)=`

- `(sqrt(a)+sqrt(e/q))^2`, for `e<=a p^2/q`;
- `(e+p a)(1/p+1/q)`, for `e>=a p^2/q`.

For pure bilateral synthesis,

`boxed: Psi_0=e(1/p+1/q)`.

Thus the effective bilateral spectral cost is harmonic:

`epsilon_parallel=(1/p+1/q)^(-1)`.

For the symmetric clean exact-gap choice `p=q=hbar nu`,

`boxed: A_G^(2) >= (hbar nu/8)[Tr F_N/N]`,

recovering WP09. One-sided synthesis recovers the sharp `hbar nu/4` coefficient of WP07/WP10.

An unequal-cost exact-gap qutrit with one Fourier measurement saturates

`Tr F_1=4A_G^(2)(1/p+1/q)`

for arbitrary positive `p,q`.

### WP14 — rank-one curvature-metric principal-angle law

For rank-one synthesized ranges

`R_+=|u><u|`, `R_-=|v><v|`,

short the curvature first to

`C_S=Short_span{u,v}(C)`.

Define

`s_u=1/<u|C_S^(-1)|u>`,

`s_v=1/<v|C_S^(-1)|v>`,

and the curvature-whitened overlap

`c=|<u|C_S^(-1)|v>|`

`  /sqrt(<u|C_S^(-1)|u><v|C_S^(-1)|v>)`.

The complete feasible boundary is

`boxed: y_max(x)`

`=s_v[1-x/s_u]/[1-(1-c^2)x/s_u]`.

For

`r=alpha s_u/(beta s_v)`,

the exact linear WP12 allocation is

`boxed: h_(alpha,beta)=`

- `beta s_v`, if `r<=c^2`;
- `[alpha s_u+beta s_v-2c sqrt(alpha beta s_u s_v)]/(1-c^2)`, if `c^2<r<c^(-2)`;
- `alpha s_u`, if `r>=c^(-2)`.

Thus every rank-one WP12 instance contains no SDP: only the final one-dimensional `eta` minimization remains.

Crucially, `c` is not the ordinary Hilbert-space angle. Two ranges with the same ordinary overlap `1/2` can have curvature-metric cosines `1/sqrt(13)` or `2/sqrt(7)` depending only on the available curvature. The matrix resource therefore contains irreducible information lost under scalar energy/action compression.

## Current frontier

The next high-value target is no longer the existence of a local resource law; that hierarchy is now fairly well defined. The main unresolved questions are:

1. **measurement compatibility:** determine whether the WP12 shared-kernel `12` versus SLD-QFI `10.75` gap is exactly a Holevo/common-record compatibility penalty;
2. **operator + action Pareto law:** retain both WP14 curvature overlap and WP13 spectral cost rather than compressing immediately to one scalar action;
3. **autonomous relational lift:** apply the full operator/action resource simultaneously to clock and signal sides of a globally stationary exact exchange tangent;
4. **Gaussian covariance synthesis:** test whether squeezing/covariance-changing temporal families obey the same curvature-action hierarchy;
5. **priority audit:** compare explicitly against 2026 energy-constrained quantum-metrology results before manuscript formation.

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

## Priority discipline

Energy-constrained quantum metrology, shorted operators, rank-one semidefinite packing/SOCP reductions, principal angles in weighted metrics, SDP duality, Holevo theory, PSD-cone curvature, rank-deficient QFI, and Gaussian metrology are established. Candidate novelty is restricted to their **frequency-resolved rank-changing temporal-information resource consequences** and the exact theorem hierarchy connecting survival, synthesis curvature, spectral action, and arbitrary-POVM Fisher information.

Priority remains **unverified, not certified**.

Read `AGENTS.md`, `ROADMAP.md`, and WP01--WP14 before continuing. Record every material theorem, counterexample, prior-art collision, or killed conjecture immediately; do not rely on chat history.
