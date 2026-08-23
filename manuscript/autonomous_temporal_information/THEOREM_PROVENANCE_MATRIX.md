# Theorem provenance and claim-control matrix

**Branch:** `agent/autonomous-temporal-information-law`

This file is an internal manuscript-control artifact. It maps every planned main-text result to its exact assumptions, authoritative research note, numerical validator, sharpness construction, and prior-art collision. If the manuscript statement changes materially, update this matrix before changing novelty language.

| Main result | Core statement | Essential assumptions | Authoritative source | Validator / audit | Sharpness / counterexample | Mandatory prior-art boundary |
|---|---|---|---|---|---|---|
| R1 | `(R_lin^2/4) Tr F_N/N <= min(D_nu,U_nu) <= T(nu)` | exact nonzero Bohr mode; `R_lin>0`; finite `N`; arbitrary collective POVM; stationary baseline for the sharp endpoint-pair form; arbitrary baseline for the upper-tail version | `WP02_LOCAL_FISHER_NO_GO_AND_ROBUST_TANGENT_RADIUS_LAW.md`; `WP06_NONSTATIONARY_ROBUST_TAIL_AND_HISTORY_STATE_EXTENSION.md` | `verify_robust_tangent_radius_law.py` | fixed-mean-energy two-level family asymptotically saturates generic factor 4 and proves energy-only no-go | numerical radius; modes of asymmetry; QFI as asymmetry |
| R2 | `(R_lin^2/4) Tr F_N/N <= min(T_C,T_S)` | global stationarity; exact exchange `[H_S,A]=+hbar nu A`, `[H_C,A]=-hbar nu A`; `R_lin>0`; arbitrary coherent baseline allowed | `WP03_RELATIONAL_DUAL_ENERGY_SURVIVAL_LAW.md`; WP06 | `verify_relational_autonomous_laws.py`; WP06 analytic audit | two-qubit exchange; total coefficient 2 asymptotically sharp under compatible collective estimation | Page--Wootters; relative-phase metrology; WAY/reference-frame theory |
| R3a | `Tr F_N/N <= J <= Delta T_U` | `C^2` physical family; support-to-kernel one-sided tangent `A=P_U A P`; baseline-empty endpoint | `WP07_NONLINEAR_ZERO_RADIUS_CURVATURE_AND_FINITE_AMPLITUDE_LAW.md` | `verify_nonlinear_zero_radius_law.py`; `WP07_WP18_SINE_COORDINATE_CONVENTION_ERRATUM.md` | minimal pure qubit + equatorial POVM; coherent sideband equality | PSD-cone second-order geometry; rank-changing QFI/Bures |
| R3b | `sqrt(Tr F_N/N) <= sqrt(J_+)+sqrt(J_-)` and clean curvature corollary | `QAQ=0`; pure boundary for clean specialization; arbitrary collective POVM | `WP09_SHARP_BILATERAL_SYNTHESIS_MINKOWSKI_LAW.md` | `verify_bilateral_synthesis_minkowski_law.py` | exact-gap qutrit Fourier measurement; additive curvature law false by factor 2 | Minkowski/triangle inequality; Fisher-symmetric multiparameter measurements |
| R4 | bilateral `A_C^(2)+A_S^(2) >= (hbar nu/4) Tr F_N/N`; one-sided coefficient `1/2` | globally stationary exact exchange; clean baseline-empty local endpoint geometry; `C^2` family | audited `WP18_AUTONOMOUS_DUAL_SYNTHESIS_ACTION_LAW.md` | strengthened `verify_autonomous_dual_synthesis_action_law.py`; `HOSTILE_MATHEMATICAL_AUDIT_WP18_WP20.md` | fixed-total-energy qutrit and qubit; one-copy exact saturation; zero global asymmetry | Page--Wootters/shared asymmetry; energetic coherence/QFI; conservation-law coherence cost; fixed-number phase metrology |
| R5 | mixed arbitrary-support `Psi` master bound | exact exchange; arbitrary coherent support; first-order physicality `QAQ=0`; shorted survival ceilings `a_+/-`; canonical `G_ex`; `C^2` family | audited `WP19_NONCOMMUTING_AUTONOMOUS_MIXED_RESOURCE_ACTION_LAW.md`; WP11--WP13 | strengthened `verify_noncommuting_autonomous_mixed_resource_action_law.py`; hostile audit | shared-kernel fixed-shell qutrit gives exact resource ceiling 12; WP11 four-level example proves shorting geometry necessary | Anderson--Trapp shorted operators; weighted principal angles; SDP/action allocation; energy-constrained metrology |
| R6 | `sum_k gamma_k Tr F_(N,k)/N <= 4 A_(G,Sigma)^(2)` | one common `C^2` multiparameter family; pure boundary modes; one supplied `G>=0`; finite `N`; same arbitrary POVM record for all blocks | audited `WP20_MULTIGAP_AUTONOMOUS_SPECTRAL_ACTION_SUM_LAW.md` | strengthened `verify_multigap_autonomous_spectral_action_sum_law.py`; hostile audit | fixed-shell star family; one DFT measurement simultaneously gives `F_k=2c_k^2 I_2` and saturates full weighted sum | multiphase/covariant measurement theory; waveform Holevo; spectral asymmetry modes |

## Non-negotiable notation/convention checks

1. Complex tangent convention:
   `D_c=(A+A^dagger)/2`, `D_s=(A-A^dagger)/(2i)`.
2. Classical two-quadrature trace:
   `Tr F=sum_y |Tr(A M_y)|^2/p_y`.
3. The convention-consistent minimal one-sided ket uses `x-i y` for `A=2c|1><0|`. The earlier WP07/WP18 `x+i y` form is only the reparameterization `y -> -y`.
4. `A_ex^(2)` in R5 is a **kernel-resolved endpoint-incidence action**, not signed energy curvature or total implementation energy.
5. In R6, the general theorem starts with one positive cost operator `G`. A simple frequency-diagonal physical interpretation is claimed sharply only in the clean mode-separated shell.

## Claim-control failures already found

- Fixed baseline mean energy alone cannot bound arbitrary local high-frequency Fisher information.
- Naive additive bilateral endpoint synthesis is false by factor 2.
- Naive noncommuting-support scalar tail accounting without shorting geometry gives an actual Fisher violation.
- Exact curvature plus its own scalar action is not a new Pareto resource; WP17 killed that direction as redundant.
- Physical resource, SLD-QFI, and accessible common-record Fisher are not interchangeable: benchmark `12 > 43/4 > 55/8`.

## Broad novelty claims prohibited

Do not claim novelty for:

- Page--Wootters relational time;
- Bohr/modes-of-asymmetry decomposition;
- QFI as energetic coherence/asymmetry;
- quantitative WAY or conservation-law coherence costs;
- PSD-cone curvature or rank-changing Bures/QFI geometry;
- shorted operators, principal angles, numerical-radius inequalities, SDP/SOCP duality;
- Fisher-symmetric, Fourier/covariant, multiphase, or waveform-Holevo measurement theory;
- general energy-constrained quantum metrology.

## Candidate novelty sentence allowed only with qualification

A defensible working sentence is:

> We derive finite-copy arbitrary-POVM spectral-resource laws for globally stationary relative temporal modes that distinguish a finite-radius regime backed by pre-existing two-sided spectral survival from a rank-changing zero-radius regime backed by positive second-order two-sided endpoint synthesis action, with sharp fixed-shell and multi-frequency constructions.

Always pair this with `priority remains unverified` until a formal literature review or peer review establishes otherwise.
