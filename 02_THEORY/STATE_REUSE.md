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

## Target

Bangun STWF Stateful Core dengan physical state, input, update, reuse, selective reset, dan readout.

Workload awal:
- running sum
- temporal filter
- recurrent matrix computation
