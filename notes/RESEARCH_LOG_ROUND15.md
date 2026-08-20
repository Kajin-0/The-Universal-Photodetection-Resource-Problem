# Research Log — Round 15

**Date:** 2026-08-20

## Purpose

Checkpoint the targeted Rev6 revision produced after an independent extreme adversarial review of Rev5.

The review found no failure of the central event-channel theorem stack. It recommended moderate revision because of one model-class seam, one stochastic-thermodynamics terminology problem, and two formal/self-containedness issues.

No frozen research branch was reopened.

---

## 1. Core theorem stack survived the hostile review

The reviewer independently checked and accepted:

- exact marked-Poisson Fisher-information transfer;
- Wiener atomic timing residue;
- Parseval timing-collision sum rule;
- hazard--collision inequality;
- fixed-mean/fixed-variance timing no-go;
- synchronous-clock counterexample;
- restricted thermodynamic gateway algebra;
- rare-fast stationary-thermodynamic counterexample.

No theorem coefficient or headline resource bound was changed in Rev6.

The operational results remain

\[
\mathfrak R_2\ge 4Bq,
\qquad
\mathfrak H\ge 4Bq,
\]

and, for a common conditional-hazard ceiling,

\[
\Lambda\ge\frac{4Bq}{\eta},
\qquad
q=r\eta\Rightarrow\Lambda\ge4Br.
\]

---

## 2. Rev6 mandatory referee repairs

### A. Stationary CTMC -> independent-event bridge

Rev5 moved too quickly from stationary CTMC traffic/EPR/activity to the per-photon event theorem.

Rev6 now explicitly states the isolated-event/low-overlap reduction:

1. stationary baseline thermodynamic quantities constrain microscopic CTMC rates;
2. condition on an isolated optical capture that places the gateway in state 1;
3. the subsequent autonomous CTMC supplies the per-photon post-capture delay law `mu_m`;
4. the information bound is claimed only when successive source events are sufficiently separated that occupancy/recovery do not make capture probability or the post-capture kernel history dependent.

If capture/recovery is history dependent, the independent-event kernel and the thermodynamic information bound are explicitly not claimed.

### B. “Reversible” terminology removed

The nonequilibrium CTMCs have nonzero currents/EPR and therefore are not reversible in the standard detailed-balance sense.

Rev6 uses **bidirectionally connected** and defines it as reverse-transition support for transitions used in thermodynamic accounting. This correction is propagated through the abstract, thermodynamic section, main-text rare-fast discussion, and versioned appendix.

### C. Exact DC normalization

The source-FI rate `Phi_0/2` is stated to assume nonzero sinusoidal frequency. At exact DC the incident FI rate is `Phi_0`; the same factor changes in the output FI so normalized transfer remains `G(0)=eta`.

### D. Self-contained `q_max` proof

For a pre-registration CTMC state `x`,

\[
\lambda_x=\sum_{y\ne x}W_{yx},
\qquad
q_{\max}=\max_x\lambda_x.
\]

The first holding time is `Exp(lambda_x)` and is independent of exit destination and subsequent Markov trajectory. Under the mark restriction,

\[
D\mid(M,x)=T_x+Y_{M,x},\qquad Y_{M,x}\ge0,
\]

which gives `f <= lambda_x S`, hence

\[
h_D(t\mid M,x)\le\lambda_x\le q_{\max}.
\]

Mixing over the initial pre-registration state preserves `f <= q_max S`.

### E. FWHM wording

Rev6 explicitly states that no fixed-FWHM counterexample is claimed; scalar FWHM requires shape assumptions before it can function as a resource summary.

---

## 3. Versioned files

Historical Rev5 remains frozen.

Rev6 files:

- `manuscript/event_resource_theorem_rev6.tex`
- `manuscript/appendix_rare_fast_counterexample_rev6.tex`
- `manuscript/apply_rev6.py`
- `manuscript/apply_rev6_layout_fix.py`
- `docs/MANUSCRIPT_REV6_REFEREE_REPAIR_AUDIT.md`

---

## 4. Mechanical verification

The terminology-complete Rev6 referee-repair state passed GitHub Actions generation, full LaTeX compilation, artifact upload, and source persistence for trigger commit

`7e67f03c6caf60e090458ecf2f96334199adc701`.

A later layout-only pass split an overlong boxed thermodynamic conclusion across two lines. The final-layout run for trigger commit

`4009049562838ee33ff8c9c18fdbe072b933ff57`

also succeeded and persisted the corrected source.

The previous ~59 pt overfull box was eliminated. The remaining reported overfull box is only ~2.46 pt in Appendix A and is not scientifically significant.

Steady-state CI has been restored to read-only permissions and directly compiles committed Rev6. It has no self-commit or issue-comment behavior.

---

## 5. Publication posture

**Rev6 is the current first-paper publication candidate.**

The strongest technically credible hostile-referee objections identified in the external review have been addressed without changing the core theorem stack.

Do not reopen HgCdTe/Kane, coherent-pointer, analog-detector, or non-Poisson branches merely to enlarge this paper.

The next default task is submission packaging / journal positioning.

---

## Status

**CORE EVENT THEOREM STACK: VERIFIED / UNCHANGED**

**REV6 REFEREE REPAIRS: COMPLETED**

**REV6 FULL BUILD: PASSED**

**REV6 FINAL LAYOUT SOURCE: PERSISTED**

**STEADY-STATE CI: READ-ONLY DIRECT COMPILE**

**NEXT PHASE: SUBMISSION PACKAGE**
