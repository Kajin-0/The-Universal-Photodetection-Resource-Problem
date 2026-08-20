# AGENTS.md

## Purpose

Durable handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat context, is authoritative.

Research is analytical/theoretical only. Numerical algebra and simulation are allowed for validation. Do not make laboratory experiments, fabrication, sample procurement, or measurement campaigns necessary next steps.

## Read first

A replacement agent should read, in order:

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `notes/RESEARCH_LOG_ROUND9.md`
3. `notes/WP22_HEAVY_HOLE_CURVATURE_CHARGE_NEUTRALITY_REGULARIZATION.md`
4. `notes/WP23_ANISOTROPIC_LUTTINGER_HEAVY_HOLE_DOS.md`
5. `notes/WP24_REGULARIZED_SIX_BAND_KANE_LUTTINGER_OPTICAL_AUDIT.md`
6. `notes/RESEARCH_LOG_ROUND8.md`
7. `notes/WP21_DIMENSIONLESS_RADIATIVE_KANE_PHASE_DIAGRAM.md`
8. `notes/WP17_MASSLESS_KANE_ABSORPTION_TRANSPORT_INFORMATION_THEOREM.md`
9. `notes/WP18_FINITE_GAP_KANE_ABSORPTION_TRANSPORT_BOUND.md`
10. `notes/WP15_DELAY_CONCENTRATION_AND_LOCALIZED_CAPTURE_CAPACITY.md`
11. `notes/WP11_SPATIAL_DELAY_INFORMATION_THEOREM.md`
12. `notes/WP8_UV_NON_GAUSSIAN_INSTABILITY.md`
13. `notes/WP8_GENERAL_FINITE_SUBSPACE_GENERATOR_THEOREM.md`
14. `notes/WP5_T_OPERATOR_FINITE_BAND_CAPTURE.md`
15. `notes/WP4_MICROSCOPIC_OPTICAL_COUPLING_NO_GO.md`
16. `docs/LITERATURE_MAP.md`
17. `docs/FORMALISM.md`

Older work-package notes and research logs preserve derivations, failed conjectures, and novelty corrections.

---

# Project objective

Determine which physical resources are necessary and/or sufficient for a finite-temperature photodetector to transfer information from an incident optical field into an intrinsic electrical record with specified sensitivity and **information bandwidth**.

The project is a **resource-completeness / no-go + repair program**, not a search for a naive sensitivity-bandwidth-temperature product.

Core metric:

\[
\boxed{\eta_{\mathcal I}=F_{\rm electrical}/F_{\rm incident}^{Q}}
\]

for the same encoded parameter.

For weak coherent/Poisson flux modulation,

\[
\eta_{\mathcal I}(\omega)=\Phi_0|\chi_{Y\Phi}(\omega)|^2/S_Y(\omega).
\]

Use a finite source-information task, not an unweighted all-frequency integral.

---

# Mandatory conceptual distinction

\[
\boxed{\text{latency}\neq\text{amplitude bandwidth}\neq\text{information bandwidth}.}
\]

A deterministic known delay changes phase but not stationary spectral Fisher information. A deterministic invertible LTI filter applied to signal and all upstream noise preserves `|chi|^2/S` wherever its transfer function is nonzero. Information loss needs stochastic/unresolved timing, inaccessible/coarse-grained variables, downstream noise, finite sampling/quantization/observation, or exact spectral nulls.

Do not insert conventional transit or RC `-3 dB` bandwidth into a UPRP theorem without an explicit accessible-record/noise model.

---

# Established resource-completeness chain

## Classical/Markov no-go

An explicit reversible finite-state family proves

\[
\{T,\hbar\omega_0,\text{detailed balance},f_*,\mathcal A,\Sigma,\text{edge EPRs},\eta_q\}
\not\Rightarrow\text{finite absolute detector speed}.
\]

An absolute microscopic coupling/rate scale is necessary. WP3 gives a restricted repair once gateway kinetics are bounded.

## Passive optical capture

WP5 combines coherent-state information data processing with rigorous T-operator sum rules. Optical power-bandwidth/sum-rule theory itself is prior art.

## Quantum apparatus resource

Directional SLD Stam gives, for coherent input and passive source-to-pointer transfer probability `tau`,

\[
\frac{F_{\rm elec}}{F_{\rm in}}
\le\frac{\tau J_D}{2(1-\tau)+\tau J_D}.
\]

A pre-squeezed apparatus proves coupling action alone is insufficient. With total excitation `N`,

\[
\frac{F_{\rm elec}}{F_{\rm in}}
\le\frac\tau{\tau+(1-\tau)\xi(N)},
\quad
\xi(N)=(\sqrt{N+1}-\sqrt N)^2,
\]

