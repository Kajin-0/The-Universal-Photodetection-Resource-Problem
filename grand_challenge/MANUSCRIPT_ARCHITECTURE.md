# Manuscript Architecture — Operational Energy-Survival Law for Temporal Information

**Created:** 2026-08-22

**Scientific checkpoint:** WP24 integrated hostile review PASS

**Status:** architecture for a new standalone foundational manuscript. This is not Paper 1 or Paper 2.

---

# 1. Working title

Preferred:

> **A Sharp Energy-Survival Law for Temporal Fisher Information**

Strong alternative:

> **Energy-Survival Bounds on Temporal Information Transfer from Random Quantum Events**

Photodetection-forward alternative:

> **A Quantum Energy-Survival Bound on Temporal Information Transfer in Photodetection**

Avoid `universal` in the title. The theorem is broad within the random-time encoding class but WP14 gives an explicit counterexample to arbitrary waveform-state synthesis under baseline-energy-only accounting.

---

# 2. One-sentence thesis

> When temporal information is encoded in the probability distribution of the random translation time of a fixed semibounded-energy excitation, no physical measurement—even an arbitrary entangled collective measurement across independent events—can retain more Fisher information in temporal harmonic `nu` than the excitation's probability of carrying at least energy `hbar nu` above its participating lower edge.

Operational continuum theorem:

`boxed: R(nu) <= P(Omega>=nu)`.

Immediate corollaries:

`boxed: int_R R(nu)dnu <= 2 Ebar^+/hbar`,

`boxed: Ebar^+ >= hbar nu R(nu) = h f R(2pi f)`.

For guaranteed retention `q0` at ordinary frequency `B`:

`boxed: Ebar^+ >= h B q0`.

The exponential-energy / Cauchy-time family attains the bound exactly.

---

# 3. What the paper should claim

## Primary claim

For periodic random-time encoding, with total-generator sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

For any finite number `N` of independently encoded copies and any joint POVM,

`boxed: Tr F_N^(k) <= N T_k`.

Thus

`boxed: R_N(k):=Tr F_N^(k)/N <= T_k`.

## Stronger support-sensitive form

Let `V_k` be the partial shift between occupied sector pairs separated by `k`, with

`P_dom,k=V_k^dagger V_k`,

`P_ran,k=V_k V_k^dagger`.

Define

`D_k=Tr(rho0 P_dom,k)`,

`U_k=Tr(rho0 P_ran,k)`.

Then

`boxed: R_N(k) <= min(D_k,U_k) <= T_k`.

This should be Theorem 1 in its most general discrete form, with the energy-tail version displayed as the physically transparent corollary.

## All-mode mean-energy theorem

`boxed: sum_(k>=1) R_N(k) <= nbar`.

This follows from

`sum_(k>=1)T_k=nbar`.

## Continuum survival theorem

For excitation-frequency spectral probability measure `mu`,

`boxed: R(nu)<=S_mu(nu):=mu([nu,infinity))`.

## Continuum area and pointwise Planck laws

`boxed: int_0^infinity R(nu)dnu<=omega_bar`,

`boxed: int_R R(nu)dnu<=2Ebar^+/hbar`,

`boxed: Ebar^+>=hbar nu R(nu)`.

## Sharpness

Geometric sectors

`q_n=(1-r)r^n`

with canonical phase POVM give

`R(k)=r^k=T_k`

for every `k` simultaneously.

The exact lower-bin continuum limit is

`mu(domega)=beta exp(-beta omega)domega`,

`R(nu)=exp(-beta|nu|)=S_mu(|nu|)`.

---

# 4. What the paper must NOT claim

Do not claim:

1. first `U(1)` harmonic/modes-of-asymmetry decomposition;
2. first result that weighted random phase/time twirling multiplies gap modes by Fourier coefficients;
3. first canonical phase measurement or phase Fourier-moment analysis;
4. first photon-number/energy-constrained phase estimation bound;
5. first arbitrary-measurement Fisher/QFI/Holevo bound;
6. first random-unitary probability estimation theory;
7. first use of time-translation asymmetry as a resource;
8. new Hardy--Hilbert, Mellin, rearrangement, or Beta/Gamma constant;
9. a theorem for arbitrary coherent waveform synthesis;
10. a theorem for every source that merely exhibits Poisson photocount statistics;
11. a universal thermodynamic cost law;
12. a universal bound on deterministic time-shift QFI at fixed mean energy.

