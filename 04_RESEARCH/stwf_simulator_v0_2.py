#!/usr/bin/env python3
"""
STWF Stateful Core Simulator v0.2
Dependency-free reference implementation.

Run:
  python3 stwf_simulator_v0_2.py
"""

import math
import random


def mat_vec(M, v):
    return [sum(row[j] * v[j] for j in range(len(v))) for row in M]


def vec_add(a, b):
    return [x + y for x, y in zip(a, b)]


def vec_scale(a, s):
    return [x * s for x in a]


def spectral_radius_2x2(A):
    a, b = A[0]
    c, d = A[1]
    tr = a + d
    det = a * d - b * c
    disc = tr * tr - 4.0 * det
    if disc >= 0:
        r1 = (tr + math.sqrt(disc)) / 2.0
        r2 = (tr - math.sqrt(disc)) / 2.0
        return max(abs(r1), abs(r2))
    real = tr / 2.0
    imag = math.sqrt(-disc) / 2.0
    return math.sqrt(real * real + imag * imag)


def simulate(A, B, inputs, lam=1.0, noise_std=0.0, nonlinear=None, seed=0):
    random.seed(seed)
    state = [0.0] * len(A)
    trajectory = []

    for x in inputs:
        coupled = mat_vec(A, state)
        driven = mat_vec(B, x)
        noise = [random.gauss(0.0, noise_std) for _ in state]

        nxt = [
            lam * coupled[i] + driven[i] + noise[i]
            for i in range(len(state))
        ]

        if nonlinear is not None:
            nxt = [nonlinear(v) for v in nxt]

        state = nxt
        trajectory.append(state[:])

    return trajectory


def saturation(limit):
    def fn(x):
        return max(-limit, min(limit, x))
    return fn


def rms(values):
    if not values:
        return 0.0
    return math.sqrt(sum(x * x for x in values) / len(values))


def test_scalar_accumulator():
    # S(t+1) = S(t) + X(t)
    inputs = [[3.0], [5.0], [2.0], [7.0]]
    A = [[1.0]]
    B = [[1.0]]
    result = simulate(A, B, inputs)
    states = [round(s[0], 12) for s in result]
    expected = [3.0, 8.0, 10.0, 17.0]
    assert states == expected, (states, expected)
    print("TEST 1 accumulator: PASS", states)


def test_retention_sweep():
    A = [[1.0]]
    B = [[1.0]]
    inputs = [[1.0]] + [[0.0]] * 9

    print("TEST 2 retention sweep")
    for lam in [0.0, 0.5, 0.9, 0.99, 0.999, 1.0]:
        result = simulate(A, B, inputs, lam=lam)
        final = result[-1][0]
        if 0.0 < lam < 1.0:
            tau_steps = -1.0 / math.log(lam)
            print(f"  lambda={lam:<5} final={final:.8f} tau={tau_steps:.6f} steps")
        else:
            print(f"  lambda={lam:<5} final={final:.8f}")


def test_vector_stability():
    A = [
        [0.9, 0.2],
        [-0.1, 0.8],
    ]
    B = [
        [1.0, 0.0],
        [0.0, 1.0],
    ]
    rho = spectral_radius_2x2(A)
    inputs = [[1.0, 0.0]] + [[0.0, 0.0]] * 19
    result = simulate(A, B, inputs)

    print("TEST 3 vector recurrence")
    print(f"  spectral_radius={rho:.8f}")
    print(f"  stable_linear_warning={rho >= 1.0}")
    print(f"  final_state={result[-1]}")


def test_noise():
    A = [[1.0]]
    B = [[1.0]]
    inputs = [[1.0] for _ in range(100)]
    clean = simulate(A, B, inputs)
    noisy = simulate(A, B, inputs, noise_std=0.01, seed=42)

    errors = [
        noisy[i][0] - clean[i][0]
        for i in range(len(inputs))
    ]

    print("TEST 4 noise")
    print(f"  RMS error={rms(errors):.8f}")
    print(f"  max error={max(abs(e) for e in errors):.8f}")


def test_nonlinear():
    A = [
        [1.0, 0.2],
        [0.0, 0.9],
    ]
    B = [
        [1.0, 0.0],
        [0.0, 1.0],
    ]
    inputs = [[5.0, 1.0] for _ in range(10)]
    result = simulate(
        A, B, inputs,
        nonlinear=saturation(10.0)
    )

    print("TEST 5 nonlinear saturation")
    print(f"  final_state={result[-1]}")


def main():
    print("STWF STATEFUL CORE SIMULATOR v0.2")
    print("=" * 40)
    test_scalar_accumulator()
    test_retention_sweep()
    test_vector_stability()
    test_noise()
    test_nonlinear()
    print("=" * 40)
    print("All deterministic checks completed.")


if __name__ == "__main__":
    main()
