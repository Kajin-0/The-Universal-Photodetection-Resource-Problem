# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

**Started:** 2026-08-22

The frozen Rev11 paper remains on `agent/temporal-information-resource-law` and is not to be rewritten absent a concrete defect.

## Grand question

> When signal, clock/reference, controller, detector, and memory are all finite physical systems and no ideal externally timed operation is free, what resource constrains creation, transmission, and recovery of temporal information at frequency `nu`?

Research is analytical/theoretical, falsification-first, and documentation-first. Standard asymmetry/reference-frame theory, phase estimation, WAY, Page--Wootters, PSD-cone geometry, singular QFI/Bures geometry, shorted operators, principal angles, SDP duality, Fisher-symmetric measurements, Gaussian metrology, and multiparameter compatibility theory are infrastructure unless a distinct operational temporal-information theorem is isolated.

## Current frontier

**WP12 — exact operator curvature-allocation law: analytic PASS and independently validated.**

The local theorem stack now treats the resource as naturally **operator-valued**:

- pre-existing support resource;
- second-order kernel-curvature synthesis resource;
- endpoint/support geometry through shorting/principal angles;
- joint allocation of shared curvature between opposite temporal orientations.

The next target is a positive **spectral-energy/action allocation** that incorporates energy endpoint contractions directly into the WP12 SDP.

## Compact theorem stack

### WP02 — finite-radius survival

`(R_lin^2/4)[Tr F_N^(nu)/N] <= T(nu)`.

### WP03 / WP06 — autonomous relational dual survival

`K_N=(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`,

including arbitrary pre-existing Page--Wootters/history-state relational coherence.

### WP04 / WP05 — exact structured autonomous retention

Hard cap:

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

Mean total excitation:

`R_M(1) <= (1-lambda)g_m+lambda g_(m+1)`,

`g_L=cos^2[pi/(L+2)]`.

The near-lossless coefficient `pi` is exactly sharp under both hard and mean total energy.

### WP07 — one-sided zero-radius synthesis

For `A=P_U A P`, baseline-empty `P_U`,

`boxed: Tr F_N/N <= Tr(A rho0^+ A^dagger) <= Delta T_U(0)`.

### WP08 — multimode synthesis budget

For one common arbitrary collective measurement,

`boxed: sum_k w_k Tr F_(N,k)/N <= sum_k w_k Delta_k T_k(0)`.

### WP09 — bilateral synthesis / Minkowski geometry

For `A=X+Y^dagger`,

