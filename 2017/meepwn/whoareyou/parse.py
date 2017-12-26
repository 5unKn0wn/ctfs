import re

def simul(ins):
	code = ["def simul(rbx):"]
	for i in ins:
		if "mov     rax, " in i:
			rax = int(i.split("mov     rax, ")[1].replace('h', ''), 16)

		elif "rol     rbx, " in i:
			value = int(i.split("rol     rbx, ")[1].replace('h', ''), 16)
			code.append("\trbx = rol(rbx, %s, 64)" % hex(value).replace('L', ''))

		elif "xor     rbx, rax" in i:
			if rax == 0:
				code.append("fail")
				break
			code.append("\trbx ^= %s" % hex(rax).replace('L', ''))

		elif "sub     rbx, rax" in i:
			if rax == 0:
				code.append("fail")
				break
			code.append("\trbx -= %s" % hex(rax).replace('L', ''))

		elif "ror     rbx, " in i:
			value = int(i.split("ror     rbx, ")[1].replace('h', ''), 16)
			code.append("\trbx = ror(rbx, %s, 64)" % hex(value).replace('L', ''))

		elif "add     rbx, rax" in i:
			if rax == 0:
				code.append("fail")
				break
			code.append("\trbx += %s" % hex(rax).replace('L', ''))

		elif "sub     rax, rbx" in i:
			if rax == 0:
				code.append("fail")
				break
			code.append("\treturn %s - rbx" % hex(rax).replace('L', ''))

	return code

def reverse(ins):
	code = ["\treturn rbx"]
	for i in ins:
		if "mov     rax, " in i:
			rax = int(i.split("mov     rax, ")[1].replace('h', ''), 16)

		elif "rol     rbx, " in i:
			value = int(i.split("rol     rbx, ")[1].replace('h', ''), 16)
			code.append("\trbx = ror(rbx, %s, 64)" % hex(value).replace('L', ''))

		elif "xor     rbx, rax" in i:
			if rax == 0:
				code.append("fail")
				break
			code.append("\trbx ^= %s" % hex(rax).replace('L', ''))

		elif "sub     rbx, rax" in i:
			if rax == 0:
				code.append("fail")
				break
			code.append("\trbx += %s" % hex(rax).replace('L', ''))

		elif "ror     rbx, " in i:
			value = int(i.split("ror     rbx, ")[1].replace('h', ''), 16)
			code.append("\trbx = rol(rbx, %s, 64)" % hex(value).replace('L', ''))

		elif "add     rbx, rax" in i:
			if rax == 0:
				code.append("fail")
				break
			code.append("\trbx -= %s" % hex(rax).replace('L', ''))

	code.append("def reverse(rbx):")
	return code[::-1]

with open("ida.txt", "rt") as f:
	data = f.read()

data = re.sub("seg000:000000000000.... ;.*", '', data)
data = re.sub("seg000:000000000000....\n", '', data)
data = re.sub("seg000:000000000000.... ", '', data)
data = re.sub(": .*", '', data)
data = re.sub(".*;.*", '', data)
data = re.sub("\n\n", '\n', data)

res = []
loc = None
for i in data.split('\n'):
	if loc != None:
		if loc == i:
			loc = None
		else:
			pass
	elif "jmp     short " in i:
		loc = i.split('jmp     short ')[1]
	elif "loc" in i:
		pass
	else:
		res.append(i)

for i in reverse(res):
	print i
