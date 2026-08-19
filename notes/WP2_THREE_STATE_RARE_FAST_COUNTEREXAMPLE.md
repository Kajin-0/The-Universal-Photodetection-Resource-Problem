# WP2 — Three-State Rare-Fast Counterexample

**Date:** 2026-08-19

## Executive result

A reversible three-state continuous-time Markov transducer can possess

- fixed incident optical signal scale;
- finite nonzero DC information transfer;
- uniformly bounded total stationary dynamical activity;
- uniformly bounded steady entropy-production rate;
- finite dark/background transition rates;

while its information-equivalent bandwidth

\[
B_{\mathcal I}=\int_{-\infty}^{\infty}\frac{d\omega}{2\pi}\eta_{\mathcal I}(\omega)
\]

grows at least linearly with an internal kinetic parameter \(R\to\infty\).

Therefore **stationary activity plus net entropy-production rate are not sufficient resources to upper-bound broadband optical information transfer in the abstract reversible Markov class**.

The mechanism is a rare fast state: its stationary occupation falls as \(R^{-1}\), hiding \(O(R)\) transition rates from stationary traffic. Unlike the two-state directed construction, net entropy production can also remain finite because two edge affinities diverge with opposite signs while the total cycle affinity remains finite.

The construction exposes a missing resource: **edge-resolved energetic/affinity magnitude, kinetic prefactor/capacity, or an equivalent microscopic coupling scale**.

**Status:** COUNTEREXAMPLE for the abstract reversible Markov resource set \(\{\mathcal A_{\rm tot},\sigma\}\). Photodetection-specific microscopic admissibility with fixed optical transition energy/coupling remains OPEN.

---

# 1. Reversible unicyclic model

States:

- \(0\): ready state;
- \(1\): rare fast intermediate;
- \(2\): post-readout/reset state.

All rates below are strictly positive.

Signal-facing edge:

\[
0\xrightleftharpoons[cR]{u}1.
\]

Counted readout edge:

\[
1\xrightleftharpoons[q]{R}2.
\]

Reset edge:

\[
2\xrightleftharpoons[s]{b}0.
\]

Here \(u,b,q,s,c>0\) are fixed and \(R>0\) is the kinetic scaling parameter. The forward \(1\to2\) jump is the measured electrical count.

The optical signal perturbs only the forward signal-facing rate,

\[
u(t)=u+\kappa\,\delta\Phi(t),
\]

and for the coherent-photon specialization we take

\[
u=\alpha\Phi_0,\qquad \kappa=\alpha.
\]

Using the column-vector convention, the generator is

\[
W_R=
\begin{pmatrix}
-(u+s) & cR & b\\
u & -(c+1)R & q\\
s & R & -(q+b)
\end{pmatrix}.
\]

---

# 2. Exact stationary distribution

Define

\[
D_0=bc+b+cq+cs+s+u,
\]

\[
D_1=bu+qs+qu,
\]

\[
P_0=bc+b+cq,
\qquad
P_2=cs+s+u.
\]

The normalization denominator is

\[
D_R=R D_0+D_1.
\]

Direct solution of \(W_R\pi=0\) gives

\[
\boxed{
\pi_0=\frac{R P_0}{D_R},
\qquad
\pi_1=\frac{D_1}{D_R},
\qquad
\pi_2=\frac{R P_2}{D_R}.
}
\]

Therefore

\[
\pi_0\to \frac{P_0}{D_0},
\qquad
\pi_1\sim \frac{D_1}{R D_0},
\qquad
\pi_2\to \frac{P_2}{D_0}.
\]

The fast intermediate state is occupied only \(O(R^{-1})\) of the time.

**Status:** PROVED.

---

# 3. Count rate remains finite

Counting the \(1\to2\) forward edge with unit increment,

\[
\boxed{
\bar I_R=R\pi_1=\frac{R D_1}{R D_0+D_1}.
}
\]

Hence

