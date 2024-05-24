from Crypto.Util.number import long_to_bytes
from pwn import *

r = remote("mercury.picoctf.net", 10333)
r.recvuntil("n:")
n = int(r.recvline().strip())
r.recvuntil("ciphertext:")
c = int(r.recvline().strip())
num = n + c
r.sendline(str(num))
r.recvuntil("Here you go:")
m = int(r.recvline().strip())
r.close()

print(long_to_bytes(m))
