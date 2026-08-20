# Current Research State

**Date:** 2026-08-19

This file is the first-stop handoff summary for a replacement agent. `AGENTS.md` explicitly tells future agents to read this file first. The repository, not chat history, is authoritative.

---

## Project objective

Determine the physical resources necessary and/or sufficient for a finite-temperature photodetector to transfer information from an incident optical field into an electrical measurement record with specified sensitivity and temporal bandwidth.

A valid endpoint may be a universal bound, a no-go theorem, an explicit counterexample family, or a repaired theorem after identifying a missing resource.

---

# 1. Information metric

Use source-normalized information transfer

\[
\eta_{\mathcal I}=\frac{F_{\rm electrical}}{F_{\rm incident}^{Q}},
\]

for the same encoded optical parameter.

For coherent/Poisson weak photon-flux modulation,

\[
\eta_{\mathcal I}(\omega)
=\Phi_0\frac{|\chi_{Y\Phi}(\omega)|^2}{S_Y(\omega)}.
\]

This is the temporal analogue of DQE and is not itself novel.

Do not use an unweighted all-frequency integral as the universal objective. An ideal continuous-time Poisson counter has `eta_I(omega)=1` for all baseband frequencies in the white point-process model. Use a finite optical information task:

\[
\bar\eta_{\mathcal I}
=\frac{\int(d\omega/2\pi)\mathcal J_{\rm in}(\omega)\eta_{\mathcal I}(\omega)}
{\int(d\omega/2\pi)\mathcal J_{\rm in}(\omega)}.
\]

For a flat baseband task `|Omega| <= Omega_s`, average over that interval.

**Status:** coherent/classical normalization solved; general quantum temporal-mode normalization remains open.

---

# 2. Exact finite-state Markov machinery — SOLVED

For a stationary finite-state Markov jump detector with reduced resolvent

\[
R(\omega)=Q(i\omega I-W)^{-1}Q,
\]

counted-current PSD and input response are

\[
S_I(\omega)=\mathbf1^T\mathcal J^{(2)}\pi
+2\operatorname{Re}[\mathbf1^T\mathcal J^{(1)}R(\omega)\mathcal J^{(1)}\pi],
\]

\[
\chi_{Iu}(\omega)=
\mathbf1^T\mathcal J_u^{(1)}\pi
+\mathbf1^T\mathcal J_0^{(1)}R(\omega)W_u\pi.
\]

These were independently checked against a solvable two-state model.

**Status:** PROVED for finite-state stationary Markov jump detectors. Issue #2 is closed.

---

# 3. Strongest no-go result — WP4

Weak-coupling bosonic optical rates have the standard structure

\[
\Gamma_\uparrow=\gamma(\omega_0)n(\omega_0),
\qquad
\Gamma_\downarrow=\gamma(\omega_0)[n(\omega_0)+1].
\]

Fixed photon energy and reservoir occupation/temperature fix the ratio but not the absolute coupling scale `gamma(omega_0)`.

The reversible family

\[
0\xrightleftharpoons[bR]{aR}1,
\qquad
1\xrightleftharpoons[q]{cR}2,
\qquad
2\xrightleftharpoons[sR]{p}0
\]

can preserve all of the following while `R -> infinity`:

- fixed optical detailed-balance ratio `a/b`;
- fixed photon energy / optical temperature relation;
- finite nonzero optical throughput;
- finite total stationary activity;
- finite total entropy-production rate;
- finite edge-resolved entropy-production rates;
- finite nonzero successful detection probability.

Yet the post-absorption escape rate `(b+c)R` diverges.

Therefore

\[
\boxed{
\{T,\hbar\omega_0,\text{detailed balance},f_*,\mathcal A,\Sigma,\text{edge EPRs},\eta_q\}
\not\Rightarrow
\text{finite detector speed}.
}
\]

An **absolute microscopic light–matter coupling/transition resource is necessary**.

**Status:** PROVED for the reversible finite-state Markov event-detector class.

---

# 4. Restricted internal completion theorem — WP3/WP4

For a reversible optical gateway with reverse optical rate `d`, minimum forward throughput `f_*`, total EPR budget `Sigma`, and activity budget `A`, define

\[
g(z)=\left(1-\frac1z\right)\ln z,
\qquad
Z_*=g^{-1}(\Sigma/f_*).
\]

Then

\[
\pi_1\ge\frac{f_*}{dZ_*},
\qquad
\lambda_1\le\Lambda_*=\frac{\mathcal A d}{f_*}Z_*.
\]

For a proper single-event transducer whose electrical record cannot occur before first exit from the post-absorption gateway,

\[
\eta_{\mathcal I}(\omega)
\le
\eta_q\frac{\Lambda_*^2}{\Lambda_*^2+\omega^2}.
\]

If an independent microscopic bound gives

\[
\gamma(\omega_0)\le\gamma_{\max},
\]

then

\[
d\le\gamma_{\max}[n(\omega_0)+1]
\]

and

\[
\Lambda_{\rm micro}
=
\frac{\mathcal A\gamma_{\max}[n+1]}{f_*}
\,g^{-1}(\Sigma/f_*).
\]

