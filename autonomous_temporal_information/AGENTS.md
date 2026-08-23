# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

The repository, not chat history, is authoritative. Research is analytical/theoretical; numerical validation is allowed. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

## Current phase

The PRX Quantum R3 manuscript is **build-verified, standalone, and science-frozen** while a stronger post-R3 theorem chain is developed separately.

**Canonical research frontier: WP32, hostile-audited in WP33.**

**WP31 is superseded.** Its classical-mixture insight survives, but its claim that `H_E=0` handles arbitrary prescribed curvature was false when excess curvature occupies an unpopulated target-energy shell.

Priority remains **unverified, not certified**.

## Read first

1. `notes/WP33_HOSTILE_AUDIT_WP32_AND_PRIORITY_BOUNDARY.md`
2. `notes/WP32_REPAIRED_INFINITE_DIMENSIONAL_ENERGY_CONSERVING_2JET_COST.md`
3. `notes/WP31_EXACT_INFINITE_DIMENSIONAL_ENERGY_CONSERVING_2JET_COST.md` — erratum/history only
4. `notes/WP30_INFINITE_DIMENSIONAL_DYNAMICAL_2JET_COST_AND_ENERGY_DOMAIN_BOUNDARY.md`
5. `notes/WP29_INFINITE_DIMENSIONAL_BOUNDARY_SYNTHESIS_ACTION_LAW.md`
6. `notes/WP28_INFINITE_DIMENSIONAL_FINITE_RADIUS_SURVIVAL_LAW.md`
7. `notes/WP27_APPROXIMATE_EXCHANGE_BOUNDARY_SYNTHESIS_ACTION_LAW.md`
8. `notes/WP23_EXACT_PRESCRIBED_2JET_DYNAMICAL_IMPLEMENTATION_COST.md`
9. `manuscript/autonomous_temporal_information/MANUSCRIPT_HANDOFF.md`

## Frozen R3 theorem story

R3 distinguishes two resource regimes for globally stationary relative temporal information:

- finite affine radius -> pre-existing spectral survival;
- rank-changing zero radius -> positive second-order endpoint synthesis action.

Clean exact-exchange action coefficients are `hbar nu/4` bilateral and `hbar nu/2` one-sided. R3 also contains the SLD-QFI boundary corollary, spectator-curvature no-go, coherent-support mixed bridge, exact `Psi_a` envelope, qutrit hierarchy `12 > 43/4 > 55/8`, and multi-gap shared-Hessian theorem.

Do **not** automatically modify R3 merely because stronger theory now exists.

## Post-R3 theorem chain

### WP21--WP23 — dynamical implementation cost

For a smooth unitary dilation,

`Q partial_j^2 rho Q = 2 Tr_E[(Q⊗I)K_j Omega_0 K_j(Q⊗I)]`.

For a prescribed feasible metric-contracted target-kernel Hessian `C`,

`V_min=(1/2)Tr C`.

In the clean single-gap endpoint geometry,

`V_min=A_ex^(2)/(hbar nu)`.

WP23 proves the finite-dimensional exactly energy-conserving version.

### WP24--WP27 — audit and resonance robustness

- `Psi_a(e;p,q)` independently re-derived and brute-force verified: no defect.
- classical boundary nonregularity is prior art, not quantum novelty.
- WP25: finite-radius approximate-gap leakage theorem.
- WP27: rank-boundary approximate-exchange action theorem with explicit off-resonant score-amplitude penalties.

### WP28--WP30 — infinite-dimensional extension

- WP28: finite-radius survival for trace-class baselines with bounded relative tangents.
- WP29: rank-boundary synthesis/action for Hilbert--Schmidt right-relative tangents.
- WP30: unrestricted infinite-dimensional dilation minimum `V_min=(1/2)Tr C`.

### WP32 — repaired exact infinite-dimensional energy-conserving 2-jet theorem

Assume:

- separable target Hilbert space;
- semibounded self-adjoint `H_T`;
- trace-class baseline strongly stationary under `H_T`;
- pure-boundary derivatives strongly preserving target energy;
- `Q D_j P rho_0^(-1/2)` Hilbert--Schmidt;
- prescribed positive trace-class kernel curvature `C>=C_min` strongly preserving target energy.

A stationary trace-class baseline has a countable joint `rho_0/H_T` eigenbasis on its occupied support. Split one occupied baseline eigenstate into countably many **classically incoherent ancilla-labelled copies**. Replicate its horizontal tangent proportionally across the copies, and attach arbitrary excess-curvature eigenmodes using nonnegative ancilla input/output energies

`a_r=max(0,F_r-E_*)`, `b_r=max(0,E_*-F_r)`

so each branch remains in one exact total-energy eigenspace.

The global direct-sum generator may be unbounded, but the baseline is a trace-class classical mixture. Finite quadratic cost gives summable first- and mixed-second trace-norm derivative majorants, so no fourth-moment condition is needed.

Therefore

`boxed:
inf_(semibounded exactly energy-conserving smooth unitary dilations)
V_impl=(1/2)Tr C.`

For clean exact exchange,

`boxed: V_min=A_ex^(2)/(hbar nu).`

Unlike WP31, WP32 also handles spectator curvature in target-energy shells unoccupied at baseline.

### WP33 — hostile audit verdict

**PASS** under WP32's stated finite-information assumptions.

The audit explicitly verifies:

- strong stationarity + trace-class compactness -> countable occupied pure-point energy support;
- energy preservation of horizontal tangent columns;
- strong energy preservation of `C_min` and the excess curvature;
- exact first-order invisibility of orthogonal ancilla flags;
- exact curvature and cost reproduction;
- self-adjoint direct-sum generators;
- trace-norm `C^2` dominated convergence with only quadratic cost;
- finite baseline ancilla mean energy can also be imposed by a suitable choice of split weights.

## Validators

Key permanent validators include WP21, WP22, WP23, WP24, WP25, WP27, WP28/WP29, WP31 special-case shell convergence, and

`numerics/verify_wp32_repaired_energy_conserving_2jet_cost.py`

for mixed/degenerate baselines plus random excess curvature in **unoccupied** energy shells.

## Prior-art discipline

Do not claim novelty for Bures/Uhlmann horizontal lifts, QFI convex-roof variance, generic QSL/control norms, covariant/energy-conserving Stinespring dilation, infinite-dimensional QFI/Bures geometry, classical nonregular boundary statistics, or standard PSD-cone/operator inequalities.

The narrow candidate post-R3 contribution is the **frequency-resolved endpoint synthesis action as the exact minimum state-weighted quadratic coupling cost for a prescribed feasible rank-changing local kernel 2-jet under globally conserving relational dynamics**, with controlled detuning and infinite-dimensional extensions.

## Publication direction

WP33's default recommendation is now:

**Keep R3 frozen and develop WP21--WP32 as a separate dynamical/infinite-dimensional follow-up paper.**

An R4 should be considered only if an editorial need justifies adding one compact dynamical corollary; do not import the full new theorem chain into R3.

## Current work order

1. create a follow-up-paper theorem stack and significance gate;
2. do one more targeted literature search on state-specific prescribed-second-order-jet dilation cost;
3. only then begin a follow-up manuscript skeleton;
4. if further theorem work is needed, prioritize noisy/CPTP implementation cost or approximate-exchange dynamical cost.

## Manuscript integrity

Every public-facing paper must be scientifically standalone. Never include personal repository URLs, repository names, usernames, development history, or dependencies on internal research files.