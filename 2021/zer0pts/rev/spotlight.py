#!/usr/bin/env python
# https://github.com/bozhu/KASUMI-Python/blob/master/kasumi.py
def _bitlen(x):
    assert x >= 0
    return len(bin(x)) - 2


def _shift(x, s):
    assert _bitlen(x) <= 16
    return ((x << s) & 0xFFFF) | (x >> (16 - s))


def _mod(x):
    return ((x - 1) % 8) + 1

S7 = (
     54, 50, 62, 56, 22, 34, 94, 96, 38,  6, 63, 93, 2,  18,123, 33,
     55,113, 39,114, 21, 67, 65, 12, 47, 73, 46, 27, 25,111,124, 81,
     53,  9,121, 79, 52, 60, 58, 48,101,127, 40,120,104, 70, 71, 43,
     20,122, 72, 61, 23,109, 13,100, 77,  1, 16,  7, 82, 10,105, 98,
    117,116, 76, 11, 89,106,  0,125,118, 99, 86, 69, 30, 57,126, 87,
    112, 51, 17,  5, 95, 14, 90, 84, 91,  8, 35,103, 32, 97, 28, 66,
    102, 31, 26, 45, 75,  4, 85, 92, 37, 74, 80, 49, 68, 29,115, 44,
     64,107,108, 24,110, 83, 36, 78, 42, 19, 15, 41, 88,119, 59,  3,
)

S9 = (    
    167,239,161,379,391,334,  9,338, 38,226, 48,358,452,385, 90,397,
    183,253,147,331,415,340, 51,362,306,500,262, 82,216,159,356,177,
    175,241,489, 37,206, 17,  0,333, 44,254,378, 58,143,220, 81,400,
     95,  3,315,245, 54,235,218,405,472,264,172,494,371,290,399, 76,
    165,197,395,121,257,480,423,212,240, 28,462,176,406,507,288,223,
    501,407,249,265, 89,186,221,428,164, 74,440,196,458,421,350,163,
    232,158,134,354, 13,250,491,142,191, 69,193,425,152,227,366,135,
    344,300,276,242,437,320,113,278, 11,243, 87,317, 36, 93,496, 27,
    487,446,482, 41, 68,156,457,131,326,403,339, 20, 39,115,442,124,
    475,384,508, 53,112,170,479,151,126,169, 73,268,279,321,168,364,
    363,292, 46,499,393,327,324, 24,456,267,157,460,488,426,309,229,
    439,506,208,271,349,401,434,236, 16,209,359, 52, 56,120,199,277,
    465,416,252,287,246,  6, 83,305,420,345,153,502, 65, 61,244,282,
    173,222,418, 67,386,368,261,101,476,291,195,430, 49, 79,166,330,
    280,383,373,128,382,408,155,495,367,388,274,107,459,417, 62,454,
    132,225,203,316,234, 14,301, 91,503,286,424,211,347,307,140,374,
     35,103,125,427, 19,214,453,146,498,314,444,230,256,329,198,285,
     50,116, 78,410, 10,205,510,171,231, 45,139,467, 29, 86,505, 32,
     72, 26,342,150,313,490,431,238,411,325,149,473, 40,119,174,355,
    185,233,389, 71,448,273,372, 55,110,178,322, 12,469,392,369,190,
      1,109,375,137,181, 88, 75,308,260,484, 98,272,370,275,412,111,
    336,318,  4,504,492,259,304, 77,337,435, 21,357,303,332,483, 18,
     47, 85, 25,497,474,289,100,269,296,478,270,106, 31,104,433, 84,
    414,486,394, 96, 99,154,511,148,413,361,409,255,162,215,302,201,
    266,351,343,144,441,365,108,298,251, 34,182,509,138,210,335,133,
    311,352,328,141,396,346,123,319,450,281,429,228,443,481, 92,404,
    485,422,248,297, 23,213,130,466, 22,217,283, 70,294,360,419,127,
    312,377,  7,468,194,  2,117,295,463,258,224,447,247,187, 80,398,
    284,353,105,390,299,471,470,184, 57,200,348, 63,204,188, 33,451,
     97, 30,310,219, 94,160,129,493, 64,179,263,102,189,207,114,402,
    438,477,387,122,192, 42,381,  5,145,118,180,449,293,323,136,380,
     43, 66, 60,455,341,445,202,432,  8,237, 15,376,436,464, 59,461,
)


