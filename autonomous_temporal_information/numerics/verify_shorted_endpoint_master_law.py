#!/usr/bin/env python3
"""Adversarial validation for WP11 shorted-endpoint master law.

Checks:
1. random rank-2 coherent supports P that do not commute with an equally
   spaced qutrit Hamiltonian;
2. exact +1 Bohr-gap tangents satisfying the physical first-order condition
   Q A Q = 0;
3. arbitrary one-copy POVMs obey the abstract WP11 measurement master law;
4. random two-copy collective POVMs obey the same per-copy law;
5. support-side and kernel-side shorting constants bound J_B^+/J_B^- and
   J_+/J_- respectively;
6. the resulting scalar shorted-endpoint resource law bounds all sampled
   one-copy/collective Fisher traces;
7. the explicit four-level noncommuting-support counterexample has
   lambda_U=1/4, mu_U=3/4, J_B=1/2, J_+=3/2 and disproves the naive
   no-geometry resource ceiling operationally (7/4 > 13/8).

This script validates the algebra and low-dimensional counterexamples. It is
not a substitute for the analytic proof and does not claim generic sharpness
of the full WP11 master bound.
"""

from __future__ import annotations

import math
import numpy as np

RNG = np.random.default_rng(20260822)


def random_povm(d: int, outcomes: int) -> list[np.ndarray]:
    mats = []
    for _ in range(outcomes):
        x = RNG.normal(size=(d, d)) + 1j * RNG.normal(size=(d, d))
        mats.append(x @ x.conj().T)
    total = sum(mats)
    vals, vecs = np.linalg.eigh(total)
    invsqrt = vecs @ np.diag(1.0 / np.sqrt(vals)) @ vecs.conj().T
    return [invsqrt @ m @ invsqrt for m in mats]


def fisher_trace(povm: list[np.ndarray], rho: np.ndarray, A: np.ndarray) -> float:
    out = 0.0
    for M in povm:
        p = float(np.trace(rho @ M).real)
        z = np.trace(A @ M)
        if p > 1e-14:
            out += abs(z) ** 2 / p
    return float(out)


def psd_pinv(a: np.ndarray, tol: float = 1e-11) -> np.ndarray:
    vals, vecs = np.linalg.eigh((a + a.conj().T) / 2.0)
    inv = np.array([1.0 / v if v > tol else 0.0 for v in vals])
    return vecs @ np.diag(inv) @ vecs.conj().T


def support_projector(a: np.ndarray, tol: float = 1e-9) -> np.ndarray:
    vals, vecs = np.linalg.eigh((a + a.conj().T) / 2.0)
    keep = vals > tol
    if not np.any(keep):
        return np.zeros_like(a)
    v = vecs[:, keep]
    return v @ v.conj().T


def numerical_radius(a: np.ndarray, phases: int = 3001) -> float:
    best = 0.0
    for phi in np.linspace(0.0, 2.0 * math.pi, phases, endpoint=False):
        h = (np.exp(-1j * phi) * a + np.exp(1j * phi) * a.conj().T) / 2.0
        best = max(best, float(np.linalg.eigvalsh(h).max()))
    return best


def shorting_constant(s: np.ndarray, r: np.ndarray, tol: float = 1e-10) -> float:
    """Largest lambda >=0 such that s-lambda*r is PSD.

    Here r is an orthogonal projector onto the information-bearing range.
    A simple bisection is sufficient for the small validation matrices.
    """
    if np.linalg.norm(r) < tol:
        return math.inf
    ps = support_projector(s, tol)
    if np.linalg.norm((np.eye(s.shape[0]) - ps) @ r) > 2e-7:
        return 0.0
    lo = 0.0
    hi = max(1.0, 2.0 * float(np.linalg.norm(s, 2)))
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        mineig = float(np.linalg.eigvalsh((s - mid * r + (s - mid * r).conj().T) / 2.0).min())
        if mineig >= -2e-11:
            lo = mid
        else:
            hi = mid
    return lo


def qfi_scalar(rho: np.ndarray, d: np.ndarray, tol: float = 1e-12) -> float:
    vals, vecs = np.linalg.eigh(rho)
    dm = vecs.conj().T @ d @ vecs
    out = 0.0
    for i, pi in enumerate(vals):
        for j, pj in enumerate(vals):
            den = pi + pj
            if den > tol:
                out += 2.0 * abs(dm[i, j]) ** 2 / den
    return float(out.real)


