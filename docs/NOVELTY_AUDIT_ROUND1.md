# Novelty Audit — Round 1

**Date:** 2026-08-19

## Result under audit

The current restricted gateway theorem is derived in `notes/WP3_GATEWAY_RESOURCE_THEOREM.md`.

For a reversible optical gateway with forward stationary optical traffic \(f\ge f_*>0\), fixed reverse optical rate \(d\), total steady dimensionless entropy-production rate \(\sigma_{\rm tot}\le\Sigma\), and total stationary activity \(\mathcal A_{\rm tot}\le\mathcal A\), define

\[
g(z)=\left(1-\frac1z\right)\ln z,
\qquad
Z_*=g^{-1}(\Sigma/f_*).
\]

The post-absorption gateway state obeys

\[
\pi_1\ge\frac{f_*}{dZ_*},
\]

and its escape rate obeys

\[
\boxed{
\lambda_1\le
\Lambda_*
=\frac{\mathcal A d}{f_*}Z_*.
}
\]

For a single-event proper transducer whose electrical event cannot occur before first exit from the gateway state,

\[
\eta_{\mathcal I}(\omega)
\le
\eta_q\frac{\Lambda_*^2}{\Lambda_*^2+\omega^2},
\]

and for a flat task band \(|\omega|\le\Omega_s\),

\[
\bar\eta_{\mathcal I}(\Omega_s)
\le
\eta_q\frac{\Lambda_*}{\Omega_s}
\arctan\frac{\Omega_s}{\Lambda_*}.
\]

This audit asks whether that exact chain is already known.

---

# 1. Schwarzhans et al. — closest detector-specific work

**E. Schwarzhans et al., _Quantum detectors as autonomous machines: assessing the nonequilibrium thermodynamics of information acquisition_, PRX Quantum 7, 033001 (2026), DOI `10.1103/wm5p-tjtg`, arXiv:2508.16375.**

## What overlaps

The overlap in physical setting is strong:

- discrete particle/click detector;
- autonomous finite-temperature detector;
- a detection-ready/metastable state;
- single-event transient dynamics;
- consecutive events explicitly treated as independent after reset;
- detector figures of merit include efficiency, dark counts, timing jitter, dead time, and gain;
- steady-state and transient entropy production are calculated;
- dead time is linked to the slowest nonzero Liouvillian eigenvalue;
- numerical tradeoffs connect lower jitter/dead time with higher thermodynamic/dark-count costs.

This makes Schwarzhans et al. the closest detector-specific prior work identified so far.

## What is different

The published tradeoff relations are obtained by numerical sampling of the parameters of a particular autonomous quantum thermal-machine detector. Their dead-time relation is reported as a detector-dependent proportionality between dark-count rate and inverse dead time; the proportionality coefficient depends on model-specific coupling parameters.

The paper does **not appear to derive** the UPRP gateway chain

\[
\text{forward optical throughput + edge reversibility + EPR}
\Rightarrow
\text{post-absorption occupancy floor}
\Rightarrow
\text{activity-imposed escape-rate ceiling}
\Rightarrow
\text{Lorentzian optical-information bandwidth ceiling}.
\]

It also explicitly notes that its thermodynamic analysis focuses on amplification **after the incoming particle has been captured**, while the capture process may have additional costs/inefficiencies. The UPRP gateway theorem instead uses the reversibility and entropy production of the signal-facing capture edge as a central resource constraint.

### Current classification

**Likely different theorem / complementary result**, not a direct restatement. Novelty remains provisional until citation chaining from this paper is complete.

---

# 2. Dechant — finite-frequency fluctuation-response inequality

**A. Dechant, _Finite-Frequency Fluctuation-Response Inequality_, Phys. Rev. Lett. 136, 207101 (2026), DOI `10.1103/3hs9-dz3d`, arXiv:2510.15228.**

## Overlap

Dechant proves a general finite-frequency fluctuation-response inequality for Markovian systems, including jump processes. In matrix form it bounds response precision at each frequency by the path Fisher-information cost of the perturbation. It also derives broadband response/SNR consequences.

Therefore the following statements are **not novel**:

- response-to-noise has a general finite-frequency bound;
- a Markov trajectory Fisher metric can bound susceptibility;
- generic broadband response inequalities exist.

## Difference

The gateway result is not obtained by simply relabeling Dechant's perturbation Fisher metric. It first derives a **kinetic-rate ceiling from stationary optical throughput, a fixed reverse optical rate, EPR, and total activity**, and only then converts that rate ceiling into an event-timing/information-transfer bound.

