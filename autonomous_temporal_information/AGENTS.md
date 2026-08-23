# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

The frozen Rev11 paper remains on `agent/temporal-information-resource-law` and must not be rewritten absent a concrete defect.

## Current phase

The PRX Quantum manuscript theorem stack through WP20 is frozen and build-verified, but **research has been explicitly reopened by the user to address the remaining dynamical-implementation limitation**.

The branch previously passed:

- a hostile literature/significance gate: **PROVISIONAL PASS for a narrow theorem paper**;
- a hostile mathematical audit of WP18--WP20: **PASS after targeted corrections**.

The current research frontier is now **WP21--WP22: dynamical implementation cost**.

Priority remains **unverified, not certified**.

Do not modify the current manuscript merely because new research exists. Add new results to the manuscript only after they pass a dedicated hostile proof/prior-art audit and clearly improve the paper rather than destabilizing it.

## Read first

1. `notes/WP22_EXACT_MINIMUM_ENERGY_CONSERVING_IMPLEMENTATION_COST.md`
2. `notes/WP21_DYNAMICAL_IMPLEMENTATION_COUPLING_COST.md`
3. `notes/PUBLICATION_THEOREM_STACK_AFTER_AUDITS.md`
4. `notes/HOSTILE_MATHEMATICAL_AUDIT_WP18_WP20.md`
5. `notes/FOUNDATIONAL_SIGNIFICANCE_PRIORITY_GATE_AFTER_WP20.md`
6. `README.md`
7. `ROADMAP.md`

## Scope lock for the current paper

The existing paper should claim only:

> Globally stationary relative temporal information has two complementary spectral-resource regimes. Finite-radius information requires two-sided pre-existing spectral survival; rank-changing zero-radius information requires two-sided positive second-order spectral synthesis action. The clean laws are finite-copy/arbitrary-POVM and sharp in fixed-total-energy shells, arbitrary coherent support requires operator geometry, and the boundary resource admits a sharp multi-frequency sum.

Do **not** claim a new resource theory of time or new general asymmetry/metrology framework.

## Frozen publication theorem stack through WP20

### 1. WP02 — baseline-energy no-go and robust tangent radius

Fixed baseline mean energy does not bound unrestricted high-frequency local Fisher information under arbitrary state synthesis.

Corrected finite-copy law:

`(R_lin^2/4)[Tr F_N/N] <= T(nu)`.

### 2. WP03 / WP06 — autonomous dual survival

