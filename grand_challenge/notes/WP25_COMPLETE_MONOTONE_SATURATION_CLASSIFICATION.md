# WP25 — Complete-monotone classification of exact Fisher-tail saturators

**Date:** 2026-08-22

**Status:** new theorem candidate; direct derivation complete at the one-copy level, continuum equality cone identified; finite-copy collective converse remains open and is **not** claimed.

## Motivation

Rev8 proves the sharp upper-tail law

`Tr F_1^(k) <= min(D_k,U_k) <= T_k`

and exhibits the geometric spectrum

`q_n=(1-r)r^n`

with the canonical phase POVM as one family saturating every harmonic simultaneously.

The new observation is that the geometric family is only an extreme point of a much larger equality cone.  Exact one-copy saturation is governed by the classical Hausdorff moment / complete-monotonicity structure.

This materially strengthens the equality story: the spectral distributions for which the operational tail ceiling is exactly attainable can be characterized, rather than merely exemplified.

---

# 1. Setting

Assume the full contiguous semibounded chain

`n=0,1,2,...`

with

`q_n>0`, `sum_n q_n=1`,

and baseline state

`rho0=sum_n q_n |n><n|`.

For harmonic `k`, let

`V_k=sum_(n>=0) |n+k><n| = V^k`,

where `V` is the unilateral forward shift.  Then

`A_k=rho0^(1/2) V_k rho0^(1/2)`

and, because the support is contiguous,

`D_k=1`,

`U_k=T_k=sum_(m>=k)q_m`.

Thus the active one-copy operational bound is

`Tr F_1^(k) <= T_k`.

---

# 2. Posterior-state form of the Cauchy--Schwarz proof

For an arbitrary POVM with baseline outcome measure `p(dy)`, define the positive trace-class operator-valued measure

`tau(dy)=rho0^(1/2) M(dy) rho0^(1/2)`.

Its scalar trace is the baseline probability measure:

`p(dy)=Tr tau(dy)`.

On outcomes of nonzero baseline probability, write the Radon--Nikodym posterior state as

`tau(dy)=X_y p(dy)`,

with `X_y>=0`, `Tr X_y=1`, and

`int X_y p(dy)=rho0`.

For harmonic `k`,

`z_k(y)=Tr(A_k M(dy))/p(dy)=Tr(V_k X_y)`

in density form, and therefore

`Tr F_1^(k)=int |Tr(V_k X_y)|^2 p(dy)`.

The range-side Cauchy--Schwarz inequality becomes the elementary state inequality

`|Tr(V_k X)|^2 <= Tr(X V_k V_k^dagger)`.

Integrating gives

`Tr F_1^(k) <= Tr(rho0 V_k V_k^dagger)=T_k`.

This form makes the equality condition transparent.

---

# 3. Equality condition for k=1

For `k=1`, equality in

`|Tr(V X)|^2 <= Tr(X V V^dagger)`

is equality in Cauchy--Schwarz for the semi-inner product

`<A,B>_X = Tr(X A^dagger B)`.

Hence equality holds iff

`(V^dagger-c I) X^(1/2)=0`

for some complex `c`.

Therefore the support of `X` lies in an eigenspace of the backward unilateral shift `V^dagger`.

For `|c|<1`, the normalized eigenvector is

`|psi_c> = sqrt(1-|c|^2) sum_(n>=0) c^n |n>`

and the eigenspace is one-dimensional.  Consequently every posterior state appearing in an exactly saturating measurement must be

`X=|psi_c><psi_c|`.

Writing

`r=|c|^2 in [0,1)`,

the corresponding sector probabilities are exactly geometric:

`|<n|psi_c>|^2=(1-r)r^n`.

Since the posterior ensemble averages back to `rho0`, exact first-harmonic saturation implies

`q_n = int_[0,1) (1-r) r^n pi(dr)`

for a probability measure `pi`.

Thus the sector distribution must be a **mixture of geometric pmfs**.

---

# 4. Sufficiency and simultaneous all-harmonic saturation