def random_noncommuting_qutrit_case():
    # H=diag(0,1,2), A=a|1><0|+b|2><1| is an exact +1 shift.
    # Choose Q=|q><q| and solve <q|A|q>=0 so Q A Q=0.
    while True:
        q = RNG.normal(size=3) + 1j * RNG.normal(size=3)
        q /= np.linalg.norm(q)
        if np.min(np.abs(q)) > 0.12:
            break

    Q = np.outer(q, q.conj())
    P = np.eye(3, dtype=complex) - Q
    rho = P / 2.0

    a = RNG.normal() + 1j * RNG.normal()
    b = -a * np.conj(q[1]) * q[0] / (np.conj(q[2]) * q[1])
    A = np.zeros((3, 3), dtype=complex)
    A[1, 0] = a
    A[2, 1] = b
    assert np.linalg.norm(Q @ A @ Q) < 2e-9

    rho_plus = 2.0 * P
    B = P @ A @ P
    Kp = Q @ A @ P
    Km = Q @ A.conj().T @ P

    ZBp = B @ rho_plus @ B.conj().T
    ZBm = B.conj().T @ rho_plus @ B
    Zp = Kp @ rho_plus @ Kp.conj().T
    Zm = Km @ rho_plus @ Km.conj().T

    JBp = float(np.trace(ZBp).real)
    JBm = float(np.trace(ZBm).real)
    Jp = float(np.trace(Zp).real)
    Jm = float(np.trace(Zm).real)

    abstract = min(
        (math.sqrt(JBp + Jp) + math.sqrt(Jm)) ** 2,
        (math.sqrt(JBm + Jm) + math.sqrt(Jp)) ** 2,
    )

    # Exact +1 shift endpoint projectors.
    PiD = np.diag([1.0, 1.0, 0.0]).astype(complex)
    PiU = np.diag([0.0, 1.0, 1.0]).astype(complex)
    SU = P @ PiU @ P
    SD = P @ PiD @ P
    WU = Q @ PiU @ Q
    WD = Q @ PiD @ Q

    lamU = shorting_constant(SU, support_projector(ZBp)) if JBp > 1e-12 else math.inf
    lamD = shorting_constant(SD, support_projector(ZBm)) if JBm > 1e-12 else math.inf
    muU = shorting_constant(WU, support_projector(Zp)) if Jp > 1e-12 else math.inf
    muD = shorting_constant(WD, support_projector(Zm)) if Jm > 1e-12 else math.inf

    # rho^{-1/2}=sqrt(2)P for rho=P/2.
    Bwhite = 2.0 * P @ B @ P
    w = numerical_radius(Bwhite, 1801)
    RB = math.inf if w < 1e-13 else 1.0 / w

    TU = float(np.trace(PiU @ rho).real)
    TD = float(np.trace(PiD @ rho).real)

    # Minimal operator curvature consistent with the support-to-kernel pieces.
    Cdelta = Zp + Zm
    GammaU = float(np.trace(WU @ Cdelta).real)
    GammaD = float(np.trace(WD @ Cdelta).real)

    BU = 0.0 if JBp < 1e-12 else 4.0 * TU / (RB * RB * lamU)
    BD = 0.0 if JBm < 1e-12 else 4.0 * TD / (RB * RB * lamD)
    SynU = 0.0 if Jp < 1e-12 else GammaU / muU
    SynD = 0.0 if Jm < 1e-12 else GammaD / muD

    resource = min(
        (math.sqrt(BU + SynU) + math.sqrt(SynD)) ** 2,
        (math.sqrt(BD + SynD) + math.sqrt(SynU)) ** 2,
    )

    return {
        "rho": rho,
        "A": A,
        "P": P,
        "JBp": JBp,
        "JBm": JBm,
        "Jp": Jp,
        "Jm": Jm,
        "abstract": abstract,
        "BU": BU,
        "BD": BD,
        "SynU": SynU,
        "SynD": SynD,
        "resource": resource,
    }


def check_random_noncommuting_one_copy() -> None:
    for _ in range(30):
        case = random_noncommuting_qutrit_case()
        assert case["JBp"] <= case["BU"] + 2e-5
        assert case["JBm"] <= case["BD"] + 2e-5
        assert case["Jp"] <= case["SynU"] + 2e-5
        assert case["Jm"] <= case["SynD"] + 2e-5
        for _ in range(80):
            F = fisher_trace(random_povm(3, 9), case["rho"], case["A"])
            assert F <= case["abstract"] + 3e-8, (F, case["abstract"])
            assert F <= case["resource"] + 3e-8, (F, case["resource"])
    print("Random noncommuting one-copy shorted-endpoint checks PASS")


