# WP15 — Delay concentration and localized optical-capture capacity

**Date:** 2026-08-20

## Purpose

WP11 proved that unresolved event-to-event delay dispersion, rather than deterministic transit latency, reduces event-record information bandwidth. WP5 separately bounds finite-band optical capture.

The missing bridge is not total detector thickness or total optical design volume. It is the ability to capture a large fraction of incident photons inside a **narrow delay slice**.

This note derives an exact concentration-function theorem for the ideal event-record model and identifies the optical quantity that any genuine joint optical/transport theorem must bound.

---

# 1. Event-record model

Let incident photons form a weakly modulated Poisson process. Each incident photon is captured with total probability

\[
0\le \eta_c\le 1.
\]

Conditional on successful capture, let the electrical event appear after random delay `D` with probability law `p_D`.

Let

\[
\phi_D(\Omega)=\mathbb E[e^{-i\Omega D}].
\]

For the ideal complete event-timestamp record with no dark counts,

\[
\boxed{
\eta_{\mathcal I}(\Omega)
=\eta_c|\phi_D(\Omega)|^2.
}
\]

This is the source-normalized Fisher-information transfer fraction for small fractional photon-flux modulation.

---

# 2. Flat-band average

For a flat information task on

\[
|\Omega|\le\Omega_s,
\]

define

\[
\bar\eta_{\mathcal I}
=\frac1{2\Omega_s}
\int_{-\Omega_s}^{\Omega_s}
\eta_{\mathcal I}(\Omega)d\Omega.
\]

For two independent copies `D,D'`,

