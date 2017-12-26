from pwn import *
import os
import angr
import time
import logging

angr_code = '''
def libc_hook(state):
	state.regs.%s = 0x7f

start = time.time()
project = angr.Project("./bin")

project.hook(0x%x, libc_hook, length=0x%x)
initial_state = project.factory.blank_state()
pg = project.factory.path_group(initial_state)
pg.explore(find=0x%x, avoid=0x%x)

with open("key", "wt") as f:
	f.write(pg.found[0].state.posix.dumps(0))
'''

r = remote("112.166.114.190", 19000)

r.sendlineafter("(y/n) ", "y")

for i in range(10):
	log.info("stage %d" % (i + 1))
	r.recvuntil("[*] stage %d.\n\n" % (i + 1))
	start = time.time()
	data = r.recvuntil('\n').rstrip().decode('base64')
	with open("bin.xz", "wb") as f:
		f.write(data)
	os.system("xz -d ./bin.xz")

	os.system("objdump -d -M intel ./bin | grep \"mov    edi,0x1\" > dump.txt")
	with open("dump.txt", "rt") as f:
		data = f.read().split('\n')
	find_addr = int(data[-3].split(':')[0].lstrip(), 16)
	avoid_addr = int(data[-2].split(':')[0].lstrip(), 16)

	os.system("objdump -d -M intel ./bin | grep \"ds\" -b4 > dump.txt")
	with open("dump.txt", "rt") as f:
		data = f.read().split('\n')
	
	hook_addr = int(data[4].split(':')[1].lstrip(), 16)
	hook_reg = data[6].split(',')[0].split(' ')[-1]
	end_addr = int(data[8].split(':')[0].split(' ')[-1].lstrip(), 16)
	length = end_addr - hook_addr

	exec_code = angr_code % (hook_reg, hook_addr, length, find_addr, avoid_addr)

	print exec_code
	exec(exec_code)

	with open("key", "rt") as f:
		key = f.read().replace('\x00', '')
	print key
	print time.time() - start

	r.sendlineafter("input key: ", key)
	os.system("rm bin dump.txt key")

r.interactive()
