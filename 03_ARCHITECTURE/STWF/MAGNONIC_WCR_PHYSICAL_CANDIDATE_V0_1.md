# Magnonic WCR Physical Candidate v0.1

## Status

- Classification: candidate physical implementation
- Scope: proposed WCR mechanism, not a fabricated Horizon device
- Target architecture: binary I/O with rich physical internal computation
- Validation policy: use existing microwave/magnetic measurement infrastructure (D-012)

## 1. Physical object

A candidate magnonic WCR consists of a spin-wave propagation region coupled to a controllable magnetic/spintronic state.

Conceptual stack:

DIGITAL INPUT
→ microwave/electrical encoder
→ spin-wave excitation
→ propagation
→ coupling/interference
→ nonlinear magnetic interaction
→ magnetic state update
→ state-dependent spin-wave response
→ feedback/coupling
→ electrical/microwave readout
→ digital output

The WCR is the region where the propagating collective excitation and magnetic state interact causally.

## 2. Moving quantity

Primary moving quantity: a collective spin excitation / spin wave.

Candidate computational degrees of freedom:

- amplitude
- phase
- frequency
- timing
- wave vector / spatial mode
- magnetic configuration

Phase and amplitude can coexist as independent measurable coordinates of the same propagating excitation. They should therefore be treated as candidate rich-state variables rather than separate binary channels.

## 3. State location

Candidate state may reside in:

- magnetization orientation
- magnetic texture
- domain configuration
- spintronic state
- nonlinear magnon population
- bistable magnetic/magnonic configuration

The state is computationally useful only if it changes the response to a later input.

## 4. Computational loop

A minimal loop is:

X(t)
→ spin-wave excitation
→ propagation
→ interference/coupling
→ nonlinear magnetic interaction
→ S(t+1)
→ state-dependent wave response
→ feedback/coupling
→ later output.

The contract is:

S_next = F(S, X)

Y = G(S, X)

The external system remains binary:

binary input
→ microwave/electrical encoder
→ rich magnonic state
→ readout
→ binary output.

## 5. Minimum causal experiment

Prepare two magnetic states:

S_A != S_B

Apply the same later excitation X_0.

Measure:

Y_A = G(S_A, X_0)
Y_B = G(S_B, X_0)

Pass requires:

|Y_A - Y_B| > complete measurement uncertainty

with repeatable sign and magnitude across independent repetitions.

The measurement should record amplitude, phase, frequency and timing where technically available.

## 6. Measurement requirements

Existing external measurement classes can include:

- microwave signal generator
- vector network analyzer
- calibrated RF power measurement
- oscilloscope/digitizer
- phase-sensitive/vector detection
- magnetic-field control
- magnetometry or magnetic imaging where required
- spectrum analysis
- synchronized pulse generation and detection
- electrical power measurement

Exact instruments must be selected from the observable requirements of the final DUT.

## 7. Validation ladder

M0 — controlled spin-wave excitation.

M1 — reproducible propagation and coupling.

M2 — measurable interference and phase-sensitive response.

M3 — nonlinear state interaction.

M4 — controlled magnetic/state update.

M5 — measurable state retention or controlled decay.

M6 — identical later input produces state-dependent output.

M7 — repeatability under noise, reset, and parameter variation.

M8 — energy, latency, conversion overhead, density, and scaling measurements.

M6 is the first decisive Horizon-specific causal gate.

## 8. Known external evidence boundary

Recent work demonstrates relevant building blocks rather than the Horizon architecture. A 2025 Nature Materials study reported low-loss implanted YIG spin-wave waveguides with decay lengths above 100 micrometres in submicrometre waveguides and a network with 198 crossings. Other recent work has demonstrated coherent nonlinear magnon behavior and phase-sensitive information processing. These results support physical plausibility of the wave and nonlinear layers but do not prove a general-purpose stateful WCR or its system-level advantage. citeturn0search5turn0search6

## 9. Main kill conditions

Reject this candidate for the Horizon path if:

1. excitation/readout conversion dominates energy;
2. propagation loss destroys usable state contrast;
3. magnetic state cannot be reliably prepared and reset;
4. state retention is incompatible with operating cadence;
5. state-dependent output is below uncertainty;
6. magnetic noise or material variation overwhelms the signal;
7. required control fields are impractical at chip scale;
8. integration density is insufficient;
9. cascading causes unacceptable amplitude/phase degradation;
10. binary interface overhead removes any system-level advantage.

## 10. Epistemic classification

Established physics/technology:
- spin waves, magnetic dynamics, interference, nonlinear magnon processes, and integrated magnonic waveguides.

Mathematical deduction:
- a stateful wave processor requires later output to depend on the prepared physical state.

Horizon synthesis:
- using a spin-wave field and persistent magnetic state as one WCR while preserving binary external interfaces.

Unresolved:
- exact state medium, feedback mechanism, state capacity, energy, density, CMOS compatibility, and scaling.

Not demonstrated:
- Horizon chip
- general-purpose non-binary processor
- smartphone-class implementation
- supercomputer-scale implementation
- superiority over electronic computing.
