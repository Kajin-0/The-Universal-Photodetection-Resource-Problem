# WP12 — Sharp continuum quantum random-time Fisher mode-area law

**Date:** 2026-08-21

## Status

**Major strengthening of WP10.**

The periodic quantum random-time mode budget admits a controlled continuum limit for regular positive-frequency spectral densities. The crude continuum constant inherited from the discrete estimate is not sharp. A rearrangement + Mellin/Carleman analysis gives the sharp continuum constant.

For a normalized positive-frequency spectral probability density `q(w)` with mean excitation angular frequency

`wbar=int_0^infinity w q(w)dw`,

the continuum maximal quantum Fisher-retention spectrum is

`G_Q(nu)=2 int_0^infinity q(w)q(w+nu)/[q(w)+q(w+nu)] dw`, `nu>0`,

with even extension to negative `nu`.

The sharp area theorem is

`boxed: int_0^infinity G_Q(nu)dnu <= (pi/2) wbar`,

hence

`boxed: int_R G_Q(nu)dnu <= pi wbar = pi Ebar^+/hbar`.

The constant `pi/2` on the positive side is sharp as a supremum. Consequently a detector retaining source-normalized Fisher fraction at least `q0` over ordinary temporal bandwidth `B` must obey

`boxed: Ebar^+ >= (2/pi) h B q0`.

Because WP10 bounds the encoded-state QFI before any detector is selected, every parameter-independent quantum detector and arbitrary coherent memory inherits the same mode-by-mode/area upper bound whenever the continuum encoding is obtained as the controlled periodic limit below.

---

## 1. Controlled periodic approximation

Let `q(w)` be nonnegative, continuous, compactly supported on `[0,infinity)`, normalized by

`int q(w)dw=1`.

Let the frequency spacing be `delta>0`, corresponding to period

`T_delta=2*pi/delta`.

Define discrete bin probabilities

`q_n^(delta)=int_{n delta}^{(n+1)delta} q(w)dw`.

These form a valid periodic positive-energy pure-state population profile. WP10 gives the discrete maximal mode retention

`G_delta(k)=2 sum_n q_n^(delta) q_{n+k}^(delta)/[q_n^(delta)+q_{n+k}^(delta)]`.

Define the piecewise-constant bin average

`q_delta(w)=q_n^(delta)/delta`

on bin `[n delta,(n+1)delta)`.

Using the homogeneity

`h(delta a,delta b)=delta h(a,b)`, where `h(a,b)=ab/(a+b)`,

we have the exact representation

`G_delta(k)=2 int_0^infinity h(q_delta(w),q_delta(w+k delta))dw`.

For continuous compactly supported `q`, `q_delta->q` uniformly. Thus whenever `k(delta) delta -> nu>=0`, dominated/uniform convergence gives

`boxed: G_delta(k(delta)) -> G_Q(nu)`

with

`G_Q(nu)=2 int_0^infinity h(q(w),q(w+nu))dw`.

This establishes the continuum spectrum as a controlled large-period limit rather than as a formal trace-class `infinite uniform-time twirl`.

---

## 2. Continuum area as a symmetric density functional

The positive-frequency area is

`A_+[q]=int_0^infinity G_Q(nu)dnu`.

Changing variables `y=w+nu` gives

`A_+[q]=2 int_{0<=x<y<infinity} h(q(x),q(y)) dxdy`.

Because the kernel is symmetric and the diagonal has zero two-dimensional measure,

`boxed: A_+[q]= int_0^infinity int_0^infinity h(q(x),q(y)) dxdy`.

Thus `A_+[q]` depends only on the distribution of the values of `q`, not on where those values are arranged on the positive-frequency axis.

For the discrete approximants one also has

`delta sum_{k>=1}G_delta(k)`

`= int int h(q_delta(x),q_delta(y))dxdy - delta/2`,

because the omitted same-bin diagonal contribution equals `delta/2` after normalization. Therefore

`boxed: delta sum_{k>=1}G_delta(k) -> A_+[q]`.

Meanwhile

`delta nbar_delta = sum_n (n delta) q_n^(delta) -> wbar`,

with error bounded by `delta`.

Hence the continuum theorem is a genuine scaling limit of the exact periodic WP10 model.

---

## 3. Decreasing rearrangement reduces the energy moment

The functional

`A_+[q]=iint h(q(x),q(y))dxdy`

is invariant under measure-preserving rearrangements of `q` because its integrand depends only on the pair of density values.

Let `q*` be the decreasing rearrangement of `q` on `[0,infinity)`.

