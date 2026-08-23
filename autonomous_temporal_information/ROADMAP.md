# Roadmap — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

## Goal

Seek a foundational physical resource principle for temporal information when clock, signal, controller, detector, and memory are all internal quantum systems. The finished Rev11 random-time law remains frozen on its parent branch.

## Completed foundations

### WP01 — prior-art and model boundary — PASS

Do not claim novelty for modes-of-asymmetry, QFI as asymmetry, finite clocks/control, Page--Wootters relational time, quantitative WAY, generic speed limits, phase-estimation sine states, PSD-cone curvature, singular QFI/Bures geometry, Gaussian displacement/Holevo theory, or generic waveform-estimation bounds.

### WP02 — local-Fisher no-go and robust tangent radius — PASS

For exact gap `nu`, arbitrary finite-copy collective measurements obey

`(R_lin^2/4)[Tr F_N^(nu)/N] <= min(D_nu,U_nu) <= T(nu)`.

Thus

`Ebar+ >= (hbar nu R_lin^2/4)[Tr F_N^(nu)/N]`.

Fixed baseline energy alone fails for unrestricted state synthesis; tangent robustness repairs the law.

### WP03 — relational dual-energy survival — PASS

For a globally stationary exchange tangent,

`K_N=(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`,

so

`Ebar_C^+ + Ebar_S^+ >= 2 hbar nu K_N`.

The factor `2` is asymptotically sharp.

### WP04 — exact hard total-energy cap law — PASS

For `N_C+N_S<=L`,

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

At the fundamental mode,

`E_max >= hbar nu[pi/arccos(sqrt R)-2]`,

with sharp near-unit asymptotic

`E_max >= pi hbar nu/sqrt(1-R)[1+o(1)]`.

### WP05 — exact mean-total-energy law — PASS

For

`g_L=cos^2[pi/(L+2)]`, `Lbar=m+lambda`,

`R_M(1) <= (1-lambda)g_m+lambda g_(m+1)`.

Adjacent-shell sine-chain mixtures attain equality; the sharp mean-energy asymptotic coefficient is also `pi`.

### WP06 — arbitrary coherent baseline / history-state extension — PASS

