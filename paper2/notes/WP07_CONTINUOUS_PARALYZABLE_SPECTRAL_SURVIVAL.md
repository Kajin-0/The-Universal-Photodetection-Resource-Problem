# WP07 — Continuous-Time Paralyzable Detector: Spectral Survival at the Paralysis Maximum

**Status:** theorem-grade analytic result with an exact DC zero, a rigorous finite-frequency Fisher lower bound, and an exact high-frequency limit. No priority claim yet.

## 1. Model

Let the incident optical events form a Poisson point process with weakly modulated intensity

\[
\lambda_\epsilon(t)=\lambda\,[1+\epsilon u(t)],
\qquad |\epsilon|\ll1.
\]

An ideal **paralyzable / Type-II** detector with deterministic dead interval `tau` records an incident event at time `t` iff there was no incident event in `(t-tau,t)`. Every incident event, including an unrecorded event during dead time, restarts the dead interval.

Equivalently, recorded events are starts of Poisson clusters separated by incident interarrival gaps exceeding `tau`.

Define

\[
\rho=\lambda\tau.
\]

The accessible record is the complete sequence of recorded timestamps. Hidden arrivals inside a cluster are not retained.

---

## 2. Baseline output is a renewal process

At constant `lambda`, let `E_j` be iid exponential interarrival times of rate `lambda`. Starting from a recorded event, let

\[
N=\min\{j\ge1:E_j>\tau\},
\qquad
D=\sum_{j=1}^{N}E_j
\]

be the interval to the next recorded event.

The Laplace transform of `D` is

\[
\boxed{
\psi(s)
=E[e^{-sD}]
=\frac{\lambda e^{-(\lambda+s)\tau}}
{s+\lambda e^{-(\lambda+s)\tau}}.
}
\]

Define the recorded rate

\[
\boxed{r=\lambda e^{-\lambda\tau}=\lambda e^{-\rho}.}
\]

Then

\[
\boxed{
\psi(s)=\frac{r e^{-s\tau}}
{s+r e^{-s\tau}}.
}
\]

Thus, for fixed `tau`, the **entire homogeneous stationary output renewal law depends on the incident rate `lambda` only through `r`**, not merely its mean count rate.

Also

\[
E[D]=\frac1r.
\]

---

## 3. Exact complete-record DC blindness at the paralysis maximum

For a uniform fractional perturbation, `lambda -> lambda(1+epsilon)`,

\[
\frac{dr}{d\lambda}
=e^{-\rho}(1-\rho).
\]

At the classical paralyzable count-rate maximum

\[
\boxed{\rho=\lambda\tau=1,}
\]

we have

\[
\boxed{\frac{dr}{d\lambda}=0.}
\]

Because the complete homogeneous stationary renewal law is parameterized by `lambda` only through `r`, every regular finite-dimensional likelihood derivative of the complete recorded timestamp process vanishes in the uniform/DC direction at `rho=1`.

Therefore the complete source-normalized local Fisher retention satisfies

\[
\boxed{G_{\rho=1}(0)=0.}
\]

This is stronger than the familiar statement that the mean recorded count rate has zero slope. The **whole stationary output experiment** is locally nonidentifiable for a uniform intensity perturbation.

---

## 4. Exact first-order mean response to a temporal modulation

For an arbitrary deterministic time-dependent Poisson intensity, an incident event at `t` is recorded iff the preceding dead interval is empty. Therefore the exact mean recorded intensity is

\[
\boxed{
r_\epsilon(t)
=\lambda_\epsilon(t)
\exp\!\left[-\int_{t-\tau}^{t}\lambda_\epsilon(s)\,ds\right].
}
\]

For the complex temporal mode

\[
u(t)=e^{i\omega t},
\qquad y=\omega\tau,
\]

linearization around the homogeneous baseline gives

\[
\frac{\delta r(t)}{r}
=\epsilon e^{i\omega t}M_\rho(y),
\]

with

\[
\boxed{
M_\rho(y)
=1-\rho\frac{1-e^{-iy}}{iy}.
}
\]

