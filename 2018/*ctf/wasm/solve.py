import struct

enc = [[0x2f6c8735, 0x997702bd], [0xf6482c8c, 0x5522791d], [0xcbd831e3, 0xb9d61393]]
table = [0x61626577, 0x6e696d73, 0x73726574, 0x676e6974]
flag = ''

for i in range(len(enc)):
	sum_value, key = 0xc6ef3720, 0x9e3779b9
	for j in range(32):
		enc[i][1] = (enc[i][1] - ((((enc[i][0] << 3) ^ table[2]) ^ (enc[i][0] + sum_value)) ^ ((enc[i][0] >> 5) + table[3]))) & 0xffffffff
		enc[i][0] = (enc[i][0] - ((((enc[i][1] << 3) ^ table[0]) ^ (enc[i][1] + sum_value)) ^ ((enc[i][1] >> 5) + table[1]))) & 0xffffffff
		sum_value = (sum_value - key) & 0xffffffff
	for j in range(2):
		flag += struct.pack("<L", enc[i][j])

print flag
