# WP19 — Noncommuting-support autonomous mixed resource/action law

**Date:** 2026-08-22

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** analytic PASS as a universal finite-copy arbitrary-POVM autonomous exact-exchange bound with arbitrary coherent baseline support. The theorem unifies WP03/WP06 finite-radius dual survival, WP11 noncommuting support geometry, WP13 positive spectral action, and WP18 zero-radius dual synthesis action. It uses one combined clock+signal endpoint-incidence cost operator, avoiding a separate clock-versus-signal curvature double count. The clean WP18 coefficients are recovered exactly. In the shared-kernel qutrit benchmark, the combined action reduction reproduces the WP12 abstract resource ceiling `12` with no additional looseness. Generic global sharpness is not claimed; priority remains **unverified, not certified**.

## 1. Exact autonomous exchange with arbitrary coherent support

Let clock `C` and signal `S` have semibounded Hamiltonians and let the full complex tangent satisfy

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`.

Thus

`[H_C+H_S,A_nu]=0`.

Let

`P=supp(rho0)`, `Q=I-P`.

Do **not** assume `[P,H_C]=0` or `[P,H_S]=0`.

Two-sided first-order physicality gives

`Q A_nu Q=0`.

Decompose as in WP11:

`B=P A_nu P`,

`K_+=Q A_nu P`,

`K_-=Q A_nu^dagger P`.

Then

`A_nu=B+K_+ + K_-^dagger`.

Define

`J_B^+=Tr(B rho0^+ B^dagger)`,

`J_B^-=Tr(B^dagger rho0^+ B)`,

`J_+=Tr(K_+ rho0^+ K_+^dagger)`,

`J_-=Tr(K_- rho0^+ K_-^dagger)`.

For every finite `N` and every arbitrary collective POVM,

`sqrt[Tr F_N/N]`

`<=min{sqrt(J_B^+ + J_+) + sqrt(J_-),`

`      sqrt(J_B^- + J_-) + sqrt(J_+)}`.

## 2. Two-sided pre-existing exchange resource

Let the participating signal endpoint projectors be

`Pi_(S,U)`, `Pi_(S,D)`

and the participating clock endpoint projectors be

`Pi_(C,U)`, `Pi_(C,D)`.

For the positive exchange orientation `A_nu`, the internal output is associated with

- signal upper endpoint `Pi_(S,U)`;
- clock lower endpoint `Pi_(C,D)`.

For the conjugate orientation it is associated with

- signal lower endpoint `Pi_(S,D)`;
- clock upper endpoint `Pi_(C,U)`.

Define support compressions

`S_(S,U)=P Pi_(S,U) P`,

`S_(S,D)=P Pi_(S,D) P`,

`S_(C,U)=P Pi_(C,U) P`,

`S_(C,D)=P Pi_(C,D) P`.

Let

`R_B^+=supp(B rho0^+ B^dagger)`,

`R_B^-=supp(B^dagger rho0^+ B)`.

Define shorting constants

`lambda_(S,U)=sup{lambda:S_(S,U)>=lambda R_B^+}`,

`lambda_(C,D)=sup{lambda:S_(C,D)>=lambda R_B^+}`,

`lambda_(S,D)=sup{lambda:S_(S,D)>=lambda R_B^-}`,

`lambda_(C,U)=sup{lambda:S_(C,U)>=lambda R_B^-}`.

Let baseline endpoint populations be

`T_(X,E)=Tr(Pi_(X,E) rho0)`.

Let `R_B` be the physical linear radius of the support-preserving sub-tangent `B`.

WP11 applied from the signal and clock viewpoints gives

`J_B^+<=4T_(S,U)/(R_B^2 lambda_(S,U))`,

`J_B^+<=4T_(C,D)/(R_B^2 lambda_(C,D))`,

and therefore

> `a_+:=min{`
>
> `4T_(S,U)/(R_B^2 lambda_(S,U)),`
>
> `4T_(C,D)/(R_B^2 lambda_(C,D))`
>
> `}`
>
> `>=J_B^+`.

Similarly

> `a_-:=min{`
>
> `4T_(S,D)/(R_B^2 lambda_(S,D)),`
>
> `4T_(C,U)/(R_B^2 lambda_(C,U))`
>
> `}`
>
> `>=J_B^-`.

Thus the pre-existing internal exchange coherence is already forced to be backed on both sides of the relational cut, including arbitrary support/energy principal-angle penalties.

If `B=0`, set `a_+=a_-=0`.

## 3. One combined clock+signal synthesis cost operator

Let the exact physical family be `C^2` and define the global kernel curvature

`C_Delta=Q(partial_x^2 rho+partial_y^2 rho)Q`.

Second-order positivity gives

`C_Delta>=Z_+ + Z_-`,

where

`Z_+=K_+ rho0^+ K_+^dagger`,

`Z_-=K_- rho0^+ K_-^dagger`.

Instead of bounding clock and signal synthesis separately and then adding two potentially overlapping curvature charges, define one positive **endpoint-incidence cost operator**

> `G_CS=hbar nu Q[`
>
> `Pi_(S,U)+Pi_(S,D)+Pi_(C,U)+Pi_(C,D)`
>
> `]Q`.

This counts one absolute exchange gap for every participating local endpoint incidence. If one Hilbert-space sector plays more than one endpoint role, the multiplicity is retained; this is intentional and should not be confused with signed subsystem mean energy.

Define the total positive autonomous synthesis action

> `A_CS^(2)=(1/4)Tr(G_CS C_Delta)`.

This equals the sum of the corresponding clock and signal endpoint-incidence actions defined from the same curvature operator.

Let

`R_+=supp(Z_+)`,

`R_-=supp(Z_-)`.

Define exact restricted combined costs

> `g_+=lambda_min[R_+ G_CS R_+ |_(R_+)]`,
>
> `g_-=lambda_min[R_- G_CS R_- |_(R_-)]`.

If a corresponding synthesized component vanishes, its `g` is unnecessary. If a nonzero component has `g=0`, no finite scalar action-only bound exists for that orientation.

## 4. Combined action charges the shared curvature once

Because

`C_Delta>=Z_+ + Z_-`

and `G_CS>=0`,

`4A_CS^(2)=Tr(G_CS C_Delta)`

`>=Tr(G_CS Z_+)+Tr(G_CS Z_-)`.

By the restricted minimum costs,

`Tr(G_CS Z_+)>=g_+ J_+`,

`Tr(G_CS Z_-)>=g_- J_-`.

Therefore

> `boxed: g_+ J_+ + g_- J_- <= 4A_CS^(2)`.

This is the autonomous two-sided specialization of WP13, using the **same global curvature once**.

## 5. Full mixed autonomous Fisher theorem

Write

`e=4A_CS^(2)`.

For positive `p,q` and internal resource `a>=0`, use the WP13 exact action-only envelope

`Psi_a(e;p,q)=`

- `(sqrt(a)+sqrt(e/q))^2`, if `e<=a p^2/q`;
- `(e+p a)(1/p+1/q)`, if `e>=a p^2/q`.

Since

`J_B^+<=a_+`

and

`g_+J_+ + g_-J_-<=e`,

the upper-oriented WP11 score bound gives

`Tr F_N/N<=Psi_(a_+)(e;g_+,g_-)`.

The conjugate orientation gives

`Tr F_N/N<=Psi_(a_-)(e;g_-,g_+)`.

Hence:

> **Noncommuting autonomous mixed resource/action law**
>
> `boxed: Tr F_N/N`
>
> `<=min{`
>
> `Psi_(a_+)(4A_CS^(2);g_+,g_-),`
>
> `Psi_(a_-)(4A_CS^(2);g_-,g_+)`
>
> `}`.

This is valid for arbitrary coherent baseline support, arbitrary finite copy number, and arbitrary collective POVMs.

No SLD/Holevo attainability assumption enters.

## 6. Pure-boundary corollary

If

`B=0`,

then `a_+=a_-=0`.

For bilateral synthesis with both `g_+,g_->0`,

`Psi_0(e;g_+,g_-)=e(1/g_+ + 1/g_-)`.

Define the harmonic combined endpoint price

`g_parallel=(1/g_+ + 1/g_-)^(-1)`.

Then

> `boxed: A_CS^(2)`
>
> `>= (g_parallel/4)[Tr F_N/N]`.

If only the `+` orientation is synthesized,

`Tr F_N/N<=J_+`

and

`g_+J_+<=4A_CS^(2)`, so

> `boxed: A_CS^(2)>=(g_+/4)[Tr F_N/N]`.

These are the arbitrary-support versions of WP18.

## 7. Clean WP18 limit

In the clean globally stationary exchange of WP18, each synthesized orientation lands entirely in

- one signal endpoint costing `hbar nu`;
- one opposite clock endpoint costing `hbar nu`.

Therefore

`G_CS` acts as

`2 hbar nu I`

on each information-bearing synthesized endpoint range, so

`g_+=g_-=2 hbar nu`.

The bilateral harmonic cost is

`g_parallel=hbar nu`.

Thus

`A_CS^(2)>=(hbar nu/4)[Tr F_N/N]`,

exactly WP18.

For one-sided synthesis,

`A_CS^(2)>=(2hbar nu/4)[Tr F_N/N]`

`=(hbar nu/2)[Tr F_N/N]`,

again exactly WP18.

Because WP18 supplies exact extremizers, these clean-limit coefficients remain globally sharp.

## 8. Finite-radius limit

If no new kernel population is synthesized,

`K_+=K_-=0`,

then

`A_CS^(2)=0`.

The piecewise envelope reduces to

`Psi_a(0;p,q)=a`.

Hence

`Tr F_N/N<=min(a_+,a_-)`.

This is precisely the noncommuting-support two-sided finite-radius survival structure of WP03/WP06/WP11.

Thus WP19 provides a single mathematical bridge between the finite-radius and zero-radius autonomous resource regimes.

## 9. Shared-kernel qutrit becomes an autonomous fixed-shell benchmark

The WP12/WP15 qutrit can be reinterpreted as a globally stationary exchange model.

Use the fixed-total-excitation-2 basis

`|L>=|2_C,0_S>`,

`|M>=|1_C,1_S>`,

`|U>=|0_C,2_S>`.

Set

`H_S/hbar nu=diag(0,1,2)`,

`H_C/hbar nu=diag(2,1,0)`.

Then

`H_C+H_S=2 hbar nu I`.

Take

`|q>=(1/2)|L> + sqrt(5/8)|M> + [1/(2sqrt(2))]|U>`,

`P=I-|q><q|`,

`rho0=P/2`,

and

> `A_nu=|M><L|-sqrt(2)|U><M|`.

This obeys

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`,

