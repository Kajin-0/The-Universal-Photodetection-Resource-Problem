# WP16 — Local absorption + transport information-bandwidth theorem

**Date:** 2026-08-20

## Purpose

`WP15_DELAY_CONCENTRATION_AND_LOCALIZED_CAPTURE_CAPACITY.md` identifies the exact quantity needed to compose optical capture with transit-dispersion information loss: the absolute fraction of incident photons that can be captured inside a narrow electrical-delay window.

This note supplies a first rigorous electromagnetic bound on that localized-capture capacity for a useful restricted detector class by combining:

1. the WP15 delay concentration theorem; and
2. the geometry-independent per-volume absorption limit of Miller et al. for passive lossy media.

This is the first explicit UPRP theorem in which an optical material figure of merit and a carrier-transport velocity jointly bound source-normalized information bandwidth.

---

# 1. Restricted detector class

Assume:

1. normally incident plane-wave illumination;
2. one passive, local, isotropic, nonmagnetic active material with scalar susceptibility `chi(omega)`;
3. no external passive antenna/concentrator/resonator material that funnels optical power into the active delay slice;
4. detector projected area `A` matches the incident beam area used to define capture fraction;
5. electrical event delay is a monotone planar transport coordinate with constant speed `v`, so a delay interval `Delta t` corresponds to active-material thickness

\[
\ell=v\Delta t;
\]

6. ideal complete event-timestamp record after capture;
7. narrow optical sideband/task regime in which the relevant material factor may be represented by a finite supremum over the optical carrier band.

These restrictions are essential. The theorem is not claimed for arbitrary passive concentrators or arbitrary optical/electrical geometry.

---

# 2. Per-volume absorption bound

Miller et al., *Fundamental limits to optical response in absorptive systems*, Optics Express 24, 3329–3364 (2016), DOI `10.1364/OE.24.003329`, prove for a passive electric material under plane-wave illumination

\[
\boxed{
\frac{\sigma_{\rm abs}}{V}
\le
k\frac{|\chi(\omega)|^2}{\operatorname{Im}\chi(\omega)},
}
\]

where

\[
k=\omega/c.
\]

Define the material absorption factor

\[
\boxed{
\mathcal M(\omega)
=k(\omega)\frac{|\chi(\omega)|^2}{\operatorname{Im}\chi(\omega)}
}
\]

with units of inverse length.

For a narrow optical task band `B`, define

\[
\mathcal M_B=\sup_{\omega\in B}\mathcal M(\omega).
\]

---

# 3. Localized capture in a delay slice

A delay window `Delta t` corresponds, under the planar constant-speed mapping, to an active material slab of volume

\[
V_\Delta=A v\Delta t.
\]

The maximum absorption cross section attributable to such a body obeys

\[
\sigma_{\rm abs,\Delta}
\le
A v\Delta t\,\mathcal M_B.
\]

Dividing by incident beam area `A`, the absolute fraction of incident photons capturable in that delay slice obeys

\[
\boxed{
M_D(\Delta t)
\le
\min\left[
1,
\mathcal M_B v\Delta t
\right].
}
\]

This is the required localized-capture capacity bound for the restricted class.

**Status:** PROVED from the Miller per-volume absorption theorem plus the stated geometry assumptions.

---

# 4. Compose with the WP15 concentration theorem

WP15 gives for any `x>0`

\[
\bar\eta_{\mathcal I}
\le
c_x+(1-c_x)
M_D\left(\frac{2x}{\Omega_s}\right),
\]

where

\[
c_x=\sup_{|u|\ge x}|\operatorname{sinc}u|.
\]

Therefore

\[
\boxed{
\bar\eta_{\mathcal I}
\le
c_x
+(1-c_x)
\min\left[
1,
\frac{2x\mathcal M_Bv}{\Omega_s}
\right].
}
\]

This is an explicit optical-material + transport upper bound on flat-band average information transfer.

---

# 5. Bandwidth condition for target information fraction

Suppose

\[
\bar\eta_{\mathcal I}\ge q,
\qquad q>c_x.
\]

