# AGENTS.md

## Purpose

This is the durable handoff record for **The Universal Photodetection Resource Problem (UPRP)**. The repository is authoritative project memory. Do not rely on chat context surviving.

Before new research, read:

1. `README.md`
2. `PROBLEM.md`
3. `ROADMAP.md`
4. `docs/FORMALISM.md`
5. `docs/LITERATURE_MAP.md`
6. `docs/NOVELTY_AND_FALSIFICATION.md`
7. `notes/RESEARCH_LOG.md`
8. `notes/RESEARCH_LOG_ROUND2.md`
9. `notes/WP0_WP1_ROUND1.md`
10. `notes/WP0_BANDWIDTH_CORRECTION.md`
11. `notes/WP2_REVERSIBLE_TWO_CHANNEL.md`
12. `notes/WP2_THREE_STATE_RARE_FAST_COUNTEREXAMPLE.md`
13. `notes/WP3_GATEWAY_RESOURCE_THEOREM.md`
14. `notes/WP3_MULTIGATEWAY_EXTENSION.md`
15. `notes/WP4_MICROSCOPIC_OPTICAL_COUPLING_NO_GO.md`

## Project objective

Determine what resources are necessary and/or sufficient for a finite-temperature photodetector to transfer information from an incident optical field into an electrical record with specified sensitivity and temporal bandwidth.

Valid endpoints include:

- a rigorous universal/restricted resource bound;
- a rigorous no-go theorem;
- an explicit counterexample family;
- identification of a missing resource followed by a repaired theorem.

Do **not** assume a simple sensitivity-bandwidth-temperature inequality exists.

## Research mode

Analytical/theoretical only. Numerical work may test conjectures or verify algebra. Do not make experiments, fabrication, procurement, or laboratory optimization necessary next steps.

---

# Primary information metric

For an optical parameter `theta`, use the information-transfer efficiency

\[
\boxed{\eta_{\mathcal I}=\dot F_{\rm out}/\dot F_{\rm in}^{Q}}
\]

where the numerator is classical Fisher-information rate in the complete electrical record and the denominator is quantum Fisher-information rate in the incident optical field for the same parameter.

For coherent/Poisson weak photon-flux modulation,

\[
\boxed{
\eta_{\mathcal I}(\omega)
=\Phi_0\frac{|\chi_{Y\Phi}(\omega)|^2}{S_Y(\omega)}.
}
\]

This is the temporal analogue of DQE. The normalization is useful but not novel.

Do **not** use an unqualified all-frequency integral as the primary theorem objective. An ideal white Poisson counter has `eta_I(omega)=1` for all modulation frequencies. Use a finite optical task/mode family:

\[
\boxed{
\bar\eta_{\mathcal I}
=\frac{\int \frac{d\omega}{2\pi}\mathcal J_{\rm in}(\omega)\eta_{\mathcal I}(\omega)}
{\int \frac{d\omega}{2\pi}\mathcal J_{\rm in}(\omega)}.
}
\]

For a flat task band `|omega| <= Omega_s`, average over that band.

---

# Exact Markov machinery — solved

Column-vector convention:

\[
\dot p=Wp,\qquad \mathbf1^TW=0,\qquad W\pi=0,
\]

\[
\Pi=\pi\mathbf1^T,\qquad Q=I-\Pi,
\]

\[
R(\omega)=Q(i\omega I-W)^{-1}Q.
\]

For counted jump-current operators,

\[
\boxed{
S_I(\omega)=\mathbf1^T\mathcal J^{(2)}\pi
+2\operatorname{Re}[\mathbf1^T\mathcal J^{(1)}R(\omega)\mathcal J^{(1)}\pi]
}
\]

and for scalar input `u`,

\[
\boxed{
\chi_{Iu}(\omega)
=\mathbf1^T\mathcal J_u^{(1)}\pi
+\mathbf1^T\mathcal J_0^{(1)}R(\omega)W_u\pi.
}
\]

These are **PROVED for finite-state stationary Markov jump detectors** and checked against a solvable two-state model.

---

# Important prior results

## A. Activity-only failure

