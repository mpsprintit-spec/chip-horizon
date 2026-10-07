# Independent WCR Operating Envelope Sweep v0.5

**Date:** 7 October 2026  
**Status:** Numerical simulation / hypothesis testing  
**Physical experiment:** Not performed

## Objective

Extend the nonlinear cross-coupled WCR model from v0.4 into an operating-envelope sweep.

The question is whether useful state-dependent computation survives a range of damping/retention, cross-coupling, nonlinear strength, and additive state noise.

## Model

Internal state:

S = (q, phi)

Field:

a_(t+1) = rho*a_t + kappa/(1+i*K*q_t) * exp(i*phi_t)

with kappa = 0.26 and K = 3.0.

State update:

q_(t+1) = clip[rho*q_t + eta*tanh(|a_t|^2-1) + c*sin(phi_t) + noise, -1, 1]

phi_(t+1) = wrap[phi_t + 0.5*eta*tanh(|a_t|^2-1) + 0.8*c*q_t + noise]

Two initial states receive the same external probe:

- A = (q=0.20, phi=0)
- B = (q=0.20, phi=pi)

Each run contains 120 steps. Metrics use the final 30 steps.

## Sweep

Total combinations: 4 x 4 x 4 x 5 = 320.

| Parameter | Values |
|---|---|
| rho | 0.80, 0.90, 0.97, 0.995 |
| coupling | 0.02, 0.10, 0.20, 0.40 |
| nonlinear | 0.02, 0.08, 0.20, 0.40 |
| noise | 0, 0.01, 0.05, 0.10, 0.20 |

## Metrics

Output contrast:

C_y = |Y_A-Y_B| / ((Y_A+Y_B)/2)

Higher values mean the same external input produces more distinguishable outputs for different internal states.

State separation:

D_S = mean sqrt((q_A-q_B)^2 + wrap(phi_A-phi_B)^2)

A run is bounded when q remains inside its defined range and field magnitude remains below 100.

Exploratory gate:

- output contrast > 0.10
- state separation > 0.5
- bounded dynamics

A parameter triple is called robust in this sweep when it passes at least 80% of tested noise points up to noise = 0.10. This is an internal research criterion, not a physical standard.

## Numerical result

The sweep produced 320 parameter/noise combinations.

Multiple robust regions appeared. Examples of parameter triples passing all tested noise levels up to 0.10 included:

| rho | coupling | nonlinear |
|---:|---:|---:|
| 0.80 | 0.10 | 0.02 |
| 0.90 | 0.02 | 0.02 |
| 0.90 | 0.10 | 0.08 |
| 0.90 | 0.10 | 0.20 |
| 0.90 | 0.40 | 0.40 |
| 0.97 | 0.10 | 0.08 |
| 0.97 | 0.20 | 0.02 |
| 0.97 | 0.20 | 0.08 |
| 0.97 | 0.20 | 0.20 |
| 0.995 | 0.10 | 0.02 |
| 0.995 | 0.20 | 0.08 |
| 0.995 | 0.20 | 0.20 |

At noise = 0.10, the strongest measured output-contrast case in this sweep was approximately 1.35, with bounded dynamics and state separation approximately 0.88.

## Interpretation

v0.4 showed that nonlinear cross-coupling can preserve causal separation for one parameter choice.

v0.5 shows that the phenomenon is not restricted to one isolated point of the tested grid. Several bounded regions retain state-dependent response under moderate simulated noise.

This does not establish a physical operating envelope.

The abstract parameters must eventually map to measurable quantities:

- Q factor / damping rate
- coupling coefficient
- nonlinear susceptibility or saturation coefficient
- state-transition energy
- state retention time
- phase/amplitude noise
- fabrication variability
- readout noise
- thermal drift
- reset cost

## Important observation: retention is not automatically beneficial

Increasing rho extends memory but also increases history contamination.

The design objective is therefore not maximum retention. It is maximum useful state lifetime subject to separability, controllability, stability, noise tolerance and reset requirements.

Likewise, increasing nonlinearity is not automatically beneficial. Too little may make state interaction weak; too much may produce hysteresis, instability, or uncontrolled path dependence.

Recent experiments demonstrate relevant nonlinear multistability in compact photonic systems and hysteretic nonlinear mode hopping in magnon systems. These support component-level plausibility, not Horizon validation. citeturn0search0turn0search3

## New design concept: Effective Computational State Envelope

Define:

E = {rho, c, eta, sigma : Stability = 1, D_eff > D_min, C_y > C_min}

The physical research target should be a measurable region in this parameter space rather than a single best operating point.

For a real device, extend it to:

E_physical = E intersect {E_op < E_max, tau_state > tau_min, P_error < P_max, T_reset < T_max}

This creates a direct bridge from the mathematical model to experimental engineering.

## Relation to external evidence

Recent work demonstrates several individual mechanisms relevant to this direction:

- compact photonic multistability has produced three-state optical memory using nonlinear resonances; citeturn0search0
- fully in-memory photonic computing has demonstrated integrated optical/electronic memory and computation; citeturn0search2
- nonlinear magnon systems have experimentally shown hysteretic mode hopping and multistable dynamics. citeturn0search3

These results strengthen component-mechanism plausibility. They do not prove the Horizon causal WCR architecture.

## Research classification

- **Established physics:** nonlinear wave/material dynamics, interference, damping, multistability and state-dependent physical response exist.
- **Mathematical deduction:** the defined model possesses bounded operating regions with distinguishable state-dependent responses under the tested parameter grid.
- **Simulation result:** v0.5 numerical sweep.
- **Hypothesis:** a physical WCR can be engineered so its measurable parameters occupy a useful computational envelope.
- **Not demonstrated:** a fabricated WCR implementing this exact state-update law.
- **Not demonstrated:** smartphone-scale implementation.
- **Not demonstrated:** supercomputer-scale implementation.
- **Not demonstrated:** energy advantage over advanced electronic computing.

## Next falsification step

Do not increase model complexity yet.

1. choose one physical candidate platform;
2. map rho to measured damping/Q or retention;
3. map coupling to a measurable transfer coefficient;
4. map nonlinear strength to measured nonlinear response;
5. measure state/readout noise;
6. reproduce the A/B same-input causal test;
7. determine the experimentally observed E_physical.

A candidate fails if no stable region satisfies distinguishability, state dependence, retention, repeatability, acceptable energy, and noise constraints.

## Reproducibility

Simulation source:

04_RESEARCH/independent_wcr_operating_envelope_sweep_v0_5.py

Generated result table:

04_RESEARCH/wcr_operating_envelope_v0_5_results.csv

This is a numerical research artifact, not a physical validation instrument.
