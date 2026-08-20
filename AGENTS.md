# AGENTS.md

## Purpose

This is the durable handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat context, is authoritative.

Research is analytical/theoretical. Numerical work is allowed for algebraic validation and conjecture testing. Do not make laboratory experiments, fabrication, sample procurement, or measurement campaigns necessary next steps.

## Read first

A replacement agent should read, in order:

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `notes/RESEARCH_LOG_ROUND5.md`
3. `notes/WP7_GENERAL_APPARATUS_QFI_BOUND.md`
4. `notes/WP7_ENERGY_REPAIRED_GAUSSIAN_THEOREM.md`
5. `notes/WP7_COHERENT_GAUSSIAN_QFI_TRANSFER.md`
6. `notes/WP7_QUANTUM_DISTINGUISHABILITY_TRANSFER.md`
7. `notes/WP6_RESTRICTED_COMPOSITE_THEOREM.md`
8. `notes/WP5_T_OPERATOR_FINITE_BAND_CAPTURE.md`
9. `notes/WP5_PLANE_WAVE_PHASE_ROBUSTNESS.md`
10. `notes/WP4_MICROSCOPIC_OPTICAL_COUPLING_NO_GO.md`
11. `notes/WP3_GATEWAY_RESOURCE_THEOREM.md`
12. `docs/NOVELTY_AUDIT_ROUND2.md`
13. `docs/LITERATURE_MAP.md`
14. `docs/FORMALISM.md`

Older WP0/WP1/WP2 notes and research logs preserve derivations, counterexamples, and failed conjectures and should be consulted when those branches are touched.

---

# Project objective

Determine the physical resources necessary and/or sufficient for a finite-temperature photodetector to transfer information from an incident optical field into an electrical measurement record with specified sensitivity and temporal bandwidth.

Valid endpoints include a rigorous resource bound, a no-go theorem, an explicit counterexample family, or a repaired theorem after identifying a missing resource.

Do **not** assume that a simple sensitivity-bandwidth-temperature product exists.

---

# Core information metric

Use source-normalized information transfer

\[
\eta_{\mathcal I}=F_{\rm electrical}/F_{\rm incident}^{Q}
\]

for the same encoded optical parameter.

For coherent/Poisson weak photon-flux modulation,

\[
\eta_{\mathcal I}(\omega)=\Phi_0\frac{|\chi_{Y\Phi}(\omega)|^2}{S_Y(\omega)}.
\]

This is the temporal analogue of DQE and is not itself novel.

Use a finite source task

\[
\bar\eta_{\mathcal I}
=\frac{\int(d\omega/2\pi)\mathcal J_{\rm in}(\omega)\eta_{\mathcal I}(\omega)}
{\int(d\omega/2\pi)\mathcal J_{\rm in}(\omega)}
\]

rather than an unweighted all-frequency integral.

---

# Established classical/semiclassical results

## WP1 — finite-state Markov response/noise: SOLVED

With reduced resolvent `R(omega)=Q(i omega I-W)^(-1)Q`,

\[
S_I(\omega)=\mathbf1^T\mathcal J^{(2)}\pi
+2\operatorname{Re}[\mathbf1^T\mathcal J^{(1)}R(\omega)\mathcal J^{(1)}\pi],
\]

\[
\chi_{Iu}(\omega)=\mathbf1^T\mathcal J_u^{(1)}\pi
+\mathbf1^T\mathcal J_0^{(1)}R(\omega)W_u\pi.
\]

**PROVED** for finite-state stationary Markov jump detectors.

## WP4 — strongest Markov no-go

There is an explicit reversible three-state family with fixed optical detailed balance, finite photon-energy/temperature ratio, finite nonzero optical throughput, finite total stationary activity, finite total and edge-resolved EPR, and finite detection probability while the absolute optical/internal rate scale diverges.

Therefore

\[
\boxed{
\{T,\hbar\omega_0,\text{detailed balance},f_*,\mathcal A,\Sigma,\text{edge EPRs},\eta_q\}
\not\Rightarrow\text{finite detector speed}.
}
\]

An **absolute microscopic coupling/transition scale is necessary**.

## WP3 — restricted thermokinetic completion

For a reversible optical gateway with reverse optical rate `d`, throughput `f>=f_*`, EPR budget `Sigma`, and activity budget `A`, define

\[
g(z)=(1-1/z)\ln z,
\qquad Z_*=g^{-1}(\Sigma/f_*).
\]

Then

\[
\pi_1\ge f_*/(dZ_*),
\qquad
\lambda_1\le\Lambda_*=(\mathcal A d/f_*)Z_*.
\]

For a proper single-event transducer,

\[
\eta_{\mathcal I}(\omega)
\le\eta_q\frac{\Lambda_*^2}{\Lambda_*^2+\omega^2}.
\]

## WP5 — passive finite-band optical capture

For coherent-state modulation through a passive frequency-preserving frontend,

