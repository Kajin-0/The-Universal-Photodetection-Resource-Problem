# Deterministic publication figures — Paper 4

This directory generates the standalone four-figure package for the frozen R4 manuscript *Operational temporal-information benchmarks for photodetection*.

## Rules

- The figures do **not** change or extend the frozen manuscript science.
- PDF is the canonical vector output; PNG is a 300-dpi preview.
- The generators use grayscale plus marker/line-style differences for print compatibility.
- Each generator contains hard analytic assertions for its locked scientific values.
- Companion-derived results are explicitly presented as benchmarks rather than Paper-4 novelty.
- The generated directory is a build product. Canonical publication hashes come from the clean GitHub Actions artifact, not a workstation render.

## Generate

```bash
python generate_all.py
```

Dependencies are deliberately small:

```text
numpy
matplotlib
```

The CI workflow pins exact versions.

## Outputs

`generated/` contains:

- `fig1_same_specs_different_information.pdf/.png`
- `fig2_same_saturation_different_timestamps.pdf/.png`
- `fig3_support_survival_synthesis_crossover.pdf/.png`
- `fig4_resonant_implementation_falsification.pdf/.png`
- one locked-value JSON per figure
- `locked_values.json`
- `manifest.json`

## Scientific provenance

Figure 1 is a standard detector illustration from WP08.

Figure 2 uses the exact matched recovery-law benchmark frozen in the companion memory/timestamp program and summarized in WP03. Its theorem/numerical values must remain attributed to that companion work.

Figure 3 is the principal Paper-4 figure. The plotted special path is `a_p=1-p`, `sigma_p=0`, `q=kappa=1`; the manuscript theorem is broader and permits the stated class of stationary inert spectators.

Figure 4 is a textbook equal-frequency resonant realization of the frozen companion prescribed-curvature implementation theorem.

The controlling note is:

`practical_temporal_information/notes/WP12_PUBLICATION_FIGURE_PACKAGE.md`
