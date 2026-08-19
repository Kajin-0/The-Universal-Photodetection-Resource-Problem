# AGENTS.md

## Purpose

This is the durable handoff record for **The Universal Photodetection Resource Problem (UPRP)**. The repository is authoritative project memory; do not assume chat context survives.

Before doing new work, read at minimum:

1. `README.md`
2. `PROBLEM.md`
3. `ROADMAP.md`
4. `docs/FORMALISM.md`
5. `docs/LITERATURE_MAP.md`
6. `docs/NOVELTY_AND_FALSIFICATION.md`
7. `notes/WP0_WP1_ROUND1.md`
8. `notes/WP2_REVERSIBLE_TWO_CHANNEL.md`
9. `notes/WP2_THREE_STATE_RARE_FAST_COUNTEREXAMPLE.md`
10. `notes/WP0_BANDWIDTH_CORRECTION.md`
11. the full `notes/RESEARCH_LOG.md`

## Project objective

Determine what fundamental resources are necessary and/or sufficient for a finite-temperature photodetector to transfer information from an incident optical field into an electrical measurement record with specified sensitivity and temporal bandwidth.

A successful endpoint may be:

- a rigorous universal resource bound;
- a rigorous no-go theorem showing that a proposed resource set cannot bound detector performance;
- an explicit counterexample family;
- identification of a necessary missing resource followed by a repaired theorem.

Do **not** assume a simple sensitivity-bandwidth-temperature inequality exists.

## Research mode

Analytical/theoretical only. Numerical algebra or simulation is allowed for conjecture testing and validation. Do not make laboratory experiments, fabrication, sample procurement, or measurement campaigns necessary next steps.

---

# Current central information object

For incident optical parameter \(\theta\), define the information-transfer efficiency

\[
\boxed{
\eta_{\mathcal I}
=\frac{\dot F_{\rm out}}{\dot F_{\rm in}^{Q}}
}
\]

where the numerator is classical Fisher information rate in the complete electrical output record and the denominator is quantum Fisher information rate available in the incident optical field for the same parameter.

This ratio is invariant under reparameterization of \(\theta\), invariant under invertible deterministic output transformations, and obeys

\[
0\le\eta_{\mathcal I}\le1.
\]

For coherent/Poisson weak photon-flux modulation,

\[
\boxed{
\eta_{\mathcal I}(\omega)
=\Phi_0\frac{|\chi_{Y\Phi}(\omega)|^2}{S_Y(\omega)}
=\Phi_0K_\Phi(\omega).
}
\]

This is the temporal analogue of detective quantum efficiency (DQE). The normalization is useful but not novel.

## Critical correction: do not use unweighted all-frequency bandwidth as a universal finite objective

The previously introduced

\[
B_{\mathcal I}=\int\frac{d\omega}{2\pi}\eta_{\mathcal I}(\omega)
\]

is finite for many internal-response models and is useful diagnostically, but it is **not generically finite**. An ideal continuous-time photon counter has \(\eta_{\mathcal I}(\omega)=1\) for all modulation frequencies in the white-Poisson model, hence \(B_{\mathcal I}=\infty\).

Use instead a specified optical task/mode family. If \(\mathcal J_{\rm in}(\omega)\) is the input QFI spectral density,

\[
\boxed{
\bar\eta_{\mathcal I}
=\frac{\int\frac{d\omega}{2\pi}\mathcal J_{\rm in}(\omega)\eta_{\mathcal I}(\omega)}
{\int\frac{d\omega}{2\pi}\mathcal J_{\rm in}(\omega)}.
}
\]

For a flat task band \(|\omega|\le\Omega_s\),

\[
\boxed{
\bar\eta_{\mathcal I}(\Omega_s)
=\frac{1}{2\Omega_s}\int_{-\Omega_s}^{\Omega_s}d\omega\,\eta_{\mathcal I}(\omega).
}
\]

The revised theorem target is a **resource requirement** for maintaining \(\bar\eta_{\mathcal I}(\Omega_s)\ge\eta_*\) as \(\Omega_s\) increases.

---

# Exact Markov machinery already derived

Column-vector convention:

\[
\dot p=Wp,\qquad \mathbf1^TW=0,\qquad W\pi=0.
\]

Define

\[
\Pi=\pi\mathbf1^T,\qquad Q=I-\Pi,
\]

and reduced resolvent

\[
R(\omega)=Q(i\omega I-W)^{-1}Q.
\]

For jump-counting operators \(\mathcal J^{(1)}\), \(\mathcal J^{(2)}\):

