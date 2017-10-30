import math

def encrypt(plain, urandom1, urandom2, cnt):
	inp_arr = []
	enc = ''

	idx = 0
	for i in range(cnt):
		tmp1 = []
		for j in range(cnt):
			tmp2 = []
			for k in range(cnt):
				tmp2.append(ord(plain[idx]))
				idx += 1
			tmp1.append(tmp2)
		inp_arr.append(tmp1)

	idx = 0
	for i in range(cnt):
		for j in range(cnt):
			for k in range(cnt):
				inp_arr[i][j][k] = (inp_arr[i][j][k] + ord(urandom1[idx % 8])) & 0xff
				idx += 1

	for i in range(32):
		rotate_arr = []
		urandom_byte = ord(urandom2[i])
		idx = (urandom_byte >> 2) % cnt
		if urandom_byte & 1:
			for j in range(cnt):
				tmp1 = []
				for k in range(cnt):
					tmp1.append(inp_arr[j][idx][k])
				rotate_arr.append(tmp1)
			if urandom_byte & 2:
				for j in range(cnt):
					for k in range(cnt):
						inp_arr[k][idx][cnt - j - 1] = rotate_arr[j][k]
			else:
				for j in range(cnt):
					for k in range(cnt):
						inp_arr[cnt - k - 1][idx][j] = rotate_arr[j][k]
		else:
			for j in range(cnt):
				tmp1 = []
				for k in range(cnt):
					tmp1.append(inp_arr[j][k][idx])
				rotate_arr.append(tmp1)
			if urandom_byte & 2:
				for j in range(cnt):
					for k in range(cnt):
						inp_arr[cnt - k - 1][j][idx] = rotate_arr[j][k]
			else:
				for j in range(cnt):
					for k in range(cnt):
						inp_arr[k][cnt - j - 1][idx] = rotate_arr[j][k]

	for i in range(cnt):
		for j in range(cnt):
			for k in range(cnt):
				enc += chr(inp_arr[i][j][k])

	return enc



def decrypt(encrypted, urandom1, urandom2, cnt):
	urandom2 = urandom2[::-1]
	inp_arr = []
	dec = ''

	idx = 0
	for i in range(cnt):
		tmp1 = []
		for j in range(cnt):
			tmp2 = []
			for k in range(cnt):
				tmp2.append(ord(encrypted[idx]))
				idx += 1
			tmp1.append(tmp2)
		inp_arr.append(tmp1)

	for i in range(32):
		rotate_arr = []
		urandom_byte = ord(urandom2[i])
		idx = (urandom_byte >> 2) % cnt
		if urandom_byte & 1:
			for j in range(cnt):
				tmp1 = []
				for k in range(cnt):
					tmp1.append(inp_arr[j][idx][k])
				rotate_arr.append(tmp1)
			if urandom_byte & 2:
				for j in range(cnt):
					for k in range(cnt):
						inp_arr[cnt - k - 1][idx][j] = rotate_arr[j][k]
						
			else:
				for j in range(cnt):
					for k in range(cnt):
						inp_arr[k][idx][cnt - j - 1] = rotate_arr[j][k]
		else:
			for j in range(cnt):
				tmp1 = []
				for k in range(cnt):
					tmp1.append(inp_arr[j][k][idx])
				rotate_arr.append(tmp1)
			if urandom_byte & 2:
				for j in range(cnt):
					for k in range(cnt):
						inp_arr[k][cnt - j - 1][idx] = rotate_arr[j][k]
			else:
				for j in range(cnt):
					for k in range(cnt):
						inp_arr[cnt - k - 1][j][idx] = rotate_arr[j][k]

	idx = 0
	for i in range(cnt):
		for j in range(cnt):
			for k in range(cnt):
				inp_arr[i][j][k] = (inp_arr[i][j][k] - ord(urandom1[idx % 8])) & 0xff
				idx += 1

	for i in range(cnt):
		for j in range(cnt):
			for k in range(cnt):
				dec += chr(inp_arr[i][j][k])

	return dec


enc = open("flag.enc.docx", "rb").read()

urandom1 = enc[:8]
urandom2 = enc[8:40]
enc = enc[40:]
cnt = 0x18

dec = decrypt(enc, urandom1, urandom2, cnt)

open("flag.docx", "wb").write(dec)


