# Research Roadmap — Publication Closure Phase

**Updated:** 2026-08-20

## Guiding principle
The project has converged from a broad universal-resource search to a detector-class-specific **no-go + repair/resource-completeness program**.

For the first paper, do not reopen material-specific, coherent-pointer, analog-detector, or non-Poisson branches unless a concrete defect in the autonomous event theorem requires it.

The current question is no longer “what other physics can be added?” It is:

> Is the autonomous marked-event theorem stated with the smallest defensible assumptions, are every claim and citation publication-safe, and is the source package mechanically reproducible?

---

# Core metric
For weak coherent/Poisson direct-detection intensity modulation, normalize electrical-record Fisher information by the incident Poisson FI of the same source parameter.

Critical distinction:
\[
\boxed{
\text{latency}\neq\text{amplitude bandwidth}\neq\text{information bandwidth}.
}
\]

Known deterministic delay and invertible deterministic filtering do not by themselves imply FI loss.

---

# Branch E — autonomous proper event detectors

## E0 — Exact marked-event kernel
**Status: PROVED**

Per incident photon,
\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\qquad \eta=\kappa(\mathsf M)\le1.
\]

For the complete accessible primary-event mark,
\[
\boxed{
G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm).
}
\]

Parameter-independent background and downstream processing cannot increase FI.

Primary note: `notes/WP32_GENERAL_MARKED_POISSON_EVENT_KERNEL_THEOREM.md`.

## E1 — Structural high-band obstruction
**Status: PROVED**

Wiener theory gives the exact capture-weighted atomic residue
\[
\boxed{
\lim_{\Omega\to\infty}\frac1{2\Omega}
\int_{-\Omega}^{\Omega}G(\omega)d\omega
=
\int\kappa(dm)\sum_jp_j(m)^2.
}
\]

Purely non-atomic conditional delay laws therefore force the flat-band **average** transfer to vanish asymptotically.

Primary note: `notes/WP30_WIENER_ATOMIC_DELAY_INFORMATION_THEOREM.md`.

## E2 — Quantitative collision resource
**Status: PROVED**

