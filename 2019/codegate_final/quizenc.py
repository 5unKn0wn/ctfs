from pwn import *

def dec1(dat_list, ans_list, chall):
	idx_list = []
	for dat, ans in zip(dat_list, ans_list):
		arr = [int(i) for i in dat]
		arr.sort()
		l = []
		for i in range(10):
			if arr.count(i) == ans:
				l.append(i)
		idx_list.append(l)
	res = list(set(idx_list[0]) & set(idx_list[1]) & set(idx_list[2]))
	if len(res) != 1:
		print "error dec1, retry"
		exit()
	arr = [int(i) for i in chall]
	arr.sort()
	return arr.count(res[0])

def dec2(dat_list, ans_list, chall):
	idx_list = []
	for dat, ans in zip(dat_list, ans_list):
		arr = [i for i in dat]
		arr.sort()
		chr_list = list(set(arr))
		l = []
		for i in range(10):
			if arr.count(chr_list[i]) == ans:
				l.append(chr_list[i])
		idx_list.append(l)
	res = list(set(idx_list[0]) & set(idx_list[1]) & set(idx_list[2]))
	if len(res) != 1:
		print "error dec2, retry"
		exit()
	arr = [i for i in chall]
	arr.sort()
	return arr.count(res[0])

def dec3(dat_list, ans_list, chall):
	gaps = []
	for dat, ans in zip(dat_list, ans_list):
		arr = [int(i) for i in dat]
		gap = []
		for i in range(10):
			gap.append(arr.index(i, arr.index(i) + 1) - arr.index(i) - 1)
		gaps.append(gap)
	for i in range(10):
		if gaps[0][i] == ans_list[0] and gaps[1][i] == ans_list[1] and gaps[2][i] == ans_list[2]:
			res = i
			break
	arr = [int(i) for i in chall]
	gap = []
	for i in range(10):
		gap.append(arr.index(i, arr.index(i) + 1) - arr.index(i) - 1)
	return gap[res]

def dec4(dat_list, ans_list, chall):
	gaps = []
	for dat, ans in zip(dat_list, ans_list):
		arr = [i for i in dat]
		gap = []
		l = list(set(arr))
		l.sort()
		for i in l:
			gap.append(arr.index(i, arr.index(i) + 1) - arr.index(i) - 1)
		gaps.append(gap)
	for i in range(10):
		if gaps[0][i] == ans_list[0] and gaps[1][i] == ans_list[1] and gaps[2][i] == ans_list[2]:
			res = i
			break
	arr = [i for i in chall]
	gap = []
	for i in l:
		gap.append(arr.index(i, arr.index(i) + 1) - arr.index(i) - 1)
	return gap[res]

def enc5(n0, n1, n2, n3):
        return (n1 + n2 + 100 * (n0 + n3)) % 256

def enc6(n0, n1, n2, n3):
        return ((10 * n0 + n1) + (10 * n2 + n3)) % 256

def enc7(n0, n1, n2, n3):
        return (pow(n0, n1) + pow(n2, n3)) % 256

