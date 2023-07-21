from Crypto.Util.number import long_to_bytes, bytes_to_long
from hashlib import sha256
from sage.all import *
from pwn import *

e = 0x10001
greet_pow = bytes_to_long(b'Hey!') ** e
ans_pow = bytes_to_long(b'Bye!') ** e

while True:
    r = remote("83.136.251.112", 50168, level='error')

    r.recvuntil("We say : ")
    greet_ct = int(r.recvline(keepends=False), 16)

    ans_cts = set()
    while len(ans_cts) != 3:
        r.sendlineafter("> ", "S")
        r.sendlineafter("say : ", hex(greet_ct))
        r.recvuntil("Nice! We say : ")
        ans_cts.add(int(r.recvline(keepends=False), 16))

    n_candidates = []
    for i in range(3):
        n_candidates.append(gcd(greet_pow - greet_ct, ans_pow - ans_cts.pop()))

    n_candidates = list(filter(lambda x: x.bit_length() >= 2048, n_candidates))
    if len(n_candidates) == 0:
        print("No luck..")
        r.close()
        continue

    assert len(n_candidates) == 1
    N = n_candidates[0]

    primes = primes_first_n(10000)
    for p in primes:
        if N % p == 0:
            N //= p

    assert N.bit_length() == 2048
    print(f"N: {N}")

    r.sendlineafter("> ", "F")
    h = sha256(str(N).encode()).hexdigest()
    r.sendlineafter("public key : ", h)
    r.recvuntil("token : ")
    partial_q = int(r.recvline(keepends=False))
    print(f"partial_q: {partial_q}")

    partial_q = (partial_q >> 381) << 381

    F = PolynomialRing(Zmod(N), 'x', implementation='NTL')
    x = F.gen()
    pol = x + partial_q
    roots = pol.small_roots(beta=0.5)
    print(roots)
    assert len(roots) == 1

    q = int(partial_q + roots[0])
    p = N // q
    assert N == p * q

    print(f"p: {p}")
    print(f"q: {q}")

    phiN = (p - 1) * (q - 1)
    symmetric_key = long_to_bytes(pow(0x1337, pow(0xdeadbeef, N, phiN), N))[:16]
    print(f"symmetric_key: {symmetric_key}")
    r.sendlineafter("> ", "R")
    r.sendlineafter("key : ", symmetric_key.hex())
    r.interactive()
    break
