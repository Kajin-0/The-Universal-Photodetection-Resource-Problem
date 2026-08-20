# WP9 — Finite-band quantum spectral composition theorem

**Date:** 2026-08-20

## Purpose

WP5 bounds the **band-averaged passive optical capture probability**. WP7 bounds the **pointwise source-to-detector transfer probability** through a finite interaction action. WP8 bounds the detector pointer's pre-existing directional SLD-QFI resource.

This note composes those three resources exactly for a flat coherent-state sideband-information task in a narrow band where the detector pointer resource may be treated as frequency independent.

A nontrivial result appears: the optimal spectral allocation changes from concentrated to uniform when the pointer QFI crosses the vacuum value `J=2`.

---

## 1. Pointwise QFI-transfer law

For coherent optical displacement at one frequency and a detector pointer with directional translation QFI bounded by

\[
J_D,
\]

the SLD-Stam theorem gives

\[
\boxed{
\eta(\tau)
\le
f_J(\tau)
\equiv
\frac{\tau J_D}
{2(1-\tau)+\tau J_D},
}
\]

where `tau` is the passive source-to-detector single-particle transfer probability.

The interaction-action theorem supplies a pointwise cap

\[
\boxed{
0\le\tau(\omega)\le\tau_{\max}
\equiv\sin^2\Gamma_{\max}
}
\]

for a uniform action cap `Gamma_max <= pi/2` across the task band.

---

## 2. Electromagnetic finite-band resource

For a flat sideband-QFI task over bandwidth `2 Omega_s`, define the band average

\[
\bar\tau
=\frac1{2\Omega_s}
\int_{-\Omega_s}^{\Omega_s}
\tau(\Omega)d\Omega.
\]

WP5 gives a passive electromagnetic ceiling

\[
\boxed{
\bar\tau\le B_{\rm opt}(\Omega_s),
}
\]

where `B_opt` can be the T-operator finite-band bound including the plane-wave phase correction when required.

Because the pointwise action cap also implies `bar tau <= tau_max`, define

\[
B\equiv\min\{B_{\rm opt},\tau_{\max}\}.
\]

The problem is now exact:

> maximize the flat-band average of `f_J(tau)` subject to `0<=tau<=tau_max` and `average(tau)<=B_opt`.

---

## 3. Curvature transition at `J_D=2`

Differentiate

\[
f_J(\tau)
=\frac{\tau J_D}{2+\tau(J_D-2)}.
\]

Then

\[
f_J'(\tau)
=\frac{2J_D}{[2+\tau(J_D-2)]^2},
\]

\[
\boxed{
f_J''(\tau)
=-\frac{4J_D(J_D-2)}
{[2+\tau(J_D-2)]^3}.
}
\]

Therefore:

- `J_D>2`: `f_J` is concave;
- `J_D=2`: `f_J(tau)=tau` is linear;
- `J_D<2`: `f_J` is convex.

The threshold `J_D=2` is exactly the coherent/vacuum displacement QFI in the adopted normalization.

---

## 4. Exact spectral optimization: resourceful pointer `J_D >= 2`

For a concave function, Jensen gives

\[
\overline{f_J(\tau)}
\le
f_J(\bar\tau).
\]

Since `f_J` is increasing,

\[
\boxed{
\bar\eta_{\mathcal I}
\le
f_J\!\left(
\min\{B_{\rm opt},\tau_{\max}\}
\right),
\qquad J_D\ge2.
}
\]

The bound is attained, within the abstract resource constraints, by spreading the coupling uniformly across the task band at

\[
\tau(\omega)=\min\{B_{\rm opt},\tau_{\max}\}.
\]

Thus a sufficiently metrologically resourceful pointer favors **spectrally uniform coupling**.

---

## 5. Exact spectral optimization: thermal/noisy pointer `J_D <= 2`

For convex `f_J` with `f_J(0)=0`, the graph lies below the chord joining `0` and `tau_max`:

\[
f_J(\tau)
\le
\frac{\tau}{\tau_{\max}}
f_J(\tau_{\max}).
\]

Averaging gives

\[
\boxed{
\bar\eta_{\mathcal I}
\le
f_J(\tau_{\max})
\min\left\{
1,
\frac{B_{\rm opt}}{\tau_{\max}}
\right\},
\qquad J_D\le2.
}
\]

This is attained by a **bang-bang spectral allocation** when `B_opt<tau_max`: use `tau=tau_max` over a fraction `B_opt/tau_max` of the band and zero coupling over the rest.

