# STWF SIMULATOR V0.2

## Purpose

V0.2 extends the scalar Stateful Core model into a reproducible, dependency-free Python simulator for the first mathematical/physical-analogue tests of STWF.

This is a research simulator, not evidence of hardware feasibility.

## Model

The core state equation is:

S_(t+1) = lambda S_t + A_c S_t + B X_t + epsilon_t

For the first implementation, A_c is represented by a configurable coupling matrix. The equivalent vector model is:

S_(t+1) = f(A S_t + B X_t + epsilon_t)

Y_t = g(C S_t + D X_t)

where:

- S: internal reusable state vector
- X: input vector
- A: state-to-state coupling
- B: input-to-state coupling
- C: state readout matrix
- D: direct input readout
- f: optional nonlinear state function
- g: output/readout function
- epsilon: update noise

## Physical analogue

The simulator exposes parameters that can later be mapped to physical mechanisms:

| Mathematical parameter | Physical interpretation |
|---|---|
| A | coupling, interference, phase, geometry |
| B | input coupling |
| lambda | state retention / decay |
| epsilon | physical noise / variability |
| f | nonlinear material/state interaction |
| C,D | readout coupling |
| delay | propagation or resonant delay |
| saturation | nonlinear amplitude limit |

For an exponential state lifetime:

lambda = exp(-Delta_t / tau)

therefore:

tau = -Delta_t / ln(lambda)

This relation allows simulation results to be translated into a required physical state lifetime.

## Tests

### Test 1 — Scalar accumulator

S_(t+1) = S_t + X_t

Input:

[3, 5, 2, 7]

Expected state:

[3, 8, 10, 17]

### Test 2 — Leaky state

S_(t+1) = lambda S_t + X_t

Sweep lambda:

[0, 0.5, 0.9, 0.99, 0.999, 1]

Measure effective memory and accumulated error.

### Test 3 — Noise

Add controlled epsilon to every update.

Measure:

- absolute error
- relative error
- RMS error
- error growth
- signal-to-noise ratio

### Test 4 — Vector recurrence

S_(t+1) = A S_t + B X_t

Check stability using the spectral radius of A.

A first mathematical warning condition is:

rho(A) >= 1

for an otherwise linear, discrete-time autonomous system. This is not a complete physical stability criterion.

### Test 5 — Nonlinear state

Compare:

S_(t+1) = A S_t + B X_t

against:

S_(t+1) = f(A S_t + B X_t)

with saturation and threshold functions.

### Test 6 — Delay

Introduce per-path delay before coupling.

The purpose is to test whether temporal alignment can act as a computational parameter.

## Required outputs

Every simulation run should report:

- final state
- state trajectory
- output trajectory
- RMS error
- maximum error
- stability indicator
- effective retention
- estimated tau
- parameter set
- seed when noise is enabled

## Important limitation

The simulator can establish mathematical behavior and sensitivity, but cannot establish that a real material can implement the model.

The next physical bridge is:

mathematical A/B/lambda/f
-> physical coupling/loss/delay/nonlinearity
-> electromagnetic or other wave solver
-> fabricated-device experiment

## Kill conditions

Stop or redesign if:

1. useful computation requires unrealistic precision;
2. noise overwhelms state;
3. stable operation requires excessive loss compensation;
4. delays destroy computational timing;
5. nonlinear elements dominate energy;
6. readout/conversion dominates total energy;
7. no credible advantage remains over an electronic baseline.

## Status

V0.2 is a mathematical simulator specification.

Classification:
- Established physics: decay, linear state-space dynamics, noise, wave propagation concepts.
- Mathematical deduction: lambda-to-tau mapping and stability analysis.
- Proposed synthesis: stateful wave computational cell.
- Experimental result: none yet.
