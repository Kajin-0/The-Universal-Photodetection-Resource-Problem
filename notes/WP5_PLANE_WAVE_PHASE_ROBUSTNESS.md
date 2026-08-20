# WP5 — Plane-Wave Sideband Phase Robustness

**Date:** 2026-08-19

## Purpose

`WP5_T_OPERATOR_FINITE_BAND_CAPTURE.md` proved a finite-band optical capture/QFI theorem assuming a fixed incident spatial vector `v` across the optical sideband interval. A propagating plane wave does not satisfy that assumption exactly because its phase changes with optical frequency across a finite detector.

This note proves a controlled extension for plane-wave-like frequency dependence and shows that the fixed-profile theorem is robust whenever the detector size is small compared with the **modulation wavelength** `c/Omega_s`, even if the detector is not small compared with the optical carrier wavelength.

**Status:** PROVED under the stated phase-only incident-profile model.

---

# 1. Frequency-dependent incident profile

Let the optical task band be

\[
\omega=\omega_0+\delta,
\qquad
|\delta|\le\Omega_s.
\]

Assume the incident field inside the design domain can be written

\[
\boxed{
\mathbf v_\delta(\mathbf r)
=e^{i\delta\tau(\mathbf r)}\mathbf v_0(\mathbf r),
}
\]

where `tau(r)` is a real propagation-delay field satisfying

\[
|\tau(\mathbf r)|\le\tau_*.
\]

For a plane wave with propagation direction `khat`, centered so the maximum projected displacement is `R_parallel`,

\[
\tau(\mathbf r)=\frac{\hat{\mathbf k}\cdot\mathbf r}{c},
\qquad
\tau_*\le\frac{R_\parallel}{c}.
\]

The carrier phase `exp(i omega_0 khat·r/c)` is absorbed into `v_0`; only the **sideband phase difference** matters.

---

# 2. Expansion into fixed spatial vectors

Expand

\[
\mathbf v_\delta
=
\sum_{n=0}^\infty
\frac{(i\delta)^n}{n!}\mathbf w_n,
\qquad
\mathbf w_n(\mathbf r)=\tau(\mathbf r)^n\mathbf v_0(\mathbf r).
\]

The fixed vectors `w_n` satisfy

\[
\|\mathbf w_n\|
\le
\tau_*^n\|\mathbf v_0\|.
\]

This converts frequency-dependent spatial rotation into an infinite but rapidly convergent hierarchy of fixed spatial vectors.

---

# 3. Positive-measure inequality

Let `X(omega) >= 0` be the reciprocal oscillator-strength density from the T-operator representation.

For each frequency,

\[
\sqrt{
\mathbf v_\delta^\dagger\mathbb X(\omega)\mathbf v_\delta
}
=
\|\mathbb X(\omega)^{1/2}\mathbf v_\delta\|
\]

and by the triangle inequality,

\[
\sqrt{
\mathbf v_\delta^\dagger\mathbb X\mathbf v_\delta
}
\le
\sum_{n=0}^\infty
\frac{|\delta|^n}{n!}
\sqrt{
\mathbf w_n^\dagger\mathbb X\mathbf w_n
}.
\]

Integrating the square over the band and applying Cauchy–Schwarz term by term gives

\[
\int_B
\mathbf v_\delta^\dagger\mathbb X(\omega)\mathbf v_\delta\,d\omega
\le
\left[
\sum_{n=0}^\infty
\frac{\Omega_s^n}{n!}
\sqrt{I_n}
\right]^2,
\]

where

\[
I_n
\equiv
\int_B
\mathbf w_n^\dagger\mathbb X(\omega)\mathbf w_n\,d\omega.
\]

---

# 4. High-frequency sum-rule branch

For each fixed `w_n`,

\[
I_n
\le
\frac\pi2\omega_p^2\|\mathbf w_n\|^2
\le
\frac\pi2\omega_p^2
\tau_*^{2n}\|\mathbf v_0\|^2.
\]

Therefore

\[
\sum_{n=0}^\infty
\frac{\Omega_s^n}{n!}\sqrt{I_n}
\le
\sqrt{\frac\pi2}\omega_p\|\mathbf v_0\|
\sum_{n=0}^\infty
\frac{(\Omega_s\tau_*)^n}{n!}.
\]

The series is exponential, yielding

\[
\boxed{
\int_B
\mathbf v_\delta^\dagger\mathbb X(\omega)\mathbf v_\delta\,d\omega
\le
\frac\pi2\omega_p^2\|\mathbf v_0\|^2
\exp(2\Omega_s\tau_*).
}
\]

---

# 5. Low-frequency/static branch

Let

\[
t_0\equiv\|\mathbb T_{0,D}\|_{\rm op}.
\]

For any fixed `w_n`, the low-frequency moment gives

\[
I_n
\le
\frac\pi2\omega_+^2
\mathbf w_n^\dagger\mathbb T_{0,D}\mathbf w_n
\le
\frac\pi2\omega_+^2 t_0
\|\mathbf w_n\|^2.
\]

Repeating the previous argument,

\[
\boxed{
\int_B
\mathbf v_\delta^\dagger\mathbb X(\omega)\mathbf v_\delta\,d\omega
\le
\frac\pi2\omega_+^2 t_0
\|\mathbf v_0\|^2
\exp(2\Omega_s\tau_*).
}
\]

