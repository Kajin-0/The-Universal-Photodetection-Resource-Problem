# WP03 — Prior-Art and Novelty Audit for the General-Channel Program

**Status:** initial hostile audit. Conclusion: the statistical ingredients are old; the photodetection-specific stationary spectral theorem remains a plausible novelty target but is **not yet certified novel**.

## 1. Standard mathematics we must treat as prior art

### Output score as conditional expectation

For a differentiable statistical experiment passed through a statistic / parameter-independent Markov channel, the output score is the conditional expectation of the input score given the retained observation. This is standard.

A concise modern pointer is David Pollard's notes *Sufficiency and the preservation of Fisher Information*, which explicitly writes the induced score as the conditional expectation of the original score under DQM and cites Ibragimov & Has'minskii, van der Vaart, Le Cam & Yang, and Bickel et al.

**Novelty consequence:** Paper 2 cannot claim to discover `score_out = E(score_in|Y)` or the corresponding scalar Fisher data-processing inequality.

### Fisher monotonicity under Markov morphisms

Ay, Jost, Lê, and Schwachhöfer, *Information geometry and sufficient statistics*, Probability Theory and Related Fields 162, 327–364 (2015), DOI `10.1007/s00440-014-0574-8`, develops Markov morphisms for statistical models and obtains Fisher monotonicity in a general information-geometric framework.

Chentsov/Amari information geometry also makes Fisher monotonicity/invariance under sufficient statistics foundational prior art.

**Novelty consequence:** positive contraction of local Fisher information under stochastic processing is not new.

### Translation-invariant bounded operators as Fourier multipliers

This is standard harmonic analysis. A conventional reference is Stein and Weiss, *Introduction to Fourier Analysis on Euclidean Spaces*, Chapter I, theorem on bounded translation-invariant `L^2` operators; Grafakos' *Classical Fourier Analysis* also treats operators commuting with translations.

**Novelty consequence:** "commutes with translations therefore is a multiplier" is a proof tool, not the contribution.

---

## 2. Nearby stationary-process Fisher literature

There is extensive literature on Fisher information matrices/rates of stationary Gaussian and ARMA/VARMAX processes, Whittle-type frequency-domain formulas, and Fisher information of correlated stochastic processes.

Examples found in the initial search include:

- Klein, *Matrix Algebraic Properties of the Fisher Information Matrix of Stationary Processes*, Entropy 16, 2023–2055 (2014), DOI `10.3390/e16042023`.
- Klein and Spreij, *Matrix differential calculus applied to multiple stationary time series and an extended Whittle formula for information matrices*, Linear Algebra Appl. 430, 674–691 (2009), DOI `10.1016/j.laa.2008.09.019`.
- Radaelli, Landi, Modi, and Binder, *Fisher information of correlated stochastic processes* (2022 preprint / later literature to verify), studying parameter FI scaling in memoryful processes.

These works concern FI **of parametric stochastic-process models**, often for parameters in the process dynamics/spectrum. They are not obviously the same as the proposed problem:

> a fixed stationary source tangent space is passed through an arbitrary photodetector channel, and the detector's retained local waveform FI is characterized as a positive contraction / spectral multiplier on source perturbations.

This distinction needs a full literature review before any priority claim.

---

## 3. Existing high-flux / dead-time photodetection literature

High-flux photodetection and dead-time effects are already modeled extensively, especially in TCSPC and LiDAR.

Important examples:

### Rapp et al., high-flux single-photon lidar

*High-flux single-photon lidar*, Optica (2021), DOI `10.1364/OPTICA.403190`.

This work models sequences of high-flux detection times as a Markov chain to account for detector/electronics dead time and demonstrates that high-flux measurements can be exploited rather than discarded.

Its reference chain includes earlier pile-up/dead-time compensation literature and Markov modeling.

### Wu et al., dead-time CRLB

*Performance Bounds of Ranging Precision in SPAD-Based dToF LiDAR*, Sensors 25, 6184 (2025), DOI `10.3390/s25196184`.

