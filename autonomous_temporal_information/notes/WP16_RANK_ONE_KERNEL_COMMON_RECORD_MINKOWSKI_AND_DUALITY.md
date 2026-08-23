# WP16 — Rank-one-kernel common-record Minkowski law and exact Fisher-witness duality

**Date:** 2026-08-22

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** analytic PASS for a class-level one-copy arbitrary-POVM theorem at maximally mixed rank-`r` support with one-dimensional kernel. The result gives (i) an exact convex-dual characterization of accessible common-record Fisher information by quadratic operator witnesses; (ii) a sharp universal Minkowski decomposition into regular support information and singular boundary coupling; (iii) an explicit qutrit numerical-radius corollary; and (iv) a simple qutrit extremizer proving the Minkowski coefficient sharp and the naive additive compatibility law false by factor `9/5`. The same two scalar invariants do not determine the exact optimum, so an additional phase/orientation geometry survives at the measurement layer. Convex POVM duality, generalized moment problems, numerical radius, and Ando block-matrix characterizations are prior art; candidate novelty is restricted to this rank-changing temporal-information application. Priority remains **unverified, not certified**.

## 1. General rank-one-kernel model

Let

`rho0=P/r`,

where `P` is a rank-`r` projector, and let

`Q=|q><q|=I-P`

be one dimensional.

For a two-sided physical two-quadrature tangent, first-order positivity implies

`Q A Q=0`.

In the decomposition

`H=P H directsum span{|q>}`,

write

> `A=[[B,b],[a^dagger,0]]`.

Here

- `B=PAP` is the regular support tangent;
- `b=PA|q>`;
- `a=PA^dagger|q>`;
- the lower-left block is `a^dagger=<q|AP`.

For an arbitrary POVM `{M_y}`, with

`p_y=Tr(rho0 M_y)`,

`z_y=Tr(A M_y)`,

the two-quadrature Fisher trace is

`Tr F_1=sum_(p_y>0) |z_y|^2/p_y`.

WP16 concerns the exact optimization and universal upper structure of this quantity.

## 2. Rank-one refinement

For a positive effect decomposed as

`M=sum_j M_j`,

quadratic-over-linear convexity gives

`|sum_j z_j|^2/(sum_j p_j) <= sum_j |z_j|^2/p_j`.

Therefore rank-one refinement cannot decrease `Tr F_1`.

It is enough to study effects

`M_y=w_y |phi_y><phi_y|`.

Write a normalized vector as

`|phi>=s|u>+t|q>`,

where

`|u> in P`, `||u||=1`, `s>=0`, `s^2+|t|^2=1`.

Then

`p=s^2/r`

and

`<phi|A|phi>`

`=s^2 <u|B|u>`

` +s[t<u|b>+t^*<a|u>]`.

Define

`beta(u)=<u|B|u>`,

`d(u,t)=t<u|b>+t^*<a|u>`.

The contribution of this effect is

> `w r |s beta(u)+d(u,t)|^2`.

This decomposition is the measurement-compatibility analog of the WP09 score decomposition.

## 3. Exact singular boundary invariant

Define

> `kappa=max_(||u||=1, |tau|=1)`
>
> `      |tau<u|b>+tau^*<a|u>|^2`.

The phase can be absorbed into `u`; maximizing the remaining modulus gives

> `boxed: kappa=||a||^2+||b||^2+2|a^dagger b|`.

Proof: for any scalar phase `theta`,

`max_(||u||=1) Re{e^(-i theta)[<u|b>+<a|u>]}`

`=||e^(-i theta)b+e^(i theta)a||`.

Maximizing the squared norm over `theta` gives the stated formula.

For a vector approaching the kernel,

`|phi_epsilon>=sqrt(1-epsilon^2)|q>+epsilon |u>`,

one has

`p_epsilon=epsilon^2/r`

and hence

`limsup_(epsilon->0) |<phi_epsilon|A|phi_epsilon>|^2/p_epsilon`

`<= r kappa`.

Equality is attained along a maximizing direction.

Thus `r kappa` is the exact singular one-outcome boundary ceiling.

## 4. Regular support common-record functional

Define the support-only accessible Fisher functional

> `R(B)`
>
> `=sup_(POVM {N_j} on P)`
>
> ` r sum_j |Tr(B N_j)|^2/Tr(N_j)`.

Equivalently, for rank-one support effects

`N_j=w_j |u_j><u_j|`, `sum_j N_j=P`,

`R(B)=r sum_j w_j |<u_j|B|u_j>|^2`.

This is the exact common-record Fisher optimum for the support model with baseline `P/r` and complex tangent `B`.

It is deliberately kept as an operational functional for general `r`; ordinary numerical radius alone need not determine it in higher support dimension.

## 5. Sharp regular-plus-singular Minkowski theorem

For the full rank-one POVM define outcome-space amplitudes

`alpha_y=sqrt(r w_y) s_y beta(u_y)`,

`delta_y=sqrt(r w_y) d(u_y,t_y)`.

Then

`Tr F_1=||alpha+delta||_2^2`.

