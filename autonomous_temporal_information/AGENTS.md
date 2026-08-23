# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

**Started:** 2026-08-22

This is a distinct post-Rev11 foundational program. The frozen Rev11 paper remains on `agent/temporal-information-resource-law` and must not be rewritten from this branch absent a concrete defect.

## Grand question

> When signal, clock/reference, controller, detector, and memory are all finite physical systems and no ideal externally timed operation is free, what resource constrains creation, transmission, and recovery of temporal information at frequency `nu`?

Research is analytical/theoretical, falsification-first, and documentation-first. Existing asymmetry, reference-frame, phase-estimation, WAY, Page--Wootters, PSD-cone geometry, singular QFI/Bures geometry, Fisher-symmetric measurement theory, Gaussian displacement/Holevo theory, and finite-clock results are infrastructure unless a genuinely new operational theorem is isolated.

## Current frontier

**WP10 — sharp one-sided mixed survival+synthesis law: analytic PASS and independently validated.**

The next target is the genuinely difficult case `[supp(rho),H] != 0`, where support projection and energy-gap decomposition do not commute.

Current composition hierarchy:

1. finite-radius pre-existing information:
   `Fisher x robustness <= zeroth-order spectral survival`;
2. one-sided zero-radius synthesis:
   `Fisher <= second-order endpoint synthesis`;
3. one-sided pre-existing + synthesis:
   **additive** robust-survival + synthesis law;
4. bilateral synthesis:
   **Minkowski/square-root** endpoint composition;
5. structured autonomous relative-time retention:
   exact sharp hard- and mean-energy cosine laws.

## Completed work packages

### WP01 — prior-art boundary

Do not claim novelty for modes of asymmetry, QFI/Fisher geometry as asymmetry, finite clocks/reference frames, Page--Wootters time, quantitative WAY, standard phase estimation, PSD-cone second-order geometry, singular/rank-changing QFI/Bures corrections, Fisher-symmetric measurements, Gaussian displacement/heterodyne/Holevo theory, or generic waveform-estimation bounds.

### WP02 — robust tangent-radius law

