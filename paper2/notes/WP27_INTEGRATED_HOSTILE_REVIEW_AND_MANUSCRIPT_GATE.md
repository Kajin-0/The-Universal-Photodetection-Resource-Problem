# WP27 — Integrated hostile review and Paper-2 manuscript gate

**Status:** integrated adversarial review of the candidate Paper-2 theorem stack after closure of the finite-mean/heavy-tail/fixed-window proof program. No fatal mathematical defect was found in the core stack. Several novelty and notation claims are narrowed. Subject to the explicit repairs below, the project has now **passed the threshold for manuscript drafting**.

**Date:** 2026-08-21

---

# 1. Review target

Core results reviewed together:

1. `WP10/WP17` — general autonomous-channel temporal Fisher spectrum;
2. `WP07` — deterministic continuous Type-II spectral survival at the paralysis maximum;
3. `WP25/WP26` — arbitrary finite-mean iid-recovery Type-II static Fisher singularity theorem, Palm-cycle and stationary-window versions;
4. `WP19` — exact mean+variance insufficiency/resource no-go;
5. `WP22/WP23/WP24` — conditional-score atomic timing-path bridge theory and its novelty downgrade.

The review asked:

- Is there a hidden mathematical inconsistency between the general spectral theorem and the model-specific static results?
- Does WP07 actually prove complete-record dynamic information survival, or merely mean-response survival?
- Does WP25/WP26 still hide smoothness, finite-variance, or forward-recurrence assumptions?
- Is the claimed Type-II novelty preempted by old counter/queueing theory?
- Do these results form one coherent resource-theory paper rather than a collection of dead-time observations?

---

# 2. Overall verdict

## Manuscript gate

`boxed: PASS — WITH MANDATORY POSITIONING/NOTATION REPAIRS`

The core is now strong enough to justify drafting a Paper-2 manuscript.

This does **not** mean priority is certified. It means:

1. the central theorem stack is mathematically coherent enough to write;
2. the strongest physical conclusions survive hostile proof review;
3. the novelty can be stated narrowly without relying on generic dead-time, renewal, inverse-output, or Fisher machinery as new;
4. the results form one logical thesis.

The manuscript should be written conservatively and should not contain “first,” “universal speed limit,” or generic dead-time-information priority language.

---

# 3. WP10/WP17 hostile proof review

## 3.1 Core theorem

For a homogeneous Poisson source and compactly supported smooth waveform tangents,

`S_u=int u(t)[N(dt)-Phi0 dt]`.

For any parameter-independent stochastic detector kernel,

`S_u^out=E[S_u|Y]`.

The induced Fisher form extends to a positive contraction `A_K` on `L2(R)`. Autonomy/time-translation covariance implies exact commutation with translations and hence a scalar Fourier multiplier

`0<=G_{Phi0,K}(omega)<=1` a.e.

No independent-event delay kernel is required.

## 3.2 Proof status

No fatal issue found.

The publication-grade proof route remains sound:

- standard Poisson configuration space;
- compact-support Poisson DQM;
- standard-Borel kernel randomization;
- DQM under statistics / conditional-score projection;
- bounded extension by Riesz;
- translation covariance;
- classical `L2` multiplier theorem;
- narrowband wavepacket interpretation at Lebesgue points.

## 3.3 Novelty status

All mathematical ingredients are standard. The theorem must be positioned as a **photodetection-channel synthesis/completeness result**, not a new theorem in harmonic analysis or general mathematical statistics.

The defensible conceptual contribution is:

> arbitrary autonomous classical Poisson photodetection channels, even with hidden high-flux memory, possess a complete local temporal Fisher multiplier; independent-event physics is not what creates spectral completeness — time-translation symmetry is.

This organizing theorem is worthwhile only because the Type-II consequences below are nontrivial.

---

# 4. WP07 hostile proof review

## 4.1 What is rigorous

For deterministic paralyzable dead time `tau`, `rho=lambda*tau`, output rate

`r=lambda exp(-rho)`.

At `rho=1`, the complete homogeneous output renewal law depends on `lambda` only through `r(lambda)`, whose first derivative vanishes. Hence the **stationary static Fisher rate is zero**.

For a nonzero temporal frequency, the exact first-order mean response is

`M_rho(y)=1-rho(1-exp(-iy))/(iy)`, `y=omega*tau`.

At `rho=1`, `M_1(y)!=0` for every real `y!=0`.

The baseline output Bartlett spectrum is strictly positive, so the information inequality from one long-window Fourier statistic gives

`G_1(omega)>=L_1(omega*tau)>0`

for every nonzero frequency.

Thus the complete record necessarily has positive local Fisher information at every nonzero temporal frequency.

