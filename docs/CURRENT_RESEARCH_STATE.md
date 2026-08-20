# Current Research State

**Date:** 2026-08-20

This is the first-stop handoff summary. The repository, not chat history, is authoritative. Read `AGENTS.md`, `notes/RESEARCH_LOG_ROUND5.md`, and the dedicated notes cited below before new work.

---

# 1. Project objective

Determine the physical resources necessary and/or sufficient for a finite-temperature photodetector to transfer information from an incident optical field into an electrical measurement record with specified sensitivity and temporal bandwidth.

The project now contains:

- classical/Markov no-go theorems;
- restricted thermokinetic completion theorems;
- finite-band electromagnetic capture bounds;
- fully quantum finite-hypothesis transfer bounds;
- coherent-state SLD-QFI transfer theorems;
- finite-temperature apparatus-preparation bounds;
- explicit non-Gaussian counterexamples and asymptotic optima;
- a finite-band quantum spectral-composition theorem.

Do **not** assume a simple sensitivity-bandwidth-temperature product exists.

---

# 2. Information metric

Use source-normalized information transfer

\[
\eta_{\mathcal I}
=F_{\rm electrical}/F_{\rm incident}^{Q}
\]

for the same encoded parameter.

For coherent/Poisson weak photon-flux modulation,

\[
\eta_{\mathcal I}(\omega)
=\Phi_0\frac{|\chi_{Y\Phi}(\omega)|^2}{S_Y(\omega)}.
\]

Use a finite optical information task

\[
\bar\eta_{\mathcal I}
=\frac{\int(d\omega/2\pi)\mathcal J_{\rm in}(\omega)\eta_{\mathcal I}(\omega)}
{\int(d\omega/2\pi)\mathcal J_{\rm in}(\omega)},
\]

not an unweighted all-frequency integral.

---

# 3. Classical/Markov foundation

For stationary finite-state Markov jump detectors, exact response/noise formulas are solved:

\[
S_I(\omega)=\mathbf1^T\mathcal J^{(2)}\pi
+2\operatorname{Re}[\mathbf1^T\mathcal J^{(1)}R(\omega)\mathcal J^{(1)}\pi],
\]

\[
\chi_{Iu}(\omega)=\mathbf1^T\mathcal J_u^{(1)}\pi
+\mathbf1^T\mathcal J_0^{(1)}R(\omega)W_u\pi.
\]

**Status:** PROVED. Issue #2 closed.

Strongest Markov no-go theorem: fixed photon energy/temperature ratio, fixed optical detailed balance, finite nonzero throughput, finite total activity, finite total and edge EPR, and finite nonzero detection probability do **not** bound detector speed if an absolute microscopic coupling/rate scale may diverge.

\[
\boxed{
\{T,\hbar\omega_0,\text{detailed balance},f_*,\mathcal A,\Sigma,\text{edge EPRs},\eta_q\}
\not\Rightarrow\text{finite speed}.
}
\]

Primary note: `notes/WP4_MICROSCOPIC_OPTICAL_COUPLING_NO_GO.md`.

---

# 4. Restricted thermokinetic event-detector theorem

For a reversible optical gateway with minimum throughput `f_*`, EPR budget `Sigma`, activity budget `A`, and fixed reverse optical rate `d`, define

\[
g(z)=(1-z^{-1})\ln z,
\qquad
Z_*=g^{-1}(\Sigma/f_*).
\]

Then

\[
\pi_1\ge f_*/(dZ_*),
\qquad
\lambda_1\le\Lambda_*=(\mathcal A d/f_*)Z_*.
\]

For the proper single-event class,

\[
\eta_{\mathcal I}(\omega)
\le
\eta_q\frac{\Lambda_*^2}{\Lambda_*^2+\omega^2}.
\]

**Status:** PROVED under the stated event-transducer assumptions.

Primary note: `notes/WP3_GATEWAY_RESOURCE_THEOREM.md`.

---

# 5. Passive finite-band electromagnetic capture — WP5

