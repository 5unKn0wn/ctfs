from Crypto.Cipher import AES

def decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

key = "awesomecipherkey"
iv = "handsomeinitvect"

with open("eggyolk", "rb") as f:
	cipher_text = f.read()

data = decrypt(cipher_text, key, iv)

with open("decrypt.dex", "wb") as f:
	f.write(data)
