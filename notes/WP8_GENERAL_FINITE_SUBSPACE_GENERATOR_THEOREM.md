# WP8 — General finite-subspace generator-capacity theorem

**Date:** 2026-08-20

## Purpose

The harmonic cutoff theorem `WP8_FINITE_SUPPORT_COMPLETION.md` identifies finite preparation support as one way to remove the ultraviolet coherence loophole. This note generalizes that result to an arbitrary detector-pointer preparation subspace and an arbitrary self-adjoint signal generator.

The result isolates the true structural apparatus resource:

> the maximum variance/QFI capacity of the signal generator on the accessible preparation subspace.

Finite Hilbert-space dimension alone is not enough because the generator can be rescaled independently.

---

# 1. Setup

Let `G=G^dagger` be the generator of the detector-side parameter translation

\[
\rho_\theta=e^{-i\theta G}\rho e^{i\theta G}.
\]

Let `Pi` project onto the allowed initial preparation subspace `S`, and assume

\[
\rho=\Pi\rho\Pi.
\]

`G` need not preserve `S`; it may connect the preparation subspace to states outside it during parameter encoding. Assume only that

\[
\Pi G^2\Pi
\]

is bounded on `S`. This is automatic for finite-dimensional `S` if the displayed matrix elements exist.

---

# 2. Exact maximum generator variance on a preparation subspace

For any state supported in `S`,

\[
\operatorname{Var}_\rho(G)
=\inf_{c\in\mathbb R}
\operatorname{Tr}[\rho(G-cI)^2].
\]

Define

\[
A_c=\Pi(G-cI)^2\Pi.
\]

Because the state set is compact convex and the objective is linear in `rho` and convex/coercive in `c`, minimax gives

\[
\sup_{\rho=\Pi\rho\Pi}\operatorname{Var}_\rho(G)
=
\inf_{c\in\mathbb R}
\lambda_{\max}(A_c).
\]

Define the **generator variance capacity**

\[
\boxed{
\mathcal V_{\mathcal S}(G)
\equiv
\inf_{c\in\mathbb R}
\lambda_{\max}
\left[
\Pi(G-cI)^2\Pi
\right].
}
\]

The infimum is attained because the right-hand side grows as `c^2` for large `|c|`.

At a minimizing `c_*`, the subgradient optimality condition implies that `c_*` lies in the numerical range of `G` restricted to the top eigenspace of `A_{c_*}`. Therefore one can choose a normalized **pure** vector `|psi_*>` in that top eigenspace with

\[
\langle\psi_*|G|\psi_*\rangle=c_*.
\]

For that vector,

\[
\operatorname{Var}_{\psi_*}(G)
=\langle(G-c_*)^2\rangle
=\lambda_{\max}(A_{c_*})
=\mathcal V_{\mathcal S}(G).
\]

Thus the maximum variance is achieved by a pure state.

**Status:** PROVED.

---

# 3. Exact preparation-subspace QFI capacity

For any unitary parameter family,

\[
F_Q(\rho,G)\le4\operatorname{Var}_\rho(G).
\]

Pure states saturate this inequality. Since the variance optimum above is attained by a pure state,

\[
\boxed{
J_{\mathcal S}^{\max}(G)
\equiv
\sup_{\rho=\Pi\rho\Pi}F_Q(\rho,G)
=
4\mathcal V_{\mathcal S}(G).
}
\]

Hence the exact arbitrary-state apparatus capacity is

\[
\boxed{
J_{\mathcal S}^{\max}(G)
=
4\inf_{c\in\mathbb R}
\lambda_{\max}
\left[
\Pi(G-cI)^2\Pi
\right].
}
\]

No Gaussianity, parity, Fock structure, or thermal assumption is required.

---

# 4. Invariant-subspace simplification

If `S` is invariant under `G`, define

\[
G_{\mathcal S}=\Pi G\Pi
\]

with extremal eigenvalues

\[
g_{\min},\quad g_{\max}.
\]

Then the classical maximum-variance theorem gives

\[
\mathcal V_{\mathcal S}(G)
=\frac{(g_{\max}-g_{\min})^2}{4}.
\]

Therefore

\[
\boxed{
J_{\mathcal S}^{\max}(G)
=(g_{\max}-g_{\min})^2.
}
\]

The optimum is the equal superposition of the two extremal eigenstates, up to phases.

This is the cleanest finite-level resource statement.

---

# 5. Harmonic cutoff theorem as a special case

For

\[
\mathcal S_N=\operatorname{span}\{|0\rangle,\ldots,|N\rangle\}
\]

