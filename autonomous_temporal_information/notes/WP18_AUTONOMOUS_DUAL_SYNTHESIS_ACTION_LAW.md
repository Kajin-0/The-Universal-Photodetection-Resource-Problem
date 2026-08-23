# WP18 — Sharp autonomous dual synthesis-action law at zero tangent radius

**Date:** 2026-08-22

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** analytic PASS for the clean globally stationary exact-exchange boundary regime. The theorem closes the `R_lin=0` autonomous loophole left by WP03: if relative temporal information is created by quadratic boundary synthesis rather than pre-existing finite-radius coherence, positive absolute-gap synthesis action must be paid on **both** clock and signal sides. For bilateral synthesis the total coefficient is `hbar nu/4`; for one-sided synthesis it improves to `hbar nu/2`. Both coefficients are exactly sharp in finite-dimensional globally stationary exchange models. Page--Wootters relational time, energy-conserving exchange dynamics, PSD-cone curvature, and multiparameter phase estimation are prior art. Candidate novelty is the sharp two-sided frequency-resolved synthesis-action law. Priority remains **unverified, not certified**.

## 1. Problem left by WP03

WP03 established the finite-radius autonomous law

`(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`

and hence

`Ebar_C^+ + Ebar_S^+ >= 2 hbar nu (R_lin^2/4)[Tr F_N/N]`.

But WP03 is vacuous when

`R_lin=0`.

WP07--WP14 showed that this does not make temporal information free: rank-changing tangents require second-order spectral synthesis.

WP18 asks whether the same conclusion becomes **two-sided** in a genuinely autonomous clock--signal exchange.

## 2. Globally stationary exact exchange

Let clock `C` and signal `S` have Hamiltonians `H_C,H_S`.

Let the complex temporal tangent obey

> `[H_S,A_nu]=+hbar nu A_nu`,
>
> `[H_C,A_nu]=-hbar nu A_nu`,

with `nu>0`.

Therefore

`[H_C+H_S,A_nu]=0`.

The two quadratures

`D_c=(A_nu+A_nu^dagger)/2`,

`D_s=(A_nu-A_nu^dagger)/(2i)`

encode a relative temporal mode while preserving total energy.

Let

`P=supp(rho0)`, `Q=I-P`.

For a two-sided physical `C^2` family, first-order positivity gives

`Q A_nu Q=0`.

In the pure boundary regime considered here there is no support-preserving component:

`P A_nu P=0`.

Define

`X=A_nu P`,

`Y=Q A_nu^dagger P`,

so

`A_nu=X+Y^dagger`.

The one-sided case is `Y=0` or `X=0`; bilateral synthesis has both nonzero.

## 3. Paired endpoint sectors

Because `A_nu` raises the signal and lowers the clock by exactly the same gap, the two support-to-kernel orientations terminate in paired endpoint sectors.

Choose mutually orthogonal baseline-empty projectors

`P_(S,+)`, `P_(S,-)`

for the signal upper/lower endpoints and

`P_(C,+)`, `P_(C,-)`

for the clock upper/lower endpoints such that

`X=P_(S,+) P_(C,-) X P`,

`Y=P_(S,-) P_(C,+) Y P`.

Here tensor-product identities are suppressed.

Thus:

- `X` synthesizes a signal-upper / clock-lower endpoint;
- `Y` synthesizes a signal-lower / clock-upper endpoint.

All four endpoint sectors are absent from the baseline in this clean boundary theorem.

## 4. Endpoint population curvatures

For the exact physical family `rho(x,y)`, define

`T_(S,+)=Tr[P_(S,+) rho(x,y)]`,

`T_(S,-)=Tr[P_(S,-) rho(x,y)]`,

`T_(C,+)=Tr[P_(C,+) rho(x,y)]`,

`T_(C,-)=Tr[P_(C,-) rho(x,y)]`.

Let

`Delta=partial_x^2+partial_y^2`

at the origin.

The WP07/WP09 second-order PSD-cone theorem gives

`J_X<=Delta T_(S,+)`,

`J_Y<=Delta T_(S,-)`,

where

`J_X=Tr(X rho0^+ X^dagger)`,

`J_Y=Tr(Y rho0^+ Y^dagger)`.

The same operators viewed from the clock side give

