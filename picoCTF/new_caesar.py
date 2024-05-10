import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        enc += ALPHABET[int(binary[:4], 2)]  # Since 4 bits can represent 16 characters
        enc += ALPHABET[int(binary[4:], 2)]
    return enc


def b16_decode(b16):
    dec = ""
    for c in range(0, len(b16), 2):
        first = b16[c]
        second = b16[c + 1]
        first_index = ALPHABET.index(first)
        second_index = ALPHABET.index(second)
        binary = bin(first_index)[2:].zfill(4) + bin(second_index)[2:].zfill(4)
        dec += chr(int(binary, 2))
    return dec


def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET  # (c - 97 + k - 97) % 16 = result
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]  # two numbers sum modulo 16


def inverse_shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]  # two numbers difference modulo 16


enc = "apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna"
for key in ALPHABET:
    dec = ""
    for i, c in enumerate(enc):
        dec += inverse_shift(c, key[i % len(key)])
    b16_dec = b16_decode(dec)
    print(f"Decrypted flag: {b16_dec}")

"""
Flag: et_tu?_23217b54456fb10e908b5e87c6e89156

You shoul wrap it by picoCTF{} by youself.
"""