\[
F_{\rm electrical}\le\int\frac{d\omega}{2\pi}\tau(\omega)\mathcal J_{\rm in}(\omega).
\]

Using rigorous matrix-valued T-operator oscillator/sum-rule constraints, an electrically small reciprocal detector under nearly uniform illumination obeys

\[
\bar\eta_{\mathcal I}(\Omega_s)
\le
\min\left[
1,
\frac{\pi}{4cA\Omega_s}
\min(\omega_p^2V,(\omega_0+\Omega_s)^2\alpha_{\rm stat})
\right].
\]

Plane-wave sideband variation over radius `R` costs at most `exp(2 Omega_s R/c)`.

## WP6 — restricted composite theorem

Where WP3 and WP5 assumptions overlap,

\[
\boxed{
\bar\eta_{\mathcal I}(\Omega_s)
\le\min[B_{\rm opt}(\Omega_s),B_{\rm trans}(\Omega_s)].
}
\]

This is **PROVED as a restricted classical/semiclassical theorem**, not a universal quantum theorem.

---

# WP7 — fully quantum resource structure

## QH: finite hypotheses / Helstrom information

For optical signal `F` and complete detector/apparatus `D`, initially `rho_F^(a) tensor sigma_D`, define

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

If `g_int<=E_int`, transfer fraction `r` requires `t>=r hbar/(2E_int)`.

**PROVED** under the initial product/same-apparatus-state and unitary-dilation assumptions.

Important: for bosonic bilinear interactions, the full Fock-space operator norm is generally unbounded, so this finite-dimensional/general theorem does not by itself supply the useful optical coupling resource. The passive-linear coherent branch instead uses the finite single-particle cross-coupling norm below.

## QFI does not inherit trace contraction

Exact trine POVM counterexample:

\[
\eta_{\rm Tr}=2/3,
\qquad
\eta_{\rm SLD}=1.
\]

For equatorial qubits of Bloch radius `s`, `F_out/F_in=1/(2-s)->1` as `s->1^-`.

Thus any step `QFI contraction <= trace contraction` or `<= trace contraction^2` is **REJECTED**.

---

# WP7 coherent/passive-linear QFI results

## Single-particle coupling action

For passive bosonic coupling with cross block `V(t)`, define

\[
\Gamma(t)=\int_0^t\|V(s)\|_2ds.
\]

The source-to-detector displacement transfer probability obeys

\[
\tau\le\sin^2(\min\{\Gamma,\pi/2\}).
\]

This follows from the subspace-flow inequality

\[
|\dot p_D|\le2\|V\|\sqrt{p_D(1-p_D)}.
\]

## Coherent/vacuum apparatus theorem

For coherent optical displacement encoding and detector modes initially in fixed coherent states,

\[
\boxed{
F_{\rm elec}/F_{\rm in}
\le\sin^2(\min\{\Gamma,\pi/2\}).
}
\]

The two-mode beam splitter saturates the bound.

## Squeezed-pointer no-go

For coherent optical x-displacement, beam-splitter angle `phi`, and detector x-squeezing `r`,

\[
\boxed{
F_{\rm elec}/F_{\rm in}
=
\frac{\sin^2\phi}
{\sin^2\phi+\cos^2\phi e^{-2r}}.
}
\]

For any nonzero `phi`, this tends to 1 as `r->infinity`.

Therefore **cross-coupling action alone does not bound coherent-state QFI transfer** if arbitrary preloaded detector squeezing/metrological energy is allowed.

At weak coupling, maintaining transfer fraction `q` requires detector energy `N_D ~ q/[4(1-q)phi^2]`.

This identifies a second missing quantum resource: **initial apparatus translation/metrological resource**.

---

# Tight energy-repaired Gaussian theorem

For one effective detector Gaussian mode with mean excitation budget `N`, define

\[
\xi(N)=(\sqrt{N+1}-\sqrt N)^2.
\]

At displacement-transfer probability `tau`,

\[
\boxed{
F_{\rm elec}/F_{\rm in}
\le
\frac{\tau}{\tau+(1-\tau)\xi(N)}.
}
\]

With `tau<=sin^2 Gamma`,

\[
\boxed{
F_{\rm elec}/F_{\rm in}
\le
\frac{\sin^2\Gamma}
{\sin^2\Gamma+\cos^2\Gamma\xi(N)}
}
\]

for `0<=Gamma<=pi/2`.

This is tight and saturable by an aligned squeezed-vacuum pointer, beam-splitter coupling, and homodyne readout.

To transfer fraction `q`,

\[
\boxed{
\Gamma\ge\arctan\sqrt{\frac{q\xi(N)}{1-q}}.
}
\]

At `N=0` it reduces to `Gamma>=arcsin sqrt(q)`. For large `N`, required action scales as `N^(-1/2)`.

---

# Broad arbitrary-apparatus QFI theorem under passive linear coupling

