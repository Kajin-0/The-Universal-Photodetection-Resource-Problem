# WP11 — Reservoir spectral-regularity no-go and repair

**Date:** 2026-08-20

## Purpose

`WP11_STRUCTURED_RESERVOIR_ZENO_ANTIZENO_INFORMATION.md` shows that strong-readout timing depends on the overlap of a measurement/control spectrum with the reservoir spectral density `G(omega)`. This note asks whether a coarse scalar such as total system-bath coupling weight is enough to bound the optimized event rate.

Main conclusion:

> **No. Finite integrated spectral weight alone does not bound the optimized overlap functional if arbitrarily narrow spectral features and arbitrarily short frequency offsets are allowed. A spectral-regularity/correlation-time resource is necessary.**

---

# 1. General overlap functional

Let

\[
\Gamma[F,G]=2\pi\int d\omega\,G(\omega)F(\omega),
\]

with

\[
G(\omega)\ge0,
\qquad
F(\omega)\ge0,
\qquad
\int F(\omega)d\omega=1.
\]

For continuous Lorentzian broadening centered at the detector transition `omega_0`,

\[
F_\nu(\omega)
=\frac1\pi
\frac{\nu}{(\omega-\omega_0)^2+\nu^2}.
\]

---

# 2. Narrow-line family with fixed total weight

Let

\[
L_\epsilon(x)=\frac1\pi\frac{\epsilon}{x^2+\epsilon^2}
\]

and define a reservoir feature

\[
\boxed{
G_{\epsilon,\delta}(\omega)
=W\,L_\epsilon(\omega-\omega_0-\delta),
}
\]

so that

\[
\boxed{\int G_{\epsilon,\delta}d\omega=W}
\]

for every width `epsilon` and offset `delta`.

The Lorentzian-overlap identity gives

\[
\boxed{
\Gamma(\nu)
=2W\frac{\epsilon+\nu}
{\delta^2+(\epsilon+\nu)^2}.
}
\]

If

\[
\delta>\epsilon,
\]

the overlap is maximized when

\[
\boxed{\epsilon+\nu_*=\delta,}
\]

so

\[
\boxed{
\Gamma_{\max}=W/\delta.
}
\]

Thus, at fixed integrated weight `W`, the mathematical overlap optimum can grow without bound as a narrow reservoir feature approaches the detector transition:

\[
\delta\to0,
\qquad
\epsilon\ll\delta.
\]

---

# 3. Stronger construction: vanishing unbroadened rate but growing optimized overlap

Choose for example

\[
\epsilon=\delta^3.
\]

Then at zero added broadening,

\[
\Gamma(0)
=2W\frac{\delta^3}{\delta^2+\delta^6}
\sim2W\delta\to0.
\]

But the optimized broadened overlap is

\[
\Gamma_{\max}=W/\delta\to\infty.
\]

Therefore even the pair

\[
\{\text{total spectral weight},\text{unbroadened local decay rate}\}
\]

does not control the optimized overlap if spectral shape is unrestricted.

**Important physical caveat:** before the formal divergence is reached, the weak-coupling/Markov assumptions underlying a simple overlap-rate interpretation can fail because the bath correlation time grows as the feature narrows. That breakdown strengthens rather than weakens the resource conclusion: **a correlation-time/spectral-regularity condition is required to define the admissible class.**

The divergent sequence should therefore be read as a no-go for the coarse resource set, not as a prediction of an arbitrarily fast physical detector within perturbation theory.

---

# 4. Repair A: spectral-density `L^infinity` bound

If

\[
\boxed{0\le G(\omega)\le G_{\max}}
\]

for all relevant frequencies, then normalization of `F` gives immediately

\[
\Gamma
=2\pi\int GF
\le2\pi G_{\max}\int F
\]

and therefore

\[
\boxed{\Gamma\le2\pi G_{\max}.}
\]

This is independent of the detailed control spectrum.

For an exponential event stage, the corresponding timestamp half-information angular frequency obeys

\[
\boxed{\Omega_{1/2}\le2\pi G_{\max}.}
\]

---

# 5. Repair B: total spectral weight + minimum control linewidth

Suppose only

\[
W_G=\int G(\omega)d\omega<\infty
\]

is known, but the Lorentzian control width is bounded below:

\[
\nu\ge\nu_{\min}>0.
\]

Since

\[
\sup_\omega F_\nu(\omega)=1/(\pi\nu)
\le1/(\pi\nu_{\min}),
\]

we obtain

\[
\Gamma
\le2\pi W_G\sup F
\]

and hence

\[
\boxed{
\Gamma\le2W_G/\nu_{\min}.
}
\]

This is a different completion: finite bath weight plus finite control spectral resolution.

---

# 6. Repair C: finite correlation-time / smoothness class

A physically stronger formulation would specify a class such as:

- finite reservoir bandwidth;
- bounded `G_max`;
- bounded derivative/Lipschitz constant;
- finite bath correlation time;
- a lower bound on the width of spectral features;
- or a microscopic finite-mode-volume/coupling model.

Any of these prevents arbitrarily narrow hidden spectral spikes.

The weakest useful condition for semiconductor phonon/contact reservoirs remains OPEN.

---

# 7. Resource-completeness consequence

The structured-reservoir layer now repeats the UPRP pattern:

\[
\boxed{
\text{integrated coupling weight alone}
\not\Rightarrow
\text{bounded backaction-modified event speed}.
}
\]

A repair needs

\[
\boxed{
\text{coupling weight}
+\text{spectral regularity/correlation resource}
+\text{control bandwidth}
\Rightarrow
\text{finite overlap rate}.
}
\]

This is analogous to:

- signed TRK weight requiring spectral/support information;
- finite carrier velocity requiring weighting-geometry scale;
- finite free energy requiring pointer UV/support regularization.

---

# 8. Next step

For a semiconductor-specific completion, use actual phonon/contact spectral forms and ask which material constants bound `G_max`, feature width, or bath correlation time. Candidate cases:

1. 3D acoustic phonons with smooth low-frequency power-law spectral density;
2. optical phonon bands with finite linewidth;
3. contact/escape continua with threshold density of states;
4. impurity/trap continua with potentially narrow resonances.

The target is a coarse material-resource theorem, not a full microscopic spectrum requirement.
