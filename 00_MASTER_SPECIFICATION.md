# CHIP HORIZON — MASTER SPECIFICATION

STWF (Space-Time Wave Field) adalah arsitektur komputasi yang menjadikan evolusi medan gelombang dalam ruang-waktu sebagai bagian dari proses komputasi.

Ini adalah konsep penelitian, bukan klaim chip yang telah dibuat atau terbukti unggul.

## Target sistem

Target utama Horizon adalah **supercomputer yang skalabel hingga implementasi chip kelas smartphone**.

Keduanya harus merupakan ekspresi skala dari mekanisme komputasi yang sama, bukan dua arsitektur berbeda.

Skala konseptual:

WAVE COMPUTATIONAL REGION → CORE → TILE/CLUSTER → CHIP → MULTI-CHIP SYSTEM → HORIZON SUPERCOMPUTER

Istilah **Wave Computational Region (WCR)** digunakan untuk wilayah fisik tempat medan gelombang berevolusi dan berinteraksi. Istilah WCC pada dokumen sebelumnya dipertahankan untuk unit matematis/konseptual historis dan bukan komitmen terhadap cell transistor-like.

## Masalah

Komputer konvensional memisahkan compute, memory, control, dan communication. Biaya dapat muncul dari perpindahan data, switching, synchronization, memory access, conversion, control, dan correction.

STWF mengeksplorasi apakah sebagian pekerjaan tersebut dapat dilakukan langsung oleh fisika medium.

## Hipotesis

H1 physical parallelism: banyak kontribusi dapat berevolusi simultan sebagai satu medan.

H2 propagation as computation: delay, coupling, phase, interference, dan geometry dapat membawa fungsi komputasi.

H3 state reuse: state yang masih relevan dapat dipakai kembali tanpa menghitung ulang seluruh histori.

H4 locality: komputasi lokal dapat mengurangi komunikasi jarak jauh.

H5 reduced irreversible work: arsitektur dapat dirancang untuk mengurangi operasi irreversible.

H6 scalable substrate: mekanisme komputasi yang sama dapat direalisasikan pada skala mobile-chip dan diperluas secara hierarkis menuju supercomputer.

Semua H1-H6 adalah hipotesis engineering.

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

Dengan feedback:

WAVE FIELD → STATE → WAVE FIELD.

Wave field adalah medium komputasi. State adalah bagian dari dinamika komputasi; keduanya tidak diperlakukan sebagai pengganti satu sama lain.

## Skalabilitas

Arsitektur diprioritaskan pada locality dan hierarchy:

WCR → core → tile → cluster → chip → multi-chip system.

Full all-to-all connectivity bukan default karena N_connections ~ N².

Implementasi smartphone merupakan instance berukuran kecil dari mekanisme yang sama. Implementasi supercomputer memperbesar jumlah region, kapasitas state, parallelism, dan hierarchical interconnect.

## Energi

E_total =
E_source + E_modulator + E_propagation + E_nonlinear +
E_memory + E_detector + E_control + E_correction

Tidak boleh menyatakan STWF hemat energi hanya karena propagasi dapat pasif.

## Metrik

accuracy, latency, energy/op, total energy, area, throughput, noise tolerance, state reuse ratio, communication overhead, correction overhead, scalability.

eta_ST = useful computation / (E × T)

## Batasan

STWF tidak otomatis universal, lossless, reversible, asynchronous-efficient, lebih cepat, atau lebih hemat energi.

## Validation principle

Target desain ditentukan terlebih dahulu. Pengujian diturunkan dari kebutuhan target dan dilakukan bertahap dari fenomena fisik yang diperlukan menuju sistem yang lebih besar.

Pengujian sederhana tidak boleh mengubah definisi target supercomputer.

Pengujian fisik menggunakan metode, instrumen, dan fasilitas eksternal yang sudah tersedia bila memungkinkan.

STATUS: RESEARCH / UNVALIDATED.
