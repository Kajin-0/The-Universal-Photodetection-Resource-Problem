# AGENTS.md

## Purpose

This is the durable handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat context, is authoritative.

Before new work, read in this order:

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `notes/RESEARCH_LOG_ROUND3.md`
3. `notes/WP5_T_OPERATOR_FINITE_BAND_CAPTURE.md`
4. `notes/WP5_INCIDENT_CHANNEL_QFI_SUM_RULE.md`
5. `docs/NOVELTY_AUDIT_ROUND2.md`
6. `notes/WP4_MICROSCOPIC_OPTICAL_COUPLING_NO_GO.md`
7. `notes/WP3_GATEWAY_RESOURCE_THEOREM.md`
8. `notes/RESEARCH_LOG_ROUND2.md`
9. `notes/RESEARCH_LOG.md`
10. `docs/FORMALISM.md`
11. `docs/LITERATURE_MAP.md`

The older WP0/WP1/WP2 notes remain important for derivations and failed conjectures.

---

# Project objective

Determine the resources necessary and/or sufficient for a finite-temperature photodetector to transfer information from an incident optical field into an electrical measurement record with specified sensitivity and temporal bandwidth.

Valid outcomes include:

- a rigorous resource bound;
- a rigorous no-go theorem;
- an explicit counterexample family;
- identification of a missing resource followed by a repaired theorem.

Do **not** assume a simple sensitivity-bandwidth-temperature product exists.

Research is analytical/theoretical. Numerical work may verify algebra or conjectures. Do not make laboratory experiments or fabrication necessary next steps.

---

# Information metric

Use

\[
\boxed{
\eta_{\mathcal I}
=\frac{F_{\rm electrical}}{F_{\rm incident}^{Q}}
}
\]

for the same encoded optical parameter.

For coherent/Poisson weak photon-flux modulation,

\[
\eta_{\mathcal I}(\omega)
=\Phi_0\frac{|\chi_{Y\Phi}(\omega)|^2}{S_Y(\omega)}.
\]

This is the temporal analogue of DQE and is not itself novel.

Do not use an unweighted all-frequency integral as the universal objective. Use a finite task:

\[
\bar\eta_{\mathcal I}
=\frac{\int(d\omega/2\pi)\mathcal J_{\rm in}(\omega)\eta_{\mathcal I}(\omega)}
{\int(d\omega/2\pi)\mathcal J_{\rm in}(\omega)}.
\]

For a flat baseband task `|Omega| <= Omega_s`, average over that interval.

---

# WP1 — exact finite-state Markov machinery: SOLVED

Column-vector convention:

\[
\dot p=Wp,
\qquad
\mathbf1^TW=0,
\qquad
W\pi=0.
\]

With reduced resolvent

\[
R(\omega)=Q(i\omega I-W)^{-1}Q,
\]

counted-current noise and response are

\[
\boxed{
S_I(\omega)=\mathbf1^T\mathcal J^{(2)}\pi
+2\operatorname{Re}[\mathbf1^T\mathcal J^{(1)}R(\omega)\mathcal J^{(1)}\pi]
}
\]

and

\[
\boxed{
\chi_{Iu}(\omega)=
\mathbf1^T\mathcal J_u^{(1)}\pi
+
\mathbf1^T\mathcal J_0^{(1)}R(\omega)W_u\pi.
}
\]

These are **PROVED for finite-state stationary Markov jump detectors** and checked against a solvable two-state model.

---

# WP4 — strongest no-go result

Microscopic weak-coupling bosonic optical rates are

\[
\Gamma_\uparrow=\gamma(\omega_0)n(\omega_0),
\qquad
\Gamma_\downarrow=\gamma(\omega_0)[n(\omega_0)+1].
\]

Fixed temperature and photon energy fix the ratio but not the absolute coupling `gamma`.

The reversible family

\[
0\xrightleftharpoons[bR]{aR}1,
\qquad
1\xrightleftharpoons[q]{cR}2,
\qquad
2\xrightleftharpoons[sR]{p}0
\]

preserves fixed optical detailed balance `a/b`, finite nonzero optical throughput, finite total activity, finite total and edge-resolved EPR, and finite nonzero detection probability while the post-absorption escape rate `(b+c)R` diverges.

Therefore

\[
\boxed{
\{T,\hbar\omega_0,\text{detailed balance},f_*,\mathcal A,\Sigma,\text{edge EPRs},\eta_q\}
\not\Rightarrow
\text{finite detector speed}.
}
\]

An **absolute microscopic coupling/transition resource is necessary**.

This is **PROVED for the reversible finite-state Markov event-detector class**.

