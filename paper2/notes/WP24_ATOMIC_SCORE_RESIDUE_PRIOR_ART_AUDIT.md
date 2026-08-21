# WP24 — Prior-art audit for conditional-score atomic residue / atomic timing-path resource

**Status:** targeted novelty audit of WP22/WP23. The audit finds substantial classical prior art for every mathematical ingredient and for the high-frequency shot-noise limit of ordinary point-process spectra, but no located source yet states the specific detector-channel result in terms of the **conditional source score after arbitrary stochastic processing** or interprets its atomic timing paths as a temporal Fisher-information resource. No priority claim is certified.

**Date:** 2026-08-21

---

## 1. Exact candidate under audit

WP22/WP23 should not be audited as if they claim a new Fourier theorem or a new point-process spectrum.

The narrow candidate statement is:

> For a stationary autonomous detector channel driven by a weakly modulated Poisson source, form the **efficient/conditional source score** retained by the complete accessible detector record. If its stationary score-covariance measure has zero-lag atom `a`, then the proportional high-frequency Cesaro average of the complete local Fisher-retention spectrum tends to `a/lambda`. In causal regular selector models, atomic timing paths in the score contribute additively to `a`; diffuse timing-memory paths wash out under the stated finite-measure/mixing assumptions.

The mathematical core is

`Gamma_M = a delta_0 + nu`,

`lambda G(omega)=a+nu_hat(omega)`,

and

`lim_{Omega->infinity} [(b-a)Omega]^{-1} int_{aOmega}^{bOmega}G(omega)domega = a/lambda`.

WP23 further gives the illustrative score-response decomposition

`k(dt)=sum_j c_j delta_{tau_j}(dt)+k_c(t)dt`,

for which, under the idealized stationary white-innovation normalization and diffuse finite-energy remainder,

`lim <G>_high = (r/lambda) sum_j |c_j|^2`.

The novelty question is therefore not whether atoms survive high-frequency Fourier averaging. They obviously do and this is classical. The question is whether this **conditional-score/Fisher-channel interpretation and detector resource statement** has already appeared.

---

## 2. Classical ingredient: score covariance is Fisher information

This is firmly prior art.

### 2.1 Classical Bartlett identities

For a regular likelihood, Fisher information is the covariance of the score. This is the standard second Bartlett identity.

### 2.2 Counting-process likelihood / innovation martingales

Standard multiplicative-intensity theory writes a counting-process score as

`S_theta(t)=int dot(log q_s(theta)) [dN_s-q_s(theta)ds]`.

The expected information is the predictable quadratic variation / martingale-isometry integral

`I_theta(t)=E int q_s(theta)[dot(log q_s(theta))]^2 ds`.

This is standard Aalen / Andersen-Gill / counting-process inference and must not be presented as new.

### 2.3 Function-valued point-process Fisher kernels

Daniel E. Clark, **“A Cramer Rao Bound for Point Processes,”** IEEE Trans. Information Theory 68(4), 2147–2155 (2022), DOI `10.1109/TIT.2022.3140374`, develops functional Cramer-Rao/Fisher-information structure for point processes and random measures.

Daniel E. Clark, **“Bartlett identities for spatial point processes,”** Statistics & Probability Letters 236, 110779 (2026), DOI `10.1016/j.spl.2026.110779`, goes still closer to WP10/WP22. It treats the score as a function, defines the Fisher information kernel as score covariance,

`I_phi(x,y)=E[S_phi(x)S_phi(y)]`,

and explicitly describes non-Poisson departures as off-diagonal/nonlocal structure in that kernel.

Therefore:

- score fields are prior art;
- Fisher kernels/operators are prior art;
- score covariance as Fisher kernel is prior art;
- diagonal versus off-diagonal Fisher-kernel structure is not, by itself, a new idea.

Clark does **not**, in the material inspected, specialize a stationary temporal detector channel to a Fourier multiplier or identify a high-frequency Fisher residue with the zero-lag atom of the **conditional source score after detector processing**.

---

## 3. Classical ingredient: point-process diagonal shot noise and high-frequency spectral plateau

This is also firmly prior art.

For a stationary simple point process of rate `r`, the covariance/Bartlett spectrum contains the diagonal self-event contribution associated with the rate. Under ordinary short-range correlation conditions, the correlation-dependent part decays at high frequency and the spectrum approaches the shot-noise level.

This statement is routine in point-process, spike-train, and photodetection spectral analysis.

Examples located in the audit:

