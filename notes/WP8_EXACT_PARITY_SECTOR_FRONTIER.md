# WP8 — Exact even-parity free-energy QFI frontier and asymptotic global optimality

**Date:** 2026-08-20

## Purpose

The analytic parity counterexample in `WP8_NON_GAUSSIAN_PARITY_COUNTEREXAMPLE.md` reveals a larger exactly solvable class. Inside a fixed Fock-parity sector, SLD displacement QFI becomes a linear expectation value. The relative-entropy constrained optimization can then be solved exactly by the quantum Gibbs variational principle.

This note derives the exact even-sector frontier and proves that it is **asymptotically globally optimal** at large nonequilibrium free energy.

---

## 1. Any even-supported state saturates `J = 4 <P^2>`

Let

\[
\Pi_{\rm e}=\sum_{k=0}^\infty |2k\rangle\langle2k|
\]

and assume

\[
\rho=\Pi_{\rm e}\rho\Pi_{\rm e}.
\]

Parity implies

\[
\Pi_{\rm e}P\Pi_{\rm e}=0,
\]

because `P` flips Fock parity.

Diagonalize `rho` within the even subspace. In the SLD-QFI spectral formula, all matrix elements of `P` between two occupied eigenvectors vanish. The only nonzero terms connect an occupied even eigenvector to a zero-eigenvalue odd vector. Summing those terms gives

\[
\boxed{
J_X(\rho)=4\operatorname{Tr}(\rho P^2).
}
\]

No Gaussianity, Fock diagonality, or purity is required.

**Status:** PROVED.

This identity is the reason parity-protected mixing can preserve displacement metrological power.

---

## 2. Relative-entropy optimization becomes linear

Use the harmonic thermal reference

\[
\tau_\vartheta=(1-e^{-\vartheta})e^{-\vartheta N},
\qquad
\vartheta=\beta\hbar\omega.
\]

Inside the even sector, maximizing QFI at fixed free-energy budget `D_0` is equivalent to

\[
\max_{\rho=\Pi_e\rho\Pi_e}
\operatorname{Tr}(\rho P^2)
\]

subject to

\[
D(\rho\Vert\tau_\vartheta)\le D_0.
\]

For a linear observable under a relative-entropy constraint, the Gibbs variational principle gives the exact exponential-family optimizer

\[
\boxed{
\rho_s
=\frac{
\Pi_e\exp[\log\tau_\vartheta+sP^2]\Pi_e
}{Z_e(s)},
}
\]

with

\[
Z_e(s)
=\operatorname{Tr}\!\left[
\Pi_e\exp(\log\tau_\vartheta+sP^2)
\right],
\]

for `0 <= s < vartheta/2`.

Since both `N` and `P^2` preserve parity, the projector introduces no ordering ambiguity inside the parity block.

**Status:** PROVED.

---

## 3. Closed-form partition function

Using

\[
N=\frac{X^2+P^2-1}{2},
\]

we have, up to the thermal normalization constant,

\[
-\vartheta N+sP^2
=\frac\vartheta2
-\frac\vartheta2X^2
-\left(\frac\vartheta2-s\right)P^2.
\]

Define

\[
\boxed{
\mu(s)=\sqrt{\vartheta(\vartheta-2s)}.
}
\]

A squeezing transformation diagonalizes the quadratic operator while preserving parity. The exact even-sector partition function is

\[
\boxed{
Z_e(s)
=(1-e^{-\vartheta})
\frac{e^{(\vartheta-\mu)/2}}
{1-e^{-2\mu}}.
}
\]

At `s=0`, `mu=vartheta` and

\[
Z_e(0)=\frac1{1+e^{-\vartheta}},
\]

which is exactly the thermal probability of even parity.

---

## 4. Exact QFI and free-energy parametrization

The tilted expectation is

\[
m(s)
\equiv
\langle P^2\rangle_{\rho_s}
=\partial_s\ln Z_e(s).
\]

Differentiation gives

\[
\boxed{
m(s)
=\frac{\vartheta}{\mu}
\left[
\frac12+
\frac{2}{e^{2\mu}-1}
\right].
}
\]

Hence the exact even-sector QFI is

\[
\boxed{
J_e(s)=4m(s).
}
\]

Because

\[
\log\rho_s
=\log\tau_\vartheta+sP^2-\log Z_e(s)
\]

on the even support,

\[
\boxed{
D_e(s)
=s\,m(s)-\ln Z_e(s).
}
\]

Therefore the exact even-parity resource frontier is given parametrically by

