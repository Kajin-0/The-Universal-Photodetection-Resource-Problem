#!/usr/bin/env python3
"""Generate the Physical Review Applied submission copy from frozen Rev7.

This script must not change theorem content.  It adds only submission-compliance
material that is safe before author metadata is supplied:

1. a non-rendered reminder that the APS substantive-AI disclosure must be
   finalized truthfully before submission;
2. the APS-compatible purely mathematical Data Availability statement.

The canonical Rev7 source remains untouched.
"""

from pathlib import Path

SRC = Path("event_resource_theorem_rev7.tex")
OUT = Path("event_resource_theorem_rev7_prapplied.tex")

source = SRC.read_text(encoding="utf-8")

# Assertions make accidental application to a different manuscript fail loudly.
assert "\\title{Temporal Information Transfer and Resource Bounds in Autonomous Photodetection Event Channels}" in source
assert "\\author{Anonymous}" in source
assert "\\affiliation{Anonymous}" in source
assert "\\input{section_waveform_operator_rev7}" in source
assert "\\input{section_operational_bandwidth_rev7}" in source
assert "\\input{appendix_rare_fast_counterexample_rev7}" in source
assert "\\section*{Data Availability}" not in source
assert "APS SUBMISSION TODO" not in source
assert source.count("\\appendix") == 1
assert source.count("\\bibliography{references}") == 1

compliance = r"""
% APS SUBMISSION TODO — REQUIRED BEFORE ACTUAL SUBMISSION:
% Add a truthful Acknowledgments disclosure of substantive AI use that states
% (i) the AI tool name/version, (ii) how it assisted, and (iii) how the HUMAN
% author directed and verified its output.  See
% submission/AI_DISCLOSURE_DRAFT_REV7.md.  This comment is intentionally not
% rendered because the human-verification wording has not yet been confirmed.

\section*{Data Availability}
This is a purely mathematical work and no data were created or analyzed in this study. All figures can be reproduced directly from the presented equations.

"""

submission = source.replace("\\appendix\n", compliance + "\\appendix\n", 1)

assert submission != source
assert submission.count("\\section*{Data Availability}") == 1
assert submission.count("APS SUBMISSION TODO") == 1
assert submission.count("\\appendix") == 1
assert submission.count("\\bibliography{references}") == 1

OUT.write_text(submission, encoding="utf-8")
print(f"wrote {OUT} ({len(submission)} chars)")
