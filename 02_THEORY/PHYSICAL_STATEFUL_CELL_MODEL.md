# PHYSICAL STATEFUL CELL MODEL V0.1

## Status

**Platform-neutral physical abstraction — 2026-10-05**

This model defines the minimum physical variables required to map the mathematical Stateful Core to a real device without selecting a material or fabrication platform prematurely.

The model is intentionally platform-neutral. A state may be optical, electrical, magnetic, mechanical, acoustic, ferroelectric, ionic, or hybrid.

## 1. Core abstraction

The cell has four essential elements:

\[
X_n \rightarrow C \rightarrow S_{n+1}
\]

with readout:

\[
S_n \rightarrow Y_n
\]

and, where required, feedback:

\[
S_n \rightarrow W_n \rightarrow C \rightarrow S_{n+1}
\]

where:

- \(X_n\) = encoded input;
- \(W_n\) = propagating or oscillatory wave/field variable;
- \(S_n\) = computational state;
- \(C\) = physical coupling/update mechanism;
- \(Y_n\) = measured output.

The wave variable and state variable are deliberately separated. A resonant field can carry state temporarily, while a material state can provide longer retention. They are not assumed to be the same physical quantity.

## 2. Continuous-time model

A general state equation is:

\[
\frac{dS}{dt}=F(S,W,X,P)+\xi(t)
\]

where:

- \(P\) = physical parameters;
- \(F\) = state-update dynamics;
- \(\xi(t)\) = stochastic disturbance and unmodeled variation.

The wave/field dynamics can be represented generically as:

\[
\frac{dW}{dt}=G(W,S,X,P)+\eta(t)
\]

The measured output is:

\[
Y=H(S,W,X,P)+\nu(t)
\]

This is the first physical bridge from the discrete simulator to a device.

## 3. Discrete computational step

If the system is sampled at interval \(\Delta t\):

\[
S_{n+1}=\Phi_{\Delta t}(S_n,X_n,P)+\epsilon_n
\]

For a locally linear operating region:

\[
S_{n+1}\approx A_{phys}S_n+B_{phys}X_n+\epsilon_n
\]

This gives a direct comparison with the existing Stateful Vector Core:

\[
S_{n+1}=f(AS_n+BX_n+\epsilon_n)
\]

The important distinction is that \(A\) and \(B\) are now measured or physically derived parameters, not arbitrary simulator values.

## 4. State representations

The state vector may contain one or more physical observables:

\[
S=[s_1,s_2,...,s_m]
\]

Possible examples:

| Physical quantity | Possible state meaning |
|---|---|
| optical amplitude | stored computational magnitude |
| optical phase | signed/relative state |
| resonance frequency | state-dependent parameter |
| electrical charge | integrated state |
| conductance | persistent/analog state |
| polarization | discrete or multilevel state |
| magnetization | persistent physical state |
| displacement | mechanical state |
| acoustic amplitude/phase | dynamic state |
| ionic concentration | slow state / memory |

These are candidate representations, not selections.

## 5. Retention

For a simple first-order decay:

\[
\frac{dS}{dt}=-\frac{S}{\tau}
\]

therefore:

\[
S(t)=S_0e^{-t/\tau}
\]

For a discrete interval:

\[
\lambda=e^{-\Delta t/\tau}
\]

and:

\[
S_{n+1}=\lambda S_n
\]

This relationship allows the simulator's retention parameter to be replaced by a measurable physical lifetime.

If \(\lambda\rightarrow1\), retention increases. If \(\lambda\rightarrow0\), state rapidly disappears.

A large \(\tau\) is not automatically better: long retention can conflict with reset speed, controllability, bandwidth, or energy.

## 6. State update

The first target is:

\[
S_{n+1}=\lambda S_n+wX_n+\epsilon_n
\]

where:

- \(\lambda\) = physical retention;
- \(w\) = input-to-state coupling;
- \(X_n\) = input;
- \(\epsilon_n\) = update error.

The experiment must determine whether \(w\) is stable over repeated updates.

A nonlinear extension is:

\[
S_{n+1}=f(\lambda S_n+wX_n)
\]

where \(f\) may represent saturation, thresholding, bistability, hysteresis, gain compression, or another physical nonlinearity.

## 7. Wave-state coupling

The coupling coefficient must be treated as a physical quantity:

\[
W_{interaction}=K(W,S,X)
\]

A linearized form may be:

\[
\Delta S\approx k_xX+k_wW+k_sS
\]

The actual implementation may use:

- evanescent coupling;
- field overlap;
- electrical injection;
- magneto-electric coupling;
- strain coupling;
- thermo-optic coupling;
- electro-optic coupling;
- ion migration;
- mechanical force.

No coupling mechanism is selected at this stage.

## 8. Delay

Every physical path has delay:

\[
t_{arrival}=t_{launch}+\tau_d
\]

The delay must be separated from state lifetime.

A system can have:

- short propagation delay + long state lifetime;
- long propagation delay + short state lifetime;
- comparable delay and lifetime.

The ratio:

\[
R_{delay}=\frac{\tau_d}{\tau}
\]

is therefore a useful dimensionless design parameter.

If \(R_{delay}\) becomes large, feedback may arrive after significant state decay.

