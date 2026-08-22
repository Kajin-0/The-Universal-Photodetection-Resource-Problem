# WP17 — Sharp single-measurement operational random-time mode budget

**Date:** 2026-08-21

## Status

**New theorem / operational resolution for single-copy and separable-event readout.**

WP10–WP15 bound the SLD quantum Fisher information of each random-time Fourier mode after optimizing the measurement separately for that mode. WP11 already showed that the cosine/sine SLDs are generally incompatible, leaving open whether the integrated QFI coefficient can be realized by one physical detector/measurement.

WP17 gives a sharp answer for **one fixed POVM on each encoded excitation**, and therefore for arbitrary adaptive/separable measurement of independent event excitations:

`boxed: sum_{k>=1} Tr F_M^(k) <= nbar`.

Here `F_M^(k)` is the `2 x 2` classical Fisher matrix of the cosine/sine coefficients of random-time mode `k` obtained from one fixed arbitrary POVM `M`, and

`nbar=sum_n n q_n`.

The latent classical source-label Fisher block is `(1/2)I_2`, whose trace is `1`; therefore `Tr F_M^(k)` is exactly the total source-normalized Fisher retention of the two real quadratures of mode `k`.

The constant `1` is sharp as a supremum.

The controlled continuum consequence is

`boxed: int_0^infinity R_M(nu)dnu <= omega_bar`,

or, with even extension,

`boxed: int_R R_M(nu)dnu <= 2 Ebar^+/hbar`.

A detector that retains at least fraction `q0` of **both quadratures** throughout ordinary-frequency band `|f|<=B` must satisfy

`boxed: Ebar^+ >= h B q0`.

This coefficient is sharp and is attained in the continuum by the Cauchy/exponential covariant timestamp family already identified in WP06/WP07.

Thus, within the single-copy/separable-event random-time source class, the sharp **operational** integrated-area constant is `2`, not the separately optimized QFI coefficient `pi`.

A remaining caveat is essential: WP17 does **not yet prove** the same bound for arbitrary collective entangled measurements across multiple copies of the mixed twirled state. Standard Gill–Massar theory itself distinguishes separable from collective measurements for mixed states. That becomes the next operational gate.

---

## 1. Periodic source model

Use the WP10 periodic model.

Let

`H=hbar*omega0*N`,

with nonnegative integer energy sectors and pure excitation

`|psi>=sum_{n>=0}|psi_n>`.

Define

`q_n=||psi_n||^2`,

and, for `q_n>0`, normalized orthogonal sector vectors

`|phi_n>=|psi_n>/sqrt(q_n)`.

The uniformly randomized baseline state is

`rho0=sum_n q_n |phi_n><phi_n|`.

For mode `k>=1`, the cosine and sine derivatives at zero modulation are

`D_c^(k)=(1/2) sum_n sqrt(q_n q_{n+k})`

`          * (|phi_{n+k}><phi_n|+|phi_n><phi_{n+k}|)`,

and

`D_s^(k)=(1/(2i)) sum_n sqrt(q_n q_{n+k})`

`          * (|phi_n><phi_{n+k}|-|phi_{n+k}><phi_n|)`.

The latent source-label Fisher block is

`F_in^(k)=(1/2)I_2`.

---

## 2. Arbitrary fixed POVM and Radon–Nikodym matrix

Let `M(dy)` be an arbitrary POVM, including any effective POVM obtained after appending a parameter-independent apparatus/reference state and applying arbitrary parameter-independent quantum processing before final measurement.

Let the baseline outcome law be

`P0(dy)=Tr[rho0 M(dy)]`.

For indices with positive `q_n`, define the complex measures

`mu_nm(dy)=<phi_n|M(dy)|phi_m>`.

Each `mu_nm` is absolutely continuous with respect to `P0` on the participating support. Write

`m_nm(y)=d mu_nm/dP0`.

POVM positivity implies pointwise positive-semidefiniteness of the matrix `[m_nm(y)]` for `P0`-almost every `y`. Therefore

`boxed: |m_nm(y)|^2 <= m_nn(y)m_mm(y)`.

The baseline definition gives

