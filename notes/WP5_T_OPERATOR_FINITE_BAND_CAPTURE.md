# WP5 — Fixed-Mode Finite-Band T-Operator Capture Theorem

**Date:** 2026-08-19

## Scope

This note derives the first rigorous arbitrary-passive-scatterer finite-band optical capture bound used in UPRP, directly from the matrix-valued oscillator representation of Zhang, Monticone, and Miller (Nature Communications 14, 7724, 2023).

The result is **not** yet a completely arbitrary incident-wave theorem. It applies when the incident excitation restricted to the design domain has a fixed spatial vector/profile across the frequency interval. This is exact for an abstract fixed source vector and is a controlled approximation for an electrically small detector under a nearly uniform incident field.

The extension to a frequency-dependent incident spatial profile is a separate spatio-spectral problem.

**Status:** PROVED under the assumptions stated below.

---

# 1. T-operator conventions

Use the unrenormalized positive-frequency oscillator variables of Zhang–Monticone–Miller.

For a passive linear scatterer,

\[
\mathbf p(\omega)=\epsilon_0\mathbb T(\omega)\mathbf e_{\rm inc}(\omega),
\]

where the discretized/vector inner product represents the physical volume integral over the design/scatterer domain.

At positive frequency define

\[
\mathbb Z(\omega)
=\omega\operatorname{Im}\mathbb T(\omega).
\]

Split

\[
\mathbb Z=\mathbb X+\mathbb Y,
\]

where `X` is the reciprocal/symmetric part and `Y` is the nonreciprocal/antisymmetric part in the paper's positive-frequency decomposition.

Passivity implies

\[
\mathbb X\succeq0,
\qquad
-\mathbb X\preceq\mathbb Y\preceq\mathbb X,
\]

and therefore

\[
0\preceq\mathbb Z\preceq2\mathbb X.
\]

For a reciprocal structure,

\[
\mathbb Y=0,
\qquad
\mathbb Z=\mathbb X.
\]

---

# 2. High- and low-frequency sum rules

For a fixed design domain `D`, the oscillator measure satisfies

\[
2\int_0^\infty\mathbb X(\omega)d\omega
\preceq
\pi\omega_p^2\mathbb I_D,
\]

and

\[
2\int_0^\infty
\frac{\mathbb X(\omega)}{\omega^2}d\omega
\preceq
\pi\mathbb T_{0,D}.
\]

Equivalently,

\[
\int_0^\infty\mathbb X(\omega)d\omega
\preceq
\frac{\pi}{2}\omega_p^2\mathbb I_D,
\]

\[
\int_0^\infty
\frac{\mathbb X(\omega)}{\omega^2}d\omega
\preceq
\frac{\pi}{2}\mathbb T_{0,D}.
\]

The use of a containing design domain rather than the exact scatterer is justified by the domain-monotonicity property proved in the same work.

---

# 3. Finite-band oscillator-strength lemma

Take a positive-frequency interval

\[
B=[\omega_-,\omega_+],
\qquad
0<\omega_-<\omega_+.
\]

Because `X(omega)` is positive semidefinite,

\[
\int_B\mathbb X(\omega)d\omega
\preceq
\frac{\pi}{2}\omega_p^2\mathbb I_D.
\]

Also, on the interval `B`,

\[
\omega^2\le\omega_+^2,
\]

so

\[
\mathbb X(\omega)
=\omega^2\frac{\mathbb X(\omega)}{\omega^2}
\preceq
\omega_+^2\frac{\mathbb X(\omega)}{\omega^2}.
\]

Integrating,

\[
\int_B\mathbb X(\omega)d\omega
\preceq
\frac{\pi}{2}\omega_+^2\mathbb T_{0,D}.
\]

Hence for any fixed excitation vector `v`,

\[
\boxed{
\int_B
\mathbf v^\dagger\mathbb X(\omega)\mathbf v\,d\omega
\le
\frac{\pi}{2}
\min\!\left[
\omega_p^2\|\mathbf v\|^2,
\omega_+^2\mathbf v^\dagger\mathbb T_{0,D}\mathbf v
\right].
}
\]

This is a simple two-moment finite-band bound: the high-frequency sum rule limits total oscillator strength, while the low-frequency sum rule limits how much of that strength can be placed below a specified upper frequency.

**Status:** PROVED.

---

# 4. Extinction/capture-work theorem

The power removed from a fixed incident excitation by the passive scatterer is

\[
P_{\rm ext}(\omega)
=
\frac{\epsilon_0}{2}
\mathbf v^\dagger
\left[\omega\operatorname{Im}\mathbb T(\omega)\right]
\mathbf v
=
\frac{\epsilon_0}{2}
\mathbf v^\dagger\mathbb Z(\omega)\mathbf v.
\]

Absorbed/captured power obeys

