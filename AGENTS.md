# AGENTS.md

## Purpose

This is the durable handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat context, is authoritative.

Research is analytical/theoretical. Numerical work is allowed for algebraic validation and conjecture testing. Do not make laboratory experiments, fabrication, sample procurement, or measurement campaigns necessary next steps.

## Read first

A replacement agent should read, in order:

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `notes/RESEARCH_LOG_ROUND5.md`
3. `notes/WP7_QUANTUM_DISTINGUISHABILITY_TRANSFER.md`
4. `notes/WP6_RESTRICTED_COMPOSITE_THEOREM.md`
5. `notes/WP5_T_OPERATOR_FINITE_BAND_CAPTURE.md`
6. `notes/WP5_PLANE_WAVE_PHASE_ROBUSTNESS.md`
7. `notes/WP4_MICROSCOPIC_OPTICAL_COUPLING_NO_GO.md`
8. `notes/WP3_GATEWAY_RESOURCE_THEOREM.md`
9. `docs/NOVELTY_AUDIT_ROUND2.md`
10. `docs/LITERATURE_MAP.md`
11. `docs/FORMALISM.md`

Older WP0/WP1/WP2 notes and research logs preserve derivations, counterexamples, and failed conjectures and should be consulted when those branches are touched.

---

# Project objective

Determine the physical resources necessary and/or sufficient for a finite-temperature photodetector to transfer information from an incident optical field into an electrical measurement record with specified sensitivity and temporal bandwidth.

Valid endpoints include:

- a rigorous resource bound;
- a rigorous no-go theorem;
- an explicit counterexample family;
- identification of a missing resource followed by a repaired theorem.

Do **not** assume that a simple sensitivity-bandwidth-temperature product exists.

---

# Core information metric

Use source-normalized information transfer

\[
\boxed{
\eta_{\mathcal I}=F_{\rm electrical}/F_{\rm incident}^{Q}
}
\]

for the same encoded optical parameter.

For coherent/Poisson weak photon-flux modulation,

\[
\eta_{\mathcal I}(\omega)
=\Phi_0\frac{|\chi_{Y\Phi}(\omega)|^2}{S_Y(\omega)}.
\]

This is the temporal analogue of DQE and is not itself novel.

Do not use an unweighted all-frequency integral as the universal objective. Use a finite source task:

\[
\boxed{
\bar\eta_{\mathcal I}
=\frac{\int(d\omega/2\pi)\mathcal J_{\rm in}(\omega)\eta_{\mathcal I}(\omega)}
{\int(d\omega/2\pi)\mathcal J_{\rm in}(\omega)}.
}
\]

---

# WP1 — exact finite-state Markov response/noise: SOLVED

For stationary finite-state Markov jump detectors, with reduced resolvent

\[
R(\omega)=Q(i\omega I-W)^{-1}Q,
\]

\[
\boxed{
S_I(\omega)=\mathbf1^T\mathcal J^{(2)}\pi
+2\operatorname{Re}[\mathbf1^T\mathcal J^{(1)}R(\omega)\mathcal J^{(1)}\pi]
}
\]

and

\[
\boxed{
\chi_{Iu}(\omega)=\mathbf1^T\mathcal J_u^{(1)}\pi
+\mathbf1^T\mathcal J_0^{(1)}R(\omega)W_u\pi.
}
\]

These are **PROVED** for the finite-state stationary Markov jump class and checked on solvable examples. Issue #2 is closed.

---

# WP4 — strongest classical no-go theorem

Weak-coupling bosonic optical rates have the form

\[
\Gamma_\uparrow=\gamma(\omega_0)n(\omega_0),
\qquad
\Gamma_\downarrow=\gamma(\omega_0)[n(\omega_0)+1].
\]

Temperature and photon energy fix the ratio, not the absolute coupling `gamma`.

The reversible family

\[
0\xrightleftharpoons[bR]{aR}1,
\qquad
1\xrightleftharpoons[q]{cR}2,
\qquad
2\xrightleftharpoons[sR]{p}0
\]

can keep fixed optical detailed balance, finite nonzero optical throughput, finite total stationary activity, finite total and edge-resolved EPR, and finite nonzero detection probability while its post-absorption escape rate diverges as `(b+c)R`.

Therefore

\[
\boxed{
\{T,\hbar\omega_0,\text{detailed balance},f_*,\mathcal A,\Sigma,\text{edge EPRs},\eta_q\}
\not\Rightarrow\text{finite detector speed}.
}
\]

