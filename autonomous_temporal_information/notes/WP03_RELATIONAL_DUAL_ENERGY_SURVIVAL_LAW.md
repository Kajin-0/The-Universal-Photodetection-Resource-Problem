# WP03 — Relational dual-energy survival law for globally stationary temporal information

**Date:** 2026-08-22

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** analytic theorem PASS at the local robust-Fisher level; targeted priority screen has not identified an exact predecessor. Priority remains **unverified, not certified**.

## 1. Motivation: global asymmetry is not the autonomous clock resource

A truly autonomous clock--signal description need not possess any global time-translation asymmetry.

In Page--Wootters-type relational constructions, the joint clock--system state may be globally stationary under

`H_tot = H_C + H_S`,

while nontrivial evolution appears only relationally, conditioned on the clock. This is established prior art and is not a novelty claim here.

Therefore a universal autonomous temporal-information law cannot simply say

`temporal information <= global time-translation asymmetry`.

That quantity may vanish identically while the subsystems retain useful relative-time correlations.

The correct elementary object is instead **energy-exchange coherence**: the signal moves up by a gap while the clock moves down by the same gap, keeping total energy unchanged.

## 2. Relational exact-gap tangent

Let clock `C` and signal `S` have semibounded Hamiltonians with participating lower edges `E_C,*` and `E_S,*`.

Assume the baseline state `rho0` on `C tensor S` commutes separately with both local Hamiltonians:

`[rho0,H_C]=[rho0,H_S]=0`.

This allows arbitrary classical correlations and degeneracies inside joint local-energy sectors.

Let `A_nu` be a positive relative-energy-exchange tangent satisfying

`[H_S,A_nu] = + hbar nu A_nu`,

`[H_C,A_nu] = - hbar nu A_nu`,

for `nu>0`.

Then

`[H_C+H_S,A_nu]=0`.

Define quadratures

`D_c=(A_nu+A_nu^dagger)/2`,

`D_s=(A_nu-A_nu^dagger)/(2i)`.

Thus the entire affine local experiment

`rho_(eps_c,eps_s)=rho0+eps_c D_c+eps_s D_s`

is globally stationary under total time translations. The parameter is encoded in a **relational degree of freedom**, not in global asymmetry.

Because every state in the family commutes with `H_C+H_S`, an arbitrary final POVM may be twirled with respect to total time translations without changing any outcome probabilities. Hence the theorem does not require a free external timing reference at readout.

## 3. Linear physical radius

Use the WP02 tangent robustness

`R_lin = sup { R : rho0+eps_c D_c+eps_s D_s >=0 for all eps_c^2+eps_s^2<=R^2 }`.

If `R_lin=0`, the theorem is vacuous and the nonlinear/curvature loophole remains a separate problem.

For `R_lin>0`, define the robust per-copy Fisher weight

`K_N(nu) := (R_lin^2/4) [Tr F_N^(nu)/N]`,

where `F_N^(nu)` is the two-quadrature classical Fisher block of any joint POVM on `N` independently encoded copies.

## 4. Signal-side bound

Viewed with respect to `H_S`, `A_nu` is an exact positive Bohr-gap tangent of frequency `nu`, while `rho0` is stationary.

WP02 therefore gives

`K_N(nu) <= min(D_S,nu,U_S,nu) <= T_S(nu)`,

where

`T_S(nu)=Pr[(H_S-E_S,*)/hbar >= nu]`

is the signal upper energy survival probability in the baseline state.

## 5. Clock-side bound

With respect to `H_C`, the conjugate tangent `A_nu^dagger` is a positive `+nu` Bohr-gap tangent. Its two Hermitian quadratures are the same physical tangent plane, with the sine coordinate reversed; consequently `R_lin` and the Fisher trace are unchanged.

Applying WP02 to `A_nu^dagger` therefore gives

`K_N(nu) <= T_C(nu)`,

where

`T_C(nu)=Pr[(H_C-E_C,*)/hbar >= nu]`.

## 6. Relational dual-survival theorem

Combining the two local-generator views gives:

> **Relational dual-energy survival law**
>
> For every finite `N` and every joint POVM on `N` independent copies of the globally stationary clock--signal experiment,
>
> `K_N(nu) <= min{T_C(nu),T_S(nu)}`,
>
> i.e.
>
> `(R_lin^2/4) [Tr F_N^(nu)/N] <= min{T_C(nu),T_S(nu)}`.

The result is detector/measurement independent and allows entangled collective readout.

It says that relational temporal information at gap `nu` must be backed **twice**: the signal needs population high enough to receive the energy exchange, and the clock needs population high enough to donate the matching gap.

Global stationarity does not remove the resource cost; it converts the resource from global asymmetry into matched local energy survival.

## 7. Mean-energy corollaries

Let

`Ebar_C^+ = Tr[rho0 (H_C-E_C,*)]`,

`Ebar_S^+ = Tr[rho0 (H_S-E_S,*)]`.

Since

`T_X(nu) <= Ebar_X^+/(hbar nu)`

for `X=C,S`, the dual-survival theorem gives both

`Ebar_C^+ >= hbar nu K_N(nu)`

and

`Ebar_S^+ >= hbar nu K_N(nu)`.

Therefore

