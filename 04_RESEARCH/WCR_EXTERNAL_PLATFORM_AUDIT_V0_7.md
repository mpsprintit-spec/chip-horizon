# WCR External Platform Audit V0.7

Date: 7 October 2026

Status: external-platform audit / experimental planning. No Horizon physical experiment has been performed.

## 1. Objective

The previous V0.6 gate mapped the abstract WCR parameters to physical observables and selected photonic WCR as the first mapping candidate.

V0.7 asks a narrower question:

> Which already-demonstrated external photonic platform provides the shortest path to the minimum WCR causal experiment without requiring Horizon to build custom laboratory instrumentation?

The minimum causal requirement remains:

1. prepare physical state A;
2. prepare a different physical state B;
3. apply the same later probe/input X;
4. measure outputs Y_A and Y_B;
5. demonstrate |Y_A - Y_B| > U_total, where U_total is the complete measurement uncertainty budget;
6. repeat with randomized A/B order and independent state preparations.

This is a mechanism test, not a test of universal computation, smartphone integration, or supercomputer scaling.

## 2. Candidate platforms

### P1 — Ferroelectric Pockels photonic memory

A 2025 Nature Communications device integrates a ferroelectric FeFET with a lithium-niobate microring resonator. The reported device provides six distinguishable non-volatile optical states per transistor, repeatable state characterization, approximately 28 h of directly observed state stability, projected 10-year retention, and more than 10^7 write/reset cycles. Optical states are read through resonance shifts and high-speed photodetection; the same state can also be read electrically.

The device is therefore unusually well matched to the causal A/B protocol:

state preparation -> persistent optical state -> identical optical probe -> state-dependent transmission.

The paper reports sequential identical write pulses producing six distinguishable optical states and time-series optical readout. This makes the required A/B experiment conceptually close to an already demonstrated measurement path.

Important limitation: the demonstrated device should not be treated as proof of the complete Horizon WCR. It primarily establishes a strong state/readout bridge between a persistent material state and an optical field. Its reported operation speed is in the microsecond range in the demonstrated setup, with authors identifying RC switching as a limiting factor.

### P2 — FLARE fully in-memory photonic computing

A 2026 Nature Sensors demonstration reports a monolithic 7,378-neuron photonic chip with short- and long-term memory, including approximately 7.45 s long-term retention while preserving GHz short-term dynamics. The system integrates sensing, processing and memory and uses photodiodes and RF probing for characterization.

This is the strongest existing evidence in this audit for an integrated computation-plus-memory photonic platform. It is valuable as a benchmark for scale, integration and memory/computation coupling.

However, it is less clean as the first Horizon causal mechanism experiment because the architecture is a large task-oriented computing system rather than a minimal device designed to isolate the causal transfer function of one stateful WCR. Its demonstrated architecture should therefore be treated as a benchmark and possible external validation platform, not automatically as the minimum experiment.

### P3 — Nonlinear multistable photonic microcavity

A 2026 Nature Nanotechnology demonstration uses a compact photonic-crystal microcavity with near-exceptional coupling to produce optical tristability through thermo-optical nonlinearity. The device shows hysteresis and controlled switching between three stable states and demonstrates a proof-of-concept optical RAM.

This is attractive for testing the nonlinear dynamical part of WCR:

input field -> nonlinear interaction -> multiple stable states -> state-dependent optical response.

Its weakness for the first Horizon state-retention gate is that the demonstrated state mechanism is thermo-optical rather than the long-retention non-volatile state mechanism desired for the Horizon state layer.

## 3. Audit matrix

| Requirement | P1 FeFET-Pockels | P2 FLARE | P3 nonlinear microcavity |
|---|---|---|---|
| Propagating optical field | PASS | PASS | PASS |
| Physical state preparation | PASS | PASS | PASS |
| Multiple distinguishable states | PASS | PASS | PASS |
| State retention | PASS | PASS | PARTIAL |
| Same optical probe after state preparation | STRONG | PLAUSIBLE/STRONG | STRONG |
| Optical state-dependent readout | STRONG | STRONG | STRONG |
| High-speed optical detection | PASS | PASS | PASS |
| Nonlinear state transition | PASS at memory/device level | PASS at system-neuron level | STRONG |
| Direct fit to A/B causal test | STRONGEST | STRONG | STRONG |
| Minimal experiment complexity | LOWEST of these candidates | HIGH | MEDIUM |
| Best role for Horizon | V1/V2 stateful WCR gate | benchmark/integration reference | nonlinear WCR branch |

These classifications are research-planning judgments based on the published demonstrations, not claims that the external platforms have already passed the Horizon-specific causal protocol.

## 4. Current selection

### First external platform: P1 FeFET-Pockels photonic memory

The audit promotes P1 as the first external platform to investigate for a Horizon-compatible causal measurement.

Reason:

It already exposes nearly every observable required for the first physical state gate:

- controlled state writing;
- multiple distinguishable internal states;
- optical resonance shift;
- optical transmission/readout;
- high-speed photodetection;
- retention;
- repeated state preparation;
- write/read energy;
- state-to-optical transfer.

The first experiment should not attempt to reproduce the complete WCR architecture. It should ask only whether the published device class can satisfy the causal relation:

S_A != S_B
X_A = X_B
Y_A != Y_B

with the difference surviving the complete uncertainty budget.

## 5. Proposed external measurement protocol

This protocol is deliberately smaller than a Horizon prototype.

### State preparation

Select two non-adjacent optical memory states, for example S_A and S_B, using the demonstrated write-pulse procedure.

Record the actual optical spectrum after each preparation rather than assuming the programmed pulse count equals the physical state.

### Common probe

Use the same probe wavelength and optical input power for both states.

The probe must be applied only after the state-preparation transient has settled sufficiently that the measurement is not simply observing the write pulse.

### Readout

Measure optical transmission with the existing high-speed photodetection path.

For a stronger characterization, acquire the complete transmission spectrum and extract resonance position, linewidth, extinction ratio, and selected-wavelength transmission.

### Randomized causal sequence

Use a sequence such as:

A -> B -> B -> A -> A -> B

with fresh state preparation before each trial.

The order should be randomized in the actual experiment. The sequence above is only an example.

### Uncertainty budget

Estimate:

U_total = sqrt(U_detector^2 + U_source^2 + U_temperature^2 + U_drift^2 + U_fit^2 + U_repeatability^2 + ...)

The causal result is accepted only when:

|Y_A - Y_B| > U_total

with an experimentally justified confidence criterion.

## 6. Parameter mapping

For P1, the V0.6 abstract variables can be mapped as:

- q -> ferroelectric polarization / effective electro-optic state
- a -> optical field in the microring
- rho -> optical/state persistence observable through ringdown or temporal response
- coupling -> field-state interaction / resonance-shift coupling
- nonlinear -> ferroelectric switching and state-dependent electro-optic response
- phi -> optical phase, if coherent measurement is added
- Y -> transmission power, resonance position, or coherent optical quadrature
- noise -> transmission variance, resonance-fit variance, thermal drift, source fluctuation
- tau -> measured state lifetime or relevant field/state decay time

The mapping is not an identity between the simulator equations and the device physics. The external experiment must first measure the actual transfer functions.

## 7. What this audit establishes

### Established by external literature

- Integrated photonic systems can combine propagating optical fields with physical memory states.
- Ferroelectric Pockels photonic memory can provide multiple distinguishable non-volatile optical states and optical readout.
- Large-scale photonic computing can integrate memory and computation.
- Nonlinear photonic microcavities can exhibit multiple stable states and controlled switching.

### Mathematical deduction / Horizon synthesis

- A WCR can be represented as a dynamical system S_(t+1)=F(S_t,X_t), Y_t=G(S_t,X_t).
- A stateful wave-computing region requires causal state dependence, not merely storage.
- The decisive physical test is same later input + different prepared state -> measurably different output.

### Not established

- The Horizon WCR mechanism has not been physically demonstrated.
- The published devices do not prove that the Horizon equations are the correct governing equations.
- No evidence yet establishes smartphone-scale implementation of the complete Horizon architecture.
- No evidence yet establishes supercomputer-scale superiority in speed, energy, density, or generality.

## 8. Kill conditions for P1

Stop or demote P1 if any of the following is demonstrated:

1. State separation disappears within measurement uncertainty.
2. State preparation is not repeatable.
3. Retention is inadequate for the intended computation.
4. State-dependent output disappears after drift correction.
5. Write/read energy dominates the intended computation.
6. The usable state count collapses under realistic noise.
7. Optical coupling or readout overhead dominates.
8. The physical response cannot be represented by a controllable WCR transfer function.
9. The platform cannot expose enough observables to reconstruct the causal transfer function without custom instrumentation.

## 9. Next gate

The next gate is no longer "find another material."

It is:

**Find an existing external device/lab measurement path for P1 and determine whether the full A/B protocol can be executed with existing instrumentation.**

Required information:

- device/platform access;
- optical source and detector already available;
- state-write interface;
- wavelength/power range;
- time resolution;
- spectral resolution;
- temperature/drift control;
- repeatability;
- sample/package requirements;
- data format;
- measurement uncertainty;
- access route and practical constraints.

If no accessible external platform can satisfy the minimum protocol, P1 remains a literature-supported candidate rather than an experimental candidate.

## 10. Decision status

**P1 FeFET-Pockels photonic memory: PROMOTED to first external measurement candidate.**

**P2 FLARE: RETAINED as integration/scaling benchmark.**

**P3 nonlinear microcavity: RETAINED as nonlinear-dynamics benchmark.**

**Magnonic WCR: RETAINED as an independent competing physical branch.**

No final Horizon material or physical architecture is selected.
