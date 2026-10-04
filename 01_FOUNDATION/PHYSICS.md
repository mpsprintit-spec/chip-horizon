# FOUNDATION — PHYSICS

## Gelombang

Psi(x,t) = A(x,t) exp(i phi(x,t))

A adalah amplitude dan phi adalah phase.

## Superposisi

E_total = sum(E_i)

I = |E1|² + |E2|² + 2 Re(E1 E2*)

Interferensi memberi mekanisme fisik untuk kombinasi kontribusi.

## Phase dan negative weight

-X = A exp(i pi)

Detector intensitas biasa tidak langsung mempertahankan phase. Implementasi membutuhkan coherent detection, phase-sensitive detection, atau dual-rail:
X = X_plus - X_minus

## Propagation dan delay

E_i(z,t) = E_i(0,t-tau_i) exp(-alpha_i z) exp(i beta_i z)

## Nonlinearitas

Linear interference tidak cukup untuk semua komputasi. Sistem membutuhkan threshold, compare, branch, switch, retain state, dan reset.

s = 0 jika A < T
s = 1 jika A >= T

S_(t+1) = F(S_t, E_t)

## Landauer

E_min = k_B T ln(2)

Pada sekitar 300 K sekitar 2.87e-21 J/bit untuk batas termodinamika operasi penghapusan bit tertentu.

Ini bukan konsumsi realistis transistor.

STWF berusaha mengurangi irreversible erasure; bukan komputer tanpa energi.

## Switching

Model awal:
E ~ C V²

## Communication

latency >= L/v

Locality dapat menjadi faktor penting dalam scaling.

KESIMPULAN: fisika menyediakan primitives untuk physical computation, tetapi tidak menjamin arsitektur tertentu unggul.
