import sys

def tsu_super_decrypt3(c):
	l = len(c)
	k = l % 8
	string = ""
	for i in range(l):
		string += chr((ord(c[i]) << (8 - k) | ord(c[i]) >> k) & 0xff)
	return string

def tsu_super_decrypt2(c):
	l = len(c)
	string = ""
	for i in range(l):
		string += chr((ord(c[i]) - i) % 256)
	return string

def tsu_super_decrypt1(c, key):
	l = len(key)
	string = ""
	for i in range(len(c)):
		string += chr(ord(c[i]) ^ ord(key[i % l]))
	return string

def tsu_super_decrypt0(c):
	return c.decode('zlib')

# dec = "HzhTWlvmkrR/G+vf16cbqZv84jBiw44znXFZcJYILltPeAWbhQMzZfqZXliD7vnaIWdf/RA1kYJG9cWzLomQ81EIlAZQEEQ8QgGu8Idyhdj6XQ==" # 1
# dec = "HzhTWlvmkrR/G+vf16cbqZv84jBiw44znXFZcJYILltPeAWbhQMzZfqZXliD7vnaIWdf/RA1kYJG9cWzLomQ81EIlAZQEEQ8QgGu8H9yhdT6WQ==" # 2
dec = "xw784KOf2hE="
key = "\xbf\x91\xf9\xdd\x9f\x9a\xd4\x0b"
decrypted3 = dec.decode('base64')
decrypted2 = tsu_super_decrypt3(decrypted3)
decrypted1 = tsu_super_decrypt2(decrypted2)
#decrypted0 = tsu_super_decrypt1(decrypted1, key)
#plaintext = tsu_super_decrypt0(decrypted0)

print decrypted1.encode('hex')
#print decrypted0.encode('hex')
#print plaintext
