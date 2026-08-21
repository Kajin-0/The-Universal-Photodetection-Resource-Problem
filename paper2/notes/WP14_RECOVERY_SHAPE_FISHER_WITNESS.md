# WP14 — A Quantitative Recovery-Shape Witness for Static Fisher Information

**Status:** rigorous lower-bound theorem derived for the generalized iid Type-II class. This quantifies WP13's strict identifiability result without assuming a parametric recovery family. A numerical exponential/gamma calibration is supplied separately; no universal monotonicity with variance is claimed.

## 1. Setup

Use the generalized Type-II model of WP13. The recovery duration `T` has CDF `F`, survival `bar F`, and fixed finite mean

\[
m=E[T].
\]

At the common paralysis maximum

\[
\lambda_*=1/m,
\]

the registered-event rate is

\[
r_*=\lambda_*e^{-1}.
\]

Define

\[
A(t)=E[\min(T,t)]
=\int_0^t\bar F(u)du,
\]

and the exact recorded-event renewal density

\[
U_*(t)=\lambda_*F(t)e^{-A(t)/m}.
\]

WP13 showed that its fractional-rate derivative is

\[
\dot U_*(t)
=U_*(t)\left[1-\frac{A(t)}m\right].
\]

Introduce the dimensionless **residual-recovery shape function**

\[
\boxed{
g(t)
=1-\frac{A(t)}m
=\frac{m-A(t)}m
=\frac{E[(T-t)_+]}m.}
\]

Then

\[
\boxed{\dot U_*(t)=U_*(t)g(t).}
\]

`g(t)` is nonnegative. It measures how much mean recovery time remains beyond lag `t`.

---

## 2. Laplace witness

For `s>0`, define

\[
\boxed{
u_s
=\int_0^\infty e^{-st}U_*(t)dt,}
\]

and

\[
\boxed{
W_s
=\int_0^\infty e^{-st}U_*(t)g(t)dt
=\left.\partial_\epsilon u_s\right|_0.}
\]

Let `D` be one observed inter-recording interval and

\[
\phi_s=E[e^{-sD}].
\]

The renewal-transform identity gives

\[
\boxed{
\phi_s=\frac{u_s}{1+u_s}.}
\]

Differentiating,

\[
\boxed{
\dot\phi_s
=\frac{W_s}{(1+u_s)^2}.}
\]

Thus a nonzero `W_s` is already witnessed by the mean of the single bounded interval statistic `exp(-sD)`.

---

## 3. Fisher lower bound from one bounded statistic

Let `s_D(D)` be the complete one-interval score for the fractional incident-rate perturbation and

\[
I_D=E[s_D^2].
\]

The score identity / information inequality for any statistic `Z(D)` gives

\[
I_D
\ge
\frac{(\partial_\epsilon E[Z])^2}{\operatorname{Var}(Z)}.
\]

Choose

\[
Z=e^{-sD}\in[0,1].
\]

Then

\[
\operatorname{Var}(Z)
=\phi_{2s}-\phi_s^2,
\]

so the sharp one-statistic bound is

\[
\boxed{
I_D
\ge
\frac{W_s^2}
{(1+u_s)^4\,[\phi_{2s}-\phi_s^2]}.
}
\]

Since any `[0,1]` variable has variance at most `1/4`, a simpler distribution-free denominator gives

\[
\boxed{
I_D
\ge
4\frac{W_s^2}{(1+u_s)^4}.}
\]

At the paralysis maximum `r_*/lambda_*=e^{-1}`, the normalized complete-record DC Fisher retention therefore satisfies, for every `s>0`,

\[
\boxed{
G_*(0)
\ge
\frac1e
\frac{W_s^2}
{(1+u_s)^4\,[\phi_{2s}-\phi_s^2]},
}
\]

and in particular

\[
\boxed{
G_*(0)
\ge
\frac4e
\frac{W_s^2}{(1+u_s)^4}.}
\]

Taking the supremum over `s>0` gives an entirely recovery-law-defined lower bound.

---

## 4. Why the witness is exactly sensitive to recovery randomness

If recovery is deterministic,

\[
T=m\quad\text{a.s.},
\]

then `U_*(t)>0` only for `t>=m`, while

\[
g(t)=0\quad(t\ge m).
\]

Hence

\[
\boxed{W_s=0\quad\forall s>0.}
\]

Now suppose `T` is genuinely nondegenerate. Then there exists a set of positive Lebesgue measure on which

\[
F(t)>0
\quad\text{and}\quad
P(T>t)>0.
\]

On that set,

\[
U_*(t)>0,
\qquad
g(t)>0.
\]

Therefore

\[
\boxed{W_s>0\quad\forall s>0.}
\]

and the Fisher lower bound is strictly positive.

Thus `W_s` provides a quantitative witness for the exact WP13 dichotomy

\[
G_*(0)=0
\iff
T\text{ deterministic}.
\]

---

## 5. Interpretation as overlap of early completion and residual recovery

The integrand can be written explicitly as

\[
U_*(t)g(t)
=
\frac1m
F(t)e^{-A(t)/m}
\frac{E[(T-t)_+]}m.
\]

It is nonzero only where two features coexist:

