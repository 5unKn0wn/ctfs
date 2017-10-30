from Crypto.Cipher import AES
from pkcs7 import PKCS7Encoder

enc = "PC9al1Z5yLVCjov4DxxUoxCftGm5V92neSDAtvSKSlFrQPiyFh1d56skf/Z7avSl".decode('base64')
for time in range(180):
	for cnt in range(99):
		key = "2008" + str(time) + str(cnt).zfill(2)
		key = key.zfill(32)

		aes = AES.new(key, AES.MODE_ECB)
		decoder = PKCS7Encoder()

		dec = aes.decrypt(enc)
		dec = decoder.decode(dec)
		if dec.startswith("CATSEC{"):
			print dec