The exact renewal-transition-score representation

`G_rho(omega)=exp(-rho) E|A_D(omega)|^2`

also gives the high-frequency limit

`lim_|omega|->infinity G_rho(omega)=exp(-rho)`.

At paralysis this is `1/e`.

No fatal defect was found in the lower-bound or high-frequency logic.

## 4.2 Mandatory notation repair

WP07 predates WP17 and sometimes writes a primitive infinite sinusoid and `G(0)` too casually.

The manuscript must distinguish:

- `G_DC`: stationary homogeneous/static FI retention rate;
- `G(omega)`: the model-specific continuous/narrowband spectral representative for nonzero-frequency waveform limits.

Recommended statement at the deterministic paralysis point:

`G_DC=0`,

while the model-specific continuous Fisher spectrum satisfies

`G(omega)>0` for every `omega!=0`.

For this deterministic model, continuity at zero can be proved directly from the exact interval-score representation because the geometric cluster size has finite moments; the complex transition score tends in `L2` to the uniform-rate transition score, which is zero at `rho=1`. Thus the continuous representative may be chosen with

`lim_{omega->0}G(omega)=0`.

However, this continuity is **model-specific** and must not be attributed to WP10's universal theorem.

Pure sinusoids should be described as long-window/narrowband limits, consistent with WP17.

## 4.3 Novelty pressure

Very close classical prior art exists:

- Teich & Vannucci (1978), JOSA 68, 1338, derive paralyzable dead-time photocount distributions for modulated laser radiation;
- Vannucci & Teich (1978), Optics Communications 25, 267, analyze time-varying rates and dead-time-modified mean/variance for nonparalyzable counters;
- extensive older counter theory gives Type-II count, renewal, and spectral statistics;
- modern detector literature uses CRLB/SNR under pileup/dead time;
- neural renewal/refractory literature studies timing FI and rate-vs-timing information.

No searched source states the exact complete-timestamp Fisher-spectrum phenomenon

`static complete-record blindness at the Type-II maximum + positive local FI at every nonzero frequency + exact high-frequency complete-record residue 1/e`.

No priority claim is certified, but WP07 remains a credible specific novelty result.

---

# 5. WP25 hostile proof review

## 5.1 Regularity-free bounded-statistic theorem

For arbitrary iid recovery `T` with only finite positive mean `m`, at `lambda=1/m`,

`dot phi_s=W_s/(1+u_s)^2`,

where `phi_s=E[exp(-sD)]`.

For nondegenerate recovery, `W_s>0` for every `s>0`.

This proof uses only:

- the classical busy-cycle renewal density;
- finite mean `m`;
- dominated differentiation under exponential weighting;
- positivity of the stop-loss overlap.

No DQM or density assumption is needed.

This result is robust.

## 5.2 Stopped-cycle DQM/FI

Palm-initialize at a registered cluster start. The future marked-Poisson path stopped at the next cluster start has fractional-rate score

`S_cyc=N_D-lambda D`.

Finite mean recovery implies `E[D]=1/r<infinity`.

The compensated-Poisson stopped isometry yields

`E[S_cyc^2]=lambda E[D]=lambda/r`.

The observed interval is a statistic, giving

`I_D<=lambda/r`.

### Hostile concern checked

For arbitrary heavy tails, one must not justify unbounded stopping merely by an informal optional-stopping sentence. The manuscript should state the localization argument explicitly:

1. use `D_K=D wedge K`, for which ordinary counting-process DQM is standard;
2. the stopped scores satisfy
   
   `E[(M_D-M_DK)^2]=lambda E[D-D_K] ->0`;
3. use standard stopped counting-process likelihood/Hellinger localization to pass DQM from `D_K` to `D`.

This requires only `E[D]<infinity`.

A theorem-grade counting-process likelihood citation should accompany this step.

This is a **proof-presentation obligation**, not a detected counterexample.

---

# 6. WP26 hostile proof review

## 6.1 Ordinary renewal bulk information

For one DQM interval law, progressive censoring `C_t(D)` has score

`E[a(D)|C_t(D)]`

and information `J(t)` increasing to `I_D` by `L2` martingale convergence.

An ordinary renewal experiment started at a renewal decomposes into sequential censored intervals with orthogonal score increments:

`I_ord(t)=E sum 1{S_{n-1}<=t} J(t-S_{n-1})`.

Using `J<=I_D`, `J(t)->I_D`, and the elementary renewal theorem gives

`I_ord(t)/t -> I_D/E[D]=rI_D`.

No second moment is needed.

No defect found.

## 6.2 Stationary Type-II boundary

At an arbitrary stationary time, the only pre-zero incident events capable of affecting the future detector state are the recovery intervals still active at zero:

