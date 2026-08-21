# Rev7 Submission Strategy

**Date checked:** 2026-08-20

Current manuscript:
`manuscript/event_resource_theorem_rev7.tex`

Title:
**Temporal Information Transfer and Resource Bounds in Autonomous Photodetection Event Channels**

## Recommendation

### Primary target: Physical Review Applied — Regular Article

This is the strongest first submission target.

Why the fit is unusually direct:

- Physical Review Applied explicitly covers **device physics**, **optics, optoelectronics, photonics, and photonic devices**, and quantum information science/technology.
- Its stated mission is to bridge engineering and physics and current/future technologies.
- Its acceptance criteria require fresh insight into applications-based physical phenomena, a significant contribution in a specific area, and an authoritative/substantive addition to the literature.
- Rev7 is theoretical but operationally device-facing: it replaces ambiguous speed summaries with an exact source-normalized temporal-information object and derives detector-ordering, equivalent-bandwidth, and minimum-resource results.
- A Regular Article has no formal length limit, which fits the theorem/no-go/thermodynamic stack better than a Letter.
- The manuscript is already in `revtex4-2` with the `prapplied` option.

Current journal sources:

- Scope / criteria: https://journals.aps.org/prapplied/about
- Author instructions: https://journals.aps.org/prapplied/authors

### Main editorial risk at Physical Review Applied

The manuscript is abstract and material-independent. An editor could decide that it is insufficiently tied to a concrete device technology despite its photodetector framing.

The submission package should therefore emphasize:

1. why conventional detector speed metrics are operationally non-equivalent;
2. why `G(omega)` is directly usable as a detector-comparison object;
3. the exact `B_FI` bandwidth and `4Bq` resource costs;
4. the serial stochastic-stage example as an architecture-level consequence;
5. that the framework applies across photodetector materials rather than being detached from device physics.

Do **not** weaken the manuscript by adding a material-specific case study solely to satisfy this concern unless the editor/referees explicitly request one.

---

## Fallback 1: Physical Review Research — Regular Article

Use if Physical Review Applied rejects primarily on fit/scope rather than correctness.

Advantages:

- explicitly welcomes fundamental and applied, theoretical and experimental work across all physics;
- acceptance criteria emphasize high-quality, significant, authoritative, substantive additions;
- the theorem stack fits comfortably as a general physics resource theory.

Disadvantage:

- Physical Review Research is fully open access and requires an APC after acceptance; Physical Review Applied is hybrid and does not require choosing open access.

Current sources:

- Scope / criteria: https://journals.aps.org/prresearch/about
- Author instructions: https://journals.aps.org/prresearch/authors

---

## Fallback 2: Physical Review A — Regular Article

PRA is plausible because its scope includes photonics, quantum measurement/estimation, fundamental concepts, and quantum information science.

Why it is secondary rather than primary:

- the present paper is deliberately classical/direct-detection and device-resource oriented;
- it does not center atomic/molecular physics, quantum optics, nonclassical states, or a quantum-information protocol;
- PRApplied's device-physics/photonics scope maps more directly to the manuscript's motivation and operational consequences.

Current sources:

- Scope / criteria: https://journals.aps.org/pra/about
- Author instructions: https://journals.aps.org/pra/authors

---

## Non-APS alternatives

### Optica

Scope is high-impact fundamental and applied optics/photonics. It is an ambitious alternative but likely has a substantially higher editorial impact threshold and is fully open access. The theorem stack is relevant, but Physical Review Applied is a more natural first venue for a long physics/device-resource paper.

Source:
https://opg.optica.org/optica/home.cfm

### Optics Express

Clearly within scope and explicitly publishes photodetector work. This is a technically plausible optics-specific fallback if APS placement fails, but it is not the preferred first target for this theorem package.

Source:
https://opg.optica.org/oe/home.cfm

---

# Physical Review Applied submission requirements relevant to Rev7

As checked 2026-08-20:

1. **Article type:** Regular Article; no formal length limit.
2. **Broad accessibility:** write for a broad applied-physics audience and avoid unnecessary specialized terminology.
3. **Novelty language:** APS specifically discourages dramatic priority language such as “new,” “novel,” or “the first.” The current conservative novelty posture should be retained.
4. **Cover letter:** should give context, summarize key findings, disclose relevant Physical Review submission history, and may provide recommended/excluded referees.
5. **100-word justification:** Research Articles and Letters require a compelling approximately/exactly 100-word suitability justification. A 100-word draft is stored in `submission/PRAPPLIED_100_WORD_JUSTIFICATION_REV7.txt`.
6. **Data Availability Statement:** required for all published articles. APS explicitly provides a purely mathematical-work option. Draft stored in `submission/DATA_AVAILABILITY_REV7.txt`.
7. **AI disclosure:** APS requires disclosure in the paper of substantive AI use, including scientific reasoning, derivations/calculations, literature synthesis, or drafting/revising scientific claims. Draft stored in `submission/AI_DISCLOSURE_DRAFT_REV7.md`; it must be made factually accurate about author verification before submission.
8. **References:** Physical Review Applied requires titles in published references and strongly encourages them at submission. This should be checked in the final `.bib` inventory.
9. **Initial files:** a PDF is sufficient to enter peer review, but LaTeX source is preferred and should be supplied because the source is already clean and reproducible.

Current policy sources:

- https://journals.aps.org/prapplied/authors
- https://journals.aps.org/authors/data-availability-statements
- https://journals.aps.org/authors/appropriate-use-ai-tools

---

# Submission posture

Recommended sequence:

1. **Physical Review Applied — Regular Article**
2. If rejected for journal fit, prefer an APS transfer to **Physical Review Research** if offered.
3. If the editorial feedback frames the paper as fundamental AMO/photonics information theory rather than applied device physics, consider **Physical Review A**.
4. If APS placement fails, reassess **Optica** versus **Optics Express** based on the actual editorial reports rather than rewriting preemptively.

Do not submit simultaneously to multiple journals.

---

# Remaining blockers before actual submission

The science is not blocked. Administrative items remain:

- replace `Anonymous` author and affiliation with truthful metadata;
- designate corresponding author and active email;
- supply/verify ORCID for the corresponding author (APS requires authenticated ORCID);
- finalize truthful AI-use disclosure;
- insert/confirm Data Availability Statement;
- review bibliography for reference titles;
- optionally provide recommended/excluded referees;
- confirm no relevant prior or concurrent submission history needs disclosure.

No additional foundational theorem work is currently required.
