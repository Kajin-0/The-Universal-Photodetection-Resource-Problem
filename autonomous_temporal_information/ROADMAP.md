# Roadmap — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

## Goal

Seek a foundational physical resource principle for temporal information when clock, signal, controller, detector, and memory are all internal quantum systems. The finished Rev11 random-time law remains frozen on its parent branch.

## Completed foundations

### WP01 — prior-art and model boundary — PASS

Do not claim novelty for modes-of-asymmetry, QFI as asymmetry, finite clocks/control, Page--Wootters relational time, quantitative WAY, generic speed limits, phase-estimation sine states, PSD-cone curvature, boundary QFI/Bures geometry, or simply charging preparation/control energy.

The program must produce an operational temporal-information resource law.

### WP02 — local-Fisher no-go and robust tangent radius — PASS

At fixed baseline mean energy, arbitrary local state synthesis can retain fixed local Fisher information at arbitrarily high Bohr frequency by shrinking the physical tangent neighborhood.

For stationary `rho0` and exact gap `nu`, arbitrary finite-copy collective measurements obey

`(R_lin^2/4)[Tr F_N^(nu)/N] <= min(D_nu,U_nu) <= T(nu)`.

Therefore

`Ebar+ >= (hbar nu R_lin^2/4)[Tr F_N^(nu)/N]`.

The counterexample asymptotically saturates this robust law.

### WP03 — relational dual-energy survival — PASS

