# Independent Causal Simulation of a Stateful WCR v0.1

Date: 7 October 2026

## Purpose

This is an independent numerical experiment for the WCR causal claim that was not yet demonstrated by the external-evidence survey:

> Prepare two different internal physical states, apply the same later input, and obtain measurably different outputs because of the prior state.

This is a **simulation experiment**, not a physical experiment and not evidence that a Horizon device already works.

## Model

A simplified driven wave-resonator model was used.

Internal state:
- q = state-dependent detuning parameter.

Complex wave amplitude:
- a = internal field amplitude.

At each simulation step:

    Delta = K*q
    a_next = rho*a + kappa*sqrt(P)/(1 + i*Delta)
    y = |a|^2

where:
- rho = 0.90
- kappa = 0.30
- K = 3.5
- P = 1.0
- probe input is identical for both states.

The simulation is deliberately small. It tests causal dependence, not a complete physical device.

## Causal protocol

State A:
- q_A = 0.1

State B:
- q_B = 0.8

The same probe input P=1.0 is applied for 80 steps.

The final 20 samples are averaged as the readout observable.

### Result

State A output:

    Y_A = 8.006432

State B output:

    Y_B = 1.016654

Absolute difference:

    |Y_A - Y_B| = 6.989778

Relative difference with respect to the mean output:

    147.2 %

Therefore the numerical model produces a strong state-dependent response under identical later input.

## Noise stress test

500 independent A/B trials were repeated for each additive output-noise level.

| Noise std | Mean A-B difference | Std. of measured difference | Difference / std |
|---:|---:|---:|---:|
| 0.001 | 6.9898 | 0.00031 | 22,805 |
| 0.005 | 6.9896 | 0.00157 | 4,457 |
| 0.010 | 6.9896 | 0.00320 | 2,187 |
| 0.020 | 6.9903 | 0.00631 | 1,108 |
| 0.050 | 6.9898 | 0.01556 | 449 |

The effect remains numerically distinguishable under the tested noise levels.

## Interpretation

### What passed

The simulation passes the following mathematical causal criterion:

    State A != State B
    same input X
    => output A != output B

The difference is produced by the state entering the wave-response equation. It is therefore not merely a label attached after computation.

### What did NOT pass

This does not establish:
- a fabricated Horizon WCR;
- a real material mechanism;
- experimentally achievable q values;
- realistic optical loss;
- realistic nonlinear energy;
- realistic state-writing energy;
- physical retention;
- fabrication tolerance;
- smartphone-scale integration;
- supercomputer-scale interconnect;
- superiority over CMOS.

The model is a causal numerical proof-of-concept only.

## Important control

The experiment would be invalid if the A/B difference were introduced by changing the input. Here the probe input is fixed at P=1.0 for both conditions; only the prepared internal state q differs.

A future physical experiment must implement the same control:

    prepare state A
    apply identical probe X
    measure Y_A

    prepare state B
    apply identical probe X
    measure Y_B

and require:

    |Y_A - Y_B| > complete measurement uncertainty

with repeated trials and independent state preparation.

## Relation to existing external evidence

Published experiments already demonstrate pieces of this mechanism. For example, an integrated VO2–silicon optical memory stores a material state and reads it through changed optical transmission. A ferroelectric Pockels photonic memory has demonstrated six distinguishable optical states with repeatability and long retention. These are external demonstrations, not Horizon hardware.

The present simulation goes one step further conceptually by making the causal A/B protocol explicit, but it remains a model.

## Research status

Classification:
- Established physics: resonant wave response and state-dependent response are physically plausible.
- Mathematical deduction: the simulated A/B causal effect.
- Simulation result: PASS for the stated numerical model.
- Physical experiment: NOT PERFORMED.
- Horizon WCR: NOT VALIDATED.
- Next gate: locate or perform an external physical experiment that reproduces the A/B protocol with identical later input.

## Kill condition

The Horizon hypothesis should not claim success if a real device cannot produce a repeatable A/B output difference above measurement uncertainty, or if the state preparation, retention, readout, conversion, or correction overhead eliminates the intended computational advantage.
