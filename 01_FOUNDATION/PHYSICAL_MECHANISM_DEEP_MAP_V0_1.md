# Horizon Physical Mechanism Deep Map v0.1

Date: 7 October 2026
Status: research synthesis / candidate mechanism analysis
Scope: physical mechanism behind a Wave Computational Region (WCR)

## 1. Research objective

Horizon is not being defined as a replacement for the external digital ecosystem.

Current system-level target:

binary input -> interface/encoder -> rich physical internal computation -> decoder/readout -> binary output

The internal computational substrate is therefore allowed to use physical state variables richer than binary logic, while preserving compatibility at the system boundary.

Central physical question:

> Can a compact physical region carry a propagating computational field and a persistent internal state that causally modify one another, so that the region performs useful computation without reducing every internal operation to binary switching?

This document does not claim that such a Horizon device has been demonstrated.

## 2. Mechanism stack

The proposed WCR mechanism is decomposed into five causal layers:

INPUT FIELD -> FIELD EVOLUTION -> NONLINEAR INTERACTION -> STATE UPDATE -> FEEDBACK -> LATER FIELD RESPONSE

A sixth layer performs observation:

LATER FIELD RESPONSE -> READOUT -> DIGITAL OUTPUT

### 2.1 Field

Physical entity:
- electromagnetic field / optical mode, or another propagating collective excitation.

Potential variables:
- amplitude
- phase
- frequency
- timing
- spatial mode
- polarization or analogous mode degree of freedom

Established physics:
- waves propagate;
- waves interfere;
- phase and amplitude affect interference;
- propagation can introduce delay and loss.

Horizon synthesis:
- treat the complete physical field configuration as an internal computational state rather than immediately reducing it to binary symbols.

### 2.2 Interaction

Physical mechanisms:
- coupling
- interference
- resonance
- scattering
- field-mediated interaction

Established physics:
- interacting waves can redistribute energy and phase;
- coherent magnon modes can interfere and control spin-current properties;
- integrated photonic devices can implement programmable nonlinear transformations.

Horizon synthesis:
- use interaction to transform the field before readout, rather than using waves only as communication carriers.

### 2.3 Nonlinearity

Required role:
- create transformations that cannot be represented as a purely linear superposition.

Possible physical sources:
- carrier dynamics
- optical nonlinearities
- magnetic nonlinear dynamics
- ferroelectric switching
- resistive/ionic state changes
- saturation or threshold behavior

Important constraint:
linear interference alone is not sufficient evidence of general-purpose computation.

### 2.4 Persistent state

Physical entity:
- material, magnetic, ferroelectric, resistive, resonant, or other physical state variable.

Required properties:
1. distinguishable states;
2. controlled state transition;
3. measurable retention;
4. controlled decay/reset;
5. state-dependent effect on a later input;
6. repeatability.

The key computational condition is:

S_(t+1) = F(S_t, X_t)

and not merely:

S = stored value

A state becomes computationally useful only when changing it changes the subsequent transformation.

### 2.5 Feedback

Feedback closes the causal loop:

field(t) -> state(t+1) -> field(t+1)

This is the main distinction between a passive wave-processing structure and the proposed stateful WCR.

The feedback path does not necessarily need to be a literal optical loop. It can be:
- direct physical coupling;
- material-state modulation of propagation;
- magnetic back-action;
- electro-optic coupling;
- field-dependent conductance;
- resonant recirculation.

The implementation is unresolved.

## 3. Candidate mechanism A — photonic field + physical state

### Physical chain

optical input -> waveguide/mode -> interference/coupling -> nonlinear/state element -> modified optical response -> readout

What physically moves:
- electromagnetic field.

What physically stores state:
- candidate active material/device coupled to the optical field.

What changes the state:
- optical intensity, carrier excitation, electric field, thermal effect, or another controlled stimulus depending on implementation.

What changes the later wave:
- state-dependent absorption, phase shift, refractive index, coupling, gain/loss, resonance, or transmission.

### Established evidence

Programmable photonic nonlinear computing has been experimentally demonstrated; a 2025 Nature Photonics report demonstrated field-programmable nonlinear behavior in integrated photonics by controlling carrier excitations and their dynamics. This supports the existence of programmable photonic nonlinearity, not the complete Horizon WCR.

Integrated photonic latch memory has also been demonstrated as an optical set-reset memory concept, showing that optical processing can incorporate a stateful memory element rather than relying exclusively on electronic memory.

### Horizon relevance

