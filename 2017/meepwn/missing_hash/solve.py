from z3 import *

def calc(arr1, arr2, cnt):
	res = cnt
	for i in range(cnt):
		res = (~arr2[i] & res) + (~res & arr2[i])
		res = (res & 0xff00) + ((res + arr1[i]) & 0xff)
	return res

hero = [BitVec("hero_%d" % i, 16) for i in range(10)]
s = Solver()

res_arr = [0 for i in range(7)]
arr1 = [0xA485, 0x4A8F, 0xDC23, 0x74BE, 0xBF52, 0x4580, 0x8135, 0x62D5, 0x79A2, 0xF24B]
res_arr[3] += calc([hero[7], hero[8], hero[9]], [arr1[3], arr1[4], arr1[5]], 3)
res_arr[5] += calc([hero[4], hero[5], hero[6]], [arr1[6], arr1[7], arr1[8]], 3)
res_arr[4] += calc([hero[0], hero[1], hero[2]], [arr1[5], arr1[6], arr1[7]], 3)
res_arr[6] += calc([hero[3], hero[4], hero[5]], [arr1[4], arr1[5], arr1[6]], 3)
res_arr[0] += calc([hero[5], hero[6], hero[7]], [arr1[0], arr1[1], arr1[2]], 3)
res_arr[2] += calc([hero[3], hero[4], hero[5], hero[6]], [arr1[2], arr1[3], arr1[4], arr1[5]], 4)
res_arr[1] += calc([hero[2], hero[3], hero[4]], [arr1[7], arr1[8], arr1[9]], 3)

for i in range(7):
	res_arr[i] = ((((LShR(res_arr[i], 15) * 0xffff0000) + res_arr[i]) << 8) ^ (res_arr[i] >> 8))	# fucking shift

arr2 = [0x80, 0x45, 0x85, 0xA4, 0x8F, 0x4A, 0x52]
arr3 = [0x5744, 0xAC89, 0x756B, 0x7C26, 0x7821, 0x8171, 0x8BB6]

arr3[0] = (arr3[0] + calc([arr2[2], arr2[3]], [res_arr[2], res_arr[3]], 2))
arr3[4] = (arr3[4] + calc([arr2[1], arr2[2]], [res_arr[5], res_arr[6]], 2))
arr3[1] = (arr3[1] + calc([arr2[5], arr2[6]], [res_arr[0], res_arr[1]], 2))
arr3[5] = (arr3[5] + calc([arr2[0], arr2[1]], [res_arr[4], res_arr[5]], 2))
arr3[6] = (arr3[6] + calc([arr2[3], arr2[4]], [0x1337, res_arr[0]], 2))
arr3[3] = (arr3[3] + calc([0x52, 0xBF], [res_arr[1], res_arr[2]], 2))
arr3[2] = (arr3[2] + calc([arr2[4], arr2[5]], [res_arr[3], res_arr[4]], 2))

arr4 = [0x2701, 0x651B, 0x40F9, 0x6D2, 0x43D5, 0x17FD, 0x1D86, 0x1164, 0xB2C7]

arr4[0] = (arr4[0] + calc([arr2[2], arr2[3]], [res_arr[2], res_arr[3]], 2))
arr4[4] = (arr4[4] + calc([arr2[1], arr2[2]], [res_arr[5], res_arr[6]], 2))
arr4[1] = (arr4[1] + calc([arr2[5], arr2[6]], [res_arr[0], res_arr[1]], 2))
arr4[5] = (arr4[5] + calc([arr2[0], arr2[1]], [res_arr[4], res_arr[5]], 2))
arr4[6] = (arr4[6] + calc([arr2[3], arr2[4]], [0x1337, res_arr[0]], 2))
arr4[3] = (arr4[3] + calc([0x52, 0xBF], [res_arr[1], res_arr[2]], 2))
arr4[2] = (arr4[2] + calc([arr2[4], arr2[5]], [res_arr[3], res_arr[4]], 2))
arr4[7] = (arr4[7] + calc([hero[5], hero[6]], [(arr2[3] << 8) | arr2[2], (arr2[5] << 8) | arr2[4]], 2))
arr4[8] = (arr4[8] + calc([(arr3[0] >> 8), arr3[1] & 0xff], [0xBF52, 0xF24B], 2))

for i in range(9):
	s.add(arr4[i] == 0)

s.add(hero[0] == ord('Z'))
s.add(hero[9] == ord('!'))

s.check()
m = s.model()

ans = ''
for i in range(10):
	ans += chr(m[hero[i]].as_long())
print "MeePwnCTF{" + ans + "}"
