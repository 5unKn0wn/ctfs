def reverse_bit(c):
    r = 0
    for i in range(8):
        r = (r << 1) | (c & 1)
        c >>= 1
    return r

def dec1(s):
    l = len(s)
    r = []
    for i in range(l / 2):
        r.append(reverse_bit(s[i * 2 + 1]))
        r.append(reverse_bit(s[i * 2]))
    return r

def dec2(s):
    l = len(s)
    r = []
    for i in range(l / 4):
        r.append((s[i * 4 + 1] << 4 & 0xff) | (s[i * 4 + 1] >> 4))
        r.append(s[i * 4 + 2])
        r.append(s[i * 4])
        r.append((s[i * 4 + 3] << 4 & 0xff) | (s[i * 4 + 3] >> 4))
    return r

def dec3(s):
    l = len(s)
    r = []
    for i in range(l / 5):
        r.append((s[i * 5 + 4] << 3 & 0xff) | (s[i * 5 + 4] >> 5))
        r.append(s[i * 5 + 2])
        r.append(s[i * 5] ^ (~s[i * 5 + 3] & 0xff))
        r.append(~s[i * 5 + 3] & 0xff)
        r.append(s[i * 5 + 1])
    return r

def dec4(s):
    r = []
    l = len(s)
    for i in range(l / 10):
        r += s[i * 10 + 5:i * 10 + 10]
        r += s[i * 10:i * 10 + 5][::-1]
    return r

def dec5(s):
    r = []
    r.append(s[0xb])
    r.append(reverse_bit(s[0x10]))
    r.append(reverse_bit(s[0xf]))
    r.append(s[0xe])
    r.append(reverse_bit(s[0x13]))
    r.append((s[0x5] >> 6) | (s[0x5] << 2 & 0xff))
    r.append(s[0xc])
    r.append(s[0x3] ^ s[0xd])
    r.append(s[0x2] ^ s[0xc])
    r.append(s[0xd])
    r.append(s[0xa])
    r.append((s[0x7] >> 6) | (s[0x7] << 2 & 0xff))
    r.append(reverse_bit(s[0x12]))
    r.append(reverse_bit(s[0x11]))
    r.append((s[0x8] >> 6) | (s[0x8] << 2 & 0xff))
    r.append((s[0x6] >> 6) | (s[0x6] << 2 & 0xff))
    r.append(s[0x1] ^ s[0xb])
    r.append(s[0x0] ^ s[0xa])
    r.append((s[0x9] >> 6) | (s[0x9] << 2 & 0xff))
    r.append(s[0x4] ^ s[0xe])
    return r

def unpack(s):
    s = dec5(s)
    s = dec4(s)
    s = dec3(s)
    s = dec2(s)
    s = dec1(s)
    return s

enc = [0x33, 0x34, 0x56, 0xe6, 0xb5, 0x6c, 0x4d, 0x6e, 0xf3, 0x16, 0x5d, 0x44, 0x8a, 0x41, 0xea, 0x45, 0xa0, 0x16, 0x49, 0xab, 0x74, 0xc5, 0xbd, 0xbc, 0xcc, 0xb2, 0xd5, 0x61, 0xe6, 0x36, 0x5d, 0x5d, 0x26, 0x1b, 0x87, 0xe, 0x9e, 0xb1, 0x64, 0x94, 0xea, 0xb6]
flag = unpack(enc[:20]) + unpack(enc[20:40]) + dec1(enc[40:])

print ''.join(chr(i ^ len(enc)) for i in flag)