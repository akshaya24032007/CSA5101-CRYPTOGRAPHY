import string
s = input("Enter ciphertext: ").upper()
for a in range(1, 26):
    if __import__('math').gcd(a, 26) == 1:
        for b in range(26):
            d = pow(a, -1, 26)
            print(''.join(chr((d*(ord(c)-65-b))%26+65)
                  if c in string.ascii_uppercase else c for c in s))