Thus a noisy pointer favors concentrating limited electromagnetic coupling into a narrower useful subband.

At `J_D=2`, both branches reduce continuously to

\[
\bar\eta\le\min\{B_{\rm opt},\tau_{\max}\}.
\]

**Status:** PROVED exact optimization under the stated flat-band scalar resource constraints.

---

## 6. Equilibrium thermal-pointer corollary

For an equilibrium harmonic pointer,

\[
J_D=2t_\beta,
\qquad
t_\beta=\tanh\frac{\beta\hbar\omega_D}{2}\le1.
\]

Therefore it always lies in the convex branch. Using

\[
f_\beta(\tau)
=\frac{\tau t_\beta}
{1-\tau+\tau t_\beta},
\]

we obtain

\[
\boxed{
\bar\eta_{\mathcal I}
\le
\frac{\tau_{\max}t_\beta}
{1-\tau_{\max}+\tau_{\max}t_\beta}
\min\left\{
1,
\frac{B_{\rm opt}}{\tau_{\max}}
\right\}.
}
\]

If the electromagnetic resource is the limiting one,

\[
B_{\rm opt}<\tau_{\max},
\]

this simplifies to

\[
\boxed{
\bar\eta_{\mathcal I}
\le
B_{\rm opt}
\frac{t_\beta}
{1-\tau_{\max}+\tau_{\max}t_\beta}.
}
\]

This is an explicit finite-band **electromagnetic + temperature + interaction-action** information ceiling.

---

## 7. Narrow-band T-operator bandwidth consequence

In the narrow-sideband/small-footprint regime WP5 gives schematically

\[
B_{\rm opt}(\Omega_s)
\le
\min\left\{1,\frac{\Omega_{\rm EM}}{\Omega_s}\right\},
\]

where

\[
\Omega_{\rm EM}
=\frac{\pi V}{4cA}
\min(\omega_p^2,\omega_0^2t_0)
\]

for the reciprocal electrically-small model.

In the thermal convex branch and the regime

\[
\Omega_{\rm EM}/\Omega_s<\tau_{\max},
\]

a target average information fraction `q` requires

\[
q
\le
\frac{\Omega_{\rm EM}}{\Omega_s}
\frac{t_\beta}
{1-\tau_{\max}+\tau_{\max}t_\beta}.
\]

Hence

\[
\boxed{
\Omega_s
\le
\frac{\Omega_{\rm EM}}{q}
\frac{t_\beta}
{1-\tau_{\max}+\tau_{\max}t_\beta}.
}
\]

This is a direct finite-band temperature/coupling/electromagnetic-resource bound for the restricted equilibrium passive-linear branch.

---

## 8. Resourceful-pointer corollary

For a pointer resource cap `J_D>=2`, define the transfer probability required to retain information fraction `q`:

\[
q=f_J(\tau_q).
\]

Solving gives

\[
\boxed{
\tau_q
=\frac{2q}
{J_D(1-q)+2q}.
}
\]

Therefore the concave-branch finite-band theorem requires

\[
\boxed{
\min\{B_{\rm opt},\tau_{\max}\}
\ge
\frac{2q}
{J_D(1-q)+2q}.
}
\]

A finite free-energy resource may be inserted through the global WP8 bound on `J_D`.

---

## 9. Interpretation

The three resources play genuinely different roles:

1. `B_opt` limits total coupling weight available across the optical information band.
2. `tau_max` limits how strongly any one frequency can couple within the available interaction time/action.
3. `J_D` determines how efficiently a given amount of transferred displacement can be converted into detector/electrical Fisher information.

The vacuum threshold `J_D=2` separates two spectral strategies:

\[
\boxed{
J_D<2:\ \text{concentrate bandwidth};
\qquad
J_D>2:\ \text{spread bandwidth}.
}
\]

This is a new structural consequence of composing the UPRP optical and apparatus resource bounds. Novelty relative to broader communication/resource-allocation literature remains to be audited.

---

## 10. Limitations

This theorem assumes:

- coherent displacement encoding;
- passive linear frequency-preserving channels;
- independent scalar frequency channels or a basis in which the relevant singular channel is resolved;
- a frequency-independent pointer-QFI cap `J_D` across the narrow task band;
- a uniform pointwise interaction-action cap;
- no active gain without explicit pump/noise accounting.

A total free-energy budget shared among many frequency modes requires an additional resource-allocation optimization and is not solved here.