\[
\boxed{
\bar I_R\to I_\infty=\frac{D_1}{D_0}>0.
}
\]

Although the microscopic counted rate is \(R\), the rare occupation of state 1 makes the stationary output count rate finite.

---

# 4. Total stationary activity is bounded

Using total one-way jump traffic

\[
\mathcal A_R
=\sum_i\pi_i\sum_{j\neq i}W_{ji},
\]

we obtain

\[
\mathcal A_R
=(u+s)\pi_0+(c+1)R\pi_1+(q+b)\pi_2.
\]

Thus

\[
\boxed{
\mathcal A_R
=\frac{R\left[(u+s)P_0+(c+1)D_1+(q+b)P_2\right]}
{R D_0+D_1}.
}
\]

Consequently,

\[
\boxed{
\mathcal A_R\to
\mathcal A_\infty
=\frac{(u+s)P_0+(c+1)D_1+(q+b)P_2}{D_0}<\infty.
}
\]

**Status:** PROVED.

---

# 5. Net entropy production is bounded

The steady cycle current is the same on every edge. On the counted edge,

\[
J_R=R\pi_1-q\pi_2.
\]

Substitution gives

\[
\boxed{
J_R
=\frac{R(ub-cqs)}{R D_0+D_1}
\to
J_\infty=\frac{ub-cqs}{D_0}.
}
\]

The cycle affinity is

\[
\mathcal F_R
=\ln\frac{u\,R\,b}{(cR)q s}
=\boxed{\ln\frac{ub}{cqs}},
\]

which is independent of \(R\).

The dimensionless steady entropy-production rate is therefore

\[
\boxed{
\sigma_R
=J_R\ln\frac{ub}{cqs}
\to
\frac{ub-cqs}{D_0}\ln\frac{ub}{cqs}<\infty.
}
\]

As usual, \((x-y)\ln(x/y)\ge0\), so \(\sigma_R\ge0\).

**Status:** PROVED.

---

# 6. Where the thermodynamic cost is hidden

Although the *cycle* affinity is fixed, two individual rate-ratio affinities diverge:

\[
\ln\frac{u}{cR}=-\ln R+O(1),
\]

\[
\ln\frac{R}{q}=+\ln R+O(1),
\]

while

\[
\ln\frac{b}{s}=O(1).
\]

Their \(\pm\ln R\) contributions cancel in the cycle sum.

Thus finite **net entropy production** does not imply bounded microscopic thermodynamic forces, energy gaps, chemical potentials, biases, or local detailed-balance increments.

This is not an algebraic pathology. It is exactly why total entropy production is too coarse to serve as the sole energetic resource in a broadband detector theorem.

---

# 7. High-frequency response survives up to \(O(R)\)

Let the input perturb the forward signal rate \(u\). Consider frequencies scaling with the fast kinetic rate,

\[
\omega=Rx,
\qquad x\neq0\ \text{fixed}.
\]

On the \(1/R\) time scale, the slow states 0 and 2 are effectively frozen while state 1 relaxes through its \((c+1)R\) total fast escape rate. The linearized state-1 equation gives

\[
\delta p_1(Rx)
=\frac{\pi_0}{R(c+1+ix)}\,\delta u+o(R^{-1}).
\]

The measured forward count rate is \(I=R p_1\), so

\[
\boxed{
\chi_{Iu}(Rx)
\to
\frac{\pi_{0,\infty}}{c+1+ix}
=\frac{P_0/D_0}{c+1+ix}.
}
\]

For photon-flux response,

\[
\boxed{
\chi_{I\Phi}(Rx)
\to
\frac{\alpha P_0/D_0}{c+1+ix}.
}
\]

The response does not vanish when the observation frequency is increased proportionally to \(R\).

**Status:** PROVED by singular-resolvent scaling for fixed \(x\neq0\); independently verified numerically from the full resolvent.

---

# 8. High-frequency count noise tends to finite shot noise

The counted jump operator is

