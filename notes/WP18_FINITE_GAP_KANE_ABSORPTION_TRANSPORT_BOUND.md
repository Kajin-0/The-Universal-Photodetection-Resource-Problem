# WP18 — Finite-gap Kane absorption–transport information bound

**Date:** 2026-08-20

## Purpose

WP17 derived the exact massless 6-band Kane optical conductivity and its composition with exponential absorption-depth delay. A practical HgCdTe detector is generally operated with a positive band gap to suppress thermal generation, so the next question is how a finite Kane mass changes the optical-capture/transport information scale.

This note derives the zero-temperature finite-gap interband conductivity analytically for the simplified 6x6 Kane Hamiltonian and combines it with the maximum photoelectron group velocity. The central result is that the exact `sigma v_K` cancellation survives, but the finite gap suppresses both optical spectral weight and useful carrier group velocity.

---

# 1. Massive simplified Kane spectrum

Write the low-energy Hamiltonian as

\[
H=v_K\mathbf A\cdot\mathbf p+M\Lambda,
\]

where

\[
M=m_Kv_K^2=E_g/2.
\]

The three doubly-degenerate bands are

\[
\boxed{
E_0=-M,
\qquad
E_\pm=\pm E_p,
\qquad
E_p=\sqrt{M^2+v_K^2p^2}.
}
\]

For a positive-gap intrinsic semiconductor at `T=0`, the flat/heavy-hole and lower/light-hole bands are occupied and the upper/conduction band is empty.

Define the dimensionless photon-energy ratio

\[
\boxed{
y=\frac{E_g}{\hbar\omega}=\frac{2M}{\hbar\omega}.}
\]

Interband absorption requires `0<=y<1`.

---

# 2. Finite-mass velocity-matrix weights

Let `A_x=v_x/v_K` and let `P_+`, `P_0`, `P_-` project onto the three bands.

Direct projector algebra gives, for momentum direction `n=p/p`,

\[
\operatorname{Tr}(P_+A_xP_0A_x)
=\frac34\left(1+\frac{M}{E_p}\right)(1-n_x^2),
\]

and

\[
\operatorname{Tr}(P_+A_xP_-A_x)
=\frac12(1-n_x^2)
+2\left(\frac{M}{E_p}\right)^2n_x^2.
\]

Angular averaging yields

\[
\boxed{
\overline M_{0+}
=\frac12\left(1+\frac{M}{E_p}\right),
}
\]

\[
\boxed{
\overline M_{-+}
=\frac13\left[1+2\left(\frac{M}{E_p}\right)^2\right].
}
\]

At `M=0` these reduce to the WP17 values `1/2` and `1/3`.

**Status:** PROVED by direct 6x6 projector algebra.

---

# 3. Flat-to-conduction conductivity

For the transition

\[
E_0=-M\to E_+=E_p,
\]

the photon energy condition is

\[
\hbar\omega=E_p+M.
\]

Thus

\[
E_p=\hbar\omega-M,
\]

and

\[
v_Kp
=\sqrt{\hbar\omega(\hbar\omega-2M)}
=\hbar\omega\sqrt{1-y}.
\]

Carrying the finite-mass Kubo shell factor and the angular matrix element through exactly gives

\[
\boxed{
\operatorname{Re}\sigma_{0\to+}(\omega)
=
\frac{e^2\omega}{4\pi\hbar v_K}
\sqrt{1-y}\;\Theta(1-y).
}
\]

The massless result is recovered at `y=0`.

---

# 4. Lower-cone-to-conduction conductivity

For

\[
E_-=-E_p\to E_+=E_p,
\]

the transition energy is

\[
\hbar\omega=2E_p.
\]

Hence

\[
\frac{M}{E_p}=y,
\qquad
v_Kp=\frac{\hbar\omega}{2}\sqrt{1-y^2}.
\]

The exact conductivity is

