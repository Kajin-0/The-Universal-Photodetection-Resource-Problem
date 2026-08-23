# WP28 — Infinite-dimensional finite-radius survival law for bounded relative tangents

## Status

**Exact extension of the WP02 finite-radius theorem proved for a separable infinite-dimensional Hilbert space with trace-class baseline and bounded relative tangent.**

This is the first controlled removal of the finite-dimensional assumption. It deliberately treats the finite-radius/interior regime first. Rank-changing boundary synthesis with an unbounded pseudoinverse remains a separate problem.

## 1. Setup

Let `Hspace` be a separable Hilbert space.

Let `rho_0>=0` be a trace-class density operator with support projection

`P=supp(rho_0)`.

Let `A` be a trace-class complex tangent with `Tr A=0` and assume it is **bounded relative to the baseline**:

`boxed:
A=rho_0^(1/2) B rho_0^(1/2),`

where `B` is a bounded operator on `P Hspace`, extended by zero on `P^perp`.

Define

`D_x=(A+A^dagger)/2`,

`D_y=(A-A^dagger)/(2i)`.

Assume the affine disk

`rho_0+xD_x+yD_y >=0`

is physical for every `x^2+y^2<=R^2`, with `R>0`.

No bounded inverse of `rho_0` is assumed. In an infinite-dimensional trace-class state, `rho_0^+` is typically unbounded; all formulas below are interpreted through the bounded relative factor `B` and the resulting trace-class quadratic forms.

## 2. Affine radius still controls the numerical radius

For `z=x+iy`,

`rho_0+xD_x+yD_y
 =rho_0^(1/2)
  [P+(z^*B+zB^dagger)/2]
  rho_0^(1/2).`

The range of `rho_0^(1/2)` is dense in `P Hspace`.

Therefore positivity of the trace-class operator for every `|z|<=R` is equivalent to positivity of the bounded bracket on `P Hspace`:

`P+r Re(e^{-i theta}B)>=0`

for every `0<=r<=R` and every phase `theta`.

Because the disk also contains the opposite direction, this gives

`||Re(e^{-i theta}B)|| <= 1/R`

for every `theta`.

Hence the numerical radius satisfies

`boxed: w(B)<=1/R.`

The standard numerical-radius inequality on a Hilbert space gives

`||B||<=2w(B)<=2/R`.

Thus the finite-dimensional radius estimate survives unchanged.

## 3. Trace-class weighted tangent norm without using an unbounded pseudoinverse

Define

`Z:=rho_0^(1/2) B B^dagger rho_0^(1/2)`.

Since `rho_0^(1/2)` is Hilbert--Schmidt and `B` is bounded, `Z` is positive trace class.

Formally this is

`A rho_0^+ A^dagger`,

but `Z` is the rigorous definition needed here.

Set

`J:=Tr Z=Tr(rho_0 B B^dagger)<infinity`.

From `B B^dagger<=||B||^2 P`,

`Z<=||B||^2 rho_0<=4 rho_0/R^2`.

Therefore

`boxed: J<=4/R^2.`

## 4. Arbitrary-POVM weighted score inequality

Let `M(dy)` be an arbitrary POVM on a measurable outcome space. Define the baseline probability measure

`p(dy)=Tr[rho_0 M(dy)]`.

The complex tangent measure is

`z(dy)=Tr[A M(dy)]`.

Whenever a Radon--Nikodym score density exists, the two-quadrature classical Fisher trace is

`Tr F_1^tan = int |dz/dp|^2 dp`.

For a finite or countable POVM the outcome-wise Hilbert--Schmidt Cauchy--Schwarz inequality is

`|Tr(A M_y)|^2
 <= Tr(rho_0 M_y)
    Tr(Z M_y)`.

The same statement for a general POVM follows by applying this inequality to finite measurable partitions and passing to the supremum defining the `L^2(p)` Radon--Nikodym norm.

Summing/integrating and using `int M(dy)=I`,

`boxed:
Tr F_1^tan <= Tr Z=J.`

Thus no finite outcome-set assumption is needed.

## 5. Finite copies and arbitrary collective measurements

For `N` independently encoded copies, the baseline is

`rho_N=rho_0^tensor N`.

The first-order complex tangent is

`A_N=sum_(r=1)^N
 rho_0^tensor(r-1) tensor A tensor rho_0^tensor(N-r)`.

Because `Tr A=0`, the cross-copy terms vanish in the corresponding weighted quadratic form. More explicitly, the relative tangent is the bounded operator

`B_N=sum_r I^tensor(r-1) tensor B tensor I^tensor(N-r)`

on `P^tensor N`, and

`Tr(rho_N B_N B_N^dagger)=N Tr(rho_0 B B^dagger)=N J`.

Applying the arbitrary-POVM score inequality on the tensor-product Hilbert space gives

`boxed:
Tr F_N^tan/N <= J`

for every finite `N` and every collective POVM.

No asymptotic or separability assumption is required.

## 6. Exact Bohr-gap spectral survival in infinite dimension

Now let `H` be a self-adjoint semibounded Hamiltonian with lower spectral edge `E_*` and **pure-point spectrum** on the support relevant to `rho_0,A`.

Assume

`[rho_0,H]=0`

and the exact positive-gap relation

