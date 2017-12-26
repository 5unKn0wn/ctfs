from pwn import *
import struct

def find_ret(start):
	idx = 0
	while True:
		if start[idx] == '\xc3':
			return idx + 1
		idx += 1

def find_sub_esp_8(start):
	idx = 0
	while True:
		# 83 EC 08
		if start[idx] == '\x83' and start[idx + 1] == '\xec' and start[idx + 2] == '\x08':
			return idx
		idx += 1

def stage1(binary):
	if binary[0x713] == '\x81':
		stack_size = u32(binary[0x715:0x715+4]) - 0xc
		patch_point = 0x71d
		if binary[0x71c] == '\x68':
			patch_size = 2
		elif binary[0x71c] == '\x6a':
			patch_size = 1
	elif binary[0x713] == '\x83':
		stack_size = ord(binary[0x715]) - 0xc
		patch_point = 0x71a
		if binary[0x719] == '\x68':
			patch_size = 2
		elif binary[0x719] == '\x6a':
			patch_size = 1

	# get_int = bytearray(binary[0x710:0x710 + find_ret(binary[0x710:])])

	# print disasm(str(get_int))
	# print hex(stack_size)

	binary = bytearray(binary)

	if patch_size == 1:
		binary[patch_point] = stack_size
	elif patch_size == 2:
		binary[patch_point] = stack_size & 0xff
		binary[patch_point + 1] = stack_size >> 8

	binary = str(binary)

	# get_int = bytearray(binary[0x710:0x710 + find_ret(binary[0x710:])])
	# print disasm(str(get_int))

	return binary

def stage2(binary):
	e = ELF("./stage2")
	get_file_addr = e.symbols['get_file'] - 0x8048000
	patch_size = 0

	# get_file = bytearray(binary[get_file_addr:get_file_addr + find_ret(binary[get_file_addr:])])
	# print disasm(str(get_file))

	if binary[get_file_addr+3] == '\x81':
		stack_size = u32(binary[get_file_addr+5:get_file_addr+5+4]) - 0xc
		patch_point = get_file_addr + 0x1b
		if binary[get_file_addr+0x1a] == '\x68':
			patch_size = 2
		elif binary[get_file_addr+0x1a] == '\x6a':
			patch_size = 1
	elif binary[get_file_addr+3] == '\x83':
		stack_size = ord(binary[get_file_addr+5]) - 0xc
		patch_point = get_file_addr + 0x18
		if binary[get_file_addr+0x17] == '\x68':
			patch_size = 2
		elif binary[get_file_addr+0x17] == '\x6a':
			patch_size = 1

	# print hex(stack_size), hex(len_size)

	binary = bytearray(binary)

	if patch_size == 1:
		binary[patch_point] = stack_size
	elif patch_size == 2:
		binary[patch_point] = stack_size & 0xff
		binary[patch_point + 1] = stack_size >> 8

	binary = str(binary)

	# get_file = bytearray(binary[get_file_addr:get_file_addr + find_ret(binary[get_file_addr:])])
	# print disasm(str(get_file))

	return binary

def stage3(binary):
	e = ELF("./stage3")
	modify_file_addr = e.symbols['modify_file'] - 0x8048000
	create_file_addr = e.symbols['create_file'] - 0x8048000
	buffer_size = 0

	create_file = bytearray(binary[create_file_addr:create_file_addr + find_ret(binary[create_file_addr:])])
	# print disasm(str(create_file))

	if binary[create_file_addr+find_sub_esp_8(binary[create_file_addr:])+3] == "\x68":
		buffer_size = u32(binary[create_file_addr+find_sub_esp_8(binary[create_file_addr:])+3+1:create_file_addr+find_sub_esp_8(binary[create_file_addr:])+3+1+4])
	elif binary[create_file_addr+find_sub_esp_8(binary[create_file_addr:])+3] == "\x6a":
		buffer_size = ord(binary[create_file_addr+find_sub_esp_8(binary[create_file_addr:])+3+1])

	# print hex(buffer_size)

	# modify_file = bytearray(binary[modify_file_addr:modify_file_addr + find_ret(binary[modify_file_addr:])])
	# print disasm(str(modify_file))

	patch_point = modify_file_addr + find_sub_esp_8(binary[modify_file_addr:]) + 3 + 1

	if binary[modify_file_addr+find_sub_esp_8(binary[modify_file_addr:])+3] == "\x68":
		patch_size = 2
	elif binary[modify_file_addr+find_sub_esp_8(binary[modify_file_addr:])+3] == "\x6a":
		patch_size = 1

	binary = bytearray(binary)

	if patch_size == 1:
		binary[patch_point] = buffer_size
	elif patch_size == 2:
		binary[patch_point] = buffer_size & 0xff
		binary[patch_point + 1] = buffer_size >> 8

	binary = str(binary)

	# modify_file = bytearray(binary[modify_file_addr:modify_file_addr + find_ret(binary[modify_file_addr:])])
	# print disasm(str(modify_file))

	return binary

u32 = lambda x : struct.unpack("<L", x)[0]

r = remote("bad3.eatpwnnosleep.com", 8888)

# stage1
r.recvuntil("STAGE : 1\n")
for i in range(30):
	binary = r.recvuntil("Send").replace("Send", "").decode('base64')
	with open("stage1", "wb") as f:
		f.write(binary)

	binary = stage1(binary)

	r.sendline(binary.encode('base64').replace('\n', ''))
	r.recvuntil("Success!\n")
	log.info("Stage1 : %d success" % (i + 1))

# stage2
r.recvuntil("STAGE : 2\n")
for i in range(30):
	binary = r.recvuntil("Send").replace("Send", "").decode('base64')
	with open("stage2", "wb") as f:
		f.write(binary)

	# binary = open("stage2").read()

	binary = stage1(binary)
	binary = stage2(binary)

	r.sendline(binary.encode('base64').replace('\n', ''))
	r.recvuntil("Success!\n")
	log.info("Stage2 : %d success" % (i + 1))

# stage3
r.recvuntil("STAGE : 3\n")
for i in range(30):
	binary = r.recvuntil("Send").replace("Send", "").decode('base64')
	with open("stage2", "wb") as f:
		f.write(binary)
	with open("stage3", "wb") as f:
		f.write(binary)

	# binary = open("stage3").read()

	binary = stage1(binary)
	binary = stage2(binary)
	binary = stage3(binary)

	r.sendline(binary.encode('base64').replace('\n', ''))
	r.recvuntil("Success!\n")
	log.info("Stage3 : %d success" % (i + 1))

r.interactive()
