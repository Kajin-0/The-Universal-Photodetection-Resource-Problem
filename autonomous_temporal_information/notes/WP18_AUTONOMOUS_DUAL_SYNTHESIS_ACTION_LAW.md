# WP18 — Sharp autonomous dual synthesis-action law at zero tangent radius

**Date:** 2026-08-22; hostile convention audit 2026-08-23

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** analytic PASS after independent factor/convention audit. A minor sign inconsistency in the originally written one-sided extremizer was corrected: with `D_s=(A-A^dagger)/(2i)`, the exact family uses `x-i y`, not `x+i y`. This is only a reversal of the sine coordinate and never changed the Fisher/action values or coefficients. The bilateral theorem and extremizer were convention-consistent as written.

## 1. Exact exchange and two-quadrature convention

Let

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`,

so

`[H_C+H_S,A_nu]=0`.

Use

`D_c=(A_nu+A_nu^dagger)/2`,

`D_s=(A_nu-A_nu^dagger)/(2i)`.

For a POVM `{M_y}`, write

`p_y=Tr(rho0 M_y)`,

`z_y=Tr(A_nu M_y)`.

Then

`partial_x p_y=Re z_y`,

`partial_y p_y=Im z_y`,

and therefore the two-quadrature classical Fisher trace is exactly

> `Tr F_1=sum_y |z_y|^2/p_y`.

This fixes all factors in what follows.

Let

`P=supp(rho0)`, `Q=I-P`.

In the pure-boundary theorem assume

`P A_nu P=0`.

First-order physicality gives

`Q A_nu Q=0`.

Define

`X=A_nu P`,

`Y=Q A_nu^dagger P`.

Then

`A_nu=X+Y^dagger`,

with `X,Y` support-to-kernel and hence traceless.

## 2. Finite-copy arbitrary-POVM Fisher law rederived

For `N` independently encoded copies,

`rho_N=rho0^(tensor N)`

and

`A_(N,nu)=sum_j rho0^(tensor(j-1)) tensor A_nu tensor rho0^(tensor(N-j))`.

Let `P_N=P^(tensor N)`.

The two right-supported pieces are

`X_N=A_(N,nu) P_N`

and

`Y_N=(I-P_N) A_(N,nu)^dagger P_N`.

They are sums of single-copy insertions of `X` and `Y`.

Using

`rho0 rho0^+ rho0=rho0`,

`X P=X`, `Y P=Y`,

and

`Tr X=Tr Y=0`,

all cross-copy terms in the weighted quadratic forms vanish. Therefore

`Tr(X_N rho_N^+ X_N^dagger)=N J_X`,

`Tr(Y_N rho_N^+ Y_N^dagger)=N J_Y`,

where

`J_X=Tr(X rho0^+ X^dagger)`,

`J_Y=Tr(Y rho0^+ Y^dagger)`.

The weighted Hilbert--Schmidt score bound plus Minkowski therefore gives every joint POVM on the `N` copies

> `boxed: sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

For `Y=0`, this reduces to

> `boxed: Tr F_N/N <= J_X`.

No asymptotic or separable-measurement assumption is present.

## 3. Second-order endpoint synthesis

For a `C^2` physical family, let the clean baseline-empty signal endpoint curvatures be

`Delta T_(S,+)`, `Delta T_(S,-)`

and clock endpoint curvatures

`Delta T_(C,+)`, `Delta T_(C,-)`.

Exact exchange pairs the orientations:

- `X`: signal upper / clock lower;
- `Y`: signal lower / clock upper.

The WP07 second-order PSD-cone inequality applied to the two quadratures gives

`J_X<=Delta T_(S,+)`,

`J_X<=Delta T_(C,-)`,

`J_Y<=Delta T_(S,-)`,

`J_Y<=Delta T_(C,+)`.

Hence, locally on either subsystem,

`Tr F_N/N <= [sqrt(Delta T_+)+sqrt(Delta T_-)]^2`.

## 4. Positive synthesis actions and audited coefficients

Define positive absolute-gap actions

`A_S^(2)=(hbar nu/4)[Delta T_(S,+)+Delta T_(S,-)]`,

`A_C^(2)=(hbar nu/4)[Delta T_(C,+)+Delta T_(C,-)]`.

These are not signed subsystem energy curvatures.

### Bilateral synthesis

From

`(sqrt(a)+sqrt(b))^2<=2(a+b)`,

each subsystem obeys

`A_X^(2)>=(hbar nu/8)[Tr F_N/N]`.

Adding clock and signal gives

