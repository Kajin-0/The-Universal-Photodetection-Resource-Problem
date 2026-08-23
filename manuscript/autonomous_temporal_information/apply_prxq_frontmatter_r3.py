#!/usr/bin/env python3
"""Generate the PRX Quantum R3 manuscript from the audited M2R3 body."""
from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "autonomous_temporal_resource_law_m2r3.tex"
ABSTRACT = HERE / "sections" / "prxq_abstract_r3.tex"
INTRO = HERE / "sections" / "prxq_introduction_r3.tex"
FIGURE = HERE / "sections" / "two_regime_concept_figure_r2.tex"
AI_DISCLOSURE = HERE / "sections" / "ai_use_disclosure_r1.tex"
DATA_AVAILABILITY = HERE / "sections" / "data_availability_r1.tex"
OUT = HERE / "autonomous_temporal_resource_law_prxq_r3.tex"

BASE_CLASS = r"\documentclass[aps,pra,preprint,nofootinbib]{revtex4-2}"
PRXQ_REVIEW_CLASS = r"\documentclass[aps,preprint,nofootinbib,longbibliography]{revtex4-2}"


def main() -> None:
    for required in (BASE, ABSTRACT, INTRO, FIGURE, AI_DISCLOSURE, DATA_AVAILABILITY):
        if not required.exists():
            raise FileNotFoundError(required)

    updated = BASE.read_text(encoding="utf-8")
    abstract = ABSTRACT.read_text(encoding="utf-8").strip()

    if updated.count(BASE_CLASS) != 1:
        raise RuntimeError("audited base document class changed unexpectedly")
    updated = updated.replace(BASE_CLASS, PRXQ_REVIEW_CLASS, 1)

    pattern = re.compile(r"\\begin\{abstract\}.*?\\end\{abstract\}", flags=re.DOTALL)
    replacement = "\\begin{abstract}\n" + abstract + "\n\\end{abstract}"
    updated, count = pattern.subn(lambda _match: replacement, updated, count=1)
    if count != 1:
        raise RuntimeError(f"expected exactly one abstract block, replaced {count}")

    maketitle = "\\maketitle\n"
    front = (
        maketitle
        + "\n\\input{sections/prxq_introduction_r3.tex}\n"
        + "\n\\input{sections/two_regime_concept_figure_r2.tex}\n"
    )
    if updated.count(maketitle) != 1:
        raise RuntimeError("expected exactly one \\maketitle marker")
    updated = updated.replace(maketitle, front, 1)

    bib_marker = "\\bibliographystyle{apsrev4-2}\n\\bibliography{references}"
    disclosures = (
        "\\section*{AI Use Disclosure}\n"
        "\\input{sections/ai_use_disclosure_r1.tex}\n\n"
        "\\section*{Data Availability}\n"
        "\\input{sections/data_availability_r1.tex}\n\n"
        + bib_marker
    )
    if updated.count(bib_marker) != 1:
        raise RuntimeError("expected exactly one bibliography marker")
    updated = updated.replace(bib_marker, disclosures, 1)

    if "\\section{Introduction}" in updated:
        raise RuntimeError("base manuscript unexpectedly contains a literal Introduction section")

    # Keep PDF links visually neutral in the submission rendering.
    updated = updated.replace("\\usepackage{hyperref}", "\\usepackage{hyperref}\n\\hypersetup{hidelinks}", 1)

    OUT.write_text(updated, encoding="utf-8")
    print(f"generated {OUT.name} from {BASE.name}")


if __name__ == "__main__":
    main()