By the Hardy--Littlewood/bathtub rearrangement principle, because the coordinate weight `x` is increasing,

`int x q*(x)dx <= int x q(x)dx`.

Therefore the ratio `A_+[q]/wbar` is maximized by a nonincreasing density. It is enough to prove the inequality for decreasing `q`.

---

## 4. Layer-cake inverse profile

Assume first that `q` is smooth, positive on a finite interval, and strictly decreasing; the general regular case follows by approximation.

Define the superlevel-length/inverse profile

`r(s)= measure{x>=0:q(x)>s}`.

For decreasing `q`, the superlevel set is `[0,r(s))`.

Layer cake gives

`q(x)=int_0^infinity 1_{s<q(x)} ds`.

Hence the mean frequency is

`wbar=int_0^infinity x q(x)dx`

`=int_0^infinity ds int_0^{r(s)} x dx`

`= (1/2) int_0^infinity r(s)^2 ds`.

Thus

`boxed: wbar=(1/2)||r||_2^2`.

---

## 5. Transform of the harmonic-mean functional

For smooth strictly decreasing `q`, use `s=q(x)` and `t=q(y)`. If `w(s)=-r'(s)>=0`, then

`A_+[q]=iint [s t/(s+t)] w(s)w(t) dsdt`.

Let

`K0(s,t)=st/(s+t)`.

Twice integrating by parts, with vanishing boundary terms under compact-support/regularity assumptions, gives

`A_+[q]=iint L(s,t) r(s)r(t) dsdt`,

where

`boxed: L(s,t)=partial_s partial_t K0(s,t)=2st/(s+t)^3`.

The problem is therefore the `L2(0,infinity)` operator norm of the symmetric homogeneous integral operator

`(Tr)(s)=int_0^infinity [2st/(s+t)^3]r(t)dt`.

---

## 6. Exact Mellin multiplier and operator norm

The kernel is homogeneous of degree `-1`. The unitary Mellin transform diagonalizes the operator. Acting formally on the generalized Mellin eigenfunction

`s^{-1/2+i xi}`

gives multiplier

`lambda(xi)`

`=int_0^infinity [2u/(1+u)^3] u^{-1/2+i xi}du`

`=2 B(3/2+i xi,3/2-i xi)`

`=|Gamma(3/2+i xi)|^2`.

Using

`|Gamma(1/2+i xi)|^2=pi/cosh(pi xi)`

and `Gamma(3/2+i xi)=(1/2+i xi)Gamma(1/2+i xi)`, obtain

`boxed: lambda(xi)=pi(1/4+xi^2)/cosh(pi xi)`.

This is nonnegative. Moreover

`cosh(pi xi)>=1+(pi^2 xi^2)/2 >=1+4xi^2`,

so

`lambda(xi)<=pi/4`,

with equality only at `xi=0` in the generalized spectrum.

Therefore

`boxed: ||T||_{L2->L2}=pi/4`.

This is a Carleman/Mellin-type operator calculation; the transform method is classical mathematics and must not itself be claimed as novel.

---

## 7. Sharp continuum area theorem

Using the operator norm,

`A_+[q]=<r,Tr>`

`<= (pi/4)||r||_2^2`

`= (pi/2) wbar`.

Therefore

`boxed: int_0^infinity G_Q(nu)dnu <= (pi/2) wbar`.

Since the retention spectrum is even,

`boxed: int_R G_Q(nu)dnu <= pi wbar`.

In energy units with excess excitation energy

`Ebar^+=hbar wbar`,

`boxed: int_R G_Q(nu)dnu <= pi Ebar^+/hbar`.

This improves the crude continuum limit of the discrete WP10 inequality

`int_R G_Q<=4Ebar^+/hbar`.

---

## 8. Sharpness

The multiplier norm `pi/4` is the sharp operator norm but is not attained by an `L2` eigenfunction; the generalized extremal is the scale-invariant profile

`r(s) proportional s^{-1/2}`.

This corresponds to a critical decreasing spectral density with `q(w) proportional w^{-2}` behavior.

An explicit approximating family is the normalized truncated critical Pareto density

`q_R(w)=C_R/(1+w)^2`, `0<=w<=R`,

with

`C_R=(1+R)/R`.

Let `L=1+R`. Its mean is

`wbar_R=C_R [ln L + 1/L -1]`.

Its area functional is

`A_+[q_R]=C_R I(L)`,

where

`I(L)=2 int_1^L [arctan(L/u)-pi/4] du/u`

`=2 int_1^L [arctan z-pi/4] dz/z`.

As `L->infinity`,

`I(L)=(pi/2)ln L+O(1)`,

while

