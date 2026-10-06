# STWF OPERATIONAL DATA PATH V0.1

## Status

Research architecture specification.

This document defines the end-to-end computational data path of Horizon from external input to external output. It is intended to remove ambiguity about what a chip receives, what physically changes inside the chip, and what is finally measured.

It does **not** claim that the proposed physical implementation has been fabricated or experimentally validated.

---

## 1. Core distinction

A conventional computer exposes numbers to software, but the physical chip does not receive an abstract number such as "5".

It receives physical states.

For an electronic interface, those states may be voltage/current ranges.

For a Horizon wave interface, the internal representation may instead use physical wave observables such as:

- amplitude;
- phase;
- arrival time;
- frequency;
- spatial mode;
- polarization;
- persistent physical state.

Therefore:

`number -> physical representation -> physical evolution -> physical representation -> number`

The number is an interpretation at the system boundary. The physical computation occurs in the intermediate physical states.

---

## 2. End-to-end path

The target path is:

```
EXTERNAL DATA
     |
     v
INPUT INTERFACE
     |
     v
INPUT BUFFER / CONDITIONING
     |
     v
SPACE-TIME ENCODER
     |
     v
WAVE SOURCE / MODULATOR
     |
     v
WAVE INTERCONNECT
     |
     v
WCR
 |-------------------------------|
 | propagation                    |
 | coupling                       |
 | delay                          |
 | interference                   |
 | nonlinear interaction          |
 | physical state                 |
 | state-dependent feedback       |
 |-------------------------------|
     |
     v
OUTPUT WAVE
     |
     v
READOUT / DETECTOR
     |
     v
SIGNAL CONDITIONING
     |
     v
DIGITAL / SYSTEM REPRESENTATION
     |
     v
EXTERNAL OUTPUT
```

The encoder, WCR, readout, and external interface must not be conflated.

---

## 3. Concrete example: 5 + 3 = 8

This example is a **computational contract and teaching example**, not evidence that the current Horizon WCR already performs addition.

Suppose an external device requests:

`A = 5`

`B = 3`

and the requested operation is:

`A + B`

### Step 1 — External representation

A conventional digital system may represent the integers as:

`5 = 0101`

`3 = 0011`

Those bits are not the fundamental Horizon representation.

They are simply the representation used by the external digital system.

### Step 2 — Input interface

The chip receives electrical or other physical signals representing the incoming data.

The input interface:

- detects the signal;
- establishes valid timing;
- separates channels if necessary;
- buffers the data;
- checks basic integrity;
- passes the information to the encoder.

At this point the chip still has not "calculated 8".

### Step 3 — Space-time encoding

The encoder converts the incoming information into a physical wave representation.

A hypothetical example could encode:

- value 5 as one wave condition;
- value 3 as another wave condition.

The condition could involve amplitude, phase, timing, frequency, spatial mode, or a combination.

**The final encoding has not yet been selected.**

This is one of the important unresolved engineering decisions.

### Step 4 — Wave generation

A source or modulator creates the corresponding physical wave states.

For an optical implementation this could involve:

`electrical control -> optical source/modulator -> optical wave`

The wave now carries the encoded information.

### Step 5 — Physical transport

The waves enter waveguides or another controlled propagation medium.

The physical structure can introduce:

- delay;
- attenuation;
- phase shift;
- coupling;
- routing;
- resonance;
- controlled transformation.

These are not merely wires carrying data if the architecture deliberately uses their physical behavior as part of the computation.

### Step 6 — WCR interaction

Inside the WCR, the encoded waves meet the computational structure.

A conceptual WCR is:

```
input wave
    |
    v
propagation
    |
    v
coupling / interference
    |
    v
nonlinear interaction
    |
    +------> output
    |
    v
physical state
    |
    v
feedback
    |
    +------> modifies subsequent wave evolution
```

This is the point where the architecture claims the physical system itself performs the transformation.

### Step 7 — Interference

When wave contributions overlap, their physical fields combine.

Depending on their relative phase and amplitude, the resulting field can become stronger or weaker.

This gives the architecture a physical mechanism for combining contributions.

However:

**interference alone is not enough to make a general stateful computer.**

A purely linear interference network is closer to a physical linear transform.

### Step 8 — Nonlinearity

A nonlinear element changes the relationship between input and response.

Possible functions include:

- threshold;
- saturation;
- switching;
- nonlinear phase shift;
- state-dependent coupling;
- gain/loss modification.

This is important because a useful computer needs more than unrestricted linear superposition.

### Step 9 — State

The WCR maintains a physical condition that survives long enough to affect later computation.

The state could be associated with:

- resonant energy;
- material resistance;
- polarization;
- magnetic configuration;
- ferroelectric configuration;
- phase-change state;
- another measurable physical degree of freedom.

The state is not simply "memory attached to the side".

In Horizon it is intended to participate directly in the computational dynamics.

### Step 10 — Feedback

Part of the state influences the next wave interaction.

Conceptually:

```
wave
  |
  v
state changes
  |
  v
state changes wave response
  |
  v
next wave
```