`boxed: sum_n q_n m_nn(y)=1`

for `P0`-almost every `y`.

POVM normalization also gives

`int m_nn(y) P0(dy)=1`.

---

## 3. Complex mode score

Define for mode `k`

`z_k(y)=sum_{n>=0} sqrt(q_nq_{n+k}) m_{n+k,n}(y)`.

The two classical score components are

`s_c^(k)(y)=Re z_k(y)`,

`s_s^(k)(y)=Im z_k(y)`

up to an irrelevant sign convention for the sine quadrature.

Hence the trace of the classical Fisher block is exactly

`boxed: Tr F_M^(k)=int |z_k(y)|^2 P0(dy)`.

This identity is the key operational quantity. It combines the two incompatible quadratures before any separate mode-by-mode measurement optimization.

---

## 4. Pointwise positivity/Cauchy bound

By POVM positivity,

`|z_k|`

`<=sum_n sqrt(q_n m_nn) sqrt(q_{n+k}m_{n+k,n+k})`.

Cauchy–Schwarz gives

`|z_k|^2`

`<= [sum_n q_n m_nn]`

`   [sum_n q_{n+k}m_{n+k,n+k}]`.

The first bracket is at most the full baseline normalization and equals `1` if all participating indices are included. Thus

`boxed: |z_k(y)|^2 <= sum_{m>=k}q_m m_mm(y)`.

Integrating against `P0` and using POVM normalization,

`boxed: Tr F_M^(k) <= sum_{m>=k} q_m`.

This is already a useful per-mode operational tail bound. It depends only on the population above the energy gap required by mode `k`.

---

## 5. Sharp positive-mode sum rule

Sum the previous inequality over all positive modes and use Tonelli:

`sum_{k>=1}Tr F_M^(k)`

`<=sum_{k>=1}sum_{m>=k}q_m`

`=sum_m m q_m`

`=nbar`.

Therefore

`boxed: sum_{k>=1}Tr F_M^(k) <= nbar`.

If the mode-retention trace is given an even negative-frequency copy,

`boxed: sum_{k!=0}R_M(k) <=2 nbar`,

where

`R_M(k):=Tr F_M^(|k|)`.

### Comparison with WP10 QFI

WP10 gives

`Tr F_Q^(k)=G_Q(k)`

and

`sum_{k>=1}G_Q(k)<=2 nbar`.

Hence the factor-of-two gap has a precise operational interpretation:

- `2 nbar` is a sum of **separately optimized SLD-QFI mode bounds**;
- `nbar` is the sharp total classical Fisher budget for **one fixed measurement** across all cosine/sine mode parameters.

The QFI area is therefore not generally jointly accessible by one single-copy detector.

---

## 6. Mixed states and parameter-independent apparatus resources

Let the physical excitation `sigma` be mixed with energy-sector probabilities

`q_n=Tr[P_n sigma]`.

Choose a purification `|Psi>` with the time translation acting on the physical system only. The purification has the same sector probabilities `q_n`.

Any physical POVM on the mixed state, including arbitrary parameter-independent apparatus ancillas and preprocessing, can be represented as an effective POVM on the purified model that acts trivially on the inaccessible purifier.

Therefore the pure-state proof applies unchanged and yields

`boxed: sum_{k>=1}Tr F_M^(k) <= nbar`

for arbitrary mixed excitations under one fixed physical POVM.

No covariance or reference-free condition is required for the POVM.

---

## 7. Adaptive/separable multi-event extension

Consider `N` independent quantum-marked events, each carrying the same random-time encoded excitation, but restrict the detector to **separable event measurements**: event `j` is measured by a POVM that may depend arbitrarily on all previous classical outcomes but does not perform an entangled collective measurement on multiple unmeasured event systems.

By the classical Fisher-information chain rule, the total Fisher matrix is the sum of the expected conditional Fisher matrices of the successive measurements.

Conditioned on every previous history, the next measurement is simply some fixed POVM on one copy, so the one-copy theorem gives

`sum_{k>=1}Tr F_j^(k | history) <= nbar`.

Averaging and summing over events yields

