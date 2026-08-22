# WP24 — Integrated hostile review and symmetry prior-art boundary

**Date:** 2026-08-22

## Status

**WP20--WP23 survive integrated hostile review after one support-gap repair. The operational survival law remains the strongest theorem.**

The review found:

1. no factor-of-two or source-normalization defect in the direct Fisher proof;
2. no collective-measurement loophole;
3. one nonfatal notation issue for missing energy sectors, repaired in WP20 by using a paired partial isometry;
4. a useful bilateral paired-support strengthening;
5. a significant prior-art boundary: Marvian--Spekkens already establish the `U(1)` mode decomposition and the fact that weighted random phase/time twirling multiplies each gap mode by the corresponding Fourier coefficient of the mixing distribution.

Thus the random-time harmonic encoding map itself is not a novelty claim. The candidate contribution is the operational Fisher-resource theorem built on top of that established harmonic structure.

---

## 1. Audited theorem statement

Let a fixed semibounded excitation have periodic total-generator sector probabilities

`q_n`, `n>=0`.

Let a latent random time be weakly perturbed in cosine/sine Fourier harmonic `k>=1` around the uniform distribution.

For any finite number `N` of independently encoded excitations and **any joint POVM**, including arbitrary entangled collective measurements, let `F_N^(k)` be the `2 x 2` classical Fisher block for the cosine/sine amplitudes.

Define the coarse upper energy tail

`T_k=sum_(m>=k)q_m`.

Then

`boxed: Tr F_N^(k) <= N T_k`.

Equivalently, the per-event full two-quadrature operational retention satisfies

`boxed: R_N(k):=Tr F_N^(k)/N <= T_k`.

Summing,

`boxed: sum_(k>=1)R_N(k)<=nbar`.

WP22 gives the continuum limit

`boxed: R(nu)<=P(Omega>=nu)`

and therefore

`boxed: int_R R(nu)dnu<=2Ebar^+/hbar`,