For square-integrable conditional delay densities,
\[
\boxed{
\mathfrak R_2=2\int\kappa(dm)\int f_m^2dt,
\qquad
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

Primary notes: WP26, WP28, WP32.

## E3 — Microscopic local-rate resource
**Status: PROVED WITH WP35 CORRECTION**

If `h_m(t)<=Lambda(m)`, define
\[
\boxed{
\mathfrak H=\int\Lambda(m)\kappa(dm).
}
\]
Then
\[
\boxed{\mathfrak R_2\le\mathfrak H.}
\]

The capture-weighted resource `mathfrak H` is preferred to a global worst-case hazard.

For a finite-state CTMC, the safe generic uniform bound after complete mark conditioning is
\[
\boxed{
q_{\max}=\max_{x\in S_{\rm pre}}\sum_{y\ne x}W_{yx},
}
\]
provided the accessible mark does not independently record the realized pre-registration holding times.

The older registration-edge-only bound is rejected. The generic quantum-jump operator-norm sentence is deferred rather than asserted in the first manuscript.

Primary note: `notes/WP35_MARK_CONDITIONED_MARKOV_RATE_CORRECTION.md`.

## E4 — Operational inverse cost
**Status: PROVED**

For ordinary-frequency half-band `B=Omega/(2pi)` and required absolute average transfer `q`,
\[
\boxed{
q\le\eta,
\qquad
\mathfrak R_2\ge4Bq,
\qquad
\mathfrak H\ge4Bq.
}
\]

For a common per-captured-event hazard ceiling,
\[
\boxed{
\Lambda\ge\frac{4Bq}{\eta}.
}
\]
For relative retention `q=r eta`,
\[
\boxed{\Lambda\ge4Br.}
\]

Primary note: `notes/WP34_MINIMUM_TIMING_RESOURCE_COST_THEOREM.md`.

## E5 — Resource insufficiency/no-go layer
**Status: PROVED FOR THE CLAIMS USED IN THE MANUSCRIPT**

- Exact mean delay + exact variance/RMS jitter do not bound information bandwidth: WP33.
- A free synchronous temporal reference defeats a detector-only timing bound: WP27.
- Stationary EPR/activity/throughput do not supply an absolute microscopic time scale: WP4/WP29 rare-fast no-go/repair.
- Deterministic delay is latency, not information loss.
- Downstream parameter-independent processing cannot improve the primary-record FI.

Do not overstate FWHM: no theorem is claimed for holding an arbitrary exact FWHM fixed while bandwidth diverges.

---

# Thermodynamic completion
**Status: PROVED FOR THE RESTRICTED GATEWAY CLASS**

For the finite-state time-homogeneous reversible gateway
\[
0\xrightleftharpoons[d]{u}1,
\]
with forward traffic `f>=f_*`, total EPR `<=Sigma`, and stationary one-way activity `<=A`, WP29 gives
\[
\boxed{
\lambda_1\le
\Lambda_*
=\frac{\mathcal A d}{f_*}g^{-1}(\Sigma/f_*),
\qquad
g(z)=(1-z^{-1})\ln z.
}
\]

Here `lambda1` is the **total first-exit rate** from the gateway state, so the bridge is already consistent with WP35.

The absolute reverse optical rate `d` remains an independent microscopic resource. Temperature enters only through a separately justified microscopic rate/coupling law.

---

# Other detector classes

## Continuous classical/Markov analog detectors
**Status: FROZEN FOR PAPER 1**

General finite-frequency response/noise inequalities are close prior art. Reopen only if a distinct photodetection-specific theorem is required.

## Coherent quantum pointers
**Status: FROZEN FOR PAPER 1**

WP7/WP8 show that interaction action alone is insufficient and that apparatus preparation/generator resources matter. This is scientifically distinct from the autonomous one-event theorem and should not be forced into the first manuscript.

## HgCdTe/Kane material branch WP17–24
**Status: FROZEN**

Useful as validation/examples, not needed for theorem closure. Do not resume the 6-to-8-band or nonradiative dark-mechanism calculations merely to expand the manuscript.

---

# Publication state

## Rev4
`manuscript/event_resource_theorem_rev4.tex`

**Status: FULL BUILD VERIFIED** for commit `0acd8ca6304585e44c89130ca6b31826884c85a8`.

Rev4 contains one later-discovered WP35 wording defect in its generic microscopic-rate paragraph.

## Rev5
`manuscript/apply_rev5.py`

**Status: EDITORIAL CORRECTION STAGED / BUILD GATE TRIGGERED**.

Rev5 changes only:

1. WP35 total-pre-registration-escape-rate wording;
2. removal of the generic quantum-jump sentence;
3. explicit prose references to both figures;
4. a versioned hierarchy figure whose final layer is described as a local-rate resource rather than a rate/operator resource.

No central theorem or numerical constant is changed.

---

# Remaining gates

## Gate P1 — Rev5 mechanical verification
Generate and compile Rev5 with the existing clean GitHub Actions workflow. Inspect the first fatal line if it fails. Do not reintroduce steady-state self-commit or issue-comment side effects.

## Gate P2 — Final claim/reference audit
Audit every externally comparative or novelty-bearing sentence. In particular:

- keep TCSPC/IRF prior-art claims conservative;
- keep Dechant comparison equation-level and noncompetitive;
- reserve novelty for the combined resource-completeness stack;
- preserve the exact detector-class restrictions;
- ensure WP35 wording is the only generic classical microscopic-rate statement;
- verify both figures are explicitly referenced and add scientific information rather than decoration.

## Gate P3 — Submission package
If P1 and P2 pass without substantive defects, prepare the submission-ready source/package. At that point, additional foundational research is not the default next action.