Photonic WCR is currently the strongest candidate when:
- propagation density matters;
- phase/amplitude/mode are useful internal degrees of freedom;
- optical interconnect is valuable;
- state and nonlinearity can be co-integrated without excessive conversion overhead.

### Main unresolved problem

The critical question is not whether photonic computation exists.

It is whether a WCR can combine:
- rich internal field state,
- nonlinear transformation,
- persistent physical state,
- low-overhead feedback,
- reliable readout,
- and scalable fabrication

inside one repeatable computational region.

## 4. Candidate mechanism B — magnonic/spin-wave field + magnetic/spintronic state

### Physical chain

input excitation -> spin-wave propagation -> coherent interference/coupling -> magnetic state interaction -> modified spin-wave response -> electrical/optical readout

What physically moves:
- collective spin excitation / spin wave.

What stores state:
- magnetic configuration or spintronic state.

What changes the state:
- spin-wave interaction, spin torque, magnetic-field/electrical control, or coupled dynamics depending on implementation.

What changes the later wave:
- magnetic configuration changes the propagation, phase, amplitude, dispersion, coupling, or detection response.

### Established evidence

Coherent magnon interference has been experimentally used to control spin-current polarization, demonstrating that coherent spin-wave modes can interact in a computationally relevant manner.

### Horizon relevance

This candidate is particularly interesting because the wave-like computational variable and the persistent state can belong to the same physical family.

That potentially reduces the conceptual separation between:
- signal,
- state,
- interaction,
- and feedback.

### Main unresolved problem

The integration problem is severe:
- generation;
- detection;
- state preparation;
- state retention;
- noise;
- device variability;
- coupling efficiency;
- scaling density;
- compatibility with digital I/O.

Therefore this is a strong research candidate, not a selected final architecture.

## 5. Candidate mechanism C — ferroelectric state + field interaction

Ferroelectric polarization is already established as a switchable, nonvolatile physical state variable. Recent work demonstrates multilevel ferroelectric states and CMOS-compatible implementations, including experimental multi-bit operation in a 28 nm CMOS process.

A 2026 FeTFT study also demonstrated a device combining volatile and nonvolatile functions and reported multiple fading-memory responses and multilevel nonvolatile weights.

This is important for Horizon because it demonstrates that a physical device can expose more than two useful internal states.

However:

> Multiple states are not automatically a new computational mechanism.

The Horizon requirement is stronger:

prior physical state -> different later transformation

The state must participate causally in computation.

## 6. The richer-state hypothesis

A candidate WCR state should not initially be forced into a single scalar.

Conceptually:

S = (A, phase, frequency, timing, mode, material_state)

This is a candidate state description, not a claim that one device will independently control all six dimensions.

The dimensions are research axes.

A practical WCR may use only a subset:

### Photonic example

S = (A, phase, mode, material_state)

### Magnonic example

S = (A, phase, frequency, magnetic_state)

### Ferroelectric-assisted example

S = (conductance/polarization, transient_state)

The research objective is to determine which physical dimensions remain:
- controllable;
- distinguishable;
- stable;
- useful;
- scalable.

## 7. Binary boundary, rich internal computation

The system does not need to replace binary communication.

Example:

0010 -> Horizon -> 0100

For a digital system this can represent:

2 -> Horizon -> 4

Internally, the WCR does not need to represent 2 as 0010.

It could encode the input into a physical state such as:

S_in = (A, phase, timing, mode, material_state)

The physical evolution then produces:

S_out = F(S_in, S_internal)

The readout converts the result back into binary.

This creates a compatibility boundary:

DIGITAL WORLD | ENCODER | RICH PHYSICAL WORLD | DECODER | DIGITAL WORLD

The potential advantage is that the internal computational mechanism is no longer constrained to one binary transition per logical operation.

The potential disadvantage is that encoding and decoding may consume so much energy or latency that the end-to-end system gains nothing.

Therefore the comparison must always be end-to-end.

## 8. The decisive experiment

The first decisive physical experiment is not:

> Can the device store many levels?

It is:

> Can two different physical internal states cause measurably different responses to the same later input?

Define two prepared states:

S_A != S_B

Apply the same later input:

X_later = X_0

Measure:

Y_A = G(S_A, X_0)

Y_B = G(S_B, X_0)

The causal criterion is:

Y_A != Y_B

with the difference exceeding the complete measurement uncertainty and remaining reproducible over repeated trials.

This is the physical version of the Horizon stateful-computation claim.