\[
\mathcal J_R=R|2\rangle\langle1|.
\]

The singular self-correlation contribution to the two-sided PSD is exactly \(\bar I_R\). After a counted jump the system is in state 2. Return from state 2 to the rare fast state 1 occurs through the fixed rate \(q\), so the correlated-repeat contribution at \(\omega=Rx\) is \(O(R^{-1})\).

Therefore

\[
\boxed{
S_I(Rx)\to I_\infty=\frac{D_1}{D_0}
}
\]

for every fixed \(x\neq0\).

**Status:** PROVED by resolvent scaling; independently verified numerically.

---

# 9. Nonzero information efficiency over an expanding frequency interval

For coherent/Poisson illumination,

\[
\eta_{\mathcal I}(\omega)
=\Phi_0\frac{|\chi_{I\Phi}(\omega)|^2}{S_I(\omega)}.
\]

Using \(u=\alpha\Phi_0\), the scaled-frequency limit is

\[
\boxed{
\eta_{\infty}(x)
\equiv
\lim_{R\to\infty}\eta_{\mathcal I}(Rx)
=
\frac{\alpha u\,\pi_{0,\infty}^2}
{I_\infty\left[(c+1)^2+x^2\right]}.
}
\]

Equivalently,

\[
\boxed{
\eta_{\infty}(x)
=
\frac{\alpha u P_0^2}
{D_0D_1\left[(c+1)^2+x^2\right]}.
}
\]

For all finite \(x\), this is strictly positive.

Take any compact interval \(x\in[x_1,x_2]\) with \(0<x_1<x_2<\infty\). Uniform convergence on such an interval implies that for sufficiently large \(R\), \(\eta_{\mathcal I}(Rx)\) is bounded below by a positive constant. Consequently,

\[
B_{\mathcal I}(R)
\ge
\frac{R}{\pi}\int_{x_1}^{x_2}dx\,\eta_{\mathcal I}(Rx),
\]

and therefore

\[
\boxed{
B_{\mathcal I}(R)\to\infty
\quad\text{at least linearly in }R.
}
\]

Thus no finite function

\[
B_{\mathcal I}\le f(\mathcal A_{\rm tot},\sigma)
\]

can hold over this model family if \(f\) depends only on finite stationary activity and net EPR.

**Status:** COUNTEREXAMPLE / PROVED asymptotic divergence.

---

# 10. Leading bandwidth coefficient

Matched asymptotics and direct numerical integration indicate the stronger limit

\[
\boxed{
\frac{B_{\mathcal I}(R)}{R}
\to
\frac{\alpha u\,\pi_{0,\infty}^2}
{2I_\infty(c+1)}
=
\frac{\alpha u P_0^2}
{2(c+1)D_0D_1}.
}
\]

This follows formally by integrating the scaled Lorentzian limit

\[
\int_{-\infty}^{\infty}\frac{dx}{2\pi}
\frac{1}{(c+1)^2+x^2}
=\frac{1}{2(c+1)}.
\]

A fully uniform dominated-convergence proof across the low-frequency boundary layer is still to be written, so the exact coefficient is labeled **VERIFIED**, while linear divergence itself is **PROVED**.

---

# 11. Numerical unit test

Use

\[
u=0.2,\quad b=0.7,\quad q=0.3,\quad s=0.1,
\quad c=2,\quad \alpha=0.5.
\]

Then

\[
D_0=3.2,
\qquad
D_1=0.23,
\qquad
P_0=2.7.
\]

The asymptotic stationary metrics are

\[
\pi_{0,\infty}=0.84375,
\]

\[
I_\infty=0.071875,
\]

\[
\mathcal A_\infty=0.625,
\]

\[
\mathcal F=\ln(2.333333\ldots)=0.84729786\ldots,
\]

\[
J_\infty=0.025,
\]

\[
\sigma_\infty=0.02118245\ldots.
\]

The predicted bandwidth coefficient is

