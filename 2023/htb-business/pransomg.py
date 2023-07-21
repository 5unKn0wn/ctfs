from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
from tqdm import tqdm
import os, random
import natsort

TemperingMaskB = 0x9d2c5680
TemperingMaskC = 0xefc60000

def untemper(y):
    y = undoTemperShiftL(y)
    y = undoTemperShiftT(y)
    y = undoTemperShiftS(y)
    y = undoTemperShiftU(y)
    return y

def undoTemperShiftL(y):
    last14 = y >> 18
    final = y ^ last14
    return final

def undoTemperShiftT(y):
    first17 = y << 15
    final = y ^ (first17 & TemperingMaskC)
    return final

def undoTemperShiftS(y):
    a = y << 7
    b = y ^ (a & TemperingMaskB)
    c = b << 7
    d = y ^ (c & TemperingMaskB)
    e = d << 7
    f = y ^ (e & TemperingMaskB)
    g = f << 7
    h = y ^ (g & TemperingMaskB)
    i = h << 7
    final = y ^ (i & TemperingMaskB)
    return final

def undoTemperShiftU(y):
    a = y >> 11
    b = y ^ a
    c = b >> 11
    final = y ^ c
    return final

def _xor(a, b):
    return b''.join([bytes([a[i] ^ b[i % len(b)]]) for i in range(len(a))])

contents = []
secrets = []

for fname in natsort.natsorted(os.listdir("./enc_files/")):
    with open(f'./enc_files/{fname}', 'rb') as f:
        content = f.read()
        contents.append((fname, content[:-72]))
        secrets.append(content[-72:])

for otp in tqdm(range(0x10000)):
    state = []
    for x in secrets:
        x = _xor(x, long_to_bytes(otp, 2))
        x = bytes_to_long(x)
        for i in range(18):
            state.append(untemper(x & 2**32-1))
            x >>= 32

    state += [0 for _ in range(624 - len(state))]
    state = (3, tuple(state + [0]), None)

    random.setstate(state)

    for i in range(32):
        random.getrandbits(576)

    key = long_to_bytes(random.getrandbits(1680))[:16]
    iv = long_to_bytes(random.getrandbits(1680))[:16]

    cipher = AES.new(key, AES.MODE_CBC, iv)

    try:
        pt = unpad(cipher.decrypt(contents[0][1]), 16)
        pt = unpad(cipher.decrypt(contents[1][1]), 16)
        pt = unpad(cipher.decrypt(contents[2][1]), 16)
    except ValueError:
        continue

    print(f"key: {key}")
    print(f"iv: {iv}")

    cipher = AES.new(key, AES.MODE_CBC, iv)

    os.makedirs(f'./dec_files', exist_ok=True)
    for fname, content in contents:
        with open(f'./dec_files/{fname}', 'wb') as f:
            f.write(cipher.decrypt(content))

    break