### Regular norm

The support blocks of POVM completeness satisfy

`sum_y w_y s_y^2 |u_y><u_y|=P`.

Therefore

`||alpha||_2^2`

`=r sum_y w_y s_y^2 |beta(u_y)|^2`

`<=R(B)`.

### Singular norm

By the definition of `kappa`,

`|d(u_y,t_y)|^2<=|t_y|^2 kappa`.

The kernel block of POVM completeness gives

`sum_y w_y |t_y|^2=1`.

Hence

`||delta||_2^2<=r kappa`.

Applying the Hilbert-space triangle inequality in outcome-score space gives

> **Rank-one-kernel common-record Minkowski law**
>
> `boxed: sqrt(Tr F_1)`
>
> `<=sqrt(R(B))+sqrt(r kappa)`.

Equivalently,

> `boxed: Tr F_1`
>
> `<= [sqrt(R(B))+sqrt(r kappa)]^2`.

This holds for every arbitrary one-copy POVM.

The cross term is genuine measurement compatibility. It cannot be replaced universally by ordinary addition.

## 6. Explicit qutrit corollary

Now let `r=2`, so the total Hilbert-space dimension is three.

Because `Tr A=0` and `QAQ=0`,

`Tr B=0`.

For any traceless `2 x 2` matrix `B`, if `|u>` attains the numerical radius

`w(B)=max_(||u||=1)|<u|B|u>|`,

its orthogonal complement `|u_perp>` satisfies

`<u_perp|B|u_perp>=-<u|B|u>`.

Thus the orthonormal projective measurement `{|u>,|u_perp>}` attains the support upper bound

`R(B)=4 w(B)^2`.

Hence every rank-one-kernel qutrit obeys

> **Explicit qutrit common-record law**
>
> `boxed: Tr F_1 <= [2 w(B)+sqrt(2 kappa)]^2`.

No SLD/Holevo attainability assumption enters this theorem.

## 7. Exact extremizer: signed three-cycle

Take

`rho0=diag(1/2,1/2,0)`

and

> `A_cyc=[[0,1,0],`
>
> `       [0,0,-1],`
>
> `       [1,0,0]]`.

Then

`B=[[0,1],[0,0]]`,

`a=(1,0)^T`,

`b=(0,-1)^T`.

The support numerical radius is

`w(B)=1/2`,

so

`R(B)=1`.

Also

`a^dagger b=0`,

`kappa=||a||^2+||b||^2=2`,

and therefore

`r kappa=4`.

The WP16 theorem gives

`Tr F_1 <= (1+2)^2=9`.

But `A_cyc` is unitary and satisfies

`A_cyc^3=-I`.

Its three orthonormal eigenvectors have equal coordinate magnitudes `1/sqrt(3)`. For the spectral projective measurement,

`p_j=1/3`

and

`|<v_j|A_cyc|v_j>|=1`

for every outcome.

Thus

`Tr F_1=3 x (1/(1/3))=9`.

Therefore

> `boxed: sup_POVM Tr F_1=9`

for this model, and the Minkowski coefficient is exactly sharp.

## 8. Naive additive compatibility is false by factor 9/5

The tempting additive conjecture would be

`Tr F_1 <= R(B)+r kappa`.

For the signed three-cycle this predicts

`Tr F_1<=1+4=5`.

The exact optimum is `9`.

Hence

> `boxed: additive regular+singular compatibility is false}`

with violation factor

> `9/5=1.8`.

This is distinct from WP09's factor-two resource-allocation failure: WP16 concerns **measurement-accessibility score interference** after the physical tangent has already been fixed.

## 9. The two scalar invariants are not sufficient for exact optimization

The sharp universal bound depends only on `R(B)` and `kappa`, but these two numbers do not determine the model-specific optimum.

Keep the same

`B=[[0,1],[0,0]]`,

so `R(B)=1`, and instead choose

`a=(sqrt(2),0)^T`,

`b=0`.

Then again

`kappa=2`.

Thus this model has exactly the same pair

`(R(B),r kappa)=(1,4)`

as the signed three-cycle.

However it is one-sided in support orientation. The WP11 weighted-tangent inequality reduces to

`Tr F_1 <= J_B^+ + J_+`.

With `rho0^+=2P`,

`J_B^+=2 Tr(BB^dagger)=2`,

`J_+=2||a||^2=4`.

Therefore

> `boxed: Tr F_1<=6<9`.

So two models with identical `R(B)` and `kappa` have provably different common-record optima.

Consequently an additional phase/orientation invariant is irreducible if one wants the **exact** accessible Fisher value rather than the sharp universal two-scalar envelope.

WP15's off-diagonal quadratic witness is one manifestation of this missing geometry.

## 10. Exact arbitrary-POVM Fisher-witness duality

The preceding bound is universal but not generally exact. There is, however, an exact convex-dual characterization.

For normalized `|phi>` with

`p(phi)=<phi|rho0|phi>>0`,

define

`f(phi)=|<phi|A|phi>|^2/p(phi)`.

At the kernel vector, define the upper-semicontinuous extension

