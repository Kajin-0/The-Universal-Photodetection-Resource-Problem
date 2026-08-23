# Roadmap — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

## Goal

Seek a foundational physical resource principle for temporal information when clock, signal, controller, detector, and memory are all internal quantum systems. The finished Rev11 random-time law remains frozen on its parent branch.

## Completed foundations

### WP01 — prior-art and model boundary — PASS

Do not claim novelty for:

- modes-of-asymmetry / reference-frame support laws;
- mode trace-norm monotones;
- QFI as an asymmetry resource;
- finite autonomous clocks/control per se;
- Page--Wootters relational time per se;
- quantitative WAY tradeoffs;
- generic quantum speed limits;
- standard phase-estimation sine states / Heisenberg scaling;
- simply charging preparation/control energy.

The program must produce an operational temporal-information resource law.

### WP02 — local-Fisher no-go and robust tangent radius — PASS

At fixed baseline mean energy, arbitrary local state synthesis can retain fixed local Fisher information at arbitrarily high Bohr frequency by shrinking the physical tangent neighborhood.

Define `R_lin` as the largest disk over which the linearized two-quadrature tangent remains positive.

For stationary `rho0` and exact gap `nu`, arbitrary finite-copy collective measurements obey

`(R_lin^2/4)[Tr F_N^(nu)/N] <= min(D_nu,U_nu) <= T(nu)`.

Therefore

`Ebar+ >= (hbar nu R_lin^2/4)[Tr F_N^(nu)/N]`.

The counterexample asymptotically saturates this robust law.

### WP03 — relational dual-energy survival — PASS

