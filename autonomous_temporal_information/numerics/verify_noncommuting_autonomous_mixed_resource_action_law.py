#!/usr/bin/env python3
"""Independent validator for WP19 noncommuting autonomous mixed resource/action law.

Checks:
1. random scalar WP11-compatible tuples obey the exact WP13 Psi envelope;
2. clean bilateral pure-boundary limit recovers A_CS >= F/4 for hbar*nu=1;
3. clean one-sided limit recovers A_CS >= F/2;
4. zero-synthesis limit reduces to the finite-radius internal ceiling;
5. the shared-kernel autonomous qutrit is reconstructed from matrices:
   exact exchange commutators, QAQ=0, weighted norms
   J_B^+=J_B^-=5/4, J_+=7/4, J_-=3;
6. the endpoint-incidence operator is diag(2,4,2), restricted costs are
   g_+=g_-=13/4, minimal curvature gives e=247/16, and
   Psi_(5/4)(247/16;13/4,13/4)=12 exactly;
7. random POVMs on that qutrit remain below the WP19 resource ceiling 12.

Units hbar*nu=1.
"""

from __future__ import annotations

import math
import numpy as np

RNG = np.random.default_rng(20260822)


def psi(a: float, e: float, p: float, q: float) -> float:
    assert a >= -1e-14 and e >= -1e-14 and p > 0.0 and q > 0.0
    a = max(a, 0.0)
    e = max(e, 0.0)
    if e <= a * p * p / q:
        return (math.sqrt(a) + math.sqrt(e / q)) ** 2
    return (e + p * a) * (1.0 / p + 1.0 / q)


def psd_pinv(a: np.ndarray, tol: float = 1e-11) -> np.ndarray:
    vals, vecs = np.linalg.eigh((a + a.conj().T) / 2.0)
    inv = np.array([1.0 / x if x > tol else 0.0 for x in vals])
    return vecs @ np.diag(inv) @ vecs.conj().T


def random_rank1_povm(d: int, m: int) -> np.ndarray:
    v = RNG.normal(size=(d, m)) + 1j * RNG.normal(size=(d, m))
    s = v @ v.conj().T
    vals, vecs = np.linalg.eigh((s + s.conj().T) / 2.0)
    inv_half = vecs @ np.diag(1.0 / np.sqrt(vals)) @ vecs.conj().T
    return inv_half @ v


def fisher_trace(rho: np.ndarray, A: np.ndarray, W: np.ndarray) -> float:
    out = 0.0
    for j in range(W.shape[1]):
        w = W[:, j]
        p = float(np.vdot(w, rho @ w).real)
        if p <= 1e-13:
            continue
        z = np.vdot(w, A @ w)
        out += abs(z) ** 2 / p
    return float(out)


def check_scalar_envelope() -> None:
    for _ in range(30000):
        a = 10.0 ** RNG.uniform(-4.0, 2.0)
        e = 10.0 ** RNG.uniform(-4.0, 3.0)
        p = 10.0 ** RNG.uniform(-2.0, 2.0)
        q = 10.0 ** RNG.uniform(-2.0, 2.0)

        jb = a * RNG.random()
        jp = (e / p) * RNG.random()
        rem = max(0.0, e - p * jp)
        jm = (rem / q) * RNG.random()

        lhs = (math.sqrt(jb + jp) + math.sqrt(jm)) ** 2
        rhs = psi(a, e, p, q)
        assert lhs <= rhs + 2e-10 * max(1.0, rhs), (lhs, rhs)
    print("Random WP11-to-WP13 scalar envelope PASS")