`f_sharp(q)=r kappa`.

The near-kernel calculation in Sec. 3 shows

`limsup_(phi->q) f(phi)<=f_sharp(q)`,

with equality along an optimizing direction.

The relaxed rank-one POVM problem is a compact generalized moment problem. Its exact dual is

> **Fisher-witness dual**
>
> `boxed: F_CR(rho0,A)`
>
> `=inf_(Y=Y^dagger) Tr Y`
>
> subject to
>
> `boxed: |<phi|A|phi>|^2`
>
> `<=<phi|rho0|phi><phi|Y|phi>`
>
> for every vector `|phi>`.

Here `F_CR` denotes the physical POVM **supremum**. If the relaxed optimizer places weight on the kernel vector, replace that vector by an optimizing near-kernel direction and frame-normalize the finite ensemble; this produces ordinary POVMs whose values converge to the relaxed optimum. Thus no zero-probability Fisher convention is introduced.

Strong duality follows from the standard finite-dimensional moment/POVM separation argument: the upper-semicontinuous compactified pure-state payoff is bounded, the frame constraint is finite dimensional, and a sufficiently large multiple of the identity is a strict dual majorant.

This is standard convex-duality machinery, not a novelty claim.

WP15's `Y` with `Tr Y=55/8` is an explicit optimal dual witness for one nontrivial model.

## 11. Equivalent semi-infinite LMI / generalized numerical-radius form

The quadratic witness inequality is equivalent to an operator family.

For every `lambda>0` and every phase `theta`, require

> `boxed: lambda rho0 + lambda^(-1)Y`
>
> `>= e^(i theta)A+e^(-i theta)A^dagger`.

Indeed, evaluating this on a vector gives

`lambda p+lambda^(-1)y>=2 Re[e^(i theta)z]`.

Taking the supremum over `theta` and then the infimum over `lambda` yields

`|z|^2<=p y`.

Conversely the product inequality plus scalar AM--GM gives the LMI for all `lambda,theta`.

When

`R_lambda=lambda rho0+lambda^(-1)Y`

is positive definite, the phase family is equivalent to

> `w(R_lambda^(-1/2) A R_lambda^(-1/2))<=1/2`.

Thus the exact common-record Fisher dual is a **generalized weighted numerical-radius majorization problem**.

For fixed `lambda`, Ando's classical numerical-radius theorem can further rewrite this as positivity of a `2 x 2` operator block matrix with an auxiliary Hermitian contraction. Ando/numerical-radius block positivity is prior art; the remaining continuum over `lambda` reflects the quadratic-over-linear Fisher denominator.

## 12. Relation to WP11 and WP15

WP11 controls the tangent by support orientation before optimizing measurement compatibility.

WP16 instead decomposes the **measurement score vector itself** into

- a regular support contribution;
- a singular near-kernel contribution.

The resulting bounds are complementary.

For the signed three-cycle, WP16 is exact while the orientation-based WP11 bound is looser.

For the one-sided comparison model, WP11 gives `6` while the WP16 two-scalar envelope gives `9`.

For the WP15 shared-kernel benchmark, the WP16 envelope is also substantially above the exact `55/8`; the benchmark-specific optimal quadratic witness exploits orientation information discarded by `R(B)` and `kappa`.

The best practical generic one-copy bound should therefore take the minimum of:

1. the WP11 orientation-sensitive weighted-tangent bound;
2. the WP16 regular/singular Minkowski bound;
3. any explicitly constructed Fisher-witness dual certificate.

## 13. Prior-art boundary

Do not claim novelty for:

- convex duality of POVM optimization;
- generalized moment-problem duality;
- numerical range/radius;
- Ando's block-matrix characterization of numerical radius;
- quadratic-over-linear convexity;
- Hilbert-space Minkowski inequality;
- Gill--Massar/Holevo/Fisher-symmetric measurement compatibility theory.

Relevant operator literature includes the classical Ando numerical-radius theorem and modern expositions such as Bhatia and Jain, *The numerical radius and positivity of block matrices*, Linear Algebra Appl. **656**, 463--482 (2023), DOI `10.1016/j.laa.2022.10.009`.

Candidate contribution is restricted to the rank-changing temporal-information statement that accessible two-quadrature Fisher information has a sharp **regular-support plus singular-boundary Minkowski geometry**, together with the explicit demonstration that scalar regular and singular capacities do not determine the exact common-record optimum.

Priority remains unverified.

## 14. Next work

Highest-value next targets:

1. identify the missing phase/orientation invariant that interpolates between the signed-cycle saturation `9`, the one-sided ceiling `6`, and the WP15 exact value `55/8`;
2. determine whether the Fisher-witness dual admits a finite SDP for rank-two support via Ando/Fejer--Riesz elimination of the `lambda,theta` continuum;
3. combine the WP14 operator-curvature angle and WP13 spectral action with this measurement-accessibility geometry;
4. lift the complete resource-plus-accessibility hierarchy to both sides of an autonomous clock--signal exchange;
5. perform a hostile priority/significance audit before manuscript formation.
