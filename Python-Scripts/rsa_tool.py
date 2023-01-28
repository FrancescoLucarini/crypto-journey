from Crypto.Util.number import inverse, long_to_bytes
import sys
from factordb.factordb import FactorDB

print("python3 rsa_tool.py n e c")

n = int(sys.argv[1])
e = int(sys.argv[2])
c = int(sys.argv[3])

f = FactorDB(n)
f.connect()
factors = f.get_factor_list()
p = factors[0]
q= factors[1]

phi = (p-1)*(q-1)
d = inverse(e, phi)
m = pow(c, d, n)

print(long_to_bytes(m))
