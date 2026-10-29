from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
k1, k2 = b'12345678', b'abcdefgh'
m = pad(b'HELLO', 8)
e = DES.new(k2, DES.MODE_ECB).encrypt(
    DES.new(k1, DES.MODE_ECB).encrypt(m))
d = DES.new(k1, DES.MODE_ECB).decrypt(
    DES.new(k2, DES.MODE_ECB).decrypt(e))
print("Encrypted:", e.hex())
print("Decrypted:", unpad(d, 8).decode())
