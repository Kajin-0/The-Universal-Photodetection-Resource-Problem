# WP21 — Historical inverse-output / identifiability audit for generalized Type-II recovery

**Status:** hostile prior-art audit. This note materially narrows the novelty posture of WP13/WP18. It does **not** invalidate the deterministic-recovery Fisher-singularity theorem, but it establishes that broad claims about output-flow identifiability, recovering queue characteristics from output observations, or structural information in queue outputs were already an active literature by the mid-1960s to mid-1970s.

**Date:** 2026-08-21

---

## 1. Why this audit was necessary

WP13/WP18 derived a class-wide result for iid Type-II recovery at the common mean-count saturation maximum `lambda*m=1`:

`G_DC = 0 iff T=m a.s.`

under the stated renewal-DQM / finite-Fisher-rate regularity.

A related corollary says that, for a fixed known recovery law and two distinct incident rates lying on the two equal-output-rate branches of

`r(lambda)=lambda exp(-lambda m)`, 

identical complete stationary registered-timestamp laws occur iff recovery is deterministic.

The theorem itself is about a very specific observable and local-information singularity. However, earlier repository language risked implying a broader novelty claim about recovering hidden queue/recovery characteristics from output flow. That broad claim is unsafe.

---

## 2. The 1973 Afanaseva–Mikhailova blocker is real and directly in the Type-II lineage

The exact bibliographic record is now confirmed from multiple independent sources.

L. G. Afanaseva and I. V. Mikhailova,

**“О восстановлениии характеристик некоторых систем массового обслуживания по выходящему потоку”**

(approximately: *On recovering characteristics of some queueing systems from the output flow*),

`Trudy matematicheskogo fakul'teta Voronezhskogo gosudarstvennogo universiteta`, issue 9 (1973), pp. 132–138.

Identifiers exposed by DML-CZ/EUDML:

- MR `0436667`
- Zbl `1221.53041`

This is not merely a title found in an unrelated bibliography. Dvurecenskij & Ososkov, **“Note on type II counter problem”**, Aplikace matematiky 29 (1984), 237–249, explicitly cite Afanaseva–Mikhailova [1,2] among the authors who studied the **Poisson primary-process Type-II inter-registration problem**.

Their review passage states that the Type-II secondary process consists of registered-event intervals `Z_j`, asks for their distribution `G`, and then lists Takacs, Pollaczek, Smith, Sankaranarayanan, Albert & Nelson, and **Afanaseva & Michajlova [1,2]** as authors treating the Poisson case.

Therefore Afanaseva–Mikhailova (1973) is a **direct historical risk** for any claim about inverse recovery from the Type-II registered-event interval law.

A readable copy of the 1973 paper has still not been located. Absence of online full text is not evidence of novelty.

---

## 3. More important: inverse-output identifiability was already a recognized research topic before 1973

D. J. Daley’s 1976 review,

**“Queueing output processes,”** Advances in Applied Probability 8, 395–415 (1976), DOI `10.2307/1425911`,

states in its abstract that the final topic is **identifiability** and characterization of queueing systems from properties of the output process. Its bibliography contains an extensive inverse-output literature.

The following items are especially relevant.

### 3.1 Kovalenko 1965

I. N. Kovalenko,

**“The recovery of the characteristics of a system from observations on the output flow,”** Dokl. Akad. Nauk SSSR 164 (1965), 979–981; English translation: Soviet Math. 6 (1965), 1328–1331.

This title alone establishes that inverse recovery of queue/system characteristics from output-flow observations predates WP13 by six decades.

The exact model and observable still need theorem-level inspection before deciding whether it overlaps the generalized Type-II cluster-start model.

### 3.2 Kendall & Lewis 1965

D. G. Kendall and T. Lewis,

**“On the structural information contained in the output of GI/G/infinity,”** Z. Wahrscheinlichkeitstheorie 4 (1965), 144–148.

This is another explicit structural-identifiability result for infinite-server queues. The observation regime is not automatically the same as our registered busy-cluster-start process, so it does not directly preempt WP18, but it makes any broad “output law contains hidden recovery information” framing historical rather than novel.

### 3.3 Ivnitskii 1969

V. A. Ivnitskii,

**“Recovery of characteristics of single-server systems with constraints on the duration of presence from observations on the output flow,”** Izv. Akad. Nauk SSSR, Tekhn. Kibernet. 1969 no. 3, 60–65; English translation: Engineering Cybernetics 1969 no. 3, 52–56.

This is a particularly strong warning against broad inverse-output novelty language. It is an explicit recovery theorem from output-flow observations.

Again, it is a single-server restricted-sojourn model, not obviously the iid Type-II cluster-start process.

### 3.4 Milne 1970

R. K. Milne (with A. J. Stam in accessible abstracts),

**“Identifiability for random translations of Poisson processes,”** Z. Wahrscheinlichkeitstheorie 15 (1970), 195–201.

Accessible abstract: the random displacement distribution is identifiable when the original Poisson realization and the displaced realization are both observed, even without linkage between individual points.

This is closely related to timing-channel identifiability in spirit, but the observation is richer than the Type-II output-only cluster-start record.

### 3.5 Ross 1970

S. M. Ross,

**“Identifiability in GI/G/k queues,”** Journal of Applied Probability 7 (1970), 776–780, DOI `10.2307/3211956`.

The accessible technical-report abstract states that arrival and service distributions are identifiable from the complete queue-size path `C(t)` under specified regularity conditions. This is a much richer observation than our output-timestamp-only record, so it is not a direct preemption.

### 3.6 Brown 1970 / George & Agrawal 1973

M. Brown,

