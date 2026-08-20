# Current Research State

**Date:** 2026-08-19

This is the first-stop handoff summary. The repository, not chat history, is authoritative. Read `AGENTS.md` and the dedicated notes cited below for full derivations.

---

# 1. Project objective

Determine the physical resources necessary and/or sufficient for a finite-temperature photodetector to transfer information from an incident optical field into an electrical measurement record with specified sensitivity and temporal bandwidth.

The project now has both no-go and positive restricted results. A simple sensitivity-bandwidth-temperature product is not assumed to exist.

---

# 2. Information metric

Use

\[
\eta_{\mathcal I}=F_{\rm electrical}/F_{\rm incident}^{Q}
\]

for the same encoded optical parameter.

For coherent/Poisson weak photon-flux modulation,

\[
\eta_{\mathcal I}(\omega)
=\Phi_0\frac{|\chi_{Y\Phi}(\omega)|^2}{S_Y(\omega)}.
\]

Use a finite source information task,

\[
\bar\eta_{\mathcal I}
=\frac{\int(d\omega/2\pi)\mathcal J_{\rm in}(\omega)\eta_{\mathcal I}(\omega)}
{\int(d\omega/2\pi)\mathcal J_{\rm in}(\omega)},
\]

not an unweighted all-frequency integral.

---

# 3. Finite-state Markov machinery — SOLVED

For stationary finite-state Markov jump detectors,

\[
S_I(\omega)=\mathbf1^T\mathcal J^{(2)}\pi
+2\operatorname{Re}[\mathbf1^T\mathcal J^{(1)}R(\omega)\mathcal J^{(1)}\pi],
\]

\[
\chi_{Iu}(\omega)=\mathbf1^T\mathcal J_u^{(1)}\pi
+\mathbf1^T\mathcal J_0^{(1)}R(\omega)W_u\pi.
\]

**Status:** PROVED for finite-state stationary Markov jump detectors. Issue #2 closed.

---

# 4. Strongest classical no-go theorem — WP4

A reversible three-state family preserves fixed optical detailed balance, photon energy/temperature ratio, finite nonzero optical throughput, finite total activity, finite total and edge-resolved EPR, and finite nonzero detection probability while an absolute optical/internal rate scale diverges.

Therefore

\[
\boxed{
\{T,\hbar\omega_0,\text{detailed balance},f_*,\mathcal A,\Sigma,\text{edge EPRs},\eta_q\}
\not\Rightarrow\text{finite detector speed}.
}
\]

An **absolute microscopic coupling/transition resource is necessary**.

Primary note: `notes/WP4_MICROSCOPIC_OPTICAL_COUPLING_NO_GO.md`.

---

# 5. Restricted internal completion theorem — WP3

For a reversible optical gateway, minimum throughput `f_*`, EPR budget `Sigma`, activity budget `A`, and fixed reverse optical rate `d`, define

\[
g(z)=\left(1-\frac1z\right)\ln z,
\qquad Z_*=g^{-1}(\Sigma/f_*).
\]

Then

\[
\pi_1\ge f_*/(dZ_*),
\qquad
\lambda_1\le\Lambda_*=(\mathcal A d/f_*)Z_*.
\]

For the proper single-event detector class,

\[
\eta_{\mathcal I}(\omega)
\le\eta_q\frac{\Lambda_*^2}{\Lambda_*^2+\omega^2}.
\]

If `gamma(omega_0)<=gamma_max`, then `d<=gamma_max[n+1]` and the theorem has an explicit microscopic coupling cap.

Primary note: `notes/WP3_GATEWAY_RESOURCE_THEOREM.md`.

---

# 6. Passive finite-band optical capture — WP5

For coherent-state modulation through a passive frequency-preserving optical frontend,

\[
F_{\rm electrical}\le
\int\frac{d\omega}{2\pi}\tau(\omega)\mathcal J_{\rm in}(\omega).
\]

