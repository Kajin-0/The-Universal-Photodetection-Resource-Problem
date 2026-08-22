# Formal Problem Statement

**Updated:** 2026-08-22

**Active scientific branch:** `agent/temporal-information-resource-law`

## 1. Scientific objective

Determine what fundamental resources constrain **source-to-record temporal Fisher-information transfer** when a fixed semibounded-energy quantum excitation is emitted at a latent random time whose probability distribution carries the temporal waveform.

The current goal is no longer to guess a thermodynamic sensitivity-bandwidth product. The active theorem class asks a precise statistical question:

> If the unknown temporal waveform is encoded in the probability distribution over time translations of a fixed excitation, how much information about each Fourier component can any physically allowed detector record retain, and how is that retention constrained by the excitation's energy distribution?

Paper 1 Rev11 and Paper 2 Rev7 are frozen. The Grand Challenge checkpoint is WP24.

---

## 2. Periodic random-time experiment

Let

`H=E_* I + hbar omega0 sum_(n>=0) n P_n`

on the participating semibounded total-generator subspace.

A fixed excitation `sigma` is translated by

`U_t=exp(-iHt/hbar)`.

The latent event-time distribution is weakly perturbed in harmonic `k>=1`:

`p_epsilon(t)=(1/T)[1+epsilon_c cos(k omega0 t)+epsilon_s sin(k omega0 t)]`.

The encoded state is

`rho_epsilon=int p_epsilon(t)U_t sigma U_t^dagger dt`.

The unknowns are the two real Fourier coefficients `(epsilon_c,epsilon_s)` of the **mixing distribution**, not a deterministic global phase/time shift.

For a purified excitation define total-energy-sector probabilities

`q_n=Tr(P_n sigma)`.

The uniform-time baseline is block diagonal in energy.

---

## 3. Strongest operational theorem — WP20/WP24

Define

`T_k=sum_(m>=k)q_m`.

For any finite number `N` of independently encoded excitations and **any joint POVM**, including arbitrary entangled collective measurements,

`boxed: Tr F_N^(k)<=N T_k`.

Therefore the full two-quadrature source-normalized operational retention

`R_N(k)=Tr F_N^(k)/N`

obeys

`boxed: R_N(k)<=T_k`.

Summing the tails,

`boxed: sum_(k>=1)R_N(k)<=sum_m m q_m=nbar`.

### Support-sensitive refinement

Let `V_k` be the paired partial shift between occupied sectors separated by `k`. Let

`D_k=Tr(rho0 V_k^dagger V_k)`,

`U_k=Tr(rho0 V_k V_k^dagger)`.

Then

`boxed: R_N(k)<=min(D_k,U_k)<=T_k`.

The coarse tail is the universal semibounded-energy form; the paired-support form is tighter for gapped or upper-bounded spectra.

### Proof mechanism

The complex tangent factorizes as

`A_k=rho0^(1/2)V_k rho0^(1/2)`.

For each POVM outcome, Hilbert--Schmidt Cauchy--Schwarz bounds the cosine/sine Fisher contribution by the probability weight in the range (or, using `A_k^dagger`, the domain) of the shift. For `N` copies, cross-copy terms vanish because every nonzero energy shift has zero expectation in the twirled baseline.

No detector covariance, separability, QFI attainability, Holevo asymptotics, or estimator construction is required.

---

## 4. Continuum survival-function theorem — WP22

Let `mu` be the positive excitation-frequency spectral probability measure on `[0,infinity)` with finite first moment

`omega_bar=int omega mu(domega)`.

Use periodic lower-bin approximants

`q_n^(delta)=mu([n delta,(n+1)delta))`.

Their exact discrete tails are

`T_k^(delta)=mu([k delta,infinity))`.

Every controlled modewise continuum limit satisfies

`boxed: R(nu)<=S_mu(nu):=mu([nu,infinity))`.

Therefore

`boxed: int_0^infinity R(nu)dnu<=omega_bar`,

and two-sided

`boxed: int_R R(nu)dnu<=2Ebar^+/hbar`.

The pointwise first-moment inequality gives

`boxed: Ebar^+>=hbar nu R(nu)`.

At ordinary modulation frequency `f=nu/(2pi)`,

`boxed: Ebar^+>=h f R(2pi f)`.

Thus retention `q0` at frequency `B` requires

`boxed: Ebar^+>=hBq0`.

The formulation allows atomic, absolutely continuous, singular-continuous, and mixed spectral measures.

---

## 5. Sharpness

For geometric sector populations

`q_n=(1-r)r^n`,

the canonical phase POVM gives

