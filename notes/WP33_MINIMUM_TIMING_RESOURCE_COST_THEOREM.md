# WP33 — Minimum Timing-Resource Cost Theorem

**Date:** 2026-08-20

## Purpose
Invert the WP32 marked-event information ceiling into a necessary **resource cost** for achieving a specified source-information task.

This is not a new detector class. It is the operational inverse of the current strongest autonomous proper-event theorem.

---

## 1. Starting point

For the autonomous marked event kernel

\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\qquad
\eta=\kappa(\mathsf M),
\]

define the capture-weighted timing-collision resource

\[
\mathfrak R_2
=2\int\kappa(dm)\int f_m(t)^2dt
\]

and, when markwise hazards satisfy `h_m(t)<=Lambda(m)`, the capture-weighted hazard capacity

\[
\mathfrak H
=\int\Lambda(m)\kappa(dm),
\qquad
\mathfrak R_2\le\mathfrak H.
\]

For a normalized absolutely continuous incident spectral-FI density `w(omega)`, define

\[
\mathcal W(A)
=\sup_{E:\,|E|\le A}\int_E w(\omega)d\omega.
\]

WP32/WP28 give

\[
\boxed{
\bar\eta_I[w]
\le
\eta\,\mathcal W\!\left(\frac{\pi\mathfrak R_2}{\eta}\right)
\le
\eta\,\mathcal W\!\left(\frac{\pi\mathfrak H}{\eta}\right).
}
\]

---

## 2. General inverse theorem

Let the target source-normalized information transfer be

\[
\bar\eta_I[w]\ge q>0.
\]

Necessarily

\[
q\le\eta.
\]

Define the generalized inverse

\[
\boxed{
\mathcal W^{-1}(r)
=\inf\{A\ge0:\mathcal W(A)\ge r\},
\qquad 0<r\le1.
}
\]

Since `W` is monotone nondecreasing, the WP32 upper bound implies

\[
\boxed{
\mathfrak R_2
\ge
\frac{\eta}{\pi}
\mathcal W^{-1}\!\left(\frac{q}{\eta}\right).
}
\]

Because `R2<=H`, every hazard-based microscopic realization must also satisfy

\[
\boxed{
\mathfrak H
\ge
\frac{\eta}{\pi}
\mathcal W^{-1}\!\left(\frac{q}{\eta}\right).
}
\]

Thus a desired source-information task demands a minimum capture-weighted local timing intensity.

**Status: PROVED by monotone inversion of WP32.**

---

## 3. Flat-band simplification

For a uniform source-information density on

\[
|\omega|\le\Omega,
\]

\[
\mathcal W(A)=\min\left(1,\frac{A}{2\Omega}\right).
\]

For any feasible target `q<=eta`, the inverse theorem collapses to

\[
\boxed{
\mathfrak R_2
\ge
\frac{2\Omega q}{\pi},
}
\]

and

\[
\boxed{
\mathfrak H
\ge
\frac{2\Omega q}{\pi}.
}
\]

Remarkably, the total capture probability `eta` cancels from the **absolute capture-weighted timing-resource requirement**; `eta` remains only in the feasibility condition `q<=eta`.

Writing the ordinary-frequency half-band as

\[
B=\frac{\Omega}{2\pi},
\]

gives the especially simple form

\[
\boxed{
\mathfrak R_2\ge4Bq,
\qquad
\mathfrak H\ge4Bq.
}
\]

This has a direct engineering interpretation: preserving an absolute fraction `q` of incident optical information across half-bandwidth `B` requires at least `4Bq` of capture-weighted timing-collision/local-registration capacity.

---

## 4. Uniform per-captured-event hazard

If every captured event obeys the same conditional hazard ceiling

\[
\Lambda(m)\le\Lambda,
\]

then

\[
\mathfrak H\le\eta\Lambda.
\]

Combining with the necessary flat-band cost gives

\[
\boxed{
\Lambda
\ge
\frac{4Bq}{\eta}.
}
\]

Equivalently,

\[
\boxed{
B\le\frac{\eta\Lambda}{4q},
}
\]

which is exactly the earlier WP25 bandwidth ceiling.

If the target is expressed as retention `r` relative to the captured DC information,

\[
q=r\eta,
\]

then

\[
\boxed{
\Lambda\ge4Br.
}
\]

The required **per-captured-event** local registration rate is then independent of capture efficiency.

---

## 5. Tightness

For a single constant-hazard exponential registration law,

\[
G(\omega)=\eta\frac{\Lambda^2}{\Lambda^2+\omega^2}
\]

and

\[
\bar\eta_I(\Omega)
=
\eta\frac{\Lambda}{\Omega}
\arctan\frac{\Omega}{\Lambda}.
\]

At large `Omega/Lambda`,

\[
\bar\eta_I
\sim
\eta\frac{\pi\Lambda}{2\Omega}.
\]

Thus

\[
\eta\Lambda
\sim
\frac{2\Omega q}{\pi}
=4Bq
\]

at fixed small high-band transfer `q`. The flat-band resource-cost coefficient is therefore asymptotically attainable.

---

## 6. Relation to the thermodynamic bridge

WP29 gives, for the restricted reversible gateway class,

\[
\Lambda_*
=
\frac{\mathcal A d}{f_*}
 g^{-1}\!\left(\frac{\Sigma}{f_*}\right).
\]

If the gateway bound applies uniformly to captured registrations, then a target flat-band transfer `q` requires

\[
\boxed{
\frac{\mathcal A d}{f_*}
 g^{-1}\!\left(\frac{\Sigma}{f_*}\right)
\ge
\frac{4Bq}{\eta}.
}
\]

This is the inverse-resource version of the thermokinetic bandwidth theorem.

It must not be interpreted as a universal thermodynamic law because the absolute reverse optical rate `d` remains an independent microscopic resource.

---

## 7. Significance for UPRP

The event branch can now be stated in both directions:

### Performance ceiling

\[
\text{finite timing resource}
\Longrightarrow
\text{finite source-information bandwidth}.
\]

### Resource cost

\[
\text{specified source-information bandwidth/retention}
\Longrightarrow
\text{minimum timing resource}.
\]

For the flat-band task, the latter is simply

\[
\boxed{
\mathfrak H\ge4Bq.
}
\]

This is likely the cleanest operational headline equation for the autonomous event-detector manuscript, provided the definitions and detector-class assumptions are stated immediately alongside it.

---

## Status

**PROVED** as an inversion of WP32/WP28. No new physical assumption beyond those work packages is introduced.
