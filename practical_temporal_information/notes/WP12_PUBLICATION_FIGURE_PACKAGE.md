# WP12 — Publication figure package

**Date:** 2026-08-25

**Status:** **FROZEN PASS.** The standalone four-figure package has passed deterministic clean-CI generation, locked-value assertions, output-format gates, artifact hashing, independent PDF rendering, and page-level visual QA. No manuscript science was changed during WP12.

## Purpose

Create the maximum four figures needed by the frozen R4 practical manuscript. The figures are deterministic, grayscale/line-style legible, directly tied to displayed equations or frozen companion benchmarks, and are isolated from manuscript text until this standalone package is verified.

## Canonical source and build

Figure sources:

`manuscript/practical_temporal_information/figures/`

Runner:

`manuscript/practical_temporal_information/figures/generate_all.py`

CI workflow:

`.github/workflows/practical-temporal-information-figures-check.yml`

Pinned CI dependencies:

- Python 3.12;
- NumPy 2.3.2;
- Matplotlib 3.10.5.

Canonical GitHub Actions verification:

- run: `32914889053`;
- job: `98016438281`;
- head commit: `8d3c74fb91821c492a26f101148f322e2f4fad1e`;
- result: **PASS** for dependency install, all four generators, analytic/output gates, SHA list, and artifact upload.

Canonical artifact:

- ID: `9587797682`;
- name: `practical-temporal-information-wp12-figures`;
- archive size: `875503` bytes;
- archive digest: `sha256:261acabd321706ad73dfb873bf9ca4fbc7f81722a80f316be4318578eb43bf91`.

## Canonical vector PDFs

1. `fig1_same_specs_different_information.pdf`
   - bytes: `25411`;
   - SHA-256: `9b1f3b05552a91e6a57f08034d9275f450496138738f48eb654c6952e401b48e`.

2. `fig2_same_saturation_different_timestamps.pdf`
   - bytes: `39022`;
   - SHA-256: `ffdb3a32ae3a571366b1eaf915ec8842eecc9bd48725219848f8fa233a64713e`.

3. `fig3_support_survival_synthesis_crossover.pdf`
   - bytes: `31983`;
   - SHA-256: `a7440d615fce70e8890af9d493fecf37b610938b1ec05ef53493f7f367195394`.

4. `fig4_resonant_implementation_falsification.pdf`
   - bytes: `39150`;
   - SHA-256: `7eafd153221f3617cd6fcc38c71ef92b6d2df21087490e6b3cd4c159615241f0`.

The artifact also contains 300-dpi PNG previews, per-figure locked-value JSON files, aggregate `locked_values.json`, `manifest.json`, and `SHA256SUMS.txt`.

## Figure 1 — same conventional specifications, different information spectra

Model:

`|H|^2=1/(1+u^2)`,

`S_A/S0=1`,

`S_B/S0=1/5+(4/5)/(1+25u^2)`,

`J_A=1/(1+u^2)`,

`J_B=(1+25u^2)/[(1+u^2)(1+5u^2)]`.

Locked checks include

`J_B(f_c)/J_A(f_c)=13/3`

and

`f_half-FI,B/f_c=sqrt[(22+sqrt(489))/5]=2.970297775897...`.

Role: standard detector illustration of specification incompleteness; not a novelty theorem.

## Figure 2 — same saturation, different timestamp information

Frozen companion benchmark normalized by common mean recovery `m`:

Law A: support `T/m={0.5,1.5}` with weights `{1/2,1/2}`.

Law B: support `T/m={0.25,1,1.75}` with weights `{2/9,5/9,2/9}`.

Both have exactly mean `1`, variance `1/4`, CV `1/2`, and the same complete saturation curve

`r m = rho exp(-rho)`.

Locked companion observables at `lambda m=1`:

`g_A^(2)(0.75m)=0.7274957073`,

`g_B^(2)(0.75m)=0.3188717529`,

`G_Z,A=0`,

`G_Z,B=0.00443520488427`

for `Z=1{D<=0.4m}`.

Role: companion-memory benchmark; caption must keep explicit attribution.

## Figure 3 — support-controlled survival-to-synthesis crossover

This is the principal Paper-4 figure.

Visualization path only:

`a_p=1-p`, `sigma_p=0`, `q=kappa=1`.

Locked radii:

`R_lin(0.15)=0.510102030610...`,

`R_lin(0.05)=0.242161052419...`,

`R_lin(0.01)=0.101529330317...`.

The figure shows:

- seeded support versus the empty-sideband boundary;
- collapse of the affine physical disk;
- `4p/R_lin^2 -> Delta P_s(0)=4`;
- independent baseline/tangent tomography, zero-seed curvature fitting, and phase-sensitive FI measurement.

The caption must state that the theorem itself permits the manuscript's broader class of stationary inert spectators and general `q,kappa`.

## Figure 4 — resonant implementation and failure hierarchy

Equal-frequency benchmark:

`H_0=hbar nu(N_C+N_S)`

with `|2,0>`, `|1,1>`, and `|0,2>` all in the same total bare-energy shell.

Locked equality:

`V_impl=Tr C/2=8(gt)^2`,

`A_ex/(hbar nu)=V_min`.

The failure hierarchy is explicitly separated:

- Level I — implementation/model failure;
- Level III — ideal benchmark fails to saturate the equality;
- Level II — with theorem assumptions independently verified, `V_impl<Tr C/2` challenges the frozen companion lower bound.

Role: standard-physics realization of the companion implementation theorem; not Paper-4 novelty.

## Exact visual QA

All four canonical CI PDFs were downloaded from artifact `9587797682`, independently rendered at 200 dpi, and inspected.

PASS:

- no clipping;
- no overlaps;
- no broken glyphs;
- no hidden data labels;
- no panel-title collisions;
- no line/legend ambiguity that destroys grayscale interpretation;
- Fig. 3 noncircular measurement paths legible;
- Fig. 4 Level-I/III/II hierarchy legible.

The clean-CI PNGs differ slightly in raster bytes from some local prototypes because the canonical environment is pinned; the scientific geometry and visual content are unchanged. Only artifact PDFs/hashes above are publication identities.

## Freeze rule

WP12 is closed. Do not redesign the figures, change numerical values, or alter plotted models during manuscript integration unless a genuine figure defect is discovered. Any later aesthetic edit requires a new figure revision and a fresh standalone CI/render audit.

## Next work order

Create an isolated **R5 figure-integration layer** from frozen R4 that:

1. materializes these four canonical vector PDFs into the manuscript build;
2. inserts only figure floats, labels, and captions at audited locations;
3. keeps all pre-existing R4 words/equations/proofs otherwise byte-preserved;
4. adds a gate that reconstructs the exact expected R5 transform;
5. compiles R5 in clean CI;
6. renders and visually audits the complete manuscript;
7. only after that considers publication-style compression.