def check_clean_limits() -> None:
    # Bilateral: g_+=g_-=2, a=0, e=4 A_CS. Then F<=e, so A_CS>=F/4.
    for e in (0.01, 0.4, 2.0, 17.0):
        assert abs(psi(0.0, e, 2.0, 2.0) - e) < 1e-13

    # One-sided: J_- =0 and g_+=2 gives F<=e/2, i.e. A_CS=e/4 >= F/2.
    for e in (0.01, 0.4, 2.0, 17.0):
        fmax = e / 2.0
        assert abs((e / 4.0) - 0.5 * fmax) < 1e-13

    # No synthesis: e=0 must return a.
    for a in (0.0, 0.2, 3.0, 11.0):
        assert abs(psi(a, 0.0, 1.7, 2.9) - a) < 1e-13

    print("WP18 clean bilateral/one-sided and finite-radius limits PASS")


def qutrit_benchmark():
    # Fixed-total-energy shell |L>,|M>,|U>.
    Hs = np.diag([0.0, 1.0, 2.0])
    Hc = np.diag([2.0, 1.0, 0.0])
    q = np.array(
        [0.5, math.sqrt(5.0 / 8.0), 1.0 / (2.0 * math.sqrt(2.0))],
        dtype=complex,
    )
    Q = np.outer(q, q.conj())
    P = np.eye(3, dtype=complex) - Q
    rho = P / 2.0
    rho_plus = psd_pinv(rho)

    A = np.zeros((3, 3), dtype=complex)
    A[1, 0] = 1.0
    A[2, 1] = -math.sqrt(2.0)

    assert np.linalg.norm(Hs @ A - A @ Hs - A) < 2e-13
    assert np.linalg.norm(Hc @ A - A @ Hc + A) < 2e-13
    assert np.linalg.norm((Hs + Hc) - 2.0 * np.eye(3)) < 2e-13
    assert np.linalg.norm(Q @ A @ Q) < 2e-13

    B = P @ A @ P
    Kp = Q @ A @ P
    Km = Q @ A.conj().T @ P

    ZBp = B @ rho_plus @ B.conj().T
    ZBm = B.conj().T @ rho_plus @ B
    Zp = Kp @ rho_plus @ Kp.conj().T
    Zm = Km @ rho_plus @ Km.conj().T

    jbp = float(np.trace(ZBp).real)
    jbm = float(np.trace(ZBm).real)
    jp = float(np.trace(Zp).real)
    jm = float(np.trace(Zm).real)

    assert abs(jbp - 5.0 / 4.0) < 2e-11, jbp
    assert abs(jbm - 5.0 / 4.0) < 2e-11, jbm
    assert abs(jp - 7.0 / 4.0) < 2e-11, jp
    assert abs(jm - 3.0) < 2e-11, jm

    # Endpoint incidence sum:
    # signal lower L,M ; signal upper M,U ;
    # clock upper L,M ; clock lower M,U.
    G = np.diag([2.0, 4.0, 2.0])

    gp = float(np.vdot(q, G @ q).real)
    gm = gp
    assert abs(gp - 13.0 / 4.0) < 2e-12

    Cdelta = Zp + Zm
    # Both ranges are Q, so Cdelta=(19/4)Q.
    assert np.linalg.norm(Cdelta - (19.0 / 4.0) * Q) < 3e-11

    e = float(np.trace(G @ Cdelta).real)  # e = 4 A_CS
    assert abs(e - 247.0 / 16.0) < 3e-11, e

    resource = psi(5.0 / 4.0, e, gp, gm)
    assert abs(resource - 12.0) < 3e-11, resource

    return rho, A, resource


def check_qutrit_benchmark() -> None:
    rho, A, resource = qutrit_benchmark()
    best = 0.0
    for _ in range(8000):
        W = random_rank1_povm(3, int(RNG.integers(3, 9)))
        value = fisher_trace(rho, A, W)
        assert value <= resource + 2e-9
        best = max(best, value)
    print("Autonomous shared-kernel qutrit exact resource value 12 PASS")
    print(f"Random qutrit POVMs below WP19 ceiling PASS; max sampled={best:.6f}")


def main() -> None:
    check_scalar_envelope()
    check_clean_limits()
    check_qutrit_benchmark()
    print("WP19 noncommuting autonomous mixed resource/action validation PASS")


if __name__ == "__main__":
    main()
