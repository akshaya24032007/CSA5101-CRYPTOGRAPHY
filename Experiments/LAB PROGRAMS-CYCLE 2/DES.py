from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
key = b'12345678'
msg = b'HELLO'
c = DES.new(key, DES.MODE_ECB)
e = c.encrypt(pad(msg, 8))
print("Encrypted:", e.hex())
print("Decrypted:", unpad(c.decrypt(e), 8).decode())
