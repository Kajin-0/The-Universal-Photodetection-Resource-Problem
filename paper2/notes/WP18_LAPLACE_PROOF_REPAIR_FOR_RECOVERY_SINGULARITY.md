# WP18 — Laplace-Statistic Proof Repair for Deterministic-Recovery Fisher Singularity

**Status:** proof hardening of WP13/WP14. The class-wide deterministic-recovery uniqueness result can be proved without the delicate step “zero interval score implies pointwise zero derivative of the renewal density.” A bounded Laplace statistic gives a cleaner contradiction. This also clarifies the exact renewal-likelihood regularity needed and separates the static Fisher-information rate from the a.e.-defined general WP10 multiplier at `omega=0`.

This work package changes no numerical result.

---

## 1. Terminology correction: define static DC retention separately

WP10 produces an `L^infty` Fourier multiplier

\[
G_{\Phi_0,K}(\omega)
\]

only up to equality almost everywhere. A value at the single point `omega=0` is therefore not intrinsically defined by the universal theorem unless a model-specific continuous representative or a static/narrowband identification has been proved.

For the homogeneous source-rate experiment considered in WP13, define instead the **static DC Fisher-retention rate**

\[
\boxed{
\mathcal G_{\rm DC}
\equiv
\lim_{L\to\infty}
\frac{
F_{\rm out}^{[0,L]}(\epsilon)
}{
\lambda L
}
}
\]

for the fractional incident-rate tangent

\[
\lambda_\epsilon=\lambda(1+\epsilon),
\]

whenever the limit exists.

The incident Poisson FI rate for this tangent is exactly `lambda`.

For a regular renewal output with inter-registration interval `D`, interval score

\[
a(D)=\partial_\epsilon\log f_\epsilon(D)|_0,
\]

and

\[
I_D=E[a(D)^2],
\]

standard renewal likelihood theory gives

\[
\boxed{
\mathcal G_{\rm DC}
=\frac r\lambda I_D.
}
\]

In a model where the Fisher spectrum has a continuous representative at zero, this static rate agrees with the natural `G(0)` notation. Until that identification is explicitly made, `mathcal G_DC` is the safer symbol for WP13's homogeneous experiment.

### Renewal-likelihood reference

Zhao and Nagaraja, **“Fisher information in window censored renewal process data and its applications,”** *Annals of the Institute of Statistical Mathematics* **63**, 791–825 (2011), DOI `10.1007/s10463-009-0252-2`, derive exact and asymptotic FI for a stationary/random-origin renewal process observed in a finite window. This is a more directly matched citation than an informal appeal to iid intervals.

For the theorem below, simply assume the ordinary regularity needed for

\[
F_{\rm out}^{[0,L]}/L\to r I_D,
\]

rather than claiming it for every finite-mean recovery law without qualification.

---

## 2. Generalized iid Type-II model

Incident events are homogeneous Poisson of rate `lambda`.

Each incident event starts an iid recovery interval `T` with fixed distribution function `F` and finite positive mean

\[
\boxed{m=E[T]\in(0,\infty).}
\]

The detector is dead whenever at least one event-generated recovery interval is active. Registered events are starts of `M/G/infinity` busy clusters and form a renewal process.

The classical output rate is

\[
\boxed{r(\lambda)=\lambda e^{-\lambda m}.}
\]

The common paralysis maximum is

\[
\boxed{\lambda_*=1/m,\qquad r_*=1/(em).}
\]

Classical `M/G/infinity` busy-cycle theory gives the registered-event renewal density

\[
\boxed{
U_\lambda(t)
=\lambda F(t)e^{-\lambda A(t)},
}
\]

with

\[
A(t)=\int_0^t[1-F(v)]dv
=E[\min(T,t)].
\]

WP16 establishes that this renewal-density identity is prior art and must not be claimed as a new result.

Define the residual/stop-loss function

\[
\boxed{
R(t)=m-A(t)=E[(T-t)_+],
}
\]

and at the common maximum

\[
\boxed{
g(t)=R(t)/m=1-A(t)/m.}
\]

---

## 3. Laplace transforms of the renewal and interval laws

For `s>0`, define the renewal-density Laplace transform