For exact gap `nu`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N^(nu)/N] <= min(D_nu,U_nu) <= T(nu)`.

Hence

`Ebar+ >= (hbar nu R_lin^2/4)[Tr F_N^(nu)/N]`.

### WP03 — autonomous relational dual survival

For an exact exchange tangent,

`K_N=(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`,

so

`Ebar_C^+ + Ebar_S^+ >= 2 hbar nu K_N`.

The factor `2` is asymptotically sharp.

### WP04 / WP05 — exact autonomous retention

For hard total-excitation cap `L`,

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

At the fundamental mode,

`E_max >= hbar nu[pi/arccos(sqrt R)-2]`,

with sharp near-unit coefficient `pi`.

For mean total excitation `Lbar=m+lambda`,

`R_M(1) <= (1-lambda)g_m+lambda g_(m+1)`,

`g_L=cos^2[pi/(L+2)]`,

and adjacent-shell sine mixtures attain equality. The mean-energy asymptotic coefficient is also `pi`.

### WP06 — arbitrary coherent baseline/history state

For arbitrary `rho`, positive `R_lin`, range projector `P_U`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N/N] <= Tr(P_U rho)`.

Pre-existing Page--Wootters/history-state coherence does not evade the robust tail law.

### WP07 — nonlinear zero-radius synthesis

For `P=supp(rho0)`, baseline-empty endpoint `P_U`, and `A=P_U A P`, define

`J=Tr(A rho0^+ A^dagger)`.

Then

`boxed: Tr F_N/N <= J <= Delta T_U(0)`

for every finite `N` and arbitrary entangled collective POVM.

The minimal qubit and coherent-sideband constructions saturate the coefficient.

### WP08 — quadratic synthesis sum/energy law

For mutually orthogonal baseline-empty modes and one common arbitrary collective POVM,

`Tr F_(N,k)/N <= Delta_k T_k(0)`.

Hence for arbitrary nonnegative weights,

`boxed: sum_k w_k Tr F_(N,k)/N <= sum_k w_k Delta_k T_k(0)`.

With gap weights,

`boxed: sum_k hbar nu_k Tr F_(N,k)/(4N) <= E_gap,syn^(2)`.

Multimode coherent sidebands with one common heterodyne measurement saturate every mode and positive weighted sum simultaneously.

### WP09 — bilateral zero-radius Minkowski law

For

`P=supp(rho0)`, `Q=I-P`,

write

`A=X+Y^dagger`,

`X=A P`, `Y=Q A^dagger P`.

With

`J_X=Tr(X rho0^+ X^dagger)`,

`J_Y=Tr(Y rho0^+ Y^dagger)`,

one has

`boxed: sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

For orthogonal baseline-empty upper/lower endpoint sectors,

`boxed: Tr F_N/N <= [sqrt(Delta T_+)+sqrt(Delta T_-)]^2`.

The exact-gap qutrit Fourier extremizer gives `Tr F_1=4c^2` while `Delta T_+ + Delta T_-=2c^2`, proving additive endpoint accounting false by exactly factor two.

Equal positive gap costs obey the sharp law

`E_bi,syn^(2) >= (hbar nu/8)[Tr F_N/N]`.

### WP10 — sharp one-sided mixed survival+synthesis law

Assume

`P=supp(rho0)`, `[P,H]=0`,

`[H,A_nu]=hbar nu A_nu`,

`P A_nu Q=0`.

Decompose

`A_nu=B+K`,

`B=P A_nu P`,

`K=Q A_nu P`.

Define

`J_B=Tr(B rho0^+ B^dagger)`,

`J_K=Tr(K rho0^+ K^dagger)`.

For every finite `N` and arbitrary entangled collective POVM,

`boxed: Tr F_N/N <= J_B+J_K`.

Let `R_B` be the physical linear radius of the support-preserving sub-tangent, `T_pre(nu)` the pre-existing upper endpoint population, and `T_syn(x,y)` the newly synthesized upper endpoint population. Then

`J_B <= 4T_pre/R_B^2`,

`J_K <= Delta T_syn(0)`.

Therefore

`boxed: Tr F_N/N <= 4T_pre(nu)/R_B^2 + Delta T_syn(0)`.

This additive law is exactly sharp. The qutrit family

`rho0=p0|0><0|+p1|1><1|`,

`A_nu=kappa p0|1><0|+kappa p1|2><1|`

has

`J_B=kappa^2 p0`,

`J_K=kappa^2 p1`,

and one three-outcome Fourier measurement attains

`Tr F_1=kappa^2=J_B+J_K`.

A normalized congruence family realizes the exact tangent and gives

`Delta T_syn=kappa^2 p1=J_K`,

while

`4T_pre/R_B^2=kappa^2 p0=J_B`.

The positive energy/action form is

`boxed: Ebar+/R_B^2 + E_syn^(2) >= (hbar nu/4)[Tr F_N/N]`,

`E_syn^(2)=(hbar nu/4)Delta T_syn`,

and the same qutrit family saturates it exactly.

Read:
`notes/WP10_SHARP_ONE_SIDED_MIXED_SURVIVAL_SYNTHESIS_LAW.md`.

## Numerical gates

- `numerics/verify_robust_tangent_radius_law.py`
- `numerics/verify_relational_autonomous_laws.py`
- `numerics/verify_nonlinear_zero_radius_law.py`
- `numerics/verify_quadratic_synthesis_sum_rule.py`
- `numerics/verify_bilateral_synthesis_minkowski_law.py`
- `numerics/verify_one_sided_mixed_survival_synthesis_law.py`

WP10 validation covers random energy-diagonal rank-deficient baselines, arbitrary one-copy POVMs, random two-copy collective POVMs, the internal robust-tail bound, exact normalized congruence-family curvature, qutrit Fourier saturation, and sharp energy/action equality.

## Current open frontier — noncommuting support

### 1. Remove `[P,H]=0`

For the full tangent `A_nu`, exact-gap structure remains valid. But when the baseline support projector `P` does not commute with `H`, the pieces

`P A_nu P`, `Q A_nu P`, `P A_nu Q`

need not individually be exact Bohr modes.

Do not apply WP06/WP07 to those projected pieces as if their energy orientation were unchanged.

### 2. Candidate operator geometry

Investigate:

- principal angles between `P` and participating energy endpoint subspaces;
- compressed endpoint operators `P P_U P` and `P P_D P`;
- shorted operators / Schur complements;
- generalized eigenvalues weighted by `rho`;
- matrix/Gram resources that reduce exactly to WP06, WP07, WP09, and WP10.

### 3. Scalar sufficiency test

Attempt to construct two exact-gap physical models with identical natural scalar data—spectral tails, internal tangent radius, and synthesis curvatures—but different attainable Fisher information or weighted tangent norms.

If successful, record a no-go theorem: a scalar resource law is insufficient in the noncommuting-support regime.

### 4. Secondary directions

- full finite-amplitude phase orbit with support change;
- Gaussian squeezing/covariance synthesis;
- dynamical interaction/action resource supplying synthesis curvature;
- collective-N mean-energy retention;
- many-body/cut-set laws.

## Priority status

Targeted searches have not identified exact predecessors for the specific WP07--WP10 finite-copy frequency-resolved resource composition laws. This is **not certification**. Priority remains unverified.

## Read first

1. `notes/WP10_SHARP_ONE_SIDED_MIXED_SURVIVAL_SYNTHESIS_LAW.md`
2. `notes/WP09_SHARP_BILATERAL_SYNTHESIS_MINKOWSKI_LAW.md`
3. `notes/WP08_QUADRATIC_SPECTRAL_SYNTHESIS_SUM_AND_ENERGY_LAW.md`
4. `notes/WP07_NONLINEAR_ZERO_RADIUS_CURVATURE_AND_FINITE_AMPLITUDE_LAW.md`
5. `notes/WP06_NONSTATIONARY_ROBUST_TAIL_AND_HISTORY_STATE_EXTENSION.md`
6. `notes/WP05_EXACT_MEAN_ENERGY_AUTONOMOUS_RELATIONAL_RETENTION.md`
7. `notes/WP04_EXACT_HARD_CAP_AUTONOMOUS_RELATIONAL_RETENTION.md`
8. `notes/WP03_RELATIONAL_DUAL_ENERGY_SURVIVAL_LAW.md`
9. `notes/WP02_LOCAL_FISHER_NO_GO_AND_ROBUST_TANGENT_RADIUS_LAW.md`
10. `notes/WP01_FOUNDATIONAL_SCOPE_AND_PRIOR_ART_BOUNDARY.md`
11. `ROADMAP.md`

## Documentation rule

Every material theorem, counterexample, priority collision, or killed conjecture must be recorded immediately in this directory and reflected in `README.md`, `AGENTS.md`, and `ROADMAP.md`. Do not depend on chat history. Keep Rev11 frozen and separately advertised until this branch reaches its own publication gate.
