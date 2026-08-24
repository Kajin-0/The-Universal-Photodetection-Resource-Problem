# AGENTS — Practical Temporal-Information Benchmarks

**Active branch:** `agent/practical-temporal-information-benchmarks`

The repository, not chat history, is authoritative.

## Mission

Create a fourth paper that translates the temporal-information resource program into standard detector physics and explicit falsification tests. Do not modify the frozen scientific theorem/proof layers of the three mature papers unless a genuine defect is exposed.

## Read first

1. `README.md`
2. `notes/WP01_LINEAR_GAUSSIAN_FISHER_NEP_BRIDGE.md`
3. `notes/WP02_POISSON_TIMESTAMPS_AND_JITTER.md`
4. `notes/WP03_DEAD_TIME_RECOVERY_INFORMATION_BENCHMARKS.md`
5. `notes/WP04_OPTICAL_SIDEBAND_SURVIVAL_SYNTHESIS_CROSSOVER.md`
6. `notes/WP05_RESONANT_EXCHANGE_UNITARY_COUPLING_BRIDGE.md`
7. root `docs/CURRENT_RESEARCH_STATE.md`

## Current result stack

### WP01 — analog Gaussian

`F_xx/T=F_yy/T=1/NEP(f)^2`, `Tr F/T=2/NEP(f)^2` under the convention lock.

### WP02 — ideal timestamps

`Tr F/T=lambda_0` for fractional Poisson modulation. Optical-power form exactly matches ideal shot-noise NEP. Independent jitter gives factor `|Phi_J(Omega)|^2`.

### WP03 — detector memory

Standard saturation can be information-incomplete. Deterministic Type-II recovery at `lambda tau=1` has `G(0)=0` but nonzero information at every nonzero frequency. Arbitrary finite-mean iid recovery shares `r=lambda exp(-lambda m)`, yet `G_DC=0` at the common maximum iff recovery is deterministic. Exact equal-mean/equal-variance/equal-saturation laws have different timestamp information.

### WP04 — sideband support crossover

Seeded carrier/sideband model:

`R_lin^2=p(1-p)/[kappa^2(1-2p)^2]`,

`(R_lin^2/4)Tr F<=p`.

At `p=0`,

`Delta P_s=4kappa^2`, `Tr F<=Delta P_s`,

with exact crossover

`lim_(p->0+)4p/R_lin^2=Delta P_s`.

Ordinary ideal weak phase modulation saturates the bilateral boundary law with `Delta P_+=Delta P_-=1`, `Tr F=4` under a fixed phase-sensitive three-mode analyzer.

### WP05 — resonant exchange implementation

Two resonant modes:

`H_0=hbar nu(N_C+N_S)`.

Standard beam-splitter exchange acts inside the `N_tot=2` shell

`|2,0>, |1,1>, |0,2>`.

For `U(x,y)=exp[-i g t(xB_x+yB_y)]` and baseline `|1,1>`:

`Var(K_x)=Var(K_y)=4(g t)^2`,

**`V_impl=8(g t)^2`.**

Endpoint curvature:

`Delta P_L=Delta P_U=8(g t)^2`,

`Tr C=16(g t)^2`,

so

**`V_min=(1/2)Tr C=8(g t)^2`.**

Autonomous action:

**`A_ex^(2)=8 hbar nu(g t)^2`.**

The total bare-energy distribution is exactly fixed at `2hbar nu` throughout.

For fixed interaction duration,

**`V_impl=(t^2/hbar^2)sum_j Var(H_j)`.**

This is the practical Hamiltonian interpretation. Do not call it work, consumed RF energy, average interaction energy, operator norm, peak coupling, controller bandwidth, or fixed-controller-spectrum optimum.

Practical falsification compares independently calibrated `g t` with independently measured endpoint Hessians:

`8(g t)^2=(1/2)[Delta P_L+Delta P_U]`.

## Publication status before WP06

WP03 and WP04 are the likely core new practical results. WP01/WP02 supply the common measurement language. WP05 supplies a standard Hamiltonian interpretation of the companion theorem.

Do not draft a manuscript yet. First decide the minimum coherent stack and then run prior art.

## Immediate work order

1. **WP06:** integrated falsification matrix, rank scientific value, define minimum Paper-4 result stack, demote tutorial-only material.
2. **WP07:** dedicated prior-art/significance gate before manuscript drafting.

## Claim discipline

No prize-level framing. No novelty claim for standard NEP, generic FI sensing, Poisson/dead-time formulas, renewal spectra, sideband generation, SU(2)/beam-splitter physics, or standard frequency-bin interferometry. Assign novelty only after WP07.

## Documentation rule

After every material advance, update the corresponding note and this handoff. When the frontier changes, also update root `README.md`, `AGENTS.md`, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`.
