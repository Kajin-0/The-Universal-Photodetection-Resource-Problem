# Formal Problem Statement

**Updated:** 2026-08-21

**Active scientific branch:** `agent/temporal-information-resource-law`

## 1. Current scientific objective

Determine what fundamental physical resources constrain the transfer of **temporal Fisher information** from a random optical event-time/source distribution into an accessible record, under physically realizable quantum dynamics and measurement.

The current frontier is no longer the August-20 semiconductor/structured-reservoir work program. That work remains historical background and a library of restricted no-go/repair results. The active Grand Challenge is the quantum temporal-information resource program documented in `grand_challenge/`.

The project is falsification-first. It allows that the final answer may be:

- a sharp universal theorem for a precisely defined source class;
- a hierarchy of restricted theorems with explicit boundaries;
- a no-go theorem showing that an apparently natural resource set is incomplete;
- a resource-completeness statement specifying what additional source/control/reference resources must be counted.

The repository—not chat history—is authoritative.

---

## 2. Active statistical experiment

The strongest current theorem concerns **random temporal-distribution encoding of a fixed semibounded-energy quantum excitation**.

In the periodic model, a latent event time `t` is drawn from

`p_eps(t)=(1/T)[1+eps_c cos(k omega0 t)+eps_s sin(k omega0 t)]`,

and the fixed excitation is translated by

`U_t=exp(-i Ht/hbar)`.

The encoded state is

`rho_eps=int p_eps(t) U_t sigma U_t^dagger dt`.

The unknown parameter is therefore a Fourier coefficient of the **probability law of a random event time**, not a deterministic global time shift and not an arbitrary parameter-dependent source-state synthesis operation.

For a pure excitation with total-energy-sector probabilities `q_n`, the exact scalar-quadrature source-normalized quantum Fisher retention is

`boxed: G_Q(k)=2 sum_n q_n q_{n+k}/(q_n+q_{n+k})`.

The latent classical label Fisher information is `1/2` per cosine/sine quadrature.

For mixed excitations the same population expression is an upper bound by purification and QFI monotonicity.

---

## 3. Current resource theorem

### 3.1 Periodic/discrete law — WP10/WP11

Let

`nbar=sum_n n q_n`.

Then

`boxed: sum_{k>=1}G_Q(k)<=2 nbar`,

`boxed: sum_{k!=0}G_Q(k)<=4 nbar`.

The constants are sharp as suprema.

Because the parameter is encoded before the detector is chosen, every parameter-independent apparatus state, coherent detector memory, joint quantum channel, and final measurement is downstream of this QFI bound.

### 3.2 Continuum law — WP12/WP15

For normalized `q(omega)>=0` on `[0,infinity)` with finite first moment

`omega_bar=int_0^infinity omega q(omega)domega`,

define for `nu>0`

`G_Q(nu)=2 int_0^infinity q(omega)q(omega+nu)/[q(omega)+q(omega+nu)]domega`,

with even extension.

WP15 proves for every finite-first-moment density

`boxed: int_0^infinity G_Q(nu)dnu <= (pi/2)omega_bar`,

and therefore

`boxed: int_R G_Q(nu)dnu <= pi E_bar^+/hbar`,

where

`E_bar^+=hbar omega_bar`.

If

`G_Q(2*pi*f)>=q0` for every `|f|<=B`,

then

`boxed: E_bar^+ >= (2/pi)hBq0`.

The coefficient is sharp as a supremum.

---

## 4. Mathematical provenance correction — WP16

WP15 reduces the positive-side area functional to

`A[q]=<r,Tr>`,

where

`L(s,t)=2st/(s+t)^3`.

The exact operator norm

`||T||=pi/4`

is **not a new mathematical constant**. WP16 identifies it as a direct specialization of established parameterized Hardy–Hilbert integral inequalities with best Beta-function constants.

Using the classical inequality for `(x+y)^(-lambda)` with `lambda=3` and substituting

`f(x)=x r(x)`, `g(y)=y r(y)`,

gives the best constant

`B(3/2,3/2)=pi/8`.

The factor `2` in `L` yields exactly `pi/4`.

Therefore do not claim novelty for the Mellin/operator constant, Hilbert-type inequality, rearrangement machinery, or Beta/Gamma evaluation. The possible contribution is the **quantum statistical reduction and temporal-information interpretation**.

---

## 5. Physical source scope — WP13/WP14

### Included

The periodic theorem depends on sectors of the **total generator of time translations**, not particle labels. It therefore includes:

- fixed-photon-number multiphoton pulses;
- entangled/multimode fixed-number states;
- arbitrary degeneracy within total-energy sectors;
- independent quantum-marked Poisson streams, for which QFI and total excess energy are additive;
- arbitrary subsequent parameter-independent mapping into common bosonic field modes, propagation, overlap, coherent detector memory, and measurement.

### Excluded without additional resource accounting

WP14 constructs a coherent-field counterexample to any extension based only on baseline mean energy. An arbitrarily high-frequency infinitesimal sideband can enter the state tangent at first order while its added energy appears only at second order.

