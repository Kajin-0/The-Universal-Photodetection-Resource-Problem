# WP09 — Type-II Dead-Time and Fisher-Operator Prior-Art Audit

**Status:** targeted hostile audit after WP07/WP08. The new results remain plausible novelty targets, but several surrounding ingredients are clearly old and must be conceded explicitly.

## 1. Why this audit was necessary

WP07 produced a continuous-time Type-II result:

\[
G_1(0)=0,
\qquad
G_1(\omega)>0\ \text{for every }\omega\ne0,
\qquad
\lim_{|\omega|\to\infty}G_1(\omega)=e^{-1}.
\]

WP08 then proposed a broader visible-event high-frequency residue law for history-dependent exact-timestamp selectors.

Before treating either as a breakthrough, we searched specifically for:

- modulated paralyzable photon counting;
- paralyzable dead-time count distributions and renewal spectra;
- information-theoretic dead-time analyses;
- Fisher-information operators for point processes;
- high-frequency Fisher information under point-process thinning or missing events.

---

## 2. Modulated paralyzable photon counting is old

### Teich & Vannucci 1978

Malvin C. Teich and Giovanni Vannucci,

*Observation of dead-time-modified photocounting distributions for modulated laser radiation*,
J. Opt. Soc. Am. **68**, 1338--1342 (1978),
DOI `10.1364/JOSA.68.001338`.

This paper experimentally verifies photocounting distributions for triangularly and sinusoidally modulated laser radiation and presents a new expression, for its time, for the counting distribution with **paralyzable dead time**.

The full-text discussion makes clear that they considered intensity-modulated radiation and derived fixed-window count distributions under extended dead time.

### Consequence

Paper 2 must **not** claim novelty for:

- applying modulation to a paralyzable counter;
- the existence of frequency-dependent dead-time effects;
- paralyzable count distributions under modulated illumination;
- the standard mean count-rate nonlinearity;
- simple modulation-efficiency calculations.

WP07's novelty target is narrower and stronger: **complete timestamp-record local Fisher information as a function of temporal frequency**, including exact DC nonidentifiability and finite-frequency survival.

---

## 3. Information theory with detector dead time is also old

### Teich & Cantor 1978

Malvin C. Teich and B. I. Cantor,

*Information, Error, and Imaging in Deadtime-Perturbed Doubly Stochastic Poisson Counting Systems*,
IEEE J. Quantum Electron. **14**, 993--1003 (1978),
DOI `10.1109/JQE.1978.1069731`.

This work treats likelihood-ratio detection, receiver operating characteristics, probability of error, average mutual information, channel capacity, and maximum-likelihood image estimation for **nonparalyzable** dead-time-perturbed counting systems.

### Consequence

Paper 2 must **not** claim:

- first information-theoretic analysis of photodetector dead time;
- first dead-time likelihood theory;
- first connection between dead time and channel capacity / estimation performance.

The candidate distinction is local **arbitrary-waveform Fisher spectral completeness**, especially with hidden Type-II memory.

---

## 4. Rate-variation and spectral dead-time literature is extensive

Additional prior work includes:

- Vannucci & Teich, *Effects of rate variation on the counting statistics of dead-time-modified Poisson processes*, Opt. Commun. **25**, 267--272 (1978), DOI `10.1016/0030-4018(78)90322-X`, deriving mean/variance effects for time-varying Poisson rates under nonparalyzable dead time.
- Classical and modern work on dead-time-modified power spectra, count moments, correlation functions, and pileup.
- Teich/Vannucci and later authors on dead-time-modified photocount moments and statistical distributions.
- Recent detector-engineering models for paralyzable and hybrid dead time at high flux.

### Consequence

The baseline renewal spectrum in WP07 and the exact mean response

\[
r(t)=\lambda(t)\exp[-\int_{t-\tau}^{t}\lambda(s)ds]
\]

are **supporting calculations**, not the central novelty.

---

## 5. Close 2026 statistical dead-time work

Frederic J. N. Jorgensen and Steven G. Johnson,

*Fundamental Bounds and Efficient Estimation for Dead-Time-Constrained Event Detection, with Application to Single-Photon Lidar*, arXiv:2605.23210 (2026).

They establish local asymptotic normality and Fisher-information rates for discrete periodic **nonparalyzable** dead-time event detection with arbitrary causal gating. They identify sufficient statistics and efficient estimators.

They explicitly list extension to **paralyzable (Type-II) dead time** as future work.

### Consequence

- WP04's nonparalyzable result is a validation/corollary, not a priority claim.
- WP05--WP07 remain more promising because hidden events alter future availability and the state cannot be reconstructed from output timestamps.
- Nevertheless, Jorgensen--Johnson demonstrate that rigorous LAN/FI theory for dead-time event detection already exists nearby, so Paper 2 must compare carefully rather than claim an untouched field.

---

