# Runs all of the scripts
set -e
cd "$(dirname "$0")"
python3 py/conjecture.py 1e7
python3 py/window.py 7e6
python3 py/theorem_x.py
python3 py/pair_blocks.py
gcc -O2 -o cusp cusp.c && ./cusp 100000000
echo "Slower runs are python3 py/lemma17.py, python3 py/conjecture.py 1e10, ./cusp 1000000000"
