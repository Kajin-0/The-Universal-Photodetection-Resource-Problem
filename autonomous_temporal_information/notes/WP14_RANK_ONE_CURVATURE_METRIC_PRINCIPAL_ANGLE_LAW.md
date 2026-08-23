# WP14 — Rank-one curvature-metric principal-angle law

**Date:** 2026-08-22

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** analytic PASS for the rank-one version of the WP12 operator allocation. For two one-dimensional synthesized ranges, the entire two-variable semidefinite feasible set and every linear allocation SDP admit closed analytic formulas after shorting the shared curvature to their span. The governing angle is the principal angle after whitening by the inverse shorted curvature, not the ordinary Hilbert-space angle. The nonlinear WP12 Fisher envelope is thereby reduced to a one-dimensional scalar minimization with an explicit piecewise integrand. Rank-one semidefinite packing, SOCP reductions, shorted operators, and generalized Schur-complement geometry are prior art; candidate novelty is the temporal-resource interpretation and the curvature-metric angle as the exact interference parameter. Priority remains **unverified, not certified**.

## 1. Problem

WP12 defines, for shared positive kernel curvature `C>=0`, synthesized output projectors `R_+,R_-`, and positive allocations,

`Z_+ + Z_- <= C`.

The linear inner problem is

`h_(alpha,beta)(C;R_+,R_-)`

`= max alpha Tr Z_+ + beta Tr Z_-`.

For general subspaces this is an SDP.

The roadmap asked whether the important two-rank-one case can be solved analytically and which principal angle controls the coupling.

It can.

## 2. Short first, then solve in two dimensions

Let

`R_+=|u><u|`,

`R_-=|v><v|`,

with normalized `|u>,|v>`.

Let

`S=span{u,v}`

and define the shorted curvature

> `C_S := Short_S(C)`.

Every candidate

`X=x|u><u|+y|v><v|`

has range in `S`. By the defining maximal property of the shorted operator,

`X<=C`

iff

`X<=C_S`.

Thus all curvature outside `S` can be removed exactly before optimization.

Assume first that `u,v` are independent and `C_S` is positive definite on `S`. Singular and collinear cases follow by the limits stated below.

## 3. Curvature-whitened geometry

Define

`A=<u|C_S^(-1)|u>`,

`B=<v|C_S^(-1)|v>`,

`m=<u|C_S^(-1)|v>`.

The one-direction shorted capacities are

> `s_u=1/A`,
>
> `s_v=1/B`.

Indeed,

`s_u |u><u| = Short_(span u)(C_S)`

and similarly for `v`.

Define

> `c := |m|/sqrt(A B)`.

Then

`0<=c<=1`.

Equivalently, if

`|a>=C_S^(-1/2)|u>`,

`|b>=C_S^(-1/2)|v>`,

then

> `c=|<a|b>|/(||a|| ||b||)`.

Thus `c` is the cosine of the principal angle **after whitening by the inverse shared curvature**.

It is generally not equal to the ordinary overlap `|<u|v>|`.

## 4. Exact feasible region

The constraint

`x|u><u|+y|v><v| <= C_S`

is equivalent, after congruence by `C_S^(-1/2)`, to

`x|a><a|+y|b><b| <= I_S`.

For two rank-one terms the determinant condition gives

`1-Ax-By+(AB-|m|^2)xy >=0`,

with

`0<=x<=s_u`,

`0<=y<=s_v`.

Since

`AB-|m|^2=AB(1-c^2)`,

the upper feasible boundary is

> **Rank-one curvature frontier**
>
> `boxed: y_max(x)`
>
> `= s_v [1-x/s_u]`
>
> `  / [1-(1-c^2)x/s_u]`,
>
> `0<=x<=s_u`.

This formula contains all coupling information.

### Limits

If `c=0`,

`y_max(x)=s_v`

for `0<=x<s_u`: the two allocations decouple in the whitened curvature metric.

If `c->1`,

`y_max(x)->s_v(1-x/s_u)`.

For genuinely identical rank-one subspaces, `u` and `v` are collinear, `s_u=s_v=s`, and this is simply

`x+y<=s`,

the shared-budget geometry used in WP12.

## 5. Exact linear allocation formula

Consider

`h_(alpha,beta)`

`=max alpha x + beta y`

subject to the rank-one feasible region, with `alpha,beta>0`.

Define

> `r := alpha s_u/(beta s_v)`.

For `0<c<1`, direct differentiation of

`alpha x+beta y_max(x)`

gives a single possible interior optimum.

The exact answer is

> **Closed rank-one linear allocation law**
>
> `boxed: h_(alpha,beta)=`
>
> `beta s_v`, if `r<=c^2`,
>
> `[alpha s_u + beta s_v`
>
> ` -2c sqrt(alpha beta s_u s_v)]/(1-c^2)`,
>
> `    if c^2<r<c^(-2)`,
>
> `alpha s_u`, if `r>=c^(-2)`.

The interior optimizer is

> `x_*=[s_u-c sqrt((beta/alpha)s_u s_v)]/(1-c^2)`,
>
> `y_*=[s_v-c sqrt((alpha/beta)s_u s_v)]/(1-c^2)`.

The endpoint formulas meet the interior formula continuously at

`r=c^2`

and

`r=c^(-2)`.

### Whitened-orthogonal limit

For `c=0`, the middle branch covers every finite positive `r` and reduces to

> `h_(alpha,beta)=alpha s_u+beta s_v`.

Both one-direction shorted capacities can be used simultaneously.

### Identical-subspace limit