For coherent-state modulation through a passive frequency-preserving frontend,

\[
F_{\rm electrical}
\le
\int\frac{d\omega}{2\pi}\tau(\omega)\mathcal J_{\rm in}(\omega).
\]

Rigorous matrix-valued T-operator sum rules yield, for an electrically small reciprocal detector under nearly uniform illumination,

\[
\bar\eta_{\mathcal I}(\Omega_s)
\le
\min\left[
1,
\frac{\pi}{4cA\Omega_s}
\min\left(
\omega_p^2V,
(\omega_0+\Omega_s)^2\alpha_{\rm stat}
\right)
\right].
\]

Plane-wave sideband spatial variation over radius `R` costs at most

\[
C_{\rm phase}=e^{2\Omega_sR/c}.
\]

Primary notes:
- `notes/WP5_T_OPERATOR_FINITE_BAND_CAPTURE.md`
- `notes/WP5_PLANE_WAVE_PHASE_ROBUSTNESS.md`

---

# 6. Fully quantum finite-hypothesis theorem — WP7/QH

For two optical hypotheses initially tensor the same apparatus state, define the nonlocal interaction seminorm

\[
g_{\rm int}(t)=\inf_{A_F,B_D}\|H-A_F\otimes I-I\otimes B_D\|_\infty,
\]

\[
G(t)=\hbar^{-1}\int_0^t g_{\rm int}(s)ds.
\]

Then

\[
\boxed{
D_{\rm elec}(t)/D_{\rm in}\le\min\{1,2G(t)\}.
}
\]

**Status:** PROVED for finite-hypothesis/Helstrom information under the dilation assumptions.

A trine-POVM counterexample proves trace-distance contraction cannot be differentiated into a universal SLD-QFI contraction theorem.

Primary note: `notes/WP7_QUANTUM_DISTINGUISHABILITY_TRANSFER.md`.

---

# 7. Coherent-state SLD-QFI interaction theorem

For passive number-conserving bosonic coupling with single-particle cross block `V(t)`, define

\[
\Gamma=\int_0^t\|V(s)\|_2ds.
\]

Then source-to-detector transfer probability obeys

\[
\tau\le\sin^2(\min\{\Gamma,\pi/2\}).
\]

Cross-coupling action alone is **not** enough: an arbitrarily pre-squeezed pointer can transfer nearly all coherent-state QFI at arbitrarily weak nonzero coupling. Thus initial apparatus metrological resource is necessary.

---

# 8. Directional SLD-Stam theorem and globally tight energy repair

For one output of a passive beam splitter,

\[
\boxed{
\frac1{J_C}
\ge
\frac\lambda{J_A}
+\frac{1-\lambda}{J_B}.
}
\]

This is derived directly for SLD/Bures QFI from data processing, product additivity, and displacement covariance.

For coherent input (`J_A=2`) and arbitrary detector pointer with total excitation `N`, define

\[
\xi(N)=(\sqrt{N+1}-\sqrt N)^2.
\]

Then

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac\tau{\tau+(1-\tau)\xi(N)}
}
\]

and

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac{\sin^2\Gamma}
{\sin^2\Gamma+\cos^2\Gamma\,\xi(N)}.
}
\]

A squeezed-vacuum pointer plus beam splitter and homodyne saturates the theorem.

**Status:** PROVED and globally tight under the passive-linear single-collective-mode model.

Primary note: `notes/WP8_SLD_STAM_GLOBAL_ENERGY_THEOREM.md`.

---

# 9. Finite-temperature free-energy apparatus resource — WP8

Let

\[
\vartheta=\beta\hbar\omega_D,
\qquad
D_0=\beta\Delta F=D(\rho_D\Vert\tau_\vartheta).
\]

## 9.1 Global arbitrary-state upper bound

Entropy maximization at fixed mean excitation gives

\[
D_0\ge
\vartheta N-g(N)-\ln(1-e^{-\vartheta}).
\]

