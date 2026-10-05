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
