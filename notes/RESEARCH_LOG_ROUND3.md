# Research Log — Round 3

**Date:** 2026-08-19

## 1. Incident-channel QFI capture lemma

For coherent-state optical modulation through a passive, linear, time-invariant, frequency-preserving frontend, the incident coherent displacement is unitarily distributed among optical outputs and absorptive bath/capture modes.

If `tau(omega)` is the fraction of the normalized incident channel sent into the internal capture subspace, then

\[
F_{\rm cap}^{Q}
=\int\frac{d\omega}{2\pi}\tau(\omega)\mathcal J_{\rm in}(\omega).
\]

Any downstream electrical record obeys

\[
F_{\rm elec}\le F_{\rm cap}^{Q}.
\]

Thus for a flat sideband-QFI task,

\[
\bar\eta_{\mathcal I}
\le
\frac{1}{2\Omega_s}
\int_{\omega_0-\Omega_s}^{\omega_0+\Omega_s}
\tau(\omega)d\omega.
\]

**Status:** PROVED for coherent-state displacement encoding and the stated passive frontend class.

Primary note: `WP5_INCIDENT_CHANNEL_QFI_SUM_RULE.md`.

---

## 2. Extinction-sum-rule rigor correction

An initial shortcut used a scalar all-frequency extinction/absorption sum rule proportional to electron number. A literature audit found that blanket macroscopic extinction-cross-section sum-rule claims have been criticized when not derived directly from first-principles scattering.

Decision:

- retain the electron-number formula only as a microscopic electric-dipole/TRK corollary;
- use Zhang–Monticone–Miller's rigorous matrix-valued T-operator sum rules for arbitrary passive scatterers.

**Status:** CORRECTION / DECISION.

---

## 3. 2026 novelty constraint: maximum Shannon capacity of photonic structures

Amaolo et al., npj Nanophotonics 3, 14 (2026), already combine information theory, Green functions, Maxwell constraints, and structural optimization to bound Shannon capacity of structured photonic channels.

Their paper explicitly states that the published results are single-frequency and identifies finite-band spectral-sum-rule/delay-bandwidth generalization plus macroscopic-QED extensions as future work.

Consequences:

- generic `information theory + electromagnetic bounds` is not novel;
- finite-band optical information is still an open direction in their stated framework;
- UPRP remains distinct by adding actual optical capture, endogenous detector thermodynamics/noise, and an electrical record.

**Status:** VERIFIED novelty constraint.

Primary note: `docs/NOVELTY_AUDIT_ROUND2.md`.

---

## 4. Fixed-spatial-mode T-operator finite-band theorem

Using unrenormalized positive-frequency oscillator variables of Zhang–Monticone–Miller, define

\[
\mathbb Z(\omega)=\omega\operatorname{Im}\mathbb T(\omega)
=\mathbb X(\omega)+\mathbb Y(\omega),
\]

with

\[
\mathbb X\succeq0,
\qquad
-\mathbb X\preceq\mathbb Y\preceq\mathbb X.
\]

The sum rules imply

\[
\int_0^\infty\mathbb Xd\omega
\preceq\frac\pi2\omega_p^2\mathbb I_D,
\]

\[
\int_0^\infty\frac{\mathbb X}{\omega^2}d\omega
\preceq\frac\pi2\mathbb T_{0,D}.
\]

For a band `B=[omega_-,omega_+]` and a fixed incident vector `v`,

\[
\int_Bv^\dagger\mathbb Xv\,d\omega
\le
\frac\pi2
\min\left[
\omega_p^2\|v\|^2,
\omega_+^2v^\dagger\mathbb T_{0,D}v
\right].
\]

Because `Z <= 2X`, the general passive extinction/capture-work bound is

\[
\int_BP_{\rm cap}d\omega
\le
\frac{\epsilon_0\pi}{2}
\min\left[
\omega_p^2\|v\|^2,
\omega_+^2v^\dagger\mathbb T_{0,D}v
\right].
\]

For reciprocal structures (`Y=0`), the RHS is divided by two:

\[
\boxed{
\int_BP_{\rm cap}d\omega
\le
\frac{\epsilon_0\pi}{4}
\min\left[
\omega_p^2\|v\|^2,
\omega_+^2v^\dagger\mathbb T_{0,D}v
\right].
}
\]

