# Novelty Audit — Round 4: Proper-Event Information-Bandwidth Theorem

**Date:** 2026-08-20

## Purpose

Audit the closest known literature to WP25–WP27 before any publication-level novelty claim.

Current safe posture:

> The individual mathematical/statistical ingredients of WP25 are established. A targeted search has not yet identified a prior photodetection theorem equivalent to the complete conditional-registration-hazard / marked-record / Parseval / source-Fisher-information bandwidth result. Novelty remains provisional.

---

# 1. Single-photon-detector performance metrics — established prior art

Single-photon-detector literature routinely treats the following as core performance metrics:

- detection efficiency;
- dark-count rate;
- dead time / maximum count rate;
- timing jitter / temporal resolution;
- photon-number resolution.

A standard review is:

M. D. Eisaman, J. Fan, A. Migdall, S. V. Polyakov,
`Invited Review Article: Single-photon sources and detectors`,
Review of Scientific Instruments 82, 071101 (2011),
DOI `10.1063/1.3610677`.

That literature explicitly defines timing jitter as event-to-event variation between optical arrival and electrical output, often summarized by FWHM of an instrument-response function.

**Not novel:** timing jitter as a detector metric; efficiency/dark/jitter/dead-time tradeoff discussions.

WP26's candidate contribution is narrower: prove that ordinary mean/FWHM/RMS jitter is not a sufficient variable for a universal **source-information bandwidth** theorem.

---

# 2. Detection-time distributions and jitter models — established prior art

Modern quantum photodetector models explicitly compute distributions of registration times and derived jitter metrics.

Example:

`Nanoscale architecture for frequency-resolving single-photon detectors`, Communications Physics (2023).

The paper defines channel-resolved detection probabilities and jitter from moments of the detection-time distribution.

Many SPAD/SNSPD studies likewise model or measure full instrument response functions.

**Not novel:** using a detection-time probability distribution to characterize temporal response.

No equivalent result was located that uses a **uniform conditional hazard/operator norm** to prove an integrated Fisher-information bandwidth ceiling.

---

# 3. Marked Poisson Fisher information — established prior art

Marked/spatio-temporal Poisson process Fisher-information formulas are standard in statistical imaging.

Representative reference:

S. Ram, E. S. Ward, R. J. Ober,
`A Stochastic Analysis of Performance Limits for Optical Microscopes`,
Multidimensional Systems and Signal Processing 17, 27–57 (2006),
DOI `10.1007/s11045-005-6237-2`.

Subsequent single-molecule microscopy literature gives general FI formulas for spatio-temporal marked Poisson data.

**Not novel:** FI of a marked Poisson record; treating spatial/channel labels as marks.

WP25 uses this standard machinery specifically to ensure that accessible event marks are not silently discarded when claiming timing-information loss.

---

# 4. Timing convolution / characteristic functions — established mathematics and detector practice

Jitter and instrument-response convolution are standard in photon counting, TCSPC, fluorescence timing, and detector calibration.

Fourier transforms / characteristic functions of timing kernels are standard signal-processing tools.

**Not novel:**

\[
H(\omega)=\int f(t)e^{-i\omega t}dt
\]

or the statement that timing convolution suppresses high-frequency modulation after marginalization.

WP25's candidate novelty is the resource inequality

\[
\|f(\cdot\mid m)\|_2^2\le\Lambda/2
\]

from a **conditional local registration-hazard bound**, followed by Parseval and source-FI normalization.

---

# 5. Hazard-rate mathematics — established prior art

Hazard/survival theory is standard:

\[
h(t)=f(t)/S(t).
\]

Fisher information has also been represented in terms of hazard functions in the statistics literature.

**Not novel:** hazard functions or generic FI/hazard identities.

No located source connected a physical photodetector's **maximum primary registration hazard** to an average modulation-information bandwidth through

\[
\int f^2dt\le\Lambda/2
\]

and Parseval.

---

# 6. General finite-frequency response/noise bounds — very close but distinct

Andreas Dechant,
`Finite-Frequency Fluctuation-Response Inequality`,
Physical Review Letters 136, 207101 (2026),
DOI `10.1103/3hs9-dz3d`.

This work derives a finite-frequency inequality connecting response and fluctuations for general Markovian steady-state dynamics and obtains a universal broadband SNR bound depending on damping and temperature.

