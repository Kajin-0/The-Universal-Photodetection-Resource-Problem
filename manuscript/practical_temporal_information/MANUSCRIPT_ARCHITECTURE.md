# Manuscript architecture — practical temporal-information benchmarks

**Provisional target:** Physical Review Applied, Regular Article.

**Working title:** *Operational temporal-information benchmarks for photodetection*

## One-sentence thesis

Conventional detector specifications such as static NEP, response bandwidth, saturation curves, and timing jitter remain essential but do not in general determine the information transferred about time-dependent optical signals; temporal Fisher information provides a common operational quantity, and a controllable optical sideband seed exposes a measurable transition from pre-existing spectral support to second-order spectral synthesis.

## Abstract structure

1. Standard detector problem: common specifications do not uniquely determine temporal estimation performance.
2. Measurement bridge: `Tr F/T=2/NEP(f)^2` in the linear-Gaussian limit; Poisson timestamp/jitter counterpart.
3. Concrete conventional-spec counterexample: equal DC NEP and equal response bandwidth but `13/3` FI ratio at `f_c`.
4. Memory benchmark from companion random-time paper: identical saturation curve can hide different timestamp information.
5. Principal original result: `lim_(p->0+)4p/R_lin^2=Delta P_s(0)` and ideal sideband saturation.
6. Compact fixed-energy beam-splitter implementation and falsification matrix.

## Section I — What conventional detector specifications do not determine

### Purpose

Start entirely in standard detector language.

### Required equations

For peak input power quadratures and one-sided output PSD:

`F_xx/T=F_yy/T=|R(f)|^2/S_n(f)=1/NEP(f)^2`.

Then introduce the explicit A/B model:

`|H|^2=1/(1+x^2)`.

A: `S_A/S0=1`.

B: `S_B/S0=1/5+(4/5)/(1+25x^2)`.

`J_A=1/(1+x^2)`.

`J_B=(1+25x^2)/[(1+x^2)(1+5x^2)]`.

At `x=1`, `J_B/J_A=13/3`.

Half-DC FI for B: `x=sqrt[(22+sqrt(489))/5]≈2.9703`.

### Message

The pair `{NEP(0), response f_3dB}` does not specify the FI spectrum. Full signal transfer and full noise spectrum are needed.

Do not call this a new theorem.

## Section II — From analog noise to timestamp information

### Analog bridge

Derive the convention-controlled Gaussian likelihood result concisely.

### Timestamp bridge

For fractional Poisson modulation:

`F_xx/T=F_yy/T=lambda0/2`, `Tr F/T=lambda0`.

Independent jitter:

`Tr F/T=lambda0 |Phi_J(Omega)|^2`.

Mention exact agreement between the optical-power Poisson limit and shot-noise NEP.

### Memory benchmark

Introduce the frozen companion Type-II theorem without reproducing its proof:

`r(lambda)=lambda exp(-lambda m)` for every iid recovery law of mean `m`, yet complete timestamp FI at `lambda m=1` is zero iff recovery is deterministic.

Use one explicit equal-mean/equal-variance pair only as an illustration.

The Paper-4 contribution here is the proposed characterization protocol and falsification interpretation.

## Section III — Spectral support: survival to synthesis

This is the main original section.

### Baseline model

`rho_p=(1-p)|c><c|+p|s><s|`, `0<=p<1/2`.

Two-mode mixing:

`U(x,y)=exp{kappa[(x-iy)|s><c|-(x+iy)|c><s|]}`.

### Exact measured sideband population

`P_s=p+(1-2p)sin^2(kappa sqrt(x^2+y^2))`.

### Affine radius

`R_lin^2=p(1-p)/[kappa^2(1-2p)^2]`.

### Finite-support bound

`(R_lin^2/4)Tr F<=p`.

### Boundary curvature

At `p=0`,

`Delta P_s(0)=4kappa^2`,

`Tr F<=4kappa^2`.

### Central theorem

`lim_(p->0+)4p/R_lin^2=4kappa^2=Delta P_s(0)`.

