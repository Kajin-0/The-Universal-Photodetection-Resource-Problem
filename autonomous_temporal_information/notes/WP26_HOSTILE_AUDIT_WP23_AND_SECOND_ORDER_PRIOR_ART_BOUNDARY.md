# WP26 — Hostile audit of WP23 and second-order prior-art boundary

## Verdict

**WP23 mathematical audit: PASS.**

No defect was found in the lower bound, orthogonal-flag construction, prescribed kernel-Laplacian equality, or exact energy-shell realization.

The theorem must remain narrowly stated as a finite-dimensional **metric-contracted target-kernel 2-jet** result. It does not solve an arbitrary tensor-valued second-order interpolation problem and does not identify generator variance with thermodynamic work.

Priority remains unverified.

## 1. Lower-bound audit

Let `Omega_0` be any global baseline reducing to `rho_0`, with target support projector `P=supp(rho_0)` and kernel `Q=I-P`.

Since `Tr[(Q⊗I)Omega_0]=Tr(Q rho_0)=0` and `Omega_0>=0`, positivity gives

`Omega_0=(P⊗I)Omega_0(P⊗I)`.

For one Hermitian tangent generator `K`, define

`A=(P⊗I)K(P⊗I)`,

`B=(Q⊗I)K(P⊗I)`.

Then on the support of `Omega_0`,

`(P⊗I)K^2(P⊗I)=A^2+B^dagger B`.

Also

`Tr(Omega_0 K)=Tr(Omega_0 A)`.

Therefore

`Var_Omega(K)
 = [Tr(Omega_0 A^2)-Tr(Omega_0 A)^2]
   +Tr(Omega_0 B^dagger B)`

`=Var_Omega(A)+Tr(Omega_0 B^dagger B)`.

Both terms are nonnegative.

WP21 gives

`Tr[Q partial_j^2 rho Q]
 =2 Tr(Omega_0 B_j^dagger B_j)`.

Hence

`Var_Omega(K_j)>= (1/2)Tr[Q partial_j^2 rho Q]`.

Summing coordinates gives

`boxed: V_impl >= (1/2)Tr C_Delta.`

No commutativity or purity assumption is used in this lower bound.

Equality requires the support-block generator variance to vanish. The WP23 construction sets the relevant support block to zero on the baseline purification orbit, so the equality condition is achievable.

## 2. Feasibility audit

For each real derivative `D_j`, two-sided `C^2` positivity at a rank-deficient baseline requires

`Q partial_j^2 rho Q >= 2 QD_jP rho_0^+ P D_jQ`.

Summing gives

`C_Delta>=C_min`,

`C_min=2 sum_j QD_jP rho_0^+ P D_jQ`.

Thus `C_Delta>=C_min` is necessary for the metric-contracted kernel 2-jet.

WP23 proves sufficiency **for this contracted kernel datum** by explicit unitary dilation. It does not prove that every separately prescribed tensor `Q partial_i partial_j rho Q` satisfying some naive block inequalities is jointly realizable. Mixed-Hessian compatibility is deliberately outside scope.

## 3. Horizontal part audit

Take an energy-adapted purification

`|Omega>=sum_a sqrt(lambda_a)|a>_T|a>_E`.

For

`K_j^hor=i(QD_jP rho_0^+ - rho_0^+ P D_jQ)`,

let

`|chi_j^hor>=-i(K_j^hor⊗I)|Omega>`.

Directly,

`Tr_E(|chi_j^hor><Omega|+h.c.)=D_j`.

Also

`2 Tr_E[Q|chi_j^hor><chi_j^hor|Q]
 =2 QD_jP rho_0^+ P D_jQ
 =C_j^min`.

The horizontal norm is

`||chi_j^hor||^2=(1/4)H_jj^SLD=(1/2)Tr C_j^min`.

Thus the horizontal component realizes exactly the minimum first-order-compatible kernel curvature and no more.

## 4. Orthogonal-flag invisibility audit

Let

`S=(C_Delta-C_min)/2>=0`.

Choose a purification `|eta>` in `Q⊗E_flag` with

`Tr_Eflag |eta><eta|=S`.

Require `E_flag` to be orthogonal to every ancilla state used by `|Omega>` and the horizontal vectors.

Then exactly

`Tr_E(|eta><Omega|)=0`,

so adding `eta` to a tangent vector changes no first derivative.

Likewise

`Tr_E(|eta><chi_j^hor|)=0`,

so there are no horizontal/flag cross terms in the reduced kernel curvature.

Therefore with

`chi_x=chi_x^hor+eta`, `chi_y=chi_y^hor`,

one gets

`2 sum_j Tr_E[Q|chi_j><chi_j|Q]
 =C_min+2S=C_Delta`

exactly.

The added squared norm is

`||eta||^2=Tr S`.

Hence

`sum_j ||chi_j||^2
 =(1/2)Tr C_min+Tr S
 =(1/2)Tr C_Delta`.

