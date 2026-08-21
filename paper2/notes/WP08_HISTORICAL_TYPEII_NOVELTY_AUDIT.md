# WP08 — Hostile Historical Novelty Audit: Modulated and Paralyzable Dead-Time Counting

**Status:** major historical prior art found and incorporated. The Paper-2 Type-II result remains potentially novel, but only under a sharply narrowed claim. Any statement that modulation, information theory, likelihood methods, or paralyzable dead-time statistics are themselves new is false.

## 1. Why this audit was necessary

WP06 and WP07 show striking temporal Fisher spectra for hidden-state / paralyzable dead time. Before treating those results as a breakthrough, we must compare against the older photon-counting literature, which was already sophisticated about:

- periodically modulated Poisson radiation;
- paralyzable and nonparalyzable counters;
- dead-time-modified counting distributions;
- likelihood-ratio detection;
- mutual information / channel capacity;
- rate variation during a counting window;
- count-rate contrast inversion near paralysis.

The audit found several directly relevant predecessors.

---

## 2. Teich & Vannucci 1978 — modulated radiation **with paralyzable dead time**

M. C. Teich and G. Vannucci,

**“Observation of dead-time-modified photocounting distributions for modulated laser radiation,”**
*Journal of the Optical Society of America* **68**, 1338–1342 (1978),
DOI `10.1364/JOSA.68.001338`.

This is critical prior art.

The paper explicitly states that it obtains a new expression for the counting distribution in the presence of **modulation and paralyzable dead time**. It treats triangular and sinusoidal modulation and distinguishes nonparalyzable from paralyzable counters.

The relevant scope of its paralyzable result is, however, materially different from WP07:

1. the observable is the **number of counts in a fixed sampling interval**, not the complete output timestamp record;
2. the modulation treatment used for the paralyzable result assumes a short sampling time relative to source fluctuation / modulation time (`T << T_M` or coherence time);
3. the method averages a constant-intensity paralyzable counting distribution over the integrated-intensity random variable `W`;
4. it does not formulate a complete local temporal Fisher operator or frequency-resolved FI retention spectrum;
5. it does not derive the paralysis-point statement `G(0)=0` together with finite-frequency complete-record FI recovery and a high-frequency plateau.

The paper itself says the averaging operation is valid only when intensity is virtually constant during the sampling interval; it explicitly notes that appreciable rate variation during a sampling time requires a different treatment.

### Novelty consequence

We **must not** say that Paper 2 is the first treatment of periodically modulated photon counting under paralyzable dead time.

The candidate novelty is instead the complete-timestamp local Fisher spectrum and its exact spectral consequences.

---

## 3. Vannucci & Teich 1978 — rate variation matters during dead time

G. Vannucci and M. C. Teich,

**“Effects of rate variation on the counting statistics of dead-time-modified Poisson processes,”**
*Optics Communications* **25**, 267–272 (1978),
DOI `10.1016/0030-4018(78)90322-X`.

This paper derives mean and variance of counts in a fixed sampling interval for a **nonparalyzable** dead-time counter driven by a Poisson rate that is a known function of time. It explicitly shows that the detailed rate variation during the sample matters once dead time is present; integrated energy alone no longer determines the count statistics.

### Novelty consequence

We cannot claim to discover that dead time makes detector performance depend on temporal waveform shape or on rate variation within a measurement window.

What WP02/WP07 add, if novel, is the complete Fisher metric over the temporal tangent space and its architecture-independent spectral ordering, not the qualitative observation that time variation matters.

---

## 4. Teich & Cantor 1978 — information theory with dead time already exists

M. C. Teich and B. I. Cantor,

**“Information, Error, and Imaging in Deadtime-Perturbed Doubly Stochastic Poisson Counting Systems,”**
*IEEE Journal of Quantum Electronics* **QE-14**, 993–1003 (1978),
DOI `10.1109/JQE.1978.1069731`.

This work considers fixed **nonparalyzable** dead time and develops:

- likelihood-ratio detection;
- receiver-operating characteristics;
- probability of error;
- mutual information;
- channel capacity;
- maximum-likelihood image estimation;

for modulated / doubly stochastic Poisson counting systems.

Its receiver observable is principally the **count number in a fixed sample interval**, rather than the full output event trajectory. It does not supply the complete weak-waveform Fisher multiplier of an arbitrary autonomous detector channel.

### Novelty consequence

The following claims are prohibited:

- “first information-theoretic analysis of dead-time photodetection”;
- “first information theory of modulated detectors with dead time”;
- “first likelihood or channel-capacity treatment of dead-time photon counters.”

Those would be historically wrong.

---

## 5. Jorgensen & Johnson 2026 — modern LAN/FI theory for nonparalyzable dead time

F. J. N. Jorgensen and S. G. Johnson,

