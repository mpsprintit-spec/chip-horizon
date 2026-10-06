# HORIZON WAVE COMPUTATIONAL REGION V0.1

## Status

Research architecture specification.

A WCR is the smallest proposed physical region that can demonstrate the complete Horizon computational mechanism:

wave evolution + nonlinear interaction + physical state + feedback + measurable input/output.

This document does not select a final material or claim that such a device has been fabricated.

## 1. Definition

A Wave Computational Region (WCR) is a bounded physical region containing:

1. a wave propagation domain;
2. one or more controllable coupling paths;
3. a nonlinear interaction mechanism;
4. a physical state variable;
5. a feedback path from state to subsequent wave evolution;
6. an input interface;
7. an output observable.

A passive waveguide, resonator, or interference network alone is therefore not sufficient to qualify as a complete WCR.

## 2. Functional topology

    INPUT
      |
      v
    ENCODER
      |
      v
    WAVE FIELD
      |
      +---- propagation
      +---- coupling
      +---- interference
      |
      v
    NONLINEAR INTERACTION
      |
      +------> OUTPUT OBSERVABLE
      |
      v
    PHYSICAL STATE
      |
      +---- retention / decay
      +---- update
      +---- reset
      |
      +--------------------+
                           |
                           v
                     STATE-DEPENDENT
                     WAVE INTERACTION
                           |
                           +----> WAVE FIELD

The exact physical topology remains open.

## 3. Minimum computational behavior

The WCR must be capable of history-dependent computation.

The minimum abstract contract is:

S_(t+1) = F(S_t, X_t)

Y_t = G(S_t, X_t)

The wave field supplies the physical interaction through which F and G are realized.

A stronger WCR contract is:

Psi_(t+1) = H(Psi_t, S_t, X_t)

S_(t+1) = F(S_t, Psi_t, X_t)

Y_t = G(Psi_t, S_t)

This distinguishes a stateful wave computer from a purely feed-forward wave transformer.

## 4. WCR boundaries

The WCR boundary is defined by functional causality, not by an arbitrary geometric box.

Inside the boundary must be all physical mechanisms required for:

- wave evolution;
- nonlinear interaction;
- state update;
- state influence on subsequent computation;
- observable output.

External electronics, lasers, detectors, drivers, controllers, and test instruments may remain outside the WCR boundary if their function is only to provide or observe the computational mechanism.

However, their energy, latency, bandwidth, and conversion overhead must be included in system accounting.

## 5. Candidate wave medium

The architecture currently keeps the wave medium open.

Optical/electromagnetic waves are a primary candidate because they support propagation, interference, phase encoding, spatial routing, and high bandwidth.

This is a candidate engineering choice, not a final material decision.

Other wave domains remain possible if they satisfy the same WCR contract.

## 6. Candidate state medium

The state medium must provide a controllable physical variable S.

Candidate mechanisms include:

- resonant state;
- memristive/resistive state;
- ferroelectric state;
- magnetic/spintronic state;
- phase-change state;
- other material or device states that interact with the wave field.

No candidate is selected by this specification.

## 7. State requirements

A usable WCR state must have:

- measurable state;
- controlled update;
- predictable retention or decay;
- reset/overwrite mechanism;
- sufficient state separation;
- acceptable variability;
- controlled coupling to the wave field.

For exponential decay:

S(t) = S0 exp(-t/tau)

where tau is measured.

The corresponding discrete retention factor is:

lambda = exp(-Delta_t/tau)

State lifetime is therefore a computational parameter, not merely a material property.

## 8. Nonlinearity requirement

The WCR must contain a useful nonlinear operation.

A linear system obeys:

F(a+b) = F(a) + F(b)

A required nonlinear region violates this relation for at least some operating range:

F(a+b) != F(a) + F(b)

Potential functions include thresholding, saturation, switching, state-dependent coupling, or nonlinear phase/amplitude response.

The exact nonlinear mechanism remains unresolved.

## 9. Feedback requirement

State must influence subsequent computation.