Hence

\[
|M_\rho(y)|^2
=1-2\rho\frac{\sin y}{y}
+2\rho^2\frac{1-\cos y}{y^2}.
\]

At `rho=1`, `M_1(0)=0`, but `M_1(y) != 0` for every nonzero real `y`. Indeed

\[
\left|\frac{1-e^{-iy}}{iy}\right|
=\frac{2|\sin(y/2)|}{|y|}<1
\]

for `y != 0`.

This first-moment response is established dead-time physics and is **not** by itself a novelty claim.

---

## 5. Exact baseline output power spectrum

For a stationary renewal point process of rate `r` and inter-renewal characteristic function

\[
\phi(\omega)=E[e^{-i\omega D}],
\]

the continuous Bartlett spectrum away from the DC line is

\[
S_Y(\omega)
=r\frac{1-|\phi(\omega)|^2}{|1-\phi(\omega)|^2}.
\]

Here

\[
\phi(\omega)
=\frac{r e^{-iy}}
{i\omega+r e^{-iy}},
\]

so direct simplification gives

\[
\boxed{
S_Y(\omega)
=r\left[
1-2\rho e^{-\rho}\frac{\sin y}{y}
\right].
}
\]

The bracket is strictly positive for every real `y`, because

\[
2\rho e^{-\rho}\le\frac{2}{e}<1
\]

and `sin(y)/y <= 1`.

This spectrum is a standard renewal/noise object. Its role here is to produce a rigorous information lower bound.

---

## 6. Rigorous Fisher lower bound from one Fourier statistic

For a real sinusoidal fractional perturbation at frequency `omega`, the incident Poisson Fisher-information rate is

\[
\dot F_{\rm in}=\frac{\lambda}{2}.
\]

Consider the optimally phased output Fourier statistic over a long observation window,

\[
Z_T=\int_0^T\cos(\omega t-\arg M_\rho)\,Y(dt).
\]

At baseline,

\[
\frac1T\frac{d}{d\epsilon}E_\epsilon[Z_T]\Big|_0
\to\frac{r|M_\rho(y)|}{2},
\]

while

\[
\frac1T\operatorname{Var}_0(Z_T)
\to\frac{S_Y(\omega)}{2}.
\]

The scalar information inequality

\[
F_Y\ge
\frac{(\partial_\epsilon E Z_T)^2}
{\operatorname{Var}Z_T}
\]

therefore yields the source-normalized lower bound

\[
\boxed{
G_\rho(\omega)
\ge L_\rho(y)
\equiv
e^{-\rho}
\frac{|M_\rho(y)|^2}
{1-2\rho e^{-\rho}\,\sin(y)/y}.
}
\]

Explicitly,

\[
\boxed{
L_\rho(y)=
e^{-\rho}
\frac{
1-2\rho\,\sin y/y
+2\rho^2(1-\cos y)/y^2
}
{1-2\rho e^{-\rho}\,\sin y/y}.
}
\]

This lower bound uses only one linear statistic of the complete output record. The exact complete-record Fisher spectrum can only be larger.

---

## 7. Continuous-time spectral survival theorem at `rho=1`

At the paralysis maximum,

\[
\boxed{
L_1(y)=
\frac{e^{-1}
\left[
1-2\sin y/y+2(1-\cos y)/y^2
\right]}
{1-(2/e)\sin y/y}.
}
\]

For every `y != 0`, the denominator is positive and `M_1(y) != 0`, hence

\[
\boxed{
G_1(\omega)\ge L_1(\omega\tau)>0
\qquad\text{for every }\omega\ne0.
}
\]

Combining this with the exact DC result,

\[
\boxed{
G_1(0)=0,
\qquad
G_1(\omega)>0\ \text{for every }\omega\ne0.
}
\]

Thus a continuous-time paralyzable detector can be **completely locally blind to uniform intensity while retaining temporal information at every nonzero frequency**.

This is the continuous-time counterpart of the discrete Type-II information-high-pass theorem, but it no longer relies on binning or a Bernoulli approximation.

### Small-frequency lower-bound scaling

