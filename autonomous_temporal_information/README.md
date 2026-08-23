# Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

The frozen Rev11 random-time paper remains untouched on `agent/temporal-information-resource-law`.

## Status

The publication theorem stack through **WP20** is frozen and manuscript-ready. Research was explicitly reopened on 2026-08-23 to address the remaining **dynamical implementation cost** limitation.

Current frontier: **WP21--WP22**.

- Literature/significance gate for the paper: **PROVISIONAL PASS**.
- Hostile mathematical gate through WP20: **PASS**.
- PRX Quantum manuscript: build-verified, standalone, and should remain frozen while the new dynamical work is audited.
- Priority: **unverified, not certified**.

Read first:

1. `notes/WP22_EXACT_MINIMUM_ENERGY_CONSERVING_IMPLEMENTATION_COST.md`
2. `notes/WP21_DYNAMICAL_IMPLEMENTATION_COUPLING_COST.md`
3. `AGENTS.md`
4. `ROADMAP.md`
5. `notes/PUBLICATION_THEOREM_STACK_AFTER_AUDITS.md`

## Published-manuscript theorem story through WP20

A globally stationary relative temporal mode has two complementary resource regimes.

### Finite affine tangent radius

For exact gap `nu`, finite `N`, arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N/N] <= T(nu)`.

For exact autonomous clock--signal exchange,

`(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`.

Thus robust temporal information requires **pre-existing spectral survival** on both sides of the relational cut.

### Rank-changing boundary

At `R_lin=0`, a nonlinear physical family can remain informative, but positivity requires second-order population synthesis.

One-sided:

`Tr F_N/N <= J <= Delta T`.

Bilateral:

`sqrt[Tr F_N/N] <= sqrt(J_+)+sqrt(J_-)`.

For clean globally stationary exchange,

`A_C^(2)+A_S^(2)>=(hbar nu/4)[Tr F_N/N]`

bilaterally and

`A_C^(2)+A_S^(2)>=(hbar nu/2)[Tr F_N/N]`

one-sidedly.

Both coefficients are sharp in fixed-total-energy shells where global time-translation asymmetry and signed total-energy curvature vanish.

The R3 manuscript additionally shows for the pure-boundary SLD tangent

`A_C^(2)+A_S^(2)>=(hbar nu/4)Tr H_SLD`,

and separates this from arbitrary spectator second-order Bures curvature.

## Arbitrary coherent support and multiple gaps

WP19 uses canonical endpoint-role projectors

`Pi_out=supp(A A^dagger)`,

`Pi_in=supp(A^dagger A)`,

with

`G_ex=2hbar nu Q(Pi_out+Pi_in)Q`.

WP20 gives the common-Hessian spectral sum

`sum_k gamma_k Tr F_(N,k)/N <=4A_(G,Sigma)^(2)`,

with clean bilateral form

`A_(G,Sigma)^(2)>=sum_k(hbar nu_k/4)Tr F_(N,k)/N`.

One Fourier measurement simultaneously saturates the complete clean sum in the fixed-total-energy star shell.

## New dynamical result — WP21

Let a smooth global unitary implementation have target reduction `rho(x,y)`, target baseline support `P`, kernel `Q`, global baseline `Omega_0`, and Hermitian tangent generators `K_x,K_y`.

Then the target kernel Hessian is not merely bounded; it has the exact dynamical representation

`boxed:
Q partial_j^2 rho Q
=2 Tr_E[(Q⊗I)K_j Omega_0 K_j(Q⊗I)].`

Consequently for any positive kernel price `G`,

`boxed:
A_G^(2)
=(1/2)sum_j Tr[(G⊗I)K_j Omega_0 K_j].`

So the previously kinematic synthesis action is exactly an initial-state-weighted squared coupling into the priced empty endpoint sectors.

For the clean single-gap exact exchange,

`boxed:
A_ex^(2)<=hbar nu[Var(K_x)+Var(K_y)].`

The fixed-shell bilateral and one-sided extremizers saturate this equality.

This also proves that **net bare-energy change is not the implementation resource**: the sharp constructions remain inside one total-energy eigenspace while their temporal information and coupling cost are nonzero.

## Exact minimum dynamical cost — WP22

For a globally stationary pure-boundary exact exchange tangent, let `D_j` be either physical quadrature derivative and define

`K_j^hor=i[Q D_j P rho_0^+ - rho_0^+ P D_j Q]`.

Then

`-i[K_j^hor,rho_0]=D_j`

and

`[K_j^hor,H_C+H_S]=0`.

The generator variance is

`Var(K_j^hor)=H_jj^SLD/4`.

Therefore the exact minimum quadratic implementation-coupling cost is

`boxed:
V_min
=inf [Var(K_x)+Var(K_y)]
=(1/4)Tr H_SLD.`

The infimum is attained by a **target-only, exactly total-energy-conserving implementation**; an external asymmetry battery is unnecessary.

The minimum compatible spectral synthesis action is

`boxed:
A_min^(2)
=hbar nu V_min
=(hbar nu/4)Tr H_SLD.`

Generic Bures/Uhlmann horizontal-lift minimization is prior art. The candidate distinct result is the constructive energy-conserving relational lift and its exact equality to the frequency-resolved endpoint action.

## Current open problem

Given both the first-order tangent and a prescribed **nonminimal** target-kernel Hessian/action, determine the exact minimum energy-conserving implementation cost.

Known lower bound:

`V_impl>=A_ex/(hbar nu)`.

WP22 proves equality at the minimal-curvature horizontal orbit.

A promising orthogonal-ancilla-flag construction may realize arbitrary excess positive kernel curvature without changing the first derivative, suggesting

`V_min(full kernel 2-jet)=A_ex/(hbar nu)`.

This is **not yet proved**; the remaining issue is a rigorous sector-by-sector energy-conservation construction.

## Infinite-dimensional track

Infinite-dimensional metrology is still viable, but it is second priority after the clean dynamical 2-jet problem.

The safe route is:

1. semibounded pure-point Hamiltonians and trace-class baselines;
2. explicit domains for unbounded `H`, `A`, and pseudoinverse-weighted forms;
3. finite-rank spectral truncations with uniform resource bounds;
4. monotone/closed-form convergence;
5. continuous spectra and Gaussian/CV systems only after that.

Generic Gaussian QFI is already mature prior art; the research target would be an infinite-dimensional extension of the **survival/synthesis resource law**, not another Gaussian-QFI formula.

## Prior-art boundary

Do not claim novelty for:

- Bures/Uhlmann horizontal purification geometry;
- `QFI/4 = minimum purification speed`;
- generic quantum speed limits or integrated Hamiltonian-norm cost;
- Tajima--Shiraishi--Saito coherence cost for conservation-law-violating subsystem operations;
- Marvian energetic-coherence formation cost;
- generic Gaussian/CV QFI formulas.

The dynamical candidate contribution is narrowly the **spectral endpoint synthesis action as an exact/minimal energy-conserving implementation-coupling cost for a relational temporal mode**.

## Next action

1. hostile proof/prior-art audit of WP21--WP22;
2. commit a dedicated WP22 validator;
3. prove or kill the full kernel-2-jet equality candidate;
4. only then decide whether the dynamical result enters the current manuscript or becomes a follow-up;
5. pursue the infinite-dimensional extension afterward if it remains high value.