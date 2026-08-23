# Roadmap — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

## Goal

Seek a foundational physical resource principle for temporal information when clock, signal, controller, detector, and memory are all internal quantum systems. The finished Rev11 random-time law remains frozen on its parent branch.

## Completed foundations

### WP01 — prior-art/model boundary — PASS

Do not claim novelty for standard asymmetry/reference-frame theory, QFI-as-asymmetry, finite clocks, Page--Wootters, WAY, standard phase estimation, PSD-cone curvature, singular QFI/Bures geometry, Fisher-symmetric measurements, Gaussian displacement/Holevo theory, or generic waveform estimation.

### WP02 — robust tangent-radius law — PASS

`(R_lin^2/4)[Tr F_N^(nu)/N] <= min(D_nu,U_nu) <= T(nu)`

for exact gap `nu`, finite `N`, and arbitrary collective POVM.

Hence

`Ebar+ >= (hbar nu R_lin^2/4)[Tr F_N^(nu)/N]`.

### WP03 — autonomous relational dual survival — PASS

`K_N=(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`,

so

`Ebar_C^+ + Ebar_S^+ >= 2 hbar nu K_N`.

The factor `2` is asymptotically sharp.

### WP04 / WP05 — exact structured autonomous retention — PASS

Hard cap:

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

Mean total excitation `Lbar=m+lambda`:

`R_M(1) <= (1-lambda)g_m+lambda g_(m+1)`,

`g_L=cos^2[pi/(L+2)]`.

Sine-chain extremizers make the near-unit coefficient `pi` sharp under both hard and mean total energy.

### WP06 — arbitrary coherent-baseline tail law — PASS

For arbitrary `rho`, positive `R_lin`, range projector `P_U`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N/N] <= Tr(P_U rho)`.

### WP07 — one-sided zero-radius synthesis — PASS

For `A=P_U A P`, `P=supp(rho0)`, baseline-empty `P_U`,

`boxed: Tr F_N/N <= J(A|rho0) <= Delta T_U(0)`.

The minimal qubit and coherent-sideband constructions saturate the coefficient.

### WP08 — multimode quadratic synthesis budget — PASS

For one common arbitrary collective measurement,

`boxed: sum_k w_k Tr F_(N,k)/N <= sum_k w_k Delta_k T_k(0)`

for arbitrary `w_k>=0`.

With gap weights,

`boxed: sum_k hbar nu_k Tr F_(N,k)/(4N) <= E_gap,syn^(2)`.

Multimode coherent sidebands with common heterodyne readout saturate every positive weighted sum.

### WP09 — bilateral zero-radius Minkowski law — PASS

For

`A=X+Y^dagger`,

`X=A P`, `Y=Q A^dagger P`,

`J_X=Tr(X rho0^+ X^dagger)`,

`J_Y=Tr(Y rho0^+ Y^dagger)`,

one has

`boxed: sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

For orthogonal baseline-empty upper/lower endpoints,

`boxed: Tr F_N/N <= [sqrt(Delta T_+)+sqrt(Delta T_-)]^2`.

The qutrit Fourier extremizer violates naive additive endpoint synthesis by exactly factor two and saturates the square-root law. Equal positive gap costs obey

`E_bi,syn^(2) >= (hbar nu/8)[Tr F_N/N]`.

### WP10 — one-sided mixed finite-radius + synthesis law — PASS

Assume

`P=supp(rho0)`, `[P,H]=0`,

`[H,A_nu]=hbar nu A_nu`,

`P A_nu Q=0`.

Write

`A_nu=B+K`,

`B=P A_nu P`,

`K=Q A_nu P`.

Then for every finite `N` and arbitrary collective POVM,

`boxed: Tr F_N/N <= J_B+J_K`.

If `R_B` is the support-preserving sub-tangent radius, `T_pre` the pre-existing upper endpoint population, and `T_syn` the newly synthesized upper endpoint population,

`J_B <= 4T_pre/R_B^2`,

`J_K <= Delta T_syn(0)`.

Therefore

`boxed: Tr F_N/N <= 4T_pre/R_B^2 + Delta T_syn(0)`.

This additive composition is exactly sharp. The qutrit family

`rho0=p0|0><0|+p1|1><1|`,

`A_nu=kappa p0|1><0|+kappa p1|2><1|`

with a normalized congruence family and one Fourier measurement simultaneously saturates

`Tr F_1=J_B+J_K=4T_pre/R_B^2+Delta T_syn=kappa^2`.

