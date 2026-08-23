# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

The frozen Rev11 paper on `agent/temporal-information-resource-law` must remain untouched absent a concrete defect. The current PRX Quantum manuscript on this branch is also **science-frozen at R3** while the new dynamical/robustness work is audited.

## Current phase

Research was explicitly reopened to attack the paper's remaining physical limitations.

The original theorem chain through WP20 has already passed:

- hostile literature/significance gate: **PROVISIONAL PASS for a narrow theorem paper**;
- hostile mathematical audit: **PASS after targeted corrections**;
- manuscript R3: build-verified and standalone, with an SLD-QFI boundary corollary and spectator-curvature no-go.

The active frontier is now **WP21–WP25**.

Priority is always **unverified, not certified** until a dedicated prior-art audit says otherwise.

## Read first

1. `notes/WP25_APPROXIMATE_BOHR_GAP_ROBUST_SURVIVAL_LAW.md`
2. `notes/WP24_INDEPENDENT_PSI_ENVELOPE_AND_CLASSICAL_NONREGULAR_AUDIT.md`
3. `notes/WP23_EXACT_PRESCRIBED_2JET_DYNAMICAL_IMPLEMENTATION_COST.md`
4. `notes/WP22_EXACT_MINIMUM_ENERGY_CONSERVING_IMPLEMENTATION_COST.md`
5. `notes/WP21_DYNAMICAL_IMPLEMENTATION_COUPLING_COST.md`
6. `notes/PUBLICATION_THEOREM_STACK_AFTER_AUDITS.md`
7. `README.md`
8. `ROADMAP.md`

## Frozen paper theorem arc through WP20

The publication claim remains narrowly:

> Globally stationary relative temporal information has two complementary spectral-resource regimes. Finite-radius information requires pre-existing spectral survival; rank-changing zero-radius information requires positive second-order spectral synthesis action. The clean laws are finite-copy/arbitrary-POVM and sharp in fixed-total-energy shells.

Do **not** claim a new resource theory of time, new Page–Wootters mechanism, generic QFI theory, or generic control/QSL mathematics.

Key results:

- WP02: `(R_lin^2/4)[Tr F_N/N] <= T(nu)`.
- WP03/WP06: autonomous dual survival `<=min{T_C,T_S}`.
- WP07/WP09: one-sided and bilateral rank-boundary synthesis laws.
- WP18: clean action coefficients `hbar nu/4` bilateral and `hbar nu/2` one-sided.
- WP19: arbitrary coherent-support shorted-geometry bridge with `Psi_a`.
- WP20: multi-gap shared-Hessian action sum with one common Fourier measurement saturating the clean star-shell construction.

R3 additionally proves for a clean pure-boundary tangent

`A_C^(2)+A_S^(2) >= (hbar nu/4) Tr H_SLD`

and shows that arbitrary spectator second-order curvature can increase the continuous Bures boundary metric without changing the selected first-order temporal tangent or its mode-specific action.

## New dynamical theorem chain

### WP21 — supplied unitary implementation

For a smooth unitary dilation with tangent generators `K_j`,

`Q partial_j^2 rho Q = 2 Tr_E[(Q⊗I)K_j Omega_0 K_j(Q⊗I)]`.

For any positive kernel price `G`,

`A_G^(2)=(1/2) sum_j Tr[(G⊗I)K_j Omega_0 K_j]`.

Thus the kinematic endpoint action is exactly a state-weighted squared implementation coupling into the priced empty sectors.

In the clean single-gap exchange,

`A_ex^(2) <= hbar nu [Var(K_x)+Var(K_y)]`.

The coefficient is sharp. Net bare-energy change is not the resource: the sharp constructions stay in one exact total-energy shell while this coupling cost is positive.

### WP22 — exact first-order minimum

For the pure-boundary exact relational tangent,

`K_j^hor=i(QD_jP rho_0^+ - rho_0^+ P D_jQ)`

satisfies

`-i[K_j^hor,rho_0]=D_j`,

`[K_j^hor,H_C+H_S]=0`.

The exact minimum over all smooth unitary dilations is

`boxed: V_min=(1/4)Tr H_SLD`.

The minimum is attained target-only and energy-conservingly. In the clean exchange,

`boxed: A_min^(2)=hbar nu V_min=(hbar nu/4)Tr H_SLD`.

The generic first-order Bures/Uhlmann horizontal-lift identity is prior art. Candidate novelty is only the autonomous spectral specialization.

### WP23 — exact prescribed kernel-2-jet minimum

Let the prescribed target kernel Laplacian obey

`C_Delta >= C_min := 2 sum_j QD_jP rho_0^+ P D_jQ`

and `[C_Delta,H_T]=0`.

For every unitary dilation,

