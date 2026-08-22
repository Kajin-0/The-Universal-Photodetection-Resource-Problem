# WP26 — Herglotz retention spectra and a divergent near-lossless energy law

**Date:** 2026-08-22

**Status:** theorem/proof audit passed for the one-copy exact periodic random-time experiment. The Herglotz law applies to any fixed one-copy POVM after purification and zero-population completion of missing sector labels. The controlled-continuum statement inherits the same common-measurement and convergence qualifications as WP22. No finite-N entangled-collective analogue is claimed.

## 1. Result in one line

For one fixed one-copy measurement, the entire temporal Fisher-retention spectrum is not an arbitrary set of modewise numbers. It is a normalized positive-definite Fourier sequence:

`R_M(k)=int cos(k theta) J_M(dtheta)`.

Combining this cross-mode consistency with the energy-tail theorem gives, for `q=R_M(k)` and `nu=k omega0`,

`Ebar+ >= hbar nu A(q)`,

where

`A(q) ~ 1/sqrt(2(1-q))`

as `q -> 1`.

Thus near-perfect retention at any nonzero frequency requires **divergent mean excess energy**.

---

## 2. The Herglotz law does not require an equality source

Start from the purified periodic random-time experiment. Write the uniform baseline as

`rho0=sum_(n>=0) q_n |n><n|`.

If some sector probabilities vanish, enlarge the representation by harmless zero-population basis vectors so that the labels form a complete semibounded chain. Define the full unilateral shift

`V=sum_(n>=0)|n+1><n|`.

Then for every harmonic, including across population gaps,

`A_k=rho0^(1/2) V^k rho0^(1/2)`.

A physical POVM on the original source can be lifted trivially to the purification; this does not change its outcome probabilities or Fisher information. Therefore the construction below constrains an **actual fixed one-copy POVM**, not an optimal POVM and not merely the purified upper bound.

Let

`rho0^(1/2) M(dy) rho0^(1/2)=X_y p(dy)`

be the trace-class Radon--Nikodym posterior decomposition. Then `X_y` is a density operator almost everywhere and

`R_M(k)=int |Tr(V^k X_y)|^2 p(dy)`.

For each `X_y`, let `P_y` be its canonical phase distribution. Its kth Fourier coefficient is

`phi_y(k)=Tr(V^k X_y)`.

The reflected-convolution phase-difference law

`J_y=P_y * check(P_y)`

has Fourier coefficient `|phi_y(k)|^2`. Averaging over outcomes gives the symmetric probability law

`J_M=int J_y p(dy)`

and therefore

`R_M(k)=int cos(k theta) J_M(dtheta)`.

Consequences:

- `R_M(0)=1`;
- `0<=R_M(k)<=1`;
- `{R_M(k)}_(k in Z)` is positive definite;
- every finite Toeplitz matrix `[R_M(i-j)]` is positive semidefinite.

The Herglotz theorem itself is classical prior mathematics. The candidate contribution is identifying this structure for the classical Fisher-retention spectrum of an arbitrary fixed measurement in the random-time experiment.

---

## 3. Cross-harmonic propagation from Hilbert-space angle geometry

Let

`q=R_M(k)`

and

`theta_q=arccos(q)`.

In the real Hilbert space underlying `L^2(J_M)`, set

`u_j(theta)=exp(i j k theta)`.

Each `u_j` has unit norm and

`<u_(j-1),u_j>_R=q`.

The spherical angle

`d(u,v)=arccos(<u,v>_R)`

is a metric on the unit sphere. Hence

`arccos R_M(mk) <= m arccos q`.

When `m theta_q <= pi`, monotonicity of cosine on `[0,pi]` gives

`R_M(mk) >= cos(m theta_q)`.

In particular, for the positive-cosine range `1 <= m <= floor[pi/(2 theta_q)]`,

`R_M(mk) >= cos(m theta_q) >= 0`.

No later positive lobes of `cos(m theta_q)` are inferred once `m theta_q>pi`; the spherical-angle bound is then only trivial. The elementary consequence below remains valid for every integer `m`.

On the positive-cosine range this strictly strengthens the elementary consequence

`1-R_M(mk) <= m^2 [1-R_M(k)]`.

For `m=2`, it contains the 3x3 Toeplitz-minor inequality

`R_M(2k)>=2q^2-1`.

The important point is conceptual: high retention at one harmonic forces nontrivial retention over an entire ladder of multiples under the *same physical measurement*.

---

## 4. Strong block-tail energy theorem

Use the exact tail sum

`nbar=sum_(j>=1)T_j`

and tail monotonicity. Let

`M_q=floor[pi/(2 theta_q)]`.

For each `m<=M_q`, every index in the block

`(m-1)k < j <= mk`

satisfies

`T_j >= T_(mk) >= R_M(mk) >= cos(m theta_q)`.

Therefore

`nbar >= k sum_(m=1)^(M_q) cos(m theta_q)`.

Define

`A(q)=sum_(m=1)^(M_q) cos(m theta_q)`

`= sin(M_q theta_q/2) cos((M_q+1)theta_q/2) / sin(theta_q/2)`.

Then the exact periodic resource law is

`nbar >= k A(q)`.

In energy units,

`Ebar+ >= hbar nu A(q)`.

The first term of `A` is `q`, so this contains the old pointwise law `Ebar+>=hbar nu q`. Additional positive cosine terms make it strictly stronger whenever the common-measurement spectrum is forced to carry significant higher-multiple retention.

