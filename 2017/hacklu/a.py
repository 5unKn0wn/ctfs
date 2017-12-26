from pwn import *

r = process("./a", env={"LD_PRELOAD" : "./backdoor.so"})
r.interactive()
