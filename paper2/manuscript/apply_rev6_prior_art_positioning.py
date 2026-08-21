from pathlib import Path

SRC = Path(__file__).with_name("fisher_spectra_memory_photodetectors_rev5.tex")
DST = Path(__file__).with_name("fisher_spectra_memory_photodetectors_rev6.tex")

text = SRC.read_text(encoding="utf-8")

old = (
    "The inference literature also clarifies the observation model. Barat, Dautremer, and Trigano studied Type-I/II intensity inference while observing both the counting process and the idle/dead indicator process \\cite{BaratDautremerTrigano2006}; that is a richer record than the timestamp-only record analyzed in the Type-II theorems here. Jorgensen and Johnson derive LAN and Fisher rates for a broad nonparalyzable/gated event-detection class \\cite{JorgensenJohnson2026}. Our results should therefore be read as a complementary high-flux Type-II trajectory-information analysis, not as the first statistical treatment of dead time."
)
new = (
    "The inference literature also clarifies the observation model. Barat, Dautremer, and Trigano studied Type-I/II intensity inference while observing both the counting process and the idle/dead indicator process \\cite{BaratDautremerTrigano2006}; that is a richer record than the timestamp-only record analyzed in the Type-II theorems here. Jorgensen and Johnson derive LAN and Fisher rates for a broad nonparalyzable/gated event-detection class \\cite{JorgensenJohnson2026}. More broadly, identifiability and reconstruction from queue output processes are classical topics; Daley's review explicitly treats identifiability from queue outputs \\cite{Daley1976}. We therefore make no generic output-identifiability claim. The narrow result here is the Fisher singularity at the common Type-II count maximum for the timestamp-only experiment. Our results should be read as a complementary high-flux Type-II trajectory-information analysis, not as the first statistical treatment of dead time."
)

count = text.count(old)
if count != 1:
    raise RuntimeError(f"Expected one prior-art positioning target, found {count}")
text = text.replace(old, new)

required = [
    r"\cite{Daley1976}",
    "We therefore make no generic output-identifiability claim.",
    r"\label{eq:volterraG}",
    r"\GDC=\Gcyc=\frac{r}{\lambda}I_D",
]
for token in required:
    if token not in text:
        raise RuntimeError(f"Required Rev6 invariant missing: {token}")

for forbidden in ["placeholder", "TODO", "TBD", "first paper", "The repository contains"]:
    if forbidden in text:
        raise RuntimeError(f"Drafting residue survived Rev6: {forbidden}")

DST.write_text(text, encoding="utf-8")
print(f"Wrote {DST.name}")