1. some recovery intervals have already ended by `t` (`F(t)>0`), making short recorded cycles possible;
2. some recovery intervals still extend beyond `t` (`E[(T-t)_+]>0`), making the overlap statistics sensitive to incident flux.

This is the precise sense in which **recovery-law shape** creates static information invisible to the common mean paralysis curve.

The witness is not simply the variance of `T`. Two distributions with the same variance can have different stop-loss transforms `E[(T-t)_+]`; no variance-only information law is claimed.

---

## 6. Unique minimizer under a fixed mean

Since Fisher information is nonnegative and WP13 proves that zero occurs only for deterministic recovery,

\[
\boxed{
\inf_{F:\,E[T]=m}G_F(0)=0,
}
\]

and the infimum is uniquely attained by

\[
\boxed{F=\delta_m}
\]

within the regular iid-recovery Type-II class.

Therefore deterministic recovery is an **information-singular unique minimizer** of complete-record static Fisher retention at the common paralysis maximum.

This should not be paraphrased as “noise always helps.” It is a conditional statement at a specific operating point and under a fixed mean-recovery constraint: randomness breaks an exact deterministic aliasing symmetry.

---

## 7. Exponential recovery: exact witness ingredients

For

\[
T\sim\operatorname{Exp}(\mu),
\qquad m=1/\mu,
\]

at the shared maximum `lambda=mu`, use dimensionless time `x=mu t`. Then

\[
F=1-e^{-x},
\qquad
A/m=1-e^{-x},
\qquad
g=e^{-x},
\]

and

\[
\boxed{
U_*(t)
=\mu(1-e^{-x})e^{-(1-e^{-x})}.}
\]

The fractional derivative is particularly simple:

\[
\boxed{\dot U_*(t)=U_*(t)e^{-x}.}
\]

In dimensionless Laplace variable `z=s/mu`,

\[
u_z
=e^{-1}\int_0^1 q^{z-1}(1-q)e^q\,dq,
\]

and

\[
\boxed{W_z=u_{z+1}.}
\]

This gives an inexpensive exact one-dimensional evaluation of the witness bound.

---

## 8. Numerical calibration of the full DC FI

The exact renewal equation

\[
U=f_D+f_D*U
\]

and its parameter derivative were solved by converged Volterra quadrature for exponential recovery at `lambda=mu=1`.

The complete interval Fisher information converges to approximately

\[
I_D\approx0.18798493,
\]

so

\[
\boxed{
G_{\rm exp}(0)
=e^{-1}I_D
\approx0.0691558.}
\]

Thus exponential recovery retains about **6.9%** of incident static Fisher information exactly where deterministic recovery with the same mean is completely blind.

Representative grid convergence (`T_max=35/mu`):

| step `h*mu` | `G_exp(0)` |
|---:|---:|
| 0.01000 | 0.06915409 |
| 0.00500 | 0.06915537 |
| 0.00250 | 0.06915568 |
| 0.00125 | 0.06915576 |

The grid differences decrease by about a factor four under halving, consistent with the trapezoidal Volterra discretization. Extrapolation is near `0.06915579`.

This number is numerical validation/calibration, not needed for the strict-positive theorem.

---

## 9. Gamma-family exploration under fixed mean

For a mean-one gamma recovery law with shape `k` and rate `k`, `CV^2=1/k`. Numerical Volterra calculations at the common maximum `lambda=1` give approximately:

| shape `k` | `CV` | `G(0)` |
|---:|---:|---:|
| 0.5 | 1.414 | 0.1084 |
| 1 | 1.000 | 0.06916 |
| 2 | 0.707 | 0.03534 |
| 4 | 0.500 | 0.01412 |
| 8 | 0.354 | 0.00474 |
| 16 | 0.250 | 0.00148 |
| 32 | 0.177 | 0.000454 |
| 64 | 0.125 | 0.000143 |

Within this one parametric family, static FI decreases smoothly toward the deterministic limit as recovery dispersion shrinks.

**Do not generalize this numerical monotonicity to all recovery distributions.** WP13/WP14 prove only the unique zero/minimizer, not a variance ordering.

---

## 10. Novelty boundary

The following are standard or have close precedent:

- information inequality from a statistic;
- Laplace transforms of renewal laws;
- `M/G/infinity` busy-cycle transforms;
- stop-loss / integrated-tail functions;
- Fisher information in renewal intervals;
- comparisons of spike-timing and rate information.

The candidate distinctive result is the detector-specific synthesis:

> at the universal Type-II paralysis maximum, the overlap functional `W_s` gives a rigorous positive complete-record Fisher witness for every nondegenerate recovery law, while deterministic recovery is the unique zero/minimizer despite all laws sharing exactly the same mean saturation curve.

No priority claim yet.

---

## 11. Next gates

1. Add a reproduction script for exponential and gamma-family static FI convergence.
2. Search for an inverse/identifiability theorem in old `M/G/infinity` output-flow literature that may imply WP13's deterministic uniqueness result.
3. Derive a sharper closed lower bound in terms of a standard recovery-dispersion functional if possible.
4. Investigate two-point recovery laws to test whether variance ordering fails outside gamma families.
5. Explore optimization of `G(0)` over recovery laws with fixed mean plus a second constraint (variance, support, hazard ceiling).
