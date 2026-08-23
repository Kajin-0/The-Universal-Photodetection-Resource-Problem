# Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

The frozen Rev11 paper remains untouched on `agent/temporal-information-resource-law`.

## Grand challenge

Determine the physical resource that constrains temporal information when clock/reference, signal, controller, detector, and memory are all finite internal systems and no ideal external timing operation is supplied for free.

## Current theorem hierarchy

### WP02 — finite-radius robust survival

For exact temporal gap `nu`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N^(nu)/N] <= T(nu)`.

Local Fisher strength must therefore be weighted by a physical tangent robustness.

### WP03 / WP06 — autonomous relational dual survival

For a globally stationary clock--signal exchange tangent,

`K_N=(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`.

The law survives arbitrary pre-existing Page--Wootters/history-state relational coherence.

### WP04 / WP05 — exact structured autonomous retention

Hard total-excitation cap:

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

Mean total excitation `Lbar=m+lambda`:

`R_M(1) <= (1-lambda)g_m+lambda g_(m+1)`,

`g_L=cos^2[pi/(L+2)]`.

Sine-chain extremizers make the near-lossless coefficient `pi` exactly sharp under both hard and mean total energy.

### WP07 — one-sided zero-radius synthesis

For baseline-empty endpoint `P_U`, `P=supp(rho0)`, and

`A=P_U A P`,

let

`J=Tr(A rho0^+ A^dagger)`.

Then for every finite `N` and arbitrary entangled collective POVM,

`boxed: Tr F_N/N <= J <= Delta T_U(0)`.

The resource at `R_lin=0` is second-order endpoint population synthesis. The minimal qubit and coherent-sideband constructions saturate the coefficient.

### WP08 — multimode quadratic synthesis budget

For mutually orthogonal baseline-empty modes and one common arbitrary collective measurement,

`boxed: sum_k w_k Tr F_(N,k)/N <= sum_k w_k Delta_k T_k(0)`

for all `w_k>=0`.

Gap weighting gives

`boxed: sum_k hbar nu_k Tr F_(N,k)/(4N) <= E_gap,syn^(2)`.

Multimode coherent sidebands with common heterodyne readout saturate every positive weighted sum simultaneously.

### WP09 — bilateral zero-radius Minkowski law

For arbitrary rank-deficient baseline, write

`A=X+Y^dagger`,

`X=A P`, `Y=Q A^dagger P`.

With weighted norms `J_X,J_Y`,

`boxed: sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

For orthogonal empty upper/lower endpoints,

`boxed: Tr F_N/N <= [sqrt(Delta T_+)+sqrt(Delta T_-)]^2`.

An exact-gap qutrit Fourier experiment saturates this law and disproves naive additive endpoint synthesis by exactly factor two.

### WP10 — sharp one-sided mixed survival+synthesis

For `[P,H]=0` and one-sided upper synthesis,

`A_nu=B+K`,

`B=P A_nu P`, `K=Q A_nu P`.

Then

`boxed: Tr F_N/N <= J_B+J_K <= 4T_pre/R_B^2 + Delta T_syn(0)`.

A qutrit congruence family plus one Fourier measurement simultaneously saturates the internal-survival term, synthesis-curvature term, and total Fisher law. The sharp energy/action form is

`boxed: Ebar+/R_B^2 + E_syn^(2) >= (hbar nu/4)[Tr F_N/N]`.

### WP11 — noncommuting-support shorted-endpoint master law

Let the **full** tangent remain an exact gap but allow `[P,H]!=0`, with

`P=supp(rho0)`, `Q=I-P`.

First-order physicality gives `Q A Q=0`. Decompose

`B=PAP`,

`K_+=QAP`,

`K_-=QA^dagger P`.

The finite-copy arbitrary-POVM measurement law is

`boxed: sqrt[Tr F_N/N]`

`<= min{sqrt(J_B^+ + J_+) + sqrt(J_-),`

`       sqrt(J_B^- + J_-) + sqrt(J_+)}`.

Compressed endpoint projectors

`P Pi_U P`, `P Pi_D P`, `Q Pi_U Q`, `Q Pi_D Q`

supply shorting/principal-angle constants `lambda_U,lambda_D,mu_U,mu_D`, yielding the rigorous scalar endpoint-resource master bound

`boxed: Tr F_N/N`

`<= min{[sqrt(B_U+S_U)+sqrt(S_D)]^2,`

`       [sqrt(B_D+S_D)+sqrt(S_U)]^2}`.

An exact four-level counterexample proves the geometry necessary. Without the upper shorting constant the internal term is `1/8` instead of the true `1/2`; the exact correction is `lambda_U=1/4`. A fixed one-copy randomized scalar-SLD POVM gives

`Tr F=7/4 > 13/8`,

so the no-geometry resource law is operationally false.

### WP12 — exact operator curvature-allocation law

WP11 separately charges the two synthesized orientations even though second-order positivity gives the **joint** constraint

`Z_+ + Z_- <= C_Delta`.

WP12 retains this operator resource exactly.

For positive curvature operator `C` and synthesized output projectors `R_+,R_-`, define the feasible allocation set

`Z_+>=0`, `Z_->=0`,

`Z_+=R_+ Z_+ R_+`,

`Z_-=R_- Z_- R_-`,

`Z_+ + Z_- <= C`.

For internal resource `a>=0`, define

`Phi_a(C;R_+,R_-)`

`= sup [sqrt(a+Tr Z_+) + sqrt(Tr Z_-)]^2`.

This is the tightest consequence of the kernel-curvature constraint alone for the WP11 score geometry.

The square-root identity and convex-concave minimax give the exact representation

`boxed: Phi_a`

`= inf_(0<eta<1) {a/eta`

`+ h_(1/eta,1/(1-eta))(C;R_+,R_-)}`,

where the inner linear allocation is an SDP:

`h_(alpha,beta)=max alpha Tr Z_+ + beta Tr Z_-`.

Its dual is

`boxed: h_(alpha,beta)=min_(W>=0) Tr(CW)`

subject to

`R_+ W R_+ >= alpha R_+`,

`R_- W R_- >= beta R_-`.

Thus the exact operator allocation is a **one-dimensional outer minimization over an SDP value**.

#### Exact limits

One synthesized orientation:

`boxed: Phi_a(C;R,0)=a+Tr Short_R(C)`.

Identical upper/lower synthesized subspace, with

`s=Tr Short_R(C)`:

`boxed: Phi_a(C;R,R)=`

- `(sqrt(a)+sqrt(s))^2` for `s<=a`;
- `2(a+s)` for `s>=a`.

For `a=0`, the bilateral coefficient is exactly `2s`.

If `R_+` and `R_-` are orthogonal and `C` is block decoupled across them,

`boxed: Phi_a=[sqrt(a+s_+)+sqrt(s_-)]^2`,

where `s_+/-` are the corresponding shorted-curvature traces.

#### Physical master bound

For WP11's actual curvature `C_Delta` and synthesized ranges `R_+,R_-`,

`boxed: Tr F_N/N`

`<= min{Phi_(J_B^+)(C_Delta;R_+,R_-),`

`       Phi_(J_B^-)(C_Delta;R_-,R_+)}`.

Replacing `J_B^+/-` by their WP11 endpoint-resource ceilings gives a fully resource-reduced noncommuting-support theorem. This allocation bound is never weaker than separately charging the shorted curvature to both orientations.

#### Exact shared-kernel benchmark

For

`H=hbar omega diag(0,1,2)`,

`|q>=(1/2)|0>+sqrt(5/8)|1>+[1/(2sqrt(2))]|2>`,

`rho0=(I-|q><q|)/2`,

`A=|1><0|-sqrt(2)|2><1|`,

one obtains

`J_B^+=5/4`, `J_+=7/4`, `J_-=3`,

with shared rank-one kernel curvature

`s=19/4`.

The coincident-subspace formula gives

`Phi=12`,

exactly equal to the actual abstract WP11 weighted-norm expression. Separately charging the same curvature to both orientations gives approximately `21.427`, so operator allocation removes about `43.996%` of that overcount.

The SLD-QFI trace of this model is `10.75`; the remaining `12` versus `10.75` gap is measurement-compatibility geometry, not curvature-resource double counting.

## Current frontier

The next stage is to make the WP12 allocation explicitly **spectral-energy weighted**, rather than using total kernel curvature:

1. incorporate `W_U=Q Pi_U Q` and `W_D=Q Pi_D Q` directly into the allocation SDP;
2. derive an operator-cost dual representing positive synthesis energy/action;
3. solve rank-one upper/lower subspaces with arbitrary principal angle in closed form;
4. determine whether Holevo-compatible measurement geometry can close the remaining allocation-versus-attainability gap;
5. lift the final operator allocation to both sides of a globally stationary clock--signal cut.

## Validation

- `numerics/verify_robust_tangent_radius_law.py`
- `numerics/verify_relational_autonomous_laws.py`
- `numerics/verify_nonlinear_zero_radius_law.py`
- `numerics/verify_quadratic_synthesis_sum_rule.py`
- `numerics/verify_bilateral_synthesis_minkowski_law.py`
- `numerics/verify_one_sided_mixed_survival_synthesis_law.py`
- `numerics/verify_shorted_endpoint_master_law.py`
- `numerics/verify_operator_curvature_allocation_law.py`

## Priority discipline

Shorted operators, parallel addition, principal angles, SDP duality, minimax theory, PSD-cone curvature, rank-deficient QFI, and multiparameter compatibility theory are established. Candidate novelty is restricted to their frequency-resolved arbitrary-POVM temporal-resource consequences. **Priority remains unverified, not certified.**

Read `AGENTS.md`, `ROADMAP.md`, and WP01--WP12 before continuing. Record every material theorem, counterexample, prior-art collision, or killed conjecture immediately; do not rely on chat history.