**“Fundamental Bounds and Efficient Estimation for Dead-Time-Constrained Event Detection, with Application to Single-Photon Lidar,”** arXiv:2605.23210 (2026).

They develop local asymptotic normality and Fisher-information rates for periodic binary detection with **nonparalyzable** dead time and arbitrary causal gating. They derive sufficient statistics, asymptotic bounds, MLE efficiency, and one-step estimators.

They explicitly list **paralyzable / Type-II dead time** as a future extension.

### Novelty consequence

WP04's flat nonparalyzable live-fraction result should be treated as a validation/corollary, not a priority claim. The Type-II branch remains the cleaner frontier.

---

## 6. Modern paralyzable-detector CRLB / contrast-inversion work

S. S. Hsieh and K. Iniewski,

**“Improving Paralysis Compensation in Photon Counting Detectors,”**
*IEEE Transactions on Medical Imaging* **40**, 3–11 (2021),
DOI `10.1109/TMI.2020.3019461`.

This work models paralyzable photon-counting detectors and evaluates material-decomposition variance using the Cramér–Rao lower bound. It reports sharp noise increases near the characteristic count rate due to **contrast inversion**, and studies compensation architectures.

There is also a broad recent literature on paralyzable count-rate models, pileup, energy-bin statistics, and CRLBs for specific imaging tasks.

### Novelty consequence

We cannot claim that Fisher information, CRLBs, paralysis, or local loss of static contrast near the characteristic count rate are new.

The WP07 distinction is that at the same classical paralysis point the **complete timestamp experiment is exactly DC-nonidentifiable but provably retains substantial finite-frequency temporal FI**.

This is a task/spectrum statement about the full event record, not a static material-decomposition or count-rate CRLB.

---

## 7. What survives the audit

The following combination was **not found** in the historical or modern search so far:

1. continuous-time ideal paralyzable / Type-II Poisson detector;
2. complete registered timestamp record rather than only sample counts / histograms;
3. weak arbitrary temporal intensity tangent;
4. source-normalized local Fisher transfer as a frequency-resolved quantity;
5. exact complete-record DC nonidentifiability at `lambda tau=1`;
6. rigorous proof that at `omega tau=pi` more than `0.5169` of incident temporal FI survives;
7. exact high-frequency limit `G -> exp(-lambda tau)`;
8. consequent theorem that the Fisher spectrum must overshoot its high-frequency plateau at finite frequency;
9. embedding of this example into a general arbitrary-autonomous-channel Fisher-spectrum theorem.

The discrete one-bin WP06 result is even more explicit: an exact closed-form complete-record Fisher spectrum with strict monotone rise from zero DC FI to `0.818663...` at Nyquist.

These are the candidate distinctive contributions.

---

## 8. Corrected priority language

Until a publication-level search is finished, use only language such as:

> We derive a complete-timestamp local temporal Fisher spectrum for an ideal Type-II detector and show a saturation-induced spectral inversion: the stationary detector can be locally blind to uniform intensity changes while retaining substantial information about finite-frequency modulation.

Do **not** use “first” or “previously unknown.”

If a priority sentence is eventually justified, it must be limited to the exact Fisher-spectrum theorem, not to dead-time modulation or information theory generally.

---

## 9. Especially important historical distinction

The 1978 Teich–Vannucci paralyzable-modulation result is not an enemy of Paper 2; correctly cited, it strengthens the motivation.

It establishes that sophisticated dead-time-modified **count distributions** for modulated radiation have existed for nearly fifty years. Paper 2 can then state a precise unresolved question:

> What does the **complete event-time record** retain about arbitrary weak temporal perturbations when hidden events control detector recovery?

That is a cleaner and historically honest problem than implying that modulation plus dead time was previously untreated.

---

## 10. Additional searches still required

Before manuscript drafting, search specifically for:

1. full-event-time likelihoods for Type-II/paralyzable counters with inhomogeneous Poisson inputs;
2. Fisher information rate of renewal / cluster-start processes under periodic rate modulation;
3. frequency-domain LAN of renewal point processes;
4. neural refractory-process Fisher information for sinusoidal stimuli;
5. spike-train Fisher kernels / information susceptibility under refractoriness;
6. point-process system identification using complete event-time records;
7. paralyzable detector communication-channel results with event timing rather than sample counts;
8. older nuclear-instrumentation literature on sinusoidally varying source rates and extended dead time.

---

## 11. Current verdict

**The Type-II program survives, but with substantially improved claim discipline.**

The historical search destroys any broad priority claim about modulation, information theory, or paralyzable statistics. It does **not** presently supply the specific complete-record temporal Fisher spectrum, the exact DC/finite-frequency inversion theorem, or the symmetry-based general-channel spectral framework.

Proceed, but keep the Paper-2 thesis centered on:

\[
\boxed{\text{complete temporal information under hidden detector memory}}
\]

rather than on dead time per se.