\[
0\le P_{\rm cap}(\omega)
\le P_{\rm abs}(\omega)
\le P_{\rm ext}(\omega).
\]

For a general passive possibly nonreciprocal structure,

\[
\mathbb Z\preceq2\mathbb X,
\]

so

\[
\boxed{
\int_B P_{\rm cap}(\omega)d\omega
\le
\frac{\epsilon_0\pi}{2}
\min\!\left[
\omega_p^2\|\mathbf v\|^2,
\omega_+^2\mathbf v^\dagger\mathbb T_{0,D}\mathbf v
\right].
}
\]

For a reciprocal structure, `Z=X`, improving the factor by exactly two:

\[
\boxed{
\int_B P_{\rm cap}(\omega)d\omega
\le
\frac{\epsilon_0\pi}{4}
\min\!\left[
\omega_p^2\|\mathbf v\|^2,
\omega_+^2\mathbf v^\dagger\mathbb T_{0,D}\mathbf v
\right].
}
\]

**Status:** PROVED for fixed `v`.

---

# 5. Captured-QFI theorem

Assume the incident coherent-state task has a frequency-independent normalized spatial excitation vector `v` over `B`, with constant incident power normalization `P_in` per spectral mode and flat QFI weighting over the band.

Define the capture fraction

\[
\tau(\omega)=P_{\rm cap}(\omega)/P_{\rm in}.
\]

From the incident-channel QFI lemma in `WP5_INCIDENT_CHANNEL_QFI_SUM_RULE.md`,

\[
\bar\eta_{\mathcal I}
\le
\frac1{|B|}\int_B\tau(\omega)d\omega,
\qquad
|B|=\omega_+-\omega_-.
\]

Therefore, for a general passive structure,

\[
\boxed{
\bar\eta_{\mathcal I}
\le
\min\!\left[
1,
\frac{\epsilon_0\pi}
{2P_{\rm in}|B|}
\min\!\left(
\omega_p^2\|\mathbf v\|^2,
\omega_+^2\mathbf v^\dagger\mathbb T_{0,D}\mathbf v
\right)
\right].
}
\]

For a reciprocal structure,

\[
\boxed{
\bar\eta_{\mathcal I}
\le
\min\!\left[
1,
\frac{\epsilon_0\pi}
{4P_{\rm in}|B|}
\min\!\left(
\omega_p^2\|\mathbf v\|^2,
\omega_+^2\mathbf v^\dagger\mathbb T_{0,D}\mathbf v
\right)
\right].
}
\]

For an amplitude-modulated optical carrier with baseband

\[
|\Omega|\le\Omega_s,
\]

we have

\[
B=[\omega_0-\Omega_s,\omega_0+\Omega_s],
\qquad
|B|=2\Omega_s,
\]

provided `Omega_s < omega_0`.

This yields an explicit necessary optical-side condition for maintaining a target information fraction `r`.

---

# 6. Uniform-field / electrically-small corollary

For a detector domain sufficiently small that the incident electric field is approximately spatially uniform across the entire relevant optical sideband band, let

\[
\mathbf v=\mathbf E_0
\]

inside a volume `V` and zero outside.

Then

\[
\|\mathbf v\|^2=|E_0|^2V.
\]

Define the projected static polarizability-volume

\[
\alpha_{\rm stat}^{(V)}
\equiv
\frac{\mathbf v^\dagger\mathbb T_{0,D}\mathbf v}{|E_0|^2},
\]

which has dimensions of volume in the adopted susceptibility normalization.

Normalize the incident wave to power through reference aperture `A`:

\[
P_{\rm in}
=\frac12 c\epsilon_0|E_0|^2A.
\]

For a reciprocal detector frontend,

\[
\boxed{
\bar\eta_{\mathcal I}
\le
\min\!\left[
1,
\frac{\pi}{2cA|B|}
\min\!\left(
\omega_p^2V,
\omega_+^2\alpha_{\rm stat}^{(V)}
\right)
\right].
}
\]

For the symmetric sideband interval `|B|=2Omega_s`,

\[
\boxed{
\bar\eta_{\mathcal I}(\Omega_s)
\le
\min\!\left[
1,
\frac{\pi}{4cA\Omega_s}
\min\!\left(
\omega_p^2V,
(\omega_0+\Omega_s)^2\alpha_{\rm stat}^{(V)}
\right)
\right].
}
\]

This reproduces the matter/TRK scaling in the high-frequency-moment branch because

\[
\omega_p^2V
=\frac{N_e e^2}{\epsilon_0m_e}
\]

for a simple free-electron high-frequency asymptote.

The second branch incorporates an independent static-response resource and can be much tighter when

\[
\omega_0^2\alpha_{\rm stat}^{(V)}
\ll
\omega_p^2V.
\]

---

# 7. Example scaling at 10 micrometers

For

\[
\lambda_0=10\ \mu{\rm m},
\qquad
\omega_0\approx1.884\times10^{14}\ {m s^{-1}},
\]

