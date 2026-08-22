# WP15 — General-density proof of the sharp continuum harmonic-mean area inequality

**Date:** 2026-08-21

## Status

**Proof repair / mathematical hardening of WP12.**

The sharp continuum inequality no longer needs smoothness, strict monotonicity, compact support, an inverse-density derivative, or two integrations by parts.

For every probability density `q` on `[0,infinity)` with finite first moment

`mu=int_0^infinity x q(x)dx`,

define

`A[q]=iint q(x)q(y)/[q(x)+q(y)] dxdy`,

with the integrand defined as zero when both densities vanish.

Then

`boxed: A[q] <= (pi/2) mu`.

The constant is sharp as a supremum.

This directly supplies the mathematical core of WP12's positive-frequency QFI-area bound for any continuum density for which the QFI functional is physically justified.

---

## 1. Rearrangement reduction

The functional

`A[q]=iint h(q(x),q(y))dxdy`,

`h(a,b)=ab/(a+b)`,

depends only on the distribution of the values of `q` under Lebesgue measure. Therefore it is invariant under equimeasurable rearrangement.

Let `q*` be the nonincreasing rearrangement of `q` on `[0,infinity)`.

By the standard Hardy--Littlewood/bathtub rearrangement principle, assigning the largest density values to the smallest coordinates minimizes the increasing weighted moment:

`int x q*(x)dx <= int x q(x)dx=mu`.

Since

`A[q*]=A[q]`,

it is enough to prove

`A[q*] <= (pi/2) int x q*(x)dx`.

Hence assume `q` is nonincreasing from now on.

---

## 2. Superlevel-length function

Define

`r(s)=Leb{x>=0:q(x)>s}`.

Because `q` is nonincreasing, the superlevel set is an initial interval up to null sets, but the argument only needs its measure.

Layer cake gives

`q(x)=int_0^infinity 1_{s<q(x)} ds`.

Therefore

`mu=int x q(x)dx`

`=int_0^infinity ds int_{q(x)>s} x dx`.

For decreasing `q`, `{q>s}` is `[0,r(s))`, so

`mu=int_0^infinity [r(s)^2/2] ds`.

Thus

`boxed: mu=(1/2)||r||_2^2`.

Finite first moment is exactly the statement `r in L2(ds)`.

---

## 3. Exact positive-kernel identity

For all `a,b>=0`, let

`K0(a,b)=ab/(a+b)`, with `K0(0,0)=0`.

For positive `s,t`,

`partial_s partial_t K0(s,t)=2st/(s+t)^3`.

Because `K0(a,0)=K0(0,b)=0`, the fundamental theorem of calculus yields the exact identity

`boxed: ab/(a+b)=int_0^a int_0^b [2st/(s+t)^3] dt ds`.

This identity is nonnegative and therefore works under Tonelli without any differentiability assumption on `q`.

---

## 4. Tonelli converts the density functional to an L2 quadratic form

Insert the kernel identity into `A[q]`:

`A[q]`

`=int dx int dy int_0^{q(x)}ds int_0^{q(y)}dt [2st/(s+t)^3]`.

All terms are nonnegative. Tonelli allows interchange of all integrations:

`A[q]`

`=int_0^infinity ds int_0^infinity dt [2st/(s+t)^3]`

`  * Leb{x:q(x)>s} * Leb{y:q(y)>t}`.

Therefore

`boxed: A[q]=<r,Tr>`,

where

`(Tr)(s)=int_0^infinity L(s,t)r(t)dt`,

`L(s,t)=2st/(s+t)^3`.

This obtains the WP12 Carleman/Mellin operator **without inverse functions or integration by parts**.

---

## 5. Exact operator norm

The symmetric kernel `L` is homogeneous of degree `-1`. The unitary Mellin transform on `L2(0,infinity;ds)` diagonalizes `T`.

The multiplier is

`lambda(xi)=int_0^infinity [2u/(1+u)^3]u^{-1/2+i xi}du`

`=|Gamma(3/2+i xi)|^2`

`=pi(1/4+xi^2)/cosh(pi xi)`.

Since

`cosh(pi xi)>=1+(pi^2 xi^2)/2>=1+4xi^2`,

`lambda(xi)<=pi/4`.

At `xi=0`, `lambda(0)=pi/4`. Hence

`boxed: ||T||=pi/4`.

No eigenfunction in `L2` attains the norm; the generalized extremal is proportional to `s^{-1/2}`.

---

## 6. General sharp inequality

Now

`A[q]=<r,Tr>`

`<=||T|| ||r||_2^2`

`=(pi/4)||r||_2^2`

`=(pi/2)mu`.

Thus for decreasing `q`,

`A[q]<=(pi/2)int xq(x)dx`.

Returning to the original density through rearrangement,

`boxed: A[q]<=(pi/2)int_0^infinity xq(x)dx`

for **every probability density with finite first moment**.

The normalization `int q=1` is not actually needed for the homogeneous inequality; for a general nonnegative integrable density both sides scale linearly with the total mass. Probability normalization is the physical use case.

---

## 7. Finiteness and crude bound

The sharp theorem itself ensures `A[q]` is finite whenever the first moment is finite.

There is also a simple pre-sharp estimate after decreasing rearrangement:

`h(q(x),q(y))<=min(q(x),q(y))`.

For decreasing `q`, on `x<y`, `min(q(x),q(y))=q(y)`. Hence

`A[q] <=2 int_0^infinity y q(y)dy=2mu`.

This provides an elementary finiteness bound before invoking the Mellin operator.

---

## 8. Sharpness

WP12's truncated critical Pareto family

`q_R(x)=C_R/(1+x)^2`, `0<=x<=R`,

with `C_R=(1+R)/R`, has finite mean for every finite `R` and satisfies

`A[q_R]/mu_R -> pi/2`

as `R->infinity`.

Therefore the constant `pi/2` is sharp over finite-first-moment probability densities.

No finite-mean density attains the scale-invariant generalized extremal exactly.

---

## 9. Consequence for WP12

Whenever the continuum maximal random-time QFI spectrum is

`G_Q(nu)=2 int_0^infinity h(q(w),q(w+nu))dw`,

we have

`int_0^infinity G_Q(nu)dnu=A[q]`.

Therefore for every finite-first-moment spectral density,

`boxed: int_0^infinity G_Q(nu)dnu <=(pi/2)wbar`,

and two-sided

`boxed: int_R G_Q(nu)dnu <=pi Ebar^+/hbar`.

The mathematical inequality itself is now general; the remaining continuum quantum-physics task is to justify the QFI functional for the intended source class/limit, not to strengthen the analysis regularity.

---

## 10. Prior-art caution

The proof uses standard ingredients:

- decreasing rearrangement;
- layer cake;
- positive-kernel/Tonelli identities;
- Mellin diagonalization of a homogeneous integral operator.

The exact inequality may well exist in classical analysis under another name or as a weighted Hilbert/Carleman inequality. Mathematical novelty is **not claimed** until a dedicated analysis-literature audit is complete.

The physics novelty candidate remains the identification of this sharp functional as the integrated maximal QFI retention of random temporal-distribution modes.

---

## Decision

One of WP12's main technical caveats is closed.

The sharp `pi/2` density-functional inequality is publication-grade for arbitrary finite-first-moment densities. The remaining high-value gates are now physical/prior-art rather than regularity:

1. prove/justify the continuum QFI functional for broad physical optical source classes;
2. deep-search random group-distribution estimation literature;
3. determine coherent/indefinite-number source boundaries (WP14);
4. study operational attainability of the `pi` QFI-area constant.
