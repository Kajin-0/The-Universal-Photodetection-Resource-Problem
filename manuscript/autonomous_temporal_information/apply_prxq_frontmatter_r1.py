#!/usr/bin/env python3
"""Generate the PRX Quantum prose-targeted manuscript from the audited M2R1 body.

Only two transformations are permitted:
1. replace the abstract by sections/prxq_abstract_r1.tex;
2. insert sections/prxq_introduction_r1.tex immediately after \maketitle.

The theorem body is otherwise byte-for-byte inherited from M2R1. This keeps
publication-style prose changes separate from the audited mathematical source.
"""

from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "autonomous_temporal_resource_law_m2r1.tex"
ABSTRACT = HERE / "sections" / "prxq_abstract_r1.tex"
INTRO = HERE / "sections" / "prxq_introduction_r1.tex"
OUT = HERE / "autonomous_temporal_resource_law_prxq_r1.tex"


def main() -> None:
    base = BASE.read_text(encoding="utf-8")
    abstract = ABSTRACT.read_text(encoding="utf-8").strip()

    pattern = re.compile(
        r"\\begin\{abstract\}.*?\\end\{abstract\}",
        flags=re.DOTALL,
    )
    replacement = "\\begin{abstract}\n" + abstract + "\n\\end{abstract}"
    updated, count = pattern.subn(lambda _match: replacement, base, count=1)
    if count != 1:
        raise RuntimeError(f"expected exactly one abstract block, replaced {count}")

    marker = "\\maketitle\n"
    insertion = marker + "\n\\input{sections/prxq_introduction_r1.tex}\n"
    if updated.count(marker) != 1:
        raise RuntimeError("expected exactly one \\maketitle marker")
    updated = updated.replace(marker, insertion, 1)

    # The audited base deliberately has no dedicated Introduction section.
    if "\\section{Introduction}" in updated:
        raise RuntimeError("base manuscript unexpectedly contains a literal Introduction section")

    OUT.write_text(updated, encoding="utf-8")
    print(f"generated {OUT.name} from {BASE.name}")


if __name__ == "__main__":
    main()
