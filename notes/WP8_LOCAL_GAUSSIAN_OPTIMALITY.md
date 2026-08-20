# WP8 — Regular near-equilibrium Gaussian asymptotics (CORRECTED)

**Date:** 2026-08-20  
**Correction status:** The original stronger claim of an exact Gaussian-optimal neighborhood is **REJECTED** in the unrestricted infinite-dimensional oscillator. See `WP8_UV_NON_GAUSSIAN_INSTABILITY.md`.

## Correct statement

For the thermal harmonic pointer

\[
\tau_\vartheta=(1-e^{-\vartheta})e^{-\vartheta N},
\qquad
\vartheta=\beta\hbar\omega,
\]

the squeezed-thermal Gaussian direction is the unique steepest **regular BKM perturbative direction** for displacement SLD QFI under a small relative-entropy budget. It therefore gives the correct leading algebraic near-equilibrium expansion.

However, because the oscillator Hilbert space is unbounded, arbitrarily high-Fock coherence perturbations exist outside any fixed regular tangent sector. They provide exponentially small non-Gaussian improvements for every strictly positive free-energy budget. Therefore:

\[
\boxed{
\text{Gaussian is asymptotically perturbatively optimal as }D_0\to0,
\text{ but is not exactly globally/local optimal for any }D_0>0
}
\]

in the unrestricted ideal harmonic oscillator.

---

## 1. Thermal displacement QFI and SLD

The thermal quadrature variance is

\[
V_X=\frac12\coth\frac\vartheta2.
\]

Define

\[
t=\tanh\frac\vartheta2.
\]

The SLD for `X` translation is

\[
L_\beta=2tX,
\]

and

\[
\boxed{J_\beta=2t.}
\]

Using the variational representation

\[
J_X(\rho)=\sup_L\operatorname{Tr}[\rho K_L],
\qquad
K_L=2i[P,L]-L^2,
\]

the first variation at the faithful thermal state is determined by

\[
K_\beta=4t-4t^2X^2.
\]

Thus, up to a scalar, the regular QFI gradient is quadratic.

---

## 2. BKM relative-entropy geometry

For a regular perturbation

\[
\rho=\tau+\epsilon\delta\rho,
\qquad
\operatorname{Tr}\delta\rho=0,
\]

relative entropy has the local expansion

\[
D(\rho\Vert\tau)
=\frac{\epsilon^2}{2}
\langle\delta\rho,\delta\rho\rangle_{\rm BKM}
+O(\epsilon^3).
\]

The exponential tilt

\[
\rho_\lambda
\propto
\exp(\log\tau+\lambda K_\beta)
\]

is the BKM steepest-ascent direction for the linearized QFI.

Because both `log tau` and `K_beta` are quadratic in `X,P`, this state is a squeezed thermal Gaussian state.

This establishes Gaussian optimality **within the regular local asymptotic expansion**.

---

## 3. Leading small-budget expansion

The relevant Kubo-Mori variance is

\[
\mathcal V_{\rm KM}(X^2)
=\frac{1}{2\vartheta}\coth\frac\vartheta2
+\frac14\operatorname{csch}^2\frac\vartheta2.
\]

Hence

\[
\mathcal V_{\rm KM}(K_\beta)
=\frac{8t^3}{\vartheta}+4t^2(1-t^2).
\]

The regular perturbative frontier is therefore

\[
\boxed{
J_X(D_0)
=2t
+\sqrt{
2\left[
\frac{8t^3}{\vartheta}
+4t^2(1-t^2)
\right]D_0
}
+O(D_0).
}
\]

A squeezed thermal Gaussian state attains this expansion.

For `vartheta=ln 2`, the coefficient of `sqrt(D_0)` is

\[
1.282596527\ldots.
\]

---

## 4. Why this does not imply an exact Gaussian neighborhood

The BKM argument assumes a regular perturbative direction at fixed energy scale before taking `D_0 -> 0`.

`WP8_UV_NON_GAUSSIAN_INSTABILITY.md` constructs centered adjacent-coherence perturbations whose excitation index grows as the budget shrinks. Their QFI-Hessian / relative-entropy-Hessian ratio grows linearly with excitation number and is therefore unbounded.

To beat the Gaussian branch at very small `D_0`, the required excitation index scales as

\[
n\sim O(D_0^{-1/2}),
\]

while the available thermal weight there scales as

\[
\sim\exp[-C/\sqrt{D_0}].
\]

Thus the non-Gaussian improvement is beyond ordinary algebraic perturbation theory. This is why the Gaussian expansion above remains correct despite failure of exact optimality.

---

## 5. Finite-resource macroscopic parity transition

There is a second, much larger effect distinct from the UV tail.

Within the analytically solvable squeezed/parity-reweighted family, the Gaussian branch undergoes a finite-resource parity instability. For

\[
\vartheta=\ln2,
\]

the restricted-family bifurcation occurs at

\[
D_c=0.004810238075\ldots.
\]

Above that point, a low-complexity parity-biased state gives an algebraically visible improvement over the Gaussian branch.

See:

- `WP8_PARITY_REWEIGHT_INTERPOLATION.md`;
- `WP8_GAUSSIAN_PARITY_BIFURCATION.md`.

So the project must distinguish:

1. **UV nonperturbative non-Gaussianity:** exists for every `D_0>0` in the ideal infinite oscillator;
2. **macroscopic parity engineering:** becomes visibly favorable at a finite resource scale in the restricted family.

---

## 6. Implication for future theorem statements

Do **not** state:

> Gaussian pointers are globally optimal for sufficiently small positive free energy.

Instead state:

> Gaussian pointers determine the regular near-equilibrium asymptotic frontier, while the unrestricted infinite-dimensional oscillator has UV coherence directions that produce non-Gaussian improvements at every positive budget.

Exact Gaussian neighborhoods can only be recovered after imposing an additional UV/support/microscopic regularity resource.

**Current status:** regular asymptotic theorem PROVED; original exact-local-optimality interpretation REJECTED.