import string
from pwn import *

peda = "gdb-peda$ \x01\x1B\x5B\x30\x6D\x02"
def send_cmd(cmd):
	p.sendlineafter(peda, cmd)

p = process(["gdb", "-q", "lazy"])
table = '0123456789ABCDEF}_abcdefghijklmnopqrstuvwxyzGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^`|~ '
flag = "HAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
flag_len = 100

send_cmd("b *0x00000000004006B0")	# getchar
send_cmd("r bar.lazy")
send_cmd("c")
p.sendline(flag)
for i in range(52):
    if i == 51:
        send_cmd("b *0x0000000000400E46")
    send_cmd("c")
while True:
    p.recvuntil("RAX\x1b\x5b\x30\x6d: ")
    data = p.recvuntil(" ", drop=True)
    print data,
    send_cmd("c")
    '''for k in range(len(flag) + 1):
            send_cmd("c")
    p.interactive()
    p.recv(1024)
    data = p.recv(1024)

    if "[----------------------------------registers-----------------------------------]" in data:
            flag += j
            print flag
            if j == '}':
                exit()
            break'''
# HarekazeCTF{4AD8AA3A3571EA912A6EC5EA5FDCC93C}
