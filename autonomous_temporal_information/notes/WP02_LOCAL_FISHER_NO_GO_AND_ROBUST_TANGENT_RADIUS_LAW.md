# WP02 — Local-Fisher no-go and robust tangent-radius Fisher-survival law

**Date:** 2026-08-22

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** analytic theorem PASS; targeted priority search has not identified an exact predecessor. Priority is **unverified, not certified**.

## 1. Why local Fisher information alone cannot be universally energy-bounded

A general temporal-information law cannot simply replace the Rev11 source model by an arbitrary smooth quantum statistical model while retaining a bound depending only on baseline mean energy.

Consider a two-level Hamiltonian

`H_nu = hbar nu |1><1|`

with baseline state

`rho0 = (1-p)|0><0| + p|1><1|`,

where

`p = E/(hbar nu)`

for `nu > E/hbar`. The baseline mean excess energy is exactly `E`, independent of `nu`.

Let `c>0` be fixed and define the two-parameter affine family

`rho_(x,y) = rho0 + c x sigma_x + c y sigma_y`.

Equivalently, with

`A = 2c |1><0|`,

`D_c=(A+A^dagger)/2=c sigma_x`,

`D_s=(A-A^dagger)/(2i)=c sigma_y`,

we have

`rho_(x,y)=rho0+xD_c+yD_s`.

The family is physical exactly inside the disk

`x^2+y^2 <= R_nu^2`,

`R_nu^2 = p(1-p)/c^2`.

Under the free Hamiltonian, the two parameter tangents rotate at angular frequency `nu`. The covariant equatorial qubit POVM

`M(dtheta)=dtheta/(2pi) [ I + cos(theta)sigma_x + sin(theta)sigma_y ]`

has, at `(x,y)=(0,0)`, classical Fisher matrix with trace

`Tr F = 4 c^2`,

independent of `p` and hence independent of `nu`.

Therefore, at fixed baseline mean energy `E`, an arbitrarily high Bohr frequency can carry a fixed amount of **local** Fisher information. What changes is not the local Fisher metric but the physical parameter neighborhood:

`R_nu ~ sqrt(E/(hbar nu))/c`.

Thus no inequality of the form

`F(nu) <= f(E,nu)` with `f(E,nu)->0` as `nu->infinity`

can hold for arbitrary local state families without an additional global/robustness hypothesis.

This is a stronger obstruction than merely scaling a free Hamiltonian: even when baseline mean excess energy is fixed, the local tangent can retain fixed Fisher strength at arbitrarily large gap by shrinking its admissible amplitude domain.

## 2. Physical tangent radius

Let `rho0` be stationary with respect to a semibounded Hamiltonian `H`, and let `A_nu` be an operator in one positive Bohr-frequency mode `nu>0`:

`exp(-iHt/hbar) A_nu exp(+iHt/hbar) = exp(-i nu t) A_nu`.

Define the two Hermitian quadrature tangents

`D_c=(A_nu+A_nu^dagger)/2`,

`D_s=(A_nu-A_nu^dagger)/(2i)`.

Define the **linear physical tangent radius**

`R_lin(rho0,A_nu)`

as the supremum of `R>=0` such that

`rho0 + eps_c D_c + eps_s D_s >= 0`

for every `(eps_c,eps_s)` with

`eps_c^2+eps_s^2 <= R^2`.

If no nonzero disk is allowed, set `R_lin=0`.

This quantity depends only on the baseline point and tangent and measures how far the local tangent itself can be extended linearly while remaining inside quantum state space. It is not the parameter range of an arbitrary nonlinear family; a nonlinear family can remain physical even when its linear tangent radius is zero by supplying second-order population/curvature.

## 3. Numerical-radius characterization

Restrict to the support of `rho0` and define

`B_nu = rho0^(-1/2) A_nu rho0^(-1/2)`.

Because `rho0` is stationary, this operator has the same Bohr mode `nu`.

For `beta=eps_c-i eps_s`,

`rho0 + eps_c D_c + eps_s D_s`

is congruent on the support of `rho0` to

`I + ( beta B_nu + beta^* B_nu^dagger )/2`.

