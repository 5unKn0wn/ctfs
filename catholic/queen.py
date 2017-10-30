flag_table = [74, 93, 109, 51, 212, 143, 362, 311, 393, 619, 86, 101, 86, 21, 206, 173, 355, 261, 486, 638, 108, 111, 77, 63, 208, 190, 295, 259, 465, 626, 96, 41, 68]
xor_table = []
score = 0

for i in range(1, 11):
	score += (10 * i - 1)
	xor_table.append(score & 0xff)

print ''.join(chr(((flag_table[i] & 0xff) ^ (xor_table[i % len(xor_table)] & 0xff))) for i in range(len(flag_table)))