If `q=1`, the angle is zero and every multiple would have unit retention. Then `T_(mk)>=1` for arbitrarily large `m`, contradicting `T_j -> 0` for any normalized probability distribution on a semibounded countable spectrum. Thus exact unit retention at a nonzero harmonic is unattainable for any normalized source; the energy divergence below describes the asymptotic approach `q -> 1`.

---

## 5. Near-lossless asymptotic law

As `q -> 1`,

`theta_q=arccos q ~ sqrt(2(1-q))`,

while `M_q theta_q -> pi/2`. The positive cosine sum is a Riemann sum:

`A(q) ~ theta_q^(-1) int_0^(pi/2) cos(x) dx`

`=1/theta_q`

`~1/sqrt(2(1-q))`.

Thus

`Ebar+ >= [hbar nu / sqrt(2(1-q))] [1+o(1)]`.

Equivalently, for large available resource,

`1-R_M(nu) >= (1/2)(hbar nu/Ebar+)^2 [1+o(1)]`.

This is qualitatively stronger than the original Planck-scale pointwise corollary, which approached the finite value `hbar nu` as `R -> 1`. Here **unit retention is an unattainable limit whose approach requires divergent mean excess energy**.

The divergence exponent `1/2` arises from two independent facts:

1. normalized positive-definite spectra cannot fall arbitrarily fast away from a value near one;
2. semibounded spectral tails are monotone, so forced retention at discrete multiples consumes entire frequency blocks of the energy survival function.

Neither ingredient alone yields the final blow-up law.

---

## 6. Controlled continuum version

Suppose a controlled periodic-to-continuum family uses one common one-copy POVM per approximant and the normalized retention functions converge so that the positive-definite structure is preserved. Bochner's theorem then gives

`R(nu)=int cos(nu t) J(dt)`

for a symmetric probability measure `J` on the real line.

Throughout the positive-cosine range,

`R(m nu)>=cos[m arccos R(nu)]`.

The continuum survival law gives `S(omega)>=R(omega)`, while

`Ebar+/hbar=int_0^infinity S(omega)domega`.

Partitioning the positive frequency axis into blocks of width `nu` yields

`Ebar+ >= hbar nu A(R(nu))`.

Therefore the same near-lossless divergence survives the controlled continuum limit:

`Ebar+ >= hbar nu / sqrt(2(1-R(nu))) [1+o(1)]`.

Do not remove either the common-measurement or controlled-limit qualification.

---

## 7. Relation to WP25

WP25 and WP26 constrain different objects:

- WP25 classifies source populations that **saturate** the modewise energy-tail ceiling;
- WP26 constrains the **shape of the retention spectrum of any one fixed measurement**, whether or not it saturates anything.

The completely monotone equality cone from WP25 lies naturally inside the Herglotz cone. For example,

`R(nu)=exp(-beta |nu|)`

is both completely monotone on the positive axis and positive definite on the real line; its Bochner measure is Cauchy. More generally, mixtures of exponential survival laws correspond to mixtures of Cauchy phase-difference laws.

This explains why the exponential-energy/Cauchy-time pair emerged as an extreme equality case: the energy-side Hausdorff/Bernstein cone and the timing-side Herglotz/Bochner cone meet there exactly.

---

## 8. Finite-N boundary

Do **not** automatically promote WP26 to arbitrary entangled collective measurements on `N>1` copies.

For the `N`-copy tangent,

`B_(k,N)=sum_j V_j^k`.

The natural normalized Fourier coefficient is associated with `B_(k,N)/N`, whereas the per-copy Fisher retention is `(1/N)|Tr(B_(k,N)X)|^2`. The `k=0` normalization therefore does not match the one-copy Herglotz sequence in the way needed for the same high-retention argument.

The finite-copy **modewise tail theorem remains valid**, but the cross-mode Herglotz law is presently a one-copy/common-measurement theorem. Do not claim otherwise without a new proof.

---

## 9. Priority boundary

Do not claim novelty for:

- Herglotz theorem;
- Bochner theorem;
- Toeplitz positive-definiteness;
- canonical phase distributions;
- characteristic functions and difference distributions;
- spherical-angle triangle inequalities.

Targeted web searches on 2026-08-22 found adjacent work on quantum phase distributions, temporal Fisher information, and quantum speed limits, but did not identify an exact predecessor of the present combination:

1. the classical Fisher-retention spectrum of one actual POVM is positive definite across temporal harmonics;
2. this forces cross-harmonic retention propagation;
3. semibounded energy-tail monotonicity converts that propagation into a divergent near-lossless energy law.

Priority remains **unverified, not certified**.

Recent adjacent temporal-Fisher work: T. Nishiyama and Y. Hasegawa, *Unified speed limits in classical and quantum dynamics via temporal Fisher information*, Phys. Rev. E 114, 014120 (2026). It concerns dynamical speed limits/costs rather than random-time source-to-record retention.

---

## 10. Numerical audit

`grand_challenge/numerics/verify_herglotz_high_retention.py` checks:

- Toeplitz positive semidefiniteness for random posterior phase mixtures;
- the Hilbert-angle lower bound on the positive-cosine multiple range;
- the block-tail energy inequality for exact equality sources;
- the closed finite-cosine-sum formula for `A(q)`;
- convergence of `sqrt(1-q) A(q)` to `1/sqrt(2)`.

Numerics are validation only; the results above are analytic.