Conversely, suppose

`q_n = int_[0,1) (1-r) r^n pi(dr)`.

For each `r` and phase `theta`, define

`|psi_(r,theta)> = sqrt(1-r) sum_(n>=0) r^(n/2) exp(i n theta)|n>`.

Uniform phase averaging removes all off-diagonal terms:

`rho0 = int pi(dr) int_(0)^(2pi) dtheta/(2pi) |psi_(r,theta)><psi_(r,theta)|`.

This ensemble induces the valid source-adapted POVM

`M(dr,dtheta) = rho0^(-1/2) [pi(dr)dtheta/(2pi) |psi_(r,theta)><psi_(r,theta)|] rho0^(-1/2)`

on the support of `rho0` (plus the orthogonal complement projector if needed).

Because

`(V^dagger)^k |psi_(r,theta)> = r^(k/2) exp(i k theta)|psi_(r,theta)>`,

its harmonic-`k` Fisher trace is

`Tr F_1^(k) = int pi(dr) r^k`.

But the spectral tail is

`T_k = sum_(n>=k) q_n = int pi(dr) r^k`.

Therefore

`Tr F_1^(k)=T_k`

for **every k simultaneously under one common POVM**.

A product of this one-copy POVM also saturates the per-copy bound for every finite number of independent copies.  This is only a sufficiency statement for finite `N`; the converse for arbitrary entangled collective POVMs at `N>1` is not yet proved.

---

# 5. Equivalent Hausdorff / complete-monotonicity characterizations

Define the tail sequence

`T_0=1`,

`T_k=sum_(n>=k)q_n`.

The mixture representation gives

`T_k=int_[0,1) r^k pi(dr)`.

Hence `T_k` is a **Hausdorff moment sequence**.

Equivalently, it is completely monotone in the discrete sense:

`(-1)^j Delta^j T_k >=0`

for all `j,k>=0`.

Likewise `q_n` itself is a completely monotone pmf, equivalently a mixture of geometric pmfs.

The classical equivalence between completely monotone pmfs and geometric mixtures is prior mathematics (Hausdorff moment theorem; Steutel and later statistical literature).  The new candidate contribution is the connection between that structure and **exact saturation of the arbitrary-POVM temporal Fisher-tail law**.

For the full contiguous one-copy chain, the following are therefore equivalent:

1. the first-harmonic tail bound `Tr F_1^(1)<=T_1` is attained;
2. `q_n` is a mixture of geometric pmfs;
3. `T_k` is a Hausdorff moment sequence;
4. one common POVM saturates `Tr F_1^(k)=T_k` for every `k`;
5. if `sum n q_n<infinity`, the same POVM saturates the all-mode budget `sum_(k>=1)Tr F_1^(k)=nbar`.

This is a rigidity / complete-extremizer theorem at the one-copy level.

---

# 6. Continuum equality cone

Let `Pi` be a probability measure on rates `beta>0` and define the continuous excess-frequency density

`q(omega)=int beta exp(-beta omega) Pi(dbeta)`, `omega>=0`.

Its survival function is

`S(nu)=int exp(-beta nu) Pi(dbeta)`.

For every lattice spacing `delta>0`, exact lower-bin probabilities are

`q_n^(delta)=int_[n delta,(n+1)delta) q(omega)domega`

`=int [1-exp(-beta delta)] exp(-beta n delta) Pi(dbeta)`.

Thus **every periodic approximant is exactly a mixture of geometric distributions** with

`r=exp(-beta delta)`.

By the discrete equality theorem, one common source-adapted POVM saturates every lattice harmonic for every `delta`:

`R_delta(k)=T_k^(delta)=S(k delta)`.

Hence the controlled continuum limit satisfies the exact equality

`R(nu)=S(nu)`

for the entire mixture-of-exponentials class.

By the Hausdorff--Bernstein--Widder theorem, normalized completely monotone survival functions on `[0,infinity)` are precisely Laplace transforms of positive probability measures.  Thus the continuum equality cone is naturally the class of **completely monotone survival laws / mixtures of exponential spectra**, subject to the finite-mean condition

