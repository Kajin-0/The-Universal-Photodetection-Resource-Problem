# WP8 — Gaussian-to-parity bifurcation in the squeezed parity-reweighted family

**Date:** 2026-08-20

## Purpose

`WP8_PARITY_REWEIGHT_INTERPOLATION.md` showed that reweighting only the even/odd populations of the thermal state beats the entire Gaussian free-energy frontier above `D≈0.01223` for `vartheta=ln 2`.

This note enlarges that construction to a two-parameter family that contains the exact Gaussian frontier and an independent parity bias. It reveals a **continuous local instability** of the Gaussian optimum at an even smaller free-energy budget.

The result is restricted to this analytically solvable two-parameter family; it is not yet a proof of the exact global arbitrary-state transition.

---

## 1. Gaussian-optimal quadratic tilt

Let

\[
\tau\propto e^{-\vartheta a^\dagger a}.
\]

The exact Gaussian free-energy/QFI optimum for displacement in `X` can be written

\[
\sigma_\mu
\propto
\exp(\log\tau-uX^2),
\]

where

\[
\mu\ge\vartheta,
\qquad
u\equiv u=\frac{\mu^2-\vartheta^2}{2\vartheta}.
\]

After the corresponding squeezing transformation, `sigma_mu` is a thermal state with effective Boltzmann factor

\[
Q=e^{-\mu}.
\]

Its natural even-parity probability is

\[
\boxed{
p_\mu=\frac1{1+e^{-\mu}}.
}
\]

---

## 2. Independent parity reweighting

Let `sigma_{mu,e}` and `sigma_{mu,o}` be the normalized even/odd conditional states of `sigma_mu`. Define

\[
\boxed{
\rho_{\mu,p}
=p\sigma_{\mu,e}+(1-p)\sigma_{\mu,o}.
}
\]

This family contains:

- the exact Gaussian frontier when `p=p_mu`;
- the simple thermal parity-reweight family when `mu=vartheta`;
- partially squeezed, partially parity-biased non-Gaussian pointers for general `(mu,p)`.

---

## 3. Closed-form QFI

In the squeezed number basis, the generator rescales as

\[
P\mapsto\sqrt{\mu/\vartheta}\,P'.
\]

Therefore

\[
\boxed{
J(\mu,p)
=\frac{\mu}{\vartheta}
J_{\rm pr}(p,e^{-\mu}),
}
\]

where

\[
J_{\rm pr}(p,Q)
=
\frac{2}{1-Q^2}
\left[
(2p-1)^2(1+Q^2)
+2\frac{[(1-p)-pQ^2]^2}{(1-p)+pQ^2}
\right].
\]

At `p=p_mu`,

\[
J_G(\mu)
=\frac{2\mu}{\vartheta}\tanh\frac\mu2,
\]

which is exactly the known Gaussian optimum.

---

## 4. Closed-form free-energy cost

Define

\[
A_e(\mu)=\frac12+\frac{2e^{-2\mu}}{1-e^{-2\mu}}.
\]

The `X^2` moment is

\[
\langle X^2\rangle_{\mu,p}
=\frac{\vartheta}{\mu}
\left[A_e(\mu)+(1-p)\right].
\]

The quadratic-tilt partition function is

\[
Z_\mu
=(1-e^{-\vartheta})
\frac{e^{(\vartheta-\mu)/2}}
{1-e^{-\mu}}.
\]

Since `rho_{mu,p}` differs from `sigma_mu` only by its binary parity weights,

\[
\boxed{
D(\mu,p)
=-\nu\langle X^2\rangle_{\mu,p}
-\ln Z_\mu
+D_{\rm bin}(p\Vert p_\mu).
}
\]

At `p=p_mu`, this reduces exactly to the Gaussian free-energy frontier `D_G(mu)`.

**Status:** PROVED.

---

## 5. First-order stationarity identity

At the Gaussian parity weight `p=p_mu`, direct differentiation gives

\[
\boxed{
D_p
=\frac{\mu^2-\vartheta^2}{2\mu},
}
\]

and

\[
\boxed{
J_p
=\frac{4\mu}{\vartheta}
\tanh^2\frac\mu2.
}
\]

The Gaussian tangent derivatives satisfy the exact identity

\[
\boxed{
\frac{J_p}{D_p}
=
\frac{J_\mu}{D_\mu}
=
\frac{dJ_G}{dD_G}
=
\frac{8\mu^2\tanh^2(\mu/2)}
{\vartheta(\mu^2-\vartheta^2)}.
}
\]

Thus adding parity bias to the Gaussian optimum is **first-order neutral once the free-energy constraint is enforced**.

This explains why a simple first-order/BKM argument cannot determine when non-Gaussian parity engineering becomes favorable.

---

## 6. Constrained second variation

