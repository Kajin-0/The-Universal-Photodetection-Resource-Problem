# Research Log — Round 16

**Date:** 2026-08-20

## Objective

Increase the significance and operational scope of the first autonomous-event paper **without broadening its detector model class** or reopening previously frozen side branches.

The starting point was the hostile-referee-hardened Rev6 manuscript. The target was to determine whether the exact sinusoidal Fisher-transfer spectrum

\[
G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm)
\]

could be promoted to a more complete temporal-information object and whether that promotion yielded genuinely stronger operational theorems.

---

# 1. Main conceptual result: sinusoidal theorem is a spectral probe of a complete operator

For arbitrary finite-dimensional weak temporal source perturbations
\[
\Phi_{\boldsymbol\theta}(t)
=\Phi_0\left[1+\sum_{a=1}^{p}\theta_a s_a(t)\right],
\qquad
s_a\in L^2(\mathbb R)\cap L^\infty(\mathbb R),
\]
with Plancherel transforms `S_a`, the ideal marked primary-record Fisher matrix is
\[
\boxed{
[F_{\rm out}]_{ab}
=\frac{\Phi_0}{2\pi}
\int_{-\infty}^{\infty}
G(\omega)S_a^*(\omega)S_b(\omega)d\omega.
}
\]

Therefore multiplication by `G(omega)` is the complete **local weak-waveform Fisher-information transfer operator** for the independent-event detector class.

The original sinusoidal result is its long-observation Fourier-mode specialization.

Status: **PROVED**.

Primary record:
`notes/WP36_COMPLETE_WEAK_WAVEFORM_FISHER_OPERATOR.md`

---

# 2. Regularity of the transfer spectrum

Because each `H_m` is a characteristic function,
\[
|H_m|\le1,
\qquad
H_m(-\omega)=H_m(\omega)^*,
\]
and each `H_m` is continuous. Dominated convergence through the finite capture measure gives
\[
\boxed{
0\le G(\omega)\le\eta,
\qquad
G(-\omega)=G(\omega),
\qquad
G\in C(\mathbb R).
}
\]

This continuity is important because it upgrades almost-everywhere operator statements to clean pointwise frequency statements.

Status: **PROVED**.

---

# 3. Universal weak-waveform Fisher-ordering theorem

For two detectors `A` and `B` in the same theorem class,
\[
\boxed{
G_A(\omega)\ge G_B(\omega)\quad\forall\omega
\iff
F_A\succeq F_B
\text{ for every admissible finite weak temporal waveform task.}
}
\]

Forward implication: the difference of Fisher matrices is the quadratic form of multiplication by `G_A-G_B`.

Converse: if pointwise ordering fails, continuity and evenness produce a finite symmetric frequency region on which `G_A-G_B` is uniformly negative. An `L^1\cap L^2` real-even spectrum supported there has a real bounded square-integrable inverse transform and therefore gives an admissible scalar perturbation for which `F_A<F_B`.

Interpretation:
- if `G_A=G_B` everywhere, the detectors are locally Fisher-equivalent for every weak temporal waveform task in the model;
- if the spectra cross, there is no task-independent Fisher ranking.

Scope warning: this is **not** claimed as generic Blackwell dominance.

Status: **PROVED**.

---

# 4. Exact band-subspace worst-case guarantee

For a scalar perturbation,
\[
\rho_G[s]
=\frac{F_{\rm out}[s]}{F_{\rm in}[s]}
=\frac{\int G(\omega)|S(\omega)|^2d\omega}
{\int |S(\omega)|^2d\omega}.
\]

This is the Rayleigh quotient of the multiplication operator by `G`.

For the compact symmetric band `[-Omega,Omega]`, continuity gives the exact worst-case result
\[
\boxed{
\inf_{s\ne0,\ \operatorname{supp}S\subset[-\Omega,\Omega]}
\rho_G[s]
=
\min_{|\omega|\le\Omega}G(\omega).
}
\]

Therefore preserving at least absolute Fisher fraction `q` for **every admissible weak waveform in the band** is equivalent to
\[
\boxed{G(\omega)\ge q\quad\forall|\omega|\le\Omega.}
\]

Primary record:
`notes/WP36A_BAND_SUBSPACE_FISHER_GUARANTEE.md`

