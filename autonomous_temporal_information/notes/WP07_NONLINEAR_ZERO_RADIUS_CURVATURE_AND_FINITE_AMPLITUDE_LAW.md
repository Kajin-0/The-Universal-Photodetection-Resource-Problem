# WP07 — Nonlinear zero-radius curvature law and finite-amplitude spectral discrimination

**Date:** 2026-08-22

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** analytic PASS for the support-to-kernel two-quadrature arbitrary-POVM curvature theorem and for the two-sector finite-amplitude discrimination theorem. The `R_lin=0` loophole is no longer empty: first-order temporal information can be supported by second-order creation of a previously absent spectral sector. The underlying PSD-cone curvature, singular QFI/Bures geometry, block positivity, and block-coherence inequalities are prior art. Candidate novelty is restricted to the **frequency-resolved operational temporal-resource consequence**, especially the finite-copy arbitrary-POVM two-quadrature coefficient and its autonomous interpretation. Priority remains **unverified, not certified**.

## 1. Problem left by WP02/WP06

WP02/WP06 control a first-order tangent by its nonzero linear physical radius:

`(R_lin^2/4)[Tr F_N/N] <= spectral tail`.

This becomes vacuous when `R_lin=0`.

The canonical mechanism is a rank-deficient baseline. A smooth exact nonlinear family can create off-diagonal amplitude into a previously empty sector at first order while supplying the population required for positivity only at second order.

The earlier Grand-Challenge coherent-sideband no-go (`grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`) identified exactly this mechanism: local QFI remains finite at arbitrarily high sideband frequency while sideband energy enters quadratically in the modulation parameter.

WP07 asks what resource replaces baseline spectral population in this boundary regime.

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

Hence

`Delta T_U(0)=4c^2`.

The SLD QFI matrix is

`H_Q=4c^2 I_2`,

with QFI trace `8c^2`.

A single fixed four-outcome equatorial POVM

`M_m=(1/4)[I+cos(phi_m)sigma_x+sin(phi_m)sigma_y]`,

`phi_m=0,pi/2,pi,3pi/2`,

has

`Tr F_M=4c^2=Delta T_U(0)`.

Thus the relevant one-record two-quadrature Fisher quantity is already suggesting the sharper coefficient proved below. The QFI trace is larger because the two SLD directions are incompatible at the pure-state boundary.

## 3. Second-order PSD constraint at a rank-deficient baseline

Let

`rho(theta)=rho0 + theta D + (theta^2/2) C + o(theta^2)`

be a two-sided `C^2` curve of density operators, physical for all sufficiently small positive and negative `theta`.

Let

`P=supp(rho0)`, `Q=I-P`,

and

`R=P rho0 P`,

which is strictly positive on `P`.

Two-sided positivity first implies

`Q D Q=0`.

Define

`K=Q D P`.

In the decomposition `P directsum Q`,

`rho(theta)`

`= [[R+O(theta), theta K^dagger+O(theta^2)],`

`   [theta K+O(theta^2), (theta^2/2)Q C Q+o(theta^2)]]`.

For sufficiently small `theta`, the support block is invertible. Positivity of the Schur complement requires

`(theta^2/2)Q C Q - theta^2 K R^(-1) K^dagger + o(theta^2) >=0`.

Therefore

> **Second-order support-creation condition**
>
> `Q C Q >= 2 K R^(-1) K^dagger`.

Equivalently,

> `Q rho''(0) Q >= 2 Q rho'(0)P(P rho0 P)^(-1)P rho'(0)Q`.

The coefficient `2` is sharp. Fixed-rank unitary rotations from `P` into `Q` attain equality in the newly occupied kernel block.

### Prior-art boundary

This matrix condition is not new mathematics. It is a direct instance of the established second-order tangent geometry of the PSD cone. The characteristic curvature term `V Y^dagger V` occurs in classical nonlinear semidefinite programming; see, e.g.,

- A. Shapiro, *First and second order analysis of nonlinear semidefinite programs*, Math. Programming 77, 301--320 (1997);
- J. F. Bonnans, R. Cominetti, and A. Shapiro, *Second order optimality conditions based on parabolic second order tangent sets*, SIAM J. Optim. 9, 466--492 (1999).

Later treatments recover the same curvature term using second subderivatives and Schur-complement arguments.

The research question here is the **temporal-information consequence of this established cone geometry**.

## 4. One-parameter QFI consequence — useful, but close to established singular geometry