There is no hidden cross-term cost.

## 5. Generator construction audit

Because every `chi_j` is orthogonal to `Omega`, define

`K_j=i(|chi_j><Omega|-|Omega><chi_j|)`

on the span of `Omega,chi_j`, with zero extension sufficient elsewhere.

Then

`K_j=K_j^dagger`,

`-iK_j|Omega>=|chi_j>`,

`<Omega|K_j|Omega>=0`,

and

`Var_Omega(K_j)=||chi_j||^2`.

The pure global unitary orbit

`U(x,y)=exp[-i(xK_x+yK_y)]`

therefore has exactly the required first derivatives and target kernel Laplacian.

The noncommutativity of `K_x,K_y` affects the mixed derivative `partial_x partial_y rho`, but not the separately defined `partial_x^2+partial_y^2` kernel Laplacian. This is precisely why WP23 must not be advertised as a full tensor-valued 2-jet theorem.

## 6. Exact energy-shell audit

Assume

`[rho_0,H_T]=0`, `[D_j,H_T]=0`, `[C_Delta,H_T]=0`.

Choose support eigenvectors jointly diagonalizing `rho_0,H_T` and a constant `E_*` at least as large as every target energy appearing in the finite-dimensional construction.

For each baseline Schmidt flag associated with target energy `E`, choose ancilla energy `E_*-E`. Then every term of `|Omega>` has total energy `E_*`.

Since `D_j` preserves target energy, the horizontal `chi_j^hor` use the same ancilla flags and also lie at total energy `E_*`.

Since `S` commutes with `H_T`, it is block diagonal in target-energy sectors. Diagonalize/purify each sector separately using fresh flag states of ancilla energy `E_*-E`. Thus `eta` also lies entirely in the same global shell.

Consequently `Omega` and all `chi_j` are eigenvectors of `H_tot=H_T+H_E` with the same eigenvalue. The rank-two generators built from them satisfy

`[K_j,H_tot]=0`.

Hence the complete two-parameter unitary satisfies

`[U(x,y),H_tot]=0`

for all local parameters, not merely at first order.

No external time-translation asymmetry is needed.

## 7. Clean endpoint-action equality

When the entire prescribed kernel curvature lies in the clean single-gap endpoint sector on which

`G_ex=2hbar nu Q`,

`A_ex=(1/4)Tr(G_ex C_Delta)
     =(hbar nu/2)Tr C_Delta`.

Together with the exact variational minimum,

`boxed: V_min=(1/2)Tr C_Delta=A_ex/(hbar nu).`

If there are spectator kernel sectors not priced by `G_ex`, this equality need not hold for the **total** unweighted generator variance. The generic weighted identity of WP21 remains exact, but WP23's simple `A_ex/(hbar nu)` equality must retain the clean endpoint-support hypothesis.

## 8. Prior-art search result

Targeted searches were performed for combinations of:

- second-order quantum statistical tangent / 2-jet;
- prescribed density-matrix Hessian and purification;
- second-order Stinespring dilation interpolation;
- Bures second fundamental form;
- non-faithful-state purification/geodesics;
- minimum generator norm with prescribed second derivative.

No direct predecessor of the WP23 statement was located in this search.

Important nearby prior art:

1. **Bures/Uhlmann horizontal geometry.** The first-order minimum `Tr H_SLD/4` is established and must not be claimed.
2. **Safranek, PRA 95, 052320 (2017).** Rank-changing Bures/QFI corrections explicitly involve second derivatives of zero eigenvalues. This is close conceptually to the kernel Hessian but does not provide the WP23 minimum-dilation construction.
3. **Carrasco & Spehner, arXiv:2606.06759 (2026).** Explicit Bures geodesics for non-faithful states and quantum-speed-limit consequences. Again, this strengthens the prior-art boundary around first-order/geodesic minimal motion, but the inspected abstract/results do not state a prescribed nonminimal kernel-Hessian implementation minimum.
4. General Stinespring/purification theory supplies the dilation language but no matching second-order constrained variational theorem was found in the targeted search.

Absence from this search is **not** priority certification.

## 9. Significance assessment after audit

WP23 materially resolves the statement that the manuscript's action is 'purely kinematic' in the clean boundary setting:

- the action is an exact weighted unitary-coupling quadratic form (WP21);
- its minimum first-order value is the energy-conserving horizontal cost (WP22);
- arbitrary prescribed excess kernel curvature has exactly additive minimum dilation cost (WP23).

The remaining limitation is narrower: this is generator-variance/control-action cost, not thermodynamic work including switching, controller preparation, battery depletion, and reset.

## 10. Next step

The next theorem should address the other major physical idealization: approximate rather than exact exchange in the **zero-radius synthesis regime**. WP25 already handles approximate gaps at finite radius. A successful boundary analogue would make the core paper substantially less idealized.