Status: **PROVED**.

---

# 5. Stronger interpretation of the existing inverse resource coefficient

For square-integrable conditional delay densities,
\[
\int_{-\infty}^{\infty}G(\omega)d\omega=\pi\mathfrak R_2.
\]

If `G(omega)>=q` throughout `|omega|<=Omega`, then
\[
\pi\mathfrak R_2\ge2\Omega q.
\]
With ordinary-frequency half-band
\[
B=\frac{\Omega}{2\pi},
\]
this becomes
\[
\boxed{\mathfrak R_2\ge4Bq.}
\]
Since `mathfrak R_2<=mathfrak H`, also
\[
\boxed{\mathfrak H\ge4Bq.}
\]

Thus the same coefficient previously obtained for flat-average retention has a stronger interpretation:

> `4Bq` is also a necessary timing-resource cost for guaranteeing at least `q` Fisher retention for every weak temporal waveform in the full band.

Status: **PROVED**.

---

# 6. Exact Fisher-equivalent bandwidth

For `eta>0`, define the DC-normalized equivalent rectangular Fisher bandwidth
\[
\boxed{
B_{\rm FI}
\equiv
\frac1\eta\int_0^\infty G(2\pi f)df.
}
\]

Using Parseval,
\[
\boxed{
B_{\rm FI}=\frac{\mathfrak R_2}{4\eta}.
}
\]

This is an **information-area bandwidth**, not an electrical amplitude bandwidth and not a relabeled `-3 dB` frequency.

The hazard-collision bound gives
\[
\boxed{
B_{\rm FI}\le\frac{\mathfrak H}{4\eta}.
}
\]

If all captured-event conditional hazards obey a common ceiling `Lambda`, then `mathfrak H<=eta Lambda`, giving
\[
\boxed{B_{\rm FI}\le\frac{\Lambda}{4}.}
\]

For a single exponential delay of rate `Lambda`, equality holds.

Status: **PROVED**.

---

# 7. Independent delay-stage cascade

For independent unresolved unmarked delay-only stages,
\[
H_{12}=H_1H_2,
\qquad
\eta_{12}=\eta_1\eta_2,
\]
so
\[
\boxed{G_{12}(\omega)=G_1(\omega)G_2(\omega).}
\]

This is intentionally narrow. It is **not** generalized to arbitrary retained marks or history-dependent stages.

For `k` independent serial exponential waiting stages of common rate `lambda`,
\[
G_k(\omega)
=\eta\left(\frac{\lambda^2}{\lambda^2+\omega^2}\right)^k.
\]

The exact collision resource is
\[
\boxed{
\frac{\mathfrak R_2}{\eta}
=\lambda\frac{(2k-2)!}{4^{k-1}[(k-1)!]^2}.
}
\]

Therefore
\[
\boxed{
B_{\rm FI}
=\frac{\lambda}{4}
\frac{\binom{2k-2}{k-1}}{4^{k-1}}.
}
\]

Asymptotically,
\[
\boxed{
B_{\rm FI}\sim\frac{\lambda}{4\sqrt{\pi(k-1)}}.
}
\]

This gives an architecture-level interpretation: accumulated unresolved stochastic stages progressively consume equivalent temporal Fisher bandwidth even when each microscopic stage has the same bare rate.

Status: **PROVED** for the stated cascade class.

---

# 8. Proof hardening before final Rev7 validation

Several mathematical-presentation issues were caught and repaired before freezing Rev7:

1. Fourier transforms of arbitrary `L^2 cap L-infinity` perturbations are now defined in the Plancherel sense rather than by an unjustified absolutely convergent integral.
2. Convolution with a probability measure is explicitly used as a contraction on `L^2` and `L-infinity`.
3. Converse/order proofs use finite-measure `L^1 cap L^2` spectral sets whose inverse transforms are admissible; no unsupported claim that every measurable set contains an appropriate smooth compactly supported spectrum is required.
4. Continuity/evenness of `G` converts the detector ordering to a pointwise theorem rather than an a.e.-only presentation.
5. On compact bands the essential infimum becomes an actual minimum.
6. The continuity proof was kept as a regularity result without intentionally disturbing the mature Rev6 hazard-theorem numbering.

Status: **VERIFIED** by final source inspection and CI compilation.

