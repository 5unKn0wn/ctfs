import string
from pwn import *

peda = "gdb-peda$ \x01\x1B\x5B\x30\x6D\x02"
def send_cmd(cmd):
	p.sendlineafter(peda, cmd)

p = process(["gdb", "-q", "./grrrr_1b99983c47f4e8d041eda90ae53c096841c10d4e"])
table = '_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~ '
flag = "SCTF{"
flag_len = 26

send_cmd("b *0x54c723")	# grumpy_Xor
for i in range(len(flag), flag_len):	# side channel attack
	for j in table:
		side = flag + j + '_' * (flag_len - len(flag) - 1) + '}'
		send_cmd("r \"%s\"" % side)

		for k in range(len(flag) + 1):
			send_cmd("c")

		p.recv(1024)
		data = p.recv(1024)

		if "[----------------------------------registers-----------------------------------]" in data:
			flag += j
			print flag
			break

print flag + '}'	# SCTF{6rumpy_c47_m30w5_6rrr}
