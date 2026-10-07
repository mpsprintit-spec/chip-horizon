# External Evidence Test — WCR Candidate Gate v0.1

## Date

2026-10-07

## Purpose

This is a literature/evidence test performed before any Horizon hardware exists. It does **not** constitute a Horizon physical experiment.

The test asks whether existing experimental results satisfy individual prerequisites of the proposed WCR mechanism.

## Test matrix

| Requirement | Photonic evidence | Magnonic evidence | Horizon gate |
|---|---|---|---|
| Propagating physical field | PASS | PASS | prerequisite |
| Interference / coherent interaction | PASS | PASS | prerequisite |
| Nonlinear physical response | PASS | PASS | prerequisite |
| Multiple distinguishable physical states | PARTIAL/PASS at component level | PASS at demonstrated spin-texture level | must be measured in candidate WCR |
| Controlled state transition | PASS at demonstrated device level | PASS at demonstrated spin-texture level | must be coupled to later computation |
| Retention / decay | PASS at demonstrated memory devices | PASS at demonstrated magnetic states | operating lifetime must be measured |
| Same later input gives state-dependent output | NOT YET PROVEN for Horizon WCR | NOT YET PROVEN for Horizon WCR | decisive gate |
| Binary-compatible I/O | plausible/established at device interfaces | plausible/established at RF interfaces | must be measured end-to-end |
| Smartphone-scale density | unresolved | unresolved | future gate |
| Supercomputer scaling | unresolved | unresolved | future gate |

## Photonic evidence

A 2026 Nature Sensors report demonstrated a monolithic 7,378-neuron photonic chip with long- and short-term memory dynamics and integrated sensing/processing/memory. This passes several component-level prerequisites: photonic propagation, memory, nonlinear processing, and integration. It does **not** prove the specific Horizon causal WCR architecture or general-purpose computation. citeturn0search0

A 2026 Nature report also demonstrated an integrated photonic deep neural network in which linear and nonlinear computations were performed on a single photonic chip. This further supports physical feasibility of nonlinear photonic computation, but remains a task-specific neural architecture rather than a Horizon WCR. citeturn0search1

## Magnonic evidence

A 2025 Nature Communications experiment demonstrated controlled single-shot interference of multiple magnon pulses in remotely coupled YIG resonators. It measured coherent interference as a function of frequency detuning and time delay, demonstrating controllable phase-sensitive wave interaction. citeturn0search3

A 2025 Nature Communications experiment demonstrated deterministic switching among three stable antiferromagnetic spin-texture states, with reproducible switching over 1,000 cycles. This is particularly relevant to Horizon's rich-state hypothesis because the demonstrated states are physically distinct, controllable, and persistent on the experimental timescale. However, the experiment does not establish that a subsequent computational transformation is conditioned on the prepared state in the WCR sense. citeturn0search4

## Result

### Photonic

Component-mechanism test: **PASS**

Horizon causal WCR test: **NOT TESTED**

### Magnonic

Component-mechanism test: **PASS**

Horizon causal WCR test: **NOT TESTED**

## Why the decisive test is still open

The critical experiment is not merely:

STATE A ≠ STATE B

It is:

1. prepare STATE A;
2. apply input X;
3. measure Y_A;
4. prepare STATE B;
5. apply the **same** X;
6. measure Y_B;
7. establish |Y_A − Y_B| > complete uncertainty budget;
8. repeat independently.

Only this demonstrates that the internal physical state participates causally in the later computation.

## Decision

**Do not reject either candidate.**

Both have experimentally demonstrated physical ingredients required by the Horizon hypothesis. Neither has yet demonstrated the complete Horizon WCR causal mechanism.

The next experimental action should therefore be to locate an existing external laboratory/device platform where the A/B causal protocol can be performed without building custom Horizon instrumentation.

## Epistemic status

- Literature observation: PASS.
- Component physical plausibility: PASS.
- Horizon WCR causal mechanism: OPEN.
- General-purpose computation: OPEN.
- Energy advantage: OPEN.
- Smartphone-scale implementation: OPEN.
- Supercomputer scaling: OPEN.
