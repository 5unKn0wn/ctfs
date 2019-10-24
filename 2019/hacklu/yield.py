from z3 import *

flag = ''

inp = [Int('inp_%d' % i) for i in range(16)]
res = [-5309, 63804, 11382, 42834, -54613, 11286, -12031, -29429, 24097, -42878, -21351, 32963, 15523, -6633, 14673, -33143]
mat = [
    [-95, 31, 58, -19, -87, -51, 71, 72, -9, 79, 33, -35, -21, 42, 13, -70], 
    [64, 100, -27, 66, 22, 68, -21, -2, 26, 74, 48, 93, 68, -79, 69, 92], 
    [49, 56, -75, 16, -79, 21, -5, 27, -7, 27, 50, -3, 13, -39, 2, 91], 
    [82, 40, 15, 31, 56, 78, -6, 55, -53, 81, -42, 24, -15, 80, 46, -50], 
    [-49, -92, -1, -83, -18, -87, -78, -58, -52, 39, 46, -67, -48, -79, -95, 98], 
    [39, 69, 25, -28, -44, 58, 87, -10, 0, -29, 18, -44, -25, 23, 3, -1], 
    [-79, 70, -70, 10, 10, -11, -79, -17, -11, 37, -30, 62, -27, -69, -49, 58], 
    [35, -59, -41, -80, 53, -55, 21, -88, 88, 72, -19, -57, -85, -72, -60, -35], 
    [100, 49, 98, -60, 33, 95, 51, -21, -94, -13, -43, -93, 70, -13, 11, 62], 
    [-75, -81, 29, -89, -79, 60, -16, -59, 67, -85, 51, -13, 18, -44, -13, -56], 
    [-53, 75, -74, -71, -53, 28, -36, -79, 5, -61, -61, 3, 50, -58, 50, 80], 
    [-68, 94, 100, -75, 56, 96, 40, 84, -46, -13, 72, 29, 67, -20, 0, -6], 
    [98, 35, 61, -95, -29, 71, -3, -5, -73, -11, 46, -91, -19, 67, 98, 10], 
    [22, -10, 77, -63, -1, -46, 65, 31, -17, -37, -74, 32, 10, 80, -56, -46], 
    [-34, 28, 61, 85, -65, 62, -46, 53, -28, 54, 44, 26, -93, 18, -15, -8], 
    [20, -9, -80, -41, -18, -90, -51, 85, 12, -3, -28, -48, -98, -4, 57, -98]
]
s = Solver()
for i in range(16):
    _sum = 0
    for j in range(16):
        _sum += inp[j] * mat[i][j]
    s.add(_sum == res[i])
s.check()
m = s.model()
flag +=  ''.join(chr(m[inp[i]].as_long()) for i in range(16))

tbl = [-182857, -207457, -205769, -149913, -221729]
for i in tbl:
    flag += hex((-i * 2) >> 4)[2:].decode('hex')

tbl = [89, 11025, 328509, 33362176, 10000000000, 1291467969, 42618442977, 59604644775390625]
for i in range(1, 9):
    flag += chr(int(round(tbl[i - 1] ** (i ** -1))))

print flag