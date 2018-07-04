enc = 'T10yCi0If1dOCioWdWtLDzl4D0J9QjxfHmMOcw=='.decode('base64')
flag = ''

for i in range(0, len(enc), 7):
	arr = [0 for a in range(7)]
	for j in range(7):
		for k in range(7):
			arr[k] |= ((ord(enc[i + j]) >> k) & 1) << j
	flag += chr(arr[0])
	arr.pop(0)
	arr = arr[::-1]
	flag += ''.join(chr(a) for a in arr)
print flag
