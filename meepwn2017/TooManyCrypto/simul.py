from hashlib import md5

def tsu_super_encrypt0(c):
	return c.encode('zlib')

def tsu_super_encrypt1(c, key):
	l = len(key)
	string = ""
	for i in range(len(c)):
		# string += chr((ord(c[i]) | ord(key[i % l])) & (256 + ~(ord(c[i]) & ord(key[i % l]))) % 256)
		string += chr(ord(c[i]) ^ ord(key[i % l]))
	return string

def tsu_super_encrypt2(c):
	l = len(c)
	string = ""
	for i in range(l):
		string += chr((ord(c[i]) + i) % 256)
	return string

def tsu_super_encrypt3(c):
	l = len(c)
	k = l % 8
	string = ""
	for i in range(l):
		string += chr(((ord(c[i]) << k) | ord(c[i]) >> (8 - k)) & 0xff)
	return string

enc = "testtest"
flag = "salt"
query = "secret=" + flag + "string=" + enc
key = "\xbf\x91????"
encrypted0 = tsu_super_encrypt0(query)
print encrypted0.encode('hex')
encrypted1 = tsu_super_encrypt1(encrypted0, key)
print encrypted1.encode('hex')
encrypted2 = tsu_super_encrypt2(encrypted1)
encrypted3 = tsu_super_encrypt3(encrypted2)
print encrypted3.encode('base64').replace('\n', '')
