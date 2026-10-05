# MINIMUM FALSIFIABLE EXPERIMENT — STWF STATEFUL CORE V0.1

## Status

**Research protocol draft — 2026-10-05**

This document defines the smallest physical experiment that could validate or falsify the central Stateful Core hypothesis without requiring a complete Horizon chip or laboratory.

## 1. Central hypothesis

A physical wave/state system can retain a computational state and update that state directly from a new input:

\[
S_{n+1}=F(S_n,X_n)
\]

For the first target:

\[
S_{n+1}=\lambda S_n+wX_n+\epsilon_n
\]

The key claim is **not** that any resonator automatically performs useful computation. The experiment must determine whether a physical state can be:

1. initialized,
2. retained for a controlled interval,
3. modified by an input,
4. read without destroying the state,
5. updated repeatedly,
6. reset or forgotten predictably.

## 2. Minimal physical loop

\[
X_n \rightarrow \text{wave/state interaction} \rightarrow S_{n+1}
\]

with an optional readout branch:

\[
S_n \rightarrow Y_n
\]

and feedback only if required by the selected physical mechanism:

\[
S_n \rightarrow \text{field} \rightarrow S_{n+1}
\]

The first experiment should use **one state variable or one dominant observable**, not a multi-cell chip.

## 3. Required observables

The experiment must produce time-series measurements for:

- input amplitude/energy,
- state observable,
- output observable,
- update delay,
- state decay,
- noise,
- reset response,
- energy delivered per update.

If the physical medium uses phase, frequency, polarization, mode, displacement, magnetization, or another state variable, that variable must be mapped to a measurable scalar/vector observable.

## 4. Calibration experiments

### C1 — Free decay

Initialize the state and remove the input.

Measure:

\[
S(t)=S_0e^{-t/\tau}+n(t)
\]

Estimate \(\tau\).

This establishes the natural memory lifetime.

### C2 — Single update

Apply one controlled input \(X\).

Measure:

\[
\Delta S=S_{after}-S_{before}
\]

Determine whether \(\Delta S\) is reproducible and approximately proportional to input over any operating region.

### C3 — Repeated update

Apply:

\[
X=[x_1,x_2,...,x_N]
\]

and compare the measured trajectory against:

\[
S_{n+1}=\lambda S_n+wX_n
\]

Estimate \(\lambda\) and \(w\) from measurements rather than assuming them.

### C4 — Read disturbance

Compare state evolution with and without readout.

Define:

\[
D_{read}=|S_{with\ read}-S_{without\ read}|
\]

If observation substantially changes the state, the readout is part of the computational dynamics and must be modeled explicitly.

### C5 — Reset

Drive the state toward a defined reference state.

Measure reset time, residual state, energy, and repeatability.

## 5. First computational test

Use a short integer-like sequence:

\[
X=[3,5,2,7]
\]

Target:

\[
S=[3,8,10,17]
\]

This is deliberately simple. It tests state reuse, not general intelligence.

A physical experiment passes this stage only if the measured state trajectory follows the expected recurrence within a predefined tolerance.

## 6. Precision and error model

Do not compare only final values.

Measure:

\[
e_n=S_n-S_n^{target}
\]

and report:

- mean absolute error,
- RMS error,
- maximum error,
- drift,
- run-to-run variation,
- state-dependent error,
- temperature/environment dependence.

The state must remain distinguishable from noise:

\[
SNR=\frac{\mathrm{signal\ scale}}{\mathrm{noise\ scale}}
\]

## 7. Energy accounting

Report energy for the complete update path:

\[
E_{update}=E_{source}+E_{coupling}+E_{state}+E_{read}+E_{control}
\]

Do **not** report only the energy dissipated in the active physical element.

The first experiment is not required to beat CMOS energy/op. It is required to establish a trustworthy physical energy baseline.

## 8. Falsification criteria

The Stateful Core hypothesis is considered unsupported for a candidate physical mechanism if any of the following persist after reasonable engineering optimization:

1. state cannot be retained for the required update interval;
2. state update is not reproducible;
3. readout destroys or strongly perturbs the state;
4. state noise makes successive states indistinguishable;
5. reset is unreliable or too expensive;
6. input coupling is too weak or uncontrollable;
7. useful operating range is too narrow;
8. required control energy dominates the computation;
9. conversion between information domains dominates the energy/latency budget;
10. the mechanism only stores a signal but does not provide a controllable computational update.

## 9. What this experiment does NOT prove

Passing this experiment does not prove:

- a useful processor has been built;
- STWF is faster than CPUs/GPUs;
- STWF is more energy efficient;
- large-scale interconnects are feasible;
- a selected material is manufacturable;
- a complete Horizon chip can be fabricated.

It only establishes that a candidate physical state mechanism can implement controlled stateful computation at the smallest scale.

## 10. Candidate-medium neutrality

No material is selected by this protocol.

The same test can later be instantiated with optical, microwave/electromagnetic, magnonic, acoustic/mechanical, ferroelectric, memristive, or hybrid mechanisms.

This prevents material choice from being driven by analogy before the required computational behavior is defined.

## 11. Relation to existing physical reservoir computing

Physical reservoir computing already demonstrates that physical media can provide nonlinear dynamics, memory, state evolution, and measurable readouts. These properties are well established as a research area. citeturn0search1turn0search3

Therefore the research claim here must not be:

> "A physical medium can compute using its dynamics."

The narrower STWF research question is:

> Can an explicitly configured wave/state computational cell use persistent state reuse as a direct computational primitive, with measurable update, retention, feedback, and energy characteristics?

This distinction is essential for novelty and falsifiability.

## 12. Next engineering artifact

Before selecting material, define a **platform-neutral Physical Stateful Cell Model** containing:

- state variable,
- wave variable,
- coupling coefficient,
- delay,
- loss,
- nonlinear transfer,
- noise,
- readout,
- reset,
- energy model.

Only after that model produces a measurable parameter set should a candidate physical platform be selected.
