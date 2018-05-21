def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

mul_list = [0x20656D6F636C6557, 0x2046544352206F74, 0x6548202138313032, 0x2061207369206572, 0x6320455279626142, 0x65676E656C6C6168, 0x756F7920726F6620]
res_list = [0x2B7192452905E8FB, 0x7BA58F82BD898035, 0xA3112746582E1434, 0x163F756FCC221AB0, 0xECC78E6FB9CBA1FE, 0xDCDD8B49EA5D7E14, 0xA2845FE0B3096F8E]
flag = ''

for i in range(len(mul_list)):
    inv = modinv(mul_list[i], 0xFFFFFFFFFFFFFFC5)
    flag += hex(res_list[i] * inv % 0xFFFFFFFFFFFFFFC5)[2:-1].decode('hex')[::-1]

print flag[:-3]