For a flat information task,

\[
\bar\eta_{\rm trans}(\Omega_s)
\le
\eta_q\frac{\Lambda_{\rm micro}}{\Omega_s}
\arctan\frac{\Omega_s}{\Lambda_{\rm micro}}.
\]

**Status:** PROVED for the stated Markov single-gateway event-transducer class.

---

# 5. Incident optical capture theorem — WP5

For coherent-state modulation through a passive frequency-preserving optical frontend, QFI data processing gives

\[
F_{\rm electrical}\le F_{\rm cap}^{Q}
=\int\frac{d\omega}{2\pi}\tau(\omega)\mathcal J_{\rm in}(\omega),
\]

where `tau(omega)` is the fraction of the normalized incident channel delivered into absorptive/capture modes.

For a flat optical sideband-QFI task,

\[
\bar\eta_{\mathcal I}
\le
\frac{1}{2\Omega_s}
\int_{\omega_0-\Omega_s}^{\omega_0+\Omega_s}\tau(\omega)d\omega.
\]

Using Zhang–Monticone–Miller's matrix-valued T-operator oscillator representation and high/low-frequency sum rules, for a fixed incident spatial vector `v` and band `B=[omega_-,omega_+]`:

General passive case:

\[
\int_B\omega\,v^\dagger\operatorname{Im}T(\omega)v\,d\omega
\le
\pi\min\left[
\omega_p^2\|v\|^2,
\omega_+^2v^\dagger T_{0,D}v
\right].
\]

For reciprocal media the right-hand side improves by a factor of 2.

For an electrically small reciprocal detector under nearly uniform illumination,

\[
\boxed{
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
}
\]

**Status:** PROVED under the fixed-spatial-profile passive reciprocal assumptions.

Important rigor correction: do **not** use a blanket scalar macroscopic extinction sum rule for arbitrary scatterers. The arbitrary-scatterer route must go through rigorous matrix-valued scattering/T-operator sum rules. Scalar TRK formulas are restricted to microscopic electric-dipole regimes.

---

# 6. Plane-wave sideband robustness

For a plane-wave carrier, optical sideband spatial profiles obey

\[
v_\Omega(\mathbf r)
=e^{i\Omega\hat{\mathbf k}\cdot\mathbf r/c}v_0(\mathbf r).
\]

For a detector contained within projected radius `R`, the fixed-profile optical bound survives with at most the multiplicative correction

\[
C_{\rm phase}=e^{2\Omega_sR/c}.
\]

Thus the controlling spatial-variation parameter is

\[
\epsilon_{\rm phase}=\Omega_sR/c.
\]

When `Omega_s R / c << 1`, the fixed-spatial-profile theorem is robust. Example: `R=1 mm`, `f_s=1 GHz` gives `C_phase ≈ 1.043`, only about a 4.3% penalty.

This substantially weakens the earlier concern that a separate arbitrary channel-rank resource is always dominant for ordinary plane-wave photodetection. Such a resource remains relevant for genuinely multi-spatial-mode or strongly frequency-dependent illumination.

**Status:** PROVED/derived under the stated plane-wave finite-footprint assumptions.

---

# 7. Restricted composite UPRP theorem — WP6

For the intersection of:

- coherent optical modulation;
- passive reciprocal optical frontend;
- finite T-operator high/low-frequency resources;
- controlled plane-wave sideband spatial variation;
- WP3 single-event Markov transducer assumptions;

we have

\[
\boxed{
\bar\eta_{\mathcal I}(\Omega_s)
\le
\min\left[
B_{\rm opt}(\Omega_s),
B_{\rm trans}(\Omega_s)
\right].
}
\]

The optical ceiling can be written

\[
B_{\rm opt}
=
\min\left[
1,
\frac{\pi V}{4cA\Omega_s}
 e^{2\Omega_sR/c}
\min\left(
\omega_p^2,
(\omega_0+\Omega_s)^2t_0
\right)
\right],
\]

and the internal transduction ceiling is

\[
B_{\rm trans}
=
\eta_q
\frac{\Lambda_{\rm micro}}{\Omega_s}
\arctan\frac{\Omega_s}{\Lambda_{\rm micro}}.
\]

In the narrow-sideband/small-footprint regime,

\[
\Omega_s\ll\omega_0,
\qquad
\Omega_sR/c\ll1,
\]

define

\[
\Omega_{\rm EM}
=\frac{\pi V}{4cA}
\min(\omega_p^2,\omega_0^2t_0).
\]

A necessary condition for target information fraction `r` is approximately

\[
\boxed{
\Omega_s
\lesssim
\min\left[
\frac{\Omega_{\rm EM}}{r},
\;x(r/\eta_q)\Lambda_{\rm micro}
\right],
}
\]

where `x(q)` is the positive solution of

\[
\arctan x/x=q.
\]

For `eta_q=1`, useful reference values are

- `x(0.90)=0.60253`;
- `x(0.95)=0.40565`;
- `x(0.99)=0.17478`.

**Status:** PROVED as a restricted classical/semiclassical composite theorem. It is not yet a universal quantum theorem.