Using rigorous matrix-valued T-operator oscillator/sum-rule bounds, an electrically small reciprocal detector under nearly uniform illumination obeys

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

Plane-wave sideband variation over projected radius `R` costs at most

\[
C_{\rm phase}=e^{2\Omega_sR/c}.
\]

Primary notes:
- `notes/WP5_T_OPERATOR_FINITE_BAND_CAPTURE.md`
- `notes/WP5_PLANE_WAVE_PHASE_ROBUSTNESS.md`

---

# 7. Restricted composite theorem — WP6

For coherent modulation, passive reciprocal finite-band optical capture, controlled finite-footprint phase variation, and the WP3 event-transducer assumptions,

\[
\boxed{
\bar\eta_{\mathcal I}(\Omega_s)
\le\min[B_{\rm opt}(\Omega_s),B_{\rm trans}(\Omega_s)].
}
\]

This is a valid restricted classical/semiclassical optical+thermokinetic theorem, not a universal quantum theorem.

Primary note: `notes/WP6_RESTRICTED_COMPOSITE_THEOREM.md`.

---

# 8. Fully quantum finite-hypothesis theorem — WP7/QH

Partition the closed dilation into optical signal `F` and complete apparatus `D`, initially with the same apparatus state under both optical hypotheses.

Define

\[
g_{\rm int}(t)=\inf_{A_F,B_D}\|H-A_F\otimes I-I\otimes B_D\|_\infty,
\]

\[
G(t)=\hbar^{-1}\int_0^t g_{\rm int}(s)ds.
\]

Then the transferred trace distinguishability satisfies

\[
\boxed{
D_{\rm elec}(t)/D_{\rm in}\le\min\{1,2G(t)\}.
}
\]

If `g_int<=E_int`, transferring fraction `r` of the available binary distinguishability requires

\[
t\ge r\hbar/(2E_{\rm int}).
\]

**Status:** PROVED under the initial product/same-apparatus-state and unitary-dilation assumptions.

Primary note: `notes/WP7_QUANTUM_DISTINGUISHABILITY_TRANSFER.md`.

---

# 9. Exact obstruction: QFI is a separate quantum problem

A qubit trine POVM gives

\[
\eta_{\rm Tr}=2/3
\]

but, for near-pure equatorial phase families,

\[
F_{\rm out}/F_{\rm in}=1/(2-s)\to1.
\]

Hence

\[
\boxed{\eta_{\rm SLD}=1\quad\text{while}\quad\eta_{\rm Tr}=2/3.}
\]

The trace-distance theorem cannot simply be differentiated into an SLD/QFI theorem.

**Status:** PROVED analytic counterexample.

---

# 10. Coherent-state/passive-linear QFI theorem

For coherent optical displacement encoding coupled to detector bosonic modes through a passive number-conserving quadratic Hamiltonian with single-particle cross block `V(t)`, define

\[
\Gamma(t)=\int_0^t\|V(s)\|_2ds.
\]

The optical-to-detector single-particle transfer probability obeys

\[
\|U_{DF}\|_2^2
\le\sin^2(\min\{\Gamma,\pi/2\}).
\]

If detector modes initially occupy fixed coherent states, then

\[
\boxed{
F_{\rm elec}/F_{\rm in}
\le\sin^2(\min\{\Gamma,\pi/2\}).
}
\]

For a two-mode beam splitter this is saturated.

Primary note: `notes/WP7_COHERENT_GAUSSIAN_QFI_TRANSFER.md`.

---

# 11. Stronger quantum no-go: preloaded pointer squeezing

The coherent/vacuum theorem is not universal. For a coherent optical x-displacement coupled by beam-splitter angle `phi` to an x-squeezed detector pointer,

\[
\boxed{
F_{\rm elec}/F_{\rm in}
=
\frac{\sin^2\phi}
{\sin^2\phi+\cos^2\phi e^{-2r}}.
}
\]

For every nonzero `phi`, this tends to 1 as the detector squeezing `r->infinity`.

