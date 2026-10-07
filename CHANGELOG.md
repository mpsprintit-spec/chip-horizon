## 2026-10-07 — WCR external access route audit v0.8

- Added `04_RESEARCH/WCR_EXTERNAL_ACCESS_ROUTE_AUDIT_V0_8.md`.
- Identified NUS/SHINE as the highest-value external route because the demonstrated FeFET-Pockels photonic-memory platform and its characterization ecosystem are directly associated with that research centre.
- Audited Indonesian fallback measurement routes at ITS and ITB; these provide relevant optical/photonic measurement capabilities but public evidence does not establish access to the exact FeFET-Pockels DUT.
- Simplified the first physical causal experiment to scalar optical-power readout, avoiding phase-sensitive coherent detection until phase becomes an explicit computational state coordinate.
- Defined V0.9 as the external collaboration / DUT availability gate.

## 2026-10-07 — WCR external platform audit v0.7

- Added `04_RESEARCH/WCR_EXTERNAL_PLATFORM_AUDIT_V0_7.md`.
- Audited three existing photonic platform classes against the minimum Horizon WCR causal experiment: ferroelectric Pockels photonic memory, FLARE fully in-memory photonic computing, and nonlinear multistable photonic microcavity.
- Promoted the FeFET-Pockels photonic memory platform as the first external measurement candidate because it already exposes controlled multi-state preparation, optical state-dependent response, retention, repeatability, and high-speed photodetection.
- Retained FLARE as an integration/scaling benchmark and nonlinear multistable microcavity as a nonlinear-dynamics benchmark.
- Defined the external A/B protocol: prepare S_A and S_B, apply the same later optical probe X, measure Y_A and Y_B, randomize trial order, and require output separation greater than the complete uncertainty budget.
- Explicitly separated literature-established device behaviour from Horizon mathematical synthesis and from unperformed Horizon physical experiments.
- Applied D-012: the next step is to identify an existing external device/laboratory measurement path; no custom Horizon instrumentation is proposed.

## 2026-10-07 — Concrete WCR physical candidates

- Added `03_ARCHITECTURE/STWF/PHOTONIC_WCR_PHYSICAL_CANDIDATE_V0_1.md`.
- Defined a concrete photonic WCR candidate as a confined optical propagation region coupled to a nonlinear/stateful material or device.
- Specified the physical moving quantity, candidate state locations, computational feedback loop, causal state-dependent response test, external measurement classes, validation ladder, and kill criteria.
- Added `03_ARCHITECTURE/STWF/MAGNONIC_WCR_PHYSICAL_CANDIDATE_V0_1.md`.
- Defined a concrete magnonic WCR candidate as a spin-wave propagation region coupled to a controllable magnetic/spintronic state.
- Specified amplitude, phase, frequency, timing, spatial mode, and magnetic configuration as candidate rich-state coordinates subject to measurement validation.
- Added `04_RESEARCH/WCR_CANDIDATE_COMPARISON_GATE_V0_1.md`.
- Established a common A/B causal experiment: prepare two states, apply the same later input, measure state-dependent outputs, and require output separation greater than the complete uncertainty budget with repeatability.
- Preserved photonic and magnonic platforms as open candidates; no final physical platform selected.
- Incorporated recent external evidence as prior art and physical plausibility, without treating it as evidence that Horizon has already achieved the proposed architecture.
- Reinforced the rule that nominal state count is not computational capacity unless states are distinguishable, writable, retainable, transformable, and readable.

## 2026-10-07 — WCR candidate causal mapping

- Added `04_RESEARCH/WCR_CANDIDATE_CAUSAL_MAPPING_V0_1.md`.
- Mapped photonic and magnonic/spin-wave WCR candidates from digital input through physical field evolution, state interaction, readout, and digital output.
- Defined candidate-specific causal experiments for state preparation, retention, identical later input, and state-dependent output.
- Compared propagation, interference, state coupling, conversion overhead, loss, integration, and scalability risks.
- Preserved both candidates as open; no final material platform selected.
- Defined kill criteria based on measurement uncertainty, state controllability, retention, energy, coupling, variability, and chip-scale integration.

## 2026-10-07 — Physical mechanism deep map

- Added `01_FOUNDATION/PHYSICAL_MECHANISM_DEEP_MAP_V0_1.md`.
- Decomposed the proposed WCR into field, interaction, nonlinearity, persistent state, feedback, and readout layers.
- Mapped photonic, magnonic/spin-wave, and ferroelectric candidate mechanisms to physical entities, state variables, causal paths, strengths, and unresolved integration problems.
- Formalized the rich-internal-state / binary-I/O architecture as a system-level hypothesis.
- Defined the decisive physical test as same later input producing different measurable output after preparation of different internal physical states.
- Mapped required observables to existing external measurement classes, consistent with D-012.
- Added candidate-selection criteria covering state distinguishability, retention, latency, energy, noise, variability, coupling, density, and end-to-end binary I/O overhead.
- Preserved epistemic separation between established physics, mathematical deduction, Horizon synthesis, unresolved engineering, and unproven claims.

