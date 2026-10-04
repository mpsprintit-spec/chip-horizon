# OPEN PROBLEMS

## Physics / device

1. Medium fisik apa yang memberi kombinasi terbaik antara loss, controllability, nonlinearity, lifetime, dan manufacturability?
2. Bagaimana amplitude dan phase di-encode secara robust?
3. Bagaimana negative information direpresentasikan?
4. Nonlinear element seperti apa yang praktis?
5. Bagaimana state dipertahankan tanpa energy cost berlebihan?

## Architecture

6. Bagaimana local cores berkomunikasi?
7. Bagaimana region beroperasi tanpa global clock?
8. Bagaimana state contamination dicegah?
9. Bagaimana decay mempengaruhi precision?
10. Bagaimana arsitektur scale beyond small matrices?

## Energy

11. Berapa joule/op sebenarnya?
12. Pada skala berapa conversion menjadi bottleneck?
13. Apakah physical parallelism mengimbangi source/detector overhead?
14. Berapa energi untuk correction?

## Software

15. Programming model apa yang memetakan algoritma ke physical trajectories?
16. Bagaimana compiler memilih weights, phase, dan delay?
17. Bagaimana state lifecycle diekspresikan?
18. Bagaimana physical computation di-debug?

## Verification

19. Seberapa dekat simulation dengan hardware?
20. Benchmark apa yang dapat membuktikan keunggulan nyata?

## Prioritas berikutnya

Bangun mathematical STWF Stateful Core dan uji running sum, temporal filter, serta recurrent matrix computation dengan loss, noise, timing jitter, readout cost, dan state contamination yang realistis.
