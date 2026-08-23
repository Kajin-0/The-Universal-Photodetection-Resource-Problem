# WP15 — Exact common-record Fisher supremum for the shared-kernel qutrit

**Date:** 2026-08-22

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** analytic PASS for the one-copy arbitrary-POVM optimization in the WP12 shared-kernel qutrit benchmark. The exact supremum of the two-quadrature classical Fisher trace is `55/8`, strictly below both the WP12 resource-allocation ceiling `12` and the SLD-QFI trace `43/4`. The upper bound is certified by an explicit POVM-dual quadratic witness; the lower bound is reached as a limit of ordinary three-outcome projective measurements with strictly positive baseline probabilities. Generic multiparameter compatibility theory, Gill--Massar inequalities, numerical-radius bounds, and rank-changing QFI/Bures geometry are prior art. Candidate novelty is the exact resolution of this benchmark and the separation of physical-resource, quantum-statistical, and common-record measurement layers. Priority remains **unverified, not certified**.

## 1. Benchmark left by WP12

Use the three-level Hamiltonian basis and define

`|q>=(1/2)|0> + sqrt(5/8)|1> + [1/(2sqrt(2))]|2>`.

Let

`Q=|q><q|`,

`P=I-Q`,

`rho0=P/2`.

Choose the exact `+omega` complex tangent

`A=|1><0| - sqrt(2)|2><1|`.

WP12 showed that, in the upper-oriented decomposition,

`J_B^+=5/4`,

`J_+=7/4`,

`J_-=3`,

and the exact shared-curvature allocation ceiling is

`Phi=12`.

The ordinary SLD-QFI matrix for the two real quadratures is

> `F_Q=diag(39/8,47/8)`,

so

> `Tr F_Q=43/4=10.75`.

The SLD commutator expectation is nonzero:

`Tr[rho0(L_x L_y-L_y L_x)/(2i)]=5/4`.

Therefore the SLD matrix is not jointly attainable by one common measurement. WP15 asks for the exact maximum of

`Tr F_1`

over all one-copy POVMs.

## 2. Support/kernel basis

Choose an orthonormal basis of `P`:

`|e1>=(1/sqrt(3))|0> - sqrt(2/3)|2>`,

`|e2>=-(sqrt(15)/6)|0> + (sqrt(6)/4)|1> -(sqrt(30)/12)|2>`.

In the ordered basis

`{|e1>,|e2>,|q>}`,

one has

> `rho0=diag(1/2,1/2,0)`

and

> `A = [[0, sqrt(2)/2, sqrt(30)/6],`
>
> `     [sqrt(2)/4, 0, sqrt(6)/3],`
>
> `     [sqrt(30)/12, -sqrt(6)/3, 0]]`.

Write the block form

`A=[[B,b],[a^dagger,0]]`,

with

`B=[[0,sqrt(2)/2],[sqrt(2)/4,0]]`,

`a=(sqrt(30)/12,-sqrt(6)/3)`,

`b=(sqrt(30)/6,sqrt(6)/3)^T`.

For a POVM effect `M_y`, define

`p_y=Tr(rho0 M_y)`,

`z_y=Tr(A M_y)`.

With the project's two-quadrature convention,

> `Tr F_1=sum_y |z_y|^2/p_y`

for outcomes with `p_y>0`.

## 3. Rank-one refinement loses no upper-bound generality

For a positive effect decomposed as

`M=sum_j M_j`,

let

`p_j=Tr(rho0 M_j)`, `z_j=Tr(A M_j)`.

Quadratic-over-linear convexity gives

`|sum_j z_j|^2/(sum_j p_j) <= sum_j |z_j|^2/p_j`.

Thus refining every POVM effect into rank-one components cannot decrease the Fisher trace.

It is therefore enough to bound a rank-one effect

`M=w |phi><phi|`.

Its contribution is

`w |<phi|A|phi>|^2/<phi|rho0|phi>`.

## 4. Exact POVM-dual witness

Define the Hermitian operator

> `Y = [[9/16, 0, 0],`
>
> `     [0, 9/16, 3sqrt(15)/8],`
>
> `     [0, 3sqrt(15)/8, 23/4]]`.

The central inequality is

> **Quadratic witness**
>
> `boxed: |<phi|A|phi>|^2`
>
> `<= <phi|rho0|phi> <phi|Y|phi>`
>
> for every vector `|phi>`.

Once established, every rank-one POVM obeys

`Tr F_1`