`boxed: sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

For clean empty endpoints,

`boxed: Tr F_N/N <= [sqrt(Delta T_+)+sqrt(Delta T_-)]^2`.

The factor-two departure from additive synthesis is exactly sharp.

### WP10 — one-sided mixed survival+synthesis

For energy-invariant baseline support and one-sided upper synthesis,

`boxed: Tr F_N/N <= 4T_pre/R_B^2 + Delta T_syn(0)`.

The additive composition and energy/action coefficient are exactly sharp.

### WP11 — noncommuting-support shorted-endpoint master law

For arbitrary coherent support, decompose

`B=PAP`, `K_+=QAP`, `K_-=QA^dagger P`.

The finite-copy arbitrary-POVM information law is

`boxed: sqrt[Tr F_N/N]`

`<= min{sqrt(J_B^+ + J_+) + sqrt(J_-),`

`       sqrt(J_B^- + J_-) + sqrt(J_+)}`.

Compressed energy endpoint projectors and shorting/principal-angle constants reduce the tangent norms to physical spectral resources. An exact four-level example gives

`lambda_U=1/4`, `mu_U=3/4`

and proves the geometric correction operationally necessary:

`Tr F=7/4 > 13/8`

for the naive no-geometry resource ceiling.

### WP12 — exact operator curvature allocation

Second-order positivity gives the **joint** kernel constraint

`Z_+ + Z_- <= C_Delta`.

Define the feasible positive-operator allocation set by

`Z_+=R_+ Z_+ R_+`,

`Z_-=R_- Z_- R_-`,

`Z_+ + Z_- <= C`.

For internal nonnegative `a`, define

`Phi_a(C;R_+,R_-)`

`= sup [sqrt(a+Tr Z_+) + sqrt(Tr Z_-)]^2`.

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

Hence the curvature allocation is exactly one scalar minimization over an SDP value.

Important closed forms:

- one-sided:
  `Phi_a(C;R,0)=a+Tr Short_R(C)`;
- coincident synthesized subspaces, `s=Tr Short_R(C)`:
  `Phi=(sqrt(a)+sqrt(s))^2` for `s<=a`,
  `Phi=2(a+s)` for `s>=a`;
- decoupled orthogonal subspaces:
  `Phi=[sqrt(a+s_+)+sqrt(s_-)]^2`.

The physical finite-copy bound is

`boxed: Tr F_N/N`

`<= min{Phi_(J_B^+)(C_Delta;R_+,R_-),`

`       Phi_(J_B^-)(C_Delta;R_-,R_+)}`.

Replacing `J_B^+/-` by their WP11 endpoint-resource ceilings gives a fully resource-reduced theorem.

#### Shared-kernel benchmark

For

`rho0=(I-|q><q|)/2`,

`|q>=(1/2)|0>+sqrt(5/8)|1>+[1/(2sqrt(2))]|2>`,

`A=|1><0|-sqrt(2)|2><1|`,

one has

`J_B^+=5/4`, `J_+=7/4`, `J_-=3`, `s=19/4`.

The exact allocation gives

`Phi=12`,

while separately charging the same curvature to both orientations gives approximately

`21.427`.

The allocation law removes about `43.996%` of that resource overcount. The SLD-QFI trace is `10.75`; that residual gap is measurement compatibility, not resource allocation.

Read:
`notes/WP12_EXACT_OPERATOR_CURVATURE_ALLOCATION_SDP_LAW.md`.

## Numerical gates

- `numerics/verify_robust_tangent_radius_law.py`
- `numerics/verify_relational_autonomous_laws.py`
- `numerics/verify_nonlinear_zero_radius_law.py`
- `numerics/verify_quadratic_synthesis_sum_rule.py`
- `numerics/verify_bilateral_synthesis_minkowski_law.py`
- `numerics/verify_one_sided_mixed_survival_synthesis_law.py`
- `numerics/verify_shorted_endpoint_master_law.py`
- `numerics/verify_operator_curvature_allocation_law.py`

WP12 validation checks the scalar variational identity, random two-dimensional rank-one allocation problems, one-sided/identical/orthogonal closed forms, and the exact shared-kernel qutrit benchmark.

## Current open frontier — spectral-energy allocation

### 1. Put endpoint energy into the SDP itself

WP12 allocates total kernel curvature. For an exact temporal gap, define endpoint contractions

`W_U=Q Pi_U Q`,

`W_D=Q Pi_D Q`.

Seek a positive operator cost whose value on `Z_+` and `Z_-` measures the actual upper/lower spectral population or energy action required by each orientation.

### 2. Candidate weighted allocation

Study optimization problems of the form

`max [sqrt(a+Tr Z_+) + sqrt(Tr Z_-)]^2`

subject to

`Z_+ + Z_- <= C_Delta`

plus a fixed energy/action budget

`Tr(G_+ Z_+) + Tr(G_- Z_-) <= E`.

Determine the optimal dual and whether the effective scalar coefficient is a harmonic/parallel sum of positive endpoint cost operators.

### 3. Rank-one principal-angle solution

Solve the case `R_+,R_-` rank one with arbitrary angle and arbitrary positive `C`. This should expose the exact interpolation between:

- decoupled additive allocation;
- coincident-subspace factor-two enhancement;
- singular principal-angle suppression.

### 4. Measurement compatibility

Test whether combining WP12 with a Holevo/RLD/SLD-compatible common-record bound can close the residual resource-versus-attainability gap without losing arbitrary-POVM rigor.

### 5. Autonomous relational lift

Apply the operator allocation from both clock and signal Hamiltonian viewpoints. Determine whether a globally stationary exchange requires matching shorted/allocation resources on both sides of the relational cut.

## Priority status

Shorted operators, parallel addition, SDP duality, minimax theory, PSD-cone curvature, rank-deficient QFI, and Holevo compatibility mathematics are established. Candidate novelty is restricted to their frequency-resolved temporal-information resource use. **Priority remains unverified, not certified.**

## Documentation rule

Every material theorem, counterexample, priority collision, or killed conjecture must be recorded immediately in this directory and reflected in `README.md`, `AGENTS.md`, and `ROADMAP.md`. Do not depend on chat history.
