# Independent Multidimensional-State WCR Simulation v0.3

Date: 7 October 2026

## Objective

Test whether a WCR can carry more than one internal physical state coordinate at the same time, while the external probe remains identical.

This experiment addresses the next falsifiable gate after v0.2:

    S = (q, phi)

where q represents a state-dependent detuning coordinate and phi represents a state-dependent phase coordinate.

This is a numerical experiment only. It is not a physical validation of Horizon hardware.

## Model

The simulated resonant WCR uses:

    a_(t+1) = rho*a_t + kappa*sqrt(P)/(1 + i*K*q)*exp(i*phi)

with:

- rho = 0.92
- kappa = 0.28
- K = 3.2
- P = 1.0

The external probe P is identical for every state.

The internal state changes the physical response through q and phi.

The complex field amplitude a is retained as the observable. Both quadratures are measured:

    Y = (Re(a), Im(a))

This is deliberate. If only intensity |a|^2 is measured, phase information is discarded.

## Experiment 1 — four combinations of two state dimensions

Prepared states:

    S1 = (q=0.25, phi=0)
    S2 = (q=0.25, phi=pi/2)
    S3 = (q=0.75, phi=0)
    S4 = (q=0.75, phi=pi/2)

The same external probe P=1.0 was applied to all four conditions.

After 100 recurrence steps, the final 20 samples were averaged.

Measured complex-state outputs:

| State | Re(a) | Im(a) | Magnitude | Phase |
|---|---:|---:|---:|---:|
| S1 | 2.132884 | -1.706307 | 2.731425 | -0.674741 rad |
| S2 | 1.706307 | 2.132884 | 2.731425 | 0.896055 rad |
| S3 | 0.517445 | -1.241868 | 1.345358 | -1.176005 rad |
| S4 | 1.241868 | 0.517445 | 1.345358 | 0.394791 rad |

All four states are distinguishable in the two-dimensional measurement space (Re(a), Im(a)).

## Critical control

The input is identical for all four states:

    P = 1.0

The phase coordinate is part of the internal state in this model; it is not changed in the external probe.

Therefore the experiment tests:

    same input
        +
    different multidimensional internal state
        ->
    different complex output

## Experiment 2 — noise tolerance

4,000 total noisy classifications were performed for each tested noise level using nearest-state classification in the two-dimensional output plane.

| Noise std per quadrature | Classification accuracy |
|---:|---:|
| 0.01 | 100.0% |
| 0.05 | 100.0% |
| 0.10 | 100.0% |
| 0.20 | 100.0% |
| 0.50 | 93.75% |

The four-state representation remains distinguishable under substantial numerical measurement noise, although classification degrades at the highest tested noise.

## Important finding

Intensity-only readout would collapse S1 and S2:

    |a(S1)| = |a(S2)|
    |a(S3)| = |a(S4)|

Therefore a scalar intensity detector would lose the phase dimension.

A phase-sensitive or coherent readout is required if phase is intended to carry computational state.

This is an architectural constraint, not merely an implementation detail.

## Interpretation

### PASS

- Two internal coordinates can coexist in the model.
- The same external input can interrogate different combinations of those coordinates.
- The combinations produce distinct outputs when both amplitude and phase quadratures are retained.
- Measurement dimensionality directly affects usable state capacity.

### FAIL / LIMITATION OBSERVED

A detector that measures only scalar intensity cannot recover the phase coordinate in this experiment.

This is a useful failure because it identifies a concrete requirement:

    rich internal state -> matching rich readout

A richer internal representation does not automatically create useful computational information if the readout collapses the state dimensions.

## What this does NOT prove

- that real amplitude and phase state variables can be independently stored in one material/device;
- that q and phi can be independently written;
- that their dynamics remain independent under real nonlinear interactions;
- that the state can be retained for useful time;
- that the state can be reset cheaply;
- that coherent detection is energy-efficient enough;
- that the mechanism is manufacturable at smartphone scale;
- that it beats CMOS;
- that it scales to a supercomputer.

## Architectural consequence

The Horizon WCR abstraction should be treated as a vector physical state rather than a scalar memory level:

    S = (S1, S2, ... , Sn)

where each coordinate must have:

1. physical origin;
2. controlled write mechanism;
3. retention/decay law;
4. interaction with computation;
5. measurable readout;
6. acceptable cross-talk;
7. acceptable noise;
8. reset/forget mechanism.

A candidate coordinate is not accepted merely because it exists physically.

## Next experiment

The next gate should introduce **nonlinear cross-coupling between the two state coordinates**.

Test:

    S_(t+1) = F(S_t, X_t)

where q and phi alter each other through the same nonlinear interaction.

The critical question becomes whether the multidimensional state survives nonlinear coupling without collapsing into a single effective scalar state.

A physical candidate should ultimately be tested using the same principle with externally measured quadratures and state preparation.

## Research status

- Numerical multidimensional state: PASS.
- Same-input causal response: PASS in model.
- Intensity-only readout: FAIL to preserve both dimensions.
- Physical implementation: NOT TESTED.
- Material independence of state coordinates: NOT PROVEN.
- Horizon WCR: NOT VALIDATED.
