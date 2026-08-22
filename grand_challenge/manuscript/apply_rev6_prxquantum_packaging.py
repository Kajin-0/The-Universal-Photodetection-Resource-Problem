from pathlib import Path

src = Path("energy_survival_temporal_fisher_rev5.tex")
dst = Path("energy_survival_temporal_fisher_rev6_prxq.tex")

text = src.read_text(encoding="utf-8")

old = r"\documentclass[aps,pra,reprint,amsmath,amssymb,longbibliography]{revtex4-2}"
new = r"\documentclass[aps,prx,reprint,amsmath,amssymb,longbibliography]{revtex4-2}"

count = text.count(old)
assert count == 1, f"Expected exactly one PRA documentclass line, found {count}"
text = text.replace(old, new, 1)

# Rev6 is journal-target packaging only.  It must not alter the frozen Rev5
# scientific content or silently add incomplete administrative disclosures.
assert r"\documentclass[aps,prx,reprint" in text
assert r"\documentclass[aps,pra,reprint" not in text
assert r"\boxed{" not in text
assert "A Sharp Energy-Survival Law for Temporal Fisher Information" in text
assert r"\input{figure1_operational_architecture_body.tex}" in text

# Administrative submission metadata (author identity, affiliation, contact
# email, ORCID, funding, final Data Availability, and final APS AI disclosure)
# remains intentionally outside this generated source until supplied/verified
# by the human author.

dst.write_text(text, encoding="utf-8")
print(f"Wrote {dst}")
