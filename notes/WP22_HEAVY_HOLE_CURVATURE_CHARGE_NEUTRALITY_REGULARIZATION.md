# WP22 — Heavy-hole curvature and charge-neutrality regularization

**Date:** 2026-08-20

## Purpose

WP21 used the simplified six-band Kane model with an exactly flat heavy-hole band and an illustrative fixed chemical potential. That model is adequate for high-energy Kane optical matrix elements but is not thermodynamically well posed for intrinsic carrier statistics: an exactly flat three-dimensional heavy-hole band produces a UV-sensitive/ill-defined hole DOS.

This note introduces the weakest standard HgCdTe regularization needed to make the carrier statistics finite:

1. retain the nonparabolic Kane conduction band;
2. give the heavy-hole band a finite parabolic curvature `m_hh`;
3. solve charge neutrality self-consistently for the chemical potential;
4. feed the resulting Fermi level into the finite-temperature interband Pauli factors.

This is **not yet a full 8-band optical calculation**. It is a controlled hybrid carrier-statistics regularization whose main role is to determine whether the WP21 phase diagram survives a physically finite heavy-hole DOS.

---

# 1. Band model

Reference energy is the valence-band maximum.

For the Kane conduction branch,

\[
E_c(k)=\frac{E_g}{2}+\sqrt{\left(\frac{E_g}{2}\right)^2+(\hbar v_Kk)^2}.
\]

Write the conduction kinetic energy above the edge as

\[
\epsilon=E_c-E_g\ge0.
\]

Then

\[
(\hbar v_Kk)^2=\epsilon(\epsilon+E_g).
\]

The spin-degenerate conduction DOS is therefore

\[
\boxed{
D_c(\epsilon)
=\frac{(2\epsilon+E_g)\sqrt{\epsilon(\epsilon+E_g)}}
{2\pi^2\hbar^3v_K^3}.
}
\]

Regularize the heavy-hole band by

\[
\boxed{
E_{hh}(k)=-\frac{\hbar^2k^2}{2m_{hh}}.
}
\]

This is the standard approximation used in HgCdTe carrier-statistics/device modeling. Literature models commonly use `m_hh≈0.55 m0`, while reported/model values span roughly `0.3–0.7 m0`; anisotropy is one reason for the spread.

---

# 2. Exact charge-neutrality equations for the hybrid model

Let `mu` be measured from the valence-band maximum.

Electron concentration:

\[
\boxed{
n(\mu,E_g,T)
=\int_0^\infty
D_c(\epsilon)
\frac{d\epsilon}
{1+\exp[(E_g+\epsilon-\mu)/k_BT]}.
}
\]

Heavy-hole concentration:

\[
\boxed{
p(\mu,T)
=\frac1{2\pi^2}
\left(\frac{2m_{hh}}{\hbar^2}\right)^{3/2}
\int_0^\infty
\frac{\sqrt\epsilon\,d\epsilon}
{1+\exp[(\mu+\epsilon)/k_BT]}.
}
\]

For fully ionized net doping `N_net=N_D-N_A`, neutrality is

\[
\boxed{n-p=N_{net}.}
\]

For intrinsic material,

\[
\boxed{n=p=n_i.}
\]

Dimensionless variables

\[
x=\epsilon/(k_BT),\qquad x_g=E_g/(k_BT),\qquad u=\mu/(k_BT)
\]

make the calculation a one-dimensional root solve.

**Status:** exact within the stated hybrid band model.

---

# 3. Strong validation against standard HgCdTe intrinsic-density formulas

Use

- `T=300 K`,
- `v_K=1.07e6 m/s`,
- `m_hh=0.55 m0`.

For representative `Hg_0.8Cd_0.2Te` at 300 K, take `E_g≈0.155 eV`.

The hybrid charge-neutrality calculation gives

\[
\boxed{n_i=3.47\times10^{16}\;{\rm cm^{-3}}.}
\]

The standard Hansen–Schmit empirical expression at `x=0.2`, 300 K gives approximately

\[
\boxed{n_i=3.48\times10^{16}\;{\rm cm^{-3}}.}
\]

The agreement is better than one percent for this check.

Additional gap-only checks using the same parameters also track the standard intrinsic-density scale closely:

| `E_g` (eV) | hybrid `n_i` (cm^-3) |
|---:|---:|
| 0.03 | 1.42e17 |
| 0.06 | 1.09e17 |
| 0.09 | 8.01e16 |
| 0.117 | 5.81e16 |
| 0.155 | 3.47e16 |
| 0.20 | 1.75e16 |

This is a strong sanity check that the finite-curvature regularization is physically in the correct HgCdTe carrier-statistics regime.

Literature anchors:

- J. L. Schmit, *Intrinsic Carrier Concentration of Hg1-xCdxTe as a Function of x and T Using k·p Calculations*, J. Appl. Phys. 41, 2876 (1970), DOI `10.1063/1.1659330`.
- Modern HgCdTe modeling commonly uses `m_hh≈0.55m0`; reported values span approximately `0.3–0.7m0`.
- The standard narrow-gap carrier-concentration treatment uses a nonparabolic Kane conduction band and a parabolic heavy-hole density of states.

