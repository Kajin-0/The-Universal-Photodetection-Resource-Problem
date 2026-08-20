# WP11 — Detuned dissipative capture/readout extension

**Date:** 2026-08-20

## Purpose

Extend `WP11_DISSIPATIVE_MATCHING_THEOREM.md` to finite optical/electronic detuning.

---

# 1. Model

Use

\[
H/\hbar
=
\begin{pmatrix}
0 & g\\
g & \Delta
\end{pmatrix}
\]

on `|F>,|X>`, with irreversible electrical jump

\[
L=\sqrt\Gamma|C\rangle\langle X|.
\]

Start in `|F>`.

---

# 2. Exact mean first-detection time

Solving the no-click Lyapunov problem gives

\[
\boxed{
\langle T\rangle
=
\frac{\Delta^2+\Gamma^2/4+2g^2}
{\Gamma g^2}
}
\]

or equivalently

\[
\boxed{
\langle T\rangle
=
\frac{\Gamma}{4g^2}
+
\frac{2}{\Gamma}
+
\frac{\Delta^2}{\Gamma g^2}.
}
\]

The three terms correspond to:

- Zeno/overmeasurement penalty;
- finite irreversible localization time;
- detuning penalty.

**Status:** PROVED.

---

# 3. Optimal localization/readout rate

Differentiate with respect to `Gamma`:

\[
\frac{d\langle T\rangle}{d\Gamma}
=
\frac1{4g^2}
-
\frac{\Delta^2+2g^2}{\Gamma^2g^2}.
\]

Therefore

\[
\boxed{
\Gamma_{\rm opt}
=2\sqrt{\Delta^2+2g^2}.
}
\]

At the optimum,

\[
\boxed{
\langle T\rangle_{\min}
=\frac{\sqrt{\Delta^2+2g^2}}{g^2}.
}
\]

For `Delta=0`, this reduces exactly to

\[
\Gamma_{\rm opt}=2\sqrt2 g,
\qquad
\langle T\rangle_{\min}=\sqrt2/g.
\]

---

# 4. Exact second moment and variance

The second moment is

\[
\boxed{
\langle T^2\rangle
=
\frac{
16\Delta^4
+8\Delta^2\Gamma^2
+80\Delta^2g^2
+\Gamma^4
+4\Gamma^2g^2
+64g^4
}
{8\Gamma^2g^4}.
}
\]

The variance is

\[
\boxed{
{\rm Var}(T)
=
\frac{
16\Delta^4
+8\Delta^2\Gamma^2
+96\Delta^2g^2
+\Gamma^4
-8\Gamma^2g^2
+64g^4
}
{16\Gamma^2g^4}.
}
\]

For nonzero detuning, the variance-minimizing `Gamma` is not generally identical to the mean-minimizing value. Minimizing the variance gives

\[
\boxed{
\Gamma_{\rm var}^2
=4\sqrt{\Delta^4+6\Delta^2g^2+4g^4}.
}
\]

At resonance the two optima coincide.

---

# 5. Exact Laplace transform

The first-detection-time Laplace transform is

\[
\boxed{
\widetilde w(s)
=
\frac{4\Gamma g^2(\Gamma+2s)}
{
4\Delta^2\Gamma s
+4\Delta^2s^2
+\Gamma^3s
+4\Gamma^2g^2
+5\Gamma^2s^2
+16\Gamma g^2s
+8\Gamma s^3
+16g^2s^2
+4s^4
}.
}
\]

At `Delta=0` the denominator factors and reduces to the resonant result

\[
\widetilde w(s)
=\frac{4\Gamma g^2}
{(\Gamma+2s)(s^2+\Gamma s+4g^2)}.
\]

The detuned event-timestamp information spectrum is

\[
\eta_I(\omega)=|\widetilde w(i\omega)|^2.
\]

---

# 6. Resource interpretation

Detuning is an additional independent microscopic resource/penalty. The fastest irreversible readout depends on both coherent capture strength and energetic alignment:

\[
\boxed{
\Gamma_{\rm opt}/2
=\sqrt{\Delta^2+2g^2}.
}
\]

Thus a putative material-independent theorem that specifies only optical coupling and readout rate but omits energetic mismatch is incomplete even in this minimal detector.

---

# 7. Next step

Map `Delta` to semiconductor band alignment/exciton-to-transport-state detuning and replace the flat Markov electrical reservoir by a structured phonon/contact spectral density. That will determine whether the optimum crosses into anti-Zeno behavior for realistic detector reservoirs.