The detector-specific left-hand quantity is normalized by information available in the incoming optical field. The resource chain explicitly distinguishes source task, signal-facing optical transition, stationary detector resources, and downstream electrical event timing.

### Current classification

**Not mathematically identical.** Dechant is a critical background theorem and may provide a stronger/general alternative for later stages, but the present gateway inequality is not currently seen as a direct corollary.

---

# 3. Zheng & Lu — thermodynamic/kinetic finite-frequency response bounds

**Y. Zheng and Z. Lu, _Thermodynamic and Kinetic Bounds for Finite-frequency Fluctuation-Response_, arXiv:2602.18631 (2026).**

This work derives finite-frequency kinetic and thermodynamic bounds for specified perturbation classes, including barrier-like and entropic perturbations.

The main novelty risk is any claim that jointly thermodynamic and kinetic quantities can constrain finite-frequency response. That general idea is occupied.

The UPRP result differs by:

- the optical gateway/capture interpretation;
- a stationary occupancy floor derived from one reversible signal-facing edge;
- a derived ceiling on a physically identified first-post-absorption escape rate;
- a downstream first-event timing filter;
- normalization to incident optical Fisher/QFI rather than only response amplitude.

### Current classification

**Likely distinct specialization/chain**, but this source must remain in every publication-level comparison.

---

# 4. Gu & Liu — finite-frequency open-quantum response hierarchy

**J. Gu and K. Liu, _Finite-frequency fluctuation-response bounds for open quantum systems_, arXiv:2605.03340 (2026).**

Their hierarchy establishes, for specified Markovian open-quantum perturbations, that a measured downstream finite-frequency response precision is bounded by output-field quantum Fisher information, which is in turn bounded by a signal-channel activity quantity.

This directly occupies the broad statement

\[
\text{measured response precision}
\lesssim
\text{QFI/activity resource}.
\]

The UPRP project must therefore not market `information <= activity` as new.

The open difference is that the gateway theorem asks what **physical detector resources bound the kinetic scale itself** once the incoming optical reservoir and useful throughput are fixed.

### Current classification

**Adjacent and potentially composable**, not currently identical.

---

# 5. Nishiyama & Hasegawa — temporal Fisher-information speed limits

**T. Nishiyama and Y. Hasegawa, _Unified speed limits in classical and quantum dynamics via temporal Fisher information_, Phys. Rev. E 114, 014120 (2026), DOI `10.1103/x95d-fhpq`, arXiv:2504.04790v2.**

## What their Fisher information means

Their classical temporal Fisher information is

\[
\mathcal I_t(t)=\sum_i p_i(t)[\partial_t\ln p_i(t)]^2,
\]

which measures information about **elapsed time** encoded in the evolving state distribution.

For Markov jump dynamics they construct a special auxiliary perturbation that locally rescales the dynamics in time. The path Fisher information of that perturbation is bounded by accumulated entropy production and by accumulated dynamical activity, yielding state-transformation speed limits.

For general open quantum dynamics they derive

\[
\mathcal I_t(t)
\le 4\,\mathrm{Var}(H_{SE}),
\]

so the relevant quantum speed resource is explicitly the system-environment interaction-Hamiltonian variance.

## Difference from UPRP

UPRP uses Fisher information about an **externally encoded optical parameter/modulation** in a **downstream electrical record**, normalized to the corresponding input optical QFI. This is not temporal Fisher information about the clock variable \(t\), and the optical perturbation is not the special time-rescaling perturbation used in the speed-limit proof.

Thus their theorem does not directly imply the gateway information-transfer inequality.

However, their quantum result strongly supports a central UPRP lesson from the rare-fast counterexample: an ultimate speed bound requires a microscopic dynamical/coupling scale. In the quantum setting, interaction-Hamiltonian variance is a natural candidate.

### Current classification

**Distinct Fisher-information problem, highly relevant resource guidance.**

---

# 6. First-passage TUR literature

## Pal, Reuveni & Rahav

**A. Pal, S. Reuveni, S. Rahav, _Thermodynamic uncertainty relation for first-passage times on Markov chains_, Phys. Rev. Research 4, 013273 (2022), arXiv:2103.16578.**

They derive lower bounds on the **relative fluctuations** of first-passage times using integrated entropy production from reversible transitions and integrated traffic/flux from transitions treated as unidirectional. Their central quantity is

\[
CV^2=\frac{\mathrm{Var}(T)}{\langle T\rangle^2}.
\]