Do not claim this carrier-statistics model as novel.

---

# 4. Intrinsic Fermi level is strongly displaced toward/into the conduction band

For `m_hh=0.55m0`, 300 K:

| `E_g` (eV) | `mu` (eV) | `mu-E_g` (meV) | `n_i` (cm^-3) |
|---:|---:|---:|---:|
| ~0 | 0.1046 | +104.6 | 1.78e17 |
| 0.03 | 0.1104 | +80.4 | 1.42e17 |
| 0.06 | 0.1173 | +57.3 | 1.09e17 |
| 0.09 | 0.1253 | +35.3 | 8.01e16 |
| 0.105 | 0.1298 | +24.8 | 6.74e16 |
| 0.115 | 0.1330 | +18.0 | 5.96e16 |
| 0.117 | 0.1336 | +16.6 | 5.81e16 |
| 0.155 | 0.1470 | -8.0 | 3.47e16 |

The large heavy-hole DOS pushes the intrinsic Fermi level strongly upward. In the room-temperature LWIR gap range, the conduction band can be intrinsically degenerate.

This is exactly why the fixed `mu=0` assumption in WP21 cannot be used quantitatively.

---

# 5. Finite-temperature optical Pauli factors

Retain the WP18 simplified-Kane optical matrix/phase-space factors but replace the arbitrary chemical potential by the neutrality solution.

For a photon energy `x=hbar omega/(kBT)` and `x_g=E_g/(kBT)`, define the Fermi function

\[
f(z;u)=\frac1{1+e^{z-u}}.
\]

In the flat-heavy-hole optical approximation, the two channel occupation differences are

\[
\boxed{
A_{0+}=f(0;u)-f(x;u),
}
\]

and

\[
\boxed{
A_{-+}
=f((x_g-x)/2;u)-f((x_g+x)/2;u).
}
\]

Hence the self-consistent finite-temperature spectral factor is

\[
\boxed{
F_{K,T}^{sc}(x;x_g)
=12\sqrt{1-x_g/x}\,A_{0+}
+\left[1+2(x_g/x)^2\right]
\sqrt{1-(x_g/x)^2}\,A_{-+},
}
\]

with

\[
u=u(x_g;m_{hh},v_K,T,N_{net})
\]

fixed by charge neutrality.

This formula is exact for the Pauli factors of the simplified optical model and uses a physically regularized chemical potential.

---

# 6. Why using the flat optical matrix element remains a controlled first regularization

Giving the heavy-hole band finite curvature shifts the initial heavy-hole energy at the optical resonance. For a 10.6-um photon (`hbar omega≈0.11697 eV`) and `m_hh=0.55m0`, solving

\[
E_c(k)-E_{hh}(k)=\hbar\omega
\]

gives heavy-hole kinetic shifts only of order

- about `1.85 meV` at zero gap;
- below `1 meV` for `E_g≈0.06 eV`;
- below `0.5 meV` for `E_g≈0.09 eV`;
- tens of `ueV` very close to the target edge.

Thus the heavy-hole curvature is decisive for the **integrated DOS and chemical potential**, while its direct correction to a 117-meV target optical transition is percent-level or smaller in this parameter range.

Numerically, replacing the flat-state occupation factor by the actual parabolic-HH resonance changes the dominant channel occupation factor only modestly in this example.

Therefore the hybrid calculation is a useful intermediate regularization before a complete 8-band optical calculation.

---

# 7. Pauli blocking is quantitatively important at 10.6 um, 300 K

Using intrinsic neutrality and `m_hh=0.55m0`, the dominant heavy-hole-to-conduction occupation difference at the target photon is approximately:

| `E_g` (eV) | occupation difference |
|---:|---:|
| ~0 | 0.584 |
| 0.03 | 0.536 |
| 0.06 | 0.478 |
| 0.09 | 0.408 |
| 0.105 | 0.370 |
| 0.115 | 0.344 |

Thus the previous `mu=0` radiative-Kane phase diagram materially overestimated the available target absorption in intrinsic room-temperature LWIR HgCdTe.

The corresponding light-hole-to-conduction factor is also nontrivial and changes in the opposite direction over part of this range, so both channels must be retained.

---

# 8. Recomputed radiative-only phase diagram: qualitative correction

Insert the self-consistent `F_{K,T}^{sc}` into both

1. the target absorption factor `F_0`, and
2. the van Roosbroeck–Shockley thermal integral

\[
\mathcal I_K^{sc}(x_g)
=\int_{x_g}^{\infty}
\frac{x^3F_{K,T}^{sc}(x;x_g)}{e^x-1}\,dx.
\]

Then use the same finite-slab information expression as WP21.

For the representative parameters

- `T=300 K`,
- `lambda_0=10.6 um`,
- `eta_c=0.9`,
- `n=3.2`,
- intrinsic neutrality,
- `v_K=1.07e6 m/s`,
- `m_hh=0.55m0`,

numerical optimization gives a major qualitative change:

