# Autonomous Temporal Information Law

This directory contains the post-Rev11 foundational research program.

**Branch:** `agent/autonomous-temporal-information-law`

The frozen Rev11 paper remains untouched on `agent/temporal-information-resource-law`.

## Grand challenge

Determine what physical resource constrains temporal information when clock/reference, signal, controller, detector, and memory are all finite internal systems and no ideal external timing operation is supplied for free.

The emerging hierarchy is

`temporal Fisher information`

`x physical robustness / synthesis scale`

`-> spectral resource`,

with autonomous relational information requiring matched clock--signal exchange structure.

## Current theorem stack

### WP01 — prior-art boundary

Modes of asymmetry, QFI as asymmetry, finite quantum clocks, Page--Wootters relational time, quantitative WAY, phase-estimation sine states, PSD-cone curvature, singular QFI/Bures geometry, Gaussian displacement/Holevo theory, and generic waveform-estimation bounds are prior art. The target must be a distinct operational temporal-information resource law.

### WP02 — local Fisher no-go and robust tangent radius

Fixed baseline mean energy does **not** bound arbitrarily high-frequency local Fisher information for unrestricted state synthesis because the physically valid tangent neighborhood can shrink with frequency.

For exact gap `nu`, linear tangent radius `R_lin`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N^(nu)/N] <= T(nu)`.

Hence

`Ebar+ >= (hbar nu R_lin^2/4)[Tr F_N^(nu)/N]`.

The fixed-energy/high-frequency counterexample asymptotically saturates this corrected law.

### WP03 — autonomous relational dual-survival law

For an exact globally stationary exchange tangent

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`,

define

`K_N(nu)=(R_lin^2/4)[Tr F_N^(nu)/N]`.

Then

`K_N(nu) <= min{T_C(nu),T_S(nu)}`,

so

`Ebar_C^+ + Ebar_S^+ >= 2 hbar nu K_N(nu)`.

The coefficient `2` is asymptotically sharp under collective measurements.

### WP04 — exact hard-cap autonomous retention

For a globally stationary relative-time experiment with hard total-excitation cap `L`,

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

At the fundamental frequency,

`E_max >= hbar nu[pi/arccos(sqrt R)-2]`,

and near perfect retention

`E_max >= pi hbar nu/sqrt(1-R)[1+o(1)]`.

Sine-chain history states attain equality.

### WP05 — exact mean-total-energy autonomous retention

With

`g_L=cos^2[pi/(L+2)]`,

`Lbar=m+lambda`,

the exact one-copy envelope is

`R_M(1) <= (1-lambda)g_m+lambda g_(m+1)`.

Adjacent-shell sine-chain mixtures attain equality. The sharp near-unit mean-energy coefficient is again `pi`.

### WP06 — arbitrary coherent baselines / history states

For arbitrary baseline `rho`, positive `R_lin`, tangent range projector `P_U`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N/N] <= Tr(P_U rho)`.

Thus pre-existing Page--Wootters/history-state relational coherence does not evade the robust upper-tail theorem.

### WP07 — nonlinear `R_lin=0` synthesis law

For a baseline-empty endpoint and complex two-quadrature tangent

`A=P_U A P`, `P=supp(rho0)`,

define

`J(A|rho0)=Tr(A rho0^+ A^dagger)`.

For every finite `N` and arbitrary entangled collective POVM,

`boxed: Tr F_N/N <= J(A|rho0) <= Delta T_U(0)`.

Thus the zero-radius resource moves from zeroth-order endpoint population to **second-order endpoint population synthesis**.

The minimal qubit saturates the coefficient with a fixed four-outcome POVM. The coherent-sideband counterexample also saturates it under heterodyne readout:

`Delta n_sb(0)=Tr F_het=Nbar`.

A complementary finite-amplitude `pi` phase-pair law gives

`D_tr^2/4 <= min{T_C(nu),T_S(nu)}`.

### WP08 — quadratic spectral-synthesis sum and energy law

For mutually orthogonal baseline-empty endpoint sectors `P_k` and one fixed arbitrary collective measurement,

`Tr F_(N,k)/N <= Delta_k T_k(0)`

for every mode. Hence for arbitrary `w_k>=0`,

`boxed: sum_k w_k Tr F_(N,k)/N <= sum_k w_k Delta_k T_k(0)`.

With gap weights,

`E_gap,syn^(2)=(hbar/4)sum_k nu_k Delta_k T_k(0)`,

so

`boxed: sum_k hbar nu_k Tr F_(N,k)/(4N) <= E_gap,syn^(2)`.

Multimode coherent sidebands and one common heterodyne measurement saturate every mode and every nonnegative weighted sum simultaneously.

### WP09 — sharp bilateral-synthesis Minkowski law

For arbitrary rank-deficient `rho0`, let

`P=supp(rho0)`, `Q=I-P`,

and decompose every physical complex tangent with `Q A Q=0` as

`A=X+Y^dagger`,

`X=A P`,

`Y=Q A^dagger P`.

Define

`J_X=Tr(X rho0^+ X^dagger)`,

`J_Y=Tr(Y rho0^+ Y^dagger)`.

For every finite `N` and every arbitrary entangled collective POVM,

`boxed: sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

