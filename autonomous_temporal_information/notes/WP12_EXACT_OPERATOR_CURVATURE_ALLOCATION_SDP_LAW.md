# WP12 — Exact operator curvature-allocation law and SDP representation

**Date:** 2026-08-22

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** analytic PASS for the exact optimization implied by the second-order kernel-curvature constraint and the WP09/WP11 measurement-side Minkowski geometry. The result removes WP11's double counting of the same curvature operator, gives an exact one-dimensional variational representation with a semidefinite-program dual, and yields closed forms in one-sided and identical-subspace limits. Generic attainability by a single quantum measurement is **not** claimed; this work package sharpens the resource-allocation layer. SDP duality, minimax theory, and shorted operators are prior art. Priority remains **unverified, not certified**.

## 1. Loose step left by WP11

WP11 established the exact operator constraint

`C_Delta >= Z_+ + Z_-`,

where

`C_Delta=Q(partial_x^2 rho+partial_y^2 rho)Q`,

`Z_+=K_+ rho0^+ K_+^dagger`,

`Z_-=K_- rho0^+ K_-^dagger`.

The measurement-side law contains

`[sqrt(a+Tr Z_+) + sqrt(Tr Z_-)]^2`,

where `a` is the internal/support-preserving weighted tangent norm in the chosen orientation.

WP11 then bounded `Tr Z_+` and `Tr Z_-` separately using endpoint-weighted scalar curvatures. That is rigorous but can count the same positive operator `C_Delta` twice.

The correct resource problem is therefore a **joint positive-operator allocation**.

## 2. Curvature-allocation feasible set

Let `C>=0` be a finite-dimensional positive operator and let `R_+,R_-` be orthogonal projectors onto the information-bearing synthesized output subspaces.

Define

`A(C;R_+,R_-)`

as the set of pairs `(Z_+,Z_-)` satisfying

- `Z_+>=0`, `Z_->=0`;
- `Z_+=R_+ Z_+ R_+`;
- `Z_-=R_- Z_- R_-`;
- `Z_+ + Z_- <= C`.

For the physical problem, take

`C=C_Delta`,

`R_+=supp(K_+ rho0^+ K_+^dagger)`,

`R_-=supp(K_- rho0^+ K_-^dagger)`.

The actual tangent-generated pair `(Z_+,Z_-)` belongs to this set by the WP07/WP11 second-order PSD-cone theorem.

## 3. Exact allocation functional

For any internal nonnegative resource `a>=0`, define

> `Phi_a(C;R_+,R_-)`
>
> `= sup_(Z_+,Z_- in A(C;R_+,R_-))`
>
> `  [sqrt(a+Tr Z_+) + sqrt(Tr Z_-)]^2`.

This is the **tightest consequence of the kernel-curvature operator constraint alone** for the WP11 upper-oriented measurement functional.

Because the actual `(Z_+,Z_-)` is feasible,

> `boxed: [sqrt(a+J_+) + sqrt(J_-)]^2`
>
> `<= Phi_a(C_Delta;R_+,R_-)`.

The conjugate orientation uses

`Phi_b(C_Delta;R_-,R_+)`

with the lower-oriented internal norm `b`.

## 4. Variational identity for the square-root objective

For `u,v>=0`,

`(sqrt(u)+sqrt(v))^2`

`= inf_(0<eta<1) [u/eta + v/(1-eta)]`.

The minimizing value is

`eta=sqrt(u)/(sqrt(u)+sqrt(v))`

with the obvious boundary limits when one term vanishes.

Therefore

`Phi_a`

`= sup_Z inf_eta { (a+Tr Z_+)/eta + Tr Z_-/(1-eta) }`.

The feasible set is compact and convex; for fixed `eta` the expression is affine in `(Z_+,Z_-)`, and for fixed operators it is convex in `eta`. Applying the standard convex-concave minimax theorem (or first restricting `eta` to `[delta,1-delta]` and then taking `delta->0`) gives

> **Exact one-dimensional variational representation**
>
> `boxed: Phi_a(C;R_+,R_-)`
>
> `= inf_(0<eta<1) { a/eta`
>
> `+ h_(1/eta,1/(1-eta))(C;R_+,R_-) }`,

where `h_(alpha,beta)` is the linear allocation problem below.

## 5. Linear allocation SDP

For positive weights `alpha,beta`, define

`h_(alpha,beta)(C;R_+,R_-)`

`= max alpha Tr Z_+ + beta Tr Z_-`

subject to

`(Z_+,Z_-) in A(C;R_+,R_-)`.

This is a semidefinite program.

### Dual

Introduce a positive dual operator `W>=0` for

`C-Z_+-Z_- >=0`.

The support-constrained positive variables have finite Lagrangian supremum iff

`R_+ W R_+ >= alpha R_+`,

`R_- W R_- >= beta R_-`.

Hence the dual is

