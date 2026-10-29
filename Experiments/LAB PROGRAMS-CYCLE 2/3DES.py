from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
key = DES3.adjust_key_parity(b'123456789012345678901234')
c = DES3.new(key, DES3.MODE_ECB)
e = c.encrypt(pad(b'AKSHAYA', 8))
print("Encrypted:", e.hex())
print("Decrypted:", unpad(c.decrypt(e), 8).decode())
