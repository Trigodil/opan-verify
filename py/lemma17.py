# Checking Lemma 17 for odd m < 4000 with a central block and primes q < q2 < 2*sigma(m)
from collections import Counter
from common import is_prime, sums, merge

def cdiv(a,b): return -(-a//b)
st=Counter()
for m in range(15,4000,2):
    D=[d for d in range(1,m+1) if m%d==0]; s=sum(D); ss=s-m; dl=2*m-s
    if dl<1: continue
    mid=[iv for iv in sums(D[:-1]) if iv[0]<=ss//2<=iv[1]]
    if not mid or mid[0][0]+mid[0][1]!=ss: continue
    a=mid[0][0]; L=ss-2*a+1; g0=dl+2*a-1
    S0=set(range(a,ss-a+1))|set(range(m+a,s-a+1))

    # this block checks that the endpoint penalty of Z_w stays <= g0 for every shift t
    for t in range(2*a-s,s-2*a+1):
        Z=[z for z in S0 if z-t in S0]
        if Z: st['penalty ok' if min(Z)-max(a,a+t)<=g0 else 'penalty BAD']+=1
    if len(S0)**2>400000: continue
    for q in range((s-2*a+1)//2+1,2*s):
        if not is_prime(q) or m%q==0: continue
        for q2 in range(q+2,2*s):
            if not is_prime(q2) or m%q2==0: continue
            g=q2-q
            if g*(2*g0+1)>L: break
            c=2*g0+cdiv(max(q-s+2*a-1,g0),g)
            if q2>2*s-4*a-2*c: continue
            vals={q*u+q2*w for u in S0 for w in S0}
            iv=merge([[v+x,v+y] for v in vals for x,y in [[a,ss-a],[m+a,s-a]]])
            st['interval ok' if max(y-x+1 for x,y in iv)>=q*q2 else 'interval BAD']+=1
print(dict(st))
