# Paper 2 — Manuscript Architecture

**Status:** architecture approved after WP27 manuscript gate. This file is the required bridge between research notes and LaTeX drafting. Do not let the manuscript drift away from this claim structure without updating this file.

**Date:** 2026-08-21

---

# 1. Primary title and alternatives

## Recommended primary title

**Fisher Spectra and Information Singularities in Photodetectors with Memory**

Why this is preferred:

- states the two genuinely organizing objects: temporal Fisher spectrum and singularity;
- broad enough to contain the general autonomous-channel theorem;
- specific enough not to imply arbitrary quantum-optical universality;
- does not over-center dead time in the title even though Type II is the principal worked class;
- avoids claiming a universal speed limit or generic information theory of photodetectors.

## Strong alternatives

1. **Temporal Fisher Information in Photodetectors with Memory**
2. **Temporal Information Transfer Beyond Photodetector Saturation Curves**
3. **Information Spectra of Photodetectors with Memory: Type-II Paralysis and Random Recovery**
4. **When Saturation Curves Lose Information: Fisher Spectra of Photodetectors with Memory**

Avoid titles containing:

- “universal speed limit”;
- “complete theory of photodetection”;
- “fundamental limit of all photodetectors”;
- “first information theory of dead time.”

---

# 2. One-sentence thesis

> **A photodetector's conventional saturation curve is not an information-transfer law: for autonomous classical Poisson photodetection, temporal information is determined by the complete trajectory channel, allowing deterministic Type-II paralysis to erase static Fisher information while preserving every nonzero temporal mode, whereas random recovery generically removes that singularity even when conventional saturation statistics are unchanged.**

Everything in the main text should advance this sentence.

---

# 3. Four main claims

## Claim A — autonomous-channel Fisher spectral completeness

For a homogeneous Poisson source and arbitrary parameter-independent autonomous detector channel, the local output Fisher form for weak temporal intensity waveforms is represented by a bounded even multiplier

`0<=G(omega)<=1` a.e.

No independent-event delay kernel, finite detector state, low-flux approximation, or one-output-per-photon assumption is required.

Interpretation:

> spectral completeness comes from time-translation symmetry, not from independent-event timing physics.

Role in paper: **organizing theorem**, not principal novelty by itself.

---

## Claim B — deterministic Type-II spectral escape

For deterministic paralyzable dead time `tau`, at the conventional count-rate maximum `lambda*tau=1`:

- the complete stationary homogeneous experiment has `G_DC=0`;
- every nonzero temporal frequency has strictly positive complete-record local FI;
- at `omega*tau=pi`, at least `0.516975...` of incident local FI survives;
- the exact high-frequency retention tends to `1/e`.

Interpretation:

> a detector can be statically information-blind at saturation without possessing a finite temporal information cutoff.

Role in paper: **lead physical phenomenon**.

---

## Claim C — finite-mean recovery singularity theorem

Consider iid random Type-II recovery `T` with arbitrary law satisfying only

`0<E[T]=m<infinity`.

All such laws share the conventional mean curve

`r(lambda)=lambda exp(-lambda m)`.

For the complete stationary registered-timestamp record,

`G_DC=(r/lambda)I_D`, `0<=G_DC<=1`.

At the common count maximum `lambda*m=1`:

`G_DC=0 iff T=m almost surely`.

Thus deterministic recovery is the unique finite-mean recovery law that is completely static-Fisher-singular at the shared count maximum.

Every nondegenerate law has an explicit positive bounded-Laplace-statistic witness.

Interpretation:

> recovery-law shape is an information resource invisible to the conventional saturation curve; deterministic recovery is a singular boundary, not a generic feature of Type-II saturation.

Role in paper: **lead class-wide theorem**.

---

## Claim D — finite-summary resource incompleteness

Recovery mean and variance/CV still do not determine the timestamp information channel.

Explicit law A and law B have identical

`E[T]=1`, `Var(T)=1/4`, `CV=0.5`

and therefore identical complete conventional mean saturation curve, yet one common interval coarse-graining has zero FI for A and positive FI for B.

Interpretation:

> even augmenting the saturation curve by a familiar second recovery moment does not close the information-resource description.

Role in paper: **resource-completeness no-go**.

---

# 4. Main-text order

## I. Introduction

### Problem

Detector performance at high flux is commonly summarized by count-rate curves, dead time, recovery time, saturation point, timing jitter, or bandwidth-like scalars. None is automatically a complete descriptor of temporal information transfer.

### Gap

Existing dead-time literature is extensive and includes:

- paralyzable and nonparalyzable count distributions;
- renewal/cycle laws;
- modulated counting;
- mean/variance/noise spectra;
- information theory and estimation under dead time;
- inverse queue/output problems.

The missing question addressed here is narrower:

> what is the complete **local temporal Fisher transfer** of an autonomous detector with arbitrary memory, and what do familiar high-flux summaries fail to determine?

### Contributions paragraph

State the four claims above without “first” language.

### Scope

Classical Poisson/direct-detection intensity modulation; parameter-independent autonomous detector channels. Not arbitrary nonclassical light or phase-sensitive coherent detection.

---

## II. Autonomous detector channels have a temporal Fisher spectrum

Main theorem from WP10/WP17.

### Minimal derivation

1. Poisson source score
   
   `S_u=int u(t)[N(dt)-Phi0dt]`.
2. Markov image score
   
   `S_u^out=E[S_u|Y]`.
3. Positive contraction on waveform `L2`.
4. Autonomy => commutes with translations.
5. Fourier multiplier `G(omega)`.

### Main-text corollaries

- `0<=G<=1` a.e.;
- frequency-by-frequency data processing under autonomous coarse-graining;
- pointwise a.e. ordering iff local Fisher dominance for all finite-energy weak waveform tasks;
- Paper 1 independent-event transfer recovered as special case.

Keep kernel randomization, standard-Borel details, and full DQM proof in Appendix A.

End section with question:

> What can this complete spectrum do in a detector whose conventional response is already saturated?

---

## III. Deterministic Type-II paralysis creates a static information zero, not a temporal cutoff

Introduce ideal deterministic paralyzable detector.

### III.A Baseline renewal law and static singularity

`r=lambda exp(-lambda tau)`.

At `lambda*tau=1`, use `G_DC=0` terminology.

Emphasize that this is **complete timestamp** blindness in the uniform source-rate direction, not merely zero mean-count slope.

### III.B Nonzero-frequency survival

Mean mode response

`M_rho(y)=1-rho(1-exp(-iy))/(iy)`.

Baseline Bartlett spectrum.

One-statistic information lower bound

`G_rho(omega)>=L_rho(y)`.

At `rho=1`, positive for all `omega!=0`.

### III.C Exact high-frequency complete-record retention

Present compact transition-score representation and result

`G_rho(omega)->exp(-rho)`.

At paralysis: `1/e`.

Do not overload main text with Volterra derivation; numerical exact spectrum becomes Fig. 2 and equations go to Appendix B.

### III.D Interpretation

The static singularity is frequency-selective. Recovery time is not itself an information bandwidth.

---

## IV. Random recovery destroys the deterministic information singularity

General iid recovery `T` with finite mean `m`.

Credit classical `M/G/infinity` / Type-II cycle formulas immediately.

### IV.A Same conventional saturation curve for every recovery shape

`r(lambda)=lambda exp(-lambda m)`.

All equal-mean recovery laws therefore have exactly the same mean input-output count curve and the same zero count slope at `lambda*m=1`.

This sets the adversarial comparison.

### IV.B Bounded Laplace witness

Define

`A(t)=E[min(T,t)]`,

`R(t)=E[(T-t)_+]`,

and `W_s`.

At `lambda*m=1`,

`dot phi_s=W_s/(1+u_s)^2`.

Show:

`W_s=0 iff T=m a.s.`.

This gives an accessible intuition before the FI theorem: one bounded statistic already separates every nondegenerate recovery law at first order.

### IV.C Complete stationary FI theorem

State theorem:

`G_DC=(r/lambda)I_D`, `0<=G_DC<=1`,

and at `lambda*m=1`,

`G_DC=0 iff T=m a.s.`.

Main text proof sketch:

1. Palm stopped marked-Poisson cycle gives `I_D<=lambda/r`;
2. stationary boundary is a finite active Poisson cloud with mean `lambda m`;
3. boundary information is sublinear in long windows;
4. renewal bulk rate is `rI_D`.

Full DQM localization and window proof go to Appendices C and D.

### IV.D Quantitative example

Use exponential recovery as one concrete calibration:

`G_DC~0.06915579`

at `lambda=m^{-1}`.

Do not clutter main text with full gamma table unless a figure benefits.

---

## V. Mean and variance do not complete the recovery resource

Present WP19 exact pair of recovery laws.

The core analytic witness should be the common coarse-graining, not the numerical Volterra FI.

State:

- same mean;
- same variance;
- same CV;
- same entire conventional saturation curve;
- different probability and derivative for the same interval event.

Then mention supporting full-FI numerical values as a cross-check.

This section converts the Type-II example into a **resource-completeness statement**.

---

## VI. Discussion

### VI.A What the detector resource actually is

Not one scalar dead time, recovery mean, variance, count maximum, or conventional bandwidth. The complete local object is the trajectory-channel Fisher operator/spectrum.

### VI.B Atomic timing paths

Briefly use WP22/WP23:

- high-frequency Cesaro retention tracks atomic timing energy in conditional score under appropriate measure regularity;
- exact visible timestamps are one path;
- sharp delayed paths can contribute too;
- therefore do not oversimplify residue as merely registered fraction for arbitrary channels.

No standalone novelty language here.

### VI.C Relation to existing detector metrics

Discuss:

- count-rate saturation curve;
- dead/recovery time;
- timestamp jitter;
- conventional signal transfer/noise approaches;
- why each is a projection/summary rather than a complete local information descriptor.

### VI.D Scope and limitations

Explicitly list:

- classical Poisson/direct detection;
- local weak intensity modulation;
- complete accessible record;
- parameter-independent autonomous channel;
- Type-II model is idealized;
- no claim of arbitrary quantum-input/QFI result;
- no generic Blackwell dominance;
- no claim that recovery randomness is universally beneficial.

---

# 5. Appendix structure

## Appendix A — general-channel statistical/harmonic-analysis proof

- Poisson DQM;
- kernel randomization;
- DQM under statistics;
- positive contraction;
- time-shift covariance;
- translation-invariant multiplier theorem;
- narrowband/Lebesgue-point operational corollary;
- local Fisher ordering/data processing.

## Appendix B — deterministic Type-II exact calculations

- interval transform;
- Bartlett spectrum algebra;
- exact transition-score representation;
- low-frequency continuity at paralysis;
- high-frequency `1/e` proof;
- Volterra equation and convergence data.

## Appendix C — finite-mean Palm-cycle DQM

- marked-Poisson stopping construction;
- bounded stopping localization `D wedge K`;
- stopped likelihood and score;
- `L2` score convergence from `E[D]<infinity`;
- data processing to interval FI;
- bounded-Laplace separation and Hellinger/TV witness.

## Appendix D — stationary window FI rate

- censored interval information `J(t)`;
- ordinary renewal bulk rate;
- finite stationary active-cloud state;
- forward-recurrence first-stage bound;
- chain rule and random residual horizon;
- final `G_DC=G_cyc` theorem.

## Appendix E — exact resource-incompleteness construction

- moment matching for laws A/B;
- coarse-graining formula;
- exact derivative;
- optional Volterra numerical method/table.

## Appendix F — notation / connection to Paper 1

Only if needed. Do not reproduce Paper 1.

---

# 6. Figure plan

## Figure 1 — trajectory-channel concept and scalar-metric failure

One clean schematic:

Poisson input trajectory -> autonomous detector with hidden memory -> complete accessible timestamp record.

Below it, contrast:

- scalar saturation curve `r(lambda)`;
- complete Fisher spectrum `G(omega)`.

Purpose: make the paper's question visually obvious before Type-II details.

No decorative infographic elements.

## Figure 2 — deterministic Type-II information spectrum at paralysis

Plot versus `omega*tau`:

- exact numerical `G_1(omega)`;
- rigorous lower bound `L_1`;
- horizontal asymptote `1/e`;
- mark the DC zero;
- mark `pi` and the `0.516975` bound.

This is the principal result figure.

## Figure 3 — same saturation curve, different information

Upper/main panel: identical

`r(lambda)=lambda exp(-lambda m)`

for deterministic and selected random recovery laws.

At `lambda*m=1`, annotate common zero mean slope.

Companion panel or inset: static `G_DC`:

- deterministic = 0;
- exponential ~0.06916;
- perhaps one or two gamma examples if visually useful.

Purpose: immediately demonstrate that the saturation curve is not the information law.

## Figure 4 — mean+variance no-go

Show the two discrete recovery distributions A/B with same mean/variance and a compact indication of their different timestamp coarse-graining FI.

Could be a discrete stem plot + small result table rather than another continuous chart.

Avoid unnecessary fifth figure unless manuscript readability demands it.

---

# 7. Claim / prior-art matrix