For arbitrary `rho`, positive `R_lin`, tangent range projector `P_U`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N/N] <= Tr(P_U rho)`.

Pre-existing relational/history-state coherence does not evade the finite-radius tail law.

### WP07 — nonlinear zero-radius spectral-synthesis law — PASS

For a baseline-empty endpoint sector and complex two-quadrature tangent

`A=P_U A P`, `P=supp(rho0)`,

define

`J=Tr(A rho0^+ A^dagger)`.

For every finite `N` and arbitrary entangled collective POVM,

`Tr F_N/N <= J`.

Second-order PSD-cone positivity gives

`J <= Delta T_U(0)`.

Therefore

`boxed: Tr F_N/N <= J <= Delta T_U(0)`.

Equivalently,

`boxed: (1/4)[Tr F_N/N] <= (1/4)Delta T_U(0)`.

The minimal pure qubit saturates both inequalities with a fixed one-copy POVM. The coherent-sideband no-go also saturates the operational coefficient under heterodyne readout.

The one-parameter scalar relation `F_Q<=2T_U''` is close to established singular QFI/Bures geometry and is not the novelty claim.

### WP08 — quadratic spectral-synthesis sum and energy law — PASS

Let `{P_k}` be mutually orthogonal baseline-empty endpoint sectors and

`A_k=P_k A_k P`.

For one fixed arbitrary collective POVM on `N` copies,

`Tr F_(N,k)/N <= Delta_k T_k(0)`

for every mode `k`.

Hence, for arbitrary `w_k>=0`,

`boxed: sum_k w_k [Tr F_(N,k)/N] <= sum_k w_k Delta_k T_k(0)`.

Define

`S_syn^(2)=(1/4)sum_k Delta_k T_k(0)`

and

`E_gap,syn^(2)=(hbar/4)sum_k nu_k Delta_k T_k(0)`.

Then

`sum_k Tr F_(N,k)/(4N) <= S_syn^(2)`

and

`boxed: sum_k hbar nu_k [Tr F_(N,k)/(4N)] <= E_gap,syn^(2)`.

This closes the coherent-waveform baseline-energy loophole in the correct resource variable: **positive second-order spectral synthesis**.

For multimode coherent sidebands

`alpha_k=g_k(x_k+i y_k)`,

`Delta_k n_k=4|g_k|^2`.

Multimode heterodyne gives

`Tr F_k=4|g_k|^2`,

so every mode and every nonnegative weighted sum are simultaneously saturated by one fixed measurement.

With actual photon-energy weights,

`sum_k (hbar omega_k/4)Tr F_k = (1/4)sum_k Delta_k E_k(0)`.

Gaussian displacement/Holevo/heterodyne mathematics is prior art; candidate novelty is the frequency-resolved synthesis-resource sum law.

## Current frontier — mixed-endpoint exact-gap geometry

### A. Do not use a naive support projection

For arbitrary coherent `rho`, `P=supp(rho)` need not commute with `H` or with the energy endpoint projectors. Therefore, even if `A` is an exact positive-gap operator, pieces such as

`PAP`, `QAP`, `PAQ`

need not themselves remain exact-gap operators after support projection.

This invalidates the most naive plan of simply adding an independent WP06 term to an independent WP07 term.

The correct mixed theorem must retain the geometry of **both**:

- the Hamiltonian/resource endpoint subspaces;
- the baseline support/kernel subspaces.

### B. General measurement-side bound

For any tangent with `Q A Q=0`, write

`X=A P`,

`Y=Q A^dagger P`.

Then

`Tr(A M)=Tr(XM)+[Tr(YM)]^*`

for every Hermitian POVM effect `M`.

Each of `X` and `Y` is right-supported on `P`, so weighted Hilbert--Schmidt Cauchy--Schwarz separately controls its score norm by

`J_X=Tr(X rho^+ X^dagger)`,

`J_Y=Tr(Y rho^+ Y^dagger)`.

A universal Minkowski bound therefore exists:

`boxed: sqrt(Tr F_N/N) <= sqrt(J_X)+sqrt(J_Y)`

and hence

`boxed: Tr F_N/N <= (sqrt(J_X)+sqrt(J_Y))^2`.

This is a useful provisional mixed-state information geometry, but `J_X,J_Y` are not yet reduced to sharp physical spectral resources in the general noncommuting-support case.

The next task is to determine whether this Minkowski structure is sharp and whether it can be expressed through resource projectors plus second-order synthesis without hidden geometric constants.

### C. Test scalar additivity versus matrix geometry

Required work:

1. construct low-dimensional examples with noncommuting baseline support and energy projectors;
2. test the false candidate
   `Tr F <= B_pre+B_syn`
   against arbitrary POVMs;
3. test whether the sharp coefficient is instead
   `(sqrt(B_pre)+sqrt(B_syn))^2`;
4. search for a tighter Gram-matrix / shorted-operator law;
5. identify principal-angle factors when an energy endpoint subspace is nearly, but not exactly, contained in the baseline support;
6. preserve exact WP06 and WP07 constants in their pure limits.

A proof that no scalar additive law exists would be a substantive structural result, not a failure.

### D. Endpoint orientation

The upper-kernel and lower-kernel cases must be kept distinct.

- **upper kernel:** high-energy endpoint population is synthesized; WP07 applies directly in the clean orthogonal case;
- **lower kernel:** upper resource can be pre-existing while the donor/lower endpoint is synthesized through the conjugate tangent.

The autonomous clock--signal version should track which side and which endpoint pays a zeroth-order versus second-order cost.

### E. Full finite-amplitude phase orbit

The WP07 binary Helstrom theorem is weaker than continuous relative-time recovery. Seek a support-changing phase-orbit functional that remains arbitrary-POVM operational and recovers the WP04/WP05 near-unit divergence where appropriate.

### F. Gaussian families beyond displacement

WP08 solves coherent displacement synthesis sharply. Next Gaussian targets:

- squeezed-vacuum sideband generation;
- parameter-dependent covariance with fixed first moments;
- mixed thermal Gaussian baselines;
- correlated multimode synthesis.

Determine whether the correct synthesis resource is a covariance Hessian, excess photon-number Hessian, or a Holevo-compatible matrix functional.

### G. Autonomous control/action accounting

The synthesis curvature must ultimately be supplied by an interaction. For unrestricted parameter-dependent dynamics, identify a positive dynamical resource that bounds WP07/WP08 synthesis:

- interaction spectral diameter;
- integrated operator norm/action;
- energy transferred into new sectors;
- power/bandwidth;
- another invariant.

## Secondary open directions

- collective-N mean-energy retention beyond the solved one-copy WP05 envelope;
- many-body/cut-set generalization of the dual resource law;
- continuous-limit rigor for WP08 beyond controlled mode discretizations.

## Priority audit

Continue targeted searches against:

- second-order PSD-cone tangent geometry;
- singular/rank-changing quantum statistical models;
- Bures/QFI continuous completion;
- subspace/block coherence;
- principal-angle and shorted-operator matrix analysis;
- Gaussian displacement and covariance estimation;
- linear quantum waveform estimation;
- finite-reference-frame and autonomous-control resource theories.

Do not claim novelty for any of these ingredients.

## Publication / significance gate

Do not draft a new foundational manuscript yet. First require:

- a sharp mixed-endpoint theorem **or** a sharp impossibility/non-additivity result;
- deep priority audit through WP08 and the mixed geometry;
- at least one theorem not reducible to known phase estimation/WAY/asymmetry/PSD-cone/Gaussian-metrology statements;
- hostile mathematical review;
- sharp constructions;
- explicit physical consequence or thought experiment.

## Documentation discipline

Every material theorem, failed conjecture, prior-art collision, or validation result must be recorded immediately in the branch and reflected in `README.md`, `AGENTS.md`, and this file. The repository, not chat history, is authoritative.