Suppose a one-parameter tangent enters a previously empty upper sector `P_U<=Q`:

`PDP=0`,

`K=P_U D P`.

The baseline SLD QFI is

`F_Q(0)=4 Tr(K R^(-1)K^dagger)`.

Define

`T_U(theta)=Tr(P_U rho(theta))`.

Then

`T_U(0)=T_U'(0)=0`

and the PSD condition gives

`T_U''(0)>=2 Tr(K R^(-1)K^dagger)`.

Hence

> `F_Q(0) <= 2 T_U''(0)`.

The coefficient is sharp for fixed-rank unitary boundary rotations.

This scalar statement should **not** be advertised as the main novelty. Rank-changing QFI and Bures geometry are already known to acquire Hessian corrections from zero eigenvalues. In particular, Safranek, Phys. Rev. A 95, 052320 (2017), DOI `10.1103/PhysRevA.95.052320`, shows that the continuous/Bures completion of the QFI differs from the pointwise SLD QFI by second derivatives of vanishing eigenvalues.

For a support-to-kernel-only curve, the same geometry can make the continuous QFI/Bures information equal to the appropriate total kernel-population curvature coefficient. That is a close prior-art collision.

The stronger project result is therefore the direct two-quadrature arbitrary-POVM theorem below.

## 5. Direct two-quadrature arbitrary-POVM curvature theorem

Use the same complex tangent convention as WP02/WP03/WP06. Let the two real temporal quadratures have first derivatives

`D_c=(A+A^dagger)/2`,

`D_s=(A-A^dagger)/(2i)`.

Assume the zero-radius component has domain in the baseline support and range in a previously empty upper endpoint sector:

`A=P_U A P`,

`P=supp(rho0)`, `P_U<=Q=I-P`.

Define

`J(A|rho0)=Tr(A rho0^+ A^dagger)`.

### 5.1 Measurement side

For any POVM `{M_y}`, let

`p_y=Tr(rho0 M_y)`,

`z_y=Tr(A M_y)`.

The two-quadrature Fisher trace is

`Tr F_1 = sum_y |z_y|^2/p_y`.

Weighted Hilbert--Schmidt Cauchy--Schwarz gives outcome by outcome

`|Tr(A M_y)|^2/p_y <= Tr(M_y A rho0^+ A^dagger)`.

Summing outcomes yields

> `Tr F_1 <= J(A|rho0)`.

For `N` independently encoded copies, the complex tangent is

`A_N=sum_j rho0^(tensor(j-1)) tensor A tensor rho0^(tensor(N-j))`.

Because `Tr A=0`, the cross-copy terms vanish in the same quadratic form, so

`Tr(A_N rho0,N^+ A_N^dagger)=N J(A|rho0)`.

Therefore, for **every finite `N` and every entangled collective POVM**,

> `Tr F_N/N <= J(A|rho0)`.

No SLD attainability assumption is used.

### 5.2 Physical-curvature side

Let

`T_U(x,y)=Tr[P_U rho(x,y)]`

for the exact `C^2` physical family realizing `D_c,D_s`.

Along the cosine direction,

`K_c=P_U D_c P=A/2`.

Along the sine direction,

`K_s=P_U D_s P=A/(2i)`.

Applying the second-order support-creation condition separately to both directions gives

`partial_x^2 T_U(0) >= (1/2)J(A|rho0)`,

`partial_y^2 T_U(0) >= (1/2)J(A|rho0)`.

Therefore

> `Delta T_U(0) >= J(A|rho0)`.

Combining the measurement and physical sides gives the main WP07 local theorem:

> **Zero-radius arbitrary-POVM spectral-synthesis law**
>
> `boxed: Tr F_N/N <= J(A|rho0) <= Delta T_U(0)`
>
> for arbitrary finite `N` and arbitrary collective POVMs.

Equivalently, defining

`Q_U^(2):=(1/4)Delta T_U(0)`,

one has

> `boxed: (1/4)[Tr F_N/N] <= Q_U^(2)`.

This is the direct zero-radius analogue of the finite-radius robust quantity

`(R_lin^2/4)[Tr F_N/N]`.

### 5.3 Sharpness

The minimal pure-state family of Sec. 2 has

`A=2c|1><0|`,

`J=4c^2`,

`Delta T_U=4c^2`.

The four-outcome equatorial POVM stated there attains

`Tr F_1=4c^2`.

Thus **both inequalities are simultaneously sharp at one copy**.

