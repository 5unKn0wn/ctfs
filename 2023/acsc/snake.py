from pwn import *
import time
import hashlib

class modified_mt19937_64(object):
    def __init__(self):
        self.mt = [0]*312
        self.mti = 313

    def seed(self, seed):
        self.mt[0] = seed & 0xffffffffffffffff
        for i in range(1,312):
            self.mt[i] = (i - 0x778621272013F537 * (self.mt[i-1] ^ (self.mt[i-1] >> 62))) & 0xffffffffffffffff
        self.mti = 312

    def int64(self):
        if self.mti >= 312:
            if self.mti == 313:
                self.seed(5489)

            for k in range(311):
                y = (self.mt[k] & 0xFFFFFFFF80000000) | (self.mt[k+1] & 0x7fffffff)
                if k < 312 - 156:
                    self.mt[k] = self.mt[k+156] ^ (y >> 1) ^ (0xB5026F5AA96619E9 if y & 1 else 0)
                else:
                    self.mt[k] = self.mt[k+156-624] ^ (y >> 1) ^ (0xB5026F5AA96619E9 if y & 1 else 0)

            y = (self.mt[311] & 0xFFFFFFFF80000000) | (self.mt[0] & 0x7fffffff)
            self.mt[311] = self.mt[155] ^ (y >> 1) ^ (0xB5026F5AA96619E9 if y & 1 else 0)
            self.mti = 0

        y = self.mt[self.mti]
        self.mti += 1

        y ^= (y >> 26) & 0xBBBBBBBBBBBBBBBB
        y ^= (y << 19) & 0xA82C9FFFEDA60000
        y ^= (y << 37) & 0xFFFABCD000000000
        y ^= (y >> 45)

        return y

width = 0xd1
height = 0x34

t = int(time.time())
mt = modified_mt19937_64()
mt.seed(t)

md5 = hashlib.md5()

md5.update(p32(t))

score = 31338
for i in range(score):
    x = mt.int64() % (width // 2)
    y = mt.int64() % height

    md5.update(p32(x) + p32(y))

child_code = open("snake_childmem.bin", "rb").read()
md5.update(child_code)
md5_hash = md5.digest()

packet = p32(t) + p32(width) + p32(height) + p32(score) + md5_hash
print(packet)

r = remote("snake.chal.ctf.acsc.asia", 4444)

r.send(packet)

r.interactive()