1. Bernard Picinbono, **“Coincidence functions and Bartlett spectra of point processes,”** Communications in Statistics — Simulation and Computation 50 (2021; online 2019), 2581–2597, DOI `10.1080/03610918.2019.1680693`, explicitly treats coincidence functions/Bartlett spectra for time point processes, including photodetection contexts.
2. Modern spike-train reviews state the standard asymptotic formula
   
   `lim_{f->infinity} S(f)=r_0`,
   
   with `r_0` the firing rate.
3. Classical/modern spike-train work also shows refractory/dead-time correlations reshape lower and intermediate frequencies while the very-high-frequency spectrum returns to the shot-noise plateau under ordinary regularity.
4. Bartlett/Hawkes spectral theory represents point-process spectra as a white/self-event component transformed by correlation or feedback structure.

Therefore the statement

> “the high-frequency spectrum of an ordinary point process exposes its diagonal shot-noise term”

is not novel and must never be used as a priority claim for WP22.

---

## 4. Classical ingredient: atoms, Fourier-Stieltjes transforms, Cesaro extraction, Wiener

Everything on the harmonic-analysis side is classical:

- Lebesgue decomposition of finite measures;
- Fourier-Stieltjes transforms;
- a point mass contributes a nondecaying exponential Fourier component;
- proportional-band averaging kills distinct nonzero-delay cross terms;
- dominated convergence extracts the zero-lag atom from a finite measure;
- Wiener's theorem identifies the total squared mass of atoms from Cesaro averages of the squared Fourier transform;
- Rajchman measures have Fourier transforms tending to zero;
- `L1` covariance densities are Rajchman by Riemann-Lebesgue.

WP22/WP23 must cite these as standard machinery, not as discoveries.

---

## 5. Classical ingredient: frequency-domain Fisher information / derivative systems

System-identification and experimental-design literature routinely expresses Fisher information as frequency integrals of transfer-function derivatives and input spectra.

Examples include:

- R. J. Ober, **“The Fisher information matrix for linear systems,”** Systems & Control Letters 47 (2002), 221–226, DOI `10.1016/S0167-6911(02)00190-1`;
- extensive prediction-error/system-identification literature in which the information matrix is an integral of parameter-sensitivity transfer functions against stationary input/output spectra;
- frequency-domain maximum-likelihood identification literature going back at least to the 1970s.

Thus the generic algebra

`F ~ int |H_sensitivity(omega)|^2 Phi_input(omega)domega`

and the fact that deterministic delay factors have unit modulus are standard system-identification facts.

WP23's toy calculation

`|1+c exp(-i omega tau)|^2`

is therefore not novel mathematics. Its role is diagnostic: it proves that **causality alone cannot replace the non-atomic-memory assumption** in the detector theorem.

---

## 6. Neural timing/information literature is close in subject but not an exact collision

Spike-train/neural coding literature has long studied:

- information in precise spike timing versus firing rate;
- frequency-dependent stimulus-response transfer;
- spike-train power spectra under refractory dynamics;
- Fisher information carried by spike timing;
- weak-signal information rates for stochastic spike generators.

This prevents any broad claim of “first frequency-resolved information treatment of a point-process detector” or “first information-theoretic analysis of refractory timing.”

However, the sources found in this audit did not formulate the exact WP22 construction:

1. start from the **incident Poisson waveform score**;
2. condition that score on the complete output of an arbitrary detector channel;
3. form the covariance measure of that efficient/conditional score;
4. identify its zero-lag singular mass as the robust high-frequency Cesaro Fisher-retention residue;
5. interpret exact delayed score pathways as additional atomic timing resources.

---

## 7. Weak-signal stationary-channel information theory is also close

Pinsker/Prelov/van der Meulen and related weak-signal stationary-channel literature develops information-rate expansions governed by Fisher information for channels with memory. Kostal and others use weak-signal Fisher approximations for neural/information channels.

This makes it unsafe to claim that “weak-signal information in a stationary channel with memory is controlled by Fisher information” is new.

The apparent distinction of WP10/WP22 is again the specific **waveform Fisher operator of a Poisson event source passed through an arbitrary autonomous photodetector channel**, plus the atomic timing-resource consequences.

---

## 8. Closest conceptual collision: Clark 2026 + classical point-process spectrum

The strongest adversarial reconstruction of a predecessor is not one paper but a composition of two classical/modern facts:

1. Clark 2026: a point-process functional score has a Fisher kernel equal to its covariance kernel;
2. classical Bartlett spectral theory: a stationary covariance kernel/measure diagonalizes spectrally, with diagonal atoms producing nondecaying spectral components and high-frequency shot-noise plateaus under regularity.

