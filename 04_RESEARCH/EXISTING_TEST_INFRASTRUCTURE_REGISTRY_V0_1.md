# EXISTING TEST INFRASTRUCTURE REGISTRY V0.1

## Purpose

This registry records external measurement methods, instruments, and research facilities that already exist and may be used to test Horizon.

It is **not** a plan to build a Horizon laboratory.

The default research rule is:

> Define the physical observable first, then find an existing measurement method, instrument, or facility capable of measuring it.

Custom instrumentation is a last resort.

## Epistemic status

- **Established:** the listed instruments/facilities are publicly documented as existing by their operators.
- **Candidate for Horizon:** relevance to a future Horizon cell is an engineering screening judgment, not evidence that the facility can test a final Horizon device.
- **Access unresolved:** availability, external-user eligibility, cost, scheduling, sample requirements, and collaboration requirements must be confirmed directly with the facility.
- **No hardware result:** none of these entries constitutes an experiment on Horizon.

## 1. Candidate external facilities in Indonesia

### 1.1 UI Nano Device Laboratory — Depok

Publicly documented equipment includes:

- Semiconductor Parameter Analyzer HP 4145B
- Semiconductor Parameter Analyzer Keithley 4200A-SCS
- RF probe station
- Probe station for Keithley 4200A-SCS
- sputter coater
- furnaces
- maskless photolithography laser

The laboratory states that its facilities support education, research, testing, and innovation, and provides instrument booking/request information.

**Potential Horizon use:**
- electrical state-update measurements;
- I-V characteristics;
- device parameter extraction;
- electrical switching/state characterization;
- probe-level measurements for a physical state cell.

**Source:** https://frontiers.ui.ac.id/spect/laboratory/

### 1.2 UI Nano-Optics Laboratory — Depok

Publicly documented equipment includes:

- Keithley 2450
- LCR meter
- digital oscilloscope
- photodetector testing equipment
- four laser types
- solar simulator
- function generator
- thermal imager

**Potential Horizon use:**
- optical input/output experiments;
- photodetector measurements;
- time-domain electrical observation;
- source excitation;
- optical/electrical coupling characterization.

**Source:** https://physics.ui.ac.id/portfolio/nano-optics-lab/

### 1.3 ITS Photonics Engineering Laboratory — Surabaya

The laboratory publicly lists optical testing services including spectral measurement, optical power measurement, and experimental/device design.

Listed equipment includes:

- optical time-domain reflectometer (OTDR)
- photomultiplier tube
- laser sources
- photodetectors
- monochromator
- UV-VIS spectrometer
- NIR spectrometer
- optical components/devices

**Potential Horizon use:**
- optical power and signal measurement;
- spectral characterization;
- photodetection;
- propagation/delay measurements in suitable optical structures;
- characterization of optical computational cells.

**Source:** https://www.its.ac.id/tfisika/en/facilities/laboratorium/photonics-engineering/

### 1.4 ITS Laboratory of Optoelectronics and Applied Electromagnetics — Surabaya

The laboratory publicly documents research involving:

- optical communication devices;
- switching waveguides;
- optical sensors;
- interferometry;
- nonlinear optical components;
- microwave systems;
- optical and electromagnetic experimentation.

**Potential Horizon use:**
- wave/interference experiments;
- optical waveguide characterization;
- nonlinear photonic device research;
- electromagnetic/microwave alternatives if the physical architecture moves away from optics.

**Source:** https://www.its.ac.id/fisika/en/facilities/laboratories/laboratory-of-optoelectronics-and-applied-electromagnetics/

## 2. Existing measurement classes to search before designing anything

| Horizon observable | Existing measurement class | Candidate instruments/facilities |
|---|---|---|
| Input amplitude | source measurement | function/arbitrary waveform generator; SMU |
| Output waveform | time-domain measurement | digital oscilloscope; digitizer |
| State proxy | electrical/optical state measurement | SMU, oscilloscope, photodetector, optical power meter |
| State retention | time-domain decay measurement | oscilloscope/digitizer + suitable detector |
| Update response | transient measurement | oscilloscope, SMU |
| Phase | phase-sensitive measurement | oscilloscope, lock-in amplifier, VNA or optical interferometry depending on medium |
| Frequency response | frequency-domain measurement | spectrum analyzer, VNA, optical spectrum analyzer |
| Optical power | optical power measurement | optical power meter / photodetector |
| Optical spectrum | spectral measurement | spectrometer |
| Electrical I-V | source-measurement | SMU / semiconductor parameter analyzer |
| Impedance | impedance measurement | LCR meter / impedance analyzer |
| Noise | time/frequency-domain noise measurement | oscilloscope, spectrum analyzer, lock-in amplifier |
| Update energy | voltage/current/power measurement | SMU, power analyzer, synchronized V/I measurement |
| Material structure | material characterization | Raman, FTIR, XRD, SEM/TEM etc. |
| Reset/forget behavior | repeated transient/state measurement | oscilloscope/digitizer/SMU according to physical medium |

This table is a **method-selection map**, not a commitment to any specific instrument.

## 3. Minimum physical test path

The preferred physical workflow is:

```
Horizon hypothesis
      ↓
minimum observable
      ↓
existing measurement method
      ↓
existing instrument
      ↓
existing research facility
      ↓
minimal DUT interface
      ↓
measurement
      ↓
raw data
      ↓
independent analysis
      ↓
comparison with model
```

The test infrastructure should not be allowed to grow ahead of the computational cell.

## 4. Current priority

Before selecting a laboratory, Horizon must first finish the physical definition of the minimum Stateful Core cell.

The first physical observables remain:

1. input (X);
2. state proxy (S);
3. state after update (S');
4. retention/decay time (	au);
5. update delay;
6. read disturbance;
7. noise/variability;
8. reset/forget response;
9. energy per update.

Only after the physical medium is selected should the registry be narrowed to the exact instrument configuration.

## 5. Access caution

A facility being publicly documented does **not** imply unrestricted public access.

Before relying on any facility, verify:

- external-user policy;
- whether individual users or only institutional researchers are accepted;
- sample/device requirements;
- safety requirements;
- calibration status;
- measurement uncertainty;
- cost;
- scheduling;
- required proposal or collaboration;
- data-export format.

## 6. Decision

Do not build a custom Horizon test laboratory while an established measurement method and suitable external facility exist.

If a required observable cannot be measured with available infrastructure, record the gap explicitly before considering custom instrumentation.

## Status

**Version:** 0.1  
**Date:** 2026-10-06  
**Classification:** research infrastructure registry / candidate mapping  
**Hardware experiment:** none  
**Final physical platform:** not selected
