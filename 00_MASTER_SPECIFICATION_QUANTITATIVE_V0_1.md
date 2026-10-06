# HORIZON QUANTITATIVE ARCHITECTURE SPECIFICATION V0.1

## Status

Research specification. This document converts the Horizon target architecture into measurable engineering variables and scaling relationships.

It does not assign fabricated-device performance numbers without physical evidence.

## 1. Purpose

The target remains one architecture:

WCR -> Core -> Tile -> Cluster -> Chip -> Multi-chip system -> Horizon supercomputer

The purpose of this specification is to define what must eventually be quantified at every scale.

## 2. WCR state variables

For WCR r:

Psi_r(t) = wave state

S_r(t) = physical computational state

X_r(t) = incoming information

Y_r(t) = observable output

C_r = configuration parameters

The target dynamics are:

Psi_r(t+1) = H_r(Psi_r(t), S_r(t), X_r(t), C_r)

S_r(t+1) = F_r(S_r(t), Psi_r(t), X_r(t))

Y_r(t) = G_r(Psi_r(t), S_r(t))

The physical forms of H, F, and G remain unresolved.

## 3. Local interconnect

A WCR should primarily communicate with a bounded neighborhood N(r):

X_r(t) = X_local,r(t) + sum[K_rq Y_q(t - tau_rq)]

where q belongs to N(r).

Required measurements:

- neighborhood size;
- coupling strength;
- propagation delay;
- bandwidth;
- loss;
- crosstalk;
- synchronization/event uncertainty.

The architecture does not assume all-to-all WCR communication.

## 4. State capacity

State capacity must be measured physically, not inferred from an abstract variable count.

Required quantities:

- number of independently controllable state degrees of freedom;
- state precision;
- retention time;
- update time;
- reset time;
- write energy;
- read energy;
- endurance;
- variability;
- state-to-state interference.

For a decaying state:

S(t) = S0 exp(-t/tau)

where tau is the measured characteristic lifetime.

For discrete operation interval Delta_t:

lambda = exp(-Delta_t/tau)

Thus:

tau = -Delta_t / ln(lambda)

## 5. Wave capacity

Required wave-layer quantities:

- usable bandwidth B;
- propagation velocity v;
- physical path length L;
- propagation delay tau_p = L/v;
- attenuation alpha;
- phase stability;
- amplitude stability;
- mode count where applicable;
- coupling efficiency;
- source/modulation efficiency.

For a propagating field:

E(L) = E0 exp(-alpha L)

and:

I(L) = I0 exp(-2 alpha L)

Loss compensation must be included in system energy.

## 6. Computational precision

Precision must be defined from the physical observable used for computation.

For an observable z:

relative error = |z_measured - z_reference| / |z_reference|

Required error budget:

E_total_error = E_noise + E_variability + E_drift + E_coupling + E_readout + E_conversion

The exact combination rule must be established for the physical implementation.

The architecture does not assume arbitrary floating-point precision.

## 7. Latency

End-to-end latency is:

T_end = T_encode + T_compute + T_state + T_read + T_control + T_communication + T_correction

Propagation contributes approximately:

T_prop = L/v

No speed advantage is claimed until all terms are measured.

## 8. Energy

System energy per useful operation must include the complete path:

E_op = E_source + E_encode + E_wave + E_state + E_nonlinear + E_read + E_control + E_memory + E_communication + E_correction

The central comparison is not wave energy alone.

For a workload:

P_total = useful_operations_per_second * E_op

subject to thermal and power constraints.

## 9. Throughput

For N effectively parallel computational regions:

Throughput_total is bounded by:

N * throughput_WCR

but actual throughput must subtract communication, synchronization, correction, and I/O limitations.

A first-order system model is:

Throughput_effective = Throughput_raw * eta_comm * eta_control * eta_correction

where each efficiency term must be experimentally determined.

## 10. State reuse

State reuse is treated as an architectural variable rather than an assumption.

SRR = reusable computation / total computation

A useful experiment must report both:

- computation saved by retained state;
- physical cost of maintaining, updating, reading, and resetting that state.

State reuse is beneficial only if its total physical cost is lower than recomputation.

## 11. Communication scaling

For N computational regions, unrestricted all-to-all communication approaches O(N^2) links.

The target architecture instead uses bounded local degree d and hierarchy.

For approximately constant d:

N_links_local ~ dN

Higher-level links remain necessary, but hierarchy should prevent every WCR from directly communicating with every other WCR.

This is an architectural hypothesis to be validated against actual routing and workload requirements.

## 12. Scale mapping

### Smartphone-class chip

Primary constraints:

- area;
- thermal envelope;
- source and detector efficiency;
- limited state capacity;
- limited I/O;
- limited cooling;
- manufacturing compatibility.

The architecture is the same; only physical scale and resource count are reduced.

### Supercomputer

Primary scaling variables:

- WCR count;
- state capacity;
- tile count;
- hierarchy depth;
- aggregate bandwidth;
- inter-chip communication;
- total power;
- cooling;
- fault tolerance;
- correction overhead.

The architecture must remain decomposable.

## 13. Minimum quantitative specification before fabrication

Before a physical Horizon chip can be credibly specified, the following must have measured or bounded values:

1. WCR physical dimensions;
2. wave medium and usable bandwidth;
3. state medium and state capacity;
4. coupling range and strength;
5. nonlinear transfer function;
6. state retention/update/reset;
7. input encoding efficiency;
8. output readout efficiency;
9. propagation loss;
10. noise and variability;
11. energy per state update;
12. energy per read/write;
13. latency;
14. computational precision;
15. communication overhead;
16. correction overhead;
17. thermal load;
18. expected fabrication yield.

Until these are known, numerical chip-scale performance targets would be speculative.

## 14. Required comparison baselines

Any claimed advantage must be compared against appropriate measured baselines, potentially including:

- conventional electronic compute;
- electronic memory-centric compute;
- established photonic compute;
- other wave-based computing approaches where directly comparable.

The comparison must use equivalent workload, precision, I/O assumptions, and complete energy accounting.

## 15. Kill conditions

The architecture should be reconsidered if experiments show any of the following:

- nonlinear interaction is too weak or uncontrollable;
- physical state cannot be retained or updated reproducibly;
- feedback becomes unstable at useful operating points;
- read/write or conversion energy dominates computation;
- propagation loss requires excessive compensation;
- noise/variability prevents required precision;
- communication overhead destroys scaling;
- fabrication density is insufficient;
- state reuse costs more energy than recomputation;
- measured performance is consistently inferior to suitable baselines without a compensating system-level advantage.

## 16. Epistemic classification

### Established physics

Propagation, interference, attenuation, finite propagation delay, nonlinear material responses, and physical state retention are established physical phenomena in appropriate systems.

### Mathematical deductions

The equations in this document express measurable relationships and architectural abstractions. They do not prove that a specific material/device realizes them.

### Horizon engineering hypothesis

A WCR combining wave evolution, nonlinear interaction, physical state, and feedback may form a useful computational primitive that can be hierarchically scaled from smartphone-class chip to supercomputer.

### Unresolved

The physical implementation, numerical operating envelope, fabrication technology, and system-level advantage remain unvalidated.
