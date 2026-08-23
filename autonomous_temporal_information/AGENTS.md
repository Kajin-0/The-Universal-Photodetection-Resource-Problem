# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

The frozen Rev11 paper remains on `agent/temporal-information-resource-law` and must not be rewritten absent a concrete defect.

## Current phase

**Research theorem production is paused. Manuscript formation is now the highest-priority task.**

The branch passed:

- a hostile literature/significance gate: **PROVISIONAL PASS for a narrow theorem paper**;
- a hostile mathematical audit of WP18--WP20: **PASS after two targeted corrections**.

Priority remains **unverified, not certified**.

Do not create WP21 unless manuscript drafting exposes a concrete missing theorem, counterexample, or defect.

## Read first

1. `notes/PUBLICATION_THEOREM_STACK_AFTER_AUDITS.md`
2. `notes/HOSTILE_MATHEMATICAL_AUDIT_WP18_WP20.md`
3. `notes/FOUNDATIONAL_SIGNIFICANCE_PRIORITY_GATE_AFTER_WP20.md`
4. `README.md`
5. `ROADMAP.md`

## Scope lock for the main paper

The paper should claim only:

> Globally stationary relative temporal information has two complementary spectral-resource regimes. Finite-radius information requires two-sided pre-existing spectral survival; rank-changing zero-radius information requires two-sided positive second-order spectral synthesis action. The clean laws are finite-copy/arbitrary-POVM and sharp in fixed-total-energy shells, arbitrary coherent support requires operator geometry, and the boundary resource admits a sharp multi-frequency sum.

Do **not** claim a new resource theory of time or new general asymmetry/metrology framework.

## Main theorem stack

### 1. WP02 — baseline-energy no-go and robust tangent radius

Fixed baseline mean energy does not bound unrestricted high-frequency local Fisher information under arbitrary state synthesis.

Corrected finite-copy law:

`(R_lin^2/4)[Tr F_N/N] <= T(nu)`.

### 2. WP03 / WP06 — autonomous dual survival

For exact exchange

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`,

`(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`.

WP06 allows arbitrary coherent/history-state support.

### 3. WP07 / WP09 — rank-changing boundary completion

At `R_lin=0`, exact nonlinear physical families can still carry local Fisher information.

One-sided:

`Tr F_N/N <= J <= Delta T`.

Bilateral:

`sqrt[Tr F_N/N] <= sqrt(J_+)+sqrt(J_-)`.

The qutrit extremizer proves additive bilateral endpoint cost false by factor two.

### 4. WP18 — autonomous dual synthesis action

Bilateral clean exchange:

`A_C^(2)+A_S^(2)>=(hbar nu/4)[Tr F_N/N]`.

One-sided clean exchange:

`A_C^(2)+A_S^(2)>=(hbar nu/2)[Tr F_N/N]`.

Both are exactly sharp in fixed-total-energy shells with zero global time-translation asymmetry.

The audited one-sided exact ket uses `c(x-i y)`, consistent with `D_s=(A-A^dagger)/(2i)`.

### 5. WP19 — arbitrary coherent-support bridge

Use canonical joint endpoint-role projectors

`Pi_out=supp(A A^dagger)`,

`Pi_in=supp(A^dagger A)`.

Define

`G_ex=2hbar nu Q(Pi_out+Pi_in)Q`,

`A_ex^(2)=(1/4)Tr(G_ex C_Delta)`.

With two-sided shorted pre-existing ceilings `a_+,a_-` and restricted costs `g_+,g_-`,

`Tr F_N/N`

`<=min{Psi_(a_+)(4A_ex;g_+,g_-),`

`      Psi_(a_-)(4A_ex;g_-,g_+)}`.

The shared-kernel fixed-shell qutrit retains the exact resource value `12`.

### 6. WP20 — multi-gap autonomous action sum

For one common boundary family,

`C_Sigma>=sum_k[Z_(k,+)+Z_(k,-)]`.

For any positive spectral cost `G`,

`sum_k gamma_k Tr F_(N,k)/N <=4A_(G,Sigma)^(2)`.

Clean bilateral exchange gives

`A_(G,Sigma)^(2)>=sum_k(hbar nu_k/4)Tr F_(N,k)/N`.

One fixed Fourier measurement simultaneously saturates every block and the complete sum in the star-shell extremizer.

## Supplement / supporting material

Keep the following mostly out of the main narrative:

- WP10 clean mixed special case;
- WP11 shorting constants and counterexample details;
- WP12 allocation SDP;
- WP13 action envelope derivation;
- WP14 inverse-curvature angle law;
- WP15 exact `55/8` witness;
- WP16 generic accessibility theorem;
- validators and full algebra.

WP04/WP05 structured finite-amplitude retention should not be pulled into this manuscript unless a specific narrative need appears.

## Mandatory prior-art positioning

Explicitly distinguish from:

- Marvian--Spekkens modes of asymmetry;
- Carmo--Soares-Pinto Page--Wootters shared asymmetry;
- Tajima--Shiraishi--Saito coherence cost under conservation laws;
- Marvian QFI energetic-coherence formation cost;
- quantitative WAY/reference-frame theory;
- Safranek rank-changing QFI/Bures geometry;
- Gardner et al. waveform Holevo bound;
- Chen--Yang total-protocol energy-constrained metrology;
- fixed-number relative-phase/multiphase metrology and Fourier/covariant measurements.

The synthesis action is a **kinematic state-family resource**, not a demonstrated total implementation-energy cost.

## Audit corrections already applied

1. WP18 one-sided family sine-coordinate sign corrected; coefficients unchanged.
2. WP19 endpoint action canonicalized with `Pi_in/Pi_out`; coefficients and qutrit benchmark unchanged.
3. WP20 validator strengthened to reconstruct the common kernel Hessian from the actual nonlinear family and verify the full common-record Fisher matrix.

## Manuscript work order

1. Create a manuscript skeleton from the frozen theorem stack.
2. Write abstract/introduction only after theorem statements and notation are fixed.
3. State all main theorems with assumptions precise enough for hostile review.
4. Move technical matrix geometry to supplement aggressively.
5. Build a prior-art comparison table internally before finalizing novelty language.
6. Add figures only when they clarify the two-regime physical picture or extremizers.
7. Run another hostile review on the assembled manuscript before publication formatting.

## Documentation rule

Every manuscript-level change in theorem scope, claim strength, or prior-art boundary must be reflected in this file, `README.md`, `ROADMAP.md`, and the manuscript handoff. The repository is authoritative.
