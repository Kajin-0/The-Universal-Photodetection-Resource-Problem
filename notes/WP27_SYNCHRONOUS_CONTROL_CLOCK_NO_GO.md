# WP27 — Synchronous-Control / Reference-Clock No-Go

**Date:** 2026-08-20

## Purpose

Stress-test WP25 against detectors with explicit time-dependent control, synchronous gating, heterodyne-style references, or internal clocks.

Main result:

> A free high-frequency reference clock can convert optical arrival-time information into a slowly reported electrical mark before the registration delay acts. Therefore no universal temporal information-bandwidth theorem can cover arbitrary time-dependent/synchronous detectors unless the control/reference bandwidth is itself bounded. WP25 must be understood as an autonomous/time-translation-invariant proper-event theorem, or equivalently as a theorem in which event marks do not acquire source timing information from an unbounded external clock.

---

# 1. Incident optical task

Take a weakly modulated Poisson/coherent photon flux

\[
\Phi_\theta(t)
=\Phi_0[1+\theta\cos(\omega t)],
\qquad |\theta|\ll1.
\]

At `theta=0`, the incident Fisher-information rate is

\[
\dot F_{in}
=\int_0^T
\frac{(\partial_\theta\Phi)^2}{\Phi}\frac{dt}{T}
=\frac{\Phi_0}{2}
\]

for an observation time containing an integer number of modulation periods.

Thus the incident FI **per photon** is

\[
\boxed{F_{in}/N_{ph}=1/2.}
\]

---

# 2. Ideal synchronous phase-mark detector

Assume the detector possesses a phase-locked internal or external clock at frequency `omega`.

When a photon is captured at time `t`, the detector stores the phase mark

\[
\boxed{M=\omega t\pmod{2\pi}.}
\]

The primary electrical registration may occur much later. Let its delay be any parameter-independent random variable `D`, including an arbitrarily slow exponential delay with finite hazard `Lambda_reg`.

The event eventually reports the stored phase mark `M`.

Over many periods, the mark distribution is

\[
\boxed{
p_\theta(M)
=\frac{1}{2\pi}[1+\theta\cos M].}
\]

Its Fisher information at `theta=0` is

\[
F_M
=\int_0^{2\pi}
\frac{[\partial_\theta p_\theta(M)]^2}
{p_0(M)}dM
\]

\[
=\frac1{2\pi}
\int_0^{2\pi}\cos^2M\,dM
\]

so

\[
\boxed{F_M=1/2.}
\]

Therefore

\[
\boxed{
F_M/F_{in,\ per\ photon}=1.
}
\]

The full incident modulation FI is preserved in the phase mark even if the later electrical registration is arbitrarily slow.

**Status:** PROVED explicit counterexample.

---

# 3. Why this does not contradict WP25

WP25 assumes that the mark law and conditional delay channel are not themselves modulated by the source parameter except through the stationary arrival-time displacement channel.

The synchronous detector violates that assumption:

\[
p_\theta(M)
\neq p_0(M).
\]

The mark is an actively generated sufficient statistic of the arrival phase.

Thus a finite post-capture registration hazard is not enough to limit a detector that may perform arbitrarily fast source-synchronous preprocessing **before** the bounded registration stage.

---

# 4. Even binary synchronous gating defeats pointwise bandwidth bounds

A continuous phase mark is not necessary to demonstrate the loophole.

Take a time-dependent capture gate

\[
g(t)=\frac{1+\cos\omega t}{2}.
\]

Suppose only the total number of captured events is reported after a long integration.

The mean captured count over time `T` is

\[
\mu_\theta
=\Phi_0T
\left\langle
\frac{1+\cos\omega t}{2}
[1+\theta\cos\omega t]
\right\rangle
\]

\[
=\Phi_0T\left(\frac12+\frac\theta4\right).
\]

The FI of this slow Poisson count at `theta=0` is

\[
F_{gate}
=\frac{(\partial_\theta\mu)^2}{\mu_0}
=\frac{\Phi_0T}{8}.
\]

The incident time-resolved FI is `Phi_0 T/2`, so

\[
\boxed{
F_{gate}/F_{in}=1/4,
}
\]

independent of the modulation frequency `omega`.

Thus even a one-bit-style synchronous gate can retain a nonzero constant fraction of arbitrarily high-frequency source information if the gate clock is free.

---

# 5. Resource-completeness consequence

For arbitrary actively controlled detectors,

\[
\boxed{
\text{finite registration hazard alone}
\not\Rightarrow
\text{finite source-information bandwidth}.
}
\]

A valid theorem must do one of two things.

### Option A — autonomous detector class

Require the intrinsic optical-to-primary-electrical channel to be time-translation invariant / stationary and forbid an unbounded external phase reference from encoding arrival time into a mark before registration.

This is the intended WP25 class.

### Option B — count control/reference resources

Allow time-dependent control, but include explicit bounds on resources such as

- control bandwidth;
- clock frequency and phase precision;
- control Hamiltonian norm/action;
- number of parallel demodulation channels;
- memory capacity/resolution for stored arrival phase;
- energy/free-energy cost of the reference/control system.

Without one of these restrictions, a universal detector bandwidth bound can be defeated by synchronous down-conversion.

---

# 6. Relation to heterodyne/lock-in detection

The physical mechanism is not exotic. Heterodyne, homodyne, lock-in, synchronous-gating, and mixer architectures deliberately transfer high-frequency signal information into lower-frequency observables using a reference oscillator.

Those techniques and their noise limits are established prior art.

The UPRP point is narrower:

> **An externally supplied temporal reference is itself a resource in any universal information-bandwidth theorem.**

A theorem that ignores it can mistake down-converted high-frequency information for impossible detector speed.

---

# 7. Revised detector-class taxonomy

The event branch now separates into:

1. **autonomous/time-translation-invariant proper event detectors** — WP25/WP26 apply;
2. **actively synchronized event detectors** — require explicit control/reference resources;
3. **coherent continuous-pointer detectors** — WP7/WP8 apparatus/coupling resource theory;
4. **continuous classical/Markov analog detectors** — largely overlap existing finite-frequency fluctuation-response theory.

This strengthens the conclusion that no single minimal scalar resource list covers every device called a photodetector without first fixing the detector/control class.

---

# 8. Minimality statement

For the autonomous proper-event class:

\[
\text{finite conditional timing concentration}
\Rightarrow
\text{finite average information bandwidth}.
\]

For the unrestricted actively driven class:

\[
\boxed{
\text{unbounded control/reference bandwidth}
\Rightarrow
\text{no detector-only temporal information-bandwidth ceiling}.
}
\]

This is another explicit no-go/repair pair in the UPRP program.

---

# 9. Novelty posture

Synchronous detection, heterodyne mixing, lock-in detection, time gating, and the use of reference clocks are long-established techniques and are not novel.

The candidate novelty is their role as a **missing resource in a universal photodetection information theorem**, together with the explicit FI-preserving phase-mark counterexample.

A theorem-level literature audit is still required before publication claims.

---

# Status

**PROVED explicit counterexamples.**

WP25 must henceforth be labeled an **autonomous/time-translation-invariant proper-event theorem** unless finite control/reference resources are added.