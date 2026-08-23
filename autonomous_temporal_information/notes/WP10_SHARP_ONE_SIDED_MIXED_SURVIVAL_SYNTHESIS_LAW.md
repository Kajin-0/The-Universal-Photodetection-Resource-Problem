# WP10 — Sharp one-sided mixed survival+synthesis law

**Date:** 2026-08-22

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** analytic PASS for an energy-invariant baseline support with a finite-radius pre-existing exact-gap component plus one-sided support-to-kernel synthesis. The finite-copy arbitrary-POVM coefficient is sharp, and one qutrit family simultaneously saturates the pre-existing tail term, the quadratic synthesis term, and the total information law. This is the first exact bridge between the WP06 finite-radius and WP07 zero-radius regimes. Priority remains **unverified, not certified**.

## 1. Why this mixed sector matters

WP06 controls a support-preserving finite-radius tangent by pre-existing spectral population.

WP07 controls a support-to-kernel zero-radius tangent by second-order spectral population synthesis.

WP09 showed that if both **opposite** endpoint orientations are synthesized, their score amplitudes can interfere and the sharp resource law becomes Minkowski/square-root rather than additive.

Before attacking a fully coherent noncommuting support, there is a cleaner mixed problem:

> one exact positive-gap tangent contains both a support-preserving component and a newly synthesized **upper** endpoint, but no lower-endpoint synthesis.

In this orientation the two pieces are both right-supported on the baseline support and their output subspaces are orthogonal. The weighted tangent norm therefore adds quadratically rather than by Minkowski.

The result is a sharp additive bridge between pre-existing survival and quadratic synthesis.

## 2. Assumptions and exact-gap decomposition

Let `rho0` be an arbitrary density operator with support projector

`P=supp(rho0)`,

`Q=I-P`.

Let `H` be a semibounded Hamiltonian and assume the support is energy invariant:

`[P,H]=0`.

Let `A_nu` be an exact positive-gap complex tangent,

`[H,A_nu]=hbar nu A_nu`, `nu>0`,

with two Hermitian quadratures

`D_c=(A_nu+A_nu^dagger)/2`,

`D_s=(A_nu-A_nu^dagger)/(2i)`.

Assume **one-sided upper synthesis**:

`P A_nu Q=0`.

Equivalently, the positive-gap operator is right-supported on the baseline support:

`A_nu=A_nu P`.

Decompose

`B=P A_nu P`,

`K=Q A_nu P`.

Then

`A_nu=B+K`.

Because `[P,H]=0`, both pieces remain exact `+nu` gap operators:

`[H,B]=hbar nu B`,

`[H,K]=hbar nu K`.

Let `P_U` denote the participating upper endpoint energy projector. Since `P` commutes with `H`, it also commutes with `P_U`. Define

`P_U,pre=P_U P`,

`P_U,syn=P_U Q`.

These are orthogonal spectral sectors.

`B` lands in `P_U,pre`, while `K` lands in the baseline-empty sector `P_U,syn`.

## 3. Weighted tangent norms

Define

`J_B=Tr(B rho0^+ B^dagger)`,

`J_K=Tr(K rho0^+ K^dagger)`.

Because the ranges of `B` and `K` lie in orthogonal subspaces `P` and `Q`,

`Tr(A_nu rho0^+ A_nu^dagger)=J_B+J_K`.

This exact quadratic addition is the key distinction from WP09, where an oppositely oriented term appears as `Y^dagger` and the measurement score vectors can only be combined by Minkowski.

## 4. Arbitrary-POVM mixed Fisher bound

For any POVM effect `M_y`, let

`p_y=Tr(rho0 M_y)`,

`z_y=Tr(A_nu M_y)`.

Since `A_nu=A_nu P`, the weighted Hilbert--Schmidt Cauchy--Schwarz argument used in WP06/WP07 gives

`|z_y|^2/p_y <= Tr[M_y A_nu rho0^+ A_nu^dagger]`.

Summing outcomes gives

> **One-copy mixed information law**
>
> `Tr F_1 <= J_B+J_K`.

For `N` independently encoded copies,

`A_(nu,N)=sum_j rho0^(tensor(j-1)) tensor A_nu tensor rho0^(tensor(N-j))`.

Cross-copy terms vanish because `Tr A_nu=0`. Therefore

> **Finite-copy collective mixed information law**
>
> `boxed: Tr F_N/N <= J_B+J_K`
>
> for every finite `N` and every arbitrary entangled collective POVM.

No SLD, Holevo, compatibility, or asymptotic-estimation assumption is used.

## 5. Pre-existing component is paid by robust spectral survival

