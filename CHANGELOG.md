# CHANGELOG

## 2026-10-05

- STWF Stateful Core Simulator v0.2 ditambahkan.
- Model diperluas dari scalar state menjadi vector recurrence: S_(t+1)=f(A S_t+B X_t).
- Parameter physical-analogue ditetapkan: coupling, input coupling, retention/decay, noise, nonlinearity, readout, delay, saturation.
- Hubungan retention dan lifetime dicatat: lambda=exp(-Delta_t/tau), sehingga tau=-Delta_t/ln(lambda).
- Test suite konseptual ditetapkan: accumulator, retention sweep, noise, vector stability, nonlinear state, dan delay.
- Implementasi referensi dependency-free Python ditambahkan agar dapat dijalankan di Termux tanpa library eksternal.
- Status tetap dipisahkan: mathematical model/deduction dan proposed synthesis; belum ada hasil hardware experiment.

## 2026-10-04

- Repository chip-horizon dibuat.
- Hardware, software, dan documentation licence notices ditambahkan.
- Pembahasan STWF sebelumnya dikonsolidasikan menjadi research documentation.
- Dasar fisika: superposition, interference, phase, propagation, delay, nonlinear state, Landauer limit, switching energy, communication latency.
- Teori STWF: space-time field, temporal coincidence, collision concept, resonant state, event-driven operation, computational trajectory.
- Stateful Core dan state reuse dicatat.
- Wave Computational Cell dan prototype 4x4 dicatat.
- Mathematical model, noise model, energy model, dan test plan dicatat.
- Rejected assumptions dan open problems dicatat.
- Next research target ditetapkan: STWF Stateful Core.
- Material-to-operator mapping ditambahkan: kandidat magnonik, fotonik, memristive/oxide, ferroelectric, phase-change, dan magnetic state dipetakan berdasarkan fungsi wave/state/nonlinearity.
- Prinsip material-independent ditegaskan: operator dan dinamika state ditentukan sebelum pemilihan material.
- Masalah representasi signed state, state contamination, decay sebagai fungsi temporal, dan kill test end-to-end dicatat.