Thus

`boxed: Tr F_N/N <= (sqrt(J_X)+sqrt(J_Y))^2`.

For two orthogonal baseline-empty endpoint sectors,

`J_X<=Delta T_+`, `J_Y<=Delta T_-`,

so

`boxed: Tr F_N/N <= [sqrt(Delta T_+)+sqrt(Delta T_-)]^2`.

The square-root resource composition is **necessary**. On the exact-gap qutrit ladder

`H=hbar nu diag(0,1,2)`,

`rho0=|1><1|`,

`A=c(|2><1|+|1><0|)`,

a three-outcome Fourier measurement gives

`Tr F_1=4c^2`,

while

`Delta T_+ + Delta T_-=2c^2`.

Therefore the naive additive endpoint law fails by exactly a factor of two, whereas the Minkowski law is saturated exactly.

For equal positive gap costs,

`E_bi,syn^(2)=(hbar nu/4)(Delta T_+ + Delta T_-)`

obeys the sharp law

`boxed: E_bi,syn^(2) >= (hbar nu/8)[Tr F_N/N]`.

For unequal positive endpoint costs `epsilon_+,epsilon_-`, the effective coefficient is their harmonic combination

`epsilon_parallel=(1/epsilon_+ + 1/epsilon_-)^(-1)`.

Triangle/Minkowski inequalities, Fisher-symmetric measurement theory, and Fourier measurements are prior art. Candidate novelty is the frequency-resolved temporal-resource consequence and the unavoidable square-root endpoint geometry.

## Current frontier — fully mixed finite-radius + synthesis geometry

WP09 resolves bilateral **zero-radius** synthesis. The highest-value unresolved problem is now a tangent that simultaneously contains:

- genuinely pre-existing finite-radius information;
- support-to-kernel synthesis;
- kernel-to-support synthesis;
- noncommuting baseline support and Hamiltonian endpoint projectors.

The key obstacle is structural: support projection of an exact-gap operator need not itself remain an exact-gap operator when `[supp(rho),H] != 0`. The next theorem may require principal-angle, shorted-operator, or matrix-valued resource geometry rather than an additive scalar budget.

A sharp impossibility result proving that the usual scalar data are insufficient would be as valuable as a positive theorem.

## Validation

Independent numerical/adversarial validators:

- `numerics/verify_robust_tangent_radius_law.py`
- `numerics/verify_relational_autonomous_laws.py`
- `numerics/verify_nonlinear_zero_radius_law.py`
- `numerics/verify_quadratic_synthesis_sum_rule.py`
- `numerics/verify_bilateral_synthesis_minkowski_law.py`

The WP09 validator checks random rank-deficient one-copy POVMs, random two-copy collective POVMs, exact `N J_X/N J_Y` scaling, qutrit Fourier saturation, factor-two failure of additive endpoint accounting, the sharp `hbar nu/8` coefficient, and unequal-cost harmonic weighting.

## Priority discipline

The mathematical ingredients overlap strongly with phase estimation, asymmetry/reference-frame theory, Page--Wootters, PSD-cone geometry, singular QFI/Bures geometry, Fisher-symmetric measurements, Gaussian displacement estimation, and quantum waveform estimation. Targeted searches have not identified exact predecessors for the combined WP07--WP09 frequency-resolved finite-copy resource laws, but **priority remains unverified, not certified**.

Read `AGENTS.md`, `ROADMAP.md`, and WP01--WP09 before continuing. Record every material theorem, counterexample, prior-art collision, or killed conjecture immediately; do not rely on chat history.
