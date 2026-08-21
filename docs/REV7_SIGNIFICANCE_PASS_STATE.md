# Rev7 Significance Pass — Current State

**Date:** 2026-08-20

## Purpose

Record the deliberate reopening of the first-paper manuscript for a significance upgrade after Rev6 had already passed hostile-referee hardening.

Rev6 remains the last frozen build-verified publication candidate until Rev7 independently passes generation, full LaTeX compilation, and artifact inspection.

The Rev7 pass does **not** broaden the physical detector class. It strengthens the interpretation and operational reach of the existing autonomous independent-event theorem.

---

## New theorem-grade content

### 1. Complete weak-waveform Fisher operator

For

\[
\Phi_{\boldsymbol\theta}(t)
=\Phi_0\left[1+\sum_{a=1}^{p}\theta_a s_a(t)\right],
\qquad
s_a\in L^2\cap L^\infty,
\]

Rev7 adds

\[
\boxed{
[F_{\rm out}]_{ab}
=\frac{\Phi_0}{2\pi}
\int G(\omega)S_a^*(\omega)S_b(\omega)d\omega,
}
\]

where the same

\[
G(\omega)=\int|H_m(\omega)|^2\kappa(dm)
\]

appears as in Rev6.

Interpretation: `G` is the spectral multiplier of the complete local weak-temporal-waveform Fisher operator. The sinusoidal theorem is a Fourier-mode specialization, not the fundamental source restriction.

### 2. Complete detector ordering

For two detectors `A` and `B` in the same theorem class,

\[
\boxed{
G_A(\omega)\ge G_B(\omega)\ \text{a.e.}
\iff
F_A\succeq F_B
}
\]

for every finite admissible weak temporal perturbation family.

Thus `G` completely orders detectors for all local weak temporal estimation tasks in the model. Crossing spectra mean no task-independent ordering exists.

### 3. Exact band-subspace guarantee

For scalar perturbation spectrum `S`,

\[
\rho_G[s]
=\frac{\int G|S|^2}{\int |S|^2}.
\]

For spectra supported in `E`, the exact worst/best retentions are

\[
\boxed{
\inf \rho_G=\operatorname*{ess\,inf}_{E}G,
\qquad
\sup \rho_G=\operatorname*{ess\,sup}_{E}G.
}
\]

Therefore retaining at least `q` Fisher information for **every** weak waveform in `|omega|<=Omega` is equivalent to `G>=q` almost everywhere on the band.

Combining with Parseval yields the same resource coefficient as Rev6,

\[
\boxed{
\mathfrak R_2\ge4Bq,
\qquad
\mathfrak H\ge4Bq,
}
\]

but now with the stronger interpretation that it is also a necessary cost for a universal band-limited waveform guarantee, not merely a flat-average task.

### 4. Exact Fisher-equivalent bandwidth

For square-integrable conditional delay densities,

\[
\boxed{
B_{\rm FI}
=\frac1\eta\int_0^\infty G(2\pi f)df
=\frac{\mathfrak R_2}{4\eta}.
}
\]

Hence

\[
\boxed{
B_{\rm FI}\le\frac{\mathfrak H}{4\eta}.
}
\]

For a common hazard ceiling,

\[
\boxed{B_{\rm FI}\le\Lambda/4.}
\]

The exponential delay saturates the last bound.

### 5. Independent timing-stage cascade

For independent unmarked delay-only stages,

\[
\boxed{G_{12}=G_1G_2.}
\]

For `k` serial exponential stages of rate `lambda`,

\[
G_k(\omega)
=\eta\left(\frac{\lambda^2}{\lambda^2+\omega^2}\right)^k,
\]

\[
\frac{\mathfrak R_2}{\eta}
=\lambda\frac{(2k-2)!}{4^{k-1}[(k-1)!]^2},
\]

and

