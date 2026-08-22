# WP21 — Targeted priority audit for the operational survival-function law

**Date:** 2026-08-22

## Status

**No exact predecessor located in this targeted pass. Priority remains unverified.**

WP20 reduces the strongest operational theorem to a direct finite-copy POVM contraction for the special random-time tangent factorization

`A_k = rho^(1/2) V_k rho^(1/2)`,

where `V_k` is a semibounded energy-sector shift and

`V_k V_k^dagger = P_>=k`.

The theorem is

`Tr F_N^(k)/N <= Tr(rho P_>=k)=T_k`,

followed by

`sum_{k>=1}T_k=nbar`

and, in the controlled continuum limit,

`R(nu)<=P(Omega>=nu)`.

This audit searched specifically for prior work that could already contain this result under phase-estimation, random-unitary, information-geometric, or Fourier-analysis language.

---

## 1. Generic arbitrary-measurement Fisher bounds are prior art

Richard D. Gill, *Conciliation of Bayes and Pointwise Quantum State Estimation: Asymptotic information bounds in quantum statistics*, arXiv:math/0512443; published in *Quantum Stochastics and Information* (World Scientific, 2008), develops dual Holevo bounds that can be interpreted as upper bounds on the Fisher-information matrix obtainable from arbitrary measurements on multiple identical quantum systems.

Therefore do **not** claim novelty for the existence of finite-copy/arbitrary-collective upper bounds on classical Fisher information.

WP20 is more specialized: the random-time Fourier tangent admits a shift-factorization whose measurement bound evaluates to the explicit energy-tail probability `T_k` and whose harmonic sum is exactly the mean excitation index.

---

## 2. Random-unitary probability estimation is prior art

Fujiwara and Imai, *A fibre bundle over manifolds of quantum channels and its application to quantum statistics*, J. Phys. A **36**, 8093 (2003), DOI `10.1088/0305-4470/36/29/314`, treat statistical estimation for generalized Pauli/random-unitary channels parameterized by mixing probabilities and optimize SLD Fisher information.

Modern work also explicitly studies multiparameter estimation of convex mixture weights in unitary channels.

Therefore do **not** frame the contribution as the first quantum estimation theory for unknown random-unitary mixing distributions.

The candidate distinction is the `U(1)` random-time distribution, Fourier-mode coordinates, semibounded generator, and exact tail/mean-generator operational budget.

---

## 3. Phase/Fourier estimation under photon-number constraints is prior art

The closest older phase-estimation literature includes:

- Bužek, Derka, and Massar, *Optimal Quantum Clocks*, Phys. Rev. Lett. **82**, 2207 (1999), DOI `10.1103/PhysRevLett.82.2207`;
- Imai and Hayashi, *Fourier Analytic Approach to Phase Estimation in Quantum Systems*, New J. Phys. **11**, 043034 (2009), DOI `10.1088/1367-2630/11/4/043034`;
- Hayashi, *Phase estimation with photon number constraint*, Progress in Informatics **8**, 81--87 (2011), DOI `10.2201/NiiPi.2011.8.9`, arXiv:1011.2546.

These works establish that:

- phase estimation is naturally a Fourier/covariant problem;
- globally attainable performance can differ from local SLD-Fisher optima;
- photon-number constraints impose nontrivial phase-estimation limits;
- optimal states/measurements can be derived with Fourier analytic methods.

Thus the broad narrative `energy/photon number constrains phase/timing information` is not new.

However, the searched works optimize estimation of a deterministic phase/time-shift parameter. WP20 instead estimates Fourier coefficients of a **latent random-time probability distribution after the absolute phase has been twirled out**. The theorem controls source-to-record Fisher transfer for each distribution harmonic by an upper energy-tail probability.

---

## 4. Canonical phase moments are prior art

Canonical phase distributions and their exponential/Fourier moments are classical quantum-optics material. In number basis, canonical phase Fourier moments involve energy-number coherences separated by `k`, and there is extensive literature on measuring or reconstructing those moments.

Positivity gives the standard matrix-element inequality

`|rho_mn|^2 <= rho_mm rho_nn`,

and Cauchy--Schwarz gives familiar bounds on sums of coherence amplitudes.

