# Physical Stateful Cell Sweep V0.1

**Status:** Numerical screening experiment  
**Date:** 2026-10-05  
**Evidence class:** Simulation result only

## Objective

V0.1 tests whether the stateful-cell model has a usable parameter region before any material or device is selected.

The sweep varies:

- state lifetime tau;
- feedback delay;
- state noise;
- read back-action;
- nonlinearity.

The goal is to find a feasible region, not a single impressive simulation.

## Baseline

Input sequence: \`[3, 5, 2, 7]\`

Target accumulator: \`[3, 8, 10, 17]\`

Default time step: Delta t = 1 ns.

The model remains normalized. No material constants are assumed.

## Metrics

Primary:

- relative RMS computational error;
- maximum error;
- state SNR;
- delay/lifetime ratio;
- read disturbance;
- stability.

Secondary:

- normalized update energy;
- normalized reset energy;
- reset burden.

## Screening region

Initial sweep:

- tau: 1, 2, 5, 10, 20, 50, 100 ns
- delay: 0, 1, 2, 5, 10 steps
- noise sigma: 0, 0.01, 0.05, 0.1, 0.25, 0.5
- read back-action: 0, 0.01, 0.05, 0.1
- nonlinearity: linear, saturation, tanh

Initial screening thresholds:

- relative error < 5%;
- state SNR > 10;
- delay/lifetime < 0.1;
- read disturbance ratio < 0.1;
- stable trajectory.

These are engineering screening criteria, not physical laws.

## Important interpretation

A large feasible region is more useful than one fine-tuned point.

If feasibility disappears when noise, delay, or read disturbance changes slightly, the computational cell is fragile.

If feasibility survives broad parameter variation, the concept becomes a stronger candidate for physical mapping.

## Expected next step

After the numerical sweep, select the least demanding physical mechanism capable of reproducing the required parameter region.

Do not select a material because it has the smallest reported energy figure in isolation. The relevant comparison is the complete cell:

\[
E_{cell}=E_{drive}+E_{couple}+E_{state}+E_{read}+E_{control}+E_{reset}.
\]

Recent photonic work demonstrates that memory retention and latency must be considered together; a 2026 study explicitly reports a retention-to-network-latency ratio as an accuracy constraint. citeturn0search10

Recent integrated photonic work also shows that memory, sensing and computation can be co-designed at large scale, reinforcing the need for complete system accounting rather than treating the state element alone as the processor. citeturn0search0

## Falsification

The concept should be reconsidered if no reasonable region simultaneously satisfies the screening criteria, or if the feasible region requires parameter values that have no credible physical implementation.

This sweep does not establish speed, energy advantage, scalability, manufacturability, or hardware feasibility.
