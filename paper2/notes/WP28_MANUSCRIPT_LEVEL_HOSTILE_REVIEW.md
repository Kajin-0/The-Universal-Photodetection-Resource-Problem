# WP28 — Manuscript-level hostile review and Rev6 science freeze

**Date:** 2026-08-21

**Status:** manuscript-level adversarial review completed. No fatal theorem, normalization, observation-model, or prior-art-positioning defect was found in the core Paper-2 stack. The concrete issues found during the review were repaired through Rev5 and Rev6. The science draft should now be treated as **frozen by default** unless a new concrete defect, external-review objection, or verified priority collision appears.

Current working title:

> **Fisher Spectra and Information Singularities in Photodetectors with Memory**

Current generated science draft: **Rev6**.

---

## 1. Review standard

The manuscript was read adversarially along four independent axes:

1. theorem/proof correctness and hidden regularity assumptions;
2. consistency among the a.e. spectral multiplier `G(omega)`, Palm-cycle retention `G_cyc`, and stationary static retention `G_DC`;
3. prior-art and priority language;
4. numerical/figure claims versus analytically proved statements.

The review also included clean LaTeX builds, log inspection, and rendered-page inspection.

---

# 2. General autonomous-channel theorem

## Result

**Survives hostile review.**

The source Poisson tangent is initially defined on a genuine physical dense class such as `C_c^infty(R)`. DQM under the parameter-independent detector channel gives the conditional output score, and the Fisher form is a positive contraction. Time-translation covariance gives exact commutation with shifts; the classical `L2` multiplier theorem then yields an a.e. bounded spectrum.

### Manuscript repair made in Rev5

Earlier wording could be read as though every arbitrary `L2` function itself were a physical intensity perturbation. Rev5 now states explicitly that the Fisher bilinear form initially defined on `C_c^infty(R)` **extends uniquely and continuously** to `L2(R)`. The multiplier statement is for that extended form.

### Scope retained

The theorem remains for classical Poisson intensity perturbations and parameter-independent autonomous detector channels. It is not a theorem for arbitrary quantum inputs, phase-sensitive optical measurements, or generic Blackwell ordering.

No independent-event kernel, finite detector state, low-flux assumption, or one-output-per-photon structure is required.

---

# 3. Deterministic Type-II spectral escape

## Result

**Survives hostile review and remains the strongest concrete dynamic result.**

At deterministic paralyzable saturation `lambda*tau=1`:

- the stationary homogeneous timestamp experiment has `G_DC=0`;
- the model-specific narrowband/continuous representative satisfies `G_1(omega)>0` for every `omega!=0`;
- `lim_|omega|->infinity G_1(omega)=1/e`;
- at `omega*tau=pi`, the analytic lower bound is `0.51697536...`;
- the exact Volterra calculation gives approximately `0.52814265` after step-size extrapolation.

### Important notation point

The manuscript correctly avoids identifying the universal WP10 `L^infinity` multiplier with a primitive point value at `omega=0`. Static information uses `G_DC`; finite-frequency statements use narrowband limits and the model-specific transition-score representation. Appendix B establishes the continuous extension for the deterministic Type-II model itself.

### Rev5 reproducibility repair

The manuscript previously referred vaguely to an underlying Volterra derivation. Rev5 now prints the actual causal equations for `k_0`, `k_1`, and

`G_1(omega)=e^{-1} int |k_1|^2/k_0`,

and records the `h=0.005`, `h=0.0025`, and Richardson-extrapolated value at `pi`.

The numerical curve remains validation; the theorem's strict positivity and high-frequency limit are analytic.

---

# 4. Arbitrary finite-mean iid recovery theorem

## Result

**Survives hostile review.**

For every iid nonnegative recovery law with only

`0 < m=E[T] < infinity`,

all laws share the classical conventional rate curve

`r(lambda)=lambda exp(-lambda m)`.

WP25 establishes the Palm-cycle stopped-Poisson experiment with finite latent information `lambda/r`, and therefore finite interval FI `I_D<=lambda/r` without requiring a density, finite recovery variance, finite interval variance, or separate finite-FI assumption.

WP26 establishes the stationary-window equality

`G_DC=G_cyc=(r/lambda)I_D`

throughout this finite-mean Type-II class.

