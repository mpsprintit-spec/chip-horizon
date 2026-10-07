# WCR External Collaboration / DUT Availability Gate v0.9

**Date:** 7 October 2026  
**Status:** External access route defined; DUT availability NOT YET VERIFIED  
**Research stage:** Pre-V0 physical experiment  
**Applies D-012:** External test infrastructure first

## 1. Purpose

This gate determines whether Horizon can obtain access to an existing physical device/platform capable of performing the minimum WCR causal experiment without building a custom instrument.

The target is not to fabricate a Horizon device at this stage. The target is to test whether a persistent physical state can causally alter the response of a later identical input.

Core causal relation:

\[
S_A \neq S_B, \qquad X_A=X_B, \qquad Y_A \neq Y_B
\]

with the experimental requirement:

\[
|Y_A-Y_B| > U_{total}
\]

where \(U_{total}\) is the combined measurement uncertainty, repeatability uncertainty, and relevant drift budget.

## 2. Current primary route

The first external route is the NUS SHINE ecosystem.

The 2025 Pockels photonic memory publication reports an integrated HZO/IGZO FeFET with an LNOI microring resonator. The device demonstrates six distinct nonvolatile optical states per transistor, femtojoule-per-state operation, projected ten-year retention, and read/write endurance exceeding 10^7 cycles. The optical memory state is manifested through resonance shifts and transmission response. The paper also describes optical and electrical readout.

SHINE's official partnership page states that institutions interested in working with SHINE are welcome to join its consortium and lists Shared R&D and Dedicated R&D as collaboration types. Public contact: **shine@nus.edu.sg**.

This establishes a credible collaboration route, but **does not establish that a sample/DUT is currently available to an external researcher**.

## 3. DUT acceptance specification

A candidate device is acceptable for the first physical gate if it provides:

1. At least two reproducibly distinguishable physical states.
2. Controlled state preparation/write.
3. A later identical probe/input for both states.
4. A measurable output affected by the prepared state.
5. State-dependent output difference exceeding the uncertainty budget.
6. Repeatable A/B/B/A/A/B or equivalent randomized sequence.
7. Measurable state retention or decay.
8. Existing laboratory instrumentation sufficient for the measurement.
9. No requirement to build a custom Horizon instrument for the first test.
10. Access to raw or sufficiently resolved measurement data for independent analysis.

The DUT does **not** need to implement the complete Horizon WCR.

## 4. Minimum experiment

### Test A — State-dependent response

Prepare state A.

Apply identical input \(X\).

Measure \(Y_A\).

Prepare state B.

Apply the same \(X\).

Measure \(Y_B\).

Repeat in randomized order.

Primary scalar optical implementation:

\[
X=(\lambda_{probe},P_{in})
\]

\[
Y=P_{out}
\]

or equivalently transmission:

\[
T=\frac{P_{out}}{P_{in}}
\]

This first test does not require phase-sensitive coherent detection.

### Test B — Retention

After writing state \(S\), measure its observable versus time:

\[
S(t) \approx S_0 e^{-t/\tau}
\]

or use a non-exponential empirical retention model if appropriate.

### Test C — State transition

Characterize:

\[
S_{new}=F(S_{old},V_{write},t_{write},N_{pulse},history)
\]

The purpose is to determine whether the state is controllable and whether history dependence is measurable.

## 5. Candidate route classification

| Route | Status | Interpretation |
|---|---|---|
| NUS/SHINE HZO-LNOI / Pockels memory | **ACCESSIBLE VIA COLLABORATION — route verified** | Official Shared/Dedicated R&D route exists; actual DUT access still requires confirmation |
| Exact 2025 Pockels DUT sample | **NOT VERIFIED** | Publication proves device existence, not current external sample availability |
| Generic integrated photonic test platform | **CAPABILITY EXISTS / DUT MISSING** | Can support optical measurements, but must have an appropriate persistent-state DUT |
| Indonesian optical laboratories | **CAPABILITY EXISTS / DUT MISSING** | Useful fallback measurement partners if a suitable DUT is obtained |
| Custom Horizon instrument | **REJECTED AT THIS STAGE** | Conflicts with D-012 unless no existing measurement path can perform the required observable |

## 6. Why the NUS/SHINE route is currently strongest

The exact mechanism has already been physically demonstrated in the literature:

- HZO ferroelectric polarization provides nonvolatile state.
- The state changes the electro-optic response of lithium niobate.
- The microring resonance shifts according to the programmed state.
- Multiple optical states are experimentally distinguishable.
- Optical transmission and resonance spectra can be measured.
- The device supports electrical and photonic readout.

Therefore the shortest path is not to invent another device. It is to determine whether the existing platform can be accessed for an independent causal characterization.

## 7. What must NOT be claimed

The following remain unproven for Horizon:

- The HZO-LNOI device is a Horizon WCR.
- The device implements the Horizon state equations.
- The device demonstrates useful general-purpose computation.
- The device proves superiority over CMOS/CPU/GPU.
- The device proves smartphone-scale implementation.
- The device proves supercomputer-scale implementation.
- Literature evidence is equivalent to a Horizon experiment.

The current evidence supports only a **candidate physical mechanism and an experimentally accessible causal test**.

## 8. External request scope

The first collaboration request should be narrow.

Requested capability:

> Access to an existing or comparable ferroelectric-photonic memory device and an existing measurement setup capable of controlled state programming, identical optical probing, optical transmission/power measurement, and retention characterization.

The request should explicitly state that fabrication of a new Horizon device is not required for the first experiment.

## 9. Decision gate

### Promote to V0 physical experiment if:

- a real DUT is available;
- state A/B can be prepared;
- identical input can be applied;
- output can be measured;
- uncertainty can be quantified;
- repeated A/B testing is possible.

### Hold if:

- platform exists but DUT access is uncertain;
- state preparation is inaccessible;
- required observables cannot be measured;
- measurement uncertainty cannot be bounded.

### Reject candidate if:

- no persistent state is demonstrated;
- state cannot be reproducibly prepared;
- later identical input produces no measurable state-dependent output;
- measurement requires custom infrastructure disproportionate to the research objective.

## 10. Immediate next action

**User action:** none yet.

**Research action:** prepare the external collaboration request and identify the smallest set of information needed from NUS/SHINE to determine DUT availability.

Once an external response is received, classify it as:

- ACCESSIBLE NOW
- ACCESSIBLE VIA COLLABORATION
- CAPABILITY EXISTS / DUT MISSING
- NOT VERIFIED

Only after that decision will Horizon enter **V0 — physical phenomenon / causal device experiment**.

## 11. Evidence

- NUS SHINE, “Ferroelectric-Based Pockels Photonic Memory”, 19 September 2025.
- Xu et al., *Nature Communications* 16, 8329 (2025), DOI 10.1038/s41467-025-63850-z.
- NUS SHINE official Partnership page, describing Shared R&D and Dedicated R&D collaboration.

**Research classification:**  
Literature evidence = established external evidence.  
DUT access = unresolved.  
Horizon physical validation = not performed.
