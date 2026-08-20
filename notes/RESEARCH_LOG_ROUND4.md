# Research Log — Round 4

**Date:** 2026-08-19

This file records the major results obtained after the older chronological `notes/RESEARCH_LOG.md` became stale. It is intentionally redundant with the dedicated WP notes so a replacement agent can recover context quickly.

---

## 1. Research direction changed from generic thermodynamic bound to missing-coupling theorem

A stronger reversible three-state family was constructed that preserves fixed optical detailed balance while allowing an absolute optical coupling scale to diverge:

\[
0\xrightleftharpoons[bR]{aR}1,
\qquad
1\xrightleftharpoons[q]{cR}2,
\qquad
2\xrightleftharpoons[sR]{p}0.
\]

The optical ratio `a/b` is fixed. Stationary ready/gateway occupations scale as `O(1/R)` while the dominant state tends to unit occupation. Every `O(R)` rate therefore acts on an `O(1/R)` occupation.

As `R -> infinity`:

- optical detailed-balance ratio stays fixed;
- optical throughput stays finite and nonzero;
- total stationary activity stays finite;
- each edge entropy-production contribution stays finite;
- total EPR stays finite;
- successful detection probability can remain finite;
- post-absorption escape rate `(b+c)R` diverges.

Therefore fixed temperature, photon energy, detailed-balance ratios, throughput, stationary activity, total EPR, edge EPR, and low-frequency efficiency do not determine an absolute detector speed.

**Status:** PROVED for the reversible finite-state Markov event-detector class.

Primary note: `notes/WP4_MICROSCOPIC_OPTICAL_COUPLING_NO_GO.md`.

---

## 2. Microscopic interpretation of the missing resource

For a weak-coupling bosonic optical reservoir,

\[
\Gamma_\uparrow=\gamma(\omega_0)n(\omega_0),
\qquad
\Gamma_\downarrow=\gamma(\omega_0)[n(\omega_0)+1].
\]

Temperature/photon energy fix the ratio but not the spectral coupling scale `gamma(omega_0)`.

Thus the classical gateway rate `d` in WP3 is not fundamentally fixed by thermodynamics. It must be supplied or bounded by an independent microscopic light–matter coupling resource.

Young–Sarovar–Léonard's dark-state detector contains the same qualitative escape hatch: optical coupling and localization can be taken arbitrarily fast relative to the incident-wavepacket timescale in the idealized model.

**Status:** VERIFIED physical interpretation; novelty of the no-go/completion composition remains under audit.

---

## 3. Restricted internal completion theorem retained

For fixed reverse optical rate `d`, minimum useful forward throughput `f_*`, activity budget `A`, and EPR budget `Sigma`, define

\[
g(z)=\left(1-\frac1z\right)\ln z,
\qquad
Z_*=g^{-1}(\Sigma/f_*).
\]

Then

\[
\pi_1\ge f_*/(dZ_*),
\]

\[
\lambda_1\le(\mathcal A d/f_*)Z_*.
\]

For a proper single-event transducer whose electrical record cannot precede first exit from the gateway,

\[
\eta_{\mathcal I}(\omega)
\le
\eta_q\frac{\lambda_1^2}{\lambda_1^2+\omega^2}.
\]

If `gamma <= gamma_max`, then `d <= gamma_max[n+1]`, giving a finite microscopic conditional speed/resource bound.

**Status:** PROVED under the stated Markov event-transducer assumptions.

Primary note: `notes/WP3_GATEWAY_RESOURCE_THEOREM.md`.

---

## 4. Incident optical QFI capture lemma

For coherent-state modulation through a passive frequency-preserving linear frontend,

\[
F_{\rm electrical}\le F_{\rm cap}^{Q}
=\int\frac{d\omega}{2\pi}\tau(\omega)\mathcal J_{\rm in}(\omega),
\]

where `tau(omega)` is the incident-channel capture/absorption fraction.

Thus for a flat sideband-QFI task,

\[
\bar\eta_{\mathcal I}
\le
\frac{1}{2\Omega_s}
\int_{\omega_0-\Omega_s}^{\omega_0+\Omega_s}\tau(\omega)d\omega.
\]

This is a direct data-processing statement and gives the correct bridge between photonic capture and electrical information.

**Status:** PROVED for coherent displacement encoding and passive frequency-preserving frontends.

Primary note: `notes/WP5_INCIDENT_CHANNEL_QFI_SUM_RULE.md`.

---

## 5. Rigorous finite-band T-operator capture theorem

A blanket scalar extinction sum rule for arbitrary macroscopic scatterers was rejected as insufficiently rigorous. The arbitrary-scatterer route was moved to the matrix-valued T-operator oscillator representation of Zhang–Monticone–Miller.

For fixed incident vector `v`, band `B=[omega_-,omega_+]`, and passive response:

\[
\int_B\omega\,v^\dagger\operatorname{Im}T(\omega)v\,d\omega
\le
\pi\min\left[
\omega_p^2\|v\|^2,
\omega_+^2v^\dagger T_{0,D}v
\right].
\]

For reciprocal media the right-hand side is reduced by a factor of two.

For an electrically small reciprocal detector under nearly uniform illumination:

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

**Status:** PROVED under the fixed-spatial-profile passive reciprocal assumptions.

Primary note: `notes/WP5_T_OPERATOR_FINITE_BAND_CAPTURE.md`.

---

## 6. Plane-wave sideband profile variation is controlled

For plane-wave sidebands,

\[
v_\Omega(\mathbf r)=e^{i\Omega\hat k\cdot r/c}v_0(\mathbf r).
\]

