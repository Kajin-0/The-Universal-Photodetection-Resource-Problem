# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

The repository, not chat history, is authoritative. Research is analytical/theoretical; numerical work is allowed for validation. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

## Current phase

The PRX Quantum manuscript through R3 is **build-verified and scientifically frozen while the post-manuscript theorem chain is audited**. Research was explicitly reopened to address the paper's remaining physical limitations.

**Current research frontier: WP31.**

The old instruction “do not create WP21” is obsolete.

Do not modify the R3 manuscript merely because new results exist. Add WP21–WP31 only after a dedicated proof/prior-art/significance decision shows that an R4 improves the paper more than it destabilizes it. A separate follow-up paper is a live alternative.

Priority remains **unverified, not certified**.

## Mandatory first read

1. `notes/WP31_EXACT_INFINITE_DIMENSIONAL_ENERGY_CONSERVING_2JET_COST.md`
2. `notes/WP30_INFINITE_DIMENSIONAL_DYNAMICAL_2JET_COST_AND_ENERGY_DOMAIN_BOUNDARY.md` — historical obstruction, resolved by WP31
3. `notes/WP29_INFINITE_DIMENSIONAL_BOUNDARY_SYNTHESIS_ACTION_LAW.md`
4. `notes/WP28_INFINITE_DIMENSIONAL_FINITE_RADIUS_SURVIVAL_LAW.md`
5. `notes/WP27_APPROXIMATE_EXCHANGE_BOUNDARY_SYNTHESIS_ACTION_LAW.md`
6. `notes/WP26_HOSTILE_AUDIT_WP23_AND_SECOND_ORDER_PRIOR_ART_BOUNDARY.md`
7. `notes/WP25_APPROXIMATE_BOHR_GAP_ROBUST_SURVIVAL_LAW.md`
8. `notes/WP24_INDEPENDENT_PSI_ENVELOPE_AND_CLASSICAL_NONREGULAR_AUDIT.md`
9. `notes/WP23_EXACT_PRESCRIBED_2JET_DYNAMICAL_IMPLEMENTATION_COST.md`
10. `notes/WP22_EXACT_MINIMUM_ENERGY_CONSERVING_IMPLEMENTATION_COST.md`
11. `notes/WP21_DYNAMICAL_IMPLEMENTATION_COUPLING_COST.md`
12. `manuscript/autonomous_temporal_information/MANUSCRIPT_HANDOFF.md`

## Frozen R3 manuscript story through WP20

The manuscript distinguishes two spectral-resource regimes for a globally stationary relative temporal mode.

### Finite affine radius

