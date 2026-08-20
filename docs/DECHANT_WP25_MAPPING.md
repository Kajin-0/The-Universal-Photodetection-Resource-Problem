# Equation-Level Mapping: Dechant 2026 FRI vs WP25

**Date:** 2026-08-20

## Purpose

Determine whether WP25 is a direct specialization or corollary of Andreas Dechant's 2026 finite-frequency fluctuation-response inequality (FRI).

Reference:

A. Dechant, `Finite-Frequency Fluctuation-Response Inequality`, Physical Review Letters 136, 207101 (2026), DOI `10.1103/3hs9-dz3d`.

---

# 1. Dechant's central finite-frequency result

For response matrix `R(omega)` and observable spectral-density matrix `S(omega)`, Dechant proves

\[
\boxed{
R^\dagger(\omega)S^{-1}(\omega)R(\omega)\le A,
}
\]

where `A` is frequency independent and depends on the perturbation/environment. For a scalar observable/perturbation,

\[
\boxed{
|R(\omega)|^2\le A S(\omega).
}
\]

The paper defines a dimensionless response efficiency

\[
\eta_R(\omega)=\frac{|R(\omega)|^2}{A S(\omega)}\le1.
\]

For jump processes the corresponding `A` is related to dynamical activity.

This is a highly relevant prior theorem.

---

# 2. Why this does not directly give WP25

For weak Poisson/coherent optical modulation, UPRP's frequency-resolved source-normalized FI kernel has the form

\[
\eta_I(\omega)
\propto
\Phi_0\frac{|R(\omega)|^2}{S(\omega)}.
\]

Dechant's pointwise FRI therefore gives a **frequency-independent ceiling**

\[
\eta_I(\omega)\lesssim\Phi_0 A.
\]

By itself this does not force

\[
\eta_I(\omega)\to0
\]

or a finite average-bandwidth integral as `|omega|` grows.

Indeed, a pointwise constant bound can be integrated over an arbitrarily wide source band unless another resource controls the frequency support/shape of the response.

WP25 supplies exactly such an additional structure through the first-registration delay kernel.

---

# 3. Dechant's broadband corollary is a different integral

Dechant also derives, for an equilibrium environment, a broadband bound of the form

\[
\int_0^\infty d\omega\,[\mathrm{SNR}(\omega)]^2
\le\text{environment/perturbation constant},
\]

where the paper's SNR is defined using response magnitude divided by the **static variance** of the measured observable.

This is not the same object as the photodetection Fisher-information kernel

\[
|R(\omega)|^2/S(\omega).
\]

Therefore the displayed broadband FRI corollary does not algebraically reduce to WP25's

\[
\int|H_D(\omega)|^2d\omega
\le\pi\Lambda
\]

or its source-normalized event-information theorem.

---

# 4. WP25's additional physical structure

WP25 assumes an autonomous proper primary-event detector in which, after conditioning on all accessible parameter-independent event marks, the source timing dependence enters through a first-registration delay density

\[
f(t\mid m).
\]

A local conditional hazard ceiling

\[
h(t\mid m)\le\Lambda
\]

implies

\[
\int f(t\mid m)^2dt\le\Lambda/2.
\]

Parseval then gives

\[
\boxed{
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}|H_m(\omega)|^2
\le\Lambda/2.
}
\]

This is the step that forces a finite source-information bandwidth.

The resource is a **local first-registration intensity**, not stationary activity.

WP4's rare-fast counterexample already demonstrates why stationary activity can remain finite while local rates diverge.

---

# 5. Overlap in the Markov subclass

For a stationary Markov jump photodetector, both theorems can apply simultaneously:

- Dechant constrains response/noise at each frequency in terms of an activity-like perturbation resource;
- WP25 constrains the integrated timing transfer of the proper first-event channel in terms of the maximum local registration intensity.

These constraints are complementary rather than obviously identical.

A detector may have bounded stationary activity yet unbounded local registration intensity; WP4 constructs precisely this type of family.

Thus a Dechant activity bound does not automatically replace the WP25 `Lambda` resource.

---

# 6. Distinguishing counterexample

Consider the exponential first-registration family

\[
f_n(t)=n e^{-nt}.
\]

Then

\[
H_n(\omega)=\frac{n}{n+i\omega}.
\]

For each fixed finite frequency, response/noise can remain consistent with a finite pointwise FRI while the characteristic timing bandwidth scales with `n`.

If stationary occupation of the fast state is simultaneously scaled down, stationary activity can remain bounded while the local registration rate `n` diverges, as in the WP4 rare-fast construction.

Hence a stationary activity-like resource and the WP25 local hazard norm are genuinely different quantities.

---

# 7. Current classification

Based on the displayed equations in Dechant 2026:

\[
\boxed{
\text{WP25 is not a direct algebraic corollary of the published finite-frequency FRI.}
}
\]

This does **not** prove novelty. A result equivalent to WP25 may exist elsewhere in first-passage, point-process, communication, reliability, or detector-timing literature.

Current classification:

- **identical theorem:** not found;
- **direct corollary of Dechant Eq. (7)/(9)/(15):** no;
- **overlapping Markov-domain constraint:** yes;
- **distinct added resource:** local conditional first-registration intensity / timing-density concentration.

---

# 8. Remaining audit

Search next for:

1. first-passage Fourier bounds under bounded hazard;
2. Poisson communication channels with random propagation delay;
3. timing-jitter modulation-transfer integrals;
4. queueing/reliability results bounding characteristic-function `L2` norm from failure-rate constraints.

---

# Status

**Equation-level audit passed the 'not an obvious direct Dechant corollary' gate. Novelty remains provisional.**