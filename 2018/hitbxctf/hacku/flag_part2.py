rol = lambda val, r_bits, max_bits: \
	(val << r_bits%max_bits) & (2**max_bits-1) | \
	((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

ror = lambda val, r_bits, max_bits: \
	((val & (2**max_bits-1)) >> r_bits%max_bits) | \
	(val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

enc = [37, 161, 57, 137, 166, 157, 213, 165, 117, 141, 74, 146, 241, 89, 94, 145]

flag = ''
for c in enc:
	c -= 1
	if c % 2 == 0:
		c += 2
	c -= 0x47
	c = ror(c, 5, 8)
	c ^= 0x74
	c = rol(c, 3, 8)
	flag += chr(c)

print flag
