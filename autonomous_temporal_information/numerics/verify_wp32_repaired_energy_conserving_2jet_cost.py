#!/usr/bin/env python3
"""Random-matrix validator for the repaired WP32 theorem.

This explicitly tests the case omitted by WP31:
  * mixed stationary baseline;
  * degenerate occupied target-energy sectors;
  * complex support-to-kernel tangents preserving target energy;
  * positive excess curvature in target-energy shells unoccupied at baseline;
  * classical splitting of one occupied baseline eigenstate;
  * nonnegative ancilla input/output energies compensating target-energy gaps.

For each seed it verifies:
  1. exact reduced first derivatives;
  2. exact prescribed metric-contracted target-kernel Hessian;
  3. exact branchwise total-energy conservation;
  4. exact implementation cost V_impl=(1/2)Tr C.
"""

from __future__ import annotations

import math
import numpy as np

NSEEDS = 50
NCOORD = 2


def ptrace_anc(m: np.ndarray, td: int, ad: int) -> np.ndarray:
    return np.einsum("iaja->ij", m.reshape(td, ad, td, ad))


def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def run_seed(seed: int) -> tuple[float, float, float, float]:
    rng = np.random.default_rng(seed)

    # Occupied support has a degenerate E=0 sector plus E=2 and E=4.
    support_energies = [0.0, 0.0, 2.0, 4.0]
    ns = len(support_energies)

    # Horizontal kernel sectors at the same energies as the support.
    horizontal_kernel_energies = [0.0, 0.0, 2.0, 4.0]

    # Spectator kernel sectors include energies 1,3,7 that are NOT occupied
    # by the baseline.  E=1 is twofold degenerate so S can have a genuinely
    # non-diagonal PSD block there.
    spectator_energies = [1.0, 1.0, 3.0, 7.0]

    energies = np.asarray(
        support_energies + horizontal_kernel_energies + spectator_energies,
        dtype=float,
    )
    td = len(energies)

    support = list(range(ns))
    kh = list(range(ns, ns + len(horizontal_kernel_energies)))
    spectator = list(range(ns + len(horizontal_kernel_energies), td))

    lambdas = rng.random(ns) + 0.2
    lambdas /= lambdas.sum()

    rho = np.zeros((td, td), dtype=complex)
    rho[support, support] = lambdas

    pproj = np.diag([1.0] * ns + [0.0] * (td - ns))
    qproj = np.eye(td) - pproj

    rho_plus = np.zeros_like(rho)
    rho_plus[support, support] = 1.0 / lambdas

    # Random complex energy-preserving pure-boundary derivatives.  Within the
    # degenerate E=0 block this is a full random matrix, not a diagonal toy.
    derivs: list[np.ndarray] = []
    for _ in range(NCOORD):
        d = np.zeros((td, td), dtype=complex)
        for energy in sorted(set(support_energies)):
            sidx = [
                i for i, e in zip(support, support_energies) if e == energy
            ]
            kidx = [
                i
                for i, e in zip(kh, horizontal_kernel_energies)
                if e == energy
            ]
            block = 0.2 * (
                rng.normal(size=(len(kidx), len(sidx)))
                + 1j * rng.normal(size=(len(kidx), len(sidx)))
            )
            for a, ki in enumerate(kidx):
                for b, si in enumerate(sidx):
                    d[ki, si] = block[a, b]
                    d[si, ki] = block[a, b].conjugate()
        derivs.append(d)

    cmin = np.zeros_like(rho)
    for d in derivs:
        cmin += 2.0 * qproj @ d @ pproj @ rho_plus @ pproj @ d @ qproj

    # Random positive spectator curvature.  Crucially, most of it is placed
    # in baseline-UNoccupied target-energy sectors.
    s_op = np.zeros_like(rho)
    excess_modes: list[tuple[float, np.ndarray, float]] = []

    groups = [
        (1.0, spectator[:2]),
        (3.0, [spectator[2]]),
        (7.0, [spectator[3]]),
        # Also include an occupied-energy kernel block to test both cases.
        (0.0, kh[:2]),
    ]

    for energy, idxs in groups:
        x = 0.1 * (
            rng.normal(size=(len(idxs), len(idxs)))
            + 1j * rng.normal(size=(len(idxs), len(idxs)))
        )
        block = 0.3 * (x @ x.conj().T)
        s_op[np.ix_(idxs, idxs)] += block

        vals, vecs = np.linalg.eigh(block)
        for val, vec in zip(vals, vecs.T):
            if val > 1e-12:
                q = np.zeros(td, dtype=complex)
                q[idxs] = vec
                excess_modes.append((float(val), q, energy))

    c_target = cmin + 2.0 * s_op

    # Split the first occupied eigenstate into one branch per excess mode.
    nstar = 0
    estar = support_energies[nstar]
    lstar = float(lambdas[nstar])

    raw = rng.random(len(excess_modes)) + 0.1
    split_weights = lstar * raw / raw.sum()

    agg_d = [np.zeros((td, td), dtype=complex) for _ in range(NCOORD)]
    agg_c = np.zeros((td, td), dtype=complex)
    total_cost = 0.0
    max_energy_commutator = 0.0

    def add_branch(
        n: int,
        weight: float,
        input_ancilla_energy: float,
        excess: tuple[float, np.ndarray, float, float] | None,
    ) -> None:
        nonlocal total_cost, max_energy_commutator

        ad = 2 if excess is not None else 1

        def ket(t: int, a: int) -> np.ndarray:
            v = np.zeros(td * ad, dtype=complex)
            v[t * ad + a] = 1.0
            return v

        omega_vec = ket(n, 0)
        omega = np.outer(omega_vec, omega_vec.conj())

        chis: list[np.ndarray] = []
        for j, d in enumerate(derivs):
            h = qproj @ d[:, n] / lambdas[n]
            anc_in = np.asarray([1.0, 0.0], dtype=complex) if ad == 2 else np.asarray([1.0], dtype=complex)
            chi = np.kron(h, anc_in)

            if j == 0 and excess is not None:
                sval, q, _fenergy, _output_energy = excess
                chi += math.sqrt(sval / weight) * np.kron(
                    q, np.asarray([0.0, 1.0], dtype=complex)
                )
            chis.append(chi)

        ancilla_energies = (
            np.asarray([input_ancilla_energy, excess[3]], dtype=float)
            if excess is not None
            else np.asarray([input_ancilla_energy], dtype=float)
        )

        htot = np.kron(np.diag(energies), np.eye(ad)) + np.kron(
            np.eye(td), np.diag(ancilla_energies)
        )

        local_c = np.zeros((td, td), dtype=complex)
        for j, chi in enumerate(chis):
            k = 1j * (
                np.outer(chi, omega_vec.conj())
                - np.outer(omega_vec, chi.conj())
            )

            max_energy_commutator = max(
                max_energy_commutator,
                float(np.linalg.norm(comm(k, htot))),
            )

            first = ptrace_anc(-1j * comm(k, omega), td, ad)
            agg_d[j][:] += weight * first

            second = ptrace_anc(-comm(k, comm(k, omega)), td, ad)
            local_c += qproj @ second @ qproj

            total_cost += weight * float(
                np.vdot(omega_vec, k @ k @ omega_vec).real
            )

        agg_c[:] += weight * local_c

    # All unsplit occupied eigenstates use one branch with zero ancilla energy.
    for n in range(ns):
        if n == nstar:
            continue
        add_branch(n, float(lambdas[n]), 0.0, None)

    # Each excess mode receives its own split copy of nstar.  Nonnegative
    # ancilla energies compensate arbitrary target-energy differences.
    for weight, (sval, q, fenergy) in zip(split_weights, excess_modes):
        ain = max(0.0, fenergy - estar)
        bout = max(0.0, estar - fenergy)
        add_branch(nstar, float(weight), ain, (sval, q, fenergy, bout))

    derivative_error = max(
        float(np.linalg.norm(agg_d[j] - derivs[j])) for j in range(NCOORD)
    )
    curvature_error = float(np.linalg.norm(agg_c - c_target))
    cost_error = abs(total_cost - 0.5 * float(np.trace(c_target).real))

    return derivative_error, curvature_error, cost_error, max_energy_commutator


def main() -> None:
    worst = np.zeros(4, dtype=float)

    for seed in range(NSEEDS):
        errors = np.asarray(run_seed(seed))
        worst = np.maximum(worst, errors)

        assert errors[0] < 5e-12
        assert errors[1] < 5e-11
        assert errors[2] < 5e-11
        assert errors[3] < 5e-12

    print("WP32 repaired energy-conserving 2-jet validator PASS")
    print(f"  seeds: {NSEEDS}")
    print(f"  worst first-derivative error: {worst[0]:.3e}")
    print(f"  worst prescribed-curvature error: {worst[1]:.3e}")
    print(f"  worst cost equality error: {worst[2]:.3e}")
    print(f"  worst [K,H_tot] error: {worst[3]:.3e}")


if __name__ == "__main__":
    main()
