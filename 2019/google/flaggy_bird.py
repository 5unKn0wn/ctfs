from itertools import product
from hashlib import sha256
from z3 import *

def merge_sort(tbl, start, size):
	res = [0 for i in range(size)]
	global p
	if size >= 2:
		half_size = size / 2
		merge_sort(tbl, start, half_size)
		half_rem_size = size - half_size
		merge_sort(tbl, start + half_size, size - half_rem_size)
		i_hi = 0
		i_lo = 0
		i_cur = 0
		if half_rem_size >= 1:
			while True:
				c_hi = tbl[start + half_size + i_hi]
				c_lo = tbl[start + i_lo]
				if d[p] == 0:
					s.add(c_lo > c_hi)
					cur = c_hi
					i_hi += 1
				else:
					s.add(c_hi > c_lo)
					cur = c_lo
					i_lo += 1
				p += 1
				res[i_cur] = cur
				i_cur += 1
				if i_lo >= half_size or i_hi >= half_rem_size:
					break
		if half_size > i_lo:
			for i in range(half_size - i_lo):
				res[i_cur + i] = tbl[start + i_lo + i]
			i_cur = i_cur + half_size - i_lo
		if i_hi < half_rem_size:
			for i in range(size - i_hi - half_size):
				res[i_cur + i] = tbl[start + i_hi + half_size + i]
		for i in range(size):
			tbl[start + i] = res[i]


inp = [Int('inp_%d' % i) for i in range(16)]
o_inp = inp[::]
d = [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0]
c = 1
p = 0

s = Solver()

for i in range(16):
	s.add(inp[i] >= 0, inp[i] < 16)

merge_sort(inp, 0, 16)

assert(s.check() == sat)
m = s.model()

target = []
for i in range(16):
	target.append(m[o_inp[i]].as_long())

arr = []
for i in target:
	arr.append([(0, i), (i, 0)])

for l in product(*arr):
	s = ''.join(chr(i[0]) + chr(i[1]) for i in l)
	if sha256(s).hexdigest() == "2e325c91c91478b35c2e0cb65b7851c6fa98855a77c3bfd3f00840bc99ace26b":
		print l
		break