\[
\boxed{
\lim_{R\to\infty}\frac{B_{\mathcal I}}{R}
=0.1650815217\ldots
}
\]

Direct numerical evaluation of the exact finite-state resolvent/PSD gives:

| \(R\) | \(B_{\mathcal I}\) | \(B_{\mathcal I}/R\) |
|---:|---:|---:|
| 10 | 1.632324 | 0.1632324 |
| 30 | 4.933890 | 0.1644630 |
| 100 | 16.489574 | 0.1648957 |
| 300 | 49.505872 | 0.1650196 |
| 1000 | 165.062935 | 0.1650629 |

At \(R=1000\), the relative deviation from the predicted asymptotic coefficient is approximately \(1.13\times10^{-4}\).

Meanwhile \(\mathcal A_R\to0.625\) and \(\sigma_R\to0.02118245\), both finite.

**Status:** VERIFIED numerical check.

---

# 12. No conflict with known finite-frequency fluctuation-response inequalities

Recent finite-frequency FRIs bound the **pointwise** response precision for a specified perturbation by a perturbation Fisher/activity quantity. This counterexample does not violate such bounds: \(\eta_{\mathcal I}(\omega)\le1\) remains finite at every frequency.

The divergence comes from an interval of useful frequencies whose width grows as \(R\). A frequency-independent pointwise ceiling does not by itself limit

\[
\int d\omega\,\frac{|\chi(\omega)|^2}{S(\omega)}.
\]

Likewise, published frequency-integrated response inequalities commonly integrate \(|\chi|^2\) normalized by a **time-domain variance**, not the spectral-information ratio \(|\chi|^2/S(\omega)\). These are distinct objects.

This distinction must be maintained in all novelty claims.

---

# 13. Critical physical-admissibility caveat

The signal-facing reverse rate is \(cR\) while its forward baseline \(u\) is fixed. If that edge is literally interpreted as absorption/emission of a fixed-frequency optical mode with fixed microscopic coupling and occupation, the scaling may violate Einstein/detailed-balance relations for that optical reservoir.

Therefore the result presently proves insufficiency of \(\{\mathcal A,\sigma\}\) for the **abstract reversible Markov transducer class**, not yet for a fully microscopic fixed-\(\hbar\omega\) photodetector class.

The divergent individual affinities also imply unbounded edge-resolved energy/free-energy scales under ordinary local-detailed-balance interpretations. This is likely the physically missing resource rather than a defect to hide.

**Status:** OPEN physical embedding.

---

# 14. Consequence for the Universal Photodetection Resource Problem

The original candidate resource set was already broader than \(\{\mathcal A,\sigma\}\). This counterexample now shows why.

A credible universal bound will likely need at least one quantity that sees **latent kinetic capacity or local energetic scale**, for example:

- maximum/suitable norm of transition escape rates;
- edge-resolved activity rather than only total stationary activity;
- maximum local thermodynamic force / maximum log rate ratio;
- absolute free-energy or heat throughput rather than signed/net entropy production alone;
- bath spectral-density/coupling norm;
- transition matrix-element or linewidth sum rule;
- generator norm, spectral diameter, or another kinetic-capacity functional;
- microscopic optical oscillator-strength / absorption sum-rule constraints.

The next problem is to determine which of these is fundamental and which merely parameterizes a model.

---

# 15. Immediate next target

Construct a stronger model in which

1. the optical transition energy \(\hbar\omega_{\rm opt}\) is fixed;
2. the signal-facing absorption/emission channel obeys a physically fixed reservoir relation;
3. the detector remains finite-temperature and reversible;
4. all incident optical resources are fixed;
5. internal kinetic rates are allowed to vary;
6. activity and net EPR remain bounded if possible.

Then determine whether broadband information can still diverge.

If it can, the missing resource is genuinely internal/microscopic. If it cannot, the optical detailed-balance constraint may be the key ingredient that converts the abstract counterexample into a finite photodetection bound.