\[
\boxed{
\operatorname{Re}\sigma_{-\to+}(\omega)
=
\frac{e^2\omega}{48\pi\hbar v_K}
(1+2y^2)\sqrt{1-y^2}\;\Theta(1-y).
}
\]

Again, this reduces to the WP17 cone-to-cone contribution at `y=0`.

---

# 5. Total finite-gap Kane interband conductivity

Adding the two channels,

\[
\boxed{
\operatorname{Re}\sigma_K(\omega;E_g)
=
\frac{e^2\omega}{48\pi\hbar v_K}
F_K(y)\;\Theta(1-y),
}
\]

where

\[
\boxed{
F_K(y)
=12\sqrt{1-y}
+(1+2y^2)\sqrt{1-y^2}.
}
\]

At zero gap,

\[
F_K(0)=13,
\]

recovering WP17.

At the absorption edge,

\[
F_K(y)\to0
\qquad(y\to1^-).
\]

---

# 6. Exact conductivity–Kane-velocity cancellation survives the gap

Multiplying by `v_K` gives

\[
\boxed{
 v_K\operatorname{Re}\sigma_K
=
\frac{e^2\omega}{48\pi\hbar}F_K(y).
}
\]

Thus the explicit Kane velocity still cancels exactly from the conductivity-times-band-velocity product.

The finite gap enters only through the dimensionless spectral factor `F_K(E_g/hbar omega)`.

This is a stronger statement than the massless special case.

---

# 7. Photoelectron group-velocity penalty

Optical conductivity alone is not enough for the delay problem. The photoelectron created in the conduction band has group velocity below `v_K` when `M>0`.

## 7.1 Dominant flat-to-conduction channel

On the `0 -> +` shell,

\[
E_p=\hbar\omega-M.
\]

Therefore

\[
\frac{v_{g,0+}}{v_K}
=\frac{v_Kp}{E_p}
=\sqrt{1-\left(\frac{M}{E_p}\right)^2}.
\]

In terms of `y`,

\[
\boxed{
 u_0(y)
\equiv\frac{v_{g,0+}}{v_K}
=\frac{2\sqrt{1-y}}{2-y}.
}
\]

## 7.2 Cone-to-cone channel

For the `- -> +` shell,

\[
E_p=\hbar\omega/2,
\]

so

\[
\boxed{
 u_c(y)
\equiv\frac{v_{g,-+}}{v_K}
=\sqrt{1-y^2}.
}
\]

For `0<=y<1`,

\[
\boxed{u_0(y)\ge u_c(y).}
\]

Thus the fastest interband photoelectron channel is the dominant flat-to-conduction process.

---

# 8. Weak-loss absorption-depth/transport figure

In the weak-loss optical regime,

\[
a_{\rm abs}
\simeq
\frac{\operatorname{Re}\sigma_K}
{n\epsilon_0c}.
\]

Using

\[
\alpha_{\rm fs}=\frac{e^2}{4\pi\epsilon_0\hbar c},
\]

one gets

\[
\boxed{
\frac{a_{\rm abs}v_K}{\omega}
\simeq
\frac{\alpha_{\rm fs}}{12n}F_K(y).
}
\]

If carrier collection is restricted by the actual maximum interband photoelectron group velocity, an optimistic delay-rate scale is

\[
\Gamma_{K,g}
\le
 a_{\rm abs}v_Ku_0(y).
\]

Hence

\[
\boxed{
\frac{\Gamma_{K,g}}{\omega}
\lesssim
\frac{\alpha_{\rm fs}}{12n}G_K(y),
}
\]

where

\[
\boxed{
G_K(y)=F_K(y)u_0(y)
}
\]

or explicitly

\[
\boxed{
G_K(y)
=
\frac{2(1-y)}{2-y}
\left[
12+(1+2y^2)\sqrt{1+y}
\right].
}
\]

At zero gap,

\[
G_K(0)=13.
\]

Near the band edge,