This is close to the UPRP timing-jitter corollary and therefore creates substantial novelty risk for any generic statement that dissipation/activity constrain first-passage-time fluctuations.

However, their theorem does not supply the stationary optical-edge occupancy argument or an upper bound on a gateway escape rate from fixed optical throughput plus stationary EPR/activity. It also does not formulate a frequency-resolved optical-information-transfer efficiency.

## Other FPT bounds

Relevant branches include:

- Garrahan (2017), kinetic bounds on fluctuations and first-passage times of counting observables;
- Hasegawa (2022), quantum first-passage TUR;
- Bakewell-Smith et al. (2024), rigorous FPT fluctuation/tail bounds for classical and quantum Markov counting processes;
- unified thermodynamic-kinetic uncertainty relations and mixed FPT bounds.

### Current classification

The **jitter/FPT consequence alone is not a safe novelty claim**. The candidate novelty, if any, lies in the photodetection-specific resource chain and optical-information formulation.

---

# 7. Detective quantum efficiency / information normalization

The normalized quantity

\[
\eta_{\mathcal I}
=F_{\rm out}/F_{\rm in}^{Q}
\]

is a useful invariant formulation. In the coherent Poisson linear regime,

\[
\eta_{\mathcal I}(\omega)
=\Phi_0|\chi_{I\Phi}(\omega)|^2/S_I(\omega),
\]

which is the temporal analogue of detective quantum efficiency, i.e. output SNR squared divided by input SNR squared.

### Current classification

**Normalization/bridge, not novelty.**

---

# 8. Current novelty matrix

| Result/claim | Current classification |
|---|---|
| Generic detector performance costs entropy | Occupied |
| Generic Markov finite-frequency response/noise bound | Occupied |
| Response precision bounded by activity/QFI | Occupied |
| Generic temporal-FI speed limit | Occupied |
| Generic FPT/jitter fluctuation bound from EPR/activity | Occupied |
| Information efficiency normalized to incident optical information | Useful but closely related to DQE |
| Activity + net EPR alone insufficient to bound latent Markov bandwidth | Explicit UPRP counterexample; novelty not yet fully audited |
| Rare-fast-state counterexample with finite activity and finite net EPR | Candidate novel constructive result; physical optical embedding still limited |
| Fixed optical gateway: EPR + throughput gives occupancy floor | Candidate novel lemma |
| Occupancy floor + total activity gives gateway escape-rate ceiling | Candidate novel lemma |
| Gateway escape-rate ceiling -> optical information-transfer Lorentzian | Elementary timing consequence once gateway lemma holds |
| Full combined finite-band photodetection theorem | **Candidate new result; novelty not closed** |

---

# 9. Most defensible publication direction after Round 1

A paper should **not** be framed as “the first thermodynamic limit on photodetection.” That would be false or at least indefensible given the 2026 literature.

A more defensible direction is:

> **Which resources are actually sufficient to bound temporal optical-information transfer in a detector?**

The paper could have a theorem/counterexample structure:

1. define source-normalized photodetection information efficiency;
2. prove that an unqualified all-frequency detector bandwidth is ill posed (ideal Poisson counter);
3. construct a reversible rare-fast-state family showing that stationary activity plus net EPR do not suffice in an abstract Markov transducer;
4. identify the missing signal-facing microscopic constraint;
5. impose a fixed reversible optical gateway and nonzero useful throughput;
6. prove the gateway occupancy/escape-rate theorem;
7. derive the information-spectrum, finite-band, and timing consequences;
8. identify what must replace the gateway rate in a fully quantum detector (likely an interaction/coupling resource).

This combination is substantially stronger and safer than trying to claim a single generic TUR-like inequality.

---

# 10. Remaining novelty gates

Before publication-level novelty language:

- citation-chain Dechant, Gu & Liu, Zheng & Lu, Pal-Reuveni-Rahav, and Schwarzhans;
- audit thermodynamic speed limits involving traffic + entropy production jointly;
- audit biochemical sensing speed-energy-accuracy theorems, which may contain structurally similar gateway arguments;
- audit queueing/phase-type/renewal literature for the first-exit filter;
- audit optical communications/information theory for temporal DQE/Fisher-transfer formulations;
- audit optical absorption/emission detailed-balance constraints and Einstein-rate relations;
- audit quantum speed limits based specifically on interaction-Hamiltonian or Liouvillian norms.

**Novelty status after Round 1: promising but not closed.**