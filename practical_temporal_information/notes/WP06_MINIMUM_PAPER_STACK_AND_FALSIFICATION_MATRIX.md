# WP06 — Minimum Paper-4 stack and integrated falsification matrix

**Date:** 2026-08-23

**Status:** scope gate complete. No new physical theorem is introduced. WP06 ranks WP01–WP05, removes redundant material, and defines the falsification hierarchy needed for a defensible practical manuscript.

## 1. Decision

A practical fourth paper is scientifically coherent **if it is not presented as five equal sections**.

The minimum useful structure is:

1. **measurement bridge** — show how ordinary analog and timestamp records map to temporal Fisher information;
2. **memory counterexample** — show that conventional dead-time/saturation characterization can fail to determine temporal-information transfer;
3. **spectral support crossover** — show experimentally legible finite-radius survival -> rank-boundary synthesis using seeded/empty optical sidebands;
4. **compact implementation benchmark** — show that the synthesized curvature has a standard fixed-energy resonant-exchange coupling interpretation;
5. **falsification table** — state exactly what would contradict each layer.

WP03 and WP04 are the central scientific results. WP01/WP02 are bridge material. WP05 should be compact, not a second theory paper inside Paper 4.

---

# 2. Scientific-value ranking

## Tier A — headline results

### A1. Same conventional recovery characterization, different temporal information

Retain the strongest WP03 statement:

- generalized iid Type-II recovery with mean `m` has the universal saturation curve `r=lambda exp(-lambda m)`;
- at the common count maximum, timestamp DC FI vanishes iff recovery is deterministic;
- explicit equal-mean/equal-variance laws have identical complete saturation curves but different pair correlations and accessible FI.

Why headline-worthy:

This is directly relevant to ordinary detector characterization and demonstrates a concrete failure of standard low-dimensional figures of merit.

### A2. Seeded-to-empty sideband survival/synthesis crossover

Retain the exact WP04 two-bin result:

`R_lin^2=p(1-p)/[kappa^2(1-2p)^2]`,

`(R_lin^2/4)Tr F<=p` for `p>0`,

`Tr F<=Delta P_s(0)=4kappa^2` at `p=0`,

and

**`lim_(p->0+)4p/R_lin^2=Delta P_s(0)`.**

Also retain ordinary weak phase modulation as the recognizable boundary saturation example:

`Delta P_+=Delta P_-=1`, `Tr F=4`.

Why headline-worthy:

This makes the flagship's support transition visible in standard optical observables rather than only density-operator geometry.

## Tier B — necessary operational bridge

### B1. Linear Gaussian FI/NEP identity

Retain only the core convention-controlled identity and arbitrary-waveform form:

`F_xx/T=1/NEP(f)^2`,

`Tr F/T=2/NEP(f)^2`,

`F_ij=4 Re integral q_i^* q_j/NEP^2 df`.

Use information bandwidth only as one illustrative consequence, not a novelty claim.

### B2. Ideal timestamp / shot-noise equivalence

Retain:

`Tr F/T=lambda_0`

for ideal fractional Poisson modulation and the exact optical-power agreement with `2/NEP_shot^2`.

Timing jitter should appear as one compact extension:

`Tr F/T=lambda_0|Phi_J|^2`.

This is useful because it shows analog current and raw timestamps fit the same information language.

## Tier C — compact physical completion

### C1. Resonant beam-splitter implementation benchmark

Retain as a short section or boxed example:

`V_min=8(g t)^2=(1/2)Tr C`,

`A_ex=hbar nu V_min`,

with exact fixed total bare energy.

Do not repeat the full PRA proof or infinite-dimensional construction.

Why include:

It answers the natural practical question “what does this coupling cost look like in a Hamiltonian I recognize?”

---

# 3. Material to demote or remove

Do **not** add dedicated main-text sections for:

- a separate photoconductor lifetime-pole model; WP01 already covers linear transfer/noise and another pole example adds little;
- a separate RC photodiode worked example unless needed for a figure;
- generalized `NEP_F` terminology before WP07 establishes that it is useful and nonredundant;
- many recovery distributions beyond the deterministic class and the exact same-mean/same-variance pair;
- extra sideband modulation technologies;
- unequal-frequency converters with explicit pumps unless needed by a referee;
- infinite-dimensional implementation machinery from the PRA supplement;
- additional quantum-resource formalism not required to state the practical tests.

This is essential scope control.

---

# 4. Three levels of falsifiability

A practical paper must distinguish what a failed measurement actually falsifies.

## Level I — detector-model/reduction falsification

Examples:

- measured Gaussian-record FI disagrees with `R^2/S_n`;
- measured jitter transfer disagrees with `|Phi_J|^2`;
- measured beam-splitter endpoint curvature disagrees with the calibrated ideal Hamiltonian.

Interpretation:

The assumed detector/channel model, calibration, stationarity, independence, or parameter convention is wrong. This is **not automatically** a violation of an upstream general theorem.

## Level II — resource-law falsification under independently verified assumptions

Examples:

- finite-radius sideband experiment yields `(R_lin^2/4)Tr F>p` after state support, `p`, `R_lin`, parameter normalization, and measurement FI are independently verified;
- boundary experiment yields `Tr F>Delta P_s` or exceeds the bilateral square-root curvature bound after the physical `C^2` state family and endpoint sectors are verified.

Interpretation:

If all theorem hypotheses are independently satisfied, such a violation challenges the resource inequality itself.

## Level III — saturating implementation equality

Examples:

- ideal phase modulator fails to attain the predicted equality because of loss or imperfect mode analysis;
- resonant beam-splitter benchmark fails `8(g t)^2=(1/2)Tr C` because of leakage, detuning, decoherence, or calibration error.

Interpretation:

Failure usually falsifies the **specific saturating model**, not the theorem lower bound. A fundamental challenge requires showing `V_impl<(1/2)Tr C` within the theorem's implementation class after all quantities are independently established.

This hierarchy must be explicit in the manuscript.

---

# 5. Integrated falsification matrix

| Test | Standard measured quantities | Prediction | What a failure means first |
|---|---|---|---|
| Gaussian analog bridge | complex `R(f)`, one-sided `S_n(f)`, raw waveform likelihood | `F_xx/T=|R|^2/S_n`; `Tr F/T=2/NEP^2` | linear/stationary/Gaussian/noise-calibration model failure |
| Ideal timestamp bridge | incident/detected rate, raw timestamps, weak modulation | fractional `Tr F/T=lambda_0` | non-Poisson statistics, gating, memory, background, estimator/model failure |
| Independent jitter | jitter distribution and timestamp FI spectrum | normalized FI=`|Phi_J(Omega)|^2` | jitter not independent displacement; hidden memory/filtering |
| Deterministic Type-II spectral escape | `tau`, rate sweep, timestamp Fourier response/noise | at `lambda tau=1`: `G(0)=0`, `G(f)>0`; at `f=1/(2tau)`, `G>=0.516975` | deterministic paralyzable model/calibration failure; theorem only after hypotheses verified |
| Random-recovery singularity | mean recovery, rate dither, registered intervals | at `lambda m=1`, `d E[e^{-D/m}]/d epsilon=0` iff deterministic recovery | iid Type-II/recovery-law assumption failure or theorem challenge if hypotheses certified |
| Same-curve counterexample | saturation curve, recovery mean/variance, pair-delay histogram | matched conventional metrics can coexist with different `g^(2)`/FI | demonstrates insufficiency of conventional summary; not a universal equality test |
| Seeded sideband survival | baseline seed `p`, calibrated `kappa`, phase-sensitive FI | `(R_lin^2/4)Tr F<=p` | resource-law challenge only after support/radius/model hypotheses verified |
| Empty-sideband boundary | sideband population Hessian, phase-sensitive FI | one-sided `Tr F<=Delta P_s`; bilateral square-root law | boundary theorem challenge only after state/parameter calibration verified |
| Ideal phase-modulation saturator | `Delta P_+`, `Delta P_-`, interferometric FI | `Delta P_+=Delta P_-=1`, `Tr F=4` in locked units | usually modulator/analyzer/loss model failure |
| Fixed-shell beam splitter | exchange rate `g`, duration `t`, endpoint Hessians, shell leakage | `V=8(gt)^2=(1/2)Tr C`, `A=hbar nu V` | usually Hamiltonian/model failure; theorem challenge only if lower bound is beaten under certified assumptions |

