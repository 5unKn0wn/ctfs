from Crypto.Cipher import AES
from pkcs7 import PKCS7Encoder
import base64

shared_key = "26a6f9cc-d019-4f"
IV = "0000000000000000"

with open("flag_db", "rt") as f:
	while True:
		cipher_text = f.readline().rstrip()
		aes_decrypter = AES.new(shared_key, AES.MODE_CBC, IV)
		aes_decrypter.block_size = 128
		clear_text = PKCS7Encoder().decode(aes_decrypter.decrypt(base64.b64decode(cipher_text)))
		if clear_text.startswith("RCTF{"):
			print clear_text
			break
