# Roadmap — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

## Goal

Seek a foundational physical resource principle for temporal information when clock, signal, controller, detector, and memory are finite internal quantum systems. The finished Rev11 random-time law remains frozen on its parent branch.

## Completed theorem chain

### WP02 / WP03 / WP06 — finite-radius survival — PASS

`(R_lin^2/4)[Tr F_N/N] <= T(nu)`.

For globally stationary exact exchange,

`(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`.

### WP04 / WP05 — exact structured autonomous retention — PASS

Hard and mean total-energy constraints have exact sine-chain envelopes and sharp near-lossless coefficient `pi`.

### WP07 / WP08 — zero-radius synthesis — PASS

One-sided boundary:

`Tr F_N/N <= J <= Delta T_U`.

Orthogonal modes admit frequency-weighted quadratic synthesis budgets.

### WP09 — bilateral synthesis — PASS

`sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

The factor-two failure of additive endpoint synthesis is exactly sharp.

### WP10 — one-sided mixed law — PASS

For energy-invariant support,

`Tr F_N/N <= 4T_pre/R_B^2 + Delta T_syn`.

### WP11 / WP12 — noncommuting support and shared-curvature allocation — PASS

Shorting/principal-angle geometry is necessary. The exact second-order resource is one shared operator constraint

`Z_+ + Z_- <= C_Delta`.

The induced allocation `Phi_a` has an exact SDP dual representation.

### WP13 / WP14 — positive action and curvature metric — PASS

`A_G^(2)=(1/4)Tr(G C_Delta)`.

Bilateral costs combine harmonically. Rank-one allocation is controlled by an inverse-curvature principal angle rather than ordinary Hilbert-space overlap.

### WP15 — exact shared-kernel measurement optimum — PASS

`physical resource 12 > SLD 43/4 > accessible Fisher 55/8`.

### WP16 — generic rank-one-kernel common-record theorem — PASS

`sqrt(Tr F_1)<=sqrt(R(B))+sqrt(r kappa)`.

The qutrit signed three-cycle saturates the universal envelope at `9`; naive regular/singular additivity predicts `5`. Exact model-specific accessibility needs additional phase/orientation geometry.

### WP17 — operator/action Pareto target — NO-GO

Exact curvature plus its own scalar action is redundant. Action-only optimization collapses to WP13. Direction killed absent new independent physics.

### WP18 — clean autonomous dual synthesis action — PASS

For globally stationary zero-radius exact exchange:

bilateral

`A_C^(2)+A_S^(2)>=(hbar nu/4)[Tr F_N/N]`,

one-sided

`A_C^(2)+A_S^(2)>=(hbar nu/2)[Tr F_N/N]`.

Both coefficients are exactly sharp in fixed-total-energy shells.

### WP19 — noncommuting autonomous mixed resource/action — PASS

For arbitrary coherent support, use two-sided shorted pre-existing resources `a_+,a_-` and the combined positive clock+signal **kernel endpoint-incidence action**

`A_CS^(2)=(1/4)Tr(G_CS C_Delta)`.

With restricted costs `g_+,g_-`,

`Tr F_N/N`

`<=min{Psi_(a_+)(4A_CS;g_+,g_-),`

`      Psi_(a_-)(4A_CS;g_-,g_+)}`.

The general action is kernel resolved; do not equate it with the full local population Laplacian or signed mean energy.

The shared-kernel qutrit is an exact globally stationary exchange and WP19 returns resource ceiling `12`, after which WP15 gives `43/4` and `55/8` at the statistical/accessibility layers.

### WP20 — multi-gap autonomous spectral-action sum — PASS

For zero-radius pure-boundary modes in one common multiparameter family,

`C_Sigma>=sum_k[Z_(k,+)+Z_(k,-)]`.

For any positive cost `G`,

`sum_k gamma_k Tr F_(N,k)/N <=4A_G,Sigma^(2)`,

`A_G,Sigma^(2)=(1/4)Tr(G C_Sigma)`.

For clean bilateral exact exchanges,

`A_G,Sigma^(2)>=sum_k (hbar nu_k/4)Tr F_(N,k)/N`.

A single fixed Fourier measurement simultaneously saturates every mode and the complete weighted sum in the fixed-total-energy shell

`|n>=|m-n>_C|m+n>_S`.

Thus common-record incompatibility cannot improve the frequency-weighted coefficient.

## Current gate — significance and priority before WP21

The project has reached the point where more theorem production risks becoming a sidequest. Before creating another work package, perform the following audit.

### A. Page--Wootters / shared asymmetry

Compare directly against Carmo--Soares-Pinto, *Quantifying resources for the Page-Wootters mechanism: Shared asymmetry as relative entropy of entanglement*, PRA 103, 052420 (2021).

Question: are WP03/WP18 genuinely new quantitative Fisher/action statements, or reformulations of known asymmetry constraints in a special tangent language?

### B. Fixed-number relative-phase / multiphase metrology

Compare the fixed-shell extremizers and common Fourier measurement against established simultaneous phase-estimation work, including optimal multiphase measurements.

Do not claim novelty for the Fourier readout or simultaneous phase compatibility itself.

### C. Waveform estimation

Compare WP20 against waveform-estimation QCRB/Holevo results, especially PRL 132, 130801 (2024).

Question: is the positive **rank-changing synthesis action** genuinely a different physical resource, or can the theorem be recovered immediately by applying an established waveform bound with an energy norm?

### D. Energy-constrained metrology

Compare explicitly against Chen--Yang, PRL 136, 070801 (2026), which constrains total energy used by preparation, controls, and measurement.

WP18--WP20 use a local kinematic endpoint-incidence action, not total protocol energy. Determine whether this distinction has publication-level value.

### E. Quantitative WAY / quantum reference frames

Check whether energy-conservation measurement limitations or finite-reference-frame results already imply the two-sided clock+signal cost after translation into Fisher information.

### F. Mathematical novelty audit

Shorted operators, SDP allocation, weighted numerical radius, harmonic costs, and PSD-cone curvature are all standard mathematical ingredients. The paper claim, if any, must be a physical theorem not an assemblage of known inequalities.

## Decision rule

A new foundational manuscript is justified only if the audit supports a concise claim such as:

> A globally stationary relative temporal mode has two complementary resource regimes: finite-radius information requires two-sided pre-existing spectral survival, while rank-changing zero-radius information requires two-sided positive spectral synthesis action; both laws are sharp, extend to arbitrary coherent support, and admit a sharp multi-frequency sum.

If prior art already implies this statement with comparable constants and generality, do not force a new paper.

## Secondary work only after the audit

- mixed finite-radius + multi-gap theorem, only if stronger than a mechanical sum of WP19;
- controlled continuum spectral-action limit;
- Gaussian covariance-changing synthesis;
- further exact measurement-accessibility geometry only if directly relevant to the autonomous theorem story.

## Validation

Current validators include all earlier scripts plus:

- `verify_rank_one_kernel_common_record_minkowski.py`
- `verify_autonomous_dual_synthesis_action_law.py`
- `verify_noncommuting_autonomous_mixed_resource_action_law.py`
- `verify_multigap_autonomous_spectral_action_sum_law.py`

Every future nontrivial theorem must receive an independent validator before PASS status.

## Documentation discipline

Every material theorem, failed conjecture, priority collision, or killed direction must be recorded immediately and reflected in `README.md`, `AGENTS.md`, and this file. The repository, not chat history, is authoritative.
