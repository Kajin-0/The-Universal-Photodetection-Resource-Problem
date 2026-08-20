# Research Log — Round 11

**Date:** 2026-08-20

## Purpose

Durable checkpoint after the event-detector branch was compressed into a theorem hierarchy and directly reconnected to the original thermodynamic no-go/repair question.

The repository, not chat history, is authoritative.

---

# 1. WP29 — thermodynamic bridge completed

The old WP3 reversible optical-gateway theorem has now been composed directly with WP25/WP28.

WP3 gives

\[
\pi_1\ge\frac{f_*}{dZ_*},
\qquad
Z_*=g^{-1}(\Sigma/f_*),
\]

and therefore

\[
\lambda_1\le
\Lambda_*
=\frac{\mathcal A dZ_*}{f_*}.
\]

The new mark-robust lemma proves that if no electrical registration occurs before the first exit from state 1, then for any autonomous downstream mark and delay,

\[
h_D(t|M)\le\lambda_1.
\]

Hence

\[
\Lambda_{cond}\le\Lambda_*.
\]

WP25 then gives

\[
\boxed{
\bar\eta_I(\Omega_s)
\le
C\min\left[
1,
\frac{\pi\mathcal A d}{2f_*\Omega_s}
 g^{-1}(\Sigma/f_*)
\right].
}
\]

WP28 gives the arbitrary-source version

\[
\boxed{
\bar\eta_I[w]
\le
C\,\mathcal W\!\left(
\pi\frac{\mathcal A d}{f_*}
 g^{-1}(\Sigma/f_*)
\right).
}
\]

WP4 remains the complementary no-go: remove the absolute local/microscopic rate scale and bounded temperature/EPR/activity/throughput do not imply finite information bandwidth.

**Interpretation:** thermodynamics is conditional, not standalone. It can convert a bounded microscopic rate scale into a finite information-bandwidth ceiling but cannot create the absolute scale itself.

Primary note: `notes/WP29_THERMODYNAMIC_BRIDGE_TO_REGISTRATION_INTENSITY.md`.

---

# 2. WP30 — hazard is not mathematically minimal

A stronger minimality audit used Wiener's classical theorem for the Fourier transform of a finite measure.

For registration-delay measure `mu` with atomic masses `p_j`,

\[
\boxed{
\lim_{\Omega\to\infty}
\frac1{2\Omega}\int_{-\Omega}^{\Omega}|H(\omega)|^2d\omega
=\sum_jp_j^2.
}
\]

Therefore the asymptotic flat-band information residual is exactly the squared atomic timing mass.

For complete accessible mark `M`,

\[
\boxed{
\lim_{\Omega\to\infty}\bar\eta_I(\Omega)
=\eta_c\,\mathbb E_M\left[\sum_jp_j(M)^2\right].
}
\]

Thus:

- purely non-atomic conditional delays imply asymptotic average information loss even without bounded hazard or finite `L2` density;
- deterministic/discrete timing branches leave a nonzero information residue;
- a mark revealing a deterministic branch can restore full high-frequency timing information.

This produces the correct hierarchy:

\[
\text{finite hazard}
\Rightarrow
R_2<\infty
\Rightarrow
\text{non-atomic delay}
\Rightarrow
\bar\eta_I\to0.
\]

The converses fail.

Primary note: `notes/WP30_WIENER_ATOMIC_DELAY_INFORMATION_THEOREM.md`.

---

# 3. WP31 — resource necessity matrix

The event-branch primitive list was compressed further.

### Necessary for well-posedness

- normalized finite source-information task;
- complete accessible record/mark specification.

### Exact asymptotic structural obstruction

- mark-conditioned atomic timing mass.

### Quantitative timing resources

- finite `R2` is sufficient for an integrated spectral budget;
- finite local conditional hazard `Lambda` is a physically interpretable microscopic sufficient condition with `R2<=Lambda`.

### Rejected primitive resources

- mean latency;
- deterministic transit time;
- RMS/FWHM jitter;
- RC `-3 dB` amplitude bandwidth;
- stationary EPR/activity without an absolute local rate scale.

### Not required for the intrinsic upper speed bound

- dark/background events;
- downstream electronics;
- nontrivial optical capture theorem beyond the trivial `C<=1`, unless a stronger sensitivity bound is desired.

### Separate-class resource

- external clock/control; WP27 proves free synchronous phase memory defeats autonomous timing bounds.

### Parallelism

Source-normalized efficiency is extensive correctly. Identical replication does not increase the normalized performance ratio. Multiple primary routes require bounding their total local intensity, not each route separately.

Primary note: `notes/WP31_EVENT_BRANCH_RESOURCE_NECESSITY_MATRIX.md`.

---

# 4. Literature audit update

Targeted searches were performed in:

- reliability/hazard literature;
- first-passage literature;
- Poisson communication channels;
- random-delay communication/remote estimation;
- detector timing-jitter / IRF literature;
- FI-based TCSPC/FLIM literature.

Located prior work confirms that all ingredients individually are standard:

- hazard/survival functions;
- Poisson FI;
- IRF convolution;
- timing jitter and correction;
- random-delay point-process/channel models;
- Wiener harmonic-analysis theorem.

The FI-based FLIM literature explicitly computes CRLB degradation from finite IRFs and background, but the searches did not locate a theorem equivalent to the WP25–30 stack: a source-normalized optical timing-information bound controlled by conditional first-registration intensity / timing collision concentration, together with the exact atomic high-bandwidth residual.

This remains a provisional novelty conclusion, not a first-of-kind claim.

An older report by Efron and Johnstone titled *Fisher's Information in Terms of the Hazard Rate* exists, so title-level overlap must be handled carefully. Its subject is statistical Fisher information of lifetime distributions expressed through hazards; it should not be confused with the WP25 source-to-detector spectral information-transfer theorem.

---

# 5. Strategic conclusion

The autonomous proper-event branch is now close to logical closure.

The central answer is no longer an oversized list of detector resources. It is a hierarchy:

\[
\boxed{
\text{source spectral information}
+\text{registration timing structure}
\Longrightarrow
\text{information-transfer ceiling}.
}
\]

Microscopic detector physics enters by bounding timing structure:

\[
\boxed{
\text{local rate/operator norm}
\Rightarrow
\Lambda
\Rightarrow
R_2
\Rightarrow
\text{spectral ceiling}.
}
\]

Restricted thermodynamics enters one level earlier:

\[
\boxed{
\text{EPR/activity/throughput}
+\text{absolute microscopic rate scale}
\Rightarrow
\Lambda_*.
}
\]

Without the absolute local scale, WP4 proves no finite thermodynamic speed theorem.

---

# 6. Highest-value next work

1. Finish the theorem-level novelty audit, especially older first-passage/random-delay channel literature.
2. Produce a compact theorem/counterexample manuscript skeleton and test whether every headline claim is supported without overselling.
3. Decide whether extension beyond coherent/Poisson direct detection is required for the first paper or should be deferred.
4. Keep WP17–24 HgCdTe material work frozen.

**Status:** central event theorem stack substantially closed; novelty/publication gate remains.