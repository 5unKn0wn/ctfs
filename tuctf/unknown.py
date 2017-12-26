import string
from pwn import *

peda = "gdb-peda$ \x01\x1B\x5B\x30\x6D\x02"
def send_cmd(cmd):
	p.sendlineafter(peda, cmd)

p = process(["gdb", "-q", "./unknown"])
table = '_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~ '
flag = "TUCTF{"
flag_len = 55

send_cmd("b *0x401C90")
send_cmd("b *0x401C86")
for i in range(len(flag), flag_len):	# side channel attack
	for j in table:
		side = flag + j + '_' * (flag_len - len(flag) - 1) + '}'
		send_cmd("r \"%s\"" % side)
		for k in range(len(flag)):
			send_cmd("c")
                data = p.recvuntil("EFLAGS")
                if "0x401c86" not in data:
                    flag += j
                    print flag
                    break

print flag + '}'
