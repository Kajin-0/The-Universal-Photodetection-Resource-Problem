# WP31 — Autonomous Event-Branch Resource Necessity Matrix

**Date:** 2026-08-20

## Purpose

Consolidate WP25–WP30 into a minimal no-go/repair map for the autonomous proper-event detector class. The goal is to distinguish:

- resources that are genuinely necessary for a stated kind of bound;
- resources that are merely convenient sufficient conditions;
- quantities that affect achievable sensitivity but are not required in the universal upper bound;
- assumptions whose removal changes the detector class.

This note is intended to prevent the project from re-expanding into an unnecessary list of primitive variables.

---

# 1. Detector class being closed

The matrix applies to an **autonomous/time-translation-invariant proper event detector** driven by weak coherent/Poisson optical flux.

A captured signal photon produces one primary intrinsic electrical event. All accessible event marks are retained. Parameter-independent dark/background additions and downstream processing may be present.

Architectures that encode arrival phase with an external clock, maintain a coherent continuous pointer before irreversible registration, or generate multiple independent pre-registration timing records per captured photon belong to separate classes unless their extra timing/control resources are explicitly counted.

---

# 2. Source-side resource

## Requirement

A finite, normalized source-information task must be specified.

Preferred general formulation:

\[
w(\omega)=\frac{\mathcal J_{in}(\omega)}{\int\mathcal J_{in}(\omega)d\omega}.
\]

WP28 characterizes the source through its spectral concentration function

\[
\mathcal W(A)=\sup_{|E|\le A}\int_Ew(\omega)d\omega.
\]

## Why it is needed

An unweighted all-frequency integral can diverge even for an ideal photon counter with `eta_I(omega)=1` at every frequency in the white Poisson model.

Thus the source temporal/spectral task is not a detector resource but is necessary to make the question well posed.

**Status:** NECESSARY FOR WELL-POSEDNESS.

---

# 3. Accessible-mark specification

## Requirement

The theorem must condition on the **complete accessible autonomous event mark** `M`.

## Why it is needed

A mark can reveal a deterministic delay branch, capture position, path identity, or other side information that allows timing correction. Applying a bound to the marginal delay distribution can therefore underestimate the available FI.

WP30 gives the exact mark-resolved atomic residual.

**Status:** NECESSARY FOR RECORD-INVARIANT STATEMENT.

---

# 4. Atomic timing content: weakest current asymptotic obstruction

For conditional delay measure `mu_m`, define

\[
a(m)=\sum_j p_j(m)^2
\]

from its atomic masses.

WP30 proves

\[
\lim_{\Omega\to\infty}\bar\eta_I(\Omega)
=\eta_c\,\mathbb E_M[a(M)]
\]

in the ideal no-background event channel.

Therefore:

- if every conditional delay law is non-atomic, the flat-band average information tends to zero;
- deterministic/discrete timing branches leave an exact nonzero asymptotic residue.

No hazard, `L2`, mean, or variance condition is needed for this qualitative statement.

**Status:** SHARPEST STRUCTURAL ASYMPTOTIC RESULT CURRENTLY KNOWN IN PROJECT.

---

# 5. Timing-concentration resource R2

Define

\[
\mathcal R_2
=2\,\mathbb E_M\int f(t|M)^2dt
\]

when the conditional densities are square-integrable.

Then WP26/WP28 give

\[
\bar\eta_I[w]
\le C\mathcal W(\pi\mathcal R_2).
\]

For a flat band,

\[
\bar\eta_I(\Omega)
\le C\min\left(1,\frac{\pi\mathcal R_2}{2\Omega}\right).
\]

## Necessity status

Finite `R2` is **not necessary** for qualitative asymptotic information loss: non-atomic distributions outside `L2` can still have vanishing Cesaro spectral information.

However, without some concentration regularizer of this kind, no universal `1/Omega`-type quantitative rate follows.

