# AGENTS.md

## Purpose
Durable handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

Research is analytical/theoretical only. Numerical work is allowed for validation. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

## Read first
1. `docs/CURRENT_RESEARCH_STATE.md`
2. `notes/RESEARCH_LOG_ROUND12.md`
3. `manuscript/event_resource_theorem_rev3.tex`
4. `docs/MANUSCRIPT_HOSTILE_PROOF_AUDIT_ROUND2.md`
5. `notes/WP32_GENERAL_MARKED_POISSON_EVENT_KERNEL_THEOREM.md`
6. `notes/WP33_EXACT_FIXED_MEAN_VARIANCE_JITTER_NO_GO.md`
7. `notes/WP29_THERMODYNAMIC_BRIDGE_TO_REGISTRATION_INTENSITY.md`
8. `notes/WP30_WIENER_ATOMIC_DELAY_INFORMATION_THEOREM.md`
9. `notes/WP31_EVENT_BRANCH_RESOURCE_NECESSITY_MATRIX.md`
10. `docs/NOVELTY_AUDIT_ROUND5_EVENT_THEOREM_STACK.md`
11. `manuscript/references.bib`
12. `manuscript/appendix_rare_fast_counterexample.tex`
13. earlier WP0–WP24 notes only as needed.

**Freeze:** detailed HgCdTe/Kane WP17–24 unless a core theorem explicitly requires material validation.

---

# Strategic state
The mature core is the **autonomous proper marked-event detector** branch. The first-paper candidate is now manuscript Rev3 on branch:

`agent/uprp-core-theorem-round10`

Primary source:

`manuscript/event_resource_theorem_rev3.tex`

Do not reopen broad material-specific or analog-detector branches unless a concrete counterexample forces it.

---

# Core event theorem
Weak coherent/direct-detection source:
\[
\Phi_\theta(t)=\Phi_0[1+\theta\cos\omega t].
\]

Per incident photon, autonomous primary-event kernel:
\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\qquad
\eta=\kappa(\mathsf M)\le1.
\]

The per-photon kernel is independent of the small source parameter; the source parameter modulates arrival intensity only. `M` is the complete accessible primary-event mark.

Exact ideal-record source-normalized FI transfer:
\[
\boxed{
G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm).
}
\]

Parameter-independent background or downstream processing can only reduce FI.

---

# Timing-resource hierarchy

## Atomic timing
If `p_j(m)` are the atoms of the mark-conditioned delay measure,
\[
\boxed{
\lim_{\Omega\to\infty}
\frac1{2\Omega}\int_{-\Omega}^{\Omega}G(\omega)d\omega
=
\int\kappa(dm)\sum_jp_j(m)^2.
}
\]

This is an asymptotic flat-band average statement; do not claim pointwise Fourier decay for every non-atomic singular measure.

## Collision intensity
For square-integrable conditional densities,
\[
\boxed{
\mathfrak R_2
=2\int\kappa(dm)\int f_m(t)^2dt,
}
\]
and
\[
\boxed{
\int G(\omega)d\omega=\pi\mathfrak R_2.
}
\]
Thus
\[
\boxed{
\bar\eta_I(\Omega)
\le
\min\left[\eta,\frac{\pi\mathfrak R_2}{2\Omega}\right].
}
\]

## Microscopic hazard capacity
If
\[
h_m(t)\le\Lambda(m),
\]
define
\[
\boxed{
\mathfrak H=\int\Lambda(m)\kappa(dm).
}
\]
Then
\[
\boxed{\mathfrak R_2\le\mathfrak H.}
\]

A global worst-case hazard is only a stronger corollary. Rare ultra-fast branches are harmless if their capture weight vanishes sufficiently fast.

Preferred proof:
\[
\int f^2=\int h^2S^2
\le\Lambda\int hS^2
=\Lambda/2.
\]

---

