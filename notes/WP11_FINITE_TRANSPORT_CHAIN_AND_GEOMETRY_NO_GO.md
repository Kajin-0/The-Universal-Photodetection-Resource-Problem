# WP11 — Finite transport chain, weighting geometry, and the electrical spatial resource

**Date:** 2026-08-20

## Purpose

The minimal three-node model identifies the internal transduction rate with an electrical current matrix element. `WP11_SHOCKLEY_RAMO_KANE_RESOURCE_BOUND.md` maps that current to carrier velocity and weighting-field geometry.

This note makes the spatial structure explicit with a finite transport chain and proves that **carrier velocity or material bandwidth alone is not a complete electrical speed resource**. The joint optical/electrical geometry matters.

---

# 1. Tight-binding transport chain

Consider one carrier on a one-dimensional chain with spacing `a` and nearest-neighbor hopping energy `J>0`:

\[
H_{m tr}
=-J\sum_{j=0}^{M-2}
\left(|j+1\rangle\langle j|+|j\rangle\langle j+1|\right).
\]

Let

\[
X=a\sum_{j=0}^{M-1}j|j\rangle\langle j|.
\]

The velocity operator is

\[
\boxed{
v=\frac{i}{\hbar}[H_{m tr},X]
=\frac{iJa}{\hbar}
\sum_j
\left(|j+1\rangle\langle j|-|j\rangle\langle j+1|\right).
}
\]

For the infinite periodic chain,

\[
E(k)=-2J\cos(ka),
\]

so

\[
\boxed{
v_{\max}=\frac{2Ja}{\hbar}.}
\]

The one-band width is

\[
W=4J,
\]

hence

\[
\boxed{
v_{\max}=\frac{Wa}{2\hbar}.}
\]

For a finite open chain the velocity-operator norm is no larger than this periodic value.

**Status:** PROVED elementary tight-binding result.

---

# 2. Planar Shockley-Ramo induced-charge speed

For planar weighting potential across length `L`,

\[
\phi_w(x)=x/L,
\qquad
Q_w=eX/L.
\]

Therefore

\[
\frac{d}{dt}\langle Q_w\rangle
=\frac{e}{L}\langle v\rangle.
\]

Using `|<v>|<=v_max`,

\[
\boxed{
\left|\frac{d}{dt}\langle Q_w\rangle\right|
\le
\frac{e v_{\max}}{L}
=\frac{eWa}{2\hbar L}.
}
\]

If the initial induced charge is zero, producing a fraction `r` of a one-electron full induced-charge swing requires

\[
\boxed{
t\ge r\frac{L}{v_{\max}}
=\frac{2r\hbar L}{Wa}.}
\]

Thus in the nearest-neighbor lattice model the electrical transit resource is not simply an energy bandwidth `W`; it is the combination

\[
\boxed{Wa/L.}
\]

This is a concrete realization of the more general velocity + weighting-length resource.

---

# 3. Why finite material velocity is still not enough

Replace the planar weighting potential by an arbitrary monotone `phi_w(x)`. Then

\[
\frac{d}{dt}\langle Q_w\rangle
=e\left\langle v\frac{d\phi_w}{dx}\right\rangle
\]

in the semiclassical/local limit.

If the entire weighting-potential change is compressed into a layer of width `epsilon`, a carrier with fixed finite velocity can generate most of the electrode signal in time

\[
\Delta t\sim\epsilon/v_{\max}.
\]

Therefore

\[
\boxed{
v_{\max}<\infty
\quad\not\Rightarrow\quad
\text{finite induced-current pulse bandwidth}
}
\]

unless the weighting potential itself is spatially regularized.

This is the electrical analogue of other UPRP hidden-resource mechanisms: a fixed integral resource can hide increasingly sharp structure.

---

# 4. Weighting-potential Lipschitz resource

Define

\[
\ell_w^{-1}
=\sup_x|d\phi_w/dx|.
\]

Then

\[
\left|\frac{d}{dt}\langle Q_w\rangle\right|
\le e v_{\max}/\ell_w.
\]

For target induced-charge fraction `r`,