Expanding around zero,

\[
\boxed{
L_1(y)
=\frac{y^2}{4(e-2)}+O(y^4).
}
\]

So the rigorous surviving-information bound opens quadratically away from the DC information zero.

### A concrete finite-frequency bound

At

\[
\omega=\frac{\pi}{\tau},
\]

`sin(pi)=0` and `cos(pi)=-1`, hence

\[
\boxed{
G_1(\pi/\tau)
\ge
\frac1e\left(1+\frac4{\pi^2}\right)
\approx0.51697536.
}
\]

Therefore more than 51% of the incident local Fisher information is guaranteed to survive at this finite temporal frequency despite **zero complete-record DC Fisher information**.

---

## 8. Exact complete-record renewal-score representation

The lower bound above is not the definition of `G`. The complete output process admits an exact renewal-score representation.

Let `k_epsilon(T,d)` be the conditional density of the next recorded interval `D=d` given a recorded event at absolute time `T`. For a complex mode, stationarity of the baseline implies

\[
\partial_\epsilon\log k_\epsilon(T,D)|_{\epsilon=0}
=e^{i\omega T}A_D(\omega),
\]

where `A_D(omega)` is the exact transition score conditioned on the observed interval.

Because `k_epsilon(T,.)` is normalized for every `epsilon`,

\[
\boxed{E[A_D(\omega)]=0.}
\]

At baseline the successive intervals are iid, so cross-interval score covariances vanish. The exact complexified Fisher rate is therefore

\[
\dot F_{\rm out}(\omega)
=r\,E|A_D(\omega)|^2.
\]

Since the incident complex-mode Fisher rate is `lambda`,

\[
\boxed{
G_\rho(\omega)
=e^{-\rho}E|A_D(\omega)|^2.
}
\]

This expression is exact; the difficulty is evaluating the conditional interval score in closed form.

A useful latent representation is

\[
A_D(\omega)
=E\!\left[
\sum_{j=1}^{N}e^{i\omega S_j}
\,\middle|\,D
\right]
-\lambda\frac{e^{i\omega D}-1}{i\omega},
\]

where `S_N=D` is the final incident arrival (the next recorded event) and the earlier `S_j` are hidden cluster arrivals.

---

## 9. Exact high-frequency limit

Conditional on `D`, the final recorded arrival contributes the atom `e^{i omega D}`. The hidden-arrival conditional mean measure inside `(0,D)` is absolutely continuous. Its Fourier transform therefore vanishes by the Riemann--Lebesgue lemma as `|omega| -> infinity`. The compensator term is `O(1/|omega|)`.

The stopped gap count `N` is geometric with success probability `e^{-rho}`, so it has finite second moment. This supplies the required uniform integrability for dominated convergence in the exact score representation.

Consequently

\[
A_D(\omega)-e^{i\omega D}\to0
\quad\text{in }L^2,
\]

and

\[
E|A_D(\omega)|^2\to1.
\]

Therefore

\[
\boxed{
\lim_{|\omega|\to\infty}G_\rho(\omega)
=e^{-\rho}.
}
\]

At the paralysis maximum,

\[
\boxed{
\lim_{|\omega|\to\infty}G_1(\omega)=e^{-1}\approx0.367879.
}
\]

This is an exact complete-record limit, not merely the Fourier-statistic lower bound.

Interpretation: at very high temporal frequency the hidden-cluster contributions average away, while the directly observed cluster-start arrivals retain the instantaneous source phase. The asymptotic information fraction equals the fraction `r/lambda=e^{-rho}` of incident events that appear as recorded cluster starts.

---

## 10. Numerical exact-spectrum cross-check

The first-order interval-density equation can be solved as a causal Volterra renewal equation. At `lambda=tau=1`, with baseline first-arrival density `g(v)=e^{-v}`, let

\[
h_\omega(v)
=e^{i\omega v}-\frac{e^{i\omega v}-1}{i\omega}.
\]

The baseline next-output density satisfies