\[
\boxed{
\bar I=\mathbf1^T\mathcal J^{(1)}\pi,
}
\]

\[
\boxed{
S_I(\omega)=\mathbf1^T\mathcal J^{(2)}\pi
+2\operatorname{Re}[\mathbf1^T\mathcal J^{(1)}R(\omega)\mathcal J^{(1)}\pi].
}
\]

For scalar input \(u\) perturbing both generator and possibly the counted edge,

\[
\boxed{
\chi_{Iu}(\omega)
=\mathbf1^T\mathcal J_u^{(1)}\pi
+\mathbf1^T\mathcal J_0^{(1)}R(\omega)W_u\pi.
}
\]

These formulas were checked against a solvable two-state model and are treated as **PROVED within the finite-state stationary Markov jump class**.

---

# Results already obtained

## Result A — two-state activity-only counterexample

For excitation \(a\), reset/readout \(b\), counting the reset jump,

\[
\eta_{\mathcal I}(\omega)
=\frac{\alpha b^3}{(a+b)(a^2+b^2+\omega^2)},
\]

\[
B_{\mathcal I}
=\frac{\alpha b^3}{2(a+b)\sqrt{a^2+b^2}}.
\]

With fixed \(a\) and \(b\to\infty\), stationary activity tends to \(2a\) while \(B_{\mathcal I}\propto b\). Stationary activity alone therefore cannot encode latent reset speed in an unconstrained kinetic model.

## Result B — reversible two-channel fast-reset lemma

For a reversible two-state detector with optical channel \(u\leftrightarrow d\) and readout channel \(r\leftrightarrow s\), fixed \(u,d>0\), and \(r\to\infty\): both total stationary activity and entropy-production rate cannot remain bounded simultaneously.

- bounded \(s\): activity finite, but affinity/EPR diverges as \(\ln r\);
- growing \(s\): bidirectional traffic/activity diverges.

This is **PROVED for that model**, not universal.

## Result C — three-state rare-fast counterexample

Reversible unicycle:

\[
0\xrightleftharpoons[cR]{u}1,
\qquad
1\xrightleftharpoons[q]{R}2,
\qquad
2\xrightleftharpoons[s]{b}0.
\]

Count the forward \(1\to2\) jump; perturb \(u\).

The fast intermediate has \(\pi_1=O(R^{-1})\). As \(R\to\infty\):

- mean forward output count remains finite;
- total stationary activity tends to a finite constant;
- cycle affinity \(\ln[ub/(cqs)]\) is fixed;
- net entropy-production rate tends to a finite constant;
- at frequencies \(\omega=Rx\), response remains finite and output noise tends to finite shot noise;
- therefore \(\eta_{\mathcal I}(Rx)\) tends to a positive function of \(x\), and the diagnostic \(B_{\mathcal I}\) grows at least linearly with \(R\).

Thus \(\{\mathcal A_{\rm stationary},\sigma_{\rm net}\}\) cannot bound latent broadband transduction in the abstract reversible Markov class.

**Critical caveat:** the signal-facing reverse rate is \(cR\) while forward baseline \(u\) is fixed. A literal fixed-frequency optical absorption/emission reservoir may forbid that scaling. Therefore this is an abstract Markov counterexample, not yet a fully microscopic fixed-\(\hbar\omega\) photodetector counterexample.

The construction hides the growing rate in large local detailed-balance/rate-ratio scales. This strongly points to a missing microscopic energetic/kinetic resource.

---

# Current no-go hypothesis

The strongest current hypothesis is:

> **No finite universal photodetector sensitivity-speed bound can depend only on stationary thermodynamic observables such as temperature, photon flux, net entropy production, stationary activity, and low-frequency efficiency. A source temporal-mode constraint and at least one microscopic detector kinetic/coupling resource are necessary.**

Candidate missing detector resources include:

- maximum or suitable norm of escape/transition rates;
- edge-resolved kinetic prefactors;
- maximum local detailed-balance increment / absolute energy bias;
- heat/work/free-energy throughput before sign cancellation;
- generator norm or spectral diameter;
- system-bath coupling norm / bath spectral density;
- Hamiltonian norm or energy variance in the quantum problem;
- oscillator-strength / optical absorption sum-rule budget;
- detector size / propagation-speed resource where relativity matters.

Do not choose one prematurely. The next objective is to identify the weakest physically meaningful resource that repairs the no-go.

---

# Proper-transducer distinction

If the optical input directly modulates the counted electrical edge, the susceptibility contains a direct feedthrough term

\[
\mathbf1^T\mathcal J_{\Phi}^{(1)}\pi,
\]