> **The radiative-only optimum moves to the smallest allowed gap for the tested DC through 100-GHz tasks and source-flux range.**

At DC, the controlling ratio

\[
\mathcal I_K^{sc}/F_0
\]

increases from about `4.59` near zero gap to about `6.28` at `x_g=4`, before diverging at the target edge. The finite-gap minimum at `x_g≈3.635` found in WP21 under `mu=0` therefore disappears for the standard `m_hh=0.55m0` intrinsic-neutrality model.

Example at `psi=100`:

| task | optimum `x_g` | max `eta_I` |
|---:|---:|---:|
| DC | boundary `x_g -> 0` | ~0.805 |
| 10 GHz | boundary `x_g -> 0` | ~0.788 |
| 20 GHz | boundary `x_g -> 0` | ~0.737 |
| 50 GHz | boundary `x_g -> 0` | ~0.460 |
| 100 GHz | boundary `x_g -> 0` | ~0.111 |

These remain **restricted-model calculations**, not device predictions.

---

# 9. Heavy-hole mass is a qualitative phase-diagram resource

The result is highly sensitive to the heavy-hole DOS curvature, which is precisely the parameter omitted by the flat-band model.

At 300 K, 10.6 um, the DC slope of the radiative ratio at zero gap changes sign near

\[
\boxed{m_{hh}^{crit}\approx0.4205m_0}
\]

within the present hybrid approximation.

Representative global DC optima for `psi=100`:

| `m_hh/m0` | optimum `x_g=E_g/kBT` |
|---:|---:|
| 0.30 | ~2.70 |
| 0.40 | ~0.263 |
| 0.50 | boundary `0` |
| 0.55 | boundary `0` |
| 0.70 | boundary `0` |

At a 20-GHz information task, even the `m_hh=0.30m0` example is driven to the gapless boundary in the same restricted model.

Therefore

\[
\boxed{
\text{heavy-hole DOS curvature can change the topology of the information-optimal-gap phase diagram.}
}
\]

This is a resource-sensitivity result, not a claim that `0.4205m0` is universal. The number depends on the target wavelength, temperature, optical model, and other assumptions.

---

# 10. Why a full 8-band calculation remains necessary

HgCdTe heavy-hole mass is anisotropic and model dependent. Reported/effective values span roughly `0.3–0.7m0`, and different measurements probe different combinations of the warped valence-band curvature.

An 8-band Kane/Luttinger Hamiltonian introduces the remote-band parameters `gamma_1,gamma_2,gamma_3`, split-off band, and anisotropic valence dispersion. In an isotropic/directional approximation the heavy-hole masses involve combinations such as

\[
m_{hh,[001]}^{-1}/m_0^{-1}=\gamma_1-2\gamma_2,
\]

\[
m_{hh,[111]}^{-1}/m_0^{-1}=\gamma_1-2\gamma_3.
\]

Published HgTe parameter sets illustrate substantial directional variation, consistent with the broad effective-mass range used in HgCdTe modeling.

Thus the next calculation should use an explicit, cited bulk-HgCdTe 8-band parameter set and compute the full anisotropic DOS rather than choose one scalar `m_hh`.

---

# 11. Main correction to WP21

The WP21 `mu=0` table remains useful only as a **structural fixed-chemical-potential example**.

It must not be read as a self-consistent intrinsic-HgCdTe optimum.

The physically regularized result is:

\[
\boxed{
\text{charge neutrality + heavy-hole curvature materially changes both target absorption and radiative dark generation.}
}
\]

For standard `m_hh≈0.55m0`, the former interior radiative-only gap optimum disappears in the tested 300-K/10.6-um model.

Even the sign of the small-gap optimization slope depends on the heavy-hole DOS resource.

This materially strengthens the broader UPRP conclusion that a supposedly universal optimum cannot be obtained from `E_g`, `T`, and the target photon energy alone.

---

# 12. Status and next work

**PROVED/DERIVED:**

- exact hybrid Kane-conduction + parabolic-HH neutrality equations;
- finite intrinsic chemical potential;
- self-consistent finite-temperature Pauli factors;
- strong agreement with standard intrinsic-density formulas;
- numerical destruction of the WP21 interior optimum for the standard `m_hh=0.55m0` example;
- heavy-hole-mass bifurcation in the restricted radiative phase diagram.

**OPEN:**

1. Replace scalar `m_hh` by the full anisotropic 8-band HgCdTe valence DOS.
2. Include the split-off band and remote-band terms in the optical conductivity, not only in the carrier statistics.
3. Solve neutrality with real donor/acceptor densities and incomplete ionization where relevant.
4. Recompute the radiative phase diagram with the full 8-band spectrum and optical matrix elements.
5. Add Auger/SRH only after the equilibrium band/statistics layer is stable.

**Novelty caution:** nonparabolic carrier statistics, heavy-hole mass modeling, Moss–Burstein/Pauli blocking, and 8-band HgCdTe theory are established prior art. Candidate UPRP value is the way these resources alter the source-information optimum and demonstrate resource incompleteness of simpler gap-temperature statements.