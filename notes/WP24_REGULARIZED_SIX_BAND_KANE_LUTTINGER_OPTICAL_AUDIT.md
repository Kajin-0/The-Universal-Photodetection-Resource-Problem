# WP24 — Regularized six-band Kane–Luttinger optical-conductivity audit

**Date:** 2026-08-20

## Purpose

WP22–23 regularized the heavy-hole DOS and chemical potential but still used the simplified massive-Kane optical matrix/phase-space factors. This note tests whether the neglected quadratic remote-band and valence-warping terms materially change the target interband optical response.

The calculation uses the published bulk HgCdTe Kane/Luttinger parameters from Beugeling et al. (`kdotpy`, SciPost Phys. Codebases 47, 2025) and evaluates the Kubo conductivity directly from a six-band `Gamma_6 + Gamma_8` Hamiltonian.

The split-off `Gamma_7` sector is still omitted, so this is not yet the final 8-band calculation. At 10.6 um, however, the split-off energy is near 1 eV and is expected primarily to renormalize the low-energy parameters already entering the six-band block. WP24 tests that statement at the level accessible without the explicit `Gamma_7` sector.

---

# 1. Quadratic six-band Hamiltonian

Use basis

`{|Gamma6,+1/2>, |Gamma6,-1/2>, |Gamma8,+3/2>, |Gamma8,+1/2>, |Gamma8,-1/2>, |Gamma8,-3/2>}`.

The conduction block is

\[
H_{cc}=\left[E_g+\frac{\hbar^2}{2m_0}(2F+1)k^2\right]I_2.
\]

The Kane coupling block is

\[
H_{cv}=P
\begin{pmatrix}
-k_+/\sqrt2 & \sqrt{2/3}k_z & k_-/\sqrt6 & 0\\
0 & -k_+/\sqrt6 & \sqrt{2/3}k_z & k_-/\sqrt2
\end{pmatrix}.
\]

For the `Gamma_8` block define

\[
P_v=-\frac{\hbar^2}{2m_0}\gamma_1k^2,
\]

\[
Q_v=-\frac{\hbar^2}{2m_0}\gamma_2(k_x^2+k_y^2-2k_z^2),
\]

\[
R_v=-\frac{\hbar^2}{2m_0}\sqrt3[-\gamma_2(k_x^2-k_y^2)+2i\gamma_3k_xk_y],
\]

\[
S_v=-\frac{\hbar^2}{2m_0}2\sqrt3\gamma_3(k_x-ik_y)k_z.
\]

Then

\[
H_{vv}=\begin{pmatrix}
P_v+Q_v&-S_v&R_v&0\\
-S_v^*&P_v-Q_v&0&R_v\\
R_v^*&0&P_v-Q_v&S_v\\
0&R_v^*&S_v^*&P_v+Q_v
\end{pmatrix}.
\]

This is the standard cubic Luttinger `Gamma_8` block used inside the Kane model.

Material parameters used here:

- `P = 846 meV nm`;
- `2F+1` interpolated from 1 for HgTe to 0.82 for CdTe, so approximately `1-0.18x`;
- `gamma_1,2,3(x)` from WP23 / kdotpy;
- `E_g(x,T)` from the same parameterization.

---

# 2. Velocity operator and Kubo conductivity

For each Cartesian direction,

\[
\boxed{v_i(\mathbf k)=\frac1\hbar\frac{\partial H}{\partial k_i}.}
\]

For an isotropic/cubic bulk sample, use the polarization average

\[
M_{nm}(\mathbf k)=\frac13\sum_{i=x,y,z}
|\langle n\mathbf k|v_i|m\mathbf k\rangle|^2.
\]

The real interband conductivity is

\[
\boxed{
\operatorname{Re}\sigma(\omega)
=\frac{\pi e^2}{\omega}
\sum_{n<m}\int\frac{d^3k}{(2\pi)^3}
(f_n-f_m)M_{nm}(\mathbf k)
\delta(E_m-E_n-\hbar\omega).
}
\]

For a fixed direction `khat`, the radial delta integral is evaluated exactly at the resonance roots:

\[
\int k^2dk\,M\delta(\Delta E-\hbar\omega)
=\sum_r\frac{k_r^2M(k_r)}{|d\Delta E/dk|_{k_r}}.
\]

Angular integration is then performed numerically over the sphere.

---

# 3. Unit test: exact recovery of the simplified Kane coefficient

Set

\[
\gamma_1=\gamma_2=\gamma_3=0,
\qquad 2F+1=0.
\]

The Hamiltonian reduces to the simplified six-band Kane model.

For a gapless target, the numerical radial Kubo weights satisfy

\[
\boxed{W_{hh\to c}/W_{lh\to c}=12}
\]

to numerical precision.

Using the absolute Kubo prefactor reproduces

\[
\boxed{
\operatorname{Re}\sigma
=\frac{13e^2\omega}{48\pi\hbar v_K}
}
\]

