# WP6 — Restricted Composite Photodetection Resource Theorem

**Date:** 2026-08-19

## Purpose

This note assembles the independently proved optical-front-end and internal-transducer bounds into one complete restricted theorem for finite-band optical-to-electrical information transfer.

The result is deliberately narrower than the ultimate UPRP target. It is a valid theorem for a physically useful class and provides a publication-grade scaffold for later generalization.

**Status:** PROVED under the explicit assumptions below. Novelty of the full composition remains provisional pending the dedicated literature gate.

---

# 1. Detector class

Assume all of the following.

## Optical input

1. The incident optical field is a coherent-state temporal mode centered at carrier frequency `omega_0`.
2. The encoded parameter appears in coherent displacement/amplitude modulation with baseband support

\[
|\Omega|\le\Omega_s,
\qquad
0<\Omega_s<\omega_0.
\]

3. The input QFI spectral density is flat over the task band for the explicit closed-form statements below. Non-flat tasks use the weighted form directly.

## Optical frontend

4. The optical frontend is passive, linear, time invariant, frequency preserving, and reciprocal.
5. It is contained in a finite design domain of volume `V` and is illuminated through reference aperture/incident-channel area `A`.
6. Its passive electromagnetic T-operator satisfies the Zhang–Monticone–Miller high- and low-frequency sum-rule resources characterized by

\[
\omega_p^2
\]

and

\[
t_0\equiv\|\mathbb T_{0,D}\|_{\rm op}.
\]

7. The sideband spatial profile is plane-wave-like,

\[
\mathbf v_\Omega(\mathbf r)
=e^{i\Omega\tau(\mathbf r)}\mathbf v_0(\mathbf r),
\qquad
|\tau(\mathbf r)|\le R/c,
\]

where `R` is the maximum projected half-extent of the frontend along the propagation direction.

## Internal detector

8. Captured photons enter a reversible post-absorption gateway state of a finite-state Markov event detector.
9. The electrical detection record cannot occur before first exit from that gateway state; there is no instantaneous optical-to-electrical feedthrough.
10. Events are in the low-overlap/single-event regime.
11. Useful forward optical throughput obeys

\[
f\ge f_*>0.
\]

12. Total dimensionless steady entropy-production rate and one-way stationary activity obey

\[
\sigma\le\Sigma,
\qquad
\mathcal A_{\rm tot}\le\mathcal A.
\]

13. The microscopic optical gateway is weak-coupling bosonic with occupation `n(omega_0)` and a separately bounded absolute spectral coupling

\[
\gamma(\omega_0)\le\gamma_{\max}.
\]

14. The zero-frequency successful-event probability is `eta_q <= 1`.

These assumptions are part of the theorem. Do not silently enlarge the class.

---

# 2. Information metric

Define

\[
\bar\eta_{\mathcal I}(\Omega_s)
=\frac{F_{\rm electrical}}
{F_{\rm incident}^{Q}}
\]

for the specified flat finite-band optical task.

By quantum/classical data processing,

\[
0\le\bar\eta_{\mathcal I}\le1.
\]

---

# 3. Optical-front-end ceiling

From `WP5_PLANE_WAVE_PHASE_ROBUSTNESS.md`, the reciprocal passive frontend obeys

\[
\boxed{
B_{\rm opt}(\Omega_s)
\equiv
\min\left[
1,
\frac{\pi V}{4cA\Omega_s}
 e^{2\Omega_sR/c}
\min\left(
\omega_p^2,
(\omega_0+\Omega_s)^2t_0
\right)
\right].
}
\]

The electrical information cannot exceed optical capture information, so

\[
\boxed{
\bar\eta_{\mathcal I}(\Omega_s)
\le B_{\rm opt}(\Omega_s).
}
\]

This part contains only passive electromagnetic resources and source geometry/task variables.

---

# 4. Internal thermokinetic ceiling

For the bosonic gateway,

\[
\Gamma_\downarrow
=\gamma(\omega_0)[n(\omega_0)+1]
\le
\gamma_{\max}[n+1].
\]

Define

