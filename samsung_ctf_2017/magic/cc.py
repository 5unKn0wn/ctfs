from z3 import *

serial = BitVec('serial', 128)
s = Solver()
v9 = []
v4 = None
v5 = 0
table1 = [0x577402D733AA7E7, 0x69BFDBF76396DB95, 0xBF4477DE78DF7CE1, 0x6496707F80B1999F]
table3 = [0xB567, 0xE3C5, 0xEE19, 0xFE4B]
for i in range(4):
	v9.append(LShR((table1[i] * serial), 64))
v9[0] = (LShR(((LShR(((serial - v9[0])), 1) + v9[0])), 14) * 0x7D53)
v9[1] = (LShR(((LShR(((serial - v9[1])), 1) + v9[1])), 14) * 0x5A95)
v9[2] = (LShR(v9[2], 14) * 0x55A9)
v9[3] = (LShR(v9[3], 13) * 0x5171)

for j in range(4):
	v4 = (serial - v9[j])
	for k in range(4):
		if k != j:
			v4 = (v4 * table3[k])
	v5 = (v5 + v4)

s.add(v5 == 0xC41FC083535F81E7)

while s.check() == sat:
	print s.model()
