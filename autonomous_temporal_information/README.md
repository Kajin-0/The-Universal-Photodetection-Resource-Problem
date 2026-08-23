# Autonomous Temporal Information Law

This directory contains the new post-Rev11 foundational research program.

**Branch:** `agent/autonomous-temporal-information-law`

The frozen Rev11 paper remains untouched on `agent/temporal-information-resource-law`.

## Grand challenge

Determine whether there exists a general physical resource law governing temporal information when **all timing and control resources are internal physical systems**, rather than ideal classical clocks or free time-dependent Hamiltonians.

The emerging hierarchy is

`local Fisher information`

`x physical robustness or synthesis curvature`

`-> spectral resource`

and, for autonomous relational clock--signal information,

`matching exchange resource on clock and signal`

`-> finite-resource temporal-information retention`.

## Current theorem stack

### WP01 — prior-art and model boundary

Qualitative mode support, QFI-as-asymmetry, finite quantum clocks, WAY tradeoffs, Page--Wootters relational time, and standard phase-estimation sine states are prior art. The target must be a quantitative operational temporal-information law.

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

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`

for any fixed one-copy POVM.

At the fundamental frequency,

`E_max >= hbar nu[pi/arccos(sqrt R)-2]`,

and near perfect retention

`E_max >= pi hbar nu/sqrt(1-R)[1+o(1)]`.

Sine-chain history states attain equality.

### WP05 — exact mean-total-energy autonomous retention

Let

`g_L=cos^2[pi/(L+2)]`

and write the mean total excitation as

`Lbar=m+lambda`, `m=floor(Lbar)`, `0<=lambda<1`.

Because `{g_L}` is discretely concave, the exact sharp envelope is

`R_M(1) <= G(Lbar)=(1-lambda)g_m+lambda g_(m+1)`.

Equality is achieved by mixing the two adjacent-shell sine-chain extremizers and resolving the shell before canonical relative-phase readout.

Thus the sharp mean-energy asymptotic is also

`Ebar_C^+ + Ebar_S^+ >= pi hbar nu/sqrt(1-R)[1+o(1)]`.

### WP06 — arbitrary coherent baselines / history states

The robust upper-tail theorem does **not** require the baseline to commute with the relevant Hamiltonian.

For arbitrary baseline `rho`, positive `R_lin`, tangent `A` with upper-endpoint range projector `P_U`, and arbitrary finite-copy collective POVMs,

`(R_lin^2/4)[Tr F_N/N] <= Tr(P_U rho)`.

Therefore the relational dual-survival law remains valid for globally stationary clock--signal states that already contain Page--Wootters/history-state relational coherence:

`[rho_CS,H_C+H_S]=0`

while generally

`[rho_CS,H_C] != 0`, `[rho_CS,H_S] != 0`.

Pre-existing clock coherence does not evade the robust law.

### WP07 — nonlinear `R_lin=0` curvature and finite-amplitude law

The zero-radius sector is no longer completely open.

For a two-sided `C^2` physical curve

`rho(theta)=rho0+theta D+(theta^2/2)C+o(theta^2)`

at a rank-deficient baseline, let `P=supp(rho0)`, `Q=I-P`, `R=P rho0 P`, and `K=QDP`.

Positivity forces the second-order PSD-cone condition

`Q C Q >= 2 K R^(-1) K^dagger`.

When the first-order tangent enters a previously empty upper resource sector `P_U<=Q`, the SLD QFI and every classical FI satisfy

`F_Q(0) <= 2 T_U''(0)`,

and, for arbitrary finite-copy collective readout,

`(1/4)[F_N(0)/N] <= J_U^(2)`,

`J_U^(2)=T_U''(0)/2`.

Thus zero-radius synthesis is paid for by **quadratic spectral population creation** rather than by baseline population.

The earlier coherent upper-sideband counterexample exactly saturates the coefficient:

`F_Q=Nbar=2 n_sb''(0)`.

A complementary finite-amplitude two-endpoint phase experiment obeys

`D_tr^2/4 <= min{T_C(nu),T_S(nu)}`

for a pi relative-phase pair, yielding

`Ebar_C^+ + Ebar_S^+ >= (hbar nu/2)D_tr^2`.

The PSD-cone curvature, block-coherence, and Helstrom ingredients are prior art. Candidate novelty is their frequency-resolved autonomous temporal-resource interpretation.

## Current frontier — unified interior/boundary resource law

The highest-value next target is to combine the two regimes without double counting:

- support-to-support exact-gap information: controlled by WP06 pre-existing spectral survival and `R_lin`;
- support-to-kernel exact-gap information: controlled by WP07 quadratic spectral injection.

A successful unified theorem should then be tested on full phase orbits and coherent bosonic sideband synthesis, not only local boundary curves or binary phase pairs.

## Validation

Independent numerical/adversarial validators:

- `numerics/verify_robust_tangent_radius_law.py`
- `numerics/verify_relational_autonomous_laws.py`
- `numerics/verify_nonlinear_zero_radius_law.py`

They cover the fixed-energy no-go, robust-tail inequality, finite-copy collective POVMs, dual-tail relations, weak-commutativity sharpness, finite-shift numerical radii, sine extremizers, higher-harmonic cosine laws, zero-radius curvature saturation, random PSD block-coherence inequalities, and finite-phase Helstrom bounds.

## Priority discipline

The mathematical ingredients overlap strongly with phase estimation, modes of asymmetry, quantitative WAY/reference-frame theory, Page--Wootters relational time, numerical-radius theory, PSD-cone second-order geometry, boundary QFI/Bures geometry, block coherence, and quantum statistical geometry. Targeted searches have not identified exact predecessors for the combined operational temporal-resource laws above, but **priority remains unverified, not certified**.

Read `AGENTS.md`, `ROADMAP.md`, and the WP01--WP07 notes before continuing. Record every material theorem, counterexample, prior-art collision, or killed conjecture immediately; do not rely on chat history.