and the bound is globally tight in the passive-linear single-effective-mode model.

WP8 further proves a UV coherence loophole for an unrestricted harmonic pointer: finite free energy and all diagonal energy moments do not uniformly bound displacement QFI. Exact finite-support/generator repair:

\[
\sup_{\rho\subset S}F_Q(\rho,G)=
4\inf_c\lambda_{\max}[\Pi_S(G-cI)^2\Pi_S].
\]

TRK alone fails for arbitrary excited pointer states because signed oscillator strengths can cancel.

---

# Semiconductor embedding

WP11 maps the abstract coupling into finite-level current capacity and Shockley–Ramo geometry. For a finite electrical subspace,

\[
\|I\|\le W_S\Delta Q_S/(2\hbar),
\]

and with weighting potential `phi_w`, velocity capacity `v_S`, and `ell_w^{-1}=sup|grad phi_w|`,

\[
\|I_w\|\le |q|v_S/\ell_w.
\]

For independently captured events with unresolved delay `D`,

\[
\eta_I(\omega)=\eta_c|\mathbb E e^{-i\omega D}|^2.
\]

Uniform unresolved depth gives

\[
\eta_I=\eta_c\operatorname{sinc}^2(\omega L/2v),
\qquad
f_{1/2}=0.4429464707\,v/L.
\]

This coefficient is an unresolved-delay information result, not deterministic latency.

---

# WP15 localized capture

For flat modulation band and conditional event delay `D`, define

\[
M_D(\Delta t)=\eta_c\sup_a\Pr[D\in[a,a+\Delta t]].
\]

For any `x>0`, `c_x=sup_{|u|>=x}|sinc u|`,

\[
\boxed{\bar\eta_I\le c_x+(1-c_x)M_D(2x/\Omega_s).}
\]

Thus the relevant optical/transport bridge is **localized capture capacity in delay space**, not total absorber/device volume.

---

# Kane semiconductor branch — current frontier

## WP17 massless Kane

For the gapless simplified six-band model,

\[
\boxed{\operatorname{Re}\sigma_K=\frac{13e^2\omega}{48\pi\hbar v_K}.}
\]

Flat-HH-to-cone : cone-to-cone spectral weight is `12:1`. This coefficient agrees with prior Orlita HgCdTe theory; do not claim it as new.

Weak-loss absorption/transport scale:

\[
\alpha_{abs}v_K/\omega\simeq\frac{13}{12n}\alpha_{fs}.
\]

Ordinary `alpha*v` photodiode bandwidth-efficiency physics is longstanding prior art.

## WP18 finite positive gap

For `y=Eg/(hbar omega)`,

\[
\operatorname{Re}\sigma_K=\frac{e^2\omega}{48\pi\hbar v_K}F_K(y),
\]

\[
F_K(y)=12\sqrt{1-y}+(1+2y^2)\sqrt{1-y^2}.
\]

The dominant flat-to-conduction group velocity factor is

\[
u_0(y)=2\sqrt{1-y}/(2-y).
\]

At zero temperature the ideal optical-depth/transport resource worsens monotonically with increasing gap. Any finite optimum must come from dark/statistical resources.

## WP21 old fixed-chemical-potential phase diagram — IMPORTANT LIMITATION

WP21 used an illustrative `mu=0` because the exactly flat heavy-hole band cannot define a finite intrinsic DOS. Its finite-gap optimum near `Eg/kT≈3.635` is a **structural fixed-mu example only** and is superseded quantitatively by WP22–24.

---

# WP22–WP24 — current HgCdTe regularized result

## WP22 finite heavy-hole curvature + charge neutrality

Use nonparabolic Kane conduction plus a parabolic heavy-hole DOS and solve

\[
n(\mu)-p(\mu)=N_D-N_A.
\]

For intrinsic 300-K HgCdTe with `m_hh≈0.55m0`, the result reproduces standard intrinsic-density formulas very closely; e.g. near `Eg≈0.155 eV`,

\[
n_i\approx3.47\times10^{16}\,cm^{-3}
\]

versus approximately `3.48e16 cm^-3` from the standard empirical expression.

The large heavy-hole DOS pushes the intrinsic Fermi level very high. At room-temperature LWIR gaps the conduction band can be intrinsically degenerate, causing strong Pauli/Moss-Burstein suppression of target absorption.

Within the restricted radiative-only 300-K/10.6-um model, `m_hh≈0.55m0` destroys the old finite-gap optimum and moves the optimum to the smallest allowed gap over the tested task/source range.

A scalar-mass bifurcation appears near `m_hh≈0.4205m0` for that specific DC task; the number is not universal.

## WP23 anisotropic Luttinger DOS

Using the published 2025 `kdotpy` HgCdTe Kane/Luttinger parameterization, the exact warped-quadratic DOS-equivalent mass is

