# WP8 — UV non-Gaussian instability of the Gaussian free-energy frontier

**Date:** 2026-08-20

## Executive result

A previous WP8 statement said that squeezed-thermal Gaussian pointers are globally/local optimal sufficiently close to thermal equilibrium. That statement is **too strong in the unrestricted infinite-dimensional oscillator**.

Corrected result:

> The Gaussian branch gives the correct regular/BKM near-equilibrium asymptotics, but for every strictly positive free-energy budget `D_0>0` there exist arbitrarily high-Fock, centered non-Gaussian coherence perturbations that increase SLD displacement QFI at the same free-energy budget.

Thus the Gaussian state is **not an exact local maximum in the full oscillator state space for any `D_0>0`**.

The advantage is nonperturbatively small as `D_0 -> 0`, so the earlier Gaussian leading-order expansion remains useful and correct within regular finite-energy tangent families.

This result exposes an ultraviolet-tail hidden resource/regularity issue in the free-energy-only formulation.

---

# 1. Gaussian stationary point

Let the Gaussian free-energy optimum be

\[
\rho_\mu
\propto
\exp(\log\tau-uX^2),
\qquad
\mu>\vartheta,
\]

with

\[
u=\frac{\mu^2-\vartheta^2}{2\vartheta}.
\]

In the squeezed basis, `rho_mu` is thermal:

\[
\rho_\mu=(1-q)\sum_{n=0}^\infty q^n|n\rangle\langle n|,
\qquad q=e^{-\mu}.
\]

The physical generator and SLD become

\[
P_{\rm phys}=gP,
\qquad
g=\sqrt{\mu/\vartheta},
\]

\[
L_0=2t g X,
\qquad
t=\tanh(\mu/2)=\frac{1-q}{1+q}.
\]

The Gaussian state is an exact first-order stationary point of

\[
J_X-\lambda_GD(\rho\Vert\tau)
\]

with

\[
\boxed{
\lambda_G
=\frac{8\mu^2\tanh^2(\mu/2)}
{\vartheta(\mu^2-\vartheta^2)}.
}
\]

This equality is equivalent to the exact Gaussian relation

\[
K_{L_0}=\lambda_G(\log\rho_\mu-\log\tau)+cI.
\]

---

# 2. Exact second variation of SLD QFI

For a Hermitian traceless perturbation `delta rho`, define

\[
C[\delta\rho]
=2i[\delta\rho,P_{\rm phys}]
-\{\delta\rho,L_0\}.
\]

Linearizing the SLD variational problem gives the exact QFI Hessian

\[
\boxed{
\delta^2J_X
=\sum_{ij}
\frac{|C_{ij}|^2}{r_i+r_j},
}
\]

where

\[
r_n=(1-q)q^n.
\]

The relative-entropy Hessian is the BKM metric

\[
\boxed{
\delta^2D
=\sum_{ij}|\delta\rho_{ij}|^2
\frac{\ln r_i-\ln r_j}{r_i-r_j},
}
\]

with the diagonal coefficient understood as `1/r_i`.

Hence local constrained stability is controlled by

\[
\delta^2J_X-\lambda_G\delta^2D.
\]

---

# 3. Adjacent-coherence test mode

Take the normalized symmetric adjacent coherence

\[
B_n
=\frac{|n\rangle\langle n+1|
+|n+1\rangle\langle n|}{\sqrt2}.
\]

It is traceless and obeys

\[
\operatorname{Tr}(B_nX^2)=0,
\]

so it is tangent to the free-energy surface to first order because

\[
\delta D\propto\delta\langle X^2\rangle.
\]

Direct evaluation of the two Hessians yields the exact ratio

\[
\boxed{
R_n(\mu,\vartheta)
\equiv
\frac{\delta^2J_X[B_n]}
{\delta^2D[B_n]}
=
\frac{8(1-q)}{\vartheta}
\left[
 n\frac{1+q+q^2}{(1+q)(1+q^2)}
+
\frac{1+q+3q^2+q^3}
{(1+q)^2(1+q^2)}
\right],
}
\]

where `q=e^{-mu}`.

Therefore

\[
\boxed{
R_n
=\alpha(\mu,\vartheta)n+O(1),
}
\]

with

\[
\boxed{
\alpha(\mu,\vartheta)
=
\frac{8(1-e^{-\mu})}{\vartheta}
\frac{1+e^{-\mu}+e^{-2\mu}}
{(1+e^{-\mu})(1+e^{-2\mu})}>0.
}
\]

Thus

\[
\boxed{R_n\to\infty\quad(n\to\infty).}
\]

**Status:** PROVED exactly.

---

# 4. Removing the trivial first-moment loophole

A single `B_n` changes the pointer mean `X`, so one might suspect the instability is only a useless coherent displacement of the apparatus. It is not.

Choose two well-separated adjacent pairs, for example `m=n+4`, and define

\[
\delta\rho_n
=B_n-c_nB_m,
\]

with

\[
\boxed{
c_n=\sqrt{\frac{n+1}{m+1}}}
\]

so that

\[
\operatorname{Tr}(\delta\rho_nX)=0.
\]

Because the perturbation is real symmetric,

\[
\operatorname{Tr}(\delta\rho_nP)=0.
\]

Each adjacent-coherence component separately obeys

\[
\operatorname{Tr}(B_kX^2)=0,
\]

hence

\[
\operatorname{Tr}(\delta\rho_nX^2)=0.
\]

The two local Hessian supports are disjoint for the chosen separation, so their quadratic contributions add. The centered perturbation therefore has a Hessian ratio that is a positive weighted average of `R_n` and `R_m`.