Let `N_+(D0,vartheta)` be the largest equality root. Then every pointer obeys

\[
\boxed{
J_D\le\frac2{\xi(N_+)}
}
\]

and therefore

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac\tau{\tau+(1-\tau)\xi(N_+)}.
}
\]

Finite nonequilibrium free energy is therefore sufficient to close the hidden preloaded-pointer loophole.

Primary note: `notes/WP8_GLOBAL_FREE_ENERGY_UPPER_BOUND.md`.

## 9.2 Gaussian global optimality is false

At

\[
\vartheta=\ln2,
\qquad
D_0=\ln(3/2),
\]

the even-conditioned thermal state

\[
\rho_e=\sum_{k\ge0}\frac34 4^{-k}|2k\rangle\langle2k|
\]

has exactly

\[
J_X=14/3,
\qquad
\langle N\rangle=2/3.
\]

The Gaussian free-energy theorem proves every Gaussian pointer at the same budget has `J_X<3.783`.

**Status:** analytic COUNTEREXAMPLE / PROVED.

Primary note: `notes/WP8_NON_GAUSSIAN_PARITY_COUNTEREXAMPLE.md`.

## 9.3 Exact parity-sector frontier

For any even-supported state,

\[
J_X(\rho)=4\operatorname{Tr}(\rho P^2).
\]

The exact free-energy optimizer in that sector is

\[
\rho_s\propto\Pi_e e^{\log\tau+sP^2}\Pi_e.
\]

With

\[
\mu=\sqrt{\vartheta(\vartheta-2s)},
\]

\[
Z_e=(1-e^{-\vartheta})
\frac{e^{(\vartheta-\mu)/2}}{1-e^{-2\mu}},
\]

\[
m=\frac{\vartheta}{\mu}
\left[\frac12+\frac{2}{e^{2\mu}-1}\right],
\]

\[
J_e=4m,
\qquad
D_e=s m-\ln Z_e.
\]

This is the exact optimum over all even-supported states.

At large free energy,

\[
J_e^{\rm opt}
=\frac{8D_0}{\vartheta}+O(\ln D_0).
\]

The global upper bound has the same leading asymptotic term, so the parity-sector family is asymptotically globally optimal to relative error tending to zero.

Primary note: `notes/WP8_EXACT_PARITY_SECTOR_FRONTIER.md`.

## 9.4 Gaussian states are locally optimal near equilibrium

At `D0 -> 0`, the QFI first variation at the thermal state is generated by a quadratic operator and the relative-entropy Hessian is the BKM metric. The steepest-ascent exponential tilt is therefore Gaussian.

Thus squeezed-thermal Gaussian pointers are globally optimal to leading order near equilibrium, while the finite-budget parity state later beats every Gaussian.

A **Gaussian-to-non-Gaussian resource crossover** is therefore proved for the explicit temperature example.

Primary note: `notes/WP8_LOCAL_GAUSSIAN_OPTIMALITY.md`.

---

# 10. Exact equilibrium thermal-pointer theorem

With no nonequilibrium apparatus preparation,

\[
J_\beta
=2t_\beta,
\qquad
t_\beta=\tanh(\beta\hbar\omega_D/2).
\]

The exact passive-linear optimum is

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
=
\frac{\tau t_\beta}
{1-\tau+\tau t_\beta}
}
\]

and with `tau<=sin^2 Gamma`,

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac{t_\beta\sin^2\Gamma}
{\cos^2\Gamma+t_\beta\sin^2\Gamma}.
}
\]

This is a literal temperature–interaction-action–information theorem for the restricted equilibrium pointer class.

Primary note: `notes/WP8_EXACT_THERMAL_POINTER_THEOREM.md`.

---

# 11. Finite-band quantum spectral composition — WP9

Let WP5 give

\[
\bar\tau\le B_{\rm opt}(\Omega_s)
\]

and WP7 give

\[
\tau(\omega)\le\tau_{\max}=\sin^2\Gamma_{\max}.
\]

