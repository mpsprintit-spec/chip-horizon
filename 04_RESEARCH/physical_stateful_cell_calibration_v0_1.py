#!/usr/bin/env python3
"""Numerical calibration for the Physical Stateful Cell V0.1 model."""

from __future__ import annotations

import csv
import math
from pathlib import Path


TAUS_NS = (1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 5000)
DT_NS = 1.0
INPUTS = (3.0, 5.0, 2.0, 7.0)
THRESHOLD = 0.05


def run(tau_ns: float) -> dict:
    lam = math.exp(-DT_NS / tau_ns)
    state = 0.0
    target = 0.0
    errors = []

    for x in INPUTS:
        state = lam * state + x
        target += x
        errors.append(state - target)

    rms = math.sqrt(sum(e * e for e in errors) / len(errors))
    max_error = max(abs(e) for e in errors)
    relative = rms / max(abs(sum(INPUTS)), 1.0)

    return {
        "tau_ns": tau_ns,
        "lambda": lam,
        "rms_error": rms,
        "max_error": max_error,
        "relative_error": relative,
        "pass": relative < THRESHOLD,
    }


def main() -> None:
    rows = [run(tau) for tau in TAUS_NS]
    out = Path("physical_stateful_cell_calibration_v0_1.csv")

    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    passed = [r for r in rows if r["pass"]]

    print("Physical Stateful Cell Calibration V0.1")
    print("---------------------------------------")
    print(f"dt                  : {DT_NS:g} ns")
    print(f"inputs              : {list(INPUTS)}")
    print(f"target              : {[3, 8, 10, 17]}")
    print(f"threshold           : relative RMS < {THRESHOLD:g}")
    print(f"tested tau values   : {len(rows)}")
    print(f"passing tau values  : {len(passed)}")

    for row in rows:
        print(
            f"tau={row['tau_ns']:7g} ns  "
            f"lambda={row['lambda']:.9f}  "
            f"rel_err={row['relative_error']:.6f}  "
            f"PASS={row['pass']}"
        )

    if passed:
        print(
            "feasible tau range : "
            f"{passed[0]['tau_ns']:g} ns .. {passed[-1]['tau_ns']:g} ns"
        )


if __name__ == "__main__":
    main()
