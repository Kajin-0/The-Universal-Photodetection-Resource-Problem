# Roadmap — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

## Goal

Seek a foundational physical resource principle for temporal information when clock, signal, controller, detector, and memory are all internal quantum systems. The finished Rev11 random-time law remains frozen on its parent branch.

## Completed foundations

### WP01 — prior-art and model boundary — PASS

Do not claim novelty for modes-of-asymmetry, QFI as asymmetry, finite clocks/control, Page--Wootters relational time, quantitative WAY, generic speed limits, phase-estimation sine states, PSD-cone curvature, singular QFI/Bures geometry, or simply charging preparation/control energy.

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

### WP07 — nonlinear zero-radius spectral-synthesis law — PASS in the support-to-kernel/two-sector regimes

For a two-sided `C^2` physical curve at a rank-deficient baseline, established PSD-cone second-order geometry gives

`Q rho''(0) Q >= 2 Q rho'(0)P(P rho0 P)^(-1)P rho'(0)Q`.

The one-parameter scalar consequence

`F_Q <= 2 T_U''`

is close to known rank-changing QFI/Bures Hessian geometry and is not the main novelty claim.

The stronger operational result uses the project's two-quadrature complex tangent convention. For

`A=P_U A P`,

where `P=supp(rho0)` and `P_U` is a previously empty upper endpoint, define

`J(A|rho0)=Tr(A rho0^+ A^dagger)`.

For every finite `N` and arbitrary entangled collective POVM,

`Tr F_N/N <= J(A|rho0)`.

Second-order positivity applied to the two quadratures gives

`J(A|rho0) <= Delta T_U(0)`,

where

`T_U(x,y)=Tr[P_U rho(x,y)]`.

Hence the sharp zero-radius law is

`boxed: Tr F_N/N <= J(A|rho0) <= Delta T_U(0)`.

Equivalently,

`boxed: (1/4)[Tr F_N/N] <= (1/4)Delta T_U(0)`.

The minimal pure qubit saturates both inequalities at one copy with a fixed four-outcome equatorial POVM.

The coherent-sideband no-go also saturates the operational coefficient:

`alpha_sb(x,y)=(A/2)(x+i y)`,

`n_sb=Nbar(x^2+y^2)/4`,

`Delta n_sb(0)=Nbar`,

while heterodyne measurement gives

`Tr F=Nbar`.

Thus the high-frequency family that evades baseline-energy-only bounds is paid for exactly by second-order sideband population synthesis.

A complementary finite-amplitude two-endpoint phase theorem gives

`D_tr^2/4 <= min{T_C(nu),T_S(nu)}`

for a `pi` relative-phase pair and therefore

`Ebar_C^+ + Ebar_S^+ >= (hbar nu/2)D_tr^2`.

The underlying PSD-cone, singular-QFI/Bures, block-coherence, and Helstrom mathematics is prior art. Candidate novelty is restricted to the frequency-resolved finite-copy arbitrary-POVM temporal-resource consequence.

## Current frontier — unified mixed-endpoint exact-gap law

### A. Decompose a general exact-gap tangent

For a rank-deficient arbitrary baseline, a positive-gap tangent can contain several endpoint types:

1. **support-to-support:** both endpoints already populated. This is the WP06 finite-radius sector.
2. **support-to-kernel:** the upper endpoint is absent at baseline and is synthesized at second order. This is the sharp WP07 sector.
3. **kernel-to-support:** the upper endpoint is present but the lower endpoint is absent and must be synthesized at second order in the conjugate direction.

The next theorem should charge all three without double counting.

### B. Determine whether sharp scalar additivity is possible

Write schematically

`A=A_int+A_syn`.

For an arbitrary POVM outcome,

`z_y=Tr(A_int M_y)+Tr(A_syn M_y)`.

The Fisher trace contains

`|z_y|^2/p_y`,

so score-space cross terms need not vanish merely because the operator blocks are orthogonal.

Required work:

- test whether exact-gap block structure forces any cancellation after summing a POVM;
- if not, derive the sharp universal Minkowski-type bound;
- construct counterexamples to naive additive resource formulas;
- identify a matrix/Gram resource that may retain sharpness even when no scalar sum does.

A proof that scalar additivity is impossible would be scientifically useful because it would identify the correct geometry of the unified resource.

### C. Preserve the endpoint orientation

The upper-kernel and lower-kernel cases are physically different.

- upper kernel: high-energy population is synthesized and the WP07 upper-curvature law applies directly;
- lower kernel: the high-energy endpoint may be pre-existing, but the donor/lower state must be synthesized; the resource accounting should involve upper survival **and** lower-endpoint curvature.

The autonomous clock--signal version should then test whether each local subsystem incurs the appropriate pre-existing/synthesis cost under the opposite orientation of the exchange.

### D. Full finite-amplitude phase orbit

The binary Helstrom theorem is useful but deliberately weaker than continuous relative-time recovery. Seek a support-changing phase-orbit metric that:

- remains arbitrary-POVM operational;
- reduces locally to WP07;
- recovers WP04/WP05 divergence for near-lossless continuous temporal recovery when appropriate.

Candidate tools include Bures/Hellinger orbit distance, posterior phase sharpness, Holevo phase cost, Chernoff information over phase, or a generalized Herglotz retention functional.

### E. General bosonic sideband synthesis theorem

WP14/WP07 now match exactly in the one-sideband model. Generalize to:

- multiple upper/lower sidebands;
- arbitrary carrier spectrum;
- sideband-number Hessian as the spectral synthesis resource;
- arbitrary phase-sensitive POVMs;
- autonomous clock/control implementation.

Seek a modewise sum/area law for the quadratic sideband-supply spectrum.

### F. Deep priority audit

Continue targeted searches against:

- second-order tangent sets of the PSD cone;
- singular/rank-changing quantum statistical models;
- Bures/QFI continuous completion;
- subspace/block coherence;
- finite-reference-frame phase discrimination;
- quantum waveform estimation and Gaussian sensing;
- resource theories with second-order/asymptotic conversion rates.

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

- a unified mixed-endpoint theorem or a sharp impossibility result explaining why no scalar unification exists;
- deep priority audit including the WP07 collision neighborhood;
- at least one theorem clearly not reducible to known phase estimation/WAY/asymmetry/PSD-cone statements;
- hostile mathematical review;
- sharp or near-sharp constructions;
- explicit physical consequence or thought experiment.

## Documentation discipline

Every material theorem, failed conjecture, prior-art collision, or validation result must be recorded immediately in the branch and reflected in `README.md`, `AGENTS.md`, and this file. The repository, not chat history, is authoritative.
