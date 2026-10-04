# CHIP HORIZON — MASTER SPECIFICATION

STWF (Space-Time Wave Field) adalah arsitektur komputasi yang menjadikan evolusi medan gelombang dalam ruang-waktu sebagai bagian dari proses komputasi.

Ini adalah konsep penelitian, bukan klaim chip yang telah dibuat atau terbukti unggul.

## Masalah

Komputer konvensional memisahkan compute, memory, control, dan communication. Biaya dapat muncul dari perpindahan data, switching, synchronization, memory access, conversion, control, dan correction.

STWF mengeksplorasi apakah sebagian pekerjaan tersebut dapat dilakukan langsung oleh fisika medium.

## Hipotesis

H1 physical parallelism: banyak kontribusi dapat berevolusi simultan sebagai satu medan.

H2 propagation as computation: delay, coupling, phase, interference, dan geometry dapat membawa fungsi komputasi.

H3 state reuse: state yang masih relevan dapat dipakai kembali tanpa menghitung ulang seluruh histori.

H4 locality: komputasi lokal dapat mengurangi komunikasi jarak jauh.

H5 reduced irreversible work: arsitektur dapat dirancang untuk mengurangi operasi irreversible.

Semua H1-H5 adalah hipotesis engineering.

## Model

Konvensional: Y = F(X)

STWF:
Y_t = G(X_t, S_t)
S_(t+1) = F(S_t, X_t)

Global:
Psi_(t+1) = F(Psi_t, X_t, C_t)
Y_t = G(Psi_t)

## State hierarchy

S = (S_T, S_W, S_P)

S_T = transient state.
S_W = working state.
S_P = persistent state.

Target: memory ikut menjadi bagian dari mekanisme komputasi.

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

Dengan feedback: WAVE FIELD → STATE → WAVE FIELD.

## Energi

E_total =
E_source + E_modulator + E_propagation + E_nonlinear +
E_memory + E_detector + E_control + E_correction

Tidak boleh menyatakan STWF hemat energi hanya karena propagasi dapat pasif.

## Metrik

accuracy, latency, energy/op, total energy, area, throughput, noise tolerance, state reuse ratio, communication overhead, correction overhead.

eta_ST = useful computation / (E × T)

## Batasan

STWF tidak otomatis universal, lossless, reversible, asynchronous-efficient, lebih cepat, atau lebih hemat energi.

STATUS: RESEARCH / UNVALIDATED.
