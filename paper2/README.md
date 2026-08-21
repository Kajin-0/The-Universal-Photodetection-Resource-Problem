# Paper 2 — General Fisher-Channel Resource Theory for Photodetection

## Status

**Active theoretical research program.** Paper 1 / Rev11 is scientifically frozen by default and remains the preferred first-paper submission candidate. Paper 2 removes the independent-event restriction and studies complete local temporal Fisher transfer through arbitrary autonomous detector channels with memory and high-flux nonlinear dynamics.

For current recovery state, read first:

1. `notes/RESEARCH_LOG_ROUND03_WP13_WP20_CHECKPOINT.md`
2. `AGENTS_PAPER2.md`
3. `notes/WP20_CESARO_VISIBLE_EVENT_RESIDUE.md`
4. `notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
5. `notes/WP18_LAPLACE_PROOF_REPAIR_FOR_RECOVERY_SINGULARITY.md`
6. `notes/WP17_PUBLICATION_GRADE_WP10_FORMALIZATION.md`
7. `notes/WP16_HOSTILE_RANDOM_TYPEII_PRIOR_ART_AUDIT.md`

## Central question

For a stationary Poisson optical input passed through an arbitrary parameter-independent autonomous detector channel, what object exactly describes the local temporal Fisher information retained in the complete accessible detector record?

The target detector class may include dead time, saturation, recovery, afterpulsing, hidden states, state-dependent capture, multiple outputs per incident event, analog marks, and arbitrary high-flux history dependence.

## Organizing theorem — WP10/WP17

For homogeneous Poisson baseline flux `Phi0` and local waveform tangents `u`, the source score is

`S_u=int u(t)[N(dt)-Phi0 dt]`.

For any parameter-independent detector channel with accessible record `Y`, the output score is

`S_u^out=E[S_u|Y]`.

This defines a positive contraction `A_K` on the scalar temporal tangent space. Time-translation covariance implies `A_K` commutes with translations, so

`F_out[u,v]=Phi0/(2*pi) int G_{Phi0,K}(omega) U*(omega)V(omega)domega`,

with

`0<=G_{Phi0,K}(omega)<=1` a.e.

WP17 supplies the publication-grade route through standard-Borel trajectory spaces, stochastic-kernel randomization, DQM under statistics, the translation-invariant `L2` multiplier theorem, and narrowband wavepacket interpretation.

Paper 1 is recovered exactly as the independent marked-Poisson special case.

Candidate message:

> **Spectral completeness is symmetry-driven, not independent-event-driven.**

The abstract statistical/harmonic-analysis ingredients are prior art. Any contribution must lie in the photodetection-channel synthesis and detector-specific consequences.

## Strongest exact spectral example — continuous Type II

For deterministic paralyzable dead time `tau`, input rate `lambda`, and `rho=lambda*tau`, at the classical paralysis maximum `rho=1` the complete registered-timestamp process satisfies

`G_1(0)=0`,

`G_1(omega)>0` for every `omega!=0`,

`lim_|omega|->infty G_1(omega)=1/e`.

At `omega=pi/tau`,

`G_1>=exp(-1)(1+4/pi^2)=0.516975...`,

while independent complete-record Volterra numerics give approximately `0.52814`.

Thus complete static intensity information can vanish while dynamic temporal information survives at every nonzero frequency.

See `notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`.

## General iid Type-II recovery — Fisher singularity

For iid recovery duration `T` with finite mean `m`, every recovery law shares the same conventional mean curve

`r(lambda)=lambda exp(-lambda m)`.

Classical `M/G/infinity` theory also supplies the registered-event renewal density

`U_lambda(t)=lambda F(t) exp[-lambda A(t)]`,

`A(t)=E[min(T,t)]`.

These are prior art.

For the homogeneous fractional-rate experiment define the static FI retention per unit time `G_DC` separately from the a.e.-defined general spectral multiplier. Under renewal DQM/window regularity,

`G_DC=(r/lambda)I_D`.

At `lambda*m=1`, all count/rate FI vanishes. WP18 then uses bounded interval Laplace statistics to prove, under the stated regularity,

`G_DC=0 iff T=m almost surely`.

Thus deterministic recovery is the unique fixed-mean iid Type-II law that is completely static-Fisher-blind at the common mean-rate maximum.

A quantitative stop-loss witness is given in WP14/WP18.

## Mean and variance are not enough — WP19

WP19 gives two exact recovery laws with identical

`E[T]=1`, `Var(T)=1/4`, `CV=0.5`,

and therefore identical entire mean saturation curve `r(lambda)=lambda exp(-lambda)`, but different timestamp information channels.

A common interval coarse-graining has zero FI for one law and normalized per-time FI approximately `0.00443520488427` for the other at `lambda=1`.

Converged complete static FI values differ by about `8.78%`.

Therefore recovery mean plus variance/CV plus the conventional saturation curve are not resource-complete descriptors of timestamp information.

## Visible-event residue — WP20 supersedes WP08 as the robust theorem

For an exact-timestamp selector `Y<=N`, package the conditional source score into a stationary random measure with covariance

`Gamma_M=r delta_0+nu`.

If `nu` has finite total variation and no atom at zero, then the robust high-frequency result is

`lim_{Omega->infty} 1/[(b-a)Omega] int_{aOmega}^{bOmega} G(omega)domega = r/lambda`

for every fixed `0<a<b`.

If `nu` is atomless, Wiener's theorem yields high-frequency mean-square Cesaro convergence. If `nu` is Rajchman, e.g. has an `L1` density, then the stronger pointwise limit `G(omega)->r/lambda` follows.

Interpretation: exact visible timestamps contribute a zero-lag conditional-score covariance atom of weight `r`, fixing the high-frequency averaged Fisher residue independently of detailed detector memory.

## Major prior-art corrections

Do not claim novelty for:

- random Type-II/paralyzable recovery;
- `M/G/infinity` modeling, busy periods/cycles, or the classical renewal density above;
- random-paralyzable pair-correlation formulas;
- the identity `g_Y^(2)(t)=F(t)exp[lambda E[(T-t)_+]]`;
- pair-correlation dead-time inversion generally;
- infinite-server service/recovery inference generally;
- renewal-process FI or generic spike-timing-vs-rate FI ideas;
- conditional-score/Fisher data processing;
- function-valued FI operators;
- translation-invariant Fourier multipliers;
- stationary random-measure spectral theory/Wiener's theorem;
- dead-time information theory generally;
- modulated paralyzable photocounting generally.

WP15's pair-correlation result is operational/supporting, not a lead novelty theorem. Apanasovich & Paltsev (1995) already contain the equivalent random-paralyzable second-order formula.

## Historical novelty risk

Afanaseva & Mikhailova (1973), approximately `On recovering characteristics of some queueing systems from the output flow`, is cited in the direct Type-II lineage, but a readable theorem text has not yet been obtained. Older infinite-server output-identifiability literature also exists.

Therefore no `first`, `unprecedented`, or certified-priority language is allowed for the recovery-identifiability theorem.

No verified predecessor has yet been located for either:

- the fixed-recovery-law Fisher singularity `G_DC=0 iff T deterministic` at the universal Type-II mean-rate maximum;
- the WP07 complete-record dynamic escape from static blindness.

## Current novelty hierarchy

1. `WP10/WP17`: arbitrary-autonomous-channel local Fisher spectrum as a photodetection-channel synthesis.
2. `WP07`: continuous Type-II static blindness with positive information at every nonzero temporal frequency and residue `1/e`.
3. `WP18`: deterministic recovery as the unique regular static Fisher-singular fixed-mean iid Type-II recovery law.
4. `WP20`: visible-event zero-lag covariance-atom / high-frequency Cesaro residue theorem, pending targeted novelty audit.
5. `WP19`: exact resource no-go for recovery mean+variance sufficiency.

Supporting only: WP14 recovery-shape witness, rate/shape decomposition, WP15 pair-correlation inversion.

## Immediate gates

1. Finish the historical inverse-output audit, especially Afanaseva–Mikhailova and old Type-II/infinite-server identifiability literature.
2. Audit WP20 against dependent thinning, missing-event point-process inference, stationary score spectra, and information-spectrum literature.
3. Recheck WP18 renewal DQM and window-censoring assumptions for atomic and heavy-tailed recovery laws.
4. Only after these gates decide whether the WP10/WP07/WP18/WP20/WP19 stack has earned manuscript drafting.

## Documentation rule

Material results must be committed as they are obtained. Do not allow theorem status, proof repairs, prior-art collisions, numerical values used in arguments, or next-gate decisions to exist only in chat. Update a `WP*.md` or research log immediately, and synchronize `AGENTS_PAPER2.md` / `docs/CURRENT_RESEARCH_STATE.md` when the project-level state changes.