`wbar_R=ln L+O(1)`.

Hence

`boxed: A_+[q_R]/wbar_R -> pi/2`.

Thus the continuum constant is sharp as a supremum over finite-mean densities.

The maximizing sequence develops an increasingly long near-critical `1/w^2` tail; no finite-mean normalized density exactly attains the supremum.

---

## 9. Flat-band inverse law

If a final detector has source-normalized retention

`G_Y(2*pi f)>=q0`

for all ordinary frequencies `|f|<=B`, and its classical FI is bounded mode-by-mode by the continuum encoded-state QFI spectrum, then

`int_R G_Y(nu)dnu >=4*pi B q0`.

Using

`int_R G_Y<=int_R G_Q<=pi Ebar^+/hbar`,

obtain

`4*pi Bq0 <= pi Ebar^+/hbar`.

Therefore

`boxed: Ebar^+ >=4 hbar B q0 = (2/pi) h B q0`.

This is the sharp continuum arbitrary-measurement inverse law implied by the current theorem.

Compare:

- covariant continuous timestamp WP07: `E^+>=hBq0`;
- arbitrary-measurement continuum WP12: `E^+>=(2/pi)hBq0`.

Thus the maximal possible advantage of unrestricted quantum readout in this area metric is bounded by a factor `pi/2` relative to the sharp covariant-timestamp resource law.

Whether this factor can be approached operationally by a sequence of actual measurements over a broad band is a separate attainability question.

---

## 10. Detector independence

WP12 inherits WP10's key detector-independence property.

For every finite periodic approximation, the parameter is encoded in the quantum state before any detector is chosen. Any parameter-independent apparatus state, joint quantum channel, coherent memory, external reference, and final measurement are downstream of QFI and cannot exceed the mode-wise bound.

Taking the controlled continuum limit preserves the area upper bound for any corresponding sequence of final detectors whose modewise classical Fisher retentions converge appropriately.

Thus WP12 is not a covariant-detector theorem. The covariance/randomization is in the **source encoding of latent event time**, while the subsequent detector can be arbitrary and quantum.

---

## 11. Relation to WP09

There is no contradiction with the fixed-mean-energy divergent deterministic-shift QFI family of WP09.

WP09 estimates a coherent global time-shift parameter. WP12 estimates Fourier amplitudes of a **random event-time distribution**. Baseline randomization removes absolute phase coherence and converts the relevant resource into overlap between positive-energy sectors separated by each temporal Fourier mode.

This is why mean energy can bound the integrated random-time mode information even though it cannot bound arbitrary deterministic-shift QFI.

---

## 12. Prior-art boundary

The following ingredients are standard/prior art:

- SLD QFI and its harmonic-mean denominator;
- `U(1)` modes of asymmetry;
- QFI monotonicity;
- decreasing rearrangement/Hardy--Littlewood principles;
- layer-cake representations;
- Mellin diagonalization of homogeneous integral operators / Carleman-type bounds.

Targeted searches have not located the combined theorem

`int_R G_Q(nu)dnu <= pi Ebar^+/hbar`

for Fourier modes of a random temporal-distribution encoding, nor the inverse information-bandwidth law

`Ebar^+ >= (2/pi) h B q0`.

The integral inequality for the harmonic-mean density functional may itself exist in analysis literature under another formulation. Do **not** claim mathematical priority for the `pi/2` functional inequality until a dedicated analysis-literature search is completed.

---

## 13. Remaining hostile gates

1. Write the periodic-to-continuum convergence proof at publication rigor beyond continuous compact support, ideally for general densities with finite first moment by approximation/lower-semicontinuity.
2. Search analysis literature specifically for the sharp inequality
   `iint q(x)q(y)/(q(x)+q(y)) dxdy <= (pi/2) int xq(x)dx`
   after decreasing rearrangement.
3. Search quantum phase-noise/group-distribution estimation literature for the exact continuum QFI functional.
4. Determine operational attainability of the `pi` two-sided area constant by actual measurements, not only QFI.
5. Extend the physically clean input model from quantum-marked events to a second-quantized bosonic optical field.
6. Determine whether coherent/multiphoton/entangled inputs can violate the single-excitation mean-energy constant or require a different many-body resource.
7. Only after these gates decide whether WP10--WP12 justify a standalone manuscript.

## Decision

The continuum limit is no longer merely conjectural for regular densities, and the sharp constant is substantially better than the crude discrete bound:

`boxed: int_R G_Q(nu)dnu <= pi Ebar^+/hbar`.

This is currently the strongest measurement-independent Planck-scale temporal-information resource law in the program.
