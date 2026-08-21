# WP07 — Continuous-Time Paralyzable Detector: Exact Score Representation and Spectral Inversion at Saturation

**Status:** theorem-grade continuous-time result derived; exact complete-record score representation obtained; rigorous finite-frequency lower bound and high-frequency limit proved; high-accuracy numerical evaluation independently reproduces the exact representation. Priority/novelty remains provisional pending the historical dead-time audit in WP08.

## 1. Model

Let the incident optical events form an inhomogeneous Poisson process with weak fractional intensity perturbation

\[
\lambda_\epsilon(t)=\lambda\,[1+\epsilon u(t)],
\qquad |\epsilon|\ll1.
\]

An ideal deterministic **paralyzable / Type-II** detector of dead time `tau` records an incident event at time `t` iff there was no incident event in the preceding interval `(t-tau,t)`. Every incident event, including an unrecorded one, restarts the dead interval.

Equivalently, for the incident point process `N`, a point at `t` is retained iff

\[
N((t-\tau,t))=0.
\]

Unlike the nonparalyzable detector in WP04, the hidden incident events alter future detector availability, so the detector state is not reconstructible from the output timestamps.

Define

\[
\rho=\lambda\tau,
\qquad
r=\lambda e^{-\rho}.
\]

Here `r` is the stationary registered-event rate.

---

## 2. Baseline output is a renewal process

Starting immediately after a registered event, let the incident exponential interarrival gaps be iid with density `lambda exp(-lambda t)`. The next registered event occurs at the first incident gap exceeding `tau`.

Define the defective short-gap and terminal long-gap kernels

\[
k(t)=\lambda e^{-\lambda t}\mathbf 1_{(0,\tau]}(t),
\qquad
g(t)=\lambda e^{-\lambda t}\mathbf 1_{(\tau,\infty)}(t).
\]

If `D` is the interval between successive registered events, then

\[
f_D=\sum_{n\ge0}k^{*n}*g.
\]

Its Laplace transform is

\[
\boxed{
F(s)=E[e^{-sD}]
=\frac{\lambda e^{-(\lambda+s)\tau}}
{s+\lambda e^{-(\lambda+s)\tau}}
=\frac{r e^{-s\tau}}
{s+r e^{-s\tau}}.
}
\]

Consequently

\[
\boxed{E[D]=\frac1r,}
\]

so the registered rate is indeed `r=lambda exp(-rho)`.

Let

\[
q(t)=P(D>t).
\]

Since `(1-F(s))/s=1/(s+r e^{-s tau})`, `q` is the delayed-exponential survival function obeying

\[
\boxed{
q'(t)=-r q(t-\tau),
\qquad
q(t)=1\quad(0\le t<\tau),
}
\]

and

\[
\boxed{
f_D(t)=r q(t-\tau)\mathbf1_{t\ge\tau}.}
\]

At the dimensionless saturation point `rho=1` and with `tau=1`,

\[
q(t)=\sum_{k=0}^{\lfloor t\rfloor}
\frac{(-e^{-1})^k(t-k)^k}{k!}.
\]

---

## 3. Conditional-score decomposition of the complete timestamp record

The incident Poisson score for tangent `u` is

\[
S_{\rm in}[u]
=\int u(t)[N(dt)-\lambda dt].
\]

For the complex Fourier tangent

\[
u(t)=e^{i\omega t},
\]

the incident Fisher-information rate is `lambda` in the complexified tangent convention.

Condition on two successive registered events separated by `D=d`. Let

\[
R(t)=\sum_{n\ge1}k^{*n}(t)
\]

be the renewal density of hidden incident events reachable from the preceding registered event through only short gaps. Factorization of the hidden cluster at an interior incident event gives the exact posterior mean hidden-event density

\[
\boxed{
m_d(t)=\frac{R(t)f_D(d-t)}{f_D(d)},
\qquad0<t<d.}
\]

The final registered event at `d` is known exactly. Assigning the starting event to the preceding renewal interval, the conditional output-score reward of one interval is

\[
\boxed{
A_d(\omega)
=e^{i\omega d}
+\int_0^d e^{i\omega t}[m_d(t)-\lambda]dt.
}
\]

Thus the complete-record output score is a renewal sum of these exact conditional rewards.

---

## 4. Exact transform of the interval score

Define

\[
H_\omega(s)
=\int_0^\infty e^{-sd}f_D(d)A_d(\omega)\,dd.
\]

Using the hidden-renewal factorization above,

\[
H_\omega(s)
=F(s-i\omega)
+\widehat R(s-i\omega)F(s)
-\frac{\lambda}{i\omega}[F(s-i\omega)-F(s)].
\]

Let

\[
y=\omega\tau,
\]

and define the exact fractional mean-response factor

\[
\boxed{
M_\rho(y)
=1-\rho\frac{1-e^{-iy}}{iy}.
}
\]

After algebraic cancellation,

