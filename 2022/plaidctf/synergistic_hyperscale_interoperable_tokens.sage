from pwn import *
import subprocess

def f(v, w):
    elem = vector(v) * vector(w)
    v[:9] = v[1:]
    v[9] = elem
    return v

def generate_token(n):
    initial_state = [0x05BA2B30F33009E3, 0xBDEF1E03F8A42971, 0x2CE572B38B540058, 0x405943E2C746EF8A, 0x012DA654BC29E00C, 0x4A901FC9B5E1F7EF, 0x4707916C3F4F882C, 0x01E948B96DC61489, 0x88C7AF20A872B40F, 0x2DEF3A950A3DF2EE]
    multiply_vector = [0xEC32EF2CA379F6EF, 0x646B9980E07FBDE6, 0xD005C98621B0A224, 0xDED12B11AA38888, 0x895DD3AA6089713E, 0x2868836EDEE04734, 0xD313806DAD60830A, 0xF63D4B112D6FD165, 0x4BDA5E346CF43679, 0x1C4EF5256BF7691F]
    M = identity_matrix(Zmod(2^64), 10)

    F.<x> = Zmod(2^64)[]
    G.<x0, x1, x2, x3, x4, x5, x6, x7, x8, x9> = F[]

    v1 = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9]
    v2 = vector(multiply_vector)

    for i in range(10):
        v1 = f(v1, v2)

    coeff = Matrix(Zmod(2^64), 10, 10, [v.coefficients() for v in v1])

    quo = n // 10
    rem = n % 10

    res = M * coeff ^ quo
    vv = []
    for i in res:
        vv.append(vector(initial_state) * i)

    for i in range(rem):
        vv = f(vv, v2)

    return int(vv[-1])

r = remote("synergistic.chal.pwni.ng", 1337)

pow_cmd = r.recvline(keepends=False)
print(pow_cmd)
hashcash = subprocess.check_output(pow_cmd.split(b" ")).decode().rstrip("\n")

print(hashcash)
r.sendline(hashcash)

for i in range(10):
    r.recvuntil("token for ")
    n = int(r.recvline())
    token = generate_token(n)
    print(f"token for {n} = {token}")
    r.sendline(str(token))

print(r.recvall())