\[
\boxed{
u_s(\lambda)
=\int_0^\infty e^{-st}U_\lambda(t)dt.}
\]

Let

\[
\boxed{\phi_s(\lambda)=E_\lambda[e^{-sD}]}
\]

be the Laplace transform of one observed inter-registration interval.

The standard renewal identity

\[
U=f_D+f_D*f_D+\cdots
\]

gives

\[
\boxed{
u_s=\frac{\phi_s}{1-\phi_s}}
\]

and equivalently

\[
\boxed{
\phi_s=\frac{u_s}{1+u_s}.}
\]

The statistic

\[
Z_s=e^{-sD}
\]

is bounded in `[0,1]`. This boundedness is the key to the proof repair.

---

## 4. Exact fractional-rate derivative of the Laplace transform

Use the fractional rate parameter

\[
\lambda_\epsilon=\lambda(1+\epsilon).
\]

For fixed recovery law `F`,

\[
\partial_\epsilon U_{\lambda_\epsilon}(t)|_0
=U_\lambda(t)[1-\lambda A(t)].
\]

At

\[
\lambda=\lambda_*=1/m,
\]

this becomes

\[
\boxed{
\dot U_*(t)=U_*(t)g(t)
=U_*(t)\frac{R(t)}m.}
\]

For every fixed `s>0`, differentiation under the integral for `u_s` is elementary. In a small neighborhood of `lambda_*`,

- `0<=A(t)<=m`;
- `U_lambda(t)<=lambda`;
- `|1-lambda A(t)|` is uniformly bounded;
- `e^{-st}` is integrable.

Hence dominated convergence yields

\[
\boxed{
\dot u_s
=W_s
\equiv
\int_0^\infty
 e^{-st}U_*(t)g(t)dt.}
\]

Differentiating

\[
\phi_s=\frac{u_s}{1+u_s}
\]

gives

\[
\boxed{
\dot\phi_s
=\frac{W_s}{(1+u_s)^2}.}
\]

This identity is exact.

---

## 5. Nondegenerate recovery implies `W_s>0` for every `s>0`

The integrand defining `W_s` is nonnegative.

If `T` is genuinely nondegenerate, its essential lower and upper support endpoints are distinct. Therefore there exist real numbers `a<b` such that

\[
P(T\le a)>0,
\qquad
P(T>b)>0.
\]

For every `t in [a,b]`,

\[
F(t)\ge P(T\le a)>0,
\]

while

\[
R(t)=E[(T-t)_+]
\ge E[(T-b)_+]>0.
\]

Hence on an interval of positive Lebesgue measure,

\[
U_*(t)>0,
\qquad
g(t)>0.
\]

Since `e^{-st}>0`,

\[
\boxed{
T\text{ nondegenerate}
\Longrightarrow
W_s>0
\quad\forall s>0.}
\]

Conversely, if

\[
T=m\quad\text{a.s.},
\]

then `F(t)=0` for `t<m`, while `R(t)=0` for `t>=m`, so

\[
\boxed{W_s=0\quad\forall s>0.}
\]

Thus

\[
\boxed{
W_s=0\ \text{for one/every }s>0
\iff
T=m\ \text{a.s.}}
\]

within the positive finite-mean class.

---

## 6. Repaired necessity proof using only a bounded statistic

Assume the stationary renewal experiment is DQM in the fractional source-rate parameter and has the standard per-time FI reduction

\[
\mathcal G_{\rm DC}=\frac r\lambda I_D.
\]

At the paralysis maximum `r_*>0`. Suppose

\[
\boxed{\mathcal G_{\rm DC}=0.}
\]

Then

\[
I_D=0.
\]

Therefore the interval score satisfies

\[
a(D)=0\quad\text{a.s.}
\]

For any bounded interval statistic `Z`, the score identity gives

\[
\partial_\epsilon E_\epsilon[Z]|_0
=E[Za(D)]
=0.
\]

Choose the bounded statistic

\[
Z_s=e^{-sD}.
\]

Then

\[
\boxed{\dot\phi_s=0.}
\]

But the exact classical-renewal calculation above gives

\[
\dot\phi_s
=\frac{W_s}{(1+u_s)^2}.
\]

