# Research Roadmap

**Updated:** 2026-08-21

`main` is the repository landing/index branch.

**Active scientific branch:** `agent/temporal-information-resource-law`

## Program split

- **Paper 1 / Rev11:** frozen; submission metadata/compliance only.
- **Paper 2 / Rev7:** frozen preferred science draft.
- **Grand Challenge:** active high-risk/high-ceiling theoretical program.

The Grand Challenge **theorem stack is through WP15**. The **latest checkpoint is WP16**, a deep priority audit.

## Active objective

Find sharp, physically meaningful quantum resource constraints on temporal Fisher-information transfer, while explicitly proving no-go results and prior-art boundaries for overbroad claims.

## Current strongest result — WP15

For normalized positive excitation-frequency density `q(omega)` with finite first moment `omega_bar`, random-time mode retention obeys

`G_Q(nu)=2 int_0^infinity q(omega)q(omega+nu)/[q(omega)+q(omega+nu)]domega`, `nu>0`,

with even extension, and

`boxed: int_0^infinity G_Q(nu)dnu <= (pi/2) omega_bar`,

or

`boxed: int_R G_Q(nu)dnu <= pi E_bar^+/hbar`.

A guaranteed flat band implies

`boxed: E_bar^+ >= (2/pi) h B q0`.

The coefficient is sharp as a supremum.

## WP16 — priority correction

The sharp WP15 operator norm

`||T||=pi/4`, for `L(s,t)=2st/(s+t)^3`,

is a direct specialization of established parameterized Hardy–Hilbert integral inequalities. Setting `lambda=3`, `f(x)=xr(x)`, `g(y)=yr(y)` yields `B(3/2,3/2)=pi/8`, and the factor `2` in the WP15 kernel yields `pi/4`.

Therefore **the operator constant, Mellin/Hilbert inequality, and Beta/Gamma evaluation are prior art and are not mathematical novelty claims**.

The unresolved priority question is now narrower: has quantum estimation theory already derived the Fisher geometry and mean-generator mode budget for Fourier perturbations of a random `U(1)` translation distribution?

No exact predecessor has yet been located for

`G_Q(k)=2 sum_n q_n q_{n+k}/(q_n+q_{n+k})`

or

`sum_{k>=1}G_Q(k)<=2 nbar`.

This absence is **not priority certification**.

## Supporting theorem chain

### WP10/WP11 — discrete random-time mode budget

`G_Q(k)=2 sum_n q_n q_{n+k}/(q_n+q_{n+k})`,

with

`sum_{k>=1}G_Q(k)<=2 nbar`,

`sum_{k!=0}G_Q(k)<=4 nbar`.

### WP06-WP08 — covariant timestamp subclass

`int_R G_timestamp(nu)dnu <= 2 E_det^+/hbar`,

and therefore

`E_det^+ >= h B q`.

The bound survives arbitrary downstream parameter-independent classical detector memory.

### WP13 — second-quantized/Poisson embedding

Fixed-photon-number multiphoton/entangled/multimode excitations are included through total-energy sectors. Independent quantum-marked Poisson events inherit source-normalized bounds by additivity and downstream QFI monotonicity.

### WP14 — arbitrary-waveform no-go

Baseline mean energy does not bound arbitrary parameter-dependent coherent waveform synthesis. A broader theorem needs an encoding/control/action resource.

## Closed or deprioritized directions

- entropy-production-only universal law — rejected;
- generic frequency-domain thermodynamic FI/response law — already covered by neighboring literature;
- generic quantum waveform-QFI spectrum — prior art;
- detector work cost determined by `G` alone — underdetermined;
- generic classical-vs-quantum accessibility gap — insufficiently distinctive by itself;
- mathematical novelty of the WP15 `pi/4` operator constant — explicitly preempted by Hardy–Hilbert theory.

## Manuscript gate

Do **not** draft the grand-challenge paper yet.

Required before drafting:

1. **Quantum priority Gate 1A:** search estimation of Fourier coefficients/mixing weights of `U(1)` random-unitary channels and probability measures on compact groups.
2. **Analysis provenance Gate 1B:** determine whether the harmonic-mean density inequality itself appears explicitly; its sharp operator constant is already classical.
3. **Operational attainability audit:** determine whether one measurement family can approach the integrated `pi` coefficient; different mode SLDs may be incompatible.
4. **Physical source mapping:** strengthen the quantum-marked Poisson/event model into realistic incoherent optical-field language.
5. Preserve the WP14 scope boundary and avoid implying a theorem for arbitrary waveform state engineering.

If those gates survive, the candidate manuscript would center on the random-distribution mode-estimation problem, discrete `2 nbar` budget, continuum Planck-scale area law with proper Hardy–Hilbert attribution, inverse bandwidth-energy inequality, photodetection embedding, and explicit coherent-waveform no-go.

## Immediate work order

1. Search group-distribution estimation, random-unitary mixing-weight estimation, phase-noise Fourier/characteristic-coefficient inference, and nonparametric dephasing-channel estimation.
2. Search exact classical provenance of the harmonic-mean density-functional statement.
3. Analyze joint/collective measurements for integrated-area attainability.
4. Harden the quantum optical source embedding.
5. Decide on manuscript formation only afterward.

## Documentation policy

Detailed derivations live on `agent/temporal-information-resource-law`, but `main` must always show the active branch and latest checkpoint. Any project-level theorem/gate change must update both the active branch state docs and these default-branch landing docs, including `PROBLEM.md` when needed to prevent stale routing.