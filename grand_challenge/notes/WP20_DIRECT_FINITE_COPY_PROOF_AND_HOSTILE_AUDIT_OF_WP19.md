# WP20 — Direct finite-copy proof and hostile audit of WP19

**Date:** 2026-08-22

## Status

**WP19 survives hostile audit and is strengthened substantially.**

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

## 1. One-copy factorization

At the uniform random-time baseline, for the purified pure excitation write

`rho0 = sum_n q_n |phi_n><phi_n|`,

where the participating `|phi_n>` lie in mutually orthogonal total-energy sectors.

Define the unilateral sector shift

`V_k = sum_{n>=0} |phi_{n+k}><phi_n|`.

On the participating subspace,

`V_k^dagger V_k = I`,

while

`V_k V_k^dagger = P_>=k`,

where `P_>=k` projects onto participating sectors with index at least `k`.

The complex mode tangent is

`A_k = sum_n sqrt(q_n q_{n+k}) |phi_{n+k}><phi_n|`.

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

`=Tr[M_y rho0 P_>=k]`.

Therefore

`boxed: |z_y|^2/p_y <= Tr[M_y rho0 P_>=k]`.

Summing/integrating over all POVM outcomes and using `int M(dy)=I`,

`Tr F_1^(k)`

`<= Tr(rho0 P_>=k)`

`= sum_{m>=k}q_m`

`=T_k`.

Thus the pointwise tail bound follows directly for one arbitrary POVM, with no Fisher/QFI optimization theorem required.

---

## 3. Exact finite-N collective extension

For `N` independently encoded copies,

`rho_N=rho0^tensor N`.

The complex derivative of the product state is

`A_(k,N)=sum_{j=1}^N rho0^tensor(j-1) tensor A_k tensor rho0^tensor(N-j)`.

Define

`B_(k,N)=sum_{j=1}^N V_k^(j)`.

Because `rho0^(1/2) I rho0^(1/2)=rho0`,

`boxed: A_(k,N)=rho_N^(1/2) B_(k,N) rho_N^(1/2)`.

For an arbitrary joint POVM element `M_y` on all `N` copies, the same Hilbert--Schmidt argument yields

`|Tr(A_(k,N)M_y)|^2 / Tr(rho_N M_y)`

`<= Tr[M_y rho_N^(1/2) B_(k,N) B_(k,N)^dagger rho_N^(1/2)]`.

Summing over outcomes gives

`Tr F_N^(k) <= Tr[rho_N B_(k,N) B_(k,N)^dagger]`.

Expand the right side:

`B B^dagger = sum_j V_j V_j^dagger + sum_{i!=j} V_i V_j^dagger`.

For each diagonal term,

`Tr[rho_N V_j V_j^dagger]=Tr[rho0 V_k V_k^dagger]=T_k`.

For `i!=j`, product structure gives

`Tr[rho_N V_i V_j^dagger]`

`=Tr(rho0 V_k) Tr(rho0 V_k^dagger)`

`=0`,

because a nonzero sector shift has zero diagonal expectation in the twirled state:

`Tr(rho0 V_k)=0` for `k>=1`.

Hence

`Tr[rho_N B B^dagger]=N T_k`.

Therefore

`boxed: Tr F_N^(k) <= N T_k`.

This is an exact finite-copy inequality for arbitrary entangled collective POVMs.

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

`sum_n sqrt(q_nq_{n+k}) <= sqrt[(sum_n q_n)(sum_n q_{n+k})] <=1`.

The shift `V_k` is bounded with operator norm `1` on the participating sector chain.

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

`(1/N) sum_{k>=1} Tr F_N^(k)`

`<= sum_{k>=1}T_k`

`=sum_m m q_m`

`=nbar`.

Under the WP12 controlled periodic-to-continuum limit,

`T_k -> S_q(nu)=P(Omega>=nu)`

for `k delta -> nu`.

Therefore

`boxed: R(nu)<=S_q(nu)`.

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

WP19's geometric equality family remains correct.

For

`q_n=(1-r)r^n`,

`T_k=r^k`.

The canonical phase POVM has

`Tr F_1^(k)=|sum_n sqrt(q_nq_{n+k})|^2=r^k=T_k`.

Thus the direct Cauchy--Schwarz inequality is simultaneously saturated for every mode by the same one-copy measurement.

The continuum limit `r=exp(-beta delta)` gives

`q(omega)=beta exp(-beta omega)`

and

`R(nu)=exp(-beta|nu|)=S_q(|nu|)`,

recovering the Cauchy timestamp equality family.

---

## 9. Numerical sanity check

Independent finite-dimensional random-POVM checks were performed for representative finite sector distributions at `N=1` and `N=2`. In every case the directly computed two-quadrature classical Fisher trace was below `N T_k`, as required. These calculations are validation only; the theorem is analytic.

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

Targeted searches still have not located the specific random-time translation theorem

`Tr F_N^(k) <= N sum_{m>=k}q_m`,

its all-mode mean-generator budget, or the continuum source-to-record survival-function law.

Priority remains **unverified**, not certified.

---

## 11. Decision

WP19's main theorem is retained, but its original Holevo proof should be treated as superseded by WP20.

The current strongest operational statement is now supported by a direct finite-copy proof:

> For independent random-time encoding of a fixed semibounded-energy excitation, every parameter-independent collective detector measurement obeys a pointwise temporal-mode Fisher-retention ceiling equal to the excitation-energy survival probability above that modulation frequency.

The next highest-value gates are:

1. continue the exact-priority search for the tail/survival theorem;
2. harden the periodic-to-continuum convergence statement;
3. harden WP13's quantum-marked Poisson-to-bosonic-field channel map;
4. then reconsider manuscript formation.