`A_0={(s,T):s<=0<s+T}`.

This is a finite Poisson cloud with total mean measure

`lambda E[T]=lambda m`.

For the fractional rate parameter its latent FI is therefore `lambda m`.

Conditional on this cloud, future evolution up to the first registered event is driven by a fresh marked Poisson process. For `tau_L=min(Y,L)`, the stopped future score has conditional variance `lambda E[tau_L|A_0]` and zero conditional mean. Hence

`I(C_L(Y)) <= lambda m + lambda E[min(Y,L)]`.

Because the Type-II process generated from a stationary Poisson input with finite mean recovery is ergodic and has positive registered rate `r`, `Y<infinity` a.s.; therefore

`E[min(Y,L)]/L ->0`.

The left-boundary FI is sublinear even if `E[Y]=infinity`.

Conditional on a first registered event at time `Y<L`, the future is a fresh ordinary renewal process. Chain rule gives

`I_stat(L)=I(C_L(Y))+E[1{Y<L}I_ord(L-Y)]`.

The second term has rate `rI_D`, so

`I_stat(L)/L -> rI_D`.

No fatal defect found.

### Mandatory detail to add in manuscript

Do not assert `Y<infinity` merely from “positive intensity.” State the actual model reason: the stationary marked-Poisson `M/G/infinity` process is ergodic for finite mean service/recovery, its empty-state probability is `exp(-lambda m)>0`, and cluster starts therefore recur almost surely. This makes the proper-forward-recurrence step explicit.

## 6.3 Prior-art boundary

Zhao & Nagaraja (2011) already prove the generic window-censored renewal asymptotic `I_window/L -> I_D/E[D]` under regularity including finite FRT FI.

Dvurecenskij & Ososkov (1985), *On a modified counter with prolonging dead time*, Journal of Applied Probability 22, 678–687, derive cycle Laplace transforms for a broad class of prolonging-dead-time counters with random impulse lengths.

Therefore do not claim:

- first cycle transform for random Type-II recovery;
- first renewal-window FI asymptotic;
- first heavy-tail renewal theorem in general.

The project-specific theorem is the Type-II information consequence and the use of its finite stationary marked-Poisson boundary state to remove the generic FRT regularity caveat within this detector class.

---

# 7. WP19 hostile review

The analytic no-go construction remains useful and logically independent of the exact numerical full-FI values.

Two recovery laws share exactly

`E[T]=1`, `Var(T)=1/4`, `CV=0.5`

and hence the entire conventional count-rate curve

`r(lambda)=lambda exp(-lambda)`.

Yet the common coarse-graining `Z=1{D<=2/5}` is constant for law A and parameter-sensitive for law B, proving that the information experiments differ.

Thus no numerical solver is needed for the fundamental claim:

`mean + variance + conventional saturation curve are not resource-complete`.

The ~8.78% difference in full static FI is supporting calibration only.

No defect found.

---

# 8. Important novelty downgrade for WP25/WP26

The exact random-recovery pair-correlation formula from older paralyzable-counting literature already implies that a nondegenerate recovery law generically changes second-order output structure with `lambda` even at the mean-count maximum.

Thus, once ordinary statistical regularity is granted, the **qualitative fact that random recovery can preserve information where the mean slope is zero is not mathematically mysterious**.

The value of WP25/WP26 is stronger and should be stated precisely:

1. a sharp **iff** characterization at the universal count maximum;
2. validity for every finite-mean recovery distribution, including singular/heavy-tailed laws;
3. a complete stationary timestamp Fisher-rate statement, not merely a pair-correlation observation;
4. explicit bounded-statistic lower witnesses;
5. connection to WP07's dynamic spectral escape and WP19's resource incompleteness.

This should prevent overselling the result as a profound new queueing identity.

---

# 9. Richer-observation prior art that must be cited

Barat, Dautremer & Trigano (2006), *Nonparametric Bayesian Estimation of Censored Counter Intensity from the Indicator Data*, explicitly treat Type-I and Type-II dead-time intensity inference in a multiplicative-intensity framework while observing both the recorded counting process and the idle/dead indicator process.

For Type II they note that the censoring component is informative; their practical inference uses a partial-likelihood approximation rather than the full informative censoring likelihood.

This is important close inference prior art but does not preempt the present **timestamp-only complete-record** Fisher theorems because their observation is richer and their target/method is different.

---

# 10. Experiment/notation consistency

Three objects must remain distinct in the manuscript.

## 10.1 General waveform spectrum

`G(omega)`:

- an a.e. `L^infinity` multiplier from WP10;
- meaningful operationally through finite-energy/narrowband waveform limits;
- no universal point value at zero and no universal continuity.