and in the narrow-sideband regime `Omega_s << omega_0`, the reciprocal static branch implies approximately

\[
\Omega_s
\lesssim
\frac{\pi\omega_0^2}{4cr}
\frac{\alpha_{\rm stat}^{(V)}}{A}
\]

as a necessary condition for `bar eta_I >= r`.

In ordinary frequency,

\[
f_s=\frac{\Omega_s}{2\pi}
\lesssim
\frac{\omega_0^2}{8cr}
\frac{\alpha_{\rm stat}^{(V)}}{A}.
\]

For `r=0.9`, the coefficient is approximately

\[
1.64\times10^{19}\ {m Hz/m}
\]

multiplying the effective static length `alpha_stat^(V)/A`.

Illustrative values:

| `alpha_stat^(V)/A` | static-branch `f_s` ceiling (`r=0.9`) |
|---:|---:|
| `1 um` | `~16.4 THz` |
| `100 nm` | `~1.64 THz` |
| `10 nm` | `~164 GHz` |

These are not universal HgCdTe or semiconductor limits; they show the scale and the importance of the static-response/geometry resource.

---

# 8. Why this does not yet solve arbitrary photodetection

The theorem assumes the same incident spatial vector `v` across the frequency interval.

For a propagating plane wave over a large detector,

\[
\mathbf v(\omega,\mathbf r)
\propto
e^{i\omega\hat{\mathbf k}\cdot\mathbf r/c}
\]

changes with frequency. The oscillator-strength measure can, in principle, allocate response to different spatial directions/subspaces at different frequencies.

Therefore the arbitrary-wave problem introduces a **spatio-spectral degrees-of-freedom resource**. A rigorous extension needs one of:

1. a finite-dimensional incident-field subspace with explicit dimension `M`;
2. a footprint/space-bandwidth theorem controlling the effective rank of `v(omega)` over the band;
3. direct optimization of the full frequency-dependent incident-channel matrix under the T-operator sum rules.

This is closely connected to the spatial-channel optimization in Amaolo et al. (2026), but their published capacity bounds are single-frequency and explicitly leave finite-band sum-rule extensions open.

---

# 9. Finite-dimensional subspace fallback bound

Suppose all incident profiles over the task band lie in a fixed `M`-dimensional orthonormal subspace `S`, and satisfy

\[
\|\mathbf v(\omega)\|^2\le V_{\max}^2.
\]

Using positivity,

\[
\mathbf v^\dagger\mathbb X\mathbf v
\le
V_{\max}^2\operatorname{Tr}_S\mathbb X.
\]

The high-frequency sum rule then gives the coarse bound

\[
\int_B
\mathbf v(\omega)^\dagger\mathbb X(\omega)\mathbf v(\omega)d\omega
\le
\frac{\pi}{2}
V_{\max}^2\omega_p^2 M.
\]

An analogous static-moment bound uses

\[
\operatorname{Tr}_S\mathbb T_{0,D}.
\]

This shows explicitly how a spatial-channel count enters once the incident profile is allowed to rotate with frequency.

The factor `M` is not expected to be tight. It is valuable because it exposes the missing resource: arbitrary finite-band capture cannot be bounded by a single scalar oscillator-strength budget while an unbounded number of orthogonal spatial channels is allowed.

**Status:** PROVED coarse fallback in a finite-dimensional discretized subspace.

---

# 10. Composition with internal detector dynamics

Let the optical capture theorem provide

\[
\bar\eta_{\rm opt}(\Omega_s)
\le B_{\rm opt}(\Omega_s),
\]

and WP3/WP4 provide

\[
\bar\eta_{\rm trans}(\Omega_s)
\le B_{\rm trans}(\Omega_s).
\]

Then the total electrical information efficiency obeys

\[
\boxed{
\bar\eta_{\mathcal I}^{\rm total}(\Omega_s)
\le
\min\{B_{\rm opt}(\Omega_s),B_{\rm trans}(\Omega_s)\}.
}
\]

This already gives a valid restricted **optical + internal** completion theorem for:

- passive linear reciprocal optical frontend;
- fixed incident spatial profile across the optical task band;
- coherent-state encoding;
- downstream event-transducer class satisfying WP3/WP4 assumptions.

The next work is to enlarge this class without losing a finite bound.

---

# 11. Immediate next target

The decisive extension is to replace the fixed-vector assumption by a rigorous finite-band incident-channel operator with controlled spatial degrees of freedom. The most natural resource set is now

\[
\boxed{
\{\omega_p^2\mathbb I_D,\ \mathbb T_{0,D},\ \text{spatial channel/footprint resource},\ \Sigma,\mathcal A,f_*,\text{source QFI task}\}.
}
\]

This should be compared directly with the single-frequency Maxwell-channel formulation of Amaolo et al. (2026).