`R(k)=r^k=T_k`

for every harmonic simultaneously and saturates

`sum_(k>=1)R(k)=nbar`.

Under `r=exp(-beta delta)`, the continuum excitation measure becomes exponential and

`R(nu)=exp(-beta|nu|)=P(Omega>=|nu|)`.

With `beta=2a`, this is the Cauchy timestamp equality family.

Hence the operational coefficient `2E/hbar` is exact and attainable.

---

## 6. Independent Poisson source to physical bosonic field — WP23

For independent quantum-marked events with parameter-independent Poisson mean `mu`, define the upstream compound event register

`Sigma_epsilon=directsum_N p_mu(N)rho_epsilon^tensor N`.

Revealing event number can only increase Fisher information, so

`Tr F_compound^(k)<=mu T_k`.

Any subsequent physical source/emission/detector process whose dynamics are fixed after the event-time parameter is encoded is a parameter-independent CPTP map `Gamma`.

For any final POVM `M`, the outcome law equals that of the pulled-back POVM

`Gamma^*(M)`

on the upstream event register. Therefore arbitrary common-field formation, bosonic overlap, mode mixing, coherent detector memory, ancillas, loss, and final readout cannot evade

`boxed: R_final(k)<=T_k`

or the continuum survival law.

This is an **independent-event source theorem**, not a consequence of Poisson photocount statistics alone.

---

## 7. Secondary separately optimized QFI envelope

WP10/WP12/WP15 give the modewise SLD-QFI envelope

`G_Q(k)=2 sum_n q_nq_(n+k)/(q_n+q_(n+k))`,

`sum_(k>=1)G_Q(k)<=2nbar`,

and continuum

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

These remain mathematically correct but are not the main operational theorem. They optimize measurements separately mode by mode. WP20 shows that an actual common detector obeys the smaller sharp operational budget.

WP16 identifies the `pi/4` continuum operator norm as established Hardy--Hilbert mathematics.

---

## 8. Mandatory scope boundary — WP14

Baseline mean energy does **not** bound arbitrary parameter-dependent state-valued waveform synthesis.

An infinitesimal coherent sideband can carry first-order high-frequency parameter sensitivity while the added mean energy is second order in the perturbation amplitude.

Therefore the positive theorem requires:

1. a fixed excitation/mark state;
2. temporal information entering through the random translation/event-time probability law;
3. parameter-independent downstream processing.

A broader waveform theorem would need an explicit encoding/control/action resource.

---

## 9. Prior-art boundary — WP21/WP24

The following are established and must not be claimed as new:

- `U(1)` energy-gap/modes-of-asymmetry decomposition;
- weighted random phase/time twirling and Fourier-mode multiplication;
- canonical phase POVMs/Fourier phase moments;
- photon-number/energy-constrained phase estimation;
- arbitrary-measurement Fisher/Holevo/RLD/SLD information bounds;
- random-unitary probability estimation;
- QFI/time-translation asymmetry;
- Hardy--Hilbert/Mellin/rearrangement inequalities;
- compound Poisson, CPTP, Stinespring, and POVM-pullback machinery.

Especially close is Marvian--Spekkens, Phys. Rev. A **90**, 062110 (2014), which proves for weighted `U(1)` twirling

`sigma^(k)=p_(-k)rho^(k)`.

Thus the harmonic encoding mechanism itself is prior art.

The candidate contribution is specifically:

> the arbitrary-measurement Fisher ceiling for local Fourier perturbations of the random-time mixing distribution, its evaluation as a paired population mass / semibounded survival tail, the sharp mean-energy harmonic budget, and the source-to-record photodetection interpretation.

Targeted searches have not located an exact predecessor. **Priority remains unverified, not certified.**

---

## 10. Current publication status

WP24 integrated hostile review: **PASS**, after:

- replacing the Holevo route with the direct finite-copy proof;
- repairing missing-sector support notation;
- making the continuum limit measure-theoretic;
- making the compound-Poisson-to-field map explicit;
- fencing off the weighted-`U(1)` twirling prior art.

The project has reached a reasonable standalone manuscript-formation threshold.

Immediate next step: create a manuscript architecture centered on the operational survival-function theorem while continuing a conservative historical priority audit.

---

## 11. Recovery order

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
3. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
4. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
5. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`
6. `grand_challenge/notes/WP21_TARGETED_PRIORITY_AUDIT_SURVIVAL_FUNCTION_LAW.md`
7. `ROADMAP.md`
8. `docs/CURRENT_RESEARCH_STATE.md`

Do not resume the historical August-20 semiconductor-resource work by default.