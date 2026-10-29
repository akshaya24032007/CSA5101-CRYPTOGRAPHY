from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad,unpad
c=Blowfish.new(b'mysecret',Blowfish.MODE_ECB)
e=c.encrypt(pad(b'PYTHON',8))
print("Encrypted:",e.hex())
print("Decrypted:",unpad(c.decrypt(e),8).decode())