---

# 9. Novelty positioning

Do not claim that Fisher-information transfer functions are generically new. Koppell and Kasevich (Optica 2021, DOI `10.1364/OPTICA.412129`) already use a Fisher-information-based information transfer function in phase imaging.

Do not claim generic detector response metrics are interchangeable; recent photodetector metrology explicitly emphasizes that pulse response, ultrafast transient response, and `-3 dB` bandwidth can probe different dynamics (Deng, Van Thourhout, and Hens, ACS Photonics 2026, DOI `10.1021/acsphotonics.6c00438`).

Defensible Rev7 claim:

> For the autonomous independent-event marked photodetection kernel, the same exact marked-delay spectrum is the complete spectral multiplier of the local weak-temporal-waveform Fisher operator; pointwise ordering of this spectrum is necessary and sufficient for local Fisher dominance over every admissible weak temporal waveform task; and its integrated area yields an exact equivalent Fisher bandwidth tied to collision and local-hazard resources.

The novelty remains strongest in the **combined theorem stack**, not any classical mathematical ingredient in isolation.

---

# 10. Rev7 manuscript integration

Current manuscript:

`manuscript/event_resource_theorem_rev7.tex`

Supporting Rev7 source modules:

- `manuscript/section_waveform_operator_rev7.tex`
- `manuscript/section_operational_bandwidth_rev7.tex`
- `manuscript/appendix_rare_fast_counterexample_rev7.tex`
- `manuscript/apply_rev7.py` — historical assertion-based Rev6->Rev7 generator used during validation; steady-state CI no longer runs it.

Canonical main-source Git blob:

`f59e36e32a2d6eb36752c847cbdd40b07b241db0`

---

# 11. Mechanical verification

## Canonical persistence run

GitHub Actions run:

`32433326375`

Result:

**SUCCESS**

Generation, full LaTeX compilation, artifact upload, and verified-source persistence all succeeded.

## Independent proof-hardened validation

Temporary draft PR:

`#13` — now **CLOSED, UNMERGED**

GitHub Actions run:

`32433375491`

Job:

`96629549205`

Result:

**SUCCESS**

Final independent build:

- PDF: 24 pages;
- PDF size: 360775 bytes;
- artifact ID: `9429898246`;
- artifact ZIP size: 368538 bytes;
- artifact ZIP SHA-256:
  `733262dc3b07b6959c175bbddb5ee1185016500b276dd932061342c75199f276`.

The generated artifact source matched the canonical committed Rev7 source.

The only surviving nontrivial layout warning is the inherited approximately `2.45667 pt` overfull appendix line involving “timing-concentration.” No new Rev7 overfull defect was introduced.

---

# 12. CI cleanup / repository freeze

Temporary PR/self-persistence validation machinery has been removed.

Steady-state workflow:

`.github/workflows/manuscript-check.yml`

Restored in commit:

`8b9118bd7ae428dd51952853c1571624356fdc94`

Steady-state behavior:

- `permissions: contents: read`;
- direct compile of committed `event_resource_theorem_rev7.tex`;
- artifact upload only;
- no `apply_rev7.py` generation;
- no self-commit/push;
- no temporary pull-request validation trigger.

Temporary PR #13 was closed after validation and is not to be merged.

---

# 13. Publication posture after Round 16

The first-paper foundational derivation phase is now **closed by default**.

Rev7 is materially stronger than Rev6 because the central transfer spectrum is now shown to govern arbitrary local weak temporal waveforms, provides a complete local Fisher ordering, yields an exact worst-case band guarantee, and supports an exact information-area bandwidth.

Further expansion into capacity, QFI, coherent pointers, high-flux memory, or general marked multistage networks should be treated as a **second-paper program**, not a requirement for the first manuscript, unless a concrete referee-level defect in Rev7 is identified.

## Next action

Proceed to submission packaging and journal positioning:

1. verify current journal aims/scope and article requirements;
2. choose primary/fallback journal;
3. prepare cover letter and concise significance statement;
4. add author/affiliation metadata when supplied;
5. perform final source/package inventory and reproducibility check;
6. make only scientifically neutral title/abstract polishing if justified.

Status: **REV7 FIRST-PAPER SCIENCE FROZEN FOR SUBMISSION PACKAGING**.
