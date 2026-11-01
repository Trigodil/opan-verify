# Checking where the window [23, n-23] first fails, then the missing k <= 40 for exactly n = 6917805
import sys
from common import opan, divs, sums, primes_upto

N=int(float(sys.argv[1])) if len(sys.argv)>1 else 7*10**6
first=None
for f,n in sorted(opan(N),key=lambda x:x[1]):
    S=sums(divs(f)[:-1]); c=n//2
    lo=next(a for a,b in S if a<=c<=b)
    if lo>23 and first is None: first=(n,f,lo)
print("first n where [23, n-23] fails:",first)
n=6917805; D=[d for d in range(1,41) if n%d==0]; R={0}
for d in D: R|={x+d for x in R}
print(n,"missing k <= 40:",sorted(set(range(41))-R))