This creates history dependence.

For example, a sequence:

`3, 5, 2, 7`

could have the abstract state trajectory:

`3 -> 8 -> 10 -> 17`

if the computational contract is a running sum.

Again, this trajectory is currently a mathematical reference behavior, not a demonstrated physical Horizon computation.

### Step 11 — Readout

The output must be measured.

A detector may observe:

- amplitude;
- intensity;
- phase;
- arrival time;
- frequency;
- spectrum;
- another selected observable.

If the computation depends on phase or signed information, intensity-only detection may be insufficient.

The readout therefore has to match the internal representation.

### Step 12 — Conversion to external data

The measured physical signal is converted back into the representation expected by the external system.

For example:

```
physical output
    |
    v
detector
    |
    v
electrical signal
    |
    v
signal processing
    |
    v
digital value 8
```

Only at this boundary do we say that the system has produced the number "8".

---

## 4. Where the actual computation occurs

The architecture should not be described as:

`laser -> cable -> detector`

That would describe communication.

The computational region is where the physical laws are intentionally arranged so that the input state evolves into a useful output state.

For Horizon:

```
wave propagation
      +
coupling/interference
      +
nonlinearity
      +
physical state
      +
feedback
      =
candidate computational mechanism
```

The exact physical implementation is unresolved.

---

## 5. Communication versus computation

An optical fiber can carry a signal from A to B without computing anything.

A waveguide inside a WCR can also carry a signal.

The difference is what the physical structure does to that signal.

### Communication

```
A --------------------------> B
       preserve / transport
```

### Computation

```
A ----> transform ----                       >---- result
B ----> transform ----/
          ^
          |
       state
```

In Horizon, the goal is to make selected propagation, coupling, delay, interference, nonlinear response, and state evolution perform useful computation rather than treating them only as transport.

---

## 6. What belongs inside one WCR

A candidate WCR should contain, within its causal computational boundary:

1. wave propagation domain;
2. controllable coupling;
3. nonlinear interaction;
4. physical state;
5. state-dependent feedback;
6. input interface;
7. measurable output.

External lasers, drivers, detectors, controllers, and laboratory instruments do not automatically belong inside the WCR.

They are system or measurement infrastructure.

Their energy and latency must nevertheless be counted in the complete system budget.

---

## 7. From one WCR to a chip

One WCR is not the whole chip.

The intended hierarchy is:

```
WCR
  |
  +-- WCR
  +-- WCR
  +-- WCR
  +-- ...
       |
       v
     CORE
       |
       v
      TILE
       |
       v
     REGION
       |
       v
      CHIP
       |
       v
   MULTI-CHIP
       |
       v
 HORIZON SUPERCOMPUTER
```

The same physical computational mechanism should remain recognizable at every level.

The larger system primarily adds:

- more WCRs;
- more state capacity;
- more local bandwidth;
- more hierarchy;
- more routing;
- more parallelism;
- more aggregate I/O.

---

## 8. Smartphone-scale versus supercomputer-scale

### Smartphone-class chip

The same mechanism would use a relatively small number of WCRs with:

- short local paths;
- limited state capacity;
- limited optical/wave power;
- compact I/O;
- strict thermal constraints.

### Supercomputer

The same mechanism would use:

- very large WCR count;
- many cores and tiles;
- hierarchical optical/electrical interconnect;
- distributed state;
- high aggregate bandwidth;
- large cooling and power infrastructure.

The architecture must not become a completely different computer merely because it is larger.

---

## 9. What is established and what is not

### Established physics

Established phenomena include:

- wave propagation;
- interference;
- coupling;
- attenuation;
- finite propagation delay;
- nonlinear material response;
- physical state retention in suitable systems;
- optical/electromagnetic communication.

### Mathematical model

The stateful computational contracts are mathematical abstractions used to specify expected behavior.

### Horizon synthesis

The proposed combination is:

`wave dynamics + nonlinearity + physical state + feedback`

inside a scalable WCR hierarchy.

### Unresolved engineering

Still unresolved:

- final wave medium;
- final state medium;
- physical encoding;
- signed representation;
- nonlinear device;
- state-update mechanism;
- feedback geometry;
- fabrication process;
- WCR dimensions;
- energy/op;
- latency;
- precision;
- yield;
- scaling advantage.

No claim of a finished Horizon chip is made.

---

## 10. Immediate research consequence

Before selecting a final material or fabrication process, the project should answer one narrower question:

> Can one physical WCR demonstrably implement a reproducible history-dependent transformation in which a wave input changes a physical state, and that state measurably changes a later wave output?

That is the bridge between the mathematical Stateful Core and an actual Horizon computational device.

The next physical validation should therefore be derived from this causal chain:

```
wave input
   ->
controlled interaction
   ->
nonlinear/state change
   ->
retained state
   ->
state-dependent later response
   ->
measurable output
```

Existing external measurement infrastructure should be used wherever suitable.

## Epistemic status

**Research specification / proposed architecture. No hardware result.**