The positive energy/action form

`boxed: Ebar+/R_B^2 + E_syn^(2) >= (hbar nu/4)[Tr F_N/N]`

is likewise sharp.

This resolves the mixed **commuting-support / one-sided** bridge: same-orientation pre-existing and synthesis resources add, whereas opposite-orientation synthesis obeys the WP09 Minkowski law.

## Current frontier — WP11: noncommuting baseline support

### A. Core obstruction

Remove `[P,H]=0` while keeping the full `A_nu` an exact Bohr-gap operator.

When `[P,H] != 0`, the support pieces

`P A_nu P`, `Q A_nu P`, `P A_nu Q`

are generally not exact-gap operators. Therefore the WP10 proof cannot attach independent energy endpoints to those support pieces.

### B. First target: principal-angle bridge

Let `P_U` and `P_D` be the participating upper/lower energy endpoint projectors. Study the compressed positive contractions

`S_U=P P_U P`,

`S_D=P P_D P`

and the kernel-side contractions

`W_U=Q P_U Q`,

`W_D=Q P_D Q`.

Their nonzero eigenvalues are squared cosines/sines of principal angles between baseline support and endpoint subspaces.

Test whether these operators provide the minimal geometric correction required to convert the abstract WP09 norms `J_X,J_Y` into physical spectral resources.

### C. Candidate support-internal estimate

For the support-preserving compression `B=P A_nu P`, its range lies in `range(P P_U)`. If `R_U=supp(S_U)` and `lambda_U` is the smallest positive eigenvalue of `S_U`, then a plausible rigorous chain is

`J_B^+ <= 4 Tr(R_U rho)/R_B^2`

and

`Tr(P_U rho)=Tr(S_U rho) >= lambda_U Tr(R_U rho)`,

which would imply

`J_B^+ <= 4 T_U/(R_B^2 lambda_U)`.

Derive this carefully, including the lower-orientation analogue and all zero-eigenvalue cases. Determine sharpness and whether the principal-angle penalty is unavoidable.

### D. Kernel synthesis geometry

Second-order positivity gives a kernel curvature operator rather than a clean energy-sector scalar when `P_U` and `P` do not commute.

Test endpoint-weighted kernel curvature objects such as

`Tr[Q P_U Q C_Delta]`,

where

`C_Delta=Q(partial_x^2 rho + partial_y^2 rho)Q`.

Determine whether principal-angle eigenvalues convert these quantities into rigorous bounds on the support-to-kernel weighted tangent norm.

### E. Scalar sufficiency / no-go test

Construct exact-gap low-dimensional models with noncommuting `P` and `H` and ask whether the sharp information ceiling is determined by only:

- baseline upper/lower scalar tails;
- one internal tangent radius;
- total upper/lower scalar synthesis curvature.

If two models can share these scalars but have different `J_X,J_Y` or attainable Fisher information, record a scalar-insufficiency theorem and promote the operator geometry as necessary.

### F. Numerical protocol

For candidate WP11 laws:

1. use 3--5 level equally spaced Hamiltonians;
2. generate coherent rank-deficient baseline supports not diagonal in energy;
3. enforce the physical tangent condition `Q A Q=0` for exact-gap shifts;
4. test random POVMs and explicit Fourier/phase POVMs;
5. test `N=2` collective measurements;
6. sweep principal angles toward `0` and `pi/2` to test singular limits;
7. require reduction to WP06, WP07, WP09, and WP10.

### G. Priority audit

Search against shorted operators, principal-angle inequalities, PSD block matrix completion, singular quantum estimation, support-changing models, and coherence/asymmetry resource theory. Do not claim novelty for the matrix-analysis machinery.

## Secondary open directions

- full finite-amplitude phase orbit with support change;
- Gaussian covariance/squeezing synthesis beyond displacement;
- autonomous dynamical interaction/action resource;
- collective-N mean-energy retention beyond WP05;
- many-body/cut-set laws;
- continuum synthesis limits.

## Publication / significance gate

Do not draft the foundational manuscript yet. First require a sharp WP11 theorem or scalar-insufficiency result, deep priority audit, hostile mathematical review, sharp constructions, and a clear autonomous physical consequence.

## Documentation discipline

Every material theorem, failed conjecture, prior-art collision, or validation result must be recorded immediately in the branch and reflected in `README.md`, `AGENTS.md`, and this file. The repository, not chat history, is authoritative.
