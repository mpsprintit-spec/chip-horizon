# STATEFUL CORE SIMULATOR V0.1

## Purpose

Test the minimum mathematical dynamics required by the STWF Stateful Core before selecting a physical material.

Classification: mathematical research model / proposed experiment. It is not a hardware result.

## Core equation

The first-order model is:

S_(t+1) = lambda S_t + w X_t + epsilon_t

Y_t = g(S_t)

Parameters:
- lambda: retention/decay coefficient, 0 <= lambda <= 1
- w: input coupling
- X_t: input event
- epsilon_t: state/update noise
- g: readout function

## Test A — Ideal accumulator

Set:

lambda = 1
w = 1
epsilon = 0

For X = [3, 5, 2, 7]:

S = [3, 8, 10, 17]

Expected property: state is reused directly rather than recomputing the complete history.

## Test B — Leaky state

Set:

0 < lambda < 1

Example:

S_(t+1) = 0.9 S_t + X_t

The resulting state represents a weighted temporal history:

S_t = sum_k lambda^k X_(t-k)

This is a temporal filter, not an ideal accumulator.

## Test C — Noise tolerance

Sweep epsilon under controlled distributions.

Measure:
- absolute state error
- relative state error
- error growth with event count
- recovery after reset
- output signal-to-noise ratio

## Test D — Retention sweep

Sweep lambda across:

0, 0.1, 0.5, 0.9, 0.99, 0.999, 1

Measure:
- useful state lifetime
- accumulated error
- response to sparse events
- response to burst events

## Test E — Recurrent matrix state

Extend to:

S_(t+1) = A S_t + B X_t

Y_t = C S_t + D X_t

This is the first bridge from a scalar state cell to a network of stateful cells.

## Physical mapping metrics

For each candidate material/mechanism, eventually estimate:

- retention time tau
- update energy E_update
- read energy E_read
- write energy E_write
- update latency
- state precision
- noise
- endurance
- variability
- reset cost
- coupling efficiency
- conversion overhead

## Energy accounting

Do not count only energy inside the wave/state medium.

Use:

E_total = E_source + E_encoding + E_field + E_state + E_nonlinear + E_read + E_control + E_memory + E_correction

A candidate is not considered efficient until end-to-end energy is estimated.

## Kill criteria

Reject or revise a mechanism if:
1. state error diverges for the target workload;
2. retention cannot be controlled;
3. read/write energy dominates;
4. conversion overhead dominates;
5. required precision is incompatible with noise/variability;
6. scaling causes impractical communication or coupling;
7. no advantage remains against an electronic baseline.

## Next stage

After the scalar simulator is validated, build:
1. vector state;
2. local coupled cells;
3. nonlinear state update;
4. wave/state feedback;
5. material-to-operator comparison.

No final material choice is made by this document.
