# WP24 — Independent mixed-envelope derivation and classical nonregular-statistics audit

## Status

**Mixed-resource scalar optimization independently re-derived: PASS.**

**Classical nonregular-statistics scope correction identified:** the existence of statistical irregularity at a boundary is not quantum novelty and should be credited explicitly in any future manuscript revision. The quantum-specific content is the PSD-cone/operator/spectral implementation structure, not the generic fact that support-changing models are nonregular.

The current manuscript remains frozen while WP21–WP23 dynamical work is audited.

## 1. Independent derivation of the mixed scalar envelope

The first WP19 measurement branch has the form

`F <= (sqrt(a+J_+) + sqrt(J_-))^2`

with the action budget

`p J_+ + q J_- <= e`,

where `a,e>=0`, `p,q>0`, and `J_+,J_->=0`.

Because the objective is monotone in both variables, the budget is saturated at the maximum.

Set

`u=a+J_+`, `v=J_-`.

Then

`p u + q v = e + p a := E`,

with `u>=a`, `v>=0`.

Write

`s=sqrt(u)`, `t=sqrt(v)`.

The problem is

`maximize (s+t)^2`

subject to

`p s^2 + q t^2 = E`, `s>=sqrt(a)`, `t>=0`.

### Interior ellipse optimum

Maximizing `s+t` with a Lagrange multiplier gives

`1=2 lambda p s`,

`1=2 lambda q t`,

hence

`p s=q t`.

Therefore

`s=c/p`, `t=c/q`,

with

`c^2=E p q/(p+q)`.

Thus

`u_*=E q/[p(p+q)]`,

`v_*=E p/[q(p+q)]`.

The interior point is feasible iff `u_*>=a`, i.e.

`E q >= a p(p+q)`.

Since `E=e+pa`, this is equivalent to

`boxed: e >= a p^2/q.`

At the interior optimum,

`(s+t)^2
 = E(1/p+1/q)
 = (e+pa)(1/p+1/q).`

### Boundary optimum

If

`e < a p^2/q`,

the unconstrained ellipse optimum would have `u<a`, so the constrained optimum sits at the boundary `u=a`, i.e. `J_+=0`.

Then

`v=e/q`,

and

`(sqrt(u)+sqrt(v))^2
 = (sqrt(a)+sqrt(e/q))^2.`

Therefore

`boxed:
Psi_a(e;p,q)=
  (sqrt(a)+sqrt(e/q))^2,                    e<=a p^2/q,
  (e+pa)(1/p+1/q),                          e>=a p^2/q.`

The two formulas agree continuously at the threshold.

This exactly matches WP13/WP19 and the manuscript.

## 2. Edge cases

The displayed bilateral envelope assumes `p,q>0` and both synthesis variables are genuine degrees of freedom.

- If one orientation is absent, set the corresponding `J` identically to zero and optimize the surviving one-sided branch directly.
- If a nonzero orientation has zero scalar price, no finite scalar action-only ceiling follows for that orientation; retain the operator curvature or choose a different positive cost.
- If an internal shorting ceiling is unavailable, omit that measurement branch rather than introducing an extended-real square root.

These are the same conventions already enforced in manuscript R2/R3.

## 3. Numerical hostile check

A brute-force optimizer over `J_+ in [0,e/p]` was compared with the analytic formula for 100 random positive quadruples `(a,e,p,q)` spanning several orders of magnitude.

Maximum relative discrepancy was below `2e-11`, consistent with grid discretization.

No scalar-optimization defect was found.

A permanent validator should be added as

`numerics/verify_wp24_psi_envelope.py`.

## 4. Shared-kernel qutrit check

For the manuscript benchmark,

`a=5/4`,

`e=247/16`,

`p=q=13/4`.

The threshold is

`a p^2/q = a p = 65/16`,

so the interior branch applies.

Then

`Psi=(e+pa)(1/p+1/q)`

`=(312/16)(8/13)`

`=12`.

Thus the physical mixed-resource ceiling `12` is reproduced exactly.

The separate one-copy accessibility optimum `55/8` is not expected to equal this resource ceiling; WP15/WP16 explicitly distinguish resource sufficiency from common-record attainability.

## 5. Response to the external critique: what is correct and what is stale

### Correct criticism: mathematical infrastructure is standard

Agreed. Numerical-radius inequalities, PSD-cone second-order geometry, shorted operators, Cauchy–Schwarz, and the scalar ellipse optimization are mathematical infrastructure.

