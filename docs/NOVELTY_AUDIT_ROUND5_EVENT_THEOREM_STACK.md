# Novelty Audit — Round 5: Autonomous Event Theorem Stack

**Date:** 2026-08-20

## Purpose

Audit the complete WP25–WP31 event-detector theorem stack against nearby timing, reliability, Poisson-channel, fluorescence-imaging, and finite-frequency response literature.

This document is intentionally conservative. It does not claim priority from absence of a search hit.

---

# 1. Current candidate contribution

For an autonomous/time-translation-invariant proper marked photodetection event channel, the project now has the following linked results:

1. source-normalized Poisson/coherent modulation FI is filtered by conditional registration-delay characteristic functions;
2. the asymptotic flat-band information residue equals conditional atomic timing collision mass (WP30, via classical Wiener theorem);
3. finite timing collision intensity
   \[
   R_2=2E_M\int f(t|M)^2dt
   \]
   gives an integrated spectral budget (WP26/WP28);
4. finite conditional local hazard `Lambda` gives `R2<=Lambda` and an explicit `1/Omega` information-bandwidth ceiling (WP25);
5. stationary EPR/activity/temperature labels do not bound `Lambda` by themselves (WP4);
6. in a restricted reversible optical-gateway Markov class, EPR/activity/throughput plus an absolute microscopic rate scale do bound `Lambda`, producing an explicit thermokinetic information-bandwidth theorem (WP29);
7. free source-synchronous clock/control defeats detector-only timing bounds unless reference resources are counted (WP27).

The potential novelty is the **photodetection-specific theorem stack and resource-completeness logic**, not the individual mathematical ingredients.

---

# 2. Detector timing / IRF literature

Single-photon detector metrology and TCSPC literature routinely characterize detector timing jitter through an instrument-response distribution. NIST terminology explicitly defines detector timing jitter as variation in the delay from optical arrival to electrical output and notes that the full shape may matter, not only one scalar width.

Time-correlated photon-counting literature treats finite IRFs as convolutions and analyzes their impact on measured temporal signals.

### Overlap

- registration-delay distributions / IRFs;
- timing-jitter shapes;
- convolution of optical timing signals with detector response;
- correction using additional timing/pulse information.

### Distinction

The located detector-timing sources do not formulate a source-normalized spectral Fisher-information theorem in terms of conditional local registration hazard, `L2` collision intensity, or atomic timing mass.

**Assessment:** adjacent prior art, not an identified theorem collision.

---

# 3. Fisher information + IRF / TCSPC / FLIM

There is substantial prior work applying Fisher information and Cramer-Rao analysis to time-correlated single-photon counting and fluorescence lifetime microscopy.

Representative work:

- information-theoretical analysis of TCSPC single-molecule measurements discusses instrument-response information losses;
- Bouchet et al. (2019) calculate CRLBs including instrument response and nonuniform background;
- Trinh & Esposito (2021) analyze how IRF width, temporal sampling, and photon statistics determine biochemical resolving power;
- Sumaya-Martinez & Torres-Garcia (2026) optimize time-gating/binning using Poisson Fisher information with IRF and background.

### Overlap

- Poisson photon-counting FI;
- IRF convolution;
- timing-resolution dependence of per-photon information;
- background and temporal sampling;
- additional observed channels/partitioning can increase accessible FI.

### Distinction

The located work generally asks for precision of **sample/lifetime parameters after convolution with a specified IRF**, or optimization of sampling. It does not identify a universal detector-side resource theorem of the form

\[
\bar\eta_{source\to electrical}
\le C\,W(\pi\Lambda)
\]

or the exact high-bandwidth atomic residual

\[
\lim\bar\eta_I
=\eta_cE_M\sum_jp_j(M)^2.
\]

It also does not appear to prove that conventional RMS/FWHM jitter moments are insufficient to bound source-information bandwidth by the WP26 spike-tail construction.

**Assessment:** this is the closest application-level prior art found so far. The manuscript must cite it and clearly distinguish source-modulation information transfer from lifetime-parameter estimation.

---

# 4. Hazard / reliability literature

Hazard rate

\[
h(t)=f(t)/S(t)
\]

and cumulative hazard are standard survival/reliability objects. Constant hazard and the exponential lifetime are standard.

An Efron–Johnstone 1987 technical report is explicitly titled *Fisher's Information in Terms of the Hazard Rate*.

### Overlap

- hazard functions;
- statistical Fisher information expressed using lifetime/hazard representations;
- characteristic functions and transforms of lifetime distributions;
- first-failure / first-passage models.

### Distinction

The Efron–Johnstone title is a terminology hazard for publication, but the located metadata indicate a statistical lifetime-distribution FI problem rather than optical source modulation transferred through a random registration delay.

The WP25 proof uses hazard as a **physical local registration-intensity cap** to bound

\[
\int f^2dt
\]

and then a source spectral FI integral via Parseval. No equivalent reliability theorem with this photodetection interpretation has yet been located.

**Assessment:** mathematical ingredients are prior art; wording must avoid suggesting the concept of Fisher information + hazard is new.

---

# 5. First-passage literature

First-passage theory contains extensive results on densities, transforms, moment generating functions, and bounds on first-passage densities for diffusions and Markov processes.

Some work explicitly derives upper bounds on first-passage densities from process/boundary data.

### Overlap

- first-registration/first-passage distributions;
- bounds on first-passage densities;
- Laplace/Fourier transforms;
- exponential first-exit stages in Markov chains.

