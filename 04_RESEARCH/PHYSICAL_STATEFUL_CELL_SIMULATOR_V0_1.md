# Physical Stateful Cell Simulator V0.1

**Status:** Research tool / mathematical simulator  
**Date:** 2026-10-05  
**Scope:** Platform-neutral computational model for the first physical stateful-cell experiment.

## 1. Purpose

This simulator is the numerical bridge between the platform-neutral Physical Stateful Cell Model and a future physical demonstrator.

It does not simulate a particular material, fabrication process, electromagnetic geometry, or laboratory instrument. It makes the following physical effects explicit:

- state retention and decay;
- wave/state coupling;
- propagation delay;
- wave loss;
- nonlinear state response;
- stochastic noise;
- read disturbance;
- reset;
- update energy.

The simulator therefore asks:

> Can a stateful computational cell preserve, modify, read, and reset a physical state while remaining computationally useful under finite lifetime, delay, loss, noise, and energy constraints?

A passing numerical result is not evidence that a physical device works.

## 2. Model

### 2.1 State decay

For state vector S:

$$
S^-_n = D_\lambda S_n
$$

with

$$
D_\lambda=diag(\lambda_1,\lambda_2,...)
$$

and

$$
\lambda_i=e^{-\Delta t/\tau_i}.
$$

This separates passive retention from active state coupling.

### 2.2 Coupling and update

The physical coupling matrix is C:

$$
S_{n+1}=f(CS^-_n + BX_n + K_W W_n + \epsilon_n).
$$

Where:

- C = local state-to-state physical coupling;
- B = input-to-state coupling;
- K_W = wave-to-state coupling;
- X_n = external input;
- W_n = wave/state carrier;
- epsilon_n = state-update noise;
- f = optional nonlinear state response.

For the scalar minimum model:

$$
S_{n+1}=f(\lambda S_n+wX_n+k_WW_n+\epsilon_n).
$$

This formulation avoids the ambiguity of applying a retention coefficient twice to a full transition matrix.

### 2.3 Wave carrier

V0.1 uses a real-valued wave abstraction rather than a full complex electromagnetic field:

$$
W_{n+1}=a_WW_n+b_XX_n+b_SS_n+\eta_n.
$$

A delayed feedback term can be added:

$$
W_{n+1}=a_WW_n+b_XX_n+b_SS_n+rW_{n-d}+\eta_n.
$$

This is a reduced dynamical model. It is not an EM, photonic, acoustic, or magnonic field solver.

### 2.4 Loss

For propagation length L:

$$
W(L)=W_0e^{-\alpha L}.
$$

The simulator represents this through a dimensionless per-step transmission factor:

$$
T_W=e^{-\alpha L}.
$$

### 2.5 Nonlinearity

Default:

$$
f(z)=sat(z,S_{max})
$$

where

$$
sat(z,S_{max})=\max(-S_{max},\min(z,S_{max})).
$$

Optional smooth nonlinearity:

$$
f(z)=S_{max}\tanh(z/S_{max}).
$$

Nonlinearity is treated as an engineering parameter, not automatically as an advantage.

## 3. Readout

The readout is:

$$
Y_n=G_SS_n+G_WW_n+\nu_n.
$$

The simulator also calculates a read-disturbance experiment by comparing a state trajectory with and without readout coupling.

A useful dimensionless metric is:

$$
R_{read}=\frac{D_{read}}{\Delta S_{min}}
$$

where D_read is the state change caused by measurement and Delta S_min is the minimum distinguishable state change.

## 4. Reset

Reset is modeled as:

$$
S\rightarrow S_{reset}.
$$

The simulator records reset time, residual state, reset energy, and repeatability.

Reset is not assumed to be free.

## 5. Energy accounting

V0.1 keeps energy explicit:

$$
E_{update}=
E_{drive}+E_{couple}+E_{state}+E_{read}+E_{control}+E_{reset}.
$$

The values are supplied by the user/model configuration. The simulator must not invent a material's energy efficiency.

When only normalized energy is available, results are reported as normalized units.

## 6. Dimensionless screening metrics

Retention:

$$
R_{delay}=\frac{\tau_d}{\tau}.
$$

Noise:

$$
R_{noise}=\frac{\sigma_{noise}}{\Delta S_{min}}.
$$

Read disturbance:

$$
R_{read}=\frac{D_{read}}{\Delta S_{min}}.
$$

Loss compensation:

$$
R_{loss}=\frac{E_{compensation}}{E_{update}}.
$$

Reset burden:

