from pwn import *

def legendre(a, p):
    return pow(a, (p - 1) // 2, p)

while True:
    r = remote("crypto.ctf.zer0pts.com", 10463)

    r.recvuntil("Here is g: ")
    g = int(r.recvuntil(", ", drop=True))
    r.recvuntil("and p: ")
    p = int(r.recvuntil("\n", drop=True))

    r.recvuntil(", ")
    c2 = int(r.recvuntil(")\n", drop=True))
    r.sendlineafter("your hand(1-3): ", "3")
    r.recvuntil("Your hand is ...")
    r.recvuntil("\n")
    res = r.recvuntil("\n")

    if b"Yo! You win!!! Ho!" not in res:
        r.close()
        continue

    print("Win")
    r.recvuntil("\n")
    legen_1 = legendre(c2, p)
    legen_2 = legendre(c2 * 2, p)
    legen_3 = legendre(c2 * 3, p)

    if legen_1 == 1 and legen_2 == p - 1 and legen_3 == p - 1:
        print("Found what I want 1")
        target = 1
        matched = 3
        notmatched = 2
        break
    elif legen_1 == p - 1 and legen_2 == 1 and legen_3 == p - 1:
        print("Found what I want 2")
        target = 1
        matched = 1
        notmatched = 3
        break
    elif legen_1 == p - 1 and legen_2 == p - 1 and legen_3 == 1:
        print("Found what I want 3")
        target = 1
        matched = 2
        notmatched = 1
        break
    elif legen_1 == p - 1 and legen_2 == 1 and legen_3 == 1:
        print("Found what I want 4")
        target = p - 1
        matched = 3
        notmatched = 2
        break
    elif legen_1 == 1 and legen_2 == p - 1 and legen_3 == 1:
        print("Found what I want 5")
        target = p - 1
        matched = 1
        notmatched = 3
        break
    elif legen_1 == 1 and legen_2 == 1 and legen_3 == p - 1:
        print("Found what I want 6")
        target = p - 1
        matched = 2
        notmatched = 1
        break

win = 1
while True:
    r.recvuntil(", ")
    c2 = int(r.recvuntil(")\n", drop=True))
    if legendre(c2, p) == target:
        r.sendlineafter("your hand(1-3): ", str(matched))
    else:
        r.sendlineafter("your hand(1-3): ", str(notmatched))
    r.recvuntil("Your hand is ...")
    r.recvuntil("\n")
    if b"Yo! You win!!! Ho!" in r.recvuntil("\n"):
        win += 1
        print(win)
    if win == 100:
        break

r.interactive()
