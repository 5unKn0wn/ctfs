from pwn import *
import string

table = string.printable[:-5]
cnt = 0
for i in table:
	r = process("./bl4ck_4rtz")
	r.recv(1024)
	r.sendline("FLAG{n0_a4cr&eic?zf0_th1s_m4%c1C}" % i)
	data = r.recv(1024)
	if "WITCH!" in data:
		cnt += 1
	r.close()

print cnt