## 10.2 Palm-cycle static retention

`G_cyc=(r/lambda)I_D`:

- one regenerative interval/cycle;
- exactly defined in the iid Type-II recovery class.

## 10.3 Stationary homogeneous static retention

`G_DC=lim I_stat(L)/(lambda L)`:

- long stationary timestamp window;
- WP26 proves `G_DC=G_cyc` for every finite-mean iid Type-II recovery law.

For a model where the waveform spectrum has a continuous representative at zero, one may additionally identify

`lim_{omega->0}G(omega)=G_DC`,

but this is model-specific and should be proved where used.

This separation eliminates the largest remaining notation vulnerability.

---

# 11. Coherence/significance review

The results do form one coherent resource-theory story.

The paper should **not** be framed as “a collection of dead-time formulas.”

The central question is:

> What information about a weak temporal optical waveform survives a detector with arbitrary autonomous memory, and why can conventional scalar detector summaries fail completely?

The logical progression is:

1. **General completeness theorem:** autonomy forces a complete local Fisher spectrum for any classical Poisson detector channel.
2. **Deterministic Type-II counterexample to scalar intuition:** at the familiar count-rate maximum the complete static experiment is blind, yet every nonzero temporal frequency remains informative.
3. **Recovery shape as hidden information resource:** all equal-mean recovery laws share the same conventional saturation curve, but deterministic recovery is uniquely Fisher-singular; any randomness restores static timestamp information.
4. **Finite-summary no-go:** even adding recovery variance/CV does not determine the information channel.
5. **Structural interpretation:** information is carried by the full trajectory channel; atomic timing paths and recovery-shape structure are invisible to simple count-rate or timing-width summaries.

That is a genuine resource-theory narrative.

---

# 12. Recommended manuscript claims

Safe lead claims:

1. **Autonomous-channel spectral completeness:** local waveform FI of any parameter-independent autonomous classical Poisson photodetector is completely represented by a bounded Fisher-retention spectrum.
2. **Type-II spectral escape:** deterministic paralyzable detection at its count-rate maximum is statically Fisher-blind but retains positive complete-record information at every nonzero temporal frequency, with exact high-frequency retention `1/e`.
3. **Finite-mean recovery singularity:** within the iid random-recovery Type-II class, deterministic recovery is the unique finite-mean recovery law with zero complete stationary static FI at the common mean-count maximum.
4. **Resource incompleteness:** recovery mean and variance, even together with the full conventional mean saturation curve, do not determine the timestamp information experiment.

Avoid:

- “first information theory of dead time”;
- “first Type-II inference theorem”;
- “first queue-output identifiability result”;
- “new renewal spectrum”;
- “new cycle transform”;
- “noise helps”;
- generic Blackwell dominance;
- all-photodetector / quantum-universal speed-limit language.

---

# 13. Manuscript threshold decision

The earlier rule was not to draft until at least one organizing theorem and one substantial Type-II theorem survived hostile proof and novelty review.

That condition is now met:

- WP10/WP17 supplies the organizing theorem;
- WP07 supplies a concrete dynamic Type-II information phenomenon;
- WP25/WP26 supplies a class-wide static singularity theorem with only finite mean recovery;
- WP19 supplies an exact resource-completeness no-go.

The prior-art audits have materially narrowed, not destroyed, the candidate claims.

`boxed: PAPER 2 HAS EARNED MANUSCRIPT DRAFTING.`

Next action should be **architecture first**, not immediate prose sprawl:

1. define one central thesis/title;
2. choose theorem order and what moves to appendices;
3. write a one-page claim/novelty matrix against the close literature;
4. only then begin LaTeX manuscript source;
5. preserve all existing work packages as provenance and proof notes.

---

# 14. Mandatory repairs before/during drafting

1. Rewrite WP07 manuscript notation around `G_DC` versus continuous `G(omega)` and wavepacket/narrowband frequency interpretation.
2. Give a theorem-grade stopped-counting-process DQM/localization citation for WP25 rather than leaving the unbounded-stop passage informal.
3. In WP26 explicitly justify proper `Y` via ergodicity/positive empty probability of stationary `M/G/infinity`, not generic positive intensity.
4. Cite Zhao–Nagaraja as generic window-FI prior art with stronger FRT assumptions.
5. Cite Dvurecenskij–Ososkov 1985 for broad random prolonging-dead-time cycle transforms.
6. Cite Barat–Dautremer–Trigano 2006 as close Type-II intensity-inference work using a richer idle/dead indicator observation.
7. Keep Afanaseva–Mikhailova 1973 historical uncertainty visible in internal provenance; do not write priority language that depends on ruling it out.

These are drafting requirements, not reasons to delay the manuscript architecture step.