For an exact gap `nu`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N^tan/N] <= T(nu)`.

For autonomous clock--signal exchange,

`(R_lin^2/4)[Tr F_N^tan/N] <= min{T_C(nu),T_S(nu)}`.

### Rank-changing zero radius

One-sided boundary:

`Tr F_N^tan/N <= J <= Delta T`.

Bilateral boundary:

`sqrt(Tr F_N^tan/N) <= sqrt(J_+)+sqrt(J_-)`.

Clean autonomous synthesis action:

- bilateral: `A_C^(2)+A_S^(2) >= (hbar nu/4)[Tr F_N^tan/N]`;
- one-sided: `A_C^(2)+A_S^(2) >= (hbar nu/2)[Tr F_N^tan/N]`.

R3 additionally records

`A_C^(2)+A_S^(2) >= (hbar nu/4) Tr H_SLD`

for the pure-boundary SLD tangent and proves that arbitrary extra Bures boundary curvature can be injected in a spectator sector without changing the selected temporal tangent.

The manuscript also contains the WP19 coherent-support bridge, the audited `Psi_a` envelope, the `12 > 43/4 > 55/8` qutrit hierarchy, and the WP20 multi-gap shared-Hessian law.

## Post-manuscript theorem chain

### WP21 — supplied implementation coupling identity

For a smooth unitary dilation with baseline `Omega_0` and tangent generators `K_j`,

`Q partial_j^2 rho Q = 2 Tr_E[(Q⊗I)K_j Omega_0 K_j(Q⊗I)]`.

For any positive kernel price `G`,

`A_G^(2)=(1/2)sum_j Tr[(G⊗I)K_j Omega_0 K_j]`.

Thus the previously kinematic synthesis action is exactly a state-weighted squared dynamical coupling into priced empty sectors.

### WP22 — exact minimum for a prescribed pure-boundary tangent

The energy-conserving horizontal generator realizes the tangent and gives

`V_min=(1/4)Tr H_SLD`,

`A_min^(2)=hbar nu V_min=(hbar nu/4)Tr H_SLD`.

Generic Bures/Uhlmann `QFI/4` horizontal-lift geometry is prior art; candidate novelty is only the energy-conserving relational specialization and endpoint-action equality.

### WP23 — exact prescribed kernel 2-jet cost

For a prescribed feasible metric-contracted target-kernel Hessian

`C >= C_min`,

finite-dimensional clean pure-boundary dilations obey and attain

`boxed: V_min=(1/2)Tr C=A_ex^(2)/(hbar nu)`.

Excess curvature is realized in an orthogonal ancilla flag sector without changing the first derivative.

### WP24 — independent mixed-envelope audit + classical boundary prior art

The manuscript's piecewise `Psi_a(e;p,q)` envelope was independently re-derived and brute-force validated. No defect was found.

Boundary nonregularity itself is **not quantum novelty**. Chernoff/Self--Liang/Shapiro-type nonregular classical statistics must be acknowledged in any future revision. The quantum-specific content is the operator PSD-cone support/kernel geometry, coherent orientation interference, spectral pricing, autonomous exchange structure, and dynamical implementation results.

### WP25 — approximate-gap finite-radius robustness

With commutator residual

`R_nu=[H,A]-hbar nu A`,

`eta_nu^2=Tr(R_nu rho_0^+ R_nu^dagger)`,

one obtains for every `0<delta<nu`

`(R_lin^2/4)[Tr F_N^tan/N]
 <= T(nu-delta)+(R_lin^2 eta_nu^2)/(4 hbar^2 delta^2)`.

Thus exact resonance is not an all-or-nothing assumption.

### WP26 — hostile audit / second-order prior-art boundary

WP23's lower bound, flag construction, and finite-dimensional exact energy-conserving realization passed a dedicated hostile audit. The theorem prescribes the physical metric contraction of the kernel Hessian, not an arbitrary full mixed-second-derivative tensor.

### WP27 — approximate-exchange boundary robustness

For bilateral rank-boundary synthesis, the Fisher score amplitude satisfies a near-resonant endpoint-curvature bound plus explicit off-resonant residual penalties. Schematically,

`sqrt(Tr F_N^tan/N)
 <= sqrt(Delta T_+^(delta))+sqrt(Delta T_-^(delta))+epsilon_delta`.

The corresponding autonomous action law approaches the exact `hbar nu/4` coefficient continuously as detuning vanishes.

### WP28 — infinite-dimensional finite-radius survival

For a separable Hilbert space, trace-class baseline, and bounded relative tangent

`A=rho_0^(1/2) B rho_0^(1/2)`, `B` bounded,

the finite-radius arbitrary-POVM/finite-copy theorem extends exactly. Using the covariance form of an exact Bohr gap and the spectral theorem removes the pure-point restriction on the ambient Hamiltonian.

### WP29 — infinite-dimensional rank-boundary synthesis

If

`X rho_0^(-1/2)` and `Y rho_0^(-1/2)`

are Hilbert--Schmidt, finite-rank support truncations and monotone positive quadratic forms give

`C_Delta >= X rho_0^+ X^dagger + Y rho_0^+ Y^dagger`

in the rigorous trace-class sense. The arbitrary-POVM Minkowski law, clean autonomous action coefficients, and SLD relation survive.

### WP30 — unrestricted infinite-dimensional dynamical 2-jet cost

Under WP29 finite-information regularity,

`inf_(smooth unitary dilations) V_impl=(1/2)Tr C`.

WP30 initially left exact semibounded energy conservation open for unbounded stationary target-energy support because one coherent fixed-shell purification created a domain/fourth-moment issue.

### WP31 — exact infinite-dimensional energy-conserving 2-jet cost

WP31 resolves that obstruction by using a **classically mixed energy-shell dilation** rather than one coherent purification across target energies.

A stationary trace-class state has countable pure-point support on the part occupied by the state. Decompose

`rho_0=direct_sum_E rho_E`.

Within each target-energy shell, build the WP23 optimal dilation and use a zero-energy ancilla. Form the global baseline as the incoherent mixture

`Omega_0=direct_sum_E p_E |Omega_E><Omega_E|`.

Finite quadratic cost already dominates all first and mixed second trace-norm derivatives. The global direct-sum generator may be unbounded, but no fourth-moment condition is required.

Therefore, even with unbounded occupied target energies,

`boxed:
inf_(semibounded exactly energy-conserving smooth unitary dilations)
V_impl=(1/2)Tr C.`

For the clean single-gap endpoint price,

`boxed: V_min=A_ex^(2)/(hbar nu).`

The ancilla Hamiltonian may be chosen `H_E=0`.

## Validators

Permanent validators include:

- `numerics/verify_wp21_dynamical_implementation_cost.py`
- `numerics/verify_wp22_exact_minimum_implementation_cost.py`
- `numerics/verify_wp23_prescribed_2jet_implementation_cost.py`
- `numerics/verify_wp24_psi_envelope.py`
- `numerics/verify_wp25_approximate_gap_robustness.py`
- `numerics/verify_wp27_approximate_boundary_action.py`
- `numerics/verify_wp28_wp29_infinite_truncation.py`
- `numerics/verify_wp31_infinite_energy_conserving_shell_dilation.py`

## Prior-art discipline

Do not claim novelty for:

- Page--Wootters relational time or modes of asymmetry;
- generic Fisher/QFI/Bures/Holevo theory;
- Bures/Uhlmann horizontal purification geometry or `QFI/4=min purification speed`;
- classical nonregular boundary statistics;
- shorted operators, numerical radius, PSD-cone/Schur-complement mathematics;
- generic quantum speed limits or integrated Hamiltonian norms;
- energy-conserving/covariant Stinespring dilation theory;
- Tajima--Shiraishi--Saito external coherence cost;
- infinite-dimensional QFI/Bures functional analysis.

The candidate post-R3 contribution is narrowly the **frequency-resolved endpoint synthesis action as the exact minimum state-weighted quadratic coupling cost for a prescribed feasible rank-changing local kernel 2-jet under globally conserving relational dynamics**, together with controlled approximate-gap and infinite-dimensional extensions.

Priority is not certified.

## Current work order

1. hostile-audit WP31's stationary trace-class energy-support lemma and trace-norm dominated-convergence proof;
2. targeted priority search for state-specific prescribed-second-order-jet implementation-cost theorems and energy-shell dilation equivalents;
3. run/expand WP31 validators, including mixed/degenerate shell cases;
4. make a deliberate publication decision: R4 of the current PRXQ paper versus a separate dynamical follow-up;
5. if continuing theory, prioritize noisy/CPTP implementation cost or unbounded-relative-tangent quadratic-form extensions, not more formal branch bookkeeping.

## Manuscript integrity rule

Every public-facing paper must be scientifically standalone. Never include personal GitHub URLs, repository names, usernames, development history, or instructions that require the reader to consult the repository. The repository is internal research infrastructure only.

## Documentation rule

Every material theorem, counterexample, proof repair, prior-art collision, or strategy change must update the relevant WP note and these landing files. Do not allow the authoritative research state to exist only in chat.