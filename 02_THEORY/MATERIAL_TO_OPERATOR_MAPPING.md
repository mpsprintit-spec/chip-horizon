# MATERIAL-TO-OPERATOR MAPPING

## Status

This document records the 2026-10-04 research discussion following the STWF Stateful Core work.

**Classification:** proposed research synthesis / hypothesis. It is not an experimental result and does not establish that any candidate material can implement the complete STWF architecture.

## Core principle

Do not select a material first and force the architecture to fit it.

The intended order is:

```
Computation
  ↓
State dynamics
  ↓
Physical mechanism
  ↓
Material
  ↓
Hardware
```

The current Stateful Core target is:

`[
S_{t+1}=F(S_t,X_t)
]]

For the coupled STWF formulation:

`[
Psi_{t+1}=G(Psi_t,X_t,S_t)
]

[
S_{t+1}=F(S_t,Psi_{t+1})
]

[
Y_t=R(Psi_t,S_t)
]`

## Functional layers

### 1. Wave medium

Required properties:
- propagation
- interference
- controllable phase/amplitude or equivalent state variables
- coupling
- delay
- acceptable loss

Candidate classes:
- photonic/optical
- magnonic/spin-wave
- electromagnetic/RF
- phononic/acoustic

### 2. State medium

Required properties:
- state modification by input
- retention
- controlled update
- decay/reset/forgetting
- interaction with the wave field

Candidate classes:
- memristive/resistive-switching materials
- ferroelectric materials
- phase-change materials
- magnetic/spintronic state systems
- resonant physical states

### 3. Nonlinear element

Required for functions beyond purely linear transformation:

`[
F(a+b)
eq F(a)+F(b)
]`

Potential functions:
- thresholding
- saturation
- switching
- gain
- state-dependent coupling

## Candidate assessment

### Magnonic / spin-wave systems

Primary hypothesis: strong candidate for the wave layer.

Relevant properties:
- propagating collective spin excitations
- amplitude and phase
- interference/coupling
- potentially useful nonlinear dynamics

Main unresolved issues:
- efficient state retention
- read/write overhead
- reproducibility and variability
- integration and scaling
- whether total system energy is competitive

### Memristive / oxide systems

Primary hypothesis: strong candidate for the physical state layer.

The internal state can conceptually follow:

`[
m_{t+1}=F(m_t,V_t)
]`

which structurally resembles the Stateful Core requirement.

Main unresolved issues:
- analog/multilevel precision
- device variability
- endurance
- retention/update trade-offs
- wave coupling mechanism

### Ferroelectric systems

Primary hypothesis: candidate for state plus nonlinear interaction.

Polarization can be treated abstractly as:

`[
P_{t+1}=F(P_t,E_t)
]`

Main unresolved issues:
- integration with a wave field
- state precision
- switching energy
- retention and cycling
- scalable readout

### Photonic systems

Primary hypothesis: strong candidate for the wave/interference layer.

Advantages to investigate:
- high propagation speed
- coherent amplitude/phase manipulation
- natural interference

Main unresolved issue:
- persistent state and nonlinear computation may require additional materials/devices, and electro-optical conversion can dominate total system energy.

## Hybrid hypothesis

A single material does not need to perform every function.

A candidate computational cell may instead combine:

```
Wave medium
    ↓
Interference / coupling
    ↓
Nonlinear interaction
    ↓
State medium
    ↓
Feedback to wave medium
```

Therefore the relevant research object is the **computational cell**, not an isolated material.

## Critical representation problem

For optical or other field-based implementations, intensity measurement may yield:

`[
Ipropto |A|^2
]`

which does not directly preserve the sign of a scalar state.

Possible representations to investigate:
- dual-rail representation
- phase encoding
- coherent/phase-sensitive detection
- other signed state encodings

No choice has been finalized.

## State contamination

A physical state may not implement an ideal accumulator:

`[
S_{t+1}=S_t+X_t
]`

and may instead behave approximately as:

`[
S_{t+1}=lambda S_t+wX_t+epsilon_t
]`

This can be an error source, but for controlled `lambda` it can also implement a temporal filter:

`[
S_t=sum_k lambda^k X_{t-k}
]`

Therefore material lifetime/decay may become a computational parameter rather than merely an imperfection.

## Current research position

No material is selected as the final STWF substrate.

The current priority is:

1. define required operators;
2. simulate Stateful Core dynamics;
3. map each operator to physical mechanisms;
4. compare candidate material classes;
5. estimate end-to-end energy, latency, precision, area, retention, and conversion overhead;
6. reject architectures that fail these tests.

## Kill test

A material/architecture combination should be rejected or revised if:

- conversion energy dominates the computation;
- state cannot be controlled with adequate precision;
- accumulated error grows uncontrollably;
- read/write overhead removes the expected benefit;
- scaling requires impractical connectivity;
- no measurable advantage remains against an appropriate electronic baseline.

## Classification boundary

Established physics: wave propagation, interference, material state dynamics, nonlinear physical phenomena.

Proposed synthesis: combining wave computation with persistent physical state in the STWF Stateful Core.

Hypothesis: a heterogeneous wave/state computational cell could reduce data movement by making state part of computation.

Unresolved: whether such a system can outperform conventional electronic computing in a complete end-to-end workload.
