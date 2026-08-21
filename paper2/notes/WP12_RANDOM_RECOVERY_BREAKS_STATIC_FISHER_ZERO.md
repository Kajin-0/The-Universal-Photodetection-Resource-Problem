# WP12 — Identical Paralysis Curves, Different Information: Random Recovery Breaks the Static Fisher Zero

**Status:** exact qualitative theorem with an asymptotic Fisher lower bound for exponential recovery. This isolates recovery-law shape as an information resource invisible to the ordinary mean count-rate curve. Prior-art search confirms random Type-II counter theory is classical; no priority claim yet for the Fisher contrast.

## 1. Generalized Type-II model

Let incident events form a homogeneous Poisson process of rate `lambda`.

Attach to every incident event time `S_i` an iid positive recovery/dead duration `T_i` with distribution `G` and finite mean

\[
\boxed{m=E[T].}
\]

Each event creates an active dead interval

\[
[S_i,S_i+T_i).
\]

The detector is live at time `t` iff no such interval covers `t`. An incident event is recorded exactly when it arrives while the detector is live.

Equivalently, the active dead intervals form a one-dimensional Poisson Boolean coverage process, or the customer population of an `M/G/infinity` system. Recorded events are starts of busy clusters.

For deterministic `T=m`, this reduces to the standard fixed Type-II/paralyzable dead-time model of WP07.

Random Type-II counters and their `M/G/infinity` connection are classical. In particular, Dvurecenskij & Ososkov, *Note on type II counter problem*, Aplikace matematiky 29, 237--249 (1984), DOI `10.21136/AM.1984.104092`, explicitly formulate Type-II counters with iid random impulse durations. Takacs and later queueing literature treat the corresponding busy-period/busy-cycle problem.

---

## 2. Universal mean output paralysis curve

At a stationary time, the number of active intervals in an `M/G/infinity` system is Poisson with mean

\[
\lambda m.
\]

Therefore

\[
P(\text{detector live})=e^{-\lambda m}.
\]

By PASTA, an incident Poisson event sees the same live probability. Hence the stationary recorded-event rate is

\[
\boxed{
r(\lambda)=\lambda e^{-\lambda m}.
}
\]

Crucially, **this mean count-rate curve depends on the recovery distribution only through its mean `m`.**

Thus every generalized Type-II detector with the same mean recovery time has the same:

- low-flux slope;
- maximum observed rate;
- location of the paralysis maximum;
- static count-rate ambiguity.

The maximum occurs at

\[
\boxed{
\lambda m=1,
\qquad
r_{\max}=\frac{1}{em}.
}
\]

and

\[
\frac{dr}{d\lambda}=e^{-\lambda m}(1-\lambda m)=0
\]

there.

The ordinary saturation curve therefore cannot reveal the shape of the recovery law.

---

## 3. Deterministic recovery is completely DC-blind at the maximum

For

\[
T=m\quad\text{a.s.},
\]

WP07/WP11 establish the much stronger property that the **entire homogeneous stationary timestamp law** depends on `lambda` only through

\[
r=\lambda e^{-\lambda m}.
\]

Therefore at

\[
\lambda m=1
\]

the complete-record local DC Fisher information vanishes:

\[
\boxed{
G_{\rm det}(0)=0.
}
\]

This is not merely a zero derivative of the mean count rate.

---

## 4. Exponential recovery has the same mean curve but retains DC information

Now let the event-specific recovery durations be exponential,

\[
\boxed{
T\sim\operatorname{Exp}(\mu),
\qquad m=1/\mu.
}
\]

The hidden detector occupancy is then the customer count of an `M/M/infinity` immigration--death process. Recorded events are arrivals that find this occupancy equal to zero.

The mean recorded rate remains

\[
r(\lambda)=\lambda e^{-\lambda/\mu},
\]

identical to the deterministic-recovery rate curve with `m=1/mu`.

Nevertheless the **inter-recording interval shape** depends on `lambda` beyond this scalar mean rate.

A short-interval asymptotic proves this directly.

---

## 5. Short-cycle probability

Condition on a recorded event at time `0`. It initiates one exponential recovery interval `T_0`.

Let `D` be the time to the next recorded event. For small `delta>0`, the leading way to obtain

\[
D\le\delta
\]

is:

1. the initial recovery ends at `t<delta`;
2. no hidden incident event arrives before `t`;
3. at least one incident event arrives during `(t,delta]`, and its first such arrival is recorded.

The probability of this path is

\[
I_\delta(\lambda)
=\int_0^\delta
\mu e^{-\mu t}e^{-\lambda t}
\left[1-e^{-\lambda(\delta-t)}\right]dt.
\]

Expanding at small `delta`,

\[
\boxed{
I_\delta(\lambda)
=\frac{\lambda\mu}{2}\delta^2
+O(\delta^3).
}
\]

Paths containing one or more hidden arrivals before the system first empties require additional arrival and recovery events and contribute only at higher order. Hence the complete short-cycle probability obeys

\[
\boxed{
p_\delta(\lambda)
\equiv P_\lambda(D\le\delta)
=\frac{\lambda\mu}{2}\delta^2
+O(\delta^3).
}
\]

Therefore, for a **fractional** uniform source perturbation

\[
\lambda_\epsilon=\lambda(1+\epsilon),
\]

\[
\boxed{
\partial_\epsilon p_\delta|_0
=\frac{\lambda\mu}{2}\delta^2
+O(\delta^3),
}
\]

which is nonzero for sufficiently small positive `delta` at every positive `lambda`, including the count-rate maximum `lambda=mu`.

Thus the complete renewal-interval law is locally sensitive to the incident rate even when the mean output count is not.

---

## 6. Explicit Fisher-information lower bound

Use only the binary statistic

