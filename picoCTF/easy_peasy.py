from pwn import *
import binascii  # binascii.unhexlify() is used to convert hex to binary

offset = 50000 - 32

r = remote("mercury.picoctf.net", 11188)

print(r.recvline())
print(r.recvline())
encrypted_flag = r.recvline().strip()

print(encrypted_flag)

r.recvuntil(b"?")
r.sendline(b"A" * offset)
r.recvuntil(b"?")
r.sendline(b"A" * 32)
r.recvline()

encoded = r.recvline().strip()
encoded = binascii.unhexlify(encoded)

message = "A" * 32
key = []
for i in range(len(encoded)):
    key.append(ord(message[i]) ^ encoded[i])

flag = []
encrypted_flag = binascii.unhexlify(encrypted_flag)
for i in range(len(encrypted_flag)):
    flag.append(chr(key[i] ^ encrypted_flag[i]))

flag = "".join(flag)
print(flag)