Collective measurements cannot improve the per-copy coefficient because the first inequality already holds for arbitrary finite `N`.

This sharp arbitrary-POVM two-quadrature result is stronger by a factor of two than bounding the classical FI trace through the multiparameter QFI matrix.

## 6. Coordinate behavior

At the empty sector,

`T_U(0)=0`, `grad T_U(0)=0`.

Therefore its Hessian transforms tensorially under smooth local reparameterizations. The quadratic supply is not an artifact of adding an arbitrary second derivative to a function with nonzero slope.

Nevertheless its numerical value depends on the physical normalization of the modulation coordinates, exactly as Fisher information does. The invariant statement is the comparison between the two tensors/quadratures under the same parameter convention.

## 7. Frequency-resolved energetic interpretation

Suppose `P_U` is an endpoint sector whose occupation represents synthesis of at least an energy quantum `hbar nu` relative to the relevant lower endpoint or resource reference.

Define the two-quadrature **quadratic spectral-energy supply coefficient**

`E_U^(2)(nu):=(hbar nu/4) Delta T_U(0)`.

Then the main theorem gives

> `boxed: E_U^(2)(nu) >= (hbar nu/4)[Tr F_N/N]`.

This is deliberately **not** identified with the total mean-energy curvature `d^2 Tr(H rho)/dtheta^2`. Other second-order redistributions can compensate in total mean energy. The controlled object is the population synthesized in the frequency-resolved endpoint sector.

This distinction is essential.

## 8. The old coherent-sideband no-go saturates the operational coefficient

WP14 used a coherent carrier and a newly synthesized upper sideband. Extend its real modulation parameter to two quadratures:

`alpha_sb(x,y)=(A/2)(x+i y)`,

with `Nbar=|A|^2`.

Then

`n_sb(x,y)=Nbar(x^2+y^2)/4`,

so

`Delta n_sb(0)=Nbar`.

For either single quadrature the coherent-state QFI is `Nbar`. For the simultaneous two-quadrature problem the QFI trace is `2Nbar`, but a single phase-space measurement cannot attain both SLD directions simultaneously.

Heterodyne measurement gives

`Tr F_het=Nbar`.

Therefore

> `Tr F_het = Delta n_sb(0)=Nbar`.

So the coherent-sideband family that destroyed a baseline-energy-only theorem **exactly saturates the sharp arbitrary-POVM two-quadrature curvature law**.

For the original single real sideband amplitude,

`n_sb''(0)=Nbar/2`

and

`F_Q=Nbar=2n_sb''(0)`.

The result charges exactly the second-order sideband population that WP14 showed was missing from baseline energy.

## 9. Exact finite-amplitude two-sector coherence bound

A complementary finite-amplitude statement follows directly from positivity.

Let

`rho=[[rho_D,C^dagger],[C,rho_U]]`

on two orthogonal endpoint sectors `D directsum U`, with

`q_D=Tr(rho_D)`,

`q_U=Tr(rho_U)`.

Positive block-matrix factorization gives

`C=rho_U^(1/2) K rho_D^(1/2)`, `||K||<=1`.

Hence

> `||C||_1^2 <= q_D q_U <= min(q_D,q_U)`.

This matrix/coherence inequality is prior art and is not claimed as new.

## 10. Helstrom discrimination of a finite relative-phase change

Let `rho_phi` differ only by the relative phase of the endpoint coherence,

`C -> exp(i phi)C`,

with diagonal blocks fixed.

Direct singular-value evaluation gives

`D_tr(rho_phi1,rho_phi2)`

`=2|sin[(phi_1-phi_2)/2]| ||C||_1`.

Thus

> `D_tr^2/{4 sin^2[(Delta phi)/2]} <= q_D q_U`.

For `Delta phi=pi`,

> `boxed: D_tr^2/4 <= q_D q_U <= min(q_D,q_U)`.

Because trace distance is the exact arbitrary-POVM binary-discrimination resource, this statement is fully finite amplitude and measurement independent.

With equal priors,

`P_succ=(1+D_tr)/2`.

## 11. Autonomous relational finite-amplitude corollary

Interpret `D` and `U` as two joint clock--signal endpoint sectors connected by an exact exchange gap `nu`:

- in `D`, the clock carries the donor gap;
- in `U`, the signal carries the receiver gap.

Then

`q_D<=T_C(nu)`,

`q_U<=T_S(nu)`.

Therefore

