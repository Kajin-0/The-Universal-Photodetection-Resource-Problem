# WP20 — Direct finite-copy proof and hostile audit of WP19

**Date:** 2026-08-22

## Status

**WP19 survives hostile audit and is strengthened substantially. A support-gap notation issue found in the integrated audit is repaired here.**

The collective survival-function theorem does not require the Holevo Cramer--Rao bound, asymptotic attainability, local asymptotic normality, a repeated-block construction, or finite-dimensional regularity assumptions.

There is a direct outcome-by-outcome POVM inequality valid for every finite number `N` of independently encoded copies. The proof is a Hilbert--Schmidt Cauchy--Schwarz argument plus the orthogonality of nonzero energy-shift operators at the twirled baseline.

For temporal harmonic `k>=1`, with excitation-sector probabilities `q_n` and tail

`T_k = sum_{m>=k} q_m`,

any joint POVM on `N` independently random-time-encoded excitations satisfies

`boxed: Tr F_N^(k) <= N T_k`.

Consequently

`boxed: R_N(k):=Tr F_N^(k)/N <= T_k`,

`boxed: sum_{k>=1} R_N(k) <= nbar`,

and in the continuum

`boxed: R(nu) <= P(Omega>=nu)`.

This is the same theorem claimed in WP19, now with a much shorter and more robust proof.

---

## 1. One-copy factorization with arbitrary support gaps

At the uniform random-time baseline, for the purified pure excitation write

`rho0 = sum_n q_n |phi_n><phi_n|`,

where the nonzero participating `|phi_n>` lie in mutually orthogonal total-energy sectors.

A previous version of this note wrote a unilateral shift as though every intermediate energy sector necessarily existed and participated. That is unnecessarily strong. For arbitrary support, define the **paired partial shift**

`V_k = sum_(n: q_n q_(n+k)>0) |phi_(n+k)><phi_n|`.

Then `V_k` is a partial isometry with

`V_k^dagger V_k = P_dom,k <= I`,

and

`V_k V_k^dagger = P_ran,k <= P_>=k`,

where `P_>=k` projects onto all participating sectors with index at least `k`.

The complex mode tangent is

`A_k = sum_n sqrt(q_n q_(n+k)) |phi_(n+k)><phi_n|`.

It factorizes exactly as

`boxed: A_k = rho0^(1/2) V_k rho0^(1/2)`.

The real cosine/sine derivatives are

`D_c=(A_k+A_k^dagger)/2`,

`D_s=(A_k^dagger-A_k)/(2i)`.

For any POVM outcome element `M_y`, put

`p_y=Tr(rho0 M_y)`

and

`z_y=Tr(A_k M_y)`.

Then

`partial_c p_y = Re z_y`,

`partial_s p_y = -Im z_y`,

so the contribution of this outcome to the two-parameter Fisher trace is

`[(partial_c p_y)^2+(partial_s p_y)^2]/p_y = |z_y|^2/p_y`.

Zero-probability outcomes are understood in the standard limiting convention; DQM/positivity forces zero derivative on any outcome with zero baseline mass in a regular finite-FI experiment.

---

## 2. Direct one-copy Cauchy--Schwarz bound

Using cyclicity of trace,

`z_y = Tr[M_y^(1/2) rho0^(1/2) V_k rho0^(1/2) M_y^(1/2)]`.

Set

`X=M_y^(1/2) rho0^(1/2) V_k`,

`Y=rho0^(1/2) M_y^(1/2)`.

Hilbert--Schmidt Cauchy--Schwarz gives

`|z_y|^2 <= Tr(XX^dagger) Tr(Y^dagger Y)`.

The second factor is exactly

`Tr(Y^dagger Y)=p_y`.

The first is

`Tr(XX^dagger)`

`=Tr[M_y rho0^(1/2) V_k V_k^dagger rho0^(1/2)]`

`=Tr[M_y rho0 P_ran,k]`

`<=Tr[M_y rho0 P_>=k]`.

Therefore

`boxed: |z_y|^2/p_y <= Tr[M_y rho0 P_>=k]`.

Summing/integrating over all POVM outcomes and using `int M(dy)=I`,

`Tr F_1^(k)`

