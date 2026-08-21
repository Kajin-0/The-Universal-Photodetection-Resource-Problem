# Research Roadmap — Rev7 Submission Package Phase

**Updated:** 2026-08-20

## Guiding principle

The autonomous marked-event branch has passed its theorem, hostile-review, significance-upgrade, proof-hardening, and manuscript-compilation gates. The first-paper task is now **submission packaging and journal positioning**, not additional foundational derivation.

Do not reopen material-specific, coherent-pointer, analog-detector, non-Poisson, or high-flux/history-dependent branches unless a concrete defect in Rev7 requires it.

---

# Closed theorem stack

## E0 — Exact autonomous marked-event kernel
**PROVED**

\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\qquad
G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm).
\]

Exact DC is handled separately; normalized transfer remains `G(0)=eta`.

## E1 — Complete weak-waveform Fisher operator
**PROVED — REV7**

For finite-dimensional weak temporal perturbations,
\[
\boxed{
[F_{\rm out}]_{ab}
=\frac{\Phi_0}{2\pi}
\int G(\omega)S_a^*(\omega)S_b(\omega)d\omega.
}
\]

Thus `G` is the spectral multiplier of the complete local weak-waveform Fisher operator for the stated detector class.

## E2 — Universal weak-waveform Fisher ordering
**PROVED — REV7**

\[
\boxed{
G_A(\omega)\ge G_B(\omega)\ \forall\omega
\iff
F_A\succeq F_B
\text{ for every admissible finite weak-waveform task.}
}
\]

This is a local Fisher-ordering result, not generic Blackwell dominance.

## E3 — Exact band-subspace guarantee
**PROVED — REV7**

For `supp S subset [-Omega,Omega]`,
\[
\boxed{
\inf\rho_G[s]
=
\min_{|\omega|\le\Omega}G(\omega).
}
\]

Hence retaining at least absolute Fisher fraction `q` for every weak waveform in the band is equivalent to
\[
\boxed{G(\omega)\ge q\quad\forall|\omega|\le\Omega.}
\]

## E4 — Atomic high-band residue
**PROVED**

\[
\boxed{
\lim_{\Omega\to\infty}\frac1{2\Omega}
\int_{-\Omega}^{\Omega}G(\omega)d\omega
=
\int\kappa(dm)\sum_jp_j(m)^2.
}
\]

## E5 — Timing-collision spectral resource
**PROVED**

\[
\boxed{
\mathfrak R_2=2\int\kappa(dm)\int f_m^2dt,
\qquad
\int G(\omega)d\omega=\pi\mathfrak R_2.
}
\]

## E6 — Exact Fisher-equivalent bandwidth
**PROVED — REV7**

For `eta>0`,
\[
\boxed{
B_{\rm FI}
=\frac1\eta\int_0^\infty G(2\pi f)df
=\frac{\mathfrak R_2}{4\eta}.
}
\]

This is an information-area bandwidth, not an electrical amplitude bandwidth.

## E7 — Capture-weighted local-hazard resource
**PROVED; WP35 + REV6 SELF-CONTAINED CTMC COMPLETION**

\[
\boxed{
\mathfrak H=\int\Lambda(m)\kappa(dm),
\qquad
\mathfrak R_2\le\mathfrak H,
\qquad
B_{\rm FI}\le\frac{\mathfrak H}{4\eta}.
}
\]

For a common conditional-hazard ceiling,
\[
\boxed{B_{\rm FI}\le\Lambda/4.}
\]

For finite-state CTMC pre-registration states,
\[
\boxed{
q_{\max}=\max_{x\in S_{\rm pre}}
\sum_{y\ne x}W_{yx}.
}
\]

The old successful-registration-edge-only statement is rejected. The generic quantum-jump extension remains deferred.

## E8 — Operational inverse cost
**PROVED; STRONGER REV7 INTERPRETATION**

For ordinary-frequency half-band `B=Omega/(2pi)` and required absolute transfer `q`,
\[
\boxed{
q\le\eta,
\qquad
\mathfrak R_2\ge4Bq,
\qquad
\mathfrak H\ge4Bq.
}
\]

Originally derived for flat-average retention, the same coefficient is also a necessary cost for guaranteeing at least `q` Fisher retention for **every weak waveform in the full band**.

For a common hazard ceiling,
\[
\boxed{\Lambda\ge4Bq/\eta.}
\]
For relative retention `q=r eta`,
\[
\boxed{\Lambda\ge4Br.}
\]

## E9 — Independent-stage architecture law
**PROVED FOR THE STATED UNMARKED INDEPENDENT DELAY-ONLY CLASS — REV7**

\[
\boxed{G_{12}=G_1G_2.}
\]

For `k` serial exponential waits of rate `lambda`,
\[
\boxed{
B_{\rm FI}
=\frac{\lambda}{4}
\frac{\binom{2k-2}{k-1}}{4^{k-1}}
\sim\frac{\lambda}{4\sqrt{\pi(k-1)}}.
}
\]

Do not generalize the scalar product law to retained-mark or history-dependent cascades without a new proof.

