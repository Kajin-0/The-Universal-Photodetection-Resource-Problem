# WP26 — Jitter-Moment No-Go and Collision-Intensity Timing Resource

**Date:** 2026-08-20

## Purpose

Stress-test whether the WP25 conditional hazard can be replaced by familiar detector timing metrics such as mean latency, RMS timing jitter, FWHM jitter, or a finite collection of timing moments.

Main conclusions:

1. **Finite mean delay and finite RMS timing jitter do not imply a finite information-bandwidth ceiling.**
2. The exact timing quantity selected by Parseval is the conditional delay-density `L2` concentration.
3. A uniform conditional hazard is a physically local sufficient resource that bounds this concentration, but the mathematically weakest WP25-style resource is an averaged conditional collision intensity.

---

# 1. General marked-event timing resource

Retain the marked proper-event class of WP25. Conditional on accessible mark `m`, let

\[
f_m(t)=f(t\mid m),
\qquad
H_m(\omega)=\int f_m(t)e^{-i\omega t}dt.
\]

Define the **conditional collision-intensity resource**

\[
\boxed{
\mathcal R_2
=2\int p(m)
\left[\int_0^\infty f_m(t)^2dt\right]dm.
}
\]

It has dimensions of inverse time.

The factor `2` is chosen so that a constant-hazard exponential law of rate `Lambda` has

\[
\mathcal R_2=\Lambda.
\]

Parseval gives exactly

\[
\int p(m)
\left[
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}|H_m(\omega)|^2
\right]dm
=\frac{\mathcal R_2}{2}.
\]

Therefore WP25 immediately generalizes to

\[
\boxed{
\bar\eta_I(\Omega_s)
\le
C\min\left[
1,
\frac{\pi\mathcal R_2}{2\Omega_s}
\right].
}
\]

A uniform conditional hazard bound `h(t|m)<=Lambda` implies

\[
\boxed{\mathcal R_2\le\Lambda}
\]

by the WP25 survival/hazard proof.

Thus:

- `R_2` is the weakest timing-concentration object used by the Parseval theorem;
- `Lambda` is the stronger local microscopic resource that can be bounded directly from Markov transition rates or quantum jump-operator norms.

`R_2` should not be mislabeled as a fundamental material constant; it is an operational intermediate resource of the full detector channel.

---

# 2. Why variance is insufficient

Consider a smooth two-exponential mixture

\[
\boxed{
f_{\epsilon,n}(t)
=(1-\epsilon)n e^{-nt}
+\epsilon\lambda_\epsilon e^{-\lambda_\epsilon t},}
\]

with

\[
0<\epsilon<1.
\]

Its characteristic function is

\[
\boxed{
H_{\epsilon,n}(\omega)
=(1-\epsilon)\frac{n}{n+i\omega}
+\epsilon\frac{\lambda_\epsilon}{\lambda_\epsilon+i\omega}.
}
\]

The first two raw moments are

\[
\mathbb E[D]
=\frac{1-\epsilon}{n}
+\frac{\epsilon}{\lambda_\epsilon},
\]

\[
\mathbb E[D^2]
=\frac{2(1-\epsilon)}{n^2}
+\frac{2\epsilon}{\lambda_\epsilon^2}.
\]

Choose, asymptotically,

\[
\boxed{
\lambda_\epsilon
=\frac{\sqrt{2\epsilon}}{\sigma}.}
\]

Then as

\[
n\to\infty,
\qquad
\epsilon\to0,
\]

one has

\[
\mathbb E[D^2]\to\sigma^2,
\]

while

\[
\mathbb E[D]\to0,
\]

so

\[
\boxed{\operatorname{Var}(D)\to\sigma^2.}
\]

The small slow component carries the prescribed second moment while an asymptotically unit fraction of events occupies the prompt component.

---

# 3. Information bandwidth remains arbitrarily large at fixed variance

For every finite frequency window `|omega|<=Omega`,

\[
\left|
\frac{n}{n+i\omega}-1
\right|
\le\frac{|\omega|}{n}.
\]

Also, for any characteristic function,

\[
\left|
\frac{\lambda}{\lambda+i\omega}-1
\right|
\le2.
\]

Therefore

\[
\sup_{|\omega|\le\Omega}
|H_{\epsilon,n}(\omega)-1|
\le
\frac{\Omega}{n}+2\epsilon.
\]

Choose first `epsilon` small and then `n` large. For any fixed finite `Omega`,

\[
\boxed{
\sup_{|\omega|\le\Omega}
|H_{\epsilon,n}(\omega)-1|
\to0,
}
\]

while the variance approaches the prescribed nonzero value `sigma^2`.

Hence

\[
\boxed{
\operatorname{Var}(D)=\sigma^2<\infty
\quad\not\Rightarrow\quad
\text{finite information bandwidth}.
}
\]

Indeed, for every finite target band and every target retention below unity, a member of this family can preserve that retention while maintaining the same asymptotic RMS jitter.