`<= Tr(rho0 P_>=k)`

`= sum_(m>=k)q_m`

`=T_k`.

Thus the pointwise tail bound follows directly for one arbitrary POVM, with no Fisher/QFI optimization theorem required.

The support-gap repair can only make the intermediate bound tighter because `P_ran,k` may be strictly smaller than `P_>=k`.

---

## 3. Exact finite-N collective extension

For `N` independently encoded copies,

`rho_N=rho0^tensor N`.

The complex derivative of the product state is

`A_(k,N)=sum_(j=1)^N rho0^tensor(j-1) tensor A_k tensor rho0^tensor(N-j)`.

Define

`B_(k,N)=sum_(j=1)^N V_k^(j)`.

Because `rho0^(1/2) I rho0^(1/2)=rho0`,

`boxed: A_(k,N)=rho_N^(1/2) B_(k,N) rho_N^(1/2)`.

For an arbitrary joint POVM element `M_y` on all `N` copies, the same Hilbert--Schmidt argument yields

`|Tr(A_(k,N)M_y)|^2 / Tr(rho_N M_y)`

`<= Tr[M_y rho_N^(1/2) B_(k,N) B_(k,N)^dagger rho_N^(1/2)]`.

Summing over outcomes gives

`Tr F_N^(k) <= Tr[rho_N B_(k,N) B_(k,N)^dagger]`.

Expand the right side:

`B B^dagger = sum_j V_j V_j^dagger + sum_(i!=j) V_i V_j^dagger`.

For each diagonal term,

`Tr[rho_N V_j V_j^dagger]`

`=Tr[rho0 V_k V_k^dagger]`

`=Tr(rho0 P_ran,k)`

`<=T_k`.

For `i!=j`, product structure gives

`Tr[rho_N V_i V_j^dagger]`

`=Tr(rho0 V_k) Tr(rho0 V_k^dagger)`

`=0`,

because a nonzero sector shift has zero diagonal expectation in the twirled state:

`Tr(rho0 V_k)=0` for `k>=1`.

Hence

`Tr[rho_N B B^dagger]`

`=N Tr(rho0 P_ran,k)`

`<=N T_k`.

Therefore

`boxed: Tr F_N^(k) <= N T_k`.

This is an exact finite-copy inequality for arbitrary entangled collective POVMs and arbitrary gaps in the participating energy support.

---

## 4. Why this proof is stronger than the WP19 Holevo route

WP19 used:

1. a lower bound on the two-parameter Holevo cost;
2. phase symmetrization of a collective POVM;
3. repeated-block asymptotic classical efficiency;
4. asymptotic Holevo attainability/lower-bound logic.

Those steps are no longer needed.

The direct proof:

- is finite-copy;
- does not invert a Fisher matrix;
- allows singular Fisher blocks automatically;
- does not require isotropizing the measurement;
- does not require a locally unbiased estimator construction;
- does not require finite-dimensional quantum LAN;
- works naturally on a separable countable participating sector space whenever the displayed trace/Hilbert--Schmidt quantities are finite.

Richard Gill's dual-Holevo work is still close methodological prior art for finite-copy Fisher-information inequalities under arbitrary collective measurements, but it is no longer a logical dependency of the theorem.

---

## 5. Infinite-support and domain audit

For a normalized sector distribution `q_n`,

`A_k` is trace class because

`sum_n sqrt(q_nq_(n+k)) <= sqrt[(sum_n q_n)(sum_n q_(n+k))] <=1`.

The paired shift `V_k` is a bounded partial isometry with operator norm at most `1`, regardless of support gaps.

Therefore the factorization

`A_k=rho0^(1/2)V_k rho0^(1/2)`

is well defined for countably infinite support.

For finite `N`, `B_(k,N)` is bounded with norm at most `N`, and all traces used above are finite.

Thus the direct finite-copy proof avoids the main infinite-dimensional regularity concern in the former Holevo proof.

---

## 6. Mixed excitations

For a mixed physical excitation `sigma`, purify it and let time translation act only on the physical system.

The purification has the same total-energy sector probabilities

`q_n=Tr(P_n sigma)`.