and

`Q A_nu Q=0`.

WP12 gives

`J_B^+=J_B^-=5/4`,

`J_+=7/4`,

`J_-=3`.

The relevant endpoint-incidence operator before kernel compression is

`G_CS/(hbar nu)=diag(2,4,2)`.

Since both synthesized weighted operators have the same rank-one range `Q`,

`g_+=g_-=<q|G_CS|q>`

`=(13/4)hbar nu`.

For the minimal curvature

`C_Delta=Z_++Z_-=(19/4)Q`,

one has

`4A_CS^(2)=Tr(G_CS C_Delta)`

`=(247/16)hbar nu`.

Take units `hbar nu=1` and use the exact internal value

`a=5/4`.

The threshold is

`a p^2/q=a p=65/16`,

while

`e=247/16`,

so the second branch applies:

`Psi_(5/4)(247/16;13/4,13/4)`

`=[247/16+(13/4)(5/4)] x [8/13]`

`=(312/16)(8/13)`

`=12`.

Therefore

> `boxed: WP19 autonomous action envelope =12`

exactly equal to the original WP12 abstract resource-allocation ceiling.

The autonomous endpoint-action reduction introduces **no additional resource-layer looseness** in this noncommuting coherent-support benchmark.

WP15 then supplies the lower accessibility layer:

`resource 12 > SLD 43/4 > common-record 55/8`.

This places the entire benchmark inside one globally stationary relational-time experiment.

## 10. Meaning of the combined action

`A_CS^(2)` is not ordinary total mean-energy curvature.

In a fixed-total-energy shell the signed total energy is constant and can have zero curvature identically.

Instead `G_CS` counts absolute endpoint incidences of the exact exchange gap on both subsystems. It is a positive kinematic resource attached to the exchange structure.

This is why globally stationary relative temporal information can have nonzero resource cost even when global asymmetry and total-energy curvature both vanish.

## 11. Prior-art boundary

Do not claim novelty for:

- Page--Wootters relational time;
- fixed-total-number relative-phase metrology;
- energy-conserving exchange interactions;
- shorted operators and principal angles;
- SDP/action-budget duality;
- harmonic resource allocation;
- QFI/Holevo/Gill--Massar measurement compatibility.

Candidate novelty is restricted to the combined theorem:

> arbitrary finite-copy relative temporal Fisher information in a globally stationary exact exchange is jointly bounded by two-sided pre-existing endpoint survival and one positive shared clock+signal synthesis action, with the clean finite-radius and zero-radius laws recovered as exact limits.

Priority remains unverified.

## 12. Next work

Highest-value next steps:

1. perform a hostile proof audit of WP19, especially endpoint-projector overlap/multiplicity and the definition of `G_CS`;
2. search prior art specifically for two-sided energy-conserving metrology bounds in fixed-total-energy sectors;
3. derive a multi-gap autonomous version using a single combined spectral action operator;
4. test whether `G_CS` can be replaced by a smaller orientation-labelled operator resource without losing positivity or reintroducing curvature double counting;
5. decide manuscript significance only after these audits.