`<= sum_y w_y <phi_y|Y|phi_y>`

`=Tr Y`.

Since

`Tr Y=9/16+9/16+23/4`,

> `boxed: Tr F_1 <= 55/8`.

By rank-one refinement, this holds for every arbitrary POVM.

## 5. Exact positivity certificate for the witness

The quadratic witness is equivalent to a family of linear matrix inequalities.

For every `lambda>0` and phase `theta`, define

`M(lambda,theta)`

`=lambda rho0 + lambda^(-1)Y`

` -(e^(i theta)A+e^(-i theta)A^dagger)`.

If

`M(lambda,theta)>=0`

for all `lambda,theta`, then for every `|phi>`

`2 |<phi|A|phi>|`

`<= lambda <phi|rho0|phi>`

` +lambda^(-1)<phi|Y|phi>`.

Minimizing the right side over `lambda` gives precisely the product inequality in Sec. 4.

Set

`x=lambda^2`,

`t=cos^2(theta)`.

The first leading principal minor is

> `(8x+9)/(16 lambda) >0`.

The second leading principal minor simplifies exactly to

> `[t(8x-9)^2`
>
> ` +(1-t)(64x^2+112x+81)]/(256x)`.

The determinant simplifies exactly to

> `[t(8x-9)^2`
>
> ` +(1-t)(40x+81)]/(128 lambda^3)`.

Both numerators are manifestly nonnegative for

`x>0`, `0<=t<=1`.

They are strictly positive except at the isolated point

`t=1`, `x=9/8`.

Away from that point, Sylvester's criterion gives

`M(lambda,theta)>0`.

At the isolated equality point, positive semidefiniteness follows by continuity.

Therefore

> `boxed: M(lambda,theta)>=0`

for every `lambda>0`, every `theta`, proving the quadratic witness exactly.

No sampled or numerical positivity assumption enters the theorem.

## 6. Why the witness constants are natural

The two diagonal resource pieces in `Y` correspond to the sharp regular-support and singular-kernel directional ceilings.

### Support numerical-radius piece

The support block is

`B=[[0,r],[s,0]]`

with

`r=sqrt(2)/2`,

`s=sqrt(2)/4`.

Its numerical radius is

`w(B)=(r+s)/2=3sqrt(2)/8`.

Hence

`2 |<psi|B|psi>|^2 <= 2w(B)^2=9/16`

for every unit support vector.

The two support projectors

`|s_+>=(|e1>+|e2>)/sqrt(2)`,

`|s_->=(|e1>-|e2>)/sqrt(2)`

simultaneously saturate this bound with opposite signs. Their total Fisher contribution is

> `2 x (9/16)=9/8`.

### Kernel approach piece

For a vector approaching the kernel,

`|phi_epsilon>=cos(epsilon)|q>+sin(epsilon)|t>`,

with `|t>` a unit support vector, the baseline probability is

`p_epsilon=sin^2(epsilon)/2`.

The tangent amplitude is

`<phi_epsilon|A|phi_epsilon>`

`=sin(epsilon)cos(epsilon)`

` x [<q|A|t>+<t|A|q>] + O(sin^2 epsilon)`.

Therefore its Fisher contribution tends to

`2 |<q|A|t>+<t|A|q>|^2`.

Because `a,b` are real, taking

> `|t_*>= i (a-b)^T/||a-b||`

gives

`|<q|A|t_*>+<t_*|A|q>|^2`

`=||a-b||^2`.

Here

`||a-b||^2=23/8`.

Thus the optimal near-kernel contribution is

> `boxed: 23/4`.

The off-diagonal witness entry `3sqrt(15)/8` is exactly what makes the support and kernel pointwise bounds coexist for arbitrary mixed support/kernel vectors; simply placing the two scalar ceilings on the diagonal is insufficient.

## 7. Projective sequence reaches 55/8

The upper bound is a true supremum.

Let

`U_epsilon`

be a unitary that performs a rotation by angle `epsilon` in the two-dimensional subspace

`span{|q>,|t_*>}`

and acts as the identity on its orthogonal complement.

Measure the orthonormal projective basis

`{U_epsilon|s_+>, U_epsilon|s_->, U_epsilon|q>}`.

For every `epsilon>0` small enough, all three outcomes have ordinary well-defined probabilities, and the outcome descending from `|q>` has positive baseline probability.

As

`epsilon ->0^+`,

