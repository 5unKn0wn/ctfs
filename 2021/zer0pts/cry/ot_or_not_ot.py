'''
u = a^r*c^s mod p
v = b^r*c^s mod p
z = d^r*t^s mod p
let a=2, b=2^-1 mod p, c=t^-1 mod p, d=-1 mod p
then
u = 2^r*t^-s mod p
v = 2^-r*t^-s mod p
z = (-1)^r*t^s mod p
so
u*z = 2^r*(-1)^r mod p
v*z = 2^-r*(-1)^r mod p
u*z*v*z = (-1)^2r mod p
Because u*z*v*z has an even exponent, it must be 1
'''
from base64 import b64decode
from Crypto.Util.number import long_to_bytes
from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
from pwn import *

r = remote("crypto.ctf.zer0pts.com", 10130)

r.recvuntil("Encrypted flag: ")
enc_flag = b64decode(r.recvuntil("\n", drop=True))
r.recvuntil("p = ")
p = int(r.recvuntil("\n", drop=True))
r.recvuntil("key.bit_length() = ")
key_len = int(r.recvuntil("\n", drop=True))

key = ''
for i in range(0, key_len, 2):
    r.recvuntil("t = ")
    t = int(r.recvuntil("\n", drop=True))
    a = 2
    b = pow(2, -1, p)
    c = pow(t, -1, p)
    d = p - 1
    r.sendlineafter("a = ", str(a))
    r.sendlineafter("b = ", str(b))
    r.sendlineafter("c = ", str(c))
    r.sendlineafter("d = ", str(d))

    r.recvuntil("x = ")
    x = int(r.recvuntil("\n", drop=True))
    r.recvuntil("y = ")
    y = int(r.recvuntil("\n", drop=True))
    r.recvuntil("z = ")
    z = int(r.recvuntil("\n", drop=True))
    
    if x * y * z * z % p == 1:
        key += "00"
    elif (x ^ 1) * y * z * z % p == 1:
        key += "10"
    elif x * (y ^ 1) * z * z % p == 1:
        key += "01"
    elif (x ^ 1) * (y ^ 1) * z * z % p == 1:
        key += "11"
    else:
        print("?")

    print(f"{i} / {key_len}")

key = long_to_bytes(int(key[::-1], 2))
aes = AES.new(key=key, mode=AES.MODE_CBC, iv=enc_flag[:16])
print(unpad(aes.decrypt(enc_flag[16:]), 16))
