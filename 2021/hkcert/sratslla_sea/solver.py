from sage.all import *
from Crypto.Util.number import long_to_bytes, bytes_to_long
from aes import AES
from pwn import *
import random
import os

# A function that does nothing
no_op = lambda *x: None

def bin2ascii(bits):
    return long_to_bytes(int(''.join(str(i) for i in bits), 2))

def ascii2bin(s):
    return [int(i) for i in bin(bytes_to_long(s))[2:].zfill(128)]

def solve_ark(blk):
    cipher = AES(b"\x00" * 16)
    cipher._add_round_key = no_op
    return cipher.decrypt(blk)[::4]

def solve_sb(pt, ct, blk):
    cipher = AES(b'\x00' * 16)
    cipher._add_round_key = no_op
    cipher._sub_bytes = no_op

    A = Matrix(GF(2), 128)
    for i in range(128):
        col = bin2ascii([0 if i != j else 1 for j in range(128)])
        col = [int(str(j)) for j in ascii2bin(cipher.encrypt(col))]
        A.set_column(i, col)

    pt_vec = vector(GF(2), [int(str(i)) for i in ascii2bin(pt)])
    ct_vec = vector(GF(2), [int(str(i)) for i in ascii2bin(ct)])

    k = ct_vec - A * pt_vec

    blk_vec = vector(GF(2), [int(str(i)) for i in ascii2bin(blk)])
    return bin2ascii(A.solve_right(blk_vec + k))[::4]

def solve_sr(key_dict, blk):
    blk_l = [blk[:4], blk[4:8], blk[8:12], blk[12:]]
    k = b''

    not_found = False
    for b in blk_l:
        if key_dict.get(b) == None:
            not_found = True
            print("not found")
        else:
            k += key_dict.get(b)
            print("found !")

    if not_found:
        return False
    return k

while True:
    r = remote("chalp.hkcert21.pwnable.hk", 28207)
    k = b''

    r.recvuntil("decrypt: ")
    flag_ct = r.recvuntil(".", drop=True)
    print(f"flag_ct = {flag_ct}")

    r.sendlineafter("> ", "ark secret")
    ark_blk = bytes.fromhex(r.recvline().decode())
    k += solve_ark(ark_blk)

    pt = os.urandom(16)
    r.sendlineafter("> ", f"sb data {pt.hex()}")
    ct = bytes.fromhex(r.recvline().decode())
    r.sendlineafter("> ", "sb secret")
    sb_blk = bytes.fromhex(r.recvline().decode())
    k += solve_sb(pt, ct, sb_blk)

    ranchars = list(range(256))
    random.shuffle(ranchars)
    key_dict = {}
    for i in range(124):
        r.sendlineafter("> ", f"sr data {bytes([ranchars[i] for j in range(16)]).hex()}")
        ct = bytes.fromhex(r.recvline().decode())
        key_dict[ct[:4]] = bytes([ranchars[i]])
        key_dict[ct[4:8]] = bytes([ranchars[i]])
        key_dict[ct[8:12]] = bytes([ranchars[i]])
        key_dict[ct[12:]] = bytes([ranchars[i]])

    r.sendlineafter("> ", "sr secret")
    sr_blk = bytes.fromhex(r.recvline().decode())
    sr = solve_sr(key_dict, sr_blk)
    if sr == False:
        print("failed..")
        r.close()
        continue
    k += sr

    print(f"partial 12 byte key = {k.hex()}")
    break
