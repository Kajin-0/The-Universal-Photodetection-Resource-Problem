# Research Log — Round 6

**Date:** 2026-08-20

## Purpose

Durable checkpoint for the WP8/WP9 quantum apparatus branch after the finite-temperature free-energy problem produced both a low-cost parity advantage and a stronger ultraviolet coherence no-go theorem.

This round materially changes the resource hierarchy and corrects an earlier overstatement of Gaussian local optimality.

---

# 1. Exact parity-reweight interpolation

For thermal factor

\[
q=e^{-\vartheta},
\qquad
p_\beta=1/(1+q),
\]

define

\[
\rho_p=p\tau_e+(1-p)\tau_o,
\]

where `tau_e,tau_o` are the normalized thermal conditional states in even/odd parity.

Then

\[
D(\rho_p\Vert\tau)=D_{\rm bin}(p\Vert p_\beta)
\]

and

\[
\boxed{
J_{\rm pr}(p)
=
\frac{2}{1-q^2}
\left[
(2p-1)^2(1+q^2)
+2\frac{[(1-p)-pq^2]^2}{(1-p)+pq^2}
\right].
}
\]

At `vartheta=ln2`, this elementary non-Gaussian family crosses the globally optimal Gaussian free-energy frontier at

\[
p_\times=0.7388649385\ldots,
\]

\[
D_\times=0.01222932896\ldots,
\]

\[
J_\times=0.8306097037\ldots.
\]

Thus a modest parity bias beats every Gaussian state at a free-energy cost far smaller than complete parity conditioning.

Primary note: `WP8_PARITY_REWEIGHT_INTERPOLATION.md`.

---

# 2. Squeezed/parity-reweighted bifurcation

Enlarge the family to the exact Gaussian-optimal squeezed thermal state `sigma_mu` plus independent parity reweighting:

\[
\rho_{\mu,p}=p\sigma_{\mu,e}+(1-p)\sigma_{\mu,o}.
\]

The QFI and resource cost are closed form. At the natural Gaussian parity weight, first-order constrained stationarity holds identically; the parity decision is second order.

For `vartheta=ln2`, the Gaussian branch loses local stability **inside this two-parameter family** at

\[
\mu_c=0.7441373808086\ldots,
\]

\[
D_c=0.0048102380752\ldots,
\]

\[
J_c=0.7639473250677\ldots.
\]

This is a macroscopic low-complexity non-Gaussian bifurcation, but not the exact global onset because of the stronger UV result below.

Primary note: `WP8_GAUSSIAN_PARITY_BIFURCATION.md`.

---

# 3. Major correction: Gaussian exact local optimality is false in the ideal infinite oscillator

At a Gaussian candidate with effective thermal factor `q=e^{-mu}`, construct high-Fock adjacent coherences. The exact QFI-Hessian / relative-entropy-Hessian ratio for

\[
B_n=(|n\rangle\langle n+1|+\mathrm{h.c.})/\sqrt2
\]

is

\[
\boxed{
R_n
=
\frac{8(1-q)}{\vartheta}
\left[
 n\frac{1+q+q^2}{(1+q)(1+q^2)}
+
\frac{1+q+3q^2+q^3}
{(1+q)^2(1+q^2)}
\right].
}
\]

Hence

\[
R_n\sim\alpha n\to\infty.
\]

Combining two separated adjacent coherences yields a centered perturbation satisfying

\[
\delta\langle X\rangle
=\delta\langle P\rangle
=\delta\langle X^2\rangle
=0.
\]

For every strictly positive free-energy budget, the Gaussian Lagrange multiplier is finite. Therefore sufficiently high `n` produces a positive constrained QFI second variation.

Conclusion:

\[
\boxed{
D_0>0
\Rightarrow
\text{the exact unrestricted harmonic-pointer optimum is non-Gaussian.}
}
\]

The non-Gaussian gain becomes approximately `exp[-C/sqrt(D_0)]` near equilibrium, so the Gaussian BKM expansion remains correct to ordinary algebraic orders.

The earlier `WP8_LOCAL_GAUSSIAN_OPTIMALITY.md` was corrected. Its former exact-neighborhood interpretation is **REJECTED**; only regular/asymptotic perturbative Gaussian optimality remains.