> `D_tr^2/4 <= min{T_C(nu),T_S(nu)}`.

Using the usual tail-to-mean-energy inequality,

> `Ebar_C^+ >= (hbar nu/4)D_tr^2`,
>
> `Ebar_S^+ >= (hbar nu/4)D_tr^2`,
>
> `boxed: Ebar_C^+ + Ebar_S^+ >= (hbar nu/2)D_tr^2`.

This is a finite-amplitude nonlinear two-endpoint analogue of the WP03/WP06 two-sided survival principle. It requires no nonzero `R_lin` and no local Fisher approximation.

The underlying block-positivity and Helstrom ingredients are standard; only the autonomous temporal-resource packaging is a candidate contribution.

## 12. Prior-art audit after the stronger derivation

The following are established and must not be claimed as new:

1. **PSD-cone second-order geometry.** Exact second-order tangent formulas contain the same pseudoinverse curvature structure used in Sec. 3.
2. **Rank-changing QFI/Bures geometry.** Safranek (2017) and subsequent work analyze QFI discontinuities and Hessian corrections from vanishing eigenvalues.
3. **Block-matrix positivity and contraction factorization.** Standard matrix analysis.
4. **Trace-norm/block-coherence population tradeoffs.** Existing subspace-coherence literature derives closely related bounds from positivity.
5. **Helstrom discrimination.** Standard.
6. **Phase estimation, asymmetry, and coherence resource theory.** Standard.
7. **Quantum waveform estimation.** Modern waveform-estimation literature derives QFI/Holevo limits for linear sensors; this must be treated as an adjacent but distinct collision class.

The narrow candidate novelty after this audit is:

> a frequency-resolved, finite-copy, arbitrary-POVM **two-quadrature Fisher-versus-quadratic-spectral-synthesis law**, tied directly to the high-frequency coherent-sideband loophole and autonomous clock--signal resource accounting.

That priority claim remains unverified.

## 13. What WP07 closes

The statement

> `R_lin=0` means high-frequency temporal information escapes any physical resource law

is false.

There are now two rigorously distinct regimes.

### Interior / finite-radius regime

`(R_lin^2/4)[Tr F_N/N] <= pre-existing spectral survival`.

### Boundary / zero-radius support-creation regime

`(1/4)[Tr F_N/N] <= (1/4) Delta T_U(0)`.

Thus arbitrary waveform synthesis does not make high-frequency information free. It changes **the order in the parameter expansion at which the spectral resource appears**:

- zeroth-order population for finite-radius tangents;
- second-order population creation for zero-radius support-creating tangents.

The coherent-sideband counterexample sits exactly in the second regime and saturates its coefficient.

## 14. What remains open

WP07 does **not** yet give one universal scalar law for every arbitrary nonlinear waveform family.

Remaining issues:

1. a general exact-gap tangent can contain both support-to-support and support-to-kernel pieces;
2. a kernel endpoint can occur on the lower rather than upper side of the gap, changing which resource is pre-existing and which is synthesized;
3. multiple gaps and endpoint sectors can coexist;
4. the sharp direct arbitrary-POVM decomposition of mixed interior/boundary pieces is not yet known;
5. total energy curvature can contain compensating redistributions, so frequency-resolved endpoint synthesis is safer than naive `E''(0)`;
6. binary finite-phase discrimination does not reproduce the near-unit continuous-time retention divergence of WP04/WP05, nor should it;
7. an unrestricted autonomous control Hamiltonian can supply the required synthesis resource unless control action/generator resources are also charged.

## 15. Next work — unified endpoint law

The highest-value next target is a **mixed support/interior exact-gap theorem**.

1. Decompose the complex gap tangent into support-to-support, support-to-kernel, and kernel-to-support endpoint pieces.
2. Preserve the sharp WP06 arbitrary-POVM coefficient on the support-to-support component.
3. Preserve the sharp WP07 curvature coefficient on the support-to-kernel component.
4. Determine whether the score-space cross terms admit an exact Minkowski/shorted-operator bound or whether a counterexample proves that no additive scalar unification is possible.
5. Treat the lower-kernel/upper-support case explicitly; it should be charged by pre-existing upper-tail population plus lower-endpoint synthesis rather than upper synthesis.
6. Seek a full finite-amplitude phase-orbit law and a multimode bosonic sideband sum/area theorem.
7. Continue the priority audit against singular quantum metrology, subspace coherence, quantum waveform estimation, and finite autonomous reference frames.
