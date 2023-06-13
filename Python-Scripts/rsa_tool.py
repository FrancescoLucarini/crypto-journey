from factordb.factordb import FactorDB
from Crypto.Util.number import inverse, long_to_bytes
import sympy

n = int(input("n value > "))
e = int(input("e value > "))
c = int(input("c value > "))

if sympy.isprime(n):
	phi = n-1
else:
	f = FactorDB(n)
	f.connect()
	factors = f.get_factor_list()
	if len(factors) == 2:
		p = factors[0]
		q = factors[1]
		if p==q:
			phi = p*(q-1)
		else:
			phi = (p-1)*(q-1)
		
	else:
		phi = 1
		for factor in factors:
			phi *= (factor-1)
	
	
d = inverse(e, phi)
m = pow(c, d, n)

print(long_to_bytes(m))
