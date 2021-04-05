from Crypto.Hash import HMAC, SHA256
import struct
 
p32 = lambda x: struct.pack("<L", x)
 
key = b'SECRET_KEYXD'
pt = b"\xd3\x84\x1a\xb0\xc2\x8f\xdd\xd5\x00\x8f\xf9\x04\xc9\xdaUO\x92r\xf1\x98\x08\xdcU\x9e\xe8}f\xdf\xda\xd1!\x95\xb3\x1b\x95\xa1\x97B\xf0\x89%\x862\t\xca\xe6\x13/;\xaa2\xa7a\xa4\tx4\xe8\x8d\xb0%\x9f\xe1\xe9f\xb6\x9e\x1c\xd5\xb7Ti\xe4\xad]\xd9\xac\x18&\xdd\xa9'S\x0b\xf6<A\xd1n?Em\xee\xd2NX\x90\xaf\x1c\xf2\xa9\xc7\x9d\x90}z\xe9\xe9\xa0\x0c\xa2H\x9e\xf3\xf9Va\xf2m\xb3\x94\xfc\x08AT\x05\x9d5\xffa#_\xfa\xe8\xd0\xf8\xd4Q\xcb\xe8\xb3\xfc\n\x9cca\x1b\xb0\x07;\x19\xcd\x0c\x180p\xd6h\xa3\nBH\xccEl7\xdc!84>\xdd\x12=\xe2P\x03Q\x16\xec\x81\x16\xf0\xc8\x00q+\x98\\\xb2\n\x9e\x1e\x0fC\xbdiR\xcb(\xa8\xb5b\xfbLL\x18\x8aL\xc3\x96\xbe\xab>\x056\xfe\x8ejU@?\\\x94\xf6d\x1f?6\xe0l\x9b!\x92o\x83PO^\xb5\x0e\xd4\xb2xh7Q\xddm.\x80YH\xde\xb6\x91"
usage = 4
data = p32(usage) + pt
h = HMAC.new(key, digestmod=SHA256)
h.update(data)
print(f"LINECTF{{{h.hexdigest()}}}")
