# TEST INFRASTRUCTURE SCOPE

## Status

**Decision record — 2026-10-05**

This document separates the Horizon computational chip from the infrastructure used to validate it.

The current STWF work exposed an important scope boundary: a browser visual laboratory is useful for developing and testing the mathematical model, but it is not itself part of the chip architecture. A future physical implementation will also require a test fixture and measurement system.

## 1. Three distinct layers

### Layer A — Device Under Test (DUT)

The actual Horizon computational device.

Target responsibilities:

- wave propagation / coupling
- interference
- nonlinear interaction
- computational state
- state retention / decay
- feedback
- input and output interfaces

The DUT is the primary research object.

### Layer B — Test Fixture

The physical interface between the DUT and laboratory instruments.

Possible functions:

- mechanical mounting
- optical / RF / electrical coupling
- alignment
- thermal control
- bias routing
- signal injection
- signal extraction
- shielding / isolation
- calibration references

The fixture must not be counted as computational capability of the chip.

### Layer C — Test and Measurement System

External equipment used to characterize the DUT.

Depending on the final physical implementation, this may include:

- signal source
- wavelength/frequency source
- polarization control
- power measurement
- detector
- oscilloscope / time-domain measurement
- electrical source-measure unit
- temperature measurement/control
- positioning/alignment system
- control computer and acquisition software

These are validation infrastructure, not part of the computational core.

## 2. Development hierarchy

The research should proceed in this order:

1. mathematical model
2. browser visualization
3. physical abstraction model
4. minimal device demonstrator
5. minimal test fixture
6. measurement procedure
7. calibrated physical experiment
8. only then larger chip architecture

This prevents the project from simultaneously becoming a chip-design project, laboratory-instrumentation project, and manufacturing project before the computational principle is validated.

## 3. Scope rule

A component belongs to the **chip** only if removing it would remove the intended computational mechanism from the DUT.

A component belongs to the **test system** if its primary purpose is to stimulate, observe, calibrate, protect, align, or characterize the DUT.

A component belongs to the **fixture** if it provides the physical/electrical/optical interface required to test the DUT but does not implement the computational mechanism itself.

## 4. Important consequence

We should **design the test requirements before designing the full laboratory**.

The immediate question is not:

> "How do we build the whole laboratory?"

It is:

> "What minimum observable quantities must be measured to falsify or validate the STWF Stateful Core?"

For the current stateful model, the minimum measurement set is likely:

- input signal
- output signal
- state proxy
- propagation delay
- attenuation/loss
- phase or equivalent signed-state observable
- noise
- state retention time
- update energy
- reset/forget behavior

The exact instruments depend on which physical medium survives the material and device selection stage.

## 5. Research classification

- **Established engineering principle:** physical devices require suitable stimulation, coupling, measurement, and calibration infrastructure.
- **Mathematical deduction:** the simulator parameters must eventually map to measurable quantities such as lifetime, delay, loss, coupling, noise, and energy.
- **Proposed synthesis:** separate DUT, fixture, and measurement system as independent architectural layers.
- **Unresolved:** final physical medium, material stack, coupling method, detector architecture, and laboratory instrumentation.
- **Not yet demonstrated:** any claim that the proposed STWF Stateful Core outperforms conventional electronics.

## 6. External infrastructure first

The default assumption is that testing will use instruments, measurement methods, and research facilities that already exist outside the Horizon project.

The workflow is:

1. define the falsifiable claim;
2. define the minimum observables;
3. identify established measurement methods for those observables;
4. identify existing commercial instruments or research facilities that provide those methods;
5. design only the minimum DUT interface/fixture needed to connect the Horizon cell to that infrastructure;
6. acquire and analyze the measurements.

Custom instrumentation is a last resort. It is justified only when no suitable existing method or instrument can measure a required observable and the missing capability is essential to the experiment.

## 7. Scope boundary

The following are explicitly **outside the Horizon core project** unless a specific research requirement forces reconsideration:

- custom oscilloscope development;
- custom signal-generator development;
- custom detector development when a suitable detector exists;
- custom power/energy measurement systems when standard instruments exist;
- custom calibration systems;
- a dedicated Horizon measurement laboratory;
- a browser-based test laboratory intended to substitute for physical instrumentation.

The existing browser laboratory remains a software verification and visualization tool only.

## 8. Design constraint

Do not optimize or expand test infrastructure before the computational cell and its minimum observables are physically defined. The test environment must remain subordinate to the device-under-test and must not become a second large engineering project.