WP26's prompt-spike/long-tail family shows that fixed conventional moments do not control the crossover bandwidth.

**Status:** SUFFICIENT QUANTITATIVE RESOURCE; NOT MATHEMATICALLY NECESSARY FOR QUALITATIVE DECAY.

---

# 6. Local conditional hazard Lambda

Define

\[
\Lambda=\operatorname*{ess\,sup}_{M,t}h(t|M).
\]

WP25 proves

\[
\mathcal R_2\le\Lambda
\]

and hence

\[
\bar\eta_I(\Omega)
\le C\min\left(1,\frac{\pi\Lambda}{2\Omega}\right).
\]

Microscopic sufficient realizations:

Classical Markov:

\[
\Lambda_{cl}=\max_x\sum_{y\in E_{reg}(x)}W_{yx}.
\]

Quantum jump:

\[
\Lambda_q=\left\|\sum_\alpha L_\alpha^\dagger L_\alpha\right\|_\infty.
\]

## Necessity status

A bounded hazard is not the weakest possible mathematical assumption, but an **absolute local rate/operator scale of this type is necessary for the restricted thermodynamic route**. WP4 shows stationary EPR/activity can remain bounded while local rates diverge.

**Status:** PHYSICALLY INTERPRETABLE SUFFICIENT RESOURCE; ABSOLUTE LOCAL RATE SCALE NECESSARY FOR WP29 THERMODYNAMIC COMPLETION.

---

# 7. Stationary EPR/activity/temperature

## Candidate claim rejected

\[
(T,\Sigma,\mathcal A,\text{detailed balance},f_*)
\Rightarrow
\text{finite information bandwidth}.
\]

WP4 disproves this in an abstract reversible Markov class: bare/local rates can diverge in rare states while the stationary thermodynamic quantities remain bounded.

## Conditional repair

WP29 shows that, once a finite reverse optical/local rate `d` is supplied,

\[
\Lambda_*
=\frac{\mathcal A d}{f_*}
 g^{-1}(\Sigma/f_*)
\]

bounds the conditional registration hazard in the single-gateway class. WP25/WP28 then yield a finite information ceiling.

Thus thermodynamics is a **conditional amplifier of a microscopic rate bound**, not a standalone speed resource.

**Status:** INSUFFICIENT ALONE; USEFUL IN RESTRICTED COMPOSITION.

---

# 8. Conventional latency/jitter metrics

The following do not provide a resource-complete quantitative information-bandwidth bound:

- mean delay;
- deterministic transit time;
- RMS jitter/variance;
- FWHM jitter;
- conventional `-3 dB` amplitude bandwidth.

Reasons:

- deterministic delay preserves stationary spectral FI;
- fixed moments permit arbitrarily narrow prompt spikes with compensating rare tails;
- invertible deterministic filtering preserves FI before downstream noise/coarse graining.

**Status:** REJECTED AS PRIMITIVE UNIVERSAL RESOURCES.

---

# 9. Capture efficiency C

For one incident photon in the proper-event class,

\[
0\le\eta_c\le1
\]

already follows from probability conservation.

A nontrivial optical capture ceiling `C<1` sharpens sensitivity/information efficiency, but **no extra capture theorem is required merely to obtain finite timing bandwidth**, because one may always use the trivial `C=1` upper bound.

Optical T-operator/sum-rule resources become relevant when the objective is a stronger sensitivity-speed bound rather than timing decay alone.

**Status:** TRIVIALLY BOUNDED; NONTRIVIAL OPTICAL RESOURCE OPTIONAL FOR STRONGER SENSITIVITY CLAIMS.

---

# 10. Dark/background events

Parameter-independent dark/background events cannot increase source FI.

Therefore they are unnecessary in the universal upper bound. Signal-indistinguishable background can be included to obtain sharper achievable-sensitivity ceilings.

