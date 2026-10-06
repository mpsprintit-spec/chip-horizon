# HORIZON SCALABLE WAVE ARCHITECTURE

## Status

Research architecture. Target: a scalable Horizon supercomputer architecture that can be reduced to a smartphone-class chip without changing the underlying computational mechanism.

This document does not claim a fabricated device or demonstrated performance.

## 1. Architectural target

Horizon is one computational architecture expressed at different scales:

```
Wave Computational Region
        ↓
Wave Computational Core
        ↓
Region / Tile
        ↓
Chip
        ↓
Multi-chip system
        ↓
Horizon supercomputer
```

The scaling variable is primarily the number, size, connectivity, bandwidth, state capacity, and physical implementation of wave-computational regions. The fundamental computation should remain the same.

## 2. Wave Computational Region (WCR)

A WCR is a physical region in which the wave field evolves and interacts with nonlinear/state elements.

It is not equivalent to a conventional transistor or memory cell.

The conceptual flow is:

```
INPUT
  ↓
SPACE-TIME ENCODING
  ↓
WAVE FIELD
  ↓
PROPAGATION / COUPLING / INTERFERENCE
  ↓
NONLINEAR INTERACTION
  ↓
PHYSICAL STATE
  ↕
FEEDBACK
  ↓
READOUT
```

The wave field is the computational medium. State is part of the computational dynamics.

The term WCR is preferred when discussing architecture. Earlier documents may use WCC (Wave Computational Cell) for the mathematical unit `Y = AX`; WCC is retained as historical terminology and is not a commitment to a transistor-like physical cell.

## 3. Scaling rule

The architecture must satisfy:

```
same mechanism
+ more regions
+ controlled locality
+ hierarchical communication
= larger system
```

Scaling must not require an entirely different computational principle at the supercomputer level.

## 4. Locality

Full connectivity is rejected as a default scaling strategy because:

[
N_{connections}sim N^2
]

The preferred structure is local coupling plus hierarchical aggregation.

```
local WCRs
   ↓
local core
   ↓
tile
   ↓
cluster
   ↓
system
```

Only information that must cross hierarchy boundaries should do so.

## 5. Smartphone-scale expression

A mobile implementation is a reduced physical instance of the same architecture:

- fewer WCRs;
- shorter/localer communication paths;
- lower state capacity;
- lower total optical/wave power;
- smaller readout and control subsystem;
- tighter thermal and area constraints.

It is not a different algorithmic architecture.

## 6. Supercomputer-scale expression

A supercomputer implementation increases:

- WCR count;
- parallel wave-field capacity;
- aggregate state capacity;
- local interconnect capacity;
- number of tiles/clusters;
- aggregate I/O and memory resources.

The architecture must remain decomposable so that increasing scale does not force global synchronization or all-to-all communication.

## 7. Critical physical requirement

The following must eventually be demonstrated for a real WCR:

1. controllable wave propagation;
2. controllable coupling/interference;
3. useful nonlinear interaction;
4. measurable physical state;
5. state retention/update/reset or controlled decay;
6. feedback from state into subsequent computation;
7. measurable input/output function;
8. energy and latency that include encoding, propagation, state, readout, control, and correction.

Failure of any essential mechanism is a potential architecture kill condition.

## 8. Validation direction

Validation proceeds from the already-defined target architecture downward:

```
Horizon supercomputer requirements
        ↓
scalable system requirements
        ↓
tile/core requirements
        ↓
WCR requirements
        ↓
physical observables
        ↓
existing external measurement methods
        ↓
physical experiment
```

A simpler experiment is acceptable only when it isolates a necessary mechanism of the target architecture. It must not redefine the target.

## 9. Epistemic status

Established physics:
- electromagnetic/optical fields propagate and interfere;
- physical media can exhibit nonlinear and state-dependent behavior;
- hierarchical/local architectures can reduce communication requirements compared with unrestricted all-to-all connectivity.

Engineering hypotheses:
- STWF can combine wave propagation, nonlinear interaction, and persistent physical state into a useful computational mechanism;
- the same mechanism can scale from mobile-class silicon-area constraints to a much larger computing system;
- state reuse and physical parallelism can provide useful system-level advantages.

Unresolved:
- final wave medium;
- final state medium;
- achievable precision;
- loss and noise;
- conversion overhead;
- fabrication method;
- energy/op;
- latency;
- density;
- scaling limits;
- comparison against electronic and photonic baselines.