> `boxed: h_(alpha,beta)`
>
> `= min_(W>=0) Tr(CW)`
>
> subject to
>
> `R_+ W R_+ >= alpha R_+`,
>
> `R_- W R_- >= beta R_-`.

Strict dual feasibility follows from `W=tI` with `t>max(alpha,beta)`, so standard finite-dimensional SDP strong duality applies.

Consequently `Phi_a` is exactly a **one-dimensional outer minimization over an SDP value**.

No heuristic allocation remains.

## 6. Shorted-operator one-orientation limit

Suppose `R_-=0`.

Then the objective becomes

`a+Tr Z_+`.

The Anderson--Trapp shorted operator

`Short_(R_+)(C)`

is the largest positive operator below `C` whose range lies in `R_+`.

Therefore

> `boxed: Phi_a(C;R_+,0)`
>
> `= a + Tr Short_(R_+)(C)`.

Thus the exact one-sided curvature resource is not merely an endpoint-weighted scalar bound; it is the trace of the **shorted curvature operator**.

For a clean baseline-empty energy endpoint where `R_+` is itself the endpoint sector and the curvature is supported there, this reduces to WP07/WP10:

`Tr Short_(R_+)(C)=Delta T_syn`.

## 7. Separate shorts give a rigorous but generally loose bound

Define

`s_+=Tr Short_(R_+)(C)`,

`s_-=Tr Short_(R_-)(C)`.

Every feasible allocation satisfies

`Tr Z_+<=s_+`,

`Tr Z_-<=s_-`.

Hence

> `Phi_a(C;R_+,R_-)`
>
> `<= [sqrt(a+s_+)+sqrt(s_-)]^2`.

This is the operator-short analogue of WP11's separate scalar charging.

Moreover, in the endpoint-weighted WP11 notation,

`s_+ <= Gamma_U/mu_U`,

`s_- <= Gamma_D/mu_D`.

Indeed, `Short_(R_+)(C)<=C`; multiplying by `W_U>=0` and using `W_U>=mu_U R_+` on the shorted range gives

`Gamma_U=Tr(W_U C)`

`>=Tr[W_U Short_(R_+)(C)]`

`>=mu_U s_+`.

Thus WP12 is never weaker than the separate WP11 synthesis reduction when the full curvature operator is retained.

## 8. Exact identical-subspace solution

Now suppose

`R_+=R_-=R`.

Let

`s=Tr Short_R(C)`.

Any feasible sum

`T=Z_++Z_-`

has range in `R` and satisfies `T<=C`, so

`T<=Short_R(C)`

and

`Tr Z_+ + Tr Z_- <= s`.

Conversely, every scalar pair

`j_+,j_->=0`, `j_++j_-<=s`

is achievable at the trace-allocation level by taking a suitable scalar multiple of `Short_R(C)` and splitting it proportionally between the two orientations.

Therefore

`Phi_a(C;R,R)`

reduces exactly to

`max_(0<=j<=s) [sqrt(a+j)+sqrt(s-j)]^2`.

The stationary point is

`j_*=(s-a)/2`.

Hence:

> **Exact coincident-subspace law**
>
> `boxed: Phi_a(C;R,R)=`
>
> `(sqrt(a)+sqrt(s))^2`, if `s<=a`,
>
> `2(a+s)`, if `s>=a`.

The function and its first derivative are continuous at `s=a`.

This identifies a clean crossover:

- weak shared synthesis resource: all curvature is optimally assigned to the opposite orientation and the law is ordinary Minkowski;
- strong shared synthesis resource: the optimal allocation balances the two score amplitudes, giving the factor `2(a+s)`.

For `a=0`,

> `boxed: Phi_0(C;R,R)=2s`.

Thus the factor-of-two bilateral enhancement is the universal coincident-subspace curvature-allocation coefficient.

## 9. Decoupled orthogonal-subspace limit

Suppose

`R_+ R_-=0`

and `C` is block diagonal with respect to

`R_+ directsum R_- directsum (R_++R_-)^perp`.

Then the allocations decouple. Let

`s_+=Tr Short_(R_+)(C)`,

`s_-=Tr Short_(R_-)(C)`.

One obtains

> `boxed: Phi_a(C;R_+,R_-)`
>
> `=[sqrt(a+s_+)+sqrt(s_-)]^2`.

This is the clean WP09/WP10 composition rule.

If `C` has cross-block coherence between `R_+` and `R_-`, the exact SDP can be strictly smaller than this separate-short expression. The operator law therefore captures information discarded by endpoint trace curvatures alone.

## 10. WP12 master Fisher bound

Return to the physical tangent of WP11.

The exact measurement-side bounds are

`sqrt[Tr F_N/N]`

`<= sqrt(J_B^+ + J_+) + sqrt(J_-)`,

and, from the conjugate orientation,

`sqrt[Tr F_N/N]`

`<= sqrt(J_B^- + J_-) + sqrt(J_+)`.