A universal temperature-dependent sensitivity floor would require a separate microscopic theorem relating temperature to unavoidable indistinguishable background or capture loss.

**Status:** NOT REQUIRED FOR UPPER SPEED BOUND; IMPORTANT FOR ACHIEVABLE SENSITIVITY.

---

# 11. Downstream electronics

Filters, deterministic gain, avalanche marks after the primary record, thresholding, ADC, finite sampling, and other parameter-independent downstream channels obey FI data processing.

They may reduce measured FI but cannot violate the intrinsic event upper bound.

RC poles are therefore not primitive information-bandwidth resources unless downstream noise/sampling is part of the specified measured record.

**Status:** NOT REQUIRED FOR INTRINSIC UPPER BOUND.

---

# 12. External clock/control

WP27 gives an explicit counterexample: a free source-synchronous clock can store arrival phase in a mark before arbitrarily slow registration.

Thus either:

1. restrict the theorem to autonomous/time-translation-invariant detectors; or
2. count clock frequency/phase precision, control Hamiltonian/action, memory, and reference bandwidth as explicit resources.

**Status:** AUTONOMY ASSUMPTION NECESSARY UNLESS CONTROL/REFERENCE RESOURCE IS COUNTED.

---

# 13. Parallel replication

Consider independent channels `j` carrying incident information weights `w_j`, with normalized `sum_j w_j=1`. If each channel has information efficiency `eta_j(omega)`, then the total source-normalized efficiency with channel identity retained is

\[
\eta_{tot}(\omega)=\sum_jw_j\eta_j(\omega).
\]

For `N` identical replicas this equals the single-channel normalized efficiency. Total FI grows with `N`, but the incident source FI grows by the same factor.

Therefore parallel replication does not evade a source-normalized bound.

If multiple parallel primary registration routes belong to one captured photon, their **total** local jump intensity is what enters `Lambda`; bounding only an individual-route rate is not resource-complete.

**Status:** PASSES EXTENSIVITY TEST.

---

# 14. Internal gain / multiple events

Two cases must be distinguished.

1. **Post-primary offspring:** once a sufficient primary electrical event record exists, parameter-independent offspring/gain is downstream processing and cannot increase source FI.
2. **Multiple independent pre-primary timing records from one captured photon:** this is outside the one-primary-event detector class unless the combined registration process is represented explicitly. Unbounded multiplicity is an additional timing resource and must not be declared free.

Thus the theorem is not silently extended to arbitrary branching cluster detectors.

**Status:** NO LOOPHOLE INSIDE STATED CLASS; SEPARATE CLASS IF MULTIPLE PRE-REGISTRATION TIMING COPIES ARE PHYSICAL.

---

# 15. Current minimal answer for the event branch

The project can now state the hierarchy without an oversized primitive list.

## Qualitative asymptotic theorem

For autonomous marked event detectors, high-band flat-spectrum information vanishes if every mark-conditioned registration delay is non-atomic.

## Quantitative source-spectrum theorem

Finite timing collision intensity `R2` yields

\[
\bar\eta_I[w]\le C\mathcal W(\pi\mathcal R_2).
\]

## Microscopic completion

A finite local conditional registration intensity `Lambda` implies `R2<=Lambda`.

## Restricted thermodynamic completion

WP29 derives a finite `Lambda_*` from EPR/activity/throughput **only when an absolute microscopic gateway rate is also bounded**.

This is the current cleanest answer to the autonomous proper-event UPRP.

---

# 16. Remaining high-value gaps

1. Theorem-level novelty audit for the WP25–WP30 stack.
2. Determine whether a useful rate theorem exists between mere non-atomicity and finite `L2` timing density.
3. Extend source statistics beyond coherent/Poisson direct detection only if it materially changes the theorem.
4. Decide whether the event theorem stack plus WP4/WP29 no-go/repair pair is sufficient for a first manuscript.

Detailed HgCdTe WP17–24 work remains frozen.