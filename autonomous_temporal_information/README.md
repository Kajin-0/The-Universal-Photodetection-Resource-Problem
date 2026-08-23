# Autonomous Temporal Information Law

This directory contains the post-Rev11 foundational research program.

**Branch:** `agent/autonomous-temporal-information-law`

The frozen Rev11 paper remains untouched on `agent/temporal-information-resource-law`.

## Grand challenge

Determine what physical resource constrains temporal information when clock/reference, signal, controller, detector, and memory are all finite internal systems and no ideal external timing operation is supplied for free.

## Current theorem hierarchy

### WP02 — finite-radius robust survival

For an exact temporal gap `nu`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N^(nu)/N] <= T(nu)`.

Thus local Fisher strength alone is not the resource; it must be multiplied by a physical tangent robustness.

### WP03 / WP06 — autonomous dual survival, including coherent history states

For a globally stationary clock--signal exchange tangent,

`K_N=(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`.

The law remains valid even when the baseline already contains Page--Wootters/history-state relational coherence and does not commute separately with the local Hamiltonians.

### WP04 / WP05 — exact structured autonomous retention

For the structured globally stationary relative-time experiment with hard total-excitation cap `L`,

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

The fundamental near-lossless law is

`E >= pi hbar nu/sqrt(1-R)[1+o(1)]`,

with coefficient `pi` exactly sharp. The same coefficient remains exactly sharp under a mean-total-energy constraint via the piecewise-linear envelope of

`g_L=cos^2[pi/(L+2)]`.

### WP07 — one-sided zero-radius synthesis

For a baseline-empty endpoint sector and complex two-quadrature tangent

`A=P_U A P`, `P=supp(rho0)`,

let

`J=Tr(A rho0^+ A^dagger)`.

For every finite `N` and arbitrary entangled collective POVM,

`boxed: Tr F_N/N <= J <= Delta T_U(0)`.

The missing resource at `R_lin=0` is second-order endpoint population synthesis. The minimal qubit and coherent-sideband constructions saturate the coefficient.

### WP08 — multimode quadratic synthesis budget

For mutually orthogonal baseline-empty modes and one common arbitrary collective measurement,

`boxed: sum_k w_k Tr F_(N,k)/N <= sum_k w_k Delta_k T_k(0)`

for all nonnegative weights. Gap weighting gives

`boxed: sum_k hbar nu_k Tr F_(N,k)/(4N) <= E_gap,syn^(2)`.

Multimode coherent sidebands with common heterodyne readout saturate every positive weighted sum simultaneously.

### WP09 — bilateral zero-radius Minkowski law

For arbitrary rank-deficient baseline, decompose

`A=X+Y^dagger`,

`X=A P`, `Y=Q A^dagger P`,

with

`J_X=Tr(X rho0^+ X^dagger)`,

`J_Y=Tr(Y rho0^+ Y^dagger)`.

Then

`boxed: sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

For orthogonal baseline-empty upper/lower endpoints,

`boxed: Tr F_N/N <= [sqrt(Delta T_+)+sqrt(Delta T_-)]^2`.

An exact-gap qutrit Fourier experiment saturates the law and disproves naive additive endpoint accounting by exactly factor two.

### WP10 — sharp one-sided mixed survival+synthesis law

When `[P,H]=0` and only the upper endpoint is newly synthesized, write

`A_nu=B+K`,

`B=P A_nu P`, `K=Q A_nu P`.

Then

`boxed: Tr F_N/N <= J_B+J_K`

with

`J_B <= 4T_pre/R_B^2`,

`J_K <= Delta T_syn(0)`.

Therefore

`boxed: Tr F_N/N <= 4T_pre/R_B^2 + Delta T_syn(0)`.

A qutrit congruence family plus one Fourier measurement simultaneously saturates the internal-survival term, the synthesis-curvature term, and the total Fisher law. The sharp positive energy/action form is

`boxed: Ebar+/R_B^2 + E_syn^(2) >= (hbar nu/4)[Tr F_N/N]`.

### WP11 — noncommuting-support shorted-endpoint master law

The remaining support-geometry loophole is now controlled.

Let the **full** tangent be an exact gap,

`[H,A_nu]=hbar nu A_nu`,

at arbitrary rank-deficient `rho0`, with

`P=supp(rho0)`, `Q=I-P`.

First-order physicality gives `Q A_nu Q=0`. Decompose

`B=P A_nu P`,

`K_+=Q A_nu P`,

`K_-=Q A_nu^dagger P`.

Define weighted tangent norms

`J_B^+=Tr(B rho0^+ B^dagger)`,

`J_B^-=Tr(B^dagger rho0^+ B)`,

`J_+=Tr(K_+ rho0^+ K_+^dagger)`,

`J_-=Tr(K_- rho0^+ K_-^dagger)`.

For every finite `N` and arbitrary entangled collective POVM,

`boxed: sqrt[Tr F_N/N]`

`<= min{sqrt(J_B^+ + J_+) + sqrt(J_-),`

`       sqrt(J_B^- + J_-) + sqrt(J_+)}`.

Let `Pi_U,Pi_D` be the participating energy endpoint projectors and define compressed endpoint operators

`S_U=P Pi_U P`, `S_D=P Pi_D P`,

`W_U=Q Pi_U Q`, `W_D=Q Pi_D Q`.

For the information-bearing internal range projectors `R_B^+,R_B^-`, define the shorting/principal-angle constants

`lambda_U=sup{lambda:S_U >= lambda R_B^+}`,

`lambda_D=sup{lambda:S_D >= lambda R_B^-}`.

For the synthesized range projectors `R_+,R_-`, define

`mu_U=sup{mu:W_U >= mu R_+}`,

`mu_D=sup{mu:W_D >= mu R_-}`.

Let

`C_Delta=Q(partial_x^2 rho+partial_y^2 rho)Q`,

`Gamma_U=Tr(W_U C_Delta)`,

`Gamma_D=Tr(W_D C_Delta)`.

Then

`J_B^+ <= 4T_U/(R_B^2 lambda_U)`,

`J_B^- <= 4T_D/(R_B^2 lambda_D)`,

`J_+ <= Gamma_U/mu_U`,

`J_- <= Gamma_D/mu_D`.

Hence the general finite-copy resource ceiling is

`boxed: Tr F_N/N`

`<= min{`

`[sqrt(B_U+S_U)+sqrt(S_D)]^2,`

`[sqrt(B_D+S_D)+sqrt(S_U)]^2`

`}`,

where

`B_U=4T_U/(R_B^2 lambda_U)`,

`B_D=4T_D/(R_B^2 lambda_D)`,

`S_U=Gamma_U/mu_U`,

`S_D=Gamma_D/mu_D`.

The full generic ceiling is not claimed globally sharp, but it reduces exactly to WP06, WP07, WP09, and WP10 in their solved limits.

#### Geometry is provably necessary

For

`H=hbar omega diag(0,1,2,3)`, `nu=2omega`,

`|r>=(1/2)|2>+(sqrt(3)/2)|3>`,

`rho0=(1/2)|0><0|+(1/2)|r><r|`,

`A_nu=|2><0|`,

one has `[P,H]!=0` and

`B=(1/2)|r><0|`,

`K_+=(sqrt(3)/2)|q><0|`.

The true internal weighted norm is

`J_B=1/2`,

but the naive no-geometry WP10 continuation gives only

`4T_U/R_B^2=1/8`.

The shorting constant is exactly

`lambda_U=1/4`,

which repairs the bound to equality. On the kernel side,

`mu_U=3/4`

and the curvature correction is also exact.

The omission causes an **operational** failure: a one-copy POVM obtained by classical randomization between the two scalar-SLD-optimal quadrature measurements has Fisher trace

`7/4`,

while the naive no-geometry total resource ceiling is only

`13/8`.

Thus principal-angle/shorted-endpoint geometry is required for observable temporal information, not merely for an intermediate proof norm.

## Current frontier

The central local support/synthesis loophole is now substantially closed. The highest-value mathematical task is to sharpen WP11 at the operator level:

1. retain Anderson--Trapp shorted operators themselves rather than scalar shorting constants;
2. allocate overlapping kernel curvature jointly between `K_+` and `K_-` instead of separately charging `Gamma_U` and `Gamma_D`;
3. formulate the tightest allocation as a variational/SDP resource;
4. seek low-dimensional exact extremizers;
5. lift the geometry to a globally stationary clock--signal bipartition.

## Validation

Independent numerical/adversarial validators:

- `numerics/verify_robust_tangent_radius_law.py`
- `numerics/verify_relational_autonomous_laws.py`
- `numerics/verify_nonlinear_zero_radius_law.py`
- `numerics/verify_quadratic_synthesis_sum_rule.py`
- `numerics/verify_bilateral_synthesis_minkowski_law.py`
- `numerics/verify_one_sided_mixed_survival_synthesis_law.py`
- `numerics/verify_shorted_endpoint_master_law.py`

## Priority discipline

Shorted operators, principal angles, PSD-cone curvature, rank-deficient QFI, Fisher-symmetric measurement theory, Gaussian metrology, and reference-frame/asymmetry theory are established mathematics and physics. Candidate novelty is restricted to the frequency-resolved arbitrary-POVM temporal-resource consequences and their sharp/counterexample structure. **Priority remains unverified, not certified.**

Read `AGENTS.md`, `ROADMAP.md`, and WP01--WP11 before continuing. Record every material theorem, counterexample, prior-art collision, or killed conjecture immediately; do not rely on chat history.