\[
G_K(y)
\sim
2(12+3\sqrt2)(1-y)
\approx32.49(1-y).
\]

Thus the useful absorption-depth/transport rate collapses linearly as the optical photon energy approaches the positive band gap.

---

# 9. Monotonic speed penalty from opening the gap

Within this ideal interband/ballistic model, `G_K(y)` decreases from 13 at `y=0` to 0 at `y=1`.

Therefore, at fixed optical photon energy and background index,

\[
\boxed{
\text{opening a positive Kane gap cannot improve the best-case absorption-depth/ballistic information rate.}
}
\]

This is not a statement about complete detector performance. A positive gap can drastically improve dark-count/noise performance, which is omitted here.

The physically interesting tradeoff therefore appears only after the thermal/dark-generation resource layer is included.

---

# 10. Information-bandwidth ceiling for the finite-gap layer

Under the same exponential-depth ideal event-record model as WP17, and using the fastest admissible photoelectron velocity as an optimistic upper envelope,

\[
\eta_{\mathcal I}(\Omega)
\lesssim
\eta_c
\frac{\Gamma_{K,g}^2}
{\Gamma_{K,g}^2+\Omega^2}.
\]

For an optimistic `eta_c=1`, edge information fraction `q` therefore requires

\[
\boxed{
\frac{\Omega_s}{\omega_0}
\lesssim
\frac{\alpha_{\rm fs}}{12n}
G_K\left(\frac{E_g}{\hbar\omega_0}\right)
\sqrt{\frac{1-q}{q}}.
}
\]

This is the finite-gap extension of the WP17 fine-structure-scale theorem in the weak-loss limit.

At `E_g=0`, it reduces exactly to

\[
\frac{13\alpha_{\rm fs}}{12n}
\sqrt{\frac{1-q}{q}}.
\]

---

# 11. Finite temperature occupation factors

At nonzero temperature and/or finite chemical potential, each interband term acquires its Pauli occupation difference

\[
\Delta f=f(E_i)-f(E_f).
\]

For ordinary Fermi occupation,

\[
0\le\Delta f\le1
\]

for an allowed absorption transition with the lower state more occupied than the upper state.

Therefore the zero-temperature formulas above provide an **upper envelope** on the corresponding interband optical spectral weight at fixed band structure.

Thermal intraband/Drude absorption is a separate channel and should not automatically be counted as useful interband photodetection capture.

---

# 12. Physical interpretation for LWIR HgCdTe

At fixed `hbar omega_0`, increasing the positive gap has two competing detector-level consequences:

1. **capture/transport layer:** worsens monotonically because `F_K(y)` and the photoelectron group velocity fall;
2. **thermal-noise layer:** generally improves because thermal carrier generation and dark counts are suppressed.

Therefore any finite-temperature optimum in full detector information performance must come from the competition between these two layers.

That optimum is not contained in a pure bandwidth or pure optical calculation.

---

# 13. Next target

The next mathematically useful model is to compose the finite-gap Kane rate with an explicit thermal dark-generation law.

At minimum, define

\[
\eta_I(\Omega)
=\frac{\eta_c}{1+d(E_g,T)/(\eta_c\Phi_0)}
\times
\frac{\Gamma_{K,g}^2(E_g)}
{\Gamma_{K,g}^2(E_g)+\Omega^2}
\]

for the event-record class and test several theoretically controlled dark-generation models.

The first goal is not a realistic HgCdTe device simulator. It is to determine whether a finite optimal `E_g/(k_BT)` follows generically, which resources set it, and whether the optimum survives adversarial changes in the dark-generation mechanism.

---

# Status

**PROVED:** finite-gap zero-temperature simplified-Kane interband conductivity and group-velocity factors.

**RESTRICTED THEOREM:** weak-loss finite-gap absorption-depth/ballistic information ceiling.

**OPEN:** thermally complete finite-gap optimum and full HgCdTe applicability.