$$
R_{reset}=\frac{E_{reset}}{E_{update}}.
$$

These are screening metrics, not universal physical laws.

## 7. Required simulation experiments

### E1 — Free decay

Initialize the state and remove the input.

Expected model:

$$
S(t)=S_0e^{-t/\tau}+n(t).
$$

Estimate effective lifetime.

### E2 — Single update

Apply one input pulse and measure:

$$
\Delta S=S_{after}-S_{before}.
$$

Determine input-to-state coupling.

### E3 — Repeated update

For input sequence [3, 5, 2, 7], the ideal accumulator is [3, 8, 10, 17].

Compare the physical abstraction against the target.

### E4 — Retention sweep

Sweep tau or lambda and measure the trade-off between memory and state error.

### E5 — Delay sweep

Sweep feedback delay and measure delay/lifetime ratio, stability, state error, and feedback-induced oscillation.

### E6 — Noise sweep

Sweep noise and measure RMS state error, maximum error, SNR, and state distinguishability.

### E7 — Read disturbance

Run identical trajectories with ideal/non-invasive read and finite read coupling. Calculate:

$$
D_{read}=|S_{with}-S_{without}|.
$$

### E8 — Reset

Drive the state to a non-zero value, issue reset, then measure residual, reset time, reset energy, and repeatability.

### E9 — Nonlinearity sweep

Compare linear, saturation, and tanh response. The objective is not to maximize nonlinearity. The objective is to find whether the required computational regime remains stable and distinguishable.

## 8. Minimum output

Every simulation run should report:

- state trajectory;
- wave trajectory;
- output trajectory;
- effective retention tau;
- delay/lifetime ratio;
- RMS error;
- maximum error;
- state range;
- noise ratio;
- read disturbance;
- reset residual;
- update energy;
- reset energy;
- stability indicator;
- parameter set;
- random seed.

## 9. Initial engineering screening thresholds

These are initial screening values only, not physical requirements:

| Metric | Initial screen |
|---|---:|
| Relative update error | < 5% |
| State SNR | > 10 |
| Read disturbance / minimum step | < 0.1 |
| Delay / lifetime | < 0.1 |
| Reset residual / state range | < 1% |
| Repeatability | > 95% |

A device failing these values is not automatically impossible. It means the current parameter region is a poor candidate and requires redesign or a revised measurement target.

## 10. Falsification conditions

The physical-stateful-cell hypothesis becomes unattractive if realistic parameter ranges consistently show one or more of:

1. state lifetime too short for the required computation;
2. update error dominated by noise or variability;
3. readout substantially disturbs state;
4. delay consumes the available state lifetime;
5. loss requires excessive compensation;
6. nonlinear operation consumes more energy than the computation saves;
7. reset is too expensive or unreliable;
8. usable state range collapses under temperature/process variation;
9. physical coupling cannot realize the required transition matrix;
10. electronic baseline remains superior after all conversion and control overhead is included.

## 11. Classification of evidence

**Established physics/engineering:** exponential decay models, propagation loss, noise, nonlinear device behavior, energy accounting, and state/read/reset measurements are legitimate physical concepts.

**Mathematical deduction:** the dimensionless ratios and state-transition decomposition follow from the model definitions.

**Proposed synthesis:** the particular Horizon cell abstraction that combines wave carrier, persistent state, local coupling, delayed feedback, and explicit reset/read accounting.

**Hypothesis:** that this synthesis can provide a useful computational primitive with an energy/latency advantage.

**Simulation result:** only numerical behavior produced by this simulator.

**Experimental result:** none at this stage.

## 12. Next bridge

The next step after V0.1 is not a larger chip.

It is to choose one physically realizable cell platform and map:

$$
\{\tau,\alpha,K_W,B,C,f,E_{update},\sigma_{noise},D_{read}\}
$$

to measurable device parameters.

Candidate platforms remain open:

- photonic/optical;
- magnonic/spin-wave;
- acoustic/phononic;
- RF/EM;
- memristive;
- ferroelectric;
- phase-change;
- magnetic/spintronic;
- hybrid combinations.

Recent literature already demonstrates physical systems with memory, nonlinearity, and wave dynamics, so Horizon should not claim those mechanisms as novel by themselves. The research question remains whether the specific stateful computational-cell formulation can be realized with favorable measured trade-offs.

## 13. Reproducibility

The Python implementation in 04_RESEARCH/physical_stateful_cell_simulator_v0_1.py must be deterministic for a fixed random seed.

No simulation output should be described as experimental evidence.
