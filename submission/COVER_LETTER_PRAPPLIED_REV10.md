# Cover Letter Draft — Physical Review Applied

**Manuscript:** *Temporal Information Transfer and Resource Bounds in Autonomous Photodetection Event Channels*

**Article type:** Regular Article

**Author metadata:** replace placeholders before submission.

---

Dear Editors of *Physical Review Applied*,

Please consider the manuscript *“Temporal Information Transfer and Resource Bounds in Autonomous Photodetection Event Channels”* for publication as a Regular Article in *Physical Review Applied*.

Photodetector temporal performance is commonly summarized by rise time, transit time, timing jitter, impulse-response width, or an electrical $-3$ dB bandwidth. These quantities are essential engineering descriptors, but they do not in general answer the distinct question of how much information about a time-dependent incident optical signal reaches the detector's electrical record. The manuscript develops an information-theoretic framework for that question within a precisely defined class of autonomous, low-overlap photodetection event channels.

The principal result is an exact source-normalized Fisher-information transfer spectrum,

\[
G(\omega)=\int |H_m(\omega)|^2\kappa(dm),
\]

which is shown to be the spectral multiplier of the complete local weak-temporal-waveform Fisher operator. This yields a necessary-and-sufficient pointwise ordering criterion for one detector to Fisher-dominate another for every admissible weak temporal waveform task. For square-integrable registration-delay densities, the same spectrum gives an exact equivalent rectangular Fisher bandwidth,

\[
B_{\rm FI}=\frac{\mathfrak R_2}{4\eta},
\]

and local registration-hazard bounds produce explicit minimum timing-resource costs for preserving information throughout a target bandwidth.

To make these results directly usable by detector physicists, the manuscript provides closed-form mappings for Gaussian, exponential, uniform, Erlang, and Gaussian--exponential timing laws together with a fit-free estimator of $B_{\rm FI}$ from ordinary digitized impulse-response histograms. It now also includes a worked example using published detector IRFs from Spinelli *et al.*: although the comparison MCP has the smaller reported FWHM (25 ps versus 35 ps for the DJ-SPAD), graphical digitization of the full published response shapes gives approximately $5.98$ GHz versus $9.16$ GHz in Fisher-equivalent bandwidth, reversing the FWHM ranking. This concrete example demonstrates why a full-shape information metric can change an engineering conclusion drawn from a conventional response width.

The manuscript further establishes counterexamples showing why fixed mean and variance, a free source-synchronous clock, and aggregate stationary thermodynamic quantities are each incomplete timing-resource descriptions under different assumptions. It also clarifies what can and cannot be inferred from finite delay support, retained event marks, and deterministic preamplifier bandwidth.

We believe the manuscript is particularly suited to *Physical Review Applied* because it connects device physics, photodetector bandwidth assessment, stochastic dynamics, and information theory without assuming a specific detector material. Its principal quantities are computable from a specified timing law or directly from timing-histogram data, and the worked published-IRF example demonstrates the framework on an experimentally measured detector comparison without requiring new experiments.

The manuscript has not been submitted simultaneously to another journal. [Replace this sentence if there is relevant prior Physical Review submission history, a related manuscript under consideration, or a preprint/e-print that should be disclosed.]

Suggested or excluded referees: [optional; add only after conflict-of-interest review].

Thank you for your consideration.

Sincerely,

[Corresponding author name]
[Affiliation]
[Email]
[ORCID]
