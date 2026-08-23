#!/usr/bin/env python3
"""Generate the PRX Quantum prose-targeted manuscript from the audited M2R1 body.

Permitted transformations:
1. replace the PRA-tagged review document class by a journal-neutral APS preprint class;
2. replace the abstract by sections/prxq_abstract_r1.tex;
3. insert sections/prxq_introduction_r1.tex immediately after \maketitle;
4. insert the APS-required substantive AI disclosure and Data Availability Statement
   immediately before the bibliography.

The theorem body is otherwise byte-for-byte inherited from M2R1. This keeps
publication-style and submission-policy text separate from the audited source.
"""

from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "autonomous_temporal_resource_law_m2r1.tex"
ABSTRACT = HERE / "sections" / "prxq_abstract_r1.tex"
INTRO = HERE / "sections" / "prxq_introduction_r1.tex"
AI_DISCLOSURE = HERE / "sections" / "ai_use_disclosure_r1.tex"
DATA_AVAILABILITY = HERE / "sections" / "data_availability_r1.tex"
OUT = HERE / "autonomous_temporal_resource_law_prxq_r1.tex"

BASE_CLASS = r"\documentclass[aps,pra,preprint,nofootinbib]{revtex4-2}"
PRXQ_REVIEW_CLASS = r"\documentclass[aps,preprint,nofootinbib,longbibliography]{revtex4-2}"


def main() -> None:
    base = BASE.read_text(encoding="utf-8")
    abstract = ABSTRACT.read_text(encoding="utf-8").strip()

    for required in (ABSTRACT, INTRO, AI_DISCLOSURE, DATA_AVAILABILITY):
        if not required.exists():
            raise FileNotFoundError(required)

    if base.count(BASE_CLASS) != 1:
        raise RuntimeError("audited base document class changed unexpectedly")
    updated = base.replace(BASE_CLASS, PRXQ_REVIEW_CLASS, 1)

    pattern = re.compile(
        r"\\begin\{abstract\}.*?\\end\{abstract\}",
        flags=re.DOTALL,
    )
    replacement = "\\begin{abstract}\n" + abstract + "\n\\end{abstract}"
    updated, count = pattern.subn(lambda _match: replacement, updated, count=1)
    if count != 1:
        raise RuntimeError(f"expected exactly one abstract block, replaced {count}")

    maketitle = "\\maketitle\n"
    intro_insertion = maketitle + "\n\\input{sections/prxq_introduction_r1.tex}\n"
    if updated.count(maketitle) != 1:
        raise RuntimeError("expected exactly one \\maketitle marker")
    updated = updated.replace(maketitle, intro_insertion, 1)

    bib_marker = "\\bibliographystyle{apsrev4-2}\n\\bibliography{references}"
    disclosure_block = (
        "\\section*{AI Use Disclosure}\n"
        "\\input{sections/ai_use_disclosure_r1.tex}\n\n"
        "\\section*{Data Availability}\n"
        "\\input{sections/data_availability_r1.tex}\n\n"
        + bib_marker
    )
    if updated.count(bib_marker) != 1:
        raise RuntimeError("expected exactly one bibliography marker")
    updated = updated.replace(bib_marker, disclosure_block, 1)

    if "\\section{Introduction}" in updated:
        raise RuntimeError("base manuscript unexpectedly contains a literal Introduction section")

    OUT.write_text(updated, encoding="utf-8")
    print(f"generated {OUT.name} from {BASE.name}")


if __name__ == "__main__":
    main()
