# WCR Physical Parameter Mapping Gate v0.6

**Date:** 7 October 2026  
**Status:** Candidate-platform selection / experimental planning  
**Physical experiment:** Not performed

## Objective

The v0.5 operating-envelope sweep showed that the mathematical WCR model has useful regions in abstract parameter space.

The next problem is to map those abstract parameters to quantities that an external experiment can actually measure.

The first candidate selected for this mapping exercise is **photonic WCR**, because recent integrated photonic work demonstrates both rich nonlinear/memory behaviour and direct optical readout.

This is a research candidate, not a final hardware selection.

## Mapping

| WCR model parameter | Physical interpretation | Candidate observable |
|---|---|---|
| rho | field/state persistence or resonator retention | ringdown time, Q factor, decay constant |
| coupling | interaction between field and state / regions | transmission coefficient, splitting, extinction-ratio change |
| nonlinear | strength of nonlinear state-dependent response | resonance shift vs optical/electrical input, bistability threshold |
| noise | uncertainty in state/output | repeated-trace variance, phase noise, amplitude noise, thermal drift |
| q | internal material/device state | resonance position, transmission level, phase shift |
| phi | internal phase state | coherent phase measurement / interferometric quadrature |
| a | propagating field amplitude | optical power or complex field quadrature |
| Y | WCR readout | photodetector / balanced coherent receiver output |

## Why photonics is currently the first mapping candidate

FLARE demonstrated integrated photonic sensing, processing and memory with short- and long-term memory on a monolithic 7,378-neuron chip. Its long-term memory was associated with an RC decay mechanism and its readout used optical transmission. citeturn0search0

A ferroelectric Pockels photonic-memory platform demonstrated six distinct non-volatile optical states per transistor, optical readout through resonance shift, projected long retention, and more than 10^7 read-write endurance. citeturn0search2

These systems are not Horizon WCRs. They are useful because they expose measurable physical variables that can calibrate the abstract model.

## Minimum physical A/B experiment

Prepare two distinguishable internal states:

SA != SB

Then apply the **same external optical probe**:

XA = XB

Measure:

YA and YB

Causal criterion:

|YA - YB| > U_total

where U_total is the combined measurement uncertainty, including detector noise, drift, repeatability and state-preparation variation.

Repeat with randomized order:

A, B, B, A, A, B, ...

This reduces the risk of confusing slow thermal drift with state causality.

## Required measurements

### 1. State distinguishability

Measure the distribution of readout values for state A and state B.

Require statistically separable distributions.

### 2. State retention

Prepare one state, remove the write stimulus, then measure S(t).

For an exponential approximation:

S(t) = S0 exp(-t/tau)

The measured tau replaces the abstract model parameter.

### 3. State-dependent response

For identical probe X:

Y = G(X,S)

Compare the response for different prepared states.

This is the most important experiment because it directly tests whether physical state participates in later computation.

### 4. Nonlinearity

Measure output versus input:

Y(X)

Test whether a reproducible deviation from a linear model exists.

### 5. Coupling

Measure how a controlled state change modifies the field:

Delta Y / Delta S

This becomes the experimentally grounded coupling coefficient.

### 6. Noise and drift

Measure detector noise, phase noise, amplitude noise, thermal drift, state-preparation variance, and device-to-device variation.

The effective noise parameter must be measured rather than chosen for simulation convenience.

## Kill criteria

Reject a candidate if:

1. A/B outputs are not separable beyond total uncertainty.
2. State retention is too short for the intended operation.
3. State transitions are not reproducible.
4. Apparent state dependence disappears after thermal/drift correction.
5. Read/write energy dominates the computational operation.
6. Required coherent phase readout is impractical.
7. State cross-talk destroys effective dimensionality.
8. The useful parameter envelope is too narrow for fabrication and environmental variation.

## Important boundary

The literature establishes that physical photonic memory, nonlinear response and multi-state behaviour can be measured.

It does **not** establish that those mechanisms naturally implement the Horizon equations.

Therefore the experiment should not ask:

> Find a device that looks like Horizon.

It should ask:

> Measure the physical transfer functions, then determine whether those measured functions can instantiate the required WCR dynamics.

This reduces confirmation bias.

## Experimental infrastructure rule

Per D-012, Horizon should not build a custom laboratory instrument merely to perform this test.

Preferred sequence:

required observable -> existing measurement method -> external laboratory/device platform -> calibration -> causal experiment

Custom instrumentation is justified only if an essential observable has no suitable established measurement path.

## Candidate status

**Photonic WCR:** first mapping candidate.

**Magnonic WCR:** retained as an independent comparison branch. Recent 2026 work demonstrates direct momentum-space detection of nonlinear magnon populations down to nanometre-scale wavelengths, showing that experimentally measurable wave-vector and nonlinear-state observables are available. citeturn0search4

No final material/platform selection is made by this document.

## Research classification

- **Established:** photonic and magnonic systems have measurable wave, nonlinear, memory and state variables.
- **Experimental evidence:** cited external systems demonstrate several individual mechanisms.
- **Mathematical mapping:** WCR abstract variables can be assigned candidate physical observables.
- **Hypothesis:** one physical platform can satisfy the complete causal state-dependent computation requirement.
- **Unresolved:** whether a real device occupies a sufficiently wide useful computational envelope.
- **Unresolved:** energy/latency advantage against electronic baselines.
- **Unresolved:** scaling from demonstrated devices to smartphone and supercomputer architectures.

## Next gate

The next research gate is **not another abstract simulation**.

It is a literature/device-platform audit asking:

1. Which existing platform exposes all required observables?
2. Which external laboratory can perform the A/B experiment?
3. What measurement precision is available?
4. What state-preparation mechanism is available?
5. What timescale can be measured?
6. What energy can be independently estimated?
7. Can the complete causal transfer function be reconstructed without custom Horizon hardware?

Only after those questions are answered should a physical candidate be promoted to V0/V1 experimental testing.
