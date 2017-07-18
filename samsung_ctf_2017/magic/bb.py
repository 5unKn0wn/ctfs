serial = 14083742555054815066
v9 = []
v4 = 0
v5 = 0
table1 = [0x577402D733AA7E7, 0x69BFDBF76396DB95, 0xBF4477DE78DF7CE1, 0x6496707F80B1999F]
table3 = [0xB567, 0xE3C5, 0xEE19, 0xFE4B]
for i in range(4):
	v9.append(((table1[i] * serial) & 0xffffffffffffffffffffffffffffffff) >> 64)
v9 = [15951665476252467200, 8466812135872675840, 13437512712287813632, 18411550647829659648]
v9[0] = (((((((serial - v9[0]) & 0xffffffffffffffff) >> 1) + v9[0]) & 0xffffffffffffffff) >> 14) * 0x7D53) & 0xffffffffffffffff
v9[1] = (((((((serial - v9[1]) & 0xffffffffffffffff) >> 1) + v9[1]) & 0xffffffffffffffff) >> 14) * 0x5A95) & 0xffffffffffffffff
v9[2] = ((v9[2] >> 14) * 0x55A9) & 0xffffffffffffffff
v9[3] = ((v9[3] >> 13) * 0x5171) & 0xffffffffffffffff
print v9
v4 = [9981835508572042242, 12985306547410166310, 16674708790985680138, 5096637448183849958]
print v4
for j in range(4):
	# v4 = (serial - v9[j]) & 0xffffffffffffffff
	for k in range(4):
		if k != j:
			v4[j] = (v4[j] * table3[k]) & 0xffffffffffffffff
	v5 = (v5 + v4[j]) & 0xffffffffffffffff

print "0xc41fc083535f81e8"
print hex(v5)
