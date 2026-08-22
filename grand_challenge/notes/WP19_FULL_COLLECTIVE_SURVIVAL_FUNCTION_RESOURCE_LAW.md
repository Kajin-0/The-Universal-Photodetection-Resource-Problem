# WP19 — Full collective survival-function resource law

**Date:** 2026-08-21

## Status

**Major theorem strengthening. The multimode collective-measurement gate is closed for the independent random-time excitation model.**

WP17 proved a sharp operational mode budget for one fixed POVM and adaptive/separable event measurements. WP18 showed by an exact mixed-qubit Holevo calculation that the first collective-measurement hostile test does not violate the resource coefficient.

WP19 removes the remaining collective loophole.

For a periodic random-time encoded excitation with nonnegative energy-sector probabilities `q_n`, define the upper-tail mass

`T_k=sum_{m>=k}q_m`.

For **any joint POVM on any finite number `N` of independently encoded copies**, let `F_N^(k)` be the `2 x 2` classical Fisher block for the cosine/sine amplitudes of temporal mode `k`, evaluated at the uniform random-time baseline. Then

`boxed: Tr F_N^(k) <= N T_k`.

Therefore the source-normalized two-quadrature trace retention

`R_N(k):=Tr F_N^(k)/N`

obeys the pointwise tail law

`boxed: R_N(k) <= T_k`.

Summing over all positive modes,

`boxed: sum_{k>=1}R_N(k) <= nbar`,

because

`sum_{k>=1}T_k=sum_m m q_m=nbar`.

This holds for arbitrary entangled collective measurements across the `N` copies. Hence coherent detector memory across independently encoded event excitations does not evade the operational resource budget.

The controlled continuum limit gives the stronger pointwise **survival-function law**

`boxed: R(nu) <= P(Omega>=nu)`, `nu>0`,

where `Omega>=0` is the excitation-frequency random variable of the fixed quantum excitation.

Integrating the survival function,

`boxed: int_0^infinity R(nu)dnu <= E[Omega]=omega_bar`,

and with even extension,

`boxed: int_R R(nu)dnu <=2Ebar^+/hbar`.

A full two-quadrature retention `q0` at modulation frequency `nu` requires

`boxed: Ebar^+ >= hbar nu q0`.

For a guaranteed ordinary-frequency band `|f|<=B`, this gives

`boxed: Ebar^+ >= h B q0`.

The coefficient and the pointwise tail law are sharp. An infinite geometric sector distribution with the canonical phase POVM saturates every discrete mode simultaneously; its continuum limit is the exponential positive-frequency / Cauchy timestamp equality family of WP06/WP07.

This is now the strongest **operational** random-time resource theorem in the program. WP12/WP15's `pi E/hbar` result remains a separately optimized modewise QFI envelope, but no single physical detector—even one making arbitrary collective entangled measurements across independent events—can jointly realize that larger integrated coefficient.

---

## 1. Periodic one-copy random-time model

Use the WP10 pure-state sector decomposition

`|psi>=sum_n sqrt(q_n)|phi_n>`,

with orthonormal participating vectors `|phi_n>` in total-energy sectors

`H=hbar omega0 sum_n n P_n`.

At the uniform random-time baseline,

`rho0=sum_n q_n |phi_n><phi_n|`.

For mode `k>=1`, define the raising operator

`A_k=sum_{n>=0} sqrt(q_nq_{n+k}) |phi_{n+k}><phi_n|`.

With a consistent sine convention,

`D_c^(k)=(A_k+A_k^dagger)/2`,

`D_s^(k)=(A_k^dagger-A_k)/(2i)`.

The latent classical source-label Fisher block is

`F_in^(k)=(1/2)I_2`.

---

## 2. Holevo lower bound for one mode

Consider only the two real parameters `(epsilon_c,epsilon_s)` of mode `k`, with all other modes fixed at zero.

Let `X_c,X_s` be any pair of Hermitian estimator operators satisfying the Holevo local-unbiasedness constraints for this two-parameter quantum statistical model.

Define

`X=X_c+iX_s`.

The unbiasedness conditions imply the complex constraint

`boxed: Tr[A_k X]=2`

(up to complex conjugation if the opposite sine convention is chosen; the modulus used below is unchanged).

For unit weight matrix, the two-parameter Holevo objective is

`h(X_c,X_s)`

`=Tr[rho0(X_c^2+X_s^2)]`

` +2|Im Tr[rho0 X_cX_s]|`.

