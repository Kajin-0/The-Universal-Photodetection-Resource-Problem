# Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

The frozen Rev11 paper remains untouched on `agent/temporal-information-resource-law`.

## Status

The foundational research phase through **WP20** is complete enough for manuscript formation.

- Literature/significance gate: **PROVISIONAL PASS for a narrowly scoped theorem paper**.
- Hostile mathematical gate: **PASS after two targeted corrections**.
- Priority: **unverified, not certified**.
- Minimal publication theorem stack: **provisionally frozen**.
- Do **not** create WP21 unless manuscript drafting exposes a concrete missing theorem or defect.

Read first:

1. `notes/PUBLICATION_THEOREM_STACK_AFTER_AUDITS.md`
2. `notes/HOSTILE_MATHEMATICAL_AUDIT_WP18_WP20.md`
3. `notes/FOUNDATIONAL_SIGNIFICANCE_PRIORITY_GATE_AFTER_WP20.md`
4. `AGENTS.md`
5. `ROADMAP.md`

## Central theorem story

A globally stationary relative temporal mode has two complementary physical-resource regimes.

### Finite affine tangent radius

For exact gap `nu`, finite `N`, arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N/N] <= T(nu)`.

For exact autonomous clock--signal exchange,

`(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`.

Thus robust temporal Fisher information requires **pre-existing spectral survival**, and in an autonomous exchange it must be backed on both sides of the relational cut.

### Rank-changing zero-radius boundary

When `R_lin=0` but a nonlinear physical family exists, the resource moves to second order.

One-sided boundary:

`Tr F_N/N <= J <= Delta T`.

Bilateral boundary:

`sqrt[Tr F_N/N] <= sqrt(J_+)+sqrt(J_-)`.

For globally stationary exchange the clean positive action laws are

`A_C^(2)+A_S^(2)>=(hbar nu/4)[Tr F_N/N]`

for bilateral synthesis and

`A_C^(2)+A_S^(2)>=(hbar nu/2)[Tr F_N/N]`

for one-sided synthesis.

Both coefficients are exactly sharp in fixed-total-energy shells where global time-translation asymmetry and signed total-energy curvature are zero.

## Arbitrary coherent support

For noncommuting support use the WP11 decomposition

`B=PAP`, `K_+=QAP`, `K_-=QA^dagger P`.

Shorted/principal-angle geometry is necessary; a naive scalar extension is operationally false.

For one exact exchange mode the audited canonical endpoint-role projectors are

`Pi_out=supp(A A^dagger)`,

`Pi_in=supp(A^dagger A)`,

and the canonical clock+signal kernel endpoint-incidence cost is

`G_ex=2hbar nu Q(Pi_out+Pi_in)Q`.

With two-sided pre-existing ceilings `a_+,a_-`, restricted costs `g_+,g_-`, and

`A_ex^(2)=(1/4)Tr(G_ex C_Delta)`,

WP19 gives

`Tr F_N/N`

`<=min{Psi_(a_+)(4A_ex;g_+,g_-),`

`      Psi_(a_-)(4A_ex;g_-,g_+)}`.

The shared-kernel fixed-shell qutrit has the exact hierarchy

`physical resource 12 > SLD trace 43/4 > accessible Fisher 55/8`.

## Multi-frequency boundary law

For zero-radius pure-boundary modes in one common multiparameter family,

`C_Sigma>=sum_k[Z_(k,+)+Z_(k,-)]`.

For any positive spectral cost `G`,

`sum_k gamma_k Tr F_(N,k)/N <=4A_(G,Sigma)^(2)`.

In the clean bilateral autonomous geometry,

`A_(G,Sigma)^(2)>=sum_k(hbar nu_k/4)Tr F_(N,k)/N`.

A fixed-total-energy star-shell family and one discrete Fourier measurement simultaneously saturate every Fisher block and the complete weighted sum. The strengthened validator confirms the full common-record Fisher matrix is block diagonal with entries `2c_k^2 I_2`.

## Audit corrections

Two issues were found and fixed on 2026-08-23:

1. WP18 one-sided exact family: `x+i y` was replaced by the convention-consistent `x-i y`. This is only `y -> -y`; no Fisher/action value changed.
2. WP19 action definition: a chosen four-local-projector representation was replaced by the canonical `Pi_in/Pi_out` endpoint-role operator above. All coefficients and the qutrit resource value `12` remain unchanged.

No error was found in WP18/WP19/WP20 coefficients, finite-copy scaling, fixed-shell physicality, global stationarity, the shared-Hessian inequality, or simultaneous Fourier saturation.

## Significance boundary

Broad novelty claims fail. The manuscript must **not** claim a new resource theory of time, Page--Wootters mechanism, theory of asymmetry, multiphase metrology framework, or general energy-constrained metrology theory.

Required prior-art comparisons include:

- Marvian--Spekkens, modes of asymmetry, PRA 90, 062110 (2014);
- Carmo--Soares-Pinto, Page--Wootters shared asymmetry, PRA 103, 052420 (2021);
- Tajima--Shiraishi--Saito, conservation-law coherence cost, PR Research 2, 043374 (2020);
- Marvian, QFI energetic-coherence cost, PRL 129, 190502 (2022);
- rank-changing QFI/Bures geometry;
- Gardner et al., waveform Holevo limit, PRL 132, 130801 (2024);
- Chen--Yang, protocol-level energy-constrained metrology, PRL 136, 070801 (2026);
- fixed-number relative-phase/multiphase and Fourier/covariant measurement theory.

The surviving candidate contribution is the **frequency-resolved rank-changing temporal-resource bridge** connecting two-sided pre-existing survival to two-sided second-order synthesis action.

## Manuscript scope

Main paper should center on:

1. WP02 baseline-energy no-go and finite-radius repair;
2. WP03/WP06 autonomous dual survival;
3. minimum WP07/WP09 boundary synthesis needed to close `R_lin=0`;
4. WP18 sharp autonomous dual synthesis action;
5. concise WP19 arbitrary-support bridge;
6. WP20 sharp multi-frequency sum.

Keep most of WP11--WP16 in the supplement. WP04/WP05 are strong but belong to a different structured finite-amplitude retention story and should not expand this manuscript.

## Next action

Begin manuscript formation using `notes/PUBLICATION_THEOREM_STACK_AFTER_AUDITS.md` as the scope lock. Do not add new theorem work unless drafting reveals a concrete logical gap.
