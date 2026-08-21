from pathlib import Path

SRC = Path(__file__).with_name("fisher_spectra_memory_photodetectors_rev6.tex")
DST = Path(__file__).with_name("fisher_spectra_memory_photodetectors_rev7.tex")
text = SRC.read_text(encoding="utf-8")

replacements = [
    (
        "These results identify the complete detector trajectory channel, rather than a saturation curve or a few recovery moments, as the relevant object for temporal information transfer in photodetectors with memory.",
        "These results identify the full accessible detector trajectory channel, within the admitted classical Poisson intensity-tangent model, rather than a saturation curve or a few recovery moments, as the relevant object for temporal information transfer in photodetectors with memory.",
    ),
    (
        "The question here is narrower. Suppose the incident optical signal is a weak temporal perturbation of a stationary Poisson flux, and suppose the detector may contain arbitrary hidden memory, saturation, recovery, state-dependent capture, or nonlinear history dependence. What object completely describes the \\emph{local temporal Fisher information} retained by the complete accessible detector record? And which familiar scalar detector summaries are insufficient to determine it?",
        "The question here is narrower. Suppose the incident optical signal is a weak temporal perturbation of a stationary Poisson flux, and suppose the detector may contain arbitrary hidden memory, saturation, recovery, state-dependent capture, or nonlinear history dependence. Within this classical Poisson intensity-tangent model, what object describes all \\emph{local temporal Fisher information} retained by the complete accessible detector record? And which familiar scalar detector summaries are insufficient to determine it?",
    ),
    (
        "The result is a bounded temporal Fisher-retention spectrum $G(\\omega)$, even when no independent-event timing kernel exists. The statistical and harmonic-analysis ingredients are standard \\cite{Pollard2013,Kallenberg2021,Stein1970,Clark2026}; the role of the theorem is to provide one complete local waveform language for photodetectors with arbitrary autonomous memory.",
        "The result is a bounded temporal Fisher-retention spectrum $G(\\omega)$, even when no independent-event timing kernel exists. The statistical and harmonic-analysis ingredients are standard \\cite{Pollard2013,Kallenberg2021,Stein1970,Clark2026}; the role of the theorem is to provide a complete local weak-intensity-waveform language within the admitted classical Poisson source model for photodetectors with arbitrary autonomous memory.",
    ),
    (
        "The resulting thesis is simple: a detector saturation curve is not an information-transfer law. Temporal information belongs to the complete trajectory channel.",
        "The resulting thesis is simple: a detector saturation curve is not an information-transfer law. Within the declared source and record model, temporal information belongs to the full accessible trajectory channel.",
    ),
    (
        "The structural reason is that local information belongs to the complete trajectory channel. In the general autonomous theorem this channel is summarized locally by the Fisher operator $A_K$ or its spectral multiplier $G(\\omega)$.",
        "The structural reason is that, within the admitted classical Poisson intensity-tangent model, local information belongs to the full accessible trajectory channel. In the general autonomous theorem this channel is summarized locally by the Fisher operator $A_K$ or its spectral multiplier $G(\\omega)$.",
    ),
    (
        "Autonomy gives a complete local temporal Fisher spectrum for classical Poisson photodetection channels even when detector memory destroys an independent-event description.",
        "Autonomy gives a complete local weak-intensity-waveform Fisher spectrum within the admitted classical Poisson source model even when detector memory destroys an independent-event description.",
    ),
    (
        "These results suggest that high-flux detector characterization should distinguish scalar engineering summaries from the complete trajectory-level information transfer they only partially constrain.",
        "These results suggest that high-flux detector characterization should distinguish scalar engineering summaries from the full accessible trajectory-level information transfer they only partially constrain.",
    ),
]

for old, new in replacements:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(
            f"Expected exactly one replacement target, found {count}: {old[:80]}"
        )
    text = text.replace(old, new)

anchor = (
    "The important point is not that the mean response depends on modulation frequency; that is established dead-time physics \\cite{TeichVannucci1978,VannucciTeich1978}. The information statement is that the complete timestamp record has a zero static tangent without a finite temporal information cutoff."
)
insert = anchor + "\n\n" + (
    "For a technology-neutral scale translation, take $\\tau=10\\,\\mathrm{ns}$. The classical count maximum then occurs at $\\lambda_*=1/\\tau=100\\,\\mathrm{MHz}$. The theorem point $\\omega\\tau=\\pi$ corresponds to an ordinary modulation frequency $f=\\omega/(2\\pi)=1/(2\\tau)=50\\,\\mathrm{MHz}$, where Eq.~\\eqref{eq:piBound} already guarantees a source-normalized Fisher retention of at least $0.516975\\ldots$. The exact high-frequency residue remains $1/e\\simeq0.3679$. These numbers are only a dimensional translation of the ideal Type-II theorem and do not assert that any particular detector technology realizes that model."
)
if text.count(anchor) != 1:
    raise RuntimeError("Dimensionful-example insertion anchor not unique")
text = text.replace(anchor, insert)

outlook_anchor = (
    "The inference literature also clarifies the observation model. Barat, Dautremer, and Trigano studied Type-I/II intensity inference while observing both the counting process and the idle/dead indicator process \\cite{BaratDautremerTrigano2006}; that is a richer record than the timestamp-only record analyzed in the Type-II theorems here. Jorgensen and Johnson derive LAN and Fisher rates for a broad nonparalyzable/gated event-detection class \\cite{JorgensenJohnson2026}. More broadly, identifiability and reconstruction from queue output processes are classical topics; Daley's review explicitly treats identifiability from queue outputs \\cite{Daley1976}. We therefore make no generic output-identifiability claim. The narrow result here is the Fisher singularity at the common Type-II count maximum for the timestamp-only experiment. Our results should be read as a complementary high-flux Type-II trajectory-information analysis, not as the first statistical treatment of dead time."
)
outlook = outlook_anchor + "\n\n" + (
    "The deterministic singularity also suggests a direct future validation: for a detector independently established to operate in a genuinely paralyzable regime, one could work near $\\lambda\\tau=1$ and compare the complete timestamp response to a quasi-static rate perturbation with its response to a weak finite-frequency modulation. The theory predicts first-order static blindness while finite-frequency information remains. Such an experiment would test the idealized model, but it is not required for the analytical conclusions developed here."
)
if text.count(outlook_anchor) != 1:
    raise RuntimeError("Outlook insertion anchor not unique")
text = text.replace(outlook_anchor, outlook)

required = [
    r"\tau=10\,\mathrm{ns}",
    r"\lambda_*=1/\tau=100\,\mathrm{MHz}",
    r"f=\omega/(2\pi)=1/(2\tau)=50\,\mathrm{MHz}",
    "complete local weak-intensity-waveform Fisher spectrum",
    "Such an experiment would test the idealized model, but it is not required",
    r"\GDC=\Gcyc=\frac{r}{\lambda}I_D",
    r"G_1(\omega)>0\qquad\text{for every }\omega\neq0",
]
for token in required:
    if token not in text:
        raise RuntimeError(f"Required Rev7 invariant missing: {token}")

for forbidden in [
    "Autonomy gives a complete local temporal Fisher spectrum",
    "Temporal information belongs to the complete trajectory channel.",
    "one complete local waveform language",
    "placeholder",
    "TODO",
    "TBD",
    "first paper",
    "The repository contains",
]:
    if forbidden in text:
        raise RuntimeError(f"Forbidden Rev7 residue survived: {forbidden}")

DST.write_text(text, encoding="utf-8")
print(f"Wrote {DST.name}")
