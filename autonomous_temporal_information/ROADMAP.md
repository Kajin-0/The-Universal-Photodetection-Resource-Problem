# Roadmap — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

## Goal

Develop and publish a rigorously scoped resource law for autonomous temporal information, then close the most important physical limitations: dynamical implementation cost, exact-resonance robustness, and ultimately infinite-dimensional systems.

The frozen Rev11 random-time paper remains untouched on its parent branch. The PRX Quantum R3 manuscript on this branch is also **science-frozen** while the new results below undergo proof and prior-art audits.

## Publication state

The theorem program through WP20 has passed the internal manuscript gates.

- Significance/literature gate: **PROVISIONAL PASS** for a narrow theorem paper.
- Hostile mathematical gate through WP20: **PASS**.
- PRX Quantum R3 manuscript: build-verified and standalone.
- Priority: **unverified, not certified**.

Research was explicitly reopened on 2026-08-23. The active research frontier is now **WP21–WP25**.

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

The mixed survival/synthesis bridge uses shorted internal ceilings and the audited `Psi_a` envelope.

### WP20 — multi-gap action sum

`C_Sigma>=sum_k[Z_(k,+)+Z_(k,-)]`,

`sum_k gamma_k Tr F_(N,k)/N <=4A_(G,Sigma)^(2)`.

Clean bilateral weighting:

`A_(G,Sigma)^(2)>=sum_k(hbar nu_k/4)Tr F_(N,k)/N`.

A single Fourier measurement saturates the complete sum in the fixed-shell star construction.

R3 also includes the clean pure-boundary SLD-QFI corollary

`A_C^(2)+A_S^(2)>=(hbar nu/4)Tr H_SLD`

and a spectator-curvature no-go separating first-order temporal tangent information from arbitrary independent second-order Bures curvature.

## WP21 — exact unitary implementation coupling identity

For a smooth unitary dilation with target support `P`, kernel `Q`, global baseline `Omega_0`, and tangent generator `K_j`,

`Q partial_j^2 rho Q
 =2 Tr_E[(Q⊗I)K_j Omega_0 K_j(Q⊗I)].`

For positive kernel price `G`,

`A_G^(2)
 =(1/2)sum_j Tr[(G⊗I)K_j Omega_0 K_j].`

Thus the kinematic action is exactly a weighted squared dynamical coupling into the priced empty sectors.

For the clean exact-exchange single-gap geometry,

`A_ex^(2)<=hbar nu [Var(K_x)+Var(K_y)].`

The coefficient is sharp. Net bare-energy change cannot be the universal resource because the sharp examples remain in one fixed total-energy shell.

## WP22 — exact minimum first-order implementation cost

For each pure-boundary real derivative `D_j`,

`K_j^hor=i(QD_jP rho_0^+ - rho_0^+ P D_jQ)`

realizes

`-i[K_j^hor,rho_0]=D_j`

and, for an exact relational tangent,

`[K_j^hor,H_C+H_S]=0`.

The exact minimum over all smooth unitary implementations is

`boxed: V_min=(1/4)Tr H_SLD`,

and it is attained by a target-only exact total-energy-conserving implementation.

Minimum clean endpoint action:

`boxed: A_min=hbar nu V_min=(hbar nu/4)Tr H_SLD.`

The generic Bures/Uhlmann horizontal-lift identity is prior art; only the constrained autonomous spectral specialization is a candidate new contribution.

## WP23 — exact minimum for a prescribed kernel 2-jet

This closes the principal dynamical question left by WP21/WP22.

Define

`C_min=2 sum_j QD_jP rho_0^+ P D_jQ`.

For any prescribed feasible globally stationary kernel Laplacian

`C_Delta>=C_min`, `[C_Delta,H_T]=0`,

every unitary dilation obeys

`V_impl >= (1/2)Tr C_Delta`.

Write the excess as

`S=(C_Delta-C_min)/2>=0`.

Purify `S` into an ancilla flag sector orthogonal to the baseline purification. The flag adds exactly the desired second-order target population while contributing zero first-order reduced tangent. Assign the flag energy sector-by-sector so baseline, horizontal tangent vectors, and excess-curvature flags all lie in one global energy shell.

Therefore

`boxed: inf V_impl=(1/2)Tr C_Delta`

and the same infimum is achieved within the exactly total-energy-conserving class.

In the clean single-gap endpoint geometry, where `G_ex=2hbar nu Q` on the prescribed kernel curvature,

`boxed: V_min(full metric-contracted kernel 2-jet)=A_ex^(2)/(hbar nu)`.

This is the strongest current dynamical result.

Validator:

`numerics/verify_wp23_prescribed_2jet_implementation_cost.py`.

