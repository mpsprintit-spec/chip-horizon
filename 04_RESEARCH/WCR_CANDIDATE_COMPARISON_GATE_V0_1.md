# WCR Candidate Comparison Gate v0.1

## Purpose

This document is the decision gate between the two current physical mechanism families:

- photonic field + nonlinear/state element
- magnonic/spin-wave field + magnetic state

No final platform is selected here.

## 1. Shared Horizon requirement

Both candidates must satisfy the same architecture:

BINARY INPUT
→ ENCODER
→ RICH PHYSICAL INTERNAL COMPUTATION
→ DECODER
→ BINARY OUTPUT

The internal state may contain multiple simultaneously measurable physical coordinates. This does not make the system quantum.

The decisive mechanism is:

prior physical state
→ later transformation
→ measurable state-dependent output.

## 2. Common causal experiment

For either platform:

### Preparation

Create two reproducible states:

S_A and S_B

with a measured separation greater than preparation uncertainty.

### Probe

Apply exactly the same later input:

X_0

### Readout

Measure:

Y_A and Y_B

### Causal gate

Require:

|Y_A - Y_B| > U_total

where U_total represents the complete uncertainty budget of preparation, instrument, synchronization, environmental variation, and readout.

### Repeatability

Repeat the A/B sequence independently.

A single visually different trace is insufficient.

## 3. Candidate scorecard

| Criterion | Photonic | Magnonic |
|---|---|---|
| Propagating wave field | strong | strong |
| Interference/phase control | strong | strong |
| Demonstrated nonlinearity | strong | strong |
| Persistent state candidate | strong | strong |
| Dense integrated routing | strong candidate | improving |
| Fast readout | strong | strong candidate |
| Binary electrical interface | mature | mature at RF/microwave level |
| State-control complexity | unresolved | unresolved |
| Conversion overhead | critical risk | critical risk |
| Thermal/noise sensitivity | critical | critical |
| Smartphone-scale fabrication | more mature ecosystem | major unresolved issue |
| Horizon-specific stateful causal proof | not yet demonstrated | not yet demonstrated |

This table is a research screening, not a benchmark of final devices.

## 4. Current external evidence

Photonic research has recently demonstrated programmable nonlinear optical functionality and photonic memory-compute integration. A 2026 Nature Sensors report describes a 7,378-neuron monolithic in-memory photonic chip with long- and short-term memory dynamics, showing that integration of memory and photonic computation is experimentally plausible. citeturn0search1turn0search0

Magnonic research has demonstrated low-loss submicrometre spin-wave waveguides and large crossing networks, as well as nonlinear coherent spin-wave dynamics. This makes the wave/state direction physically credible, but chip-scale general-purpose computation remains an open engineering problem. citeturn0search5turn0search6

These demonstrations are **prior art and physical evidence**, not evidence that Horizon has already achieved the proposed architecture.

## 5. Decision rule

Do not choose the platform based on:

- visual appearance;
- nominal number of states;
- theoretical energy alone;
- published peak bandwidth alone;
- analogy to the brain;
- analogy to quantum computing.

Choose based on measured:

1. number of reliably distinguishable states;
2. state transition controllability;
3. retention/decay;
4. state-dependent output contrast;
5. repeatability;
6. noise margin;
7. write energy;
8. read energy;
9. operation energy;
10. latency;
11. conversion overhead;
12. physical density;
13. reset cost;
14. fabrication tolerance;
15. scalability toward smartphone-class integration.

## 6. First experimental gate

The next real-world objective is not to build a Horizon chip.

It is to identify an existing external experiment/platform where the following causal test can be performed without building custom measurement infrastructure:

PREPARE S_A
→ APPLY X_0
→ MEASURE Y_A

PREPARE S_B
→ APPLY X_0
→ MEASURE Y_B

If the state-dependent difference is not statistically and physically significant, the candidate mechanism is rejected or redesigned.

If it passes, the next gate measures retention, nonlinear response, energy, latency, and scaling constraints.

## 7. Research status

Established:
- wave propagation, interference, nonlinear dynamics, memory/state phenomena.

Deduction:
- rich internal state can only be computationally useful if it participates causally in later transformation.

Hypothesis:
- a compact WCR can combine multiple physical degrees of freedom with persistent state to compute internally without forcing every internal variable into binary representation.

Engineering question:
- whether such a WCR can be fabricated densely, controlled reliably, cascaded, and connected to binary I/O at smartphone-chip scale.

Not demonstrated:
- general-purpose Horizon computation
- claimed energy advantage
- claimed speed advantage
- universal computation
- supercomputer scaling.