But

`Tr[rho0 X^dagger X]`

and

`Tr[rho0 XX^dagger]`

are exactly the two values obtained by adding/subtracting the commutator term. Hence

`boxed: h=max{Tr[rho0 X^dagger X], Tr[rho0 XX^dagger]}`.

Now write matrix elements in the participating energy basis. The complex unbiasedness constraint is

`2=sum_n sqrt(q_nq_{n+k}) X_{n,n+k}`

up to conjugation.

By Cauchy–Schwarz,

`4`

`<= [sum_n q_n |X_{n,n+k}|^2]`

`   [sum_n q_{n+k}]`.

The first bracket is a subset of

`Tr[rho0 XX^dagger]`.

The second bracket is the sector tail

`T_k=sum_{m>=k}q_m`.

Therefore

`Tr[rho0 XX^dagger] >=4/T_k`.

Since the Holevo objective is the maximum of the two positive norms,

`boxed: C_H^(k)(I_2) >=4/T_k`.

If `T_k=0`, the mode derivative vanishes and the operational Fisher block is zero, so the statement is understood trivially.

A symmetric argument using the other norm also gives a lower bound in terms of the total lower-sector mass participating in the gap, but the upper-tail bound is the one tied directly to semibounded energy.

---

## 3. From the Holevo bound to arbitrary finite-copy Fisher information

Let an arbitrary collective POVM `M_N` act jointly on `N` independently encoded copies. It may entangle all copies during measurement and may use arbitrary parameter-independent apparatus ancillas/reference states.

Let its classical mode-`k` Fisher block be

`F_N^(k)`.

We need a bound on its **trace**, not merely on a symmetric estimator chosen in advance.

### Phase symmetrization

Construct a new allowed measurement as follows:

1. draw a known time shift `s` uniformly over the source period;
2. apply the common unitary `U_s` to all `N` copies;
3. perform `M_N`;
4. retain both `s` and the measurement outcome.

At the uniform random-time baseline, the two real mode-`k` parameters rotate by an ordinary `2 x 2` rotation through angle `k omega0 s`.

Therefore the Fisher block conditional on `s` is the rotated matrix

`R_s^T F_N^(k) R_s`.

Averaging over the known random shift isotropizes the block while preserving its trace:

`boxed: F_tilde_N^(k)=[Tr F_N^(k)/2] I_2`.

### Repeated-block contradiction argument

Repeat this `N`-copy collective measurement independently over a large number `L` of blocks. The resulting classical experiment is regular, and standard classical asymptotic efficiency yields an estimator approaching covariance

`[L F_tilde_N^(k)]^{-1}`.

Let

`t_N=Tr F_N^(k)/N`.

Then

`F_tilde_N^(k)=N t_N I_2/2`.

The asymptotic scaled sum of variances per physical copy produced by this repeated strategy is

`N L * Tr[(L F_tilde_N^(k))^{-1}]`

`=4/t_N`.

But the Holevo Cramer–Rao bound is the asymptotic collective quantum lower bound for the one-copy i.i.d. model, so every such strategy must satisfy

`4/t_N >= C_H^(k)(I_2)`.

Using the tail lower bound from the previous section,

`4/t_N >=4/T_k`.

Hence

`boxed: t_N<=T_k`,

or equivalently

`boxed: Tr F_N^(k)<=N T_k`.

This holds for every finite block size `N`. If any finite collective POVM violated it, repeating that block would asymptotically violate the Holevo bound.

---

## 4. Full multimode collective sum rule

The previous inequality is valid for each positive harmonic `k` for the **same arbitrary collective detector**.

Therefore

`sum_{k>=1} [Tr F_N^(k)/N]`

`<=sum_{k>=1}T_k`.

Use the elementary tail-sum identity for a nonnegative integer random variable:

`sum_{k>=1}T_k`

`=sum_{k>=1}sum_{m>=k}q_m`

`=sum_m m q_m`

`=nbar`.

Thus

`boxed: (1/N)sum_{k>=1}Tr F_N^(k)<=nbar`.

With an even negative-frequency copy,

`boxed: (1/N)sum_{k!=0}R_N(k)<=2nbar`.

This is the full arbitrary-collective extension of WP17's fixed/separable theorem.

---

## 5. Mixed excitations

Let the physical one-event excitation `sigma` be mixed with sector probabilities

`q_n=Tr[P_n sigma]`.

