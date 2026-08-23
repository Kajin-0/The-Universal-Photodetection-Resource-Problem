# WP11 — Shorted-endpoint master law for noncommuting baseline support

**Date:** 2026-08-22

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** analytic PASS as a general finite-copy arbitrary-POVM upper bound for an exact-gap tangent at an arbitrary rank-deficient coherent baseline, with explicit support/endpoint geometry. The bound reduces exactly to WP06, WP07, WP09, and WP10 in their clean limits. A four-level exact-gap construction proves that a principal-angle/shorting correction is genuinely necessary: omitting it produces a false Fisher-resource inequality. Generic global sharpness of the full master bound is **not** claimed. Priority remains **unverified, not certified**.

## 1. Problem left by WP10

WP10 solved the mixed finite-radius + synthesis problem under

`[P,H]=0`,

where

`P=supp(rho0)`.

That condition lets the support-projected pieces of an exact Bohr-gap operator remain exact Bohr-gap pieces, and the pre-existing and synthesized upper endpoint sectors remain orthogonal spectral subspaces.

The genuinely autonomous/history-state regime need not satisfy this condition. A coherent baseline can have

`[P,H] != 0`.

Then even if the **full** tangent `A_nu` satisfies

`[H,A_nu]=hbar nu A_nu`,

the support pieces

`P A_nu P`, `Q A_nu P`, `P A_nu Q`

need not separately be exact-gap operators.

Therefore the WP10 resource reduction cannot simply be reused term by term.

WP11 identifies the missing geometry and gives a universal finite-dimensional master bound.

## 2. Full tangent decomposition remains valid

Let

`P=supp(rho0)`,

`Q=I-P`.

For a two-sided differentiable physical two-quadrature family, first-order positivity gives

`Q A_nu Q=0`.

Define

`B=P A_nu P`,

`K_+=Q A_nu P`,

`K_-=Q A_nu^dagger P`.

Then

> `A_nu=B+K_+ + K_-^dagger`.

The three pieces have a support interpretation:

- `B`: support-preserving/internal component;
- `K_+`: support-to-kernel component in the positive-gap orientation;
- `K_-`: support-to-kernel component in the conjugate/lower orientation.

They are not assumed to be independent Bohr modes after support projection.

## 3. Weighted tangent norms

Define

`Z_B^+=B rho0^+ B^dagger`,

`Z_B^-=B^dagger rho0^+ B`,

`Z_+=K_+ rho0^+ K_+^dagger`,

`Z_-=K_- rho0^+ K_-^dagger`.

Let

`J_B^+=Tr Z_B^+`,

`J_B^-=Tr Z_B^-`,

`J_+=Tr Z_+`,

`J_-=Tr Z_-`.

Because `B` and `K_+` have orthogonal output support,

`Tr[(B+K_+)rho0^+(B+K_+)^dagger]=J_B^+ + J_+`.

The opposite orientation analog is

`J_B^-+J_-`.

## 4. Measurement-side master inequality

WP09's score-space argument applies without any commutation assumption.

For one copy,

`sqrt(Tr F_1) <= sqrt(J_B^+ + J_+) + sqrt(J_-)`.

Applying the same argument to `A_nu^dagger` gives the conjugate bound

`sqrt(Tr F_1) <= sqrt(J_B^- + J_-) + sqrt(J_+)`.

For `N` independently encoded copies, all four weighted norms scale exactly by `N`; cross-copy terms vanish because `Tr A_nu=0`, hence `Tr B=0` and the support-to-kernel pieces are traceless.

Therefore, for every finite `N` and every arbitrary entangled collective POVM,

> **Abstract mixed-support master law**
>
> `boxed: sqrt[Tr F_N/N]`
>
> `<= min{`
>
> `sqrt(J_B^+ + J_+) + sqrt(J_-),`
>
> `sqrt(J_B^- + J_-) + sqrt(J_+)`
>
> `}`.

The remaining task is to reduce these four tangent norms to physical endpoint resources when `P` and the energy projectors do not commute.

## 5. Participating energy endpoint projectors

Let `Pi_U` and `Pi_D` be energy spectral projectors containing the participating upper and lower endpoints of the exact positive-gap operator, chosen so that

`A_nu=Pi_U A_nu Pi_D`.

For a semibounded exact gap `nu`, `Pi_U` lies in the energy tail at least `hbar nu` above the relevant lower edge.

Define the baseline endpoint populations

`T_U=Tr(Pi_U rho0)`,

`T_D=Tr(Pi_D rho0)`.

