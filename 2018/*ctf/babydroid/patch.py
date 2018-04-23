import struct

with open("libb.so", "rb") as f:
	libb = bytearray(f.read())

enc = libb[0xab8:0xed8]
key = 0x6674632a

for i in range(0, len(enc), 4):
	ori = struct.unpack("<L", enc[i:i+4])[0]
	ori ^= key
	enc[i] = ori & 0xff
	enc[i + 1] = (ori >> 8) & 0xff
	enc[i + 2] = (ori >> 16) & 0xff
	enc[i + 3] = (ori >> 24) & 0xff

for i in range(0x27c, len(enc), 4):
	enc[i], enc[i + 2] = enc[i + 2], enc[i]
	enc[i + 1], enc[i + 3] = enc[i + 3], enc[i + 1]
	ori = struct.unpack("<L", enc[i:i+4])[0]
	ori ^= key
	enc[i] = ori & 0xff
	enc[i + 1] = (ori >> 8) & 0xff
	enc[i + 2] = (ori >> 16) & 0xff
	enc[i + 3] = (ori >> 24) & 0xff

for i in range(len(enc)):
	libb[0xab8 + i] = enc[i]

with open("libb_patched.so", "wb") as f:
	f.write(libb)