def check_random_noncommuting_two_copy() -> None:
    for _ in range(8):
        case = random_noncommuting_qutrit_case()
        rho = case["rho"]
        A = case["A"]
        rho2 = np.kron(rho, rho)
        A2 = np.kron(A, rho) + np.kron(rho, A)
        for _ in range(100):
            F2 = fisher_trace(random_povm(9, 13), rho2, A2)
            assert F2 / 2.0 <= case["abstract"] + 5e-8
            assert F2 / 2.0 <= case["resource"] + 5e-8
    print("Random noncommuting two-copy collective checks PASS")


def check_four_level_geometric_counterexample() -> None:
    rt3 = math.sqrt(3.0)
    e0 = np.array([1.0, 0.0, 0.0, 0.0], dtype=complex)
    e2 = np.array([0.0, 0.0, 1.0, 0.0], dtype=complex)
    e3 = np.array([0.0, 0.0, 0.0, 1.0], dtype=complex)
    r = 0.5 * e2 + (rt3 / 2.0) * e3
    q = (rt3 / 2.0) * e2 - 0.5 * e3

    P = np.outer(e0, e0.conj()) + np.outer(r, r.conj())
    Q = np.eye(4, dtype=complex) - P
    rho = 0.5 * np.outer(e0, e0.conj()) + 0.5 * np.outer(r, r.conj())
    rho_plus = 2.0 * P

    A = np.outer(e2, e0.conj())  # exact +2 gap for H=diag(0,1,2,3)
    B = P @ A @ P
    Kp = Q @ A @ P
    Km = Q @ A.conj().T @ P
    assert np.linalg.norm(Km) < 2e-12

    ZB = B @ rho_plus @ B.conj().T
    Zp = Kp @ rho_plus @ Kp.conj().T
    JB = float(np.trace(ZB).real)
    Jp = float(np.trace(Zp).real)
    assert abs(JB - 0.5) < 2e-12
    assert abs(Jp - 1.5) < 2e-12

    PiU = np.diag([0.0, 0.0, 1.0, 0.0]).astype(complex)
    SU = P @ PiU @ P
    WU = Q @ PiU @ Q
    lamU = shorting_constant(SU, support_projector(ZB))
    muU = shorting_constant(WU, support_projector(Zp))
    assert abs(lamU - 0.25) < 2e-8, lamU
    assert abs(muU - 0.75) < 2e-8, muU

    TU = float(np.trace(PiU @ rho).real)
    assert abs(TU - 0.125) < 2e-12

    # Bwhite=2B on support; B=(1/2)|r><0|, so w(Bwhite)=1/2 and R_B^2=4.
    RB2 = 4.0
    naive_internal = 4.0 * TU / RB2
    corrected_internal = naive_internal / lamU
    assert abs(naive_internal - 0.125) < 2e-12
    assert abs(corrected_internal - JB) < 2e-8

    Cdelta = Zp  # minimal one-sided kernel curvature
    GammaU = float(np.trace(WU @ Cdelta).real)
    corrected_syn = GammaU / muU
    assert abs(corrected_syn - Jp) < 2e-8

    naive_total = naive_internal + Jp
    assert abs(naive_total - 13.0 / 8.0) < 2e-12

    Dc = (A + A.conj().T) / 2.0
    Ds = (A - A.conj().T) / (2j)
    Fqc = qfi_scalar(rho, Dc)
    Fqs = qfi_scalar(rho, Ds)
    assert abs(Fqc - 7.0 / 4.0) < 2e-12, Fqc
    assert abs(Fqs - 7.0 / 4.0) < 2e-12, Fqs

    # A fixed POVM that classically randomizes equally between scalar-SLD
    # optimal measurements has Fisher-trace (Fqc+Fqs)/2 = 7/4.
    randomized_trace = 0.5 * (Fqc + Fqs)
    assert abs(randomized_trace - 7.0 / 4.0) < 2e-12
    assert randomized_trace > naive_total + 1e-12

    corrected_total = corrected_internal + corrected_syn
    assert abs(corrected_total - 2.0) < 2e-8
    assert randomized_trace <= corrected_total + 1e-12

    print("Four-level principal-angle constants lambda_U=1/4, mu_U=3/4 PASS")
    print("Naive no-geometry internal bound factor-four failure PASS")
    print("Operational Fisher violation 7/4 > 13/8 PASS")
    print("Shorted-endpoint repaired resource ceiling PASS")


def main() -> None:
    check_random_noncommuting_one_copy()
    check_random_noncommuting_two_copy()
    check_four_level_geometric_counterexample()
    print("WP11 shorted-endpoint master-law validation PASS")


if __name__ == "__main__":
    main()