`boxed: sum_{k>=1}Tr F_N^(k) <= N nbar`.

For a Poisson number of independent events with parameter-independent mean `mu`,

`boxed: sum_{k>=1}Tr F_Poisson^(k) <= mu nbar`.

The latent Poisson source FI also scales by `mu`, so the **source-normalized** per-event retention bound remains the same.

Any later parameter-independent classical memory/coarse graining can only decrease Fisher information.

Thus WP17 covers arbitrary adaptive/separable detection of independent quantum-marked Poisson events, not merely a literal identical POVM repeated each time.

---

## 8. Sharpness in the periodic model

Take the two-sector family

`q_0=1-epsilon`,

`q_1=epsilon`,

with all other populations zero. Then

`nbar=epsilon`.

Use the canonical equatorial phase POVM on the two-sector span,

`M(dtheta)=(dtheta/2pi)|theta><theta|`,

`|theta>=|phi_0>+exp(i theta)|phi_1>`.

The baseline outcome is uniform. Direct calculation gives

`F_cc^(1)=F_ss^(1)=q_0 q_1/2`,

so

`Tr F_M^(1)=q_0q_1=epsilon(1-epsilon)`.

All higher modes vanish. Therefore

`[sum_k Tr F_M^(k)]/nbar =1-epsilon ->1`

as `epsilon->0`.

Hence the constant `1` is sharp as a supremum.

Note that the QFI trace for this mode is `2q_0q_1`, exactly twice the phase-POVM Fisher trace asymptotically. This exhibits the single-copy incompatibility explicitly.

---

## 9. Flat-band inverse law in the periodic model

Suppose one fixed measurement guarantees, for every `k=1,...,K`,

`F_M^(k) >= (q0/2) I_2`

in positive-semidefinite order.

This means that every real phase/quadrature direction of each temporal mode retains at least fraction `q0` of the latent source Fisher information.

Then

`Tr F_M^(k)>=q0`.

Therefore

`K q0 <= sum_{k>=1}Tr F_M^(k) <= nbar`,

so

`boxed: nbar >= K q0`.

With

`f0=1/T`,

`B=Kf0`,

`Ebar^+=h f0 nbar`,

we obtain

`boxed: Ebar^+ >= h B q0`.

This is twice as strong as the periodic bound obtained by summing separately optimized scalar QFIs,

`Ebar^+ >= (h/2)Bq0`.

---

## 10. Controlled continuum operational area law

Use the same periodic approximation as WP12 with energy spacing `delta` and `delta nbar_delta -> omega_bar`.

For each periodic approximation choose one fixed POVM `M_delta` and define

`R_delta(k)=Tr F_{M_delta}^(k)`.

WP17 gives exactly

`delta sum_{k>=1}R_delta(k) <= delta nbar_delta`.

For any controlled continuum sequence for which the mode-retention traces converge in the Riemann-sum sense to a nonnegative continuum function `R_M(nu)`, Fatou/lower-semicontinuity gives

`boxed: int_0^infinity R_M(nu)dnu <= omega_bar`.

With even extension,

`boxed: int_R R_M(nu)dnu <=2 omega_bar`

`boxed: int_R R_M(nu)dnu <=2 Ebar^+/hbar`.

This is the sharp continuum **single-measurement operational area law**.

For a phase-symmetric measurement whose Fisher block is

`F_M(nu)=(G_M(nu)/2)I_2`,

we have `R_M(nu)=G_M(nu)` and therefore

`boxed: int_R G_M(nu)dnu <=2 Ebar^+/hbar`.

More generally no phase symmetry is needed: `R_M` is the trace retention and directly measures the total information available about the two real quadratures.

---

## 11. Continuum sharpness and relation to WP06/WP07

The WP06/WP07 Cauchy/exponential timing family saturates the WP17 continuum coefficient.

Take a positive-frequency pure excitation whose spectral probability density is exponential,

`q(w)=2a exp(-2aw)`, `w>=0`.

Then

`omega_bar=1/(2a)`.

The canonical covariant time POVM gives the Cauchy timing density

`f_a(t)=a/[pi(t^2+a^2)]`,

