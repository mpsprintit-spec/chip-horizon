# Photonic WCR Physical Candidate v0.1

## Status

- Classification: candidate physical implementation
- Scope: proposed WCR mechanism, not a fabricated Horizon device
- Target architecture: binary I/O with rich physical internal computation
- Validation policy: use existing external optical/electrical measurement infrastructure (D-012)

## 1. Physical object

A candidate WCR consists of a confined optical propagation region coupled to a stateful nonlinear material/device.

Conceptual stack:

DIGITAL INPUT
→ electrical/optical encoder
→ optical source/modulator
→ waveguide / resonant region
→ coupling + interference
→ nonlinear/state element
→ state-dependent optical response
→ feedback or recirculation
→ detector
→ digital output

The WCR is the physical region in which the optical field and internal state causally interact. A waveguide alone is not the WCR computational mechanism.

## 2. Moving quantity

Primary moving quantity: electromagnetic optical field.

Potential computational degrees of freedom:

- amplitude
- phase
- frequency/wavelength
- arrival time
- spatial mode
- polarization
- coupled material state

These are candidate information-bearing variables. They must not be assumed independently usable until measurement demonstrates sufficient distinguishability and control.

## 3. State location

Candidate state may reside in:

- carrier population
- refractive-index state
- absorption state
- resonant state
- electro-optic memory
- magneto-optic state
- another coupled material state

The decisive requirement is causal persistence:

state at time t must measurably alter the response to a later input.

## 4. Computational loop

A minimal physical loop is:

X(t)
→ optical field E(t)
→ propagation/coupling
→ nonlinear interaction
→ state update S(t+1)
→ state-modified optical response
→ feedback
→ E(t+1)
→ Y(t+1)

The mathematical contract is:

S_next = F(S, X)

Y = G(S, X)

A binary interface can wrap this internal computation:

binary input
→ encoder
→ rich physical state
→ decoder
→ binary output.

## 5. Minimum causal experiment

Prepare two distinguishable states:

S_A != S_B

Apply the same later optical input X_0.

Measure:

Y_A = G(S_A, X_0)
Y_B = G(S_B, X_0)

The experiment passes the causal gate only if:

|Y_A - Y_B| > complete measurement uncertainty

and the result is repeatable over independent repetitions.

A larger nominal state count is not sufficient.

## 6. Measurement requirements

Existing external measurement classes can provide the required observables:

- calibrated optical power measurement
- fast photodetection
- oscilloscope/digitizer
- interferometric or phase-sensitive detection
- optical spectrum measurement
- electrical current/voltage measurement
- synchronized source and detector
- total electrical/optical power accounting

The exact instrument selection depends on the final candidate device.

## 7. Validation ladder

P0 — optical propagation is controlled and reproducible.

P1 — coupling/interference changes the measured output.

P2 — nonlinear response is measurable and repeatable.

P3 — an input changes a physical internal state.

P4 — the state persists for a measurable interval.

P5 — the same later input produces different outputs for different prepared states.

P6 — state-dependent behavior survives repetition, noise, and reset tests.

P7 — energy, latency, conversion overhead, and density are measured.

Only P5-P7 begin to test the Horizon-specific computational claim.

## 8. Known external evidence boundary

Recent photonic research has already demonstrated programmable on-chip nonlinear functionality and integrated photonic memory/computation. For example, a 2025 Nature Photonics device demonstrated field-programmable photonic nonlinearity, while a 2025 Nature paper demonstrated programmable on-chip nonlinear photonics. A 2026 Nature Sensors report demonstrated a large-scale in-memory photonic architecture with long- and short-term memory. These results establish that several component mechanisms are physically credible; they do not establish the Horizon WCR architecture or its claimed system-level advantage. citeturn0search4turn0search0turn0search1

## 9. Main kill conditions

Reject this candidate for the Horizon path if:

1. state preparation is not repeatable;
2. state-dependent output contrast remains below measurement uncertainty;
3. retention cannot be controlled over the intended operating interval;
4. nonlinear interaction requires excessive energy;
5. optical-electrical conversion dominates total energy;
6. accumulated loss requires impractical amplification;
7. fabrication variation destroys state distinguishability;
8. required precision is incompatible with noise;
9. binary encoding/decoding overhead removes any system-level advantage;
10. scaling from one WCR to a dense array becomes physically impractical.

## 10. Epistemic classification

Established physics/technology:
- optical propagation, interference, nonlinear optics, photonic memory, and integrated photonic devices.

Mathematical deduction:
- a stateful transformation requires the later output to depend on the prior state.

Horizon synthesis:
- using a compact optical field + nonlinear persistent state as the WCR computational substrate while retaining binary external interfaces.

Unresolved:
- the exact state mechanism, state capacity, feedback topology, operating energy, precision, density, and scalability of a general-purpose Horizon WCR.

Not demonstrated:
- a Horizon chip
- general-purpose computation
- smartphone-class implementation
- supercomputer-scale implementation
- superiority over electronic processors.
