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


## 3A. Target computational loop

The minimum target loop is:

    X_t
      |
      v
    space-time encoding
      |
      v
    wave field
      |
      v
    propagation + coupling + interference
      |
      v
    nonlinear/state interaction
      |
      v
    S_(t+1)
      |
      +---- feedback ----> wave field
      |
      v
    readout
      |
      v
    Y_t

Mathematically:

S_(t+1) = F(S_t, X_t)

Psi_(t+1) = H(Psi_t, S_t, X_t, C_t)

Y_t = G(Psi_t, S_t)

The exact physical forms of F, H, and G remain unresolved.

## 3B. Physical representation

The architecture does not assume ordinary binary voltage states as its fundamental representation.

Candidate physical degrees of freedom include:

- amplitude;
- phase;
- arrival time;
- spatial mode;
- frequency;
- polarization or another physical mode where appropriate;
- persistent material state.

The final representation must be selected from measured noise, bandwidth, stability, fabrication, and energy constraints.

## 3C. Wave layer

The wave layer performs physical evolution through propagation, coupling, interference, phase transformation, delay, spatial routing, and resonance where useful.

A conceptual field is:

Psi(x,y,z,t) = A(x,y,z,t) exp(i phi(x,y,z,t))

For coupled paths:

E_j(t) = sum_i W_ij E_i(t - tau_ij) + N_j(t)

where W_ij represents the physical transformation and tau_ij represents propagation or engineered delay.

The wave layer alone is not assumed to be a complete computer.

## 3D. Nonlinear and state layer

The state layer provides history dependence:

S_(t+1) = F(S_t, E_t)

Possible functions include thresholding, comparison, switching, saturation, state-dependent coupling, retention, controlled decay, reset, and selective overwrite.

A useful mathematical model is:

S_(t+1) = lambda S_t + w X_t + epsilon_t

This is a model, not a selected physical implementation.

## 3E. Feedback

Feedback is essential to the target stateful architecture.

Wave field -> state -> state-dependent interaction -> wave field.

Without feedback, a device may behave primarily as a feed-forward wave processor.

With feedback, prior state can influence subsequent computation. Feedback must be evaluated for stability, delay, noise accumulation, gain/loss balance, state contamination, energy, and reset behavior.

## 3F. Locality and hierarchy

Full connectivity is rejected as the default scaling strategy because:

N_connections ~ N^2

The preferred structure is local coupling plus hierarchical aggregation:

WCR -> Core -> Tile -> Cluster -> Chip -> Multi-chip system -> Supercomputer

Only information that must cross hierarchy boundaries should do so.

Global synchronization is not assumed to be necessary for every computation.

## 3G. Core and tile

A core is a group of WCRs whose interactions are predominantly local.

A tile is a larger locality domain containing multiple cores and a controlled inter-region communication boundary.

This separates:

1. physical computation inside a WCR;
2. local computation among WCRs;
3. tile-level coordination;
4. cluster/system-level communication.

This does not imply conventional CPU-style instruction execution.

## 3H. Chip-level architecture

A Horizon chip is a physical array of WCRs organized into cores and tiles.

Conceptually:

    CHIP
      |
      +-- Tile 0 <-> Tile 1 <-> Tile 2
      |      |           |           |
      |    local WCR   local WCR   local WCR
      |
      +-- encoding / readout / control / I/O

Encoder, readout, control, and I/O are system interfaces. Their energy and latency must nevertheless be included in the complete system budget.

## 3I. Multi-chip and supercomputer architecture

Multiple chips form a hierarchy:

Chip -> Node -> Cluster -> Supercomputer

Scaling should increase computational capacity without requiring every WCR to communicate with every other WCR.

Required system-level properties include locality, hierarchical routing, bounded communication domains, distributed state where appropriate, aggregation at hierarchy boundaries, and explicit treatment of synchronization or event coordination.

## 3J. Scaling invariants

The following should remain invariant across scale:

- underlying stateful computation;
- physical meaning of wave/state interaction;
- local computational principle;
- feedback principle;
- observable input/output relationship.

The following may scale:

- WCR count;
- physical area;
- bandwidth;
- state capacity;
- hierarchy depth;
- parallelism;
- aggregate I/O;
- aggregate energy and cooling capacity.

## 3K. Critical physical requirements

A real WCR must eventually demonstrate:

1. controllable wave propagation;
2. controllable coupling/interference;
3. useful nonlinear interaction;
4. measurable physical state;
5. state retention, update, reset, or controlled decay;
6. feedback from state into subsequent wave computation;
7. measurable input/output function;
8. reproducible behavior;
9. energy and latency accounting including encoding, propagation, state, readout, control, and correction.

Failure of an essential mechanism is a potential architecture kill condition.

## 3L. Performance quantities

The architecture will eventually be evaluated using throughput, latency, energy/op, area/op, state density, communication overhead, correction overhead, and effective computational bandwidth.

A state-reuse metric is:

SRR = reusable computation / total computation

No numerical target is declared until the physical implementation is defined.

## 4. Locality

Full connectivity is rejected as a default scaling strategy because:

[
N_connections ~ N^2
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

