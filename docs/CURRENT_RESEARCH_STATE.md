# Current Research State

**Date:** 2026-08-20

This is the first-stop replacement-agent summary. **The repository, not chat history, is authoritative.**

Read first:

1. `AGENTS.md`
2. `notes/RESEARCH_LOG_ROUND9.md`
3. `notes/WP22_HEAVY_HOLE_CURVATURE_CHARGE_NEUTRALITY_REGULARIZATION.md`
4. `notes/WP23_ANISOTROPIC_LUTTINGER_HEAVY_HOLE_DOS.md`
5. `notes/WP24_REGULARIZED_SIX_BAND_KANE_LUTTINGER_OPTICAL_AUDIT.md`
6. `notes/RESEARCH_LOG_ROUND8.md`
7. `notes/WP21_DIMENSIONLESS_RADIATIVE_KANE_PHASE_DIAGRAM.md`
8. `notes/WP15_DELAY_CONCENTRATION_AND_LOCALIZED_CAPTURE_CAPACITY.md`
9. `notes/WP11_SPATIAL_DELAY_INFORMATION_THEOREM.md`
10. the earlier WP0–WP14 notes as needed.

---

## Central objective

Determine which physical resources are necessary and/or sufficient for a finite-temperature photodetector to transfer information from an incident optical field into an intrinsic electrical record with specified sensitivity and temporal **information bandwidth**.

Core metric:

\[
\boxed{\eta_I=F_{\rm electrical}/F_{\rm incident}^{Q}.}
\]

The project is a resource-completeness / no-go + repair program. A simple sensitivity-bandwidth-temperature product is not assumed.

---

## Core conceptual correction

\[
\boxed{\text{latency}\neq\text{amplitude bandwidth}\neq\text{information bandwidth}.}
\]

Known deterministic delay or invertible deterministic filtering does not by itself reduce stationary Fisher information if signal and all upstream noise are transformed consistently. Information loss requires unresolved stochasticity, inaccessible/coarse-grained variables, downstream noise, finite observation/sampling/quantization, or exact nulls.

---

## Established no-go/repair structure

### Classical/Markov

Finite EPR/activity/detailed balance/throughput do not bound absolute speed if bare microscopic rates can diverge in rare states. An absolute microscopic rate/coupling resource is necessary. WP3 provides a restricted gateway repair.

### Quantum apparatus

Passive coherent transfer obeys directional SLD-Stam. Pre-squeezing proves coupling action alone is insufficient. With pointer excitation budget `N`,

\[
\frac{F_{\rm elec}}{F_{\rm in}}
\le\frac\tau{\tau+(1-\tau)(\sqrt{N+1}-\sqrt N)^2}.
\]

The ideal harmonic pointer has a UV coherence loophole under free-energy-only constraints. Finite support plus bounded generator gives an exact repair.

### Optical/transport geometry

For random unresolved event delay `D`,

\[
\eta_I(\omega)=\eta_c|\mathbb E e^{-i\omega D}|^2.
\]

Uniform unresolved depth yields

\[
f_{1/2}=0.4429464707\,v/L.
\]

WP15 proves that high average information across a modulation band requires a large fraction of incident photons to be captured in a narrow **delay window**. Total optical volume is not the right resource; localized capture in delay space is.

---

## Kane/HgCdTe material branch

### WP17–18

Gapless simplified Kane conductivity:

\[
\operatorname{Re}\sigma_K=\frac{13e^2\omega}{48\pi\hbar v_K}.
\]

The `13/12` coefficient and Kane dielectric function are prior art. Generic `alpha_abs v` photodiode bandwidth-efficiency physics is also prior art.

Finite positive gap:

\[
\operatorname{Re}\sigma_K=
\frac{e^2\omega}{48\pi\hbar v_K}
\left[12\sqrt{1-y}+(1+2y^2)\sqrt{1-y^2}\right],
\quad y=E_g/(\hbar\omega).
\]

At zero temperature, opening the gap worsens the ideal optical-depth/ballistic-transport layer; a finite optimum requires dark/statistical resources.

### WP19–21 radiative detailed balance

van Roosbroeck–Shockley ties equilibrium radiative generation to the absorption spectrum. The old WP21 dimensionless phase diagram used **illustrative fixed `mu=0`** because the perfectly flat heavy-hole band has no finite thermodynamic DOS.

Important: WP21's finite-gap optimum near `E_g/kT≈3.635` is now **superseded quantitatively** by WP22–24. It remains only a structural fixed-chemical-potential example.

---

## WP22 — finite heavy-hole curvature and self-consistent neutrality

Use nonparabolic Kane conduction plus a finite parabolic heavy-hole DOS and solve

\[
n(\mu)-p(\mu)=N_D-N_A.
\]

For intrinsic 300-K material and `m_hh≈0.55m0`, the calculation agrees closely with standard HgCdTe intrinsic-density formulas. Example near `E_g≈0.155 eV`:

\[
n_i\approx3.47\times10^{16}\,cm^{-3}
\]

versus approximately `3.48e16 cm^-3` from the standard empirical expression.

The large heavy-hole DOS pushes the intrinsic Fermi level toward/into the conduction band over much of the room-temperature LWIR gap range, producing strong Pauli/Moss–Burstein suppression of target absorption.