The denominator is finite and strictly positive for `s>0`. Hence

\[
W_s=0.
\]

Section 5 then forces

\[
\boxed{T=m\quad\text{a.s.}}
\]

This proves necessity without ever asserting pointwise differentiability of `f_D(t)` or pointwise equality `dot U(t)=0` as a consequence of zero Fisher information.

---

## 7. Sufficiency for deterministic recovery

If

\[
T=m\quad\text{a.s.},
\]

then the deterministic Type-II inter-registration transform is

\[
\widetilde f_D(s)
=\frac{r(\lambda)e^{-sm}}
{s+r(\lambda)e^{-sm}},
\]

so the **entire homogeneous interval law depends on `lambda` only through**

\[
r(\lambda)=\lambda e^{-\lambda m}.
\]

At

\[
\lambda m=1,
\]

the fractional derivative of `r` is zero. Hence the interval score vanishes and

\[
\boxed{\mathcal G_{\rm DC}=0.}
\]

Combining with the repaired necessity proof gives

\[
\boxed{
\mathcal G_{\rm DC}=0
\iff
T=m\quad\text{a.s.}}
\]

under the stated renewal-DQM/FI-rate regularity.

---

## 8. Why this proof is stronger than the original WP13 necessity argument

The original proof route was:

`G_DC=0 -> I_D=0 -> interval score zero -> dot U_*(t)=0 pointwise -> deterministic T`.

The vulnerable step is the transition from zero DQM score to a pointwise derivative of a renewal density. It can be justified under enough common-density regularity, but a hostile referee can reasonably demand details, especially for mixed/atomic recovery laws or parameter-dependent zero-density sets.

The repaired proof uses only:

1. standard DQM score identity for the **bounded** statistic `exp(-sD)`;
2. the classical renewal Laplace identity;
3. the exact classical busy-cycle renewal density;
4. dominated differentiation of an exponentially weighted integral;
5. positivity of the stop-loss overlap.

No pointwise density derivative is inferred from Fisher information.

Recommended manuscript proof: use the repaired Laplace-statistic route.

---

## 9. Quantitative lower bound follows from the same statistic

The same bounded statistic gives the WP14 information inequality

\[
I_D
\ge
\frac{\dot\phi_s^2}
{\operatorname{Var}(e^{-sD})}.
\]

Since

\[
\dot\phi_s=\frac{W_s}{(1+u_s)^2},
\]

\[
\boxed{
I_D
\ge
\frac{W_s^2}
{(1+u_s)^4[\phi_{2s}-\phi_s^2]}.}
\]

At the common maximum

\[
\frac{r_*}{\lambda_*}=e^{-1},
\]

so

\[
\boxed{
\mathcal G_{\rm DC}
\ge
\frac1e
\frac{W_s^2}
{(1+u_s)^4[\phi_{2s}-\phi_s^2]}.}
\]

Using `Var(Z)<=1/4` for `Z in [0,1]`,

\[
\boxed{
\mathcal G_{\rm DC}
\ge
\frac4e\frac{W_s^2}{(1+u_s)^4}.}
\]

Thus the strict uniqueness theorem and quantitative witness now share one proof mechanism.

---

## 10. Global branch-aliasing uniqueness can also be simplified

WP16 established that the stationary random-paralyzable pair-correlation formula

\[
\boxed{
g_Y^{(2)}(t)=F(t)e^{\lambda R(t)}}
\]

is prior art, following directly from Apanasovich and Paltsev (1995) after stationary specialization and normalization.

This old formula yields an extremely short proof of the global uniqueness corollary.

Take two distinct rates `lambda_1 != lambda_2` with the same conventional registered rate

\[
\lambda_1e^{-\lambda_1m}
=\lambda_2e^{-\lambda_2m}.
\]

If their complete stationary output laws are equal, their pair-correlation functions are equal. Hence for every lag with `F(t)>0`,

\[
e^{\lambda_1R(t)}=e^{\lambda_2R(t)}.
\]

Since the rates are distinct,

\[
R(t)=0
\]

wherever `F(t)>0`.