For a fixed free-energy surface `D(mu,p)=D_0`, choose `p` as the local coordinate and let

\[
\mu'=-\frac{D_p}{D_\mu}.
\]

Let

\[
\lambda_G=\frac{J_\mu}{D_\mu}.
\]

The constrained second derivative of QFI along the parity-bias direction at `p=p_mu` is

\[
\boxed{
\mathcal C(\mu,\vartheta)
=
J_{pp}+2J_{p\mu}\mu'+J_{\mu\mu}(\mu')^2
-\lambda_G
\left[
D_{pp}+2D_{p\mu}\mu'+D_{\mu\mu}(\mu')^2
\right].
}
\]

Interpretation:

- `C<0`: Gaussian point is locally QFI-maximizing inside this two-parameter family;
- `C>0`: Gaussian point is locally unstable and a parity-biased non-Gaussian state increases QFI at the same free energy;
- `C=0`: bifurcation point.

All derivatives are analytic elementary functions of `(mu,vartheta)`. The explicit fully expanded expression is lengthy and is less informative than this invariant Hessian form.

---

## 7. Explicit bifurcation at vartheta = ln 2

For

\[
\vartheta=\ln2,
\]

the unique nontrivial curvature zero found on the Gaussian branch is

\[
\boxed{
\mu_c=0.7441373808086297\ldots
}
\]

At this point,

\[
\boxed{
D_c=0.004810238075205503\ldots,
}
\]

\[
\boxed{
J_c=0.7639473250676845\ldots,
}
\]

and

\[
\boxed{
p_c=\frac1{1+e^{-\mu_c}}
=0.6778999241684234\ldots.
}
\]

The Gaussian frontier slope there is

\[
\boxed{
\lambda_c^{(\rm bif)}
=11.0395865220\ldots.
}
\]

Numerical constrained optimization of the exact closed-form `(mu,p)` family confirms:

- below `D_c`, the optimum is the Gaussian point `p=p_mu`;
- above `D_c`, the optimum develops `p>p_mu`, i.e. an even-parity bias;
- the non-Gaussian gain starts continuously from zero at the bifurcation.

Representative values:

| `D_0` | best `J` in `(mu,p)` family | Gaussian `J_G` | gain |
|---:|---:|---:|---:|
| 0.001 | 0.70889085 | 0.70889085 | ~0 |
| 0.005 | 0.76604705 | 0.76602561 | 2.14e-5 |
| 0.010 | 0.82182099 | 0.81279944 | 9.02e-3 |
| 0.020 | 0.93432900 | 0.88542853 | 4.89e-2 |
| 0.050 | 1.27443416 | 1.05591739 | 0.21852 |
| 0.100 | 1.84007745 | 1.30095074 | 0.53913 |

At larger resource the optimum of this restricted family eventually returns to `mu=vartheta`, spending essentially all additional resource on parity bias rather than further Gaussian squeezing.

**Status:** analytic bifurcation criterion + numerically solved scalar root for the explicit temperature example.

---

## 8. Relation to earlier crossover result

The simpler family with `mu=vartheta` crossed the Gaussian frontier only at

\[
D_\times=0.01222932896\ldots.
\]

Allowing the detector to optimize squeezing and parity bias jointly reveals that the Gaussian state actually loses local stability much earlier:

\[
\boxed{D_c=0.00481023808\ldots.}
\]

Thus the simple parity-reweight crossing was not the onset of non-Gaussian advantage; it was merely the point where **zero-squeezing parity bias alone** overtook the Gaussian family.

---

## 9. Important interpretation and caution

This result refines the previous statement that the Gaussian pointer is optimal near equilibrium.

Correct statement:

> The Gaussian branch is locally optimal for sufficiently small free-energy budgets and supplies the exact leading near-equilibrium behavior, but it undergoes a finite-resource parity instability. In the explicit `vartheta=ln2` example, that instability occurs at `D_0≈4.81e-3` within the analytically solvable squeezed-parity-reweighted family.

This is stronger and more precise than saying merely that a distant pure-parity state eventually beats Gaussian states.

However, it remains **OPEN** whether some still broader non-Gaussian family destabilizes the Gaussian branch at an even smaller budget or whether the above `D_c` is the true global transition.

---

## 10. Next step

1. Use the exact global dual fixed-point equations to test whether the parity-reweighted squeezed family is locally exhaustive at the bifurcation.
2. Compute the Hessian spectrum against arbitrary parity-even/odd SLD perturbations, not just the one binary parity-bias mode.
3. If the binary parity mode is the first instability, promote `D_c(vartheta)` to the exact global Gaussian-to-non-Gaussian transition curve.
4. Compare this transition against the recent hot-parity displacement-sensing literature; do not claim parity enhancement itself as novel.