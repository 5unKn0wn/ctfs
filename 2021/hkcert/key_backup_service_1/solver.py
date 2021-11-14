from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
from sage.all import *
from pwn import *

while True:
    r = remote("chalp.hkcert21.pwnable.hk", 28157, level='error')

    r.sendlineafter("[cmd] ", "flag")
    flag_ct = bytes.fromhex(r.recvline().decode())

    ns = []
    cs = []
    for i in range(5):
        r.sendlineafter("[cmd] ", "pkey")
        r.sendlineafter("[cmd] ", "send 125fffffffffffff")
        c = int(r.recvline(), 16)
        if c == pow(0x125fffffffffffff, 17):
            print("failed... 1")
            r.close()
            break
        n = pow(0x125fffffffffffff, 17) - c
        if n > 2**1024:
            print("failed... 2")
            r.close()
            break
        ns.append(n)
        r.sendlineafter("[cmd] ", "backup")
        cs.append(int(r.recvline(), 16))

    if len(ns) != 5:
        continue
    master_secret = int.to_bytes(int(crt(cs, ns).nth_root(17)), 32, 'big')
    print(unpad(AES.new(master_secret, AES.MODE_CBC, b'\x00' * 16).decrypt(flag_ct), 16))
    break
