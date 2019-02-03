l = []
o = []
t = bytearray('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
s = bytearray("H1\xc0H\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xffH\xf7\xdbST^\x99P_\xb0B\xb4\x01\x0f\x05")
ss = ''
rcx = 0x50506174

for i in range(len(s)):
	if s[i] not in t:
		l.append(s[i])
		o.append(0x3f + i)

print """push r12
pop rcx"""

for i in range(len(l)):
	for j in t:
		if ((rcx * j) & 0xff) ^ l[i] in t:
			print "imul edi,DWORD PTR [rcx], 0x%x" % j
			print "push rdi"
			print "pop rax"
			print "xor BYTE PTR [rcx+0x%x], al" % o[i]
			ss += chr(((rcx * j) & 0xff) ^ l[i])
			# print i, l[i], j
			break
idx = 0
res = ''
for i in range(len(s)):
	if s[i] in t:
		res += chr(s[i])
	else:
		res += ss[idx]
		idx += 1
print res