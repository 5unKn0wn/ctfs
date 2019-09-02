import struct

rol = lambda val, r_bits, max_bits: \
	(val << r_bits%max_bits) & (2**max_bits-1) | \
	((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
 
# Rotate right: 0b1001 --> 0b1100
ror = lambda val, r_bits, max_bits: \
	((val & (2**max_bits-1)) >> r_bits%max_bits) | \
	(val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

def encrypt(plain, ks):
	if len(plain) % 8 != 0:
		plain += "\x00" * (8 - (len(plain) % 8))
	plain = list(struct.unpack(">LL", plain))
	a = (plain[0] + ks[0]) & 2**32-1
	b = (plain[1] + ks[1]) & 2**32-1
	for i in range(24):
		prev_b = b
		b = (ks[i + 2] + rol(a ^ b, b & 0x1f, 32)) & 2**32-1
		a = prev_b
	return (struct.pack(">L", a) + struct.pack(">L", b)).encode('hex')

def decrypt(cipher, ks):
	cipher = struct.unpack(">LL", cipher.decode('hex'))
	a = cipher[0]
	b = cipher[1]
	for i in range(23, -1, -1):
		prev_a = a
		a = ror(b - ks[i + 2], a & 0x1f, 32) ^ a
		b = prev_a
	a = (a - ks[0]) & 2**32-1
	b = (b - ks[1]) & 2**32-1
	return (struct.pack(">L", a) + struct.pack(">L", b)).rstrip('\x00')

# key stream from ida
ks1 = [0x83f19eeeL, 0xda45ed22L, 0xf746d84L, 0x5956ab6dL, 0x8917c0efL, 0x7a5cf3b6L, 0x796712ddL, 0x6009fb1fL, 0x6a5bc569L, 0x376c57d3L, 0xe9ba0d38L, 0xbe82e078L, 0x77856cc1L, 0xa273cfeeL, 0xd4142c83L, 0x17374a6L, 0xa3aeae68L, 0x2b52304L, 0xe3d4b9eL, 0x1eb080bfL, 0x30a8374bL, 0x84f10f0fL, 0x2823509L, 0xd0dabfabL, 0xc85353c6L, 0x768e268eL, 0xcdd1b42L, 0xddf3d584L, 0xfbdba0d4L, 0xa15d7381L, 0x83f4a3f6L, 0xd4eac3eaL]
ks2 = [0xa8780381L, 0xd325b893L, 0x2889f25fL, 0x93c9281L, 0xca31370L, 0xf01abbbeL, 0x69b1eebL, 0x335b65cdL, 0xdba0f812L, 0x26641f2eL, 0xcdcd48e0L, 0x2ffb8009L, 0x75077d6dL, 0x8f23624aL, 0x71c8f20aL, 0xe254b801L, 0x443ba936L, 0x6f4f4a2fL, 0x8aba595fL, 0x9a8530a6L, 0xc42a5a0eL, 0x9ad8308dL, 0x42628dbdL, 0xabab10deL, 0x9f95660eL, 0xae0ee93cL, 0x9e704772L, 0x9e0fe2c0L, 0x53e83f2bL, 0x37dd53c7L, 0xdfa1fe01L, 0x4fbed0dL]
ks3 = [0x77354950L, 0x113b306dL, 0x3f8a1235L, 0xe3af6ed1L, 0xf54cd1e9L, 0x9efb71e8L, 0x298d44baL, 0x8f672270L, 0xe9a97023L, 0x7100d45bL, 0x8f2a5e4L, 0xee09e4a5L, 0xc6539fc7L, 0xc8538753L, 0xf59e1b4bL, 0xd268290eL, 0x76f1d203L, 0x9917e9b2L, 0x908a32d4L, 0xe8d20101L, 0x6092f88eL, 0x84fc73ecL, 0xcbd92758L, 0x44a66424L, 0x82779517L, 0xec39befeL, 0xd9fe6b2dL, 0x2520232cL, 0xdda34a8dL, 0x1e5fe69aL, 0xd99e98baL, 0x66aa19e2L]
ks4 = [0x105426f8L, 0x2945d55fL, 0x5a6ec101L, 0x3c60fc75L, 0xbc365fa3L, 0x5576699cL, 0x99548715L, 0x1c08bd1fL, 0xd5375697L, 0x1f16fc4cL, 0x541be791L, 0x169314ffL, 0xddbfc2dbL, 0x9c131e7fL, 0xec9b6a6eL, 0x19700898L, 0x630bc067L, 0x5154dfc8L, 0x739a5761L, 0x9ebce304L, 0x6d8f9d46L, 0x369056a4L, 0x5bc4e09eL, 0xa139bbe8L, 0x93023d62L, 0xe5979177L, 0x73911ea2L, 0xed9a6998L, 0x6aad6804L, 0xc6ec99aaL, 0xaf8f109cL, 0x81793378L]
ks5 = [0x6e15b6edL, 0xf259349eL, 0xfed4fdd8L, 0x759a482bL, 0x4b150fd6L, 0xd42698f1L, 0x85d88ce1L, 0x253796eeL, 0x941af694L, 0x997b347L, 0xcdb22ebbL, 0x365ef56cL, 0x458f3e90L, 0xa1c536c3L, 0xe1284dL, 0x5f557b37L, 0xadf6dff8L, 0x6260a096L, 0x3db81ff5L, 0x7a8e070aL, 0x7a0609faL, 0x9e6ded19L, 0x377743d5L, 0x8ead5a5bL, 0x69bf4721L, 0x4ea93a4L, 0xc2c34e47L, 0xee0b5f03L, 0x9a03038aL, 0xde6ba695L, 0xc7997ad9L, 0xc195d2dL]

dat = "d4f5f0aa8aeee7c83cd8c039fabdee6247d0f5f36edeb24ff9d5bc10a1bd16c12699d29f54659267"
enc1 = dat[:16]
enc2 = dat[16:32]
enc3 = dat[32:48]
enc4 = dat[48:64]
enc5 = dat[64:]

print decrypt(enc1, ks1) + decrypt(enc2, ks2) + decrypt(enc3, ks3) + decrypt(enc4, ks4) + decrypt(enc5, ks5)