Therefore neither the shift operator `V_k`, canonical phase POVM, nor Fourier moment sums should be advertised as novel mathematical objects.

WP19/WP20 use the canonical phase POVM only as the exact equality construction for the geometric sector distribution.

---

## 5. Monotone quantum Fisher metrics are prior art

Classical Fisher information produced by a POVM is bounded by appropriate quantum monotone metrics; SLD, RLD, and the wider Petz family are established information geometry.

WP20's outcome-wise Hilbert--Schmidt Cauchy--Schwarz proof is closely related in spirit to such metric contraction arguments.

Accordingly do **not** claim novelty for `measurement cannot increase a suitable quantum Fisher metric`.

The special content is the exact evaluation produced by the random-time tangent factorization:

`rho^(1/2) V_k V_k^dagger rho^(1/2)=rho P_>=k`,

so the resulting operational metric budget is not an abstract matrix but the physically transparent survival probability

`T_k=P(N>=k)`.

---

## 6. Exact searches performed

Searches were run using combinations of:

- `sqrt(q_n q_{n+k})` / `sqrt(p_n p_{n+k})`;
- canonical phase plus photon-number distribution;
- exponential phase moments plus photon-number bounds;
- Fisher information plus photon-number tail;
- phase estimation plus survival/tail probability;
- random-unitary mixture probabilities plus Fisher information;
- dual Holevo/Fisher-information inequalities for collective measurements;
- Fourier phase estimation under mean/maximum photon-number constraints.

The searches found the neighboring literatures above but did not locate an explicit theorem equivalent to

`boxed: Tr F_N^(k)/N <= sum_{m>=k}q_m`,

nor

`boxed: sum_{k>=1} Tr F_N^(k)/N <= nbar`,

nor the continuum source-to-record statement

`boxed: R(nu)<=P(Omega>=nu)`.

Absence in these searches is not proof of novelty.

---

## 7. Revised novelty boundary

The strongest defensible candidate contribution is now narrowly stated as follows:

> For random temporal-distribution encoding of a fixed semibounded-energy excitation, the `k`th Fourier tangent factorizes through a `k`-sector energy shift. This converts the general measurement contraction of Fisher information into the explicit operational ceiling `R(k)<=P(N>=k)`, valid even for arbitrary finite-copy collective measurements. The tail-sum identity then gives a sharp mean-energy budget across all temporal harmonics, with continuum survival-function and Planck-scale pointwise corollaries.

Do not claim novelty for any of the following separately:

- arbitrary-measurement Fisher contraction;
- RLD/SLD/monotone quantum metrics;
- random-unitary probability estimation;
- covariant phase estimation;
- canonical phase POVMs;
- Fourier phase moments;
- photon-number-constrained phase estimation;
- Cauchy--Schwarz or tail-sum identities.

---

## 8. Priority risk assessment

Current qualitative risk:

- **generic ingredients:** high prior-art occupancy;
- **exact discrete tail theorem:** no equivalent located, moderate residual priority risk;
- **all-mode mean-generator sum rule:** no equivalent located, moderate residual priority risk;
- **continuum operational survival law:** no equivalent located, moderate residual priority risk;
- **photodetection/source-to-record interpretation:** appears less occupied than generic phase metrology, but still requires deeper optical-coherence literature search.

The most dangerous remaining hidden predecessor would likely appear under one of:

1. covariant `U(1)` statistical experiments / group estimation;
2. number-phase uncertainty expressed through Fisher information rather than variance/entropy;
3. quantum local asymptotic theory for dephasing/noise-distribution coefficients;
4. coherence-mode resource theory with modewise accessible-information bounds;
5. harmonic analysis of canonical phase measurements with energy-tail constraints.

---

## 9. Decision

WP20's theorem survives this priority pass as a candidate original synthesis/result, but **priority is not certified**.

The project should now stop describing the `pi` QFI coefficient or general quantum-estimation machinery as the headline novelty. The operational survival-function theorem is both simpler and more physically direct.

Next gates:

1. publication-grade continuum-limit theorem;
2. explicit quantum-marked Poisson-to-bosonic-field channel map;
3. one deeper historical search in number-phase/coherence-mode literature;
4. only then manuscript formation.