Because `rho0=P rho0 P`, these can also be written using the support compressions

`S_U=P Pi_U P`,

`S_D=P Pi_D P`:

`T_U=Tr(S_U rho0)`,

`T_D=Tr(S_D rho0)`.

The positive contractions `S_U,S_D` encode the principal-angle geometry between the baseline support and the endpoint energy subspaces.

## 6. Shorting constants for the internal component

Let

`R_B^+=supp(Z_B^+)`,

`R_B^-=supp(Z_B^-)`

be the support projectors of the two internal weighted tangent operators.

Define the **upper and lower support-shortening constants**

`lambda_U=sup{lambda>=0 : S_U >= lambda R_B^+}`,

`lambda_D=sup{lambda>=0 : S_D >= lambda R_B^-}`.

If the corresponding internal tangent norm vanishes, the associated term is defined to be zero and no positive constant is required.

These constants are finite-dimensional generalized principal-angle/shorted-operator quantities. Equivalently, they are the largest scalar multiples of the information-bearing output projectors that fit below the compressed endpoint operators.

This is directly connected to the classical Krein--Anderson--Trapp shorted-operator construction

`Short_R(S)=max{X>=0 : X<=S, range(X) subseteq range(R)}`.

No novelty is claimed for shorted operators or their principal-angle interpretation.

## 7. Internal robust-tail bound with noncommuting support

Let `R_B` be the physical linear tangent radius of the support-preserving complex sub-tangent `B`:

`R_B=1/w(rho0^(-1/2) B rho0^(-1/2))`.

As in WP02/WP06,

`Z_B^+ <= (4/R_B^2) rho0`,

`Z_B^- <= (4/R_B^2) rho0`.

Because `Z_B^+` is supported in `R_B^+`,

`J_B^+ <= (4/R_B^2) Tr(R_B^+ rho0)`.

But

`S_U >= lambda_U R_B^+`,

so

`T_U=Tr(S_U rho0) >= lambda_U Tr(R_B^+ rho0)`.

Hence

> `boxed: J_B^+ <= 4 T_U/(R_B^2 lambda_U)`.

Likewise

> `boxed: J_B^- <= 4 T_D/(R_B^2 lambda_D)`.

When the internal component is itself a genuine support-preserving exact endpoint map, its output lies in `P cap Pi_U` (or the lower analog), and the corresponding shorting constant is exactly `1`. Thus WP06 is recovered without penalty.

When the support only intersects the endpoint obliquely, `lambda<1`; the penalty is physically necessary, as Sec. 12 demonstrates.

## 8. Kernel curvature operator

Let the exact physical family be `C^2` in the two quadratures and define

`C_Delta=Q[partial_x^2 rho(0)+partial_y^2 rho(0)]Q`.

Second-order PSD-cone geometry gives

`C_Delta >= Z_+ + Z_-`.

This is the operator form of the WP07/WP09 quadratic synthesis requirement.

The endpoint projectors no longer restrict to clean kernel subspaces. Instead define the positive kernel-side endpoint contractions

`W_U=Q Pi_U Q`,

`W_D=Q Pi_D Q`.

These encode the principal angles between the kernel and the endpoint energy sectors.

## 9. Shorting constants for synthesized components

Let

`R_+=supp(Z_+)`,

`R_-=supp(Z_-)`.

Define

`mu_U=sup{mu>=0 : W_U >= mu R_+}`,

`mu_D=sup{mu>=0 : W_D >= mu R_-}`.

Define the positive endpoint-weighted kernel curvatures

`Gamma_U=Tr(W_U C_Delta)`,

`Gamma_D=Tr(W_D C_Delta)`.

Since

`C_Delta>=Z_++Z_- >= Z_+`

and `W_U>=0`,

`Gamma_U>=Tr(W_U Z_+)`.

Since `W_U>=mu_U R_+` and `Z_+` is supported on `R_+`,

`Tr(W_U Z_+)>=mu_U Tr Z_+=mu_U J_+`.

Therefore

> `boxed: J_+ <= Gamma_U/mu_U`.

Similarly

> `boxed: J_- <= Gamma_D/mu_D`.

When a synthesized endpoint lies entirely in the baseline kernel, `W_U` or `W_D` acts as the identity on that endpoint and the corresponding `mu=1`; the bound reduces exactly to WP07/WP09 endpoint population curvature.

## 10. General shorted-endpoint master resource law

Define

`B_U=4 T_U/(R_B^2 lambda_U)`,

`B_D=4 T_D/(R_B^2 lambda_D)`,

