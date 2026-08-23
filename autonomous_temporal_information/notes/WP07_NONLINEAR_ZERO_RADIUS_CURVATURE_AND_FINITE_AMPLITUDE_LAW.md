# WP07 — Nonlinear zero-radius curvature law and finite-amplitude spectral discrimination

**Date:** 2026-08-22

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** analytic PASS for the support-to-kernel curvature theorem and for the two-sector finite-amplitude discrimination theorem. These results materially narrow the `R_lin=0` loophole but do **not** yet constitute a universal arbitrary-waveform energy theorem. The underlying second-order PSD-cone and block-coherence inequalities are prior art; candidate novelty is the frequency-resolved temporal-information/resource interpretation and its connection to the earlier coherent-sideband no-go. Priority remains **unverified, not certified**.

## 1. Problem left by WP02/WP06

WP02/WP06 control a first-order tangent by its nonzero linear physical radius:

`(R_lin^2/4)[Tr F_N/N] <= spectral tail`.

This becomes vacuous when `R_lin=0`.

The canonical mechanism is a rank-deficient baseline. A smooth exact nonlinear family can create an off-diagonal amplitude into a previously empty sector at first order while supplying the population required for positivity only at second order.

The earlier Grand-Challenge coherent-sideband no-go (`grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`) identified exactly this mechanism: local QFI remains finite at arbitrarily high sideband frequency while sideband energy enters quadratically in the modulation parameter.

WP07 asks whether the missing second-order resource can be bounded sharply.

## 2. Minimal exact zero-radius family

Take

`rho0=|0><0|`

and

`|psi(x,y)>=sqrt(1-c^2(x^2+y^2))|0> + c(x+i y)|1>`

for `c^2(x^2+y^2)<1`.

The first derivatives at the origin are

`D_x=c(|1><0|+|0><1|)`,

`D_y=-i c|1><0|+i c|0><1|`.

The affine family

`rho0+xD_x+yD_y`

is nonpositive for every nonzero radius, so

`R_lin=0`.

Nevertheless the exact nonlinear pure-state family is physical. Its upper-level population is

`T_U(x,y)=c^2(x^2+y^2)`.

The QFI matrix at the origin is

`F_Q=4c^2 I_2`.

Thus the missing resource is manifestly second order:

`F_Q = 2 Hess[T_U](0)`.

The general theorem below shows that this equality is the sharp boundary case of a PSD-cone inequality.

## 3. Second-order PSD constraint at a rank-deficient baseline

Let

`rho(theta)=rho0 + theta D + (theta^2/2) C + o(theta^2)`

be a two-sided `C^2` curve of density operators, physical for all sufficiently small positive and negative `theta`.

Let

`P=supp(rho0)`, `Q=I-P`,

and let

`R=P rho0 P`

which is strictly positive on `P`.

Two-sided positivity first implies

`Q D Q=0`.

Define the support-to-kernel tangent block

`K=Q D P`.

In the decomposition `P directsum Q`, the state has the block expansion

`rho(theta)`

`= [[R+O(theta), theta K^dagger+O(theta^2)],`

`   [theta K+O(theta^2), (theta^2/2)Q C Q+o(theta^2)]]`.

For sufficiently small `theta`, the `P` block is invertible. Positivity of the Schur complement therefore requires

`(theta^2/2)Q C Q - theta^2 K R^(-1) K^dagger + o(theta^2) >=0`.

Dividing by `theta^2` and taking the limit gives the exact necessary curvature condition

> **Second-order support-creation inequality**
>
> `Q C Q >= 2 K R^(-1) K^dagger`.

Equivalently,

> `Q rho''(0) Q >= 2 Q rho'(0) P (P rho0 P)^(-1) P rho'(0) Q`.

The coefficient `2` is sharp. Any unitary boundary rotation

`rho(theta)=exp(theta G) rho0 exp(-theta G)`

with an off-diagonal anti-Hermitian generator `G` attains equality in the newly occupied kernel block.

### Prior-art boundary

This matrix inequality is not claimed as new mathematics. It is a direct instance of the established second-order tangent geometry of the positive-semidefinite cone. Classical semidefinite-optimization literature gives curvature terms involving `V Y^dagger V` and exact second-order tangent-set conditions; see, e.g.,

- A. Shapiro, *First and second order analysis of nonlinear semidefinite programs*, Math. Programming 77, 301--320 (1997);
- J. F. Bonnans, R. Cominetti, and A. Shapiro, *Second order optimality conditions based on parabolic second order tangent sets*, SIAM J. Optim. 9, 466--492 (1999);
- later elementary treatments of the same semidefinite-cone curvature term via second subderivatives.

The research question here is what this established cone geometry implies for **frequency-resolved temporal information and energy/resource supply**.

## 4. Boundary QFI is bounded by upper-sector population curvature

Assume the relevant first-order tangent is entirely support-to-upper-kernel at the requested resource sector:

`P D P=0`,

`K=P_U D P`,

with `P_U<=Q`.

The SLD QFI of this one-parameter model at the baseline is

