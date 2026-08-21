# Research Roadmap

**Updated:** 2026-08-21

Active branch: `agent/uprp-core-theorem-round10`.

## Program split

The project now has two separate tracks:

- **Paper 1 / Rev11:** scientifically frozen; technically validated for Physical Review Applied; only human metadata/compliance remain.
- **Paper 2:** active theoretical program on arbitrary autonomous detector channels and hidden-memory/high-flux information transfer.

Do not reopen Paper 1 merely because Paper 2 advances.

---

# Paper 1 — closed scientific gates

The first-paper autonomous marked-event theorem stack has passed theorem construction, hostile review, proof hardening, weak-waveform completion, empirical grounding, published-IRF demonstration, ENBW positioning correction, package generation, and validation.

Core closed results include:

- exact marked-event transfer `G(omega)=int |H_m(omega)|^2 kappa(dm)`;
- complete local weak-waveform Fisher operator;
- necessary-and-sufficient pointwise local Fisher ordering;
- exact band-subspace guarantee;
- collision/hazard resource hierarchy and inverse bandwidth costs;
- timing-width no-go results within stated scope;
- CTMC microscopic-rate repair and thermodynamic bridge;
- existing-data histogram estimator and finite-count bootstrap;
- Spinelli 1998 worked published-IRF ranking reversal;
- explicit recognition that single-mark `B_FI` is conventional one-sided ENBW.

Preferred submission candidate: **Rev11**.

Canonical Rev11 PDF SHA-256:

`9eedbf562ed5fa70b78a8c1c63627e1c578f149074f7f25f3fd3988c8668ecef`.

PRApplied Rev11 PDF SHA-256:

`d9e4a3330543106a272d4aa7b26cf6187bbd2f6ef170db4a8927b06edb824db7`.

Package ZIP SHA-256:

`b9f1abff76bbcc7a97ca8b2c3038f1e44e5adbb68f230cdb7d13c02431b6183e`.

Remaining Paper-1 work is factual/personal only: author/order, affiliation, corresponding email, ORCID, truthful AI disclosure, funding/conflict/prior-submission declarations, then final metadata-stage validation.

---

# Paper 2 — active gates

## P2-G0 — General arbitrary-channel retention operator

**PASSED at proof-architecture level.**

For a parameter-independent detector channel, output score is conditional expectation of the Poisson source score, yielding a positive contraction on the temporal source tangent space.

## P2-G1 — Autonomy forces spectral diagonalization

**PASSED at proof-architecture level; novelty audit remains.**

WP10/WP17 show that time-translation covariance makes the retention operator commute with temporal shifts, hence

`F_out[u,v]=Phi0/(2*pi) int G_{Phi0,K}(omega) U*(omega)V(omega)domega`,

`0<=G<=1` a.e.

WP17 closes the main formal gaps using standard-Borel trajectory spaces, stochastic-kernel randomization, DQM under statistics, the classical translation-invariant `L2` multiplier theorem, and narrowband wavepacket interpretation.

**Open gate:** determine whether the photodetection-specific synthesis is genuinely distinct from stationary-channel/statistical-experiment prior art.

## P2-G2 — Discrete Type-II information high-pass

**PASSED.**

At the symmetric point of the one-bin paralyzable model,

`G(omega)=1-1/(2x)+ln(1+4x)/(8x^2)`, `x=1-cos(omega)`.

It rises strictly from `G(0)=0` to

`G(pi)=3/4+ln(3)/16=0.818663268...`.

Retain as exact prototype, not primary physical evidence.

## P2-G3 — Continuous deterministic Type-II spectral escape

**PASSED analytically; novelty still under audit.**

For deterministic paralyzable dead time at `lambda*tau=1`:

`G_1(0)=0`,

`G_1(omega)>0` for every nonzero frequency,

`G_1(infty)=1/e`.

At `omega=pi/tau`, rigorous lower bound `0.516975...`; independent complete-record Volterra calculation approximately `0.52814`.

This is the strongest current concrete physical spectral theorem.

## P2-G4 — General iid-recovery static Fisher singularity

**PASSED under explicit renewal-DQM/window regularity; historical novelty unresolved.**

Every recovery law of fixed mean `m` shares

`r(lambda)=lambda exp(-lambda m)`.

At `lambda*m=1`, WP18's bounded-Laplace-statistic proof gives

`G_DC=0 iff T=m almost surely`.

This replaces the older pointwise-density necessity argument.

Quantitative witness:

`G_DC >= (4/e)W_s^2/(1+u_s)^4`.

