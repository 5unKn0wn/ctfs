def find_key(dat, known_length, table):
	known = [0x55, 0x48, 0x89, 0xe5, 0x48, 0x83, 0xec]
	known_24 = [0xff, 0xc9, 0xc3]
	known_5 = [0xff, 0xff, 0xc9]
	stage5 = 0
	if known_length == 11:
		known2 = known_5
		known_length = 10
		stage5 = 1
	else:
		known2 = known_24
	for i in range(7):
		idx = table.index(chr(dat[i] ^ known[i]))
		if idx + 0x47 <= 96:
			key[i] = idx + 0x41
		elif idx + 0x41 > 96:
			key[i] = idx + 0x47
		else:
			c1 = idx + 0x41
			c2 = idx + 0x47
			if chr(c1) in alphanum and chr(c2) not in alphanum:
				key[i] = c1
			elif chr(c2) in alphanum and chr(c1) not in alphanum:
				key[i] = c2
			else:
				print "retry"
				exit(0)
	for i in range(7, 10):
		print dat[-(10 - i - stage5)]
		idx = table.index(chr(dat[-(10 - i + stage5)] ^ known2[i - 7]))
		if idx + 0x47 <= 96:
			key[i] = idx + 0x41
		elif idx + 0x41 > 96:
			key[i] = idx + 0x47
		else:
			c1 = idx + 0x41
			c2 = idx + 0x47
			if chr(c1) in alphanum and chr(c2) not in alphanum:
				key[i] = c1
			elif chr(c2) in alphanum and chr(c1) not in alphanum:
				key[i] = c2
			else:
				print "retry"
				exit(0)
	return key

def PatchBytes(ea, dat):
	for n, c in enumerate(dat):
		PatchByte(ea + n, c)

def decrypt(ea, length, key, table):
	dat = bytearray(idaapi.get_many_bytes(ea, length))
	key = bytearray(key)
	table = bytearray(table)
	for i in range(length):
		if key[i % len(key)] > 96:
			dat[i] ^= table[key[i % len(key)] - 0x47]
		else:
			dat[i] ^= table[key[i % len(key)] - 0x41]
	PatchBytes(ea, dat)

lengths = [240L, 80L, 80L, 230L, 240L, 89L, 79L, 220L, 230L, 230L, 230L, 223L, 30L, 30L, 245L, 245L, 30L, 183L, 276L, 240L, 230L, 240L, 49L, 241L, 240L, 277L, 353L, 306L, 230L, 216L, 250L, 563L, 30L, 276L, 276L, 260L, 240L, 30L, 240L, 290L, 270L, 276L, 221L, 512L, 229L, 198L]
decrypt(0x40329C, 0xf0, 'bZke', 'ETGUwpvlsIZkoQcYdqOhMfySgarRAbXueDPnBmFzCtxjWJNLVKHi')