At the common count maximum:

`G_DC=0 iff T=m almost surely`.

Every nondegenerate law also has the explicit bounded-Laplace first-order witness based on `exp(-sD)`.

### Heavy-tail boundary check

The stationary boundary does not require finite forward-recurrence mean. The pre-zero active state is a finite marked-Poisson cloud with mean population `lambda*m`, and the censored boundary horizon contributes sublinear source information because `E[Y wedge L]/L -> 0` for proper finite `Y`.

### Rev5 proof repair

The stationary-window appendix now states the explicit data-processing domination

`I_ord(s) <= lambda*s`,

which is the linear bound used in the final split on `Y<=delta L` and `Y>delta L`.

---

# 5. Mean-and-variance resource incompleteness

## Result

**Survives hostile review.**

The two explicit recovery laws have exactly identical mean `1`, variance `1/4`, CV `0.5`, and the same complete conventional rate curve `lambda exp(-lambda)`.

The analytic theorem uses the same observable

`Z=1{D<=2/5}`

for both models. It is constant for law A and therefore has zero FI, while law B has normalized per-time FI

`0.00443520488427...`.

This is enough to prove that mean, variance, and the entire mean saturation curve do not determine the timestamp statistical experiment.

The approximately `8.78%` difference in complete static FI is numerical calibration only and is not needed for the theorem.

---

# 6. Prior-art / novelty audit

## Result

**Positioning is conservative enough after Rev6. Priority is still not certified.**

The paper explicitly credits or disclaims novelty for:

- modulated paralyzable photocounting;
- classical Type-II/random-prolonging-dead-time cycle laws;
- generic dead-time information theory;
- censored counter inference;
- generic renewal/window-censored renewal FI;
- Fisher data processing / conditional-score projection;
- point-process Fisher kernels and Bartlett identities;
- translation-invariant Fourier multipliers;
- generic queue-output identifiability.

Rev6 adds D. J. Daley, *Advances in Applied Probability* **8**, 395–415 (1976), DOI `10.2307/1425911`, and explicitly states that generic identifiability/reconstruction from queue outputs is classical. The manuscript therefore frames the finite-mean Type-II result narrowly as a **Fisher singularity at the common count maximum for the timestamp-only experiment**.

Afanaseva & Mikhailova (1973) remains an inaccessible direct Type-II-lineage historical risk. No priority claim should depend on excluding it.

No verified predecessor has been located for the exact combined statements used as the manuscript's central physical results, but absence of a located predecessor is not proof of priority.

---

# 7. Coherence / significance

The paper is now coherent as one resource-theory story rather than a collection of dead-time calculations:

1. autonomy gives a complete local Fisher spectrum;
2. deterministic Type-II paralysis shows that a scalar saturation maximum can be an isolated **static information zero** without a finite temporal-information cutoff;
3. arbitrary finite-mean random recovery shows that this singularity is uniquely deterministic even though the complete conventional mean curve is unchanged;
4. the exact mean/variance counterexample proves that adding the next obvious scalar recovery resource still does not complete the information description.

The strongest conceptual message is therefore:

> a saturation curve is not an information-transfer law; the complete trajectory channel is the relevant local information object.

This is substantially stronger and broader than merely reporting another dead-time correction formula.

---

# 8. Remaining limitations — not defects

1. classical Poisson/direct-detection source model only;
2. local Fisher information rather than global finite-contrast discrimination or Shannon capacity;
3. autonomous, parameter-independent channel assumption;
4. idealized Type-II recovery class for the concrete theorems;
5. no generic Blackwell-dominance claim;
6. no claim that recovery randomness is beneficial away from the specified common count maximum;
7. priority remains uncertified because some historical literature is inaccessible.

These should remain explicit rather than being hidden in appendices.

---

# 9. Manuscript decision

**Rev6 passes the internal science/manuscript gate.**

No further theorem accumulation is recommended by default.

The next work should be submission preparation / external-style review only:

- inspect the GitHub Actions Rev6 job when accessible;
- add truthful author/affiliation/contact metadata;
- add any journal-required Data Availability / code availability / AI disclosure / funding/conflict statements;
- decide final journal target and format;
- perform one final referee-style review after metadata/package preparation.

Reopen scientific derivations only if that process identifies a concrete flaw.
