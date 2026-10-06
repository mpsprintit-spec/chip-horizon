# DESIGN DECISIONS

D-001 — STWF digunakan sebagai nama arsitektur kerja karena space dan time merupakan bagian eksplisit dari computational field.

D-002 — State diperlakukan sebagai first-class computational element karena target bukan sekadar matrix accelerator.

D-003 — Wave, nonlinear, state, dan persistent layers dipisahkan karena kebutuhan fisik dan failure mode berbeda.

D-004 — Locality dan hierarchy diprioritaskan untuk mengendalikan communication cost.

D-005 — Energy dihitung end-to-end.

D-006 — Failed approaches dipertahankan sebagai research record.

D-007 — Established physics dipisahkan dari hypothesis.

D-008 — Stateful Core dikerjakan sebelum skala chip besar karena pertanyaan kunci adalah apakah persistent physical state benar-benar memberi computational reuse.


D-009 — Chip, test fixture, dan test/measurement system dipisahkan sebagai tiga lapisan berbeda agar validasi tidak berubah menjadi scope creep arsitektur chip.

D-010 — Test infrastructure dirancang dari minimum falsifiable experiment; laboratorium lengkap tidak dirancang sebelum computational cell dan physical observables ditetapkan.


### D-011 — Validation UI must be independently auditable

The web laboratory must separate fixed reference truth from runtime-computed results. A test must not derive both expected and actual values from the same runtime implementation and then treat agreement as independent validation. Visual elements that represent information flow should also make state transport observable rather than relying only on static node values.

**Rationale:** A testing interface is itself part of the verification chain. If the test harness cannot be independently inspected, a PASS can be circular. The web layer is therefore treated as a verification instrument for the mathematical model, not as evidence of physical behavior.

**Status:** Accepted, 6 October 2026.


### D-012 — External Test Infrastructure First

Horizon will not develop custom laboratory instruments or a custom web test system as part of the core project when suitable external methods, commercial instruments, or established research facilities already exist. Testing infrastructure is treated as external research infrastructure.

**Rule:** first identify the minimum physical observables required by the falsifiable experiment, then locate an existing measurement method/instrument/facility capable of measuring them. A custom fixture or instrument may be considered only when no suitable existing method is available and the missing interface is necessary to execute the experiment.

**Rationale:** The research objective is the Horizon computational mechanism, not the construction of a parallel instrumentation project. Test infrastructure must remain subordinate to the device-under-test and must not become a second primary engineering program.

**Status:** Accepted, 6 October 2026.