> **Autonomous dual synthesis-action law — bilateral**
>
> `boxed: A_C^(2)+A_S^(2)`
>
> `>= (hbar nu/4)[Tr F_N/N]`.

### One-sided synthesis

If `Y=0`, then

`Tr F_N/N<=Delta T_(S,+)`

and

`Tr F_N/N<=Delta T_(C,-)`.

Thus each subsystem contributes `hbar nu/4` times the Fisher trace, and

> **Autonomous dual synthesis-action law — one-sided**
>
> `boxed: A_C^(2)+A_S^(2)`
>
> `>= (hbar nu/2)[Tr F_N/N]`.

The factor audit therefore confirms the published branch coefficients `1/4` and `1/2` exactly.

## 5. Exact bilateral fixed-shell extremizer

Use the total-excitation-2 shell

`|L>=|2_C,0_S>`,

`|M>=|1_C,1_S>`,

`|U>=|0_C,2_S>`.

Every vector has total energy `2 hbar nu`.

Take

`rho0=|M><M|`,

`A_nu=c(|U><M|+|M><L|)`.

The exact normalized family is

`|psi(x,y)>`

`=sqrt[1-(c^2/2)(x^2+y^2)]|M>`

` +(c/2)(x+i y)|L>`

` +(c/2)(x-i y)|U>`.

It is physical on the open disk

`x^2+y^2 < 2/c^2`.

Direct differentiation gives precisely

`partial_x rho(0)=D_c`,

`partial_y rho(0)=D_s`.

All states remain in one total-energy eigenspace, so

`[rho(x,y),H_C+H_S]=0`

throughout the disk.

Each of the four local endpoint populations equals

`c^2(x^2+y^2)/4`,

so every endpoint Laplacian is `c^2` and

`A_S^(2)=A_C^(2)=hbar nu c^2/2`.

The three-outcome Fourier basis

`|v_m>=(e^(-i phi_m)|L>+|M>+e^(i phi_m)|U>)/sqrt(3)`,

`phi_m=2 pi m/3`,

has baseline probabilities `1/3` and gives

`Tr F_1=4c^2`.

Therefore

> `A_C^(2)+A_S^(2)=hbar nu c^2=(hbar nu/4)Tr F_1`.

The bilateral coefficient is exactly sharp with an ordinary nonsingular POVM.

## 6. Exact one-sided fixed-shell extremizer — corrected convention

Use

`|D>=|1_C,0_S>`,

`|U>=|0_C,1_S>`,

`rho0=|D><D|`,

`A_nu=2c|U><D|`.

The convention-consistent exact family is

> `|psi(x,y)>=sqrt[1-c^2(x^2+y^2)]|D>+c(x-i y)|U>`.

It is physical on

`x^2+y^2<1/c^2`

and satisfies exactly

`partial_x rho(0)=D_c`,

`partial_y rho(0)=D_s`.

The baseline-empty signal-upper and clock-lower populations are both

`c^2(x^2+y^2)`,

so

`Delta T_(S,+)=Delta T_(C,-)=4c^2`.

A fixed four-outcome equatorial POVM gives

`Tr F_1=4c^2`.

Thus

`A_S^(2)=A_C^(2)=hbar nu c^2`

and

> `A_C^(2)+A_S^(2)=2hbar nu c^2=(hbar nu/2)Tr F_1`.

The one-sided coefficient is exactly sharp.

## 7. Meaning of the theorem

The fixed-shell extremizers make three points simultaneously:

1. global time-translation asymmetry is exactly zero;
2. signed total-energy curvature is exactly zero;
3. relative temporal Fisher information is nevertheless nonzero and requires positive endpoint synthesis action on both local sides.

The resource is therefore not ordinary total energy or global asymmetry. It is a positive frequency-resolved kinematic cost of creating the local endpoint structure that supports the relative temporal score.

## 8. Prior-art boundary

Do not claim novelty for Page--Wootters relational time, energy-conserving exchange, fixed-number relative-phase metrology, Fourier phase measurements, PSD-cone curvature, or generic QFI/Holevo theory.

Candidate novelty remains the sharp finite-copy arbitrary-POVM two-sided action statement and its role as the zero-radius completion of WP03.

Priority remains **unverified, not certified**.

## 9. Audit result

The 2026-08-23 hostile rederivation found **no coefficient or physicality defect** in WP18.

The only defect was the sign of `y` in the originally written one-sided exact ket. It has been corrected above. Since replacing `y` by `-y` is only a coordinate reversal, no Fisher information, endpoint curvature, action, or sharpness result changed.