---

# 6. Minimum experimental data products

Paper 4 should be written so each proposed test can be executed from familiar data products:

1. transfer-function sweep `R(f)`;
2. noise PSD `S_n(f)`;
3. raw timestamp file under controlled rate/modulation;
4. registered inter-event histogram / pair-correlation histogram;
5. carrier/sideband spectra versus calibrated modulation quadratures;
6. phase-sensitive sideband/carrier analysis for FI;
7. resonant exchange oscillation/calibration plus endpoint-population curves.

No tomography of a large Hilbert space should be required for the central practical examples.

---

# 7. Proposed minimum manuscript structure

## I. Motivation: sensitivity and saturation are not information-transfer laws

Use one paragraph of the three-paper theoretical context only.

## II. Temporal information in detector language

Derive the NEP identity and Poisson timestamp identity. Keep to approximately 1.5–2 pages.

## III. Memory: same saturation, different information

This is the first main result. Include deterministic information-high-pass behavior and the exact equal-mean/equal-variance counterexample.

## IV. Spectral support: from survival to sideband synthesis

This is the second main result. Include seeded two-bin crossover and ordinary phase-modulation boundary saturation.

## V. What synthesis costs in a standard Hamiltonian

Short fixed-shell beam-splitter benchmark; no general proof repetition.

## VI. Falsification protocol and discussion

One consolidated table, experimental assumptions, and clear hierarchy of what each failure would mean.

Supplement:

- convention/factor-of-two derivations;
- finite-window Poisson formulas;
- explicit POVMs;
- beam-splitter algebra;
- reused upstream theorem statements with precise citations rather than copied proofs.

Target main-text length: roughly 10–14 journal pages before references, not another 20–30 page theorem manuscript.

---

# 8. Candidate figures

Keep to four figures maximum.

### Fig. 1 — common information language

Analog `1/NEP^2` and timestamp `lambda_0`/jitter spectrum as two routes to the same Fisher benchmark.

### Fig. 2 — same saturation, different information

Top: identical Type-II saturation curves for equal-mean recovery laws.
Bottom: dramatically different timestamp pair correlation / one-bit interval response.

### Fig. 3 — survival-to-synthesis sideband crossover

Show seed `p`, affine radius collapse, finite-radius ceiling, and boundary sideband-curvature limit. Include phase-modulation sideband inset.

### Fig. 4 — fixed-energy coupling realization + falsification map

Two-mode `|2,0> <-> |1,1> <-> |0,2>` exchange inside one total-energy shell, with `V=(1/2)Tr C`, plus compact measurement arrows.

Do not add decorative conceptual diagrams if these four already communicate the mechanism.

---

# 9. Publication criterion after WP06

The practical program now has a coherent minimum paper architecture.

However, **manuscript drafting remains blocked on WP07 prior-art/significance review**.

The strongest candidate distinct claims to test in WP07 are:

1. the detector-characterization consequence that identical full homogeneous Type-II saturation curves, even with matched recovery mean/variance, need not determine temporal FI and admit simple accessible separating statistics;
2. the exact seeded-to-empty optical support crossover `lim 4p/R_lin^2=Delta P_s` as a practical realization of survival -> synthesis;
3. the combined falsification framework linking NEP/timestamps, support curvature, and fixed-shell coupling without conflating model failure with theorem failure.

WP01, WP02, standard phase-modulation formulas, and standard beam-splitter algebra should be assumed prior/common until shown otherwise.

## Next

WP07: perform a dedicated, adversarial prior-art/significance search around the three candidate distinct claims above. If the distinct core survives, then and only then create a Paper-4 manuscript workspace.