Combining both moments,

\[
\boxed{
\int_B
\mathbf v_\delta^\dagger\mathbb X(\omega)\mathbf v_\delta\,d\omega
\le
\frac\pi2\|\mathbf v_0\|^2
e^{2\Omega_s\tau_*}
\min\left[
\omega_p^2,
\omega_+^2t_0
\right].
}
\]

**Status:** PROVED.

---

# 6. Capture/QFI bound

For a reciprocal passive structure,

\[
\omega\operatorname{Im}\mathbb T=\mathbb X.
\]

Therefore

\[
\boxed{
\int_BP_{\rm cap}(\omega)d\omega
\le
\frac{\epsilon_0\pi}{4}
\|\mathbf v_0\|^2
e^{2\Omega_s\tau_*}
\min\left[
\omega_p^2,
\omega_+^2t_0
\right].
}
\]

For constant incident-power normalization `P_in` and flat coherent-state QFI weighting,

\[
\boxed{
\bar\eta_{\mathcal I}
\le
\min\left[
1,
\frac{\epsilon_0\pi\|\mathbf v_0\|^2}
{8P_{\rm in}\Omega_s}
\,e^{2\Omega_s\tau_*}
\min(\omega_p^2,\omega_+^2t_0)
\right].
}
\]

This is the plane-wave-phase-robust version of the fixed-profile theorem.

---

# 7. Uniform-magnitude plane-wave corollary

If `|v_0|=|E_0|` over design volume `V`, with reference incident aperture `A`,

\[
\|\mathbf v_0\|^2=|E_0|^2V,
\]

\[
P_{\rm in}=\frac12c\epsilon_0|E_0|^2A.
\]

Then

\[
\boxed{
\bar\eta_{\mathcal I}(\Omega_s)
\le
\min\left[
1,
\frac{\pi V}{4cA\Omega_s}
\,e^{2\Omega_s\tau_*}
\min\left(
\omega_p^2,
(\omega_0+\Omega_s)^2t_0
\right)
\right].
}
\]

For a plane wave through a detector whose maximum centered projected extent is `R_parallel`,

\[
\tau_*\le R_\parallel/c.
\]

Define

\[
\epsilon_{\rm phase}
\equiv
\Omega_sR_\parallel/c.
\]

The finite-spatial-phase correction is simply

\[
\boxed{C_{\rm phase}=e^{2\epsilon_{\rm phase}}.}
\]

---

# 8. Quantitative size of the correction

For baseband frequency `f_s`,

\[
\epsilon_{\rm phase}
=\frac{2\pi f_sR_\parallel}{c}.
\]

Examples:

| `R_parallel` | `f_s` | `epsilon_phase` | `exp(2 epsilon_phase)` |
|---:|---:|---:|---:|
| `1 mm` | `1 GHz` | `0.02096` | `1.0428` |
| `1 mm` | `10 GHz` | `0.2096` | `1.5207` |
| `100 um` | `10 GHz` | `0.02096` | `1.0428` |
| `100 um` | `100 GHz` | `0.2096` | `1.5207` |
| `50 um` | `10 GHz` | `0.01048` | `1.0212` |

Thus for ordinary micron-to-submillimeter photodetector dimensions and GHz-scale electrical bandwidths, the fixed-spatial-profile approximation can be quantitatively excellent even when the device is many optical wavelengths across.

The controlling wavelength is the **modulation wavelength**, not the optical carrier wavelength.

---

# 9. Interpretation

The previous concern that a frequency-dependent plane-wave profile necessarily introduces a large spatial-channel factor is too pessimistic in the narrow-sideband regime.

The correct hierarchy is:

- if `Omega_s R/c << 1`, use the phase-robust fixed-mode theorem with a small explicit correction;
- if `Omega_s R/c ~ 1` or larger, genuine spatio-spectral channel structure becomes important;
- at very large `Omega_s R/c`, the present exponential estimate becomes loose and a communication-mode/space-bandwidth treatment is preferable.

This substantially enlarges the physically relevant class covered by the finite-band optical capture theorem.

---

# 10. Literature connection

Miller, Kuang, and Miller (Nature Photonics 19, 284–290, 2025) provide a physical/rigo­rous spherical-wave picture for the finite number of strongly coupled spatial channels entering or escaping a bounded volume, with a heuristic strong-channel count per polarization

\[
N_{\rm SH}\simeq(kR)^2.
\]

That communication-mode framework is the natural next tool when the narrow-sideband phase condition fails.

Amaolo et al. (2026) provide the closest single-frequency information-capacity formulation for structured photonic channels; their stated finite-band extension remains open.

---

# 11. Next action

Use this result to divide WP5 into two regimes:

### Regime A — narrow modulation in space

\[
\Omega_sR/c\ll1.
\]

The optical frontend theorem is already controlled analytically. Focus on tightening material/static resources and composing with the internal detector theorem.

### Regime B — spatially broadband modulation

\[
\Omega_sR/c\gtrsim1.
\]

Introduce an explicit communication-mode / tunnelling channel resource and derive a finite-band matrix optimization.

For most conventional high-speed photodetectors, Regime A is likely the relevant theoretical route.
