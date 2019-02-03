res = "l_pApQIAWm8IpcIK4cc4E"
table = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

for i in range(len(res)):
	for j in range(len(table)):
		inp = j
		inp += 4.1
		inp = (inp * 3.0) - 8.98
		inp += 1.03
		inp = (inp * 1.998) - 3.201
		inp += 7.10345
		inp = (inp * 5.0102) - 0.98912
		inp = int(inp)
		if table[inp % 0x3f] == res[i]:
			print table[j],
	print
print "nv1d14_d03S_1t_8etteR"
# nv1d14_d03S_1t_8etteR
'''
n
a v
G 1
d y
G 1
J 4
_
d y
F 0
I 3
S
_
G 1
t
_
N 8
e z
t
t
e z
R
'''
