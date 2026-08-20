# WP8 — Exact parity-reweight interpolation

**Date:** 2026-08-20

## Purpose

The exact global WP8 free-energy/QFI problem is still open at intermediate resource. This note solves a particularly simple two-parity interpolation exactly: change only the total even/odd parity weights of the thermal state while leaving each conditional parity distribution thermal.

This construction is analytically elementary, starts continuously at the thermal state, and already beats the globally optimal Gaussian free-energy frontier at a surprisingly small nonequilibrium free-energy budget.

It therefore strengthens the earlier pure-even counterexample substantially.

---

## 1. Thermal reference and parity decomposition

Let

\[
q=e^{-\vartheta},\qquad 0<q<1,
\]

and

\[
\tau=(1-q)\sum_{n=0}^\infty q^n|n\rangle\langle n|.
\]

The thermal even-parity probability is

\[
\boxed{p_\beta=\frac1{1+q}},
\]

and the odd probability is

\[
1-p_\beta=\frac{q}{1+q}.
\]

The normalized conditional thermal distributions are

\[
\tau_e=(1-q^2)\sum_{k=0}^\infty q^{2k}|2k\rangle\langle2k|,
\]

\[
\tau_o=(1-q^2)\sum_{k=0}^\infty q^{2k}|2k+1\rangle\langle2k+1|.
\]

Define the parity-reweighted family

\[
\boxed{
\rho_p=p\tau_e+(1-p)\tau_o,
\qquad 0\le p\le1.
}
\]

At `p=p_beta`, this is exactly the thermal state.

---

## 2. Exact relative-entropy cost

Because the conditional states inside each parity sector are unchanged from the thermal reference, the full quantum relative entropy reduces exactly to a binary divergence:

\[
\boxed{
D(\rho_p\Vert\tau)
=D_{\rm bin}(p\Vert p_\beta)
}
\]

with

\[
D_{\rm bin}(p\Vert p_\beta)
=p\ln\frac{p}{p_\beta}
+(1-p)\ln\frac{1-p}{1-p_\beta}.
\]

Thus the construction spends **only parity-bias free energy** and no within-sector preparation resource.

---

## 3. Exact displacement QFI

Use `[X,P]=i` and

\[
|\langle n|P|n+1\rangle|^2=\frac{n+1}{2}.
\]

For a number-diagonal state with probabilities `r_n`, the SLD translation QFI is

\[
J_X
=2\sum_{n=0}^\infty(n+1)
\frac{(r_n-r_{n+1})^2}{r_n+r_{n+1}}.
\]

For `rho_p`,

\[
r_{2k}=p(1-q^2)q^{2k},
\]

\[
r_{2k+1}=(1-p)(1-q^2)q^{2k}.
\]

The two alternating edge classes can be summed geometrically. The exact result is

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

At the thermal parity weight,

\[
J_{\rm pr}(p_\beta)
=2\frac{1-q}{1+q}
=2\tanh\frac{\vartheta}{2},
\]

as required.

At `p=1`, the state is the even-conditioned thermal state and

\[
J_{\rm pr}(1)
=2\frac{3+q^2}{1-q^2}.
\]

For `q=1/2`, this gives `J=14/3`, reproducing the earlier analytic parity counterexample.

**Status:** PROVED.

---

## 4. Near-equilibrium expansion

Write

\[
p=p_\beta+\delta.
\]

The binary relative entropy obeys

\[
D(\rho_p\Vert\tau)
=
\frac{\delta^2}{2p_\beta(1-p_\beta)}
+O(\delta^3).
\]

The QFI derivative at the thermal point is

\[
\boxed{
\left.\frac{dJ_{\rm pr}}{dp}\right|_{p_\beta}
=4\frac{(1-q)^2}{(1+q)^2}.
}
\]

Hence along the QFI-increasing parity-bias direction,

\[
J_{\rm pr}(D_0)
=J_\beta
+c_{\rm pr}(q)\sqrt{D_0}
+O(D_0),
\]

with

\[
\boxed{
c_{\rm pr}(q)
=\frac{4\sqrt{2q}(1-q)^2}{(1+q)^3}.
}
\]