\[
\left(m_{hh,DOS}/m_0\right)^{3/2}
=\langle[\gamma_1-\Delta_\gamma(\hat k)]^{-3/2}\rangle_\Omega.
\]

Across the 300-K positive-gap interval relevant to a 10.6-um photon,

\[
\boxed{m_{hh,DOS}\approx0.531-0.542m_0.}
\]

Directional masses simultaneously span roughly `0.34m0` `[001]` to `0.68m0` `[111]`. Thus directional transport mass and thermodynamic DOS mass are distinct resources.

The realistic DOS branch lies safely above the WP22 restricted bifurcation and supports the `~0.55m0` neutrality result.

## WP24 direct quadratic six-band Kubo audit

Using the same HgCdTe parameterization, an explicit `Gamma6+Gamma8` Kane–Luttinger Hamiltonian with quadratic conduction and cubic valence terms was evaluated with

\[
v_i=(1/\hbar)\partial H/\partial k_i
\]

and the interband Kubo formula.

Critical unit test: turning off the quadratic remote-band terms recovers the exact gapless `12:1` spectral-weight ratio and `13/12` conductivity coefficient to numerical precision.

At 10.6 um, realistic quadratic/warping terms change the zero-temperature target conductivity by only about `2.5–4%` across `Eg=0` to `0.115 eV`.

By contrast, self-consistent intrinsic Pauli blocking reduces the finite-T target spectral weight to roughly

- `0.553` of zero-T at `Eg≈0`;
- `0.450` at `Eg=0.06 eV`;
- `0.389` at `Eg=0.09 eV`;
- `0.344` at `Eg=0.115 eV`.

Therefore

\[
\boxed{\text{carrier statistics / Pauli blocking is the order-unity correction; remote-band optical curvature is only a few-percent correction.}}
\]

This is the current strongest material-layer conclusion.

---

# Current resource hierarchy

The best-supported structure is

\[
\boxed{
\text{finite source task}
+\text{finite-band/localized optical capture}
+\text{absolute microscopic coupling}
+\text{finite apparatus preparation/support/generator resource}
+\text{semiconductor band/DOS/current resources}
+\text{self-consistent carrier occupations/doping}
+\text{optical/electrical geometry and timing statistics}
+\text{thermokinetic/dark resources}
+\text{readout noise/sampling resources}
\Rightarrow\text{finite information-transfer ceiling}
}
\]

under explicit model assumptions.

Recurring failure mode: an omitted resource hides in a rare, canceling, UV, spatially localized, or unobserved sector.

---

# Novelty constraints

Do not claim novelty for generic:

- detector gain/speed or absorption/transit tradeoffs;
- `alpha_abs*v` bandwidth-efficiency products;
- Kane optical conductivity/dielectric function;
- nonparabolic HgCdTe carrier statistics;
- Luttinger/8-band heavy-hole theory;
- Moss–Burstein/Pauli blocking;
- van Roosbroeck–Shockley radiative detailed balance;
- Shockley–Ramo signals;
- transit `0.44/tau` scaling;
- RC bandwidth;
- Zeno/anti-Zeno detector effects;
- squeezing/non-Gaussian metrology;
- optical sum rules/T-operator bounds.

Candidate novelty remains the **photodetection-specific source-information resource-completeness chain**, especially explicit no-go/repair sequences showing why reduced resource sets such as `{Eg,T}`, fixed `mu`, one unspecified effective mass, total optical volume, or conventional `-3 dB` bandwidth do not determine intrinsic information performance.

---

# Highest-priority next work

1. **Explicit eight-band `Gamma7` audit:** add the split-off doublet using a consistent HgCdTe parameter set and repeat the Kubo/neutrality calculation. The split-off energy is ~1 eV, so a modest correction is expected but must be checked.
2. **Doping sensitivity:** solve `n-p=N_D-N_A` over realistic net doping, quantify Moss–Burstein blocking, and map movement of the information optimum. This is an independent resource and likely another no-go against a universal `Eg/kT` optimum.
3. Use one Hamiltonian consistently for DOS, neutrality, and optics where feasible.
4. Only after the equilibrium band/statistics layer is stable, add Auger and SRH mechanisms one at a time.
5. Continue theorem-level novelty audit before publication claims.

---

# Recordkeeping

After every substantive result:

- create/update a dedicated derivation note;
- create a numbered research-log checkpoint when direction changes;
- update this file and `docs/CURRENT_RESEARCH_STATE.md`;
- update relevant GitHub issues;
- preserve failed conjectures and corrections.

Status vocabulary: **PROVED**, **VERIFIED**, **CONJECTURE**, **COUNTEREXAMPLE**, **OPEN**, **BLOCKED**, **REJECTED**.