Primary note: `WP8_UV_NON_GAUSSIAN_INSTABILITY.md`.

---

# 4. Energy populations/moments do not repair the UV loophole

The unstable coherence perturbations are parity odd, while `H_D` and every spectral function `f(H_D)` are parity even. Hence

\[
\boxed{
\operatorname{Tr}[\delta\rho f(H_D)]=0.
}
\]

Thus mean energy, variance, any finite set of moments, or even the complete diagonal energy distribution cannot detect/control the UV coherence.

Ordinary time-translation/energetic-coherence QFI is also not uniformly sufficient in a perfect harmonic ladder because adjacent gaps stay fixed while displacement-generator matrix elements grow as `sqrt(n)`.

This proves the missing regularizer must be coherence-/support-/matrix-element-sensitive.

Primary note: `WP8_UV_REGULARIZATION_RESOURCE.md`.

---

# 5. Exact finite-support repair

Restrict only the **initial pointer preparation** to

\[
\mathcal H_N=\operatorname{span}\{|0\rangle,\ldots,|N\rangle\}.
\]

For arbitrary pointer states in that support,

\[
\boxed{
J_N^{\max}
=4\lambda_{\max}(\Pi_NP^2\Pi_N).
}
\]

The upper bound is saturated by a parity-definite top eigenvector, so it is exact.

Simple bounds:

\[
4N+2\le J_N^{\max}\le8N+4.
\]

With coherent optical displacement input and passive transfer probability `tau`, directional SLD Stam gives

\[
\boxed{
F_{\rm elec}/F_{\rm in}
\le
\frac{\tau J_N^{\max}}
{2(1-\tau)+\tau J_N^{\max}}.
}
\]

With interaction action `Gamma`, `tau<=sin^2 Gamma`.

For pointwise target information fraction `q`, define

\[
\tau_q(N)
=
\frac{2q}{J_N^{\max}(1-q)+2q}.
\]

Then necessarily

\[
\Gamma\ge\arcsin\sqrt{\tau_q(N)}
\]

and, using the WP5 narrow-band electromagnetic capture resource,

\[
\Omega_s\le\Omega_{\rm EM}/\tau_q(N).
\]

This is an exact cutoff-regularized quantum information-bandwidth theorem.

Primary note: `WP8_FINITE_SUPPORT_COMPLETION.md`.

---

# 6. Updated resource-completeness hierarchy

The successive no-go/repair chain is now

\[
\boxed{
\text{finite source task}
+
\text{finite-band EM capture}
+
\text{absolute microscopic coupling}
+
\text{apparatus preparation resource}
+
\text{UV/support/generator-matrix-element regularizer}
+
\text{internal thermokinetic resources}
\Rightarrow
\text{finite information-bandwidth ceiling}.
}
\]

Interpretation:

- classical hidden resource: a rare, fast state can carry an unbounded rate at vanishing occupancy;
- quantum hidden resource: arbitrarily high-energy coherence can carry disproportionate displacement-QFI curvature at vanishing probability.

Both are **vanishing-weight hidden-resource mechanisms**.

---

# 7. Literature constraints

Do not claim novelty for parity-enhanced/hot displacement sensing, non-Gaussian force sensing, work-vs-coherence resource distinctions, or QFI as an asymmetry/thermodynamic resource. Relevant prior art includes Narasimhachar et al., Marvian, Grochowski & Filip, and Grochowski's 2026 hot-state parity work.

Potential surviving novelty is the **photodetection-specific resource-completeness sequence** and the UV-coherence failure of a free-energy-only apparatus closure when combined with finite-band optical information transfer.

Novelty remains provisional.

---

# 8. Immediate next action

1. Generalize the finite-support theorem to an arbitrary finite-level pointer, preparation subspace `S`, and signal generator `G`.
2. Identify the minimal microscopic resource: support/dimension alone will not be enough if the generator scale can be arbitrarily rescaled.
3. Test whether TRK/f-sum or other matter sum rules constrain the relevant internal-pointer generator matrix elements. Preserve any signed-cancellation failure as a no-go result.
4. Compose the resulting finite-level resource with WP5/WP9 without double-counting optical-front-end oscillator strength.