| Candidate manuscript claim | Closest established literature | What is already old | Narrow delta retained here | Positioning |
|---|---|---|---|---|
| Autonomous detector local FI diagonalizes into `G(omega)` | conditional-score/Fisher data processing; function-valued FI operators; translation-invariant `L2` multipliers; Clark 2026 | score projection, FI contraction, operator/kernel formalism, Fourier multipliers | photodetection-channel synthesis for arbitrary autonomous hidden-memory Poisson detectors + waveform ordering | Organizing theorem; no “first” |
| Deterministic Type-II static blindness but every nonzero frequency informative | Teich/Vannucci 1978 modulated paralyzable counting; classical Type-II renewal/count spectra; neural refractory timing work | modulation under dead time, mean response, count distributions, renewal spectra | complete-timestamp Fisher statement, all nonzero frequencies, exact high-frequency complete-record residue `1/e` | Lead specific novelty candidate |
| Random recovery shares same mean curve but deterministic uniquely has zero static FI | classical random Type-II / `M/G/infinity`; Dvurecenskij/Ososkov 1984/1985; Apanasovich/Paltsev 1995 pair correlation; inverse-output literature | cycle laws, busy periods, pair correlation, recovery/output identifiability | exact finite-mean complete stationary FI `zero iff deterministic` at universal count maximum; explicit bounded witness | Lead class-wide novelty candidate, conservative wording |
| Stationary window FI equals Palm interval rate under finite mean | Zhao/Nagaraja 2011 | generic WCRP FI asymptotic under stronger FRT regularity | Type-II-specific finite-mean proof via finite stationary active-cloud boundary | Proof hardening/support, not lead novelty |
| Mean+variance do not determine information channel | generic moment insufficiency is philosophically unsurprising | moments often fail to determine distributions | explicit same-mean/same-variance/same-saturation Type-II construction with common timestamp statistic giving different FI | Strong resource no-go |
| High-frequency atom interpretation | Bartlett spectra, Campbell/Palm, Wiener/Rajchman, score covariance | all harmonic/spectral ingredients | conditional-source-score atomic timing interpretation in detector framework | Discussion/bridge only |
| Type-II intensity inference | Barat/Dautremer/Trigano 2006 and related censoring/inference work | estimation of time-varying Type-II intensity, richer idle/dead observation | present work uses complete timestamps only and derives local FI/resource theorems | Cite explicitly, no priority claim |
| Generic output identifiability | Kovalenko; Kendall/Lewis; Ivnitskii; Afanaseva/Mikhailova; Brown; Ross; George/Agrawal | output-based queue/service identification | none claimed generically | Background boundary only |

---

# 8. Abstract skeleton

Do not write a novelty-heavy abstract. Structure:

1. **Problem sentence:** high-flux photodetectors are commonly characterized by scalar saturation/dead-time summaries, but these need not determine temporal information transfer.
2. **General result:** derive the local temporal Fisher operator for an arbitrary autonomous parameter-independent detector channel driven by weak Poisson intensity modulation; time-translation symmetry makes it a bounded spectrum `G(omega)`.
3. **Deterministic Type-II result:** at the classical paralyzable count maximum, the complete timestamp record is statically Fisher-blind while every nonzero temporal frequency remains informative; high-frequency retention tends to `1/e`.
4. **Random recovery result:** for arbitrary finite-mean iid recovery, all laws share the same mean saturation curve, yet deterministic recovery is uniquely zero-FI at the shared maximum; any nondegenerate recovery has positive static timestamp information.
5. **No-go:** even equal recovery mean and variance do not determine the timestamp information channel.
6. **Conclusion:** complete trajectory-channel structure, rather than the conventional saturation curve or a few recovery moments, is required to characterize temporal information transfer in detectors with memory.

No “first,” no generic all-photodetector claim, no quantum/QFI overreach.

---

# 9. Introduction literature buckets

Do not organize references as a long chronology. Use four buckets:

1. **Classical dead-time / Type-II counter theory** — Takacs, Pyke, Smith, Dvurecenskij/Ososkov, etc.
2. **Optical modulation and dead-time information/statistics** — Teich/Vannucci, Vannucci/Teich, Teich/Cantor.
3. **Modern estimation/FI under detector dead time** — Barat/Dautremer/Trigano; Jorgensen/Johnson; relevant SPAD/lidar literature.
4. **Statistical foundations** — DQM/Markov projection, renewal-window FI, functional point-process FI.

This makes it obvious that the paper builds on established fields rather than claiming they were absent.

---

# 10. Manuscript drafting rules

1. Main text should emphasize physical/information consequences; move measure-theory and renewal technicalities to appendices.
2. Never use `G(0)` from WP10 without a model-specific continuous/static identification. Use `G_DC` where the experiment is homogeneous/static.
3. Pure sinusoids are long-window/narrowband limits, not primitive `L2` source tangents.
4. Credit classical formulas at first use.
5. Keep the analytic theorem separate from numerical validation.
6. Never write “randomness helps” without the precise fixed-mean, count-maximum qualification.
7. Use “complete accessible timestamp record,” not “complete detector state,” unless the latter is truly observed.
8. Avoid generic Blackwell language; the ordering result is local Fisher ordering over the admitted waveform tangent class.
9. Do not hide inaccessible Afanaseva–Mikhailova prior art behind a priority claim.
10. If a new theorem is discovered while drafting, document it in a new WP before modifying the manuscript.

---

# 11. Next file to create

After one architecture sanity check, create:

`paper2/manuscript/fisher_spectra_memory_photodetectors_rev1.tex`

The initial draft should prioritize theorem statements, section logic, and citation placeholders over polished prose. Do not attempt submission formatting until the science draft is internally stable.
