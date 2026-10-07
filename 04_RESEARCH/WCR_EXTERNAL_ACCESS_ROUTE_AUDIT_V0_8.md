# WCR External Access Route Audit V0.8

Date: 7 October 2026

Status: external access planning. No Horizon physical experiment has been performed.

## 1. Decision from V0.7

V0.7 promoted the FeFET-Pockels photonic-memory platform as the first external measurement candidate.

The literature identifies the demonstrated platform with the National University of Singapore (NUS), the Singapore Hybrid-Integrated Next-Generation μ-Electronics Centre (SHINE), and POET Technologies. The published device is an HZO/IGZO FeFET integrated with a lithium-niobate-on-insulator microring resonator. The published characterization uses a tunable laser, polarization control, fiber coupling, optical spectrum analyzer/power sensor, high-speed photodetection, and semiconductor parameter-analysis equipment. citeturn2search0turn2search1

Therefore the most direct external route is not to reproduce the device elsewhere first. It is to seek access to the demonstrated device/platform or to a directly comparable device through the research group or an external collaboration.

## 2. Primary route: NUS / SHINE

### Why this route is technically strongest

SHINE is the research centre directly associated with the demonstrated FeFET-Pockels photonic-memory work. Its published research portfolio includes the HZO-LNOI integrated ferroelectric electro-optic modulator and memory. SHINE also operates heterogeneous-integration, packaging, characterization, and testing infrastructure. citeturn3search0turn3search9

The 2025 paper reports:

- six distinct nonvolatile optical states per FeFET;
- state characterization using repeated measurements;
- optical readout using a monochromatic probe and high-speed photodetection;
- resonance-spectrum characterization;
- electrical state readout;
- optical/electrical measurement instrumentation;
- expected long retention and high write endurance. citeturn2search0

This makes NUS/SHINE the highest-value route because the device, state mechanism, and measurement chain already exist in one research ecosystem.

### What must be requested

The request should be narrow.

Do not ask for fabrication of a Horizon device.

Ask whether an existing or comparable FeFET-Pockels/LNOI photonic-memory device can be used to perform a small independent causal characterization:

1. prepare state A;
2. prepare state B;
3. apply identical optical probe X;
4. measure optical response Y;
5. repeat with randomized A/B order;
6. estimate the uncertainty budget;
7. determine whether the state-dependent output remains statistically distinguishable.

The purpose is independent causal characterization, not reproduction of the original publication's performance claims.

## 3. Secondary route: Indonesian photonics laboratories

Indonesia already has laboratories with relevant optical characterization capabilities, but the current audit does **not** find evidence that the listed facilities possess the exact NUS FeFET-Pockels device.

### ITS — Photonics Engineering Laboratory

ITS publicly lists optical testing services covering spectral measurement, optical power, experimental/device design, and optical-system work. Its equipment list includes lasers, photodetectors, optical components, monochromators, spectrometers, and optical-fiber test equipment. ITS also lists computational photonics and optical simulation as a research area. citeturn0search4

This makes ITS a plausible **measurement-capability partner**, especially if a suitable photonic memory sample becomes available.

It is not currently evidence of access to the FeFET-Pockels device itself.

### ITS — Laboratory of Optoelectronics and Applied Electromagnetics

The laboratory lists work on interferometry, optical communication devices, thin-film optical components, nonlinear photonic-component characterization, and optical instrumentation. citeturn0search5

This is relevant to the WCR coupling/interference/nonlinearity layers, but again there is no evidence in the public material reviewed here that the exact Pockels-memory DUT is available.

### ITB — Optical Instrumentation / Laser Laboratory

ITB publicly describes optical instrumentation and laser facilities supporting optical measurement, laser/fiber research, spectroscopy, and related instrumentation. citeturn0search6turn0search7

This is a possible secondary measurement route, but the same limitation applies: no evidence was found that the exact FeFET-Pockels photonic-memory DUT is available.

## 4. Route ranking