Since both diverge linearly with `n`,

\[
\boxed{
\frac{\delta^2J_X[\delta\rho_n]}
{\delta^2D[\delta\rho_n]}
\to\infty.
}
\]

Thus the instability survives after imposing

\[
\operatorname{Tr}\delta\rho=0,
\quad
\delta\langle X\rangle=0,
\quad
\delta\langle P\rangle=0,
\quad
\delta\langle X^2\rangle=0.
\]

It is not a mean-displacement artifact.

---

# 5. Consequence: Gaussian exact local optimality fails for every D_0 > 0

For every nonzero Gaussian preparation budget, `mu>vartheta` and therefore `lambda_G` is finite.

Because `R_n -> infinity`, choose sufficiently large `n` such that

\[
R_n>\lambda_G.
\]

Then the centered tangent perturbation above has

\[
\boxed{
\delta^2J_X
-\lambda_G\delta^2D>0.
}
\]

The Gaussian state is therefore not a constrained local maximum in the unrestricted oscillator state space.

Because `rho_mu` is faithful, the perturbation amplitude can always be chosen small enough to preserve positivity. A compensating `O(epsilon^2)` shift along the Gaussian resource direction keeps the relative entropy exactly fixed while preserving the positive QFI improvement.

Hence

\[
\boxed{
D_0>0
\Longrightarrow
\text{the exact unrestricted optimum is non-Gaussian.}
}
\]

under the ideal infinite-dimensional harmonic-pointer model.

**Status:** PROVED local non-Gaussian improvement for every positive budget.

---

# 6. Why the regular Gaussian near-equilibrium expansion still works

As `D_0 -> 0`, the Gaussian multiplier diverges:

\[
\lambda_G\sim\frac{c_G}{2\sqrt{D_0}}.
\]

To beat the Gaussian Hessian one needs roughly

\[
n\gtrsim\lambda_G/\alpha
=O(D_0^{-1/2}).
\]

But the Gaussian thermal tail at that level is

\[
r_n\sim e^{-\mu n}
\sim
\exp[-C/\sqrt{D_0}].
\]

Positivity forces the usable coherence amplitude to shrink with this exponentially small tail weight. Consequently the non-Gaussian gain is itself nonperturbative in the near-equilibrium limit, schematically

\[
\Delta J_{\rm NG}
\sim
\exp[-C/\sqrt{D_0}]
\]

up to algebraic factors.

Therefore the squeezed-thermal state remains asymptotically optimal to ordinary algebraic orders in the regular near-equilibrium expansion even though it is **never exactly optimal at any finite `D_0>0`** in the unrestricted oscillator.

This resolves the apparent tension with the previous BKM first-order analysis.

---

# 7. Correction to previous WP8 language

The statement in `WP8_LOCAL_GAUSSIAN_OPTIMALITY.md` that Gaussian states are globally optimal to leading order near equilibrium remains valid only in the following qualified sense:

- Gaussian squeezing is the steepest **regular perturbative** direction and gives the correct leading algebraic expansion;
- it is not an exact neighborhood of global Gaussian optimality in the full infinite-dimensional state space;
- UV-tail coherence perturbations provide exponentially small non-Gaussian improvements for every positive budget.

Accordingly, any future publication must avoid claiming a finite interval `0<D_0<D_c` of exact global Gaussian optimality unless an additional UV/energy-support regularity constraint is imposed.

---

# 8. Physical interpretation: a new hidden-resource regularity

Relative entropy/free energy controls the *average thermodynamic preparation cost*, but it does not forbid infinitesimal coherent structure in arbitrarily high-energy tails.

SLD displacement QFI is highly sensitive to such coherences because the generator matrix elements grow as

\[
|\langle n|P|n+1\rangle|\sim\sqrt n.
\]

Thus free energy alone does not regularize the local metrological curvature uniformly over the oscillator Hilbert space.

Possible physical repair resources include:

- a hard maximum excitation or finite spectral support;
- a bound on a higher energy moment `Tr(rho H^{1+epsilon})`;
- preparation-channel bandwidth/complexity constraints;
- bounded coherence at high energy;
- finite Hilbert-space detector models;
- a microscopic anharmonic cutoff.

This is analogous in spirit to the earlier Markov `rare-fast-state` loophole: a resource can be hidden in a sector carrying vanishing stationary weight.

Here the hidden sector is an **ultraviolet, vanishing-probability quantum tail**.

---

# 9. Relation to parity bifurcation result

`WP8_GAUSSIAN_PARITY_BIFURCATION.md` remains correct **within its explicit two-parameter squeezed/parity-reweighted family**. Its threshold

\[
D_c\approx0.00481024
\]

at `vartheta=ln 2` is the point where a *macroscopic binary parity-bias mode* becomes locally favorable.

It is **not** the exact global onset of non-Gaussianity, because the UV coherence instability proved here occurs for every positive budget.

Thus there are two distinct phenomena:

1. exponentially weak UV-tail non-Gaussian improvement for arbitrarily small `D_0`;
2. a finite-resource parity bifurcation where a simple low-complexity non-Gaussian structure becomes favorable by an algebraically visible amount.

This distinction should be preserved.

---

# 10. Next step

1. Determine the weakest physically natural UV regularizer that restores a finite Gaussian-optimal neighborhood.
2. Test whether a second energy moment or a hard excitation cutoff suffices.
3. Quantify how the cutoff scale enters the photodetection bandwidth theorem.
4. Compare this UV-tail effect with known unbounded-generator pathologies in infinite-dimensional quantum metrology and quantum-information geometry before making novelty claims.