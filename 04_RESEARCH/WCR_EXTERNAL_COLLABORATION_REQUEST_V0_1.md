# WCR External Collaboration Request v0.1

**Date:** 7 October 2026  
**Purpose:** Request clarification on availability/access to an existing photonic-memory DUT for the first Horizon WCR causal experiment.

## 1. Scope

This request is intentionally narrow.

We are **not** requesting fabrication of a new Horizon device.

We are asking whether an existing or comparable ferroelectric-photonic memory device can be made available for an independent characterization experiment.

## 2. Minimum device requirements

A suitable device should ideally provide:

- at least two reproducible nonvolatile or persistent optical states;
- controllable electrical state programming;
- identical optical probing after different state preparation;
- measurable optical transmission/power or resonance response;
- repeatable state preparation;
- sufficient retention to perform repeated measurements;
- an existing laboratory measurement path.

The 2025 HZO-IGZO FeFET + LNOI microring Pockels photonic memory is a direct candidate because its published characterization reports six distinguishable optical states, repeated measurements, optical resonance/transmission characterization, and long retention. This is cited as external literature evidence only; it is not being treated as Horizon validation.

## 3. Proposed minimum experiment

Prepare two states:

\[
S_A \neq S_B
\]

Apply the same optical probe:

\[
X_A=X_B
\]

Measure:

\[
Y_A=T(X,S_A)
\]

\[
Y_B=T(X,S_B)
\]

Use a randomized sequence such as A-B-B-A-A-B and repeat enough times to estimate measurement uncertainty and drift.

The first experiment can use scalar optical transmission/power. Phase-sensitive coherent detection is not required unless later experiments require phase as a computational state coordinate.

## 4. Measurements requested

If the platform permits, measure:

1. state-dependent transmission or resonance shift;
2. repeatability of each state;
3. state retention/decay versus time;
4. state transition response versus programming pulse;
5. measurement noise and drift;
6. write energy if available.

## 5. Questions for the facility/research group

1. Is an existing device/sample from this or a comparable HZO-LNOI photonic-memory platform currently available?
2. Is external academic/independent research access possible?
3. Can controlled state programming and optical probing be performed using the existing setup?
4. What measurements can the existing setup provide?
5. Is raw measurement data available to the collaborating researcher?
6. What collaboration, access, cost, scheduling, authorship, IP, or NDA requirements apply?
7. If the exact 2025 device is unavailable, is there a comparable device with at least two persistent optical states?

## 6. Scientific boundary

The experiment is intended to test one causal property:

> Does a physically retained state measurably change the response of a later identical input?

A positive result would establish the measured state-dependent physical response of the tested device.

It would **not**, by itself, establish a complete Horizon computer, general-purpose computation, smartphone-scale implementation, or supercomputer-scale implementation.

## 7. Requested response

A short response indicating one of the following is sufficient:

- ACCESSIBLE NOW
- ACCESSIBLE VIA COLLABORATION
- COMPARABLE DUT AVAILABLE
- DUT NOT AVAILABLE
- MEASUREMENT CAPABILITY AVAILABLE BUT DUT NOT AVAILABLE
- NOT POSSIBLE

## 8. Technical references

- Xu et al., “Ferroelectric-based Pockels photonic memory,” Nature Communications 16, 8329 (2025), DOI: 10.1038/s41467-025-63850-z.
- NUS SHINE publication page for the same device.
- NUS SHINE Partnership page describing Shared R&D and Dedicated R&D collaboration.

**Important:** This document is a technical request specification, not evidence that external access has been granted.