## 2026-10-06 — Minimum WCR causal experiment

- Added `04_RESEARCH/MINIMUM_WCR_CAUSAL_EXPERIMENT_V0_1.md`.
- Defined the smallest falsifiable causal claim for a stateful WCR: controlled wave input changes physical state, state persists, and the same later input produces a measurably different response.
- Defined E0-E8 validation stages covering instrument baseline, propagation, coupling/interference, nonlinearity, state update, retention, causal state-dependent response, repeatability, and energy/latency accounting.
- Added control conditions and an independence requirement to prevent circular validation.
- Explicitly separated WCR-mechanism validation from claims about universal computation, speed, energy advantage, manufacturability, smartphone integration, or supercomputer scaling.
- Mapped the experiment to existing external measurement classes rather than proposing a custom Horizon laboratory.

## 2026-10-06 — Operational computational data path

- Added `03_ARCHITECTURE/STWF/OPERATIONAL_DATA_PATH_V0_1.md`.
- Defined the end-to-end path from external data to input interface, space-time encoding, wave generation/transport, WCR computation, nonlinear/state interaction, feedback, readout, and external output.
- Explicitly separated numerical/system representation from internal physical wave/state representation.
- Recorded the concrete `5 + 3 = 8` example as a computational contract and teaching case only; it is not a hardware result.
- Clarified the distinction between wave communication and wave computation.
- Added the causal requirement that a candidate WCR must show wave input -> physical state change -> retained state -> state-dependent later wave response -> measurable output.
- Added D-014 to the design-decision record.

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


## 2026-10-07 — Natural mechanism reconstruction hypothesis

- Added `01_FOUNDATION/NATURAL_MECHANISM_RECONSTRUCTION_HYPOTHESIS_V0_1.md`.
- Recorded the methodological hypothesis that engineering can discover physical mechanisms already permitted by nature and then engineer them into new architectures, rather than treating current binary computation as the boundary of possible computation.
- Used the bird-wing analogy to distinguish natural physical mechanism from engineered implementation.
- Formalized the distinction between creating a physical object, discovering a physical mechanism, and engineering a new architecture.
- Recorded the binary-interface / rich-internal-state direction as a hypothesis rather than an established result.
- Added explicit requirements for distinguishability, write/read control, transformation, retention, noise tolerance, programmability, scalability, energy, and latency.


## 2026-10-07 — Natural computational mechanism candidate screening

- Added `01_FOUNDATION/NATURAL_COMPUTATIONAL_MECHANISM_CANDIDATE_SCREEN_V0_1.md`.
- Screened photonic, magnonic/spin-wave, ferroelectric, memristive/oxide, and phononic/acoustic mechanisms against the required Horizon properties.
- Identified coupled wave-field plus persistent-state regions as the most relevant current research direction, without selecting a final material.
- Defined the first falsifiable candidate test around distinguishable internal states, controlled state transitions, retention, state-dependent response, repeatability, noise, energy, and latency.
- Explicitly rejected nominal state count as evidence of computational capacity unless states are physically distinguishable, writable, retainable, transformable, and readable.


## 2026-10-07 — Independent WCR operating-envelope sweep v0.5

- Added 04_RESEARCH/INDEPENDENT_WCR_OPERATING_ENVELOPE_SWEEP_V0_5.md.
- Added 04_RESEARCH/independent_wcr_operating_envelope_sweep_v0_5.py.
- Swept damping/retention, cross-coupling, nonlinear strength, and state noise across 320 numerical conditions.
- Found multiple bounded parameter regions where two different internal states remain distinguishable under the exploratory gate.
- Introduced the Effective Computational State Envelope concept as a bridge between mathematical parameters and experimentally measurable device parameters.
- Explicitly classified the result as numerical simulation, not physical validation.
- Next falsification target: map abstract parameters to measurable physical quantities on one candidate WCR platform.


## 2026-10-07 — WCR physical parameter mapping gate v0.6

- Added 04_RESEARCH/WCR_PHYSICAL_PARAMETER_MAPPING_GATE_V0_6.md.
- Selected photonic WCR as the first parameter-mapping candidate because existing integrated photonic platforms expose optical field, memory, nonlinear response, multi-state behaviour, and readout observables.
- Mapped abstract WCR parameters to candidate measurable quantities such as Q/ringdown, coupling, resonance shift, coherent phase, transmission, noise, drift, and retention.
- Defined the minimum same-input/different-state A/B causal experiment with randomized state order and total uncertainty.
- Preserved magnonic WCR as an independent comparison branch.
- Applied D-012: use existing external measurement infrastructure before designing custom instrumentation.