# WP33 exact jitter no-go
For any prescribed
\[
\mu_0>0,
\qquad
\sigma^2>0,
\]
there exists a smooth two-exponential-plus-shift family satisfying exactly
\[
\boxed{
\mathbb ED=\mu_0,
\qquad
\operatorname{Var}D=\sigma^2
}
\]
for every family member while
\[
|H_D(\omega)|^2\to1
\]
uniformly on every prescribed finite frequency band.

Therefore
\[
\boxed{
\{\text{exact mean delay, exact RMS jitter}\}
\not\Rightarrow
\text{finite information bandwidth}.
}
\]

Do not overstate this as an arbitrary exact-FWHM theorem.

---

# External clock/control no-go
A free source-synchronous temporal reference can store arrival phase in a mark and report it arbitrarily slowly while preserving source timing FI.

Therefore the central theorem applies to **autonomous/time-translation-invariant** event detectors unless clock/control bandwidth, phase precision, memory, and action are explicitly included as resources.

---

# Thermodynamic bridge
Restricted finite-state time-homogeneous Markov gateway:
\[
0\xrightleftharpoons[d]{u}1,
\qquad
f=u\pi_0\ge f_*.
\]

With EPR `<=Sigma` and activity `<=A`, define
\[
g(z)=(1-z^{-1})\ln z.
\]
Then
\[
\boxed{
\lambda_1
\le
\Lambda_*
=
\frac{\mathcal A d}{f_*}
 g^{-1}(\Sigma/f_*).
}
\]

Because the finite-state Markov holding time in state 1 is exponential and independent of exit destination, any downstream mark generated only from the exit destination and later autonomous Markov path satisfies
\[
\boxed{h_D(t|M)\le\lambda_1.}
\]

Hence
\[
\boxed{
\bar\eta_I(\Omega)
\le
C\min\left[
1,
\frac{\pi\mathcal A d}{2f_*\Omega}
 g^{-1}(\Sigma/f_*)
\right].
}
\]

The absolute rate `d` is a microscopic resource. WP4/rare-fast appendix shows aggregate stationary EPR/activity/throughput plus fixed optical detailed-balance ratio do not determine the local temporal scale if hidden nonoptical microscopic scales may diverge.

Do not claim every edge-resolved affinity is fixed in that counterexample.

---

# Manuscript status
Current target:

`manuscript/event_resource_theorem_rev3.tex`

Rev3 incorporates all proof-audit corrections and includes

`manuscript/appendix_rare_fast_counterexample.tex`.

Bibliography:

`manuscript/references.bib`.

Branch-only compile workflow:

`.github/workflows/manuscript-check.yml`.

The connector has not yet exposed a completed push-triggered Actions result. Do **not** claim the manuscript has compiled successfully until a build result is actually inspected.

---

# Novelty posture
Closest known work includes FI/CRLB lifetime estimation, Talaga's IRF information/effective-bandwidth treatment, later FLIM FI/IRF analyses, and Dechant's finite-frequency response--noise inequality.

Do not claim:
- first information-theoretic detector timing analysis;
- first timing-response information loss result;
- first detector sensitivity--bandwidth tradeoff;
- generic finite-frequency response/noise novelty;
- universal all-detector speed limit.

Current defensible candidate contribution:

> A resource-completeness theorem for source-modulation information transfer in autonomous marked photodetection event channels, with exact atomic and collision-intensity timing resources and explicit no-go/repair results for low-order jitter moments, free synchronous control, and aggregate stationary thermodynamics.

Novelty remains provisional but no equivalent complete stack has been located in targeted searches.

---

# Immediate next actions
1. Obtain and inspect a real LaTeX compile result for Rev3.
2. Repair any build errors and run a final equation/reference cross-check.
3. Add only high-information figures that clarify theorem content.
4. Perform a final publication-level claim/citation audit.
5. Decide whether to prepare a submission-ready manuscript package.
6. Defer non-Poisson/nonclassical source extension unless a referee-style review shows it is necessary.
7. Keep WP17–24 frozen.

Status vocabulary: **PROVED**, **VERIFIED**, **CONJECTURE**, **COUNTEREXAMPLE**, **OPEN**, **BLOCKED**, **REJECTED**.