For clock `C` and signal `S`, take a globally stationary energy-exchange tangent

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`.

With

`K_N=(R_lin^2/4)[Tr F_N/N]`,

for any finite `N` and arbitrary joint POVM,

`K_N(nu) <= min{T_C(nu),T_S(nu)}`.

Thus

`Ebar_C^+ + Ebar_S^+ >= 2 hbar nu K_N`.

The factor `2` is asymptotically sharp: a symmetric two-qubit exchange model satisfies weak multiparameter commutativity, so collective measurements asymptotically attain both local tail bounds simultaneously.

All-mode lattice budget:

`sum_k K_N(k) <= min(nbar_C,nbar_S)`.

### WP04 — exact hard total-energy cap law — PASS

For a structured relative-time experiment inside a fixed/hard-capped total-excitation shell `N_C+N_S<=L`, the exchange shift is finite.

For one fixed one-copy POVM,

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

With `nu=k omega0` and `E_max=hbar omega0 L`,

`R_M(nu) <= cos^2{pi/[floor(E_max/(hbar nu))+2]}`.

For the fundamental mode,

`E_max >= hbar nu[pi/arccos(sqrt R)-2]`.

Near unit retention,

`E_max >= pi hbar nu/sqrt(1-R)[1+o(1)]`.

This bound is exactly sharp. A globally stationary fixed-total-energy sine-chain history state and canonical relative-phase POVM attain equality.

### WP05 — exact mean-total-energy law — PASS

For the structured one-copy relative-time experiment, let

`g_L=cos^2[pi/(L+2)]`.

If the baseline total-energy shell distribution is `W_L`, arbitrary measurement-dependent posterior reshuffling obeys

`R_M(1) <= sum_L W_L g_L`.

The sequence `{g_L}` is discretely concave. For

`Lbar=m+lambda`, `m=floor(Lbar)`, `0<=lambda<1`,

the exact sharp envelope is

`R_M(1) <= G(Lbar)=(1-lambda)g_m+lambda g_(m+1)`.

Equality is achieved by an adjacent-shell mixture of sine-chain extremizers, followed by total-energy-shell resolution and canonical relative-phase readout.

Therefore, under a **mean** total-energy constraint,

`Ebar_C^+ + Ebar_S^+ >= pi hbar nu/sqrt(1-R)[1+o(1)]`

with sharp leading constant `pi` in the solved one-copy structured setting.

### WP06 — nonstationary robust tail / pre-existing history state — PASS

The robust tail theorem does not require baseline stationarity.

For arbitrary density operator `rho`, positive linear tangent radius `R_lin`, and complex tangent `A`, positivity implies on `supp(rho)`

`R_lin=1/w(rho^(-1/2) A rho^(-1/2))`.

For any one-copy POVM,

`Tr F_1 <= Tr(A rho^+ A^dagger)`.

If the range of `A` lies in a projector `P_U`, then

`(R_lin^2/4)Tr F_1 <= Tr(P_U rho)`.

For `N` independently encoded copies and arbitrary collective readout,

`(R_lin^2/4)[Tr F_N/N] <= Tr(P_U rho)`.

For an exact positive energy gap, this is the same upper-tail energy-survival theorem as WP02 without any commutation assumption on `rho`.

Consequently the relational law survives a globally stationary but locally coherent history state:

`[rho_CS,H_C+H_S]=0`,

while generally

`[rho_CS,H_C] != 0`, `[rho_CS,H_S] != 0`.

Pre-existing relational clock coherence therefore does not evade

`K_N(nu) <= min{T_C(nu),T_S(nu)}`.

## Current frontier — WP07: nonlinear `R_lin=0` synthesis

This is the highest-priority unresolved sector.

### A. Minimal boundary-family theorem

Construct the smallest exact physical family with:

- rank-deficient baseline `rho_0`;
- a nonzero first-order tangent `A_nu` connecting the baseline support to a high-energy subspace;
- `R_lin=0` for the affine tangent;
- second-order population/curvature that restores positivity of the exact nonlinear family.

The two-level pure-state family

`|psi(theta)>=sqrt(1-|z(theta)|^2)|0>+z(theta)|1>`

is the canonical starting point. For `z(theta)=a theta+O(theta^2)`, the coherence is first order while upper-level population is `|a|^2 theta^2+O(theta^3)`.

The work package should isolate the general PSD constraint behind this mechanism rather than relying on one qubit example.

### B. Curvature-population inequality

Seek a general second-order positivity theorem of the schematic form

`P_U rho''(0) P_U >= 2 A rho_0^+ A^dagger`

or its correct Schur-complement / shorted-operator variant for a smooth state curve

`rho(theta)=rho_0+theta D+(theta^2/2)C+o(theta^2)`

when the first-order tangent reaches the kernel of `rho_0`.

Determine the exact coefficient, support conditions, and matrix/operator generalization.

If successful, combine it with energy weighting to show that high-gap first-order Fisher information is paid for by **second-order energy injection** even when `R_lin=0`.

### C. Decide whether a local curvature law is genuinely operational

A curvature bound is useful only if it controls an observable information quantity without arbitrary reparameterization pathologies.

Test:

1. SLD/Bures QFI at boundary states;
2. Hellinger/Bures finite differences;
3. trace distance and Helstrom discrimination at finite amplitude;
4. quantum Chernoff / hypothesis-testing exponents;
5. finite-difference Fisher or chi-square divergence.

A likely robust target is a finite-amplitude theorem rather than another purely differential quantity.

### D. Finite-amplitude spectral-energy law

For a family `rho_theta` and baseline `rho_0`, define a physically meaningful amplitude scale `delta` and seek inequalities of the form

`distinguishability(rho_delta,rho_0)`

`<= function[upper-tail population or energy injected at order delta^2]`.

The theorem must survive coherent-sideband families and arbitrary POVMs.

### E. Autonomous relational extension

After the one-system boundary geometry is understood, lift it to a globally stationary clock--signal pair where first-order coherence exchanges `hbar nu` while second-order populations appear on both sides.

Test whether positivity forces **matched second-order population injection** into the local endpoint sectors and therefore a nonlinear analogue of the WP03/WP06 dual-tail law.

### F. Priority audit for WP07

Search specifically against:

- perturbation theory of positive semidefinite matrices and Schur-complement positivity;
- tangent cones / second-order tangent sets of the PSD cone;
- boundary quantum Fisher information and rank-changing statistical models;
- Bures/Hellinger geometry at rank-deficient states;
- quantum local asymptotic theory with changing support;
- quantum speed limits and finite-amplitude distinguishability;
- asymmetry robustness / coherence cost;
- coherent-state and sideband phase estimation;
- Page--Wootters and autonomous clock models with finite-amplitude interactions.

Do not claim a new theorem until this collision boundary is explicit.

## Secondary open directions

### WP08 — collective-N mean-energy retention

Determine whether entangled collective measurements can beat the one-copy exact envelope `G(Lbar)` per copy and characterize the asymptotic limit.

### WP09 — many-body cut law

Test the conjecture:

> temporal information crossing any autonomous bipartition requires matched energy-exchange resources on both sides of the cut.

Seek a cut-set/network generalization of WP03/WP06.

### WP10 — autonomous control-generator resource

If operations do not obey the energy-conserving/covariant structure, arbitrary interaction strength is a loophole. Determine which dynamical resource must be charged: spectral diameter, interaction norm, action, power, or another invariant.

## Publication / significance gate

Do not draft a new foundational manuscript merely because WP02--WP06 are mathematically interesting. First require:

- deep priority audit;
- a successful resolution or sharply characterized impossibility result for WP07;
- at least one theorem clearly not reducible to known phase estimation/WAY/asymmetry statements;
- hostile mathematical review;
- sharp or near-sharp constructions;
- explicit physical consequence or thought experiment.

## Documentation discipline

Every material theorem, failed conjecture, prior-art collision, or validation result must be recorded immediately in the branch and reflected in `README.md`, `AGENTS.md`, and this file. The repository, not chat history, is authoritative.
