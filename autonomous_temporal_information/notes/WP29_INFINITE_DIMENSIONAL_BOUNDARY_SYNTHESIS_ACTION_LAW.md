# WP29 — Infinite-dimensional rank-boundary synthesis and autonomous action law

## Status

**Exact extension of the pure-boundary WP07/WP09/WP18 theorem chain proved for separable infinite-dimensional Hilbert spaces under a Hilbert--Schmidt right-relative tangent condition and trace-norm `C^2` physicality.**

Together WP28 and WP29 remove finite dimensionality from the clean survival/synthesis dichotomy under controlled operator-domain hypotheses.

This does not yet cover the full arbitrary coherent-support WP19 shorted geometry or unbounded/non-Hilbert--Schmidt tangent directions.

## 1. General rank-deficient trace-class baseline

Let `Hspace` be separable and

`rho_0>=0`, `Tr rho_0=1`

be trace class.

Let

`P=supp(rho_0)`, `Q=I-P`.

Because `rho_0` is compact, its positive spectrum on `P` is discrete (finite or countably infinite) with eigenvalues `lambda_n>0` tending to zero if the rank is infinite.

Choose an eigenbasis

`rho_0=sum_n lambda_n |n><n|`

on `P`.

Let `rho_0^{-1/2}` denote the unbounded inverse square root on its natural support domain.

Consider a two-sided physical family

`rho(x,y)>=0`, `Tr rho(x,y)=1`

that is `C^2` in trace norm near `(0,0)` and satisfies

`rho(0,0)=rho_0`.

Trace-norm `C^2` implies the first and second derivatives are trace class and the Taylor remainder is `o(x^2+y^2)` in operator norm as well.

## 2. Infinite-dimensional PSD-cone curvature lemma

Let `D=D^dagger` be one real derivative of a two-sided `C^2` curve `rho(t)` at `t=0`.

First-order positivity gives

`Q D Q=0`.

Set

`K=QDP`.

Assume the right-relative operator

`L:=K rho_0^{-1/2}`

extends to a Hilbert--Schmidt operator from `P Hspace` to `Q Hspace`.

Define the positive trace-class operator

`Z:=L L^dagger`.

Formally `Z=K rho_0^+ K^dagger`.

Let `P_n` project onto the first `n` positive eigenvectors of `rho_0` and let

`rho_n=P_n rho_0 P_n`.

For any `q in Q Hspace`, choose a finite-support trial vector

`p_n=-rho_n^{-1} P_n D q`.

Positivity of

`<q+t p_n|rho(t)|q+t p_n>`

for both signs of sufficiently small `t` gives, at order `t^2`,

`<q|Q rho''(0) Q|q>
 >=2 <q|K P_n rho_n^{-1}P_n K^dagger|q>`.

The positive operators on the right increase monotonically in quadratic-form sense to

`K rho_0^+ K^dagger=L L^dagger=Z`.

Therefore

`boxed:
Q rho''(0) Q >= 2 Z`

as a bounded/trace-class quadratic-form inequality.

This is the infinite-rank PSD-cone Schur-complement law needed below.

## 3. One-sided boundary synthesis

Assume the complex tangent is one-sided,

`A=QAP`,

with

`L_A:=A rho_0^{-1/2}`

Hilbert--Schmidt.

Define

`J=||L_A||_2^2=Tr(L_A L_A^dagger)<infinity`.

The real derivatives satisfy

`Q D_x P=A/2`,

`Q D_y P=A/(2i)`.

Applying the curvature lemma separately to `x` and `y` gives

`Q(partial_x^2+partial_y^2)rho(0)Q
 >= A rho_0^+ A^dagger`

in the rigorous sense

`boxed:
C_Delta>=L_A L_A^dagger.`

Let `Pi_U` be any closed endpoint subspace containing the range of `A` and orthogonal to `P`. Define

`Delta T_U=Tr(Pi_U C_Delta)`.

Then

`boxed: J<=Delta T_U.`

### Measurement side

For an arbitrary POVM `M(dy)`, the complex tangent measure satisfies the same setwise Hilbert--Schmidt inequality

`|Tr[A M(E)]|^2
 <=Tr[rho_0 M(E)] Tr[(L_A L_A^dagger)M(E)].`

Finite partitions and Radon--Nikodym passage give

`Tr F_1^tan<=J`.

For `N` copies, the off-support tangent has trace zero and the cross-copy weighted terms vanish, yielding

`boxed:
Tr F_N^tan/N<=J<=Delta T_U`

for every finite `N` and arbitrary collective POVM.

Thus WP07 holds unchanged.

## 4. Bilateral pure-boundary law

Now assume

`PAP=0`, `QAQ=0`.

Define

`X=QAP`,

`Y=QA^dagger P`,

so

`A=X+Y^dagger`.

Assume both

`L_+=X rho_0^{-1/2}`

and

`L_-=Y rho_0^{-1/2}`

are Hilbert--Schmidt.

Set

`Z_+=L_+L_+^dagger`, `Z_-=L_-L_-^dagger`,

`J_+=Tr Z_+`, `J_-=Tr Z_-`.

The support-to-kernel blocks of the real derivatives are

`K_x=(X+Y)/2`,

`K_y=(X-Y)/(2i)`.

Both right-relative operators are Hilbert--Schmidt. Applying the curvature lemma and summing cancels the cross terms:

`boxed:
C_Delta
 >= Z_+ + Z_- .`

The arbitrary-POVM score vectors split into the `X` and `Y` orientations. Hilbert-space Minkowski gives

`boxed:
sqrt(Tr F_1^tan)
 <=sqrt(J_+)+sqrt(J_-).`

The finite-copy weighted norms scale by `N`, hence

