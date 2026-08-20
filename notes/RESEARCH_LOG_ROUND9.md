# Research Log — Round 9

**Date:** 2026-08-20

## Purpose

Durable checkpoint after the radiative-Kane branch was regularized with finite heavy-hole curvature, self-consistent charge neutrality, anisotropic Luttinger DOS, and a direct quadratic six-band Kubo optical calculation.

This round materially corrects the old fixed-chemical-potential WP21 phase diagram. A replacement agent should treat WP21's `mu=0` table as a structural example only and read WP22–WP24 before making any quantitative HgCdTe statement.

---

# 1. Main correction to WP21

WP21 used the simplified six-band Kane model with a perfectly flat heavy-hole band and an illustrative fixed chemical potential `mu=0`. That model has an ill-defined thermodynamic heavy-hole DOS and cannot determine intrinsic carrier statistics.

Regularizing the heavy-hole curvature and solving charge neutrality changes the result qualitatively:

> for a realistic HgCdTe heavy-hole DOS mass near `0.53–0.55 m0`, the finite-gap radiative-only optimum found at fixed `mu=0` disappears in the tested 300-K / 10.6-um model; the optimum moves to the smallest allowed gap.

The controlling correction is self-consistent Pauli blocking caused by the large heavy-hole DOS, not a failure of the simplified Kane optical matrix elements.

---

# 2. WP22 — hybrid Kane conduction + finite-curvature heavy hole

Conduction branch:

\[
E_c(k)=\frac{E_g}{2}+\sqrt{(E_g/2)^2+(\hbar v_Kk)^2}.
\]

With conduction kinetic energy `epsilon=E_c-E_g`,

\[
(\hbar v_Kk)^2=\epsilon(\epsilon+E_g),
\]

\[
D_c(\epsilon)=
\frac{(2\epsilon+E_g)\sqrt{\epsilon(\epsilon+E_g)}}
{2\pi^2\hbar^3v_K^3}.
\]

Heavy hole:

\[
E_{hh}(k)=-\hbar^2k^2/(2m_{hh}).
\]

Charge neutrality:

\[
n(\mu)-p(\mu)=N_D-N_A.
\]

Intrinsic: `n=p=n_i`.

At 300 K, `v_K=1.07e6 m/s`, `m_hh=0.55m0`, and representative `Eg≈0.155 eV`, the hybrid model gives

\[
n_i\approx3.47\times10^{16}\;{\rm cm^{-3}},
\]

while the standard Hansen–Schmit HgCdTe intrinsic-density expression gives approximately `3.48e16 cm^-3`. This is a strong sanity check.

The intrinsic Fermi level lies very high because of the large heavy-hole DOS. Representative values:

- `Eg≈0`: `mu≈0.1046 eV`;
- `Eg=0.06 eV`: `mu≈0.1173 eV`;
- `Eg=0.09 eV`: `mu≈0.1253 eV`;
- `Eg=0.117 eV`: `mu≈0.1336 eV`.

Thus room-temperature LWIR material can be intrinsically conduction-degenerate in this model.

At a 10.6-um photon, the dominant HH→C Pauli occupation difference falls roughly from `0.58` at zero gap to `0.34` near `Eg=0.115 eV`.

Primary note: `notes/WP22_HEAVY_HOLE_CURVATURE_CHARGE_NEUTRALITY_REGULARIZATION.md`.

---

# 3. Heavy-hole mass is itself a resource

Within the hybrid radiative-only model, the DC small-gap slope changes sign near

\[
\boxed{m_{hh}^{crit}\approx0.4205m_0}
\]

for `T=300 K`, `lambda0=10.6 um`.

Representative DC optima:

- `m_hh=0.30m0`: finite optimum `Eg/kT≈2.70`;
- `m_hh=0.40m0`: shallow finite optimum near `0.26`;
- `m_hh>=0.50m0`: optimum at smallest allowed gap.

At a 20-GHz information task even the `0.30m0` example is driven to the gapless boundary.

The numerical critical mass is not universal; the qualitative lesson is that thermodynamic DOS curvature can change the topology of the information-optimal-gap phase diagram.

---

# 4. WP23 — anisotropic Luttinger DOS resolves scalar-mass ambiguity

Using the published HgCdTe material parameterization in `kdotpy` (Beugeling et al., SciPost Phys. Codebases 47, 2025),

\[
\gamma_1(x)=4.1-2.8801x+0.3159x^2-0.0658x^3,
\]

\[
\gamma_2(x)=0.5-0.7175x-0.0790x^2+0.0165x^3,
\]

\[
\gamma_3(x)=1.3-1.3325x+0.0790x^2-0.0165x^3.
\]

For a warped quadratic heavy-hole band, define

\[
\Delta_\gamma(\hat k)=\sqrt{Q^2+|R|^2+|S|^2},
\]

and the exact DOS-equivalent mass