A minimal causal loop is:

X_t -> wave -> state_t+1 -> modified wave -> Y_(t+1)

The loop must have measurable:

- delay;
- gain/coupling;
- stability range;
- noise accumulation;
- state contamination;
- reset behavior.

If state cannot measurably influence subsequent wave evolution, the implementation does not satisfy the stateful WCR definition.

## 10. Signed information

The mathematical model may require positive and negative contributions.

Candidate physical representations include:

- phase opposition;
- dual-rail/differential representation;
- coherent phase-sensitive detection;
- differential state variables.

Intensity-only readout may discard phase/sign information and therefore cannot automatically be assumed sufficient.

The physical signed representation remains unresolved.

## 11. WCR observables

A WCR experiment must expose measurable observables:

### Wave observables

- amplitude;
- phase;
- frequency;
- spectrum;
- timing;
- propagation loss;
- coupling;
- mode behavior where applicable.

### State observables

- state value;
- state lifetime;
- update response;
- reset response;
- drift;
- noise;
- variability.

### Computational observables

- input/output relationship;
- latency;
- precision;
- repeatability;
- energy;
- state reuse;
- error rate.

## 12. Minimum WCR test contract

A candidate WCR is not accepted merely because a wave propagates.

The minimum validation sequence is:

1. demonstrate controllable wave propagation;
2. demonstrate controllable coupling/interference;
3. demonstrate measurable nonlinearity;
4. demonstrate a measurable physical state;
5. demonstrate controlled state update;
6. demonstrate retention/decay;
7. demonstrate reset;
8. demonstrate state-dependent modification of later wave behavior;
9. demonstrate a reproducible input/output computation;
10. measure complete energy and latency.

These are validation requirements derived from the architecture, not a proposal to build a custom laboratory.

Existing external instruments and facilities should be used.

## 13. WCR parameter vector

A candidate implementation can be represented by:

C_WCR = {
  geometry,
  wave_medium,
  state_medium,
  coupling,
  nonlinear_function,
  retention_tau,
  delay,
  bandwidth,
  loss,
  noise,
  readout,
  reset,
  control
}

The vector is a specification interface, not a claim that these parameters are independently programmable.

## 14. WCR performance quantities

The minimum quantities are:

E_op = complete energy per useful computational operation

T_op = end-to-end operation latency

B = usable computational bandwidth

P = computational precision

R = reproducibility

tau = state lifetime

D = state density

C = coupling capacity

L = propagation loss

N = noise/variability budget

The useful operating point must satisfy all required constraints simultaneously.

## 15. Kill conditions

A candidate WCR should be rejected or redesigned if:

- state cannot affect subsequent computation;
- nonlinearity is too weak or uncontrollable;
- state retention is insufficient;
- reset is impractical;
- noise destroys state separation;
- coupling loss dominates;
- conversion energy dominates;
- readout destroys the useful state;
- feedback is unstable;
- useful precision cannot be achieved;
- complete energy/op is not competitive for the intended workload;
- scaling from WCR to local arrays becomes communication-dominated.

## 16. Scale relationship

The WCR is not the final computer.

It is the primitive that must remain physically meaningful when replicated:

WCR -> Core -> Tile -> Cluster -> Chip -> Supercomputer

Replication is valid only if WCR interactions remain controllable and system communication does not dominate the computation.

## 17. Epistemic status

### Established physics

Wave propagation, interference, attenuation, finite propagation delay, nonlinear material responses, and physical state retention are established phenomena in appropriate physical systems.

### Mathematical deduction

The stateful feedback equations define a testable computational contract.

### Horizon architecture proposal

A WCR should combine wave dynamics, nonlinear interaction, physical state, feedback, and measurable I/O in one causally closed computational region.

### Engineering hypothesis

Such a WCR can become the scalable primitive of a computer whose same mechanism extends from smartphone-class chip to supercomputer.

### Unresolved

Final wave medium, state medium, geometry, nonlinear mechanism, signed representation, fabrication process, operating point, and achievable energy/latency remain open.
