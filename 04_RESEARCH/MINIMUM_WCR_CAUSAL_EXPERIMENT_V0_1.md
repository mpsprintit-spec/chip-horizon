# MINIMUM WCR CAUSAL EXPERIMENT V0.1

## Status

Research experiment specification.

Purpose: define the smallest externally measurable experiment capable of falsifying the central causal claim of the Horizon WCR:

> A wave input changes a physical computational state, the state persists, and that state measurably changes a later wave response.

This document does not define a custom laboratory or custom measurement instrument. Existing external instruments and facilities are preferred according to D-012.

---

## 1. Claim being tested

A candidate WCR must demonstrate more than wave propagation or optical communication.

The causal chain under test is:

```
input wave
    |
    v
physical interaction
    |
    v
state changes
    |
    v
state persists
    |
    v
later input
    |
    v
state-dependent response
    |
    v
measurable output
```

If the state does not measurably affect the later response, the candidate does not satisfy the stateful WCR requirement.

---

## 2. Minimum observables

The experiment must independently observe, or otherwise establish with calibrated measurement:

1. input wave condition;
2. physical state proxy;
3. state evolution versus time;
4. later input condition;
5. output wave response;
6. timing relationship;
7. repeatability;
8. energy or power where available.

The exact observable depends on the selected physical platform.

Examples include:

- optical power;
- waveform;
- phase;
- frequency/spectrum;
- impedance;
- resistance/conductance;
- resonant response;
- switching state;
- transient response.

---

## 3. Experiment sequence

### E0 — Instrument and interface baseline

Measure the external source, detector, cables/waveguides, and measurement chain without the candidate computational mechanism.

Purpose:

- establish instrument noise;
- establish drift;
- establish baseline loss;
- establish timing uncertainty;
- prevent the test system from being mistaken for the WCR.

No Horizon computational claim is made at E0.

### E1 — Controlled wave propagation

Send a known input through the candidate wave path.

Measure the output.

Required observations:

- propagation exists;
- attenuation is measurable;
- delay is measurable;
- output is repeatable.

This establishes the wave path but does not yet establish computation.

### E2 — Controlled coupling/interference

Apply at least two controlled wave contributions where the platform permits.

Vary their relative condition.

Observe the resulting output.

The experiment should establish that coupling/interference is controllable rather than accidental.

### E3 — Nonlinear response

Vary input level or another relevant control variable.

Measure output response.

The objective is to distinguish a nonlinear response from:

- detector saturation;
- source saturation;
- amplifier saturation;
- instrument clipping;
- ordinary linear loss.

An independent baseline is therefore required.

### E4 — State update

Apply a defined input sequence.

Measure a state proxy before and after the stimulus.

The state must change reproducibly.

The state variable must not be inferred solely from the same output signal that is used to claim computation if an independent state observable is available.

### E5 — Retention / decay

After the update stimulus is removed, observe the state over time.

Determine:

- retention;
- decay;
- drift;
- noise;
- reset behavior.

State lifetime is an experimentally measured quantity.

### E6 — Causal state-dependent response

This is the central test.

Prepare two physically distinguishable conditions:

**Condition A:** state has been updated.

**Condition B:** state has been reset, erased, or otherwise placed in a controlled reference condition.

Apply the same later input to both conditions.

Measure the output.

Required result:

`Output_A != Output_B`

by an amount that exceeds the experimentally established uncertainty and nuisance effects.

If the two outputs are indistinguishable within uncertainty, the state-dependent computational claim fails for that operating point.

### E7 — Repeatability

Repeat E6 over multiple cycles.

Measure:

- cycle-to-cycle variation;
- state drift;
- failure probability;
- hysteresis;
- reset reliability;
- environmental sensitivity.

A single successful trace is not sufficient evidence of a reproducible WCR.

### E8 — Energy and latency accounting

Measure or bound:

- source energy;
- modulation/encoding energy;
- propagation loss;
- nonlinear/state energy;
- readout energy;
- control energy;
- reset energy;
- correction energy where applicable;
- end-to-end latency.