Thus baseline mean energy does **not** bound arbitrary waveform state engineering.

A broader theorem would need to include an explicit encoding/control/action resource, such as energy curvature, tangent energy, or control-Hamiltonian bandwidth/action.

---

## 6. Covariant timestamp subclass

For a reference-free covariant timestamp measurement, WP06–WP08 give the sharper measurement-class-specific law

`boxed: int_R G_timestamp(nu)dnu <=2 E_det^+/hbar`,

with flat-band inverse form

`boxed: E_det^+>=hBq`.

The resource is the detected energy above the participating lower spectral edge, so it is invariant under `H -> H+cI`.

WP08 lifts this through arbitrary downstream parameter-independent classical memory. Finite-energy quantum timing therefore regularizes the exact infinite-frequency `1/e` plateau of Paper 2's ideal deterministic Type-II classical model.

---

## 7. Established no-go boundaries

Do not restart or overclaim the following directions:

1. **Entropy production alone:** does not universally bound information acquisition.
2. **Generic frequency-domain FI/response vs dissipation:** neighboring uncertainty relations already exist.
3. **Generic quantum waveform QFI kernels:** established quantum-metrology territory.
4. **Thermodynamic cost inferred from `G` alone:** underdetermined by the input-output channel.
5. **Mean energy for deterministic global time-shift QFI:** false with sparse high-energy coherence and an external time/phase reference.
6. **Baseline mean energy for arbitrary waveform synthesis:** false by WP14 coherent-sideband construction.
7. **Mathematical novelty of the WP15 `pi/4` operator constant:** preempted by classical Hardy–Hilbert theory.

---

## 8. Novelty discipline

Do not claim novelty for generic:

- SLD QFI or QFI monotonicity;
- harmonic denominators in the SLD metric;
- `U(1)`/energy-gap mode decomposition;
- waveform QFI kernels;
- covariant time POVMs;
- time-translation asymmetry/resource theory;
- Hardy/Gagliardo–Nirenberg inequalities;
- Hardy–Hilbert integral inequalities and their sharp Beta-function constants;
- rearrangement/layer-cake/Mellin/Carleman techniques;
- generic time-energy uncertainty relations.

The current candidate novelty, if priority survives, is the combined theorem stack:

1. Fourier-mode estimation of a latent random time distribution encoded by a fixed excitation;
2. exact source-normalized mode retention `G_Q(k)`;
3. the `2 nbar` all-positive-mode budget;
4. the continuum `pi E/hbar` temporal-information area interpretation;
5. the Planck-scale inverse flat-band law;
6. the detector-independent inheritance through arbitrary downstream parameter-independent quantum processing;
7. the explicit boundary separating random-time encoding from arbitrary waveform synthesis.

Priority is **not certified**.

---

## 9. Current hostile gates

1. **Quantum-priority Gate 1A:** search estimation of Fourier coefficients/mixing weights of `U(1)` random-unitary channels and quantum statistical inference for probability measures on compact groups.
2. **Analysis-provenance Gate 1B:** determine whether the harmonic-mean density inequality appears explicitly in classical analysis, although its sharp operator constant is already known.
3. **Operational attainability Gate 2:** determine whether a single measurement family can approach the integrated `pi` QFI-area coefficient despite multiparameter/multimode SLD incompatibility.
4. **Physical embedding Gate 3:** strengthen the independent quantum-marked Poisson/event model into publication-grade incoherent optical-field language.
5. Only if these gates survive should WP10–WP15 be drafted as a standalone foundational manuscript.

---

## 10. Historical detector-resource program

The August-20 semiconductor/transport/resource-completeness program remains valuable historical work in the repository. It established multiple restricted no-go/repair pairs involving microscopic rates, finite-support pointers, optical capture, Shockley–Ramo geometry, spatial delay, and readout noise.

Those results are **not the current research frontier** and should not be resumed by default. Consult historical notes only when a Grand Challenge proof or physical mapping specifically requires them.

---

## 11. Recovery order

A replacement agent should read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP16_DEEP_PRIORITY_AUDIT_RANDOM_TIME_QFI_AND_HARDY_HILBERT_COLLISION.md`
3. `grand_challenge/notes/WP15_GENERAL_DENSITY_PROOF_OF_SHARP_PI_AREA_INEQUALITY.md`
4. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`
5. `grand_challenge/notes/WP13_SECOND_QUANTIZED_SCOPE_AND_POISSON_EVENT_EMBEDDING.md`
6. `grand_challenge/notes/WP12_SHARP_CONTINUUM_QUANTUM_MODE_AREA_LAW.md`
7. `grand_challenge/notes/WP11_WP10_FACTOR_AUDIT_AND_PRIOR_ART.md`
8. `grand_challenge/notes/WP10_QUANTUM_RANDOM_TIME_MODE_BUDGET.md`
9. `docs/CURRENT_RESEARCH_STATE.md`
10. `ROADMAP.md`

Do not treat older semiconductor work-package numbering as the active checkpoint.