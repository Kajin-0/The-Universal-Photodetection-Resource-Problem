# Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

The PRX Quantum R3 manuscript is **build-verified and science-frozen** while the post-manuscript theorem chain is audited. The older random-time Rev11 paper remains frozen on `agent/temporal-information-resource-law`.

**Current research frontier: WP31.**

Priority for all post-R3 results remains **unverified, not certified**.

## Read first

1. `notes/WP31_EXACT_INFINITE_DIMENSIONAL_ENERGY_CONSERVING_2JET_COST.md`
2. `notes/WP30_INFINITE_DIMENSIONAL_DYNAMICAL_2JET_COST_AND_ENERGY_DOMAIN_BOUNDARY.md`
3. `notes/WP29_INFINITE_DIMENSIONAL_BOUNDARY_SYNTHESIS_ACTION_LAW.md`
4. `notes/WP28_INFINITE_DIMENSIONAL_FINITE_RADIUS_SURVIVAL_LAW.md`
5. `notes/WP27_APPROXIMATE_EXCHANGE_BOUNDARY_SYNTHESIS_ACTION_LAW.md`
6. `notes/WP26_HOSTILE_AUDIT_WP23_AND_SECOND_ORDER_PRIOR_ART_BOUNDARY.md`
7. `notes/WP25_APPROXIMATE_BOHR_GAP_ROBUST_SURVIVAL_LAW.md`
8. `notes/WP24_INDEPENDENT_PSI_ENVELOPE_AND_CLASSICAL_NONREGULAR_AUDIT.md`
9. `notes/WP23_EXACT_PRESCRIBED_2JET_DYNAMICAL_IMPLEMENTATION_COST.md`
10. `AGENTS.md`
11. `ROADMAP.md`

## Frozen R3 theorem story

The paper establishes two complementary resource regimes for globally stationary relative temporal information.

### Finite affine radius

