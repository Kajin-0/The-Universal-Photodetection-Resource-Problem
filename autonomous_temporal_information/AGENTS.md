# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

**Started:** 2026-08-22

This is a distinct post-Rev11 foundational program. The frozen Rev11 paper remains on `agent/temporal-information-resource-law` and must not be rewritten from this branch absent a concrete defect.

## Grand question

> When signal, clock/reference, controller, detector, and memory are all finite physical systems and no ideal externally timed operation is free, what resource constrains creation, transmission, and recovery of temporal information at frequency `nu`?

Research is analytical/theoretical, falsification-first, and documentation-first. Existing asymmetry, reference-frame, phase-estimation, WAY, Page--Wootters, PSD-cone geometry, singular QFI/Bures geometry, Fisher-symmetric measurement theory, Gaussian displacement/Holevo theory, and finite-clock results are infrastructure unless a genuinely new operational theorem is isolated.

## Current frontier

**WP09 — sharp bilateral-synthesis Minkowski law: analytic PASS and independently validated.**

The next target is the **fully mixed finite-radius + boundary-synthesis exact-gap problem** with noncommuting baseline support and Hamiltonian endpoint projectors.

Current resource hierarchy:

1. finite-radius pre-existing information:
   `Fisher x tangent robustness <= zeroth-order spectral survival`;
2. one-sided boundary synthesis:
   `Fisher <= second-order endpoint synthesis`;
3. bilateral boundary synthesis:
   `sqrt(Fisher) <= sqrt(upper synthesis)+sqrt(lower synthesis)`;
4. structured autonomous relative-time retention:
   exact sharp hard- and mean-energy cosine laws.

The bilateral square-root law is not a proof artifact: an exact-gap qutrit Fourier experiment saturates it and violates naive additive endpoint accounting by exactly factor two.

## Completed work packages

### WP01 — prior-art boundary

Do not claim novelty for modes of asymmetry, QFI/Fisher geometry as asymmetry, finite clocks/reference frames, Page--Wootters relational time, quantitative WAY, standard phase estimation, PSD-cone second-order geometry, singular/rank-changing QFI/Bures corrections, Fisher-symmetric measurements, Gaussian displacement/heterodyne/Holevo theory, or generic waveform-estimation bounds.

### WP02 — robust tangent-radius law

Fixed baseline energy alone does not bound arbitrary local high-frequency Fisher information. With physical linear tangent radius `R_lin`, exact gap `nu`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N^(nu)/N] <= min(D_nu,U_nu) <= T(nu)`.

Hence

`Ebar+ >= (hbar nu R_lin^2/4)[Tr F_N^(nu)/N]`.

The high-frequency counterexample asymptotically saturates.

### WP03 — autonomous relational dual survival

For

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`,

let

`K_N=(R_lin^2/4)[Tr F_N/N]`.

Then

`K_N(nu) <= min{T_C(nu),T_S(nu)}`

for arbitrary finite-copy collective measurements, so

`Ebar_C^+ + Ebar_S^+ >= 2 hbar nu K_N`.

The factor `2` is asymptotically sharp.

### WP04 — exact hard total-energy cap

For structured globally stationary relative-time experiments with `N_C+N_S<=L`,

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

At the fundamental mode,

`E_max >= hbar nu[pi/arccos(sqrt R)-2]`,

with sharp near-unit asymptotic

`E_max >= pi hbar nu/sqrt(1-R)[1+o(1)]`.

### WP05 — exact mean-total-energy law

For `g_L=cos^2[pi/(L+2)]` and `Lbar=m+lambda`,

`R_M(1) <= (1-lambda)g_m+lambda g_(m+1)`.

Adjacent-shell sine-chain mixtures attain equality; the sharp mean-energy asymptotic coefficient is also `pi`.

### WP06 — coherent-baseline/history-state extension

Baseline stationarity is unnecessary. For arbitrary `rho`, positive `R_lin`, tangent range projector `P_U`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N/N] <= Tr(P_U rho)`.

Thus pre-existing Page--Wootters/history-state coherence does not evade the finite-radius tail law.

### WP07 — nonlinear zero-radius spectral synthesis

For `P=supp(rho0)` and baseline-empty endpoint `P_U`, let

`A=P_U A P`,

`J(A|rho0)=Tr(A rho0^+ A^dagger)`.

Then for every finite `N` and arbitrary entangled collective POVM,

`boxed: Tr F_N/N <= J(A|rho0) <= Delta T_U(0)`.

The resource is second-order endpoint population synthesis. The minimal pure qubit and the inherited coherent-sideband family both saturate the operational coefficient.

A finite-amplitude `pi` phase-pair law also gives

`D_tr^2/4 <= min{T_C(nu),T_S(nu)}`.

### WP08 — spectral synthesis sum/energy law

For mutually orthogonal baseline-empty modes and one common arbitrary collective POVM,

`Tr F_(N,k)/N <= Delta_k T_k(0)`.

Thus for any `w_k>=0`,

`boxed: sum_k w_k Tr F_(N,k)/N <= sum_k w_k Delta_k T_k(0)`.

With gap weights,

`E_gap,syn^(2)=(hbar/4)sum_k nu_k Delta_k T_k(0)`

and

`boxed: sum_k hbar nu_k Tr F_(N,k)/(4N) <= E_gap,syn^(2)`.

Multimode coherent sidebands with one common heterodyne measurement saturate every mode and every positive weighted sum simultaneously.

### WP09 — bilateral zero-radius synthesis / Minkowski geometry

For arbitrary rank-deficient baseline

`P=supp(rho0)`, `Q=I-P`,

a physical complex tangent has `Q A Q=0` and can be written

`A=X+Y^dagger`,

`X=A P`,

`Y=Q A^dagger P`.

Define

`J_X=Tr(X rho0^+ X^dagger)`,

`J_Y=Tr(Y rho0^+ Y^dagger)`.

For every finite `N` and arbitrary entangled collective POVM,

`boxed: sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

