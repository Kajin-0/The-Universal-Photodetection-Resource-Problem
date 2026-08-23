# Roadmap — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

## Goal

Develop and publish a rigorously scoped resource law for autonomous temporal information, then determine whether the rank-boundary synthesis action admits a genuine dynamical implementation interpretation.

The frozen Rev11 random-time paper remains untouched on its parent branch.

## Publication state

The theorem program through WP20 has passed the internal manuscript gates.

- Significance/literature gate: **PROVISIONAL PASS** for a narrow theorem paper.
- Hostile mathematical gate: **PASS after targeted corrections**.
- PRX Quantum manuscript: build-verified and standalone.
- Priority: **unverified, not certified**.
- Main publication theorem stack through WP20: **frozen unless a concrete new theorem materially improves the paper**.

The user explicitly reopened research on 2026-08-23 to address the remaining **dynamical implementation cost** limitation. This produced WP21 and WP22.

## Frozen publication theorem arc

### WP02 — finite-radius survival

`(R_lin^2/4)[Tr F_N/N] <= T(nu)`.

### WP03 / WP06 — autonomous dual survival

`(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`.

### WP07 / WP09 — rank-changing boundary

One-sided:

`Tr F_N/N <= J <= Delta T`.

Bilateral:

`sqrt[Tr F_N/N] <= sqrt(J_+)+sqrt(J_-)`.

### WP18 — clean autonomous synthesis action

Bilateral:

`A_C^(2)+A_S^(2)>=(hbar nu/4)[Tr F_N/N]`.

One-sided:

`A_C^(2)+A_S^(2)>=(hbar nu/2)[Tr F_N/N]`.

Both are sharp in fixed-total-energy shells.

### WP19 — arbitrary coherent support

Canonical endpoint roles:

`Pi_out=supp(A A^dagger)`,

`Pi_in=supp(A^dagger A)`,

`G_ex=2hbar nu Q(Pi_out+Pi_in)Q`.

The mixed survival/synthesis bridge uses the audited shorted ceilings and `Psi_a` envelope.

### WP20 — multi-gap action sum

`C_Sigma>=sum_k[Z_(k,+)+Z_(k,-)]`,

`sum_k gamma_k Tr F_(N,k)/N <=4A_(G,Sigma)^(2)`.

Clean bilateral frequency weighting:

`A_(G,Sigma)^(2)>=sum_k(hbar nu_k/4)Tr F_(N,k)/N`.

A single Fourier measurement saturates the complete sum in the fixed-shell star construction.

## New active research: dynamical implementation cost

### WP21 — implementation coupling identity and lower bound

For a smooth unitary dilation of the encoded family with target support `P`, kernel `Q`, global baseline `Omega_0`, and tangent generators `K_j`,

`boxed:
Q partial_j^2 rho Q
=2 Tr_E[(Q⊗I)K_j Omega_0 K_j(Q⊗I)].`

For any positive kernel price `G`,

`boxed:
A_G^(2)
=(1/2)sum_j Tr[(G⊗I)K_j Omega_0 K_j].`

Thus the previously kinematic action is exactly a state-weighted squared dynamical coupling into the priced empty endpoint sectors.

For the clean exact-exchange single-gap geometry,

`boxed:
A_ex^(2)<=hbar nu [Var(K_x)+Var(K_y)].`

This is exactly sharp in the existing bilateral and one-sided fixed-total-energy extremizers.

The same models prove a no-go for ordinary net-energy accounting: total bare energy can remain exactly fixed while `A_ex`, generator variance, and temporal information are nonzero.

### WP22 — exact minimum energy-conserving tangent implementation

For a globally stationary pure-boundary exact exchange tangent, let `D_j` be either real quadrature derivative and define

`K_j^hor=i[Q D_j P rho_0^+ - rho_0^+ P D_j Q]`.

Then

`-i[K_j^hor,rho_0]=D_j`,

and

`[K_j^hor,H_C+H_S]=0`.

The horizontal generator variance is

`Var(K_j^hor)=H_jj^SLD/4`.

Therefore

`boxed:
V_min
=inf [Var(K_x)+Var(K_y)]
=(1/4)Tr H^SLD,`

and the infimum is attained by a target-only exact total-energy-conserving implementation.

The minimum compatible spectral action is

`boxed:
A_min^(2)=hbar nu V_min=(hbar nu/4)Tr H^SLD.`

Generic Bures/Uhlmann horizontal-lift minimization is prior art. The candidate new element is the exact energy-conserving relational realization and its equality to the frequency-resolved endpoint synthesis action.

## Current theorem target — full kernel 2-jet

The next question is now sharply defined:

> Given the first-order temporal tangent and a prescribed nonminimal target-kernel Hessian/action, what is the exact minimum generator/control cost over all energy-conserving Stinespring dilations?

Known:

`V_impl >= A_ex/(hbar nu)` from WP21.

At the minimal-curvature horizontal orbit:

`V_min=A_min/(hbar nu)` from WP22.

Promising construction: purify the baseline, realize the horizontal tangent in the baseline ancilla sector, and realize excess positive kernel curvature by coupling to an orthogonal ancilla flag sector so that the added coupling has zero first-order reduced signature but exactly the desired second-order population.

Candidate clean result:

`V_min(full kernel 2-jet)=A_ex/(hbar nu)`.

**This is not yet proved.** The remaining audit is whether the orthogonal-flag construction can always be imposed sector-by-sector while preserving exact total-energy conservation.

## Secondary future track — infinite-dimensional metrology

Do not start this until the dynamical 2-jet question is resolved or blocked.

A sensible infinite-dimensional program would proceed in stages:

1. discrete semibounded pure-point Hamiltonians with trace-class `rho_0` and unbounded `H`;
2. impose explicit domain conditions on `A`, `rho_0^+`, and energy-weighted endpoint operators;
3. prove finite-rank spectral truncation bounds uniform in cutoff;
4. pass to the limit by monotone convergence / closed quadratic forms;
5. only then address continuous spectra and Gaussian/CV families.

Continuous-variable Gaussian metrology already has mature QFI machinery, so novelty would have to come from extending the survival/synthesis resource law, not from generic Gaussian QFI formulas.

## Prior-art constraints

Do not claim novelty for:

- Bures/Uhlmann horizontal purification geometry;
- `QFI/4 = minimum purification speed`;
- generic quantum speed limits;
- integrated Hamiltonian/Frobenius/operator norm control cost;
- Tajima--Shiraishi--Saito external coherence cost under conservation laws;
- Marvian energetic-coherence formation cost;
- generic Gaussian/CV QFI formulas.

The candidate dynamical contribution is narrowly the **spectral endpoint-action / energy-conserving implementation-coupling bridge** for a relational mode whose total time-translation asymmetry can remain zero.

## Immediate work order

1. hostile proof audit WP21/WP22;
2. commit a dedicated WP22 random-matrix validator;
3. prove or kill the full kernel-2-jet equality candidate;
4. targeted prior-art search on constrained Bures horizontal lifts and endpoint-weighted Stinespring implementation;
5. only then decide whether the dynamical theorem belongs in the existing paper or a separate follow-up;
6. pursue infinite-dimensional extension afterward if still valuable.

## Documentation discipline

Every material theorem, proof repair, prior-art collision, or strategy change must be synchronized across `README.md`, `AGENTS.md`, this roadmap, and the relevant WP note. The repository is authoritative.