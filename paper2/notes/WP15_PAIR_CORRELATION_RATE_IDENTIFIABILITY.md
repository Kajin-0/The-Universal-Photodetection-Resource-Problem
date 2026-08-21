# WP15 — Exact Pair-Correlation Rate Identifiability for Random Type-II Recovery

**Status:** exact operational corollary of WP13. It makes the deterministic-recovery uniqueness theorem directly measurable from second-order timestamp statistics. Pair-correlation methods for dead-time inversion are established prior art; the potentially distinctive point is the exact generalized-Type-II identity and its deterministic-vs-random identifiability consequence.

## 1. Setup

Use the generalized iid Type-II detector of WP13.

Incident events are Poisson with rate `lambda`. Each incident event starts an iid recovery interval `T` with known CDF `F`, survival `bar F`, finite mean

\[
m=E[T],
\]

integrated survival

\[
A(t)=E[\min(T,t)]
=\int_0^t\bar F(u)du,
\]

and stop-loss / residual-tail transform

\[
\boxed{
R(t)=m-A(t)=E[(T-t)_+].}
\]

The stationary registered-event rate is

\[
\boxed{r=\lambda e^{-\lambda m}.}
\]

WP13 derived the exact renewal density conditioned on a registered event at the origin:

\[
\boxed{
U_\lambda(t)=\lambda F(t)e^{-\lambda A(t)},
\qquad t>0.}
\]

---

## 2. Exact output pair-correlation function

For a stationary simple renewal process of rate `r`, the second-order product density at positive lag is

\[
\rho^{(2)}(0,t)=rU_\lambda(t).
\]

Therefore the normalized pair-correlation function is

\[
\boxed{
g_Y^{(2)}(t)
=\frac{U_\lambda(t)}r.}
\]

Substituting the Type-II formulas for `U_lambda` and `r` gives the exact identity

\[
\boxed{
g_Y^{(2)}(t)
=F(t)\exp\!\left[\lambda\{m-A(t)\}\right]
=F(t)e^{\lambda R(t)}.}
\]

No low-rate approximation is used.

This identity separates the two recovery features at lag `t`:

- `F(t)`: probability that an individual recovery interval has already completed;
- `R(t)=E[(T-t)_+]`: mean residual recovery tail beyond that lag.

---

## 3. One-lag exact inversion of the incident rate

Suppose the recovery law is known and choose any lag `t` satisfying

\[
F(t)>0,
\qquad
R(t)>0.
\]

Then

\[
\boxed{
\lambda
=\frac{\ln[g_Y^{(2)}(t)/F(t)]}{R(t)}.}
\]

Thus **one exact pair-correlation value at one suitable lag globally identifies the incident Poisson rate**, independent of whether the conventional mean count-rate curve is locally flat or globally double-valued.

At the common paralysis maximum `lambda*m=1`, the formula remains nonsingular. Hence the apparent static ambiguity of the mean output characteristic is removed by second-order timestamp structure whenever the recovery law has an overlap region with both completed and still-active recovery intervals.

A two-lag form that avoids writing the long-lag normalization explicitly is

\[
\boxed{
\lambda
=
\frac{
\ln\!\left[
U(t_1)F(t_2)/(U(t_2)F(t_1))
\right]
}{A(t_2)-A(t_1)},}
\]

for `F(t_j)>0` and `A(t_1) != A(t_2)`.

---

## 4. Why every nondegenerate recovery law admits an informative lag

For a genuinely nondegenerate positive recovery law, there exists a lag `t` in an overlap region such that

\[
0<F(t)<1.
\]

Then automatically

\[
F(t)>0
\]

and

\[
R(t)=E[(T-t)_+]>0.
\]

Therefore the one-lag inversion applies.

This gives an operational form of WP13's global injectivity theorem:

\[
\boxed{
T\text{ nondegenerate and known}
\Longrightarrow
\lambda\text{ is identifiable from }g_Y^{(2)}(t)
\text{ at a suitable single lag}.}
\]

---

## 5. Deterministic recovery is exactly the exceptional case

If

\[
T=m\quad\text{a.s.},
\]

then

\[
F(t)=0\quad(t<m),
\]

whereas

\[
R(t)=0\quad(t\ge m).
\]

There is **no lag** for which both `F(t)>0` and `R(t)>0`.

The pair correlation becomes