`F_Q = 4 Tr(K R^(-1) K^dagger)`.

Compressing the support-creation inequality to `P_U` and taking the trace gives

`Tr(P_U C) >= 2 Tr(K R^(-1)K^dagger)`.

Define the upper-sector population

`T_U(theta)=Tr(P_U rho(theta))`.

Because the sector is empty at the baseline and has no first-order diagonal population,

`T_U(0)=0`, `T_U'(0)=0`,

and

`T_U''(0)=Tr(P_U C)`.

Therefore

> **Zero-radius Fisher--curvature law**
>
> `F_Q(0) <= 2 T_U''(0)`.

For any POVM,

`F_M(0)<=F_Q(0)`, so

> `F_M(0)/4 <= T_U''(0)/2`.

For `N` independently encoded copies and an arbitrary entangled collective POVM, QFI additivity gives

> `(1/4)[F_N(0)/N] <= J_U^(2)`,
>
> `J_U^(2):=T_U''(0)/2`.

Thus the natural zero-radius replacement for a zeroth-order survival probability is a **quadratic spectral supply**: half the curvature with which the previously empty upper sector is populated.

The theorem is exactly saturated by the minimal pure-state family of Sec. 2 and by arbitrary fixed-rank unitary rotations from the support into the kernel.

## 5. Multiparameter / two-quadrature matrix form

Let `theta=(theta_1,...,theta_d)` and let

`H_U,ij = partial_i partial_j T_U(0)`

be the Hessian of upper-sector population.

For every real direction `u`, the one-parameter curve `theta=t u` obeys the previous theorem. Hence, in Loewner order,

> `F_Q(0) <= 2 H_U`.

For any collective POVM on `N` copies,

> `F_N(0)/N <= 2 H_U`.

Define the quadratic spectral-supply matrix

`S_U^(2)=H_U/2`.

Then

> `F_N(0)/(4N) <= S_U^(2)`.

For a two-quadrature temporal mode,

> `Tr F_N(0)/(4N) <= (1/2) Delta T_U(0)`.

This is coordinate-consistent at a zero-population sector: because `T_U(0)=0` and `grad T_U(0)=0`, the Hessian transforms tensorially under smooth local reparameterizations.

## 6. Frequency-resolved energetic interpretation

Suppose `P_U` is an upper endpoint sector whose excitation requires at least an energy quantum `hbar nu` relative to the relevant lower endpoint/resource reference.

Define the **quadratic upper-tail energy supply**

`E_U^(2)(nu) := (hbar nu/2) T_U''(0)`

for a one-parameter tangent, or the corresponding Hessian-weighted object in the multiparameter case.

Then

> `E_U^(2)(nu) >= (hbar nu/4)[F_N(0)/N]`.

This is deliberately **not** called a bound on the total energy curvature `d^2 Tr(H rho_theta)/dtheta^2`. Other second-order population redistributions can compensate in the total mean-energy derivative. The theorem controls the physically relevant **high-energy endpoint population that must be synthesized**.

That distinction is essential for a general theorem.

## 7. The old coherent-sideband counterexample saturates the curvature coefficient

WP14 used a coherent carrier with one newly synthesized upper sideband:

`alpha_(n0+k)(epsilon)=epsilon A/2`,

with `Nbar=|A|^2`.

The sideband occupation is

`n_sb(epsilon)=epsilon^2 Nbar/4`,

so

`n_sb''(0)=Nbar/2`.

The coherent-state QFI is

`F_Q=Nbar`.

Therefore

> `F_Q = 2 n_sb''(0)`.

The coherent-sideband family that destroyed any baseline-energy-only theorem **exactly saturates the zero-radius curvature coefficient** when the newly occupied sideband number is used as the spectral-supply observable.

This is a strong consistency check: the new law charges precisely the resource that WP14 showed baseline energy omits.

The high sideband frequency still enters through the energy per synthesized sideband excitation. Thus fixed local information at increasing sideband frequency requires a proportionally increasing quadratic spectral-energy supply even though the baseline source energy is unchanged.

## 8. Exact finite-amplitude two-sector coherence bound

The differential curvature law still uses derivatives. A complementary finite-amplitude statement follows directly from positivity.

Let a density operator be decomposed into two orthogonal endpoint sectors `D` and `U`:

`rho = [[rho_D, C^dagger], [C, rho_U]]`.

Define

`q_D=Tr(rho_D)`, `q_U=Tr(rho_U)`.

Positivity of the block matrix implies the standard contraction factorization

`C=rho_U^(1/2) K rho_D^(1/2)`, `||K||<=1`.

Therefore

> `||C||_1^2 <= q_D q_U <= min(q_D,q_U)`.

This inequality, and closely related block-coherence tradeoffs, are established prior art and are not claimed as new.

## 9. Helstrom discrimination of a finite relative-phase change

Let `rho_phi` differ only by the relative phase of the endpoint coherence:

`C -> exp(i phi) C`,

with the diagonal blocks fixed.

For two phases `phi_1,phi_2`, direct singular-value evaluation of the off-diagonal difference gives

