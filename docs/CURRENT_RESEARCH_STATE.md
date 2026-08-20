# Current Research State

**Date:** 2026-08-20

This is the first-stop replacement-agent summary. **The repository, not chat history, is authoritative.**

## Read first
1. `AGENTS.md`
2. `notes/RESEARCH_LOG_ROUND13.md`
3. `docs/MANUSCRIPT_REV4_INTEGRATION_AUDIT.md`
4. `manuscript/event_resource_theorem_rev3.tex`
5. `manuscript/apply_rev4.py`
6. `notes/WP34_MINIMUM_TIMING_RESOURCE_COST_THEOREM.md`
7. `notes/WP32_GENERAL_MARKED_POISSON_EVENT_KERNEL_THEOREM.md`
8. `notes/WP33_EXACT_FIXED_MEAN_VARIANCE_JITTER_NO_GO.md`
9. `notes/WP29_THERMODYNAMIC_BRIDGE_TO_REGISTRATION_INTENSITY.md`
10. `notes/WP30_WIENER_ATOMIC_DELAY_INFORMATION_THEOREM.md`
11. `notes/WP31_EVENT_BRANCH_RESOURCE_NECESSITY_MATRIX.md`
12. `docs/MANUSCRIPT_HOSTILE_PROOF_AUDIT_ROUND2.md`
13. `docs/NOVELTY_AUDIT_ROUND5_EVENT_THEOREM_STACK.md`
14. `manuscript/references.bib`
15. `manuscript/appendix_rare_fast_counterexample.tex`

Detailed HgCdTe/Kane WP17–24 is **frozen**.

---

# 1. Central objective
Determine the smallest physical resource set that bounds source-normalized optical-to-electrical temporal information transfer for a precisely stated photodetector class, and prove insufficiency by explicit counterexample when proposed resources are omitted.

The mature answer is for **autonomous, independent-event, one-primary-registration photodetection of weak coherent/direct-detection intensity modulation**.

Do not describe the current result as a universal all-detector speed limit.

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

Any parameter-independent background addition or downstream processing cannot exceed `G` by FI data processing.

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

Purely non-atomic conditional timing gives zero asymptotic **flat-band average** transfer. Do not strengthen this into a general pointwise Fourier-decay claim.

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
=\Lambda/2,
\]
because `d(S^2)/dt=-2hS^2`.

A uniform global hazard is only a stronger sufficient corollary. Rare arbitrarily fast branches can be harmless if their capture weight shrinks sufficiently rapidly.

---

# 6. WP34 inverse resource cost

For flat two-sided task `|omega|<=Omega`, define ordinary-frequency half-band
\[
B=\frac{\Omega}{2\pi}.
\]

A target absolute average transfer `q` requires `q<=eta` and
\[
\boxed{
\mathfrak R_2\ge4Bq,
\qquad
\mathfrak H\ge4Bq.
}
\]

For uniform markwise hazard ceiling `Lambda`,
\[
\boxed{
\Lambda\ge\frac{4Bq}{\eta}.
}
\]

For retention `q=r eta` relative to captured DC information,
\[
\boxed{\Lambda\ge4Br.}
\]

This is an exact inversion of the established upper bound and introduces no new detector assumption.

---

# 7. WP33 exact low-order-jitter no-go

For any target
\[
\mu_0>0,
\qquad
\sigma^2>0,
\]
there is a smooth delay family with exactly
\[
\boxed{
\mathbb ED=\mu_0,
\qquad
\operatorname{Var}D=\sigma^2
}
\]
for every selected family member while
\[
|H_D(\omega)|^2\to1
\]
uniformly on every prescribed finite frequency band.

Therefore exact mean delay and exact RMS jitter do not bound information bandwidth.

Do not claim WP33 simultaneously fixes an arbitrary exact FWHM.

---

# 8. Autonomous-control boundary

A free source-synchronous temporal reference can encode optical arrival phase into an internal/event mark and report it later with arbitrarily slow final registration while preserving timing FI.

Therefore autonomy is a genuine resource assumption. Clocked/gated/heterodyne/lock-in architectures require explicit accounting of clock frequency, phase precision, control action, memory, or equivalent temporal-reference resources.

---

# 9. Thermodynamic no-go + restricted repair

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

# 10. Publication frontier

## Verified scientific base

`manuscript/event_resource_theorem_rev3.tex`

Rev3 is the fully reconstructed and line-by-line audited scientific source. It includes the rare-fast appendix and the current conservative novelty/scope statements.

## Rev4 deterministic candidate

`manuscript/apply_rev4.py`

generates `event_resource_theorem_rev4.tex` from Rev3.

Rev4 adds:
- TikZ/pgfplots dependencies;
- `figure_resource_hierarchy.tex`;
- WP34 minimum resource-cost corollary;
- `figure_jitter_no_go.tex`;
- one Discussion sentence highlighting the inverse cost.

Generator Python syntax: VERIFIED.
Generator exact anchors against Rev3: VERIFIED.

### Figures

`manuscript/figure_resource_hierarchy.tex`

Final form shows the source -> autonomous kernel -> primary record plus the three intrinsic timing-resource layers. Clock/control is left to its separate theorem.

`manuscript/figure_jitter_no_go.tex`

Shows exact WP33 families with common mean `mu0=2 sigma` and exact variance `sigma^2`; CSV data were checked against the analytic formula.

Both final figures:
- compile locally in a minimal RevTeX document;
- pass visual overlap/clipping inspection;
- produce no overfull/underfull warnings in that test.

### Full build status

`.github/workflows/manuscript-check.yml` safely generates and compiles Rev4 and uploads artifacts on an ordinary observable branch push.

Connector-authored commits in this session have not exposed a push-triggered Actions run. Temporary self-report/persistence experiments were removed.

Therefore **full bibliography-resolved Rev4 compile remains an open mechanical gate**. Do not claim success until a real build result is inspected.

Supporting audit:

`docs/MANUSCRIPT_REV4_INTEGRATION_AUDIT.md`

Latest log:

`notes/RESEARCH_LOG_ROUND13.md`

---

# 11. Novelty status

Verified prior work already includes:
- Köllner & Wolfrum 1992: photon requirements/lifetime estimation;
- Talaga 2009: information-theoretical TCSPC with IRF convolution, information loss, effective bandwidth and sensitivity-bandwidth discussion;
- Bouchet et al. 2019: FI lifetime precision with IRF/background;
- Trinh & Esposito 2021: FI analysis of IRF/photon-statistics resolution;
- Dechant 2026: general finite-frequency fluctuation-response inequality.

Therefore do **not** claim first information-theoretic detector timing analysis or first detector sensitivity-bandwidth result.

Current defensible candidate contribution:

> A resource-completeness theorem for source-modulation information transfer in autonomous marked photodetection event channels, including exact atomic and timing-collision resources, a minimum timing-resource cost, and explicit no-go/repair results for low-order jitter moments, free synchronous control, and aggregate stationary thermodynamics.

No equivalent complete theorem stack has been identified in targeted searches. Novelty remains provisional.

---

# 12. Immediate next actions
1. Obtain an observable complete Rev4 LaTeX build result when possible.
2. Final line-by-line claim/reference audit of generated Rev4.
3. Keep only the two theorem figures unless a third figure clearly adds scientific information.
4. Decide whether to prepare submission-ready source/package.
5. Defer non-Poisson/nonclassical sources unless review shows they are required.
6. Keep WP17–24 frozen.

**Latest durable checkpoint:** `notes/RESEARCH_LOG_ROUND13.md`.