After constant incident-power normalization and flat-QFI weighting, this directly bounds captured QFI.

**Status:** PROVED for a fixed incident spatial vector.

Primary note: `WP5_T_OPERATOR_FINITE_BAND_CAPTURE.md`.

---

## 5. Electrically-small uniform-field corollary

For a reciprocal detector sufficiently small that the incident field is nearly uniform across the optical sideband band, with detector/design volume `V`, aperture `A`, and projected static polarizability-volume `alpha_stat`,

\[
\boxed{
\bar\eta_{\mathcal I}(\Omega_s)
\le
\min\left[
1,
\frac{\pi}{4cA\Omega_s}
\min\left(
\omega_p^2V,
(\omega_0+\Omega_s)^2\alpha_{\rm stat}
\right)
\right].
}
\]

The first branch reproduces electron-number/total-oscillator-strength scaling. The second uses static response and can be significantly tighter for low optical carrier frequency / small static response.

At `lambda_0=10 um`, `r=0.9`, narrow sideband, the static-branch frequency ceiling scales as

\[
f_s\lesssim1.64\times10^{19}
\left(\alpha_{\rm stat}/A\right)\ {\rm Hz/m}.
\]

Illustrative effective static lengths:

- `1 um` -> `~16.4 THz`;
- `100 nm` -> `~1.64 THz`;
- `10 nm` -> `~164 GHz`.

These are scaling examples, not material-specific photodetector limits.

**Status:** DERIVED corollary.

---

## 6. New spatial-channel obstruction

The fixed-vector theorem does not automatically apply to a propagating field over a large device because

\[
v(\omega,r)\propto e^{i\omega\hat k\cdot r/c}
\]

rotates in spatial function space with frequency.

If all incident profiles lie in an `M`-dimensional fixed subspace, positivity plus the matrix sum rule gives a coarse bound proportional to `M`.

Therefore the arbitrary finite-band theorem needs an explicit **spatio-spectral degrees-of-freedom / footprint / channel-rank resource**.

This is not a nuisance parameter: without it, different frequency slices can consume different orthogonal oscillator-strength directions.

**Status:** PROVED qualitative necessity in finite-dimensional subspace formulation; tight continuous space-bandwidth theorem OPEN.

---

## 7. Current resource hierarchy

The likely minimum resource hierarchy is now

\[
\boxed{
\text{source temporal task}
+
\text{matter oscillator strength}
+
\text{static/finite-band EM response}
+
\text{spatial channel/footprint resource}
+
\text{internal thermokinetic resources}.
}
\]

Temperature, entropy production, and stationary activity alone are insufficient by WP4.

---

## 8. Current strongest restricted completion theorem

For the intersection of:

- coherent-state optical encoding;
- passive reciprocal optical frontend;
- fixed incident spatial profile over the sideband band;
- finite T-operator high/low-frequency resource bounds;
- WP3/WP4 proper single-event downstream detector assumptions;

we have two independent ceilings:

\[
\bar\eta_{\rm total}\le B_{\rm opt}(\Omega_s),
\qquad
\bar\eta_{\rm total}\le B_{\rm trans}(\Omega_s).
\]

Hence

\[
\boxed{
\bar\eta_{\rm total}(\Omega_s)
\le
\min\{B_{\rm opt}(\Omega_s),B_{\rm trans}(\Omega_s)\}.
}
\]

This is a valid restricted optical-plus-internal resource theorem. It is not yet the full UPRP theorem.

---

## 9. Immediate next action

Derive a tight frequency-dependent incident-channel extension using a controlled spatial resource. The natural comparison target is Amaolo et al.'s single-frequency Maxwell channel formulation combined with Zhang–Monticone–Miller's finite-frequency oscillator measure.

Possible routes:

1. finite-dimensional source/receiver channel basis with rank `M`;
2. space-bandwidth/Shannon-number bound for fields inside a finite design domain;
3. direct semidefinite optimization of frequency-dependent channel vectors against the matrix oscillator measure;
4. domain/volume/footprint-limited plane-wave channel family.

Then compose the resulting optical capture ceiling with the WP3/WP4 internal transducer theorem.
