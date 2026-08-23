# Roadmap — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

## Goal

Seek a foundational physical resource principle for temporal information when clock, signal, controller, detector, and memory are all internal quantum systems. The finished Rev11 random-time law remains frozen on its parent branch.

## Completed foundations

### WP02 — robust tangent-radius law — PASS

`(R_lin^2/4)[Tr F_N^(nu)/N] <= T(nu)`.

### WP03 / WP06 — autonomous dual survival and coherent-history extension — PASS

`K_N=(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`.

### WP04 / WP05 — exact structured autonomous retention — PASS

Hard cap:

`R_M(k) <= cos^2{pi/[floor(L/k)+2]}`.

Mean total excitation:

`R_M(1) <= (1-lambda)g_m+lambda g_(m+1)`.

The sharp near-lossless coefficient is `pi`.

### WP07 / WP08 — quadratic synthesis — PASS

One-sided boundary:

`Tr F_N/N <= J <= Delta T_U(0)`.

Multimode one-sided sum:

`sum_k w_k Tr F_(N,k)/N <= sum_k w_k Delta_k T_k(0)`.

### WP09 — bilateral Minkowski synthesis — PASS

`sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

For clean empty endpoints,

`Tr F_N/N <= [sqrt(Delta T_+)+sqrt(Delta T_-)]^2`.

The factor-two departure from additive synthesis is exactly sharp.

### WP10 — one-sided mixed survival+synthesis — PASS

For `[P,H]=0`,

`Tr F_N/N <= 4T_pre/R_B^2 + Delta T_syn(0)`.

The `hbar nu/4` energy/action coefficient is exactly sharp.

### WP11 — noncommuting-support shorted-endpoint geometry — PASS

For

`B=PAP`, `K_+=QAP`, `K_-=QA^dagger P`,

`sqrt[Tr F_N/N]`

`<= min{sqrt(J_B^+ + J_+) + sqrt(J_-),`

`       sqrt(J_B^- + J_-) + sqrt(J_+)}`.

Compressed endpoint projectors and support/kernel geometry are necessary. A four-level exact-gap example proves that dropping the geometric factor gives a false observable Fisher-resource bound.

### WP12 — exact shared-curvature allocation — PASS

The exact second-order constraint is

`Z_+ + Z_- <= C_Delta`.

For

`Phi_a(C;R_+,R_-)=sup [sqrt(a+Tr Z_+) + sqrt(Tr Z_-)]^2`,

one has

`Phi_a=inf_(0<eta<1){a/eta+h_(1/eta,1/(1-eta))}`,

where `h_(alpha,beta)` is an SDP with dual

`min_(W>=0) Tr(CW)`

subject to

`R_+ W R_+>=alpha R_+`,

`R_- W R_->=beta R_-`.

### WP13 — positive spectral-action allocation — PASS

For one positive cost operator `G`,

`A_G^(2)=(1/4)Tr(G C_Delta)`

and restricted costs `g_+,g_-`,

`g_+J_+ + g_-J_- <= 4A_G^(2)`.

Pure bilateral synthesis has harmonic effective price

`(1/g_+ + 1/g_-)^(-1)`.

Clean equal gap costs recover the sharp `hbar nu/8` coefficient; one-sided synthesis recovers `hbar nu/4`.

### WP14 — rank-one curvature-metric principal-angle law — PASS

For rank-one synthesized ranges, short to their span and define inverse-curvature capacities `s_u,s_v` and whitened overlap `c`. The complete feasible frontier is

`y_max(x)=s_v[1-x/s_u]/[1-(1-c^2)x/s_u]`.

The relevant angle is defined by the inverse shorted-curvature metric, not ordinary Hilbert-space overlap.

### WP15 — exact common-record Fisher supremum in shared-kernel qutrit — PASS

For the WP12 qutrit benchmark,

`rho0=(I-|q><q|)/2`,

`A=|1><0|-sqrt(2)|2><1|`,

one has

- physical shared-curvature ceiling `12`;
- SLD-QFI trace `43/4`;
- exact one-copy arbitrary-POVM Fisher supremum `55/8`.

The theorem is

`boxed: sup_POVM Tr F_1 = 55/8`.

Upper bound: explicit Hermitian quadratic witness `Y` satisfying

`|<phi|A|phi>|^2 <= <phi|rho0|phi><phi|Y|phi>`

for every vector, with exact LMI factorization.

Lower bound: a sequence of ordinary three-outcome projective measurements with positive baseline probabilities approaches `55/8`.

This proves the hierarchy

`physical resource > quantum-statistical ceiling > accessible common-record Fisher`

can be strict at both arrows even in dimension three.

## Current frontier — WP16 and beyond

### A. WP16: generic rank-one-kernel common-record law — highest immediate priority

Study

`rho0=P/r`, `rank(Q)=1`, `Q=|q><q|`,

and

`A=[[B,b],[a^dagger,0]]`

with `QAQ=0`.

The singular near-kernel directional invariant is

`kappa=max_(||t||=1)|<q|A|t>+<t|A|q>|^2`

`      =||a||^2+||b||^2+2|a^dagger b|`.

A tempting conjecture is

`sup Tr F = support-only optimum + r kappa`.

**Do not assume this. It is false in generic random qutrit tests:** mixed support/kernel projective outcomes can exceed the naive sum. This killed conjecture must be preserved.

Required tasks:

1. formulate the exact arbitrary-POVM dual witness problem;
2. determine whether it reduces to a finite SDP, generalized numerical-radius inequality, or Ando-type matrix condition;
3. identify a solvable nontrivial class containing WP15;
4. find a compact counterexample to naive additive measurement compatibility;
5. add an independent validator before marking WP16 PASS.

### B. Operator + spectral-action Pareto law

WP13 compresses curvature to scalar action while WP14 retains matrix overlap. Derive a joint Pareto theorem retaining both.

### C. Autonomous relational lift

Apply the WP12--WP14 operator/action hierarchy simultaneously from clock and signal Hamiltonian viewpoints for a globally stationary exact exchange tangent.

### D. Gaussian covariance-changing synthesis

Test squeezed-vacuum, parameter-dependent covariance, thermal Gaussian baselines, and correlated multimode synthesis.

### E. Deep priority audit

Compare explicitly against:

- energy-constrained quantum metrology, including Chen--Yang (PRL 136, 070801, 2026);
- generalized numerical radius and Ando-type operator inequalities;
- POVM/frame design convex duality;
- Gill--Massar and Fisher-symmetric measurement bounds;
- singular/rank-changing QFI/Bures geometry;
- Holevo waveform-estimation limits;
- shorted operators and parallel addition;
- quantitative WAY/reference-frame resource theories.

## Publication / significance gate

Do not draft a new foundational manuscript yet.

A publication gate now requires at least:

1. a genuine class-level result beyond the benchmark-specific WP15 witness **or** a sharp autonomous two-sided action theorem;
2. hostile mathematical review of WP11--WP15;
3. deeper priority audit against 2025--2026 metrology and operator-inequality literature;
4. clear separation of standard matrix/SDP ingredients from the frequency-resolved temporal-resource contribution;
5. at least one physically interpretable sharp thought experiment beyond the current qutrit/four-level extremizers.

## Validation requirements

Current independent validators:

- `numerics/verify_robust_tangent_radius_law.py`
- `numerics/verify_relational_autonomous_laws.py`
- `numerics/verify_nonlinear_zero_radius_law.py`
- `numerics/verify_quadratic_synthesis_sum_rule.py`
- `numerics/verify_bilateral_synthesis_minkowski_law.py`
- `numerics/verify_one_sided_mixed_survival_synthesis_law.py`
- `numerics/verify_shorted_endpoint_master_law.py`
- `numerics/verify_operator_curvature_allocation_law.py`
- `numerics/verify_positive_spectral_action_allocation_law.py`
- `numerics/verify_rank_one_curvature_metric_angle_law.py`
- `numerics/verify_exact_common_record_fisher_supremum.py`

Every future WP must add an independent validator before being marked PASS when the theorem has nontrivial algebraic or numerical content.

## Documentation discipline

Every material theorem, failed conjecture, prior-art collision, or validation result must be recorded immediately and reflected in `README.md`, `AGENTS.md`, and this file. The repository, not chat history, is authoritative.