A two-state excitation/reset model can have bounded stationary activity while latent reset bandwidth diverges. Therefore stationary activity alone cannot bound speed in an unconstrained kinetic model.

## B. Reversible two-channel lemma

With fixed optical rates and a readout rate `r -> infinity`, bounded activity and bounded EPR cannot both be maintained in the minimal two-state/two-channel reversible detector.

## C. First rare-fast reversible counterexample

A three-state reversible cycle with a rare `O(1/R)` intermediate can keep stationary activity and net EPR finite while an internal bandwidth grows as `R`. Its first version changed the signal-facing optical reverse rate without preserving a fixed optical detailed-balance ratio, so it was not the final microscopic counterexample.

---

# WP3 positive restricted theorem

For a reversible optical gateway

\[
0\xrightleftharpoons[d]{u}1
\]

with forward stationary optical throughput `f >= f_* > 0`, total dimensionless EPR `sigma <= Sigma`, and total stationary activity `A_tot <= A`, define

\[
g(z)=\left(1-\frac1z\right)\ln z,
\qquad
Z_*=g^{-1}(\Sigma/f_*).
\]

Then

\[
\boxed{\pi_1\ge \frac{f_*}{dZ_*}}
\]

and the gateway escape rate obeys

\[
\boxed{
\lambda_1\le
\Lambda_*
=\frac{\mathcal A d}{f_*}Z_*.
}
\]

For a proper single-event detector whose electrical record cannot occur before first exit from state 1,

\[
\boxed{
\eta_{\mathcal I}(\omega)
\le
\eta_q\frac{\Lambda_*^2}{\Lambda_*^2+\omega^2}.
}
\]

This is **PROVED for the stated restricted event-transducer class**.

Critical point: `d` is itself a microscopic optical rate. The theorem is finite only if an independent physical resource bounds `d`.

---

# WP4 strongest no-go theorem — current central result

Microscopic weak-coupling bosonic optical rates have the form

\[
\Gamma_\uparrow=\gamma(\omega_0)n(\omega_0),
\qquad
\Gamma_\downarrow=\gamma(\omega_0)[n(\omega_0)+1].
\]

For a thermal optical reservoir,

\[
\Gamma_\uparrow/\Gamma_\downarrow=e^{-\beta\hbar\omega_0}.
\]

Thus temperature and photon energy fix the **ratio** of optical rates but not the absolute coupling scale `gamma(omega_0)`.

The following reversible family preserves the optical rate ratio while increasing only the absolute scale:

\[
0\xrightleftharpoons[bR]{aR}1,
\qquad
1\xrightleftharpoons[q]{cR}2,
\qquad
2\xrightleftharpoons[sR]{p}0,
\]

with fixed positive `a,b,c,p,q,s` and fixed `a/b`.

Define

\[
\Delta=ac+s(b+c),
\]

\[
x=\frac{p(b+c)+bq}{\Delta},
\qquad
y=\frac{(a+s)q+ap}{\Delta}.
\]

The exact stationary distribution is

\[
\boxed{
\pi_0=\frac{x}{R+x+y},\quad
\pi_1=\frac{y}{R+x+y},\quad
\pi_2=\frac{R}{R+x+y}.
}
\]

As `R -> infinity`:

- forward optical throughput `aR pi_0 -> ax > 0`;
- total stationary activity stays finite;
- every edge’s stationary traffic stays finite;
- total EPR stays finite;
- every individual edge EPR stays finite;
- optical detailed-balance ratio `a/b` remains fixed;
- successful first-exit electrical branch probability `c/(b+c)` remains fixed and nonzero;
- post-absorption escape rate `(b+c)R -> infinity`;
- timing jitter scales as `1/R` and timing bandwidth scales as `R`.

Therefore:

\[
\boxed{
\{T,\hbar\omega_0,\text{optical detailed balance},f_*,\mathcal A,\sigma,\text{edge EPRs},\eta_q\}
\not\Rightarrow
\text{finite detector speed bound}.
}
\]

An **absolute microscopic coupling/transition resource is necessary**.

