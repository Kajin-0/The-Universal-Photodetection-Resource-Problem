# WP28 — Arbitrary Source Spectral-Concentration Theorem

**Date:** 2026-08-20

## Purpose

Remove the flat-band convention from WP25/WP26 and express the autonomous proper-event information theorem for an arbitrary finite source-information spectrum.

Main result:

> The natural source-side object is not a conventionally defined scalar bandwidth but the **spectral concentration function** of the normalized incident information spectrum. The detector-side collision-intensity resource limits the total spectral measure over which substantial transfer can occur.

---

# 1. Source-information spectrum

Let the incident optical estimation task have nonnegative spectral Fisher-information density

\[
\mathcal J_{\rm in}(\omega)\ge0
\]

with finite nonzero total information

\[
\mathcal J_{\rm tot}
=\int_{-\infty}^{\infty}\mathcal J_{\rm in}(\omega)d\omega.
\]

Define the normalized source-information spectrum

\[
\boxed{
w(\omega)
=\frac{\mathcal J_{\rm in}(\omega)}{\mathcal J_{\rm tot}},
\qquad
\int w(\omega)d\omega=1.}
\]

Thus `w` is a probability density on angular-frequency space.

For a detector with frequency-resolved source-normalized transfer `eta_I(omega)`, define task-averaged transfer

\[
\boxed{
\bar\eta_I[w]
=\int w(\omega)\eta_I(\omega)d\omega.}
\]

---

# 2. Autonomous marked-event detector

Use the autonomous/time-translation-invariant proper marked-event class of WP25/WP27.

For capture probability `eta<=C` and accessible mark `M`,

\[
\eta_I(\omega)
\le
\eta\,G(\omega),
\]

where

\[
\boxed{
G(\omega)
=\mathbb E_M|H_M(\omega)|^2,
\qquad 0\le G(\omega)\le1.}
\]

Define the conditional delay collision-intensity resource

\[
\boxed{
\mathcal R_2
=2\,\mathbb E_M\int_0^\infty f(t\mid M)^2dt.}
\]

By Parseval,

\[
\boxed{
\int_{-\infty}^{\infty}G(\omega)d\omega
=\pi\mathcal R_2.}
\]

If the conditional hazard obeys `h(t|M)<=Lambda`, then

\[
\boxed{\mathcal R_2\le\Lambda.}
\]

---

# 3. Spectral concentration function

For normalized source density `w`, define

\[
\boxed{
\mathcal W(A)
=\sup_{E\subset\mathbb R:\,|E|\le A}
\int_E w(\omega)d\omega,
\qquad A\ge0,}
\]

where `|E|` is Lebesgue measure in angular-frequency units.

Equivalently, if `w^*(s)` is the nonincreasing rearrangement of `w`,

\[
\boxed{
\mathcal W(A)=\int_0^A w^*(s)ds.}
\]

Properties:

\[
0\le\mathcal W(A)\le1,
\]

`W(A)` is monotone increasing, and

\[
\lim_{A\to\infty}\mathcal W(A)=1.
\]

Operationally, `W(A)` is the largest fraction of the incident Fisher information that can be packed into any set of total angular-frequency width `A`.

---

# 4. Rearrangement bound

We need to maximize

\[
\int w(\omega)G(\omega)d\omega
\]

over the relaxed class

\[
0\le G\le1,
\qquad
\int G\,d\omega\le A.
\]

By the bathtub principle / Hardy-Littlewood rearrangement, the maximum is obtained by allocating `G=1` first on the frequencies where `w` is largest (with a possible fractional boundary set). Therefore

\[
\boxed{
\int wG\,d\omega
\le\mathcal W(A).}
\]

Using

\[
A=\pi\mathcal R_2
\]

gives

\[
\boxed{
\bar\eta_I[w]
\le
C\,\mathcal W(\pi\mathcal R_2).}
\]

Since `R2<=Lambda` under a uniform conditional hazard ceiling,

\[
\boxed{
\bar\eta_I[w]
\le
C\,\mathcal W(\pi\Lambda).}
\]

This is the arbitrary-source spectral-concentration theorem.

**Status:** PROVED for the autonomous proper marked-event class.

The use of the relaxed `G` class can only make the upper bound looser; no assumption is made that every optimizer `G` is physically realizable as a delay characteristic-function magnitude.