## WP24 — external-critique mathematical audit

### Mixed `Psi_a` envelope

Independently re-derived from

`max (sqrt u+sqrt v)^2`

subject to

`p u+q v=e+pa`, `u>=a`, `v>=0`.

The exact result is

`Psi_a=(sqrt a+sqrt(e/q))^2` for `e<=a p^2/q`,

`Psi_a=(e+pa)(1/p+1/q)` for `e>=a p^2/q`.

No defect was found. The qutrit benchmark gives exactly `12`.

Validator:

`numerics/verify_wp24_psi_envelope.py`.

### Classical nonregular-statistics boundary

The mere existence of nonregular behavior at a probability/support boundary is established classical statistics and is **not a quantum novelty claim**.

Future manuscript positioning should cite at minimum:

- Chernoff (1954);
- Shapiro (1985);
- Self & Liang (1987).

The quantum candidate contribution is the noncommutative PSD-cone support-to-kernel coherence structure, exact spectral pricing, autonomous clock-signal exchange, and the dynamical endpoint-action theorem.

## WP25 — approximate Bohr-gap robustness

This attacks the exact-commutator idealization in the finite-radius stationary regime.

For

`R_nu=[H,A]-hbar nu A`,

`eta_nu^2=Tr(R_nu rho_0^+ R_nu^dagger)`,

and every `0<delta<nu`,

`boxed:
(R_lin^2/4)[Tr F_N^tan/N]
 <= T(nu-delta)
   +R_lin^2 eta_nu^2/(4hbar^2 delta^2).`

The proof splits the tangent into near-resonant matrix elements, paid by a lower spectral tail, and off-resonant leakage, paid by the weighted commutator residual.

The exact-gap theorem is recovered as the residual vanishes.

A locally energy-stationary autonomous pair obeys the corresponding minimum of the clock and signal leakage-corrected tails.

Validator:

`numerics/verify_wp25_approximate_gap_robustness.py`.

## Prior-art constraints

Do not claim novelty for:

- Bures/Uhlmann horizontal purification geometry;
- `QFI/4 = minimum purification speed`;
- generic quantum-speed-limit or Hamiltonian-norm control bounds;
- generic classical boundary/nonregular asymptotics;
- numerical-radius, PSD-cone, shorted-operator, Cauchy–Schwarz, or ellipse-optimization mathematics;
- generic modes-of-asymmetry/Page–Wootters theory.

Important current neighbor:

- Carrasco & Spehner, arXiv:2606.06759 (2026): Bures geodesics for non-faithful states and QSL consequences. This further removes any plausible novelty claim for the first-order Bures horizontal geometry.

The narrow WP23 candidate is the **prescribed second-order kernel-jet completion with an exactly energy-conserving endpoint-action implementation**. Priority is unverified.

## Current theorem target — approximate zero-radius synthesis

The most valuable next physical question is now:

> Does the rank-changing synthesis/action theorem remain quantitatively stable when the intended exact clock-signal exchange has detuning or off-resonant leakage?

A successful theorem should distinguish:

1. near-resonant support-to-kernel tangent components that are charged by approximately correct endpoint sectors;
2. off-resonant tangent components controlled by commutator residuals;
3. second-order kernel population needed for positivity;
4. possible leakage into spectator sectors.

This would remove the strongest remaining exact-resonance idealization from the paper's headline boundary regime.

## Infinite-dimensional track — next after approximate boundary robustness

Proceed in stages:

1. separable Hilbert space, trace-class `rho_0`, semibounded pure-point `H`;
2. bounded relative tangent `B=rho_0^{-1/2}A rho_0^{-1/2}` or an explicitly closed quadratic-form analogue;
3. finite spectral truncations with cutoff-independent inequalities;
4. monotone convergence / closed-form limits;
5. only then continuous spectra and unbounded generators;
6. treat Gaussian/CV covariance-changing families as a separate specialization.

Do not begin with unrestricted continuous-variable models.

## Immediate work order

1. hostile proof audit WP23, especially the variance decomposition, flag invisibility, prescribed curvature equality, and energy-shell construction;
2. targeted prior-art search for second-order constrained Stinespring/purification interpolation;
3. audit WP25 against approximate eigenoperator/Bohr-mode leakage literature;
4. prove or kill an approximate-gap **zero-radius synthesis/action** theorem;
5. then attack the staged infinite-dimensional extension;
6. only after these pass decide whether the manuscript merits an R4 or whether WP21–WP25 belong in a follow-up paper.

## Documentation discipline

Every material theorem, proof repair, prior-art collision, or strategy change must be synchronized across `README.md`, `AGENTS.md`, this roadmap, and the relevant WP note. The repository is authoritative.