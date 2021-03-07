from z3 import *
import struct

a = """ 0104: 0x15 0x25 0x00 0xf5ffc1f6  if (A == 4127179254) goto 0142
 0105: 0x15 0x14 0x00 0x7344aeee  if (A == 1933881070) goto 0126
 0106: 0x15 0x1f 0x00 0xfda6effe  if (A == 4255576062) goto 0138
 0107: 0x15 0x0a 0x00 0x638f7ca2  if (A == 1670347938) goto 0118
 0108: 0x15 0x0f 0x00 0xa2285400  if (A == 2720551936) goto 0124
 0109: 0x15 0x1a 0x00 0x8990fefe  if (A == 2307981054) goto 0136
 0110: 0x15 0x1d 0x00 0x9f576dd4  if (A == 2673307092) goto 0140
 0111: 0x15 0x0a 0x00 0xf6b9ebe2  if (A == 4139379682) goto 0122
 0112: 0x15 0x0f 0x00 0xf9e28bee  if (A == 4192373742) goto 0128
 0113: 0x15 0x14 0x00 0x1f9b8fb4  if (A == 530288564) goto 0134
 0114: 0x15 0x1d 0x00 0xefec86de  if (A == 4025255646) goto 0144
 0115: 0x15 0x0e 0x00 0xdf60093a  if (A == 3747612986) goto 0130
 0116: 0x15 0x03 0x00 0xb8af3fbe  if (A == 3098492862) goto 0120
 0117: 0x15 0x0e 0x00 0x7f01bbcc  if (A == 2130820044) goto 0132
 0118: 0x60 0x00 0x00 0x00000009  A = mem[9]
 0119: 0x15 0x32 0x54 0xf1cf5c2e  if (A == 4056898606) goto 0170 else goto 0204
 0120: 0x60 0x00 0x00 0x00000009  A = mem[9]
 0121: 0x15 0x20 0x52 0xb6af7dbe  if (A == 3064954302) goto 0154 else goto 0204
 0122: 0x60 0x00 0x00 0x00000009  A = mem[9]
 0123: 0x15 0x18 0x50 0xd6b9bde2  if (A == 3602496994) goto 0148 else goto 0204
 0124: 0x60 0x00 0x00 0x00000009  A = mem[9]
 0125: 0x15 0x22 0x4e 0x60fad508  if (A == 1627051272) goto 0160 else goto 0204
 0126: 0x60 0x00 0x00 0x00000009  A = mem[9]
 0127: 0x15 0x22 0x4c 0x77600ede  if (A == 2002783966) goto 0162 else goto 0204
 0128: 0x60 0x00 0x00 0x00000009  A = mem[9]
 0129: 0x15 0x1c 0x4a 0xf3b68ece  if (A == 4088827598) goto 0158 else goto 0204
 0130: 0x60 0x00 0x00 0x00000009  A = mem[9]
 0131: 0x15 0x24 0x48 0x4fe90926  if (A == 1340672294) goto 0168 else goto 0204
 0132: 0x60 0x00 0x00 0x00000009  A = mem[9]
 0133: 0x15 0x0c 0x46 0x7e1933ac  if (A == 2115580844) goto 0146 else goto 0204
 0134: 0x60 0x00 0x00 0x00000009  A = mem[9]
 0135: 0x15 0x24 0x44 0x1f9b8fb4  if (A == 530288564) goto 0172 else goto 0204
 0136: 0x60 0x00 0x00 0x00000009  A = mem[9]
 0137: 0x15 0x1c 0x42 0xcb94e7da  if (A == 3415533530) goto 0166 else goto 0204
 0138: 0x60 0x00 0x00 0x00000009  A = mem[9]
 0139: 0x15 0x0a 0x40 0xb9c2adfe  if (A == 3116543486) goto 0150 else goto 0204
 0140: 0x60 0x00 0x00 0x00000009  A = mem[9]
 0141: 0x15 0x0e 0x3e 0x0f01b94c  if (A == 251771212) goto 0156 else goto 0204
 0142: 0x60 0x00 0x00 0x00000009  A = mem[9]
 0143: 0x15 0x14 0x3c 0xf5efe5f6  if (A == 4126139894) goto 0164 else goto 0204
 0144: 0x60 0x00 0x00 0x00000009  A = mem[9]
 0145: 0x15 0x06 0x3a 0xa7ad8d4e  if (A == 2813168974) goto 0152 else goto 0204
 0146: 0x60 0x00 0x00 0x0000000a  A = mem[10]
 0147: 0x15 0x2e 0x38 0x7efd33a4  if (A == 2130523044) goto 0194 else goto 0204
 0148: 0x60 0x00 0x00 0x0000000a  A = mem[10]
 0149: 0x15 0x24 0x36 0xd6f33dda  if (A == 3606265306) goto 0186 else goto 0204
 0150: 0x60 0x00 0x00 0x0000000a  A = mem[10]
 0151: 0x15 0x26 0x34 0xbbdaa5e6  if (A == 3151668710) goto 0190 else goto 0204
 0152: 0x60 0x00 0x00 0x0000000a  A = mem[10]
 0153: 0x15 0x22 0x32 0x24a7ad2e  if (A == 614968622) goto 0188 else goto 0204
 0154: 0x60 0x00 0x00 0x0000000a  A = mem[10]
 0155: 0x15 0x2a 0x30 0xb7fdfcbe  if (A == 3086875838) goto 0198 else goto 0204
 0156: 0x60 0x00 0x00 0x0000000a  A = mem[10]
 0157: 0x15 0x10 0x2e 0x0f01b94c  if (A == 251771212) goto 0174 else goto 0204
 0158: 0x60 0x00 0x00 0x0000000a  A = mem[10]
 0159: 0x15 0x12 0x2c 0xb3bdaed6  if (A == 3015552726) goto 0178 else goto 0204
 0160: 0x60 0x00 0x00 0x0000000a  A = mem[10]
 0161: 0x15 0x22 0x2a 0x60ffd7bc  if (A == 1627379644) goto 0196 else goto 0204
 0162: 0x60 0x00 0x00 0x0000000a  A = mem[10]
 0163: 0x15 0x0c 0x28 0x5f785fd2  if (A == 1601724370) goto 0176 else goto 0204
 0164: 0x60 0x00 0x00 0x0000000a  A = mem[10]
 0165: 0x15 0x12 0x26 0x27aeff3e  if (A == 665780030) goto 0184 else goto 0204
 0166: 0x60 0x00 0x00 0x0000000a  A = mem[10]
 0167: 0x15 0x0e 0x24 0xc39dc1ca  if (A == 3281895882) goto 0182 else goto 0204
 0168: 0x60 0x00 0x00 0x0000000a  A = mem[10]
 0169: 0x15 0x1e 0x22 0x4d8f1f86  if (A == 1301225350) goto 0200 else goto 0204
 0170: 0x60 0x00 0x00 0x0000000a  A = mem[10]
 0171: 0x15 0x14 0x20 0x99ff4c6e  if (A == 2583645294) goto 0192 else goto 0204
 0172: 0x60 0x00 0x00 0x0000000a  A = mem[10]
 0173: 0x15 0x06 0x1e 0xe97d7d54  if (A == 3917315412) goto 0180 else goto 0204
 0174: 0x60 0x00 0x00 0x0000000b  A = mem[11]
 0175: 0x15 0x1b 0x1c 0x9f576dd4  if (A == 2673307092) goto 0203 else goto 0204
 0176: 0x60 0x00 0x00 0x0000000b  A = mem[11]
 0177: 0x15 0x19 0x1a 0x5b5cffe2  if (A == 1532821474) goto 0203 else goto 0204
 0178: 0x60 0x00 0x00 0x0000000b  A = mem[11]
 0179: 0x15 0x17 0x18 0xb9e9abf6  if (A == 3119098870) goto 0203 else goto 0204
 0180: 0x60 0x00 0x00 0x0000000b  A = mem[11]
 0181: 0x15 0x15 0x16 0xe97d7d54  if (A == 3917315412) goto 0203 else goto 0204
 0182: 0x60 0x00 0x00 0x0000000b  A = mem[11]
 0183: 0x15 0x13 0x14 0x8199d8ee  if (A == 2174343406) goto 0203 else goto 0204
 0184: 0x60 0x00 0x00 0x0000000b  A = mem[11]
 0185: 0x15 0x11 0x12 0x27bedb3e  if (A == 666819390) goto 0203 else goto 0204
 0186: 0x60 0x00 0x00 0x0000000b  A = mem[11]
 0187: 0x15 0x0f 0x10 0xf6f36bda  if (A == 4143147994) goto 0203 else goto 0204
 0188: 0x60 0x00 0x00 0x0000000b  A = mem[11]
 0189: 0x15 0x0d 0x0e 0x6ce6a6be  if (A == 1827055294) goto 0203 else goto 0204
 0190: 0x60 0x00 0x00 0x0000000b  A = mem[11]
 0191: 0x15 0x0b 0x0c 0xffbee7e6  if (A == 4290701286) goto 0203 else goto 0204
 0192: 0x60 0x00 0x00 0x0000000b  A = mem[11]
 0193: 0x15 0x09 0x0a 0x0bbf6ce2  if (A == 197094626) goto 0203 else goto 0204
 0194: 0x60 0x00 0x00 0x0000000b  A = mem[11]
 0195: 0x15 0x07 0x08 0x7fe5bbc4  if (A == 2145762244) goto 0203 else goto 0204
 0196: 0x60 0x00 0x00 0x0000000b  A = mem[11]
 0197: 0x15 0x05 0x06 0xa22d56b4  if (A == 2720880308) goto 0203 else goto 0204
 0198: 0x60 0x00 0x00 0x0000000b  A = mem[11]
 0199: 0x15 0x03 0x04 0xb9fdbebe  if (A == 3120414398) goto 0203 else goto 0204
 0200: 0x60 0x00 0x00 0x0000000b  A = mem[11]
 0201: 0x15 0x01 0x02 0xdd061f9a  if (A == 3708166042) goto 0203 else goto 0204""".split("\n")