Choose a purification with the time translation acting only on the physical system. The purified pure state has the same sector weights `q_n` and therefore obeys the WP19 collective bound.

Any collective measurement on the physical mixed copies corresponds to a restricted collective POVM on the purified copies. Giving the detector access to the purifier could only enlarge its measurement set.

Hence the same tail and sum bounds hold for arbitrary mixed excitations.

---

## 6. Independent Poisson event streams and arbitrary coherent detector memory

For `N` independent quantum-marked events, the bound is

`Tr F_N^(k)<=N T_k`.

For a Poisson number of events with parameter-independent mean `mu`, reveal the event-number sector as side information. This can only increase accessible Fisher information. Conditional on `N`, the collective bound applies; averaging gives

`Tr F_Poisson^(k)<=mu T_k`.

The latent Poisson source Fisher block has trace `mu`. Therefore the **source-normalized** collective retention remains

`boxed: R_Poisson(k)<=T_k`.

Any parameter-independent source-to-field mapping, bosonic symmetrization/overlap, propagation, coherent detector memory, joint detector channel, and final measurement are downstream quantum operations. Their final record is equivalent to some POVM on the upstream event state and cannot evade the bound.

Thus, within WP13's independent quantum-marked Poisson source model, WP19 covers arbitrary coherent collective detector memory rather than only separable event measurements.

---

## 7. Controlled continuum survival-function law

Use the periodic approximation of WP12 with frequency spacing `delta` and bin probabilities `q_n^(delta)` approaching a positive-frequency density `q(omega)`.

For `k delta -> nu>0`, the discrete tail satisfies

`T_k^(delta)=sum_{m>=k}q_m^(delta)`

`-> int_nu^infinity q(omega)domega`.

Define the excitation-frequency survival function

`S_q(nu)=P(Omega>=nu)`

`=int_nu^infinity q(omega)domega`.

For any controlled sequence of physical detectors/collective measurements whose source-normalized mode-trace retention converges to `R(nu)`, the discrete bound gives

`boxed: R(nu)<=S_q(nu)`

at continuity points of the limiting survival function, with the usual limsup formulation in general.

This is strictly stronger than an integrated area law.

---

## 8. Sharp continuum area and pointwise energy law

Integrate the survival bound. For any nonnegative random variable,

`int_0^infinity P(Omega>=nu)dnu=E[Omega]=omega_bar`.

Therefore

`boxed: int_0^infinity R(nu)dnu<=omega_bar`.

With even extension,

`boxed: int_R R(nu)dnu<=2omega_bar`

`boxed: int_R R(nu)dnu<=2Ebar^+/hbar`.

### Single-frequency inverse law

The survival function also obeys Markov's elementary tail-moment inequality

`omega_bar>=nu P(Omega>=nu)`.

Since `R(nu)<=P(Omega>=nu)`, any full two-quadrature operational retention `R(nu)>=q0` implies

`boxed: Ebar^+>=hbar nu q0`.

Thus at ordinary modulation frequency `f=nu/(2pi)`,

`boxed: Ebar^+>=h f q0`.

This is stronger in interpretation than deriving the same coefficient only from an integrated flat-band argument: the Planck-scale cost already appears **pointwise at the top modulation frequency**.

For a guaranteed band `|f|<=B`, take `f=B` and obtain

`boxed: Ebar^+>=hBq0`.

---

## 9. Exact discrete equality family — geometric sectors

Take the infinite geometric energy distribution

`q_n=(1-r)r^n`, `0<r<1`.

Then

`nbar=r/(1-r)`

and the sector tail is

`T_k=r^k`.

Use the canonical phase POVM

`M(dtheta)=(dtheta/2pi)|theta><theta|`,

`|theta>=sum_{n>=0}exp(i n theta)|n>`

in the standard generalized-POVM sense.

At the uniform random-time baseline the outcome phase is uniform. For mode `k`, the complex score amplitude is proportional to

`sum_n sqrt(q_nq_{n+k}) exp(i k theta)`.

But

`sqrt(q_nq_{n+k})=r^(k/2)q_n`,

so

`sum_n sqrt(q_nq_{n+k})=r^(k/2)`.

Hence

`F_cc^(k)=F_ss^(k)=r^k/2`,

and

`boxed: R(k)=Tr F^(k)=r^k=T_k`.

The **same one-copy canonical phase measurement** therefore saturates the collective tail bound for every mode simultaneously.

Summing,