\[
|\phi_D(\Omega)|^2
=\mathbb E[e^{-i\Omega(D-D')}].
\]

Averaging over the symmetric band gives

\[
\boxed{
\bar\eta_{\mathcal I}
=\eta_c\,
\mathbb E\left[
\operatorname{sinc}\big(\Omega_s(D-D')\big)
\right],
}
\]

with

\[
\operatorname{sinc}x=\frac{\sin x}{x}.
\]

**Status:** PROVED.

---

# 3. Delay concentration function

Define the conditional Levy concentration function of the delay distribution

\[
Q_D(\Delta t)
=\sup_a
\Pr[D\in[a,a+\Delta t]].
\]

Define the corresponding **absolute incident-photon localized capture fraction**

\[
\boxed{
M_D(\Delta t)
=\eta_c Q_D(\Delta t).
}
\]

Thus `M_D(Delta t)` is the largest fraction of all incident photons that can be successfully captured into any electrical-delay window of width `Delta t`.

This is the natural joint optical/transport quantity.

---

# 4. General concentration inequality

Choose any `x>0` and define

\[
c_x=\sup_{|u|\ge x}|\operatorname{sinc}u|.
\]

Then `0<=c_x<1` for every `x>0` away from zero.

Split pairs `(D,D')` according to

\[
|D-D'|<x/\Omega_s
\]

or its complement. On the first set, `sinc<=1`; on the second set,

\[
\operatorname{sinc}[\Omega_s(D-D')]\le c_x.
\]

Hence

\[
\frac{\bar\eta_{\mathcal I}}{\eta_c}
\le
c_x+(1-c_x)
\Pr\left[|D-D'|<\frac{x}{\Omega_s}\right].
\]

For fixed `D=d`, the event `|D-D'|<a` places `D'` inside an interval of width `2a`. Therefore

\[
\Pr(|D-D'|<a)\le Q_D(2a).
\]

Thus

\[
\bar\eta_{\mathcal I}
\le
c_x\eta_c
+(1-c_x)M_D\left(\frac{2x}{\Omega_s}\right).
\]

Since `eta_c<=1`,

\[
\boxed{
\bar\eta_{\mathcal I}
\le
c_x
+(1-c_x)M_D\left(\frac{2x}{\Omega_s}\right).
}
\]

This is a universal upper bound within the ideal Poisson event-record model.

**Status:** PROVED.

---

# 5. Necessary localized-capture condition

If a target average information fraction `q` is required and

\[
q>c_x,
\]

then necessarily

\[
\boxed{
M_D\left(\frac{2x}{\Omega_s}\right)
\ge
\frac{q-c_x}{1-c_x}.
}
\]

Thus high finite-band information transfer demands that a large absolute fraction of incident photons be captured into a sufficiently narrow delay slice.

---

# 6. Convenient explicit choice x=pi/2

For

\[
x=\pi/2,
\]

the sinc function is still on its decreasing first positive lobe and all later side lobes are smaller, so

\[
\boxed{c_{\pi/2}=2/\pi.}
\]

Therefore

\[
\boxed{
\bar\eta_{\mathcal I}
\le
\frac2\pi
+\left(1-\frac2\pi\right)
M_D\left(\frac\pi{\Omega_s}\right).
}
\]

Since

\[
\frac\pi{\Omega_s}=\frac1{2f_s},
\qquad \Omega_s=2\pi f_s,
\]

a target `q>2/pi` requires

\[
\boxed{
M_D\left(\frac1{2f_s}\right)
\ge
\frac{q-2/\pi}{1-2/\pi}.
}
\]

Reference values:

- `q=0.90`: required localized capture fraction `>= 0.7248`;
- `q=0.95`: required localized capture fraction `>= 0.8624`;
- `q=0.99`: required localized capture fraction `>= 0.9725`.

Interpretation: preserving 99% of incident optical information on average across a flat baseband requires roughly 97% of incident photons to be captured inside some delay window shorter than half one period at the band edge.

---

# 7. Why total optical volume/thickness cannot replace M_D

A tempting but invalid step is to identify the total optical matching thickness or total electromagnetic design volume with the width of the carrier-delay distribution.

That fails physically.

A passive optical structure may occupy substantial volume while irreversible absorption is concentrated in a much thinner active region. The canonical example is a Salisbury-screen-type absorber: a thin resistive sheet supplies dissipation while a lossless spacer and reflector supply optical matching phase.

Therefore a Rozanov thickness bound on the **whole matching structure** does not imply a lower bound on the thickness of the region in which mobile charge is generated.

Likewise, the global WP5 T-operator resource

\[
\omega_p^2V
\]

for the entire optical design domain does not by itself bound how much of the absorbed power can be funneled into a narrow electrical-delay subset.

Hence

\[
\boxed{
\text{total finite-band capture resource}
+v_{\max}
\not\Rightarrow
\text{transit-dispersion information bound}
}
\]

without a localized-capture/participation resource.

**Status:** physical counterexample mechanism established; a fully parameter-fixed EM counterexample family can be developed if needed.

---

# 8. Localized optical-capture capacity

Define a detector-class-dependent function

\[
\boxed{
\mathcal C_{\rm loc}(\Delta t;\mathcal R_{\rm EM})
=\sup_{\text{admissible detectors}}
M_D(\Delta t),
}
\]

where `R_EM` denotes the allowed electromagnetic/matter/geometry resources.

Then the concentration theorem immediately gives

\[
\boxed{
\bar\eta_{\mathcal I}(\Omega_s)
\le
c_x
+(1-c_x)
\mathcal C_{\rm loc}\left(\frac{2x}{\Omega_s};\mathcal R_{\rm EM}\right).
}
\]

This is the correct formal composition target for WP5 + WP11.

Any rigorous upper bound on `C_loc` becomes a joint optical-capture/transport information-bandwidth theorem.

Conversely, if `C_loc(delta)` can approach unity for arbitrarily small `delta` while the claimed resource set remains bounded, then no such joint information-bandwidth theorem exists for that resource set.

---

# 9. Relation to probability theory

The use of a concentration function and a characteristic function is mathematically adjacent to classical Levy/Esseen concentration inequalities. That probability-theory connection is prior art and must not be claimed as new.

The project-specific use is the interpretation

\[
\text{delay characteristic function}
\leftrightarrow
\text{photodetector information transfer},
\]

and the resulting identification of localized optical capture as a missing detector resource.

Useful literature anchors:

- classical Levy concentration function;
- Esseen inequalities relating concentration functions and characteristic functions.

---

# 10. Consequences for the research program

The correct hierarchy is now more precise:

\[
\boxed{
\text{finite-band total optical capture}
\neq
\text{finite-band localized optical capture}.
}
\]

The next theorem must bound `C_loc`, not merely total absorption.

Promising restricted classes:

1. homogeneous Beer-Lambert semiconductor absorber, where absorption depth and optical attenuation are directly linked;
2. single-material planar active layer with no external passive concentrator;
3. finite local susceptibility and bounded active-material oscillator-strength density;
4. structures in which all optically participating material is also the charge-generating material;
5. finite active participation ratio / local dissipation-density constraints.

The unrestricted arbitrary-geometry class likely requires an explicit active-participation/localization resource.

---

# Status

**PROVED:** delay-concentration theorem and necessary localized-capture condition for the ideal event-record model.

**NO-GO IDENTIFIED:** total optical matching thickness/volume is not a valid proxy for carrier-delay spread.

**OPEN:** derive a first-principles electromagnetic upper bound on localized capture capacity for a useful semiconductor detector class.