Therefore

`boxed: Tr F_N/N <= (sqrt(J_X)+sqrt(J_Y))^2`.

For two mutually orthogonal baseline-empty endpoint sectors,

`J_X<=Delta T_+`,

`J_Y<=Delta T_-`,

so

`boxed: Tr F_N/N <= [sqrt(Delta T_+)+sqrt(Delta T_-)]^2`.

Sharp extremizer:

`H=hbar nu diag(0,1,2)`,

`rho0=|1><1|`,

`A=c(|2><1|+|1><0|)`.

A three-outcome Fourier measurement gives

`Tr F_1=4c^2`,

while

`Delta T_+ + Delta T_-=2c^2`.

Hence naive additive synthesis accounting fails by **exactly factor two**, while the Minkowski ceiling is exactly saturated.

Equal positive gap costs give the sharp synthesis-action law

`E_bi,syn^(2)=(hbar nu/4)(Delta T_+ + Delta T_-)`

and

`boxed: E_bi,syn^(2) >= (hbar nu/8)[Tr F_N/N]`.

For unequal positive endpoint costs `epsilon_+,epsilon_-`, the effective coefficient is

`epsilon_parallel=(1/epsilon_+ + 1/epsilon_-)^(-1)`.

Read:
`notes/WP09_SHARP_BILATERAL_SYNTHESIS_MINKOWSKI_LAW.md`.

## Numerical gates

- `numerics/verify_robust_tangent_radius_law.py`
- `numerics/verify_relational_autonomous_laws.py`
- `numerics/verify_nonlinear_zero_radius_law.py`
- `numerics/verify_quadratic_synthesis_sum_rule.py`
- `numerics/verify_bilateral_synthesis_minkowski_law.py`

WP09 validation covers random rank-deficient one-copy POVMs, random two-copy collective POVMs, exact `N J_X`/`N J_Y` scaling, qutrit Fourier saturation, factor-two failure of the additive law, the sharp `hbar nu/8` coefficient, and unequal-cost harmonic weighting.

## Current open frontier — fully mixed exact-gap geometry

### 1. Highest priority: finite-radius + synthesis in one tangent

A general exact-gap tangent may simultaneously contain:

- support-to-support finite-radius information;
- support-to-kernel synthesis;
- kernel-to-support synthesis.

When `[P,H] != 0`, support projection does not preserve exact-gap structure. Do **not** treat `PAP`, `QAP`, and `PAQ` as independent Bohr modes without proof.

### 2. Candidate geometry

The measurement-side WP09 inequality already holds generally through `J_X,J_Y`. The unresolved step is to reduce these weighted tangent norms to sharp physical spectral resources.

Test:

- principal angles between `supp(rho)` and energy endpoint subspaces;
- shorted operators / Schur complements of energy projectors onto baseline support;
- operator-valued or Gram resources rather than scalar sums;
- impossibility of determining the sharp Fisher ceiling from only scalar tail, tangent-radius, and curvature data.

A rigorous scalar-insufficiency counterexample would be a valid major result.

### 3. Required reductions

Any proposed unified theorem must recover exactly:

- WP06 in the pure finite-radius limit;
- WP07 in one-sided zero-radius synthesis;
- WP09 in bilateral zero-radius synthesis.

### 4. Secondary directions

- full finite-amplitude phase orbit with support change;
- Gaussian covariance/squeezing synthesis beyond coherent displacement;
- dynamical interaction/action resource that supplies synthesis curvature;
- collective-N mean-energy retention beyond WP05;
- many-body/cut-set extension.

## Priority status

Targeted searches have not identified exact predecessors for WP02, WP03/WP06, or the specific WP07--WP09 finite-copy frequency-resolved synthesis laws. This is **not certification**. Priority remains unverified.

## Read first

1. `notes/WP09_SHARP_BILATERAL_SYNTHESIS_MINKOWSKI_LAW.md`
2. `notes/WP08_QUADRATIC_SPECTRAL_SYNTHESIS_SUM_AND_ENERGY_LAW.md`
3. `notes/WP07_NONLINEAR_ZERO_RADIUS_CURVATURE_AND_FINITE_AMPLITUDE_LAW.md`
4. `notes/WP06_NONSTATIONARY_ROBUST_TAIL_AND_HISTORY_STATE_EXTENSION.md`
5. `notes/WP05_EXACT_MEAN_ENERGY_AUTONOMOUS_RELATIONAL_RETENTION.md`
6. `notes/WP04_EXACT_HARD_CAP_AUTONOMOUS_RELATIONAL_RETENTION.md`
7. `notes/WP03_RELATIONAL_DUAL_ENERGY_SURVIVAL_LAW.md`
8. `notes/WP02_LOCAL_FISHER_NO_GO_AND_ROBUST_TANGENT_RADIUS_LAW.md`
9. `notes/WP01_FOUNDATIONAL_SCOPE_AND_PRIOR_ART_BOUNDARY.md`
10. `ROADMAP.md`
11. inherited coherent-sideband no-go: `../grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`

## Documentation rule

Every material theorem, counterexample, priority collision, or killed conjecture must be recorded immediately in this directory and reflected in `README.md`, `AGENTS.md`, and `ROADMAP.md`. Do not depend on chat history. Keep Rev11 frozen and separately advertised until this branch reaches its own publication gate.