`J_X<=Delta T_(C,-)`,

`J_Y<=Delta T_(C,+)`.

The pairing is the autonomous content: one synthesized score amplitude simultaneously consumes a signal endpoint and the matching opposite clock endpoint.

## 5. Arbitrary finite-copy Fisher law from each side

WP09 gives, for every finite `N` and every arbitrary entangled collective POVM on `N` independently encoded copies,

> `sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

Therefore the signal endpoint curvatures obey

> `boxed: Tr F_N/N`
>
> `<= [sqrt(Delta T_(S,+))+sqrt(Delta T_(S,-))]^2`.

Independently, the clock endpoint curvatures obey

> `boxed: Tr F_N/N`
>
> `<= [sqrt(Delta T_(C,+))+sqrt(Delta T_(C,-))]^2`.

No external timing reference, SLD attainability, or separable readout is assumed.

## 6. Positive local synthesis actions

Ordinary signed subsystem energy curvature is not the correct quantity because synthesizing a lower endpoint can reduce that subsystem's mean energy.

Instead assign the positive **absolute exchange-gap action**

> `A_S^(2)=(hbar nu/4)[Delta T_(S,+)+Delta T_(S,-)]`,
>
> `A_C^(2)=(hbar nu/4)[Delta T_(C,+)+Delta T_(C,-)]`.

These are the local specializations of the WP09/WP13 positive spectral-synthesis action.

Using

`(sqrt(a)+sqrt(b))^2<=2(a+b)`,

each local Fisher law implies

> `A_S^(2) >= (hbar nu/8)[Tr F_N/N]`,
>
> `A_C^(2) >= (hbar nu/8)[Tr F_N/N]`.

Adding them gives the main theorem:

> **Autonomous dual synthesis-action law — bilateral boundary**
>
> `boxed: A_C^(2)+A_S^(2)`
>
> `>= (hbar nu/4)[Tr F_N/N]`.

This is the zero-radius analogue of WP03's statement that a relative temporal mode must be backed on both sides of the clock--signal cut.

## 7. One-sided boundary refinement

If only one support orientation is present, say

`Y=0`,

then WP07 gives directly

`Tr F_N/N<=Delta T_(S,+)`

and

`Tr F_N/N<=Delta T_(C,-)`.

Therefore

> `A_S^(2)>=(hbar nu/4)[Tr F_N/N]`,
>
> `A_C^(2)>=(hbar nu/4)[Tr F_N/N]`.

Hence

> **Autonomous dual synthesis-action law — one-sided boundary**
>
> `boxed: A_C^(2)+A_S^(2)`
>
> `>= (hbar nu/2)[Tr F_N/N]`.

The stronger coefficient occurs because there is no opposite synthesized score amplitude with which to interfere constructively.

## 8. Exact bilateral extremizer in a fixed-total-energy shell

Take equally spaced local Hamiltonians

`H_C=hbar nu N_C`,

`H_S=hbar nu N_S`.

Restrict to the fixed-total-excitation-2 shell spanned by

`|L>=|2_C,0_S>`,

`|M>=|1_C,1_S>`,

`|U>=|0_C,2_S>`.

Every vector in this shell has exactly the same total energy

`2 hbar nu`.

Thus every density operator supported in the shell is globally stationary under

`H_C+H_S`.

Choose

`rho0=|M><M|`

and

> `A_nu=c(|U><M|+|M><L|)`.

Both terms satisfy

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`.

The support decomposition is

`X=c|U><M|`,

`Y=c|L><M|`,

so

`J_X=J_Y=c^2`.

### Exact physical family

Use

`|psi(x,y)>`

`=sqrt[1-(c^2/2)(x^2+y^2)] |M>`

` +(c/2)(x+i y)|L>`

` +(c/2)(x-i y)|U>`.

This remains entirely inside the fixed-total-energy shell and is therefore globally stationary for every `(x,y)`.

The four local endpoint populations are paired:

`T_(S,-)=T_(C,+)=c^2(x^2+y^2)/4`,

`T_(S,+)=T_(C,-)=c^2(x^2+y^2)/4`.

Hence

`Delta T_(S,-)=Delta T_(S,+)=c^2`,

`Delta T_(C,-)=Delta T_(C,+)=c^2`.

