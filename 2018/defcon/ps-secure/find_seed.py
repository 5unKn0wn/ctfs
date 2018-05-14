def backward():
	global seed
	seed = ((seed - 0x269EC3) * 0xb9b33155) & 0xffffffff

def forward():
	global seed
	seed = (0x343FD * seed + 0x269EC3) & 0xffffffff
	return (seed >> 16) & 0x7fff

seed = 0
l = []
for i in range(0, 0x10000) + range(0x80000000, 0x80010000):
	seed = i
	if forward() % 65 == 50:
		l.append(seed)

#print l

for i in l:
	seed = i
	for j in range(1 + 11500):
		backward()
	for j in range(50):
		backward()
		if seed < 100000:
			print hex(i)	# --> 0x374b2e90 is correct seed1 when after call rax