The support-preserving component `B` has its own physical linear tangent radius

`R_B=1/w(rho0^(-1/2) B rho0^(-1/2))`

when `B!=0`.

This is the radius of the **internal support-preserving sub-tangent**, not the radius of the full family. The full family can still have `R_lin=0` because `K` enters the kernel.

The numerical-radius inequality gives

`B rho0^+ B^dagger <= (4/R_B^2) rho0`.

Since the range of `B` lies in `P_U,pre`,

`J_B <= (4/R_B^2) Tr(P_U,pre rho0)`.

Define the pre-existing upper endpoint population

`T_pre(nu)=Tr(P_U,pre rho0)`.

Then

> `boxed: J_B <= 4 T_pre(nu)/R_B^2`.

This is exactly the WP06 robust survival mechanism applied to the support-preserving part.

## 6. Synthesized component is paid by endpoint curvature

Let the exact physical two-parameter family be `C^2` near the origin,

`rho(x,y)=rho0+xD_c+yD_s+O(x^2+y^2)`.

Define the newly occupied upper endpoint population

`T_syn(x,y)=Tr[P_U,syn rho(x,y)]`.

At the baseline,

`T_syn(0,0)=0`,

`grad T_syn(0,0)=0`.

For the kernel block,

`Q D_c P=K/2`,

`Q D_s P=K/(2i)`.

Applying the second-order PSD-cone inequality to the `x` and `y` directions separately and summing gives

`Delta T_syn(0) >= Tr(K rho0^+ K^dagger)=J_K`.

Thus

> `boxed: J_K <= Delta T_syn(0)`.

This is exactly the WP07 synthesis mechanism, now coexisting with a nonzero support-preserving tangent.

## 7. Sharp mixed survival+synthesis theorem

Combining the measurement bound with the two resource reductions gives:

> **One-sided mixed temporal-information resource law**
>
> For an energy-invariant baseline support, an exact positive-gap tangent with no lower-endpoint synthesis, any finite `N`, and any arbitrary joint POVM,
>
> `boxed: Tr F_N/N`
>
> `<= J_B+J_K`
>
> `<= 4 T_pre(nu)/R_B^2 + Delta T_syn(0)`.

The pre-existing and newly synthesized resource contributions combine **additively** in this one-sided orientation.

This contrasts sharply with WP09 bilateral synthesis:

`Tr F/N <= [sqrt(Delta T_+)+sqrt(Delta T_-)]^2`.

The resource-composition rule therefore depends on support orientation, not merely on the total amount of endpoint population involved.

## 8. Positive gap-energy/action corollary

Define the quadratic positive synthesis energy at gap `nu`

`E_syn^(2)(nu)=(hbar nu/4) Delta T_syn(0)`.

The pre-existing endpoint population obeys

`hbar nu T_pre(nu) <= Ebar+`

for mean excess energy `Ebar+` above the participating lower edge.

Multiplying the mixed theorem by `hbar nu/4` gives

`(hbar nu/4)[Tr F_N/N]`

`<= hbar nu T_pre/R_B^2 + E_syn^(2)`

`<= Ebar+/R_B^2 + E_syn^(2)`.

Therefore

> **Mixed robust-energy + synthesis-action law**
>
> `boxed: Ebar+/R_B^2 + E_syn^(2)(nu)`
>
> `>= (hbar nu/4)[Tr F_N/N]`.

The two terms have the same parameter-normalized energy dimension: the first charges finite-radius pre-existing spectral support, while the second charges quadratic creation of a previously absent endpoint.

A sharper endpoint-specific version replaces `Ebar+` by `hbar nu T_pre` when that quantity is retained explicitly.

## 9. Exact three-level extremizer

Take

`H=hbar nu diag(0,1,2)`

and baseline

`rho0=p0 |0><0| + p1 |1><1|`,

with

`p0>0`, `p1>0`, `p0+p1=1`.

The level `|2>` is absent from the baseline.

For any `kappa>0`, choose

`A_nu=kappa p0 |1><0| + kappa p1 |2><1|`.

Then

`B=kappa p0 |1><0|`,

`K=kappa p1 |2><1|`.

The weighted norms are

`J_B=kappa^2 p0`,

`J_K=kappa^2 p1`,

so

`J_B+J_K=kappa^2`.

### Pre-existing term is exactly saturated

For `B`,

`rho0^(-1/2)B rho0^(-1/2)`

`=kappa sqrt(p0/p1)|1><0|`.

The numerical radius of a rank-one nilpotent shift `a|1><0|` is `|a|/2`. Hence