`boxed: Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

WP23 carries the same theorem through an independent compound-Poisson event source, arbitrary parameter-independent formation of a common bosonic field, coherent detector memory, and final measurement.

---

## 2. Bilateral paired-support refinement

The repaired WP20 proof uses the paired partial shift

`V_k=sum_(n:q_n q_(n+k)>0)|phi_(n+k)><phi_n|`.

Define its domain and range projectors

`P_dom,k=V_k^dagger V_k`,

`P_ran,k=V_k V_k^dagger`.

Define the corresponding paired probability masses

`D_k=Tr(rho0 P_dom,k)`

`=sum_(n:q_n q_(n+k)>0)q_n`,

and

`U_k=Tr(rho0 P_ran,k)`

`=sum_(n:q_n q_(n+k)>0)q_(n+k)`.

Clearly

`U_k<=T_k`.

WP20's Cauchy--Schwarz proof applied to

`A_k=rho0^(1/2)V_k rho0^(1/2)`

gives

`Tr F_N^(k)<=N U_k`.

But the same outcome probabilities satisfy

`|Tr(A_k M_y)|=|Tr(A_k^dagger M_y)|`

for Hermitian POVM elements. Applying the identical proof to

`A_k^dagger=rho0^(1/2)V_k^dagger rho0^(1/2)`

gives

`Tr F_N^(k)<=N D_k`.

Hence the stronger state/support-sensitive theorem is

`boxed: Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`.

The survival tail `T_k` remains the clean universal version determined solely by semibounded energy and the population distribution above the lower edge.

### Example: two sectors

For `q_0=1-p`, `q_1=p`, mode `k=1` has

`D_1=1-p`,

`U_1=p`.

Therefore

`R_N(1)<=min(p,1-p)`,

which exactly reproduces the WP18 asymptotic collective two-sector result without Holevo theory.

This is a strong internal cross-check of the direct proof and its normalization.

---

## 3. Factor-of-two audit

At the latent classical source level, one nonzero temporal harmonic is parameterized as

`p_epsilon(theta)=(1/2pi)[1+epsilon_c cos(k theta)+epsilon_s sin(k theta)]`.

At the uniform baseline,

`F_in,cc=F_in,ss=1/2`,

so

`Tr F_in=1` per event.

Therefore defining

`R(k)=Tr F_out^(k)`

is the correct full two-quadrature source-normalized retention.

For a Poisson mean event number `mu`, the input block becomes `(mu/2)I_2`, so its trace is `mu` and

`R=Tr F_out/mu`.

Thus no hidden factor of two remains in WP20/WP23.

The two-sided ordinary/angular-frequency conversion is also consistent:

`int_R R(nu)dnu<=2omega_bar=2Ebar^+/hbar`.

If `nu=2pi f`, then the pointwise law

`Ebar^+>=hbar nu q`

is exactly

`Ebar^+>=h f q`.

---

## 4. Collective-measurement audit

WP20 is already a finite-copy theorem for arbitrary joint POVMs.

The key factorization for `N` copies is

`A_(k,N)=rho_N^(1/2) [sum_j V_k^(j)] rho_N^(1/2)`.

Outcome-wise Hilbert--Schmidt Cauchy--Schwarz bounds the Fisher contribution directly. Cross-copy resource terms vanish because

`Tr(rho0 V_k)=0`

for every nonzero harmonic at the twirled baseline.

No separability, adaptivity restriction, covariance of the detector, Holevo asymptotics, or estimator attainability assumption is used.

Therefore the former collective-measurement gate is genuinely closed for the independent random-time source model.

---

## 5. Equality audit

For the geometric full-support distribution

`q_n=(1-r)r^n`,

`D_k=1`,

`U_k=T_k=r^k`.

The canonical phase POVM gives

`R(k)=r^k`.

Thus the coarse survival ceiling and the bilateral refinement are both saturated on the range side for every `k` by the same one-copy POVM.

The continuum exponential law

`q(omega)=beta exp(-beta omega)`

has

`R(nu)=P(Omega>=|nu|)=exp(-beta|nu|)`

and saturates

`int_0^infinity R=omega_bar=1/beta`.

Therefore the operational coefficient `2E/hbar` is exact, not merely an upper-bound artifact.

---

## 6. Major prior-art collision: weighted `U(1)` twirling

Marvian and Spekkens, *Modes of asymmetry: The application of harmonic analysis to symmetric quantum dynamics and quantum reference frames*, Phys. Rev. A **90**, 062110 (2014), DOI `10.1103/PhysRevA.90.062110`, provide the directly relevant harmonic framework.

For a `U(1)` representation they decompose operators into gap modes `rho^(k)` and show that a weighted twirling operation

`sigma=int p(theta) U(theta)rho U(theta)^dagger dtheta`

obeys

`sigma^(k)=p_(-k) rho^(k)`,

where `p_k` is the Fourier transform/coefficient of the probability distribution.

This is essentially the kinematic statement underlying the project's random-time distribution encoding: Fourier coefficients of the latent time/phase law modulate corresponding energy-gap coherence modes.

They also develop modewise asymmetry monotones such as

`||rho^(k)||_1`,

which are nonincreasing under `U(1)`-covariant dynamics.

Therefore **do not claim novelty** for:

- decomposing the state into energy-gap modes;
- identifying the random-time Fourier coefficient with the multiplier of the corresponding gap mode;
- using shift/gap operators to represent these modes;
- modewise coherence/asymmetry monotones under covariant processing.

This prior-art collision materially narrows the manuscript's novelty language.

---

## 7. Why the operational Fisher theorem is not supplied by that prior art

The Marvian--Spekkens results concern harmonic decomposition and asymmetry monotonicity under symmetry-respecting transformations.

WP20 asks a different local statistical question:

> Given a symmetric/twirled baseline and a small perturbation of the **probability distribution over translations**, how much classical Fisher information about the two real Fourier coefficients can any measurement extract?

The direct theorem is valid for arbitrary parameter-independent measurements/channels, not only `U(1)`-covariant ones, because the parameter is already encoded upstream and the proof acts on the final POVM itself.

The resource evaluates to a population support/tail:

`R(k)<=min(D_k,U_k)<=P(N>=k)`.

Summing that explicit tail gives the mean generator. The targeted searches to date have not found this Fisher-statistical step or the resulting mean-energy/survival law in the asymmetry literature.

Accordingly, the candidate contribution is not a new mode decomposition but a new **operational statistical inequality for perturbations of the mixing distribution**.

---

## 8. Other prior-art boundaries confirmed

The review also confirms that the following are established and must be credited rather than presented as new:

- generic phase/time estimation under photon-number or energy constraints;
- canonical phase POVMs and phase Fourier moments;
- local/global discrepancies between SLD Fisher information and attainable phase-estimation performance;
- arbitrary-measurement/collective Fisher-information matrix bounds (Holevo, Gill and related work);
- SLD/RLD/Petz monotone quantum information metrics;
- random-unitary probability estimation;
- QFI as a time-translation asymmetry resource;
- compound Poisson models, CPTP data processing, POVM pullback, and Stinespring dilation;
- tail-sum and survival-function identities.

No exact equivalent of the operational tail theorem was located. Priority remains unverified rather than certified.

---

## 9. Scope audit

The strongest theorem requires:

1. a fixed semibounded excitation/mark state;
2. the unknown nonzero temporal Fourier parameters enter through a random event-time/translation probability distribution;
3. independent copies/events conditional on the waveform for the collective/Poisson extension;
4. all later source-to-field and detector processing is parameter independent.

It does not cover arbitrary state-valued waveform synthesis, coherent pump modulation, or correlated source processes whose parameter enters collectively rather than through independent random event times.

WP14 supplies an explicit reason this boundary is necessary.

---

## 10. Publication-level hierarchy after the audit

The clean hierarchy is now:

### Primary operational theorem — WP20/WP22/WP23

`R(nu)<=P(Omega>=nu)`

and

`int_R R(nu)dnu<=2Ebar^+/hbar`,

with pointwise inverse

`Ebar^+>=h f R(2pi f)`.

This is sharp and directly source-to-record operational.

### Discrete refinement

`R_N(k)<=min(D_k,U_k)<=T_k`.

### Equality family

Geometric energy sectors / exponential continuum spectrum with canonical phase/time measurement.

### Secondary quantum envelope — WP10/WP12/WP15

The separately optimized SLD-QFI mode formula and `pi E/hbar` area law remain mathematically correct but should be presented as an **incompatible modewise quantum envelope**, not as the main physically attainable broadband theorem.

### Boundary theorem — WP14

Baseline energy cannot bound arbitrary coherent waveform state engineering.

---

## 11. Manuscript gate assessment

The scientific stack is now substantially more coherent than it was at WP15.

The former three major gates have been addressed:

- **operational attainability:** resolved by the direct arbitrary-collective theorem and equality family;
- **continuum rigor:** addressed by WP22;
- **independent event-to-bosonic-field mapping:** addressed by WP23.

The remaining external-risk gate is **priority**, especially in old number-phase and group-distribution statistical literature.

Because exact priority can never be established by finite search, the appropriate publication standard is now:

1. perform one final focused historical search;
2. use conservative novelty wording that explicitly cites weighted-twirl/mode-asymmetry predecessors;
3. draft the theorem manuscript around the operational survival law rather than the `pi` QFI coefficient;
4. continue prior-art checking during manuscript preparation.

There is no longer a scientific reason to postpone manuscript formation solely because of measurement incompatibility, continuum regularity, or bosonic-field embedding.

---

## 12. Decision

**Integrated hostile review: PASS, with the support-gap repair and narrowed prior-art positioning above.**

The project has reached a reasonable manuscript-formation threshold, conditional on conservative priority language.

Recommended next action:

> synchronize all landing documents through WP24, mirror the checkpoint to `main`, then create a standalone manuscript architecture centered on the sharp operational survival-function resource theorem.