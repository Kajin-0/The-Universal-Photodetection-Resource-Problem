# WP11 — Finite transport chain, weighting geometry, and electrical spatial resources

**Date:** 2026-08-20  
**Corrected:** 2026-08-20 after the spatial-delay information theorem

## Critical interpretation

This note bounds **carrier/induced-charge signal-formation latency and current slew**, not Fisher-information bandwidth by itself. A deterministic known transit delay can preserve stationary spectral information exactly. Information rolloff requires unresolved delay dispersion, stochastic timing, downstream noise, finite sampling/coarse graining, or a true spectral null.

The information-theoretic correction is derived in `WP11_SPATIAL_DELAY_INFORMATION_THEOREM.md` and `WP12_READOUT_FILTER_INFORMATION_INVARIANCE.md`.

---

# 1. Tight-binding transport chain

Consider one carrier on a one-dimensional nearest-neighbor chain,

\[
H_{\rm tr}=-J\sum_{j=0}^{M-2}(|j+1\rangle\langle j|+|j\rangle\langle j+1|),
\]

with

\[
X=a\sum_jj|j\rangle\langle j|.
\]

Then

\[
\boxed{v=(i/\hbar)[H_{\rm tr},X]}
\]

and for the infinite periodic chain

\[
E(k)=-2J\cos ka,
\qquad
\boxed{v_{\max}=2Ja/\hbar}.
\]

The one-band width is `W=4J`, hence

\[
\boxed{v_{\max}=Wa/(2\hbar).}
\]

A finite open chain has no larger velocity norm.

---

# 2. Planar Shockley–Ramo charge-slew bound

For planar weighting potential

\[
\phi_w(x)=x/L,
\qquad
Q_w=eX/L,
\]

we have

\[
\frac{d}{dt}\langle Q_w\rangle=\frac{e}{L}\langle v\rangle.
\]

Therefore

\[
\boxed{
\left|d\langle Q_w\rangle/dt\right|
\le ev_{\max}/L
=eWa/(2\hbar L).
}
\]

To accumulate induced-charge fraction `r` from zero requires at least

\[
\boxed{t_{\rm lat}\ge rL/v_{\max}=2r\hbar L/(Wa).}
\]

This is a kinematic/charge-formation latency bound. It is **not automatically an information-bandwidth bound**.

---

# 3. Weighting-geometry no-go

For arbitrary monotone weighting potential,

\[
i=qv\,d\phi_w/dx
\]

in the semiclassical local limit. If the weighting-potential swing is compressed into a layer of width `epsilon`, then at fixed finite carrier speed

\[
|i|\sim |q|v/\epsilon,
\qquad
\Delta t\sim\epsilon/v.
\]

Thus

\[
\boxed{v_{\max}<\infty\not\Rightarrow\text{bounded current-pulse bandwidth}}
\]

unless weighting geometry is spatially regularized. The pulse area remains finite because `int i dt=q Delta phi_w`.

This is the known physical mechanism behind strongly localized weighting fields such as the small-pixel effect; that detector physics is prior art.

---

# 4. Weighting-length repair

Define

\[
\ell_w^{-1}=\sup_x|d\phi_w/dx|.
\]

Then

\[
\boxed{|d\langle Q_w\rangle/dt|\le ev_{\max}/\ell_w}
\]

and a target weighting-potential/induced-charge change `r` requires

\[
\boxed{t_{\rm lat}\ge r\ell_w/v_{\max}.}
\]

For the nearest-neighbor chain,

\[
\boxed{t_{\rm lat}\ge2r\hbar\ell_w/(Wa).}
\]

Again this is a latency/slew theorem. Whether it becomes an information limit depends on the accessible output record and stochastic/noise model.

---

# 5. Joint optical/electrical geometry

Detector thickness alone is not the relevant geometry when optical absorption and electrode weighting fields can be co-designed.

For capture point `r0`, define the path length needed to accumulate weighting-potential change `r`:

\[
d_w(r_0;r)=\inf\{\text{path length from }r_0\text{ needed for }|\Delta\phi_w|\ge r\}.
\]

With speed bound `v_max`,

\[
\boxed{t_{\rm lat}(r_0;r)\ge d_w(r_0;r)/v_{\max}.}
\]

For absorption support `A`, the fastest kinematic latency is bounded by

\[
\boxed{d_{\rm cap\to read}(r)=\inf_{r_0\in A}d_w(r_0;r).}
\]

But a scalar minimum does not determine information bandwidth. For event timestamps the correct object is the **distribution** of delays induced by the optical capture distribution:

\[
H_{\rm geom}(\omega)=\int p_{\rm abs}(r)e^{-i\omega D(r)}dr,
\]

\[
\eta_I^{\rm timestamp}=\eta_{\rm cap}|H_{\rm geom}|^2.
\]

See `WP11_SPATIAL_DELAY_INFORMATION_THEOREM.md`.

---

# 6. Uniform-depth information result

For unresolved uniform absorption depth in a planar layer and constant carrier speed,

\[
D\sim {\rm Uniform}(0,L/v).
\]

Then

\[
\boxed{
\eta_I(\omega)=\eta_{\rm cap}\operatorname{sinc}^2(\omega L/2v)
}
\]

and the half-information frequency is

\[
\boxed{f_{1/2}=0.4429464707\ldots\,v/L.}
\]

This recovers the familiar transit-time coefficient in an information setting, but the mechanism is **unresolved delay dispersion**, not deterministic propagation time itself.

---

# 7. Side-information recovery

If the capture location or another variable sufficient to determine the deterministic delay is retained in the output record, the delay can be corrected event by event. In the ideal model the geometric FI loss disappears.

Therefore joint optical/electrical geometry is partly an **observability/coarse-graining resource**, not only a transport resource.

---

# 8. HgCdTe/Kane interpretation

A narrow-gap HgCdTe transport sector can have a ballistic Kane velocity scale near `10^6 m/s`, giving a planar microscopic rate scale `~v_K/L`. This is not a device bandwidth. Scattering, trapping, absorption-depth dispersion, weighting geometry, contacts, circuit noise, and output coarse graining determine whether that kinematic scale is converted into recoverable information.

---

# 9. Resource-completeness statement

The semiconductor transport/readout geometry layer is better written as

\[
\boxed{
\text{band/current scale}
+\text{transport support}
+\text{optical capture distribution}
+\text{weighting geometry}
+\text{timing randomness/output observability}
\Rightarrow\text{transport information kernel}.
}
\]

A universal material-only information-bandwidth bound is not expected without restricting geometry and output record.

---

# 10. Status

- Tight-binding velocity/current-slew bounds: **PROVED**.
- Weighting-length latency bound: **PROVED**.
- Earlier interpretation of this latency as an automatic information-bandwidth bound: **CORRECTED/REJECTED**.
- Exact event-timestamp information theorem: moved to `WP11_SPATIAL_DELAY_INFORMATION_THEOREM.md`.