\[
Z=\mathbf 1\{D\le\delta\}
\]

from each observed renewal cycle.

Its Fisher information per cycle for the fractional perturbation is

\[
I_Z
=\frac{(\partial_\epsilon p_\delta)^2}
{p_\delta(1-p_\delta)}.
\]

Using the asymptotics above,

\[
\boxed{
I_Z
=\frac{\lambda\mu}{2}\delta^2
+O(\delta^3).
}
\]

There are asymptotically `r` observed cycles per unit time. Hence the complete output Fisher-information rate satisfies

\[
\dot F_{\rm out}^{\rm DC}
\ge
r I_Z
=\frac{r\lambda\mu}{2}\delta^2
+O(\delta^3).
\]

The incident Poisson FI rate for a uniform fractional perturbation is `lambda`. Therefore

\[
\boxed{
G_{\rm exp}(0)
\ge
\frac{r\mu}{2}\delta^2
+O(\delta^3).
}
\]

At the shared paralysis maximum

\[
\lambda=\mu,
\qquad
r=\mu/e,
\]

so

\[
\boxed{
G_{\rm exp}(0)
\ge
\frac{(\mu\delta)^2}{2e}
+O((\mu\delta)^3)
>0
}
\]

for sufficiently small `delta>0`.

This is only a lower bound from one crude interval statistic. The full timestamp record may contain substantially more DC information.

---

## 7. Information inequivalence despite identical mean response

We therefore have two Type-II detectors with the same mean dead time `m` and the exact same conventional output-rate curve

\[
r(\lambda)=\lambda e^{-\lambda m},
\]

but at

\[
\lambda m=1
\]

they satisfy

\[
\boxed{
G_{\rm deterministic}(0)=0,
\qquad
G_{\rm exponential}(0)>0.
}
\]

Thus

\[
\boxed{
\text{same saturation curve}
\not\Rightarrow
\text{same complete-record information}.
}
\]

This is a stronger statement than saying count rate omits higher-order statistics: the two detectors are indistinguishable by the entire conventional **mean input-output characteristic**, including its maximum and local slope, yet differ qualitatively in local identifiability.

---

## 8. Physical interpretation

Deterministic recovery creates an exact static aliasing symmetry: at fixed `tau`, the complete output renewal law collapses onto the scalar

\[
r=\lambda e^{-\lambda\tau}.
\]

Random recovery destroys that collapse. Even when the mean output rate is stationary with respect to `lambda`, the **shape** of the observed inter-recording distribution changes because the incident rate changes how random recovery intervals overlap.

Hence recovery-time randomness can act as **side information encoded in timestamp statistics**.

This does not mean noise generically improves a detector. It means that two internal dynamics with identical average sensitivity can retain different identifiable features of the source.

A useful design/resource message is:

> the recovery-law distribution, not just its mean, can be an information resource.

---

## 9. Connection to the general Fisher-channel theorem

The general autonomous-channel spectrum of WP10 explains why this distinction is possible.

Both detectors have the same first-moment transfer at DC, but their full conditional-score projections differ. The Fisher-retention operator is sensitive to all record statistics, not merely the mean count response.

WP12 therefore supplies an explicit counterexample to any attempted universal law of the form

\[
G(0)=F(r(\lambda),r'(\lambda),m)
\]

based only on the conventional saturation curve and mean recovery time.

---

## 10. Prior-art boundary

Random dead-time and Type-II counter theory is extensive and old.

Important close work:

- Dvurecenskij & Ososkov, *Note on type II counter problem*, Aplikace matematiky 29, 237--249 (1984), DOI `10.21136/AM.1984.104092`: Type-II counters with iid random impulse durations and joint interval transforms.
- Classical Takacs/Pyke/Smith Type-II counter and `M/G/infinity` busy-period theory.
- Apanasovich & Paltsev, *Distortion of photon-correlation functions in detection systems with paralyzable dead-time effects*, JOSA B 12, 1550--1554 (1995), DOI `10.1364/JOSAB.12.001550`: constant and random paralyzable dead times in photon-correlation measurements.
- Peterson, *A numerical method for computing interval distributions for an inhomogeneous Poisson point process modified by random dead times*, Biol. Cybern. 115, 177--190 (2021), DOI `10.1007/s00422-021-00868-8`: arbitrary random dead-time interval distributions, though the developed method is nonparalyzable.
- Mandalapu & Jagannathan, *The Capacity of Photonic Erasure Channels with Detector Dead Times*, NCC 2021, DOI `10.1109/NCC52529.2021.9530152`: information-theoretic capacity with random detector dead times, considering paralyzable and nonparalyzable classes.

Therefore do **not** claim novelty for random recovery, random dead-time capacity, or `M/G/infinity` modeling.

The candidate new point requiring further search is the **Fisher-identifiability contrast at a shared paralysis curve**:

> deterministic and random-recovery Type-II detectors can have the same `r(lambda)=lambda exp(-lambda m)` but different complete-record DC Fisher information, including zero versus strictly positive information at the common rate maximum.

No priority language yet.

---

## 11. Next questions

1. Compute the exact DC Fisher information for exponential recovery, rather than only proving positivity.
2. Determine which recovery distributions produce complete static aliasing. Is deterministic recovery essentially unique?
3. Characterize the map

\[
G\mapsto \text{static output renewal law}
\]

and identify when `lambda` is locally identifiable at `lambda m=1`.
4. Determine whether greater variance of `T` monotonically increases or decreases DC identifiability under fixed mean. There is no reason to assume monotonicity before proof.
5. Compute the finite-frequency Fisher spectrum for exponential recovery using hidden Markov / birth-death methods.
6. Ask whether recovery-law shape can be optimized for a specified temporal task under a fixed mean recovery budget.