For a frequency-independent pointer QFI cap `J_D`, define

\[
f_J(\tau)=\frac{\tau J_D}{2(1-\tau)+\tau J_D}.
\]

Its curvature changes sign exactly at `J_D=2`.

For `J_D>=2` (resourceful pointer, concave),

\[
\boxed{
\bar\eta
\le
f_J(\min\{B_{\rm opt},\tau_{\max}\}).
}
\]

Uniform spectral coupling is optimal under the scalar constraints.

For `J_D<=2` (thermal/noisy pointer, convex),

\[
\boxed{
\bar\eta
\le
f_J(\tau_{\max})
\min\{1,B_{\rm opt}/\tau_{\max}\}.
}
\]

Bang-bang spectral concentration is optimal.

For an equilibrium thermal pointer and the WP5 narrow-band `B_opt<=Omega_EM/Omega_s` regime,

\[
\boxed{
\Omega_s
\le
\frac{\Omega_{\rm EM}}{q}
\frac{t_\beta}
{1-\tau_{\max}+\tau_{\max}t_\beta}
}
\]

is necessary to retain average information fraction `q` when the EM resource is limiting.

Primary note: `notes/WP9_FINITE_BAND_QUANTUM_SPECTRAL_COMPOSITION.md`.

Issue #9 tracks the shared multimode/free-energy extension.

---

# 12. Novelty constraints

Do **not** claim novelty for:

- generic photodetector sensitivity-speed/gain-bandwidth tradeoffs;
- general quantum photodetector frameworks;
- generic thermodynamic or kinetic precision bounds;
- finite-frequency response/noise inequalities;
- squeezing-enhanced metrology;
- generic non-Gaussian displacement sensing;
- sparse/`N`-spaced Fock-support sensing states;
- optical LDOS/power-bandwidth limits;
- T-operator sum rules;
- Maxwell-constrained communication capacity.

Important adjacent results include:

- Young–Sarovar–Léonard quantum photodetector limits/frameworks;
- Hasegawa and later thermodynamic/kinetic uncertainty relations;
- Schwarzhans et al. detector thermodynamics;
- Dechant/Liu-Gu/Zheng-Lu finite-frequency response bounds;
- Shim et al. finite-band optical response limits;
- Zhang–Monticone–Miller T-operator sum rules;
- Amaolo et al. Maxwell-constrained Shannon capacity;
- Grochowski & Filip (PRL 135, 230802, 2025) `N`-spaced non-Gaussian force-sensing states;
- Marvian (PRL 129, 190502, 2022) thermodynamic operational interpretation of QFI/coherence cost.

Current candidate novelty is the **photodetection-specific resource-completeness structure**: explicit no-go counterexamples identifying missing microscopic and apparatus resources, followed by finite-band completion theorems when those resources are supplied.

---

# 13. Current sharp open problems

1. Exact finite-budget arbitrary-state pointer frontier

\[
J_F^{\max}(D_0,\vartheta)
=\sup_{\rho:D(\rho\Vert\tau_\vartheta)\le D_0}J_X(\rho).
\]

Known regimes:
- small `D0`: Gaussian optimal to leading order;
- finite `D0`: non-Gaussian parity beats Gaussian;
- large `D0`: exact even-parity exponential family asymptotically globally optimal;
- all `D0`: rigorous global upper bound.

Next route: two-parity interpolation or tight dual variational solution.

2. WP9 shared spectral preparation budget: replace a per-frequency `J_D` cap by one total free-energy budget across frequency modes and solve the joint spectral allocation.

3. Multimode scattering/channel rank: extend scalar singular-channel composition to multiple spatial channels without hiding footprint resources.

4. Active gain: explicitly count pump/free-energy resource and added quantum noise.

5. Final novelty/publication gate: decide whether the strongest paper should emphasize the Markov missing-coupling theorem, the quantum apparatus free-energy crossover, the finite-band composition, or a unified no-go + completion structure.
