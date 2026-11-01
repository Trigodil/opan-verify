import bisect
from math import isqrt

def primes_upto(n):
    s=bytearray([1])*(n+1); s[:2]=b'\0\0'
    for i in range(2,isqrt(n)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]

def is_prime(x):
    return x>1 and all(x%d for d in range(2,isqrt(x)+1))

def sigma(f):
    r=1
    for p,a in f: r*=(p**(a+1)-1)//(p-1)
    return r

def divs(f):
    D=[1]
    for p,a in f: D=[d*p**e for d in D for e in range(a+1)]
    return sorted(D)

def merge(L):
    L=sorted(L); M=[]
    for a,b in L:
        if M and a<=M[-1][1]+1: M[-1][1]=max(M[-1][1],b)
        else: M.append([a,b])
    return M

def sums(D):
    # Subset sums of D stored as merged closed intervals
    S=[[0,0]]
    for d in D: S=merge(S+[[a+d,b+d] for a,b in S])
    return S

def contains(S,t):
    i=bisect.bisect_right([a for a,_ in S],t)-1
    return i>=0 and S[i][1]>=t

def opan(N):
    # Walks the factorizations and yields every odd primitive ample n <= N
    P=primes_upto(N//15+2)[1:]
    def dfs(i,f,n,s):
        for j in range(i,len(P)):
            p=P[j]
            if n*p>N: return
            h=s/n; m=n; k=j
            while k<len(P) and m*P[k]<=N: h*=P[k]/(P[k]-1); m*=P[k]; k+=1
            if h<=2: return
            pa=1
            for a in range(1,64):
                pa*=p
                if n*pa>N: break
                nf=f+[(p,a)]; nn=n*pa; ns=sigma(nf)
                if ns>2*nn:
                    if all(2*(nn//q)>=sigma([(r,b-(r==q)) for r,b in nf]) for q,_ in nf):
                        yield nf,nn
                    break
                yield from dfs(j+1,nf,nn,ns)
    yield from dfs(0,[],1,1)