The direct pure-state proof applies on the enlarged physical-plus-reference Hilbert space. Any POVM available on the physical copies alone is a restricted POVM on the purified copies (`M tensor I_ref`).

Therefore the same bound holds for arbitrary mixed excitations.

---

## 7. Sum rule and continuum corollaries survive unchanged

Summing the exact finite-copy tail bound over positive modes gives

`(1/N) sum_(k>=1) Tr F_N^(k)`

`<= sum_(k>=1)T_k`

`=sum_m m q_m`

`=nbar`.

WP22 supplies the publication-grade periodic-to-continuum statement for arbitrary positive spectral probability measures. In particular, every controlled modewise continuum limit obeys

`boxed: R(nu)<=S_mu(nu)=P(Omega>=nu)`.

Integrating,

`boxed: int_0^infinity R(nu)dnu<=E[Omega]=omega_bar`,

and two-sided,

`boxed: int_R R(nu)dnu<=2Ebar^+/hbar`.

The pointwise Markov corollary remains

`boxed: Ebar^+ >= hbar nu R(nu)`

and hence at ordinary modulation frequency `f`,

`boxed: Ebar^+ >= h f R(2pi f)`.

---

## 8. Equality audit

WP19's geometric equality family remains correct because it has contiguous full support.

For

`q_n=(1-r)r^n`,

`T_k=r^k` and `P_ran,k=P_>=k`.

The canonical phase POVM has

`Tr F_1^(k)=|sum_n sqrt(q_nq_(n+k))|^2=r^k=T_k`.

Thus the direct Cauchy--Schwarz inequality is simultaneously saturated for every mode by the same one-copy measurement.

The continuum limit `r=exp(-beta delta)` gives

`q(omega)=beta exp(-beta omega)`

and

`R(nu)=exp(-beta|nu|)=S_q(|nu|)`,

recovering the Cauchy timestamp equality family.

---

## 9. Numerical sanity check

Independent finite-dimensional random-POVM checks were performed for representative finite sector distributions at `N=1` and `N=2`. In every case the directly computed two-quadrature classical Fisher trace was below `N T_k`, as required. These calculations are validation only; the theorem is analytic.

The support-gap repair is also immediate numerically: deleting an intermediate occupied sector removes terms from `V_k V_k^dagger` and cannot increase the Cauchy--Schwarz resource trace.

---

## 10. Prior-art update

The direct ingredients are standard:

- POVM Fisher information;
- Hilbert--Schmidt Cauchy--Schwarz;
- partial-isometry energy shifts;
- tensor-product factorization;
- tail-sum/survival identities;
- canonical phase POVMs.

Close quantum-statistics literature also contains general finite-copy information inequalities and dual Holevo bounds for arbitrary collective measurements; see Richard D. Gill, *Conciliation of Bayes and Pointwise Quantum State Estimation: Asymptotic information bounds in quantum statistics* (arXiv:math/0512443; World Scientific 2008), which explicitly develops upper bounds on Fisher-information matrices for arbitrary measurements.

The `U(1)` coherence-mode decomposition itself is also established prior art; see Marvian and Spekkens, Phys. Rev. A **90**, 062110 (2014), DOI `10.1103/PhysRevA.90.062110`.

Targeted searches still have not located the specific random-time translation theorem

`Tr F_N^(k) <= N sum_(m>=k)q_m`,

its all-mode mean-generator budget, or the continuum source-to-record survival-function law.

Priority remains **unverified**, not certified.

---

## 11. Decision

WP19's main theorem is retained, but its original Holevo proof should be treated as superseded by this repaired WP20 proof.

The current strongest operational statement is supported by a direct finite-copy proof:

> For independent random-time encoding of a fixed semibounded-energy excitation, every parameter-independent collective detector measurement obeys a pointwise temporal-mode Fisher-retention ceiling no larger than the excitation-energy survival probability above that modulation frequency.

For spectra with gaps, the actual paired-sector projector `P_ran,k` can make the ceiling stricter than the coarse survival tail `T_k`; `T_k` is the universal energy-only version.

WP22 and WP23 now close the continuum and source-to-bosonic-field formulation gates. The remaining tasks are an integrated hostile review and final priority/manuscript decision.