This is **PROVED for the finite-state reversible Markov event-detector class**.

---

# Microscopic repair

If a separate constraint supplies

\[
\gamma(\omega_0)\le\gamma_{\max},
\]

then

\[
d\le\gamma_{\max}[n(\omega_0)+1]
\]

and the WP3 theorem becomes

\[
\boxed{
\Lambda_{\rm micro}
=\frac{\mathcal A\gamma_{\max}[n+1]}{f_*}
\,g^{-1}(\Sigma/f_*).
}
\]

The same Lorentzian information and timing bounds follow with `Lambda_micro`.

Thus the current positive theorem is a **conditional completion theorem**: it needs an optical coupling cap.

---

# Matter-side coupling bound: TRK free-space corollary

For a free-space electric-dipole transition,

\[
\Gamma_0=\frac{\omega_0^3|\mathbf d|^2}{3\pi\epsilon_0\hbar c^3}.
\]

With conventional oscillator strength

\[
f_{01}=\frac{2m_e\omega_0}{3\hbar e^2}|\mathbf d|^2
\]

and `sum_f f_0f = N_e`, one obtains

\[
\boxed{
\Gamma_0
\le
\frac{N_e e^2\omega_0^2}{2\pi\epsilon_0m_ec^3}
=2N_e\alpha\frac{\hbar\omega_0}{m_ec^2}\omega_0.
}
\]

Illustrative one-electron values:

- `10 um`: `6.67e5 s^-1`, inverse rate `1.50 us`;
- `1.55 um`: `2.78e7 s^-1`, inverse rate `36 ns`;
- `500 nm`: `2.67e8 s^-1`, inverse rate `3.75 ns`.

Do **not** present this as a universal photodetector limit. `N_e` is extensive, solids require careful normalization, and photonic environments modify the LDOS/Purcell factor.

---

# Electromagnetic-side missing resource

Matter TRK alone does not bound the full device coupling. The electromagnetic environment controls the Green tensor / LDOS. Resonators, slow light, plasmonic confinement, collective coupling, and cavity mode volume introduce additional resources.

Existing optical-response theory already gives:

- geometry/material-dependent single-frequency optical bounds;
- LDOS sum rules;
- arbitrary-bandwidth LDOS power-bandwidth bounds;
- broadband coupling/absorption bounds.

The leading route is therefore a **composition theorem** combining:

1. matter oscillator-strength / f-sum budget;
2. electromagnetic LDOS / susceptibility / geometry / bandwidth budget;
3. the photodetector thermokinetic gateway theorem;
4. a finite optical information task.

Key physical observation: detecting amplitude/phase modulation up to baseband `Omega_s` requires an optical frontend that accepts carrier sidebands over a corresponding optical bandwidth. An arbitrarily large but arbitrarily narrow Purcell resonance should therefore not automatically yield arbitrarily large information bandwidth.

This composition is **OPEN**.

---

# Quantum-photodetector connection

Young–Sarovar–Léonard (2018) explicitly found in their dark-state fully quantum detector that near-perfect detection is obtained when optical coupling `gamma` and localization rate become arbitrarily large compared with photon wavepacket duration. Their model therefore contains the same unbounded-coupling escape hatch isolated by WP4.

Do not claim their result is wrong. It is a model with unconstrained `gamma`. The UPRP contribution is to identify and constrain the physical resource represented by `gamma`.

Nishiyama–Hasegawa (2026) independently indicate that quantum evolution speed depends on interaction-Hamiltonian fluctuations, supporting the expectation that the quantum completion will involve `Var(H_int)` or a related coupling functional rather than entropy production alone.

---

# Current strongest research question

> **What is the weakest architecture-independent microscopic light–matter resource that, together with a finite optical task bandwidth and thermodynamic/kinetic budgets, yields a finite upper bound on optical-to-electrical information-transfer speed?**

Leading candidates:

\[
\gamma_{\max}(\omega),
\quad
J_{\rm EM}(\omega),
\quad
|d|^2\rho_{\rm EM},
\quad
\text{TRK/f-sum budget},
\quad
\text{finite-band LDOS/absorption functional},
\quad
\operatorname{Var}(H_{\rm int}),
\quad
\|H_{\rm int}\|.
\]

