# Independent Rich-State WCR Simulation v0.2

Date: 7 October 2026

## Objective

Extend the previous causal simulation from a binary A/B state demonstration toward the Horizon requirement of a **rich internal physical state** while preserving binary external I/O.

This remains a numerical experiment. It is not a physical device validation.

## Model

The simulated WCR is a resonant wave region with:

- complex internal wave amplitude a;
- state variable q;
- state-dependent detuning Delta = K*q;
- wave recurrence a_next = rho*a + kappa*sqrt(P)/(1 + i*Delta);
- observable output Y = |a|^2.

Parameters:

- rho = 0.97
- kappa = 0.22
- K = 4.0
- P = 1.0

The same probe input is used for every state.

## Experiment 1 — six distinguishable internal states

Six prepared states were selected:

    q = 0.05, 0.20, 0.35, 0.50, 0.65, 0.80

After identical probing, the mean output values were:

    51.1688
    32.4485
    17.9782
    10.6431
     6.8577
     4.7345

All six outputs are distinct in this model.

This demonstrates a numerical mapping:

    multiple internal states
          +
    identical external probe
          ↓
    multiple distinguishable outputs

The result is compatible with the Horizon rich-state hypothesis, but it does not prove that a physical WCR can realize six equally reliable states.

## Experiment 2 — readout noise tolerance

For each of the six states, 1,000 noisy readout trials were generated. The state was classified by nearest expected output.

Accuracy:

| Output noise std | Six-state classification accuracy |
|---:|---:|
| 0.01 | 100.0% |
| 0.10 | 100.0% |
| 0.50 | 99.4% |
| 1.00 | 94.1% |
| 2.00 | 82.8% |

This establishes a useful design constraint: increasing state count is only useful if state separation remains large relative to measurement noise.

## Experiment 3 — state retention

The internal state was allowed to decay before the identical probe was applied.

For decay law:

    q(t) = q0 * exp(-t/tau)

the model was evaluated after a delay of 20 simulation units.

For tau=10, 50, 200, the six state outputs remained ordered, but their separation changed.

The result demonstrates that retention time is not merely a memory-storage specification; it changes the computational readout.

## Interpretation

### PASS

1. A single WCR model can contain more than two distinguishable internal states.
2. The same external input can interrogate different internal states and produce different outputs.
3. State distinguishability can be quantified under measurement noise.
4. State decay changes the computation/readout and therefore can act as a computational parameter.

### NOT PROVEN

- that the six states correspond to six independent computational symbols;
- that a real material can maintain these states with the same separation;
- that state transitions are energy-efficient;
- that writing/reading is cheaper than binary electronics;
- that multiple state dimensions can coexist independently;
- that phase, amplitude, frequency, timing and material state can all be used simultaneously;
- smartphone-scale fabrication;
- supercomputer-scale networking.

## Important conclusion

The experiment does **not** justify saying:

    "six states = six bits"

That would be incorrect.

The correct statement is:

    six reliably distinguishable physical states
    provide log2(6) approximately 2.585 bits of single-shot
    information capacity under ideal noiseless encoding.

More generally:

    information capacity = log2(N)

only when N states are reliably distinguishable and usable with the required error rate.

For computation, distinguishability alone is insufficient. The states must also be writable, transformable, readable, retainable/resettable, and causally coupled to subsequent computation.

## Architectural implication

The WCR should therefore not be defined as merely a binary gate.

A more accurate abstraction is:

    WCR = physical state space + dynamical transformation

with:

    S_(t+1) = F(S_t, X_t)

and:

    Y_t = G(S_t, X_t)

where S may contain several physical coordinates:

    S = (amplitude, phase, frequency, timing, spatial mode, material state)

The simulation only validates a one-dimensional state coordinate q. The other coordinates remain open research questions.

## Research status

- Mathematical model: PASS for tested causal and multi-state behavior.
- Rich-state numerical demonstration: PASS.
- Noise robustness: PASS within tested ranges; accuracy degrades as expected.
- Retention dependence: PASS in the model.
- Physical material validation: NOT TESTED.
- Complete WCR validation: NOT TESTED.
- Binary I/O compatibility: architecture-level design, not physical validation.

## Next falsifiable gate

The next independent experiment should test **two or more physical state dimensions simultaneously**, rather than simply increasing the number of scalar levels.

Candidate:

    S = (amplitude, phase, material_state)

with identical binary-derived probe input and a readout that determines whether the dimensions remain independently distinguishable after nonlinear interaction.

A physical experiment should reject the hypothesis if state dimensions collapse, become strongly correlated, cannot be independently written/read, or the encoding/decoding overhead dominates the intended computational benefit.