---

# 5. Flat-band theorem recovered exactly

For a flat source-information spectrum on

\[
[-\Omega_s,\Omega_s],
\]

\[
w(\omega)=\frac{1}{2\Omega_s}
\mathbf1_{|\omega|\le\Omega_s}.
\]

Then

\[
\boxed{
\mathcal W(A)
=\min\left(1,\frac{A}{2\Omega_s}\right).}
\]

Hence

\[
\bar\eta_I
\le
C\min\left(1,
\frac{\pi\mathcal R_2}{2\Omega_s}
\right)
\]

and, with `R2<=Lambda`,

\[
\boxed{
\bar\eta_I
\le
C\min\left(1,
\frac{\pi\Lambda}{2\Omega_s}
\right),}
\]

which is exactly WP25/WP26.

---

# 6. Simple L-infinity corollary

Because

\[
\mathcal W(A)
\le
\min[1,A\|w\|_\infty],
\]

one obtains

\[
\boxed{
\bar\eta_I[w]
\le
C\min[1,
\pi\mathcal R_2\|w\|_\infty]
\le
C\min[1,
\pi\Lambda\|w\|_\infty].}
\]

Define

\[
\boxed{
\Omega_{\rm eff}
=\frac{1}{2\|w\|_\infty}.}
\]

For a flat band this equals `Omega_s`. Then

\[
\boxed{
\bar\eta_I[w]
\le
C\min\left(1,
\frac{\pi\mathcal R_2}{2\Omega_{\rm eff}}
\right).}
\]

This scalar effective-bandwidth form is convenient but weaker than the full concentration-function theorem.

---

# 7. Multi-band and colored tasks

The concentration theorem handles source spectra that are:

- multi-band;
- nonuniform;
- asymmetric;
- colored by a source or estimation task;
- concentrated around several carrier-sideband regions.

No arbitrary choice of `-3 dB bandwidth`, RMS bandwidth, or support width is required.

If the source information is highly concentrated in narrow spectral islands, `W(pi R2)` may be close to one even when the total span from lowest to highest frequency is enormous. This is physically correct: a sparse set of known modulation frequencies is not the same task as continuously preserving information across a wide band.

---

# 8. Target-information condition

If the task requires

\[
\bar\eta_I[w]\ge q,
\]

then necessarily

\[
\boxed{
\mathcal W(\pi\mathcal R_2)
\ge q/C.}
\]

Under a hazard ceiling,

\[
\boxed{
\mathcal W(\pi\Lambda)
\ge q/C.}
\]

Equivalently, if

\[
A_q(w)
=\inf\{A:\mathcal W(A)\ge q/C\},
\]

then

\[
\boxed{
\pi\mathcal R_2\ge A_q(w)}
\]

is necessary, and therefore any microscopic hazard resource must satisfy

\[
\boxed{
\pi\Lambda\ge A_q(w).}
\]

This expresses the resource requirement directly in terms of how much spectral measure is needed to contain the desired fraction of the source information.

---

# 9. Why a monochromatic task is different

For an ideal delta-function source-information spectrum, `w` is not an ordinary bounded density and the `L-infinity/effective-bandwidth` corollary becomes vacuous.

This is appropriate. A theorem about preserving one known modulation frequency is fundamentally weaker than a theorem about preserving a continuum of frequencies.

The concentration-function formulation makes this distinction explicit and avoids falsely identifying the total carrier frequency or spectral span with information bandwidth.

---

# 10. Resource-completeness interpretation

For autonomous proper event detectors, the core theorem can now be stated without a flat-band convention:

\[
\boxed{
\text{source information spectral concentration}
+
\text{conditional registration timing concentration}
\Longrightarrow
\text{finite task-averaged information transfer}.}
\]

The microscopic local hazard/jump-rate norm remains a sufficient physical mechanism for bounding timing concentration.

This is a cleaner answer to the UPRP than a single sensitivity-times-bandwidth product.

---

# 11. Novelty posture

Rearrangement inequalities, spectral concentration functions, and Parseval are standard mathematics.

The candidate contribution is their photodetection-specific composition with the marked primary-event FI channel and local conditional registration-intensity resource.

No novelty claim should be made for the mathematical bathtub principle itself.

---

# Status

**PROVED for the autonomous proper marked-event class.**