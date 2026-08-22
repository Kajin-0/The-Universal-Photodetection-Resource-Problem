# Research Roadmap

**Updated:** 2026-08-21

`main` is the repository landing/index branch.

**Active scientific branch:** `agent/temporal-information-resource-law`

## Program split

- **Paper 1 / Rev11:** frozen; submission metadata/compliance only.
- **Paper 2 / Rev7:** frozen preferred science draft.
- **Grand Challenge:** active high-risk/high-ceiling theoretical program.

## Active objective

Find sharp, physically meaningful quantum resource constraints on temporal Fisher-information transfer, while explicitly proving no-go results for overbroad resource proposals.

## Current strongest result — WP15

For normalized positive excitation-frequency density `q(omega)` with finite first moment `omega_bar`, random-time mode retention obeys

`G_Q(nu)=2 int_0^infinity q(omega)q(omega+nu)/[q(omega)+q(omega+nu)]domega`, `nu>0`,

with even extension, and

`boxed: int_0^infinity G_Q(nu)dnu <= (pi/2) omega_bar`,

or

`boxed: int_R G_Q(nu)dnu <= pi E_bar^+/hbar`.

A guaranteed flat band implies

`boxed: E_bar^+ >= (2/pi) h B q0`.

The constant is sharp as a supremum. WP15 supplies the general finite-first-moment proof.

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
- generic classical-vs-quantum accessibility gap — insufficiently distinctive by itself.

## Manuscript gate

Do **not** draft the grand-challenge paper yet.

Required before drafting:

1. **Deep priority audit** for exact equivalents of WP10/WP12/WP15.
2. **Operational attainability audit** of the integrated `pi` coefficient under a single measurement family; different mode SLDs may be incompatible.
3. **Physical source mapping** from the quantum-marked Poisson/event model to realistic incoherent optical fields.
4. Preserve the WP14 scope boundary and avoid implying a theorem for arbitrary waveform state engineering.

If those gates survive, the candidate manuscript would center on the discrete mode budget, sharp continuum Planck-scale area law, inverse bandwidth-energy inequality, photodetection embedding, and explicit coherent-waveform no-go.

## Immediate work order

1. Search random-unitary/group-distribution estimation, phase-noise estimation, Rényi/time-observable inequalities, and harmonic-analysis literature for exact prior equivalents.
2. Analyze joint/collective measurements for integrated-area attainability.
3. Harden the quantum optical source embedding.
4. Decide on manuscript formation only afterward.

## Documentation policy

Detailed derivations live on `agent/temporal-information-resource-law`, but `main` must always show the active branch and latest checkpoint. Any project-level theorem/gate change must update both the active branch state docs and these default-branch landing docs.