\[
\boxed{
t\ge r\ell_w/v_{\max}.}
\]

For the nearest-neighbor transport model,

\[
\boxed{
t\ge
\frac{2r\hbar\ell_w}{Wa}.}
\]

A finite weighting length is therefore a genuine electrical geometry resource.

---

# 5. Small-pixel effect as the known physical realization

Pixelated semiconductor detectors provide the standard physical example: their weighting potential is nearly flat through much of the detector and rises rapidly near the collecting pixel. The corresponding weighting field is strongly localized near the electrode, concentrating induced signal formation into the final part of the carrier trajectory.

This is the well-known **small-pixel effect** and must not be presented as a new detector-physics claim. It is useful here because it supplies a real architecture that exercises the UPRP weighting-geometry resource.

References include:

- Z. He, Nucl. Instrum. Meth. A 463, 250–267 (2001), Shockley-Ramo review;
- modern CdZnTe pixel-detector studies explicitly describe the localized weighting field and near-anode signal formation.

---

# 6. Joint optical/electrical geometry obstruction

A conventional transit-time argument often uses the full absorber/depletion thickness `L`. This is not universally the relevant distance.

If optical absorption is engineered close to the region where `phi_w` changes rapidly, the carrier can generate a large fraction of its electrical signal without traversing the full detector thickness.

Thus

\[
\boxed{
\{v_{\max},L\}
\text{ alone do not determine electrical information delay}
}
\]

when the optical absorption profile and weighting potential are design variables.

A resource-complete spatial description needs the relative geometry of:

1. optical absorption/capture support;
2. carrier transport paths;
3. electrical weighting-potential level sets.

Define, for an absorption point `r0` and target weighting change `r`,

\[
d_w(r_0;r)
=\inf\{\text{path length from }r_0\text{ required to achieve }|\Delta\phi_w|\ge r\}.
\]

If carrier speed is bounded by `v_max`, then

\[
\boxed{t(r_0;r)\ge d_w(r_0;r)/v_{\max}.}
\]

For an optical absorption region `A`, the fastest possible event can use

\[
\boxed{d_{\rm cap\to read}(r)=\inf_{r_0\in A}d_w(r_0;r).}
\]

Hence

\[
\boxed{t\ge d_{\rm cap\to read}(r)/v_{\max}.}
\]

This is a useful geometric definition for future finite-band composition.

**Status:** definition + kinematic bound PROVED; how best to average it for a full optical QFI task remains OPEN.

---

# 7. Relation to conventional high-speed photodiodes

Conventional UTC/MUTC and p-i-n photodiode models already show that response speed depends on absorber/collector dimensions, carrier drift/diffusion velocities, and RC response. Transit-time estimates use forms such as

\[
\tau_{\rm tr}\sim W/v,
\]

with architecture-dependent numerical factors.

UPRP should not claim this scaling as new.

The new project role is to identify which geometric quantity must appear in a **resource-complete information theorem** once arbitrary optical/electrode co-design is allowed.

---

# 8. Consequence for HgCdTe/Kane mapping

If a narrow-gap HgCdTe transport sector has a ballistic Kane velocity scale near

\[
v_K\sim10^6\ {\rm m/s},
\]

then a planar device gives the microscopic rate scale

\[
\kappa\lesssim v_K/L.
\]

But a nonplanar weighting field replaces `L` by `ell_w` or, more precisely, the capture-to-readout weighting distance `d_cap->read`.

Therefore even with a material velocity that is nearly composition-insensitive, detector speed can remain strongly geometry dependent.

---

# 9. New resource-completeness statement

The electrical transduction layer requires at least

\[
\boxed{
\text{band/current scale}
+
\text{accessible transport support}
+
\text{electrode weighting geometry}
+
\text{optical-to-electrical spatial overlap}.
}
\]

A universal material-only electrical bandwidth bound is therefore not expected without restricting detector geometry.

---

# 10. Next step

The next high-value calculation is to turn `d_cap->read(r)` into an average/pointwise optical-information bound by weighting it with the optical capture distribution from WP5. That would create the first explicit **joint optical-field geometry + semiconductor transport + electrical weighting geometry** information-speed theorem.