Especially cite Marvian--Spekkens for weighted `U(1)` twirling and energy-gap modes.

---

# 5. Proposed abstract logic

The abstract should contain exactly five moves.

1. **Problem:** temporal bandwidth is usually discussed through response functions, while ultimate information transfer depends on the full source-to-record statistical experiment.
2. **Source class:** temporal structure is encoded in the probability distribution of the random translation time of a fixed semibounded-energy excitation.
3. **Main theorem:** arbitrary finite-copy collective measurement obeys `R(nu)<=P(Omega>=nu)`.
4. **Consequences/sharpness:** `int R<=2E/hbar`, `E>=hfR`, exact exponential/Cauchy saturation, and compound-Poisson/bosonic-field inheritance.
5. **Boundary:** the theorem does not apply to arbitrary parameter-dependent waveform synthesis; a coherent-sideband construction shows why an encoding/control resource is then necessary.

Do not lead the abstract with the separately optimized `pi E/hbar` SLD-QFI envelope.

---

# 6. Suggested manuscript structure

## I. Introduction — temporal information needs a resource law

Purpose:

- motivate temporal information transfer rather than conventional amplitude bandwidth;
- state the tension created by ideal point-event models with arbitrarily large temporal information bandwidth;
- introduce the question: what source resource must be present for an actual detector to retain temporal Fourier information?

Do not spend pages re-explaining Paper 2. One paragraph is sufficient:

- classical autonomous detectors admit temporal Fisher spectra;
- ideal event timing can exhibit nondecaying high-frequency information;
- the present paper asks what quantum source structure permits such temporal information in the first place.

Then immediately state the new random-time source experiment and preview the survival theorem.

### Introduction claim ladder

Safe language:

- `We derive...`
- `For the random-time encoding class considered here...`
- `The resulting bound is independent of the downstream detector architecture...`
- `To our knowledge, we have not found the following Fisher-information tail law in prior work...`

Avoid:

- `first universal quantum speed limit for photodetectors`;
- `fundamental limit on all temporal measurements`;
- `new modes-of-asymmetry theory`.

---

## II. Random-time encoding as a quantum statistical experiment

### A. Periodic model

Define period `T`, `omega0=2pi/T`, semibounded generator

`H=E_* I+hbar omega0 sum_n nP_n`.

For fixed state `sigma` and random event time `t`,

`rho_epsilon=int p_epsilon(t)U_t sigma U_t^dagger dt`.

For one harmonic `k`,

`p_epsilon(t)=(1/T)[1+epsilon_c cos(komega0t)+epsilon_s sin(komega0t)]`.

Record the classical input Fisher block:

`F_in^(k)=(1/2)I_2` per event,

so its trace is `1`.

This normalization must be explicit before any source-normalized retention is defined.

### B. Relation to established weighted twirling

State explicitly that weighted `U(1)` twirling and gap-mode decomposition are established. Cite Marvian--Spekkens and write schematically

`rho_out^(k)=p_(-k) rho_in^(k)`.

Explain the distinction:

- prior theory describes harmonic structure/asymmetry;
- this paper asks how much **classical Fisher information about a perturbation of the mixing distribution** any measurement can recover.

### C. Purified sector representation

For a pure/purified excitation,

`rho0=sum_n q_n |phi_n><phi_n|`.

Define the complex tangent

`A_k=sum_n sqrt(q_nq_(n+k))|phi_(n+k)><phi_n|`.

For gaps, define the paired partial shift

`V_k=sum_(n:q_nq_(n+k)>0)|phi_(n+k)><phi_n|`.

Then

`A_k=rho0^(1/2)V_k rho0^(1/2)`.

This factorization is the algebraic engine of the paper.

---

## III. Main theorem: finite-copy operational energy-tail bound