Combining these facts makes the mathematics behind WP22 fairly natural.

This substantially lowers the defensibility of a claim such as:

> “We discover that a zero-lag score covariance atom produces a high-frequency information plateau.”

That phrasing is too close to an immediate synthesis of known score-covariance and spectral-measure facts.

A safer contribution claim, if a manuscript is written, is:

> The autonomous photodetection problem admits a complete local Fisher transfer spectrum even with arbitrary hidden memory. Within that detector-channel formulation, the singular/atomic component of the **conditional incident-source score** provides a physically interpretable high-frequency timing resource; solved dead-time models and generalized Type-II recovery then expose nontrivial static/dynamic information phenomena that scalar timing or saturation summaries miss.

In other words, WP22/WP23 are likely **structural synthesis/supporting theory**, not a standalone mathematical breakthrough.

---

## 9. What the search did NOT find

No located source explicitly states all of the following together:

- arbitrary parameter-independent stochastic detector channel from complete incident Poisson trajectory to complete accessible output;
- output score as conditional incident waveform score;
- autonomy forcing a scalar temporal Fisher multiplier;
- covariance-measure Lebesgue/atomic decomposition of that **conditional incident score**;
- high-frequency Cesaro Fisher retention equal to its zero-lag atomic mass divided by incident rate;
- exact delayed conditional-score paths contributing additively to that atomic residue;
- use of this structure as a photodetector resource statement independent of dead-time/recovery constants.

This absence is **not priority certification**. The individual steps are sufficiently standard that novelty must be claimed at the level of the integrated detector theory and nontrivial consequences, not at the level of the Fourier lemma.

---

## 10. Revised novelty status of WP22/WP23

### Not a lead standalone novelty theorem

WP22/WP23 should **not** be sold as a new general theorem of stationary random measures or point-process statistics. The underlying spectral atom result is classical, and Fisher kernels as score covariance are established.

### Valuable as a general structural theorem/corollary inside Paper 2

They remain highly useful because they:

1. identify the correct invariant after arbitrary detector processing as the **conditional-source-score covariance atom**, not raw output shot noise;
2. prevent the false universal statement `Y<=N => residue r/lambda`;
3. show why a perfectly sharp delayed memory path survives high-frequency averaging while diffuse memory need not;
4. connect Paper 1's atomic/diffuse timing-resource hierarchy to arbitrary-memory channels;
5. provide the right language for interpreting WP07's `1/e` residue without pretending that a dead-time constant itself is the resource.

### Current rating

- mathematical correctness under stated assumptions: **strong**;
- conceptual usefulness: **high**;
- standalone mathematical novelty: **low to moderate at best**;
- detector-theory synthesis novelty: **plausible but uncertified**;
- priority language: **disabled**.

---

## 11. Recommended manuscript role

If Paper 2 proceeds, WP22/WP23 should be used as a **bridge theorem** between the abstract WP10 Fisher spectrum and the concrete WP07/WP18 Type-II phenomena.

Suggested architecture:

1. WP10/WP17: autonomous detector channels possess a complete local Fisher spectrum.
2. WP22: in a covariance-measure regularity class, the high-frequency Cesaro residue is the zero-lag atom of the conditional-source-score covariance.
3. WP23: that atom represents total atomic timing-path energy; visible exact timestamps are one path, exact delayed score memory can add others, while diffuse memory is spectrally washed out under stronger regularity.
4. WP07: deterministic Type-II paralysis gives a concrete dramatic example—zero static information but positive information at every nonzero frequency and residue `1/e`.
5. WP18: random recovery breaks the deterministic static Fisher singularity.
6. WP19: even mean plus variance plus the full mean saturation curve remain information-incomplete.

This makes WP22/WP23 explanatory infrastructure rather than the paper's sole novelty pillar.

---

## 12. Next gate after this audit

The novelty audit is sufficiently complete for strategy. Do not keep searching generic score/Bartlett-spectrum literature indefinitely unless a directly matching citation emerges.

The next higher-value task is **proof hardening of WP18 across atomic and heavy-tailed recovery laws**:

- separate the broad bounded-statistic sensitivity/identifiability statement from the stronger finite positive Fisher-rate statement;
- determine minimum moment/DQM conditions for `G_DC=(r/lambda)I_D`;
- handle finite-window boundary/censoring rigorously;
- determine what remains true when `E[T]<infinity` but `Var(T)=infinity` or interval FI diverges;
- ensure the deterministic-recovery iff theorem is stated at exactly the strongest justified level.

This gate is more likely to improve Paper 2 materially than further generic novelty searches around WP22/WP23.
