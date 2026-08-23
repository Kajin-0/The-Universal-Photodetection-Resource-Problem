# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

**Started:** 2026-08-22

This is a distinct post-Rev11 foundational program. The frozen Rev11 paper remains on `agent/temporal-information-resource-law` and must not be rewritten from this branch absent a concrete defect.

## Grand question

> When signal, clock/reference, controller, detector, and memory are all finite physical systems and no ideal externally timed operation is free, what resource constrains creation, transmission, and recovery of temporal information at frequency `nu`?

Research is analytical/theoretical, falsification-first, and documentation-first. Established asymmetry/reference-frame theory, phase estimation, WAY, Page--Wootters, PSD-cone geometry, singular QFI/Bures geometry, principal angles/shorted operators, Fisher-symmetric measurements, and Gaussian metrology are infrastructure unless a distinct operational temporal-information theorem is isolated.

## Current frontier

**WP11 — noncommuting-support shorted-endpoint master law: analytic PASS and independently validated.**

The local theorem hierarchy now covers:

1. pre-existing finite-radius information;
2. one-sided boundary synthesis;
3. multimode synthesis budgets;
4. bilateral synthesis interference;
5. one-sided mixed pre-existing+synthesis information;
6. arbitrary coherent noncommuting baseline support through endpoint shorting geometry.

The next high-value target is to replace WP11's scalar shorting constants and separately charged kernel curvatures by the **tight operator-valued allocation problem**.

## Completed work packages

### WP02 — robust tangent-radius law