### Theorem 1 — collective temporal-harmonic Fisher bound

State the fully support-aware version:

For every finite `N` and every POVM on `N` independent encoded copies,

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`.

### Proof

Keep main-text proof short and transparent.

For POVM outcome `M_y`, define

`p_y=Tr(rho M_y)`,

`z_y=Tr(A_k M_y)`.

Then

`partial_c p_y=Re z_y`,

`partial_s p_y=-Im z_y`,

so the Fisher trace contribution is

`|z_y|^2/p_y`.

With

`A_k=sqrt(rho)V_ksqrt(rho)`,

Hilbert--Schmidt Cauchy--Schwarz gives

`|z_y|^2/p_y <= Tr[M_y rho P_ran,k]`.

Sum outcomes.

For `N` copies use

`B_k^(N)=sum_j V_k^(j)`

and

`A_k^(N)=sqrt(rho_N) B_k^(N) sqrt(rho_N)`.

Cross terms vanish because

`Tr(rho V_k)=0`.

This yields `N U_k`; repeat with `A_k^dagger` for `N D_k`.

The proof should fit roughly one journal page.

### Corollary 1 — energy-tail form

`R_N(k)<=T_k=P(N_energy>=k)`.

### Corollary 2 — mean-generator sum rule

`sum_(k>=1)R_N(k)<=nbar`.

This is the first major physical punchline.

---

## IV. Continuum energy-survival theorem

### A. Exact periodic approximation

Let `mu` be a probability measure on `[0,infinity)` with finite first moment.

Define

`q_n^(delta)=mu([n delta,(n+1)delta))`.

Then exactly

`T_k^(delta)=mu([kdelta,infinity))`.

The discretized mean satisfies

`omega_bar_delta=delta sum_n n q_n^(delta)<=omega_bar`,

and tends to `omega_bar`.

### B. Theorem 2 — continuum survival bound

For any controlled modewise detector limit,

`R(nu)<=mu([nu,infinity))`.

State limsup version if no pointwise limit exists.

### C. Corollaries

Area:

`int_0^infinity R<=omega_bar`.

Two-sided:

`int_R R<=2Ebar^+/hbar`.

Pointwise:

`Ebar^+>=hbar nu R(nu)`.

Ordinary frequency:

`Ebar^+>=h f R(2pi f)`.

Flat band:

`Ebar^+>=hBq0`.

Emphasize that the **pointwise** statement is stronger conceptually than deriving the same coefficient only by integrating a flat band.

---

## V. Equality and extremal source family

### A. Geometric periodic state

`q_n=(1-r)r^n`.

Show

`T_k=r^k`.

For canonical phase POVM,

`F_cc=F_ss=r^k/2`,

`R(k)=r^k`.

Thus one simple one-copy measurement saturates **every harmonic simultaneously**.

### B. Continuum exponential spectrum

Take `r=exp(-beta delta)`.

Then

`mu(domega)=beta exp(-beta omega)domega`,

`R(nu)=exp(-beta|nu|)`.

### C. Cauchy timestamp

With `beta=2a`, canonical covariant time measurement yields

`f_a(t)=a/[pi(t^2+a^2)]`,

whose characteristic-function Fisher retention is

`R(nu)=exp(-2a|nu|)`.

This connects the abstract energy-tail theorem directly to a recognizable timing distribution.

---

## VI. From quantum events to photodetection

### A. Compound-Poisson event register

Define

`Sigma_epsilon=directsum_N p_mu(N)rho_epsilon^tensor N`.

For nonzero harmonics the Poisson weights are parameter independent.

Reveal `N`:

`Tr F<=sum_N p_mu(N) N T_k=mu T_k`.

Latent Poisson input Fisher trace is `mu`.

Hence

`R_Poisson(k)<=T_k`.

### B. Physical field formation

Let

`Gamma: event register -> physical Fock field + auxiliaries`

be the fixed CPTP source/emission map.

For final POVM `M`, define pullback

`M_tilde=Gamma^*(M)`.

Then the exact final probability law is already a POVM experiment on the event register.

Therefore wavepacket overlap, bosonic interference, propagation, coherent detector memory, and arbitrary final quantum measurement cannot increase the source-normalized retention beyond `T_k`.

### C. Scope sentence that must appear in main text

> Poisson photocount statistics alone do not imply this source model; the theorem assumes an independent quantum-marked event representation before the parameter-independent source-to-field channel.

This protects the coherent-state boundary.

---

## VII. Separately optimized quantum Fisher envelope

This section should be short and explicitly secondary.

For pure excitation sector populations,

`G_Q(k)=2 sum_n q_nq_(n+k)/(q_n+q_(n+k))`.

Then

`sum_(k>=1)G_Q(k)<=2nbar`,

and in the continuum

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

Explain:

- each mode/quadrature is optimized independently at the SLD level;
- one common physical detector instead obeys the survival theorem;
- therefore the larger QFI coefficient is not a broadband detector resource advantage;
- the `pi/4` analytic constant is Hardy--Hilbert prior art.

Avoid overinterpreting the exact numerical `pi/2` ratio as a universal incompatibility measure beyond this setup.

---

## VIII. Why the theorem cannot be extended to arbitrary waveform synthesis

Present WP14 as a concise counterexample.

A coherent carrier can acquire an arbitrarily high-frequency infinitesimal sideband whose state tangent is first order in modulation amplitude while the added mean energy is second order.

Therefore no theorem of the form

`baseline mean energy -> arbitrary waveform Fisher bandwidth`

can hold without counting an encoding/control/action resource.

This section is important: it turns a limitation into a precise theorem boundary rather than a caveat buried in Discussion.

---

## IX. Discussion

Core physical interpretation:

> To retain information about a temporal harmonic at angular frequency `nu`, a random-time excitation must place corresponding probability weight at least `hbar nu` above its participating lower energy edge.

This is stronger than saying merely that fast timing requires energy uncertainty. It identifies a **survival probability** of the generator spectrum as the directly relevant resource for operational Fisher transfer.

Discuss:

- why the result is source-to-record and detector architecture independent within its source class;
- distinction from conventional response bandwidth;
- distinction from deterministic time-shift metrology;
- relation to idealized delta-time events and high-frequency plateaus;
- why exact exponential/Cauchy saturation matters;
- possible extensions to correlated/non-Poisson quantum event processes.

Do not speculate about universal thermodynamics unless clearly marked future work.

---

# 7. Recommended appendices

## Appendix A — general mixed state and purification

Formalize sector probabilities for mixed states and the purification dominance argument.

## Appendix B — infinite/countable sector support and support gaps

Prove trace-class/boundedness statements and paired partial-shift identities.

## Appendix C — continuum periodic approximation

Full measure-theoretic statement from WP22, including atoms and weak limits.

## Appendix D — compound-Poisson and CPTP pullback

Formal event-register construction and final-field POVM pullback from WP23.

## Appendix E — SLD-QFI envelope

Derive the harmonic-mean formula and quote/prove the discrete `2nbar` bound. Put the continuum `pi E/hbar` proof here or in Supplemental Material, with explicit Hardy--Hilbert attribution.

## Appendix F — arbitrary waveform no-go

Full coherent-sideband construction from WP14.

## Appendix G — prior-art map

Optional but useful during drafting; may later collapse into main-text citations plus a short supplement table.

---

# 8. Figure plan

Keep figures conceptually simple and theorem-driven.

## Figure 1 — source-to-record theorem architecture

Left to right:

`random time distribution p(t)`

`-> fixed semibounded excitation U_t sigma U_t^dagger`

`-> physical source-to-field CPTP channel`

`-> arbitrary detector/coherent memory`

`-> record Y`.

Above the chain show

`R(nu)<=P(Omega>=nu)`.

This should make the theorem scope immediately obvious.

## Figure 2 — survival-function bound and exact saturation

Plot excitation spectral density `q(omega)` and its survival `S(nu)` for exponential `q`.

On a second aligned panel or overlay, plot allowed retention `R(nu)` and equality `R=S`.

This is the most important quantitative figure.

## Figure 3 — operational law versus separately optimized QFI envelope

Show schematically:

- operational area ceiling: `2E/hbar`;
- separately optimized SLD-QFI area ceiling: `pi E/hbar`;
- single equality family saturating the operational law.

Do not make this figure imply that every state achieves a fixed `pi/2` incompatibility ratio.

A fourth figure is probably unnecessary unless the Poisson-to-field architecture is too dense for Fig. 1.

---

# 9. Table plan

One compact scope/prior-art table may be useful.

Columns:

- object/result;
- established predecessor;
- role in this manuscript.

Rows:

- `U(1)` gap modes / weighted twirl — Marvian--Spekkens — starting formalism;
- canonical phase POVM — established — equality construction;
- phase estimation under number constraints — established — neighboring metrology;
- arbitrary collective FI/Holevo bounds — established — neighboring statistics;
- Hardy--Hilbert best constant — established — supplemental QFI envelope;
- operational Fisher tail `R(k)<=T_k` — no exact predecessor located — primary theorem.

This table is for claim discipline, not to imply priority certification.

---

# 10. Recommended claim ordering in title/abstract/conclusion

1. `energy-survival law`;
2. `arbitrary collective measurement`;
3. `sharp exact equality family`;
4. `source-to-record compound-Poisson/photodetection embedding`;
5. `pointwise Planck-scale consequence`;
6. `secondary SLD-QFI envelope`;
7. `arbitrary waveform no-go`.

Do not reverse this ordering by leading with the `pi` coefficient.

---

# 11. Candidate theorem numbering

- **Theorem 1:** finite-copy operational paired-support/tail bound.
- **Corollary 1:** all-positive-mode mean-excitation sum rule.
- **Theorem 2:** continuum survival-function theorem.
- **Corollary 2:** two-sided area and pointwise `h f` energy law.
- **Proposition 1:** geometric/canonical-phase exact equality.
- **Theorem 3:** compound-Poisson source-to-field inheritance.
- **Proposition 2:** separately optimized SLD-QFI harmonic formula and envelope.
- **Proposition 3 / No-go:** baseline energy cannot bound arbitrary coherent waveform synthesis.

This hierarchy makes the genuinely operational theorem the center of gravity.

---

# 12. Technical red-team checklist before Rev1

A Rev1 manuscript should not be declared complete until all of the following are checked line by line:

1. cosine/sine derivative normalization and input FI trace `=1` per event;
2. all `1/2`, `2`, `pi`, `h`, and `hbar` conversions;
3. zero-probability POVM outcomes and finite-FI convention;
4. support-gap partial-isometry definition;
5. mixed-state purification inequality direction;
6. N-copy cross-term cancellation;
7. tail-sum identity;
8. continuum closed-tail convention at atoms;
9. no illegal normalized uniform twirl on noncompact `R`;
10. compound-Poisson event-number side-information direction;
11. CPTP pullback direction and parameter-independence assumption;
12. exact equality calculation for canonical phase POVM;
13. distinction between lower spectral edge and arbitrary carrier-energy subtraction;
14. no extension to direct coherent waveform synthesis;
15. explicit credit to Marvian--Spekkens weighted twirling;
16. explicit credit to canonical phase/number-constrained phase literature;
17. no novelty claim for Hardy--Hilbert `pi/4` constant;
18. no assertion that finite literature search certifies priority.

---

# 13. Manuscript readiness assessment

**Scientific readiness:** high enough to draft Rev1.

Reasons:

- core operational theorem has a short finite-copy proof;
- arbitrary collective measurements are included;
- support gaps are repaired;
- continuum statement is explicit for general spectral measures;
- exact equality family exists;
- independent-event photodetection embedding is rigorous at the channel/statistical-experiment level;
- principal overbroad source class has an explicit no-go boundary;
- major adjacent prior art is identified and can be credited conservatively.

**Remaining risk:** historical priority. This should be handled by continued targeted literature checking during drafting rather than by indefinitely postponing the manuscript.

## Next action

Create the Rev1 LaTeX manuscript skeleton from this architecture, with theorem statements and proof skeletons already inserted, then perform a manuscript-level hostile review before polishing or journal formatting.