---

# WP3 — restricted internal completion theorem

For a reversible optical gateway with fixed reverse optical rate `d`, minimum forward throughput `f_*`, total EPR budget `Sigma`, and activity budget `A`, define

\[
g(z)=\left(1-\frac1z\right)\ln z,
\qquad
Z_*=g^{-1}(\Sigma/f_*).
\]

Then

\[
\pi_1\ge\frac{f_*}{dZ_*},
\]

\[
\lambda_1\le
\Lambda_*
=\frac{\mathcal A d}{f_*}Z_*.
\]

For a proper single-event detector whose electrical record cannot occur before first exit from the post-absorption gateway,

\[
\boxed{
\eta_{\mathcal I}(\omega)
\le
\eta_q\frac{\Lambda_*^2}{\Lambda_*^2+\omega^2}.
}
\]

If an independent microscopic resource gives

\[
\gamma(\omega_0)\le\gamma_{\max},
\]

then `d <= gamma_max[n+1]` and the same theorem becomes a microscopic conditional bound.

---

# WP5 — incident optical capture: current frontier

## Coherent passive capture lemma

For a passive frequency-preserving linear frontend and coherent-state displacement encoding, let `tau(omega)` be the fraction of the normalized incident channel delivered to absorptive/capture modes. Then

\[
F_{\rm electrical}
\le
F_{\rm cap}^{Q}
=
\int\frac{d\omega}{2\pi}
\tau(\omega)\mathcal J_{\rm in}(\omega).
\]

Thus for a flat optical sideband-QFI task,

\[
\boxed{
\bar\eta_{\mathcal I}
\le
\frac1{2\Omega_s}
\int_{\omega_0-\Omega_s}^{\omega_0+\Omega_s}
\tau(\omega)d\omega.
}
\]

This is **PROVED** for the stated coherent/passive frontend class.

## Fixed-spatial-mode T-operator theorem

Use the unrenormalized positive-frequency oscillator variables of Zhang–Monticone–Miller (2023):

\[
\mathbb Z(\omega)
=\omega\operatorname{Im}\mathbb T(\omega)
=\mathbb X(\omega)+\mathbb Y(\omega),
\]

with `X >= 0` and `-X <= Y <= X`.

Their high- and low-frequency sum rules imply

\[
\int_0^\infty\mathbb Xd\omega
\preceq\frac\pi2\omega_p^2\mathbb I_D,
\]

\[
\int_0^\infty\frac{\mathbb X}{\omega^2}d\omega
\preceq\frac\pi2\mathbb T_{0,D}.
\]

For `B=[omega_-,omega_+]` and a **fixed incident spatial vector** `v`,

\[
\int_Bv^\dagger\mathbb Xv\,d\omega
\le
\frac\pi2
\min\left[
\omega_p^2\|v\|^2,
\omega_+^2v^\dagger\mathbb T_{0,D}v
\right].
\]

Hence for a reciprocal passive structure,

\[
\boxed{
\int_BP_{\rm cap}d\omega
\le
\frac{\epsilon_0\pi}{4}
\min\left[
\omega_p^2\|v\|^2,
\omega_+^2v^\dagger\mathbb T_{0,D}v
\right].
}
\]

General nonreciprocal passive case has twice this RHS.

For an electrically small reciprocal detector under nearly uniform illumination,

\[
\boxed{
\bar\eta_{\mathcal I}(\Omega_s)
\le
\min\left[
1,
\frac{\pi}{4cA\Omega_s}
\min\left(
\omega_p^2V,
(\omega_0+\Omega_s)^2\alpha_{\rm stat}
\right)
\right].
}
\]

This is **PROVED under the fixed-spatial-profile assumptions**.

At `lambda_0=10 um`, `r=0.9`, narrow sideband, the static branch scales as

\[
f_s\lesssim1.64\times10^{19}(\alpha_{\rm stat}/A)\ {\rm Hz/m}.
\]

Examples: effective static length `1 um -> 16.4 THz`, `100 nm -> 1.64 THz`, `10 nm -> 164 GHz`. These are scaling examples, not material-specific limits.

---

# New spatial-channel obstruction

For a propagating field over a large device, the incident profile generally changes with frequency:

\[
v(\omega,r)\propto e^{i\omega\hat k\cdot r/c}.
\]

Different frequencies can exploit different spatial response directions. If all profiles lie in an `M`-dimensional fixed subspace, a coarse sum-rule bound scales explicitly with `M`.

Therefore the arbitrary finite-band theorem needs a **spatio-spectral degrees-of-freedom / footprint / channel-rank resource** in addition to oscillator strength and static response.

