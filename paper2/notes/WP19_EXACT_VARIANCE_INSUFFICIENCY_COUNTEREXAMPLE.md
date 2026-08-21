# WP19 — Exact Same-Mean/Same-Variance Recovery Information No-Go

**Status:** rigorous counterexample at the level of the accessible timestamp information channel, with converged full-interval-Fisher numerics. This replaces the handoff-only gamma/lognormal evidence with a durable analytic construction.

The exact theorem below does **not** claim that a scalar full DC Fisher information can never accidentally coincide for two equal-variance laws. It proves the stronger structural point needed by the resource program: **mean and variance do not determine the local registered-timestamp statistical experiment or its accessible Fisher information under coarse-graining.** A converged Volterra calculation additionally shows that the complete static Fisher rates differ for this explicit pair.

---

## 1. Two recovery laws with exactly the same mean and variance

Scale the mean recovery to

\[
E[T]=1.
\]

Define recovery law A by

\[
\boxed{
P(T_A=1/2)=1/2,
\qquad
P(T_A=3/2)=1/2.}
\]

Then

\[
E[T_A]=1,
\qquad
\operatorname{Var}(T_A)=1/4.
\]

Define recovery law B by

\[
\boxed{
P(T_B=1/4)=2/9,
\quad
P(T_B=1)=5/9,
\quad
P(T_B=7/4)=2/9.}
\]

Its mean is

\[
E[T_B]
=\frac29\frac14+\frac59+\frac29\frac74
=1,
\]

and its variance is

\[
\operatorname{Var}(T_B)
=\frac29\left(\frac34\right)^2
+\frac29\left(\frac34\right)^2
=\frac14.
\]

Thus both laws have exactly

\[
\boxed{
E[T]=1,
\qquad
\operatorname{Var}(T)=1/4,
\qquad
\mathrm{CV}=1/2.}
\]

They also have the identical generalized-Type-II conventional count-rate curve

\[
\boxed{
r(\lambda)=\lambda e^{-\lambda}}
\]

for every `lambda`, with common paralysis maximum at

\[
\lambda_*=1,
\qquad
r_*=e^{-1}.
\]

Therefore **mean recovery, recovery variance/CV, the complete mean saturation curve, its maximum, and its zero slope are all identical** for the two detectors.

---

## 2. Their stationary pair structures are analytically different

Classical random-paralyzable correlation theory gives

\[
\boxed{
g_Y^{(2)}(t)=F(t)e^{\lambda R(t)},}
\qquad
R(t)=E[(T-t)_+].
\]

As established in WP16, this formula is prior art and must be credited to the older random-dead-time literature, particularly Apanasovich and Paltsev (1995).

Evaluate it at the shared operating point

\[
\lambda=1
\]

and lag

\[
t=3/4.
\]

### Law A

At `t=3/4`,

\[
F_A(3/4)=1/2,
\]

and only the `T=3/2` branch contributes residual recovery:

\[
R_A(3/4)
=\frac12\left(\frac32-\frac34\right)
=\frac38.
\]

Hence

\[
\boxed{
g_A^{(2)}(3/4)=\frac12 e^{3/8}}
\]

or numerically

\[
g_A^{(2)}(3/4)\approx0.7274957073.
\]

### Law B

At the same lag,

\[
F_B(3/4)=2/9,
\]

while

\[
R_B(3/4)
=\frac59\left(1-\frac34\right)
+\frac29\left(\frac74-\frac34\right)
=\frac{13}{36}.
\]

Therefore

\[
\boxed{
g_B^{(2)}(3/4)=\frac29 e^{13/36}}
\]

or numerically

\[
g_B^{(2)}(3/4)\approx0.3188717529.
\]

Thus

\[
\boxed{
g_A^{(2)}(3/4)\ne g_B^{(2)}(3/4)}
\]

despite exact equality of mean and variance of `T` and equality of the entire conventional mean saturation curve.

This already proves that the complete stationary registered-timestamp law is not determined by `(E[T],Var(T))`.

---

## 3. Their local source-rate response is also analytically different

For the fractional source-rate tangent

\[
\lambda_\epsilon=\lambda(1+\epsilon),
\]

with recovery law held fixed,

\[
\partial_\epsilon g_Y^{(2)}(t)|_0
=\lambda R(t)g_Y^{(2)}(t).
\]

At `lambda=1`, `t=3/4`:

### Law A

\[
\boxed{
\dot g_A^{(2)}(3/4)
=\frac38\left(\frac12e^{3/8}\right)
\approx0.2728108902.}
\]

### Law B

\[
\boxed{
\dot g_B^{(2)}(3/4)
=\frac{13}{36}\left(\frac29e^{13/36}\right)
\approx0.1151481330.}
\]

Hence even the **local tangent of a directly observable second-order timestamp statistic** is not fixed by mean recovery plus variance.

This is an exact variance-insufficiency result at the local statistical-experiment level.

---

## 4. Stronger exact Fisher counterexample from a short-cycle binary statistic

The previous section proves different local output laws. We can go further and exhibit a specific accessible coarse-grained statistic with different Fisher information.

Let

\[
\delta=2/5
\]

and from one observed renewal interval `D` retain only

\[
\boxed{Z=\mathbf1\{D\le2/5\}.}
\]

### Law A: identically zero statistic

Every recovery interval under law A is at least `1/2`. A registered event at time zero starts such a recovery interval, so the next registered event cannot occur before `1/2`:

\[
D_A\ge1/2\quad\text{a.s.}
\]

Therefore for **every incident rate**

\[
\boxed{P(D_A\le2/5)=0.}
\]

The binary statistic is constant and has exactly zero Fisher information:

\[
\boxed{I_Z^{(A)}=0.}
\]

### Law B: exact positive Fisher information

Law B has minimum recovery `1/4`, so `D_B>=1/4`. Moreover `2/5<2(1/4)=1/2`; therefore before time `2/5` there can be at most one registered renewal after the origin. On this interval the ordinary inter-registration density equals the renewal density:

\[
f_D(t)=U_\lambda(t),
\qquad 1/4\le t\le2/5.
\]

For law B on this interval,

\[
F_B(t)=2/9,
\]

and

\[
A_B(t)
=\frac29\frac14+\frac79t
=\frac1{18}+\frac79t.
\]

Thus

\[
U_\lambda(t)
=\lambda\frac29
\exp\!\left[-\lambda\left(\frac1{18}+\frac79t\right)\right].
\]

Integrating exactly,

\[
\boxed{
p_B(\lambda)
\equiv P_\lambda(D_B\le2/5)
=\frac27\left[
e^{-\lambda/4}-e^{-11\lambda/30}
\right].}
\]

At the common paralysis maximum `lambda=1`,

\[
\boxed{
p_B\approx0.024502903710.}
\]

For the fractional rate tangent, the derivative is

\[
\boxed{
\dot p_B
=\frac27\left[
-\frac14e^{-1/4}
+\frac{11}{30}e^{-11/30}
\right]
\approx0.016975628075.}
\]

The Bernoulli Fisher information per observed renewal cycle is therefore

\[
\boxed{
I_Z^{(B)}
=\frac{\dot p_B^2}{p_B(1-p_B)}
\approx0.0120561368424.}
\]

Since registered cycles occur at rate `r_*=e^{-1}` and the incident fractional-rate FI rate is one at `lambda=1`, this one-bit-per-cycle statistic alone supplies the normalized per-time witness

\[
\boxed{
\mathcal G_{Z}^{(B)}
=e^{-1}I_Z^{(B)}
\approx0.00443520488427>0.}
\]

while

\[
\boxed{\mathcal G_Z^{(A)}=0.}
\]

Hence two recovery laws with the same mean and variance can allocate **strictly different Fisher information to the same accessible timestamp coarse-graining**.

This is an exact information-theoretic counterexample, not a numerical observation.

---

## 5. Exact no-go statement

The construction proves:

> **Same-mean/same-variance recovery-information no-go.** Within the generalized iid Type-II recovery class, the pair `(E[T],Var(T))` does not determine the complete stationary registered-timestamp experiment, its local source-rate tangent, or the Fisher information retained by all accessible timestamp statistics, even when the two detectors share exactly the same conventional mean saturation curve.

Equivalently, there is no universal reduction of the generalized Type-II recovery-information channel to

\[
\boxed{\{E[T],\operatorname{Var}(T)\}}
\]

alone.

The full integrated tail / stop-loss function

\[
R(t)=E[(T-t)_+]
\]

contains information not recoverable from the first two moments.

This is the rigorous version of the intuition behind WP14.

---

## 6. What this does and does not prove about scalar full DC Fisher information

