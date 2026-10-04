# STWF MATHEMATICAL MODEL

Psi(x,t) = A(x,t) exp(i phi(x,t))

E_i(t) = A_i(t) exp(i phi_i(t))

W_i = (w_i, phi_i, tau_i, alpha_i)

E_i(z,t) = E_i(0,t-tau_i) exp(-alpha_i z) exp(i beta_i z)

E_i'(t) =
w_i A_i(t-tau_i)
exp(-alpha_i L_i)
exp(i[phi_i(t-tau_i)+theta_i])

E_j(t) =
sum_i [
w_ij A_i(t-tau_ij)
exp(-alpha_ij L_ij)
exp(i[phi_i(t-tau_ij)+theta_ij])
]

Matrix shorthand:
E_out(t) = W(tau,phi,alpha) E_in(t)

Noise:
E_real = E_ideal + N
N = N_A + N_phi + N_t + N_d

Phase error:
phi -> phi + delta_phi
exp(i delta_phi) approximately 1 + i delta_phi

Timing jitter:
t = t0 + delta_t
E_i(t) -> E_i(t-tau_i-delta_t_i)

Loss:
E(L) = E0 exp(-alpha L)
I(L) = I0 exp(-2 alpha L)

Nonlinear state:
S_(t+1) = F(S_t,E_t)

Example:
S_(t+1) = H(|E_t|-T)

Global:
Psi_(t+1) = F(Psi_t,X_t,C_t)
Y_t = G(Psi_t)

Energy:
E_total =
E_source + E_encoding + E_field + E_control +
E_nonlinear + E_memory + E_detection + E_correction

Energy advantage tidak boleh disimpulkan hanya dari propagation.