class Kasumi:
    def __init__(self):
        self.key_KL1 = [None] * 9
        self.key_KL2 = [None] * 9
        self.key_KO1 = [None] * 9
        self.key_KO2 = [None] * 9
        self.key_KO3 = [None] * 9
        self.key_KI1 = [None] * 9
        self.key_KI2 = [None] * 9
        self.key_KI3 = [None] * 9


    def set_key(self, master_key):
        tbl = [0xf4ca, 0xe460, 0xe0e8, 0xe640, 0x86a8, 0x8c40, 0x6460, 0x6462, 0xf9df, 0xbecf, 0xbd88, 0xfcb8, 0x4464, 0x21, 0x7b46, 0x3757, 0x460e, 0xe8e, 0x640e, 0x6a88, 0xc408, 0x4606, 0x4626, 0x4caf, 0x2046, 0x3032, 0x3132, 0x657a, 0x3072, 0x7470, 0x2073, 0x5443, 0x646, 0x2646, 0xaf4c, 0xe46, 0x8e0e, 0xe64, 0x886a, 0x8c4, 0xbd88, 0xfcb8, 0x4464, 0x21, 0x7b46, 0x3757, 0xf9df, 0xbecf, 0xbecf, 0xbd88, 0xfcb8, 0x4464, 0x21, 0x7b46, 0x3757, 0xf9df, 0x21, 0x7b46, 0x3757, 0xf9df, 0xbecf, 0xbd88, 0xfcb8, 0x4464]
        assert _bitlen(master_key) <= 128

        key       = [None] * 9
        key_prime = [None] * 9

        master_key_prime = master_key ^ 0x0123456789ABCDEFFEDCBA9876543210
        for i in range(1, 9):
            key[i]       = (master_key       >> (16 * (8 - i))) & 0xFFFF
            key_prime[i] = (master_key_prime >> (16 * (8 - i))) & 0xFFFF

        for i in range(1, 9):
            self.key_KL1[i] =  _shift(key[_mod(i + 0)], 1)
            self.key_KL2[i] =   key_prime[_mod(i + 2)]
            self.key_KO1[i] =  _shift(key[_mod(i + 1)], 5)
            self.key_KO2[i] =  _shift(key[_mod(i + 5)], 8)
            self.key_KO3[i] =  _shift(key[_mod(i + 6)], 13)
            self.key_KI1[i] =   key_prime[_mod(i + 4)]
            self.key_KI2[i] =   key_prime[_mod(i + 3)]
            self.key_KI3[i] =   key_prime[_mod(i + 7)]


    def fun_FI(self, input, round_key):
        # assert _bitlen(input)  <= 16
        
        left  = input >> 7
        right = input & 0b1111111

        round_key_1 = round_key >> 9
        round_key_2 = round_key & 0b111111111

        tmp_l = right
        # assert _bitlen(left)  <= 9
        tmp_r = S9[left] ^ right

        left  = tmp_r ^ round_key_2
        # assert _bitlen(tmp_l) <= 7
        right = S7[tmp_l] ^ (tmp_r & 0b1111111) ^ round_key_1

        tmp_l = right
        # assert _bitlen(left)  <= 9
        tmp_r = S9[left] ^ right

        # assert _bitlen(tmp_l) <= 7
        left  = S7[tmp_l] ^ (tmp_r & 0b1111111)
        right = tmp_r

        # assert _bitlen(left)  <= 7
        # assert _bitlen(right) <= 9
        return (left << 9) | right


    def fun_FO(self, input, round_i):
        # assert _bitlen(input)  <= 32
        # assert round_i >= 1 and round_i <= 8

        in_left  = input >> 16
        in_right = input & 0xFFFF

        out_left  = in_right # this is not Feistel at all, maybe not reversible
        out_right = self.fun_FI(in_left ^ self.key_KO1[round_i], 
                                          self.key_KI1[round_i]) ^ in_right

        in_left   = out_right # use in_* as temp variables
        in_right  = self.fun_FI(out_left ^ self.key_KO2[round_i],
                                           self.key_KI2[round_i]) ^ out_right

        out_left  = in_right
        out_right = self.fun_FI(in_left ^ self.key_KO3[round_i], 
                                          self.key_KI3[round_i]) ^ in_right

        # assert _bitlen(out_left)  <= 16
        # assert _bitlen(out_right) <= 16
        return (out_left << 16) | out_right


    def fun_FL(self, input, round_i):
        # assert _bitlen(input)  <= 32
        # assert round_i >= 1 and round_i <= 8

        in_left  = input >> 16
        in_right = input & 0xFFFF

        out_right = in_right ^ _shift(in_left   & self.key_KL1[round_i], 1)
        out_left  = in_left  ^ _shift(out_right | self.key_KL2[round_i], 1)

        # assert _bitlen(out_left)  <= 16
        # assert _bitlen(out_right) <= 16
        return (out_left << 16) | out_right


    def fun_f(self, input, round_i):
        # assert _bitlen(input)  <= 32
        # assert round_i >= 1 and round_i <= 8

        if round_i % 2 == 1:
            state  = self.fun_FL(input, round_i)
            output = self.fun_FO(state, round_i)
        else:
            state  = self.fun_FO(input, round_i)
            output = self.fun_FL(state, round_i)

        # assert _bitlen(output) <= 32
        return output


    def enc_1r(self, in_left, in_right, round_i):
        # assert _bitlen(in_left)  <= 32
        # assert _bitlen(in_right) <= 32
        # assert round_i >= 1 and round_i <= 8

        out_right = in_left # note this is different from normal Feistel
        out_left  = in_right ^ self.fun_f(in_left, round_i)

        # assert _bitlen(out_left)  <= 32
        # assert _bitlen(out_right) <= 32
        return out_left, out_right


    def dec_1r(self, in_left, in_right, round_i):
        # assert _bitlen(in_left)  <= 32
        # assert _bitlen(in_right) <= 32
        # assert round_i >= 1 and round_i <= 8

        out_left  = in_right
        out_right = self.fun_f(in_right, round_i) ^ in_left

        # assert _bitlen(out_left)  <= 32
        # assert _bitlen(out_right) <= 32
        return out_left, out_right


    def enc(self, plaintext):
        assert _bitlen(plaintext) <= 64
        left  = plaintext >> 32
        right = plaintext & 0xFFFFFFFF
        for i in range(1, 9):
            left, right = self.enc_1r(left, right, i)
        return (left << 32) | right


    def dec(self, ciphertext):
        assert _bitlen(ciphertext) <= 64
        left  = ciphertext >> 32
        right = ciphertext & 0xFFFFFFFF
        for i in range(8, 0, -1):
            left, right = self.dec_1r(left, right, i)
        return (left << 32) | right

def trans(aa):
    a = aa & 0xff 
    b = (aa >> 8) & 0xff 
    c = (aa >> 16) & 0xff 
    d = (aa >> 24) & 0xff 
    e = (aa >> 32) & 0xff 
    f = (aa >> 40) & 0xff 
    g = (aa >> 48) & 0xff 
    h = (aa >> 56) & 0xff 

    return h | (g << 8) | (f << 16) | (e << 24) | (d << 32) | (c << 40) | (b << 48) | (a << 56)


if __name__ == '__main__':
    key     = 0x7a657230707473204354462032303231
    text    = 0x3604084950321c03

    my_kasumi = Kasumi()
    my_kasumi.set_key(key)
    flag = b''

    enc = [0x2DE23334718727BB, 0xB298DE796E944115, 0xE45EF960FBEC841B, 0x314FC3F835E2958E, 0xDC115329AA177509, 0x7CB37E8F516BC981, 0x2D9D9AD4ADAF9925, 0x1808A242A2A693E1]

    x = 0x4c617a7920466f78
    import struct
    for i in enc:
        ans = my_kasumi.dec(trans(i))
        flag += struct.pack("<Q", ans ^ x)[::-1]
        x = trans(i)

    print(flag.rstrip(b'\x00'))
