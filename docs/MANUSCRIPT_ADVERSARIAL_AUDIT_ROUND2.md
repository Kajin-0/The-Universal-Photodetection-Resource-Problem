# Manuscript Adversarial Audit — Round 2

**Date:** 2026-08-20

## Purpose
Hostile referee-style audit of the first event-resource manuscript after WP32. Focus: hidden assumptions, claims stronger than proofs, and novelty wording.

## 1. Exact marked-Poisson transfer

The formula

\[
G(\omega)=\int |H_m(\omega)|^2\,\kappa(dm)
\]

is internally correct for the stated weak sinusoidal modulation of an inhomogeneous Poisson source and an autonomous independent one-primary-event kernel. The factor `1/2` from time averaging cancels exactly between source and output FI.

**Referee risk:** the identity may be viewed as an elementary consequence of standard Poisson marking/displacement theory rather than a standalone novel theorem.

**Recommended framing:** present it as the exact channel lemma on which the resource theorems are built. Reserve novelty language for the atomic/collision/hazard + no-go/repair hierarchy.

## 2. QFI language

For coherent intensity modulation, direct-detection Poisson FI equals the corresponding coherent-state QFI locally, so source normalization is valid.

**Do not generalize** this equivalence to optical phase modulation or nonclassical sources in the first paper.

## 3. Wiener atomic theorem

The high-band Cesaro limit

\[
\lim_{\Omega\to\infty}\frac1{2\Omega}\int_{-\Omega}^{\Omega}|H_m(\omega)|^2d\omega
=\sum_jp_j(m)^2
\]

is classical Wiener theory. The marked photodetection corollary is correct by dominated convergence.

**Recommended novelty wording:** `exact atomic-timing corollary for source-normalized photodetection information`, not a new Fourier theorem.

## 4. Collision resource and spectral concentration

For square-integrable conditional densities,

\[
\int G(\omega)d\omega=\pi\mathfrak R_2
\]

and

\[
\bar\eta_I(\Omega)\le\min\{\eta,\pi\mathfrak R_2/(2\Omega)\}
\]

are correct.

The arbitrary-source bound

\[
\bar\eta_I[w]\le\eta\,\mathcal W(\pi\mathfrak R_2/\eta)
\]

is correct for an absolutely continuous normalized spectral-FI density `w`. Discrete line spectra need a measure-theoretic variant and should be excluded from the first theorem statement.

## 5. Hazard completion

The markwise inequality

\[
2\int f_m^2\le\Lambda(m)
\]

and capture-weighted result

\[
\mathfrak R_2\le\mathfrak H=\int\Lambda(m)\kappa(dm)
\]

are correct.

WP32 is stronger than a global worst-case hazard. A rare branch with huge `Lambda(m)` is harmless if its capture weight makes `mathfrak H` finite. Therefore the manuscript should lead with `mathfrak R_2`/`mathfrak H` and present `sup Lambda` only as a clean microscopic corollary.

## 6. Fixed-jitter no-go

The two-exponential construction rigorously fixes the variance asymptotically. A deterministic shift fixes any prescribed sufficiently large mean without changing `|H|` or the variance. Thus the manuscript may safely claim:

\[
\{\mathbb E D,\operatorname{Var}D\}\text{ fixed}\not\Rightarrow\text{finite information bandwidth}.
\]

The manuscript should explicitly mention the shift if it says the mean is fixed.

The general statement that **any finite collection of moments** is insufficient remains a conjectural extension in WP26 and should not be asserted as proved.

FWHM is correctly criticized as non-resource-complete, but the current construction does not prove a theorem at *fixed prescribed FWHM*. Phrase this as a shape/summary insufficiency statement rather than a fixed-FWHM theorem.

## 7. Clock/control no-go

The synchronous phase-mark construction is correct. It shows that a free external temporal reference can preserve arrival-phase FI while final registration is arbitrarily slow.

**Scope consequence:** autonomy/time-translation covariance is not cosmetic. It is a resource assumption. Do not apply the theorem to lock-in, heterodyne, gated, or clocked detectors without pricing the reference/control system.

## 8. Thermodynamic bridge

The gateway result

\[
\lambda_1\le\frac{\mathcal A d}{f_*}g^{-1}(\Sigma/f_*)
\]

is dimensionally and algebraically correct under WP3 assumptions.

The mark-robust downstream hazard inequality is valid only when the downstream mark does not separately reveal the hidden gateway dwell time. If it does, that timing record must be included in the general marked-kernel accounting.

## 9. Rare-fast thermodynamic no-go — important wording

For

\[
0\xrightleftharpoons[bR]{aR}1,\quad
1\xrightleftharpoons[q]{cR}2,\quad
2\xrightleftharpoons[sR]{p}0,
\]

the exact stationary distribution in the appendix was independently checked against the generator: `W pi = 0` exactly and `sum pi = 1`.

All stationary one-way flows stay finite. The steady edge flux affinities `ln[(W_ij pi_j)/(W_ji pi_i)]` and the total cycle affinity stay finite. The post-capture holding rate `(b+c)R` diverges.

However, some **bare nonoptical rate ratios** such as `cR/q` and `sR/p` diverge individually. This is not a flaw; it identifies the omitted microscopic edge-scale/energetic resource. But the manuscript must not say that all microscopic local-detailed-balance forces or all bare edge affinities are fixed.

Safe conclusion:

> bounded stationary EPR, stationary activity, throughput, and fixed optical detailed-balance ratio do not bound absolute post-capture speed unless an additional microscopic rate/edge-scale resource is supplied.

## 10. Prior-art boundary

Closest identified work:

- Köllner–Wolfrum 1992: FI/CRLB photon requirements for fluorescence lifetime;
- Talaga 2009: information-theoretical TCSPC, explicit IRF convolution, information loss, detector sensitivity–bandwidth language and IRF spectral response;
- later FLIM FI/IRF papers;
- standard marked/filtered Poisson-process and Poisson-channel literature;
- Dechant 2026 finite-frequency fluctuation-response inequality.

No located result reproduces the complete WP32 + Wiener + collision/hazard + jitter/clock + thermodynamic no-go/repair stack.

**Do not claim:** first use of information theory for detector bandwidth, first FI treatment of IRFs, first marked-Poisson FI, first hazard theorem, or first thermodynamic detector tradeoff.

**Defensible provisional claim:** a new photodetection-specific resource-completeness theorem stack for autonomous event channels.

## 11. Build issue found

The current TeX source contains the literal typo

```tex
=rac{\Lambda}{\Omega}...
```

instead of `\frac`. The exact fix and appendix/citation insertions are recorded in `manuscript/BUILD_AND_PROOF_FIXES_ROUND2.md` and scripted in `manuscript/apply_round2_fixes.py`.

## Overall assessment

**Scientific theorem stack: STRONG / internally consistent within scope.**

**Main remaining risks before submission:**

1. novelty overclaim;
2. failing to state autonomy and complete-mark assumptions prominently enough;
3. conflating stationary thermodynamic constraints with fixed microscopic edge forces;
4. overclaiming arbitrary finite-moment/FWHM no-go results;
5. mechanical LaTeX integration/build issues.

No central theorem counterexample or prefactor error was found in this audit.
