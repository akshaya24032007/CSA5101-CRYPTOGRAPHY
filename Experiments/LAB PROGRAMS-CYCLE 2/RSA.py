from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
k=RSA.generate(2048)
e=PKCS1_OAEP.new(k.publickey()).encrypt(b'APPLE')
print("Encrypted:",e.hex())
print("Decrypted:",PKCS1_OAEP.new(k).decrypt(e).decode())