`S_U=Gamma_U/mu_U`,

`S_D=Gamma_D/mu_D`,

with absent components assigned zero.

Then every finite `N` and every arbitrary joint POVM obeys

> **Shorted-endpoint master law**
>
> `boxed: Tr F_N/N`
>
> `<= min{`
>
> `[sqrt(B_U+S_U)+sqrt(S_D)]^2,`
>
> `[sqrt(B_D+S_D)+sqrt(S_U)]^2`
>
> `}`.

This is a universal scalar consequence of an underlying operator geometry. It is not claimed to be globally sharp for arbitrary noncommuting supports because `Gamma_U` and `Gamma_D` can count overlapping kernel curvature.

Its significance is that it remains finite-copy, arbitrary-POVM, frequency-endpoint resolved, and reduces exactly to all previously solved limiting regimes.

## 11. Exact reductions

### WP06 — finite-radius pre-existing tangent

If `K_+=K_-=0`, then `A_nu=B` is support preserving. Its upper/lower weighted tangent supports lie in the true endpoint intersections, so

`lambda_U=lambda_D=1`.

The master law reduces to

`Tr F_N/N <= min{4T_U/R_B^2,4T_D/R_B^2}`,

the WP02/WP06 support-sensitive robust tail law.

### WP07 — one-sided zero-radius synthesis

If `B=K_-=0` and the upper endpoint is baseline empty, then

`mu_U=1`,

`Gamma_U=Delta T_U`,

so

`Tr F_N/N <= Delta T_U`.

### WP09 — bilateral zero-radius synthesis

If `B=0` and the upper/lower synthesized endpoint sectors are baseline-empty and orthogonal, then

`mu_U=mu_D=1`,

`Gamma_U=Delta T_+`,

`Gamma_D=Delta T_-`,

and the master law becomes exactly

`Tr F_N/N <= [sqrt(Delta T_+)+sqrt(Delta T_-)]^2`.

### WP10 — one-sided mixed commuting support

If `[P,H]=0` and `K_-=0`, then the pre-existing and synthesized upper sectors are genuine orthogonal energy subspaces,

`lambda_U=mu_U=1`,

and

`Tr F_N/N <= 4T_pre/R_B^2 + Delta T_syn`.

Thus WP10 is recovered exactly.

## 12. Principal-angle correction is necessary: exact counterexample

A naive extension of WP10 might try to keep the same pre-existing term

`4T_U/R_B^2`

when `[P,H]!=0`.

That is false.

Take a four-level equally spaced Hamiltonian

`H=hbar omega diag(0,1,2,3)`

and exact positive gap

`nu=2 omega`.

Let

`|r>=(1/2)|2>+(sqrt(3)/2)|3>`,

`|q>=(sqrt(3)/2)|2>-(1/2)|3>`.

Choose baseline

`rho0=(1/2)|0><0|+(1/2)|r><r|`.

Thus

`P=|0><0|+|r><r|`

and `[P,H]!=0`.

Let

`A_nu=|2><0|`.

This is an exact `+2omega` Bohr-gap operator and is right-supported on the baseline because `|0>` lies in `P`.

Using

`|2>=(1/2)|r>+(sqrt(3)/2)|q>`,

we obtain

`B=(1/2)|r><0|`,

`K_+=(sqrt(3)/2)|q><0|`,

`K_-=0`.

The weighted tangent norms are

`J_B^+=1/2`,

`J_+=3/2`,

so the exact measurement-side ceiling is

`J_B^+ + J_+=2`.

### Naive internal endpoint term fails by factor four

The participating upper endpoint is

`Pi_U=|2><2|`.

The baseline endpoint population is

`T_U=Tr(Pi_U rho0)=1/8`.

For

`B=(1/2)|r><0|`

with equal baseline support weights, the internal tangent radius is

`R_B^2=4`.

A naive WP10 continuation would give

`4T_U/R_B^2=1/8`.

But the actual internal weighted tangent norm is

`J_B^+=1/2`.

Thus the naive resource term undercounts by exactly factor four.

### Shorting constant repairs it exactly

Here

`S_U=P Pi_U P=(1/4)|r><r|`.

The information-bearing internal output projector is

`R_B^+=|r><r|`.

Therefore

`lambda_U=1/4`.

The corrected theorem gives

`4T_U/(R_B^2 lambda_U)`

`=4(1/8)/(4 x 1/4)`

`=1/2`

`=J_B^+`.

The principal-angle/shorting coefficient is therefore exact in this noncommuting example.

