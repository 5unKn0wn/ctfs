import ctypes

arr = [1323740511, 6312588704]
libc = ctypes.CDLL("libc.so.6")
time = 1551401676
for z in range(1000000*20, 1000000*30):
	libc.srand(time - z)

	key = range(10)
	for i in range(9, 0, -1):
		r = libc.rand()
		key[i], key[r % (i + 1)] = key[r % (i + 1)], key[i]

	s = bytearray(str(arr[0]).rjust(10, '0'))
	res = bytearray('\x00' * 10)
	for i in range(10):
		res[key[i]] = s[i]

	if int(res) & 0xffffffff == 0x89504E47:
		for i in range(9, 0, -1):
			r = libc.rand()
			key[i], key[r % (i + 1)] = key[r % (i + 1)], key[i]

		s = bytearray(str(arr[1]).rjust(10, '0'))
		res = bytearray('\x00' * 10)
		for i in range(10):
			res[key[i]] = s[i]
			
		if int(res) & 0xffffffff == 0x0D0A1A0A:
			print hex(time - z)
			break
