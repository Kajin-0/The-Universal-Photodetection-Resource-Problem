# APS AI-Use Disclosure Draft — Rev8

**Policy checked:** 2026-08-20

APS currently requires authors to disclose substantive AI use in a submitted paper. The policy explicitly includes scientific reasoning or interpretation, derivations/calculations, literature synthesis beyond routine organization, and drafting or revising scientific claims or explanations.

Current policy:
https://journals.aps.org/authors/appropriate-use-ai-tools

## Why a disclosure is required for this project

AI assistance in this project has been substantive rather than limited to grammar/polish. It has included theorem exploration, derivation and counterexample work, literature synthesis, claim-boundary analysis, adversarial review, source drafting, and mechanical consistency checks.

Therefore omitting an AI disclosure would not match the current APS policy.

## Draft acknowledgment language

The following is a conservative draft and **must be reviewed by the submitting author for factual accuracy before insertion**:

> OpenAI ChatGPT (GPT-5.6 Sol) was used as an AI-assisted research and writing tool for literature synthesis, exploration and checking of mathematical derivations, adversarial claim review, and manuscript drafting and revision. The author directed the research questions and scope, reviewed and revised the resulting material, and retained responsibility for the mathematical claims, citations, interpretation, and final manuscript.

## Verification-detail issue

APS asks authors to state not only how AI assisted, but also how the authors directed and **verified** the AI output.

The repository documents substantial mechanical and mathematical validation, including:

- explicit derivations and counterexamples recorded in numbered work packages;
- assertion-based manuscript transformations;
- independent proof-hardening passes;
- repeated claim/citation audits;
- a full Rev8 LaTeX+bibliography+cross-reference validation from the independently verified Rev7 artifact;
- generated-source SHA-256 checks against recorded expected hashes and visual inspection of the affected pages.

However, these records do not by themselves establish every action personally performed by the human author. Before submission, the submitting author should make the acknowledgment precisely truthful about their own verification process.

If accurate, a stronger final sentence could be:

> The author independently reviewed the derivations and literature claims, checked the cited sources and theorem assumptions, and approved all material retained in the final manuscript.

Do **not** use that stronger sentence unless it accurately describes the author's actual verification.

## Placement

APS guidance says substantive AI uses not already described as research methods should normally be disclosed in the **Acknowledgments**. If an AI tool was itself used as part of the research method, the relevant use may also need description where methods are discussed.

The current recommendation is to add the finalized disclosure as an unnumbered acknowledgment immediately before the Data Availability Statement / bibliography during the submission-compliance pass.