This derives Cramér–Rao bounds for specific dToF architectures with dead time and photon-number resolution and shows that pile-up reduces per-bin information and introduces parameter coupling.

### Other dead-time work

There are specific dead-time compensation/coding and SPAD ranging papers, including Rapp et al. on dead-time compensation and later synchronous/multi-trigger architectures.

**Novelty consequence:** Paper 2 cannot claim that Fisher information with dead time, Markov detector memory, or high-flux SPAD modeling is itself new.

The candidate distinction is a detector-model-independent theorem that **every autonomous channel driven by the same weak Poisson waveform tangent admits a complete source-normalized Fisher multiplier**, with exact pointwise ordering and data processing.

---

## 4. What appears potentially new

The following combination was not located in the first-pass search:

1. arbitrary parameter-independent stochastic detector channel from full incident photon trajectory to full detector record;
2. no independent-event, low-flux, dead-time form, finite-state form, or particular detector architecture assumed;
3. complete local weak temporal source tangent space of stationary Poisson intensity modulations;
4. detector information represented by a positive contraction operator on that source tangent space;
5. autonomy forces the operator to commute with temporal shifts;
6. multiplicity-one temporal representation forces exact scalar Fourier diagonalization;
7. `0 <= G_Phi0(omega) <= 1` a.e.;
8. pointwise `G_A >= G_B` iff universal local weak-waveform Fisher dominance at that operating flux;
9. arbitrary autonomous record coarse-graining gives **pointwise frequency-by-frequency** data processing;
10. Paper 1's marked-delay formula is recovered as an exact soluble special case.

The high-level message would be:

> **spectral completeness is symmetry-driven, not independent-event-driven.**

That is the candidate conceptual breakthrough.

---

## 5. Strongest current novelty claim we may eventually make — provisional only

A defensible eventual claim, if the audit continues to find no predecessor, would be approximately:

> We derive a complete local temporal Fisher-transfer spectrum for arbitrary autonomous classical photodetection channels driven by weak Poisson intensity perturbations, without assuming independent detection events or low flux. The result follows from a general score-projection operator plus time-translation symmetry, yields necessary-and-sufficient pointwise detector ordering and pointwise data-processing laws, and reduces exactly to the marked-delay spectrum of the independent-event theory.

Do not use "first" until a much deeper search is complete.

---

## 6. Claims that are already unsafe

Do **not** claim:

- first Fisher-information data-processing theorem;
- first conditional-score representation;
- first Fisher operator on a tangent space;
- first translation-invariant spectral representation;
- first FI analysis of detector dead time;
- first high-flux photodetection information theory;
- generic Blackwell dominance;
- a theorem for nonclassical optical states;
- a theorem for arbitrary coherent/phase-sensitive measurements;
- a universal all-detector scalar speed limit.

---

## 7. Literature searches still required

Before publication-level novelty can be asserted, search specifically for:

1. local asymptotic comparison of statistical experiments under stationary channels;
2. Fisher contraction operators / canonical correlations of score spaces;
3. frequency-resolved Fisher data processing for stationary input-output channels;
4. arbitrary hidden-Markov sensor channels with waveform perturbations;
5. point-process LAN/DQM under thinning, dead time, and nonlinear observation channels;
6. system-identification literature where Fisher information operators are diagonalized by temporal stationarity;
7. neural/spike-train information transfer using Fisher kernels or coherence;
8. quantum continuous-measurement analogues that may already formulate an operator-level local information spectrum.

---

## 8. Current verdict

**Promising enough to proceed.**

The general score-projection operator is not the breakthrough. The research value rests on whether the symmetry theorem yields a genuinely new architecture-independent photodetection result and whether we can extract nontrivial consequences beyond restating standard `L^2` multiplier theory.

The next decisive work package should therefore be an explicit **history-dependent detector example**—preferably a nonparalyzable dead-time or finite-state recovery model—to calculate or bound `G_Phi0(omega)` and demonstrate behavior impossible in Paper 1's flux-independent delay-kernel class.
