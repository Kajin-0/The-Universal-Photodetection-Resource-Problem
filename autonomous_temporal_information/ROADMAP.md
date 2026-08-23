# Roadmap — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

## Goal

Develop and publish a rigorously scoped physical resource law for autonomous temporal information. The finished Rev11 random-time paper remains frozen on its parent branch.

## Research status

The theorem program through WP20 has passed the current internal gates.

- Significance/literature gate: **PROVISIONAL PASS for a narrow theorem paper**.
- Hostile mathematical gate: **PASS after minor corrections**.
- Priority: **unverified, not certified**.
- Main publication theorem stack: **provisionally frozen**.

Authoritative gate notes:

- `notes/FOUNDATIONAL_SIGNIFICANCE_PRIORITY_GATE_AFTER_WP20.md`
- `notes/HOSTILE_MATHEMATICAL_AUDIT_WP18_WP20.md`
- `notes/PUBLICATION_THEOREM_STACK_AFTER_AUDITS.md`

## Frozen main theorem arc

### Result 1 — WP02

Mean baseline energy alone does not bound unrestricted synthesized local temporal Fisher information.

Physical repair:

`(R_lin^2/4)[Tr F_N/N] <= T(nu)`.

### Result 2 — WP03 / WP06

For globally stationary exact exchange,

`(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`.

This survives arbitrary coherent/history-state support.

### Result 3 — WP07 / WP09

At `R_lin=0`, nonlinear physical state families can remain informative. Second-order endpoint synthesis becomes the resource.

One-sided:

`Tr F_N/N<=J<=Delta T`.

Bilateral:

`sqrt[Tr F_N/N]<=sqrt(J_+)+sqrt(J_-)`.

### Result 4 — WP18

Globally stationary boundary exchange requires positive action on both sides:

bilateral

`A_C^(2)+A_S^(2)>=(hbar nu/4)[Tr F_N/N]`,

one-sided

`A_C^(2)+A_S^(2)>=(hbar nu/2)[Tr F_N/N]`.

Both coefficients are exactly sharp in fixed-total-energy shells.

### Result 5 — WP19

For arbitrary coherent support, use canonical endpoint roles

`Pi_out=supp(A A^dagger)`,

`Pi_in=supp(A^dagger A)`

and

`G_ex=2hbar nu Q(Pi_out+Pi_in)Q`.

The mixed finite-radius/synthesis bridge is

`Tr F_N/N`

`<=min{Psi_(a_+)(4A_ex;g_+,g_-),`

`      Psi_(a_-)(4A_ex;g_-,g_+)}`.

### Result 6 — WP20

For a common zero-radius multiparameter exchange family,

`C_Sigma>=sum_k[Z_(k,+)+Z_(k,-)]`

and

`sum_k gamma_k Tr F_(N,k)/N<=4A_(G,Sigma)^(2)`.

Clean bilateral frequency weighting gives

`A_(G,Sigma)^(2)>=sum_k(hbar nu_k/4)Tr F_(N,k)/N`.

The full sum is simultaneously sharp with one common Fourier measurement.

## Audit results incorporated

### WP18 correction

The one-sided exact family now uses `c(x-i y)`, consistent with the branch sine-quadrature convention. This is only a coordinate reversal from the earlier text and changes no theorem values.

### WP19 correction

The endpoint-incidence action is now canonical for one exact exchange mode through the joint domain/range supports of `A`. This removes arbitrary local endpoint-projector broadening while preserving all reported constants.

### WP20 strengthening

The validator now reconstructs `C_Sigma` from finite differences of the actual common nonlinear family and verifies the entire Fourier Fisher matrix, including vanishing cross-mode/cos-sin blocks.

## Publication significance boundary

### Claims that are not allowed

Do not claim:

- a new resource theory of time;
- a new Page--Wootters mechanism;
- new modes-of-asymmetry theory;
- new general QFI/coherence resource theory;
- new Fourier/multiphase measurement theory;
- a general solution to energy-constrained metrology;
- novelty of PSD-cone, shorted-operator, numerical-radius, SDP, or Holevo mathematics.

### Candidate paper claim

The publication should instead defend the **finite-radius / rank-changing resource bridge**:

> pre-existing two-sided spectral survival supports finite-radius relative temporal information, while two-sided positive second-order spectral synthesis action supports rank-changing boundary information; both have sharp autonomous fixed-shell consequences and the boundary action has a sharp spectral sum.

## Manuscript phase — current priority

**Do not create WP21 unless manuscript drafting identifies a concrete missing theorem.**

### Phase M1 — skeleton and theorem statements

1. Create manuscript directory/files on this branch.
2. Fix notation and assumptions globally.
3. Write formal statements of Results 1--6 before prose expansion.
4. Add a compact prior-art comparison section/table.

### Phase M2 — proofs and supplement split

Main text should contain conceptual proof cores only.

Move to supplement:

- WP10;
- detailed WP11 shorting counterexample;
- WP12 SDP allocation;
- WP13 action-envelope derivation;
- WP14 curvature-metric angle law;
- WP15 exact `55/8` witness;
- WP16 generic accessibility theorem;
- extended algebra and validator details.

WP04/WP05 should stay outside this manuscript unless a concrete narrative reason emerges.

### Phase M3 — extremizers and figures

At minimum consider:

1. a two-regime schematic: finite-radius pre-existing survival vs zero-radius synthesis action;
2. fixed-total-energy WP18 qutrit exchange diagram;
3. optional spectral WP20 star-shell diagram.

Figures must clarify the physics, not decorate the paper.

### Phase M4 — hostile manuscript review

Before formatting for submission:

- verify all theorem assumptions against proofs;
- verify every novelty sentence against the priority audit;
- remove any claim that confuses kinematic synthesis action with total implementation energy;
- verify the supplement contains enough detail to reproduce the finite-copy and operator-geometry arguments;
- run the complete numerical validator suite.

## Required prior art

At minimum engage explicitly with:

- Marvian--Spekkens, PRA 90, 062110 (2014);
- Carmo--Soares-Pinto, PRA 103, 052420 (2021);
- Tajima--Shiraishi--Saito, PR Research 2, 043374 (2020);
- Marvian, PRL 129, 190502 (2022);
- Safranek, PRA 95, 052320 (2017);
- Gardner et al., PRL 132, 130801 (2024);
- Chen--Yang, PRL 136, 070801 (2026);
- relevant quantitative WAY/reference-frame and fixed-number relative-phase literature.

## Deferred work

Defer unless required by manuscript review:

- mixed finite-radius + multi-gap theorem;
- continuum spectral-action limit;
- Gaussian covariance-changing synthesis;
- further common-record measurement geometry.

## Documentation discipline

Manuscript formation is now part of the research record. Any change in theorem scope, assumptions, or novelty boundary must be synchronized across `README.md`, `AGENTS.md`, this roadmap, and manuscript handoff files.