In the resource-limited branch

\[
\frac{2x\mathcal M_Bv}{\Omega_s}<1,
\]

one must have

\[
q-c_x
\le
(1-c_x)
\frac{2x\mathcal M_Bv}{\Omega_s}.
\]

Hence

\[
\boxed{
\Omega_s
\le
2x\mathcal M_Bv
\frac{1-c_x}{q-c_x}.
}
\]

Substituting the material factor,

\[
\boxed{
\Omega_s
\le
2x\,k_Bv
\frac{|\chi|^2}{\operatorname{Im}\chi}
\frac{1-c_x}{q-c_x}
}
\]

when a single representative/worst-case material value is appropriate over the optical task band.

---

# 6. Simple explicit x=pi/2 version

Take

\[
x=\pi/2,
\qquad
c_x=2/\pi.
\]

Then

\[
\boxed{
\bar\eta_{\mathcal I}
\le
\frac2\pi
+\left(1-\frac2\pi\right)
\min\left[
1,
\frac{\pi\mathcal M_Bv}{\Omega_s}
\right].
}
\]

For target `q>2/pi` in the resource-limited branch,

\[
\boxed{
\Omega_s
\le
(\pi-2)\mathcal M_Bv
\frac1{q-2/\pi}.
}
\]

Equivalently,

\[
\boxed{
\Omega_s
\le
(\pi-2)
\frac{k_Bv}{q-2/\pi}
\frac{|\chi|^2}{\operatorname{Im}\chi}.
}
\]

This is the cleanest closed form.

---

# 7. Interpretation

The theorem is not a conventional transit-time formula.

It says that high information bandwidth requires a large fraction of incident photons to be captured inside a narrow delay slice. But passivity and material loss place a maximum absorption cross section per unit active-material volume. Therefore a finite material absorption strength prevents arbitrary concentration of successful capture into an arbitrarily thin transport layer.

The resources are explicitly:

\[
\boxed{
\text{optical material factor }|\chi|^2/\operatorname{Im}\chi
+
\text{optical wavenumber }k
+
\text{carrier velocity }v.
}
\]

The projected detector area cancels in this planar single-material class.

---

# 8. Why this does not contradict thin-sheet perfect absorbers

The theorem explicitly excludes external passive concentrators/matching structures.

A Salisbury screen, cavity-coupled quantum well, antenna-coupled absorber, or metasurface can use fields generated by additional passive structure to funnel energy into a very small active volume. In that case the incident field acting on the active material is not simply the free-space plane wave used in the single-body Miller cross-section normalization, and the full optical design domain/resources must be included.

Thus

\[
\boxed{
\text{arbitrary field concentration can evade the restricted theorem only by consuming additional EM geometry/resources}.
}
\]

This is expected, not a contradiction.

---

# 9. Novelty posture

The Miller per-volume absorption limit is established prior art and must be cited as such.

The Levy/Esseen-style concentration-function mathematics underlying WP15 is also established probability theory.

The candidate project contribution is their detector-specific composition:

\[
\boxed{
\text{finite local optical absorption capacity}
+\text{delay concentration requirement}
\Rightarrow
\text{finite source-information bandwidth}.
}
\]

No novelty claim should be made until a targeted literature search confirms that this exact photodetection-information composition has not already appeared.

---

# 10. Immediate next tests

1. Replace constant drift speed with bounded stochastic drift/scattering and determine how the localized-capacity theorem changes.
2. Extend the local absorption bound to multiple active materials and tensor susceptibilities.
3. Determine whether a rigorous version survives an external lossless concentrator when total design-domain T-operator resources are included.
4. Derive a homogeneous Beer-Lambert/sum-rule special case and compare its scaling with the present local-material theorem.
5. Evaluate the bound parametrically for LWIR HgCdTe without presenting the result as a realistic device bandwidth; use actual optical `chi` and a physically bounded transport velocity.

---

# Status

**PROVED under explicit restricted assumptions.**

This is the first explicit joint optical-material/transport information-bandwidth theorem in the repository.