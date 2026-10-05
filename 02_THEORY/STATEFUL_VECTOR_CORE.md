# STATEFUL VECTOR CORE

## Purpose

Extend the scalar Stateful Core into a coupled vector state:

S_(t+1) = A S_t + B X_t

Y_t = C S_t + D X_t

This is a mathematical target for physical realization, not evidence of a working hardware implementation.

## Why vector state matters

A scalar state can accumulate or filter one quantity. A vector state permits multiple coupled internal variables.

S = [S1, S2, ..., Sn]^T

The matrix A defines state-to-state coupling.

B defines input coupling.

C and D define readout/direct paths.

## Physical interpretation

In STWF, the matrix A should eventually be interpreted as a physical network of couplings, delays, phases, losses, and state interactions rather than as a conventional digital matrix multiply.

A conceptual mapping is:

A_ij -> coupling strength / transmission / phase / delay / nonlinear state-dependent response

This mapping remains a hypothesis until demonstrated physically.

## Nonlinear extension

The next model is:

S_(t+1) = f(A S_t + B X_t)

Y_t = g(C S_t + D X_t)

where f and g are physical nonlinear/readout functions.

Candidate nonlinear mechanisms may include:
- thresholding
- saturation
- hysteresis
- state-dependent coupling
- nonlinear wave interaction

No specific mechanism is selected yet.

## Minimal 2-state example

Let:

A = [[0.9, 0.2],
     [-0.1, 0.8]]

B = identity

and:

X_t = [x1_t, x2_t]^T.

Then:

S1_(t+1) = 0.9 S1_t + 0.2 S2_t + x1_t

S2_(t+1) = -0.1 S1_t + 0.8 S2_t + x2_t

The off-diagonal terms represent internal coupling.

The negative coefficient is not yet a statement about a particular device. It defines a mathematical requirement that a physical implementation must realize through an appropriate signed/phase representation.

## Test objectives

Measure:
1. state stability
2. controllability
3. observability
4. precision
5. noise accumulation
6. retention
7. update latency
8. energy per state update
9. coupling overhead
10. scalability

## Stability

For the linear model, the eigenvalues of A determine whether state magnitude tends to decay, remain bounded, or diverge.

For a stable linear system:

|lambda_max(A)| < 1

where lambda_max denotes the eigenvalue with largest magnitude.

This criterion is mathematical. Physical stability additionally depends on nonlinearities, noise, saturation, material variation, and feedback delay.

## Important physical constraint

A mathematical matrix coefficient is not automatically a free physical parameter.

Changing A_ij may require:
- changing geometry
- changing coupling
- changing material properties
- changing phase
- changing path length
- changing resonant conditions
- active control

The physical cost of programming A must therefore be included in later energy and area analysis.

## Next bridge

The immediate research bridge is:

mathematical A
    ↓
physical coupling network
    ↓
wave propagation/interference
    ↓
state update
    ↓
new vector state

The goal is to determine whether a small vector state can be realized without converting every interaction into conventional digital arithmetic.