\[
B_{\rm FI}
=\frac{\lambda}{4}
\frac{\binom{2k-2}{k-1}}{4^{k-1}}
\sim\frac{\lambda}{4\sqrt{\pi(k-1)}}.
\]

---

## Manuscript implementation

New files:

- `notes/WP36_COMPLETE_WEAK_WAVEFORM_FISHER_OPERATOR.md`
- `notes/WP36A_BAND_SUBSPACE_FISHER_GUARANTEE.md`
- `manuscript/section_waveform_operator_rev7.tex`
- `manuscript/section_operational_bandwidth_rev7.tex`
- `manuscript/figure_resource_hierarchy_rev7.tex`
- `manuscript/apply_rev7.py`

`apply_rev7.py` is assertion-based. It reads frozen `event_resource_theorem_rev6.tex`, writes `event_resource_theorem_rev7.tex`, and copies the Rev6 rare-fast appendix to the versioned Rev7 appendix.

The Rev7 title becomes:

> Temporal Information Transfer and Resource Bounds in Autonomous Photodetection Event Channels

The abstract and prior-work positioning are updated to emphasize the complete weak-waveform operator and detector ordering while explicitly avoiding a generic priority claim for Fisher-information transfer functions.

Two literature additions are included:

- Koppell and Kasevich, *Optica* 8, 493–501 (2021), DOI `10.1364/OPTICA.412129` — prior FI information-transfer-function concept in phase imaging;
- Deng, Van Thourhout, and Hens, *ACS Photonics* 13, 1752–1756 (2026), DOI `10.1021/acsphotonics.6c00438` — current photodetector response-time non-equivalence motivation.

---

## Mechanical state

`.github/workflows/manuscript-check.yml` has temporarily been changed from direct Rev6 compilation to:

1. checkout;
2. run `python manuscript/apply_rev7.py`;
3. compile generated `event_resource_theorem_rev7.tex`;
4. upload the Rev7 PDF, generated main TeX, versioned appendix, and new section files.

The workflow remains `contents: read`; it does not self-commit or mutate the branch.

**Important:** the available GitHub connector in the current agent session does not expose listing of push-triggered workflow runs, so a final success/failure run ID has not yet been retrieved here. Do not call Rev7 build-verified until a workflow run or equivalent local compile is explicitly inspected.

Latest manuscript-triggering integration commits include:

- `ccd4304fd899da00862346a7be22d68211a9dc62` — switch CI to generated Rev7;
- `f6e540ee627c8880767a6879b12a8f19135aaee2` — place operational section after hazard theorem;
- `2e32cbef556b8e28ffc31097b5ed9b3f37ab3e6e` — add universal band-subspace resource interpretation.

---

## Novelty posture

Do not claim:

- generic invention of Fisher-information transfer functions;
- arbitrary waveform theory beyond local weak direct-detection intensity perturbations;
- high-flux/history-dependent detector completeness;
- generic channel capacity;
- universal all-photodetector speed ordering.

Defensible Rev7 claim:

> In the autonomous independent-event direct-detection class, the exact marked-delay spectrum `G(omega)` is the complete local weak-temporal-waveform Fisher multiplier; its pointwise ordering is necessary and sufficient for universal Fisher dominance, while atomic timing, timing collision, and capture-weighted hazard resources constrain its high-frequency residue, total spectral area, equivalent information bandwidth, and universal band-limited retention.

---

## Next gate

1. Obtain and inspect the Rev7 CI run/log/artifact.
2. Repair only concrete generation/LaTeX/layout defects.
3. Adversarially review the new operator/order/bandwidth statements.
4. If clean, persist the generated Rev7 main source and versioned appendix or otherwise freeze the deterministic generator as the canonical source path.
5. Then update `AGENTS.md`, `CURRENT_RESEARCH_STATE.md`, `ROADMAP.md`, and README from Rev6 to Rev7 publication state.

Until gate 1–3 pass, Rev6 remains the last mechanically validated publication candidate.