An **absolute microscopic coupling/transition resource is necessary**.

**Status:** PROVED for the reversible finite-state Markov event-detector class.

---

# WP3 — restricted internal completion theorem

For a reversible optical gateway with reverse optical rate `d`, forward throughput `f>=f_*>0`, EPR budget `Sigma`, and activity budget `A`, define

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

For a proper single-event detector whose electrical event cannot occur before first exit from the post-absorption gateway,

\[
\boxed{
\eta_{\mathcal I}(\omega)
\le\eta_q\frac{\Lambda_*^2}{\Lambda_*^2+\omega^2}.
}
\]

If `gamma(omega_0)<=gamma_max`, then `d<=gamma_max[n+1]` and the theorem has an explicit microscopic coupling cap.

---

# WP5 — finite-band passive optical capture

For coherent-state displacement modulation through a passive frequency-preserving frontend,

\[
F_{\rm electrical}
\le\int\frac{d\omega}{2\pi}\tau(\omega)\mathcal J_{\rm in}(\omega).
\]

For a flat optical sideband-QFI task,

\[
\bar\eta_{\mathcal I}
\le\frac1{2\Omega_s}
\int_{\omega_0-\Omega_s}^{\omega_0+\Omega_s}\tau(\omega)d\omega.
\]

Using the rigorous matrix-valued T-operator oscillator/sum-rule framework, for an electrically small reciprocal detector under nearly uniform illumination,

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

Do not assert a blanket scalar macroscopic extinction sum rule for arbitrary scatterers. Use the T-operator route for arbitrary passive scatterers; use scalar TRK only in its microscopic dipole domain.

Plane-wave sideband variation is controlled by

\[
C_{\rm phase}=e^{2\Omega_sR/c}.
\]

Thus fixed-profile bounds remain robust when `Omega_s R/c << 1`.

---

# WP6 — restricted composite theorem

For coherent modulation, passive reciprocal capture with finite EM resources, controlled plane-wave sideband variation, and the WP3 event-transducer assumptions,

\[
\boxed{
\bar\eta_{\mathcal I}(\Omega_s)
\le\min[B_{\rm opt}(\Omega_s),B_{\rm trans}(\Omega_s)].
}
\]

With

\[
B_{\rm opt}
=
\min\left[
1,
\frac{\pi V}{4cA\Omega_s}e^{2\Omega_sR/c}
\min(\omega_p^2,(\omega_0+\Omega_s)^2t_0)
\right],
\]

and

\[
B_{\rm trans}
=\eta_q\frac{\Lambda_{\rm micro}}{\Omega_s}
\arctan\frac{\Omega_s}{\Lambda_{\rm micro}},
\]

\[
\Lambda_{\rm micro}
=\frac{\mathcal A\gamma_{\max}[n(\omega_0)+1]}{f_*}
 g^{-1}(\Sigma/f_*).
\]

This is **PROVED as a restricted classical/semiclassical theorem**, not as a universal quantum theorem.

---

# WP7 — fully quantum branch

## QH: finite hypotheses / Helstrom information — PROVED

Partition the closed dilation into optical signal `F` and complete detector/apparatus `D`, initially

\[
\rho_{FD}^{(a)}(0)=\rho_F^{(a)}\otimes\sigma_D.
\]

Define the decomposition-invariant nonlocal interaction seminorm

\[
\boxed{
g_{\rm int}(t)=\inf_{A_F,B_D}\|H(t)-A_F\otimes I-I\otimes B_D\|_\infty
}
\]

and

\[
G(t)=\hbar^{-1}\int_0^t g_{\rm int}(s)ds.
\]

Then

\[
\boxed{
D_{\rm elec}(t)/D_{\rm in}\le\min\{1,2G(t)\}.
}
\]

If `g_int<=E_int`, transferring a fraction `r` of available binary distinguishability requires

\[
\boxed{t\ge r\hbar/(2E_{\rm int}).}
\]

This retains coherent detector pointer rotations and arbitrary non-Markovian internal dynamics when all apparatus degrees of freedom are included in `D`.

## QF: local parameter / SLD-QFI information — OPEN

The QH theorem cannot simply be differentiated into a QFI theorem.

Exact trine-POVM unit test:

\[
\boxed{\eta_{\rm Tr}=2/3,\qquad\eta_{\rm SLD}=1.}
\]