Since `(Z_+,Z_-)` is feasible for `C_Delta`,

> `boxed: Tr F_N/N`
>
> `<= min{`
>
> `Phi_(J_B^+)(C_Delta;R_+,R_-),`
>
> `Phi_(J_B^-)(C_Delta;R_-,R_+)`
>
> `}`.

If one wants a theorem expressed only through pre-existing resource ceilings, use any bounds

`J_B^+<=a_U`,

`J_B^-<=a_D`.

Because `Phi_a` is monotone in `a`,

> `boxed: Tr F_N/N`
>
> `<= min{`
>
> `Phi_(a_U)(C_Delta;R_+,R_-),`
>
> `Phi_(a_D)(C_Delta;R_-,R_+)`
>
> `}`.

For the WP11 spectral reductions one may take

`a_U=4T_U/(R_B^2 lambda_U)`,

`a_D=4T_D/(R_B^2 lambda_D)`.

This gives a strictly sharpened noncommuting-support resource law while retaining the exact endpoint geometry already established in WP11.

## 11. Exact rank-one-kernel benchmark

The coincident-subspace case occurs naturally when the baseline kernel is one dimensional and both orientations are present.

Take

`H=hbar omega diag(0,1,2)`

and

`|q>=(1/2)|0> + sqrt(5/8)|1> + [1/(2sqrt(2))]|2>`.

Let

`P=I-|q><q|`,

`rho0=P/2`.

Choose the exact `+omega` tangent

`A=|1><0| - sqrt(2)|2><1|`.

The condition

`<q|A|q>=0`

holds exactly, so

`Q A Q=0`

and the tangent is first-order compatible with the rank-two support.

A direct calculation gives, in the upper-oriented decomposition,

`J_B^+=5/4`,

`J_+=7/4`,

`J_-=3`.

Both synthesized weighted operators have range equal to the same rank-one kernel projector `Q`.

For the minimal kernel curvature

`C_Delta=Z_++Z_-`,

`Short_Q(C_Delta)=C_Delta`

and

`s=Tr C_Delta=19/4`.

Since `s>a=5/4`, the coincident-subspace formula gives

`Phi_a=2(a+s)=12`.

The **actual abstract WP11 weighted-norm expression** is also

`[sqrt(a+J_+)+sqrt(J_-)]^2`

`=[sqrt(3)+sqrt(3)]^2`

`=12`.

Thus the allocation theorem is exactly saturated at the weighted-tangent resource layer.

By contrast, separately charging the same shorted curvature to both orientations would give

`[sqrt(a+s)+sqrt(s)]^2`

`approximately 21.427`.

The exact allocation law therefore lowers this benchmark ceiling by about

`43.996%`.

The SLD-QFI trace for this particular two-parameter model is `10.75`, so the remaining difference between `12` and physically attainable common-record Fisher information is measurement-compatibility geometry, not resource double counting. WP12 deliberately does not claim to solve that separate multiparameter attainability problem.

## 12. Relation to prior art

The following are established and not novelty claims:

- Anderson--Trapp/Krein shorted operators;
- parallel addition of positive operators;
- semidefinite programming and strong duality;
- convex-concave minimax theorems;
- the scalar identity representing `(sqrt(u)+sqrt(v))^2` as a weighted quadratic infimum;
- multiparameter QFI/Holevo compatibility theory.

Candidate novelty is restricted to the temporal-information statement:

> the exact second-order curvature required by a support-changing temporal tangent is a **shared operator resource**, and the sharp arbitrary-POVM resource ceiling induced by the WP11 score geometry is obtained by an operator allocation SDP rather than independent endpoint curvature charges.

Targeted searches have not identified this combined frequency-resolved statement. Priority remains **unverified, not certified**.

## 13. Consequence for the grand program

The local resource picture is now naturally operator-valued.

- baseline interior information is controlled by a positive support-weighted tangent operator;
- boundary synthesis is controlled by a positive kernel-curvature operator;
- opposite temporal orientations compete for the **same** curvature through a semidefinite allocation constraint;
- endpoint energy tails are scalar corollaries obtained by projecting/shorting these operators against energy subspaces.

This is conceptually cleaner than treating survival probability, tangent radius, and curvature as unrelated scalar corrections.

## 14. Next work

Highest-value next targets:

1. incorporate the energy endpoint contractions `W_U,W_D` directly inside the allocation SDP so that the optimized object is a positive **spectral-energy synthesis action**, not only total kernel curvature;
2. derive a dual formulation in which endpoint energy weights appear as operator costs;
3. solve rank-one `R_+,R_-` with arbitrary principal angle in closed form;
4. test whether the WP12 allocation plus a Holevo-compatible measurement bound can close the remaining `12` versus `10.75` gap in the rank-one-kernel benchmark;
5. lift the operator allocation to both clock and signal sides of a globally stationary relational exchange;
6. perform a deeper priority audit before any manuscript formation.
