# WP08 — Final pre-manuscript stack and conventional detector-specification incompleteness

**Date:** 2026-08-23

**Status:** PASS. The practical program has a coherent non-duplicative manuscript stack. Manuscript drafting may begin after this note is synchronized into the handoff files.

## 1. Purpose

Close the final pre-manuscript gate by:

1. giving one explicit standard-detector example showing that conventional sensitivity plus responsivity bandwidth does not determine temporal-information performance;
2. locking assumptions, units and parameter conventions;
3. separating new Paper-4 science from cited upstream theorems and standard detector/statistical bridges;
4. fixing the minimal manuscript architecture.

## 2. Conventional detector-specification incompleteness

Consider two linear detectors estimating peak optical-power quadratures `x,y` in watts at modulation frequency `f`.

Both have the same DC responsivity scale `R0` and the same normalized single-pole response

`|H(f)|^2 = 1/[1+(f/f_c)^2]`.

Thus both have the same ordinary responsivity 3-dB frequency `f_c`.

Let both also have the same DC output-noise PSD `S0`, so both have the same DC NEP

`NEP(0)=sqrt(S0)/R0`.

### Detector A — white noise

`S_A(f)=S0`.

Using WP01,

`F_A,xx/T = (R0^2/S0) / [1+x^2]`,

where `x=f/f_c`.

Normalize by the common DC single-quadrature FI rate `I0=R0^2/S0`:

`J_A(x)=1/(1+x^2)`.

At `x=1`,

`J_A(1)=1/2`.

### Detector B — white floor plus Lorentzian excess noise

Take the physically ordinary colored-noise model

`S_B(f)/S0 = 1/5 + (4/5)/[1+25 x^2]`.

At DC,

`S_B(0)=S0`,

so Detector B has exactly the same DC NEP as A.

The responsivity is also identical, so the ordinary response 3-dB bandwidth is exactly the same `f_c`.

But

`S_B/S0 = (1+5x^2)/(1+25x^2)`

and therefore

`J_B(x) = (1+25x^2)/[(1+x^2)(1+5x^2)]`.

At the advertised response bandwidth `x=1`,

`J_B(1)=26/(2*6)=13/6`.

Thus

`J_B(1)/J_A(1) = (13/6)/(1/2) = 13/3 ≈ 4.3333`.

So two detectors with the same DC NEP and exactly the same responsivity transfer function can differ by more than a factor four in Fisher information at the nominal 3-dB response frequency solely because their noise spectra differ.

### Half-DC information frequency for B

Solve

`J_B(x)=1/2`.

With `y=x^2`,

`(1+25y)/[(1+y)(1+5y)] = 1/2`,

which gives

`5y^2-44y-1=0`.

The positive root is

`y=(22+sqrt(489))/5 ≈ 8.8226688775`,

hence

`x=sqrt[(22+sqrt(489))/5] ≈ 2.970297776`.

Therefore B remains above half its **DC Fisher-information rate** until almost `3 f_c`, despite having the same responsivity 3-dB bandwidth `f_c` as A.

The FI spectrum is nonmonotonic because the Lorentzian excess-noise term rolls off faster than the signal response. That is physically allowed and illustrates why a response-only bandwidth is not an information bandwidth.

### Interpretation

This is not presented as a deep novelty theorem. It is a clean detector-physics counterexample to the proposition that the pair

`{DC NEP, responsivity 3-dB bandwidth}`

specifies temporal estimation performance.

It does not. Frequency-resolved signal transfer **and** frequency-resolved noise are required, equivalently the full weighting

`|R(f)|^2/S_n(f)`.

## 3. Locked units and conventions

### 3.1 Analog bridge

Input:

`P(t)=P0 + x cos(2πft) + y sin(2πft)`

with `x,y` **peak** optical-power quadratures in watts.

`R(f)` is complex responsivity in A/W or V/W.

`S_n(f)` is a **one-sided** output-noise PSD in A^2/Hz or V^2/Hz.

Long observation, stationary Gaussian noise, parameter-independent covariance.

Then

`F_xx/T=F_yy/T=|R(f)|^2/S_n(f)=1/NEP(f)^2`,

`Tr F/T=2/NEP(f)^2`.

Units:

- `F_xx`: W^-2;
- `F_xx/T`: W^-2 s^-1;
- `NEP`: W/sqrt(Hz)=W sqrt(s);
- `1/NEP^2`: W^-2 s^-1.

### 3.2 Poisson timestamp bridge

Fractional modulation:

`lambda(t)=lambda0[1+x cos(Omega t)+y sin(Omega t)]`,

with dimensionless peak `x,y`.

Then ideal long-time Poisson timestamps give

`F_xx/T=F_yy/T=lambda0/2`,

`Tr F/T=lambda0`.

Independent timing jitter `J` multiplies the trace spectrum by

