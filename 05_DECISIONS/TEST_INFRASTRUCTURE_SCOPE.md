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

## 6. Design constraint

Do not optimize the laboratory before the computational cell is physically defined.

The test environment should evolve from the minimum falsifiable experiment rather than become a second large engineering project.
