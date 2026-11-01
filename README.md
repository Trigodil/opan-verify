Verification scripts for the MO answer on (n+1)/2 for odd primitive abundant n

Needs Python 3 with numpy and sympy and gcc, and ./run_all.sh runs the quick checks

conjecture.py N checks (n+1)/2 in P(n) for every odd primitive abundant n up to N

window.py N finds where the window [23, n-23] first fails and shows 26 is missing for 6917805

theorem_x.py checks the algebra behind Theorem X
lemma17.py checks pair healing for odd m < 4000 and is (very) slow
pair_blocks.py checks central blocks of V(m, q*q2) for m = 315 including resonant pairs
cusp.c K scans odd squares k^2 for k up to K and compares delta with sqrt(N)