| Route | Exact/comparable DUT likelihood | Measurement capability | Main advantage | Main uncertainty |
|---|---:|---:|---|---|
| NUS/SHINE | Highest | Highest | Device + researchers + infrastructure are co-located | External collaboration/access |
| ITS Photonics Engineering | Unknown | Good for optical characterization | Indonesia-based measurement capability | DUT availability |
| ITS Optoelectronics | Unknown | Relevant optics/nonlinearity | Interferometry and nonlinear photonics | DUT availability |
| ITB optical instrumentation | Unknown | Optical/laser measurement | Established optical instrumentation | DUT availability |

This ranking is a planning assessment, not a claim about institutional willingness to collaborate.

## 5. Critical correction to the experimental plan

The first physical test should **not** require phase-sensitive coherent detection.

The Pockels-memory device already provides a simpler observable:

[
S ightarrow Deltalambda_{res}
ightarrow T(lambda_{probe},S)
]

where the ferroelectric state changes the microring resonance and therefore the transmission at a selected probe wavelength. The published work demonstrates both resonance-spectrum and monochromatic-power readout. citeturn0search0

Therefore the first WCR causal test can use scalar optical power:

[
Y=P_{out}
]

rather than immediately requiring:

[
Y=(Re(E),Im(E)).
]

This significantly reduces experimental complexity.

Phase-sensitive readout remains necessary later if Horizon adopts optical phase as an independent computational coordinate.

## 6. Minimum physical test now defined

### Test A — state-dependent transmission

Prepare:

[
S_A 
eq S_B
]

Apply identical:

[
X=(lambda_{probe},P_{in})
]

Measure:

[
Y_A=P_{out,A}
]

[
Y_B=P_{out,B}
]

Calculate:

[
Delta Y=|Y_A-Y_B|
]

and compare with:

[
U_{total}.
]

Acceptance:

[
Delta Y>U_{total}
]

plus repeatability across independent preparations.

### Test B — state retention

After preparing S_A or S_B, remove the write stimulus and repeatedly measure the optical state:

[
S(t)
]

Fit an appropriate decay/retention model rather than assuming exponential decay.

The measured lifetime becomes the physical parameter replacing the abstract simulator parameter τ.

### Test C — nonlinear/state transition

Apply controlled write amplitude or pulse count and measure:

[
S=f(V_{write},t_{write},N_{pulse},history)
]

The objective is to determine whether the state transition is:

- deterministic;
- multilevel;
- repeatable;
- bounded;
- history dependent;
- sufficiently distinguishable.

## 7. What is already externally demonstrated

The published FeFET-Pockels device already reports six distinct nonvolatile optical states, repeated statistical characterization, optical-power readout, resonance-spectrum characterization, and electrical/optical bimodal readout. citeturn0search0

Therefore Horizon does **not** need to prove from scratch that this class of device can store multiple optical states.

The unresolved Horizon-specific question is narrower:

> Can the measured physical transfer function be used as the stateful computational operator required by WCR?

That distinction is important.

## 8. Current status

**DUT availability:** unresolved.

**External laboratory measurement capability:** demonstrated to exist in multiple institutions.

**Exact Horizon causal experiment:** not performed.

**Best route:** NUS/SHINE collaboration or access to an equivalent FeFET-Pockels/LNOI device.

**Indonesian fallback:** use an established photonics laboratory only after obtaining a suitable DUT/sample.

**Custom Horizon instrumentation:** rejected under D-012 unless no existing measurement path can expose the required observables.

## 9. Next gate

The next research gate is now:

**V0.9 — External collaboration / DUT availability gate**

Required evidence:

1. a real device/sample that exposes a persistent physical state;
2. permission/access to characterize it;
3. existing optical input and output measurement path;
4. electrical state-write/read interface;
5. repeatable state preparation;
6. enough raw data to independently reconstruct the A/B causal test.

Until these exist, the project remains at the **literature-supported candidate / experimental-planning stage**, not physical validation.

No claim of Horizon hardware performance is made.
