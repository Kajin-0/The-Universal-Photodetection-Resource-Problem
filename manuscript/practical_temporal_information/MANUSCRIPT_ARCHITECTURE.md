# Manuscript architecture — practical temporal-information benchmarks

**Provisional target:** Physical Review Applied, Regular Article.

**Working title:** *Operational temporal-information benchmarks for photodetection*

**Current scientific freeze:** R4; figures not yet integrated.

## One-sentence thesis

Conventional detector specifications such as static NEP, response bandwidth, saturation curves, and timing jitter remain essential but do not in general determine the information transferred about time-dependent optical signals; temporal Fisher information supplies a common operational quantity, and a controllable incoherent sideband seed exposes a measurable finite-radius-to-boundary crossover between pre-existing spectral support and second-order spectral synthesis.

## Claim hierarchy

### Candidate original Paper-4 content

1. stationary selected-mode seed regularization:
   `lim_(p->0+)4p/R_lin^2=Delta P_s(0)`;
2. independent measurement/falsification architecture for radius, curvature, and FI;
3. ideal weak phase-modulation boundary saturation under the locked convention.

### Cited companion results

- Type-II recovery information theorem from the frozen random-time paper;
- prescribed-curvature unitary-coupling theorem from the frozen PRA paper.

### Standard detector/optics bridges

- `Tr F/T=2/NEP(f)^2` in the linear stationary Gaussian regime;
- ideal Poisson timestamp/jitter relation;
- colored-noise detector specification counterexample;
- standard equal-frequency resonant beam-splitter realization.

## Novelty boundary

Finite FI associated with probabilities/eigenvalues that vanish quadratically at a boundary is prior art (Gefen--Rotem--Retzker 2019; Safranek 2017). The paper must never claim that mechanism itself as new.

The candidate new structure is the experimentally controlled continuation from a nonzero population seed and nonzero affine physical radius to the empty-sideband curvature, plus the noncircular detector-facing test.

## Main-text architecture

### I. Introduction

Start with standard photodetector specifications and the question they do not answer: how much information does the complete record contain about a specified temporal perturbation?

Do not open with resource theory.

### II. Detector information in standard measurement language

#### A. Linear Gaussian detector

For peak input-power quadratures and one-sided output PSD:

`F_xx/T=F_yy/T=|R(f)|^2/S_n(f)=1/NEP(f)^2`,

so

`Tr F/T=2/NEP(f)^2`.

#### B. Equal DC NEP and equal response bandwidth do not fix temporal FI

Common signal response:

`|H|^2=1/(1+u^2)`, `u=f/f_c`.

Detector A noise:

`S_A/S0=1`.

Detector B noise:

`S_B/S0=1/5+(4/5)/(1+25u^2)`.

FI spectra:

`J_A=1/(1+u^2)`,

`J_B=(1+25u^2)/[(1+u^2)(1+5u^2)]`.

At `u=1`:

`J_B/J_A=13/3≈4.33`.

Detector B reaches half its DC FI at

`u=sqrt[(22+sqrt(489))/5]≈2.9703`.

This is an illustrative specification-incompleteness example, not a new theorem.

#### C. Ideal photon timestamps and independent jitter

`F_xx/T=F_yy/T=lambda0/2`,

`Tr F/T=lambda0`,

and independent jitter multiplies by `|Phi_J(Omega)|^2`.

### III. Detector memory: identical saturation does not imply identical information

Use the frozen companion Type-II theorem without reproducing its proof:

`r(lambda)=lambda exp(-lambda m)`

for the entire iid recovery-law class of mean `m`, while at `lambda m=1` timestamp DC FI is zero iff recovery is deterministic.

Paper-4 contribution here: practical model-discrimination/falsification framing only.

### IV. Spectral support: from survival to synthesis

This is the principal original section.

#### A. Stationary selected pair with spectators

Let free-Hamiltonian modes satisfy

`E_s-E_c=hbar Omega`.

Baseline:

`rho_p=a_p|c><c|+p|s><s|+sigma_p`,

with `[rho_p,H]=0`, stationary inert spectators, `a_p>p`, `a_p->q>0`, and an incoherent/phase-randomized sideband population seed.

Local converter:

`U(x,y)=exp{kappa[(x-iy)|s><c|-(x+iy)|c><s|]}`.

Exact sideband population:

`P_s(p;r)=p+(a_p-p)sin^2(kappa r)`.

Exact affine radius:

`R_lin^2=a_p p/[kappa^2(a_p-p)^2]`.

Finite-seed survival bound:

`(R_lin^2/4)Tr F<=p`.

#### B. Boundary and central proposition

At `p=0`:

`Delta P_s(0)=4kappa^2 q`,

`Tr F<=Delta P_s(0)`.

Central result:

**`lim_(p->0+)4p/R_lin^2=4kappa^2 q=Delta P_s(0)`.**

Completed equatorial active-subspace POVM plus spectator projector attains

`Tr F=Delta P_s(0)`.

#### C. Noncircular operational protocol

Measure separately:

1. baseline/tangent tomography -> `R_lin`;
2. zero-seed second-order sideband fit -> `Delta P_s(0)`;
3. phase-sensitive likelihood -> FI.

The identity itself is a selected-model test. Exceeding the FI resource bound under independently verified theorem assumptions is the stronger Level-II test.

#### D. Bilateral weak phase modulation

`P_+=P_-=(x^2+y^2)/4+O[(x^2+y^2)^2]`,

`Delta P_+=Delta P_-=1`,

so

`Tr F<=[sqrt(Delta P_+)+sqrt(Delta P_-)]^2=4`,

with an ideal fixed interferometric measurement attaining equality.

### V. Standard Hamiltonian implementation benchmark

Use equal-frequency resonant bosonic modes:

`H_0=hbar nu(N_C+N_S)`.

Fixed `N_tot=2` states:

`|M>=|1,1>`, `|L>=|2,0>`, `|U>=|0,2>`.

For calibrated interaction time `t`:

`K_j=tH_j/hbar`,

`V_impl=(t^2/hbar^2)sum_j Var(H_j)`.

Ideal benchmark:

`V_min=8(gt)^2=(1/2)Tr C`,

`A_ex=hbar nu V_min`.

State explicitly:

- total bare-energy distribution is fixed because the equal-frequency exchange commutes with `H_0`;
- unequal bare frequencies require explicit pump/controller degrees of freedom;
- this quadratic coupling cost is not thermodynamic work, RF consumption, peak Hamiltonian norm, or controller bandwidth.

### VI. What would falsify the framework?

REVTeX paragraph/list/table machinery proved fragile in the initial draft. Keep the current conservative bold-paragraph falsification blocks unless a later journal-layout need justifies another representation.

Required categories:

- Gaussian NEP/FI reduction — Level I;
- Poisson+jitter reduction — Level I;
- Type-II memory benchmark — selected recovery-model/companion test;
- finite-seed survival — Level II only under verified stationary selected-mode hypotheses;
- zero-seed curvature — Level II;
- ideal phase-modulation equality — Level III;
- resonant exchange equality — Level III plus companion lower-bound interpretation.

### VII. Discussion

Emphasize:

1. standard detector metrics remain useful but are incomplete for arbitrary temporal tasks;
2. FI provides a common operational quantity across analog and event records;
3. memory and spectral support are distinct mechanisms;
4. the incoherent support seed is a direct control parameter for moving from finite-radius survival to boundary synthesis;
5. model/resource/saturator failures have different meanings;
6. no experimental data are claimed.

## Publication figures — WP12

Maximum four figures. All must be deterministic and pass numerical + visual QA before manuscript integration.

### Fig. 1 — Same conventional specs, different information spectrum

Three compact panels:

1. common `|H(f)|^2`;
2. `S_A/S0`, `S_B/S0`;
3. `J_A`, `J_B`.

Mark `f_c`, `J_B/J_A=13/3`, and `u=2.9703` half-DC-FI point for B.

### Fig. 2 — Same Type-II saturation, different timestamp information

Show one common normalized saturation curve plus one compact statistic/information contrast for two recovery laws. Explicitly label the theorem as a companion result. Do not reproduce a full Paper-2 figure set.

### Fig. 3 — Support-controlled survival→synthesis crossover

Principal figure. Include:

- stationary carrier/sideband + spectator schematic;
- finite-seed affine disk shrinking with `p`;
- `4p/R_lin^2` versus `p` approaching `Delta P_s(0)=4kappa^2 q`;
- distinct measurement routes: tangent tomography, zero-seed curvature fit, phase-sensitive FI.

Use a simple normalized path such as `a_p=1-p`, `q=1`, `kappa=1` for plotted numbers, while caption states the general theorem.

### Fig. 4 — Equal-frequency resonant implementation + falsification map

Show the fixed-energy `|1,1>` to `|2,0>,|0,2>` exchange, calibrated `gt`, endpoint curvature/cost identity, and a compact Level-I/II/III interpretation map.

## Figure-production rules

- deterministic script/source committed with each figure;
- no decorative AI imagery;
- no unlabeled arbitrary units unless explicitly normalized;
- all equations/data checked independently;
- journal-readable labels at single-column/two-column scale;
- export vector PDF/SVG plus high-resolution PNG preview as needed;
- visual QA before manuscript integration.

## Supplement strategy

Keep main text experimentally legible. If needed, supplement may contain:

- Gaussian FI prefactor derivation;
- Poisson/jitter derivation;
- exact colored-noise algebra;
- detailed selected-mode affine-radius derivation and saturating POVM;
- resonant beam-splitter matrix elements/cost calculation.

Do not duplicate proofs from the mature companion papers.

## Claim language

Prefer:

- “we show in the explicit stationary support-controlled model...”
- “the companion random-time analysis establishes...”
- “the companion implementation theorem gives...”
- “this provides a direct falsification protocol...”

Avoid:

- “first ever”;
- “new universal detector metric”;
- “NEP is obsolete”;
- “dead-time timestamp information is newly discovered”;
- “finite FI from a zero-probability outcome is new”;
- “unitary coupling cost is work.”