`int_0^infinity S(nu)dnu = int beta^(-1) Pi(dbeta) < infinity`

when the mean excess energy is required to be finite.

The exponential spectrum in Rev8 is the extreme-point case `Pi=delta_beta`.

---

# 7. Non-exponential exact equality examples

A gamma mixing distribution for `beta` produces algebraic survival.  For example, if

`beta ~ Gamma(alpha, rate=a)`,

then

`S(nu)=(a/(a+nu))^alpha`.

The corresponding excess-frequency density is

`q(omega)=alpha a^alpha/(a+omega)^(alpha+1)`.

For `alpha>1`,

`<Omega>=a/(alpha-1)`

is finite.

Thus the exact Fisher-survival equality class contains heavy-tailed algebraic retention laws, not only the exponential/Cauchy extreme point.

The saturating POVM can be interpreted as a rate-resolved mixture of the exponential-spectrum equality measurements.  Conditional on `beta`, the corresponding transform-limited spectral amplitude produces a Cauchy timing kernel; retaining the `beta` outcome label is part of the optimal generalized measurement.

---

# 8. Why this matters for significance

Rev8 currently exhibits one exact equality family.  WP25 instead supplies a **classification theorem** and connects the operational quantum-metrology extremizers to classical moment theory:

- quantum arbitrary-POVM Fisher saturation;
- unilateral-shift eigenvectors;
- mixtures of geometric distributions;
- Hausdorff moment sequences;
- complete monotonicity;
- Bernstein/Laplace mixtures in the continuum.

This is qualitatively deeper than adding another physical example or detector extension.  It changes the equality result from “there exists a sharp family” to “the one-copy exact saturators are characterized by a classical rigidity structure.”

---

# 9. Prior-art boundary

Do **not** claim novelty for:

- Hausdorff moment theorem;
- complete monotonicity;
- mixtures of geometric pmfs;
- mixtures of exponential densities;
- Bernstein--Widder representation;
- unilateral/backward-shift eigenvectors;
- canonical phase POVMs.

Targeted web searches on 2026-08-22 did not identify a prior quantum-metrology result connecting these classical structures to exact saturation of an arbitrary-POVM temporal Fisher-tail resource law.  Priority remains **unverified, not certified**.

Useful classical provenance found:

- F. Balabdaoui and G. de Fournas-Labrosse, *Least squares estimation of a completely monotone pmf: From Analysis to Statistics*, J. Stat. Plann. Inference 204, 55--71 (2020), DOI `10.1016/j.jspi.2019.04.006`.  Explicitly states the Hausdorff-theorem equivalence between completely monotone pmfs and mixtures of geometric pmfs.
- F. Balabdaoui and Y. Kulagina, *Completely monotone distributions: Mixing, approximation and estimation of number of species*, Comput. Stat. Data Anal. 150, 107014 (2020), DOI `10.1016/j.csda.2020.107014`.
- R. L. Schilling, R. Song, and Z. Vondracek, *Bernstein Functions: Theory and Applications*, De Gruyter (2nd ed. 2012; later editions available), Chapter 1: Laplace transforms and completely monotone functions, DOI `10.1515/9783110269338.1`.

---

# 10. Next theorem gates

Before promotion into a manuscript revision:

1. hostile-audit the operator-valued Radon--Nikodym step for fully general POVMs;
2. write the equality proof first for dominated/countable POVMs, then determine the cleanest general-outcome formulation;
3. test the equivalence numerically for finite truncations approaching the infinite chain;
4. verify the continuum mixture construction exactly at the lower-bin level;
5. decide whether the finite-`N` **converse** can be proved.  Do not claim it unless established;
6. run a targeted literature search specifically for quantum phase/Fisher extremizer classifications involving completely monotone or geometric-mixture spectra.

If these gates pass, WP25 is strong enough to justify a genuine Rev9 scientific revision rather than another polish pass.