For exact gap `nu`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N^tan/N] <= T(nu)`.

Autonomous exact exchange gives the two-sided version

`(R_lin^2/4)[Tr F_N^tan/N] <= min{T_C(nu),T_S(nu)}`.

### Rank-changing boundary

At `R_lin=0`, positive second-order endpoint synthesis replaces pre-existing survival.

Clean autonomous action laws:

- bilateral: `A_C^(2)+A_S^(2) >= (hbar nu/4)[Tr F_N^tan/N]`;
- one-sided: `A_C^(2)+A_S^(2) >= (hbar nu/2)[Tr F_N^tan/N]`.

R3 also contains the pure-boundary SLD-QFI corollary

`A_C^(2)+A_S^(2) >= (hbar nu/4)Tr H_SLD`,

the spectator-curvature no-go, the coherent-support mixed bridge, the exact `Psi_a` envelope, the `12 > 43/4 > 55/8` qutrit hierarchy, and the multi-gap shared-Hessian theorem.

## Dynamical completion — WP21 to WP23

For any smooth unitary dilation,

`Q partial_j^2 rho Q
 =2 Tr_E[(Q⊗I)K_j Omega_0 K_j(Q⊗I)]`.

Hence the kinematic endpoint action is exactly a state-weighted squared implementation coupling.

For a prescribed feasible metric-contracted target-kernel Hessian

`C >= C_min`,

WP23 proves in finite dimension

`boxed: V_min=(1/2)Tr C`.

For the clean exact-exchange endpoint price,

`boxed: V_min=A_ex^(2)/(hbar nu)`.

The minimum is attained by an exactly total-energy-conserving dilation. Net bare-energy change can remain zero, so the correct dynamical resource is coupling/control strength rather than work defined only by mean-energy change.

## Robustness and audit — WP24 to WP27

- **WP24:** independently re-derived and brute-force validated the manuscript's `Psi_a(e;p,q)` envelope; no defect found. Also records classical nonregular boundary statistics as mandatory prior art.
- **WP25:** finite-radius approximate-gap theorem with an explicit commutator-residual leakage penalty.
- **WP26:** hostile audit of the prescribed-2-jet theorem and its second-order prior-art boundary.
- **WP27:** approximate-exchange rank-boundary law; off-resonant score amplitude is charged by explicit residual penalties, and the exact `hbar nu/4` bilateral coefficient is recovered continuously as detuning vanishes.

Thus exact Bohr resonance is no longer an all-or-nothing idealization in either headline regime.

## Infinite-dimensional extension — WP28 to WP31

### WP28 — finite-radius survival

For a trace-class baseline on a separable Hilbert space and bounded relative tangent

`A=rho_0^(1/2) B rho_0^(1/2)`, `B` bounded,

the arbitrary-POVM, arbitrary-finite-copy finite-radius theorem extends exactly. Using the exact-gap covariance relation and the spectral theorem allows general semibounded spectral measures, not only pure-point ambient Hamiltonians.

### WP29 — rank-boundary synthesis

If

`X rho_0^(-1/2)` and `Y rho_0^(-1/2)`

are Hilbert--Schmidt, finite-rank support truncations give the rigorous trace-class limit

`C_Delta >= X rho_0^+ X^dagger + Y rho_0^+ Y^dagger`.

The common-record Minkowski law, clean autonomous action coefficients, and SLD relation survive.

### WP30 — unrestricted dilation cost

For prescribed positive trace-class kernel curvature `C`,

`inf_(smooth unitary dilations) V_impl=(1/2)Tr C`.

WP30 initially left exact semibounded energy conservation open when the stationary state had unbounded target-energy support.

### WP31 — exact energy-conserving infinite-dimensional cost

WP31 resolves the WP30 domain issue.

A stationary trace-class state occupies a countable set of normalizable target-energy eigenspaces on its support. Decompose

`rho_0=direct_sum_E rho_E`.

Build the optimal WP23 dilation separately in every occupied target-energy shell, use a zero-energy ancilla, and form the global baseline as the **incoherent shell mixture**

`Omega_0=direct_sum_E p_E |Omega_E><Omega_E|`.

Finite quadratic cost is then sufficient to dominate the first and mixed second trace-norm derivatives, even when the direct-sum generator is unbounded. No fourth-moment condition is needed.

Therefore, including unbounded occupied target energies,

`boxed:
inf_(semibounded exactly energy-conserving smooth unitary dilations)
V_impl=(1/2)Tr C.`

For the clean single-gap endpoint action,

`boxed: V_min=A_ex^(2)/(hbar nu).`

The ancilla Hamiltonian can be chosen `H_E=0`.

## Validators

Permanent validators cover WP21, WP22, WP23, WP24, WP25, WP27, WP28/WP29, and WP31. The WP31 validator deliberately uses shell-generator norms that diverge with energy while the state-weighted cost and trace-norm `C^2` domination sums converge.

## Prior-art boundary

Do not claim novelty for Bures/Uhlmann horizontal lifts, generic QFI/QSL/control-norm relations, covariant or energy-conserving Stinespring dilation theory, classical nonregular boundary statistics, infinite-dimensional QFI/Bures functional analysis, Page--Wootters relational time, or standard operator inequalities.

The narrow candidate post-R3 contribution is the **frequency-resolved endpoint synthesis action as the exact minimum state-weighted quadratic implementation-coupling cost for a prescribed feasible rank-changing local kernel 2-jet under globally conserving relational dynamics**, plus controlled approximate-gap and infinite-dimensional extensions.

## Current work order

1. hostile-audit WP31's compactness/energy-support lemma and trace-norm dominated-convergence proof;
2. targeted priority search against state-specific second-order Stinespring/purification implementation-cost results;
3. extend WP31 validation to mixed/degenerate energy shells;
4. decide deliberately between manuscript R4 and a separate dynamical follow-up;
5. if further theory is needed, prioritize noisy/CPTP implementation cost or unbounded-relative-tangent quadratic-form extensions.

Every public-facing paper must remain scientifically standalone: never include personal repository URLs, usernames, repository names, or development-history dependencies.