\[
\boxed{
H_\omega(s)
=M_\rho(y)e^{iy}
\frac{s r e^{-s\tau}}
{[s+r e^{-s\tau}]
[s-i\omega+r e^{-(s-i\omega)\tau}]}.
}
\]

Two important consequences follow immediately.

### Zero mean interval reward

For every nonzero Fourier frequency,

\[
\boxed{E[A_D(\omega)]=H_\omega(0)=0.}
\]

Hence the cross-renewal term in the long-record Fourier-score variance vanishes exactly. The complete FI rate is therefore the registered-event rate times the same-interval score variance.

### Exact complete-record Fisher spectrum

Therefore

\[
\boxed{
G_{\lambda,\tau}(\omega)
=\frac{r}{\lambda}E|A_D(\omega)|^2.
}
\]

This is already an exact complete-record formula; no output-count approximation has been made.

---

## 5. One-dimensional exact integral representation

Let

\[
Q(s)=\frac1{s+r e^{-s\tau}},
\qquad
q_\omega(t)=e^{i\omega t}q(t),
\]

and define

\[
c_\omega(t)=(f_D*q_\omega)(t).
\]

Because `F(s)Q(s-i omega)` is the Laplace transform of `c_omega`, the transform above gives

\[
\boxed{
f_D(d)A_d(\omega)
=M_\rho(y)e^{iy}c_\omega'(d).}
\]

Thus

\[
\boxed{
G_{\lambda,\tau}(\omega)
=\frac{r}{\lambda}|M_\rho(y)|^2
\int_\tau^\infty
\frac{|c_\omega'(t)|^2}{f_D(t)}dt.
}
\]

This is an exact one-dimensional representation of the complete timestamp Fisher spectrum.

For numerical work, `c_omega` obeys the simple method-of-steps delay equation

\[
\boxed{
c_\omega'(t)
=f_D(t)+i\omega c_\omega(t)
-r e^{iy}c_\omega(t-\tau),}
\]

with `c_omega(t)=0` for `t<tau`.

No hidden-state Monte Carlo is required.

---

## 6. Exact DC blindness at classical paralysis

For a constant fractional perturbation, `y -> 0` and

\[
M_\rho(0)=1-\rho.
\]

At the classical maximum of the paralyzable count-rate curve,

\[
\boxed{\rho=\lambda\tau=1,}
\]

we have

\[
\boxed{M_1(0)=0.}
\]

The exact integral factor is finite. Therefore

\[
\boxed{G_{\rho=1}(0)=0.}
\]

This is a complete-record statement, not merely the familiar fact that the mean registered rate `r=lambda exp(-lambda tau)` has zero derivative at `lambda tau=1`.

A second proof follows from the baseline renewal law itself: `F(s)` depends on `lambda` only through `r=lambda exp(-lambda tau)`, and `dr/dlambda=0` at `lambda tau=1`. Hence the entire stationary output renewal experiment is locally insensitive to a uniform change of `lambda`.

---

## 7. Rigorous finite-frequency lower bound from one observable

The exact mean registered intensity under an arbitrary deterministic incident rate is

\[
\boxed{
r_\epsilon(t)
=\lambda_\epsilon(t)
\exp\!\left[-\int_{t-\tau}^{t}\lambda_\epsilon(s)ds\right].}
\]

For a Fourier perturbation, its first-order fractional response is exactly `M_rho(y)`.

At baseline the registered events form a renewal point process. Its Bartlett counting spectrum is

\[
S_Y(\omega)
=r\frac{1-|F(i\omega)|^2}{|1-F(i\omega)|^2}
=\boxed{
r\left[1-2r\tau\frac{\sin y}{y}\right].}
\]

Now retain only the long-record Fourier component of the registered counting process. Fisher information in the complete record must be at least the information contained in this single statistic. The scalar information inequality gives

\[
\boxed{
G_{\rho}(y)
\ge
L_\rho(y)
\equiv
e^{-\rho}
\frac{\left|1-\rho\dfrac{1-e^{-iy}}{iy}\right|^2}
{1-2\rho e^{-\rho}\dfrac{\sin y}{y}}.
}
\]

This lower bound is rigorous and requires only the exact first- and second-order output statistics; it does not assume that the Fourier count statistic is sufficient.

---

## 8. More than half the incident FI survives at a finite frequency

At the paralysis point `rho=1`, evaluate the bound at

\[
y=\pi,
\qquad
\omega=\pi/\tau.
\]

Since `sin(pi)=0`,

\[
\boxed{
G_1(\pi)
\ge
\frac1e\left(1+\frac4{\pi^2}\right)
=0.5169753628\ldots
}
\]

Therefore

\[
\boxed{
G_1(0)=0
\quad\text{while}\quad
G_1(\pi/\tau)>0.5169.
}
\]

An ideal continuous-time paralyzable detector can be **completely locally blind to DC intensity changes while retaining more than one half of the incident local Fisher information at a finite temporal frequency**.

This is a theorem about the complete output record because the finite-frequency value is a lower bound on complete-record FI.

---

## 9. Exact high-frequency plateau

For a fixed renewal interval `d`, the oscillatory hidden-intensity and compensator integrals in `A_d(omega)` vanish as `|omega| -> infinity` by the Riemann-Lebesgue lemma. The known registered endpoint remains:

\[
A_d(\omega)=e^{i\omega d}+o(1).
\]

The renewal interval has finite moments, so dominated convergence yields

\[
E|A_D(\omega)|^2\to1.
\]

Therefore

\[
\boxed{
\lim_{|\omega|\to\infty}
G_{\lambda,\tau}(\omega)
=\frac r\lambda
=e^{-\rho}.}
\]

At classical paralysis,

\[
\boxed{
\lim_{|\omega|\to\infty}G_1(\omega)=e^{-1}=0.3678794412\ldots}
\]

Combining this with the previous section,

\[
0=G_1(0),
\qquad
G_1(\pi/\tau)>0.5169,
\qquad
G_1(\infty)=0.3679.
\]

Thus the continuous-time Type-II detector cannot have a monotone low-pass or monotone high-pass Fisher spectrum. It must exhibit a **finite-frequency information overshoot** above its high-frequency plateau.

---

## 10. Numerical evaluation of the exact complete-record integral

The method-of-steps representation above was independently evaluated at `rho=1` with `tau=1`, using the exact delayed-exponential survival function and successively refined time steps.

At `omega=pi`, the complete-record value converges to

\[
\boxed{
G_1(\pi)\approx0.5281424250.
}
\]

Representative convergence:

| truncation / method | `G_1(pi)` |
|---|---:|
| method of steps, `T=15 tau` | 0.5281385 |
| `T=20 tau` | 0.52814238 |
| `T=25 tau` | 0.52814242 |
| `T=30 tau` | 0.528142425 |

The rigorous one-statistic lower bound `0.51697536` therefore captures roughly 97.9% of the numerically evaluated complete-record FI at this frequency.

A one-dimensional optimization of the exact representation gives a shallow maximum near

\[
\omega\tau\approx3.334,
\qquad
G\approx0.52916,
\]

but this maximum location/value is **numerical, not a closed-form theorem**, and should not be elevated above the exact endpoint/bound statements.

---

## 11. Physical interpretation

The conventional paralyzable count-rate curve reaches its maximum at `lambda tau=1`; a static count-rate measurement is locally blind there. The complete timestamp record is also DC-blind because the entire stationary renewal law is first-order insensitive to `lambda` at this point.

A finite-frequency perturbation is different. It modulates the probability that a long quiet gap opens at different phases. The sequence of cluster starts therefore retains timing information even when a uniform flux perturbation is locally unidentifiable.

At extremely high modulation frequency, hidden-cluster contributions average out and only the directly registered endpoints survive, giving the plateau `r/lambda=e^{-rho}`. At intermediate frequency, correlations in the hidden cluster boundaries provide additional information above that endpoint-only plateau.

The resulting pattern is

\[
\boxed{
\text{DC blindness}
\;\to\;
\text{finite-frequency information recovery/overshoot}
\;\to\;
\text{high-frequency endpoint plateau}.}
\]

This is the continuous-time physical counterpart of the discrete one-bin theorem in WP06, but its unlimited frequency axis produces an overshoot rather than a monotone rise to Nyquist.

---

## 12. Novelty posture

Do **not** claim novelty for:

- the classical paralyzable rate law `r=lambda exp(-lambda tau)`;
- renewal representations of paralyzable counters;
- count distributions or moments under paralyzable dead time;
- the fact that sinusoidally/periodically modulated photon streams with dead time were studied historically;
- generic likelihood, Fisher, or information analysis of dead-time systems.

The candidate new result is much narrower:

> complete-timestamp **local temporal Fisher information** of the continuous Type-II/paralyzable detector, including exact DC nonidentifiability at `lambda tau=1`, a rigorous finite-frequency FI recovery exceeding one half of incident FI, the exact high-frequency plateau, and the resulting information-spectral overshoot.

WP08 performs the hostile historical audit. No `first` or priority language is permitted yet.

---

## 13. Next gates

1. Add a dependency-light reproduction script for the exact integral and lower bound.
2. Complete the historical audit of Teich/Vannucci/Cantor and older paralyzable-counter work.
3. Determine whether the integral factor admits a closed form or useful sharp analytic bounds at `rho=1`.
4. Map the spectrum versus `rho` to determine whether `rho=1` is a bifurcation/transition point in spectral shape.
5. Tie WP07 formally into the arbitrary-autonomous-channel theorem of WP02.
6. Only after novelty survives: decide whether the discrete WP06 theorem and continuous WP07 theorem together are sufficient to anchor Paper 2.