This is an important novelty constraint.

WP25 is not allowed to claim the first universal broadband response/noise inequality.

Current distinction:

- Dechant: general steady-state Markov response/fluctuation inequality for observables and perturbations;
- WP25: proper primary-event photodetection, source-normalized optical modulation FI, marked first-registration records, and a local conditional registration-intensity resource. The proof does not assume Markovianity once the event delay/hazard description exists.

A theorem-level variable mapping must still be done to ensure WP25 is not an indirect corollary of Dechant in its overlapping Markov subclass.

---

# 7. Quantum/kinetic precision bounds — nearby prior art

Relevant 2026 results include:

- T. V. Vu, R. Honma, K. Saito, `Universal Precision Limits in General Open Quantum Systems`, PRL 136, 190401 (2026), DOI `10.1103/kldv-l3wl`;
- K. Liu, J. Gu, `Response kinetic uncertainty relation for Markovian open quantum systems`, PRA 113, 062443 (2026), DOI `10.1103/ps1b-8l1x`.

These constrain precision/response using generalized activity, asymmetry, or quantum transition terms.

WP4 already demonstrates why **stationary** activity/EPR need not bound the local registration-rate norm needed by WP25.

Do not claim generic activity/precision relations as new.

---

# 8. Synchronous/heterodyne/lock-in detection — established prior art

Heterodyne, homodyne, lock-in detection, synchronous gating, and time-dependent mixing are long-established methods for down-converting high-frequency information using a reference oscillator.

**Not novel:** synchronous detection itself.

WP27's candidate contribution is only the resource-theorem consequence:

> a free reference clock/control bandwidth is a missing resource that invalidates a detector-only temporal bandwidth theorem for unrestricted nonautonomous detectors.

The explicit phase-mark FI counterexample is used as a no-go construction, not as a claim of inventing synchronous detection.

---

# 9. Conventional photodiode bandwidth-efficiency theory — established prior art

Classical high-speed photodiode theory already contains bandwidth-efficiency tradeoffs such as

\[
B\eta\propto\alpha v
\]

for vertically illuminated devices, and traveling-wave/waveguide architectures are known to relax conventional transit/RC limitations.

This strongly constrains any attempt to frame WP15–WP24 as a new generic photodiode speed theorem.

Those work packages are now frozen as validation/examples.

---

# 10. Targeted searches performed

Searches on 2026-08-20 included combinations of:

- photodetector / single-photon detector + Fisher information + timing jitter;
- characteristic function + timing jitter + detector response;
- hazard rate + photodetection + information bandwidth;
- marked Poisson + photodetection + Fisher information;
- finite-frequency photodetector information bounds.

Results located standard jitter metrics, marked-Poisson FI frameworks, timing-distribution models, and general fluctuation-response bounds, but no exact match to WP25's complete theorem.

Absence from targeted search is **not proof of novelty**.

---

# 11. Current defensible novelty statement

Safe wording:

> We derive, for an autonomous proper marked-event photodetector class, a source-normalized Fisher-information bandwidth bound controlled by the conditional local primary-registration intensity after all accessible event side information is retained. The result is assembled from standard point-process, hazard, Parseval, and data-processing tools. Targeted literature search has not identified an equivalent photodetection resource theorem; novelty remains subject to theorem-level comparison with general finite-frequency response and detector-timing literature.

Unsafe wording:

- `first fundamental detector bandwidth bound`;
- `first information-theoretic photodetector limit`;
- `first relation between jitter and bandwidth`;
- `first Fisher-information detector theorem`;
- `first thermodynamic photodetection bound`.

---

# 12. Remaining novelty gates

1. Read Dechant's theorem at equation level and test whether WP25 follows after choosing a counting observable and optical perturbation.
2. Search point-process/queueing/reliability literature for Fourier or information inequalities under bounded hazard.
3. Search single-photon timing literature for integrated modulation-transfer bounds based on the full IRF rather than FWHM.
4. Search communication theory for Poisson channels with random propagation delay and FI/capacity bounds.
5. Only after these checks decide whether WP25 is a paper-level theorem or a useful photodetection specialization of known mathematics.

---

# Status

**Novelty provisional. Strong overlap boundaries identified; no exact prior theorem located yet.**