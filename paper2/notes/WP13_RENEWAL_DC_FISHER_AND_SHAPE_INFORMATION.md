# WP13 — Exact DC Fisher Rate for Renewal Outputs and the Information Hidden Beyond Count Rate

**Status:** exact renewal-process Fisher formula plus a rigorous count-statistic lower bound. This formalizes the distinction exposed by WP11/WP12 between mean-rate sensitivity and interval-shape information.

## 1. Setting

Let the complete detector output under a homogeneous source parameter `epsilon` be a stationary renewal point process with iid interior inter-recording intervals

\[
D_i\sim k_\epsilon(d)\,dd,
\]

with finite mean and variance near `epsilon=0`.

The source is a Poisson process of baseline rate `lambda` under a **fractional DC perturbation**

\[
\lambda_\epsilon=\lambda(1+\epsilon).
\]

The incident Fisher-information rate is therefore

\[
\boxed{\dot F_{\rm in}=\lambda.}
\]

Let

\[
r_\epsilon=\frac{1}{E_\epsilon[D]}
\]

be the stationary output event rate, and write `r=r_0`.

Assume ordinary DQM/regularity for the interval-density family, with interval score

\[
\boxed{
a(D)=\partial_\epsilon\log k_\epsilon(D)|_{\epsilon=0}.
}
\]

Then

\[
E[a(D)]=0.
\]

---

## 2. Exact complete-timestamp Fisher rate

Over a long observation window, the interior renewal intervals contribute likelihood

\[
\prod_i k_\epsilon(D_i).
\]

The equilibrium first/last censored intervals contribute only `O(1)` Fisher information under the usual finite-moment regularity and therefore vanish after division by observation time.

The asymptotic score is thus a sum of iid interval scores,

\[
S_T
=\sum_{i=1}^{N_T}a(D_i)+O_{L^2}(1).
\]

Because the interval scores have zero mean, cross terms vanish. The renewal theorem gives `N_T/T -> r`, hence

\[
\boxed{
\dot F_{\rm out}^{\rm DC}
=r\,E[a(D)^2].
}
\]

Normalizing by the incident Poisson FI rate gives the exact DC retention

\[
\boxed{
G(0)
=\frac r\lambda
E\!\left[
\left(\partial_\epsilon\log k_\epsilon(D)|_0\right)^2
\right].
}
\]

This formula uses the **complete timestamp record**, not only the output count.

It is the zero-frequency renewal counterpart of WP07's transition-score representation

\[
G(\omega)=\frac r\lambda E|A_D(\omega)|^2.
\]

---

## 3. What the total count alone can guarantee

The renewal central limit theorem gives

\[
E[N_T]=rT+o(T),
\]

and

\[
\operatorname{Var}(N_T)
=r^3\sigma_D^2T+o(T),
\qquad
\sigma_D^2=\operatorname{Var}(D).
\]

For any statistic `Z`, Fisher information obeys

\[
F\ge\frac{(\partial_\epsilon E Z)^2}{\operatorname{Var}Z}.
\]

Applying this to `N_T` and dividing by `T` gives

\[
\dot F_{\rm out}^{\rm DC}
\ge
\frac{\dot r^2}{r^3\sigma_D^2},
\]

where

\[
\dot r=\partial_\epsilon r_\epsilon|_0.
\]

Therefore

\[
\boxed{
G(0)
\ge
\frac{\dot r^2}{\lambda r^3\sigma_D^2}.
}
\]

Writing the interval coefficient of variation

\[
\mathrm{CV}_D^2=r^2\sigma_D^2
\]

and

\[
\alpha_r=\partial_\epsilon\ln r_\epsilon|_0=\frac{\dot r}{r},
\]

this becomes

\[
\boxed{
G(0)
\ge
\frac r\lambda
\frac{\alpha_r^2}{\mathrm{CV}_D^2}.
}
\]

This is a rigorous **count-rate-statistic lower bound**, not generally an equality.

---

## 4. Count-rate blindness does not imply timestamp blindness

Suppose

\[
\boxed{\dot r=0.}
\]

Then the count-statistic lower bound vanishes:

\[
G_{\rm count\ witness}(0)=0.
\]

But the exact complete-record formula is

