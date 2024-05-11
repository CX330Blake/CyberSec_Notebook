"""
LKOb (bwvek ove lgqkhej kwj osgx) gej g kyqj vo lvrqhkje bjlhetky lvrqjktktvu. Lvukjbkgukb gej qejbjukjz dtkw g bjk vo lwgssjuxjb dwtlw kjbk kwjte lejgktftky, kjlwutlgs (guz xvvxstux) bitssb, guz qevmsjr-bvsftux gmtstky. Lwgssjuxjb hbhgssy lvfje g uhrmje vo lgkjxvetjb, guz dwju bvsfjz, jglw ytjszb g bketux (lgssjz g osgx) dwtlw tb bhmrtkkjz kv gu vustuj blvetux bjeftlj. LKOb gej g xejgk dgy kv sjgeu g dtzj geegy vo lvrqhkje bjlhetky bitssb tu g bgoj, sjxgs juftevurjuk, guz gej wvbkjz guz qsgyjz my rguy bjlhetky xevhqb gevhuz kwj dvesz ove ohu guz qeglktlj. Ove kwtb qevmsjr, 
kwj osgx tb: qtlvLKO{OE3AH3ULY_4774LI5_4E3_L001_6J0659OM}
"""

ciphertext = "kwj osgx tb: qtlvLKO{OE3AH3ULY_4774LI5_4E3_L001_6J0659OM}"
key = "QSJWRVAUKETCBXFZPMLINOHGYD"  # get it from https://www.guballa.de/substitution-solver

key_dict = {}
for i, c in enumerate(key):
    key_dict[chr(i + 65)] = c

plaintext = ""
for c in ciphertext:
    if c.islower():
        c = c.upper()
        plaintext += key_dict[c].lower()
    elif c in key_dict:
        plaintext += key_dict[c]
    else:
        plaintext += c
print(plaintext)
# picoCTF{FR3QU3NCY_4774CK5_4R3_C001_6E0659FB}