## 9. Loss

Wave or field amplitude may decay approximately as:

\[
W(L)=W_0e^{-\alpha L}
\]

and power/intensity as:

\[
P(L)=P_0e^{-2\alpha L}
\]

depending on the definition of \(\alpha\).

The model must record both the propagation loss and any energy required to compensate it.

Loss compensation cannot be omitted from the energy budget.

## 10. Noise and variability

Separate at least three error sources:

\[
\epsilon=\epsilon_{dynamic}+\epsilon_{material}+\epsilon_{read}
\]

where:

- dynamic noise affects state evolution;
- material/process variation changes device parameters;
- readout noise corrupts observation.

The measured state should therefore be modeled as:

\[
Y=H(S)+\nu
\]

A state is computationally useful only if neighboring valid states remain distinguishable under the complete noise budget.

## 11. Read disturbance

Readout is not assumed to be passive.

Define:

\[
D_{read}=|S_{with\ read}-S_{without\ read}|
\]

A low-disturbance read requires:

\[
D_{read}\ll\Delta S_{computational}
\]

If this condition fails, the detector becomes part of the computational dynamics and must be included in \(F\).

## 12. Reset and forgetting

Reset is an explicit operation:

\[
S\rightarrow S_{reset}
\]

Measure:

- reset time;
- reset energy;
- residual state;
- repeatability;
- recovery time.

Selective forgetting may instead use controlled decay:

\[
S_{n+1}=\lambda_rS_n
\]

where \(\lambda_r\) is deliberately different from normal operating retention.

This makes state lifecycle a physical parameter rather than a software-only concept.

## 13. Energy model

For one update:

\[
E_{update}=E_{source}+E_{encode}+E_{couple}+E_{state}+E_{nonlinear}+E_{read}+E_{control}
\]

For a complete system:

\[
E_{total}=E_{update}+E_{conversion}+E_{correction}+E_{idle}
\]

No efficiency claim should be made from the active cell alone.

A cell with extremely low intrinsic switching energy can still be system-level inefficient if source, detector, conversion, control, or correction dominate.

## 14. Dimensionless operating parameters

The first physical model should expose ratios rather than only absolute numbers:

\[
R_{delay}=\frac{\tau_d}{\tau}
\]

\[
R_{noise}=\frac{\sigma_{noise}}{\Delta S_{min}}
\]

\[
R_{read}=\frac{D_{read}}{\Delta S_{min}}
\]

\[
R_{loss}=\frac{E_{compensation}}{E_{update}}
\]

\[
R_{reset}=\frac{E_{reset}}{E_{update}}
\]

where \(\Delta S_{min}\) is the minimum state separation required by the computation.

These ratios make candidate physical platforms easier to compare without prematurely optimizing for a single absolute number.

## 15. Minimum parameter set

A candidate physical cell cannot enter the next design stage without estimates or measurements for:

1. state range;
2. minimum distinguishable state step;
3. state lifetime \(\tau\);
4. input coupling \(w\);
5. update nonlinearity \(f\);
6. propagation delay \(\tau_d\);
7. propagation/coupling loss;
8. state noise;
9. read disturbance;
10. reset time;
11. reset energy;
12. update energy;
13. operating temperature range;
14. cycle-to-cycle variability;
15. endurance.

Unknown values remain explicitly **unknown** rather than being filled with optimistic assumptions.

## 16. Candidate-platform screening

The model can now compare candidate media without selecting one.

A platform is promising only if it simultaneously provides:

\[
\text{retention} + \text{controllability} + \text{coupling} + \text{readability} + \text{nonlinearity}
\]

while keeping:

\[
\text{loss} + \text{noise} + \text{energy} + \text{reset cost}
\]

within acceptable bounds.

Recent work demonstrates that several physical platforms can provide parts of this combination: coupled silicon microrings have demonstrated non-fading memory and nonlinear dynamics; ferroelectric/LN devices have demonstrated multistate photonic memory; and piezoelectric resonators have demonstrated nonlinear temporal processing. These results establish candidate mechanisms, not evidence that any one is optimal for Horizon. citeturn0search1turn0search0turn0search3

## 17. Classification

**Established physics / engineering:** physical systems have measurable propagation, loss, delay, state relaxation, noise, coupling, and readout behavior.

**Mathematical deduction:** \(\lambda=e^{-\Delta t/\tau}\) connects a first-order discrete retention factor to an exponential physical lifetime.

**Proposed synthesis:** represent the Stateful Core using separate wave, state, coupling, nonlinear, readout, reset, and energy layers.

**Hypothesis:** a properly coupled physical state can function as a reusable computational operand across successive updates.

**Not demonstrated:** any complete Horizon physical cell, energy advantage, speed advantage, or scalable fabrication.

## 18. Next step

Implement this model as **Physical Stateful Cell Simulator V0.1**.

The simulator should accept physical parameters rather than abstract labels and produce:

- state trajectory;
- wave trajectory;
- delayed feedback;
- loss;
- noise;
- read disturbance;
- reset;
- update energy;
- dimensionless operating ratios;
- pass/fail result against the minimum experiment.

Only after this simulator is internally consistent should we select the first candidate physical platform.
