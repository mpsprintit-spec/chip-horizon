# Independent Nonlinear Cross-Coupled WCR Simulation v0.4

Date: 7 October 2026

## Objective

Test the next gate after v0.3:

> Can multiple internal state coordinates remain computationally useful when they are coupled by a nonlinear transformation?

The model uses two state coordinates:

    S = (q, phi)

and a complex wave field a.

This is a numerical experiment only.

## Nonlinear state dynamics

The state is updated from the previous state and the current field intensity:

    q_next   = clamp(0.97*q + 0.08*tanh(I - 1.0) + 0.025*sin(phi), -1, 1)

    phi_next = wrap(phi + 0.12*tanh(I - 1.0) + 0.20*q)

where:

    I = |a|^2

The two coordinates therefore affect one another. q changes the phase evolution, while phi feeds back into q.

The wave field is:

    a_next = 0.91*a + 0.26*sqrt(P)/(1 + i*3.0*q)*exp(i*phi)

The external input P is identical across the state-comparison experiment.

## Experiment 1 — state-dependent response

Two initial states were prepared:

    A = (q=0.20, phi=0.00)
    B = (q=0.20, phi=pi)

The same probe sequence was applied for 120 steps.

The final 20 outputs were compared in complex form.

Result:

- State A converged to a distinct dynamical trajectory.
- State B converged to a distinct dynamical trajectory.
- The output trajectories did not collapse onto the same solution.

The causal criterion therefore passes in the numerical model:

    A != B
    X_A = X_B
    => Y_A != Y_B

## Experiment 2 — nonlinear coupling is actually active

A control simulation was run with cross-coupling removed:

    0.025*sin(phi) -> 0
    0.20*q        -> 0

The state coordinates then behaved as independent channels.

The coupled model produced trajectories that differed from this independent-channel control.

Therefore the observed multidimensional behavior is not merely two independent scalar simulations placed side by side.

## Experiment 3 — perturbation test

A small perturbation was applied only to q while keeping the external input unchanged.

The perturbation propagated into phi through the nonlinear coupling and subsequently altered q again.

Likewise, a perturbation to phi propagated into q and then returned to phi.

This establishes a numerical bidirectional causal loop:

    q -> phi -> q

rather than:

    q     phi
    |      |
    +------+
    independent

## Experiment 4 — collapse test

The model was tested for whether nonlinear coupling forces the two coordinates into one effective scalar variable.

The result was negative within the tested parameter range: q and phi remained distinguishable in the state trajectory and contributed separately to the complex output.

However, this is parameter-dependent. Stronger coupling or stronger damping can cause loss of usable dimensionality.

## Important result

The experiment identifies a new quantity for Horizon research:

### Effective State Dimensionality

A WCR may have N physical coordinates but fewer than N computationally useful dimensions.

Define:

    D_physical = number of physical state coordinates

    D_effective = number of independently controllable,
                  distinguishable and computationally relevant
                  state dimensions

The design objective is not to maximize D_physical.

It is to maximize useful D_effective subject to noise, cross-talk, energy, latency, retention and readout constraints.

## New failure mode discovered

Nonlinear coupling can be either:

1. computationally useful coupling; or
2. destructive state collapse.

Therefore nonlinear interaction must not simply be maximized.

A useful WCR requires a bounded operating region in which:

- state dimensions remain distinguishable;
- coupling creates meaningful transformations;
- perturbations do not explode;
- state does not collapse into one dimension;
- readout remains separable;
- energy remains bounded.

## Relevance to Horizon

This moves the architecture beyond:

    binary state
    ↓
    multilevel scalar state
    ↓
    multidimensional state
    ↓
    nonlinear multidimensional state

The proposed internal computational object is now better described as a **nonlinear physical state-space dynamical system**.

External interface remains:

    binary input -> encoder -> WCR -> decoder -> binary output

The internal representation is not required to be binary.

## What is NOT proven

- physical realization;
- independent physical storage of q and phi;
- real material cross-coupling parameters;
- stable nonlinear operation at room temperature;
- energy efficiency;
- fabrication;
- smartphone-scale density;
- supercomputer scaling;
- computational advantage over CMOS;
- universality.

## Experimental implication

The next physical gate should not merely ask whether a device has nonlinearity.

It should ask whether a real device exhibits:

    state A != state B

with:

    identical later input

and whether the difference remains measurable after nonlinear evolution.

For multidimensional state, the physical experiment should measure at least two observables and test whether perturbing coordinate 1 predictably changes coordinate 2 and vice versa.

Recent photonic and magnonic experiments support the physical existence of nonlinear coupling and multistability, but they do not by themselves validate the complete Horizon WCR causal architecture. For example, compact photonic microcavities have demonstrated tristability from thermo-optical nonlinearity, while magnonic experiments have demonstrated nonlinear mode coupling. These are component-level evidence, not Horizon validation.

## Research status

- Nonlinear cross-coupled numerical model: PASS.
- Bidirectional state coupling: PASS in model.
- Same-input state-dependent response: PASS in model.
- Effective dimensionality concept: introduced.
- Physical experiment: NOT PERFORMED.
- Horizon WCR: NOT VALIDATED.
