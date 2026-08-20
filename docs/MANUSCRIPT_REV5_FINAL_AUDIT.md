# Manuscript Rev5 Final Audit

**Date:** 2026-08-20

## Purpose
Record the final editorial/theorem audit from build-verified Rev4 through WP35-corrected Rev5.

---

## 1. Scientific scope preserved

Rev5 remains restricted to the autonomous/time-translation-invariant, independent-event, one-primary-registration photodetection event channel driven by weak coherent/Poisson direct-detection intensity modulation.

No new material-specific, coherent-pointer, analog-detector, high-flux trajectory, or nonclassical-source theorem was added.

The central formulas are unchanged:

\[
G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm),
\]

\[
\int_{-\infty}^{\infty}G(\omega)d\omega=\pi\mathfrak R_2,
\]

\[
\mathfrak R_2\le\mathfrak H,
\]

and, for flat ordinary-frequency half-band `B` and required absolute average transfer `q`,

\[
\boxed{\mathfrak R_2\ge4Bq,\qquad \mathfrak H\ge4Bq.}
\]

---

## 2. WP35 correction applied

Rev4's generic microscopic sentence bounded the complete mark-conditioned CTMC registration hazard using only the successful first-registration transition intensity. WP35 proves that this is insufficient when registration competes with other exits.

Rev5 replaces it with the conservative finite-state CTMC statement:

\[
q_x=\sum_{y\ne x}W_{yx},
\qquad
q_{\max}=\max_{x\in S_{\rm pre}}q_x,
\]

where `S_pre` is the pre-registration state set.

Provided the accessible mark does not independently record the realized pre-registration holding times,

\[
\boxed{h_D(t\mid M)\le q_{\max}.}
\]

The generic quantum-jump operator-norm sentence is removed from the first manuscript. No quantum-trajectory claim is needed for the stated Poisson event-channel theorem.

WP29 is unchanged because its gateway theorem already uses the gateway's **total first-exit rate** `lambda_1`.

---

## 3. Capture-weighted theorem remains the preferred primitive

The WP35 competing-exit example reinforces rather than weakens the WP32 resource:

\[
P(M=\mathrm{success})=\frac{r}{r+R},
\qquad
\Lambda(M=\mathrm{success})=r+R,
\]
so
\[
P(M=\mathrm{success})\Lambda(M=\mathrm{success})=r.
\]

Thus a large conditional hazard on a rare branch need not produce a large capture-weighted local-hazard cost.

The manuscript correctly keeps

\[
\mathfrak H=\int\Lambda(m)\kappa(dm)
\]

as the sharper rate resource, with a uniform `Lambda` only as a stronger corollary.

---

## 4. Figure integration corrected

Rev4 inserted both theorem figures but did not explicitly reference them in prose.

Rev5 now contains explicit references to:

- `Fig. \ref{fig:resourceHierarchy}` immediately before the hierarchy figure;
- `Fig. \ref{fig:jitterNoGo}` in the fixed-mean/fixed-variance no-go discussion.

The hierarchy graphic is versioned as

`manuscript/figure_resource_hierarchy_rev5.tex`

and its final-layer descriptor is now `microscopic sufficient local-rate resource`, avoiding an unnecessary generic quantum-operator implication.

No third figure was added.

---

## 5. Claim/citation audit

The eight-entry bibliography was checked against the claims actually made in the manuscript.

### TCSPC / IRF literature

The manuscript conservatively credits prior work for:

- fluorescence-lifetime photon requirements;
- information-theoretical TCSPC treatment of IRF convolution/information loss;
- finite-IRF/background Fisher-information analysis;
- IRF/photon-statistics resolving-power analysis.

The manuscript does **not** claim first use of information theory, Fisher information, IRFs, timing jitter, or sensitivity--bandwidth language in photon counting.

### Dechant finite-frequency response work

The comparison was tightened in Rev5. It now states only that recent finite-frequency fluctuation--response inequalities constrain steady-state finite-frequency response/fluctuations in general Markovian dynamics and yield broadband signal-to-noise bounds.

The manuscript explicitly distinguishes that response/noise framework from the first-registration timing-measure Parseval sum rule and does not claim generic finite-frequency response/noise novelty.

### Harmonic-analysis/probability ingredients

Poisson marking/displacement, Wiener theory, Parseval, hazard/survival calculus, and rearrangement arguments remain explicitly treated as established ingredients.

The novelty posture is the **combined photodetection resource-completeness stack**, not invention of those tools.

---

## 6. Mechanical verification

An assertion-based transformer

`manuscript/apply_rev5.py`

maps Rev4 to Rev5 and requires every replacement anchor to occur exactly once.

The final manuscript-only transformer state at commit

`0b464b3914bf358a4b296d1942df09b5aea9a5e5`

was verified by GitHub Actions. The bot reported successful Rev5 generation, LaTeX compilation, and artifact upload.

Therefore the WP35 correction, both figure references, the conservative Dechant wording, and the explicit `S_pre` definition all survived a complete build.

---

## 7. Final scientific assessment

No remaining defect found in this audit changes:

- the exact marked-event FI transfer;
- the Wiener atomic residual;
- the Parseval coefficient;
- the hazard--collision inequality;
- the WP34 inverse resource cost;
- the exact fixed-mean/fixed-variance no-go;
- the free-clock counterexample;
- the restricted thermodynamic gateway theorem;
- the rare-fast stationary-thermodynamic no-go.

The manuscript should now be treated as being at the **submission-package decision point**.

Additional foundational research is not the default next action.

---

## Status

**WP35 CORRECTION: APPLIED**

**FIGURE PROSE REFERENCES: APPLIED**

**FINAL CLAIM/CITATION AUDIT: PASSED WITH CONSERVATIVE DECHANT WORDING CHANGE**

**FINAL REV5 GENERATED BUILD: VERIFIED PASSED AT COMMIT `0b464b3914bf358a4b296d1942df09b5aea9a5e5`**

**SCIENTIFIC PUBLICATION GATE: PASSED TO SUBMISSION-PACKAGE STAGE**