## 9. Measurement ladder

Following D-012, Horizon should not build its own laboratory when established infrastructure can perform the measurement.

Minimum external measurement classes:

| Question | Observable | Existing measurement class |
|---|---|---|
| Does the field propagate? | amplitude / intensity / phase vs time/position | photodetector, optical power meter, oscilloscope/digitizer |
| Does interference occur? | phase/intensity redistribution | interferometric / phase-sensitive measurement |
| Is there nonlinearity? | output deviation from linear prediction | calibrated source + detector + parameter sweep |
| Does state change? | conductance, polarization, magnetic or optical response | SMU / parameter analyzer / magnetometry / spectroscopy |
| Does state persist? | response vs time after write | time-resolved electrical/optical measurement |
| Does state affect later input? | same-input/different-state output comparison | synchronized source + detector |
| Is behavior repeatable? | distribution over repeated trials | automated instrument acquisition |
| What does it cost? | energy per write/read/operation | electrical power measurement + optical power accounting |
| How fast is it? | propagation/state/read latency | oscilloscope, digitizer, network/phase measurement |

No measurement result should be called a Horizon result until the device, setup, calibration, uncertainty, and causal protocol are documented.

## 10. Candidate selection rule

The next material/device candidate should be selected by measured system-level criteria, not by novelty or state-count alone.

Required score dimensions:

1. number of reliably distinguishable states;
2. state-transition energy;
3. state-retention time;
4. write latency;
5. read latency;
6. state-dependent output contrast;
7. noise;
8. device-to-device variation;
9. reset/forget cost;
10. field-to-state coupling efficiency;
11. state-to-field coupling efficiency;
12. fabrication density;
13. temperature stability;
14. compatibility with binary I/O;
15. total end-to-end energy.

A candidate fails the Horizon path if any one of the following dominates:

encoding/decoding energy >> computation energy

state noise >> useful state contrast

read/write energy >> saved computation energy

state retention is too unstable for the intended temporal workload

fabrication variability destroys reproducibility

scaling requires impractical global connectivity

## 11. Current conclusion

The research direction is now narrower.

We are no longer asking:

> What material should Horizon use?

The more fundamental question is:

> What physical mechanism can provide a rich internal computational state that simultaneously participates in propagation, nonlinear transformation, memory, and feedback?

Current candidate families:

1. Photonic field + state/nonlinearity — primary candidate for high-density wave computation.
2. Magnonic/spin-wave field + magnetic/spintronic state — primary candidate for strongly coupled wave/state computation.
3. Ferroelectric state + field/electronic interaction — strong state-layer candidate and benchmark for multilevel physical state.
4. Memristive/oxide state — strong state-layer comparison baseline.
5. Phononic/acoustic field — exploratory candidate; currently less attractive for smartphone-scale general-purpose density and latency.

No final physical platform is selected.

## 12. Research status classification

### Established physics / reported technology
- wave propagation and interference;
- coherent magnon interference;
- programmable photonic nonlinear behavior;
- ferroelectric nonvolatile physical states;
- multilevel ferroelectric devices;
- optical latch memory concepts.

### Mathematical deduction
- a stateful WCR can be represented as a dynamical system;
- useful state must affect later transformations;
- richer physical state can be represented as multiple coupled degrees of freedom.

### Horizon proposed synthesis
- binary external interface with rich internal physical computation;
- WCR as a physical state space rather than a binary gate;
- coupled propagating field + nonlinear interaction + persistent state + feedback as the fundamental computational region.

### Unresolved engineering
- exact material stack;
- exact WCR geometry;
- state dimensionality;
- encoding method;
- nonlinear mechanism;
- feedback implementation;
- readout mechanism;
- energy/latency advantage;
- fabrication process;
- smartphone-scale integration;
- supercomputer-scale interconnection.

### Not demonstrated
- a Horizon WCR;
- general-purpose computation using the proposed mechanism;
- superiority to CPUs/GPUs;
- smartphone-scale fabrication;
- supercomputer-scale implementation.

## 13. Immediate next step

Do not build a custom laboratory.

Select the two strongest candidate mechanism families and map each one to an existing external experimental platform.

For each candidate, define exactly:

INPUT -> PHYSICAL INTERACTION -> STATE CHANGE -> RETENTION -> SAME LATER INPUT -> DIFFERENT OUTPUT

Then identify the minimum existing measurement setup capable of observing every arrow independently.

That becomes the next physical research gate.