## 6. Function-valued Fisher-information operators for point processes are not new

Daniel E. Clark,

*Bartlett identities for spatial point processes*, Statistics & Probability Letters **236** (2026), article 110779,
DOI `10.1016/j.spl.2026.110779`.

Clark treats the log-likelihood as a functional of a function-valued point-process parameter and develops score, curvature, cumulant, and Fisher-information operators on configuration space. In the Poisson case the Fisher operator is pointwise; more general point processes generate nonlocal operator structure.

There is also broader literature on Fisher operators in inverse problems, wave-field shaping, stationary time series, and stochastic processes.

### Consequence

Paper 2 cannot claim novelty for:

- introducing a Fisher-information operator for a function-valued parameter;
- saying correlated point processes lead to a nonlocal FI kernel/operator;
- using operator order to compare quadratic information forms in the abstract.

The candidate new step is the **detector-channel retention operator acting on a fixed Poisson source tangent**, followed by autonomy-induced temporal Fourier diagonalization and photodetection-specific consequences.

---

## 7. Dead-time power spectra do not equal Fisher spectra

There is substantial literature on how detector dead time distorts the power spectral density of measured point processes. This includes X-ray timing, radiation counting, photon correlation, and laser-Doppler applications.

WP07 uses the baseline output renewal PSD only inside the information inequality

\[
F\ge(\partial E Z)^2/\operatorname{Var}Z
\]

to obtain a **lower bound** on the complete output Fisher spectrum.

The dead-time PSD itself is therefore not the proposed new metric. The distinction is:

- PSD: second-order fluctuations of the observed process at a fixed parameter;
- Fisher spectrum `G(omega)`: local distinguishability of source-waveform perturbations after the full detector channel.

Do not blur these concepts in a manuscript.

---

## 8. What the search did not locate

The targeted search did **not** locate a predecessor for the following combined statements:

### A. General autonomous-channel Fisher spectrum

For a fixed stationary Poisson source tangent passed through an arbitrary parameter-independent autonomous detector channel, the complete local waveform FI is represented by a bounded scalar frequency multiplier `G_Phi0(omega)` even with arbitrary detector memory.

### B. Discrete Type-II exact information high-pass

For

\[
Y_n=X_n(1-X_{n-1})
\]

at `p=1/2`, the complete-record local Fisher spectrum has the exact closed form from WP06, vanishes at DC, and is strictly increasing to `3/4+ln(3)/16` at Nyquist.

### C. Continuous Type-II spectral survival

For the ideal continuous paralyzable Poisson counter at `lambda*tau=1`, the complete homogeneous output experiment has zero local DC FI, while every nonzero temporal frequency retains positive FI; the high-frequency limit is `e^{-1}`.

### D. Visible-event high-frequency Fisher residue

For a broad history-dependent exact-timestamp event-selector class under mixing/diffuse-posterior conditions,

\[
G(\omega)\to r/\lambda.
\]

These remain **plausible novelty targets**, not certified priorities.

---

## 9. Important related 2026 engineering literature

P. Zambon,

*Dead time models for multi-threshold counting detectors in paralyzable and retrigger-based nonparalyzable modes*,
Nucl. Instrum. Methods Phys. Res. A **1092**, 171795 (2026),
DOI `10.1016/j.nima.2026.171795`.

This derives recorded count-rate models for arbitrary threshold order under Poisson arrivals, including paralyzable operation, and validates them numerically/experimentally.

Other 2026 work studies higher-order interarrival statistics and hybrid paralysis characterization.

### Consequence

The practical relevance of paralyzable/high-flux detector modeling is current, but count-rate or interarrival characterization by itself is not a novelty route.

---

## 10. Current novelty verdict

**Proceed, but with narrower claims.**

The novelty has survived this targeted audit in the following form:

> The possible breakthrough is not `dead time + Fisher information`. It is a complete temporal Fisher-transfer theory for arbitrary autonomous detector channels, with exact hidden-memory examples showing information-spectral behavior that count-rate slopes and conventional dead-time response do not characterize.

The continuous Type-II result materially strengthens this case because it proves a phenomenon in a physically standard continuous-time paralyzable model rather than only in a discrete toy model.

---

## 11. Searches still required before submission-level priority language

1. Statistical experiments for **dependent thinning** of point processes and full survivor timestamps.
2. Frequency-domain LAN/Fisher theory for stationary point-process observation channels.
3. Neural refractory-process information spectra / stimulus Fisher kernels.
4. Missing-event / hidden-event point-process inference where survivor times are exact.
5. System-identification literature deriving waveform FI spectra for nonlinear stationary channels.
6. Continuous-measurement and spike-train literature using score projections under temporal stationarity.
7. Older nuclear-counting literature on sinusoidal rate perturbations of paralyzable counters beyond fixed-window count moments.

Until these are checked, avoid `first`, `unprecedented`, or universal-priority language.