A nondegenerate recovery law has an interval on which both `F(t)>0` and `R(t)>0`, contradiction. Therefore

\[
T=m\quad\text{a.s.}
\]

is necessary.

Conversely deterministic recovery has a complete interval law depending on `lambda` only through `r(lambda)`, so equal-rate Lambert-W branches have identical full renewal laws.

Therefore

\[
\boxed{
\begin{array}{c}
\lambda_1\ne\lambda_2,\ r(\lambda_1)=r(\lambda_2),\\
\mathcal L_{\lambda_1}(Y)=\mathcal L_{\lambda_2}(Y)
\end{array}
\iff
T=m\ \text{a.s.}}
\]

for fixed known recovery law.

### Positioning consequence

Because the necessity half is now an immediate corollary of a 1995 second-order formula, do **not** oversell the global branch-aliasing uniqueness theorem as deep new stochastic-process theory. Its strongest role is as the global identifiability counterpart of the local Fisher singularity.

---

## 11. Regularity assumptions to state explicitly in any manuscript

The stochastic-process identities `r(lambda)`, `U_lambda(t)`, `g^(2)(t)`, and the global full-law injectivity argument do not require the same FI regularity as the local Fisher theorem.

For

\[
\mathcal G_{\rm DC}=\frac r\lambda I_D
\]

and the zero-IFF-deterministic Fisher theorem, assume explicitly that:

1. the inter-registration family is DQM at the operating rate for the fractional source-rate parameter;
2. the interval Fisher information `I_D` is finite;
3. the stationary/window-censored renewal experiment has asymptotic FI rate `r I_D`, i.e. boundary/censoring terms are `o(L)` in Fisher information.

These are standard renewal-likelihood conditions, but they should be hypotheses rather than silently inferred from `E[T]<infinity` alone.

In particular, do not claim that finite mean recovery by itself guarantees every second-moment/boundary condition used by a particular FI-rate theorem. Heavy-tailed recovery laws may require separate treatment.

The strict identifiability statement based on the classical pair correlation is broader than the current regular Fisher theorem.

---

## 12. Recommended hierarchy after the proof repair

### Broad stochastic identifiability statement

For any fixed known nondegenerate recovery law with finite positive mean, the classical second-order registered-timestamp structure depends nontrivially on `lambda` at every overlap lag. Deterministic recovery is the unique case with no overlap lag.

### Regular Fisher theorem

Within the regular iid-recovery Type-II subclass satisfying renewal DQM and the per-time FI reduction,

\[
\boxed{
\mathcal G_{\rm DC}=0
\iff
T=m\ \text{a.s.}}
\]

at `lambda*m=1`.

### Quantitative theorem

For every `s>0`,

\[
\mathcal G_{\rm DC}
\ge
\frac4e\frac{W_s^2}{(1+u_s)^4},
\]

with strict positivity for every nondegenerate recovery law.

This hierarchy is more rigorous than presenting one theorem as if finite-mean recovery automatically supplied every statistical regularity condition.

---

## 13. Novelty posture after the repair

The repaired proof makes the theorem stronger mathematically but **does not increase novelty confidence**.

The ingredients are classical:

- `M/G/infinity` busy-cycle renewal density;
- renewal Laplace-transform identity;
- DQM score identity;
- FI of renewal/window-censored observations;
- stop-loss transforms;
- random-paralyzable pair correlation.

The candidate distinctive statement remains the photodetection information consequence:

> among equal-mean iid Type-II recovery laws sharing exactly the same conventional paralysis curve, deterministic recovery is uniquely Fisher-singular at the common paralysis maximum; every nondegenerate recovery law retains static information in interval shape.

WP16's unresolved inverse-output historical search remains the priority obstacle to any priority language.

---

## 14. Next action

1. Use this repaired Laplace proof, not the original pointwise-density necessity argument, in any manuscript draft.
2. Keep `mathcal G_DC` notation until a model-specific theorem identifies it with a continuous representative of the general spectral multiplier at `omega=0`.
3. Continue the Afanaseva–Mikhailova (1973) historical audit.
4. If the historical theorem survives, then test whether a same-mean/same-variance recovery no-go adds real value; otherwise stop expanding the random-recovery branch.
