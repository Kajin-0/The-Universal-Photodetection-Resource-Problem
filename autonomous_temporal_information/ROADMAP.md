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

Gap weighting gives the WP08 positive synthesis-energy law.

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

The law removes WP11's double counting of shared curvature and has exact one-sided, orthogonal, and coincident-subspace limits.

### WP13 — positive spectral-action allocation — PASS

Use one positive kernel cost operator

`G=epsilon_U QPi_UQ + epsilon_D QPi_DQ`

and define

`A_G^(2)=(1/4)Tr(G C_Delta)`.

For synthesized ranges,

`g_+=lambda_min[R_+ G R_+ |_(R_+)]`,

`g_-=lambda_min[R_- G R_- |_(R_-)]`.

Then

`boxed: g_+J_+ + g_-J_- <= 4A_G^(2)`.

If a relevant `g` vanishes, no finite action-only bound exists for that orientation.

For `e=4A_G^(2)`, `p=g_+`, `q=g_-`, and upper-oriented internal resource `a`,

`boxed: Psi_a(e;p,q)=`

- `(sqrt(a)+sqrt(e/q))^2`, if `e<=a p^2/q`;
- `(e+p a)(1/p+1/q)`, if `e>=a p^2/q`.

For pure bilateral synthesis,

`Psi_0=e(1/p+1/q)`.

Thus the effective endpoint price is harmonic. Clean equal gap costs `p=q=hbar nu` recover the sharp WP09 coefficient

`A_G^(2) >= (hbar nu/8)[Tr F_N/N]`,

while one-sided synthesis recovers the WP07/WP10 `hbar nu/4` coefficient.

An exact unequal-cost qutrit and one Fourier measurement saturate the harmonic coefficient for arbitrary positive `p,q`.

### WP14 — rank-one curvature-metric principal-angle law — PASS

For

`R_+=|u><u|`, `R_-=|v><v|`,

short first to

`C_S=Short_span{u,v}(C)`.

Define

`s_u=1/<u|C_S^(-1)|u>`,

`s_v=1/<v|C_S^(-1)|v>`,

`c=|<u|C_S^(-1)|v>|/sqrt(<u|C_S^(-1)|u><v|C_S^(-1)|v>)`.

Then the complete feasible frontier is

`boxed: y_max(x)=s_v[1-x/s_u]/[1-(1-c^2)x/s_u]`.

For

`r=alpha s_u/(beta s_v)`,

the exact WP12 linear allocation becomes

`boxed: h_(alpha,beta)=`

- `beta s_v`, if `r<=c^2`;
- `[alpha s_u+beta s_v-2c sqrt(alpha beta s_u s_v)]/(1-c^2)`, if `c^2<r<c^(-2)`;
- `alpha s_u`, if `r>=c^(-2)`.

Therefore rank-one WP12 instances require no SDP; only the outer scalar `eta` minimization remains.

The governing overlap is the principal angle in the **inverse shorted-curvature metric**, not the ordinary Hilbert-space angle. The same ordinary overlap `1/2` can correspond to `c=1/sqrt(13)` or `c=2/sqrt(7)` depending solely on the available curvature.

This proves that matrix resource information remains irreducible even in the smallest nontrivial overlapping allocation problem.

## Current frontier — WP15 and beyond

### A. Measurement compatibility — highest immediate priority

The WP12 shared-kernel qutrit benchmark has resource ceiling

`Phi=12`

but SLD-QFI trace

`Tr F_Q=10.75`.

Determine the exact common-record/Holevo optimum for that two-parameter local model.

The key question is whether the final gap is entirely standard measurement incompatibility:

`physical resource ceiling -> quantum statistical ceiling -> attainable common-record Fisher`.

If yes, the grand local theorem can be cleanly factorized into physical resource and measurement compatibility layers.

### B. Operator + spectral-action Pareto law

WP13 deliberately compresses the full curvature operator to one scalar `Tr(GC_Delta)` and therefore loses WP14's curvature-angle invariant `c`.

Derive the sharp Pareto bound when both are retained:

- fixed/shared operator curvature `C_Delta`;
- positive spectral action `Tr(GC_Delta)`;
- overlapping synthesized ranges.

Determine whether the resulting dual requires only one extra scalar multiplier added to the WP12 witness operator.

### C. Autonomous relational lift

Apply the WP12--WP14 operator/action hierarchy simultaneously from clock and signal Hamiltonian viewpoints for a globally stationary exact exchange tangent.

Target: determine whether sharp positive spectral-action resources must be paid on **both** sides of the relational cut, generalizing WP03/WP06 beyond finite-radius survival.

### D. Gaussian covariance-changing synthesis

Test squeezed-vacuum, parameter-dependent covariance, thermal Gaussian baselines, and correlated multimode synthesis.

Determine whether positive kernel curvature priced by spectral cost remains sufficient or whether Gaussian covariance geometry introduces a distinct resource.

### E. Deep priority audit

Explicitly compare against:

- Longyun Chen and Yuxiang Yang, *Optimal Quantum Metrology under Energy Constraints*, Phys. Rev. Lett. 136, 070801 (2026), DOI `10.1103/6ghs-frtx`;
- Holevo waveform-estimation limits;
- rank-one semidefinite packing/SOCP results such as Sagnol (2011);
- Anderson--Trapp shorted operators and parallel addition;
- singular/rank-changing QFI/Bures geometry;
- quantitative WAY/reference-frame resource theories.

Do not claim novelty for these ingredients.

## Publication / significance gate

Do not draft a new foundational manuscript yet.

A publication gate now requires at least:

1. exact resolution of the shared-kernel measurement-compatibility benchmark **or** a sharp autonomous two-sided action theorem;
2. hostile mathematical review of WP11--WP14;
3. deeper priority audit against 2025--2026 energy-constrained metrology;
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

Every future WP must add an independent validator before being marked PASS when the theorem has nontrivial algebraic or numerical content.

## Documentation discipline

Every material theorem, failed conjecture, prior-art collision, or validation result must be recorded immediately and reflected in `README.md`, `AGENTS.md`, and this file. The repository, not chat history, is authoritative.
