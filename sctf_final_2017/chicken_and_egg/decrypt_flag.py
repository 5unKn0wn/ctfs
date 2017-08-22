from Crypto.Cipher import AES

def pkcs5_unpad(s):
    return s[0:-ord(s[-1])]

def decrypt(key, iv, value):
    crypted = value
    cipher = AES.new(key,AES.MODE_CBC,iv)
    return pkcs5_unpad(cipher.decrypt(crypted))

key = "kingodemperorchungmugongalmighty"
iv = "superduperinjung"

with open("flag_d3d69b8e17770c367ec4e8e877482419a2e36f8f.enc", "rb") as f:
    data = f.read()

data = decrypt(key, iv, data)

with open("flag.pdf", "wb") as f:
    f.write(data)
