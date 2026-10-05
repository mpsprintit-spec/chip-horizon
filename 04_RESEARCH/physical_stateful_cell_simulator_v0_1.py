#!/usr/bin/env python3
"""Physical Stateful Cell Simulator V0.1.

Platform-neutral numerical model.
This is a mathematical simulator, not a material or field solver.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from typing import List

import numpy as np


@dataclass
class Config:
    dt: float = 1e-9
    tau: float = 10e-9
    wave_retention: float = 0.80
    input_gain: float = 1.0
    state_gain: float = 0.10
    wave_feedback: float = 0.15
    wave_loss: float = 1.0
    state_wave_gain: float = 0.20
    nonlinearity: str = "linear"
    state_limit: float = 100.0
    noise_sigma: float = 0.0
    read_gain_state: float = 1.0
    read_gain_wave: float = 0.0
    read_noise_sigma: float = 0.0
    read_backaction: float = 0.0
    delay_steps: int = 0
    reset_value: float = 0.0
    reset_energy: float = 1.0
    update_energy: float = 1.0
    min_state_step: float = 1.0
    seed: int = 0


def activation(value: float, cfg: Config) -> float:
    if cfg.nonlinearity == "linear":
        return value
    if cfg.nonlinearity == "saturation":
        return float(np.clip(value, -cfg.state_limit, cfg.state_limit))
    if cfg.nonlinearity == "tanh":
        return cfg.state_limit * math.tanh(value / cfg.state_limit)
    raise ValueError(f"unknown nonlinearity: {cfg.nonlinearity}")


def simulate(inputs: List[float], cfg: Config) -> dict:
    rng = np.random.default_rng(cfg.seed)
    n = len(inputs)

    if cfg.tau <= 0:
        raise ValueError("tau must be > 0")
    if not 0 <= cfg.wave_retention <= 1:
        raise ValueError("wave_retention must be in [0, 1]")
    if not 0 <= cfg.wave_loss <= 1:
        raise ValueError("wave_loss must be in [0, 1]")
    if cfg.delay_steps < 0:
        raise ValueError("delay_steps must be >= 0")
    if not 0 <= cfg.read_backaction <= 1:
        raise ValueError("read_backaction must be in [0, 1]")

    lam = math.exp(-cfg.dt / cfg.tau)

    state = np.zeros(n + 1, dtype=float)
    wave = np.zeros(n + 1, dtype=float)
    output = np.zeros(n, dtype=float)
    state_noise = rng.normal(0.0, cfg.noise_sigma, n)
    read_noise = rng.normal(0.0, cfg.read_noise_sigma, n)

    for i, x in enumerate(inputs):
        delayed_wave = 0.0
        j = i - cfg.delay_steps
        if j >= 0:
            delayed_wave = wave[j]

        wave[i + 1] = (
            cfg.wave_retention * cfg.wave_loss * wave[i]
            + cfg.input_gain * x
            + cfg.state_gain * state[i]
            + cfg.wave_feedback * delayed_wave
        )

        raw_state = (
            lam * state[i]
            + cfg.state_wave_gain * wave[i + 1]
            + state_noise[i]
        )
        state[i + 1] = activation(raw_state, cfg)

        # Finite read coupling is represented as a multiplicative back-action.
        state[i + 1] *= 1.0 - cfg.read_backaction

        output[i] = (
            cfg.read_gain_state * state[i + 1]
            + cfg.read_gain_wave * wave[i + 1]
            + read_noise[i]
        )

    target = np.cumsum(np.asarray(inputs, dtype=float))
    error = output - target

    rms_error = float(np.sqrt(np.mean(error ** 2))) if n else 0.0
    max_error = float(np.max(np.abs(error))) if n else 0.0
    target_scale = float(np.max(np.abs(target))) if n else 0.0
    relative_error = rms_error / max(target_scale, cfg.min_state_step)

    state_range = float(np.max(state) - np.min(state)) if len(state) else 0.0
    snr = state_range / max(cfg.noise_sigma, 1e-15)
    noise_ratio = cfg.noise_sigma / max(cfg.min_state_step, 1e-15)

    return {
        "config": asdict(cfg),
        "lambda": lam,
        "effective_tau": cfg.tau,
        "delay_lifetime_ratio": (cfg.delay_steps * cfg.dt) / cfg.tau,
        "state": state.tolist(),
        "wave": wave.tolist(),
        "output": output.tolist(),
        "target": target.tolist(),
        "error": error.tolist(),
        "rms_error": rms_error,
        "max_error": max_error,
        "relative_error": relative_error,
        "state_range": state_range,
        "state_snr": float(snr),
        "noise_ratio": float(noise_ratio),
        "update_energy": cfg.update_energy,
        "reset_energy": cfg.reset_energy,
        "reset_ratio": cfg.reset_energy / max(cfg.update_energy, 1e-15),
        "stable": bool(
            np.all(np.isfinite(state))
            and np.all(np.abs(state) <= cfg.state_limit * 1.001)
        ),
    }


def read_disturbance_experiment(inputs: List[float], cfg: Config) -> dict:
    """Compare non-invasive and finite-backaction read trajectories."""
    base_cfg = Config(**asdict(cfg))
    base_cfg.read_backaction = 0.0
    finite_cfg = Config(**asdict(cfg))

    baseline = simulate(inputs, base_cfg)
    with_read = simulate(inputs, finite_cfg)

    base_state = np.asarray(baseline["state"], dtype=float)
    read_state = np.asarray(with_read["state"], dtype=float)
    disturbance = np.abs(read_state - base_state)

    return {
        "max_read_disturbance": float(np.max(disturbance)) if len(disturbance) else 0.0,
        "mean_read_disturbance": float(np.mean(disturbance)) if len(disturbance) else 0.0,
        "read_disturbance_ratio": (
            float(np.max(disturbance))
            / max(cfg.min_state_step, 1e-15)
            if len(disturbance)
            else 0.0
        ),
    }


def reset_experiment(inputs: List[float], cfg: Config) -> dict:
    result = simulate(inputs, cfg)
    state_before = result["state"][-1]

    # V0.1 models reset as an explicit state assignment. Physical reset time
    # and energy remain configuration/measured parameters, not invented values.
    reset_state = cfg.reset_value
    residual = abs(reset_state)

    result["reset"] = {
        "state_before": state_before,
        "reset_value": reset_state,
        "residual": residual,
        "residual_fraction_of_range": residual / max(
            result["state_range"], cfg.min_state_step
        ),
        "reset_energy": cfg.reset_energy,
    }
    result["read_disturbance"] = read_disturbance_experiment(inputs, cfg)
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--inputs",
        default="3,5,2,7",
        help="comma-separated input sequence",
    )
    parser.add_argument("--tau-ns", type=float, default=10.0)
    parser.add_argument("--delay", type=int, default=0)
    parser.add_argument("--noise", type=float, default=0.0)
    parser.add_argument("--read-backaction", type=float, default=0.0)
    parser.add_argument(
        "--nonlinearity",
        choices=("linear", "saturation", "tanh"),
        default="linear",
    )
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    inputs = [float(v.strip()) for v in args.inputs.split(",") if v.strip()]

    cfg = Config(
        tau=args.tau_ns * 1e-9,
        delay_steps=args.delay,
        noise_sigma=args.noise,
        read_backaction=args.read_backaction,
        nonlinearity=args.nonlinearity,
        seed=args.seed,
    )

    result = reset_experiment(inputs, cfg)

    if args.json:
        print(json.dumps(result, indent=2))
        return

    print("Physical Stateful Cell Simulator V0.1")
    print("------------------------------------")
    print(f"inputs              : {inputs}")
    print(f"lambda              : {result['lambda']:.9f}")
    print(f"effective tau (ns)  : {result['effective_tau'] * 1e9:.6g}")
    print(f"delay/tau           : {result['delay_lifetime_ratio']:.6g}")
    print(f"state               : {np.round(result['state'], 6).tolist()}")
    print(f"wave                : {np.round(result['wave'], 6).tolist()}")
    print(f"output              : {np.round(result['output'], 6).tolist()}")
    print(f"target              : {np.round(result['target'], 6).tolist()}")
    print(f"RMS error           : {result['rms_error']:.6g}")
    print(f"max error           : {result['max_error']:.6g}")
    print(f"relative error      : {result['relative_error']:.6g}")
    print(f"state range         : {result['state_range']:.6g}")
    print(f"state SNR           : {result['state_snr']:.6g}")
    print(f"noise ratio         : {result['noise_ratio']:.6g}")
    print(f"update energy       : {result['update_energy']:.6g}")
    print(f"reset energy        : {result['reset_energy']:.6g}")
    print(f"reset ratio         : {result['reset_ratio']:.6g}")
    print(f"stable              : {result['stable']}")
    print(f"reset residual      : {result['reset']['residual']:.6g}")
    print(
        "max read disturbance: "
        f"{result['read_disturbance']['max_read_disturbance']:.6g}"
    )


if __name__ == "__main__":
    main()