Thus

`A_S^(2)=A_C^(2)=hbar nu c^2/2`.

## 9. Fourier measurement saturates the bilateral coefficient

Use the orthonormal Fourier basis in the ordered shell `{|L>,|M>,|U>}`:

`phi_m=2 pi m/3`,

`|v_m>=(e^(-i phi_m)|L>+|M>+e^(i phi_m)|U>)/sqrt(3)`.

As in WP09,

`Tr F_1=4c^2`.

Therefore

`A_C^(2)+A_S^(2)=hbar nu c^2`

and

`(hbar nu/4)Tr F_1=hbar nu c^2`.

Hence

> `boxed: A_C^(2)+A_S^(2)=(hbar nu/4)Tr F_1`.

The bilateral coefficient is exactly sharp already at one copy.

Crucially, global time-translation asymmetry is zero throughout the entire family: the temporal information is purely relational inside one degenerate total-energy shell.

## 10. Exact one-sided extremizer

Use the fixed-total-excitation-1 shell

`|D>=|1_C,0_S>`,

`|U>=|0_C,1_S>`.

Choose

`rho0=|D><D|`,

`A_nu=2c |U><D|`.

The exact family

`|psi(x,y)>=sqrt[1-c^2(x^2+y^2)]|D>+c(x+i y)|U>`

is globally stationary because both basis states have total energy `hbar nu`.

One has

`Tr F_1=4c^2`,

`Delta T_(S,+)=Delta T_(C,-)=4c^2`.

Hence

`A_S^(2)=A_C^(2)=hbar nu c^2`

and

> `A_C^(2)+A_S^(2)`
>
> `=2 hbar nu c^2`
>
> `=(hbar nu/2)Tr F_1`.

Thus the one-sided coefficient is also exactly sharp.

## 11. Relation to WP03

WP03 and WP18 describe complementary physical regimes.

### Finite-radius regime

Pre-existing spectral population/coherence allows a nonzero affine neighborhood.

Resource:

`robust Fisher x R_lin^2 -> two-sided baseline survival/mean energy`.

### Zero-radius boundary regime

The affine tangent is not itself physical for any finite radius; an exact nonlinear family must synthesize new endpoint population at second order.

Resource:

`Fisher -> two-sided positive quadratic spectral action`.

In both regimes, autonomous relative temporal information requires matched resources on both sides of the relational cut.

The resource changes order in the local parameter expansion, but the **two-sided exchange principle survives**.

## 12. Why signed mean-energy curvature is insufficient

In the bilateral fixed-total-energy extremizer,

`<H_C>+<H_S>=2 hbar nu`

exactly for every `(x,y)`.

Indeed each subsystem's mean energy is also unchanged by symmetry between its upper and lower endpoint populations.

Therefore ordinary total-energy curvature is zero while

`Tr F_1=4c^2>0`.

This is an autonomous version of the WP14 coherent-sideband lesson: signed mean energy can cancel even when positive spectral synthesis is unavoidable.

The correct action counts absolute exchange-gap population on both sides.

## 13. Prior-art boundary

Do not claim novelty for:

- Page--Wootters relational time or globally stationary history states;
- energy-conserving exchange Hamiltonians;
- relative-phase estimation in fixed-number sectors;
- PSD-cone second-order tangent geometry;
- Fourier qutrit phase measurements;
- generic quantum Fisher/Holevo compatibility theory.

Candidate novelty is the specific frequency-resolved arbitrary-POVM statement:

> at zero affine tangent radius, globally stationary relational temporal Fisher information requires positive second-order spectral exchange action on **both** clock and signal, with sharp total coefficients `hbar nu/4` in the bilateral case and `hbar nu/2` in the one-sided case.

Priority remains unverified.

## 14. Next work

Highest-value next targets:

1. remove the clean baseline-empty endpoint assumption using the WP11/WP12 shorted-operator geometry on both clock and signal sides;
2. determine whether a single joint operator allocation couples the two local action bounds more tightly than simply adding them;
3. extend the autonomous action theorem across multiple gaps and derive a common spectral-action budget;
4. perform a deep priority/significance audit of WP03+WP18 against relational quantum metrology and quantitative WAY literature;
5. only after that decide whether the autonomous theorem pair is publication-grade.
