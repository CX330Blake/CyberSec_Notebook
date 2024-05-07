"""
RSA 加解密演算法詳細步驟:

1. 選擇兩個大質數 p 和 q。計算它們的乘積 n = p * q。這是 RSA 的模數。
   選擇的質數應該足夠大，以防止通過分解 n 來破解 RSA 加密。

2. 計算 n 的歐拉函數 φ(n) = (p-1) * (q-1)。φ(n) 是 n 以下與 n 互質的正整數的個數。

3. 選擇一個與 φ(n) 互質的整數 e，稱為加密指數。通常選擇一個較小的質數，如 65537。

4. 使用 e 和 n 構建公鑰 (e, n)。公鑰將被公開，用於加密數據。

5. 計算 e 的模反元素 d，即 d ≡ e^(-1) (mod φ(n))。d 稱為私鑰指數。

6. 使用 d 和 n 構建私鑰 (d, n)。私鑰應該保密，只有擁有私鑰的人可以解密數據。

7. 加密過程:
   a. 將明文轉換為整數表示。可以使用 ASCII 編碼，每個字符對應一個數字。
   b. 對每個整數 m，計算密文 c = m^e mod n。
   c. 將所有密文組成的列表作為加密後的消息。

8. 解密過程:
   a. 對於每個密文 c，計算明文 m = c^d mod n。
   b. 將所有明文 m 組成的列表拼接在一起，得到原始的明文消息。

9. RSA 的安全性基於大數分解問題和數論中的數學性質。即使知道公鑰 (e, n)，也很難通過已知的信息來計算出私鑰 d。

10. 選擇合適的質數 p 和 q、適當的公鑰指數 e，以及足夠長的模數 n，是確保 RSA 安全性的關鍵。

11. 了解攻擊手法: https://blog.csdn.net/m0_52842062/article/details/119537547

"""

import random
from sympy import mod_inverse
from math import gcd


def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that e and phi are coprime
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Compute d, the modular multiplicative inverse of e mod phi
    d = mod_inverse(e, phi)

    return ((e, n), (d, n))


def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher


def decrypt(private_key, ciphertext):
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return "".join(plain)


# Example usage
p = 61
q = 53
public_key, private_key = generate_keypair(p, q)
message = "This is the RSA encryption."
encrypted_message = encrypt(public_key, message)
decrypted_message = decrypt(private_key, encrypted_message)

print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
