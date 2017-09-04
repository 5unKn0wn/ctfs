import struct

with open('table', 'rb') as f:
	table = map(ord, f.read())

with open('cryptal', 'rb') as f:
	binary = map(ord, f.read())

with open('flag.png.enc', 'rb') as f:
	enc_flag = f.read()

p32 = lambda x : struct.pack("<L", x)
u32 = lambda x : struct.unpack("<L", x)[0]

def encrypt(inp, inp_len):
	inp = inp.ljust(len(inp) + ((4 - (len(inp) % 4)) % 4), '\x00')
	length = inp_len * 8
	for i in range(0x20):
		inp = [u32(i) for i in map(''.join, zip(*[iter(str(inp))] * 4))] # string to int list ("\x11\x22\x33\x44\x55\x66\x77\x88" --> [0x44332211, 0x88776655])
		bin_idx = 0
		table_idx = 0
		
		for j in range(length):
			mul = binary[bin_idx % len(binary)] * table[table_idx % len(table)]
			if (j % 2) == 1:
				mod = (mul + j) % length
				inp[j / 0x20] ^= (1 << (j % 0x20))
				bit1 = (inp[mod / 0x20] & (1 << (mod % 0x20))) == (1 << (mod % 0x20))
				bit2 = (inp[j / 0x20] & (1 << (j % 0x20))) == (1 << (j % 0x20))
				if bit2:
					inp[mod / 0x20] |= (1 << (mod % 0x20))
				else:
					inp[mod / 0x20] &= ~(1 << (mod % 0x20))
				if bit1:
					inp[j / 0x20] |= (1 << (j % 0x20))
				else:
					inp[j / 0x20] &= ~(1 << (j % 0x20))
			else:
				mod = j - mul
				if mod < 0:
					mod = length - (-mod % length)
				if mod > length - 1:
					mod = -mod % length
				inp[(j / 0x20)] ^= (1 << (j % 0x20))
				bit1 = (inp[mod / 0x20] & (1 << (mod % 0x20))) == (1 << (mod % 0x20))
				bit2 = (inp[j / 0x20] & (1 << (j % 0x20))) == (1 << (j % 0x20))
				if bit2:
					inp[mod / 0x20] |= (1 << (mod % 0x20))
				else:
					inp[mod / 0x20] &= ~(1 << (mod % 0x20))
				if bit1:
					inp[j / 0x20] |= (1 << (j % 0x20))
				else:
					inp[j / 0x20] &= ~(1 << (j % 0x20))
			bin_idx += 1
			table_idx += 1

		inp = bytearray(''.join(p32(i) for i in inp)) # int list to string ([0x44332211, 0x88776655] --> "\x11\x22\x33\x44\x55\x66\x77\x88")
		bin_idx = 0
		table_idx = 0

		for j in range(inp_len):
			mul = binary[bin_idx % len(binary)] * table[table_idx % len(table_idx)]
			if (j % 2) == 1:
				mod = (mul + j) % inp_len
				inp[mod], inp[j] = inp[j], inp[mod]
			else:
				mod = j - mul
				if mod < 0:
					mod = inp_len - (-mod % inp_len)
				if mod > inp_len - 1:
					mod = -mod % inp_len
				inp[mod], inp[j] = inp[j], inp[mod]
			bin_idx += 1
			table_idx += 1
	return str(inp).rstrip('\x00')

def decrypt(enc, enc_len):
	enc = bytearray(enc)
	length = enc_len * 8
	for i in range(0x20):
		bin_idx = enc_len - 1
		table_idx = enc_len - 1
		for j in range(enc_len - 1, -1, -1):
			mul = binary[bin_idx % len(binary)] * table[table_idx % len(table)]
			if (j % 2) == 1:
				mod = (mul + j) % enc_len
				enc[mod], enc[j] = enc[j], enc[mod]
			else:
				mod = j - mul
				if mod < 0:
					mod = enc_len - (-mod % enc_len)
				if mod > enc_len - 1:
					mod = -mod % enc_len
				enc[mod], enc[j] = enc[j], enc[mod]
			bin_idx -= 1
			table_idx -= 1
		enc = enc.ljust(len(enc) + ((4 - (len(enc) % 4)) % 4), '\x00')
		enc = [u32(i) for i in map(''.join, zip(*[iter(str(enc))] * 4))]
		bin_idx = length - 1
		table_idx = length - 1
		for j in range(length - 1, -1, -1):
			mul = binary[bin_idx % len(binary)] * table[table_idx % len(table)]
			if (j % 2) == 1:
				mod = (mul + j) % length
				bit1 = (enc[mod / 0x20] & (1 << (mod % 0x20))) == (1 << (mod % 0x20))
				bit2 = (enc[j / 0x20] & (1 << (j % 0x20))) == (1 << (j % 0x20))
				if bit1 != bit2:
					if bit1:
						enc[mod / 0x20] &= ~(1 << (mod % 0x20))
						enc[j / 0x20] |= (1 << (j % 0x20))
					else:
						enc[j / 0x20] &= ~(1 << (j % 0x20))
						enc[mod / 0x20] |= (1 << (mod % 0x20))
				enc[j / 0x20] ^= (1 << (j % 0x20))
			else:
				mod = j - mul
				if mod < 0:
					mod = length - (-mod % length)
				if mod > length - 1:
					mod = -mod % length
				bit1 = (enc[mod / 0x20] & (1 << (mod % 0x20))) == (1 << (mod % 0x20))
				bit2 = (enc[j / 0x20] & (1 << (j % 0x20))) == (1 << (j % 0x20))
				if bit1 != bit2:
					if bit1:
						enc[mod / 0x20] &= ~(1 << (mod % 0x20))
						enc[j / 0x20] |= (1 << (j % 0x20))
					else:
						enc[j / 0x20] &= ~(1 << (j % 0x20))
						enc[mod / 0x20] |= (1 << (mod % 0x20))
				enc[(j / 0x20)] ^= (1 << (j % 0x20))
			bin_idx -= 1
			table_idx -= 1
		enc = bytearray(''.join(p32(i) for i in enc))
	return str(enc).rstrip('\x00')

flag = decrypt(enc_flag, len(enc_flag))
with open('flag.png', 'wb') as f:
	f.write(flag)