anses = [[] for j in range(14)]

def find_addr(s):
    for aa in a:
        if s in aa:
            return aa

for i in range(14):
    goto = "01" + str(i + 4).zfill(2)
    for j in range(4):
        s = find_addr(goto)
        cmp_val = s.split("== ")[1].split(")")[0]
        goto = str(int(s.split("goto ")[1].split(' ')[0]) + 1).zfill(4)

        anses[i].append(int(cmp_val))

flag = b''
cmp_idx = [2, 7, 5, 1, 12, 3, 8, 10, 11, 0, 6]  # found by hand
cnt = len(cmp_idx)
z = [BitVec("flag_%d" % j, 32) for j in range(14)]
s = Solver()
s.add(z[0] == 0x3072657a)
s.add(z[1] == 0x7b737470)
for i in range(cnt):
    args = [z[i], z[(i + 1) % 14], z[(i + 2) % 14], z[(i + 3) % 14]]
    mem = [0 for j in range(12)]
    if i != cnt - 1:
        s.add(Extract(7, 0,args[0]) < 0x7f, Extract(7, 0,args[0]) >= 0x20)
        s.add(Extract(15, 8,args[0]) < 0x7f, Extract(15, 8,args[0]) >= 0x20)
        s.add(Extract(23, 16,args[0]) < 0x7f, Extract(23, 16,args[0]) >= 0x20)
        s.add(Extract(31, 24,args[0]) < 0x7f, Extract(31, 24,args[0]) >= 0x20)
        s.add(Extract(7, 0,args[1]) < 0x7f, Extract(7, 0,args[1]) >= 0x20)
        s.add(Extract(15, 8,args[1]) < 0x7f, Extract(15, 8,args[1]) >= 0x20)
        s.add(Extract(23, 16,args[1]) < 0x7f, Extract(23, 16,args[1]) >= 0x20)
        s.add(Extract(31, 24,args[1]) < 0x7f, Extract(31, 24,args[1]) >= 0x20)
        s.add(Extract(7, 0,args[2]) < 0x7f, Extract(7, 0,args[2]) >= 0x20)
        s.add(Extract(15, 8,args[2]) < 0x7f, Extract(15, 8,args[2]) >= 0x20)
        s.add(Extract(23, 16,args[2]) < 0x7f, Extract(23, 16,args[2]) >= 0x20)
        s.add(Extract(31, 24,args[2]) < 0x7f, Extract(31, 24,args[2]) >= 0x20)
        s.add(Extract(7, 0,args[3]) < 0x7f, Extract(7, 0,args[3]) >= 0x20)
        s.add(Extract(15, 8,args[3]) < 0x7f, Extract(15, 8,args[3]) >= 0x20)
        s.add(Extract(23, 16,args[3]) < 0x7f, Extract(23, 16,args[3]) >= 0x20)
        s.add(Extract(31, 24,args[3]) < 0x7f, Extract(31, 24,args[3]) >= 0x20)
    A = args[0]
    mem[0] = A
    A = args[1]
    X = mem[0]
    A ^= X
    mem[1] = A
    A = args[2]
    X = mem[1]
    A ^= X
    mem[2] = A
    A = args[3]
    X = mem[2]
    A ^= X
    mem[3] = A
    A = mem[0]
    X = mem[1]
    A += X
    X = mem[2]
    A += X
    X = mem[3]
    A += X
    mem[4] = A
    A = mem[0]
    X = mem[1]
    A -= X
    X = mem[2]
    A += X
    X = mem[3]
    A -= X
    mem[5] = A
    A = mem[0]
    X = mem[1]
    A += X
    X = mem[2]
    A -= X
    X = mem[3]
    A -= X
    mem[6] = A
    A = mem[0]
    X = mem[1]
    A -= X
    X = mem[2]
    A -= X
    X = mem[3]
    A += X
    mem[7] = A
    A = mem[4]
    X = mem[5]
    A |= X
    mem[8] = A
    A = mem[6]
    X = mem[7]
    A &= X
    X = mem[8]
    A ^= X
    mem[8] = A
    A = mem[5]
    X = mem[6]
    A |= X
    mem[9] = A
    A = mem[7]
    X = mem[4]
    A &= X
    X = mem[9]
    A ^= X
    mem[9] = A
    A = mem[6]
    X = mem[7]
    A |= X
    mem[10] = A
    A = mem[4]
    X = mem[5]
    A &= X
    X = mem[10]
    A ^= X
    mem[10] = A
    A = mem[7]
    X = mem[4]
    A |= X
    mem[11] = A
    A = mem[5]
    X = mem[6]
    A &= X
    X = mem[11]
    A ^= X
    mem[11] = A
    A = mem[8]

    s.add(A == anses[(cmp_idx[i])][0])
    s.add(mem[9] == anses[(cmp_idx[i])][1])
    s.add(mem[10] == anses[(cmp_idx[i])][2])
    s.add(mem[11] == anses[(cmp_idx[i])][3])

s.check()
m = s.model()
arr = []
cond = True
for j in range(3 + cnt):
    arr.append(z[j])
    cond = And(cond, z[j] != m[z[j]].as_long())
    flag += struct.pack("<L", m[z[j]].as_long())
    s.add(cond)
print(flag)