The purpose is not to prove an advantage immediately.

The purpose is to prevent an apparent computational gain from being created by uncounted external costs.

---

## 4. Required control conditions

The experiment should include controls capable of distinguishing the claimed mechanism from common false positives.

### Control A — No state update

Apply the later input without first updating the state.

### Control B — State reset

Update the state, reset it, then apply the later input.

### Control C — Linear-path reference

Use an otherwise comparable path without the nonlinear/state mechanism where possible.

### Control D — Instrument baseline

Characterize the measurement chain independently.

### Control E — Repeated identical sequence

Repeat the same input sequence to detect drift and hidden dependence.

---

## 5. Independence requirement

The experiment must avoid circular validation.

Bad structure:

```
same model
   -> expected result
   -> actual result
   -> PASS
```

Preferred structure:

```
independent input
      |
      v
physical DUT
      |
      +--> independent state measurement
      |
      +--> independent output measurement
      |
      v
independent analysis
      |
      v
comparison against predefined reference/control
```

The reference defines what should be observed. The physical measurement determines what was observed.

---

## 6. Minimum falsifiable result

The smallest result capable of supporting the WCR stateful claim is a reproducible difference between two later responses caused by a controlled difference in prior physical state.

Conceptually:

```
same later input
       |
       +--> state A --> output A
       |
       +--> state B --> output B

where:

state A != state B

and:

output A != output B

with the difference exceeding measured uncertainty.
```

This is stronger than demonstrating:

- a laser;
- a waveguide;
- interference;
- resonance;
- material switching;
- optical memory;
- a nonlinear curve

individually.

The required evidence is the causal connection between state and later computation.

---

## 7. What this experiment does not prove

Passing this experiment would **not** prove:

- universal computation;
- useful addition or multiplication;
- superior speed;
- superior energy efficiency;
- commercial manufacturability;
- smartphone-scale integration;
- supercomputer-scale scalability.

It would establish only that a candidate physical region satisfies the minimum stateful causal mechanism required by the WCR architecture.

---

## 8. External infrastructure mapping

The exact instrument depends on the final wave/state platform.

Candidate measurement classes already identified in the external infrastructure registry include:

- oscilloscope / digitizer;
- optical power measurement;
- photodetection;
- spectrum measurement;
- phase/frequency measurement;
- semiconductor parameter analyzer / SMU;
- LCR / impedance measurement;
- spectroscopy;
- thermal measurement where relevant.

No custom Horizon measurement instrument is required by this specification.

A facility may be suitable only after confirming:

- access policy;
- sample compatibility;
- calibration;
- uncertainty;
- bandwidth;
- dynamic range;
- environmental control;
- data export;
- scheduling and cost.

---

## 9. Kill conditions

The candidate physical mechanism should be reconsidered if:

- state update is not reproducible;
- state retention is below useful operating requirements;
- state reset cannot be controlled;
- later response does not depend measurably on prior state;
- observed state dependence is explained by detector/source artifacts;
- noise is larger than the state-dependent signal;
- feedback is unstable;
- conversion overhead dominates;
- the required operating point is incompatible with fabrication or thermal constraints.

---

## 10. Relation to Horizon scaling

The experiment validates only one WCR.

The next stages remain:

```
WCR
  -> Core
  -> Tile
  -> Region
  -> Chip
  -> Multi-chip
  -> Supercomputer
```

Scaling is not accepted merely by copying a successful laboratory trace.

At each higher level, communication, routing, state interference, synchronization, energy, thermal load, fabrication variation, and fault tolerance must be measured.

---

## 11. Epistemic classification

### Established

The measurement methods and physical phenomena are established in appropriate platforms.

### Proposed experiment

The sequence E0-E8 is a Horizon validation design derived from the WCR causal requirement.

### Not yet demonstrated

No Horizon hardware result is implied by this document.

## Status

**Ready as a falsification-oriented experiment specification once a candidate physical WCR platform is selected.**
