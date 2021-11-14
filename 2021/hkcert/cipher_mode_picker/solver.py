from pwn import *

r = remote("chalp.hkcert21.pwnable.hk", 28102)

r.sendlineafter("> ", "cbc data " + "00" * 80)
ct = bytes.fromhex(r.recvline().decode())

r.sendlineafter("> ", "ofb flag")
flag_ct = bytes.fromhex(r.recvline().decode())

print(xor(ct, flag_ct))