\[
\boxed{
\frac{m_{hh,DOS}}{m_0}
=\left\langle
[\gamma_1-\Delta_\gamma(\hat k)]^{-3/2}
\right\rangle_\Omega^{2/3}.
}
\]

At 300 K over the positive-gap range relevant to a 10.6-um photon:

\[
\boxed{m_{hh,DOS}\approx0.531-0.542m_0.}
\]

At the same time directional masses span approximately

\[
m_{hh,[001]}\approx0.34-0.35m_0,
\]

\[
m_{hh,[111]}\approx0.677-0.683m_0.
\]

Thus the commonly quoted `0.3–0.7m0` range is largely compatible with valence-band warping, while the thermodynamic DOS mass is close to the common scalar modeling value `0.55m0`.

This puts the physically relevant DOS branch safely above the WP22 `~0.4205m0` bifurcation.

Primary note: `notes/WP23_ANISOTROPIC_LUTTINGER_HEAVY_HOLE_DOS.md`.

---

# 5. WP24 — direct quadratic six-band Kubo audit

Implemented a bulk `Gamma6 + Gamma8` Hamiltonian with

- quadratic conduction term `2F+1`;
- Kane coupling `P`;
- cubic Luttinger `gamma1,gamma2,gamma3` valence block;
- the same current HgCdTe parameterization used in WP23.

Velocity operators:

\[
v_i=(1/\hbar)\partial H/\partial k_i.
\]

Interband conductivity:

\[
\operatorname{Re}\sigma(\omega)=
\frac{\pi e^2}{\omega}
\sum_{n<m}\int\frac{d^3k}{(2\pi)^3}
(f_n-f_m)
\frac13\sum_i|\langle n|v_i|m\rangle|^2
\delta(E_m-E_n-\hbar\omega).
\]

### Unit test

Turning off all quadratic remote-band terms reproduces the known simplified gapless Kane result:

- HH→C : LH→C spectral weight = `12:1`;
- total conductivity `13 e^2 omega/(48 pi hbar v_K)`;
- numerical/analytic ratio `0.999999996`.

### Realistic quadratic/warping correction at 10.6 um

Full quadratic six-band / simplified massive-Kane zero-T total conductivity:

- `Eg≈0`: `0.9746`;
- `0.03 eV`: `0.9696`;
- `0.06 eV`: `0.9653`;
- `0.09 eV`: `0.9618`;
- `0.115 eV`: `0.9596`.

Thus remote-band/warping terms change the target optical conductivity by only about `2.5–4%`.

### Self-consistent finite-T Pauli suppression

Using intrinsic neutrality from WP23, finite-T / zero-T target spectral weight is approximately:

- `Eg≈0`: `0.553`;
- `0.03 eV`: `0.507`;
- `0.06 eV`: `0.450`;
- `0.09 eV`: `0.389`;
- `0.115 eV`: `0.344`.

Therefore

\[
\boxed{
\text{carrier statistics / Pauli blocking is the order-unity correction; quadratic optical curvature is only a few-percent correction.}
}
\]

Primary note: `notes/WP24_REGULARIZED_SIX_BAND_KANE_LUTTINGER_OPTICAL_AUDIT.md`.

---

# 6. Current quantitative interpretation

The old WP21 fixed-`mu=0` finite-gap optimum is **not** a self-consistent intrinsic-HgCdTe prediction.

For the current best restricted branch:

- anisotropic heavy-hole DOS from a published parameterization;
- self-consistent intrinsic charge neutrality;
- direct quadratic six-band Kubo target conductivity;
- radiative-only dark generation;
- 300 K, 10.6 um;

the information optimum remains at the smallest allowed gap over the tested source-flux/task range.

This is still not a complete detector prediction because nonradiative dark mechanisms, doping, electrostatics, and real readout remain omitted.

---

# 7. Novelty posture

Do not claim novelty for:

- HgCdTe nonparabolic carrier statistics;
- Luttinger heavy-hole warping/DOS;
- charge-neutrality Fermi-level calculations;
- Moss–Burstein/Pauli blocking;
- six-/eight-band Kane optical conductivity;
- radiative detailed balance;
- ordinary absorption/transit-time tradeoffs.

The candidate UPRP contribution remains the **source-normalized information/resource-completeness construction** and the explicit demonstration that apparently natural reduced resource sets (`Eg,T`, fixed `mu`, one `effective mass`, etc.) are insufficient to determine an information-optimal detector.

---

# 8. Immediate next work

1. Perform an explicit `Gamma7` split-off / eight-band optical audit using a consistent HgCdTe parameter set.
2. Solve doping sensitivity `n-p=N_D-N_A` over realistic net doping and quantify Pauli blocking/information-optimum movement.
3. Use the same eight-band Hamiltonian for DOS, neutrality, and Kubo response if feasible.
4. Only after the equilibrium band/statistics layer is stable, add Auger and SRH mechanisms one at a time.

**Status:** WP22–WP24 substantially close the heavy-hole/statistics regularization; full eight-band and doping layers remain open.