`boxed:
sqrt(Tr F_N^tan/N)
 <=sqrt(J_+)+sqrt(J_-)`

for every finite `N` and arbitrary collective POVM.

This is the full WP09 measurement-side law in infinite dimension.

## 5. Endpoint curvature

Suppose closed orthogonal endpoint-role projectors `Pi_+`,`Pi_-` satisfy

`Pi_+ Z_+ Pi_+=Z_+`,

`Pi_- Z_- Pi_-=Z_-`.

Define

`Delta T_+=Tr(Pi_+ C_Delta)`,

`Delta T_-=Tr(Pi_- C_Delta)`.

Because `C_Delta>=Z_++Z_-`,

`J_+<=Delta T_+`,

`J_-<=Delta T_-`.

Therefore

`boxed:
Tr F_N^tan/N
 <=[sqrt(Delta T_+)+sqrt(Delta T_-)]^2.`

The square-root/Minkowski structure is unchanged.

## 6. SLD-QFI trace

Under the same Hilbert--Schmidt conditions, the pure-boundary SLD quadratic form is finite and

`boxed:
Tr H_SLD=2(J_++J_-).`

This follows either from finite support truncations followed by monotone convergence or directly from the standard spectral formula for a trace-class baseline.

Thus the R3 separation between common-record tangent Fisher and SLD geometry also survives.

## 7. Infinite-dimensional autonomous exact-exchange action

Let the Hilbert space factor as `C⊗S` with self-adjoint semibounded local Hamiltonians.

Assume the exact relational mode in covariance form,

`e^{-iH_S t/hbar} A e^{+iH_S t/hbar}=e^{-i nu t}A`,

`e^{-iH_C t/hbar} A e^{+iH_C t/hbar}=e^{+i nu t}A`.

Assume the baseline is globally stationary under `H_C+H_S`. For the clean endpoint geometry, assume the positive and negative synthesized orientations have well-defined closed local endpoint-role subspaces on the clock and signal sides, with finite population Laplacians.

Define exactly as in WP18

`A_S^(2)=(hbar nu/4)(Delta T_{S,+}+Delta T_{S,-})`,

`A_C^(2)=(hbar nu/4)(Delta T_{C,+}+Delta T_{C,-})`.

The boundary Minkowski theorem applied to the local endpoint incidences gives for each subsystem

`A_X^(2)
 >=(hbar nu/8)[Tr F_N^tan/N]`, `X in {C,S}`.

Therefore

`boxed:
A_C^(2)+A_S^(2)
 >=(hbar nu/4)[Tr F_N^tan/N]`

for bilateral synthesis.

If only one orientation is present, the one-sided theorem on each local side gives

`boxed:
A_C^(2)+A_S^(2)
 >=(hbar nu/2)[Tr F_N^tan/N].`

The coefficients are exactly the finite-dimensional WP18 coefficients.

The SLD corollary likewise remains

`boxed:
A_C^(2)+A_S^(2)
 >=(hbar nu/4)Tr H_SLD`

in the clean pure-boundary geometry.

## 8. Hamiltonian spectrum need not be discrete

The PSD-cone and measurement proofs depend only on the compact spectral decomposition of the **trace-class state** `rho_0`, not on an energy eigenbasis.

The exact temporal-frequency condition is stated through unitary covariance and therefore remains meaningful for continuous local Hamiltonian spectra.

Endpoint role subspaces can be defined from the closed supports of the covariant tangent ranges and local spectral-measure shifts rather than from individual eigenstates.

Thus continuous Hamiltonian spectrum is not, by itself, an obstruction to the clean infinite-dimensional boundary theorem.

## 9. What is solved

- separable infinite-dimensional state space;
- arbitrary trace-class rank-deficient baseline;
- trace-norm `C^2` physical family;
- Hilbert--Schmidt right-relative support-to-kernel tangent;
- one-sided and bilateral PSD-cone synthesis laws;
- arbitrary POVMs, including continuous outcomes;
- arbitrary finite-copy collective measurements;
- finite SLD-QFI boundary trace;
- clean autonomous exact-exchange action laws with the same coefficients;
- continuous Hamiltonian spectra allowed through covariance formulation.

## 10. What remains open

1. Tangents for which `X rho_0^{-1/2}` or `Y rho_0^{-1/2}` is unbounded/non-Hilbert--Schmidt.
2. Full WP19 arbitrary coherent-support shorted geometry in infinite dimension; closed range and shorted-operator subtleties become serious.
3. Infinite-dimensional WP21--WP23 implementation minima with unbounded generators.
4. Approximate-exchange WP27 in full spectral-measure form.
5. Gaussian covariance-changing families with genuinely unbounded canonical generators.
6. Tensor-valued rather than metric-contracted second-order jets.

## 11. Prior-art boundary

The infinite-rank Schur-complement argument, Hilbert--Schmidt trace ideals, monotone convergence of positive quadratic forms, and continuous-outcome Fisher measure theory are standard functional analysis/statistics.

Do not claim mathematical novelty for them.

The candidate contribution is the extension of the specific autonomous spectral **survival/synthesis resource dichotomy** and its sharp action coefficients beyond finite-dimensional Hilbert spaces under explicit finite-information regularity assumptions.

## 12. Immediate next work

1. Add a numerical truncation validator with rapidly decaying support eigenvalues and rank-deficient infinite-ladder models.
2. Hostile-audit the finite-rank Schur-complement limit, especially trace-norm `C^2` sufficiency.
3. Determine whether the clean endpoint role assumptions can be expressed entirely with spectral-measure covariance projectors.
4. Decide whether WP28--WP29 materially eliminate the manuscript's finite-dimensional limitation enough to justify R4.
5. Keep unbounded relative tangents and full WP19 infinite-dimensional shorting as separate research problems.
