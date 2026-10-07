# NATURAL COMPUTATIONAL MECHANISM CANDIDATE SCREEN V0.1

## Status

**Epistemic class:** literature-grounded candidate screening / proposed research synthesis.

This document does not select a final Horizon material. It identifies physical mechanisms that already demonstrate pieces of the required behavior and asks which combination could form a richer internal computational state while retaining a binary external interface.

## 1. Required mechanism

The target is not optical computing by itself.

The candidate mechanism should provide, preferably in one coupled physical system:
- multiple distinguishable internal states;
- propagation or interaction of physical signals;
- nonlinear transformation;
- state retention or controlled decay;
- feedback;
- local coupling;
- measurable input/output;
- a path toward dense integration.

The desired system-level contract is:

binary input -> encoding -> rich physical state -> physical evolution/interactions -> binary readout

## 2. Candidate A — integrated photonic field + nonlinear/state element

Photonic systems provide mature mechanisms for propagation, interference, phase and amplitude manipulation. Recent integrated-photonic work also demonstrates analog signal processing and programmable photonic nonlinearity. These facts support the wave-layer requirement, but do not by themselves establish persistent computational state.

**Strength:** wave propagation and interference.

**Weakness:** nonlinear and persistent-state functions may require additional devices or materials; electro-optical conversion can dominate system cost.

**Horizon role:** candidate wave field.

## 3. Candidate B — magnonic/spin-wave field + magnetic/spintronic state

Spin-wave systems provide propagating collective excitations with amplitude, phase and interference. Spintronic systems also provide nonlinear and nonvolatile physical degrees of freedom and can couple to photonic and phononic systems.

**Strength:** wave dynamics and intrinsic magnetic state are physically related.

**Weakness:** efficient generation, detection, retention/control, variability and dense integration remain difficult engineering questions.

**Horizon role:** strong candidate for investigating a genuinely stateful wave substrate rather than simply adding memory beside a wave processor.

## 4. Candidate C — ferroelectric physical state + electronic/field interaction

Ferroelectric polarization is a directly physical state variable. Recent reviews report nonvolatile polarization, multilevel/analog programmability through partial domain switching, scalable thin-film integration, and computing applications.

**Strength:** controllable persistent state and multilevel behavior.

**Weakness:** by itself it is not a wave-computation mechanism; it needs a coupling mechanism that turns state into useful physical transformation.

**Horizon role:** candidate state/nonlinearity layer.

## 5. Candidate D — memristive/oxide state + wave or electrical field

Memristive systems provide history-dependent conductance and analog state. This maps naturally onto the state equation required by the Stateful Core.

**Strength:** explicit history dependence and in-memory computation.

**Weakness:** variability, noise, precision and peripheral overhead can erase system-level benefits.

**Horizon role:** state element or alternative non-wave baseline.

## 6. Candidate E — phononic/acoustic field + material state

Mechanical waves provide spatial and temporal degrees of freedom, resonances, delay and nonlinear interactions.

**Strength:** physical delay and resonance can naturally create temporal computation.

**Weakness:** losses, speed and integration density are major concerns for a smartphone-scale general-purpose substrate.

**Horizon role:** mechanism exploration, not current primary candidate.

## 7. Current screening result

The most interesting direction is not to choose a material immediately.

The strongest research hypothesis is a coupled rich-state region in which a propagating physical field and a persistent material/collective state are not separate subsystems but interact causally:

input field -> field evolution -> nonlinear interaction -> physical state update -> feedback -> later field response

Two particularly important candidate families for this experiment are:

1. photonic field + state/nonlinear element;
2. magnonic/spin-wave field + magnetic/spintronic state.

Ferroelectric and memristive systems remain important state-layer candidates and should be used as comparison baselines.

## 8. Why this is different from simply using more bits

The hypothesis is not that four physical levels are automatically equivalent to two extra bits.

The question is whether the physical state participates directly in transformation:

S_(t+1) = F(S_t, X_t)

rather than merely storing a binary or multibit result between conventional operations.

A useful candidate therefore combines representation and dynamics.

## 9. First falsifiable experiment

Before fabricating a Horizon chip, test whether a candidate physical region can show:

1. at least N reliably distinguishable internal states;
2. controlled transitions between states;
3. measurable retention/decay;
4. the same later input producing different output for different prior states;
5. repeatable state-dependent behavior;
6. bounded error under noise;
7. measurable write/read/operation energy;
8. measurable latency.

N must be determined experimentally from the noise distribution and readout uncertainty; it must not be chosen merely because it looks impressive.

## 10. Important negative result to preserve

If a candidate has many nominal physical states but those states cannot be reliably distinguished, written, retained, or read, then its apparent state richness is not computational capacity.

Likewise, if encoding and decoding energy dominate the physical computation, the candidate fails the end-to-end efficiency objective even if its internal physics is elegant.

## 11. Current conclusion

No final physical substrate is selected.

The immediate research object is:

a causally stateful physical computational region with a richer internal state space and a binary-compatible external interface.

This is the next physical question for Horizon, and it remains a hypothesis until experimentally demonstrated.