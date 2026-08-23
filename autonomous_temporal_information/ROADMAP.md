# Roadmap — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

## Goal

Seek a foundational physical resource principle for temporal information when clock, signal, controller, detector, and memory are all internal quantum systems. The finished Rev11 random-time law remains frozen on its parent branch.

## Completed foundations

### WP01 — prior-art/model boundary — PASS

Do not claim novelty for modes of asymmetry, QFI as asymmetry, finite clocks/control, Page--Wootters time, quantitative WAY, standard phase estimation, PSD-cone curvature, singular QFI/Bures geometry, Fisher-symmetric measurements, Gaussian displacement/Holevo theory, or generic waveform-estimation bounds.

### WP02 — robust tangent-radius law — PASS

For exact gap `nu`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N^(nu)/N] <= min(D_nu,U_nu) <= T(nu)`.

Thus

`Ebar+ >= (hbar nu R_lin^2/4)[Tr F_N^(nu)/N]`.

Fixed baseline energy alone fails under unrestricted state synthesis; tangent robustness repairs the law.

### WP03 — relational dual-energy survival — PASS

For a globally stationary exchange tangent,

`K_N=(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`,

so

`Ebar_C^+ + Ebar_S^+ >= 2 hbar nu K_N`.

The factor `2` is asymptotically sharp.

### WP04 — exact hard total-energy cap — PASS

For `N_C+N_S<=L`,

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

At the fundamental mode,

`E_max >= hbar nu[pi/arccos(sqrt R)-2]`,

with sharp near-unit asymptotic

`E_max >= pi hbar nu/sqrt(1-R)[1+o(1)]`.

### WP05 — exact mean-total-energy law — PASS

For `g_L=cos^2[pi/(L+2)]`, `Lbar=m+lambda`,

`R_M(1) <= (1-lambda)g_m+lambda g_(m+1)`.

Adjacent-shell sine-chain mixtures attain equality; the sharp mean-energy asymptotic coefficient is also `pi`.

### WP06 — coherent-baseline/history-state extension — PASS

For arbitrary `rho`, positive `R_lin`, tangent range projector `P_U`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N/N] <= Tr(P_U rho)`.

Pre-existing relational/history-state coherence does not evade the finite-radius tail law.

### WP07 — nonlinear zero-radius synthesis — PASS

For baseline-empty endpoint `P_U`, `P=supp(rho0)`, and

`A=P_U A P`,

let

`J=Tr(A rho0^+ A^dagger)`.

For every finite `N` and arbitrary entangled collective POVM,

`boxed: Tr F_N/N <= J <= Delta T_U(0)`.

The minimal qubit and coherent-sideband construction saturate the coefficient.

### WP08 — quadratic synthesis sum/energy law — PASS

For mutually orthogonal baseline-empty endpoint modes and one fixed arbitrary collective POVM,

`Tr F_(N,k)/N <= Delta_k T_k(0)`.

Hence for arbitrary `w_k>=0`,

`boxed: sum_k w_k Tr F_(N,k)/N <= sum_k w_k Delta_k T_k(0)`.

With

`E_gap,syn^(2)=(hbar/4)sum_k nu_k Delta_k T_k(0)`,

`boxed: sum_k hbar nu_k Tr F_(N,k)/(4N) <= E_gap,syn^(2)`.

Multimode coherent sidebands with one common heterodyne measurement saturate every mode and positive weighted sum simultaneously.

### WP09 — bilateral zero-radius Minkowski law — PASS

For arbitrary rank-deficient baseline, let

`P=supp(rho0)`, `Q=I-P`,

and write a physical complex tangent (`Q A Q=0`) as

`A=X+Y^dagger`,

`X=A P`,

`Y=Q A^dagger P`.

Define

`J_X=Tr(X rho0^+ X^dagger)`,

`J_Y=Tr(Y rho0^+ Y^dagger)`.

For every finite `N` and arbitrary entangled collective POVM,

`boxed: sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

Thus

`boxed: Tr F_N/N <= (sqrt(J_X)+sqrt(J_Y))^2`.

For orthogonal baseline-empty upper/lower endpoint sectors,

`J_X<=Delta T_+`, `J_Y<=Delta T_-`,

so

`boxed: Tr F_N/N <= [sqrt(Delta T_+)+sqrt(Delta T_-)]^2`.

The exact-gap qutrit

`H=hbar nu diag(0,1,2)`,

`rho0=|1><1|`,

`A=c(|2><1|+|1><0|)`

with a three-outcome Fourier measurement attains

`Tr F_1=4c^2`.

But

`Delta T_+ + Delta T_-=2c^2`.

Therefore naive additive endpoint synthesis is false by **exactly factor two**, while the square-root law is sharp.

For equal positive gap costs,

`E_bi,syn^(2)=(hbar nu/4)(Delta T_+ + Delta T_-)`

obeys the sharp law

`boxed: E_bi,syn^(2) >= (hbar nu/8)[Tr F_N/N]`.

For unequal costs `epsilon_+,epsilon_-`, the effective coefficient is

`epsilon_parallel=(1/epsilon_+ + 1/epsilon_-)^(-1)`.

This closes the principal WP08 score-interference question in the bilateral zero-radius sector.

## Current frontier — WP10: fully mixed finite-radius + synthesis geometry

### A. Problem statement

A general exact-gap tangent at an arbitrary coherent baseline can simultaneously contain:

1. support-to-support finite-radius information;
2. support-to-kernel endpoint synthesis;
3. kernel-to-support endpoint synthesis.

When `P=supp(rho)` does not commute with `H`, the support-projected pieces `PAP`, `QAP`, `PAQ` need not individually remain exact Bohr-gap operators. Therefore one cannot simply add an independent WP06 energy-tail term to independent WP07/WP09 synthesis terms.

### B. Measurement side is already solved abstractly

WP09 gives

`sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`

with

`X=A P`, `Y=Q A^dagger P`.

The remaining problem is **resource reduction**: express `J_X,J_Y` through physical spectral quantities while preserving the exact constants in all solved limits.

### C. Test scalar sufficiency

First determine whether the sharp ceiling can be inferred from only scalar data such as:

- baseline upper/lower spectral tails;
- an internal tangent radius;
- upper/lower synthesis curvatures.

Construct low-dimensional families with the same such scalar data but different attainable `J_X,J_Y` or Fisher information. If possible, record a no-go theorem: scalar resource accounting is insufficient in the noncommuting-support regime.

### D. Candidate operator geometry

If scalar sufficiency fails, test:

- principal angles between baseline support and energy endpoint subspaces;
- compressed endpoint operators `P P_U P`, `P P_D P`;
- Anderson--Trapp/shorted operators or Schur complements;
- generalized eigenvalues of endpoint overlaps weighted by `rho`;
- matrix/Gram resource objects whose quadratic form gives the resource for each tangent orientation.

The theorem must reduce exactly to:

- WP06 when the full tangent is support preserving and `R_lin>0`;
- WP07 for one-sided support creation;
- WP09 for bilateral support creation.

### E. Sharpness / falsification protocol

For every proposed mixed law:

1. test random coherent supports not commuting with the energy basis;
2. optimize or randomly sample POVMs numerically in dimensions 3--5;
3. test pure-state and mixed-support boundary cases;
4. test tensor-copy scaling for `N=2`;
5. search for phase/Fourier measurements that align score amplitudes and expose hidden cross terms;
6. attempt an analytic extremizer before promoting the result.

### F. Priority audit

Search against:

- shorted operators and PSD block matrix completion;
- principal-angle/operator-range inequalities;
- singular quantum statistical models;
- local quantum estimation with changing support;
- Fisher-symmetric/informationally complete measurements;
- resource theories of coherence/asymmetry with noncommuting support projections.

Do not claim novelty for the mathematical machinery.

## Secondary open directions

- full finite-amplitude phase orbit with support change;
- Gaussian covariance/squeezing synthesis beyond displacement;
- autonomous dynamical interaction/action resource supplying synthesis curvature;
- collective-N mean-energy retention beyond WP05;
- many-body/cut-set resource laws;
- continuum synthesis limits beyond controlled discrete modes.

## Publication / significance gate

Do not draft the foundational manuscript yet. First require:

- a sharp WP10 mixed theorem **or** a sharp scalar-insufficiency/no-go result;
- deep priority audit through the WP09/WP10 collision neighborhood;
- hostile mathematical review;
- sharp constructions;
- a clear autonomous physical consequence.

## Documentation discipline

Every material theorem, failed conjecture, prior-art collision, or validation result must be recorded immediately in the branch and reflected in `README.md`, `AGENTS.md`, and this file. The repository, not chat history, is authoritative.
