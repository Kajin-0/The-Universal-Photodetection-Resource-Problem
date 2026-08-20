# Current Research State

**Date:** 2026-08-20

This is the first-stop replacement-agent summary. **The repository, not chat history, is authoritative.**

## Read first
1. `AGENTS.md`
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

Detailed HgCdTe/Kane WP17–24 is **frozen**.

---

# 1. Central objective
Determine the smallest physical resource set that bounds source-normalized optical-to-electrical temporal information transfer for a precisely defined photodetector class, and prove insufficiency by explicit counterexample when candidate resources are omitted.

The current mature answer is for **autonomous, independent-event, one-primary-registration photodetection of weak coherent/direct-detection intensity modulation**.

Do not describe the result as a universal all-detector speed limit.

---

# 2. Exact marked-event theorem

Source:
\[
\Phi_\theta(t)=\Phi_0[1+\theta\cos\omega t].
\]

Per incident photon:
\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\qquad
\eta=\kappa(\mathsf M)\le1.
\]

`M` is the complete accessible primary-event mark. The kernel is independent of the small modulation parameter; the parameter modulates only incident arrival intensity. The detector is time-translation invariant/autonomous.

Exact ideal-record source-normalized FI transfer:
\[
\boxed{
G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm).
}
\]

Any parameter-independent background addition or downstream processing obeys FI data processing and cannot exceed `G`.

---

# 3. Exact structural timing result

If `p_j(m)` are atomic masses of the mark-conditioned delay law,
\[
\boxed{
\lim_{\Omega\to\infty}
\frac1{2\Omega}\int_{-\Omega}^{\Omega}G(\omega)d\omega
=
\int\kappa(dm)\sum_jp_j(m)^2.
}
\]

Purely non-atomic conditional timing therefore gives zero asymptotic **flat-band average** transfer. Do not strengthen this into a general pointwise Fourier-decay claim.

---

# 4. Quantitative timing resources

For square-integrable conditional delay densities,
\[
\boxed{
\mathfrak R_2
=2\int\kappa(dm)\int f_m(t)^2dt.
}
\]

Parseval:
\[
\boxed{
\int G(\omega)d\omega=\pi\mathfrak R_2.
}
\]

Flat-band result:
\[
\boxed{
\bar\eta_I(\Omega)
\le
\min\left[\eta,\frac{\pi\mathfrak R_2}{2\Omega}\right].
}
\]

For weighted frequency-resolved source tasks,
\[
\int wG
\le
\eta\,\mathcal W(\pi\mathfrak R_2/\eta).
\]
This is not a theorem for arbitrary correlated multiparameter quantum estimation.

---

# 5. Microscopic hazard completion

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

Preferred proof:
\[
\int f^2=\int h^2S^2
\le\Lambda\int hS^2
=\Lambda/2
\]
because `d(S^2)/dt=-2hS^2`.

A uniform global hazard is only a stronger sufficient corollary. Rare arbitrarily fast branches can be harmless if their capture weight shrinks sufficiently rapidly.

---

# 6. WP33 exact low-order-jitter no-go

For any target
\[
\mu_0>0,
\qquad
\sigma^2>0,
\]
there exists a smooth delay family with
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

Therefore exact mean delay and exact RMS jitter do not bound information bandwidth.

Do not claim WP33 simultaneously fixes an arbitrary exact FWHM.

---

# 7. Autonomous-control boundary

A free source-synchronous temporal reference can encode optical arrival phase into an internal/event mark and report it later with arbitrarily slow final registration while preserving timing FI.

Therefore autonomy is a genuine resource assumption. Clocked/gated/heterodyne/lock-in architectures require explicit accounting of clock frequency, phase precision, control action, memory, or equivalent temporal-reference resources.

---

# 8. Thermodynamic no-go + restricted repair

For the finite-state time-homogeneous reversible Markov optical gateway
\[
0\xrightleftharpoons[d]{u}1,
\qquad f=u\pi_0\ge f_*,
\]
with total steady EPR `<=Sigma` and stationary activity `<=A`, define
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

Memorylessness gives, for downstream marks generated from exit destination and later autonomous Markov trajectory,
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

The reverse optical rate `d` is an absolute microscopic rate resource. The rare-fast appendix shows aggregate stationary activity/EPR/throughput plus a fixed optical detailed-balance ratio do not control the local temporal scale if other microscopic nonoptical scales are unbounded.

Important limitation: not every nonoptical bare edge affinity is held fixed in the rare-fast family. The no-go is against the stated aggregate stationary resource set.

---

# 9. Publication frontier

Current manuscript target:

`manuscript/event_resource_theorem_rev3.tex`

Supporting files:
- `manuscript/references.bib`
- `manuscript/appendix_rare_fast_counterexample.tex`
- `docs/MANUSCRIPT_HOSTILE_PROOF_AUDIT_ROUND2.md`
- `notes/RESEARCH_LOG_ROUND12.md`

Branch compile workflow:

`.github/workflows/manuscript-check.yml`

It points to Rev3. The connector has not exposed a completed push-triggered Actions result, so compile success is **not yet verified**.

---

# 10. Novelty status

Verified prior work already includes:
- Köllner & Wolfrum 1992: photon requirements/lifetime estimation;
- Talaga 2009: information-theoretical TCSPC with IRF convolution, information loss, effective bandwidth and sensitivity-bandwidth discussion;
- Bouchet et al. 2019: FI lifetime precision with IRF/background;
- Trinh & Esposito 2021: FI analysis of IRF/photon-statistics resolution;
- Dechant 2026: general finite-frequency fluctuation-response inequality.

Therefore do **not** claim first information-theoretic detector timing analysis or first detector sensitivity-bandwidth result.

Current defensible candidate contribution:

> A resource-completeness theorem for source-modulation information transfer in autonomous marked photodetection event channels, including exact atomic and timing-collision resources and explicit no-go/repair results for low-order jitter moments, free synchronous control, and aggregate stationary thermodynamics.

No equivalent complete theorem stack has been identified in targeted searches. Novelty remains provisional.

---

# 11. Immediate next actions
1. Obtain an actual LaTeX compile result for Rev3 and fix any errors.
2. Final equation/reference cross-check.
3. Add only figures that materially clarify the theorem/counterexamples.
4. Final hostile claim/citation review.
5. Decide whether to prepare submission-ready source/package.
6. Defer non-Poisson/nonclassical sources unless review shows they are required.
7. Keep WP17–24 frozen.

**Latest durable checkpoint:** `notes/RESEARCH_LOG_ROUND12.md`.