`D_tr(rho_phi1,rho_phi2)`

`= 2 |sin[(phi_1-phi_2)/2]| ||C||_1`,

where `D_tr=(1/2)||rho-sigma||_1` is the operational trace distance.

Hence

> `D_tr^2 / {4 sin^2[(Delta phi)/2]} <= q_D q_U`.

For the maximally separated phase pair `Delta phi=pi`,

> `D_tr^2/4 <= q_D q_U <= min(q_D,q_U)`.

Since trace distance is exactly the arbitrary-POVM binary-discrimination resource, this is a genuinely finite-amplitude measurement-independent statement.

With equal priors, the optimal Helstrom success probability is

`P_succ=(1+D_tr)/2`.

## 10. Autonomous relational finite-amplitude corollary

Interpret `D` and `U` as two joint clock--signal endpoint sectors connected by an exact exchange gap `nu`:

- in `D`, the clock carries the donor gap;
- in `U`, the signal carries the receiver gap.

Then

`q_D <= T_C(nu)`,

`q_U <= T_S(nu)`.

Therefore the phase-pair theorem gives

> `D_tr^2/4 <= min{T_C(nu),T_S(nu)}`.

Consequently

> `Ebar_C^+ >= (hbar nu/4) D_tr^2`,
>
> `Ebar_S^+ >= (hbar nu/4) D_tr^2`,
>
> `Ebar_C^+ + Ebar_S^+ >= (hbar nu/2) D_tr^2`.

This is a finite-amplitude nonlinear analogue of the WP03/WP06 two-sided survival principle for the restricted two-endpoint phase experiment. It requires no nonzero `R_lin` and no local Fisher approximation.

The ingredients are standard block positivity and Helstrom theory; the autonomous temporal-resource packaging is the candidate contribution.

## 11. What WP07 does and does not solve

### Closed

The statement

> `R_lin=0` means no spectral resource law is possible

is false.

For smooth support-creating families, positivity itself forces a second-order resource:

`first-order Fisher information <= second-order upper-sector population creation`.

The exact coherent-sideband no-go family saturates the coefficient.

Finite-amplitude endpoint coherence is likewise bounded by endpoint populations and therefore by both local energy tails in an autonomous exchange experiment.

### Still open

WP07 does **not** yet establish one universal scalar law for every arbitrary nonlinear waveform family.

Remaining issues:

1. a general tangent may contain both support-to-support and support-to-kernel pieces;
2. several energy gaps and endpoint sectors can coexist and interfere in one parameter direction;
3. total mean-energy curvature can contain compensating second-order redistributions, so the invariant resource is spectral injection rather than naively `E''(0)`;
4. binary finite-phase discrimination does not reproduce the near-unit Fisher-retention divergence of WP04/WP05, nor should it: a finite-dimensional system can perfectly distinguish some discrete phase pairs at finite energy;
5. an unrestricted autonomous control Hamiltonian can still supply the required curvature unless its generator/action resource is charged.

## 12. Prior-art collisions identified

The following are established and must not be claimed as new:

- second-order tangent/curvature formulas for the PSD cone, including the `V Y^dagger V` curvature term;
- QFI/Bures subtleties at rank-changing points and Hessian corrections associated with singular statistical models (e.g. D. Safranek, Phys. Rev. A 95, 052320 (2017), DOI `10.1103/PhysRevA.95.052320`);
- positivity factorization of PSD block matrices;
- trace-norm/block-coherence tradeoffs between orthogonal subspaces;
- Helstrom trace-distance discrimination;
- ordinary phase-estimation and asymmetry/coherence resource theory.

A future manuscript must present WP07 as a **spectral temporal-information consequence** of these ingredients, not as a new theory of the PSD cone or boundary QFI.

## 13. Significance for the grand program

The autonomous program now has a clean two-regime picture.

### Interior / finite-radius regime

`local Fisher x R_lin^2 <= pre-existing spectral survival`.

### Boundary / zero-radius regime

`local Fisher <= quadratic creation of previously absent spectral population`.

Thus arbitrary waveform synthesis does not make high-frequency information free. It changes **which order of the physical resource expansion pays for it**.

This is the most important conceptual result of WP07.

For coherent-sideband synthesis, the resource that escaped the baseline-energy theorem is exactly the second-order sideband population/energy injection.

## 14. Next work

The highest-value next target is a **unified support/interior theorem** for an arbitrary exact-gap tangent:

1. decompose the tangent into support-to-support and support-to-kernel components;
2. combine WP06 pre-existing-tail control with the WP07 quadratic-injection control without double counting;
3. seek a finite-amplitude version for a full phase orbit, not only a binary phase pair;
4. determine whether the resulting quantity has a sharp Herglotz/retention law and whether near-perfect continuous relative-time recovery still forces divergent autonomous energy;
5. extend the coherent-state sideband example from a consistency check to a general bosonic synthesis theorem using sideband-number/energy creation;
6. perform a deeper priority audit against boundary quantum metrology, second-order quantum resource theory, phase-covariant discrimination, and finite-reference-frame simulation.
