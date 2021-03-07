import struct

output_from_flag_first = """5aaf63e5c1f262bf
a967ff06da3b455c
ee8d95ecc2ae3151
20804abbaeac4ae3
f01c8c72aa0b3739""".split("\n")

output_from_flag = """3b9d8f4c92f4f0d0
90001647bc8a675c
835c980e129e538e
394bfa98b73bffdf
7876cbb1a44c996a
a774dad1600b3e58
d37047de18e38357
ddd981d4f33bcbea
bc139d43d82491cb
99a5cc916ab543b8
5c5620c4ba3de3f0
d40ab2894a2489cf
d5b8807c7f47c3a6
058b8381f79aff17
d9902bdc2e6a3e6a
1f569bbabf0fdf66
5e447290badcde7b
4b9c020bd47e0def
d165a57131d62406
036ed392a229447d
e9dbbe77a59fefd4
394496b6ea1e625e
45fb008d74552738
a221578e8dd49f21
e6eaf6d9107169e7
891c57041c1baf12
870dd78a4e2c9411
30e0f41d8fd96653
037dfaab96abea25
1488ecf994d2047d
4d69bfe642d4c35a
f5e72ef86576f024
e55767e6301bdebd
55dc33ac167d4985
d10186dc89be859a
2bd5f106f6a52cc5
89a759a718d94cc5
dacd0d9efc7c61b2
cc0a041031e50277
0c410476911f48ea
cf8f1cc5cf2b8ac7
c3ab424687092a0b
edd67d3016e3df56
684d11d8e5776759
8606ab4a52871ac7
5ba67fd82bf558f8
dc7a01a35e492e77
5b22150dc59f14dc
b6cf77280d0e34cc
973455e6b5a8586c
3ad544be84569692
1bd3c6b8a4011119
7be81be8a69ccbba
08a0ed17999b7bcf
4d2bc86ab7f81e2e
f8a5682e0c3aeb32
999ee9486f7168ab
b8509f9a19b4834b
2d675a714f1dab33
0dfc906f054428cb
65bd9b6dc1017ef6
c2112f5596386429
1ebb9ce12865cbb0
8e97775bf89ac543
9946a12cea92f07c
b791ea2007b2851c
3cd9815806928e3a
271f7b82da378518
8f16acd5c3a7cb83
3e2b49ec7aaf7abc""".split("\n")

output_from_mine = """3b9d8f4c92f4f0d4
90001647bc8a674e
835c980e129e53b0
394bfa98b73bfff7
7876cbb1a44c997f
a774dad1600b3e4a
d37047de18e38369
ddd981d4f33bcbe3
bc139d43d82491de
99a5cc916ab543ad
5c5620c4ba3de3e1
d40ab2894a2489dd
d5b8807c7f47c3fd
058b8381f79aff59
d9902bdc2e6a3e24
1f569bbabf0fdf70
5e447290badcde6d
4b9c020bd47e0df9
d165a57131d62449
036ed392a2294474
e9dbbe77a59fefdc
394496b6ea1e624b
45fb008d74552738
a221578e8dd49f23
e6eaf6d9107169ee
891c57041c1baf1a
870dd78a4e2c945e
30e0f41d8fd96651
037dfaab96abea2b
1488ecf994d20471
4d69bfe642d4c314
f5e72ef86576f037
e55767e6301bdeb8
55dc33ac167d49cb
d10186dc89be8582
2bd5f106f6a52cd6
89a759a718d94cc8
dacd0d9efc7c61fc
cc0a041031e50275
0c410476911f48f9
cf8f1cc5cf2b8adf
c3ab424687092a1a
edd67d3016e3df43
684d11d8e5776757
8606ab4a52871a89
5ba67fd82bf558f4
dc7a01a35e492e63
5b22150dc59f14da
b6cf77280d0e34c4
973455e6b5a85822
3ad544be8456969e
1bd3c6b8a401110d
7be81be8a69ccbbc
08a0ed17999b7bc7
4d2bc86ab7f81e10
f8a5682e0c3aeb20
999ee9486f7168ba
b8509f9a19b4834f
2d675a714f1dab7c
0dfc906f054428da
65bd9b6dc1017ef3
c2112f559638642e
1ebb9ce12865cbac
8e97775bf89ac57e
9946a12cea92f035
b791ea2007b28523
3cd9815806928e34
271f7b82da378527
8f16acd5c3a7cbcb
3e2b49ec7aaf7aee""".split("\n")

flag = b''

for i in range(2):
    flag += struct.pack("<Q", int(output_from_flag_first[i], 16) ^ int(output_from_flag_first[i + 3], 16))

for i in range(len(output_from_flag)):
    flag += chr((int(output_from_flag[i], 16) ^ int(output_from_mine[i], 16) ^ 0x61) & 0xff).encode()

print(flag)
