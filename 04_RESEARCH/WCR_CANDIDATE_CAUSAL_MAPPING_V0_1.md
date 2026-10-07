# WCR Candidate Causal Mapping v0.1

Date: 7 October 2026
Status: candidate mechanism mapping; no Horizon hardware result

## 1. Purpose

This document converts the two strongest candidate families into explicit causal chains.

The goal is not to select a final material yet. The goal is to determine which physical family can satisfy the minimum Horizon WCR condition:

same later input + different prior physical state -> measurably different later output.

## 2. Candidate A: photonic WCR

### 2.1 Physical chain

DIGITAL INPUT
-> optical/electrical encoder
-> optical field
-> propagation
-> coupling/interference
-> nonlinear/state element
-> state-dependent optical response
-> feedback or recirculation
-> readout
-> DIGITAL OUTPUT

### 2.2 Physical entities

Moving quantity:
- electromagnetic field in an optical mode.

Candidate state:
- carrier population;
- refractive-index state;
- absorption state;
- resonant state;
- coupled material state.

Potential internal variables:
- amplitude;
- phase;
- frequency;
- spatial mode;
- material state.

### 2.3 Causal test

Prepare state A.

Apply identical optical input X.

Measure output Y_A.

Reset/prep state B.

Apply the identical optical input X.

Measure output Y_B.

Required result:

Y_A != Y_B

The difference must exceed the combined measurement uncertainty and survive repeated trials.

### 2.4 Why this candidate is interesting

Integrated photonics already demonstrates programmable nonlinear behavior. A 2025 Nature Photonics experiment used spatially controlled carrier excitation to create reconfigurable nonlinear connections in an integrated photonic processor.

A 2026 Nature paper also demonstrated a programmable nonlinear waveguide whose effective chi(2) distribution could be dynamically configured and updated.

These results establish useful physical ingredients, not the complete Horizon mechanism.

### 2.5 Main engineering risks

1. optical source energy;
2. electro-optical conversion;
3. detector energy;
4. nonlinear response strength;
5. state lifetime;
6. optical loss;
7. thermal effects;
8. fabrication variation;
9. readout precision;
10. feedback latency.

The key Horizon question is whether state can be retained and coupled strongly enough to alter later optical computation without making the peripheral energy dominate.

## 3. Candidate B: magnonic WCR

### 3.1 Physical chain

DIGITAL INPUT
-> microwave/electrical excitation
-> spin-wave excitation
-> propagation
-> magnon coupling/interference
-> magnetic state interaction
-> modified spin-wave response
-> readout
-> DIGITAL OUTPUT

### 3.2 Physical entities

Moving quantity:
- collective spin excitation / magnon mode.

Candidate state:
- magnetic configuration;
- magnetization orientation;
- magnetic texture;
- spintronic state.

Potential internal variables:
- amplitude;
- phase;
- frequency;
- spatial mode;
- magnetic state.

### 3.3 Existing experimental evidence

A 2025 Nature Communications experiment demonstrated single-shot interference of multiple magnon pulses in coupled YIG resonators. The interference was controlled through pulse timing and frequency detuning, and the experiment measured coherent energy exchange between coupled resonators.

A 2025 Nature Materials experiment demonstrated implanted YIG spin-wave waveguides with decay lengths above 100 micrometres in submicrometre waveguides and a network containing 198 crossings.

These results are particularly relevant to the WCR concept because they demonstrate both coherent wave interaction and integrated waveguide-network structures.

They do not demonstrate a Horizon stateful computational region.

### 3.4 Main engineering risks

1. spin-wave excitation efficiency;
2. propagation loss;
3. state preparation;
4. state retention;
5. detection;
6. thermal stability;
7. device variation;
8. magnetic-field/control requirements;
9. integration with conventional CMOS;
10. scaling from laboratory structures to dense chip-scale arrays.

## 4. Direct comparison

| Property | Photonic WCR | Magnonic WCR |
|---|---|---|
| Propagating field | electromagnetic | spin wave |
| Natural interference | strong | strong |
| Phase degree of freedom | strong | strong |
| Frequency degree | strong | strong |
| Spatial mode | strong | strong |
| Persistent state | requires coupled material/device | potentially magnetic state in same platform |
| Nonlinearity | available | available |
| Optical/electrical conversion | potentially significant | microwave/electrical conversion required |
| Propagation loss | low-loss photonics possible | major engineering variable |
| Dense interconnect | strong candidate | promising but harder |
| CMOS integration | comparatively mature | harder |
| Stateful coupling | unresolved | conceptually attractive |
| Current Horizon priority | very high | very high |

## 5. Important distinction

The photonic candidate has an advantage in propagation and interconnect.

The magnonic candidate has an attractive conceptual property:

the signal and state may be two manifestations of closely related physical dynamics.

That could reduce the conceptual separation between:

wave -> memory -> feedback.

However, the engineering cost may be much higher.

Therefore the project should not choose between them based on intuition.

## 6. Minimum causal experiment for each candidate

### Photonic

E-P0:
measure input and output without state interaction.

E-P1:
demonstrate controlled state preparation.

E-P2:
measure state retention/decay.

E-P3:
apply identical later optical input to state A and state B.

E-P4:
demonstrate reproducible output separation.

E-P5:
measure write energy, read energy, propagation loss, latency and uncertainty.

### Magnonic

E-M0:
measure excitation and propagation baseline.

E-M1:
demonstrate controlled magnetic-state preparation.

E-M2:
measure magnetic-state retention/decay.

E-M3:
apply identical later spin-wave excitation to state A and state B.

E-M4:
demonstrate reproducible output separation.

E-M5:
measure excitation energy, detection energy, propagation loss, latency and uncertainty.

## 7. External infrastructure principle

No custom Horizon laboratory is required for these first experiments.

The experimental interface should be reduced to the minimum device under test and whatever adapters are required by an existing facility.

For photonics, relevant established measurement classes include:
- calibrated optical source;
- optical power measurement;
- photodetection;
- oscilloscope/digitizer;
- interferometric or phase-sensitive measurement;
- spectroscopy when required.

For magnonics:
- microwave source;
- vector network analysis;
- time-domain digitization;
- magnetic-field control;
- microwave power measurement;
- magnetic/spin-wave characterization.

The exact facility must be selected after the candidate device geometry and required observable are fixed.

## 8. Kill criteria

A candidate should be rejected from the primary Horizon path if:

- state-dependent output contrast is below measurement uncertainty;
- state cannot be reliably prepared;
- state cannot be reliably reset;
- state lifetime is incompatible with the intended computation;
- read/write energy dominates the computational energy budget;
- field-state coupling is too weak;
- device variability destroys repeatability;
- required control infrastructure prevents chip-scale integration;
- the rich physical state does not provide measurable computational benefit over a binary/electronic baseline.

## 9. Current research decision

Do not declare photonics the final platform.

Do not declare magnonics the final platform.

The correct next gate is experimental:

candidate device -> state preparation -> retention -> identical later input -> state-dependent output.

Whichever physical family can demonstrate this causal chain with the strongest combination of contrast, repeatability, energy, latency, and scalability becomes the stronger WCR substrate candidate.

## 10. Important epistemic boundary

Reported photonic and magnonic experiments demonstrate physical ingredients.

They are not evidence that Horizon already works.

The Horizon hypothesis remains:

a physical computational region can retain a rich internal state and use that state to alter subsequent field evolution while remaining compatible with binary system-level I/O.

That hypothesis remains experimentally open.