`V_impl >= (1/2)Tr C_Delta`.

Conversely, write

`S=(C_Delta-C_min)/2 >=0`.

Purify `S` into an ancilla flag sector orthogonal to the baseline purification. This adds the desired second-order population without changing the first derivative. Assign flag energies sector-by-sector so every baseline/horizontal/flag vector lies in one global energy shell.

Therefore

`boxed: inf V_impl=(1/2)Tr C_Delta`

**even over the exactly total-energy-conserving class**.

In the clean single-gap endpoint geometry `G_ex=2hbar nu Q`, hence

`boxed: V_min(full kernel 2-jet)=A_ex^(2)/(hbar nu)`.

This is the strongest dynamical result so far.

Permanent validator:

`numerics/verify_wp23_prescribed_2jet_implementation_cost.py`

Twenty random multi-energy mixed-baseline stress tests passed privately before commit.

## External-critique audit

### WP24 — `Psi_a` re-derivation

The WP19 scalar envelope was independently derived from the ellipse optimization

`max (sqrt u+sqrt v)^2`, `p u+q v=e+pa`, `u>=a`, `v>=0`.

Result:

`Psi_a=(sqrt a+sqrt(e/q))^2` for `e<=a p^2/q`,

`Psi_a=(e+pa)(1/p+1/q)` for `e>=a p^2/q`.

No defect found. A 100-case brute-force audit agreed to `<2e-11` relative error.

Permanent validator:

`numerics/verify_wp24_psi_envelope.py`

### Classical nonregular statistics

Boundary nonregularity itself is **not quantum novelty**. Future manuscript positioning must explicitly acknowledge at least:

- Chernoff (1954), likelihood-ratio boundary asymptotics;
- Self & Liang (1987), nonstandard MLE/LR boundary theory;
- Shapiro (1985), cone/chi-bar-square inequality-constrained asymptotics.

The candidate quantum contribution is the noncommutative PSD-cone coherence constraint, exact spectral pricing, autonomous exchange structure, and dynamical endpoint-cost theorem—not the mere fact that zero-probability outcomes can appear nonregularly.

## WP25 — approximate Bohr-gap robustness

For `[rho_0,H]=0`, `R=R_lin>0`, and residual

`R_nu=[H,A]-hbar nu A`,

`eta_nu^2=Tr(R_nu rho_0^+ R_nu^dagger)`,

then for every `0<delta<nu`, every finite `N`, and every collective POVM,

`boxed:
(R^2/4)[Tr F_N^tan/N]
 <= T(nu-delta)+R^2 eta_nu^2/(4hbar^2 delta^2).`

Optimize over `delta` if desired.

This decomposes the tangent into near-resonant matrix elements paid by a slightly lower spectral tail and off-resonant leakage paid by the commutator residual.

Exact gap is recovered as `eta_nu->0`, `delta->0`.

A locally stationary clock-signal pair has the corresponding two-sided minimum of signal and clock leakage-corrected tails.

Permanent validator:

`numerics/verify_wp25_approximate_gap_robustness.py`

A private 100-random-instance check passed before commit.

## Mandatory prior-art boundary for WP21–WP25

Do not claim novelty for:

- `QFI/4 = minimum horizontal purification/Fubini–Study metric`;
- Bures/Uhlmann geometry;
- generic Mandelstam–Tamm/quantum-speed-limit bounds;
- generic integrated Hamiltonian/control norms;
- standard boundary likelihood asymptotics;
- approximate-eigenvector spectral leakage as a generic mathematical idea.

Important current neighbor: Carrasco & Spehner, arXiv:2606.06759 (2026), derives Bures geodesics for non-faithful states and quantum-speed-limit consequences. This makes the first-order Bures/QSL boundary even more clearly prior art. The WP23 prescribed second-order kernel-jet construction remains the narrower candidate distinction; priority unverified.

## Immediate research order

1. Hostile-audit WP23's energy-shell flag construction and search second-order constrained Stinespring/purification prior art.
2. Search approximate eigenoperator/Bohr-mode robustness literature for WP25 collisions.
3. Extend **zero-radius synthesis/action** to approximate exchange if possible; this directly attacks the remaining exact-resonance idealization in the paper's headline boundary regime.
4. Then attempt the infinite-dimensional theorem, beginning with trace-class `rho_0`, semibounded pure-point `H`, and bounded relative tangent before continuous spectra/unbounded generators.
5. Only after these pass decide whether a manuscript R4 is justified. Do not destabilize R3 merely because new research exists.

## Documentation rule

Every material theorem, proof repair, prior-art collision, validator, or strategy change must be recorded in `notes/`, then synchronized into this file, `README.md`, and `ROADMAP.md`. The repository is authoritative; chat is not.