For a globally stationary energy-exchange tangent

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`,

with

`K_N=(R_lin^2/4)[Tr F_N/N]`,

one has

`K_N(nu) <= min{T_C(nu),T_S(nu)}`

for arbitrary finite-copy collective measurements.

Thus

`Ebar_C^+ + Ebar_S^+ >= 2 hbar nu K_N`.

The factor `2` is asymptotically sharp.

### WP04 — exact hard total-energy cap law — PASS

For the structured relative-time experiment inside `N_C+N_S<=L`,

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

At the fundamental mode,

`E_max >= hbar nu[pi/arccos(sqrt R)-2]`,

so near unit retention

`E_max >= pi hbar nu/sqrt(1-R)[1+o(1)]`.

Sine-chain history states attain equality.

### WP05 — exact mean-total-energy law — PASS

With

`g_L=cos^2[pi/(L+2)]`

and mean total excitation

`Lbar=m+lambda`,

the exact one-copy envelope is

`R_M(1) <= (1-lambda)g_m+lambda g_(m+1)`.

Adjacent-shell sine-chain mixtures attain equality. Hence the sharp mean-energy asymptotic coefficient is also `pi`.

### WP06 — nonstationary robust tail / pre-existing history state — PASS

The robust upper-tail theorem survives arbitrary baseline energy coherence.

For arbitrary `rho`, positive `R_lin`, tangent range projector `P_U`, finite `N`, and arbitrary collective readout,

`(R_lin^2/4)[Tr F_N/N] <= Tr(P_U rho)`.

Thus the relational dual-tail theorem remains valid for globally stationary Page--Wootters/history states that are not separately stationary under the local Hamiltonians.

### WP07 — nonlinear zero-radius curvature and finite-amplitude laws — PASS in the boundary/two-sector regimes

For a two-sided `C^2` physical curve

`rho(theta)=rho0+theta D+(theta^2/2)C+o(theta^2)`

at a rank-deficient baseline, let

`P=supp(rho0)`, `Q=I-P`, `R=P rho0 P`, `K=QDP`.

Second-order PSD-cone geometry gives

`Q C Q >= 2 K R^(-1)K^dagger`.

If the first-order tangent enters a previously empty upper resource sector `P_U<=Q`, then

`F_Q(0) <= 2 T_U''(0)`.

For arbitrary finite-copy collective readout,

`(1/4)[F_N(0)/N] <= J_U^(2)`,

`J_U^(2)=T_U''(0)/2`.

In multiparameter form,

`F_N(0)/N <= 2 Hess[T_U](0)`.

Thus `R_lin=0` does not eliminate resource accounting: it moves the cost from zeroth-order spectral population to **second-order spectral population creation**.

The earlier coherent-sideband counterexample saturates this coefficient exactly:

`F_Q=Nbar=2 n_sb''(0)`.

A complementary finite-amplitude two-sector phase theorem gives, for a pi relative-phase pair,

`D_tr^2/4 <= q_D q_U <= min(q_D,q_U)`.

For an exact autonomous exchange pair,

`D_tr^2/4 <= min{T_C(nu),T_S(nu)}`

and

`Ebar_C^+ + Ebar_S^+ >= (hbar nu/2)D_tr^2`.

The underlying PSD-cone, block-coherence, and Helstrom mathematics is prior art. Candidate novelty is the frequency-resolved autonomous temporal-resource interpretation.

## Current frontier — unified support/interior law

### A. Combine WP06 and WP07 without double counting

For a general exact-gap tangent at an arbitrary baseline, decompose the information-bearing operator into:

1. **support-to-support** components, which use pre-existing endpoint population and should be charged by a WP06-style survival/robustness term;
2. **support-to-kernel** components, which synthesize a new endpoint sector and should be charged by a WP07 quadratic-supply term.

The target is one coordinate-invariant inequality that reduces exactly to WP06 in the interior and WP07 on the boundary.

Questions:

- Does the SLD-QFI orthogonal decomposition of support-support and support-kernel matrix elements give the correct additive resource decomposition?
- Can a classical arbitrary-POVM Fisher bound inherit that decomposition without replacing the result by a loose total-QFI envelope?
- Is there a natural generalized robustness functional that interpolates continuously between `R_lin^2 T` and `T_U''`?

### B. Full finite-amplitude phase orbit

The binary Helstrom theorem is useful but deliberately weaker than full relative-time recovery. Seek a finite-amplitude orbit metric or phase-estimation functional that:

- survives support changes;
- remains arbitrary-POVM operational;
- reduces locally to the WP07 curvature law;
- recovers the WP04/WP05 divergence for near-lossless continuous temporal recovery when appropriate.

Candidate tools:

- Bures/Hellinger distance over a complete orbit;
- average phase fidelity/sharpness;
- Holevo phase cost;
- Chernoff information integrated over phase;
- posterior first-harmonic retention generalized to rank-changing families.

### C. General bosonic sideband synthesis theorem

WP14/WP07 gives one exactly matched example. Generalize to multimode coherent/Gaussian synthesis:

- multiple upper/lower sidebands;
- arbitrary carrier spectrum;
- sideband-number Hessian as the synthesis resource;
- arbitrary phase-sensitive POVMs;
- autonomous clock/control implementation.

Determine whether a modewise sum/area law exists for the quadratic sideband-supply spectrum.

### D. Deep priority audit

Search specifically against:

- second-order tangent sets of the PSD cone and semidefinite curvature terms;
- singular/rank-changing quantum statistical models;
- Bures/QFI continuous completion;
- block coherence and subspace-coherence monogamy;
- finite-reference-frame phase discrimination;
- resource theories with second-order/asymptotic conversion rates;
- coherent and Gaussian phase/frequency estimation;
- quantum waveform estimation and bandlimited controls.

Do not claim novelty for the underlying matrix geometry.

## Secondary open directions

### Collective-N mean-energy retention

Determine whether entangled collective measurements can beat the one-copy exact envelope `G(Lbar)` per copy.

### Many-body cut law

Test whether temporal information across an autonomous bipartition obeys matched spectral constraints on both sides of the cut.

### Autonomous control-generator resource

If operations do not obey the energy-conserving/covariant structure, determine which dynamical resource must be charged: spectral diameter, interaction norm, action, power, or another invariant.

## Publication / significance gate

Do not draft a new foundational manuscript yet. First require:

- a unified interior/boundary theorem or a sharp impossibility result explaining why no such scalar unification exists;
- deep priority audit including the WP07 collision neighborhood;
- at least one theorem clearly not reducible to known phase estimation/WAY/asymmetry/PSD-cone statements;
- hostile mathematical review;
- sharp or near-sharp constructions;
- explicit physical consequence or thought experiment.

## Documentation discipline

Every material theorem, failed conjecture, prior-art collision, or validation result must be recorded immediately in the branch and reflected in `README.md`, `AGENTS.md`, and this file. The repository, not chat history, is authoritative.
