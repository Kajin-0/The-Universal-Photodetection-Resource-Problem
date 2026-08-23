# WP28 — Infinite-dimensional finite-radius survival law for bounded relative tangents

## Status

**Exact extension of the WP02 finite-radius theorem proved for a separable infinite-dimensional Hilbert space with trace-class baseline, bounded relative tangent, and an arbitrary semibounded self-adjoint Hamiltonian.**

The initial pure-point restriction is unnecessary. Stating the exact Bohr mode through unitary covariance gives a spectral-measure proof that includes continuous spectrum.

This deliberately treats the finite-radius/interior regime first. Rank-changing boundary synthesis with an unbounded pseudoinverse remains a separate problem.

## 1. Setup

Let `Hspace` be a separable Hilbert space.

Let `rho_0>=0` be a trace-class density operator with support projection

`P=supp(rho_0)`.

Let `A` be a trace-class complex tangent with `Tr A=0` and assume it is **bounded relative to the baseline**:

`boxed:
A=rho_0^(1/2) B rho_0^(1/2),`

where `B` is bounded on `P Hspace`, extended by zero on `P^perp`.

Define

`D_x=(A+A^dagger)/2`,

`D_y=(A-A^dagger)/(2i)`.

Assume the affine disk

`rho_0+xD_x+yD_y >=0`

is physical for every `x^2+y^2<=R^2`, with `R>0`.

No bounded inverse of `rho_0` is assumed. In an infinite-dimensional trace-class state, `rho_0^+` is typically unbounded; all quadratic expressions are defined through the bounded relative factor `B`.

## 2. Affine radius controls the bounded relative tangent

For `z=x+iy`,

`rho_0+xD_x+yD_y
 =rho_0^(1/2)
  [P+(z^*B+zB^dagger)/2]
  rho_0^(1/2).`

The range of `rho_0^(1/2)` is dense in `P Hspace`.

Therefore positivity of the trace-class operator for every `|z|<=R` is equivalent to positivity of the bounded bracket on `P Hspace`.

Because the disk contains both opposite directions,

`||Re(e^{-i theta}B)||<=1/R`

for all phases `theta`.

Hence

`boxed: w(B)<=1/R`,

and the Hilbert-space numerical-radius inequality gives

`boxed: ||B||<=2/R`.

No finite-dimensional compactness is used.

## 3. Trace-class weighted tangent norm

Define

`Z:=rho_0^(1/2) B B^dagger rho_0^(1/2)`.

Since `rho_0^(1/2)` is Hilbert--Schmidt and `B` is bounded, `Z` is positive trace class.

Formally this equals `A rho_0^+ A^dagger`, but `Z` is the rigorous infinite-dimensional definition.

Set

`J:=Tr Z=Tr(rho_0 B B^dagger)<infinity`.

Because

`B B^dagger<=||B||^2 P`,

one has

`Z<=||B||^2 rho_0<=4 rho_0/R^2`.

Thus

`boxed: J<=4/R^2`.

## 4. Arbitrary POVMs, including continuous outcomes

Let `M(dy)` be an arbitrary POVM on a measurable outcome space. Define

`p(E)=Tr[rho_0 M(E)]`,

`z(E)=Tr[A M(E)]`.

For every measurable set `E`, Hilbert--Schmidt Cauchy--Schwarz gives

`|z(E)|^2<=p(E) mu(E)`,

where

`mu(E)=Tr[Z M(E)]`.

In particular `z` is absolutely continuous with respect to `p`.

For any finite measurable partition `{E_alpha}`,

`sum_alpha |z(E_alpha)|^2/p(E_alpha)
 <=sum_alpha mu(E_alpha)=Tr Z`.

The `L^2(p)` norm of the Radon--Nikodym derivative `dz/dp` is the supremum of these coarse-grained quadratic forms over finite partitions. Therefore

`boxed:
Tr F_1^tan
 =int |dz/dp|^2 dp
 <=Tr Z=J.`

Thus the weighted score inequality is valid for arbitrary POVMs without assuming a discrete outcome set.

## 5. Finite copies and arbitrary collective measurements

For `N` independently encoded copies,

`rho_N=rho_0^tensor N`,

and

`A_N=sum_(r=1)^N
 rho_0^tensor(r-1) tensor A tensor rho_0^tensor(N-r)`.

The bounded relative tangent is

`B_N=sum_r I^tensor(r-1) tensor B tensor I^tensor(N-r)`

on `P^tensor N`.

Since

`Tr(rho_0 B)=Tr A=0`,

the cross-copy terms vanish exactly:

`Tr(rho_N B_N B_N^dagger)
 =N Tr(rho_0 B B^dagger)=N J`.

Applying the arbitrary-POVM inequality on the tensor product gives

`boxed:
Tr F_N^tan/N<=J`

for every finite `N` and every collective POVM.

No asymptotic or measurement-separability assumption is required.

## 6. Domain-safe exact Bohr mode for an arbitrary spectrum

Let `H` be any self-adjoint Hamiltonian bounded below by `E_*`.

Write its spectral measure as `E_H(.)` and its time-translation unitary as

`U_t=exp(-iHt/hbar)`.

Assume the baseline is stationary,

`U_t rho_0 U_t^dagger=rho_0`

for all real `t`.

