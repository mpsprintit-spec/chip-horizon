#!/usr/bin/env python3
"""Run a parameter sweep for Physical Stateful Cell Simulator V0.1."""

from __future__ import annotations

import argparse
import csv
import itertools
from dataclasses import replace
from pathlib import Path

from physical_stateful_cell_simulator_v0_1 import Config, simulate


TAUS_NS = (1, 2, 5, 10, 20, 50, 100)
DELAYS = (0, 1, 2, 5, 10)
NOISES = (0, 0.01, 0.05, 0.1, 0.25, 0.5)
READ_BACKACTIONS = (0, 0.01, 0.05, 0.1)
NONLINEARITIES = ("linear", "saturation", "tanh")


def passes(result: dict) -> bool:
    return (
        result["relative_error"] < 0.05
        and result["state_snr"] > 10.0
        and result["delay_lifetime_ratio"] < 0.1
        and result["read_disturbance_ratio"] < 0.1
        and result["stable"]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="physical_stateful_cell_sweep_v0_1.csv")
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    inputs = [3.0, 5.0, 2.0, 7.0]
    rows = []

    for tau_ns, delay, noise, read_b, nonlinearity in itertools.product(
        TAUS_NS, DELAYS, NOISES, READ_BACKACTIONS, NONLINEARITIES
    ):
        cfg = Config(
            tau=tau_ns * 1e-9,
            delay_steps=delay,
            noise_sigma=noise,
            read_backaction=read_b,
            nonlinearity=nonlinearity,
            seed=args.seed,
        )
        result = simulate(inputs, cfg)

        # The simulator's read-disturbance field is not returned by simulate(),
        # so use the state back-action parameter as the controlled screening
        # observable for this sweep. A dedicated paired-read experiment remains
        # available in the simulator module.
        read_ratio = read_b / max(cfg.min_state_step, 1e-15)

        row = {
            "tau_ns": tau_ns,
            "delay_steps": delay,
            "noise_sigma": noise,
            "read_backaction": read_b,
            "nonlinearity": nonlinearity,
            "relative_error": result["relative_error"],
            "max_error": result["max_error"],
            "state_snr": result["state_snr"],
            "noise_ratio": result["noise_ratio"],
            "delay_lifetime_ratio": result["delay_lifetime_ratio"],
            "read_disturbance_ratio": read_ratio,
            "stable": result["stable"],
            "pass": (
                result["relative_error"] < 0.05
                and result["state_snr"] > 10.0
                and result["delay_lifetime_ratio"] < 0.1
                and read_ratio < 0.1
                and result["stable"]
            ),
        }
        rows.append(row)

    fieldnames = list(rows[0].keys())
    out = Path(args.out)
    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    passed = [r for r in rows if r["pass"]]
    print("Physical Stateful Cell Sweep V0.1")
    print("----------------------------------")
    print(f"total combinations : {len(rows)}")
    print(f"passing combinations: {len(passed)}")
    print(f"pass fraction       : {len(passed) / len(rows):.6f}")
    print(f"output              : {out}")

    if passed:
        tau_values = sorted({r["tau_ns"] for r in passed})
        delay_values = sorted({r["delay_steps"] for r in passed})
        noise_values = sorted({r["noise_sigma"] for r in passed})
        read_values = sorted({r["read_backaction"] for r in passed})
        nonlinearities = sorted({r["nonlinearity"] for r in passed})
        print(f"feasible tau_ns     : {tau_values}")
        print(f"feasible delays     : {delay_values}")
        print(f"feasible noise      : {noise_values}")
        print(f"feasible read       : {read_values}")
        print(f"feasible nonlinearities: {nonlinearities}")


if __name__ == "__main__":
    main()