Primary derivation: `notes/WP6_RESTRICTED_COMPOSITE_THEOREM.md`.

---

# 8. Quantum extension: current best route

The Nishiyama–Hasegawa temporal-Fisher quantum speed limit is relevant but cannot simply replace `gamma_max` because its distance is unitarily residual and removes purely local/unitary rotations. A photodetector can potentially encode useful information through coherent detector pointer rotation before irreversible localization.

A direct subsystem distinguishability-transfer route avoids that loophole.

For two incident optical hypotheses with initial trace distance

\[
D_{\rm in}=\frac12\|\rho_F^{(0)}-\rho_F^{(1)}\|_1,
\]

and corresponding reduced detector states with trace distance `D_det(t)`, move to an interaction picture that removes field-only and detector-only Hamiltonians. Using partial-trace contractivity and

\[
\|[H,X]\|_1\le2\|H\|_\infty\|X\|_1,
\]

one obtains the candidate lemma

\[
\boxed{
D_{\rm det}(t)
\le
\frac{2D_{\rm in}}{\hbar}
\int_0^t g_{\rm int}(s)ds,
}
\]

where a decomposition-independent interaction strength is

\[
\boxed{
g_{\rm int}
=
\inf_{A_F,B_D}
\|H-A_F\otimes I_D-I_F\otimes B_D\|_\infty.
}
\]

If `g_int(t) <= E_int`, then transferring a fraction `r` of incident distinguishability requires

\[
t\ge r\hbar/(2E_{\rm int}).
\]

This route retains coherent pointer rotations and is therefore better matched to photodetection than a unitarily residual state-speed metric.

**Status:** DERIVED CANDIDATE LEMMA; theorem-level novelty comparison and conversion to QFI/continuous temporal modulation remain OPEN. Do not claim novelty yet.

---

# 9. Critical novelty constraints

Do not claim novelty for any of the following:

- generic photodetector sensitivity-speed or gain-bandwidth tradeoffs;
- general quantum photodetector frameworks/coherence-backaction tradeoffs — Young, Sarovar, Léonard;
- generic thermodynamic precision bounds — Hasegawa and successors;
- detector performance versus dissipation — Schwarzhans et al.;
- finite-frequency response/noise inequalities — Dechant, Liu/Gu, Zheng/Lu;
- LDOS or optical power-bandwidth limits — Shim et al. and related work;
- general T-operator sum rules — Zhang, Monticone, Miller;
- information theory + Maxwell-constrained structured photonic channels — Amaolo et al.

Amaolo et al. are especially close on the optical side but their published formulation is single-frequency; finite-band spectral-sum-rule/macroscopic-QED extensions remain a key comparison point.

Current candidate novelty is specifically the **finite-band incident optical information -> physical capture -> finite-temperature electrical transducer no-go/completion structure**, including proof that stationary thermodynamic resources do not set an absolute speed without a microscopic coupling scale.

Novelty remains provisional until the quantum and theorem-level citation audit is closed.

---

# 10. Exact next actions

1. **Quantum lemma audit:** compare the subsystem trace-distance transfer inequality against known distinguishability-transfer, entangling-rate, Lieb–Robinson, and interaction-norm quantum speed-limit literature.
2. **QFI conversion:** derive a version directly controlling Fisher/QFI transfer for weak continuous optical modulation rather than binary trace-distance hypotheses.
3. **Microscopic closure:** determine whether `g_int` / `gamma_max` can be bounded from the same matter + electromagnetic resources (`omega_p`, static response, footprint/volume, passive T-operator constraints) without circularly inserting detector bandwidth.
4. **General optical modes:** extend coherent-state displacement encoding to nonclassical optical temporal modes.
5. **Stress tests:** high-Q, vanishing mode volume, slow light, plasmonic near-contact, parallel detector replication, active/gain media, strong/ultrastrong coupling, non-Markovianity, and direct-feedthrough architectures.
6. **Publication gate:** only after the above, decide whether the strongest paper is a no-go theorem, restricted completion theorem, or combined no-go + completion result.

---

# 11. Files a replacement agent should read next

1. `AGENTS.md`
2. `docs/CURRENT_RESEARCH_STATE.md` — this file
3. `notes/RESEARCH_LOG_ROUND4.md`
4. `notes/WP6_RESTRICTED_COMPOSITE_THEOREM.md`
5. `notes/WP5_PLANE_WAVE_PHASE_ROBUSTNESS.md`
6. `notes/WP5_T_OPERATOR_FINITE_BAND_CAPTURE.md`
7. `notes/WP5_INCIDENT_CHANNEL_QFI_SUM_RULE.md`
8. `notes/WP4_MICROSCOPIC_OPTICAL_COUPLING_NO_GO.md`
9. `notes/WP3_GATEWAY_RESOURCE_THEOREM.md`
10. `docs/NOVELTY_AUDIT_ROUND2.md`
11. `docs/LITERATURE_MAP.md`

Older WP0/WP1/WP2 notes preserve the derivation history, failed conjectures, and counterexamples and should be read if theorem assumptions are being modified.