For any unit vector `psi`, minimization over the phase of `beta` gives

`1 - |beta| |<psi|B_nu|psi>|`.

Therefore the disk of radius `R` is positive iff

`R w(B_nu) <= 1`,

where `w(B)` is the numerical radius. Hence, when `R_lin>0`,

`R_lin = 1 / w(B_nu)`.

The classical numerical-radius inequality

`||B|| <= 2 w(B)`

then gives

`||B_nu|| <= 2/R_lin`.

The numerical-radius mathematics is prior art; see, e.g., Bhatia and Jain, *Linear Algebra and its Applications* 656, 463--482 (2023), DOI `10.1016/j.laa.2022.10.009`. The candidate contribution here is its use to connect physical tangent robustness to an arbitrary-measurement Fisher/energy tail law.

## 4. One-copy robust Fisher-survival theorem

Let `P_U,nu` project onto the upper endpoint sectors participating in the `+nu` mode and `P_D,nu` onto the corresponding lower endpoint sectors. Define

`U_nu = Tr(rho0 P_U,nu)`,

`D_nu = Tr(rho0 P_D,nu)`.

Because `B_nu` maps lower endpoints to upper endpoints,

`B_nu B_nu^dagger <= (4/R_lin^2) P_U,nu`,

`B_nu^dagger B_nu <= (4/R_lin^2) P_D,nu`.

For an arbitrary POVM effect `M_y`, let

`p_y=Tr(rho0 M_y)`,

`z_y=Tr(A_nu M_y)`.

Since

`A_nu=rho0^(1/2) B_nu rho0^(1/2)`,

Hilbert--Schmidt Cauchy--Schwarz gives

`|z_y|^2/p_y <= Tr[M_y rho0^(1/2) B_nu B_nu^dagger rho0^(1/2)]`.

Summing outcomes gives

`sum_y |z_y|^2/p_y <= 4 U_nu/R_lin^2`.

Applying the conjugate factorization gives the same expression with `D_nu`, so

`sum_y |z_y|^2/p_y <= 4 min(D_nu,U_nu)/R_lin^2`.

For the chosen quadrature normalization, the outcome derivatives are

`partial_c p_y = Re z_y`,

`partial_s p_y = Im z_y`,

so the two-quadrature Fisher-trace contribution is exactly `|z_y|^2/p_y`. Therefore

> **Robust tangent-radius Fisher-survival theorem, one copy**
>
> `R_lin^2 Tr F_1^(nu) / 4 <= min(D_nu,U_nu)`.

Equivalently,

`Tr F_1^(nu) <= 4 min(D_nu,U_nu)/R_lin^2`.

The factor 4 is the generic price of converting the numerical-radius constraint imposed by positivity into an operator-norm bound. It cannot generally be removed by the present argument; the two-level construction below asymptotically saturates it after the upper-tail step.

## 5. Arbitrary finite-copy collective measurements

For `N` independent copies, the complex tangent is

`A_(nu,N) = sum_(j=1)^N rho0^(tensor(j-1)) tensor A_nu tensor rho0^(tensor(N-j))`.

Factor

`A_(nu,N)=rho0,N^(1/2) B_(nu,N) rho0,N^(1/2)`,

with

`B_(nu,N)=sum_j B_nu^(j)`.

The same outcome-wise Cauchy--Schwarz argument yields a bound by

`Tr[rho0,N B_(nu,N) B_(nu,N)^dagger]`.

For `j != l`, the cross-copy terms vanish because

`Tr(rho0 B_nu)=Tr(A_nu)=0`

for nonzero Bohr mode. Hence

`Tr[rho0,N B_(nu,N)B_(nu,N)^dagger]`

`= N Tr(rho0 B_nu B_nu^dagger)`

`<= 4N U_nu/R_lin^2`.

Conjugation again gives `D_nu`. Therefore, for **any finite N and any joint POVM**, including entangled collective measurements,

> `R_lin^2 [Tr F_N^(nu)/N] / 4 <= min(D_nu,U_nu)`.

No asymptotic-estimation or separability assumption is used.

## 6. Semibounded-energy corollary