Define the detector's pre-existing translation susceptibility

\[
\boxed{
\mathcal R_D
=2\sup_c\operatorname{Var}(P_c),
}
\]

where `c` runs over normalized collective detector modes accessible to the passive coupling/local processing. Vacuum has `R_D=1`.

For coherent displacement input and arbitrary theta-independent detector state,

\[
\boxed{
F_{\rm elec}/F_{\rm in}
\le\min\{1,\tau\mathcal R_D\}
\le\min\{1,\mathcal R_D\sin^2\Gamma\}.
}
\]

If total detector pointer excitation is bounded by `N`, Robertson uncertainty plus the energy constraint gives

\[
\mathcal R_D\le2N+1+2\sqrt{N(N+1)}=1/\xi(N).
\]

Hence

\[
\boxed{
F_{\rm elec}/F_{\rm in}
\le
\min\left[1,\frac{\sin^2\Gamma}{\xi(N)}\right].
}
\]

This is looser than the tight Gaussian theorem but applies to arbitrary pointer states within the stated passive-linear oscillator/energy assumptions.

---

# Current resource hierarchy

The most complete structure now supported by explicit theorems/counterexamples is

\[
\boxed{
\text{source temporal/information task}
+
\text{finite-band EM capture resources}
+
\text{absolute microscopic cross-coupling}
+
\text{initial apparatus translation/metrological resource}
+
\text{ongoing thermokinetic resources}
\Longrightarrow
\text{information-transfer ceiling}.
}
\]

WP4 proves the coupling resource cannot be omitted. WP7 proves the apparatus-preparation resource cannot be omitted in the local-QFI quantum branch.

---

# Highest-priority next tasks

1. **Thermodynamic closure of apparatus preparation.** Bound `R_D` or the pointer energy/squeezing resource by nonequilibrium free energy, ergotropy, asymmetry, or another finite-temperature preparation cost for a specified detector Hamiltonian.
2. **Multimode tightening.** Determine whether the tight Gaussian `xi(N)` denominator theorem survives arbitrary multimode Gaussian apparatus under a total energy budget; the broad variance theorem already survives but is looser.
3. **Full quantum composition.** Compose WP7 QFI transfer with WP5 finite-band EM capture and, where compatible, WP3 thermokinetic conversion.
4. **Active/gain stress test.** Any active amplifier/pump must bring explicit pump energy/free energy and quantum-added-noise resources.
5. **Novelty audit.** Compare against Gaussian metrology, squeezed readout, weak-coupling ancilla metrology, interaction-speed limits, and quantum Doeblin/contraction literature.

---

# Novelty constraints

Do not claim novelty for generic photodetector tradeoffs, squeezing-enhanced metrology, Gaussian QFI, quantum speed limits, contraction coefficients, thermodynamic uncertainty relations, optical power-bandwidth limits, T-operator sum rules, or Maxwell-constrained photonic information capacity.

The current candidate novelty is the **photodetection-specific resource-completeness/no-go/completion structure**, especially the explicit sequence of counterexamples showing exactly which hidden resources must be added before finite information-speed bounds become possible.

---

# Mandatory adversarial tests

For every theorem/resource set test:

1. dimensions and reparameterization invariance;
2. deterministic output gain;
3. ideal photon counter/direct feedthrough;
4. source bandwidth leakage;
5. parallel replication/extensivity;
6. rare-fast states;
7. bounded total/edge EPR with divergent bare rates;
8. fixed optical detailed balance with divergent absolute coupling;
9. high-Q/vanishing mode volume;
10. finite-footprint phase;
11. active/gain media and hidden pump resources;
12. strong/ultrastrong coupling and non-Markovianity;
13. coherent pointer rotations;
14. near-rank-deficient source families;
15. squeezed/energetic preloaded apparatus;
16. whether a proposed resource merely restates the bandwidth being bounded.

---

# Recordkeeping

After each substantive result:

- create/update a dedicated derivation note;
- add a numbered research-log checkpoint when project direction changes;
- update `AGENTS.md` and `docs/CURRENT_RESEARCH_STATE.md` when the frontier materially changes;
- preserve failed conjectures and counterexamples.

Status vocabulary: **PROVED**, **VERIFIED**, **CONJECTURE**, **COUNTEREXAMPLE**, **OPEN**, **BLOCKED**, **REJECTED**.

## Current state — late Round 5, 2026-08-19

The project now contains: a Markov missing-coupling no-go theorem; a restricted optical+thermokinetic completion theorem; a fully quantum finite-hypothesis interaction-action theorem; an exact trace-vs-QFI obstruction; a coherent/passive-linear QFI coupling theorem; a squeezed-pointer no-go; a tight energy-repaired Gaussian theorem; and a broader arbitrary-pointer energy/translation-susceptibility theorem. The immediate frontier is to convert the initial apparatus resource into a finite-temperature thermodynamic preparation resource and then compose all resource layers.