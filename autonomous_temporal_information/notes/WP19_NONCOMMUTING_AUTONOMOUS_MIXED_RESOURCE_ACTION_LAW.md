# WP19 — Noncommuting-support autonomous mixed resource/action law

**Date:** 2026-08-22; hostile action-definition audit 2026-08-23

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** analytic PASS as a universal finite-copy arbitrary-POVM exact-exchange bound for arbitrary coherent baseline support. The 2026-08-23 audit replaces the earlier noncanonical sum of four chosen local endpoint projectors by a **canonical joint domain/range endpoint-incidence operator** built directly from the exact-gap tangent. All clean coefficients and the shared-kernel qutrit benchmark remain unchanged.

## 1. Exact autonomous exchange with arbitrary coherent support

Let

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`.

Thus

`[H_C+H_S,A_nu]=0`.

Let

`P=supp(rho0)`, `Q=I-P`.

No commutation between `P` and either local Hamiltonian is assumed.

Two-sided first-order physicality gives

`Q A_nu Q=0`.

Decompose

`B=P A_nu P`,

`K_+=Q A_nu P`,

`K_-=Q A_nu^dagger P`,

so

`A_nu=B+K_+ + K_-^dagger`.

Define

`J_B^+=Tr(B rho0^+ B^dagger)`,

`J_B^-=Tr(B^dagger rho0^+ B)`,

`J_+=Tr(K_+ rho0^+ K_+^dagger)`,

`J_-=Tr(K_- rho0^+ K_-^dagger)`.

For every finite `N` and arbitrary joint POVM,

`sqrt[Tr F_N/N]`

`<=min{sqrt(J_B^+ + J_+) + sqrt(J_-),`

`      sqrt(J_B^- + J_-) + sqrt(J_+)}`.

## 2. Two-sided pre-existing exchange resource

The support-preserving piece `B` must be backed by both local sides of the exact exchange.

Let the participating signal upper/lower and clock upper/lower spectral projectors be chosen minimally for the actual support-preserving transition content. Compress them to `P` and define the corresponding WP11 shorting constants on the output supports of

`B rho0^+ B^dagger`

and

`B^dagger rho0^+ B`.

This gives rigorous ceilings

`J_B^+<=a_+`,

`J_B^-<=a_-`,

where `a_+` is the minimum of the signal-upper and clock-lower shorted survival ceilings, and `a_-` is the minimum of the signal-lower and clock-upper ceilings.

In the commuting clean limit the shorting constants are `1`, and this reduces to the WP03/WP06 two-sided pre-existing survival law.

If `B=0`, set `a_+=a_-=0`.

## 3. Canonical endpoint-role projectors for synthesis

The original WP19 note expressed the synthesis cost through a sum of four local endpoint projectors. That is valid if those projectors are fixed, but unnecessarily noncanonical: broad choices can inflate the resource while leaving the theorem true.

For a single exact exchange mode there is a canonical replacement.

Define the joint range and domain projectors of the full tangent

> `Pi_out=supp(A_nu A_nu^dagger)`,
>
> `Pi_in=supp(A_nu^dagger A_nu)`.

Because

`[H_X,A_nu]=s_X hbar nu A_nu`,

with `s_S=+1`, `s_C=-1`,

one has

`[H_X,A_nu A_nu^dagger]=0`,

`[H_X,A_nu^dagger A_nu]=0`

for `X=C,S`.

Therefore `Pi_out` and `Pi_in` are invariant joint local-energy endpoint-role subspaces.

Interpretation:

- `Pi_out`: signal-upper / clock-lower endpoint role of `A_nu`;
- `Pi_in`: signal-lower / clock-upper endpoint role of `A_nu`.

A joint endpoint incidence costs one absolute gap `hbar nu` on the signal and one on the clock, hence `2 hbar nu` in total.

Define the canonical positive clock+signal endpoint-incidence operator

> **Canonical exchange cost operator**
>
> `boxed: G_ex`
>
> `=2 hbar nu Q(Pi_out+Pi_in)Q`.

If a joint energy state belongs to both the domain and range of the full ladder operator, it is counted twice because it genuinely plays two endpoint roles. This is role multiplicity, not arbitrary double counting.

## 4. Shared kernel curvature is charged once

For a `C^2` exact physical family define

`C_Delta=Q(partial_x^2 rho+partial_y^2 rho)Q`.

Second-order positivity gives

`C_Delta>=Z_+ + Z_-`,

where

`Z_+=K_+ rho0^+ K_+^dagger`,

`Z_-=K_- rho0^+ K_-^dagger`.

Define the canonical kernel-resolved endpoint-incidence action

> `A_ex^(2)=(1/4)Tr(G_ex C_Delta)`.

Let

`R_+=supp Z_+`,

`R_-=supp Z_-`,

and define restricted costs

`g_+=lambda_min[R_+ G_ex R_+ |_(R_+)]`,

`g_-=lambda_min[R_- G_ex R_- |_(R_-)]`.

Then

`4A_ex^(2)=Tr(G_ex C_Delta)`

`>=Tr(G_ex Z_+)+Tr(G_ex Z_-)`

`>=g_+J_+ + g_-J_-`.

Hence

> `boxed: g_+J_+ + g_-J_- <=4A_ex^(2)`.

The same global curvature operator is charged once.

If a nonzero orientation has zero restricted cost, no finite scalar action-only bound follows from this cost operator, exactly as in WP13.

## 5. Full mixed autonomous Fisher theorem

For positive `p,q`, internal resource `a>=0`, and `e>=0`, define the WP13 envelope

`Psi_a(e;p,q)=`

- `(sqrt(a)+sqrt(e/q))^2`, if `e<=a p^2/q`;
- `(e+p a)(1/p+1/q)`, if `e>=a p^2/q`.

Since

`J_B^+<=a_+`

and

`g_+J_+ + g_-J_-<=4A_ex^(2)`,

the upper orientation gives

`Tr F_N/N<=Psi_(a_+)(4A_ex^(2);g_+,g_-)`.

The conjugate orientation gives

`Tr F_N/N<=Psi_(a_-)(4A_ex^(2);g_-,g_+)`.

Therefore

> **Noncommuting autonomous mixed resource/action law**
>
> `boxed: Tr F_N/N`
>
> `<=min{`
>
> `Psi_(a_+)(4A_ex^(2);g_+,g_-),`
>
> `Psi_(a_-)(4A_ex^(2);g_-,g_+)`
>
> `}`.

This is valid for arbitrary coherent baseline support, arbitrary finite copy number, and arbitrary collective POVMs.

## 6. Pure-boundary and finite-radius limits

### Pure bilateral boundary

If `B=0`,

`a_+=a_-=0`.

With both restricted costs positive,

`Tr F_N/N<=4A_ex^(2)(1/g_+ +1/g_-)`.

Equivalently, with

`g_parallel=(1/g_+ +1/g_-)^(-1)`,

> `A_ex^(2)>=(g_parallel/4)[Tr F_N/N]`.

### Pure one-sided boundary

If only `K_+` is nonzero,

> `A_ex^(2)>=(g_+/4)[Tr F_N/N]`.

### Finite radius

If `K_+=K_-=0`, the synthesis action vanishes and the theorem reduces to

`Tr F_N/N<=min(a_+,a_-)`,

the noncommuting-support two-sided survival law.

## 7. Clean WP18 limit

In a clean exact exchange,

- every `K_+` output lies in `Pi_out` and not `Pi_in`;
- every `K_-` output lies in `Pi_in` and not `Pi_out`.

Thus

`g_+=g_-=2hbar nu`.

The bilateral harmonic price is `hbar nu`, giving

`A_ex^(2)>=(hbar nu/4)[Tr F_N/N]`.

For one-sided synthesis,

`A_ex^(2)>=(hbar nu/2)[Tr F_N/N]`.

These are exactly WP18's sharp coefficients.

## 8. Shared-kernel qutrit benchmark reconstructed canonically

Use the fixed-total-excitation-2 basis

`|L>=|2_C,0_S>`,

`|M>=|1_C,1_S>`,

`|U>=|0_C,2_S>`.

Take

`|q>=(1/2)|L>+sqrt(5/8)|M>+[1/(2sqrt(2))]|U>`,

`P=I-|q><q|`,

`rho0=P/2`,

`A_nu=|M><L|-sqrt(2)|U><M|`.

Then

`Pi_out=|M><M|+|U><U|`,

`Pi_in=|L><L|+|M><M|`.

Therefore, before kernel compression,

`G_ex/(hbar nu)`

`=2(Pi_out+Pi_in)`

`=diag(2,4,2)`

in the `{L,M,U}` basis.

This is exactly the operator used numerically in the original WP19 benchmark, but it is now derived canonically rather than from a chosen list of four local projectors.

The reconstructed tangent norms remain

`J_B^+=J_B^-=5/4`,

`J_+=7/4`,

`J_-=3`.

Both synthesized weighted operators have range `Q`, and

`g_+=g_-=(13/4)hbar nu`.

For the minimal curvature

`C_Delta=(19/4)Q`,

`4A_ex^(2)=(247/16)hbar nu`.

Using units `hbar nu=1`, `a_+=a_-=5/4`, the second branch of `Psi` gives

`Psi_(5/4)(247/16;13/4,13/4)=12`.

Thus the canonical audited WP19 action still reproduces the WP12 physical resource ceiling exactly.

## 9. Interpretation boundary

`A_ex^(2)` is a **kernel-resolved positive endpoint-incidence action**.

It is not generally:

- the full Laplacian of a local endpoint population;
- signed clock or signal mean-energy curvature;
- total global energy curvature;
- the physical implementation energy of probe preparation, control, or measurement.

The action is a kinematic necessary resource of the local encoded state family.

In a fixed-total-energy shell, signed total energy can be exactly constant while `A_ex^(2)>0`.

## 10. Audit result

The 2026-08-23 hostile audit found no algebraic defect in the WP19 Fisher/action inequality or benchmark.

It did identify a **definition-quality issue**: the earlier four-projector cost representation depended on a choice of participating local endpoint projectors and could be inflated by unnecessarily broad choices.

The canonical `Pi_in/Pi_out` construction above removes that ambiguity for a single exact exchange mode while preserving the theorem and all reported constants.

Generic global sharpness remains unclaimed.

Priority remains **unverified, not certified**.