\[
k_0(d)
=e^{-d}\mathbf 1_{d>1}
+\int_0^{\min(1,d)}e^{-v}k_0(d-v)\,dv,
\]

and its first-order complex-mode derivative satisfies

\[
\begin{aligned}
k_1(d)=&\ e^{-d}h_\omega(d)\mathbf 1_{d>1}\\
&+\int_0^{\min(1,d)}e^{-v}
\left[h_\omega(v)k_0(d-v)
+e^{i\omega v}k_1(d-v)\right]dv.
\end{aligned}
\]

Then

\[
\boxed{
G_1(\omega)
=e^{-1}\int_1^\infty
\frac{|k_1(d)|^2}{k_0(d)}\,dd.
}
\]

Grid refinement gives, approximately,

- `G_1(0.5/tau) ~ 0.0973`,
- `G_1(1/tau) ~ 0.2649`,
- `G_1(pi/tau) ~ 0.5281`,

while the rigorous lower bound at `pi/tau` is `0.51698`.

These numerical values are validation only. The theorem does not depend on them.

---

## 11. Prior-art boundary

Important close literature already identified:

1. **Teich and Vannucci (1978), JOSA 68, 1338--1342, DOI `10.1364/JOSA.68.001338`.** They derive dead-time-modified photocounting distributions for modulated laser radiation and include a paralyzable result. This establishes that modulated paralyzable count statistics are old; our mean modulation relation must not be advertised as new.

2. **Teich and Cantor (1978), IEEE JQE 14, 993--1003, DOI `10.1109/JQE.1978.1069731`.** They study likelihood-ratio detection, mutual information, channel capacity, and imaging for **nonparalyzable** dead-time-perturbed doubly stochastic Poisson counting systems. This is important information-theoretic prior art.

3. **Jorgensen and Johnson (2026), arXiv:2605.23210.** They establish LAN/Fisher-information rates for nonparalyzable dead-time event detection with arbitrary causal gating and explicitly list paralyzable/Type-II dead time as future work.

4. Classical renewal/dead-time literature contains the output count-rate law, interval statistics, count distributions, and power spectra. None of those ingredients is a novelty claim.

The candidate new contribution requiring deeper search is the **complete-record local temporal Fisher-spectrum statement**: exact DC nonidentifiability at the paralyzable maximum combined with rigorous positive Fisher retention at every nonzero temporal frequency and the exact high-frequency information fraction.

No `first` or priority claim is yet permitted.

---

## 12. Significance if novelty survives

The standard high-flux intuition uses the count-rate curve

\[
r(\lambda)=\lambda e^{-\lambda\tau}
\]

and regards `rho=1` as the point where small intensity changes become undetectable because the count-rate slope vanishes.

The complete-record Fisher result shows that statement is profoundly task dependent:

\[
\boxed{
\text{DC direction: zero information}
\quad\text{but}\quad
\text{every nonzero temporal frequency: positive information}.
}
\]

Moreover,

\[
\boxed{
\lim_{|\omega|\to\infty}G_1(\omega)=e^{-1}.
}
\]

Thus a detector can be at the **maximum of its paralysis curve** while retaining a finite asymptotic fraction of information about arbitrarily rapid weak temporal modulation.

This cannot be represented by a scalar `dead time`, count-rate slope, or conventional low-pass bandwidth.

---

## 13. Next gates

1. Deep search specifically for complete-timestamp Fisher/LAN results for continuous paralyzable counters and modulation-frequency-resolved information.
2. Formalize DQM/increasing-window assumptions for the renewal score theorem and the general autonomous-channel spectral theorem.
3. Verify the Volterra exact-spectrum calculation with an independent implementation and convergence table.
4. Determine whether the continuous `G_1(omega)` itself has monotonicity/oscillation theorems; unlike the discrete one-bin model, preliminary numerics suggest a rise followed by damped oscillation toward `e^{-1}` rather than strict monotonicity.
5. Generalize from a deterministic dead interval to a recovery-time distribution and ask which features of the spectral-survival theorem persist.
6. Search for a resource/order theorem separating **predictable** dead time from **hidden/retriggered** dead time.
