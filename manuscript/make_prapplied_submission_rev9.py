#!/usr/bin/env python3
"""Generate the Physical Review Applied submission copy from Rev9."""
from pathlib import Path

SRC = Path("event_resource_theorem_rev9.tex")
OUT = Path("event_resource_theorem_rev9_prapplied.tex")

s = SRC.read_text(encoding="utf-8")
assert "\\author{Anonymous}" in s
assert "\\affiliation{Anonymous}" in s
assert "\\input{section_practical_grounding_rev9}" in s
assert "\\input{section_empirical_grounding_rev9}" in s
assert s.count("\\appendix") == 1
assert "\\section*{Data Availability}" not in s

compliance = r"""
% APS SUBMISSION TODO -- REQUIRED BEFORE ACTUAL SUBMISSION:
% Add a truthful Acknowledgments disclosure of substantive AI use that states
% (i) the AI tool name/version, (ii) how it assisted, and (iii) how the HUMAN
% author directed and verified its output. See submission/AI_DISCLOSURE_DRAFT_REV9.md.

\section*{Data Availability}
This is a purely mathematical work and no data were created or analyzed in this study. All figures can be reproduced directly from the presented equations.

"""

out = s.replace("\\appendix\n", compliance + "\\appendix\n", 1)
assert out.count("\\section*{Data Availability}") == 1
assert out.count("APS SUBMISSION TODO") == 1
OUT.write_text(out, encoding="utf-8")
print(f"wrote {OUT}")
