r, s, k, h = (0x92acb929727872bc1c7a5f69c1c3c97ae1c333e2, 0xe060459440ebc11a7cd811a66a341f095f5909e5, 0xef2b0000, 0x68e548ef4984f6e7d05cbcea4fc7c83393806bbf)
 
# secp160r1
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF7FFFFFFF
a = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF7FFFFFFC
b = 0x1C97BEFC54BD7A8B65ACF89F81D4D4ADC565FA45
g = (0x4A96B5688EF573284664698968C38BB913CBFC82, 0x23A628553168947D59DCC912042351377AC5FB32)
 
E = EllipticCurve(Zmod(p), [a, b])
order = E.order()
G = E(g)
 
for i in range(0x10000):
    _k = k + i
    if (G * _k).xy()[0] == r:
        k = _k
        print(f"Found k: {hex(k)}")
        break
 
x = (s * k - h) * inverse_mod(r, order) % order
print(f"LINECTF{{{format(x, 'x').zfill(40)}}}")
