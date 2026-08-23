# WP17 — Operator/action Pareto redundancy no-go

**Date:** 2026-08-22

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** analytic NO-GO / scope clarification. The previously listed target of combining WP14's exact curvature-operator geometry with WP13's scalar spectral action does **not** define a new intrinsic resource theorem when both are derived from the same exact curvature operator. If the exact curvature is retained, the scalar action is redundant. If the curvature is discarded and only the scalar action is retained, optimization collapses exactly to the WP13 action-only law. A nontrivial Pareto problem requires an additional independent operator constraint not currently supplied by the physical model. This work package prevents an unnecessary sidequest.

## 1. Setup

WP12/WP14 retain the positive kernel curvature operator

`C_Delta>=Z_+ + Z_-`.

WP13 assigns one positive spectral cost operator `G>=0` and defines

`A_G^(2)=(1/4)Tr(G C_Delta)`.

A natural-looking next problem was to 'retain both' the full operator geometry and the scalar action in a joint Pareto theorem.

That sounds stronger, but with the present definitions it is not new information.

## 2. Exact curvature known: action is redundant

Suppose the exact physical curvature operator `C_Delta` is retained.

Then

`4 A_G^(2)=Tr(G C_Delta)`

is a deterministic linear functional of the already-known operator.

The WP12 feasible set is

`Z_+>=0`, `Z_->=0`,

`range(Z_+) subset R_+`,

`range(Z_-) subset R_-`,

`Z_+ + Z_- <= C_Delta`.

Adding the scalar condition

`Tr[G(Z_+ + Z_-)] <= Tr(G C_Delta)`

does not remove any feasible point, because it already follows from

`Z_+ + Z_- <= C_Delta`

and `G>=0`.

Therefore the exact WP12/WP14 operator allocation is unchanged.

> **No-go 1**
>
> Once exact `C_Delta` is retained, its scalar spectral action supplies no additional independent constraint.

## 3. Curvature discarded: action-only optimization collapses to WP13

Now discard `C_Delta` and keep only an action budget

`Tr(G C)<=e`

for some positive curvature `C` satisfying

`C>=Z_+ + Z_-`.

Because `G>=0`, every such feasible triple obeys

`Tr[G(Z_+ + Z_-)]<=e`.

Conversely, if a positive pair `(Z_+,Z_-)` satisfies

`Tr[G(Z_+ + Z_-)]<=e`,

then choosing

`C=Z_+ + Z_-`

makes it feasible.

Hence existence of an unspecified curvature with action at most `e` is **equivalent** to

> `boxed: Tr(G Z_+) + Tr(G Z_-) <= e`.

There is no residual WP14 overlap geometry because the curvature can always be chosen to equal the required sum.

## 4. Exact reduction to restricted minimum costs

Let

`g_+=lambda_min[R_+ G R_+ |_(R_+)]`,

`g_-=lambda_min[R_- G R_- |_(R_-)]`.

For positive support-constrained `Z_+/-`,

`Tr(G Z_+)>=g_+ Tr Z_+`,

`Tr(G Z_-)>=g_- Tr Z_-`.

Moreover these inequalities are individually attainable at the trace/cost level by concentrating each `Z` on a minimum-cost eigenvector of the corresponding restricted operator.

Therefore, when only scalar action is retained, the exact trace-feasible region is

`g_+ j_+ + g_- j_- <= e`,

`j_+,j_->=0`,

which is precisely the WP13 scalar action problem.

Thus the WP13 piecewise `Psi_a(e;g_+,g_-)` envelope is not merely a relaxation created by throwing away the curvature operator; it is the exact optimum over **all possible** positive curvatures consistent with the scalar action budget alone.

## 5. Consequence

There are two legitimate information regimes:

### Operator-resolved regime

Know `C_Delta`.

Use WP12/WP14.

The scalar action `Tr(G C_Delta)` is a derived reportable quantity but does not sharpen the feasible set.

### Action-only regime

Know only `e=Tr(G C_Delta)` or an upper bound on it.

Use WP13.

Optimizing over unknown curvature removes the matrix overlap geometry exactly.

There is no third intrinsic 'operator plus its own scalar action' regime.

## 6. When a genuine Pareto problem would exist

A nontrivial joint optimization requires **independent** information, for example:

- an operator envelope `C_Delta<=C_max` plus a separate action budget `Tr(G C_Delta)<=e`;
- a fixed curvature shape with variable scale and an independent power/action constraint;
- multiple non-proportional cost operators `G_1,G_2,...` with independent budgets;
- dynamical constraints that restrict which `C_Delta` can realize a given spectral action.

None of these is presently implied by the local kinematic model.

Introducing one merely to obtain a new mathematical Pareto theorem would be model invention rather than progress on the stated physical question.

## 7. Research decision

> **Killed direction:** do not pursue a generic WP14+WP13 Pareto theorem using only `C_Delta` and `Tr(G C_Delta)`.

The correct next high-value direction is the autonomous relational lift or a deeper class-level measurement-accessibility theorem.

This is exactly the kind of sidequest the project should eliminate early.