For a detector contained within projected radius `R`, the fixed-profile theorem can be retained with correction

\[
C_{\rm phase}=e^{2\Omega_sR/c}.
\]

Therefore the controlling parameter is `Omega_s R / c`. When this is small, a separate large spatial-channel resource is not needed for ordinary plane-wave illumination.

Example: `R=1 mm`, `f_s=1 GHz` gives `C_phase ≈ 1.043`.

**Status:** DERIVED/PROVED under the stated finite-footprint plane-wave assumptions.

Primary note: `notes/WP5_PLANE_WAVE_PHASE_ROBUSTNESS.md`.

---

## 7. Restricted composite UPRP theorem assembled

For coherent modulation, passive reciprocal optical capture, controlled plane-wave sideband variation, finite T-operator resources, and the WP3 proper event-transducer class:

\[
\bar\eta_{\mathcal I}(\Omega_s)
\le
\min\left[B_{\rm opt}(\Omega_s),B_{\rm trans}(\Omega_s)\right].
\]

Use

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

and

\[
B_{\rm trans}
=
\eta_q\frac{\Lambda_{\rm micro}}{\Omega_s}
\arctan\frac{\Omega_s}{\Lambda_{\rm micro}}.
\]

In the narrow-sideband/small-footprint regime, define

\[
\Omega_{\rm EM}
=\frac{\pi V}{4cA}
\min(\omega_p^2,\omega_0^2t_0).
\]

A necessary condition for target average information fraction `r` is approximately

\[
\Omega_s
\lesssim
\min\left[
\Omega_{\rm EM}/r,
\;x(r/\eta_q)\Lambda_{\rm micro}
\right],
\]

where `arctan(x)/x=q` defines `x(q)`.

For `eta_q=1`, `x(0.90)=0.60253`, `x(0.95)=0.40565`, `x(0.99)=0.17478`.

**Status:** PROVED as a restricted classical/semiclassical composite theorem; not universal quantum theorem.

Primary note: `notes/WP6_RESTRICTED_COMPOSITE_THEOREM.md`.

---

## 8. Quantum completion route changed

Nishiyama–Hasegawa's temporal-Fisher open-system speed limit is relevant because its speed resource involves interaction-Hamiltonian energetic fluctuations, but it uses a unitarily residual distance and therefore removes pure unitary rotations.

That is not sufficient for photodetection because a coherent detector pointer rotation could carry useful electrical information before irreversible localization.

A direct subsystem distinguishability-transfer bound was derived instead.

For two optical hypotheses initially separated by trace distance

\[
D_{\rm in}=\frac12\|\rho_F^{(0)}-\rho_F^{(1)}\|_1,
\]

and corresponding detector reduced states with distance `D_det(t)`, move to an interaction picture removing local field/detector Hamiltonians. Using partial-trace contractivity and the trace-norm commutator bound gives

\[
D_{\rm det}(t)
\le
\frac{2D_{\rm in}}{\hbar}
\int_0^t g_{\rm int}(s)ds,
\]

with decomposition-independent interaction strength

\[
g_{\rm int}
=
\inf_{A_F,B_D}
\|H-A_F\otimes I_D-I_F\otimes B_D\|_\infty.
\]

If `g_int <= E_int`, transfer of fraction `r` of incident distinguishability requires

\[
t\ge r\hbar/(2E_{\rm int}).
\]

This bound retains coherent detector rotations, unlike the residual-Bures route.

**Status:** DERIVED CANDIDATE LEMMA. Novelty comparison, proof formalization, and conversion to QFI/continuous modulation are OPEN.

---

## 9. Novelty constraints accumulated

Do not claim novelty for:

- general detector tradeoffs;
- quantum photodetector frameworks/coherence-backaction tradeoffs;
- generic TUR/KUR/precision limits;
- generic finite-frequency response/noise inequalities;
- detector thermodynamics versus jitter/dark counts;
- optical LDOS or power-bandwidth limits;
- T-operator sum rules;
- generic information theory + Maxwell-constrained structured photonic channels.

Amaolo et al. are especially close on the optical-information side but their 2026 capacity result is single-frequency and identifies finite-band spectral-sum-rule/macroscopic-QED extensions as future directions.

Current candidate novelty is the full finite-band chain

\[
\text{incident optical information}
\rightarrow
\text{physical capture}
\rightarrow
\text{finite-temperature transduction}
\rightarrow
\text{electrical information},
\]

together with a no-go proof showing why stationary thermodynamic resources alone cannot set the absolute speed.

**Status:** PROVISIONAL novelty hypothesis only.

---

## 10. Exact next action for a replacement agent

Do not restart broad literature searching or rederive WP1.

Proceed in this order:

1. audit the subsystem trace-distance transfer lemma against existing interaction-norm distinguishability/entangling-rate/Lieb–Robinson literature;
2. formalize the lemma carefully, including time-dependent interactions and optimal subtraction of local Hamiltonian components;
3. derive a QFI/Fisher-information-transfer version for weak continuous optical modulation;
4. test whether `g_int` or `gamma_max` can be bounded from the same passive matter + electromagnetic resources already used in WP5, without inserting bandwidth circularly;
5. extend beyond coherent optical states;
6. stress-test active/gain, high-Q, vanishing-mode-volume, strong-coupling, non-Markovian, direct-feedthrough, and parallel-replication limits;
7. only then select the publication theorem and finalize novelty claims.

## Handoff status

A replacement agent should be able to resume from `docs/CURRENT_RESEARCH_STATE.md`, this file, and the dedicated WP notes without access to the originating chat.