State the exact positive temporal mode in the domain-safe covariance form

`boxed:
U_t A U_t^dagger=e^{-i nu t}A`

for all `t`.

Because `rho_0^(1/2)` commutes with `U_t`,

`rho_0^(1/2)
 [U_t B U_t^dagger-e^{-i nu t}B]
 rho_0^(1/2)=0`.

The range of `rho_0^(1/2)` is dense in `P Hspace`, and the bracket is bounded. Hence on the support

`boxed:
U_t B U_t^dagger=e^{-i nu t}B.`

Thus the relative tangent is itself a bounded eigenoperator of the adjoint time-translation representation.

## 7. Spectral-shift identity and upper survival

For a bounded operator satisfying the covariance above, the spectral theorem gives the shift relation

`boxed:
E_H(Delta) B
 =B E_H(Delta-hbar nu)`

for Borel sets `Delta`, with the obvious translated-set convention.

Equivalently, `B` maps source spectral support at energy `E` into energy `E+hbar nu`.

Since `H>=E_* I`, there is no source spectrum below `E_*`. Therefore

`boxed:
P_U(nu) B=B,`

where

`P_U(nu)=E_H([E_*+hbar nu,infinity)).`

Consequently

`Z=P_U Z P_U`.

Define the baseline upper-tail probability

`T(nu)=Tr[rho_0 P_U(nu)].`

Using `Z<=4rho_0/R^2`,

`J=Tr(P_U Z)
 <=(4/R^2)Tr(P_U rho_0)`.

Therefore, for every finite `N` and arbitrary collective POVM,

`boxed:
(R^2/4)[Tr F_N^tan/N]<=T(nu).`

This is exactly the WP02 survival law on an arbitrary separable Hilbert space and does **not** require pure-point spectrum.

## 8. Mean-energy corollary

If

`Ebar^+=Tr[rho_0(H-E_*)]<infinity`,

then the spectral Markov inequality gives

`T(nu)<=Ebar^+/(hbar nu)`.

Hence

`boxed:
Ebar^+
 >=(hbar nu R^2/4)[Tr F_N^tan/N].`

The robust energy--frequency law therefore survives continuous spectra as well.

## 9. Spectral truncation interpretation

For numerical/constructive approximation one may choose increasing finite-rank support projections `P_L` converging strongly to `P` and, when available, commuting with the relevant spectral decomposition.

Each finite-dimensional compression inherits a bound controlled by the same bounded relative operator norm. The direct trace-class/spectral-measure proof above shows that truncation is not logically required and that there is no cutoff-dependent constant to control.

## 10. Autonomous extension

For `T=C⊗S` with self-adjoint semibounded local Hamiltonians, a clean locally stationary exact exchange may be stated through the two covariance relations

`e^{-iH_S t/hbar}A e^{+iH_S t/hbar}=e^{-i nu t}A`,

`e^{-iH_C t/hbar}A e^{+iH_C t/hbar}=e^{+i nu t}A`.

If

`[rho_0,H_S]=[rho_0,H_C]=0`,

the spectral-measure proof applies independently to the signal positive orientation and the clock-conjugate positive orientation. Therefore

`boxed:
(R^2/4)[Tr F_N^tan/N]
 <=min{T_S(nu),T_C(nu)}`

for arbitrary semibounded local spectra, including continuous components.

The fully coherent/history-state case where `rho_0` commutes only with `H_C+H_S`, not with the local Hamiltonians separately, should be audited independently before being claimed in infinite dimension.

## 11. What is solved

- separable infinite-dimensional Hilbert space;
- trace-class baseline;
- bounded relative tangent;
- arbitrary POVMs, including continuous outcome spaces;
- arbitrary finite-copy collective measurements;
- arbitrary semibounded self-adjoint Hamiltonian, including continuous spectrum;
- exact finite-radius spectral survival and mean-energy law;
- locally stationary autonomous dual version.

## 12. What remains open

1. Rank-changing zero-radius synthesis/action with unbounded `rho_0^+`.
2. Unbounded relative tangents treated as closed quadratic forms.
3. Fully arbitrary coherent/history-state support in infinite dimension.
4. Infinite-dimensional WP21--WP23 dynamical implementation with potentially unbounded generators.
5. Gaussian covariance-changing boundary families.
6. Approximate-gap WP25/WP27 extensions in the spectral-measure setting.

## 13. Prior-art boundary

All functional-analysis ingredients are standard:

- trace ideals and Hilbert--Schmidt Cauchy--Schwarz;
- numerical radius of bounded operators;
- covariant/eigenoperators of a one-parameter unitary group;
- spectral-measure shift identities;
- spectral Markov inequality;
- Radon--Nikodym Fisher information.

Do not claim novelty for these mathematical facts.

The candidate contribution is only the extension of the **specific physical survival-resource theorem** to trace-class infinite-dimensional quantum statistical models under a bounded-relative-tangent hypothesis.

## 14. Immediate next work

1. Add a large-ladder/truncation validator.
2. Hostile-audit the arbitrary-POVM partition argument and the bounded-eigenoperator spectral-shift step.
3. Attack the one-sided rank-changing boundary theorem under a Hilbert--Schmidt support-to-kernel tangent condition.
4. Keep unbounded relative tangents deferred until the bounded case is fully audited.
