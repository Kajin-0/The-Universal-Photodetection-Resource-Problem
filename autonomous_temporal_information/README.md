# Autonomous Temporal Information Law

This directory contains the new post-Rev11 foundational research program.

**Branch:** `agent/autonomous-temporal-information-law`

The frozen Rev11 paper remains untouched on `agent/temporal-information-resource-law`.

## Grand challenge

Determine whether there exists a general physical resource law governing temporal information when **all timing and control resources are internal physical systems**, rather than ideal classical clocks or free time-dependent Hamiltonians.

The emerging hierarchy is

`temporal Fisher information`

`x physical robustness / synthesis scale`

`-> spectral resource`,

and, for autonomous relational clock--signal information,

`matching exchange structure on clock and signal`

`-> finite-resource temporal-information retention`.

## Current theorem stack

### WP01 — prior-art and model boundary

Qualitative mode support, QFI-as-asymmetry, finite quantum clocks, WAY tradeoffs, Page--Wootters relational time, standard phase-estimation sine states, PSD-cone curvature, singular QFI/Bures geometry, and Gaussian displacement/Holevo theory are prior art. The target must be a quantitative operational temporal-information law.

### WP02 — local Fisher no-go and robust tangent radius

Fixed baseline mean energy does **not** bound arbitrarily high-frequency local Fisher information for general state synthesis: the physical parameter neighborhood can shrink with frequency.

For linear tangent radius `R_lin`, arbitrary finite-copy collective measurements satisfy

`(R_lin^2/4)[Tr F_N^(nu)/N] <= T(nu)`.

Hence

`Ebar+ >= (hbar nu R_lin^2/4)[Tr F_N^(nu)/N]`.

The fixed-energy/high-frequency counterexample asymptotically saturates the corrected law.

### WP03 — autonomous relational dual-survival law

