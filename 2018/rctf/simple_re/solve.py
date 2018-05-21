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

mul_list = [0x556E4969, 0x2E775361, 0x893DAE7, 0x96990423, 0x6CF9D3E9, 0xA505531F]
res_list = [0x54A0B9BD, 0x4B818640, 0x8EB63387, 0xA9EABEFD, 0xB8CDF96B, 0x113C3052]
flag = ''

for i in range(len(mul_list)):
	flag += hex(modinv(mul_list[i], 0x100000000) * res_list[i] & 0xffffffff)[2:].replace('L', '').decode('hex')[::-1]

print "RCTF{" + flag + "echn!qu3s}"	# just guess... :p
