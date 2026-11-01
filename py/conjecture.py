# Checking (n+1)/2 in P(n) for every odd primitive ample n up to N
import sys
from common import opan, divs, sums, contains

N=int(float(sys.argv[1])) if len(sys.argv)>1 else 10**7
total=fails=0
for f,n in opan(N):
    total+=1
    if not contains(sums(divs(f)[:-1]),(n+1)//2):
        fails+=1; print("FAIL",n,f)
print(f"odd primitive abundant n <= {N}: {total}, failures of (n+1)/2: {fails}")
