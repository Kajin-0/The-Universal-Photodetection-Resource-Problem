# Roadmap — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

## Goal

Seek a foundational physical resource principle for temporal information when clock, signal, controller, detector, and memory are all internal quantum systems. The finished Rev11 random-time law remains frozen on its parent branch.

## Completed foundations

### WP02 — robust tangent-radius law — PASS

For exact gap `nu`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N^(nu)/N] <= min(D_nu,U_nu) <= T(nu)`.

Thus

`Ebar+ >= (hbar nu R_lin^2/4)[Tr F_N^(nu)/N]`.

### WP03 / WP06 — autonomous dual survival and coherent-history extension — PASS

For a globally stationary exchange tangent,

`K_N=(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`.

WP06 removes separate local stationarity and allows pre-existing Page--Wootters/history-state coherence.

### WP04 / WP05 — exact structured autonomous retention — PASS

Hard cap:

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

Mean total excitation `Lbar=m+lambda`:

`R_M(1) <= (1-lambda)g_m+lambda g_(m+1)`,

`g_L=cos^2[pi/(L+2)]`.

Sine-chain extremizers make the near-lossless coefficient `pi` exactly sharp under both hard and mean total energy.

### WP07 — one-sided zero-radius synthesis — PASS

For `A=P_U A P`, `P=supp(rho0)`, baseline-empty `P_U`,

`boxed: Tr F_N/N <= J(A|rho0) <= Delta T_U(0)`.

### WP08 — multimode quadratic synthesis budget — PASS

For one common arbitrary collective measurement,

`boxed: sum_k w_k Tr F_(N,k)/N <= sum_k w_k Delta_k T_k(0)`

for arbitrary `w_k>=0`.

Gap weighting gives

`boxed: sum_k hbar nu_k Tr F_(N,k)/(4N) <= E_gap,syn^(2)`.

### WP09 — bilateral zero-radius Minkowski law — PASS

For

`A=X+Y^dagger`,

`X=A P`, `Y=Q A^dagger P`,

`boxed: sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

For orthogonal empty upper/lower endpoints,

`boxed: Tr F_N/N <= [sqrt(Delta T_+)+sqrt(Delta T_-)]^2`.

The exact-gap qutrit Fourier extremizer violates naive additive synthesis by exactly factor two and makes the equal-gap `hbar nu/8` coefficient sharp.

### WP10 — one-sided mixed finite-radius + synthesis law — PASS

For `[P,H]=0` and one-sided upper synthesis,

`A_nu=B+K`,

`B=P A_nu P`, `K=Q A_nu P`,

and

`boxed: Tr F_N/N <= J_B+J_K <= 4T_pre/R_B^2 + Delta T_syn(0)`.

A qutrit congruence family and one Fourier measurement simultaneously saturate all terms. The sharp energy/action form is

`boxed: Ebar+/R_B^2 + E_syn^(2) >= (hbar nu/4)[Tr F_N/N]`.

### WP11 — shorted-endpoint master law for noncommuting support — PASS

Let the full tangent remain an exact gap but allow `[P,H] != 0`, with `P=supp(rho0)`, `Q=I-P` and `Q A Q=0`. Decompose

`B=PAP`,

`K_+=QAP`,

`K_-=QA^dagger P`.

The finite-copy arbitrary-POVM measurement law is

`boxed: sqrt[Tr F_N/N]`

`<= min{sqrt(J_B^+ + J_+) + sqrt(J_-),`

`       sqrt(J_B^- + J_-) + sqrt(J_+)}`.

Compressed endpoint projectors `P Pi_U P`, `P Pi_D P`, `Q Pi_U Q`, `Q Pi_D Q` supply principal-angle/shorting constants that reduce the weighted tangent norms to physical endpoint populations and curvatures. An exact four-level counterexample proves these geometric factors are operationally necessary: omitting the upper shorting constant produces a false Fisher bound.

### WP12 — exact operator curvature-allocation law — PASS

Second-order positivity supplies the **joint** kernel-curvature constraint

`Z_+ + Z_- <= C_Delta`,

not two independent curvature budgets.

For positive `C` and synthesized output projectors `R_+,R_-`, define

`Phi_a(C;R_+,R_-)`

`= sup [sqrt(a+Tr Z_+) + sqrt(Tr Z_-)]^2`

over positive support-constrained allocations `Z_++Z_-<=C`.

The exact variational representation is

`boxed: Phi_a`

`= inf_(0<eta<1) {a/eta`

`+ h_(1/eta,1/(1-eta))(C;R_+,R_-)}`,

where

`h_(alpha,beta)=max alpha Tr Z_+ + beta Tr Z_-`

is an SDP with dual

`boxed: h_(alpha,beta)=min_(W>=0) Tr(CW)`

subject to

`R_+ W R_+ >= alpha R_+`,

`R_- W R_- >= beta R_-`.

Thus the exact resource allocation is a one-dimensional outer minimization over an SDP value.

Exact limits:

- one synthesized orientation:
  `Phi_a(C;R,0)=a+Tr Short_R(C)`;
- identical synthesized subspace, with `s=Tr Short_R(C)`:
  `Phi_a=(sqrt(a)+sqrt(s))^2` for `s<=a`, and `Phi_a=2(a+s)` for `s>=a`;
- orthogonal decoupled synthesized subspaces:
  `Phi_a=[sqrt(a+s_+)+sqrt(s_-)]^2`.

The physical master bound is

`boxed: Tr F_N/N`

`<= min{Phi_(J_B^+)(C_Delta;R_+,R_-),`

`       Phi_(J_B^-)(C_Delta;R_-,R_+)}`.

Replacing the internal norms by their WP11 endpoint-resource ceilings gives a fully resource-reduced noncommuting-support theorem.

In the shared rank-one-kernel benchmark,

`J_B^+=5/4`, `J_+=7/4`, `J_-=3`, `s=19/4`,

and the exact allocation gives `Phi=12`, whereas separately charging the same curvature to both orientations gives approximately `21.427`. The allocation law removes about `43.996%` of the overcount. The model's SLD-QFI trace is `10.75`, so the remaining gap is measurement-compatibility geometry rather than curvature-resource double counting.

## Current frontier — WP13: spectral-energy operator allocation

WP12 allocates total kernel curvature exactly but does not yet price that curvature by physical endpoint energy/action.

### A. Put endpoint costs inside the allocation

Retain the kernel endpoint contractions

`W_U=Q Pi_U Q`,

`W_D=Q Pi_D Q`

or, more generally, positive spectral cost operators obtained by compressing energy above the relevant endpoint threshold into `Q`.

The next theorem should constrain the same feasible `Z_+,Z_-` by a positive operator-valued synthesis cost, rather than replacing `W_U,W_D` by scalar shorting constants `mu_U,mu_D`.

### B. Define the correct spectral synthesis action

Candidate form:

`E_syn^(2)=(1/4)Tr[G C_Delta]`

for an appropriate positive cost operator `G`, or an optimized version in which distinct positive costs `G_+,G_-` are assigned to the two synthesized orientations.

Required properties:

1. positivity even when one orientation corresponds to a lower ordinary subsystem-energy endpoint;
2. exact reduction to WP07/WP08 energy weighting in clean baseline-empty sectors;
3. exact or controlled reduction to WP09's bilateral `hbar nu/8` coefficient;
4. compatibility with WP12's shared-curvature allocation without double counting;
5. preservation of principal-angle geometry when `[P,H]!=0`.

### C. Derive primal and dual energy-weighted SDPs

For positive endpoint cost operators `G_+,G_-`, derive the sharp maximum Fisher-compatible allocation for a fixed synthesis-action budget and the dual witness operator. Determine whether the dual can be written as a single positive operator dominating weighted compressions on `R_+` and `R_-`.

### D. Closed-form benchmarks

Solve at least:

- one orientation;
- orthogonal endpoint subspaces;
- coincident endpoint subspaces;
- rank-one `R_+,R_-` with arbitrary principal angle;
- the WP12 shared-kernel qutrit model.

### E. Measurement compatibility

After the resource allocation is energy weighted, test whether the remaining difference to attainable common-record Fisher information is exactly a standard Holevo/multiparameter compatibility penalty or whether another physical resource appears.

### F. Autonomous relational lift

Apply the final positive synthesis-action allocation from both clock and signal sides of a globally stationary exact exchange tangent. Determine whether a sharp two-sided spectral-action law results.

## Secondary directions

- rank-one arbitrary-principal-angle closed form for WP12/WP13;
- Gaussian covariance-changing synthesis;
- continuous-frequency limit rigor;
- collective-N mean-energy retention beyond WP05;
- many-body/cut-set resource laws.

## Priority and significance gate

Do not draft the new foundational manuscript yet. Require at least one of:

- a sharp positive spectral-energy WP13 theorem;
- a sharp impossibility result proving no scalar spectral-action law can represent the operator allocation;
- a clean autonomous two-sided lift with a nontrivial sharp coefficient.

Continue explicit prior-art checks against shorted operators/parallel addition, semidefinite resource allocation, operator-valued energy costs, singular quantum estimation, Holevo bounds, WAY/reference-frame theory, and quantum waveform estimation. Priority remains unverified until demonstrated otherwise.

## Validation requirements

Current independent validators:

- `numerics/verify_robust_tangent_radius_law.py`
- `numerics/verify_relational_autonomous_laws.py`
- `numerics/verify_nonlinear_zero_radius_law.py`
- `numerics/verify_quadratic_synthesis_sum_rule.py`
- `numerics/verify_bilateral_synthesis_minkowski_law.py`
- `numerics/verify_one_sided_mixed_survival_synthesis_law.py`
- `numerics/verify_shorted_endpoint_master_law.py`
- `numerics/verify_operator_curvature_allocation_law.py`

WP13 must add an independent energy-weighted allocation validator before being marked PASS.

## Documentation discipline

Every material theorem, failed conjecture, prior-art collision, or validation result must be recorded immediately in the branch and reflected in `README.md`, `AGENTS.md`, and this file. The repository, not chat history, is authoritative.
