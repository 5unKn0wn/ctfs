from capstone import *
from hashlib import *
from pwn import *

def calc(block, eax, edx, cmp_block=True):
	skip = 0
	for (address, size, mnemonic, op_str) in md.disasm_lite(block, 0):
		if cmp_block:
			if skip < 4:
				skip += 1
				continue

		if mnemonic == "mov":
			if op_str.split(", ")[0] == "eax":
				eax = int(op_str.split(", ")[1], 16)
			elif op_str.split(", ")[0] == "edx":
				edx = int(op_str.split(", ")[1], 16)

		elif mnemonic == "add":
			if op_str.split(", ")[0] == "eax":
				eax = (eax + int(op_str.split(", ")[1], 16)) & 0xffffffff
			elif op_str.split(", ")[0] == "edx":
				edx = (edx + int(op_str.split(", ")[1], 16)) & 0xffffffff

		elif mnemonic == "sub":
			if op_str.split(", ")[0] == "eax":
				eax = (eax - int(op_str.split(", ")[1], 16)) & 0xffffffff
			elif op_str.split(", ")[0] == "edx":
				edx = (edx - int(op_str.split(", ")[1], 16)) & 0xffffffff

		elif mnemonic == "mul":
			tmp = eax * edx
			eax = tmp & 0xffffffff
			edx = (tmp >> 32) & 0xffffffff

	return eax, edx

r = remote("buildingblocks.eatpwnnosleep.com", 46115)
md = Cs(CS_ARCH_X86, CS_MODE_64)

for i in range(10):
	r.recvuntil("stage (%d/10)\n" % (i + 1))
	code_list = [j.decode('base64') for j in eval(r.recvuntil("\n").rstrip())]

	# for l in code_list:
		# print disasm(l)
		# print "========================================"

	start_block = None
	calc_block = []
	end_block = None
	for l in code_list:
		if l[0] == '\xb8':
			start_block = l
		elif l[len(l) - 2] == '\x0f' and l[len(l) - 1] == '\x05':
			end_block = l
		else:
			calc_block.append(l)

	eax = 0
	edx = 0
	answer = start_block

	eax, edx = calc(start_block, eax, edx, cmp_block=False)
	# print hex(eax)

	for l in range(len(calc_block)):
		find = -1
		for ll in calc_block:
			for op in md.disasm(ll, 0):
				if int(op.op_str.split(", ")[1], 16) == eax:
					find = calc_block.index(ll)
					answer += calc_block[find]
					break
				else:
					break
			if find != -1:
				break

		eax, edx = calc(calc_block[find], eax, edx)

		# print hex(eax)

	answer += end_block

	# print disasm(answer)
	r.sendline(sha256(answer).hexdigest())
	log.info("stage%d success", (i + 1))

r.interactive()
