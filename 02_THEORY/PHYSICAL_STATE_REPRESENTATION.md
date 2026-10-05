# Physical State Representation and Computation

Status: foundational theory.

## Purpose

This document fixes a conceptual point that must precede material selection and chip architecture:

**A physical state does not intrinsically contain a number.**

A number is assigned through a representation/mapping from a measurable physical state to an abstract computational value.

\[
M:P\rightarrow N
\]

where:

- \(P\) = physical state
- \(M\) = representation/measurement mapping
- \(N\) = computational value

## 1. Physical state

A system possesses a physical configuration \(P\). Examples include:

- electrical charge
- voltage
- current
- magnetization
- optical amplitude or phase
- resonance frequency
- mechanical displacement
- acoustic amplitude or phase
- polarization

The physical quantity exists independently of the numerical interpretation.

## 2. Representation

We choose a mapping:

\[
N=M(P)
\]

Example:

\[
P_0\rightarrow0
\]

\[
P_1\rightarrow1
\]

or a continuous mapping:

\[
P\rightarrow3.7.
\]

Changing the unit or encoding changes the numerical representation without necessarily changing the physical state.

## 3. Computation

A physical system evolves according to some physical law:

\[
P_{t+1}=F(P_t,X_t).
\]

A computational interpretation exists when the representation mapping makes that physical transition correspond to a desired mathematical transformation:

\[
M(P_{t+1})
=
f(M(P_t),M(X_t)).
\]

This is the key criterion.

The physical system does not need to contain an abstract number internally. Its state only needs to participate in a reproducible causal transformation that is isomorphic or sufficiently faithful to the desired computation under the chosen representation.

## 4. Example: physical accumulator

Suppose a physical quantity \(P\) is mapped to a numerical state \(S\):

\[
S=M(P).
\]

If the physical dynamics satisfy:

\[
P_{t+1}=F(P_t,X_t)
\]

and the mapping gives:

\[
M(P_{t+1})=M(P_t)+M(X_t),
\]

then the physical dynamics implement an accumulator:

\[
S_{t+1}=S_t+X_t.
\]

For:

\[
X=[3,5,2,7]
\]

the abstract trajectory is:

\[
0\rightarrow3\rightarrow8\rightarrow10\rightarrow17.
\]

The numbers are the computational interpretation. The physical substrate undergoes its own continuous or discrete physical evolution.

## 5. Why arbitrary labeling is insufficient

Any object can be assigned arbitrary labels. That alone does not make it a computer.

A valid computational mapping requires:

1. distinguishable physical states;
2. a defined encoding of inputs;
3. controlled or sufficiently predictable state transitions;
4. a decoding/readout mapping;
5. repeatability within an acceptable error bound;
6. a causal correspondence between physical evolution and the intended mathematical transformation.

A random object labeled with numbers fails these requirements.

## 6. Stateful computation

The relevant class for Horizon is:

\[
S_{t+1}=F(S_t,X_t).
\]

The current state participates in producing the next state.

This differs from a memoryless mapping:

\[
Y_t=F(X_t).
\]

A stateful system can retain information from previous inputs and transform that information together with new input.

## 7. Important distinction

Three layers must remain separate:

### Physical layer

What actually evolves?

\[
P_t\rightarrow P_{t+1}.
\]

### Representation layer

How is the physical state interpreted?

\[
S_t=M(P_t).
\]

### Computational layer

What mathematical transformation does the represented evolution realize?

\[
S_{t+1}=f(S_t,X_t).
\]

Confusing these layers leads to incorrect claims such as “the material stores a number” or “the wave is performing arithmetic” without defining the physical observable and mapping.

## 8. Consequence for Horizon

Horizon research should therefore not begin by searching for a “material that can calculate.”

The correct sequence is:

\[
\boxed{
\text{physical degree of freedom}
\rightarrow
\text{state dynamics}
\rightarrow
\text{representation}
\rightarrow
\text{computational transformation}
}
\]

Only after this mapping is demonstrated should material selection and device architecture be optimized.

## Evidence classification

**Established principle:** physical computing can use physical dynamics as a computational kernel when input encoding, physical evolution, and output decoding are defined.

**Mathematical deduction:** a physical transition becomes an implementation of a mathematical function when the chosen representation maps the physical transition to that function within specified error bounds.

**Proposed Horizon synthesis:** use persistent physical state as a first-class computational variable and investigate \(S_{t+1}=F(S_t,X_t)\) before designing a full chip.

**Not demonstrated:** no Horizon physical device has yet demonstrated this mapping experimentally.

## Research implication

The next fundamental experiment should not ask “Can the chip calculate?”

It should ask:

> Can a chosen physical observable be encoded, transformed by controlled physical dynamics, and decoded so that the measured trajectory reproduces a specified mathematical transformation within a falsifiable error bound?

That experiment is the bridge from abstract physical computation to a real Horizon computational element.
