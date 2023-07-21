from Crypto.Util.number import bytes_to_long, long_to_bytes
from pwn import *
import json

def find_collision(l, r, n):
    q = 26189572440233739420990528170531051459310363621928135990243626537967

    M = Matrix(ZZ, n + 2, n + 2)
    offset = 65

    target = bytes_to_long(l + bytes(n) + r)
    target %= q

    for i in range(n):
        M[i, i] = 1
        M[i, n] = pow(256, i + len(r), q)

    for i in range(n):
        M[n, i] = -offset

    M[n, n] = target
    M[n, n + 1] = 1
    M[n+1,n] = q

    L = M.LLL()
    for i in L:
        if i[-2] == 0 and i[-1] == 1:
            _sum = target
            for j in range(n):
                _sum += (i[j] + offset) * pow(256, (j + len(r)), q)
            _sum %= q
            assert _sum == 0

            x = list(i)[-3::-1]
            for j in range(len(x)):
                x[j] += offset
            res = l + bytes(x) + r
            print(res)
            assert bytes_to_long(res) % q == 0

            return bytes(x).decode()

username = find_collision(b'{"username": "', b'", "admin": false}', 300)
x = find_collision(b'{"admin":"', b'"}', 70)

r = remote("94.237.52.136", 58847)

r.sendlineafter("> ", "1")
r.sendlineafter("> ", username)

sig = json.loads(r.recvline())

r.sendlineafter("> ", "2")
r.sendlineafter("> ", str(sig['r']))
r.sendlineafter("> ", str(sig['s']))
r.sendlineafter("> ", f'{{"admin":"{x}"}}')

r.interactive()