**“An M/G/infinity estimation problem,”** Ann. Math. Statist. 41 (1970), 651–654,

and L. L. George & A. C. Agrawal,

**“Estimation of a hidden service distribution of an M/G/infinity system,”** Naval Research Logistics Quarterly 20 (1973), 549–555,

are explicit service-distribution inference results.

The latter uses departure/output times from repeated systems starting empty. It therefore does not observe the same stationary busy-cluster-start record as WP18, but it confirms that hidden service/recovery-shape inference from queue outputs is old prior art.

### 3.7 Shanbhag 1973

D. N. Shanbhag,

**“Characterization for the queueing system M/G/infinity,”** Proc. Cambridge Philos. Soc. 74 (1973), 141–143, DOI `10.1017/S0305004100047897`.

This is another characterization result in the immediate infinite-server queue family. Accessible extract does not expose enough detail to assess overlap with cluster-start-only identifiability.

---

## 4. What the 1984 Type-II paper tells us about the 1973 Afanaseva–Mikhailova scope

Dvurecenskij & Ososkov define a Type-II counter with prolonging dead time, registered particle indices `n_j`, and recurrent registered-event spacings

`Z_j = T_{n_j} - T_{n_{j-1}}`.

They state that the main problem is to determine the distribution `G(x)=P(Z_j<x)` or its Laplace transform.

They then explicitly say the Poisson primary-process case was discussed by Takacs, Pollaczek, Smith, Sankaranarayanan, Albert & Nelson, and **Afanaseva and Michajlova [1,2]**.

This is strong evidence that the inaccessible 1973 paper concerns essentially the same **registered-event interval law** that underlies WP13.

What it does **not** establish is that Afanaseva–Mikhailova proved the specific Fisher-information statement

`G_DC=0 iff T deterministic`

at `lambda*m=1`, or the exact fixed-recovery-law equal-branch full-law equivalence iff deterministic.

Therefore the 1973 paper remains a blocker for priority confidence, not a demonstrated preemption of WP18.

---

## 5. Revised novelty boundary

### Definitely old / do not claim

Do not claim novelty for any of the following:

1. recovering hidden queue/system characteristics from output-flow observations in general;
2. queue-output identifiability as a research topic;
3. structural information being contained in a queue output process;
4. hidden service/recovery-distribution inference from queue observations;
5. identifying random displacement laws of Poisson processes under richer input/output observations;
6. Type-II registered-interval analysis for random prolonging dead times;
7. the classical generalized Type-II / `M/G/infinity` busy-cycle renewal formulas;
8. the random-paralyzable pair-correlation identity already demoted in WP16.

### Still a candidate contribution

The historically sharper candidate is now:

> **At the universal mean-count maximum `lambda*m=1`, deterministic iid recovery is the unique regular Type-II recovery law for which the complete registered-cluster-start timestamp experiment has zero static Fisher information for a fractional source-rate tangent.**

Equivalently, under the WP18 regularity:

`G_DC=0 iff T=m a.s.`

This is a **local information-singularity / extremal theorem**, not a generic output-identifiability theorem.

The related full-law branch aliasing statement should be treated as a corollary unless the 1973 source can be ruled out:

> for a fixed known recovery law, distinct equal-mean-output-rate incident-rate branches generate identical stationary registered timestamp laws iff recovery is deterministic.

Because pair-correlation already distinguishes every nondegenerate fixed law at an overlap lag, this global corollary is mathematically easy once the classical pair-correlation formula is admitted. Its novelty weight is correspondingly lower than the Fisher singularity itself.

---

## 6. Impact on Paper-2 architecture

The audit **lowers the novelty weight of WP13’s identifiability language** but does not weaken the mathematics of the Fisher theorem.

Recommended hierarchy after this audit:

1. **WP10/WP17** — general autonomous-channel Fisher-spectrum synthesis and local waveform ordering.
2. **WP07** — complete-record continuous Type-II spectral survival at deterministic paralysis.
3. **WP18** — deterministic recovery as unique static Fisher singularity at the common Type-II count maximum.
4. **WP20** — exact-timestamp zero-lag covariance atom fixes high-frequency Cesaro Fisher residue.
5. **WP19** — mean + variance/CV + mean saturation curve are insufficient to determine the information channel.
6. Full-law branch aliasing and pair-correlation inversion — supporting corollaries only.

This is a cleaner and safer manuscript architecture than centering Paper 2 on generic recovery identifiability.

---

## 7. Remaining historical tasks

1. Obtain or inspect the actual theorem text of Afanaseva & Mikhailova (1973), pp. 132–138, if realistically possible.
2. Inspect Kovalenko (1965) Soviet Math. 6, 1328–1331 for its exact model/observable.
3. Inspect the identifiability section of Daley (1976) if a full readable copy can be obtained; its abstract and bibliography confirm the field but not theorem details.
4. Search citations to Afanaseva–Mikhailova (1973) beyond Dvurecenskij & Ososkov to infer whether their inverse result reconstructs the service/recovery law from the registered-interval distribution.
5. Keep **all priority language disabled** until these checks are exhausted.

---

## 8. Current conclusion

The hostile audit did **not** find a source that explicitly states the WP18 Fisher singularity theorem.

However, it did show that the surrounding inverse-output-identifiability territory is heavily occupied by classical work beginning at least in 1965. Therefore Paper 2 must not present the result as a new generic identifiability principle.

The defensible candidate is narrower and more interesting from the present resource-theory perspective:

`deterministic recovery = unique zero-static-Fisher boundary at the universal Type-II saturation maximum`,

with the dynamic spectral escape of WP07 and high-frequency visible-event residue of WP20 providing the genuinely information-theoretic structure around that singularity.
