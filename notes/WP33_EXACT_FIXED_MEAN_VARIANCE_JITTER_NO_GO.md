# WP33 — Exact Fixed-Mean / Fixed-Variance Jitter No-Go

**Date:** 2026-08-20

## Purpose

Strengthen the WP26 timing-jitter counterexample so that **every member of the family**, not merely the limiting family, can have the same prescribed mean delay and the same prescribed variance while source-normalized information transfer approaches the capture limit uniformly on every fixed finite frequency band.

This removes a natural referee objection to the earlier asymptotic construction.

---

# 1. Two-exponential family

Let

\[
f_{\epsilon,n,\lambda}(t)
=(1-\epsilon)n e^{-nt}
+\epsilon\lambda e^{-\lambda t},
\qquad 0<\epsilon<1,
\]

with fast-path rate `n` and rare slow-path rate `lambda`.

Write

\[
x=1/\lambda.
\]

The mean and second moment are

\[
m=(1-\epsilon)/n+\epsilon x,
\]

\[
\mathbb E[X^2]
=2(1-\epsilon)/n^2+2\epsilon x^2.
\]

Hence

\[
V_{\epsilon,n}(x)
=2(1-\epsilon)/n^2+2\epsilon x^2
-\left[(1-\epsilon)/n+\epsilon x\right]^2.
\]

---

# 2. Exact variance solution

Fix any target variance

\[
\sigma^2>0.
\]

For sufficiently large `n`, the equation

\[
V_{\epsilon,n}(x)=\sigma^2
\]

has the positive solution

\[
\boxed{
 x_{\epsilon,n}
=
\frac{
\sqrt{(2-\epsilon)n^2\sigma^2-2(1-\epsilon)}
+\sqrt\epsilon(1-\epsilon)
}
{
\sqrt\epsilon\,n(2-\epsilon)
}.
}
\]

Define

\[
\boxed{
\lambda_{\epsilon,n}=1/x_{\epsilon,n}.
}
\]

Then **exactly**

\[
\boxed{
\operatorname{Var}(X_{\epsilon,n})=\sigma^2.
}
\]

Existence can also be seen without the closed form: for fixed `epsilon`, `V(lambda)` is continuous, tends to infinity as `lambda -> 0`, and tends to `(1-epsilon^2)/n^2` as `lambda -> infinity`, which is below `sigma^2` for sufficiently large `n`.

As `n -> infinity`,

\[
x_{\epsilon,n}
\longrightarrow
\frac{\sigma}{\sqrt{\epsilon(2-\epsilon)}},
\]

so

\[
\lambda_{\epsilon,n}
\longrightarrow
\frac{\sqrt{\epsilon(2-\epsilon)}}{\sigma}.
\]

The corresponding mean obeys

\[
m_{\epsilon,n}
\longrightarrow
\sigma\sqrt{\frac{\epsilon}{2-\epsilon}}
\longrightarrow0
\]

as `epsilon -> 0`.

---

# 3. Exact fixed mean by deterministic shift

Fix any target mean

\[
\mu_0>0.
\]

Choose `epsilon` sufficiently small and `n` sufficiently large that

\[
m_{\epsilon,n}<\mu_0.
\]

Set

\[
\delta_{\epsilon,n}
=\mu_0-m_{\epsilon,n}\ge0,
\]

and define

\[
D_{\epsilon,n}
=X_{\epsilon,n}+\delta_{\epsilon,n}.
\]

Then for **every member** of the chosen sequence,

\[
\boxed{
\mathbb E[D_{\epsilon,n}]=\mu_0,
}
\]

and

\[
\boxed{
\operatorname{Var}(D_{\epsilon,n})=\sigma^2.
}
\]

A deterministic shift multiplies the characteristic function only by a phase,

\[
H_D(\omega)
=e^{-i\omega\delta}H_X(\omega),
\]

so

\[
|H_D(\omega)|=|H_X(\omega)|.
\]

Thus fixing the mean exactly has no effect on source-normalized timing-information transfer.

---

# 4. Uniform finite-band information limit

For the unshifted mixture,

\[
H_{\epsilon,n}(\omega)
=(1-\epsilon)\frac{n}{n+i\omega}
+\epsilon\frac{\lambda_{\epsilon,n}}
{\lambda_{\epsilon,n}+i\omega}.
\]

Fix any finite band

\[
|\omega|\le\Omega_*.
\]

For fixed `epsilon`,

\[
\sup_{|\omega|\le\Omega_*}
\left|
\frac{n}{n+i\omega}-1
\right|
\to0
\]

as `n -> infinity`.

The slow-path contribution has magnitude at most `epsilon` for every frequency. Therefore

\[
\limsup_{n\to\infty}
\sup_{|\omega|\le\Omega_*}
|H_{\epsilon,n}(\omega)-1|
\le2\epsilon.
\]

Taking `epsilon -> 0` gives

\[
\boxed{
\sup_{|\omega|\le\Omega_*}
|H_{D_{\epsilon,n}}(\omega)-e^{-i\omega\delta_{\epsilon,n}}|
\to0.
}
\]

Consequently

\[
\boxed{
|H_{D_{\epsilon,n}}(\omega)|^2\to1
}
\]

uniformly on every prescribed finite frequency band.

For the ideal signal-only event detector,

\[
\eta_I(\omega)=\eta_c|H_D(\omega)|^2,
\]

so the transfer approaches the capture ceiling uniformly throughout that band.

---

# 5. No-go theorem

The construction proves

\[
\boxed{
\{\mathbb E[D]=\mu_0,
\operatorname{Var}(D)=\sigma^2\}
\not\Rightarrow
\text{finite temporal information bandwidth}.
}
\]

This is stronger than the earlier statement that finite variance is insufficient.

It also clarifies what the result does **not** say:

- a complete specified IRF can of course determine information transfer;
- a specified shape family plus its width may be sufficient inside that family;
- the theorem only rejects low-order moments as architecture-independent primitive resources.

An FWHM specification is likewise not a complete resource without shape assumptions, but WP33 does not claim a family with an arbitrary fixed exact FWHM and diverging information bandwidth.

---

# 6. Consequence for the manuscript

The first paper should state the no-go as:

> Even exact knowledge of the mean registration delay and RMS timing jitter does not bound autonomous event-channel information bandwidth.

This is fully proved by WP33.

Avoid the stronger unsupported wording that an arbitrary exact FWHM value can simultaneously be held fixed while information bandwidth diverges.

**Status: PROVED.**