For equatorial qubit states of Bloch radius `s`, phase encoding aligned to one trine arm gives

\[
F_{\rm out}/F_{\rm in}=1/(2-s)\to1
\quad(s\to1^-).
\]

Thus any claim `QFI contraction <= trace contraction` or `<= trace contraction^2` is **REJECTED**.

Primary note: `notes/WP7_QUANTUM_DISTINGUISHABILITY_TRANSFER.md`. Issue #7 tracks QH/QF.

---

# Current highest-priority mathematical gate

Solve QF for the physically relevant coherent-state displacement/sideband source family used in WP0/WP5.

Preferred attack order:

1. event/no-click detector channels: test for a theta-independent replacer branch and derive exact FI contraction if present;
2. direct channel-QFI derivative bound from `H_int`;
3. quantum Doeblin/replacer strong-data-processing route if a nonzero replacer coefficient follows from physical detector structure;
4. if no state-independent bound exists, construct the counterexample and identify the minimal source/output regularity resource;
5. only then compose the quantum result with WP5/WP6.

Important warning: bounded interaction action alone has **not** yet been proved to imply a positive Doeblin/replacer coefficient for arbitrary unitary field-detector interactions.

---

# Novelty constraints

Do not claim novelty for generic:

- photodetector tradeoffs;
- quantum photodetector frameworks/coherence-backaction tradeoffs;
- thermodynamic precision bounds;
- detector dissipation-performance tradeoffs;
- finite-frequency response/noise bounds;
- optical LDOS/power-bandwidth limits;
- T-operator sum rules;
- Maxwell-constrained photonic Shannon-capacity bounds;
- quantum-channel contraction coefficients;
- interaction-norm entangling/information-transfer speed limits.

Key adjacent literature includes Young–Sarovar–Léonard, Hasegawa and later uncertainty-relation work, Schwarzhans et al., Dechant, Liu/Gu, Zhang–Monticone–Miller, Shim et al., Amaolo et al., Hiai–Ruskai, quantum Doeblin coefficient work, and interaction-Hamiltonian speed/entangling bounds.

The current candidate novelty is the **photodetection-specific no-go/completion composition**:

\[
\text{finite optical information task}
\to\text{physical EM capture}
\to\text{microscopic coupling}
\to\text{finite-temperature transduction}
\to\text{electrical information},
\]

including proof that stationary thermodynamic resources do not supply an absolute speed scale.

Novelty remains provisional until theorem-level citation chaining is complete.

---

# Mandatory adversarial tests

For every theorem/resource set test:

1. dimensional and reparameterization invariance;
2. deterministic output-gain invariance;
3. ideal photon counter / direct feedthrough;
4. source-bandwidth leakage;
5. parallel replication/extensivity;
6. rare-fast states;
7. bounded total/edge EPR with divergent bare rates;
8. fixed optical detailed balance with divergent absolute coupling;
9. high-Q / vanishing mode volume;
10. large participating electron number;
11. finite-footprint propagating phase;
12. increasing spatial channel count;
13. active/gain media and pump/noise resources;
14. strong/ultrastrong coupling and non-Markovianity;
15. coherent pointer rotations;
16. near-rank-deficient quantum source families;
17. whether a proposed resource merely restates the bandwidth being bounded.

---

# Recordkeeping protocol

After each substantive result:

- create/update a dedicated derivation note;
- add a numbered research-log checkpoint when project direction changes;
- update this file and `docs/CURRENT_RESEARCH_STATE.md` when the frontier changes materially;
- preserve failed conjectures and counterexamples.

Status labels:

- **PROVED** — complete derivation under explicit assumptions;
- **VERIFIED** — independently checked but not fully formalized;
- **CONJECTURE** — plausible and unproved;
- **COUNTEREXAMPLE** — explicit model violates a stated claim;
- **OPEN** — unresolved;
- **BLOCKED** — missing theoretical/source input;
- **REJECTED** — invalid or redundant.

## Current state — Round 5, 2026-08-19

The classical/semiclassical branch contains a strong missing-coupling no-go theorem and a restricted finite-band optical+thermokinetic completion theorem. The fully quantum branch now contains a rigorous finite-hypothesis interaction-action transfer theorem and an exact proof that local-QFI transfer is a separate problem. The immediate research frontier is QFI transfer for coherent optical displacement/sideband families.