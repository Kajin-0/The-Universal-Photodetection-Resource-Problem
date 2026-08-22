#!/usr/bin/env python3
"""Numerical sanity checks for WP20/WP24 operational Fisher tail theorem.

This script is validation only; the theorem is analytic.

It samples random finite-dimensional energy-sector populations, including
support gaps, constructs random rank-one frame POVMs, and verifies for
N=1 and N=2 that

    Tr F_N^(k) <= N min(D_k, U_k) <= N T_k.

It also checks the exact geometric/canonical-phase equality formula
analytically at machine precision.
"""

from __future__ import annotations

import numpy as np

SEED = 20260822
TOL = 5e-11


def random_frame_povm(rng: np.random.Generator, dim: int, outcomes: int):
    vecs = rng.normal(size=(outcomes, dim)) + 1j * rng.normal(
        size=(outcomes, dim)
    )
    frame = sum(np.outer(v, v.conj()) for v in vecs)
    vals, vecmat = np.linalg.eigh(frame)
    invsqrt = vecmat @ np.diag(1.0 / np.sqrt(vals)) @ vecmat.conj().T
    povm = []
    for v in vecs:
        w = invsqrt @ v
        povm.append(np.outer(w, w.conj()))
    completeness_error = np.linalg.norm(sum(povm) - np.eye(dim))
    assert completeness_error < 1e-10
    return povm


def one_copy_objects(q: np.ndarray, k: int):
    q = np.asarray(q, dtype=float)
    dim = len(q)
    rho = np.diag(q)

    V = np.zeros((dim, dim), dtype=complex)
    for n in range(dim - k):
        if q[n] > 0.0 and q[n + k] > 0.0:
            V[n + k, n] = 1.0

    sqrt_rho = np.diag(np.sqrt(q))
    A = sqrt_rho @ V @ sqrt_rho
    Dc = (A + A.conj().T) / 2.0
    Ds = (A - A.conj().T) / (2.0j)

    Pdom = V.conj().T @ V
    Pran = V @ V.conj().T
    D = float(np.trace(rho @ Pdom).real)
    U = float(np.trace(rho @ Pran).real)
    T = float(q[k:].sum())
    return rho, A, Dc, Ds, D, U, T


def fisher_trace(rho, Dc, Ds, povm):
    total = 0.0
    for M in povm:
        p = float(np.trace(rho @ M).real)
        if p <= 1e-14:
            continue
        dc = float(np.trace(Dc @ M).real)
        ds = float(np.trace(Ds @ M).real)
        total += (dc * dc + ds * ds) / p
    return total


def tensor_power(a: np.ndarray, n: int):
    out = np.array([[1.0]], dtype=complex)
    for _ in range(n):
        out = np.kron(out, a)
    return out


def n_copy_objects(q: np.ndarray, k: int, N: int):
    rho, A, _, _, D, U, T = one_copy_objects(q, k)
    rhoN = tensor_power(rho, N)
    dim = len(q)
    AN = np.zeros_like(rhoN, dtype=complex)
    for j in range(N):
        factors = [A if ell == j else rho for ell in range(N)]
        term = factors[0]
        for factor in factors[1:]:
            term = np.kron(term, factor)
        AN += term
    DcN = (AN + AN.conj().T) / 2.0
    DsN = (AN - AN.conj().T) / (2.0j)
    assert rhoN.shape == (dim**N, dim**N)
    return rhoN, DcN, DsN, D, U, T


def sample_population(rng: np.random.Generator, dim: int):
    q = rng.dirichlet(np.ones(dim))
    if dim >= 3 and rng.random() < 0.45:
        gap = int(rng.integers(1, dim - 1))
        q[gap] = 0.0
        q /= q.sum()
    return q


def random_povm_sweep(rng, N, dims, populations, povms_per_case):
    max_ratio = 0.0
    checked = 0
    for dim in dims:
        for _ in range(populations):
            q = sample_population(rng, dim)
            for k in range(1, dim):
                rhoN, DcN, DsN, D, U, T = n_copy_objects(q, k, N)
                tight_bound = N * min(D, U)
                coarse_bound = N * T
                assert tight_bound <= coarse_bound + TOL
                if tight_bound <= 1e-14:
                    continue
                for _ in range(povms_per_case):
                    dN = dim**N
                    povm = random_frame_povm(rng, dN, 3 * dN)
                    FI = fisher_trace(rhoN, DcN, DsN, povm)
                    if FI > tight_bound + TOL:
                        raise AssertionError(
                            f"Violation: N={N}, dim={dim}, k={k}, "
                            f"FI={FI:.16g}, tight={tight_bound:.16g}, "
                            f"coarse={coarse_bound:.16g}, q={q}"
                        )
                    max_ratio = max(max_ratio, FI / tight_bound)
                    checked += 1
    return checked, max_ratio


def check_geometric_equality():
    # Canonical phase POVM gives R(k)=|sum_n sqrt(q_n q_{n+k})|^2.
    # The infinite geometric sum is analytic; a long truncation checks it.
    for r in (0.1, 0.35, 0.7, 0.9):
        for k in (1, 2, 5, 10):
            n = np.arange(4000)
            q = (1.0 - r) * r**n
            alpha = np.sum(np.sqrt(q[:-k] * q[k:]))
            numerical = alpha * alpha
            exact = r**k
            if not np.isclose(numerical, exact, rtol=2e-12, atol=2e-14):
                raise AssertionError(
                    f"Geometric equality failed: r={r}, k={k}, "
                    f"numerical={numerical}, exact={exact}"
                )


def main():
    rng = np.random.default_rng(SEED)

    n1, max1 = random_povm_sweep(
        rng, N=1, dims=(2, 3, 4, 5), populations=50, povms_per_case=25
    )
    n2, max2 = random_povm_sweep(
        rng, N=2, dims=(2, 3), populations=30, povms_per_case=12
    )
    check_geometric_equality()

    print("WP20/WP24 numerical validation PASS")
    print(f"seed={SEED}")
    print(f"one-copy random POVMs checked={n1}, max FI/[N min(D,U)]={max1:.9f}")
    print(f"two-copy global POVMs checked={n2}, max FI/[N min(D,U)]={max2:.9f}")
    print("geometric/canonical-phase equality check=PASS")


if __name__ == "__main__":
    main()