**Status:** PROVED explicit smooth counterexample family.

---

# 4. Mean delay can also be fixed

A deterministic shift

\[
D\mapsto D+t_0
\]

changes

\[
H(\omega)\mapsto e^{-i\omega t_0}H(\omega)
\]

but leaves

\[
|H(\omega)|
\]

unchanged.

Therefore, after choosing the mixture above, a deterministic offset can set any sufficiently large desired mean delay without changing the information spectrum or variance.

More generally, the mixture parameters can be adjusted continuously to match prescribed finite first and second moments exactly while retaining an arbitrarily narrow dominant prompt component.

Thus

\[
\boxed{
\{\mathbb E[D],\operatorname{Var}D\}
\text{ finite/fixed}
\not\Rightarrow
\text{finite information bandwidth}.
}
\]

---

# 5. Why FWHM jitter is even less suitable

Single-photon-detector timing jitter is commonly reported as the FWHM of the instrument-response histogram.

A distribution with a very narrow high-amplitude prompt peak and a low-amplitude long tail can have arbitrarily small FWHM while retaining substantial tail probability or moments.

Conversely, a broad marginal FWHM can be informationally harmless when an accessible event mark identifies the relevant delay and permits event-by-event correction.

Therefore FWHM is a useful engineering descriptor of a particular measured IRF, but it is not a resource-complete variable for source-information bandwidth.

Do not claim that this criticism of FWHM as a generic shape descriptor is new. The new UPRP point is its failure as a sufficient variable in a universal information theorem.

---

# 6. Finite collections of timing moments are generically insufficient

The same hiding mechanism extends beyond the first two moments.

A distribution can place probability `1-epsilon` in an increasingly narrow prompt component while distributing a vanishing total probability among sufficiently remote tail components to satisfy a finite collection of prescribed moments.

The high-frequency information over any fixed finite band is dominated by the prompt weight, while the remote low-weight components carry the moment constraints.

This is the timing-domain analogue of the recurring UPRP hidden-resource mechanism:

- rare-fast Markov states hide large rates from stationary activity;
- UV coherences hide metrological power from diagonal energy moments;
- remote timing tails hide moments while a prompt spike carries bandwidth.

A full constructive proof for an arbitrary number of prescribed moments is not written here; the first-two-moment theorem above is already sufficient to reject mean/RMS jitter as a universal timing resource.

**Status for arbitrary finite moment sets:** CONJECTURE / straightforward truncated-moment construction to formalize if needed.

---

# 7. Collision intensity versus conventional jitter

The spectral identity

\[
\boxed{
\int\frac{d\omega}{2\pi}|H(\omega)|^2
=\int f(t)^2dt
}
\]

shows why `L2` concentration is the natural timing quantity for **average spectral information**.

Two distributions can have the same variance yet arbitrarily different values of

\[
\int f^2dt.
\]

In the two-exponential counterexample, the prompt component gives

\[
\int f_{\epsilon,n}(t)^2dt
\sim\frac{(1-\epsilon)^2n}{2}
\to\infty,
\]

so

\[
\mathcal R_2\to\infty
\]

while `Var(D)` remains fixed.

This is precisely why the WP25 bound correctly refuses to follow from RMS jitter alone.

---

# 8. Minimal timing-resource hierarchy

For the proper event branch, the timing hierarchy is now

\[
\boxed{
\text{microscopic local rate/operator bound }\Lambda
\Longrightarrow
\text{collision intensity }\mathcal R_2\le\Lambda
\Longrightarrow
\text{finite average information bandwidth}.
}
\]

By contrast,

\[
\boxed{
\text{mean latency / RMS jitter / FWHM alone}
\not\Rightarrow
\text{finite information bandwidth}.
}
\]

This sharply identifies what kind of timing resource the universal theorem actually needs.

---

# 9. Literature posture

Standard single-photon-detector literature defines timing jitter as event-to-event variation of electrical response delay and commonly reports FWHM of an instrument response function. This is established detector metrology and not novel.

Marked Poisson-process Fisher-information formulas are also standard in imaging/statistical estimation.

Targeted search on 2026-08-20 did not identify a prior photodetection theorem using a local conditional hazard or conditional delay-density `L2` norm to prove a source-normalized information-bandwidth ceiling. Novelty remains provisional.

---

# 10. Consequence for UPRP

The event-detector branch can now be stated in a genuinely minimal form:

\[
\boxed{
\text{finite source information spectrum}
+
\text{finite conditional registration collision intensity}
\Rightarrow
\text{finite average information transfer},
}
\]

with a local hazard/jump-rate norm providing the physically transparent microscopic sufficient condition.

The common detector metric `timing jitter` is not itself enough unless its full distributional shape or a stronger concentration resource is controlled.

---

# Status

**PROVED for fixed first/second timing moments; general finite-moment extension remains to be formalized only if publication needs it.**