`R_B^2=4p1/(kappa^2 p0)`.

The pre-existing upper population is

`T_pre=p1`.

Therefore

`4T_pre/R_B^2=kappa^2 p0=J_B`.

### Exact physical nonlinear family saturating synthesis curvature

Let

`G=(1/2)A_nu rho0^+`

`=(kappa/2)(|1><0|+|2><1|)`.

For `z=x-i y`, define

`M(z)=I+zG`

and the exactly physical normalized family

`rho(x,y)=M(z) rho0 M(z)^dagger / Tr[M(z)rho0M(z)^dagger]`.

At the origin its complex tangent is exactly `A_nu`.

The newly synthesized level-2 population is

`T_syn(x,y)=kappa^2 p1(x^2+y^2)/4 + O[(x^2+y^2)^2]`.

Hence

`Delta T_syn(0)=kappa^2 p1=J_K`.

Thus the synthesis-curvature inequality is also exactly saturated.

## 10. One fixed Fourier measurement saturates the total information law

Let

`phi_m=2pi m/3`, `m=0,1,2`,

and use the orthonormal Fourier basis

`|v_m>=(|0>+exp(-i phi_m)|1>+exp(-2i phi_m)|2>)/sqrt(3)`.

Measure

`M_m=|v_m><v_m|`.

At the baseline,

`p_m=1/3`.

Because both exact-gap links acquire the same Fourier phase,

`Tr(A_nu M_m)=kappa exp(i phi_m)/3`

up to a convention-dependent conjugate phase.

Therefore

`Tr F_1=sum_m |Tr(A_nu M_m)|^2/p_m=kappa^2`.

Hence

> `boxed: Tr F_1`
>
> `=J_B+J_K`
>
> `=4T_pre/R_B^2 + Delta T_syn`.

All three inequalities are saturated simultaneously by one fixed measurement.

The coefficient and additive composition rule are therefore exact in this mixed one-sided sector.

## 11. Energy/action equality in the extremizer

The baseline mean excess energy above level `|0>` is

`Ebar+=hbar nu p1`.

Thus

`Ebar+/R_B^2`

`=(hbar nu/4)kappa^2 p0`.

Also

`E_syn^(2)=(hbar nu/4)kappa^2 p1`.

Therefore

`Ebar+/R_B^2 + E_syn^(2)`

`=(hbar nu/4)kappa^2`

`=(hbar nu/4)Tr F_1`.

The mixed robust-energy+synthesis-action coefficient is exactly sharp.

## 12. Lower-oriented analogue

By conjugating the construction, the same theorem holds when only a **lower** endpoint is synthesized and the pre-existing support-preserving component is charged from the opposite orientation.

The bilateral case is different: once both support-to-kernel orientations are simultaneously present, WP09 shows that square-root/Minkowski composition is unavoidable.

## 13. Prior-art boundary

Do not claim novelty for:

- Hilbert--Schmidt Cauchy--Schwarz;
- numerical-radius positivity bounds;
- PSD-cone second-order tangent geometry;
- Fourier/covariant phase measurements;
- Fisher-symmetric measurement constructions;
- singular/rank-changing QFI/Bures geometry.

Targeted searches have not identified the combined statement

`finite-radius pre-existing exact-gap information + one-sided support creation -> sharp additive arbitrary-POVM survival+synthesis law`

or the exact simultaneous qutrit saturation of both resource terms. This is a targeted screen only. Priority remains **unverified, not certified**.

## 14. Consequence for the grand program

The resource-composition hierarchy is now sharper:

### Pre-existing only

`Fisher x robustness <= spectral survival`.

### Synthesis only, one orientation

`Fisher <= endpoint curvature`.

### Pre-existing + synthesis, same orientation

`Fisher <= pre-existing robust resource + synthesis resource`,

with exact additive composition.

### Bilateral synthesis

`sqrt(Fisher) <= sqrt(upper synthesis)+sqrt(lower synthesis)`.

Thus the crossover from addition to Minkowski is controlled by **orientation of the information-bearing tangent relative to baseline support**.

This is a structural result, not merely a collection of examples.

## 15. Next work

The remaining hard problem is now specifically the noncommuting-support case:

1. remove `[P,H]=0` while retaining an exact full tangent `A_nu`;
2. quantify how projecting an energy endpoint through `P` mixes pre-existing and synthesized support;
3. test principal-angle and shorted-operator resource factors;
4. determine whether scalar tail/radius/curvature data are sufficient;
5. if not, prove a scalar-insufficiency theorem and identify the minimal operator-valued resource;
6. preserve exact reduction to WP06, WP07, WP09, and WP10.
