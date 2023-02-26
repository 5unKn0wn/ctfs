def poly2int(p):
    return Integer((Integer(p.integer_representation()).bits() + ([0] * 32))[:32][::-1], 2)

F.<x> = GF(2^32, modulus=GF(2^33).fetch_int((2^32) + 0xc0000401))
v = F.fetch_int(0xf2694bc)
c = list(b'\x01\x19\xefZ\xfa\xc8.i1\xd7\x81!')

count = 1
for i in range(12):
    v = v * F.fetch_int(2)^count
    print(chr(c[i] ^^ poly2int(v) & 0xff), end='')
    count *= 42