- the first two projectors converge to `|s_+>,|s_->` and contribute `9/8` in total;
- the near-kernel projector contributes `23/4`.

Therefore

> `lim_(epsilon->0^+) Tr F_1[U_epsilon]=9/8+23/4=55/8`.

Combined with Sec. 4,

> **Exact common-record optimum**
>
> `boxed: sup_(one-copy POVMs) Tr F_1 = 55/8`.

The result is stated as a supremum. Exact attainment by a regular POVM with all baseline probabilities strictly positive is not required and is not claimed.

## 8. Exact information hierarchy in the benchmark

The benchmark now has three distinct ceilings:

### Physical shared-curvature resource ceiling

WP12:

`Phi=12=96/8`.

### SLD quantum-statistical ceiling

`Tr F_Q=43/4=86/8`.

### Exact common-record classical Fisher supremum

WP15:

`sup Tr F_1=55/8`.

Thus

`resource -> SLD gap = 10/8 =5/4`,

`SLD -> common-record gap =31/8`,

and

`resource -> common-record gap =41/8`.

This corrects the earlier provisional wording that treated the full `12` versus `10.75` discrepancy as measurement compatibility. The resource theorem and the SLD theorem are already different relaxations before common-record incompatibility is considered.

## 9. The limiting Fisher allocation

In the projective sequence above, the limiting information splits transparently:

- the support Fourier/numerical-radius basis carries `9/8` in the regular support-sensitive quadrature;
- the nearly dark outcome carries `23/4` in the orthogonal rank-changing quadrature.

Thus the optimal common record does **not** try to approximate both SLD-optimal measurements simultaneously. It separates regular support information from singular boundary information into different outcomes of one measurement.

This is qualitatively different from simply randomizing two scalar-SLD measurements.

## 10. Prior-art boundary

The following are established and not novelty claims:

- Braunstein--Caves scalar quantum Fisher inequalities;
- Gill--Massar information-complementarity bounds;
- Fisher-symmetric POVMs and local multiparameter measurement incompatibility;
- numerical-radius inequalities;
- quadratic-over-linear convexity under POVM refinement;
- rank-changing QFI/Bures discontinuity geometry;
- semidefinite/quadratic dual witnesses in measurement optimization.

Relevant literature includes:

- R. D. Gill and S. Massar, *State estimation for large ensembles*, Phys. Rev. A **61**, 042312 (2000), DOI `10.1103/PhysRevA.61.042312`;
- N. Li, C. Ferrie, J. A. Gross, A. Kalev, and C. M. Caves, *Fisher-Symmetric Informationally Complete Measurements for Pure States*, Phys. Rev. Lett. **116**, 180402 (2016), DOI `10.1103/PhysRevLett.116.180402`;
- D. Safranek, *Discontinuities of the quantum Fisher information and the Bures metric*, Phys. Rev. A **95**, 052320 (2017), DOI `10.1103/PhysRevA.95.052320`.

The standard Gill--Massar presentation explicitly excludes POVM outcomes orthogonal to the fiducial state from the ordinary Fisher sum. WP15 likewise does **not** assign Fisher information directly to a zero-probability outcome: the `55/8` value is approached through a sequence of regular projective measurements with positive baseline probabilities.

Targeted searches have not identified this exact qutrit rank-changing common-record optimization or its `55/8` witness. This is a benchmark-specific theorem, not a certified priority claim.

## 11. Consequence for the grand program

WP15 resolves the most important ambiguity left after WP12.

The local theorem hierarchy should now be kept explicitly separated:

1. **physical resource geometry** — WP02--WP14;
2. **quantum statistical tangent geometry** — SLD/Bures-type upper bounds;
3. **single-record measurement compatibility** — the actually attainable classical Fisher region.

For rank-changing temporal models these three layers can differ substantially even in dimension three.

The operator resource law is therefore not itself a measurement-attainability statement, and the QFI is not itself the physically sharp resource law.

## 12. Next work

Highest-value next targets:

1. generalize the WP15 dual-witness method to a class of rank-one-kernel two-quadrature models and determine which invariants replace the benchmark-specific `9/8` and `23/4`;
2. combine WP14 curvature-metric overlap with WP13 spectral action into a two-resource Pareto theorem;
3. lift the positive operator/action hierarchy to both clock and signal sides of a globally stationary exchange tangent;
4. test covariance-changing Gaussian families;
5. perform a hostile priority/significance review of WP07--WP15 before deciding whether a new manuscript is justified.