with numerical/analytic ratio `0.999999996` in the test calculation.

This validates the Hamiltonian, velocity matrix elements, degeneracy counting, radial Jacobian, and Kubo normalization used below.

---

# 4. Zero-temperature remote-band/warping correction at 10.6 um

For each positive gap, solve `x` from the published 300-K HgCdTe gap relation and use the corresponding `gamma_i` and `F` parameters.

Compare the full quadratic six-band Kubo spectral weight against the simplified massive-Kane result at the same `E_g` and photon energy `hbar omega=0.11697 eV`.

| `E_g` (eV) | full/simplified total conductivity |
|---:|---:|
| ~0 | 0.9746 |
| 0.03 | 0.9696 |
| 0.06 | 0.9653 |
| 0.09 | 0.9618 |
| 0.115 | 0.9596 |

Channel-by-channel corrections are similarly small. At `E_g=0.09 eV`, for example,

- heavy-hole -> conduction: ~0.9624 of simplified;
- light-hole -> conduction: ~0.9596 of simplified.

Thus realistic quadratic/warping terms change the target zero-temperature conductivity by only roughly **2.5–4%** across the relevant interval.

**Status:** VERIFIED numerically from direct Kubo integration.

---

# 5. Self-consistent finite-temperature Pauli blocking in the same Hamiltonian

Use the composition-dependent anisotropic heavy-hole DOS mass from WP23 to solve intrinsic neutrality and obtain `mu(E_g,T)`.

At each target transition root, evaluate the actual band energies and Fermi occupations in the six-band Hamiltonian.

The ratio of finite-temperature to zero-temperature target spectral weight is approximately:

| `E_g` (eV) | HH->C occupation factor | LH->C occupation factor | total finite-T / zero-T |
|---:|---:|---:|---:|
| ~0 | 0.588 | 0.143 | 0.553 |
| 0.03 | 0.541 | 0.192 | 0.507 |
| 0.06 | 0.482 | 0.245 | 0.450 |
| 0.09 | 0.412 | 0.298 | 0.389 |
| 0.115 | 0.346 | 0.338 | 0.344 |

This confirms the main WP22 conclusion with the explicit quadratic six-band optical Hamiltonian:

\[
\boxed{
\text{the dominant correction is self-consistent carrier statistics / Pauli blocking, not remote-band optical curvature.}
}
\]

---

# 6. Physical interpretation

At room-temperature LWIR gaps, the large heavy-hole DOS forces a high intrinsic chemical potential. Final conduction states at the target photon energy are therefore significantly occupied.

The Moss–Burstein/Pauli-blocking effect suppresses the useful interband absorption precisely in the material regime where the flat-heavy-hole `mu=0` model suggested a finite-gap radiative optimum.

Quadratic Kane/Luttinger terms themselves are comparatively benign at a 117-meV photon because

- the Kane linear coupling dominates the electron/light-hole dispersion;
- the heavy-hole kinetic energy at the resonant `k` is only meV scale;
- the split-off band remains far away in energy.

---

# 7. Consequence for the WP21 phase diagram

WP21's fixed-`mu=0` optimum at `x_g≈3.635` cannot be rescued by adding realistic quadratic optical terms: those alter the conductivity by only a few percent.

The self-consistent heavy-hole DOS/charge-neutrality correction is order unity and remains the controlling change.

Thus the physically regularized six-band chain now reads

\[
\boxed{
\text{warped HH DOS}
\to\mu(E_g,T)
\to\text{Pauli blocking}
\to\operatorname{Re}\sigma(\omega)
\to\text{radiative + transit FI}.
}
\]

Within the restricted intrinsic/radiative-only 300-K 10.6-um model, this chain continues to favor the smallest allowed gap over the previously identified finite-gap optimum.

---

# 8. Remaining 8-band gap

The exact eight-band Hamiltonian adds the `Gamma_7` split-off doublet and its couplings. A final HgCdTe band-theory closure should repeat the same Kubo/neutrality calculation with all eight bands.

However, WP24 provides a quantitative prior on the expected size of that correction at 10.6 um:

- the direct quadratic/warping correction inside `Gamma_6+Gamma_8` is only a few percent;
- `Delta_SO` is roughly 1 eV, almost an order of magnitude above the target photon energy;
- therefore a dramatic reversal of the WP22–23 carrier-statistics conclusion from the explicit `Gamma_7` sector would require unexpectedly large low-energy renormalization beyond what is already encoded in the fitted Kane parameters.

This expectation must still be checked rather than asserted in a publication theorem.

---

# Status

**VERIFIED:** direct six-band Kubo conductivity, simplified-model unit test, remote-band/warping correction, and self-consistent finite-temperature occupation suppression.

**NEXT:** explicit eight-band `Gamma_7` audit and/or composition/doping-dependent neutrality before introducing nonradiative dark mechanisms.