Let the participating lower energy edge be `E_*`, define excess frequency

`Omega=(H-E_*)/hbar >=0`,

and tail

`T(nu)=Pr(Omega>=nu)`.

Every upper endpoint of a `+nu` pair lies at excess frequency at least `nu`, so

`U_nu <= T(nu)`.

Thus

> **Robust Fisher-survival law**
>
> `R_lin^2 [Tr F_N^(nu)/N] / 4 <= T(nu)`.

If the baseline has finite mean excess energy

`Ebar+ = hbar <Omega>`,

then Markov/tail first moment gives

`T(nu) <= Ebar+/(hbar nu)`.

Consequently

> **Energy--frequency--Fisher--robustness law**
>
> `Ebar+ >= (hbar nu R_lin^2 / 4) [Tr F_N^(nu)/N]`.

This applies to arbitrary exact-gap tangents about a stationary baseline; it does **not** require the random-time source structure of Rev11.

## 7. Asymptotic sharpness of the coefficient after the tail step

Return to the two-level family of Sec. 1.

For

`A=2c|1><0|`,

`R_lin^2=p(1-p)/c^2`,

and the equatorial covariant POVM gives

`Tr F_1 = 4c^2`.

Therefore

`(R_lin^2/4) Tr F_1 = p(1-p)`.

The tail is `T(nu)=p`, so

`[(R_lin^2/4)Tr F_1]/T(nu) = 1-p -> 1`

as `p->0` (equivalently `nu->infinity` at fixed mean energy `E`).

The energy corollary likewise becomes

`(hbar nu R_lin^2/4) Tr F_1 = E(1-p) -> E`.

Thus the robust law is asymptotically saturated by the very family that destroys any energy-only local-Fisher bound.

This is conceptually useful: the missing resource is exactly the shrinking linear physical radius.

## 8. Relation to Rev11

Rev11 obtains a stronger coefficient for its special random-time tangent because the tangent factorizes through a **partial isometry of norm one** fixed by source structure. The general theorem here assumes only physical tangent robustness. Positivity controls the numerical radius, and the generic inequality `||B||<=2w(B)` produces the factor 4.

Therefore this result does not supersede Rev11. It explains why Rev11 can be stronger and identifies what must replace its source-specific factorization for arbitrary state synthesis.

## 9. Boundary: nonlinear synthesis

`R_lin` is a tangent robustness, not the radius of an arbitrary nonlinear physical family.

A coherent-sideband family can have a nonzero first-order off-diagonal tangent at a rank-deficient baseline while its exact nonlinear state remains physical because second-order population appears automatically. In such a case the linear tangent radius can be zero.

Thus a genuinely universal law for arbitrary nonlinear waveform synthesis must account for at least one of:

- finite parameter amplitude / finite distinguishability;
- curvature or higher-order state change;
- explicit preparation/control dynamics;
- a reference/clock/controller resource.

This is not a defect of the theorem; it isolates the precise mechanism by which purely local Fisher geometry evades energy bounds.

## 10. Priority audit to date

Targeted searches found standard work on:

- monotone quantum Fisher geometries;
- affine tangent spaces of density matrices;
- numerical-radius characterizations via positivity of block/operator matrices;
- asymmetry-mode monotones and reference-frame simulation.

No exact predecessor was identified for the combined statement

`physical linear tangent radius + arbitrary-POVM two-quadrature Fisher at a Bohr gap + semibounded energy tail + finite-copy collective measurement`.

This is a targeted screen only. Priority remains **unverified, not certified**.

## 11. Next work

WP03 should attack two directions in parallel:

1. **Autonomous conversion:** determine whether `R_lin` or a related robustness quantity is monotone/controlled when a finite reference frame converts time-symmetric parameter information into a temporal mode under covariant processing.
2. **Nonlinear rescue:** determine the weakest finite-amplitude or curvature assumption that upgrades the robust tangent law into a theorem for arbitrary smooth physical waveform families, including coherent-sideband synthesis.

The first route is closer to the autonomous-clock grand question; the second may produce a broader foundational Fisher-versus-global-robustness theorem.
