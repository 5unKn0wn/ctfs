from Crypto.Cipher import AES
from pwn import *

r = remote("re-cses.ctfz.one", 3607)

r.sendline("encrypt::" + 'a' * 47)
dat = r.recvuntil('\x00').decode('base64')
c0, c1, c2 = dat[:16], dat[16:32], dat[32:]
r.sendline("decrypt::" + (c0 + c1 + c0).encode('base64').replace('\n', '')) # p2 == c1 ^ p0 ^ iv, iv = c1 ^ p0 ^ p2
dat = r.recv(48)
p0, p1, p2 = dat[:16], dat[16:32], dat[32:]
print AES.new("ctfzoneencaeskey", AES.MODE_ECB).decrypt(xor(c1, p0, p2))