which need not decay at high frequency. Any intrinsic transduction-bandwidth theorem must therefore either use a finite source task band or explicitly restrict to **proper transducers** with distinct optical input and electrical output channels:

\[
\boxed{\mathcal J_{\Phi}^{(1)}=0.}
\]

Do not silently assume this.

---

# Critical literature overlap as of 2026-08-19

The following areas are already occupied and must not be claimed as new:

- fundamental quantum-photodetector frameworks and coherence/backaction tradeoffs — Young, Sarovar, Léonard (2018);
- continuous-measurement/open-system thermodynamic uncertainty relations — Hasegawa and later work;
- detector performance versus thermodynamic cost — Schwarzhans et al., now PRX Quantum 7, 033001 (2026);
- finite-frequency Markov fluctuation-response inequality — Andreas Dechant, PRL 136, 207101 (2026), DOI `10.1103/3hs9-dz3d`;
- response kinetic uncertainty relations — Liu & Gu, PRA 113, 062443 (2026);
- finite-frequency thermodynamic/kinetic response bounds for barrier and entropic perturbations — Zheng & Lu, arXiv:2602.18631 (2026);
- downstream measurement response precision bounded by output-field QFI / signal-channel activity — Gu & Liu, arXiv:2605.03340 (2026);
- strong-coupling quantum KURs — Blasi et al., PRL 137, 056302 (2026);
- general open-system precision limits — Vu et al., PRL 136, 190401 (2026).

Important distinction: published frequency-integrated FRIs generally integrate squared response normalized by time-domain variance; this is not automatically identical to integrating the spectral information ratio \(|\chi(\omega)|^2/S(\omega)\). Compare theorem statements line-by-line before claiming overlap or novelty.

---

# Immediate highest-priority tasks

1. **Fixed optical reservoir test.** Keep \(\hbar\omega_{\rm opt}\), optical occupation/flux, and signal-facing absorption/emission relation fixed. Ask whether a rare-fast internal construction can still evade stationary activity + EPR bounds.
2. **No-go theorem.** Formalize the statement that source bandwidth and microscopic kinetic/coupling scale are necessary for any finite universal speed bound.
3. **Resource repair.** Test candidate resources such as maximum escape rate, absolute/local affinity budget, generator norm, coupling norm, and energy throughput.
4. **Task metric.** Use \(\bar\eta_{\mathcal I}[\mathcal J_{\rm in}]\), not an unqualified all-frequency integral, for theorem statements.
5. **Quantum extension only after classical structure is understood.** Map the missing classical kinetic resource to Hamiltonian/coupling/spectral-density resources.
6. **Novelty audit.** Continue citation chaining before any publication claim.

---

# Mandatory adversarial checks

For every candidate theorem/resource set, test:

1. units and reparameterization invariance;
2. deterministic output gain invariance;
3. ideal photon counter / direct-feedthrough limit;
4. source-bandwidth leakage;
5. parallel replication and extensivity;
6. rare-fast-state constructions;
7. hidden degrees of freedom;
8. bounded net EPR but divergent local energy biases;
9. bounded stationary activity but divergent latent escape rates;
10. equilibrium and zero-current limits;
11. weak optical flux;
12. large photon flux;
13. fixed optical frequency and fixed optical reservoir relations;
14. finite state number versus increasing state-space dimension;
15. non-Markovianity/coherence/feedback/nonreciprocity;
16. whether the proposed resource is actually measurable or merely a restatement of bandwidth.

---

# Recordkeeping protocol

After every substantive step:

1. add a dated result to `notes/RESEARCH_LOG.md`;
2. create/update a dedicated derivation note;
3. preserve failed conjectures and counterexamples;
4. update this `AGENTS.md` when the project direction materially changes;
5. do not let essential reasoning exist only in chat.

Status labels:

- **PROVED** — complete derivation under explicit assumptions;
- **VERIFIED** — independently checked but proof not fully formalized;
- **CONJECTURE** — plausible, unproved;
- **COUNTEREXAMPLE** — explicit model violates stated claim;
- **OPEN** — unresolved;
- **BLOCKED** — missing theoretical/source input;
- **REJECTED** — approach invalid/redundant.

## Current state — end of Round 1, 2026-08-19

WP0 normalization is largely solved, WP1 finite-state response/noise machinery is solved for the Markov class, and WP2 has produced both a reversible fast-reset lemma and a stronger three-state counterexample to activity+net-EPR sufficiency in the abstract Markov class. The project has pivoted from searching immediately for a simple universal bound toward a **no-go / missing-resource theorem**, with the fixed-optical-reservoir constraint now the decisive next gate.