**Open gate:** historical inverse-output literature, especially Afanaseva–Mikhailova (1973), must be exhausted before priority language.

## P2-G5 — Global equal-rate branch aliasing uniqueness

**PASSED as an identifiability corollary; do not oversell.**

For fixed known recovery law, distinct incident rates with the same conventional output rate produce identical complete registered-timestamp experiments iff recovery is deterministic.

Because the underlying renewal and pair-correlation formulas are classical, position this as a corollary of the Fisher/identifiability structure rather than new queueing theory.

## P2-G6 — Recovery mean/variance sufficiency

**FAILED by exact counterexample; no-go closed.**

WP19 constructs two recovery laws with identical

`E[T]=1`, `Var(T)=1/4`, `CV=0.5`,

and identical entire conventional saturation curve, but different timestamp experiments and different FI for a common coarse-graining.

Analytic witness for one law: normalized per-time FI `~0.00443520488427` versus zero for the other.

Converged full static FI differs by about `8.78%`.

Conclusion: mean and variance/CV are not resource-complete. **Do not continue searching for a universal variance-only law by default.**

## P2-G7 — Visible-event high-frequency residue

**WP08 pointwise theorem demoted; WP20 Cesaro theorem PASSED under weaker covariance-measure assumptions.**

For exact-timestamp selector `Y<=N`, if conditional-score covariance measure is

`Gamma_M=r delta_0+nu`,

with finite-total-variation `nu` and no zero atom, then

`lim_{Omega->infty} 1/[(b-a)Omega] int_{aOmega}^{bOmega}G(omega)domega=r/lambda`

for every fixed `0<a<b`.

If `nu` is atomless, high-frequency mean-square/Cesaro convergence follows from Wiener. If `nu` is Rajchman, e.g. has `L1` density, the stronger pointwise limit follows.

**Open gate:** targeted novelty audit of the detector-specific zero-lag Fisher-covariance formulation.

---

# Prior-art corrections that constrain all Paper-2 claims

The following are established and must not be claimed as new:

- random Type-II/paralyzable dead time;
- `M/G/infinity` representation and busy-cycle theory;
- the generalized renewal density `U_lambda(t)=lambda F(t)exp[-lambda A(t)]`;
- random-paralyzable pair-correlation formulas;
- `g_Y^(2)(t)=F(t)exp[lambda E[(T-t)_+]]`;
- pair-correlation dead-time inversion in general;
- infinite-server service/recovery inference generally;
- renewal-process FI / generic timing-versus-rate FI;
- conditional-score projection, Fisher data processing, function-valued FI operators;
- translation-invariant Fourier multipliers;
- stationary random-measure spectral theory and Wiener's theorem;
- dead-time information theory generally;
- modulated paralyzable photocounting generally.

WP15 is supporting/operational only after the Apanasovich–Paltsev 1995 prior-art correction.

---

# Current manuscript decision gate

Do **not** draft Paper 2 yet.

Draft only after all three conditions are met:

1. the historical inverse-output audit does not directly preempt WP18's fixed-recovery-law Fisher singularity;
2. WP20's detector-specific covariance-atom/Cesaro formulation survives targeted novelty review;
3. WP18's DQM/window assumptions are stated at manuscript-grade scope, including treatment/exclusion of atomic and heavy-tailed recovery laws.

If those gates survive, the intended core manuscript stack is:

- WP10/WP17 general autonomous-channel theorem;
- WP07 continuous Type-II spectral escape;
- WP18 deterministic-recovery Fisher singularity;
- WP20 visible-event Cesaro residue;
- WP19 recovery-moment insufficiency no-go.

---

# Immediate work order

1. Historical inverse-output audit: Afanaseva–Mikhailova and old Type-II/infinite-server identifiability literature.
2. WP20-specific novelty audit: dependent thinning, missing-event point processes, stationary score spectra, information-spectrum literature.
3. WP18 regularity audit: renewal DQM, censoring, atomic/heavy-tailed recovery.
4. Manuscript decision only after 1–3.

---

# Documentation discipline

Every material theorem, proof repair, prior-art collision, numerical result used in an argument, or change in the next-gate decision must be committed as it occurs.

Keep synchronized:

- the relevant `paper2/notes/WP*.md` or dated research log;
- `paper2/AGENTS_PAPER2.md` whenever recovery order/claim hierarchy/gates change;
- `docs/CURRENT_RESEARCH_STATE.md` and this roadmap whenever project-level status changes.

The repository must remain sufficient for a new agent to recover the full active state without chat history.
