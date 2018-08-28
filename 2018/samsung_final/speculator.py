import struct

table = [0x0C, 0x02, 0x07, 0x01, 0x0F, 0x0E, 0x03, 0x0A, 0x00, 0x06, 0x0D, 0x0B, 0x05, 0x08, 0x04, 0x09]
target = [0x14A96D3B, 0x75DC293F, 0x3756F67D, 0xB352EF12, 0x92433E07, 0x3FB5912B, 0x41B1541C, 0x9EA1289F]
flag = ''

def enc(inp):
	for i in range(8):
		l = []
		_sum = 0
		for j in range(4):
			l.append(table[(inp >> (j * 4)) & 0xf])
		for j in range(4):
			_sum += l[j] << (j * 4)
		_sum = ((_sum << 3) | (_sum >> 0xd)) & 0xffff
		_sum ^= (inp >> 16)
		inp = ((inp & 0xffff) << 16) | _sum
		print hex(inp)
	return inp

def dec(inp):
	for i in range(8):
		l = []
		_sum = 0
		for j in range(4):
			l.append(table[((inp >> 16) >> (j * 4)) & 0xf])
		for j in range(4):
			_sum += l[j] << (j * 4)
		_sum = ((_sum << 3) | (_sum >> 0xd)) & 0xffff
		inp = (inp >> 16) | ((_sum ^ (inp & 0xffff)) << 16)
	return inp

for i in target:
	flag += struct.pack(">L", dec(i))
print flag
