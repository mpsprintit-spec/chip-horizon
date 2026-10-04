# SPACE-TIME WAVE FIELD (STWF)

## Gagasan inti

STWF menggunakan ruang dan waktu sebagai bagian dari representasi komputasi.

State:
Psi(x,y,z,t)

Informasi dapat dikodekan melalui posisi, waktu, amplitude, dan phase.

## Computation as evolution

Psi(x,y,z,0) -> Psi(x,y,z,t1) -> ... -> Y

Perhitungan terjadi selama medan berevolusi.

## Temporal coincidence

X1 -> t0
X2 -> t1
X3 -> t2
X4 -> t3

Delay fisik membuat input bertemu pada event tertentu.

## Collision-based computation

Interaksi/collision gelombang dapat menjadi event komputasi. Collision tidak otomatis menghasilkan fungsi berguna; medium, boundary, phase, amplitude, timing, dan readout harus direkayasa.

## Resonant state

E(t) = E0 exp(-t/tau)

Delay memory:
X(t) -> MEMORY -> X(t-tau)

## Event-driven

t_(n+1) = t_n + Delta t_n

Asynchronous tidak otomatis lebih hemat energi; event generation, detection, routing, dan control tetap memiliki biaya.

## Computational trajectory

Y = F_T(X)

Konfigurasi:
C = {w_ij, theta_ij, tau_ij, F_j}

Software tetap diperlukan untuk konfigurasi dan pembacaan physical field.

## Arsitektur

INPUT
  ↓
SPACE-TIME ENCODER
  ↓
SPACE-TIME WAVE FIELD
  ↓
NONLINEAR / STATE
  ↓
READOUT
  ↓
OUTPUT

Feedback: STATE → WAVE FIELD.
