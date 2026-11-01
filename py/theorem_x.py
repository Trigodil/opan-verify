# Checking e(n) = 6, the primitivity bound and the j window for n = m*(2m-7)
import sympy as sp

m=sp.symbols('m',positive=True)
q=2*m-7
print("e(n) =",sp.expand((2*m-1)*(q+1)-2*m*q))
h=(2-1/m)*(1-sp.Rational(2,3)/m)*(1+1/q)
print("2 - h(qm/p) bound =",sp.factor(sp.simplify(2-h)),"(positive for m > 9)")
print("x for j=3 minus (2m-1) =",sp.expand((3*q+1)/2-(2*m-1)),"(positive for m > 9)")
print("x for j=1 =",sp.expand((q+1)/2))
