## 2026-10-05 — Physical Stateful Cell

- Physical Stateful Cell Model diperdalam menjadi simulator V0.1 yang memisahkan state decay, physical coupling, wave coupling, delay, loss, noise, read disturbance, reset, dan energy accounting.
- Retention sekarang dipisahkan dari coupling melalui bentuk S_(n+1)=f(C D_lambda S_n + B X_n + K_W W_n + epsilon_n), sehingga retention tidak dihitung dua kali pada transition matrix.
- Ditambahkan simulator dependency-light Python: 04_RESEARCH/physical_stateful_cell_simulator_v0_1.py.
- Ditambahkan spesifikasi eksperimen numerik: free decay, single update, repeated update, retention sweep, delay sweep, noise sweep, read disturbance, reset, dan nonlinearity sweep.
- Initial engineering screening thresholds ditetapkan sebagai screening values, bukan hukum fisika atau hasil eksperimen.
- Literatur 2025–2026 menunjukkan memory, nonlinearity, dan wave/photonic dynamics sudah memiliki demonstrasi fisik; karena itu Horizon tidak mengklaim mekanisme tersebut sebagai novelty tersendiri. Fokus novelty tetap pada formulasi computational cell dan pembuktian trade-off terukur.
- Status: mathematical simulator / proposed synthesis; belum ada hasil eksperimen hardware.

## 2026-10-05 — Web Validation Layer

- STWF Visual Laboratory ditingkatkan ke v0.4.
- Ditambahkan explicit representation layer: physical/abstract state P dipetakan menjadi numerical state S=M(P).
- Ditambahkan RUN COMPUTATION TEST berbasis target S_(n+1)=lambda*S_n+X_n dengan lambda=1, X=[3,5,2,7], expected [3,8,10,17].
- Web test menghitung actual trajectory dan RMS error, lalu memberi status PASS/FAIL.
- Test diberi batas epistemik: PASS hanya memvalidasi model numerik dan harness browser; tidak dianggap sebagai eksperimen material atau bukti hardware.
- Status web: runnable validation layer, dengan mathematical computation test terintegrasi.
- Commit: 28ce71ed1e6c7769d6e79c34807d80e818fb10b0.

## 2026-10-06 — External test infrastructure boundary

- Accepted D-012: Horizon should use existing external measurement methods, commercial instruments, and established research facilities whenever suitable infrastructure already exists.
- Custom instrumentation, custom calibration systems, dedicated Horizon laboratories, and a browser-based physical test substitute are explicitly out of core scope by default.
- Updated TEST_INFRASTRUCTURE_SCOPE.md to make the workflow: falsifiable claim → minimum observables → existing measurement method → existing instrument/facility → minimal DUT interface → measurement data.
- The browser laboratory remains a software verification/visualization tool and is not treated as physical test infrastructure.

## 2026-10-06 — Existing test infrastructure registry

- Added 04_RESEARCH/EXISTING_TEST_INFRASTRUCTURE_REGISTRY_V0_1.md.
- Mapped the minimum Stateful Core observables to established measurement classes such as oscilloscope/digitizer, SMU/semiconductor parameter analyzer, LCR/impedance measurement, optical power/photodetection, spectroscopy, and phase/frequency-domain measurements.
- Recorded publicly documented candidate facilities at UI and ITS as external infrastructure candidates; access, cost, scheduling, sample requirements, and measurement uncertainty remain unresolved and must be confirmed directly.
- No facility listing is treated as evidence of a Horizon experiment or as a commitment to a final physical platform.

# CHANGELOG

## 2026-10-05

- STWF Visual Laboratory v0.3 ditingkatkan dari model wave/state menjadi model resonance + state + feedback.
- Jalur komputasi visual sekarang dimodelkan sebagai: INPUT → WAVE FIELD → INTERFERENCE → STATE → FEEDBACK → WAVE FIELD.
- Ditambahkan parameter visual Feedback dan Resonance untuk menguji secara matematis pengaruh umpan balik dan penyimpanan state/resonansi.
- Mode INTERFERENCE sekarang memiliki fieldMemory yang memengaruhi medan pada langkah berikutnya.
- Mode STATE sekarang memiliki field-level memory yang berinteraksi dengan lima state cells dan dikembalikan melalui feedback path.
- Ditambahkan visualisasi jalur feedback dan node FIELD STATE agar hubungan antara medan dan state dapat diamati langsung.
- Model nonlinear sederhana menggunakan saturasi/tanh dan threshold attenuation; ini adalah abstraksi matematis, bukan model material tertentu.
- Status tetap dipisahkan: visual/mathematical model dan proposed synthesis; belum ada hasil eksperimen hardware.
- Commit visual upgrade: ed8ff661c9c712a18fb7f8cdd7a9800ef721a0d8.

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


## 2026-10-06 — Web validation audit correction

- Audited STWF Visual Laboratory v0.4 after manual browser inspection.
- Identified two verification weaknesses: static STATE-node visualization and circular expected-vs-actual computation.
- Updated web laboratory to v0.5.
- Added visible moving transport markers in STATE mode.
- Changed computation validation to use a fixed reference trajectory and a runtime trace with per-step error, RMS error, and maximum absolute error.
- Recorded the audit in 04_RESEARCH/WEB_TEST_AUDIT_V0_1.md.
- Clarified that web PASS verifies the numerical harness only and does not validate physical hardware.