`sum_{k>=1}R(k)=sum_{k>=1}r^k=r/(1-r)=nbar`.

Thus the collective sum constant `1` is exactly attainable, not merely a supremum.

Collective measurement cannot improve this family at any mode because the single-copy POVM already reaches the universal tail ceiling pointwise.

---

## 10. Continuum equality family and recovery of the Cauchy timestamp

Take a continuum scaling

`r=exp(-beta delta)`

as the periodic spacing `delta->0`.

The geometric sector law converges to the exponential excitation-frequency density

`q(omega)=beta exp(-beta omega)`, `omega>=0`,

with

`omega_bar=1/beta`.

The discrete exact retention

`R_delta(k)=r^k`

converges for `k delta->nu` to

`boxed: R(nu)=exp(-beta nu)`.

The survival function of the exponential density is exactly the same:

`S_q(nu)=exp(-beta nu)`.

Thus WP19's continuum survival bound is saturated **pointwise at every modulation frequency**.

Writing

`beta=2a`,

the corresponding positive-frequency amplitude is exponential and the canonical covariant time POVM gives the Cauchy timestamp density

`f_a(t)=a/[pi(t^2+a^2)]`.

Its Fisher transfer is

`G(nu)=exp(-2a|nu|)=exp(-beta|nu|)`.

Therefore WP06/WP07's Cauchy equality family is exactly the continuum limit of WP19's geometric all-mode equality family.

This unifies the formerly separate covariant-timestamp sharpness construction with the arbitrary-detector random-time resource theorem.

---

## 11. Relation to the WP12/WP15 `pi` QFI envelope

WP12/WP15 remain correct:

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

But `G_Q(nu)` is obtained by optimizing the SLD measurement **separately for each mode/quadrature**.

WP19 instead constrains the Fisher spectrum of one physical parameter-independent detector/measurement, even if that detector performs arbitrary entangled collective measurements across many independent event excitations.

The sharp operational law is

`int_R R(nu)dnu<=2Ebar^+/hbar`.

Thus the factor

`pi/2`

between the QFI and operational area coefficients is now rigorously identified as a non-joint-attainability/incompatibility gap for the independent random-time source class.

It is not a realizable broadband detector advantage.

---

## 12. Prior-art boundary

The proof uses established ingredients:

- Holevo Cramer–Rao theory and asymptotic attainability;
- classical Fisher asymptotic efficiency for a repeated fixed measurement;
- group/phase symmetrization of a measurement;
- Cauchy–Schwarz;
- tail-sum and survival-function identities;
- canonical phase/time POVMs.

Generic multiparameter Holevo theory, mixed-qubit collective advantages, canonical phase measurement, and phase-number Fourier analysis are prior art.

Targeted searches have not located the specific theorem

`Tr F_N^(k)/N <= sum_{m>=k}q_m`

for Fourier perturbations of a latent random translation distribution, nor its summed mean-generator form

`sum_k R(k)<=nbar`,

nor the continuum operational survival law

`R(nu)<=P(Omega>=nu)`

as a source-to-record temporal Fisher-information resource theorem.

Priority is **not certified**.

---

## 13. Remaining scientific gates

The principal measurement-theory gate is now closed for the independent random-time excitation class.

Highest-value remaining tasks are:

1. **Hostile proof audit:** independently rederive the Holevo-complex-operator factor-of-two normalization and the finite-block repetition argument.
2. **Priority audit:** search phase-distribution estimation, group-distribution inference, canonical phase, and Holevo literature specifically for the tail/survival theorem.
3. **Source-to-field rigor:** strengthen WP13's independent quantum-marked Poisson-to-bosonic-field construction with explicit channel maps and source assumptions.
4. **Continuum rigor:** state the detector-sequence convergence hypotheses under which the discrete collective tail law passes to `R(nu)<=S_q(nu)` for general finite-first-moment densities.
5. **Manuscript decision:** if these survive, reconsider the publication gate. WP19 is substantially more operational and simpler than the earlier `pi`-QFI endpoint.

## Decision

The Grand Challenge has advanced materially.

For random temporal-distribution encoding of a fixed semibounded-energy excitation, arbitrary parameter-independent detector processing—including coherent collective measurement across independent event excitations—obeys a sharp operational temporal-information resource law controlled by the **survival function of the excitation-energy distribution**.

The mean-energy area and Planck-scale bandwidth laws are immediate corollaries, and the geometric/exponential canonical phase/time family attains the bound exactly.