Interpretation: the finite-radius survival resource and its radius vanish together while their ratio tends to the second-order synthesis curvature.

### Saturation

Give the fixed equatorial qubit POVM at the one-sided boundary or move its explicit kets to an appendix/supplement if space is tight.

### Bilateral phase modulation

Ordinary weak phase modulation:

`P_+=P_-=(x^2+y^2)/4+O(beta^4)`.

`Delta P_+=Delta P_-=1`.

Bilateral bound:

`Tr F<=[sqrt(Delta P_+)+sqrt(Delta P_-)]^2=4`.

Fixed frequency-bin interferometer attains `Tr F=4`.

State explicitly that direct sideband-power measurement estimates the resource curvature but is not itself the phase-sensitive FI measurement.

## Section IV — Standard Hamiltonian implementation benchmark

Use the fixed-total-energy two-boson manifold:

`|M>=|1,1>`, `|L>=|2,0>`, `|U>=|0,2>`.

For the calibrated resonant exchange generators and interaction time `t`:

`K_j=t H_j/hbar`,

`V_impl=(t^2/hbar^2)sum_j Var(H_j)`.

In the benchmark:

`V_min=8(gt)^2=(1/2)Tr C`,

`A_ex=hbar nu V_min=8 hbar nu (gt)^2`.

Emphasize exact fixed total bare-energy distribution.

Do not interpret this as thermodynamic work, consumed RF energy, controller bandwidth, or peak Hamiltonian norm.

## Section V — Falsification matrix

Use one table with columns:

- model/result;
- measured quantities;
- predicted equality/inequality;
- assumptions to verify independently;
- interpretation of failure.

Rows:

1. Gaussian NEP/FI reduction — Level I.
2. Poisson+jitter timestamp reduction — Level I.
3. Type-II memory benchmark — model/companion theorem test.
4. finite-seed survival inequality — Level II if support model verified.
5. zero-seed curvature inequality — Level II.
6. ideal phase-modulation equality — Level III.
7. resonant beam-splitter equality — Level III plus companion lower-bound check.

## Section VI — Discussion

Key conclusions:

1. standard specifications are not discarded; they are incomplete for arbitrary temporal tasks;
2. FI supplies a common operational currency across analog and timestamp detectors;
3. detector memory and spectral support represent distinct mechanisms of temporal-information limitation;
4. the support seed gives a direct experimental knob for moving between survival and synthesis regimes;
5. the framework is falsifiable at model, resource-law, and saturator levels.

## Figures

### Fig. 1 — Same conventional specs, different information spectrum

Panels: identical response; noise PSDs; resulting normalized FI spectra. Mark `f_c` and the `13/3` FI ratio.

### Fig. 2 — Same Type-II saturation, different timestamp information

Use one saturation curve plus two interval/correlation or simple statistic responses. Attribute theorem to companion paper.

### Fig. 3 — Support-controlled survival-to-synthesis crossover

Show carrier/sideband populations versus seed, shrinking affine disk, and convergence of `4p/R_lin^2` to `Delta P_s`.

### Fig. 4 — Standard Hamiltonian benchmark + falsification map

Fixed-energy `|1,1> <-> |2,0>,|0,2>` exchange plus measured `gt`, endpoint curvature and FI/cost arrows.

## Supplement strategy

Keep main text experimentally legible. Supplement should contain:

- Gaussian FI prefactor derivation;
- Poisson/jitter derivation;
- exact WP08 algebra;
- full two-bin radius calculation and saturating POVMs;
- beam-splitter matrix elements and cost calculation;
- no duplicate proofs from the mature papers.

## Claim language

Prefer:

- “we show in the explicit support-controlled model...”
- “the companion random-time analysis establishes...”
- “the implementation theorem gives...”
- “this provides a direct falsification protocol...”

Avoid:

- “first ever”;
- “new universal detector metric”;
- “NEP is obsolete”;
- “dead-time timestamp information is newly discovered”;
- “sideband Fisher information is new”;
- “unitary coupling cost is work.”