`|Phi_J(Omega)|^2`.

### 3.3 Sideband support model

The sideband seed `p` is a dimensionless baseline population/probability in the normalized finite-dimensional support model.

Local coordinates `x,y` are dimensionless and use the fixed Euclidean quadrature metric inherited from the flagship theorem.

`R_lin` is the affine physical radius in those same coordinates.

`Delta P_s(0)=partial_x^2 P_s(0)+partial_y^2 P_s(0)` is dimensionless per squared local coordinate.

Do not mix this normalization with arbitrary RMS modulation conventions without re-deriving prefactors.

### 3.4 Hamiltonian benchmark

For a fixed duration `t` and local Hamiltonian family with dimensionless coordinates,

`K_j=t H_j/hbar`.

Thus

`V_impl=sum_j Var(K_j)=(t^2/hbar^2)sum_j Var(H_j)`

is dimensionless.

For the resonant beam-splitter benchmark `g` has units s^-1 and `g t` is dimensionless.

The autonomous action `A_ex` has units of action because it is `hbar nu` times a dimensionless local coupling cost under the flagship/companion normalization.

## 4. Final claim classification

### New candidate Paper-4 theorem / corollary

**P4-T1 — support-seed crossover.**

For the explicit positive-semidefinite carrier/sideband family of WP04,

`lim_(p->0+) 4p/R_lin^2 = Delta P_s(0)`.

This gives an exact controlled transition from the finite-radius survival resource to the rank-boundary second-order synthesis resource.

**P4-C1 — ideal phase-modulation boundary saturator.**

Under the locked weak-modulation convention and phase-sensitive analyzer, ordinary ideal phase modulation saturates the bilateral boundary population-curvature Fisher law.

Novelty priority remains unverified/not certified; WP07 found no direct collision.

### Cited upstream theorem/benchmark

**P4-B1 — Type-II information incompleteness.**

Use the frozen random-time paper's theorem that fixed mean recovery fixes the entire homogeneous saturation curve but not timestamp information; at the common maximum deterministic recovery is uniquely information-singular, and explicit matched conventional summaries can hide different timestamp information.

Do not restate this as a new proof/theorem. Cite the upstream paper and focus here on the measurement protocol and falsification consequences.

**P4-B2 — prescribed-curvature implementation cost.**

Use the frozen PRA companion's theorem `V_min=(1/2)Tr C`, with WP05's resonant beam-splitter realization as a standard-physics benchmark.

### Standard bridge/background

**P4-S1 — Gaussian NEP/FI relation.**

`Tr F/T=2/NEP(f)^2` under the locked convention.

**P4-S2 — ideal Poisson/jitter relation.**

`Tr F/T=lambda0 |Phi_J(Omega)|^2` for fractional two-quadrature modulation.

**P4-S3 — conventional specification incompleteness example.**

Same DC NEP and same responsivity bandwidth do not fix the FI spectrum; the A/B model above is an explicit illustration, not a priority claim.

## 5. Final main-text architecture

### I. What conventional detector specifications do not determine

Open with the explicit A/B colored-noise example. This immediately grounds the problem without abstract quantum language.

Then derive the short NEP/FI relation and timestamp counterpart.

### II. Memory: identical saturation does not imply identical information

Present the Type-II theorem as a result of the companion random-time paper, then formulate a concrete characterization protocol using source-rate sweeps plus interval/timestamp statistics.

### III. Spectral support: from survival to synthesis

This is the new theorem section. Present the controllable seed `p`, finite-radius bound, exact crossover, zero-seed boundary law, and phase-modulation saturator.

### IV. Standard Hamiltonian implementation

Present the fixed-energy beam-splitter benchmark compactly and connect measured endpoint curvature to calibrated `g t`.

### V. Falsification matrix

State Level I/II/III tests and what each observed failure means.

### VI. Discussion

Emphasize that the framework does not replace NEP, bandwidth, D*, dead-time curves or standard Hamiltonian modeling; it identifies what those conventional summaries do and do not determine about temporal-information transfer.

## 6. Figure architecture

Maximum four figures:

1. **Same conventional specs, different FI spectrum** — A/B responsivity/noise/FI comparison.
2. **Same Type-II saturation, different timestamp information** — practical imported benchmark.
3. **Seeded support -> empty-sideband synthesis** — main new figure showing `p>0` finite radius and `p=0` curvature limit.
4. **Fixed-energy exchange + falsification map** — resonant beam-splitter benchmark and measurement arrows.

## 7. Manuscript decision

**PASS. Create the manuscript workspace.**

The paper is not an omnibus restatement of the three mature papers. Its new scientific center is WP04; its broader value is the conversion of the existing program into standard detector measurements and explicit falsification protocols.

The manuscript must remain useful to a detector physicist even if all resource-theory notation after the introductory bridge were removed.