### Kernel coefficient is also exact

On the kernel direction `|q>`,

`W_U=Q Pi_U Q=(3/4)|q><q|`,

so

`mu_U=3/4`.

For the minimal physical curvature supplied by the congruence family, the endpoint-weighted kernel curvature satisfies

`Gamma_U=(3/4)J_+`.

Hence

`Gamma_U/mu_U=J_+=3/2`.

Both geometric corrections are exact.

## 13. The missing geometric factor causes an actual Fisher violation

The preceding failure is not merely a failure to bound an intermediate norm.

For the same model, the naive total one-sided resource ceiling obtained by omitting `lambda_U` but retaining the exact synthesis contribution is

`1/8 + 3/2 = 13/8`.

Now consider the two real quadratures separately. For either one, the scalar SLD quantum Fisher information is

`F_Q,scalar`

`=(1/2)^2 + [(sqrt(3)/2)^2]/(1/2)`

`=1/4+3/2`

`=7/4`.

For a single scalar parameter, an SLD-optimal local measurement exists and attains this value.

Construct one fixed POVM by classical randomization:

- with probability `1/2`, perform the locally optimal measurement for the cosine quadrature and retain the measurement-choice label;
- with probability `1/2`, perform the locally optimal measurement for the sine quadrature and retain the label.

Classical randomization of POVMs gives the average Fisher matrices. Therefore the trace of this one fixed one-copy POVM is at least

`(1/2)(7/4)+(1/2)(7/4)=7/4`.

But

`7/4 > 13/8`.

Hence the naive no-geometry resource bound is **operationally false**.

The shorted-endpoint correction is required for observable Fisher information.

## 14. Exact physical family for the counterexample

The tangent is realized by the same normalized congruence construction used in WP10.

Since

`rho0^+|0>=2|0>`,

set

`G=(1/2)A_nu rho0^+=|2><0|`.

For `z=x-i y`, define

`M(z)=I+zG`,

`rho(x,y)=M(z)rho0M(z)^dagger / Tr[M(z)rho0M(z)^dagger]`.

This family is positive by construction and has complex tangent exactly `A_nu` at the origin.

Thus the counterexample does not rely on a formally admissible but unrealizable derivative.

## 15. Prior-art boundary

The following ingredients are established and are not novelty claims:

- Krein/Anderson--Trapp shorted operators and generalized Schur complements;
- principal angles between subspaces;
- PSD-cone second-order tangent geometry;
- numerical radius bounds;
- SLD scalar quantum Fisher information and one-parameter attainability;
- classical randomization/convex combination of POVMs;
- score-space Minkowski inequalities.

The candidate contribution is the **frequency-resolved temporal-information synthesis of these ingredients**:

1. exact-gap arbitrary-POVM Fisher information at a noncommuting coherent baseline;
2. endpoint-support shorting constants that repair the finite-radius spectral-tail term;
3. kernel-endpoint shorting constants that repair quadratic synthesis curvature;
4. one master law reducing exactly to WP06/WP07/WP09/WP10;
5. an explicit exact-gap Fisher counterexample showing the geometric correction is necessary.

Targeted searches have not identified this combined statement. Priority remains **unverified, not certified**.

## 16. Consequence for the grand program

The main local nonlinear/support loophole is now substantially closed.

The resource is not always a single scalar energy tail. At coherent noncommuting baselines, the correct local resource includes **how the information-bearing tangent sits geometrically relative to the energy endpoint subspaces**.

The hierarchy is therefore:

`temporal Fisher strength`

`<=`

`pre-existing spectral support x robustness x endpoint-overlap geometry`

`+ / Minkowski-composed quadratic endpoint synthesis`.

In the commuting limits the geometric constants become one and all earlier simpler laws are recovered.

## 17. Next work

Highest-value next targets:

1. determine whether the full WP11 master bound can be sharpened by retaining the Anderson--Trapp shorted operators themselves rather than only scalar shorting constants;
2. derive the optimal joint allocation of overlapping kernel curvature between `K_+` and `K_-` instead of separately upper-bounding both with `Gamma_U,Gamma_D`;
3. test whether the resulting operator formulation has an exact variational/SDP expression and sharp low-dimensional extremizers;
4. lift the shorted-endpoint geometry to an autonomous clock--signal bipartition and determine whether both local sides acquire matching geometric penalties;
5. perform a deep priority audit against shorted-operator matrix analysis, singular quantum estimation, and quantitative reference-frame/WAY theory;
6. only after those gates, reassess manuscript formation.
