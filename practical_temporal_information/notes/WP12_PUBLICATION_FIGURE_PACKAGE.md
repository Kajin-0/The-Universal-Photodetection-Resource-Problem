# WP12 — Publication figure package

**Date:** 2026-08-23

**Status:** ACTIVE. Four deterministic local prototypes pass analytic checks and visual QA. Canonical GitHub-CI figure artifact is not yet frozen.

## Purpose

Create the maximum four figures needed by the R4 practical manuscript without changing its scientific text. Figures must be deterministic, directly tied to displayed equations/benchmarks, and independently checked before manuscript integration.

## Global rules

- No decorative/AI-generated scientific imagery.
- Grayscale plus line/marker styles so figures remain legible in print.
- All plotted models use explicit dimensionless normalizations.
- Every generator contains hard assertions for the key analytic values.
- Vector PDF is the canonical publication output; 300-dpi PNG is a preview.
- Figure integration into the manuscript is forbidden until the standalone figure package passes CI and visual QA.
- Companion-derived content must be labeled as a benchmark, not Paper-4 novelty.

## Figure 1 — same conventional specifications, different information spectra

Three panels:

1. common single-pole signal response
   `|H|^2=1/(1+u^2)`, `u=f/f_c`;
2. output noise spectra
   `S_A/S0=1`,
   `S_B/S0=1/5+(4/5)/(1+25u^2)`;
3. normalized single-quadrature FI spectra
   `J_A=1/(1+u^2)`,
   `J_B=(1+25u^2)/[(1+u^2)(1+5u^2)]`.

Locked checks:

- `|H(f_c)|^2=1/2`;
- `S_A(0)=S_B(0)=S0`;
- `J_A(f_c)=1/2`;
- `J_B(f_c)=13/6`;
- `J_B/J_A=13/3=4.333333...` at `f_c`;
- `J_B=J_B(0)/2` at
  `f/f_c=sqrt[(22+sqrt(489))/5]=2.970297775897...`.

Scientific role: conventional specification incompleteness in standard detector language. This is an illustration, not a novelty theorem.

## Figure 2 — same saturation, different timestamp information

Use the exact matched recovery-law benchmark from frozen companion Paper 2/WP03.

Normalized by common mean `m`:

Law A:

- `P(T/m=0.5)=1/2`;
- `P(T/m=1.5)=1/2`.

Law B:

- `P(T/m=0.25)=2/9`;
- `P(T/m=1)=5/9`;
- `P(T/m=1.75)=2/9`.

Both exactly have:

- mean `1`;
- variance `1/4`;
- CV `1/2`;
- identical complete saturation `rm=rho exp(-rho)`.

Locked frozen-companion observables at `lambda m=1`:

- `g_A^(2)(0.75m)=0.7274957073`;
- `g_B^(2)(0.75m)=0.3188717529`;
- one-bit witness `Z=1{D<=0.4m}`:
  `G_Z,A=0`,
  `G_Z,B=0.00443520488427`;
- `P_A(D<=0.4m)=0`;
- `P_B(D<=0.4m)=0.024502903710`.

Four panels show the two recovery laws, their identical saturation, pair-correlation separation, and one-bit FI separation.

Scientific role: practical companion benchmark. Caption/text must attribute the theorem/numbers to frozen Paper 2.

## Figure 3 — support-controlled survival-to-synthesis crossover

This is the principal Paper-4 figure.

For visualization only, use the theorem special path

`a_p=1-p`, `sigma_p=0`, `q=1`, `kappa=1`.

The caption must state that the manuscript theorem permits arbitrary allowed stationary inert spectators and general `q,kappa`.

Panels:

1. seeded support `p>0` versus empty-sideband boundary `p=0`;
2. affine disks for `p=0.15`, `0.05`, `0.01`, collapsing to `R_lin=0`;
3. finite-seed quantity
   `4p/R_lin^2=4(1-2p)^2/(1-p)`
   tending to the boundary curvature
   `Delta P_s(0)=4`;
4. three independent measurement routes:
   baseline/tangent tomography -> `R_lin`,
   zero-seed quadratic fit -> `Delta P_s(0)`,
   phase-sensitive likelihood -> `Tr F`.

Locked radii for the plotted path:

- `R_lin(0.15)=0.510102030610...`;
- `R_lin(0.05)=0.242161052419...`;
- `R_lin(0.01)=0.101529330317...`.

Scientific role: principal candidate original result and noncircular falsification architecture.

## Figure 4 — equal-frequency resonant implementation and failure hierarchy

Panel 1: equal-frequency fixed-energy shell

`H_0=hbar nu(N_C+N_S)`,

with `|L>=|2,0>`, `|M>=|1,1>`, `|U>=|0,2>` all at total bare energy `2hbar nu` and standard exchange coupling `g`.

Panel 2: independently calibrated equality

`V_impl=8(gt)^2`,

`Tr C/2=8(gt)^2`,

`A_ex/(hbar nu)=V_min`.

Plot both calibrations on the same exact quadratic curve for representative `gt=0.1,...,0.5`.

Panel 3: failure hierarchy

- Level I: loss, unequal bare frequencies, omitted pump/controller, or other model failure;
- Level III: calibrated ideal benchmark fails to saturate `V=Tr C/2`;
- Level II: under independently verified theorem assumptions, `V<Tr C/2` challenges the companion lower bound.

Scientific role: standard-physics realization of the frozen companion implementation theorem, not Paper-4 novelty.

## Local prototype QA

All four local generators currently pass their internal analytic assertions and visually render without clipping/overlap after iterative cleanup.

Do **not** record local prototype PDF hashes as publication artifacts. The canonical hashes will come from the GitHub Actions figure-build artifact after the scripts are committed and rerun in a clean environment.

## Immediate work order

1. commit figure generators and source README;
2. add isolated figure-build CI workflow;
3. run all four generators in clean CI;
4. upload vector PDFs, PNG previews, and locked value files as one artifact;
5. download exact artifact, record hashes/sizes, and render/inspect all four PDFs;
6. repair only figure-specific defects;
7. freeze WP12;
8. only then create an isolated manuscript revision that inserts figures/captions into R4.
