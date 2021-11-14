import struct

def ror(x, b, bit_size=32, mask=0xffffffff):
    return ((x>>b) | (x<<(bit_size-b))) & mask

def major(x, y, z):
    return (x & y) ^ (y & z) ^ (z & x)

def neg(x, mask=0xffffffff):
    return x ^ mask

def choose(x, y, z):
    return (x & y) | (neg(x) & z)

class MerkleDamgard:
    def __init__(self, state):
        self.block_size = 0
        raise NotImplementedError

    def pad(self, payload: bytes):
        padded_payload  = bytes(payload[:])
        padded_payload += b'\x80'
        padded_payload += b'\x00' * ((56 - len(padded_payload)) % self.block_size)
        padded_payload += int.to_bytes(len(payload) * 8, 8, 'big')
        return padded_payload

    def feed(self, data: bytes):
        if len(data) % self.block_size != 0:
            raise Exception(f'The length of data should be a multiple of {self.block_size}')
        for i in range(0, len(data), self.block_size):
            block = data[i:i+self.block_size]
            self._feed(block)

    def _feed(self, block: bytes):
        raise NotImplementedError

    def digest(self):
        raise NotImplementedError

class SHA256(MerkleDamgard):
    def __init__(self, h=bytes.fromhex('6a09e667bb67ae853c6ef372a54ff53a510e527f9b05688c1f83d9ab5be0cd19')):
        self.h = struct.unpack('>IIIIIIII', h)
        self.block_size = 64

    def _feed(self, block: bytes):
        k = [
            0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
            0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
            0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
            0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
            0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
            0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
            0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
            0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
        ]

        # w[0:16]
        w = [int.from_bytes(block[i:i+4], 'big') for i in range(0, 64, 4)]
        # w[16:64]
        for i in range(16, 64):
            s0 = ror(w[i - 15], 7) ^ ror(w[i - 15], 18) ^ (w[i - 15] >> 3)
            s1 = ror(w[i - 2], 17) ^ ror(w[i - 2], 19) ^ (w[i - 2] >> 10)
            w.append((w[i - 16] + s0 + w[i - 7] + s1) & 0xffffffff)

        h = self.h[:]
        for i in range(64):
            s0 = ror(h[0], 2) ^ ror(h[0], 13) ^ ror(h[0], 22)
            t2 = (s0 + major(h[0], h[1], h[2])) & 0xffffffff
            s1 = ror(h[4], 6) ^ ror(h[4], 11) ^ ror(h[4], 25)
            t1 = (h[7] + s1 + choose(h[4], h[5], h[6]) + k[i] + w[i]) & 0xffffffff

            h = [(t1 + t2) & 0xffffffff, h[0], h[1], h[2], (h[3] + t1) & 0xffffffff, h[4], h[5], h[6]]

        self.h = [(self.h[i] + h[i]) & 0xffffffff for i in range(8)]

    def digest(self):
        return b''.join([int.to_bytes(s, 4, 'big') for s in self.h])

if __name__ == '__main__':
    import hashlib

    h = SHA256()

    assert h.pad(b'hello world') == b'hello world' + b'\x80' + b'\x00'*51 + b'\x58'

    h.feed(h.pad(b'hello world'))
    assert h.digest() == hashlib.sha256(b'hello world').digest()
