from z3 import *

inp = [BitVec('inp_%d' % i, 8) for i in range(18)]
s = Solver()
tmp = 0

for i in range(16):
	s.add(inp[i] >= 32, inp[i] < 0x7f)
	if i == 6:
		num1 = inp[6]
		num2 = inp[16]
		num3 = inp[17]
		temp1 = num2 >> 2 ^ num3
		temp2 = num3 >> 2 ^ num1
		temp3 = num2 >> 2 ^ num1
		s.add(num1 >= temp1, num2 >= temp2, num3 >= temp3)
	else:
		num1 = inp[i]
		num2 = (inp[i + 1] >> 2) ^ inp[i + 2]
		s.add(num1 >= num2)
	if (i % 2 == 0) and i < 14:
		num1 = inp[i]
		num2 = inp[i + 2]
		num3 = inp[i + 4]
		num4 = inp[17 - i]
		if tmp == 0:
			s.add(num1 == (num2 ^ num3) + num4, 94 == (num1 ^ num2 ^ num3))
		elif tmp == 2:
			s.add(num1 == (num2 ^ num3) - num4 + 5, 32 == (num1 ^ num2 ^ num3))
		elif tmp == 4:
			s.add(num1 == ((num2 ^ num3) - num4) * 18, 11 == (num1 ^ num2 ^ num3))
		elif tmp == 6:
			s.add(num1 == (num2 ^ num3) + num4 - 2, 49 == (num1 ^ num2 ^ num3))
		elif tmp == 8:
			s.add(num1 == (num2 ^ num3 ^ num4) - 4, 89 == (num1 ^ num2 ^ num3))
		elif tmp == 10:
			s.add(num1 == (num2 ^ num3 ^ num4) + 19, 114 == (num1 ^ num2 ^ num3))
		elif tmp == 12:
			s.add(num1 == -((num2 ^ num3) & 2) + num4, 69 == (num1 ^ num2 ^ num3))
	elif (i % 2 != 0) and i < 14:
		num1 = inp[i]
		num2 = inp[i + 2]
		num3 = inp[i + 4]
		num4 = inp[17 - i]
		if tmp == 1:
			s.add(102 == (num1 ^ num2 ^ num3))
		elif tmp == 3:
			s.add(74 == (num1 ^ num2 ^ num3))
		elif tmp == 5:
			s.add(107 == (num1 ^ num2 ^ num3))
		elif tmp == 7:
			s.add(57 == (num1 ^ num2 ^ num3))
		elif tmp == 9:
			s.add(89 == (num1 ^ num2 ^ num3))
		elif tmp == 11:
			s.add(41 == (num1 ^ num2 ^ num3))
		elif tmp == 13:
			s.add(40 == (num1 ^ num2 ^ num3))
	tmp += 1

s.check()

m = s.model()
print ''.join(chr(m[inp[i]].as_long()) for i in range(18))