The paper must continue to claim novelty only for the frequency-resolved autonomous spectral-resource application and its sharp constructions, not for the underlying inequalities.

### Partly stale criticism: only a bespoke classical Fisher block is controlled

R3 materially changes this point.

The clean pure-boundary action now also obeys the sharp quantum-statistical corollary

`A_C^(2)+A_S^(2) >= (hbar nu/4) Tr H_SLD`.

WP22–WP23 go further: the same quantity has an exact minimum dynamical implementation interpretation.

The common-record tangent Fisher remains a distinct measurement-accessibility layer, which is intentional.

### Correct criticism: exact-gap and finite-dimensional idealization

Still valid.

The project has not yet proved robustness to detuning/off-resonant terms, open-system noise, or infinite-dimensional unbounded generators.

These are genuine next-theorem candidates.

### Correct criticism: classical nonregular-statistics literature is under-engaged

Agreed.

The generic fact that likelihood/Fisher asymptotics become nonstandard at a parameter/support boundary predates the quantum setting by decades.

Mandatory classical references for a future manuscript update include at least:

- H. Chernoff, *On the Distribution of the Likelihood Ratio*, Ann. Math. Statist. 25, 573–578 (1954), DOI `10.1214/aoms/1177728725`.
- S. G. Self and K.-Y. Liang, *Asymptotic Properties of Maximum Likelihood Estimators and Likelihood Ratio Tests under Nonstandard Conditions*, JASA 82, 605–610 (1987), DOI `10.1080/01621459.1987.10478472`.
- A. Shapiro, *Asymptotic distribution of test statistics in the analysis of moment structures under inequality constraints*, Biometrika 72, 133–144 (1985), DOI `10.1093/biomet/72.1.133`.

These works establish boundary/nonstandard asymptotics and chi-bar-square/cone phenomena. They do **not** by themselves provide the quantum operator PSD-cone endpoint law, exact Bohr-frequency pricing, autonomous clock–signal duality, or energy-conserving implementation-cost theorem.

The manuscript should therefore say explicitly that **nonregularity itself is generic statistics; the quantum contribution is the operator-valued positivity geometry and spectral/autonomous resource consequence.**

### Correct criticism: formal completeness can outrun physical motivation

Agreed as a presentation issue.

The full branch bookkeeping and degenerate cases belong in Supplemental Material. The main text should retain only the clean physical theorem and one sentence directing edge cases to the supplement.

### AI-use concern

This is a process-risk observation, not a mathematical counterexample. It justifies continued independent symbolic derivations, random validators, exact finite-dimensional benchmarks, source audits, and hostile proof checks. It does not alter theorem truth by itself.

## 6. Classical-versus-quantum boundary distinction

A classical probability vector at a simplex boundary already exhibits the key regularity failure: an outcome with baseline probability zero can acquire probability only at second order along a two-sided smooth physical path, and ordinary baseline score Fisher omits that newly appearing mass.

The quantum state cone adds noncommutative structure absent from the scalar simplex:

1. support-to-kernel **coherence amplitudes** are constrained by operator Schur complements;
2. opposite complex orientations can share a kernel sector and interfere in common-record Fisher amplitudes;
3. shorted-operator/principal-angle geometry becomes necessary when the support is not aligned with energy endpoints;
4. exact Bohr-gap structure assigns physical spectral prices to the newly synthesized kernel population;
5. global stationarity can coexist with nontrivial local clock–signal exchange;
6. WP21–WP23 identify the resulting curvature with a minimum energy-conserving unitary coupling cost.

Thus “second-order population at a boundary” is not itself the novelty. The operator/spectral/dynamical theorem built on top of it is the candidate contribution.

## 7. Publication consequence

Before the next submission-facing revision, add a concise classical-statistics acknowledgement near the first discussion of rank-changing/nonregular boundary information.

Do not expand the paper into a review of chi-bar-square asymptotics; one compact paragraph/citation cluster is sufficient.

Do not modify the manuscript until the WP21–WP23 dynamical theorem chain has completed its prior-art and hostile audit, because that chain may warrant a larger R4 physical-significance revision.

## 8. Next work

1. Add and run the permanent `Psi_a` validator.
2. Hostile-audit WP23, especially the ancilla energy-shell construction.
3. Search second-order constrained Stinespring/purification prior art.
4. Decide whether approximate-gap/noise robustness or infinite-dimensional extension gives the larger physical-significance gain.
