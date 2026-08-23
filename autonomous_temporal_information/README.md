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

Qualitative mode support, QFI-as-asymmetry, finite quantum clocks, WAY tradeoffs, Page--Wootters relational time, standard phase-estimation sine states, PSD-cone curvature, and singular QFI/Bures geometry are prior art. The target must be a quantitative operational temporal-information law.

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

Let

`g_L=cos^2[pi/(L+2)]`

and write

`Lbar=m+lambda`, `m=floor(Lbar)`, `0<=lambda<1`.

The exact sharp one-copy mean-energy envelope is

`R_M(1) <= (1-lambda)g_m+lambda g_(m+1)`.

Adjacent-shell sine-chain mixtures attain equality, giving the same sharp near-unit-retention coefficient `pi` under a mean total-energy constraint.

### WP06 — arbitrary coherent baselines / history states

The robust upper-tail theorem does **not** require the baseline to commute with the relevant Hamiltonian.

For arbitrary baseline `rho`, positive `R_lin`, tangent range projector `P_U`, and arbitrary finite-copy collective POVMs,

`(R_lin^2/4)[Tr F_N/N] <= Tr(P_U rho)`.

Therefore the relational dual-survival law remains valid for globally stationary clock--signal states that already contain Page--Wootters/history-state relational coherence.

### WP07 — nonlinear `R_lin=0` synthesis is also resource-constrained

For a two-sided `C^2` physical curve at a rank-deficient baseline,

`rho(theta)=rho0+theta D+(theta^2/2)C+o(theta^2)`,

let `P=supp(rho0)`, `Q=I-P`, `R=P rho0 P`, and `K=QDP`.

Established PSD-cone geometry gives

`Q C Q >= 2 K R^(-1)K^dagger`.

The project-level result comes from applying this to the same two-quadrature complex temporal tangent convention used in WP02/WP03/WP06. If

`A=P_U A P`

enters a previously empty upper endpoint sector, define

`J(A|rho0)=Tr(A rho0^+ A^dagger)`.

Then for **every finite `N` and every entangled collective POVM**,

`Tr F_N/N <= J(A|rho0) <= Delta T_U(0)`,

where

`T_U(x,y)=Tr[P_U rho(x,y)]`.

Equivalently,

`(1/4)[Tr F_N/N] <= (1/4)Delta T_U(0)`.

This is a sharp zero-radius analogue of the WP02 robust law: the resource moves from **zeroth-order pre-existing endpoint population** to **second-order endpoint population synthesis**.

The minimal zero-radius qubit exactly saturates both inequalities with a fixed four-outcome equatorial POVM.

The earlier coherent-sideband counterexample also saturates the operational coefficient. For

`alpha_sb(x,y)=(A/2)(x+i y)`,

`n_sb=Nbar(x^2+y^2)/4`, so

`Delta n_sb(0)=Nbar`,

and heterodyne readout gives

`Tr F=Nbar`.

Thus the counterexample that killed baseline-energy-only bounds identifies exactly the quadratic spectral resource that must be charged.

A complementary finite-amplitude two-endpoint phase experiment obeys, for a `pi` relative-phase pair,

`D_tr^2/4 <= min{T_C(nu),T_S(nu)}`,

which yields

`Ebar_C^+ + Ebar_S^+ >= (hbar nu/2)D_tr^2`.

The PSD-cone curvature, rank-changing QFI/Bures, block-coherence, and Helstrom ingredients are prior art. Candidate novelty is only the frequency-resolved autonomous temporal-resource consequence and its sharp arbitrary-POVM coefficient.

## Current frontier — unified mixed endpoint law

The highest-value next target is a general exact-gap tangent containing both:

- support-to-support components, charged by WP06 pre-existing spectral survival and `R_lin`;
- support-to-kernel or kernel-to-support components, charged by WP07 second-order endpoint synthesis.

The objective is a sharp arbitrary-POVM theorem that combines these contributions without double counting or losing the WP06/WP07 constants. A counterexample proving that no additive scalar unification exists would also be a valuable result.

## Validation

Independent numerical/adversarial validators:

- `numerics/verify_robust_tangent_radius_law.py`
- `numerics/verify_relational_autonomous_laws.py`
- `numerics/verify_nonlinear_zero_radius_law.py`

The WP07 validator includes random rank-deficient curvature tests, explicit sharp qubit saturation, randomized one-copy POVMs, randomized two-copy collective POVMs, random PSD block-coherence tests, finite-phase Helstrom checks, and the coherent-sideband coefficients.

## Priority discipline

The mathematical ingredients overlap strongly with phase estimation, modes of asymmetry, quantitative WAY/reference-frame theory, Page--Wootters relational time, numerical-radius theory, PSD-cone second-order geometry, singular QFI/Bures geometry, block coherence, and quantum waveform estimation. Targeted searches have not identified an exact predecessor for the combined WP07 finite-copy two-quadrature spectral-synthesis statement, but **priority remains unverified, not certified**.

Read `AGENTS.md`, `ROADMAP.md`, and WP01--WP07 before continuing. Record every material theorem, counterexample, prior-art collision, or killed conjecture immediately; do not rely on chat history.