The analytic theorem above is deliberately phrased at the **complete local experiment / accessible-statistic** level.

It proves that equal mean and variance do not determine all Fisher information carried by the timestamp record because a common deterministic coarse-graining has zero FI for law A and positive FI for law B.

It does **not by itself** logically exclude an accidental equality

\[
\mathcal G_{\rm DC}^{(A)}
=\mathcal G_{\rm DC}^{(B)}
\]

for the full timestamp likelihood after all interval information is combined.

The numerical calculation below strongly rejects such an accidental equality for this explicit pair, but that scalar inequality is presently a converged numerical result rather than an analytic theorem.

This distinction should be preserved in any manuscript.

---

## 7. Converged complete-interval Fisher calibration

A dedicated reproduction script was added:

- `paper2/numerics/same_mean_variance_recovery_fisher.py`

and its convergence data are stored in

- `paper2/numerics/same_mean_variance_recovery_fisher.csv`.

The solver uses the exact classical renewal density

\[
U(t)=F(t)e^{-A(t)}
\]

and tangent

\[
\dot U(t)=U(t)[1-A(t)]
\]

at `lambda=1`, then solves the renewal and tangent equations for the interval density by FFT-accelerated formal power-series inversion. The discretization has been cross-checked against the direct causal Volterra recurrence and reproduces the existing exponential-recovery benchmark.

At the finest stored grid

\[
h=3.125\times10^{-4},
\qquad T_{\max}=35,
\]

the calculations give:

### Law A

\[
\boxed{
I_D^{(A)}\approx0.04798857042,
\qquad
\mathcal G_{\rm DC}^{(A)}\approx0.01765400847.}
\]

### Law B

\[
\boxed{
I_D^{(B)}\approx0.05220280299,
\qquad
\mathcal G_{\rm DC}^{(B)}\approx0.01920433799.}
\]

The ratio at this grid is

\[
\boxed{
\frac{\mathcal G_{\rm DC}^{(B)}}
{\mathcal G_{\rm DC}^{(A)}}
\approx1.087817,}
\]

i.e. an approximately **8.78%** difference despite identical mean and variance of recovery.

The final grid refinement changes the two `G_DC` values by only about

- `4.75e-5` relative for law A;
- `1.33e-5` relative for law B;

while their separation is about `8.78e-2` relative.

Both numerical interval distributions satisfy at the finest grid:

\[
\int f_D\,dt=1+O(10^{-11})
\]

and

\[
E[D]=e+O(10^{-10}),
\]

as required by the common registered rate `r=e^{-1}`.

Thus the numerical evidence that full scalar DC FI differs is extremely strong and reproducible.

---

## 8. Why this is better than the gamma/lognormal handoff evidence

The previous handoff mentioned a gamma-versus-lognormal comparison at matched mean and CV, but that calculation was not durable in the repository.

WP19 replaces it with:

1. two finite-support laws whose mean and variance equality is exact algebra;
2. an exact pair-correlation distinction;
3. an exact local pair-response distinction;
4. an exact binary-statistic Fisher distinction;
5. a dedicated reproducible full-FI solver and convergence table.

There is no need to recover or rely on the missing gamma/lognormal calculation for the variance-insufficiency claim.

---

## 9. Novelty posture

Do not claim novelty for:

- the stop-loss transform;
- moment-indeterminacy of distributions in general;
- the random-paralyzable pair-correlation formula;
- the fact that two distributions with equal first two moments can differ in higher-order statistics.

The detector-specific contribution, if useful in Paper 2, is the resource-theory consequence:

> even after fixing mean recovery, recovery variance/CV, and the entire conventional Type-II mean input-output curve, the registered-timestamp information channel is not fixed; an explicit same-mean/same-variance pair has analytically different local timestamp Fisher content.

This is best presented as a **no-go for variance as a complete recovery resource**, not as a new theorem about probability distributions.

---

## 10. Research decision

The variance-insufficiency branch has now met the requested standard and should **stop expanding by default**.

We have a rigorous counterexample and reproducible scalar-FI calibration. Searching many more parametric recovery families would add little.

The next value lies elsewhere:

1. finish the historical inverse-output audit of WP16;
2. decide the final novelty status of the WP13 deterministic Fisher singularity;
3. harden or demote WP08;
4. then decide whether the combined WP10/WP07/WP13/WP19 stack warrants a manuscript.
