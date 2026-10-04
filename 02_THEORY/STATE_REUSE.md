# COMPUTATIONAL STATE AND STATE REUSE

STWF tidak dibatasi sebagai one-shot calculator. State fisik yang masih relevan dapat dibawa ke perhitungan berikutnya.

## Running computation

S_t = S_(t-1) + X_t

Jika S2 = X1 + X2 masih tersedia, input X3 cukup melakukan update daripada menghitung ulang histori.

## State sebagai ringkasan histori

S3 = F(F(F(S0,X1),X2),X3)

State bukan histori lengkap; ia adalah informasi yang dipertahankan karena relevan.

Tidak semua histori dapat dikompresi menjadi state kecil tanpa kehilangan informasi.

## State classes

Transient State: cepat dan berumur pendek.
Working State: bertahan melewati banyak event.
Persistent State: konfigurasi/data jangka panjang.

S = (S_T, S_W, S_P)

## Lifecycle

retain
update
decay
reset
forget

S(t+Delta t) = lambda S(t) + F(X_t), 0 <= lambda <= 1.

## Selective forgetting

S_next = R(S_t, X_t)

R mempertahankan state yang relevan.

## Local state

S_i + X_i -> S_i'

Tujuannya mengurangi perpindahan state ke unit pusat.

## Scaling

Fully connected network cenderung N_connections ~ N². Karena itu locality dan hierarchy lebih masuk akal.

## State Reuse Ratio

SRR = reusable computation / total computation

SRR harus diukur.

## Stateful Core

Target minimum:

S_(t+1) = F(S_t, X_t)

Untuk STWF yang lebih lengkap:

Psi_(t+1) = G(Psi_t, X_t, S_t)

S_(t+1) = F(S_t, Psi_(t+1))

Y_t = R(Psi_t, S_t)

State dan wave field diperlakukan sebagai dua lapisan fisik yang saling berinteraksi.

## Material independence

Stateful Core tidak secara fundamental mengharuskan silikon.

Material dipilih setelah operator dan kebutuhan fisiknya ditentukan:

Computation -> State dynamics -> Physical mechanism -> Material -> Hardware

Kandidat awal untuk investigasi:
- magnonic/spin-wave systems: wave layer
- photonic systems: wave/interference layer
- memristive/resistive-switching materials: state layer
- ferroelectric systems: state + nonlinear interaction
- phase-change and magnetic state systems: persistent/state functions

Tidak ada kandidat yang ditetapkan sebagai material final.

## State contamination as computation

Model fisik dapat menyimpang dari accumulator ideal:

S_(t+1) = lambda S_t + w X_t + epsilon_t

Dengan lambda terkontrol, dinamika ini dapat menjadi temporal filter:

S_t = sum_k lambda^k X_(t-k)

Dengan demikian lifetime/decay state dapat menjadi parameter komputasi.

## Target

Bangun STWF Stateful Core dengan physical state, input, update, reuse, selective reset, readout, dan kandidat physical mechanisms.

Workload awal:
- running sum
- temporal filter
- recurrent matrix computation

Lihat juga: 02_THEORY/MATERIAL_TO_OPERATOR_MAPPING.md.