This confirms that parity reweighting becomes useful immediately away from equilibrium, although it is not the steepest leading-order direction.

The exact Gaussian free-energy frontier has the larger leading coefficient for the explicit `q=1/2` example:

\[
c_G=1.282596527\ldots,
\qquad
c_{\rm pr}=0.296296296\ldots.
\]

Thus the Gaussian branch dominates sufficiently close to equilibrium, consistent with the local BKM/SLD analysis.

---

## 5. Exact low-cost Gaussian-to-non-Gaussian crossing at vartheta = ln 2

Set

\[
\vartheta=\ln2,
\qquad q=\frac12,
\qquad p_\beta=\frac23.
\]

The globally optimal **Gaussian** QFI at fixed relative-entropy budget is known parametrically from `WP8_FREE_ENERGY_GAUSSIAN_CLOSURE.md`.

Writing

\[
a=\frac{\vartheta}{2},\qquad y\ge a,
\]

that frontier is

\[
D_G(y)
=\ln\frac{\sinh y}{\sinh a}
-\frac{y^2-a^2}{2y}\coth y,
\]

\[
J_G(y)
=\frac{2y\tanh y}{a}.
\]

Solving

\[
D_{\rm bin}(p\Vert2/3)=D_G(y)
\]

and

\[
J_{\rm pr}(p)=J_G(y)
\]

gives the nontrivial crossing

\[
\boxed{p_\times=0.7388649385\ldots}
\]

at

\[
\boxed{D_\times=0.01222932896\ldots}
\]

with

\[
\boxed{J_\times=0.8306097037\ldots}.
\]

For larger parity bias immediately beyond this crossing, the simple non-Gaussian parity-reweighted state has larger displacement QFI than **every Gaussian state at the same nonequilibrium free-energy budget**.

This is a much stronger practical counterexample than conditioning completely onto even parity, whose entry cost is

\[
D_{e,\min}=\ln(3/2)=0.405465\ldots.
\]

Therefore non-Gaussian superiority appears after only about three percent of the free-energy distance required for full even-parity conditioning in this dimensionless example.

**Status:** analytic family plus numerically solved one-dimensional crossing; Gaussian frontier itself is exact.

---

## 6. Interpretation

The mechanism is now transparent.

Near equilibrium:

- Gaussian squeezing is the steepest regular resource direction and wins at leading order.

At finite resource:

- changing the parity weights suppresses population overlap across transitions generated by `P`;
- this increases SLD displacement QFI without paying for within-sector cooling or squeezing;
- eventually that entropy-efficient parity bias beats the entire Gaussian family.

Thus the Gaussian-to-non-Gaussian change does **not** require a nearly pure parity state. It begins with a modest redistribution of the thermal parity weights.

This makes the hidden apparatus-resource problem more physically plausible than the earlier endpoint counterexample alone suggested.

---

## 7. Relation to recent literature

Grochowski, `To Cool, or Not to Cool? Displacement Sensing with Hot Quantum States`, arXiv:2606.13650 (2026), independently emphasizes that parity projection can remove thermal suppression of displacement QFI and enable hot-state enhancement.

Therefore UPRP must **not** claim discovery of parity protection or hot parity-enhanced displacement sensing itself.

The project-specific contribution is the optimization against a **nonequilibrium free-energy budget relative to a thermal state**, its role as a hidden photodetector apparatus resource, and its composition with optical-capture/coupling bandwidth constraints.

---

## 8. Next mathematical step

The present family varies only the binary parity weight. The next controlled extension is

\[
\rho=p\rho_e\oplus(1-p)\rho_o
\]

with `rho_e` and `rho_o` each allowed to move along their exact sector Gibbs-tilt frontiers.

The resource cost remains

\[
D_{\rm bin}(p\Vert p_\beta)
+pD_e+(1-p)D_o,
\]

while the exact cross-parity QFI penalty is already known from `WP8_EXACT_GLOBAL_DUAL_CHARACTERIZATION.md`.

This reduces the next search to three scalar resource-allocation variables plus the known sector parameters, rather than an unconstrained density-matrix optimization.