\[
\boxed{
\left(D_0,J_X\right)
=\left(D_e(s),4m(s)\right),
\qquad
0\le s<\vartheta/2.
}
\]

At `s=0`,

\[
D_e(0)=\ln(1+e^{-\vartheta}),
\]

recovering the thermal state conditioned on even parity.

As `s -> vartheta/2`, `mu -> 0` and both `D_e` and `J_e` diverge.

**Status:** PROVED. This is the exact optimum among all even-supported pointer states.

---

## 5. Physical form of the optimizer

The operator

\[
\exp[-\vartheta N+sP^2]
\]

is a squeezed thermal Gaussian operator. Since squeezing preserves parity, `rho_s` is equivalently

> a squeezed thermal state conditioned on even parity.

It is therefore intrinsically non-Gaussian because of the parity projection, despite being generated from a quadratic exponential family.

The exact optimizer automatically chooses both:

- the amount of squeezing; and
- the effective thermal occupation inside the squeezed basis.

This is more general than merely squeezing the original even-conditioned thermal state at fixed conditional temperature.

---

## 6. Large-free-energy asymptotics

As `mu -> 0`,

\[
\frac{2}{e^{2\mu}-1}
=\frac1\mu-1+O(\mu),
\]

so

\[
m(s)
=\frac{\vartheta}{\mu^2}
-\frac{\vartheta}{2\mu}
+O(1).
\]

Also

\[
s
=\frac\vartheta2-rac{\mu^2}{2\vartheta}.
\]

Substituting into `D_e=s m-ln Z_e` gives

\[
D_e
=\frac{\vartheta^2}{2\mu^2}
-\frac{\vartheta^2}{4\mu}
+O(|\ln\mu|).
\]

Meanwhile

\[
J_e=4m
=\frac{4\vartheta}{\mu^2}
-\frac{2\vartheta}{\mu}
+O(1).
\]

Eliminating `mu` yields

\[
\boxed{
J_e^{\rm opt}(D_0,\vartheta)
=\frac{8D_0}{\vartheta}
+O(\ln D_0).
}
\]

---

## 7. Comparison with the global arbitrary-state upper bound

`WP8_GLOBAL_FREE_ENERGY_UPPER_BOUND.md` proves

\[
J_F^{\max}(D_0,\vartheta)
\le
\frac2{\xi[N_+(D_0,\vartheta)]},
\]

where `N_+` is the largest solution of

\[
\vartheta N-g(N)-\ln(1-e^{-\vartheta})=D_0.
\]

For large `D_0`,

\[
N_+
=\frac{D_0}{\vartheta}
+O\!\left(\frac{\ln D_0}{\vartheta}\right)
\]

and

\[
\frac2{\xi(N_+)}
=8N_++O(1)
=\frac{8D_0}{\vartheta}
+O(\ln D_0).
\]

Thus the explicit even-parity construction and the global upper bound have the same leading asymptotic behavior:

\[
\boxed{
J_e^{\rm opt}(D_0,\vartheta)
\sim
J_F^{\max}(D_0,\vartheta)
\sim
\frac{8D_0}{\vartheta}
\qquad(D_0\to\infty).
}
\]

Equivalently,

\[
\boxed{
\frac{J_e^{\rm opt}}
{J_F^{\max}}
\to1
}
\]

in the sense that the known lower and upper bounds have ratio tending to unity.

**Status:** PROVED asymptotic global optimality to leading relative order.

---

## 8. Consequence for photodetection interaction resources

At large preparation free energy, the globally best possible pointer QFI scales as

\[
J_B\sim\frac{8\Delta F_\beta}{\hbar\omega_D}.
\]

Combined with the SLD-Stam photodetection theorem, keeping a fixed output/input information fraction while the passive coupling action `Gamma -> 0` necessarily requires

\[
\boxed{
\Delta F_\beta=\Theta(\Gamma^{-2})
}
\]

to leading order.

The `1/Gamma^2` preparation-cost law is therefore not a Gaussian artifact; the explicit non-Gaussian parity optimizer reaches the globally allowed leading scaling.

---

## 9. Remaining finite-budget problem

The exact arbitrary-state frontier at finite `D_0` remains open, especially below the even-sector entry cost

\[
D_0<\ln(1+e^{-\vartheta}),
\]

where a state supported entirely in one parity sector is not admissible.

The next promising analytic target is the **two-parity problem**: allow both even and odd blocks with variable total parity weights and optimize the cross-parity SLD-QFI penalty together with the relative-entropy budget.

The continuous parity-biased family in `WP8_NON_GAUSSIAN_PARITY_COUNTEREXAMPLE.md` supplies a tractable starting point.
