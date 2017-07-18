from z3 import *

serial = BitVec('serial', 64)
s = Solver()
v9 = []
v4 = 0
v5 = 0
table1 = [0x577402D733AA7E7, 0x69BFDBF76396DB95, 0xBF4477DE78DF7CE1, 0x6496707F80B1999F]
table3 = [0xB567, 0xE3C5, 0xEE19, 0xFE4B]
for i in range(4):
	v9.append(LShR(((table1[i] * serial) & 0xffffffffffffffffffffffffffffffff), 64))
v9[0] = (LShR(((LShR(((serial - v9[0]) & 0xffffffffffffffff), 1) + v9[0]) & 0xffffffffffffffff), 14) * 0x7D53) & 0xffffffffffffffff
v9[1] = (LShR(((LShR(((serial - v9[1]) & 0xffffffffffffffff), 1) + v9[1]) & 0xffffffffffffffff), 14) * 0x5A95) & 0xffffffffffffffff
v9[2] = (LShR(v9[2], 14) * 0x55A9) & 0xffffffffffffffff
v9[3] = (LShR(v9[3], 13) * 0x5171) & 0xffffffffffffffff

for j in range(4):
	v4 = (serial - v9[j]) & 0xffffffffffffffff
	for k in range(4):
		if k != j:
			v4 = (v4 * table3[k]) & 0xffffffffffffffff
	v5 = (v5 + v4) & 0xffffffffffffffff

# s.add(serial != 1183974438802706274)
# s.add(serial != 11895241035835385719)
s.add(v5 == 0xC41FC083535F81E8)

print s.check()
print s.model()
