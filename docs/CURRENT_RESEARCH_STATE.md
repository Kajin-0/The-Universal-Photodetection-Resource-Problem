# Current Research State

**Date:** 2026-08-21

Active branch: `agent/uprp-core-theorem-round10`

## Project-level status

1. **Paper 1 / Rev11:** scientifically frozen and technically validated for Physical Review Applied; only factual/personal submission metadata remain.
2. **Paper 2:** the theorem-development phase has passed an integrated hostile review. **Manuscript architecture is now authorized.**

The active frontier is no longer open-ended Paper-2 theorem accumulation. It is conservative manuscript construction around the theorem stack that survived WP27.

## Read first

1. `AGENTS.md`
2. `paper2/AGENTS_PAPER2.md`
3. `paper2/notes/WP27_INTEGRATED_HOSTILE_REVIEW_AND_MANUSCRIPT_GATE.md`
4. `paper2/notes/RESEARCH_LOG_ROUND04_WP21_WP26_CHECKPOINT.md`
5. `paper2/notes/WP26_FINITE_MEAN_STATIONARY_WINDOW_FISHER_RATE.md`
6. `paper2/notes/WP25_FINITE_MEAN_CYCLE_DQM_AND_HEAVY_TAIL_HARDENING.md`
7. `paper2/notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
8. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`
9. `paper2/notes/WP17_PUBLICATION_GRADE_WP10_FORMALIZATION.md`
10. `paper2/notes/WP10_GENERAL_AUTONOMOUS_CHANNEL_THEOREM_HARDENED.md`

# Paper 1 — frozen Rev11

Preferred candidate remains Rev11. Do not reopen science absent a concrete defect or referee request.

# Paper 2 — manuscript-ready core

## Organizing theorem — WP10/WP17

For any parameter-independent autonomous detector channel driven by a homogeneous Poisson source, local waveform Fisher information is represented by a bounded translation-invariant operator, hence an a.e. temporal multiplier

`0<=G(omega)<=1`.

This is a photodetection-channel synthesis of standard statistical/harmonic-analysis ingredients.

## Dynamic Type-II result — WP07

At deterministic paralyzable saturation `lambda*tau=1`:

- stationary homogeneous FI retention is zero;
- every nonzero temporal frequency retains positive complete-record local FI;
- the high-frequency complete-record retention tends to `1/e`;
- at `omega*tau=pi`, a rigorous lower bound is `0.516975...` and exact numerical validation gives about `0.52814`.

Mandatory notation repair in the manuscript: distinguish static `G_DC` from the a.e. general spectrum and formulate finite-frequency performance through model-specific narrowband/continuous representatives.

## Finite-mean recovery singularity — WP25/WP26

For iid recovery with only `0<E[T]=m<infinity`, the stationary registered timestamp process has

`G_DC=G_cyc=(r/lambda)I_D`,

with `r=lambda exp(-lambda m)` and `0<=G_DC<=1`.

At the universal count maximum `lambda*m=1`:

`G_DC=0 iff T=m almost surely`.

The theorem covers atomic, singular, infinite-variance, and heavy-tailed recovery distributions. Nondegenerate recovery also has an explicit positive bounded-Laplace-statistic witness.

WP27 found no fatal proof defect. Drafting must nevertheless give an explicit stopped-counting-process DQM/localization citation and explicitly justify stationary forward recurrence through the ergodic finite-mean `M/G/infinity` construction.

## Resource incompleteness — WP19

Recovery mean + variance/CV + the entire conventional mean saturation curve do not determine the timestamp information experiment. The no-go is analytic; the ~8.78% full-FI difference is supporting numerical calibration.

## Structural bridge — WP22/WP23/WP24

Conditional-score zero-lag atomic timing energy controls high-frequency Cesaro retention under appropriate spectral-measure regularity. This is retained for interpretation only; WP24 downgraded standalone novelty because the mathematical ingredients are strongly classical.

# Integrated novelty state — WP27

No exact predecessor was located for the combined claims:

1. complete deterministic Type-II static blindness with positive complete-record FI at every nonzero temporal frequency and exact high-frequency residue `1/e`;
2. deterministic recovery as the unique zero of complete stationary static FI at the common Type-II count maximum throughout the arbitrary finite-mean iid-recovery class;
3. the exact mean+variance resource-incompleteness construction.

Priority is **not certified**. Close classical work occupies modulated paralyzable photocounting, random Type-II cycle laws, queue-output identifiability, renewal FI, and dead-time information theory. The paper must present the above as narrowly scoped candidate contributions rather than first-ever claims.

# Current thesis

> A conventional detector saturation curve is not an information-transfer law. For autonomous classical photodetection, information belongs to the complete trajectory channel: deterministic Type-II paralysis can erase a static source tangent while preserving every nonzero temporal mode; random recovery generically destroys that singularity despite the same mean saturation curve; and even recovery mean plus variance do not determine the timestamp information channel.

# Manuscript gate

**PASSED WITH MANDATORY POSITIONING/NOTATION REPAIRS.**

Next action:

1. create the Paper-2 manuscript architecture and claim/prior-art matrix;
2. choose a conservative title/abstract structure;
3. then begin LaTeX drafting;
4. do not resume broad exploratory theory unless a concrete drafting defect appears.

# Documentation requirement

Material theorem results, proof repairs, prior-art collisions, numerical results used in arguments, or changes in manuscript strategy must be committed immediately. Keep `paper2/AGENTS_PAPER2.md` and this file synchronized.
