"""
picoCTF{gvswwmrkxlivyfmgsrhnrisegl}
"""

cipher = "gvswwmrkxlivyfmgsrhnrisegl"


def caesar_cipher(text, shift):
    plaintext = ""
    for c in text:
        plaintext += chr((ord(c) - 97 + shift) % 26 + 97)
    return plaintext


for i in range(26):
    plaintext = caesar_cipher(cipher, i)
    print(f"Shift {i}: {plaintext}")
