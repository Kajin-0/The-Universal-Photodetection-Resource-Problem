# Autonomous Temporal Information Law

This directory contains the post-Rev11 foundational research program.

**Branch:** `agent/autonomous-temporal-information-law`

The frozen Rev11 paper remains untouched on `agent/temporal-information-resource-law`.

## Grand challenge

Determine what physical resource constrains temporal information when clock/reference, signal, controller, detector, and memory are all finite internal systems and no ideal external timing operation is supplied for free.

## Current theorem stack

### WP01 — prior-art boundary

Modes of asymmetry, QFI as asymmetry, finite quantum clocks, Page--Wootters relational time, quantitative WAY, phase-estimation sine states, PSD-cone curvature, singular QFI/Bures geometry, Fisher-symmetric measurements, Gaussian displacement/Holevo theory, and generic waveform-estimation bounds are prior art. The target must be a distinct operational temporal-information resource law.

### WP02 — robust tangent-radius law

Fixed baseline mean energy does not bound arbitrary high-frequency local Fisher information because the physically valid tangent neighborhood can shrink with frequency. For exact gap `nu`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N^(nu)/N] <= T(nu)`.

Hence

`Ebar+ >= (hbar nu R_lin^2/4)[Tr F_N^(nu)/N]`.

### WP03 — autonomous relational dual survival

For an exact globally stationary exchange tangent,

`K_N=(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`,

so

`Ebar_C^+ + Ebar_S^+ >= 2 hbar nu K_N`.

The coefficient `2` is asymptotically sharp.

### WP04 / WP05 — exact autonomous retention under hard and mean total energy

For the structured globally stationary relative-time experiment with hard cap `L`,

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

At the fundamental mode,

`E_max >= hbar nu[pi/arccos(sqrt R)-2]`,

with sharp near-unit asymptotic

`E_max >= pi hbar nu/sqrt(1-R)[1+o(1)]`.

For mean total excitation `Lbar=m+lambda`, with

`g_L=cos^2[pi/(L+2)]`,

the exact one-copy envelope is

`R_M(1) <= (1-lambda)g_m+lambda g_(m+1)`.

Adjacent-shell sine-chain mixtures attain equality, so the mean-energy asymptotic coefficient is also exactly `pi`.

### WP06 — arbitrary coherent baselines / history states

For arbitrary baseline `rho`, positive `R_lin`, tangent range projector `P_U`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N/N] <= Tr(P_U rho)`.

Thus pre-existing Page--Wootters/history-state relational coherence does not evade the robust upper-tail theorem.

### WP07 — nonlinear zero-radius synthesis

For baseline-empty endpoint `P_U`, `P=supp(rho0)`, and

`A=P_U A P`,

let

`J=Tr(A rho0^+ A^dagger)`.

Then for every finite `N` and arbitrary entangled collective POVM,

`boxed: Tr F_N/N <= J <= Delta T_U(0)`.

The resource moves from zeroth-order endpoint population to second-order endpoint synthesis. The minimal qubit and coherent-sideband constructions saturate the coefficient.

### WP08 — quadratic spectral-synthesis sum/energy law

For mutually orthogonal baseline-empty endpoint modes and one common arbitrary collective measurement,

`Tr F_(N,k)/N <= Delta_k T_k(0)`.

Hence for any `w_k>=0`,

`boxed: sum_k w_k Tr F_(N,k)/N <= sum_k w_k Delta_k T_k(0)`.

With

`E_gap,syn^(2)=(hbar/4)sum_k nu_k Delta_k T_k(0)`,

`boxed: sum_k hbar nu_k Tr F_(N,k)/(4N) <= E_gap,syn^(2)`.

Multimode coherent sidebands with one common heterodyne measurement saturate every mode and every positive weighted sum simultaneously.

### WP09 — sharp bilateral-synthesis Minkowski law

For arbitrary rank-deficient baseline, with

`P=supp(rho0)`, `Q=I-P`,

a physical complex tangent (`Q A Q=0`) can be written

`A=X+Y^dagger`,

`X=A P`, `Y=Q A^dagger P`.

Define

`J_X=Tr(X rho0^+ X^dagger)`,

`J_Y=Tr(Y rho0^+ Y^dagger)`.

For every finite `N` and arbitrary collective POVM,

`boxed: sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

For orthogonal baseline-empty upper/lower endpoint sectors,

`boxed: Tr F_N/N <= [sqrt(Delta T_+)+sqrt(Delta T_-)]^2`.

An exact-gap qutrit Fourier experiment saturates this law and violates naive additive endpoint synthesis by exactly factor two. Equal positive gap costs therefore obey the sharp bilateral law

`E_bi,syn^(2) >= (hbar nu/8)[Tr F_N/N]`.

### WP10 — sharp one-sided mixed survival+synthesis law

WP10 bridges the finite-radius and zero-radius regimes when the baseline support is energy invariant and only the **upper** endpoint is newly synthesized.

Assume

`P=supp(rho0)`, `[P,H]=0`,

`[H,A_nu]=hbar nu A_nu`,

`P A_nu Q=0`.

Write

`A_nu=B+K`,

`B=P A_nu P`,

`K=Q A_nu P`.

Let

`J_B=Tr(B rho0^+ B^dagger)`,

`J_K=Tr(K rho0^+ K^dagger)`.

Because the two pieces are right-supported on `P` and have orthogonal output support,

`boxed: Tr F_N/N <= J_B+J_K`.

Let `R_B` be the physical linear radius of the support-preserving sub-tangent `B`, let `T_pre(nu)` be its pre-existing upper endpoint population, and let `T_syn(x,y)` be the population of the baseline-empty upper endpoint. Then

`J_B <= 4T_pre/R_B^2`,

`J_K <= Delta T_syn(0)`.

Therefore

`boxed: Tr F_N/N <= 4T_pre(nu)/R_B^2 + Delta T_syn(0)`.

This **additive** composition is sharp. For

`H=hbar nu diag(0,1,2)`,

`rho0=p0|0><0|+p1|1><1|`,

`A_nu=kappa p0|1><0|+kappa p1|2><1|`,

a normalized congruence family realizes the exact tangent and saturates the synthesis curvature, while one three-outcome Fourier measurement gives

`Tr F_1=kappa^2`

and simultaneously

`Tr F_1=J_B+J_K=4T_pre/R_B^2+Delta T_syn`.

The positive mixed energy/action law is

`boxed: Ebar+/R_B^2 + E_syn^(2)(nu) >= (hbar nu/4)[Tr F_N/N]`,

with

`E_syn^(2)=(hbar nu/4)Delta T_syn`.

The same qutrit family saturates this coefficient exactly.

This establishes an orientation-dependent resource algebra:

- same-orientation pre-existing + synthesis contributions add;
- opposite-orientation bilateral synthesis combines by square roots/Minkowski.

## Current frontier — noncommuting-support resource geometry

The remaining hard case is now sharply isolated: remove `[P,H]=0` while keeping the **full** tangent an exact Bohr-gap operator.

When baseline support and Hamiltonian endpoint subspaces do not commute, `PAP`, `QAP`, and `PAQ` generally cease to be independent exact-gap operators. A sharp reduction of the WP09 weighted tangent norms to physical spectral resources may therefore require:

- principal angles between baseline support and energy endpoint subspaces;
- compressed endpoint operators such as `P P_U P`;
- shorted operators / Schur complements;
- an operator-valued resource rather than scalar tail/radius/curvature data.

A rigorous scalar-insufficiency theorem would be a valid major result.

## Validation

Independent numerical/adversarial validators:

- `numerics/verify_robust_tangent_radius_law.py`
- `numerics/verify_relational_autonomous_laws.py`
- `numerics/verify_nonlinear_zero_radius_law.py`
- `numerics/verify_quadratic_synthesis_sum_rule.py`
- `numerics/verify_bilateral_synthesis_minkowski_law.py`
- `numerics/verify_one_sided_mixed_survival_synthesis_law.py`

## Priority discipline

The mathematical ingredients overlap strongly with phase estimation, asymmetry/reference-frame theory, Page--Wootters, PSD-cone geometry, singular QFI/Bures geometry, Fisher-symmetric measurements, Gaussian displacement estimation, and waveform estimation. Targeted searches have not identified exact predecessors for the combined WP07--WP10 finite-copy frequency-resolved resource laws, but **priority remains unverified, not certified**.

Read `AGENTS.md`, `ROADMAP.md`, and WP01--WP10 before continuing. Record every material theorem, counterexample, prior-art collision, or killed conjecture immediately; do not rely on chat history.