The likely final result may be a paired theorem:

1. **No-go:** thermodynamic ratios + stationary costs do not determine an absolute detector speed scale.
2. **Completion:** adding an explicit microscopic light–matter coupling resource restores a finite information-bandwidth bound.

---

# Critical literature overlap

Do not claim as new:

- general quantum photodetector frameworks/tradeoffs — Young, Sarovar, Léonard (2018);
- continuous-measurement/open-system TURs — Hasegawa and successors;
- detector performance versus thermodynamic cost — Schwarzhans et al. (2025/2026);
- finite-frequency fluctuation-response inequalities — Dechant (2026);
- response KURs — Liu & Gu (2026);
- finite-frequency thermodynamic/kinetic response bounds — Zheng & Lu (2026);
- output response precision bounded by QFI/activity — Gu & Liu (2026);
- general open-system precision limits — Vu et al. (2026);
- arbitrary-bandwidth LDOS/power-bandwidth bounds — Shim, Fan, Johnson, Miller (2019) and subsequent optical-limit literature.

Potential novelty is the photodetection-specific **missing absolute coupling resource** theorem and its composition with optical sum rules/power-bandwidth limits.

---

# Immediate priorities

1. Derive a rigorous finite-band optical coupling bound from TRK + Green-tensor/LDOS power-bandwidth theory.
2. Prove the carrier-sideband/baseband mapping without assuming a single-mode cavity.
3. Attempt

\[
\bar\eta_{\mathcal I}(\Omega_s)\ge r
\Rightarrow
\Omega_s\le F(\Sigma,\mathcal A,f_*,C_{\rm matter},C_{\rm EM}).
\]

4. Translate the Markov coupling resource into the Young–Sarovar–Léonard input-output quantum model.
5. Test whether `Var(H_int)` is sufficient or whether an electromagnetic bandwidth/spectral resource is still independently necessary.
6. Continue theorem-level novelty audit before publication claims.

---

# Mandatory adversarial checks

For every candidate theorem, test:

1. dimensions and reparameterization invariance;
2. deterministic output-gain invariance;
3. ideal photon counter/direct-feedthrough limit;
4. source-bandwidth leakage;
5. parallel replication/extensivity;
6. rare-fast states;
7. hidden degrees of freedom;
8. bounded total and edge EPR with divergent bare rates;
9. bounded stationary activity with divergent latent rates;
10. fixed optical detailed-balance ratio with diverging absolute coupling;
11. equilibrium/zero-current limits;
12. weak and strong optical flux;
13. increasing state-space dimension;
14. coherence/non-Markovianity/feedback/nonreciprocity;
15. cavity/LDOS/Purcell engineering;
16. whether a proposed resource merely restates bandwidth instead of explaining it.

---

# Recordkeeping

After each substantive result:

- update a dedicated derivation note;
- add to `notes/RESEARCH_LOG.md` or a numbered round log;
- preserve failed conjectures/counterexamples;
- update this file whenever project direction changes materially.

Status labels:

- **PROVED** — complete derivation under explicit assumptions;
- **VERIFIED** — independently checked but proof not fully formalized;
- **CONJECTURE** — plausible and unproved;
- **COUNTEREXAMPLE** — explicit model violating a stated claim;
- **OPEN** — unresolved;
- **BLOCKED** — missing theoretical/source input;
- **REJECTED** — invalid or redundant.

## Current state — Round 2, 2026-08-19

WP1 Markov response/noise machinery is solved. WP0 classical/coherent information normalization is largely solved. WP3 produced a restricted positive gateway theorem. WP4 produced the strongest result so far: a reversible detailed-balance-preserving counterexample proving that fixed temperature, photon energy, optical detailed balance, throughput, stationary activity, total EPR, and edge EPRs still do not bound photodetector speed when the absolute light–matter coupling scale is unconstrained. The decisive next gate is to derive the weakest physically meaningful matter+electromagnetic coupling resource that closes this loophole.