For exact gap `nu`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N^(nu)/N] <= min(D_nu,U_nu) <= T(nu)`.

Hence

`Ebar+ >= (hbar nu R_lin^2/4)[Tr F_N^(nu)/N]`.

### WP03 / WP06 — relational dual survival and coherent-history extension

For a globally stationary clock--signal exchange tangent,

`K_N=(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`.

The total-energy coefficient `2` is asymptotically sharp. WP06 removes separate local stationarity: pre-existing Page--Wootters/history-state coherence does not evade the law.

### WP04 / WP05 — exact structured autonomous retention

Hard total-excitation cap:

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

Mean-total-energy envelope:

`R_M(1) <= (1-lambda)g_m+lambda g_(m+1)`,

`g_L=cos^2[pi/(L+2)]`.

Sine-chain extremizers make the near-lossless coefficient `pi` exactly sharp under both hard and mean total energy.

### WP07 — one-sided zero-radius synthesis

For `P=supp(rho0)` and baseline-empty endpoint `P_U`, with

`A=P_U A P`,

define

`J=Tr(A rho0^+ A^dagger)`.

Then for every finite `N` and arbitrary entangled collective POVM,

`boxed: Tr F_N/N <= J <= Delta T_U(0)`.

The minimal qubit and coherent-sideband constructions saturate the coefficient.

### WP08 — multimode quadratic synthesis budget

For mutually orthogonal baseline-empty modes and one common arbitrary collective measurement,

`boxed: sum_k w_k Tr F_(N,k)/N <= sum_k w_k Delta_k T_k(0)`

for every nonnegative weight sequence.

Gap weighting gives

`boxed: sum_k hbar nu_k Tr F_(N,k)/(4N) <= E_gap,syn^(2)`.

Multimode coherent sidebands with common heterodyne readout saturate every positive weighted sum simultaneously.

### WP09 — bilateral zero-radius Minkowski law

For arbitrary rank-deficient baseline,

`A=X+Y^dagger`,

`X=A P`, `Y=Q A^dagger P`,

with weighted norms `J_X,J_Y`,

`boxed: sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

For orthogonal empty upper/lower endpoints,

`boxed: Tr F_N/N <= [sqrt(Delta T_+)+sqrt(Delta T_-)]^2`.

An exact-gap qutrit Fourier experiment proves ordinary additive endpoint accounting false by exactly factor two and saturates the Minkowski law. Equal positive gap costs obey the sharp `hbar nu/8` synthesis-action coefficient.

### WP10 — one-sided mixed survival+synthesis law

Assume `[P,H]=0` and no lower-endpoint synthesis. Write

`A_nu=B+K`,

`B=P A_nu P`, `K=Q A_nu P`.

Then

`boxed: Tr F_N/N <= J_B+J_K`

with

`J_B <= 4T_pre/R_B^2`,

`J_K <= Delta T_syn(0)`.

Therefore

`boxed: Tr F_N/N <= 4T_pre/R_B^2 + Delta T_syn(0)`.

A qutrit normalized-congruence family plus one Fourier measurement simultaneously saturates all terms. The sharp positive energy/action law is

`boxed: Ebar+/R_B^2 + E_syn^(2) >= (hbar nu/4)[Tr F_N/N]`.

### WP11 — noncommuting baseline support / shorted endpoints

Let the **full** tangent be exact gap,

`[H,A_nu]=hbar nu A_nu`,

with arbitrary rank-deficient baseline

`P=supp(rho0)`, `Q=I-P`.

First-order physicality gives `Q A_nu Q=0`. Decompose

`B=P A_nu P`,

`K_+=Q A_nu P`,

`K_-=Q A_nu^dagger P`.

Define

`J_B^+=Tr(B rho0^+ B^dagger)`,

`J_B^-=Tr(B^dagger rho0^+ B)`,

`J_+=Tr(K_+ rho0^+ K_+^dagger)`,

`J_-=Tr(K_- rho0^+ K_-^dagger)`.

The finite-copy arbitrary-POVM measurement law is

`boxed: sqrt[Tr F_N/N]`

`<= min{sqrt(J_B^+ + J_+) + sqrt(J_-),`

`       sqrt(J_B^- + J_-) + sqrt(J_+)}`.

Let `Pi_U,Pi_D` be participating energy endpoint projectors and set

`S_U=P Pi_U P`, `S_D=P Pi_D P`,

`W_U=Q Pi_U Q`, `W_D=Q Pi_D Q`.

For the internal information-bearing range projectors `R_B^+,R_B^-`, define

`lambda_U=sup{lambda:S_U >= lambda R_B^+}`,

`lambda_D=sup{lambda:S_D >= lambda R_B^-}`.

For synthesized range projectors `R_+,R_-`, define

`mu_U=sup{mu:W_U >= mu R_+}`,

`mu_D=sup{mu:W_D >= mu R_-}`.

With

`C_Delta=Q(partial_x^2 rho+partial_y^2 rho)Q`,

`Gamma_U=Tr(W_U C_Delta)`,

`Gamma_D=Tr(W_D C_Delta)`,

one obtains

`J_B^+ <= 4T_U/(R_B^2 lambda_U)`,

`J_B^- <= 4T_D/(R_B^2 lambda_D)`,

`J_+ <= Gamma_U/mu_U`,

`J_- <= Gamma_D/mu_D`.

Define

`B_U=4T_U/(R_B^2 lambda_U)`,

`B_D=4T_D/(R_B^2 lambda_D)`,

`S_U=Gamma_U/mu_U`,

`S_D=Gamma_D/mu_D`.

Then

`boxed: Tr F_N/N`

`<= min{[sqrt(B_U+S_U)+sqrt(S_D)]^2,`

`       [sqrt(B_D+S_D)+sqrt(S_U)]^2}`.

The generic master ceiling is not claimed globally sharp, but it reduces exactly to WP06, WP07, WP09, and WP10 in their solved limits.

#### Explicit necessity counterexample

Take

`H=hbar omega diag(0,1,2,3)`, `nu=2omega`,

`|r>=(1/2)|2>+(sqrt(3)/2)|3>`,

`rho0=(1/2)|0><0|+(1/2)|r><r|`,

`A_nu=|2><0|`.

Then `[P,H]!=0` and

`B=(1/2)|r><0|`,

`K_+=(sqrt(3)/2)|q><0|`.

The true internal norm is `J_B=1/2`. The naive WP10-style term without geometric correction is only

`4T_U/R_B^2=1/8`.

But

`lambda_U=1/4`,

which repairs the internal bound to equality. On the kernel side

`mu_U=3/4`

also repairs the curvature term exactly.

This is operationally necessary: a fixed one-copy POVM formed by classical randomization of scalar-SLD-optimal cosine and sine measurements has

`Tr F=7/4`,

while the naive no-geometry total resource ceiling is

`13/8`.

Thus omitting endpoint-support geometry gives a false observable Fisher bound.

Read:
`notes/WP11_SHORTED_ENDPOINT_MASTER_LAW_NONCOMMUTING_SUPPORT.md`.

## Numerical gates

- `numerics/verify_robust_tangent_radius_law.py`
- `numerics/verify_relational_autonomous_laws.py`
- `numerics/verify_nonlinear_zero_radius_law.py`
- `numerics/verify_quadratic_synthesis_sum_rule.py`
- `numerics/verify_bilateral_synthesis_minkowski_law.py`
- `numerics/verify_one_sided_mixed_survival_synthesis_law.py`
- `numerics/verify_shorted_endpoint_master_law.py`

WP11 validation uses randomized noncommuting rank-2 qutrit supports, exact-gap tangents satisfying `Q A Q=0`, arbitrary one-copy POVMs, random two-copy collective POVMs, support/kernel shorting inequalities, and the explicit four-level operational counterexample.

## Current open frontier — WP12 operator-valued curvature allocation

WP11 converts endpoint geometry to scalar constants, but this can be loose because the same kernel curvature can contribute to both `Gamma_U` and `Gamma_D`.

Highest priority:

1. retain Anderson--Trapp shorted operators instead of reducing immediately to `lambda,mu`;
2. formulate the joint feasible allocation
   `Z_+>=0, Z_->=0, Z_++Z_-<=C_Delta`
   with the required range/endpoint constraints;
3. maximize the measurement-side Minkowski functional over that feasible set;
4. derive a finite-dimensional SDP/variational expression for the tightest curvature-only resource ceiling;
5. solve overlapping-subspace special cases analytically and seek exact extremizers;
6. lift the final operator law to both sides of an autonomous clock--signal cut.

## Priority status

Shorted operators, principal angles, rank-deficient QFI, PSD-cone geometry, and scalar SLD attainability are established. Candidate novelty is restricted to the frequency-resolved temporal-information use of these objects and the necessity/sharpness statements above. **Priority remains unverified, not certified.**

## Read first

1. `notes/WP11_SHORTED_ENDPOINT_MASTER_LAW_NONCOMMUTING_SUPPORT.md`
2. `notes/WP10_SHARP_ONE_SIDED_MIXED_SURVIVAL_SYNTHESIS_LAW.md`
3. `notes/WP09_SHARP_BILATERAL_SYNTHESIS_MINKOWSKI_LAW.md`
4. `notes/WP08_QUADRATIC_SPECTRAL_SYNTHESIS_SUM_AND_ENERGY_LAW.md`
5. `notes/WP07_NONLINEAR_ZERO_RADIUS_CURVATURE_AND_FINITE_AMPLITUDE_LAW.md`
6. `notes/WP06_NONSTATIONARY_ROBUST_TAIL_AND_HISTORY_STATE_EXTENSION.md`
7. `notes/WP05_EXACT_MEAN_ENERGY_AUTONOMOUS_RELATIONAL_RETENTION.md`
8. `notes/WP04_EXACT_HARD_CAP_AUTONOMOUS_RELATIONAL_RETENTION.md`
9. `notes/WP03_RELATIONAL_DUAL_ENERGY_SURVIVAL_LAW.md`
10. `notes/WP02_LOCAL_FISHER_NO_GO_AND_ROBUST_TANGENT_RADIUS_LAW.md`
11. `notes/WP01_FOUNDATIONAL_SCOPE_AND_PRIOR_ART_BOUNDARY.md`
12. `ROADMAP.md`

## Documentation rule

Every material theorem, counterexample, priority collision, or killed conjecture must be recorded immediately in this directory and reflected in `README.md`, `AGENTS.md`, and `ROADMAP.md`. Do not depend on chat history. Keep Rev11 frozen and separately advertised until this branch reaches its own publication gate.