## E10 — No-go/repair layer
**PROVED FOR MANUSCRIPT CLAIMS**

- exact mean + exact RMS jitter do not bound information bandwidth;
- no fixed-FWHM counterexample is claimed;
- free synchronous temporal reference defeats detector-only timing bounds;
- stationary EPR/activity/throughput do not provide an absolute microscopic time scale;
- deterministic latency is not information loss;
- parameter-independent downstream processing cannot improve primary-record FI.

---

# Thermodynamic completion

**PROVED FOR THE RESTRICTED BIDIRECTIONALLY CONNECTED GATEWAY CLASS, WITH EXPLICIT LOW-OVERLAP BRIDGE**

Use **bidirectionally connected**, not “reversible,” for the nonequilibrium CTMC network. Reverse-transition support does not imply detailed balance.

For the restricted gateway,
\[
\boxed{
\lambda_1\le
\Lambda_*
=\frac{\mathcal A d}{f_*}g^{-1}(\Sigma/f_*),
\qquad
g(z)=(1-z^{-1})\ln z.
}
\]

Stationary baseline thermodynamic quantities constrain microscopic rates; application to the event theorem conditions on an isolated capture and requires low overlap so capture/recovery do not become history dependent.

If capture/recovery is history dependent, the independent-event theorem is not applied.

The absolute reverse rate `d` remains indispensable.

---

# Publication state

## Rev4
Historical build-verified revision; contains later-corrected WP35 wording.

## Rev5
Historical WP35-corrected manuscript; superseded by hostile-review Rev6.

## Rev6
Frozen hostile-referee-hardened predecessor. It contains the exact-DC clarification, self-contained `q_max` proof, conservative FWHM wording, corrected nonequilibrium terminology, explicit isolated-event thermodynamic bridge, and layout repair.

## Rev7
`manuscript/event_resource_theorem_rev7.tex`

**CURRENT FIRST-PAPER SOURCE — SIGNIFICANCE-UPGRADED + PROOF-HARDENED + BUILD VERIFIED.**

Rev7 adds:

1. arbitrary finite-dimensional weak-waveform Fisher operator;
2. continuity/evenness/boundedness of `G`;
3. necessary-and-sufficient pointwise Fisher ordering;
4. exact compact-band worst-case retention;
5. exact `B_FI=mathfrak R_2/(4 eta)`;
6. hazard bound on `B_FI`;
7. independent delay-stage cascade and serial-Erlang example;
8. conservative prior-art positioning around Fisher transfer functions and detector response metrics.

Key verification:

- canonical push run `32433326375` — success;
- independent proof-hardened validation run `32433375491` — success;
- artifact ID `9429898246`;
- main TeX blob `f59e36e32a2d6eb36752c847cbdd40b07b241db0`;
- only inherited approximately `2.45667 pt` appendix overfull warning remains.

Temporary validation PR #13 is closed and unmerged.

Steady-state workflow restored by commit `8b9118bd7ae428dd51952853c1571624356fdc94` to read-only direct compilation of committed Rev7.

---

# Closed publication gates

## P1 — Core theorem audit
**PASSED.**

## P2 — Rev6 hostile-referee model-class/terminology repairs
**PASSED.**

## P3 — Rev6 mechanical verification
**PASSED.**

## P4 — Rev7 significance upgrade
**PASSED.** The arbitrary-waveform operator, ordering theorem, band-subspace guarantee, equivalent bandwidth, and cascade example all remain within the original independent-event model class.

## P5 — Rev7 proof hardening
**PASSED.** Plancherel-level Fourier definitions, admissibility/converse proofs, continuity of `G`, pointwise ordering, and compact-band extrema were tightened before final validation.

## P6 — Rev7 mechanical verification
**PASSED.** Two full CI validation paths compiled successfully and uploaded artifacts.

## P7 — Clean steady-state CI
**PASSED CONFIGURATION GATE.** Workflow is read-only, directly compiles committed Rev7, and has no self-commit or PR-validation side effects.

---

# Next gate — Submission package

Prepare the submission-ready package and journal positioning. This may include:

- verify current target-journal aims/scope and submission requirements;
- choose primary and fallback venue;
- final author/affiliation metadata;
- journal-format/source cleanup;
- cover letter and concise novelty/significance statement;
- final package inventory / reproducibility check;
- title/abstract polish only if scientifically neutral.

Do not use submission packaging as a pretext to reopen frozen research branches.

---

# Candidate second-paper directions — NOT first-paper blockers

Only after the first paper is packaged/submitted, consider:

- high-flux/history-dependent trajectory-level event channels;
- nonclassical/phase-sensitive input information and QFI normalization;
- coherent-pointer resource accounting;
- channel-capacity or Bayesian/global-estimation extensions;
- multistage marked detector networks beyond the scalar independent-delay cascade.

These are separate research programs unless a concrete Rev7 flaw makes one necessary.

---

# Frozen branches

- HgCdTe/Kane WP17–24;
- coherent quantum pointers;
- continuous classical/analog detector generalization;
- non-Poisson/nonclassical source extensions;
- high-flux/history-dependent generalization.