def detecting_chall(chall):
	if len(chall) == 20 and chall[0] in "0123456789":
		return "dec3"
	elif len(chall) == 20 and chall[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
		return "dec4"
	elif chall[0] in "0123456789":
		return "dec1"
	else:
		return "dec2"

r = remote("110.10.147.112", 50415)

quizs, anses, challs = [], [], []
r.recvuntil("1. QUIZs\n")
for i in range(4):
	r.recvuntil("------------------------------------------------------------------------------------------\n")
	quiz, ans = [], []
	for j in range(3):
		r.recvuntil("    [EX %d] " % (j + 1))
		quiz.append(r.recvuntil(" = ", drop=True))
		ans.append(int(r.recvuntil("\n", drop=True)))
	quizs.append(quiz)
	anses.append(ans)
	r.recvuntil("    [QUIZ] ")
	challs.append(r.recvuntil(" = ", drop=True))

quiz_ans = []
for i in range(4):
	which_enc = detecting_chall(challs[i])
	if which_enc == "dec1":
		res = dec1(quizs[i], anses[i], challs[i])
	elif which_enc == "dec2":
		res = dec2(quizs[i], anses[i], challs[i])
	elif which_enc == "dec3":
		res = dec3(quizs[i], anses[i], challs[i])
	else:
		res = dec4(quizs[i], anses[i], challs[i])
	quiz_ans.append(res)

for i in range(16):
	r.recvuntil("------------------------------------------------------------------------------------------\n")
	quiz, ans, chall = [], [], []
	for j in range(3):
		r.recvuntil("    [EX %d] " % (j + 1))
		quiz.append(int(r.recv(1)))
		quiz.append(int(r.recv(1)))
		r.recvuntil(" ツ ")
		quiz.append(int(r.recv(1)))
		quiz.append(int(r.recv(1)))
		r.recvuntil(" = ")
		ans.append(int(r.recvuntil("\n", drop=True)))
	r.recvuntil("    [QUIZ] ")
	chall.append(int(r.recv(1)))
	chall.append(int(r.recv(1)))
	r.recvuntil(" ツ ")
	chall.append(int(r.recv(1)))
	chall.append(int(r.recv(1)))
	r.recvuntil(" = ")

	if enc5(quiz[0], quiz[1], quiz[2], quiz[3]) == ans[0]:
		quiz_ans.append(enc5(chall[0], chall[1], chall[2], chall[3]))
	elif enc6(quiz[0], quiz[1], quiz[2], quiz[3]) == ans[0]:
		quiz_ans.append(enc6(chall[0], chall[1], chall[2], chall[3]))
	elif enc7(quiz[0], quiz[1], quiz[2], quiz[3]) == ans[0]:
		quiz_ans.append(enc7(chall[0], chall[1], chall[2], chall[3]))
	else:
		print "??????????"
		exit(0)

print quiz_ans

r.recvuntil("2. ENC\n    ------------------------------------------------------------------------------------------\n")
enc = r.recvuntil("    ------------------------------------------------------------------------------------------", drop=True)
enc = bytearray(enc.replace("    ", "").replace("\n", "").decode('hex'))

sbox1 = [23L, 0L, 20L, 11L, 5L, 12L, 3L, 29L, 35L, 2L, 37L, 32L, 31L, 26L, 28L, 22L, 19L, 14L, 1L, 27L, 8L, 13L, 25L, 33L, 6L, 34L, 10L, 4L, 30L, 18L, 17L, 21L, 7L, 15L, 16L, 9L, 24L, 38L, 36L]
sbox2 = [46L, 27L, 41L, 14L, 24L, 8L, 1L, 0L, 34L, 36L, 48L, 6L, 16L, 43L, 47L, 26L, 25L, 32L, 4L, 33L, 30L, 18L, 51L, 3L, 2L, 21L, 44L, 7L, 40L, 29L, 37L, 20L, 15L, 11L, 35L, 31L, 5L, 13L, 28L, 12L, 50L, 45L, 39L, 9L, 49L, 42L, 17L, 10L, 23L, 19L, 38L, 22L]
sbox3 = [28L, 55L, 5L, 59L, 36L, 42L, 16L, 62L, 4L, 0L, 26L, 44L, 32L, 58L, 19L, 6L, 46L, 15L, 35L, 33L, 57L, 43L, 38L, 52L, 63L, 60L, 3L, 13L, 27L, 24L, 37L, 48L, 31L, 21L, 29L, 10L, 64L, 49L, 17L, 18L, 53L, 30L, 9L, 50L, 40L, 1L, 20L, 56L, 54L, 8L, 61L, 23L, 14L, 51L, 47L, 22L, 34L, 45L, 7L, 39L, 41L, 12L, 2L, 25L, 11L]
inverse_sbox1 = [0 for i in range(len(sbox1))]
for i in range(len(sbox1)):
	inverse_sbox1[sbox1[i]] = i
inverse_sbox2 = [0 for i in range(len(sbox2))]
for i in range(len(sbox2)):
	inverse_sbox2[sbox2[i]] = i
inverse_sbox3 = [0 for i in range(len(sbox3))]
for i in range(len(sbox3)):
	inverse_sbox3[sbox3[i]] = i

cur_table = []
length = len(enc)
if length % 39 <= 19:
	cur_table = inverse_sbox1
elif length % 52 <= 19:
	cur_table = inverse_sbox2
else:
	cur_table = inverse_sbox3
align = len(cur_table)
res = list(enc)[:]
for i in range(0, length - (length % align), align):
	for j in range(align):
		res[i + j] = enc[cur_table[j] + i]

rem_length = length % 10
quiz1_ans = quiz_ans[0]
_10_m_quiz1_ans = 10 - quiz1_ans
last = False
for i in range(0, length, 10):
	if length - i == rem_length:
		if rem_length >= quiz1_ans:
			_10_m_quiz1_ans = rem_length - quiz1_ans
		else:
			last = True
	if last == False:
		xor_len = quiz1_ans + _10_m_quiz1_ans
	else:
		xor_len = rem_length
	for j in range(xor_len):
		res[i + j] ^= quiz_ans[4 + j]
	if i % 20 == 10 and last == False:
		enc = res[:]
		for j in range(quiz1_ans):
			res[i + j] = enc[_10_m_quiz1_ans + i + j]
		for j in range(_10_m_quiz1_ans):
			res[quiz1_ans + i + j] = enc[i + j]

sbox = [122L, 153L, 58L, 119L, 178L, 128L, 39L, 64L, 94L, 28L, 180L, 177L, 120L, 85L, 154L, 49L, 121L, 191L, 99L, 220L, 102L, 217L, 36L, 189L, 136L, 158L, 83L, 143L, 71L, 59L, 46L, 246L, 92L, 26L, 117L, 43L, 254L, 199L, 107L, 171L, 66L, 57L, 245L, 163L, 223L, 13L, 101L, 23L, 208L, 239L, 135L, 227L, 222L, 65L, 52L, 173L, 211L, 183L, 166L, 44L, 18L, 159L, 72L, 161L, 200L, 226L, 47L, 149L, 112L, 228L, 42L, 248L, 86L, 40L, 134L, 236L, 93L, 224L, 6L, 186L, 51L, 213L, 156L, 172L, 130L, 9L, 104L, 76L, 31L, 109L, 152L, 111L, 123L, 79L, 193L, 56L, 132L, 14L, 35L, 174L, 253L, 19L, 70L, 82L, 95L, 201L, 17L, 87L, 137L, 250L, 29L, 2L, 67L, 21L, 204L, 89L, 229L, 241L, 167L, 168L, 98L, 74L, 96L, 188L, 202L, 75L, 118L, 125L, 80L, 140L, 12L, 142L, 103L, 60L, 231L, 212L, 84L, 15L, 113L, 157L, 164L, 190L, 114L, 115L, 244L, 184L, 148L, 150L, 0L, 155L, 242L, 237L, 187L, 131L, 78L, 209L, 20L, 10L, 88L, 7L, 195L, 54L, 198L, 255L, 81L, 170L, 207L, 182L, 55L, 165L, 235L, 32L, 50L, 24L, 238L, 77L, 234L, 196L, 126L, 145L, 34L, 219L, 194L, 62L, 185L, 162L, 210L, 240L, 25L, 22L, 91L, 124L, 144L, 48L, 4L, 232L, 33L, 147L, 243L, 73L, 106L, 169L, 41L, 11L, 216L, 97L, 38L, 181L, 247L, 90L, 225L, 218L, 214L, 233L, 69L, 252L, 45L, 3L, 141L, 37L, 221L, 203L, 146L, 139L, 192L, 249L, 175L, 63L, 138L, 100L, 230L, 8L, 206L, 151L, 68L, 176L, 205L, 116L, 133L, 1L, 251L, 179L, 127L, 105L, 27L, 197L, 30L, 215L, 53L, 16L, 129L, 110L, 160L, 61L, 108L, 5L]
for i in range(length):
	res[i] = sbox.index(res[i])

quiz4_ans = quiz_ans[3]
rem_length = length % quiz4_ans
idx = 0
for i in range(0, length, quiz4_ans):
	if length - rem_length == i:
		idx = 1
		quiz4_ans = rem_length
	for j in range(quiz4_ans):
		res[i + j] ^= quiz_ans[14 + j]
	enc = res[:]
	for j in range(quiz4_ans - idx):
		res[idx + i + j] = enc[i + j]
	for j in range(idx):
		res[i + j] = enc[quiz4_ans - idx + i + j]
	idx  = (idx + 1) % quiz4_ans

quiz2_ans = quiz_ans[1]
quiz3_ans = quiz_ans[2]
_sum = quiz2_ans + quiz3_ans
rem_length = length % _sum
answer = res[:]
for i in range(0, length, _sum):
	if length - rem_length == i:
		if rem_length < quiz2_ans:
			for j in range(rem_length):
				answer[i + j] = res[i + j]
			break
		quiz3_ans = rem_length - quiz2_ans
	for j in range(quiz2_ans):
		answer[i + j] = res[quiz3_ans + i + j]
	for j in range(quiz3_ans):
		answer[quiz2_ans + i + j] = res[i + j]

print ''.join(chr(i) for i in answer)

r.sendline(''.join(chr(i) for i in answer))

r.interactive()