For `c=1` and `R_+=R_-`,

> `h_(alpha,beta)=s max(alpha,beta)`,

which is exactly the WP12 shared scalar budget.

## 6. Derivation

Write

`D=AB-|m|^2`,

`K=|m|^2`.

The feasible boundary can also be written

`y(x)=(1-Ax)/(B-Dx)`.

Then

`d/dx [alpha x+beta y(x)]`

`= alpha - beta K/(B-Dx)^2`.

The second derivative is nonpositive for `D>=0`, so there is at most one interior maximum.

The stationary condition is

`B-Dx=sqrt(beta K/alpha)`.

Substitution gives the `x_*`,`y_*` above and

`h=[alpha B+beta A-2sqrt(alpha beta K)]/D`.

Replacing

`A=1/s_u`, `B=1/s_v`, `K=AB c^2`, `D=AB(1-c^2)`

gives the curvature-metric form in Sec. 5.

## 7. WP12 nonlinear Fisher envelope now contains no SDP

WP12 gives

`Phi_a(C;R_+,R_-)`

`= inf_(0<eta<1) {a/eta`

`+ h_(1/eta,1/(1-eta))(C;R_+,R_-)}`.

For rank-one `R_+,R_-`, Sec. 5 gives `h` explicitly.

Therefore

> `boxed: Phi_a`
>
> `= inf_(0<eta<1) {a/eta + H(eta;s_u,s_v,c)}`,

where `H` is the elementary piecewise function obtained from Sec. 5 with

`alpha=1/eta`,

`beta=1/(1-eta)`.

The SDP has disappeared completely. Only a one-dimensional scalar convex minimization remains.

The branch boundaries are determined by

`r(eta)=s_u(1-eta)/(s_v eta)`.

Thus the middle branch is active when

`c^2 < s_u(1-eta)/(s_v eta) < c^(-2)`.

This is already sufficient for stable analytic/numerical evaluation of every rank-one WP12 instance.

A compact closed radical formula for the final `eta` minimizer is not required for the theorem and is not claimed here.

## 8. Ordinary principal angle is insufficient

Take

`|u>=|0>`,

`|v>=(1/2)|0>+(sqrt(3)/2)|1>`.

Their ordinary Hilbert-space overlap is always

`|<u|v>|=1/2`.

But the curvature-metric overlap depends on `C_S`.

### Example 1

For

`C_S=diag(4,1)`,

`C_S^(-1)=diag(1/4,1)`.

One obtains

`c=1/sqrt(13)`

`approximately 0.27735`.

### Example 2

For

`C_S=diag(1/4,1)`,

`C_S^(-1)=diag(4,1)`.

One obtains

`c=2/sqrt(7)`

`approximately 0.75593`.

Thus the same physical pair of subspaces can range from nearly decoupled to strongly competing solely because the available curvature changes.

The allocation geometry is therefore **resource-metric**, not purely kinematic.

## 9. Relation to spectral action

WP13 replaces full `C` by a scalar positive action `Tr(GC)`. That coarse graining collapses the resource geometry to the restricted costs `g_+,g_-` and loses the curvature angle `c`.

WP14 shows exactly what is discarded:

- `s_u,s_v` are the independent shorted capacities;
- `c` quantifies how strongly those capacities compete for the same operator curvature;
- endpoint energy/action weighting can be applied afterward, but a single scalar action cannot generally reconstruct `c`.

Hence no scalar energy budget can be expected to reproduce the full WP12 operator allocation for arbitrary overlapping rank-one ranges.

This is not a defect of WP13. WP13 is the sharp theorem after intentionally compressing the resource to one scalar spectral action; WP14 quantifies the matrix information lost in that compression.

## 10. Prior-art boundary

Do not claim novelty for:

- shorted operators or generalized Schur complements;
- congruence whitening of positive matrix inequalities;
- rank-one semidefinite packing;
- SOCP reductions of rank-one SDPs;
- principal-angle geometry in weighted inner products.

Relevant established work includes Guillaume Sagnol, **A class of semidefinite programs with rank-one solutions**, Linear Algebra and its Applications 435, 1446--1463 (2011), DOI `10.1016/j.laa.2011.03.027`, which treats rank-one semidefinite packing/SOCP structure, and the Anderson--Trapp shorted-operator literature.

The candidate project contribution is limited to the temporal-information resource statement:

> when two synthesized temporal score directions compete for the same second-order kernel curvature, their exact rank-one resource coupling is controlled by a principal angle in the **inverse shorted-curvature metric**, and this angle determines the sharp allocation entering the arbitrary-POVM Fisher bound.

Priority remains **unverified, not certified**.

## 11. Consequence for significance

WP14 sharpens an important conceptual point.

A scalar resource law can be exact in clean orthogonal or identical-endpoint limits, but in the generic overlapping case the local temporal-information resource has at least three independent rank-one invariants:

`(s_u,s_v,c)`.

Two scalar endpoint capacities alone are insufficient.

The need for a matrix-valued curvature resource is therefore not merely an artifact of high-dimensional examples; it already appears in the smallest nontrivial two-direction allocation problem.

## 12. Next work

Highest-value next targets:

1. test whether the remaining WP12 shared-kernel Fisher gap is exactly accounted for by Holevo compatibility;
2. combine the WP14 curvature angle with WP13 endpoint spectral costs in a two-resource Pareto law retaining both operator overlap and energy action;
3. lift the operator/action resource simultaneously to clock and signal sides of a globally stationary exchange;
4. test Gaussian covariance-changing families;
5. deepen prior-art verification before any manuscript draft.