> `Ebar_C^+ + Ebar_S^+ >= 2 hbar nu K_N(nu)`
>
> `= (hbar nu R_lin^2/2) [Tr F_N^(nu)/N]`.

This is an autonomous **two-sided energetic cost** for relational temporal Fisher information.

## 8. All-mode budget on a common lattice

Suppose a family of exact energy-exchange tangent planes is indexed by integer gaps `k omega0`, each with its own linear radius `R_lin,k` and Fisher block `F_N^(k)`.

Define

`K_N(k)=(R_lin,k^2/4)[Tr F_N^(k)/N]`.

Modewise,

`K_N(k)<=min{T_C(k),T_S(k)}`.

Summing and using the tail-sum identity for each subsystem gives

`sum_(k>=1) K_N(k)`

`<= min{ sum_(k>=1)T_C(k), sum_(k>=1)T_S(k) }`

`= min{nbar_C,nbar_S}`.

Thus

> **Relational all-mode budget**
>
> `sum_(k>=1) (R_lin,k^2/4)[Tr F_N^(k)/N] <= min(nbar_C,nbar_S)`.

In energy units,

`Ebar_C^+ + Ebar_S^+ >= 2 hbar omega0 sum_(k>=1) K_N(k)`.

This statement is modewise-operational; it does not require one common POVM across different `k`, though it also applies if one common record is used.

## 9. Controlled continuum version

For controlled lattice-to-continuum families with local energy measures `mu_C,mu_S` and robust information density `K(nu)`, the pointwise law becomes

`K(nu) <= min{S_C(nu),S_S(nu)}`.

If both local mean excess frequencies are finite,

`int_0^infinity K(nu) dnu <= min{Ebar_C^+/hbar,Ebar_S^+/hbar}`.

Equivalently,

`Ebar_C^+ + Ebar_S^+ >= 2 hbar int_0^infinity K(nu)dnu`.

As in Rev11, this is a controlled-limit statement rather than an unconditional direct theorem for arbitrary continuous-spectrum relational experiments.

## 10. Minimal two-qubit exchange model

Take clock and signal qubits with the same gap `hbar nu` and basis

`|00>, |10>, |01>, |11>`

(clock label first).

Choose baseline probabilities

`rho0 = (1-a-b)|00><00| + a|10><10| + b|01><01|`

with `a,b>0`, `a+b<1`.

Let

`A_nu=2c |01><10|`.

This raises the signal by `hbar nu` and lowers the clock by the same amount, so the tangent is globally stationary.

The linear physical radius is

`R_lin^2 = ab/c^2`.

An equatorial covariant POVM on the one-excitation subspace plus a separate ground-state outcome gives

`Tr F_1 = 4 c^2/(a+b)`.

Hence

`K_1 = ab/(a+b)`.

The dual tails are

`T_C(nu)=a`,

`T_S(nu)=b`,

and indeed

`ab/(a+b) <= min(a,b)`.

If one side is the bottleneck, e.g. `a/b ->0`, then

`K_1/T_C ->1`,

showing the **dual minimum-tail coefficient is pointwise sharp** when one subsystem is resource limiting.

For `a=b`, the simple two-qubit measurement yields `K=a/2`; simultaneous saturation of both local tails is not achieved by this minimal model. The sharp total-energy prefactor remains open.

## 11. Relation to Page--Wootters and prior art

Page--Wootters and related relational-time frameworks establish that a globally stationary state can encode nontrivial internal evolution through clock--system correlations. Recent work continues to analyze finite clocks, interactions, time of arrival, and informational/conditional dynamics.

The present theorem does **not** claim relational time itself is new. Its candidate contribution is narrower and quantitative:

> robust classical Fisher information encoded in a globally time-symmetric energy-exchange mode is bounded simultaneously by the clock and signal energy survival functions, for arbitrary finite-copy collective measurements.

Targeted searches found work on Page--Wootters relational time, Fisher-geometric clock quality, energy--time uncertainty, finite-clock errors, and relative-phase estimation, but did not identify this specific dual survival/tail theorem.

Priority remains **unverified, not certified**.

## 12. Why this matters for the autonomous grand question

WP01 showed that global asymmetry/resource-frame mode support is insufficiently novel and conceptually incomplete for a closed autonomous description.

WP02 showed that local Fisher alone is too local unless tangent robustness is charged.

WP03 now shows that when temporal information is encoded in a genuinely autonomous globally stationary relation, the resource naturally becomes **two-sided local spectral support** rather than global asymmetry.

This suggests a broader principle:

> Autonomous temporal information is an energy-exchange resource. A usable relative temporal mode must be backed by matched spectral resources on both sides of the relational cut.

Whether this extends beyond separately stationary baselines and nonzero linear tangent radius is now the central open problem.

## 13. Next work

WP04 priorities:

1. derive the sharp total-energy coefficient for relational exchange, beyond the simple sum of two one-sided bounds;
2. search for equality/extremizer families on finite fixed-total-energy chains;
3. test whether a Herglotz/positive-definite consistency law exists for one common relational record across multiple exchange gaps;
4. extend from separately stationary baselines to pre-existing relationally coherent Page--Wootters history states;
5. attack the `R_lin=0` nonlinear synthesis loophole in a globally stationary setting;
6. perform a deeper priority audit against quantitative WAY, clock synchronization, and relational-phase metrology.
