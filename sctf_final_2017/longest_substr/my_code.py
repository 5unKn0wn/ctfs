def cmp(s1, s2):
	if len(s1) > len(s2):
		l = len(s2)
	else:
		l = len(s1)

	res = ''
	for i in range(l):
		if s1[i] != s2[i]:
			return i, res
		res += s1[i]
	return l, res

a = raw_input().replace("<EOF>", "")
suff = []

for i in range(len(a)):
	suff.append(a[-i:])

suff.sort()
print suff
ans = ''
l = 0

for i in range(len(suff) - 1):
	s1 = suff[i]
	s2 = suff[i + 1]
	tmp, tmp2 = cmp(s1, s2)
	if tmp > l:
		l = tmp
		ans = tmp2


print ans