`[H,A]=hbar nu A`

in the common eigenbasis / quadratic-form sense, for `nu>0`.

Because `rho_0` commutes with `H`, so does `rho_0^(1/2)`. Hence the relative bounded operator `B` has matrix elements only between energies separated by `hbar nu` wherever the baseline weights are nonzero.

Let

`P_U(nu)=1_[E_*+hbar nu,infinity)(H)`

and

`T(nu)=Tr[rho_0 P_U(nu)].`

Every range energy participating in the positive-gap tangent lies in `P_U(nu)`, so

`Z=P_U Z P_U`.

Using `Z<=4 rho_0/R^2`,

`J=Tr Z
 =Tr(P_U Z)
 <=(4/R^2)Tr(P_U rho_0)`.

Therefore

`boxed:
(R^2/4)[Tr F_N^tan/N] <= T(nu)`

for every finite `N` and arbitrary collective POVM.

This is exactly the WP02 theorem with no finite-dimensional Hilbert-space assumption.

## 7. Mean-energy corollary

If the baseline has finite mean excess energy

`Ebar^+=Tr[rho_0(H-E_*)]<infinity`,

then the spectral Markov inequality gives

`T(nu)<=Ebar^+/(hbar nu)`.

Consequently

`boxed:
Ebar^+
 >= (hbar nu R^2/4)[Tr F_N^tan/N].`

Thus the robust energy--frequency consequence also extends exactly.

## 8. Why the bounded-relative-tangent assumption is natural

The condition

`A=rho_0^(1/2)B rho_0^(1/2)`, `B bounded`,

is the infinite-dimensional replacement for the finite-dimensional support-normalized tangent `rho_0^{-1/2}A rho_0^{-1/2}`.

It simultaneously guarantees:

1. the affine tangent can be tested through a bounded operator on the support;
2. the physical radius controls `w(B)` and `||B||`;
3. the weighted tangent quadratic form is trace class;
4. arbitrary-POVM Fisher information is finite;
5. finite-copy tensor products remain controlled.

If the relative tangent is unbounded, none of these steps is automatic and a closed quadratic-form theory is required.

## 9. Spectral truncation interpretation

Let `P_L` be increasing finite-rank spectral/support truncations commuting with `rho_0,H` and converging strongly to `P`.

Define

`rho_L=P_L rho_0 P_L / Tr(P_L rho_0)`

and the corresponding truncated relative tangent from `P_L B P_L`.

Each finite-dimensional truncation obeys the original WP02 theorem. The operator proof above shows that the relevant constants are cutoff independent because they depend only on `||B||` and the physical radius.

The direct trace-class theorem is therefore consistent with, but stronger than, merely taking a numerical sequence of finite-dimensional approximations.

## 10. Autonomous extension

For `T=C⊗S` with self-adjoint semibounded local Hamiltonians, assume

`[rho_0,H_C+H_S]=0`

and exact exchange

`[H_S,A]=+hbar nu A`,

`[H_C,A]=-hbar nu A`.

If the arbitrary-coherent-support tail argument of WP06 is formulated using the corresponding local spectral projections and the same bounded relative tangent `B`, its operator steps are unchanged in infinite dimension provided all local tail probabilities are finite (automatic for a density operator) and the relevant exact-gap form relations hold.

At minimum, under separate local stationarity `[rho_0,H_C]=[rho_0,H_S]=0`, one obtains immediately

`boxed:
(R^2/4)[Tr F_N^tan/N]
 <= min{T_C(nu),T_S(nu)}.`

The fully non-locally-stationary infinite-dimensional WP06 extension should be audited separately rather than asserted from analogy.

## 11. What is solved

- separable infinite-dimensional Hilbert space;
- trace-class baseline;
- arbitrary POVMs, including continuous outcome spaces;
- arbitrary finite-copy collective measurements;
- bounded relative tangent;
- semibounded pure-point Hamiltonian;
- exact finite-radius survival and mean-energy law;
- locally stationary autonomous dual version.

## 12. What remains open

1. Rank-changing zero-radius synthesis/action with unbounded `rho_0^+`.
2. Unbounded relative tangents `B` treated as closed forms.
3. Continuous spectral components of `H`.
4. Fully arbitrary coherent/history-state support in infinite dimension.
5. Infinite-dimensional WP21--WP23 dynamical implementation with unbounded generators.
6. Gaussian covariance-changing families.

## 13. Prior-art boundary

The functional-analysis ingredients are standard:

- trace ideals / Hilbert--Schmidt Cauchy--Schwarz;
- numerical-radius inequality for bounded Hilbert-space operators;
- spectral theorem and Markov tail bound;
- Radon--Nikodym formulation of classical Fisher information.

Do not claim novelty for those.

The candidate contribution is only the extension of the **specific physical survival-resource theorem** to trace-class infinite-dimensional quantum statistical models under a bounded-relative-tangent hypothesis.

## 14. Immediate next work

1. Build a large-truncation validator showing cutoff-independent convergence on infinite ladders.
2. Replace the pure-point assumption by a spectral-measure proof if possible.
3. Attack the one-sided rank-changing boundary theorem using finite-rank support truncations and monotone positive quadratic forms.
4. Keep unbounded relative tangents deferred until the bounded case is fully audited.