### Distinction

No searched first-passage source was found that combines a local hazard/intensity ceiling with Poisson optical source FI to derive the WP25 spectral information bound, or that applies Wiener atomic-mass asymptotics as a photodetector information-bandwidth theorem.

**Assessment:** likely source of mathematical lemmas and citations, not yet an identified direct predecessor.

---

# 6. Random-delay and Poisson communication channels

Poisson optical communication theory is mature and studies continuous/discrete Poisson channels, dark current, peak/average input constraints, side information, and capacity.

Random-delay communication/remote-estimation literature studies messages or sampled processes transmitted through channels with random service/delay.

### Overlap

- Poisson event channels;
- dark counts/background;
- timing side information;
- random delay as a channel impairment;
- source/receiver side information can remove apparent information losses.

### Distinction

The located works optimize Shannon capacity, estimation age/error, or coding performance rather than source-normalized infinitesimal modulation FI under a physical first-registration hazard resource.

No result equivalent to the WP25/WP28 spectral concentration theorem was identified.

**Assessment:** important framing/citation neighborhood; no direct theorem collision found.

---

# 7. Wiener theorem / harmonic analysis

WP30 rests on a classical Wiener theorem for Fourier transforms of finite measures:

\[
\lim_{\Omega\to\infty}\frac1{2\Omega}
\int_{-\Omega}^{\Omega}|\hat\mu(\omega)|^2d\omega
=\sum_x|\mu(\{x\})|^2.
\]

This theorem is emphatically not new.

### Candidate project contribution

The new aspect, if any, is the interpretation that for an autonomous marked photodetection event channel the high-bandwidth **source-information residue** equals the conditional atomic timing collision mass.

Any paper should state explicitly that the mathematical theorem is classical and that the photodetection corollary is the derived result.

---

# 8. Finite-frequency response uncertainty literature

Dechant (PRL 2026) gives a general finite-frequency fluctuation-response inequality of the form

\[
R^\dagger S^{-1}R\le A
\]

for Markovian dynamics, plus a broadband consequence involving integrated squared response normalized by a time-domain/static observable variance.

Other 2026 response-KUR/TUR work gives related finite-frequency response/noise inequalities.

### Distinction

WP25 is not an obvious substitution into these equations:

- its left side is source-normalized Poisson/coherent optical modulation FI;
- the broadband integral arises from the Fourier transform of a first-registration delay distribution;
- the bound is controlled by local conditional first-registration intensity / timing collision concentration;
- WP30 characterizes the exact atomic residual.

**Assessment:** generic response/noise bounds are prior art; novelty can only lie in event-registration structure and resource completion.

---

# 9. Side information / timing correction

Experimental detector literature shows that timing walk/jitter can be corrected when extra pulse or event-history information is available. FI partitioning literature also establishes that retaining additional informative channels can increase accessible FI.

This strongly supports the project's insistence on conditioning on **all accessible event marks**.

Therefore the mark-robust formulation should be treated as physically necessary rather than presented as a surprising standalone novelty claim.

---

# 10. Current novelty classification

## Definitely not novel

- hazard/survival functions;
- Poisson FI formulas;
- timing-jitter / IRF convolution;
- Fisher-information analysis of time-resolved photon counting;
- Wiener atomic-mass theorem;
- Parseval/Plancherel;
- first-passage transforms;
- generic finite-frequency response/noise inequalities;
- synchronous/heterodyne detection and timing correction using side information.

## Potentially distinct

The **combined photodetection theorem stack**:

1. exact source modulation FI transfer through marked registration delays;
2. exact high-bandwidth residual = conditional atomic timing collision mass;
3. quantitative integrated spectral budget from `R2`;
4. microscopic sufficient bound from local conditional registration hazard/jump norm;
5. explicit conventional-jitter moment no-go;
6. explicit free-clock/control no-go;
7. thermodynamic no-go + restricted EPR/activity/throughput/microscopic-rate repair.

No equivalent complete stack has been identified in targeted searches.

## Safe provisional wording

> We derive a resource hierarchy for source-normalized temporal information transfer in autonomous photodetection event channels. Classical Fourier/probability results imply that deterministic timing atoms determine the asymptotic high-bandwidth information residue, while finite timing collision intensity and bounded local registration hazard provide quantitative spectral ceilings. We then show why stationary thermodynamic quantities and conventional jitter metrics do not by themselves supply these resources, and give a restricted thermokinetic completion when an absolute microscopic rate scale is bounded.

This wording claims the derived hierarchy, not invention of its mathematical ingredients.

---

# 11. Publication risk assessment

### Main risk

A mathematically equivalent result may exist in random-displacement point-process or timing-channel literature under terminology not captured by the current searches.

### Secondary risk

Reviewers may regard WP25/WP30 as elementary applications of Parseval/Wiener unless the resource-completeness counterexamples and thermodynamic bridge create sufficient conceptual value.

### Strengthening factors

- exact mark-robust formulation;
- conventional-jitter no-go;
- free-clock/control no-go;
- WP4 thermodynamic impossibility family;
- WP29 thermodynamic completion;
- clear distinction from conventional detector `-3 dB` bandwidth.

---

# 12. Status

**NOVELTY PROVISIONAL BUT IMPROVED.** No direct theorem collision found in targeted searches. A first manuscript should be framed as a photodetection resource-completeness theorem/synthesis, not as invention of hazard, Wiener, Parseval, Poisson FI, or detector timing theory.