For an exact globally stationary clock--signal exchange tangent,

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`,

and

`K_N(nu)=(R_lin^2/4)[Tr F_N^(nu)/N]`,

one has

`K_N(nu) <= min{T_C(nu),T_S(nu)}`,

so

`Ebar_C^+ + Ebar_S^+ >= 2 hbar nu K_N(nu)`.

The coefficient `2` is asymptotically sharp under collective measurements.

### WP04 — exact hard-cap autonomous retention

For a globally stationary relative-time experiment with hard total excitation cap `L`,

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

At the fundamental frequency,

`E_max >= hbar nu[pi/arccos(sqrt R)-2]`,

and near perfect retention

`E_max >= pi hbar nu/sqrt(1-R)[1+o(1)]`.

Sine-chain history states attain equality.

### WP05 — exact mean-total-energy autonomous retention

With

`g_L=cos^2[pi/(L+2)]`

and

`Lbar=m+lambda`,

the exact sharp one-copy envelope is

`R_M(1) <= (1-lambda)g_m+lambda g_(m+1)`.

Adjacent-shell sine-chain mixtures attain equality, giving the same sharp near-unit-retention coefficient `pi` under a mean total-energy constraint.

### WP06 — arbitrary coherent baselines / history states

For arbitrary baseline `rho`, positive `R_lin`, tangent range projector `P_U`, and arbitrary finite-copy collective POVMs,

`(R_lin^2/4)[Tr F_N/N] <= Tr(P_U rho)`.

Thus the robust upper-tail theorem survives pre-existing Page--Wootters/history-state relational coherence; separate local stationarity is unnecessary.

### WP07 — nonlinear `R_lin=0` synthesis is resource-constrained

For a baseline-empty endpoint sector and the same two-quadrature complex tangent convention used throughout the project,

`A=P_U A P`, `P=supp(rho0)`,

set

`J(A|rho0)=Tr(A rho0^+ A^dagger)`.

Second-order PSD-cone geometry plus the direct arbitrary-POVM Fisher proof gives, for **every finite `N` and every entangled collective POVM**,

`boxed: Tr F_N/N <= J(A|rho0) <= Delta T_U(0)`.

Equivalently,

`boxed: (1/4)[Tr F_N/N] <= (1/4)Delta T_U(0)`.

The minimal zero-radius qubit saturates both inequalities with one fixed four-outcome equatorial POVM.

The earlier coherent-sideband counterexample also saturates the operational coefficient. For

`alpha_sb(x,y)=(A/2)(x+i y)`,

`n_sb=Nbar(x^2+y^2)/4`,

so

`Delta n_sb(0)=Nbar`,

and heterodyne readout gives

`Tr F=Nbar`.

Thus the loophole created by arbitrary waveform synthesis is paid for by **second-order endpoint population synthesis** rather than baseline population.

A complementary finite-amplitude `pi` phase-pair law gives

`D_tr^2/4 <= min{T_C(nu),T_S(nu)}`

and therefore

`Ebar_C^+ + Ebar_S^+ >= (hbar nu/2)D_tr^2`.

### WP08 — quadratic spectral-synthesis sum and energy law

Let `{P_k}` be mutually orthogonal baseline-empty endpoint sectors with mode parameters `(x_k,y_k)` and tangents

`A_k=P_k A_k P`.

For one fixed arbitrary collective POVM on `N` copies, let `F_(N,k)` be the Fisher block for mode `k`. WP07 applies to every block of the same record:

`Tr F_(N,k)/N <= Delta_k T_k(0)`.

Therefore, for arbitrary nonnegative weights `w_k`,

`boxed: sum_k w_k [Tr F_(N,k)/N] <= sum_k w_k Delta_k T_k(0)`.

With temporal-gap weights,

`E_gap,syn^(2):=(hbar/4)sum_k nu_k Delta_k T_k(0)`,

so

`boxed: sum_k hbar nu_k [Tr F_(N,k)/(4N)] <= E_gap,syn^(2)`.

This is the zero-radius analogue of a spectral information budget.

For multimode coherent sidebands

`alpha_k=g_k(x_k+i y_k)`,

one has

`Delta_k n_k(0)=4|g_k|^2`.

Multimode heterodyne gives

`Tr F_k=4|g_k|^2`,

so **every mode and every nonnegative weighted sum are saturated simultaneously** by one fixed measurement.

Using actual sideband photon energies `hbar omega_k` as weights gives the exact positive synthesis-energy identity

`sum_k (hbar omega_k/4)Tr F_k`

`= (1/4)sum_k Delta_k E_k(0)`.

Coherent-state displacement estimation, heterodyne/Holevo theory, and linear waveform-estimation limits are prior art. Candidate novelty is the frequency-resolved quadratic spectral-resource law and its connection to the earlier baseline-energy no-go.

## Current frontier — unified mixed endpoint law

The highest-value unresolved problem is now a general exact-gap tangent containing both:

- support-to-support components, charged by WP06 pre-existing spectral survival and `R_lin`;
- support-to-kernel or kernel-to-support components, charged by WP07/WP08 second-order endpoint synthesis.

The objective is a sharp arbitrary-POVM theorem that combines these contributions without double counting or losing the established constants. Score-space interference means a naive additive scalar law is not guaranteed; a proof of an unavoidable Minkowski/matrix geometry would also be a substantive result.

## Validation

Independent numerical/adversarial validators:

- `numerics/verify_robust_tangent_radius_law.py`
- `numerics/verify_relational_autonomous_laws.py`
- `numerics/verify_nonlinear_zero_radius_law.py`
- `numerics/verify_quadratic_synthesis_sum_rule.py`

The WP08 validator tests same-record random weighted sums, random two-copy collective POVMs, and exact multimode coherent heterodyne population/energy saturation.

## Priority discipline

The mathematical ingredients overlap strongly with phase estimation, asymmetry/reference-frame theory, Page--Wootters, PSD-cone geometry, singular QFI/Bures geometry, Gaussian displacement estimation, and quantum waveform estimation. Targeted searches have not identified exact predecessors for the combined WP07/WP08 finite-copy frequency-resolved synthesis laws, but **priority remains unverified, not certified**.

Read `AGENTS.md`, `ROADMAP.md`, and WP01--WP08 before continuing. Record every material theorem, counterexample, prior-art collision, or killed conjecture immediately; do not rely on chat history.
