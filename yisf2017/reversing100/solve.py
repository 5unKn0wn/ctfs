with open("encoded_file.yisf", "rt") as f:
	data = map(int, f.read().split(','))
list_length = 5
length = len(data) / list_length
data = [data[i:i + length] for i in range(0, len(data), length)]
table = [1, 6, 2] + [0, 4, 2] * 20
dec = []

for i in range(2):
	for j in range(length - 1, -1, -1):
		tmp = data[list_length - i - 1][j] + 10
		data[list_length - i - 1][j] = (data[i][length - j - 1] ^ tmp) & 0xff
		data[i][length - j - 1] = tmp & 0xff

for i in data:
	dec.append(''.join(chr(j) for j in i))

dec = dec[1]
flag = ''.join(chr(ord(dec[i]) ^ table[i]) for i in range(len(dec)))

print flag