\[
g(z)=\left(1-\frac1z\right)\ln z,
\qquad z\ge1,
\]

and

\[
Z_*=g^{-1}(\Sigma/f_*).
\]

The gateway occupancy/activity theorem gives

\[
\lambda_1
\le
\Lambda_{\rm micro},
\]

where

\[
\boxed{
\Lambda_{\rm micro}
=
\frac{\mathcal A\gamma_{\max}[n(\omega_0)+1]}{f_*}
\,g^{-1}\!\left(\frac{\Sigma}{f_*}\right).
}
\]

The unavoidable first-exit waiting time therefore gives the flat-band information ceiling

\[
\boxed{
B_{\rm trans}(\Omega_s)
\equiv
\eta_q
\frac{\Lambda_{\rm micro}}{\Omega_s}
\arctan\!\left(
\frac{\Omega_s}{\Lambda_{\rm micro}}
\right).
}
\]

Hence

\[
\boxed{
\bar\eta_{\mathcal I}(\Omega_s)
\le B_{\rm trans}(\Omega_s).
}
\]

---

# 5. Composite theorem

Both bounds apply to the same information-transfer chain, so

\[
\boxed{
\bar\eta_{\mathcal I}(\Omega_s)
\le
\min\left[
B_{\rm opt}(\Omega_s),
B_{\rm trans}(\Omega_s)
\right].
}
\]

This is the current restricted **Universal Photodetection Resource inequality**.

It separates two physically distinct bottlenecks:

\[
\boxed{
\text{finite-band electromagnetic capture}
}
\]

and

\[
\boxed{
\text{finite-rate thermokinetic conversion/readout}.
}
\]

No choice of downstream electronics can recover optical QFI never captured, and no optical frontend can bypass the first-exit transduction delay under the stated event-detector assumptions.

**Status:** PROVED by composition of independently proved inequalities.

---

# 6. Necessary conditions for target information retention

Suppose the specification is

\[
\bar\eta_{\mathcal I}(\Omega_s)\ge r,
\qquad 0<r<1.
\]

A necessary condition is

\[
B_{\rm opt}(\Omega_s)\ge r
\]

and

\[
B_{\rm trans}(\Omega_s)\ge r.
\]

If

\[
r>\eta_q,
\]

the specification is impossible even at zero bandwidth.

For `r <= eta_q`, define `x(q)` as the unique positive solution of

\[
\frac{\arctan x}{x}=q,
\qquad 0<q<1.
\]

Then the internal condition is exactly

\[
\boxed{
\Omega_s
\le
x\!\left(\frac r{\eta_q}\right)
\Lambda_{\rm micro}.
}
\]

Examples for `eta_q=1`:

| `r` | `x(r)` | necessary `Omega_s/Lambda_micro <=` |
|---:|---:|---:|
| 0.99 | 0.17478 | 0.17478 |
| 0.95 | 0.40565 | 0.40565 |
| 0.90 | 0.60253 | 0.60253 |
| 0.80 | 0.94913 | 0.94913 |
| 0.50 | 2.33112 | 2.33112 |

The optical condition remains an exact implicit inequality because `Omega_s` appears in the phase and upper-frequency factors.

---

# 7. Narrow-sideband / small-modulation-phase corollary

In the regime

\[
\Omega_s\ll\omega_0,
\qquad
\frac{\Omega_sR}{c}\ll1,
\]

we may replace

\[
e^{2\Omega_sR/c}=1+O(\Omega_sR/c)
\]

and

\[
(\omega_0+\Omega_s)^2
=\omega_0^2[1+O(\Omega_s/\omega_0)].
\]

Define the optical resource scale

\[
\boxed{
\Omega_{\rm EM}
\equiv
\frac{\pi V}{4cA}
\min\left[
\omega_p^2,
\omega_0^2t_0
\right].
}
\]

Then

\[
B_{\rm opt}(\Omega_s)
\lesssim
\min\left[1,rac{\Omega_{\rm EM}}{\Omega_s}ight]
\]

to leading order.

Consequently a target `bar eta_I >= r` requires

