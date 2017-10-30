from Crypto.Cipher import AES
from Crypto import Random

unpad = lambda s : s[0:-ord(s[-1])]
enc = open("bs", "rb").read()
key = "E0297E21157EC442C440E8119E2372F5E87CA421FBCEAC0589217458D1ED80F6".decode('hex')
iv = "\x00" * 16
cipher = AES.new(key, AES.MODE_CBC, iv)
dec = unpad(cipher.decrypt(enc))
open("dex.zip", "wb").write(dec)
