# Manuscript Rev6 Referee-Repair Audit

**Date:** 2026-08-20

## Purpose

Record the targeted revision from `event_resource_theorem_rev5.tex` to `event_resource_theorem_rev6.tex` after an independent extreme adversarial review judged the core event-channel mathematics sound but identified four remaining publication-level seams.

This revision is a publication-hardening pass, not a new theorem branch.

---

## Referee issues addressed

### 1. Stationary thermodynamic gateway versus independent-event theorem

**Issue:** Theorem 1 assumes an independent per-photon event kernel, whereas the thermodynamic section uses stationary traffic, activity, and entropy production of a continuously operating finite-state CTMC. Stationary occupancy/recovery can in general make capture history dependent.

**Rev6 repair:** The thermodynamic section now states an explicit isolated-event/low-overlap reduction before applying the rate bound to source-information transfer:

1. stationary baseline thermodynamic quantities are used only to constrain microscopic CTMC rates;
2. one conditions on an isolated optical capture that places the gateway in state 1;
3. the subsequent autonomous CTMC generates the per-photon post-capture delay law `mu_m` entering the marked event kernel;
4. the information bound is claimed only when successive source events are sufficiently separated that occupancy/recovery do not make capture probability or the post-capture kernel depend on prior events.

If capture or recovery is history dependent, Eq. `eq:kernel` is explicitly declared inapplicable and the thermodynamic information bound is not claimed.

**Assessment:** conceptual model-class seam closed without changing the thermodynamic algebra or event theorem.

### 2. Misleading use of “reversible”

**Issue:** The nonequilibrium CTMCs have nonzero stationary currents and entropy production, so “reversible Markov chain” is incorrect in the standard detailed-balance sense.

**Rev6 repair:** Replaced the relevant usage with **bidirectionally connected** and defined it explicitly as reverse-transition support for transitions used in thermodynamic accounting. The manuscript states that this does not mean stationary detailed-balance reversibility. The abstract, thermodynamic section, main-text rare-fast reference, and versioned rare-fast appendix all use the corrected terminology.

**Assessment:** mandatory stochastic-thermodynamics terminology repair completed.

### 3. Exact DC normalization

**Issue:** `dot F_in = Phi_0/2` uses the long-time average of `cos^2(omega t)` and is literal only for nonzero modulation frequency. At exact `omega=0`, the incident FI rate is `Phi_0`.

**Rev6 repair:** The source-normalization subsection now states that Eq. `eq:inputFI` assumes `omega != 0`, gives the exact-DC FI rate, and explains that the same factor changes in output FI, so the normalized transfer remains `G(0)=eta`.

**Assessment:** formal endpoint ambiguity removed; no transfer theorem changes.

### 4. Proof that `q_max` bounds mark-conditioned hazard

**Issue:** Rev5 stated the finite-state CTMC `q_max` hazard ceiling without a self-contained argument.

**Rev6 repair:** Added the short proof. For initial pre-registration state `x`, the first holding time is exponential with rate

`lambda_x = sum_{y != x} W_yx`

and is independent of exit destination and subsequent Markov trajectory. Under the mark restriction,

`D | (M,x) = T_x + Y_{M,x}`

with `Y_{M,x} >= 0`. The exponential convolution gives

`f_{D|M,x}(t) <= lambda_x S_{D|M,x}(t)`,

hence

`h_D(t|M,x) <= lambda_x <= q_max`.

Mixing over a random initial pre-registration state preserves `f <= q_max S`.

**Assessment:** microscopic completion is now self-contained.

### 5. FWHM wording

Rev6 now states only that the same caution applies to scalar widths such as FWHM unless shape assumptions are imposed, and explicitly says that no fixed-FWHM counterexample is claimed.

### 6. Typesetting

The long boxed thermodynamic conclusion was split across two lines to remove a large overfull horizontal box. This is layout-only.

---

## What did not change

The following results and constants are unchanged:

- exact marked Poisson event-channel FI transfer;
- `G(0)=eta` as normalized DC transfer;
- Wiener atomic timing residue;
- Parseval sum rule `integral G d omega = pi mathfrak R_2`;
- collision-resource bound;
- hazard-collision inequality `mathfrak R_2 <= mathfrak H`;
- flat-band inverse resource cost `mathfrak R_2 >= 4 B q` and `mathfrak H >= 4 B q`;
- common-hazard requirement `Lambda >= 4 B q / eta`;
- relative-retention form `Lambda >= 4 B r`;
- exact fixed-mean/fixed-variance timing no-go;
- synchronous-clock/control no-go;
- thermodynamic gateway algebra for `Lambda_*`;
- rare-fast stationary-thermodynamic counterexample.

No new detector class is claimed.

---

## Build history

The initial Rev6 referee-repair run generated, fully compiled, and uploaded the manuscript successfully, but its final source-persistence push lost a branch race to a simultaneous terminology-propagation commit. That job-level failure was therefore not a manuscript failure.

The subsequent run for the terminology-complete Rev6 state succeeded and persisted the generated Rev6 main source and versioned appendix.

Steady-state CI is to remain read-only and compile the committed Rev6 source directly after one-shot verification machinery is removed.

---

## Publication posture

The strongest hostile-referee concern from the review—the model-class bridge between stationary CTMC thermodynamic accounting and the independent-event theorem—is now explicit in the manuscript.

Rev6 should therefore be treated as the publication candidate for the first autonomous-event paper. Further foundational expansion is not the default next action; only concrete claim, build, or submission-package defects justify additional revision.