At 10.6 um, the dominant HH→C occupation difference falls roughly from `0.58` near zero gap to `0.34` near `E_g=0.115 eV`.

In the restricted radiative-only phase diagram, a scalar heavy-hole-mass bifurcation occurs near `0.4205m0` for the specific 300-K/10.6-um DC task. `m_hh≈0.55m0` removes the old interior optimum and favors the smallest allowed gap.

---

## WP23 — anisotropic heavy-hole DOS closes the scalar-mass ambiguity

Using the published 2025 `kdotpy` HgCdTe Kane/Luttinger parameterization, the warped heavy-hole DOS-equivalent mass is

\[
\boxed{
\frac{m_{hh,DOS}}{m_0}
=\left\langle[\gamma_1-\Delta_\gamma(\hat k)]^{-3/2}\right\rangle_\Omega^{2/3}.
}
\]

Across the 300-K positive-gap range relevant to a 10.6-um photon:

\[
\boxed{m_{hh,DOS}\approx0.531-0.542m_0.}
\]

Directional masses simultaneously span roughly `0.34m0` `[001]` to `0.68m0` `[111]`.

Thus **directional transport mass is not the same resource as thermodynamic DOS mass**. The physically relevant DOS branch lies safely above the WP22 restricted bifurcation and supports the standard `~0.55m0` neutrality branch.

---

## WP24 — direct quadratic six-band optical audit

An explicit `Gamma6+Gamma8` Kane–Luttinger Hamiltonian using the same published material parameters was evaluated with

\[
v_i=(1/\hbar)\partial H/\partial k_i
\]

and the interband Kubo formula.

### Validation

Turning off quadratic remote-band terms reproduces the exact gapless simplified-Kane result:

- HH→C : LH→C spectral weight = `12:1`;
- total `13 e^2 omega/(48 pi hbar v_K)` coefficient;
- numerical/analytic ratio `0.999999996`.

### Realistic correction

At 10.6 um, realistic quadratic/warping terms reduce the zero-T target conductivity only modestly:

- `E_g≈0`: full/simplified `0.9746`;
- `0.03 eV`: `0.9696`;
- `0.06 eV`: `0.9653`;
- `0.09 eV`: `0.9618`;
- `0.115 eV`: `0.9596`.

By contrast, self-consistent finite-T occupation suppresses target spectral weight to approximately:

- `0.553` of zero-T at `E_g≈0`;
- `0.507` at `0.03 eV`;
- `0.450` at `0.06 eV`;
- `0.389` at `0.09 eV`;
- `0.344` at `0.115 eV`.

Therefore the current strongest material-layer conclusion is

\[
\boxed{
\text{self-consistent carrier statistics / Pauli blocking is the order-unity correction; remote-band optical curvature is only a few-percent correction.}
}

Within the restricted intrinsic/radiative-only 300-K/10.6-um branch, the information optimum remains at the smallest allowed gap over the tested source/task range.

---

## Current resource hierarchy

The strongest current structure is

\[
\boxed{
\text{finite source task}
+\text{localized finite-band optical capture}
+\text{absolute microscopic coupling}
+\text{apparatus support/generator resource}
+\text{semiconductor band/DOS/current resources}
+\text{self-consistent occupations/doping}
+\text{optical/electrical geometry and timing statistics}
+\text{dark/thermokinetic resources}
+\text{readout noise/sampling resources}
\Rightarrow\text{finite information ceiling}
}
\]

under explicit model assumptions.

The recurring failure mode is an omitted resource hidden in a rare, UV, canceling, spatially localized, or unobserved sector.

---

## Novelty constraints

Do not claim novelty for generic:

- `alpha_abs v` photodiode bandwidth-efficiency;
- Kane/HgCdTe optical conductivity;
- nonparabolic carrier statistics;
- heavy-hole/Luttinger/8-band theory;
- Moss–Burstein/Pauli blocking;
- van Roosbroeck–Shockley radiative balance;
- Shockley–Ramo;
- transit `0.44/tau` scaling;
- RC amplitude bandwidth;
- Zeno/anti-Zeno detector effects;
- squeezing/non-Gaussian metrology;
- optical sum rules.

Candidate novelty remains the **source-normalized photodetection resource-completeness chain** and explicit demonstration that reduced resource sets (`E_g,T`, fixed chemical potential, one unspecified effective mass, conventional amplitude bandwidth, total device volume) do not determine intrinsic information performance.

---

## Immediate next gates

1. **Explicit eight-band `Gamma7` split-off audit** using a consistent HgCdTe parameter set and Kubo calculation. The split-off scale is ~1 eV, so the correction is expected to be moderate but must be checked.
2. **Doping sensitivity:** solve `n-p=N_D-N_A` across realistic net doping and quantify Pauli blocking and movement of the information optimum.
3. Use one Hamiltonian consistently for DOS, neutrality, and optical response where feasible.
4. Add Auger and SRH only after the equilibrium band/statistics layer is stable.
5. Continue theorem-level novelty audit before publication claims.

**Latest durable checkpoint:** `notes/RESEARCH_LOG_ROUND9.md`.