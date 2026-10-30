def rol(x, n):
    n %= 32
    return ((x << n) | (x >> ((32-n) % 32))) & 0xffffffff
def ror(x, n):
    n %= 32
    return ((x >> n) | (x << ((32-n) % 32))) & 0xffffffff
def setup(key):
    P, Q = 0xB7E15163, 0x9E3779B9
    L = [int.from_bytes(key[i:i+4], 'little')
         for i in range(0, len(key), 4)]
    S = [(P+i*Q) & 0xffffffff for i in range(26)]
    A = B = i = j = 0
    for _ in range(78):
        A = S[i] = rol((S[i]+A+B) & 0xffffffff, 3)
        B = L[j] = rol((L[j]+A+B) & 0xffffffff, (A+B))
        i = (i+1) % 26
        j = (j+1) % len(L)
    return S

def encrypt(a, b, S):
    a = (a+S[0]) & 0xffffffff
    b = (b+S[1]) & 0xffffffff
    for i in range(1, 13):
        a = (rol(a ^ b, b)+S[2*i]) & 0xffffffff
        b = (rol(b ^ a, a)+S[2*i+1]) & 0xffffffff
    return a, b
def decrypt(a, b, S):
    for i in range(12, 0, -1):
        b = ror((b-S[2*i+1]) & 0xffffffff, a) ^ a
        a = ror((a-S[2*i]) & 0xffffffff, b) ^ b
    return (a-S[0]) & 0xffffffff, (b-S[1]) & 0xffffffff
key = b'12345678'
S = setup(key)
a, b = encrypt(123, 456, S)
print("Encrypted:", a, b)
print("Decrypted:", *decrypt(a, b, S))
