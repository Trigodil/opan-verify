#include <stdio.h>
#include <stdlib.h>
// Checking odd squares N = k^2 for k up to K, and tracking the smallest delta/sqrt(N) and every |delta| <= 300
int main(int argc,char**argv){
 long K=argc>1?atol(argv[1]):100000000; unsigned*spf=calloc(K+1,4);
 for(long p=2;p*p<=K;p++) if(!spf[p]) for(long j=p*p;j<=K;j+=p) if(!spf[j]) spf[j]=p;
 double best=1e9; long bk=0;
 for(long k=3;k<=K;k+=2){
  long x=k; __int128 s=1;
  while(x>1){ long p=spf[x]?spf[x]:x; int a=0; while(x%p==0){x/=p;a++;}
   __int128 t=1,pw=1; for(int i=0;i<2*a;i++){pw*=p;t+=pw;} s*=t; }
  __int128 d=2*(__int128)k*k-s;
  if(d>=-300&&d<=300) printf("small k=%ld delta=%lld\n",k,(long long)d);
  if(d>0&&(double)d/k<best){best=(double)d/k;bk=k;}
 }
 printf("K=%ld min delta/sqrt(N)=%.4f at k=%ld\n",K,best,bk);
}