and displacement generator `P`, the subspace is **not** invariant under `P` because `P|N>` contains `|N+1>`.

Nevertheless parity symmetry makes the minimizing center `c_*=0` and the top eigenvector of

\[
\Pi_NP^2\Pi_N
\]

can be chosen parity definite. Hence

\[
J_{\mathcal S_N}^{\max}(P)
=4\lambda_{\max}(\Pi_NP^2\Pi_N),
\]

recovering `WP8_FINITE_SUPPORT_COMPLETION.md`.

---

# 6. Finite dimension alone is NOT a resource bound

Suppose only the subspace dimension

\[
d=\dim\mathcal S
\]

is fixed.

For any nontrivial bounded generator `G_0`, define

\[
G_R=R G_0.
\]

Then

\[
J_{\mathcal S}^{\max}(G_R)
=R^2J_{\mathcal S}^{\max}(G_0).
\]

Therefore

\[
\boxed{
\dim\mathcal S<\infty
\quad\not\Rightarrow\quad
\text{finite universal metrological capacity independent of generator scale}.
}
\]

A finite-level completion theorem must specify at least one absolute microscopic scale controlling `G` or its matrix elements.

This is the finite-dimensional analogue of the earlier missing-rate and missing-coupling no-go results.

---

# 7. Useful coarse bounds

For any chosen centering constant `c`,

\[
J_{\mathcal S}^{\max}(G)
\le
4\|\Pi(G-cI)^2\Pi\|_\infty.
\]

In particular,

\[
J_{\mathcal S}^{\max}(G)
\le4\|\Pi G^2\Pi\|_\infty.
\]

If `G` is globally bounded with spectral diameter

\[
\Delta G=g_{\max}^{\rm global}-g_{\min}^{\rm global},
\]

then

\[
J_{\mathcal S}^{\max}(G)
\le(\Delta G)^2.
\]

These are weaker than the exact subspace formula but easier to map to microscopic estimates.

---

# 8. Photodetection composition

Where the coherent/passive-linear SLD-Stam interface applies, any pointer QFI cap

\[
J_D\le J_{\mathcal S}^{\max}(G)
\]

can be inserted into

\[
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac{\tau J_D}{2(1-\tau)+\tau J_D}.
\]

Hence

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac{\tau J_{\mathcal S}^{\max}(G)}
{2(1-\tau)+\tau J_{\mathcal S}^{\max}(G)}.
}
\]

For a target pointwise information fraction `q`, the required optical transfer probability is

\[
\boxed{
\tau_q(\mathcal S,G)
=
\frac{2q}
{J_{\mathcal S}^{\max}(G)(1-q)+2q}.
}
\]

If WP7 gives `tau<=sin^2 Gamma`, then necessarily

\[
\Gamma\ge\arcsin\sqrt{\tau_q}.
\]

If WP5 gives narrow-band average/pointwise capture resource `Omega_EM`, the same `tau_q` enters the finite-band condition

\[
\Omega_s\lesssim\Omega_{\rm EM}/\tau_q
\]

under the corresponding WP5 assumptions.

Caution: the SLD-Stam mixing formula is a bosonic/passive-linear interface. The subspace-generator theorem itself is much more general, but its photodetection composition must respect the actual coupling architecture.

---

# 9. Resource interpretation

The apparatus resource is not fundamentally `N_max`, level count, squeezing, or even mean energy. The invariant object is

\[
\boxed{
J_{\mathcal S}^{\max}(G)
}
\]

or equivalently the generator variance capacity

\[
\boxed{
\mathcal V_{\mathcal S}(G).
}
\]

A microscopic detector model must explain why this quantity is finite using independently physical inputs such as:

- finite participating degrees of freedom;
- bounded transition matrix elements;
- finite spectral span;
- saturation/anharmonicity;
- oscillator-strength/sum-rule constraints;
- finite preparation controllability.

Simply naming `J_S^max` as a resource is mathematically complete but physically unsatisfying if it merely restates the available metrological capacity. The next task is to derive it from lower-level matter resources.

---

# 10. Next step

Test whether matter sum rules, especially Thomas-Reiche-Kuhn/f-sum constraints, can upper-bound `J_S^max(G)` for realistic detector pointer degrees of freedom.

Key adversarial question:

> Does the signed nature of excited-state oscillator-strength sum rules permit cancellation loopholes analogous to the harmonic UV tail?

If yes, preserve that failure as a no-go theorem and identify the additional spectral/support condition required for a positive bound.