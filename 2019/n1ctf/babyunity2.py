from capstone import *
from capstone.x86 import *

md = Cs(CS_ARCH_X86, CS_MODE_64)
md.detail = True

dat = open("babyunity2.bin", "rb").read()

pc = 0x59c37
prev_size = 0

while True:
	insn = list(md.disasm(dat[pc:pc + 20], 0))[0]
	if insn.id == X86_INS_CALL:
		pc += insn.size
		insn = list(md.disasm(dat[pc:pc + 20], 0))[0]
		print insn.mnemonic, insn.op_str
		pc += insn.size
		prev_size = insn.size
	elif len(insn.operands) > 0 and insn.operands[0].type == X86_OP_MEM and insn.operands[0].mem.base == X86_REG_RSP:	# calculate next gadget
		pc -= prev_size
		offset = insn.operands[1].imm
		if insn.id == X86_INS_ADD:
			pc += offset
		elif insn.id == X86_INS_SUB:
			pc -= offset
	else:
		print insn.mnemonic, insn.op_str
		pc += insn.size
		if insn.id == X86_INS_RET:
			break