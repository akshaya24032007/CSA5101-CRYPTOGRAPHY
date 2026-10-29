from Crypto.Cipher import DES
from Crypto.Util.Padding import pad,unpad
k=b'12345678'; iv=b'abcdefgh'
c=DES.new(k,DES.MODE_CBC,iv)
e=c.encrypt(pad(b'CHENNAI',8))
print("Encrypted:",e.hex())
print("Decrypted:",unpad(DES.new(k,DES.MODE_CBC,iv).decrypt(e),8).decode())
