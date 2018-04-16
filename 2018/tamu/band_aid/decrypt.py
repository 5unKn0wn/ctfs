from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from base64 import b64decode

rsa_key = RSA.importKey(open('private.pem', "rb").read())
verifier = PKCS1_v1_5.new(rsa_key)
raw_cipher_data = b64decode(open('flag.enc', "rb").read())
phn = rsa_key.decrypt(raw_cipher_data)
print phn
