# Minimum Physical Computation Experiment V0.1

Status: proposed experimental protocol.

## Question

Can one measurable physical degree of freedom be used as a computational variable such that a controlled physical transition reproduces a specified mathematical function?

This experiment deliberately comes before material selection for a Horizon chip.

## Minimal abstraction

Choose one physical observable:

\[
P
\]

Define an encoding/decoding map:

\[
S=M(P).
\]

Apply an input:

\[
X=M(P_X).
\]

Measure the resulting state:

\[
P' .
\]

Decode:

\[
S'=M(P').
\]

The experiment tests whether:

\[
S'\approx f(S,X)
\]

over repeated trials and a defined operating range.

## First target

Use the simplest stateful function:

\[
f(S,X)=S+X.
\]

Reference sequence:

\[
X=[3,5,2,7]
\]

with:

\[
S_0=0
\]

and expected:

\[
S=[3,8,10,17].
\]

The first experiment does not require high speed, high density, or low energy.

It asks only whether the physical mechanism can reproduce the transformation.

## Experimental loop

\[
\boxed{
\text{initialize}
\rightarrow
\text{encode }X
\rightarrow
\text{physical interaction}
\rightarrow
\text{measure }P
\rightarrow
\text{decode }S
\rightarrow
\text{compare with }f(S,X)
}
\]

Repeat the same sequence many times.

## Required observables

At minimum:

1. input magnitude or equivalent encoded input;
2. initial physical state;
3. final physical state;
4. decoded computational value;
5. update time;
6. measurement noise;
7. run-to-run variation.

Optional but important:

- state decay;
- read disturbance;
- reset time;
- reset residual;
- drive energy;
- coupling loss;
- temperature dependence.

## Falsification

The proposed physical mapping is rejected for this mechanism if, within a clearly specified operating range:

- states cannot be reliably distinguished;
- the input cannot reproducibly alter the state;
- the transition does not match the target function;
- error is dominated by uncontrolled drift/noise;
- repeated trials are not reproducible;
- readout destroys or substantially changes the state;
- reset cannot return the system to a known initial state.

A failed mechanism is not a failure of physical computing in general.

## Evidence levels

### Established physics

The chosen physical system follows its experimentally known physical dynamics.

### Measurement result

The measured observable and its uncertainty.

### Mathematical mapping

The chosen \(M(P)\) and target function \(f\).

### Experimental validation

The measured trajectory agrees with the mathematical model within predefined error bounds.

### Horizon hypothesis

A successful minimal cell could become a computational primitive for a larger physical computational fabric.

## Important constraint

No claim of “computer,” “processor,” “supercomputer,” energy advantage, or speed advantage is permitted from this experiment alone.

The experiment only establishes whether one physical degree of freedom can serve as a controllable computational state under the selected representation.

## Relation to current physical-computing research

Recent work defines a physical computing kernel around input encoding, internal physical evolution, and output decoding, with programmability of the input-output evolution as an important criterion. This experiment adopts that discipline while making the Horizon requirement narrower: first demonstrate one explicit stateful mathematical transformation.

## Next decision gate

Only if the minimum experiment succeeds should we:

1. characterize retention;
2. characterize noise and precision;
3. characterize nonlinear operations;
4. characterize coupling between multiple states;
5. compare physical platforms;
6. design a computational cell;
7. design an array;
8. design a chip.

