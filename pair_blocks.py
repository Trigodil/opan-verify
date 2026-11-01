# checking central blocks of V(315 to q*q2) for jump ratios 2 to 8 and for resonant pairs.
import numpy as np
from sympy import nextprime, isprime, divisors

def subset_sums(D):
    b=np.zeros(sum(D)+1,bool); b[0]=1
    for d in D: b[d:]|=b[:-d].copy()
    return np.nonzero(b)[0]

def block_ratio(S,s,q,q2):

    # Ratio c/U of the central block of S + q*S + q2*S.
    U=s*(1+q+q2); V=np.zeros(U+s+2,bool)
    for y in S:
        for z in S: V[q*y+q2*z+S]=True
    bad=np.nonzero(~V[:U+1])[0]; c=U//2
    return round((bad[bad<c].max()+1 if (bad<c).any() else 0)/U,4)

m=315; D=[int(d) for d in divisors(m)]; s=sum(D); S=subset_sums(D)
for lam in (2,3,5,8):
    for gap in (16,150,1200):
        q=nextprime(int(lam*s)); q2=nextprime(q+gap)
        print(f"lambda={lam} q={q} q'={q2} ratio={block_ratio(S,s,q,q2)}")
q=1873
for k,h in ((2,-19),(3,-28),(3,4)):
    if isprime(k*q+h): print(f"resonant q'={k}q{h:+d} ratio={block_ratio(S,s,q,k*q+h)}")
