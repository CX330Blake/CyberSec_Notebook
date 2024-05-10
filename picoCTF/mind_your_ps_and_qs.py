"""
This is the problem
=============================
Decrypt my super sick RSA:
c: 421345306292040663864066688931456845278496274597031632020995583473619804626233684
n: 631371953793368771804570727896887140714495090919073481680274581226742748040342637
e: 65537
=============================
Note:
n = p * q
phi(n) = (p-1) * (q-1)
e is the encryption exponent
d = e^-1 mod phi(n)
c is the encrypted message; c = m^e mod n
m is the message; m = c^d mod n
public key  = (e, n)
private key = (d, n)
"""

from Crypto.Util.number import inverse, long_to_bytes
from factordb.factordb import FactorDB


def long2str(long_int: int) -> str:
    return long_to_bytes(long_int).decode()


c = 421345306292040663864066688931456845278496274597031632020995583473619804626233684
n = 631371953793368771804570727896887140714495090919073481680274581226742748040342637
e = 65537

# From Factor db find p and q
f = FactorDB(n)
f.connect()
factors = f.get_factor_list()
p = factors[0]
q = factors[1]

phi_n = (p - 1) * (q - 1)

d = inverse(e, phi_n)
print(f"Private key: d = {d}")
m = pow(c, d, n)
print(f"Decrypted message: m = {long2str(m)}")
