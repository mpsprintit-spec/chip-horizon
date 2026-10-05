# CHANGELOG

## 2026-10-05

- STWF Visual Laboratory v0.3 ditingkatkan dari model wave/state menjadi model **resonance + state + feedback**.
- Jalur komputasi visual sekarang dimodelkan sebagai: INPUT → WAVE FIELD → INTERFERENCE → STATE → FEEDBACK → WAVE FIELD.
- Ditambahkan parameter visual **Feedback** dan **Resonance** untuk menguji secara matematis pengaruh umpan balik dan penyimpanan state/resonansi.
- Mode INTERFERENCE sekarang memiliki `fieldMemory` yang memengaruhi medan pada langkah berikutnya.
- Mode STATE sekarang memiliki field-level memory yang berinteraksi dengan lima state cells dan dikembalikan melalui feedback path.
- Ditambahkan visualisasi jalur feedback dan node FIELD STATE agar hubungan antara medan dan state dapat diamati langsung.
- Model nonlinear sederhana menggunakan saturasi/tanh dan threshold attenuation; ini adalah abstraksi matematis, bukan model material tertentu.
- Status tetap dipisahkan: visual/mathematical model dan proposed synthesis; belum ada hasil eksperimen hardware.
- Commit visual upgrade: `ed8ff661c9c712a18fb7f8cdd7a9800ef721a0d8`.

## 2026-10-04

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