For exact exchange

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`,

`(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`.

WP06 allows arbitrary coherent/history-state support.

### 3. WP07 / WP09 — rank-changing boundary completion

At `R_lin=0`, exact nonlinear physical families can still carry local Fisher information.

One-sided:

`Tr F_N/N <= J <= Delta T`.

Bilateral:

`sqrt[Tr F_N/N] <= sqrt(J_+)+sqrt(J_-)`.

### 4. WP18 — autonomous dual synthesis action

Bilateral clean exchange:

`A_C^(2)+A_S^(2)>=(hbar nu/4)[Tr F_N/N]`.

One-sided clean exchange:

`A_C^(2)+A_S^(2)>=(hbar nu/2)[Tr F_N/N]`.

Both are exactly sharp in fixed-total-energy shells with zero global time-translation asymmetry.

### 5. WP19 — arbitrary coherent-support bridge

Use canonical joint endpoint-role projectors

`Pi_out=supp(A A^dagger)`,

`Pi_in=supp(A^dagger A)`.

Define

`G_ex=2hbar nu Q(Pi_out+Pi_in)Q`,

`A_ex^(2)=(1/4)Tr(G_ex C_Delta)`.

With two-sided shorted pre-existing ceilings `a_+,a_-` and restricted costs `g_+,g_-`, the mixed bridge is the audited `Psi_a` law.

### 6. WP20 — multi-gap autonomous action sum

For one common boundary family,

`C_Sigma>=sum_k[Z_(k,+)+Z_(k,-)]`.

For any positive spectral cost `G`,

`sum_k gamma_k Tr F_(N,k)/N <=4A_(G,Sigma)^(2)`.

Clean bilateral exchange gives

`A_(G,Sigma)^(2)>=sum_k(hbar nu_k/4)Tr F_(N,k)/N`.

One fixed Fourier measurement simultaneously saturates every block and the complete sum in the star-shell extremizer.

## New dynamical frontier

### WP21 — supplied implementation coupling-cost law

For a smooth unitary dilation with baseline tangent generators `K_x,K_y`, the target kernel Hessian has the exact representation

`Q partial_j^2 rho Q = 2 Tr_E[(Q⊗I)K_j Omega_0 K_j(Q⊗I)]`.

For any positive kernel price `G`,

`A_G^(2)=(1/2) sum_j Tr[(G⊗I)K_j Omega_0 K_j]`.

Thus the previously kinematic action is exactly a state-weighted squared implementation coupling into the priced empty sectors.

In the clean single-gap exact exchange,

`boxed: A_ex^(2) <= hbar nu [Var(K_x)+Var(K_y)]`.

The coefficient is sharp in both existing fixed-total-energy extremizers.

Net bare-energy change is not the resource: the sharp constructions remain entirely inside one total-energy shell while the coupling cost and temporal information are nonzero.

### WP22 — exact minimum energy-conserving implementation cost

For a pure-boundary exact relational tangent with globally stationary baseline, define for each real quadrature derivative `D_j`

`C_j=Q D_j P rho_0^+`,

`K_j^hor=i(C_j-C_j^dagger)`.

Then

`-i[K_j^hor,rho_0]=D_j`

and, because the tangent and baseline commute with `H_C+H_S`,

`[K_j^hor,H_C+H_S]=0`.

The horizontal generator variance is

`Var(K_j^hor)=H_jj^SLD/4`.

Therefore the exact minimum over all smooth unitary implementations, even after allowing ancillas, is

`boxed: V_min = inf [Var(K_x)+Var(K_y)] = (1/4)Tr H^SLD.`

The infimum is attained by a target-only exact total-energy-conserving implementation.

In the clean exact-exchange geometry the minimum compatible spectral synthesis action is

`boxed: A_min^(2) = hbar nu V_min = (hbar nu/4)Tr H^SLD.`

Generic `QFI/4 = minimum horizontal purification metric` is established Bures/Uhlmann geometry and is not a novelty claim. The candidate distinct content is the exact energy-conserving relational realization plus equality to the frequency-resolved spectral endpoint action.

## Next theorem target

The next high-value problem is:

> Given a prescribed first-order tangent **and a prescribed nonminimal target-kernel Hessian/action**, determine the exact minimum generator/control cost over all energy-conserving Stinespring dilations.

WP21 gives `V_impl >= A_ex/(hbar nu)`. WP22 proves equality at the minimal-curvature horizontal orbit. A promising construction uses orthogonal ancilla flag sectors to realize excess positive kernel curvature without changing the first derivative. If the sector-by-sector energy-conserving construction closes, the clean full-kernel-2-jet law should be

`V_min(full kernel 2-jet)=A_ex/(hbar nu)`.

Do not call this proved yet.

## Mandatory prior-art positioning

Explicitly distinguish from:

- Marvian--Spekkens modes of asymmetry;
- Carmo--Soares-Pinto Page--Wootters shared asymmetry;
- Tajima--Shiraishi--Saito coherence cost under conservation laws;
- Marvian QFI energetic-coherence formation cost;
- Bures/Uhlmann horizontal purification geometry;
- quantum-speed-limit and integrated Hamiltonian-norm control cost;
- quantitative WAY/reference-frame theory;
- Safranek rank-changing QFI/Bures geometry;
- Gardner et al. waveform Holevo bound;
- Chen--Yang total-protocol energy-constrained metrology.

For WP21--WP22 specifically:

- do not claim novelty for `min purification speed = QFI/4`;
- do not call generator variance thermodynamic work;
- do not call integrated RMS control length a new generic quantum speed limit;
- candidate novelty is only the exact spectral endpoint-action/dynamical-coupling bridge under globally conserving relational exchange.

## Validators

- `numerics/verify_wp21_dynamical_implementation_cost.py` validates the kernel-curvature identity and sharp fixed-shell equality.
- Additional private random-matrix checks verified the WP22 horizontal generator equation and `Var(K)=H_SLD/4` to machine precision; commit a dedicated validator if WP22 advances toward publication.

## Documentation rule

Every material theorem, proof repair, prior-art collision, or strategy change must be reflected in this file, `README.md`, `ROADMAP.md`, and the relevant notes. The repository is authoritative.