Current likely resource hierarchy:

\[
\boxed{
\text{source temporal task}
+
\text{matter oscillator strength}
+
\text{static/finite-band EM response}
+
\text{spatial channel/footprint resource}
+
\text{internal thermokinetic resources}.
}
\]

---

# Current restricted optical + internal theorem

For the intersection of:

- coherent-state encoding;
- passive reciprocal optical frontend;
- fixed incident spatial profile over the sideband band;
- finite T-operator high/low-frequency resources;
- WP3/WP4 downstream event-transducer assumptions;

we have

\[
\bar\eta_{\rm total}
\le B_{\rm opt}(\Omega_s),
\qquad
\bar\eta_{\rm total}
\le B_{\rm trans}(\Omega_s),
\]

therefore

\[
\boxed{
\bar\eta_{\rm total}(\Omega_s)
\le
\min\{B_{\rm opt}(\Omega_s),B_{\rm trans}(\Omega_s)\}.
}
\]

This is a valid restricted completion theorem. It is not the final universal theorem.

---

# Critical novelty constraints

Do **not** claim novelty for:

- general quantum photodetector tradeoffs — Young, Sarovar, Léonard (2018);
- thermodynamic measurement/precision bounds — Hasegawa and successors;
- detector performance versus dissipation — Schwarzhans et al.;
- finite-frequency fluctuation-response bounds — Dechant, Liu/Gu, Zheng/Lu;
- optical sum rules or LDOS power-bandwidth limits — Shim et al. and related literature;
- general electromagnetic T-operator sum rules — Zhang, Monticone, Miller (2023);
- information theory + Maxwell-constrained structured photonic channels — Amaolo et al. (2026).

Amaolo et al. are especially close: they bound Shannon capacity of structured photonic channels at a **single frequency** and explicitly identify finite-band spectral-sum-rule and macroscopic-QED extensions as future work.

The surviving candidate novelty is specifically a finite-band **incident optical QFI -> physical capture -> finite-temperature electrical transducer** no-go/completion theorem.

Also note the rigor correction: do not assert a blanket scalar macroscopic extinction sum rule without deriving it from a rigorous scattering framework. Use the T-operator route for arbitrary scatterers; use the scalar TRK formula only in its microscopic electric-dipole regime.

---

# Immediate highest-priority task

Replace the fixed incident-vector assumption by a finite-band frequency-dependent incident-channel theorem with an explicit physical spatial resource.

Preferred routes:

1. finite-dimensional source/receiver channel basis with rank `M`;
2. rigorous space-bandwidth/Shannon-number bound for a finite design domain;
3. semidefinite optimization of frequency-dependent incident vectors against the T-operator oscillator measure;
4. footprint/volume-limited plane-wave channel family.

Then compose the resulting optical bound with WP3/WP4 and extend coherent-state QFI to general quantum temporal modes.

Issue #6 tracks this work.

---

# Mandatory adversarial checks

For every candidate theorem, test:

1. unit/reparameterization invariance;
2. output-gain invariance;
3. ideal photon counter/direct feedthrough;
4. source-bandwidth leakage;
5. detector replication/extensivity;
6. rare-fast states;
7. bounded total and edge EPR with divergent bare rates;
8. fixed optical detailed balance with divergent absolute coupling;
9. high-Q and vanishing mode volume;
10. large participating electron number;
11. propagating spatial phase across large detector area;
12. increasing spatial channel count;
13. slow-light and plasmonic singular limits;
14. active/gain media and pump/noise resources;
15. strong/ultrastrong coupling and non-Markovianity;
16. whether the proposed resource merely restates the bandwidth being bounded.

---

# Recordkeeping

After each substantive result:

- add/update a dedicated note;
- add a numbered research-log round when project direction changes;
- update this file;
- preserve failed conjectures and counterexamples.

Status labels:

- **PROVED** — complete derivation under explicit assumptions;
- **VERIFIED** — independently checked but not fully formalized;
- **CONJECTURE** — plausible and unproved;
- **COUNTEREXAMPLE** — explicit model violates a stated claim;
- **OPEN** — unresolved;
- **BLOCKED** — missing theoretical/source input;
- **REJECTED** — invalid/redundant.

## Current state — end of Round 3, 2026-08-19

The project has a strong Markov missing-coupling no-go theorem, a restricted internal thermokinetic completion theorem, a coherent incident-channel QFI capture lemma, and a rigorous fixed-spatial-mode finite-band T-operator optical capture theorem. The decisive remaining classical/semiclassical gate is the spatio-spectral incident-channel extension. A full quantum completion and final novelty claim remain open.