Therefore

\[
\boxed{
\text{cross-coupling action alone does not bound coherent-state QFI transfer}
}
\]

if arbitrary pre-existing apparatus squeezing/metrological energy is allowed.

Maintaining fixed transfer fraction `q` at weak coupling requires detector energy

\[
N_D\sim\frac{q}{4(1-q)\phi^2}.
\]

This identifies **initial apparatus metrological resource/noise** as another necessary quantum resource.

---

# 12. Tight energy-repaired Gaussian theorem

For the one-signal-mode / one-effective-detector-mode Gaussian class, constrain the detector's initial mean excitation by

\[
N_D\le N.
\]

Define

\[
\boxed{
\xi(N)=(\sqrt{N+1}-\sqrt N)^2.
}
\]

This is the minimum detector quadrature-noise factor allowed by the Gaussian energy budget.

At transfer probability `tau`,

\[
\boxed{
F_{\rm elec}/F_{\rm in}
\le
\frac{\tau}{\tau+(1-\tau)\xi(N)}.
}
\]

Using `tau<=sin^2 Gamma`, for `0<=Gamma<=pi/2`,

\[
\boxed{
F_{\rm elec}/F_{\rm in}
\le
\frac{\sin^2\Gamma}
{\sin^2\Gamma+\cos^2\Gamma\,\xi(N)}.
}
\]

The theorem is tight: equality is attained by a pure squeezed-vacuum pointer aligned to the signal quadrature, beam-splitter coupling, and aligned homodyne readout.

To transfer fraction `q`, necessarily

\[
\boxed{
\Gamma\ge
\arctan\sqrt{\frac{q\xi(N)}{1-q}}.
}
\]

For `N=0`, this reduces to `Gamma>=arcsin sqrt(q)`. For large `N`, `xi(N)~1/(4N)` and the minimum action scales as `N^{-1/2}`.

Primary note: `notes/WP7_ENERGY_REPAIRED_GAUSSIAN_THEOREM.md`.

**Status:** PROVED and saturable for the stated single-effective-mode Gaussian class.

---

# 13. Current resource hierarchy

The emerging complete resource logic is

\[
\boxed{
\text{source temporal/information task}
+
\text{finite-band electromagnetic capture resources}
+
\text{absolute microscopic cross-coupling}
+
\text{initial apparatus metrological energy/noise}
+
\text{internal thermokinetic resources}
\Longrightarrow
\text{information-transfer bandwidth ceiling}.
}
\]

WP4 shows why the microscopic coupling is necessary. WP7 shows why a quantum apparatus-preparation resource is additionally necessary.

---

# 14. Novelty constraints

Do not claim novelty for generic photodetector tradeoffs, squeezing-enhanced metrology, Gaussian QFI, quantum speed limits, contraction coefficients, thermodynamic uncertainty relations, optical power-bandwidth limits, T-operator sum rules, or Maxwell-constrained information capacity.

Current candidate novelty remains the **photodetection-specific resource-completeness/no-go/completion structure**, especially the sequence of explicit counterexamples showing which physically hidden resources must be added before a finite information-speed theorem becomes possible.

---

# 15. Exact next actions

1. Generalize the energy-repaired Gaussian theorem to arbitrary multimode Gaussian detector apparatus with total energy budget and arbitrary passive local processing.
2. Determine whether all optimal apparatus energy can always be concentrated into the single coupled collective squeezed quadrature; if yes, the same `xi(N_total)` bound survives.
3. Relate initial apparatus energy/squeezing to a finite-temperature preparation free-energy or ergotropy resource.
4. Compose the WP7 Gaussian bound with WP5 finite-band EM capture and WP3/WP4 thermokinetic conversion where assumptions overlap.
5. Stress-test active Gaussian amplification: any pump energy and added quantum noise must be included explicitly.
6. Continue theorem-level novelty audit, including 2026 weak-coupling ancilla and squeezed-readout metrology.