\[
\boxed{
\Omega_s
\lesssim
\frac{\Omega_{\rm EM}}{r}.
}
\]

Combining optical and internal requirements gives the explicit leading-order composite bandwidth condition

\[
\boxed{
\Omega_s
\lesssim
\min\left[
\frac{\Omega_{\rm EM}}{r},
\;
 x\!\left(\frac r{\eta_q}\right)
\Lambda_{\rm micro}
\right].
}
\]

or, fully expanded,

\[
\boxed{
\Omega_s
\lesssim
\min\left[
\frac{\pi V}{4cAr}
\min(\omega_p^2,\omega_0^2t_0),
\;
 x\!\left(\frac r{\eta_q}\right)
\frac{\mathcal A\gamma_{\max}[n+1]}{f_*}
 g^{-1}\!\left(\frac{\Sigma}{f_*}\right)
\right].
}
\]

This is the most compact current theorem statement.

---

# 8. Dimension check

`omega_p^2` and `omega_0^2 t_0` both have units `s^-2` because `T_0` is dimensionless in the susceptibility/T-operator normalization used here.

`V/A` has units of length and `1/c` has units of time/length. Thus

\[
\Omega_{\rm EM}
\sim (V/A)(1/c)(s^{-2})
\sim s^{-1}.
\]

For the internal branch,

\[
\mathcal A,\gamma_{\max},f_*
\sim s^{-1},
\]

so

\[
\frac{\mathcal A\gamma_{\max}}{f_*}
\sim s^{-1}.
\]

All bandwidth terms have correct units.

---

# 9. Relation to the WP4 no-go theorem

The appearance of `gamma_max` is not an arbitrary technical choice. WP4 proves that a finite theorem **cannot** be written using only

\[
T,\hbar\omega_0,
\text{detailed balance},
 f_*,\mathcal A,\Sigma,
\eta_q
\]

in the reversible Markov event-detector class.

A family exists in which all of those remain finite while the absolute optical coupling and detector speed diverge.

Thus an absolute microscopic coupling resource is logically necessary unless it can be derived from the electromagnetic/matter resource set itself.

A future improvement may replace the separately supplied `gamma_max` by a finite-band consequence of the same T-operator/oscillator-strength resources. That elimination is not yet proved.

---

# 10. Why the result is not a generic Maxwell-capacity theorem

Amaolo et al. (2026) already combine information theory and Maxwell constraints to bound Shannon capacity of structured photonic channels at a single frequency. The present theorem is different in scope:

1. finite optical sideband / temporal task;
2. QFI-normalized capture rather than prescribed receiver-field Shannon SNR;
3. a physical absorptive detector frontend;
4. endogenous finite-temperature Markov transduction;
5. an explicit no-go theorem showing why an absolute microscopic coupling resource is required.

Do not describe the electromagnetic-information part alone as novel.

---

# 11. Limitations

The theorem does not yet cover:

- arbitrary quantum optical states beyond coherent displacement encoding;
- active/gain optical frontends;
- strong or ultrastrong light–matter coupling;
- non-Markovian internal detector dynamics;
- photoconductive continuous-occupancy output without the event-gateway structure;
- direct optical-to-electrical feedthrough;
- severe event overlap/saturation;
- highly spatially broadband modulation with `Omega_s R/c >= O(1)` without using the more general communication-mode treatment;
- a derivation of `gamma_max` directly from the T-operator resource set.

These exclusions must remain explicit.

---

# 12. Next theoretical gate

The next question is no longer whether a finite restricted theorem exists; it does.

The next question is:

> Can `gamma_max` and the Markov first-exit assumption be replaced by a genuinely quantum light–matter interaction resource, while retaining a bound directly on optical-to-electrical information transfer?

The leading candidate resource is an interaction-Hamiltonian norm/variance or channel quantum Fisher metric. Existing temporal-Fisher speed limits show that interaction-Hamiltonian fluctuations bound nonunitary state-evolution speed, but their unitarily residual Bures distance deliberately discards purely unitary pointer rotations. Therefore they cannot simply be inserted into UPRP without an additional detector-record distinguishability argument.