\[
\boxed{
g_Y^{(2)}(t)=
\begin{cases}
0,&0<t<m,\\
1,&t\ge m.
\end{cases}}
\]

It is independent of the incident rate `lambda`. All static rate dependence collapses into the scalar output rate

\[
r=\lambda e^{-\lambda m},
\]

which is double-valued below its maximum.

Thus deterministic recovery is not merely a special case in which the inversion formula happens to fail numerically. It is exactly the case in which **all pair-correlation structure beyond the hard exclusion gap loses incident-rate dependence**.

This makes the Lambert-W branch aliasing of WP11/WP13 operationally transparent.

---

## 6. Exponential-recovery example

For

\[
T\sim\operatorname{Exp}(\mu),
\qquad m=1/\mu,
\]

\[
F(t)=1-e^{-\mu t},
\qquad
R(t)=\frac{e^{-\mu t}}\mu.
\]

Therefore

\[
\boxed{
g_Y^{(2)}(t)
=(1-e^{-\mu t})
\exp\!\left[\frac\lambda\mu e^{-\mu t}\right].}
\]

At any finite `t>0`, both factors needed for inversion are nonzero, and

\[
\boxed{
\lambda
=\mu e^{\mu t}
\ln\!\left[
\frac{g_Y^{(2)}(t)}{1-e^{-\mu t}}
\right].}
\]

In particular this remains exact at `lambda=mu`, where

\[
\frac{dr}{d\lambda}=0.
\]

The information surviving at the paralysis maximum can therefore be understood directly as sensitivity of pair structure, not mean count rate.

---

## 7. Relation to the Fisher theorem

WP15 is an **identifiability/operational corollary**, not a substitute for the complete Fisher result.

A pair-correlation estimate is only one statistic of the full timestamp record. The full DC Fisher information of WP13 is

\[
G(0)=\frac r\lambda I_D,
\]

and WP14 gives rigorous lower bounds from bounded interval statistics.

The significance of WP15 is that it gives an exact closed-form observable showing *where* the missing rate information goes when the mean paralysis curve becomes flat.

---

## 8. Important prior art: pair-correlation dead-time inversion is not new

M. L. Larsen and A. B. Kostinski,

**“Dead-time corrections for non-Poisson data,”**
*Measurement Science and Technology* **20**, 095101 (2009),
DOI `10.1088/0957-0233/20/9/095101`,

explicitly develop dead-time corrections using pair-correlation functions. They consider both non-extensible and extensible dead time, derive relations between waiting-time statistics and pair correlations, and use measured pair-correlation information to improve estimates of the underlying event rate and variance-to-mean ratio.

For a Poisson source with fixed extensible dead time, their measured pair correlation is the familiar hard exclusion followed by zero excess correlation, consistent with the deterministic special case above.

Therefore Paper 2 must **not** claim:

- first use of pair correlations to correct dead time;
- first recovery of source rate from second-order dead-time statistics;
- first observation that dead time changes pair correlations.

The potentially distinctive contribution is narrower:

> for the generalized iid Type-II recovery class, the exact identity `g_Y^(2)(t)=F(t) exp[lambda E[(T-t)_+]]` makes incident-rate identifiability explicit and shows that deterministic recovery is uniquely the case in which no informative overlap lag exists.

Even this narrower point needs continued priority auditing.

---

## 9. Design/metrology interpretation

Under a known recovery law, conventional calibration by mean count rate can fail catastrophically near paralysis because

\[
r'(\lambda)=0.
\]

The exact pair statistic does not share that failure for nondegenerate recovery.

This suggests a practical hierarchy of detector characterization:

\[
\text{mean count curve}
\subset
\text{pair correlation}
\subset
\text{complete timestamp likelihood/Fisher information}.
\]

The hierarchy is an instance of data processing: each step discards less of the event record.

---

## 10. Next gates

1. Search older dead-time/correlation literature for the exact random-Type-II pair identity or equivalent formulas.
2. Derive sampling variance / asymptotic efficiency of the one-lag inversion only if it can be done without distracting from the complete Fisher theory.
3. Investigate whether several pair-correlation lags can jointly identify both `lambda` and unknown low-dimensional recovery-law parameters.
4. Do not elevate pair-correlation inversion above the complete Fisher-spectrum theorem; it is an applied interpretation of the deeper result.
