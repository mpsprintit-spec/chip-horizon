# STWF STATEFUL CORE

Tujuannya memperluas STWF dari matrix operator menjadi computational dynamical system.

Input X_t
State S_t
Output Y_t

S_(t+1) = F(S_t, X_t)
Y_t = G(S_t, X_t)

## Wave layer

E_j(t) =
sum_i [
w_ij A_i(t-tau_ij)
exp(-alpha_ij L_ij)
exp(i(phi_i(t-tau_ij)+theta_ij))
] + N_j(t)

## State layer

S_j(t+Delta t) = F_j(S_j(t), E_j(t))

Dapat digunakan untuk threshold, comparison, switching, gating, atau state transition.

## Feedback

E(t+Delta t) = F(E(t), S(t), X(t))
S(t+Delta t) = G(S(t), E(t))

Feedback mengubah sistem dari one-shot calculator menjadi dynamical computer.

## Readout

Y = G(Psi)

Detector, conversion, ADC/DAC, amplification, dan control harus dimasukkan ke energy budget.

## State contamination

State lama dapat merusak komputasi berikutnya. Diperlukan retention, decay, reset, isolation, dan selective overwrite.

## Local hierarchy

Core lokal membentuk region. Inter-region communication dibatasi pada informasi yang diperlukan.

Target:
sebanyak mungkin physical computation, sesedikit mungkin active state transition, dan komunikasi sejauh mungkin tetap lokal.
