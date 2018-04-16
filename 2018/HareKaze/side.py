import string
from pwn import *

peda = "gdb-peda$ \x01\x1B\x5B\x30\x6D\x02"
def send_cmd(cmd):
	p.sendafter(peda, cmd)

p = process(["gdb", "-q", "lazy"])
table = '0123456789ABCDEF}_abcdefghijklmnopqrstuvwxyzGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^`|~ '
flag = "HarekazeCTF{4AD8AA3A3571EA912A6EC5EA5FDCC93C}"
flag_len = 100

send_cmd("b *0x0000000000400F87")	# getchar
for i in range(len(flag), flag_len):	# side channel attack
	for j in table:
		side = flag + j
		send_cmd("r foo.lazy")
                p.sendlineafter("Starting program: /home/5unKn0wn/ctfs/2018/HareKaze/lazy foo.lazy\n", side)

		for k in range(len(flag) + 1):
			send_cmd("c")
                p.interactive()
		p.recv(1024)
		data = p.recv(1024)

		if "[----------------------------------registers-----------------------------------]" in data:
			flag += j
			print flag
                        if j == '}':
                            exit()
			break
# HarekazeCTF{4AD8AA3A3571EA912A6EC5EA5FDCC93C}