whose temporal transfer is

`G_M(nu)=exp(-2a|nu|)`.

Therefore

`int_0^infinity G_M(nu)dnu=1/(2a)=omega_bar`,

and

`int_R G_M(nu)dnu=1/a=2omega_bar=2Ebar^+/hbar`.

Thus the operational constant `2` is not merely a bound; it is **exactly attainable** by one physical covariant timestamp measurement.

This produces an important unification:

- WP06/WP07 derived the coefficient `2` from positive-frequency Hardy structure for the covariant timestamp class;
- WP17 derives the same coefficient for **every fixed POVM** in the random-time encoding class by an independent POVM-positivity/Fisher-complementarity argument;
- the covariant timestamp happens to attain the universal fixed-measurement optimum.

---

## 12. Continuum flat-band law

If one continuum measurement satisfies

`F_M(nu) >= (q0/2)I_2`

for all ordinary frequencies `|f|<=B`, `nu=2pi f`, then

`R_M(nu)>=q0` on the positive band `0<nu<=2pi B`.

Hence

`2pi B q0 <= int_0^infinity R_M(nu)dnu <= Ebar^+/hbar`.

Therefore

`boxed: Ebar^+ >= h B q0`.

This coefficient is sharp by the same covariant timestamp equality family in the area sense.

---

## 13. What WP17 does NOT yet prove — collective mixed-state measurements

This boundary is important.

WP13's independent quantum-marked Poisson source can, in principle, feed a detector that stores multiple event excitations coherently and performs an entangled collective measurement across them before producing a classical record.

WP17's separable/adaptive extension does not cover that architecture.

This is not a merely technical distinction. Gill and Massar, *Phys. Rev. A* **61**, 042312 (2000), derive multiparameter information tradeoffs that apply to arbitrary measurements for pure states but only to separable measurements for mixed states; collective measurements on mixed-state ensembles can outperform separable bounds. Later state-estimation work demonstrates persistent asymptotic separable/collective gaps.

The baseline random-time twirl `rho0` is generally mixed even when the pre-twirl excitation is pure. Therefore one must not infer from WP17 alone that an arbitrary coherent multi-event detector obeys the same `nbar` per-event budget.

### Next operational gate

Determine the asymptotic Holevo bound / quantum local asymptotic-normality limit for the full random-time Fourier-mode model, beginning with the two-sector qubit case.

The decisive question is:

> Can collective measurements across many independently twirled excitations exceed the sharp single-copy/separable area coefficient `2E/hbar`, and if so by how much?

If the answer is no, the operational `2E/hbar` theorem may become fully detector-independent for independent event streams. If yes, the collective advantage must be explicitly included in the resource hierarchy.

---

## 14. Prior-art boundary

The ingredients used in the proof are standard:

- POVM positivity and `|m_nm|^2<=m_nn m_mm`;
- Radon–Nikodym disintegration relative to the baseline outcome law;
- Cauchy–Schwarz;
- classical Fisher-information chain rules;
- generic multiparameter incompatibility / Gill–Massar tradeoffs.

Do not claim novelty for generic Fisher complementarity or Gill–Massar theory.

A targeted search has not yet located the specific **energy-weighted random-time mode sum rule**

`sum_{k>=1}Tr F_M^(k)<=nbar`

or the resulting sharp continuum law

`int_R R_M(nu)dnu<=2Ebar^+/hbar`

for arbitrary fixed POVMs applied to random temporal-distribution encodings.

Priority is not certified.

---

## Decision

WP17 materially changes the operational interpretation of the Grand Challenge theorem stack.

The sharp `pi E/hbar` WP12/WP15 QFI-area law remains valid as a modewise quantum envelope, but for one fixed measurement the jointly accessible classical Fisher area obeys the stronger sharp law

`boxed: int_R R_M(nu)dnu <=2 Ebar^+/hbar`.

The factor `pi/2` between these constants is therefore an **incompatibility gap**, not an established realizable detector advantage.

For single-copy and adaptive/separable independent-event detection, Gate 2 is closed.

The next highest-value problem is the collective mixed-state measurement loophole.