\[
G(0)=\frac r\lambda E[a(D)^2].
\]

Hence

\[
\boxed{
\dot r=0
\quad\not\Rightarrow\quad
G(0)=0.
}
\]

The exact criterion is

\[
\boxed{
G(0)=0
\iff
a(D)=0\ \text{a.s.}
}
\]

under the regular renewal model.

In words: complete DC information vanishes iff the **entire interval distribution** is locally stationary with respect to the source parameter, not merely its mean.

This formalizes the central distinction between **rate information** and **interval-shape information**.

---

## 5. Deterministic Type-II recovery

For fixed paralyzable dead time `tau`, the interval law depends on `lambda` only through

\[
r(\lambda)=\lambda e^{-\lambda\tau}.
\]

Thus

\[
k_\lambda(d)=k_{r(\lambda)}(d).
\]

At

\[
\lambda\tau=1,
\]

\[
\partial_\epsilon r=0.
\]

The chain rule then gives

\[
a(D)=0\quad\text{a.s.},
\]

and therefore

\[
\boxed{G_{\rm deterministic}(0)=0.}
\]

This recovers WP07/WP11 immediately from the general renewal formula.

---

## 6. Random recovery exposes shape information

For the generalized Type-II `M/G/infinity` cluster-start detector, every recovery law with mean `m` has the same mean rate

\[
r(\lambda)=\lambda e^{-\lambda m}.
\]

Therefore at

\[
\lambda m=1
\]

all such detectors satisfy

\[
\dot r=0.
\]

The count-rate witness is identically zero for all of them.

WP12 nevertheless proves that exponential recovery has a source-sensitive short-interval law, hence

\[
E[a(D)^2]>0
\]

and

\[
\boxed{G_{\rm exponential}(0)>0.}
\]

Thus the distinction is exactly:

- deterministic recovery: rate tangent zero **and interval-shape tangent zero**;
- exponential recovery: rate tangent zero but **interval-shape tangent nonzero**.

This is the cleanest current mathematical expression of the recovery-law resource.

---

## 7. A dimensionless shape-sensitivity functional

For any renewal-output detector define

\[
\boxed{
\mathcal J_{\rm int}
=E[a(D)^2].
}
\]

Then

\[
\boxed{G(0)=\frac r\lambda\mathcal J_{\rm int}.}
\]

`J_int` is the Fisher information in one observed interval about the fractional source perturbation.

At a rate extremum `dot r=0`, `J_int` measures information that survives **entirely through interval shape**.

This notation may be useful internally, but do not promote it as a new named resource unless it proves useful beyond renewal models; per-sample Fisher information is standard statistics.

---

## 8. Implication for detector characterization

A static detector characterization that measures only

\[
r(\lambda)
\]

cannot determine complete DC information.

Even augmenting the curve with its local slope does not solve the problem. Two detectors may have identical `r(lambda)` and identical `dr/dlambda` at every operating point while possessing different interval-density score functions and therefore different `G(0)`.

WP12 provides an explicit pair with identical mean Type-II paralysis curves but zero versus positive complete-record DC FI at the shared maximum.

Thus

\[
\boxed{
\text{mean transfer curve}
\not\Rightarrow
\text{complete statistical transfer}.
}
\]

This is the zero-frequency analogue of Paper 1's statement that FWHM does not determine temporal information bandwidth.

---

## 9. Prior-art boundary

The following are standard and not novelty claims:

- Fisher information rate of iid/renewal samples;
- renewal CLT for `N_T`;
- information inequality `(dE Z/dtheta)^2/Var Z`;
- interval-shape estimation in renewal processes;
- Type-II interval distributions.

The candidate Paper-2 contribution is the use of this exact renewal FI structure to establish **physical detector inequivalence under identical paralysis curves** and to connect the static shape information to the general temporal Fisher spectrum.

---

## 10. Next use

1. Use the exact formula to compute or tightly bound `G_exp(0)` for the exponential-recovery `M/M/infinity` example.
2. Derive sufficient/necessary conditions on a recovery distribution for `a(D)=0` at `lambda m=1`.
3. Search whether complete Type-II interval likelihood identifiability has been analyzed explicitly in counter theory.
4. Generalize the interval-score formula to marked renewal outputs and semi-Markov output records.
