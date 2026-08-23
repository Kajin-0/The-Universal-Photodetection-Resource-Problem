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

Let the **full** tangent remain an exact gap but allow

`[P,H] != 0`, `P=supp(rho0)`.

First-order physicality gives `Q A Q=0`. Decompose

`B=PAP`,

`K_+=QAP`,

`K_-=QA^dagger P`.

Define weighted norms

`J_B^+=Tr(B rho0^+ B^dagger)`,

`J_B^-=Tr(B^dagger rho0^+ B)`,

`J_+=Tr(K_+ rho0^+ K_+^dagger)`,

`J_-=Tr(K_- rho0^+ K_-^dagger)`.

Measurement-side finite-copy law:

`boxed: sqrt[Tr F_N/N]`

`<= min{sqrt(J_B^+ + J_+) + sqrt(J_-),`

`       sqrt(J_B^- + J_-) + sqrt(J_+)}`.

Let `Pi_U,Pi_D` be the participating energy endpoint projectors and define

`S_U=P Pi_U P`, `S_D=P Pi_D P`,

`W_U=Q Pi_U Q`, `W_D=Q Pi_D Q`.

Internal shorting constants:

`lambda_U=sup{lambda:S_U >= lambda R_B^+}`,

`lambda_D=sup{lambda:S_D >= lambda R_B^-}`.

Kernel shorting constants:

`mu_U=sup{mu:W_U >= mu R_+}`,

`mu_D=sup{mu:W_D >= mu R_-}`.

For

`C_Delta=Q(partial_x^2 rho+partial_y^2 rho)Q`,

`Gamma_U=Tr(W_U C_Delta)`,

`Gamma_D=Tr(W_D C_Delta)`,

one has

`J_B^+ <= 4T_U/(R_B^2 lambda_U)`,

`J_B^- <= 4T_D/(R_B^2 lambda_D)`,

`J_+ <= Gamma_U/mu_U`,

`J_- <= Gamma_D/mu_D`.

Hence, with

`B_U=4T_U/(R_B^2 lambda_U)`,

`B_D=4T_D/(R_B^2 lambda_D)`,

`S_U=Gamma_U/mu_U`,

`S_D=Gamma_D/mu_D`,

`boxed: Tr F_N/N`

`<= min{[sqrt(B_U+S_U)+sqrt(S_D)]^2,`

`       [sqrt(B_D+S_D)+sqrt(S_U)]^2}`.

The generic scalar master bound is not claimed globally sharp, but it reduces exactly to WP06, WP07, WP09, and WP10 in the solved limits.

#### Necessity of shorting geometry

Exact four-level counterexample:

`H=hbar omega diag(0,1,2,3)`, `nu=2omega`,

`|r>=(1/2)|2>+(sqrt(3)/2)|3>`,

`rho0=(1/2)|0><0|+(1/2)|r><r|`,

`A=|2><0|`.

Then

`J_B=1/2`,

but the naive no-geometry internal term is only

`4T_U/R_B^2=1/8`.

The exact support shorting constant is

`lambda_U=1/4`,

which restores equality. The kernel shorting constant is

`mu_U=3/4`

and likewise restores the exact synthesis norm.

The omission is operationally fatal: a fixed randomized scalar-SLD POVM gives

`Tr F=7/4 > 13/8`,

where `13/8` is the naive total resource ceiling with the geometric factor omitted.

Thus endpoint-support geometry is required for observable Fisher information.

## Current frontier — WP12: operator-valued allocation law

WP11's scalar constants are rigorous but can overcount when upper- and lower-oriented synthesis components draw on overlapping kernel curvature.

### A. Retain shorted operators themselves

For a positive kernel curvature operator `C_Delta` and an information-bearing subspace `R`, the Anderson--Trapp short

`Short_R(C_Delta)`

is the largest positive operator below `C_Delta` whose range lies in `R`.

For a single synthesized orientation this immediately suggests the tighter resource

`J_+ <= Tr Short_(R_+)(C_Delta)`

when only the support constraint is used.

Derive the endpoint-weighted version that also enforces compatibility with `W_U=Q Pi_U Q` rather than collapsing to the scalar `mu_U`.

### B. Joint curvature allocation

The actual second-order condition is

`Z_+ + Z_- <= C_Delta`,

not two independent inequalities.

Define the feasible set

`A(C_Delta;R_+,R_-)`

of positive pairs `(Z_+,Z_-)` satisfying

- `Z_+>=0`, `Z_->=0`;
- `range(Z_+) subseteq R_+`;
- `range(Z_-) subseteq R_-`;
- `Z_+ + Z_- <= C_Delta`;
- endpoint-weighted constraints inherited from `W_U,W_D` if necessary.

The sharp curvature-only Fisher ceiling should be obtained by maximizing the WP11 measurement functional over this feasible set.

### C. Candidate variational resource

For a fixed upper-oriented internal resource `a>=0`, define

`Phi_a(C_Delta;R_+,R_-)`

`= sup_(Z_+,Z_- in A)`

`[sqrt(a+Tr Z_+) + sqrt(Tr Z_-)]^2`.

The conjugate orientation gives a second functional with `a` attached to the lower side. The final bound should take the minimum of the two.

Questions:

1. Can `Phi_a` be represented as an SDP or one-dimensional convex dual?
2. Does the optimizer lie at an extreme decomposition of `C_Delta`?
3. When `R_+ perp R_-`, does it reduce exactly to WP09?
4. When `R_+=R_-`, what closed form results?
5. Can endpoint-weighted shorting be incorporated without destroying convexity?

### D. Analytic overlapping-subspace benchmark

If `R_+=R_-=R` and the only known scalar is

`s=Tr Short_R(C_Delta)`,

then the relaxed allocation has `j_++j_-<=s`.

For fixed internal `a`, maximize

`f(j)=[sqrt(a+j)+sqrt(s-j)]^2`, `0<=j<=s`.

The stationary point is `j=(s-a)/2` when `s>=a`. Therefore the relaxed closed form is

`Phi(a,s)=`

- `(sqrt(a)+sqrt(s))^2`, for `s<=a`;
- `2(a+s)`, for `s>=a`.

Verify this algebraically and determine whether an exact quantum family can attain it.

### E. Autonomous relational lift

After the one-system allocation law is understood, apply it from both clock and signal viewpoints to a globally stationary exchange tangent. Test whether the shorting/allocation objects must appear on **both** sides of the relational cut.

### F. Priority and significance gate

Search deeply against shorted-operator decomposition/parallel addition, semidefinite resource allocation, singular quantum estimation, quantitative WAY/reference-frame theory, and Gaussian covariance estimation.

Do not draft the new foundational manuscript until WP12 either produces a sharp operator allocation theorem or shows that the remaining optimization is standard/prior art.

## Validation requirements

- add an independent WP12 numerical/SDP validator;
- test random overlapping `R_+,R_-` subspaces;
- test orthogonal and identical-subspace limits;
- test one- and two-copy arbitrary POVMs;
- construct at least one exact physical family saturating any claimed closed form.

## Documentation discipline

Every material theorem, failed conjecture, prior-art collision, or validation result must be recorded immediately in the branch and reflected in `README.md`, `AGENTS.md`, and this file. The repository, not chat history, is authoritative.
